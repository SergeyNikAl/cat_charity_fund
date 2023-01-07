from datetime import datetime


def process_investments(
    target,
    sources
):
    modified_targets = []
    if not target.invested_amount:
        target.invested_amount = 0
    for source in sources:
        investing_volume = min(
            source.full_amount - source.invested_amount,
            target.full_amount - target.invested_amount
        )
        for object in (source, target):
            object.invested_amount += investing_volume
            if object.invested_amount == object.full_amount:
                object.fully_invested = True
                object.close_date = datetime.now()
        modified_targets.append(source)
    return modified_targets
