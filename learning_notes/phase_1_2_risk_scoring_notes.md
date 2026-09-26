
# Phase 1.2: AI Risk Scoring Engine

## What We Built

We created the first AI-style risk scoring engine for SentinelOps-AI.

The engine reads SOC/SIEM alerts and adds:

- AI risk score
- AI risk level
- SOC decision
- Recommended SOC L1 action
- AI explanation
- Risk reasons

## Why This Matters

SOC L1 analysts receive many alerts. Risk scoring helps prioritize which alerts need immediate investigation or escalation.

## Risk Logic Used

The score is calculated using:

- SIEM rule level
- Alert severity
- Successful login after failed attempts
- Failed login count
- MITRE tactic
- Repeated source IP activity
- Event type

## Risk Levels

- 0 to 34: Low
- 35 to 64: Medium
- 65 to 84: High
- 85 to 100: Critical

## Important SOC Learning

Failed login attempts alone may be suspicious.

Failed login attempts followed by successful login are more dangerous because they may indicate account compromise.

## Files Created

- ml_engine/risk_scoring_engine.py
- sample_data/alerts_enriched_with_risk.json
- learning_notes/phase_1_2_risk_scoring_notes.md

Generated on: 2026-09-25 15:19:04

## Next Step

Phase 1.3 will create an automatic incident case generator.
