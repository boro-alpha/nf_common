import xlrd
from pandas import DataFrame
from nf_common_source.code.services.file_system_service.objects.files import Files
from nf_common_source.code.services.input_output_service.excel.excel_read import convert_sheet_with_header_to_dataframe


def covert_xlxs_to_dataframe_dictionary(
        xlsx_file: Files) \
        -> dict:
    xlsx_workbook = \
        xlrd.open_workbook(
            xlsx_file.absolute_path_string,
            on_demand=True)

    dataframe_dictionary = \
        {}

    for sheet_name in xlsx_workbook.sheet_names():
        dataframe_dictionary[sheet_name] = \
            __convert_sheet_to_dataframe(
                file_name=xlsx_file.absolute_path_string,
                sheet_name=sheet_name)

    return \
        dataframe_dictionary


def __convert_sheet_to_dataframe(
        file_name: str,
        sheet_name: str) \
        -> DataFrame:
    dataframe = \
        convert_sheet_with_header_to_dataframe(
            file_name=file_name,
            sheet_name=sheet_name)

    return \
        dataframe
