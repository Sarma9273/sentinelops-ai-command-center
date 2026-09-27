# SentinelOps-AI Command Center

SentinelOps-AI is a **GitHub-only SOC L1 learning and demonstration command center**. The current release demonstrates deterministic alert risk scoring, MITRE ATT&CK context, incident-case generation, analyst workflow, and SOC L1 playbooks using repository data and browser-local state.

## Current product boundary

The deployed runtime is:

```
GitHub repository
      ↓
GitHub Pages
      ↓
HTML + CSS + browser JavaScript
      ↓
Repository sample alerts / cases / playbooks
      ↓
Browser-side risk scoring + investigation workflow
      ↓
localStorage for analyst session changes
```

It is **not** a live SIEM, persistent backend, Wazuh manager, production SOAR platform, or real-time alert-ingestion service.

## Implemented capabilities

- SOC overview dashboard
- Alert queue and search/filtering
- Deterministic risk scoring using the Phase 1 scoring rules
- Explainable risk-factor display
- MITRE ATT&CK technique/tactic context
- Alert investigation view
- Incident case creation/opening
- Case priority and status workflow
- Analyst notes
- True Positive / False Positive / Pending verdict
- Browser-local session persistence
- SOC L1 investigation playbooks
- Responsive GitHub Pages UI
- Automated JSON, Python, regression, contract, and runtime validation before deployment

## Phase history

| Phase | Scope | Status |
|---|---|---|
| 1.1 | SOC workspace and sample alerts | Completed |
| 1.2 | Risk scoring and alert enrichment | Completed |
| 1.3 | Incident case generation and playbooks | Completed |
| 1.4 | Dashboard metrics and investigation data | Completed |
| 1.5 | Static SOC web dashboard | Completed |
| 2.1 | Browser-native GitHub product shell | Completed |
| 2.2 | Automated release/validation hardening | Completed |

## Risk-scoring model

The current runtime uses deterministic, explainable rules rather than claiming live autonomous ML inference.

Contributors include:

- rule level
- alert severity
- successful login after failures
- failed-attempt volume
- MITRE tactic
- repeated source IP
- event type

The score is capped at 100 and mapped to Critical / High / Medium / Low thresholds. The Python research implementation and browser implementation are regression-tested against the same sample alert set.

## SOC L1 learning outcome

The project demonstrates how an analyst can:

- inspect an alert
- understand why a risk score was produced
- correlate evidence with MITRE ATT&CK
- decide whether an alert should become an incident
- document investigation findings
- use a playbook
- assign a case status and verdict
- escalate based on documented conditions

## Deliberate non-goals for the $0 GitHub-only release

The current release does not claim:

- live SIEM ingestion
- real-time Wazuh connectivity
- persistent server-side incident storage
- production authentication/RBAC
- automated endpoint containment
- production SOAR execution
- external threat-intelligence API calls
- autonomous production ML inference

Those capabilities require infrastructure outside the current GitHub-only architecture.

## Research layer

The Python modules and historical learning notes preserve the Phase 1 research/reference implementation. Google Colab is treated as an external experimentation environment, not as a dependency of the deployed product.

## Local run

```bash
python -m http.server 8000
```

Then open `http://localhost:8000/`.

## Release principle

The repository should only describe capabilities that are actually implemented and testable. Future integrations should be documented as future work only when implementation begins.
