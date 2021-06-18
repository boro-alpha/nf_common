from pandas import DataFrame
from nf_common_source.code.constants.standard_constants import DEFAULT_NULL_VALUE
from nf_common_source.code.services.dataframe_service.dataframe_mergers import left_merge_dataframes


def get_dataframe_focus_minus_matched_other(
        focus_dataframe: DataFrame,
        other_dataframe: DataFrame,
        matched_column_name: str) \
        -> DataFrame:
    focus_minus_matched_other_dataframe = \
        left_merge_dataframes(
            master_dataframe=focus_dataframe,
            master_dataframe_key_columns=[matched_column_name],
            merge_suffixes=['_focus', '_other'],
            foreign_key_dataframe=other_dataframe,
            foreign_key_dataframe_fk_columns=[matched_column_name],
            foreign_key_dataframe_other_column_rename_dictionary=
            {
                matched_column_name: 'nullable'
            })

    focus_minus_matched_other_dataframe = \
        focus_minus_matched_other_dataframe.fillna(
            DEFAULT_NULL_VALUE)

    focus_minus_matched_other_dataframe = \
        focus_minus_matched_other_dataframe.loc[focus_minus_matched_other_dataframe['nullable'] == DEFAULT_NULL_VALUE]

    focus_minus_matched_other_dataframe.drop(
        labels='nullable',
        axis=1,
        inplace=True)

    return \
        focus_minus_matched_other_dataframe
