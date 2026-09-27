# SentinelOps-AI Command Center

> A zero-cost, GitHub-only SOC L1 command center for **alert triage, explainable risk scoring, incident investigation, MITRE ATT&CK context, and playbook-driven response**.

[![View Demo](https://img.shields.io/badge/View%20Demo-GitHub%20Pages-222?style=for-the-badge)](https://sarma9273.github.io/sentinelops-ai-command-center/)

**[→ Open the Live Demo](https://sarma9273.github.io/sentinelops-ai-command-center/)**

---

## What is SentinelOps-AI?

If you are new to cybersecurity, think of SentinelOps-AI as a **security control room**.

A SOC receives many security alerts. An analyst has to decide:

- Which alert needs attention?
- How serious is it?
- What evidence should be checked?
- What attack technique may be involved?
- Should it become an incident?
- Which investigation procedure should be followed?
- What should the analyst record?

SentinelOps-AI brings these steps into one simple workflow:

~~~text
Security Alert
      ↓
Risk Scoring
      ↓
Alert Triage
      ↓
Investigation
      ↓
MITRE ATT&CK
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

## Why was it built?

Real SOC environments can be complex. This project provides a self-contained environment for learning and demonstrating the **SOC L1 investigation workflow** without requiring a paid cloud platform, external database, or live SIEM infrastructure.

The current release focuses on:

- Explainable alert risk scoring
- Alert prioritization
- Incident case generation
- MITRE ATT&CK context
- SOC L1 investigation playbooks
- Analyst notes, status, and verdicts
- Browser-based investigation workflow
- Automated validation through GitHub Actions

---

# Core Capabilities

| Capability | What it does |
|---|---|
| **Alert Triage** | Displays and filters security alerts for investigation |
| **Risk Scoring** | Produces an explainable 0–100 risk score |
| **Risk Classification** | Categorizes alerts as Low, Medium, High, or Critical |
| **Investigation** | Presents the evidence needed for L1 analysis |
| **MITRE ATT&CK** | Provides tactic and technique context |
| **Incident Cases** | Converts significant alerts into structured cases |
| **SOC Playbooks** | Provides investigation and escalation checklists |
| **Analyst Workflow** | Stores notes, status, and verdict in the browser |
| **Dashboard** | Summarizes alerts, risk, incidents, and escalations |
| **Validation** | Automatically checks project integrity before deployment |

---

# For a Beginner

## What happens when an alert arrives?

Suppose a server reports:

> **78 failed SSH login attempts followed by a successful login.**

SentinelOps-AI can:

1. Read the alert.
2. Calculate a risk score.
3. Assign a risk level.
4. Explain why the score increased.
5. Show the related MITRE ATT&CK technique.
6. Link the alert to an incident case.
7. Provide an investigation playbook.
8. Allow the analyst to record the investigation and decision.

The goal is not to replace the analyst.

**The system organizes the evidence and workflow; the analyst makes the final determination.**

---

# How to Use It

## 1. Open the Command Center

Start from **Overview** to see:

- Total alerts
- Critical and High alerts
- Average risk
- Open incidents
- Escalations

The dashboard uses the project's demonstration dataset.

## 2. Open Alert Triage

Review the available alerts and their:

- Alert ID
- Timestamp
- Rule
- Severity
- Source IP
- Host
- User
- Event type
- MITRE mapping
- Risk score
- Risk level

## 3. Investigate an Alert

Open an alert and examine the evidence.

### SSH brute-force activity

Check:

- Source IP
- Target account
- Failed-attempt volume
- Successful authentication after failures
- Authentication history
- Whether the activity is authorized

### Network scanning

Check:

- Source IP
- Target host
- Scanned ports
- Exposed services
- Whether the scan is authorized
- Related activity

### Privilege escalation

Check:

- User account
- Privilege-related event
- Command/activity
- Authorization
- Login history
- Related suspicious activity

## 4. Review MITRE ATT&CK

Use the mapped tactic and technique to understand what type of behavior the alert represents and what related evidence should be investigated.

**A MITRE mapping provides context; it does not by itself prove that activity is malicious.**

## 5. Review the Incident

Significant alerts can be represented as incident cases containing:

- Case ID
- Linked alert
- Priority
- Risk
- Affected asset
- Source
- MITRE mapping
- Investigation guidance
- Escalation condition

## 6. Follow the Playbook

Open **Playbooks** and use the relevant SOC L1 procedure.

The playbook acts as a structured investigation checklist.

## 7. Record the Analyst Decision

The browser workflow supports:

- Analyst notes
- Case status
- Final verdict

These session changes are stored in browser **localStorage**, not a shared server database.

---

# Risk Scoring

The current browser product uses a **deterministic and explainable scoring model**.

Risk can increase based on factors such as:

- Rule level
- Alert severity
- Successful login after failed attempts
- Failed-attempt volume
- High-risk MITRE tactics
- Repeated source IP activity
- Security-relevant event type

The score is capped at **100**.

~~~text
85–100  → Critical
65–84   → High
35–64   → Medium
0–34    → Low
~~~

The score is an **analyst-support signal**, not a replacement for investigation.

---

# Architecture

## Simple View

~~~text
GitHub Repository
       ↓
GitHub Pages
       ↓
HTML + CSS + JavaScript
       ↓
Browser-side SOC workflow
       ↓
localStorage
~~~

## Detailed View

~~~text
                    SentinelOps-AI
                          │
            ┌─────────────┼─────────────┐
            ↓             ↓             ↓
       Alert Data    Risk Engine    SOC Context
            │             │             │
            └─────────────┼─────────────┘
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
                    Local Session
~~~

The repository also contains Python reference implementations for the risk-scoring and incident-generation logic.

---

# Technology

- **Frontend:** HTML, CSS, JavaScript
- **Runtime:** Browser
- **Hosting:** GitHub Pages
- **Automation:** GitHub Actions
- **Data:** JSON demonstration datasets
- **Session state:** Browser localStorage
- **Reference layer:** Python
- **Testing:** Python unittest
- **Cost:** $0 for the current GitHub-only architecture

The deployed product is intentionally browser-native. GitHub Pages provides static hosting, so the current release does not depend on a server-side Python application.

---

# Repository Structure

~~~text
SentinelOps_AI/
├── index.html
├── styles.css
├── app.js
│
├── backend/
│   └── incident_case_generator.py
│
├── ml_engine/
│   └── risk_scoring_engine.py
│
├── sample_data/
│   ├── alerts_sample.json
│   └── alerts_enriched_with_risk.json
│
├── database/
│   └── incidents_db.json
│
├── incident_playbooks/
│   └── default_soc_playbooks.json
│
├── reports/
├── learning_notes/
├── tests/
├── docs/
├── .github/workflows/
│   └── pages.yml
│
└── project_manifest.json
~~~

---

# Demo Dataset

The current demonstration environment contains three primary alert scenarios:

| Alert | Scenario | Example ATT&CK context |
|---|---|---|
| ALERT-001 | SSH brute force | T1110 — Brute Force |
| ALERT-002 | Network service scanning | T1046 — Network Service Scanning |
| ALERT-003 | Suspicious privilege escalation | T1548 — Abuse Elevation Control Mechanism |

These are **demonstration/lab cases**, not live production telemetry.

---

# Recommended Demo

For a short recruiter or technical demonstration:

~~~text
Overview
   ↓
Alert Triage
   ↓
Open ALERT-001
   ↓
Review Risk Factors
   ↓
Review MITRE Context
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

Then demonstrate the network-scan and privilege-escalation cases to show different investigation paths.

---

# Validation & Release

Every push to **main** runs the GitHub Actions validation workflow before deployment.

The validation gate checks:

- JSON contracts
- Python syntax
- Risk-score regression
- Incident-generation contracts
- Required runtime files
- Browser runtime requirements

The current main revision has passed the validation and deployment workflow.

---

# Security Boundary

Do **not** commit:

- API keys
- Passwords
- Access tokens
- Private keys
- Certificates
- Production credentials

The current repository contains demonstration/lab data.

---

# Current Scope

### Implemented

- SOC dashboard
- Alert triage
- Explainable risk scoring
- Alert investigation
- MITRE ATT&CK context
- Incident cases
- SOC L1 playbooks
- Analyst notes/status/verdict
- Browser persistence
- Automated validation
- GitHub Pages deployment

### Intentionally outside the current release

- Live SIEM ingestion
- Live Wazuh connectivity
- Persistent server-side database
- Production authentication/RBAC
- Production SOAR execution
- External threat-intelligence API dependency
- Autonomous production ML inference

These require additional infrastructure and are outside the current **$0 GitHub-only** release.

---

# Run Locally

From the repository root:

~~~bash
python -m http.server 8000
~~~

Open:

~~~text
http://localhost:8000/
~~~

For Python reference-layer tests:

~~~bash
python -m unittest discover -s tests -p "test_*.py" -v
~~~

---

# Project Status

**Current GitHub-only product baseline: complete for the defined release scope.**

The project demonstrates a complete SOC L1 workflow from:

**Alert → Risk → Investigation → Incident → Playbook → Analyst Decision**

---

## License

See [LICENSE](LICENSE).

---

## Repository

**GitHub:** [Sarma9273/sentinelops-ai-command-center](https://github.com/Sarma9273/sentinelops-ai-command-center)

**Live Demo:** [Open SentinelOps-AI Command Center](https://sarma9273.github.io/sentinelops-ai-command-center/)
