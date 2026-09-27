# SentinelOps-AI Command Center

GitHub-only, zero-cost SOC L1 Command Center for **alert triage, explainable risk scoring, incident investigation, MITRE ATT&CK mapping, and SOC L1 playbook-driven response**.

> **Product boundary:** this is a self-contained SOC learning/demo product. It is not a live SIEM, Wazuh manager, persistent backend, or production SOAR system.

## Quick start

### Option A — Use the GitHub Pages application

Open the deployed GitHub Pages URL configured for this repository.

### Option B — Run it locally

From the repository root:

```bash
python -m http.server 8000
```

Then open:

```
http://localhost:8000/
```

No Python application server, database, API key, or paid service is required for the browser product.

---

# How to Use SentinelOps-AI

The intended workflow is **Alert → Triage → Investigate → Correlate → Incident → Playbook → Analyst Decision**.

## 1. Open the Command Center

Start on **Overview**.

Use the dashboard to understand the current demo environment:

- total alerts
- critical/high alerts
- average risk
- open incidents
- escalations
- overall SOC workload

These values come from the repository's demonstration dataset.

## 2. Go to Alert Triage

Open **Alert Triage**.

Each alert contains information such as:

- alert ID
- timestamp
- rule
- severity
- source IP
- target host
- username
- event type
- MITRE ATT&CK mapping
- risk score
- risk level

Use the alert list to decide which alert needs investigation first.

## 3. Open an alert

Select an alert to open its investigation details.

Read the evidence before making a decision.

Pay particular attention to:

- severity
- failed-attempt volume
- successful authentication after failures
- source IP repetition
- event type
- MITRE tactic and technique
- affected host/user

## 4. Understand the risk score

The application uses a **deterministic and explainable scoring model**.

Risk can increase because of:

- rule level
- severity
- successful login after failed attempts
- failed-attempt volume
- high-risk MITRE tactics
- repeated source IP activity
- security-relevant event type

The score is capped at 100.

Risk levels are:

```
85–100  → Critical
65–84   → High
35–64   → Medium
0–34    → Low
```

The score is an analyst-support signal, not a substitute for investigation.

## 5. Investigate the alert

Follow the evidence shown in the alert.

For example:

### Brute-force style alert

Check:

1. source IP
2. targeted account
3. number of failed attempts
4. whether authentication eventually succeeded
5. authentication logs
6. whether the activity is authorized
7. whether escalation is required

### Network-scan alert

Check:

1. source IP
2. target asset
3. scanned ports
4. whether the scan was authorized
5. exposed services
6. related follow-up activity

### Privilege-escalation alert

Check:

1. user account
2. privilege command/event
3. authorization
4. login source
5. authentication history
6. related suspicious activity

## 6. Use MITRE ATT&CK context

Open the MITRE ATT&CK information associated with the alert.

Use the mapping to answer:

- What tactic does this activity represent?
- What technique was detected?
- What evidence supports the mapping?
- What related activity should an L1 analyst investigate?

The MITRE mapping provides investigation context; it does not by itself prove that an incident is malicious.

## 7. Create or review the incident case

Alerts meeting the project's incident-generation conditions can be represented as incident cases.

Open **Incidents** and review:

- case ID
- linked alert
- priority
- severity
- affected host
- source
- MITRE mapping
- SOC decision
- recommended action
- investigation steps
- escalation condition

## 8. Follow the SOC L1 playbook

Open **Playbooks**.

Use the playbook corresponding to the alert type.

A playbook provides:

- investigation steps
- containment recommendation
- escalation condition

Treat the playbook as a structured checklist. Document what you actually observed rather than assuming every step is confirmed.

## 9. Record the analyst decision

Use the incident/alert workflow to document:

- analyst notes
- case status
- final verdict

The browser stores these session changes in **localStorage**.

That means:

- changes are available in the same browser profile
- they are not a shared server-side database
- clearing browser storage removes the local session state

## 10. Correlate related evidence

Do not investigate every alert in isolation.

Look for relationships such as:

