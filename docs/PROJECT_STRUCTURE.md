# Project Structure

## Runtime

- `index.html` — GitHub Pages entry point
- `styles.css` — application UI
- `app.js` — browser-native application logic, scoring, navigation and local analyst state

## Research/reference logic

- `backend/incident_case_generator.py` — incident-case generation reference implementation
- `ml_engine/risk_scoring_engine.py` — deterministic risk-scoring reference implementation
- `learning_notes/` — Phase 1 development and learning notes

## SOC data

- `sample_data/alerts_sample.json` — raw demo alerts
- `sample_data/alerts_enriched_with_risk.json` — enriched Phase 1 alert artifacts
- `database/incidents_db.json` — baseline demo incident cases
- `incident_playbooks/default_soc_playbooks.json` — SOC L1 playbooks
- `reports/` — example incident reports

## Documentation

- `README.md` — product and release overview
- `docs/project_overview.md` — scope and architecture
- `docs/PHASE_STATUS.md` — release status
- `docs/PROJECT_STRUCTURE.md` — repository map
- `docs/assets/` — repository visual assets
- `project_manifest.json` — machine-readable project manifest

## Validation and deployment

- `tests/` — regression and integrity tests
- `.github/workflows/pages.yml` — validation gate and GitHub Pages deployment
- `.env.example` — non-secret template for future research/integration work; it is not used by the browser runtime
- `requirements.txt` — Python research/test dependencies

## Architectural boundary

The deployed product does not require a Python server, external database, paid API, or external hosting service.

Empty future placeholder directories are intentionally avoided. A new integration directory should be created only when that integration has an actual implementation.
