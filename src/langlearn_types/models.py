from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path


class ImageProvider(StrEnum):
    openai = "openai"
    pexels = "pexels"


class AudioProvider(StrEnum):
    elevenlabs = "elevenlabs"
    polly = "polly"
    openai = "openai"


class ImageStyle(StrEnum):
    default = "default"
    painting = "painting"
    photo = "photo"


@dataclass(frozen=True)
class EvaluationResult:
    passed: bool
    score: float | None
    reason: str | None
    metadata: dict[str, str]


@dataclass(frozen=True)
class PromptSpec:
    text: str
    language: str | None
    style: str | None
    metadata: dict[str, str]


@dataclass(frozen=True)
class ImageRequest:
    prompt: str
    style: ImageStyle | None
    size: str | None
    language: str | None
    metadata: dict[str, str]


@dataclass(frozen=True)
class ImageResult:
    path: Path
    prompt: str
    provider: ImageProvider
    metadata: dict[str, str]


@dataclass(frozen=True)
class AudioRequest:
    text: str
    voice: str | None
    language: str | None
    rate: int | None
    metadata: dict[str, str]


@dataclass(frozen=True)
class AudioResult:
    path: Path
    text: str
    provider: AudioProvider
    metadata: dict[str, str]


@dataclass(frozen=True)
class MediaManifest:
    audio: dict[str, Path]
    images: dict[str, Path]
    metadata: dict[str, str]


@dataclass(frozen=True)
class DeckRequest:
    language: str
    deck: str
    data_dir: Path
    media: MediaManifest | None
    output_path: Path | None


@dataclass(frozen=True)
class DeckResult:
    output_path: Path
    cards_exported: int
    media_used: int
    metadata: dict[str, str]
