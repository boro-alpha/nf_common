from enum import auto
from enum import unique

from nf_common_source.code.nf.types.collection_types import CollectionTypes


@unique
class CommonCollectionTypes(
    CollectionTypes):
    SUMMARY_TABLE = auto()

    def __collection_name(
            self) \
            -> str:
        collection_name = \
            collection_name_mapping[self]

        return \
            collection_name

    collection_name = \
        property(
            fget=__collection_name)


collection_name_mapping = \
    {
        CommonCollectionTypes.SUMMARY_TABLE: 'summary_table'
    }
