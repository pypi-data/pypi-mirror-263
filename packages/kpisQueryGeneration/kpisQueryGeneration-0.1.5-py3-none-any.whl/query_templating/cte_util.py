import functools


def get_ctes_to_use(tables_to_use_mappings, kpis_to_calculate):

    return list(
        set(functools.reduce(lambda a, b: handleNone(a) + handleNone(tables_to_use_mappings.get(b)), kpis_to_calculate, [])))


def handleNone(val):

    if val is None:
        return []

    return val
