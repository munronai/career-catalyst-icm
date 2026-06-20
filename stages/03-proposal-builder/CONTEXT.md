# Stage 3: Proposal Builder

This stage builds a complete pitch/proof-of-value package for a target role, including research discovery, PRDs, strategy documents, technical architecture specs, slide decks, Gherkin user stories, and multi-persona stakeholder reviews.

## Inputs
| Source | File/Location | Section/Scope | Why |
|---|---|---|---|
| Selected Proposals Response | `../../_tv/responses/02-role-prep/004-proposals-selection.md` | Full file | The user's proposal selections submitted from the interactive card |
| Prep Report | `../02-role-prep/output/` | Prep Report | Source material for the proposals |
| Candidate Profile | `../../_config/profile.md` | Full file | Candidate details for advantage slides |
| TV Skill | `../../skill/SKILL.md` | Full file | Specification for emitting CCTV dashboard cards |

## Process
1. **Load Selected Proposals**: Read `../../_tv/responses/02-role-prep/004-proposals-selection.md` to extract the selected proposals. If the file does not exist or has empty selections, prompt the user to make a selection on the dashboard first and stop.
2. **Execute Phase Build**: For each selected proposal, execute the strict 7-phase build cycle:
   - *Phase 1: Research & Discovery*: Gather data on the target pain point (5-8 searches). Write a tabulated markdown report to `output/proposals/[proposal-name]/research/discovery_report.md`.
   - *Phase 2: Requirements & One-Pager*: Create a high-level One-Pager (`output/proposals/[proposal-name]/one-pagers/one_pager.md`) and a detailed PRD (`output/proposals/[proposal-name]/prds/prd.md`) with objectives, flows, and metrics.
   - *Phase 3: Strategy & Vision*: Create a Strategy Document (`output/proposals/[proposal-name]/strategy/strategic_alignment.md`) outlining strategic assumptions and value multipliers.
   - *Phase 4: Technical Architecture*: Write a Tech Spec (`output/proposals/[proposal-name]/technical-architecture/tech_spec.md`) with system components, API designs, and Mermaid data flows.
   - *Phase 5: Presentation Deck*: Formulate a 5-Slide slide deck (`output/proposals/[proposal-name]/presentations/deck.md`) summarizing the pitch: Hook, Problem, Solution, Architecture & Candidate Advantage, and Metrics.
   - *Phase 6: User Stories*: Generate delivery stories using Gherkin Given/When/Then format (`output/proposals/[proposal-name]/user-stories/delivery_stories.md`).
   - *Phase 7: Agent Reviews*: Simulate review feedback from Executive, Engineering, and UX Lead personas, saving reports to `output/proposals/[proposal-name]/reviews/`.
3. **Emit TV Cards**:
   - Update `../../_tv/screens/03-proposal-builder/001-active-proposal.md` displaying the active builds, status, and link.
   - Update `../../_tv/screens/03-proposal-builder/002-deliverables.md` displaying a checklist of built assets (PRD, Tech Spec, Deck, Reviews) and setting `source: stages/03-proposal-builder/output/proposals/`.

## Outputs
| Artifact | Location | Format |
|---|---|---|
| Research Summary | `output/proposals/[proposal-name]/research/discovery_report.md` | Markdown table |
| One-Pager & PRD | `output/proposals/[proposal-name]/one-pagers/` & `prds/` | Markdown files |
| Strategy & Tech Spec | `output/proposals/[proposal-name]/strategy/` & `technical-architecture/` | Markdown with diagrams |
| Presentation | `output/proposals/[proposal-name]/presentations/deck.md` | 5-slide markdown deck |
| User Stories | `output/proposals/[proposal-name]/user-stories/delivery_stories.md` | Gherkin markdown |
| Stakeholder Reviews | `output/proposals/[proposal-name]/reviews/` | Executive, Dev, UX feedback reports |
| Active Proposal Card | `../../_tv/screens/03-proposal-builder/001-active-proposal.md` | Markdown card |
| Deliverables Card | `../../_tv/screens/03-proposal-builder/002-deliverables.md` | Markdown card |
