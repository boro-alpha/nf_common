from nf_common_source.code.services.user_interaction_service.dictionary_filterers.checkbox_dictionary_filter_frames import \
    CheckboxDictionaryFilterFrames
from nf_common_source.code.services.user_interaction_service.dictionary_filterers.checkbox_dictionary_filter_responses import \
    CheckboxDictionaryFilterResponses


def filter_dictionary_using_checkboxes(
        title: str,
        dictionary: dict) -> CheckboxDictionaryFilterResponses:
    checkbox_dictionary_frames = \
        CheckboxDictionaryFilterFrames(
            title=title,
            dictionary=dictionary)

    checkbox_dictionary_frames.check_filter()

    checkbox_dictionary_filter_response = \
        checkbox_dictionary_frames.get_response()

    return \
        checkbox_dictionary_filter_response
