from datetime import datetime


def close_investing(obj_in):
    if obj_in.invested_amount == obj_in.full_amount:
        obj_in.fully_invested = True
        obj_in.close_date = datetime.now()
        return True
    return False


def process_investments(
    target,
    in_obj_invest
):
    all_targets = []
    for source in in_obj_invest:
        investing_volume = min(
            source.full_amount - source.invested_amount,
            target.full_amount - int(target.invested_amount or 0)
        )
        source.invested_amount += investing_volume
        target.invested_amount = int(
            target.invested_amount or 0
        ) + investing_volume
        close_investing(source)
        all_targets.append(source)
        breaking = close_investing(target)
        if breaking:
            break
        all_targets.append(target)
    return all_targets
