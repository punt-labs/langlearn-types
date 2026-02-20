from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, TypeVar

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


class Evaluator(Protocol[InputT]):
    def evaluate(self, item: InputT) -> EvaluationResult: ...


class PromptGenerator(Protocol):
    def generate_prompt(self, spec: PromptSpec) -> PromptSpec: ...


class ImageGenerator(Protocol):
    def generate_image(self, request: ImageRequest) -> ImageResult: ...

    def generate_images(
        self, requests: Sequence[ImageRequest]
    ) -> list[ImageResult]: ...


class AudioGenerator(Protocol):
    def generate_audio(self, request: AudioRequest) -> AudioResult: ...

    def generate_audios(
        self, requests: Sequence[AudioRequest]
    ) -> list[AudioResult]: ...


class DeckBuilder(Protocol):
    def build_deck(self, request: DeckRequest) -> DeckResult: ...
