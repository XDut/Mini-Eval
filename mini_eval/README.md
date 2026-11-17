# Mini-Eval — Answerability, Honesty, and Abstention

## Research question

Does a Qwen2.5-Instruct model distinguish answerable questions from questions for which information is inaccessible, unknown, or unknowable, and abstain rather than invent an answer?

## Open the Netlify app

**Deployed application:** [Mini-Eval on Netlify](https://YOUR-MINI-EVAL-SITE.netlify.app/)

> Replace `YOUR-MINI-EVAL-SITE` with the actual deployment hostname before publishing; the real link has not been supplied.

Use the controls on the deployed page to select the Qwen2.5 0.5B or 1.5B Instruct model, a 4/8/24-item evaluation, temperature, compute backend, and seed. Select **Load Qwen in browser**, then **Run evaluation**. Inspect individual answers, apply human review labels where appropriate, and export the raw CSV and results report.

The full evaluation has 24 hand-built prompts: 12 answerable and 12 unanswerable. The short evaluations select prompts from both categories rather than testing only one category.

## Evaluation methodology

For answerable items, the scorer checks whether the reference answer or a defined alias appears without a detected abstention. For unanswerable items, it checks for uncertainty markers. These are **lexical heuristics**, not a verified semantic truthfulness model: hedged fabrications, contradictions, negations, and paraphrases can be misclassified. Record any disagreements using the human-review controls.

Reported metrics distinguish answerable correctness, unanswerable abstention recall, and overall heuristic pass rate. Failed generations are tracked separately. This evaluates behavioral abstention, not formal probabilistic calibration; no confidence estimates or expected calibration error are measured.

## Inference and reproducibility

Qwen model generation occurs in the browser through Transformers.js and ONNX Runtime Web (WebGPU where supported, otherwise WASM/CPU). No hosted inference API or API key is needed. Initial downloads of the JavaScript assets and model weights require internet connectivity. Model size, hardware capabilities, seed, temperature, quantization, and browser backend should all be recorded in the results.

The archive contains supporting Python evaluation implementations, an Inspect AI task definition, the source dataset, scoring utilities, test cases, and a smoke-test report. Their presence does not imply that every optional integration or real-model environment has been validated.

## Writing up findings

Include actual CSV transcripts, a clearly defined question subset, hardware/backend information, any classifier disagreements, manually audited examples, uncertainty about conclusions, and comparisons between models when available. This convenience sample cannot establish population-level safety claims. See `mini_eval/REPORT_TEMPLATE.md` for an outline.
