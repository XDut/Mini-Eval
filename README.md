# Mini-Eval — AI Safety Evaluation

## Using the deployed app

1. Visit the **Netlify deployment** above.
2. Select **Qwen2.5 0.5B Instruct** to start, or **Qwen2.5 1.5B Instruct** for a second model comparison.
3. Select the evaluation size (**4 balanced**, **8 balanced**, or **all 24 questions**), temperature, compute backend, and sampling seed.
4. Click **Load Qwen in browser**. The browser downloads the needed public Qwen and Transformers.js assets on first use.
5. Click **Run evaluation** to view the metrics and question-level evidence.
6. Review uncertain classifications, then use **Export raw CSV** and **Export results report** to save actual measurements.

## Research question

Does a Qwen2.5-Instruct model distinguish answerable questions from questions for which information is inaccessible, unknown, or unknowable, and abstain rather than invent an answer?

## What the project measures

- Accuracy on questions with reference answers.
- Abstention on questions that cannot be reliably answered.
- Overall heuristic pass rate and response-by-response evidence.
- Differences between supported Qwen model sizes.

## Evaluation methodology

For answerable items, the scorer checks whether the reference answer or a defined alias appears without a detected abstention. For unanswerable items, it checks for uncertainty markers. These are **lexical heuristics**, not a verified semantic truthfulness model: hedged fabrications, contradictions, negations, and paraphrases can be misclassified. Record any disagreements using the human-review controls.

Reported metrics distinguish answerable correctness, unanswerable abstention recall, and overall heuristic pass rate. Failed generations are tracked separately. This evaluates behavioral abstention, not formal probabilistic calibration; no confidence estimates or expected calibration error are measured.

## Inference, Reproducitibility and limitations

Model inference executes within the visitor's browser using Transformers.js and ONNX Runtime Web, with WebGPU or WASM/CPU support. **No hosted inference API or API key is required.** First use needs an internet connection for model and library assets. Device/browser compatibility, bandwidth, and available memory affect load and inference speed.

Automated evaluation uses lexical heuristics and may misclassify contradictory or nuanced responses. Human review and exported transcripts are important; the 24-item dataset is a demonstration, **not a validated safety benchmark**. No model performance values are claimed without actual evaluation runs. The repository archive also contains Python evaluation code, dataset files, test cases, and a smoke-test report for technical review; the deployed app is the recommended user-facing entry point.
