# Phase 1.3: Automatic Incident Case Generator

## What We Built

In this phase, we built an automatic incident case generator.

It converts important alerts into structured SOC incident cases.

## Input

- sample_data/alerts_enriched_with_risk.json

## Output

- database/incidents_db.json
- reports/INC-XXX_incident_report.md
- backend/incident_case_generator.py
- incident_playbooks/default_soc_playbooks.json

## SOC Logic

An incident case is created when:

- AI risk score is 65 or above
- Risk level is High or Critical
- Original severity is High or Critical

## Why This Matters for SOC L1

SOC L1 analysts do not only observe alerts. They must convert meaningful alerts into incidents, document evidence, follow playbooks, and escalate when required.

## Incident Case Fields

Each case contains:

- Case ID
- Linked alert ID
- Severity
- Priority
- Source IP
- Affected host
- Username
- MITRE mapping
- AI explanation
- Recommended action
- L1 investigation checklist
- Escalation condition
- Analyst notes
- Final verdict

## Key Learning

Alert is a signal.

Incident is a security event that needs investigation and response.

Not every alert becomes an incident, but every high-risk alert should be reviewed carefully.

## Generated On

2026-09-25 15:19:06

## Next Step

Phase 1.4 will build the first SOC dashboard table in Colab before moving to the web interface.
