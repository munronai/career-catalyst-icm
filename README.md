# Career Catalyst — Job Application & Preparation Workspace

An agentic career transition workspace structured using the **Interpreted Context Methodology (ICM)** and visualised with **ICM CCTV**. 

It orchestrates a complete job search, role preparation, and value proposal pipeline directly through your filesystem and provides a live visual dashboard in your browser.

---

## What is ICM + CCTV?

**ICM** replaces heavy coordination frameworks with a sequential, plain-text directory structure. Instead of running multiple concurrent agent entities, **a single AI agent reads the right files at the right moment** guided by stage contracts (`CONTEXT.md`). 

**CCTV** is a glass-box visual canvas that reflects your pipeline state in real-time:
* The agent writes files to `_tv/screens/<screen>/<id>.md`.
* The server detects the write and pushes the update over a WebSocket.
* The board in your browser re-renders the cards instantly.
* Dragging cards rearranges them and saves coordinates to `_layout.json` (layout positions persist, and the agent never overwrites your layouts).
* Clicking card footers with a `source:` value allows you to **edit the real workspace output file directly from the board**—making every output literally an edit surface.
* **Interactive Checkpoints** (like selecting proposals) write responses back to `_tv/responses/<screen>/<id>.md` which the agent reads to dynamically steer the next stage.

---

## Five-Layer Routing Architecture

When you interact with the agent in this workspace, context is loaded progressively:

```
Layer 0: GEMINI.md           -> Identity, sitemap, and naming conventions (always loaded)
Layer 1: CONTEXT.md          -> Workspace task routing (loaded on entry)
Layer 2: Stage CONTEXT.md    -> Stage-specific inputs, process, and outputs (loaded per-task)
Layer 3: Reference material  -> Stable rules: profile, search config, defaults, TV skill (loaded selectively)
Layer 4: Working artifacts   -> Per-run inputs: dated reports, prep docs, TV responses (loaded selectively)
```

---

## Workspace Directory Structure

```
career-catalyst-icm/
  ├── GEMINI.md             # Layer 0: Workspace map & conventions
  ├── CONTEXT.md            # Layer 1: Workspace routing table
  ├── README.md             # This guide
  ├── _config/              # Layer 3: Your persistent settings
  │   ├── profile.md        # Your professional resume, history, and goals
  │   └── search-config.md  # Active job titles, locations, and queries
  ├── stages/
  │   ├── 01-job-search/    # Find roles and analyze initially
  │   │   ├── CONTEXT.md    # Stage 1 Contract
  │   │   ├── references/   # Default configs & templates
  │   │   └── output/       # Job search reports & seen_jobs history
  │   ├── 02-role-prep/     # Deep dive company research & interview prep
  │   │   ├── CONTEXT.md    # Stage 2 Contract
  │   │   ├── references/   # Templates or guidelines
  │   │   └── output/       # Tailored role preparation documents
  │   └── 03-proposal-builder/ # Build proof-of-value deliverables
  │       ├── CONTEXT.md    # Stage 3 Contract
  │       ├── references/   # Specifications & frameworks
  │       └── output/       # High-value pitch packages
  ├── _tv/                  # CCTV Visual dashboard files
  │   ├── screens/          # Layout grids divided by tab/screen
  │   │   ├── 01-job-search/
  │   │   ├── 02-role-prep/
  │   │   └── 03-proposal-builder/
  │   └── responses/        # Submissions from interactive cards
  ├── public/               # Static compiled web app assets
  ├── src/                  # React-free vanilla layout app source
  ├── server.js             # Asset compiler & Websocket watch server
  ├── package.json          # Node dependencies
  └── archive/              # Preserved legacy directories (backup)
```

---

## Running the Dashboard

### 1. Install Dependencies
Run npm install to pull down Tailwind CSS and watcher packages:
```bash
npm install
```

### 2. Boot the Visual Host
Start the local watcher and WebSockets server:
```bash
npm start
```
* The server runs on [http://localhost:4321](http://localhost:4321) by default. (Since port 4321 is currently in use, the dashboard is running on **[http://localhost:4322](http://localhost:4322)** in this workspace. Open [http://localhost:4322](http://localhost:4322) in your browser to view the board.)
* Click the **Style** button in the header to toggle between **Classic** (warm paper) and **Tailwind** (terminal dark console) themes.

---

## Operating the Stages

The workflow executes sequentially: **Job Search → Role Prep → Proposal Builder**.

### Stage 1: Job Search (`stages/01-job-search/`)
* **How to run**: Tell the agent: `"Run a job search"`.
* **Process**: The agent runs target queries, filters results against `seen_jobs.json`, performs match/gap analysis using `profile.md`, outputs a dated report, and writes to `seen_jobs.json`.
* **TV Dashboard**: Updates the **Search Status** card with search details and the **Latest Search Report** card summarizing the found roles (linked directly to the markdown report).

### Stage 2: Role Preparation (`stages/02-role-prep/`)
* **How to run**: Tell the agent: `"Prepare for Role 1"` or `"Research the Staff PM role at Ebury in deep-dive mode"`.
* **Process**: The agent scrapes the target listing, conducts competitive/leadership research, drafts 6-month product strategies, and compiles interviewer questions.
* **TV Dashboard**:
  * Emits active role data, reality checks, strategic bridge positioning, and questions to the **Role Prep** screen.
  * **Dynamic Checkpoint Card**: Rewrites the interactive card (`004-proposals-selection.md`) with the actual names of the generated proposals, setting its status to `blocked` on the dashboard.
* **Interactive Selection**:
  * Open the **Role Prep** tab on the dashboard.
  * You will see the **Checkpoint — select proposals to build** card displaying checkboxes for the 3 generated proposals.
  * Select 1, 2, or all 3 proposals, and click **Submit Selection**.
  * The selection is immediately saved to `_tv/responses/02-role-prep/004-proposals-selection.md`.

### Stage 3: Proposal Builder (`stages/03-proposal-builder/`)
* **How to run**: Tell the agent: `"Build the selected proposals for Ebury"`.
* **Process**: 
  1. The agent reads `_tv/responses/02-role-prep/004-proposals-selection.md` to see which proposals you checked.
  2. For each selected proposal, it executes the strict 7-phase build cycle (requirements PRD, architecture tech spec, Gherkin user stories, and multi-persona stakeholder reviews).
  3. Saves the deliverables to `stages/03-proposal-builder/output/proposals/[proposal-name]/`.
* **TV Dashboard**: Updates the **Active Proposal Build** card showing the generated proposal name(s) and updates the **Build Progress & Deliverables** card with a checklist tracking all built assets.
