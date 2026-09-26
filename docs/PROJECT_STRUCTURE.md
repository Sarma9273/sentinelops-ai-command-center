# Project Structure

## Core application

- `backend/` — incident-case generation logic
- `ml_engine/` — risk scoring engine
- `index.html` — current GitHub Pages entry point

## SOC data and artifacts

- `sample_data/` — sample and enriched alerts
- `database/` — demo incident database
- `incident_playbooks/` — SOC L1 playbooks
- `reports/` — example incident reports

## Documentation

- `docs/project_overview.md` — project purpose and scope
- `docs/PHASE_STATUS.md` — completed Phase 1 status
- `docs/PROJECT_STRUCTURE.md` — repository organization
- `docs/assets/` — repository visual assets
- `learning_notes/` — phase development notes

## Development

- `tests/` — validation tests
- `.github/workflows/` — GitHub Pages deployment
- `requirements.txt` — Python dependencies

Empty future placeholder directories were intentionally removed. New Wazuh, SOAR, notebook, screenshot and other integration directories should be created only when their implementation is actually started.
