# Mini-Eval repair log

1. **Factual correctness**: non-abstention alone is no longer accepted as an answerable pass; target/alias matching is required in Python and HTML.
2. **Matcher boundaries**: whole-word/number boundaries and common aliases replace naive substring matches; simple negated targets are ignored.
3. **Balanced smoke tests**: 4-/8-item tests now include both question classes. Full runs interleave classes; deterministic sampling seed added.
4. **Human quality control**: browser reviewers can label each generation pass/fail; manual labels and agreement are exported.
5. **Failure handling**: download/generation errors stay visible and are excluded from reported accuracy denominators; stop/run and model device selection improved.
6. **Inspect integration**: Inspect task now calls the same shared target-aware scoring functions; no hosted inference is needed with the `hf/` local provider.
7. **Reproducibility and evidence**: CLI CSV + JSON summaries, browser CSV + text report templates, regression tests, explicit limitations, and instructions for collecting real evidence.

Other technical improvements: quantized Qwen choices, WebGPU-to-WASM automatic fallback, HTML dataset synchronized to JSONL, no embedded fake model performance, no API-token workflow.

Important: unit tests and browser UI smoke tests do **not** prove actual Qwen ONNX inference works on every user's device. The application intentionally downloads its weights on first model load, and that step must be tested on the target device.
