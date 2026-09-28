# SentinelOps-AI 2.0 Research Specification

## Identity
SentinelOps-AI 2.0 is an AI-assisted SOC operational and decision-support platform. It prioritizes, correlates, routes, and manages security alerts and incident workflows.

## Hard boundaries
- v1.0.0 remains frozen.
- v2 is developed on `v1.1-ai-risk-engine`.
- Deployment remains GitHub-only and $0.
- No external database, paid API, hosted backend, or production SIEM/SOAR dependency.
- SentinelOps-AI does not duplicate RA-XSOC's RAG, deep evidence reasoning, competing hypotheses, information-gain planning, or adaptive investigation memory.

## Research question
Does a browser-native hybrid risk model combining an explainable deterministic baseline with a local logistic-regression model provide a reproducible basis for security-alert prioritization while preserving analyst transparency?

## Experimental configurations
1. Deterministic baseline: existing v1 risk score.
2. ML model: local logistic-regression probability.
3. Hybrid model: deterministic score + ML probability.

## Input features
`rule_norm, severity_norm, auth_success, failed_attempts_norm, tactic_risk, source_repetition_norm, event_risk, anomaly_signal`.

All ML features are normalized to [0,1].

## Hybrid output
Every scored alert should expose deterministic risk, ML probability, hybrid/final risk, confidence, risk factors, and model version.

## Evaluation
Use labelled train/test data and report precision, recall, F1, false-positive rate, accuracy where appropriate, inference latency, and explanation coverage. Results must be generated from actual experiments; no fabricated performance claims.

## Operational v2 scope
- alert normalization
- risk assessment
- alert correlation
- SOC priority/work queue
- alert lifecycle
- operational incident timeline
- interactive playbook execution
- MITRE operational context
- analyst feedback
- SOC analytics
- model evaluation

## Research reproducibility
The synthetic dataset, training script, model metadata, evaluation code, and experiment configuration remain version-controlled in GitHub.
