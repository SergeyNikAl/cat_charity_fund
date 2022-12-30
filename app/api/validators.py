from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models import CharityProject

PROJECT_ALREADY_EXISTS_MESSAGE = 'Проект с таким именем уже существует!'
PROJECT_NOT_FOUND_MESSAGE = 'Проект не найден!'
CLOSED_PROJECT_UNEDITABLE_MESSAGE = 'Закрытый проект нельзя редактировать!'
AMOUNT_LESS_THEN_DEPOSIT_MESSAGE = (
    'Нельзя установить требуемую сумму меньше внесённой в проект!'
)
FORBIDDEN_DELETE_PROJECT_WITH_MONEY = (
    'В проект были внесены средства, не подлежит удалению!'
)


async def check_name_duplicate(
    project_name: str,
    session: AsyncSession
) -> None:
    project_id = await charity_project_crud.get_project_id_by_name(
        project_name,
        session
    )
    if project_id is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=PROJECT_ALREADY_EXISTS_MESSAGE,
        )


async def check_charity_project_before_edit(
    project_id: int,
    session: AsyncSession,
    full_amount: int = None,
    delete: bool = False
) -> CharityProject:
    project = await charity_project_crud.get(project_id, session)
    if not project:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=PROJECT_NOT_FOUND_MESSAGE
        )
    if project.fully_invested and not delete:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=CLOSED_PROJECT_UNEDITABLE_MESSAGE
        )
    if full_amount and full_amount < project.invested_amount:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN,
            detail=AMOUNT_LESS_THEN_DEPOSIT_MESSAGE
        )
    if delete and project.invested_amount != 0:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=FORBIDDEN_DELETE_PROJECT_WITH_MONEY
        )
    return project
