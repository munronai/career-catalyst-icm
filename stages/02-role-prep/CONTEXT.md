# Stage 2: Role Preparation

This stage researches target companies, performs role reality checks, drafts 6-month product strategies, executes Product Sense Deep Dives, outlines positioning bridges, and designs interviewer-tailored question sets.

## Inputs
| Source | File/Location | Section/Scope | Why |
|---|---|---|---|
| Selected Role / Job Listing | User Input / `../01-job-search/output/` | latest report | Target job description to prepare for |
| Candidate Profile | `../../_config/profile.md` | Full file | Profile mapping for strategic bridges and proven outcomes |
| TV Skill | `../../skill/SKILL.md` | Full file | Specification for emitting CCTV dashboard cards |

## Process
1. **Resolve Listing**: Identify target role based on user reference (number from latest report, URL, or name). If from a report, find the listing URL in the latest report under `../01-job-search/output/` and fetch the job description.
2. **Company Research**: Conduct searches based on mode:
   - *Standard*: 5-7 searches covering business model, scale, moat, and AI signals.
   - *Deep Dive*: 10-14 searches covering vision (Founder voice for startup, BU vision for enterprise), user/market sentiment (G2/App Store pain points), and technical hurdles.
3. **Role Reality Check**: Outline spend-rate (70-80% reality check), 3-6 month success metrics, trajectory, and flags.
4. **6-Month Proposals**: Generate 3 distinct proposals (opportunity, workstreams, bridge justification, success metrics, risks). Ground them in strategic priorities or sentiment friction points if in Deep Dive mode.
5. **Product Sense Deep Dive (5 Thinking Shifts)**: Produce a comprehensive hero answer:
   - *Shift 1: Strategic Context*: Connect business model to risk and competitive posture.
   - *Shift 2: Relationship Segmentation*: Segment users by capabilities (with a Markdown table).
   - *Shift 3: Architectural Distinction*: Differentiate Core vs App layers (with a Mermaid data-flow diagram).
   - *Shift 4: Trust-by-Design*: Outline data governance / security schema (with a JSON code block).
   - *Shift 5: Growth Flywheels*: Model feedback loop logic (with LaTeX equation).
6. **Candidate Strategic Bridge**: Compose resume professional summary, 3 proven strategic outcomes, and 5 technical/operational bridge bullet points.
7. **Tailored Interview Questions**: Draft 3-5 high-signal questions per interviewer type (HM, Eng, Product) with italics coaching notes.
8. **Save & Present**: Save output as a markdown file to `output/YYYY-MM-DD-[company-slug]-[role-slug].md` (with `-comprehensive` if deep dive).
9. **Emit TV Cards**:
   - Update `../../_tv/screens/02-role-prep/001-active-role.md` with active role titles, companies, and date, setting `source` to the prep report file path.
   - Update `../../_tv/screens/02-role-prep/002-reality-check.md` summarizing Step 3.
   - Update `../../_tv/screens/02-role-prep/003-strategic-bridge.md` summarizing Step 6.
   - Update `../../_tv/screens/02-role-prep/005-interview-prep.md` summarizing Step 7.
   - **Update Selection Checkpoint Card**: Rewrite `../../_tv/screens/02-role-prep/004-proposals-selection.md` to be a `type: interactive` card with `status: blocked`. Replace the placeholder proposal titles inside the HTML checkboxes with the titles of the three proposals generated in Step 4. Set the script to handle selections.

## Outputs
| Artifact | Location | Format |
|---|---|---|
| Role Prep Report | `output/YYYY-MM-DD-[company-slug]-[role-slug].md` | Markdown with metadata header |
| Active Role Card | `../../_tv/screens/02-role-prep/001-active-role.md` | Markdown card |
| Reality Check Card | `../../_tv/screens/02-role-prep/002-reality-check.md` | Markdown card |
| Bridge Card | `../../_tv/screens/02-role-prep/003-strategic-bridge.md` | Markdown card |
| Proposal Selection Card | `../../_tv/screens/02-role-prep/004-proposals-selection.md` | Interactive card (HTML snippet) |
| Interview Prep Card | `../../_tv/screens/02-role-prep/005-interview-prep.md` | Markdown card |
