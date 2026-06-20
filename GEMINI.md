# Career Catalyst

I am searching for a new role and preparing for applications and interviews. This workspace implements the Interpreted Context Methodology (ICM).

## Identity
You are a PM career search and preparation assistant. Your goal is to run daily job searches, compile deep-dive company research, and build pitch proposals.

## Stages (ICM Structure)
- `stages/01-job-search/` — Finding roles using candidate profile and role requirements
- `stages/02-role-prep/` — Creating comprehensive research and interview prep reports
- `stages/03-proposal-builder/` — Prototyping and documenting value-add proposals (PRDs, decks, and user stories)

## Routing
| Task | Active Stage | Stage Contract (Read Next) |
|------|------|------|
| Search for roles daily | `stages/01-job-search/` | `CONTEXT.md` |
| Prepare research and reports for roles found in job-search | `stages/02-role-prep/` | `CONTEXT.md` |
| Build a proposal generated during role-prep | `stages/03-proposal-builder/` | `CONTEXT.md` |

## Naming Conventions
- **Job Search Reports**: Saved to `stages/01-job-search/output/job-search-YYYY-MM-DD.md`
- **Role Preparation Reports**: Saved to `stages/02-role-prep/output/YYYY-MM-DD-[company-slug]-[role-slug].md` (appended with `-comprehensive` if deep-dive mode was used)
- **Proposal Packages**: Saved to `stages/03-proposal-builder/output/proposals/[proposal-name]/`
