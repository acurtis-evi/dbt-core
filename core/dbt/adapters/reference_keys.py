# this module exists to resolve circular imports with the events module

from collections import namedtuple
from typing import Any, Optional
from dbt.events.proto_types import ReferenceKeyMsg


_ReferenceKey = namedtuple("_ReferenceKey", "database schema identifier")


def lowercase(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    else:
        return value.lower()


def _make_key(relation: Any) -> _ReferenceKey:
    """Make _ReferenceKeys with lowercase values for the cache so we don't have
    to keep track of quoting
    """
    # databases and schemas can both be None
    return _ReferenceKey(
        lowercase(relation.database), lowercase(relation.schema), lowercase(relation.identifier)
    )


def _make_key_msg(relation: Any):
    return _make_msg_from_key(_make_key(relation))


def _make_msg_from_key(ref_key: _ReferenceKey) -> ReferenceKeyMsg:
    return ReferenceKeyMsg(
        database=ref_key.database, schema=ref_key.schema, identifier=ref_key.identifier
    )
