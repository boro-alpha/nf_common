from pandas import DataFrame
from nf_common_source.code.services.identification_services.uuid_service.uuid_helpers.uuid_factory import \
    create_new_uuid


def uuidify_dataframe(
        dataframe: DataFrame,
        uuid_column_name: str) \
        -> DataFrame:
    uuidified_dataframe = \
        dataframe.copy()

    uuidified_dataframe[uuid_column_name] = \
        uuidified_dataframe.apply(
            lambda row: create_new_uuid(),
            axis=1)

    dataframe_without_new_uuid_column = \
        uuidified_dataframe.pop(
            uuid_column_name)

    uuidified_dataframe.insert(
        0,
        uuid_column_name,
        dataframe_without_new_uuid_column)

    return \
        uuidified_dataframe
