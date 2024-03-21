import asyncio
from typing import Any, Protocol, Sequence, TypeVar

from tdm import TalismanDocument

from tp_interfaces.abstract import AbstractDocumentProcessor, ImmutableBaseModel


class Metric(Protocol):
    pass


_Config = TypeVar("_Config", bound=ImmutableBaseModel, covariant=True)
_Metric = TypeVar("_Metric", bound=Metric, covariant=True)
_Context = TypeVar("_Context", bound=Any, covariant=True)
_Doc = TypeVar("_Doc", bound=Any, covariant=True)


class Evaluatable(Protocol[_Doc, _Metric, _Context]):
    def evaluate(self, gold_docs: Sequence[_Doc], context: _Context) -> Sequence[_Metric]:
        raise NotImplementedError


class EvaluatableProcessor(AbstractDocumentProcessor, Evaluatable, Protocol[_Metric, _Config]):
    def _evaluate(self, gold_docs: Sequence[TalismanDocument], actual_docs: Sequence[TalismanDocument]) -> Sequence[_Metric]:
        pass

    def _prepare_doc(self, doc: TalismanDocument) -> TalismanDocument:
        pass

    def evaluate(self, gold_docs: Sequence[TalismanDocument], context: _Config) -> Sequence[_Metric]:
        clear_docs = tuple(map(self._prepare_doc, gold_docs))
        actual_docs = asyncio.run(self.process_docs(clear_docs, context))
        return self._evaluate(gold_docs, actual_docs)
