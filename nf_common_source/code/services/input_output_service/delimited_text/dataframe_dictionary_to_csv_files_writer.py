import csv

import pandas


def write_dataframe_dictionary_to_csv_files(
        folder_name: str,
        dataframes_dictionary: dict):
    for dataframe_name, dataframe in dataframes_dictionary.items():
        __write_dataframe_to_csv_file(
            folder_name=folder_name,
            dataframe_name=dataframe_name,
            dataframe=dataframe)


def __write_dataframe_to_csv_file(
        folder_name: str,
        dataframe_name: str,
        dataframe: pandas.DataFrame):
    dataframe.to_csv(
        path_or_buf=folder_name + '\\' + dataframe_name + '.csv',
        sep=',',
        quotechar='"',
        index=False,
        quoting=csv.QUOTE_ALL)
