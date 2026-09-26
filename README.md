# SentinelOps-AI Command Center

GitHub-only, zero-cost SOC L1 Command Center prototype. GitHub is the canonical source and GitHub Pages is the runtime.

## What is implemented

- Phase 1.1 — SOC workspace and sample alerts
- Phase 1.2 — Risk scoring and alert enrichment
- Phase 1.3 — Incident case generation and SOC L1 playbooks
- Phase 1.4 — Dashboard metrics and investigation data
- Phase 1.5 — Static SOC dashboard
- **Phase 2.1 — Browser-native product shell**
  - Interactive alert triage
  - Client-side risk-score recalculation using the Phase 1 rules
  - Alert investigation view
  - Incident case view
  - Analyst notes, status and verdict stored in browser localStorage
  - Playbook and MITRE ATT&CK views
  - Responsive SOC UI
  - No Python server, external database, paid API or external hosting required

## GitHub-only architecture

```
GitHub repository
      ↓
GitHub Pages
      ↓
index.html + styles.css + app.js
      ↓
Browser-side scoring / cases / playbooks
      ↓
localStorage for analyst session state
```

The repository's Python modules remain useful as the research/reference implementation. The deployed product runtime is deliberately browser-native so the application can stay on GitHub Pages at $0.

## Run locally

```bash
python -m http.server 8000
```

Open `http://localhost:8000/`.

## Deploy

The existing `.github/workflows/pages.yml` publishes the repository through GitHub Pages on pushes to `main`.

## Important scope

This is a self-contained SOC learning/demo product, not a live SIEM. GitHub Pages cannot act as a persistent Python API, database, Wazuh manager, or real-time ingestion server. Those integrations require a separate runtime and are intentionally outside this zero-cost GitHub-only build.

## Security

Do not commit API keys, passwords, access tokens, certificates or production credentials.
