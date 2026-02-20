from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, TypeVar, runtime_checkable

from .models import (
    AudioRequest,
    AudioResult,
    DeckRequest,
    DeckResult,
    EvaluationResult,
    ImageRequest,
    ImageResult,
    PromptSpec,
)

InputT = TypeVar("InputT", contravariant=True)


@runtime_checkable
class Evaluator(Protocol[InputT]):
    """Evaluate a generated asset or deck."""

    def evaluate(self, item: InputT) -> EvaluationResult: ...


@runtime_checkable
class PromptGenerator(Protocol):
    """Generate or refine prompts for downstream providers."""

    def generate_prompt(self, spec: PromptSpec) -> PromptSpec: ...


@runtime_checkable
class ImageProvider(Protocol):
    """Provider that generates images from prompts."""

    def generate_image(self, request: ImageRequest) -> ImageResult: ...

    def generate_images(
        self, requests: Sequence[ImageRequest]
    ) -> list[ImageResult]: ...


@runtime_checkable
class ImageEvaluator(Evaluator[ImageResult], Protocol):
    """Evaluate generated images."""

    def evaluate(self, item: ImageResult) -> EvaluationResult: ...


@runtime_checkable
class AudioProvider(Protocol):
    """Provider that synthesizes audio from text."""

    def generate_audio(self, request: AudioRequest) -> AudioResult: ...

    def generate_audios(
        self, requests: Sequence[AudioRequest]
    ) -> list[AudioResult]: ...


@runtime_checkable
class AudioEvaluator(Evaluator[AudioResult], Protocol):
    """Evaluate generated audio."""

    def evaluate(self, item: AudioResult) -> EvaluationResult: ...


@runtime_checkable
class DeckGenerator(Protocol):
    """Provider that builds decks from structured data."""

    def build_deck(self, request: DeckRequest) -> DeckResult: ...


@runtime_checkable
class DeckExporter(Protocol):
    """Provider that exports decks to a distribution format."""

    def export_deck(self, request: DeckRequest) -> DeckResult: ...


@runtime_checkable
class DeckEvaluator(Evaluator[DeckResult], Protocol):
    """Evaluate deck output or exports."""

    def evaluate(self, item: DeckResult) -> EvaluationResult: ...
