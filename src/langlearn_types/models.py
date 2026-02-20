from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from pathlib import Path


def _metadata() -> dict[str, str]:
    return {}


class ImageProviderId(StrEnum):
    """Supported image generation providers."""

    openai = "openai"
    pexels = "pexels"


class AudioProviderId(StrEnum):
    """Supported text-to-speech providers."""

    elevenlabs = "elevenlabs"
    polly = "polly"
    openai = "openai"


class ImageStyle(StrEnum):
    """Common image style hints."""

    default = "default"
    painting = "painting"
    photo = "photo"


@dataclass(frozen=True)
class EvaluationMetric:
    """Single evaluation signal for a prompt or generated asset."""

    name: str
    score: float | None = None
    passed: bool | None = None
    reason: str | None = None
    metadata: dict[str, str] = field(default_factory=_metadata)


@dataclass(frozen=True)
class EvaluationResult:
    """Outcome of evaluating a generated asset or deck."""

    passed: bool
    score: float | None
    reason: str | None
    metrics: tuple[EvaluationMetric, ...] = field(default_factory=tuple)
    metadata: dict[str, str] = field(default_factory=_metadata)


@dataclass(frozen=True)
class EvaluationReport:
    """Aggregate evaluation results for a batch or pipeline stage."""

    passed: bool
    results: tuple[EvaluationResult, ...]
    metadata: dict[str, str] = field(default_factory=_metadata)


@dataclass(frozen=True)
class PromptSpec:
    """Prompt input and metadata for generation steps."""

    text: str
    language: str | None
    style: str | None
    metadata: dict[str, str] = field(default_factory=_metadata)


@dataclass(frozen=True)
class EvaluationSpec:
    """Configuration for evaluation gates in the orchestrator."""

    evaluator: str | None = None
    threshold: float | None = None
    required: bool = True
    metadata: dict[str, str] = field(default_factory=_metadata)


@dataclass(frozen=True)
class PromptBundle:
    """Prompt, style, and evaluation configuration for a single step."""

    prompt: PromptSpec
    style: str | None = None
    evaluator: EvaluationSpec | None = None
    metadata: dict[str, str] = field(default_factory=_metadata)


@dataclass(frozen=True)
class ImageRequest:
    """Request to generate a single image."""

    prompt: str
    provider: ImageProviderId | None = None
    size: str | None = None
    style: str | None = None
    language: str | None = None
    cultural_context: str | None = None
    quality: str | None = None
    seed: int | None = None
    metadata: dict[str, str] = field(default_factory=_metadata)


@dataclass(frozen=True)
class ImageResult:
    """Result of an image generation request."""

    path: Path
    prompt: str
    provider: ImageProviderId
    revised_prompt: str | None = None
    model: str | None = None
    metadata: dict[str, str] = field(default_factory=_metadata)


@dataclass(frozen=True)
class AudioRequest:
    """Request to synthesize a single audio clip."""

    text: str
    voice: str | None = None
    language: str | None = None
    rate: int | None = None
    stability: float | None = None
    similarity: float | None = None
    style: float | None = None
    speaker_boost: bool | None = None
    provider: AudioProviderId | None = None
    metadata: dict[str, str] = field(default_factory=_metadata)


@dataclass(frozen=True)
class AudioResult:
    """Result of an audio synthesis request."""

    path: Path
    text: str
    provider: AudioProviderId
    voice: str | None = None
    language: str | None = None
    metadata: dict[str, str] = field(default_factory=_metadata)


@dataclass(frozen=True)
class MediaManifest:
    """Mapping of media identifiers to generated asset paths."""

    audio: dict[str, Path]
    images: dict[str, Path]
    metadata: dict[str, str] = field(default_factory=_metadata)


@dataclass(frozen=True)
class DeckRequest:
    """Request to build and export a deck."""

    language: str
    deck: str
    data_dir: Path
    media: MediaManifest | None = None
    output_path: Path | None = None
    metadata: dict[str, str] = field(default_factory=_metadata)


@dataclass(frozen=True)
class DeckResult:
    """Result of a deck build request."""

    output_path: Path
    cards_exported: int
    media_used: int
    metadata: dict[str, str] = field(default_factory=_metadata)
