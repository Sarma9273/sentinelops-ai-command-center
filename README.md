# SentinelOps-AI Command Center

AI-assisted SOC L1 command-center project. This repository is the canonical development source for the application.

## Phase 1 implemented

- Phase 1.1 — Project workspace and sample SOC alerts
- Phase 1.2 — AI risk scoring and alert enrichment
- Phase 1.3 — Automatic incident case generation and SOC playbooks
- Phase 1.4 — SOC dashboard data, metrics, tables and charts
- Phase 1.5 — Static SOC web dashboard

## Current capabilities

- Sample SOC/SIEM alerts
- Risk scoring and risk-level classification
- SOC decision and recommended-action generation
- MITRE ATT&CK mapping fields
- Automatic incident case generation
- SOC L1 investigation playbooks
- Incident reports
- Static browser SOC dashboard
- Mobile-responsive dashboard layout

## Repository structure

```text
.
├── .github/workflows/       # GitHub Pages deployment
├── backend/                 # Incident-case generation logic
├── ml_engine/               # Risk scoring engine
├── sample_data/             # Sample and enriched alerts
├── database/                # Demo incident data
├── incident_playbooks/      # SOC L1 playbooks
├── reports/                 # Example generated incident reports
├── docs/                    # Project documentation
├── learning_notes/          # Phase-by-phase development notes
├── tests/                   # Validation tests
├── index.html               # GitHub Pages entry point
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── requirements.txt
└── project_manifest.json
```

## Run locally

```bash
python -m http.server 8000
```

Open `http://localhost:8000/`.

## GitHub Pages

The root `index.html` is the current static demonstration entry point. GitHub Actions publishes it through `.github/workflows/pages.yml`.

## Development direction

GitHub is the canonical source for application development. Google Colab is retained outside this repository for experimentation and research when required. The next application phase should extend the backend, API, frontend and integrations from this repository.

## Security

Never commit API keys, passwords, access tokens, certificates, or production credentials. Use local `.env` files and keep only non-secret configuration in `.env.example`.
