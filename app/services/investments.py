from datetime import datetime
from typing import Any, Tuple

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import Base


def close_project_or_donation(objects: Tuple[Any, Base]) -> None:
    for object in objects:
        if object.full_amount == object.invested_amount:
            object.fully_invested = True
            object.close_date = datetime.now()


async def process_investments(
        from_obj_invest: Base,
        in_obj_invest: Base,
        session: AsyncSession
):
    all_investments = await in_obj_invest.get_uninvested_projects(session)
    for investment in all_investments:
        need_for_invest = (
            from_obj_invest.full_amount - from_obj_invest.invested_amount
        )
        free_for_invest = investment.full_amount - investment.invested_amount
        append_obj = min(need_for_invest, free_for_invest)
        investment.invested_amount += append_obj
        from_obj_invest.invested_amount += append_obj
        close_project_or_donation((investment, from_obj_invest))
    session.add_all((*all_investments, from_obj_invest))
    await session.commit()
    await session.refresh(from_obj_invest)
    return from_obj_invest