```
Same source IP
      ↓
Repeated authentication failures
      ↓
Successful authentication
      ↓
Privilege-related activity
      ↓
Potential incident escalation
```

This is where the command-center workflow becomes useful for SOC L1 investigation practice.

## 11. Make the L1 decision

The expected analyst outcome is one of:

- continue investigation
- document as benign/authorized activity
- mark as a false positive when evidence supports it
- create/update an incident
- escalate according to the playbook condition

The application provides evidence and workflow structure; the analyst makes the final determination.

---

# Recommended Demo Flow

For a quick demonstration to a recruiter, trainer, or evaluator:

```
Overview
   ↓
Alert Triage
   ↓
Open ALERT-001
   ↓
Read risk factors
   ↓
Review MITRE mapping
   ↓
Open linked incident
   ↓
Open PB-001
   ↓
Review escalation condition
   ↓
Add analyst note
   ↓
Set case status/verdict
   ↓
Return to Incidents
```

Then repeat the workflow with the network-scan and privilege-escalation examples to demonstrate different investigation paths.

---

# What Is Actually Implemented

- Phase 1.1 — SOC workspace and sample alerts
- Phase 1.2 — Risk scoring and alert enrichment
- Phase 1.3 — Incident case generation and SOC L1 playbooks
- Phase 1.4 — Dashboard metrics and investigation data
- Phase 1.5 — Static SOC dashboard
- **Phase 2.1 — Browser-native product shell**
  - interactive alert triage
  - client-side risk-score recalculation
  - alert investigation
  - incident case view
  - analyst notes/status/verdict in localStorage
  - playbook and MITRE views
  - responsive SOC UI
- **Phase 2.2 — Automated release/validation hardening**
  - JSON contract validation
  - Python syntax validation
  - risk-score regression tests
  - incident-generation contract tests
  - runtime-file checks
  - validation-before-deployment workflow

---

# GitHub-only Architecture

```
GitHub Repository
       ↓
GitHub Pages
       ↓
index.html + styles.css + app.js
       ↓
Browser-side scoring / investigation / playbooks
       ↓
localStorage for analyst session state
```

The Python modules remain the research/reference implementation.

The deployed product deliberately remains browser-native so the current release can operate with a **$0 GitHub-only architecture**.

---

# Validation

Every push to `main` runs the validation gate before deployment.

It checks:

- JSON data contracts
- Python syntax
- deterministic risk-score regression
- incident-generation contracts
- required runtime files
- browser runtime requirements

The current risk model is deterministic and explainable. The earlier Colab/ML work remains the research/experimentation layer; the GitHub Pages runtime does not claim live autonomous ML inference.

---

# Security

Never commit:

- API keys
- passwords
- access tokens
- private keys
- certificates
- production credentials

The repository contains only demonstration/lab data for the current release.

---

# Scope Boundary

The current product does **not** provide:

- live SIEM ingestion
- live Wazuh connectivity
- persistent server-side incident storage
- production authentication/RBAC
- production SOAR execution
- external threat-intelligence API dependency
- autonomous production ML inference

Those are separate infrastructure capabilities and are intentionally outside the current $0 GitHub-only release.

---

# Local Development

```bash
python -m http.server 8000
```

Open `http://localhost:8000/`.

For Python reference-layer validation:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

---

# Repository Structure

```
index.html                         # GitHub Pages entry point
styles.css                         # SOC UI
app.js                             # Browser application
backend/                           # Incident-generation reference logic
ml_engine/                         # Risk-scoring reference logic
sample_data/                       # Demo alerts
database/                          # Demo incident cases
incident_playbooks/                # SOC L1 playbooks
reports/                           # Example incident reports
learning_notes/                    # Phase learning/reference notes
tests/                             # Automated validation
.github/workflows/pages.yml        # Validation + Pages deployment
docs/                              # Architecture and release documentation
project_manifest.json              # Machine-readable project status
```

---

# Release Status

**Code-level release baseline: complete.**

Remaining release actions are human-controlled:

1. perform final browser walkthrough
2. verify GitHub Pages accessibility
3. review repository visibility before public distribution

Repository visibility cannot be changed by the application itself.
