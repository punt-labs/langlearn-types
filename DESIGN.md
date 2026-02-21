# Design Decision Log

## 0001 — Initial split into tri-modal packages (SETTLED)
- Pure interfaces and immutable data models shared across LangLearn packages.
- No backend logic or prompt refinement in this package.

## 0002 — Expanded contracts and provider protocols (SETTLED)
- ImageRequest/ImageResult include provider, size, style, language, cultural_context, quality, seed, and metadata defaults.
- AudioRequest/AudioResult include provider, voice, language, rate, ElevenLabs settings, and metadata defaults.
- DeckRequest/DeckResult include optional media/output_path plus metadata defaults.
- Provider protocols are ImageProvider, ImageEvaluator, AudioProvider, DeckGenerator, and DeckExporter.
- EvaluationResult and PromptBundle contracts are included for orchestrator evaluation flows.
