from __future__ import annotations
from typing import TYPE_CHECKING, List
from dataclasses import dataclass

if TYPE_CHECKING:
    from pandas import DataFrame
    from .ParserResponse import ParserResponse


@dataclass
class ActionResponse:
    _responses: List[ParserResponse]
    _error_dumps: List[DataFrame]
    _files: List[str]

    @property
    def reponses(self) -> List[ParserResponse]:
        return self._responses

    @property
    def error_dumps(self) -> List[DataFrame]:
        return self._error_dumps

    @property
    def files(self) -> List[str]:
        return self._files
