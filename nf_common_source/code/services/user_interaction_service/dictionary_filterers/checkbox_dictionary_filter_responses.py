from nf_common_source.code.services.user_interaction_service.common_knowledge.window_return_types import \
    WindowReturnTypes


class CheckboxDictionaryFilterResponses:
    def __init__(
            self):
        self.selected_items = {}

        self.button_clicked = \
            WindowReturnTypes.CANCEL
