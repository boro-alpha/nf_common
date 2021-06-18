from nf_common_source.code.services.user_interaction_service.dictionary_filterers.checkbox_dictionary_filter_responses import \
    CheckboxDictionaryFilterResponses
from nf_common_source.code.services.user_interaction_service.dictionary_filterers.checkbox_dictionary_filterer import \
    filter_dictionary_using_checkboxes


def filter_dictionary(
        title: str,
        dictionary: dict) -> CheckboxDictionaryFilterResponses:
    checkbox_dictionary_filter_response = \
        filter_dictionary_using_checkboxes(
            title=title,
            dictionary=dictionary)

    return \
        checkbox_dictionary_filter_response
