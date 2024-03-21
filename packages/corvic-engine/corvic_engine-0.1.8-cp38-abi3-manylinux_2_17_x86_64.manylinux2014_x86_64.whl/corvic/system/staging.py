"""Corvic system data staging protocol."""

from collections.abc import Iterable
from typing import Any

import sqlglot
from typing_extensions import Protocol


class StagingDB(Protocol):
    """A connection to some database where staging data can be found."""

    def count_ingested_rows(self, blob_name: str, *other_blob_names: str) -> int:
        """Returns the number of rows of the given blobs available for querying.

        Callers can expect this to be cheap to call.
        """
        ...

    def query_for_blobs(
        self, blob_names: list[str], column_names: list[str]
    ) -> sqlglot.exp.Query: ...

    def run_select_query(
        self, query: sqlglot.exp.Query
    ) -> Iterable[dict[str, Any]]: ...
