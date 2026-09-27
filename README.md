# SentinelOps-AI Command Center

> **A zero-cost, GitHub-only SOC L1 command center for alert triage, explainable risk scoring, incident investigation, MITRE ATT&CK context, and playbook-driven response.**

[![View Demo](https://img.shields.io/badge/View%20Demo-GitHub%20Pages-222?style=for-the-badge)](https://sarma9273.github.io/sentinelops-ai-command-center/)

### [→ Open the Live Demo](https://sarma9273.github.io/sentinelops-ai-command-center/)

---

## 1. What is SentinelOps-AI?

If you are new to cybersecurity, think of SentinelOps-AI as a **security control room**.

A SOC receives many security alerts. An analyst has to decide:

- Which alert needs attention?
- How serious is it?
- What evidence should be checked?
- What attack technique may be involved?
- Should it become an incident?
- Which investigation procedure should be followed?
- What should the analyst record?

SentinelOps-AI brings these steps into one workflow:

~~~text
Security Alert
      ↓
Risk Scoring
      ↓
Alert Triage
      ↓
Investigation
      ↓
MITRE ATT&CK Context
      ↓
Incident Case
      ↓
SOC Playbook
      ↓
Analyst Decision
~~~

### One-line analogy

**SentinelOps-AI is like a hospital emergency desk: it identifies which cases need attention, triages them, and guides the next procedure.**

---

# 2. Why was it built?

SOC analysts routinely work through large numbers of alerts and need a structured way to prioritize, investigate, document, and escalate them.

This project provides a **self-contained SOC L1 investigation and demonstration environment** without requiring:

- A paid cloud platform
- A server-side database
- A continuously running backend
- A live SIEM installation
- Paid APIs
- External runtime infrastructure

The current release is deliberately constrained to a **$0, GitHub-only architecture**.

---

# 3. For a Beginner: What Happens When an Alert Arrives?

Suppose a server reports:

> **78 failed SSH login attempts followed by a successful login.**

SentinelOps-AI can:

1. Read the alert.
2. Calculate a risk score.
3. Assign a risk level.
4. Explain the factors contributing to the score.
5. Show the related MITRE ATT&CK context.
6. Link the alert to an incident case.
7. Provide an investigation playbook.
8. Allow the analyst to record the investigation and decision.

The system does **not** replace the analyst.

**It organizes evidence and workflow; the analyst makes the final determination.**

---

# 4. Core Capabilities

| Capability | Purpose |
|---|---|
| **Alert Triage** | Review, filter, prioritize, and open alerts |
| **Explainable Risk Scoring** | Produce a deterministic 0–100 risk score with reasons |
| **Risk Classification** | Map scores to Low, Medium, High, or Critical |
| **Investigation View** | Present alert evidence and contextual fields |
| **MITRE ATT&CK Context** | Associate alerts with tactics and techniques |
| **Incident Generation** | Convert significant alerts into structured cases |
| **SOC L1 Playbooks** | Provide investigation and escalation checklists |
| **Analyst Workflow** | Record notes, case status, and final verdict |
| **Dashboard** | Summarize alerts, risk, incidents, and escalations |
| **Automated Validation** | Validate project contracts before deployment |
| **GitHub Pages Deployment** | Publish the browser application without external hosting |

---

# 5. How to Use It

## Overview

The dashboard summarizes:

- Total alerts
- Critical and High alerts
- Average risk
- Open incidents
- Escalations

## Alert Triage

Each alert can contain:

- Alert ID
- Timestamp
- Rule name
- Rule level
- Severity
- Source IP
- Target host
- Username
- Event type
- MITRE ID
- MITRE tactic
- MITRE technique
- Risk score
- Risk level
- Risk reasons

## Investigation

Examples in the current dataset include:

### SSH brute-force activity

Check:

- Source IP
- Target account
- Failed-attempt volume
- Successful authentication after failures
- Authentication history
- Authorization/context

### Network scanning

Check:

- Source IP
- Target host
- Scanned ports
- Exposed services
- Authorization/context
- Related activity

### Privilege escalation

Check:

- User account
- Privilege-related event
- Command/activity
- Authorization
- Login history
- Related suspicious activity

## MITRE ATT&CK

Use the mapped tactic and technique to understand the behavior represented by the alert and determine what related evidence should be investigated.

**A MITRE mapping is contextual evidence; it does not independently prove malicious activity.**

## Incident Case

Significant alerts can become structured cases containing:

- Case ID
- Linked alert
- Priority
- Risk score
- Severity
- Affected host
- Source IP
- Username
- MITRE mapping
- SOC decision
- Recommended action
- Investigation explanation
- Assigned analyst
- Analyst notes
- Final verdict

## Playbook

Use the corresponding playbook as a structured SOC L1 investigation checklist.

## Analyst Decision

The workflow supports:

- Analyst notes
- Case status
- Final verdict

Browser session changes are stored in **localStorage**. They are not shared through a server-side database.

---

# 6. Professional / Technical Architecture

## 6.1 Runtime Architecture

~~~text
                         GitHub Repository
                                │
                                ↓
                         GitHub Pages
                                │
                                ↓
                  ┌─────────────────────────┐
                  │ HTML + CSS + JavaScript │
                  └─────────────────────────┘
                                │
              ┌─────────────────┼─────────────────┐
              ↓                 ↓                 ↓
        Alert Dataset      Risk Engine       SOC Context
              │                 │                 │
              └─────────────────┼─────────────────┘
                                ↓
                         Alert Triage
                                ↓
                         Investigation
                                ↓
                     MITRE ATT&CK Context
                                ↓
                         Incident Case
                                ↓
                         SOC Playbook
                                ↓
                       Analyst Decision
                                ↓
                         localStorage
~~~

## 6.2 Component Responsibilities

### Browser Application — \`app.js\`

Responsible for the deployed runtime workflow:

- Loading JSON datasets
- Rendering dashboard metrics
- Rendering alerts
- Calculating browser-side risk
- Opening alert investigation views
- Linking alerts to incidents
- Rendering playbooks
- Rendering MITRE context
- Managing analyst session state
- Persisting local analyst changes

### Risk Engine — \`ml_engine/risk_scoring_engine.py\`

Reference implementation of the deterministic scoring logic.

It calculates a score from observable alert attributes and returns:

- Risk score
- Risk level
- Human-readable scoring reasons

### Incident Generator — \`backend/incident_case_generator.py\`

Reference implementation for converting significant alerts into structured incident cases.

An alert becomes incident-eligible when:

~~~text
Risk score >= 65
       OR
Risk level = High/Critical
       OR
Severity = High/Critical
~~~

### JSON Data Layer

The current runtime uses repository-managed JSON datasets for:

- Alerts
- Enriched alerts
- Incidents
- Playbooks
- Project metadata

This makes the current release deterministic, inspectable, and reproducible.

---

# 7. Explainable Risk Engine

The current browser product uses a **deterministic, rule-based scoring model** rather than claiming live autonomous ML inference.

For an alert, the reference engine evaluates:

### Base rule contribution

~~~text
rule_level × 7
~~~

### Severity contribution

| Severity | Points |
|---|---:|
| Critical | +20 |
| High | +15 |
| Medium | +8 |
| Low | +3 |

### Authentication correlation

~~~text
Successful login after failures → +15
~~~

### Failed-attempt volume

| Failed attempts | Points |
|---|---:|
| 100+ | +15 |
| 50–99 | +10 |
| 10–49 | +5 |
| <10 | +0 |

### MITRE tactic contribution

High-risk tactics:

- Credential Access
- Privilege Escalation
- Persistence
- Defense Evasion
- Exfiltration
- Command and Control

**+10 points**

Moderate-risk tactics:

- Discovery
- Reconnaissance
- Initial Access
- Execution

**+5 points**

### Source-IP repetition

~~~text
3+ occurrences → +10
2 occurrences  → +5
otherwise       → +0
~~~

### Event type contribution

| Event type | Points |
|---|---:|
| privilege_escalation | +15 |
| authentication_failure | +8 |
| network_scan | +5 |

### Final normalization

~~~text
Final Score = min(total_points, 100)
~~~

### Risk classification

~~~text
85–100 → Critical
65–84  → High
35–64  → Medium
0–34   → Low
~~~

The engine also returns **risk reasons**, making the score auditable rather than a black-box number.

---

# 8. Incident Generation Model

The reference incident generator separates **alert scoring** from **case creation**.

### Eligibility

~~~text
Alert
  │
  ├── score >= 65 ─────────────┐
  ├── risk = High/Critical ────┤
  └── severity = High/Critical ┤
                                ↓
                         Create Incident
~~~

### Priority mapping

~~~text
Score >= 85 → P1 - Critical
Score >= 65 → P2 - High
Score >= 35 → P3 - Medium
Otherwise   → P4 - Low
~~~

### Case structure

The generated case contains operational context such as:

- \`case_id\`
- \`linked_alert_id\`
- \`case_status\`
- \`priority\`
- \`severity\`
- \`ai_risk_score\`
- \`incident_type\`
- \`affected_host\`
- \`source_ip\`
- \`username\`
- \`mitre_id\`
- \`mitre_tactic\`
- \`mitre_technique\`
- \`soc_decision\`
- \`recommended_action\`
- \`ai_explanation\`
- \`assigned_to\`
- \`analyst_notes\`
- \`final_verdict\`

---

# 9. Data / Evidence Flow

~~~text
Repository JSON
      ↓
Alert Loader
      ↓
Alert Object
      ↓
Risk Evaluation
      ↓
Risk + Reasons
      ↓
Triage View
      ↓
Investigation Context
      ↓
Incident Correlation
      ↓
Playbook
      ↓
Analyst Notes / Verdict
~~~

The current system uses demonstration data rather than live telemetry.

---

# 10. Demonstration Dataset

| Alert | Scenario | ATT&CK Context | Expected Risk |
|---|---|---|---:|
| ALERT-001 | SSH brute force | T1110 — Brute Force | 100 / Critical |
| ALERT-002 | Network service scanning | T1046 — Network Service Discovery | 67 / High |
| ALERT-003 | Suspicious privilege escalation | T1548 — Abuse Elevation Control Mechanism | 100 / Critical |

These are **lab/demo cases**, not live production telemetry.

---

# 11. Browser State Model

The deployed application maintains two categories of state:

### Baseline state

Loaded from repository data:

- Alerts
- Incidents
- Playbooks
- Project data

### Local analyst state

Stored in browser localStorage:

- Notes
- Status changes
- Verdicts
- Session-specific analyst actions

Therefore:

~~~text
Repository data
      ↓
Baseline application state

Browser actions
      ↓
localStorage
      ↓
Same browser profile
~~~

There is currently **no shared persistent backend**.

---

# 12. Security Model and Boundaries

The current release is intentionally designed as a static browser application.

### Security controls include

- Content Security Policy in \`index.html\`
- \`object-src 'none'\`
- \`frame-ancestors 'none'\`
- Same-origin application assets
- No API keys required
- No external runtime dependency
- No production credentials
- Resilient localStorage parsing
- HTTP response validation before JSON parsing

### Important boundary

The application is a **SOC learning/demo command center**, not a production security monitoring platform.

It should not be interpreted as providing:

- Production authentication
- RBAC
- Server-side authorization
- Multi-user persistence
- Live SIEM ingestion
- Production containment
- Autonomous SOAR execution

---

# 13. Validation and Quality Gates

The repository contains automated integrity tests and a GitHub Actions deployment gate.

Validation covers:

### Data integrity

- JSON files parse correctly
- Required data contracts exist

### Python integrity

- Python source compiles successfully
- Reference components can be imported

### Risk regression

The test suite verifies the expected demonstration outputs:

~~~text
Scores:
[100, 67, 100]

Levels:
[Critical, High, Critical]
~~~

### Incident contract

Tests verify that each enriched demonstration alert:

- Meets incident-generation criteria
- Produces an incident
- Links back to the source alert
- Generates a valid incident ID

### Browser runtime contract

The project also checks required browser runtime/security constructs such as:

- localStorage handling
- JSON loader behavior
- core workflow functions
- CSP requirements
- absence of external HTTP/HTTPS runtime dependencies in the application code

---

# 14. CI/CD Flow

Every push to \`main\` follows:

~~~text
Git Push
   ↓
GitHub Actions
   ↓
JSON Validation
   ↓
Python Syntax Validation
   ↓
Automated Tests
   ↓
Static Runtime Checks
   ↓
Validation Passed
   ↓
GitHub Pages Artifact
   ↓
GitHub Pages Deployment
~~~

This keeps validation ahead of deployment.

---

# 15. Technology Stack

| Layer | Technology |
|---|---|
| UI | HTML5 |
| Styling | CSS3 |
| Application logic | Vanilla JavaScript |
| Runtime | Browser |
| Data format | JSON |
| Reference logic | Python |
| Testing | Python unittest |
| Source control | GitHub |
| CI/CD | GitHub Actions |
| Hosting | GitHub Pages |
| Browser persistence | localStorage |
| Cost model | $0 |

The deployed runtime intentionally does not depend on a server-side Python application.

---

# 16. Repository Structure

~~~text
SentinelOps_AI/
│
├── index.html                         # GitHub Pages entry point
├── styles.css                         # SOC interface
├── app.js                             # Browser application
│
├── backend/
│   └── incident_case_generator.py    # Incident reference logic
│
├── ml_engine/
│   └── risk_scoring_engine.py         # Risk reference logic
│
├── sample_data/
│   ├── alerts_sample.json             # Source alerts
│   └── alerts_enriched_with_risk.json # Enriched alert examples
│
├── database/
│   └── incidents_db.json              # Demo incident cases
│
├── incident_playbooks/
│   └── default_soc_playbooks.json     # SOC L1 playbooks
│
├── reports/                           # Example incident reports
├── learning_notes/                    # Phase documentation
├── tests/                             # Automated validation
├── docs/                              # Architecture/release docs
│
├── .github/
│   └── workflows/
│       └── pages.yml                  # Validate + deploy
│
├── project_manifest.json              # Project metadata
├── README.md
└── LICENSE
~~~

---

# 17. Recommended Technical Demo

For a recruiter, SOC analyst, trainer, or technical evaluator:

~~~text
Overview
   ↓
Alert Triage
   ↓
Open ALERT-001
   ↓
Inspect Evidence
   ↓
Inspect Risk Reasons
   ↓
Review MITRE Mapping
   ↓
Open Linked Incident
   ↓
Open PB-001
   ↓
Review Escalation Condition
   ↓
Add Analyst Note
   ↓
Set Status / Verdict
~~~

Then repeat with:

- ALERT-002 — network scanning
- ALERT-003 — privilege escalation

This demonstrates multiple SOC investigation paths rather than only the dashboard.

---

# 18. What Is Implemented

### Application

- SOC dashboard
- Alert triage
- Alert investigation
- Deterministic explainable risk scoring
- Risk classification
- Incident case views
- MITRE ATT&CK context
- SOC L1 playbooks
- Analyst notes
- Status/verdict workflow
- Browser persistence
- Responsive interface

### Engineering

- JSON data contracts
- Python reference implementations
- Risk regression tests
- Incident-generation tests
- Browser runtime contract tests
- Security/runtime hardening
- GitHub Actions validation
- GitHub Pages deployment

---

# 19. Current Scope Boundary

## Implemented in this release

- Static SOC command center
- Demonstration alert dataset
- Explainable risk engine
- Incident workflow
- MITRE context
- Playbook workflow
- Analyst session state
- Automated validation
- GitHub Pages deployment

## Intentionally not implemented

- Live SIEM ingestion
- Live Wazuh connectivity
- Persistent server-side incident database
- Production authentication/RBAC
- Multi-user collaboration
- Production SOAR execution
- External threat-intelligence API dependency
- Autonomous production ML inference
- Production containment actions

These require additional infrastructure and are outside the current **$0 GitHub-only release**.

---

# 20. AI / ML Positioning

The project is named **SentinelOps-AI**, but the current GitHub Pages runtime should be understood precisely:

**The deployed browser risk engine is deterministic and explainable.**

It does not claim that the current release performs autonomous production-grade ML inference.

The repository's Python risk-scoring layer provides the reference implementation and regression-tested logic.

This distinction is intentional: the project prioritizes **reproducibility, explainability, inspectability, and zero-cost deployment** for the current release.

---

# 21. Local Development

From the repository root:

~~~bash
python -m http.server 8000
~~~

Open:

~~~text
http://localhost:8000/
~~~

Run the Python reference-layer tests:

~~~bash
python -m unittest discover -s tests -p "test_*.py" -v
~~~

---

# 22. Security Rules for Contributors

Never commit:

- API keys
- Passwords
- Access tokens
- Private keys
- Certificates
- Production credentials
- Real sensitive telemetry
- Personally identifiable security data

The current repository is designed around demonstration/lab data.

---

# 23. Project Status

**Current GitHub-only product baseline: complete for the defined release scope.**

The current release demonstrates:

**Alert → Risk → Triage → Investigation → MITRE Context → Incident → Playbook → Analyst Decision**

The architecture is intentionally small enough to run at $0 while keeping the SOC workflow explicit and inspectable.

---

## License

See [LICENSE](LICENSE).

---

## Links

**GitHub Repository:** [Sarma9273/sentinelops-ai-command-center](https://github.com/Sarma9273/sentinelops-ai-command-center)

**Live Demo:** [Open SentinelOps-AI Command Center](https://sarma9273.github.io/sentinelops-ai-command-center/)
