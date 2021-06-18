import pyodbc

from nf_common_source.code.services.file_system_service.objects.files import Files
from nf_common_source.code.services.file_system_service.objects.folders import Folders
from nf_common_source.code.services.input_output_service.delimited_text.dataframe_dictionary_to_csv_files_writer import \
    write_dataframe_dictionary_to_csv_files
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message


def write_dataframes_to_access(
        dataframes_dictionary_keyed_on_string: dict,
        database_file: Files,
        temporary_csv_folder: Folders):
    write_dataframe_dictionary_to_csv_files(
        folder_name=temporary_csv_folder.absolute_path_string,
        dataframes_dictionary=dataframes_dictionary_keyed_on_string)

    database_connection_string = \
        'Driver={Microsoft Access Driver (*.mdb, *.accdb)};' + \
        'Dbq=' + database_file.absolute_path_string + ';'

    database_connection = \
        pyodbc.connect(
            database_connection_string,
            autocommit=True)

    for dataframe_name, dataframe in dataframes_dictionary_keyed_on_string.items():
        if not dataframe.empty:
            __write_dataframe_to_access(
                dataframe_name=dataframe_name,
                database_connection=database_connection,
                temporary_csv_folder=temporary_csv_folder)

    database_connection.close()


def __write_dataframe_to_access(
        dataframe_name: str,
        database_connection: pyodbc.Connection,
        temporary_csv_folder: Folders):
    sql_query = \
        f'SELECT * INTO {dataframe_name} FROM [text;HDR=Yes;FMT=Delimited(,);' \
        f'Database={temporary_csv_folder.absolute_path_string}].{dataframe_name}.csv'

    cursor = \
        database_connection.cursor()

    log_message(
        'Executing SQL Query:')

    log_message(
        '\t' + sql_query)

    cursor.execute(
        sql_query)

    database_connection.commit()
