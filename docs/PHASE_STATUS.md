# SentinelOps-AI Release Status

## Completed

| Phase | Scope | Status |
|---|---|---|
| 1.1 | Project workspace and sample alerts | Completed |
| 1.2 | Risk scoring and alert enrichment | Completed |
| 1.3 | Incident case generation and SOC L1 playbooks | Completed |
| 1.4 | Dashboard metrics and investigation data | Completed |
| 1.5 | Static SOC web dashboard | Completed |
| 2.1 | Browser-native GitHub product shell | Completed |
| 2.2 | Automated validation and release hardening | Completed |

## Current release definition

The current product is a **GitHub-only, $0, browser-native SOC L1 learning/demo application**.

The deployed runtime uses:

- GitHub Pages
- HTML/CSS/JavaScript
- repository JSON data
- deterministic client-side risk scoring
- browser localStorage for analyst session changes

The Python modules remain the research/reference layer.

## Verified release controls

- JSON contracts are parsed in CI.
- Python files are syntax-compiled in CI.
- Risk-score regression values are tested.
- Incident-generation contracts are tested.
- Required runtime files are checked before deployment.
- Browser-side runtime dependencies are local to the repository.
- No production credentials are intended to be stored in the repository.
- The application explicitly identifies itself as browser-native rather than a live SIEM.

## Out of scope for this release

Live SIEM ingestion, Wazuh server connectivity, persistent backend APIs, production authentication/RBAC, external threat-intelligence services, and automated SOAR actions are not part of the current release.

Colab remains an external experimentation/research environment and is not required to run the GitHub Pages product.
