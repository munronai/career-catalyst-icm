# Stage 1: Job Search

This stage performs a daily search for PM roles, deduplicates against previous searches, filters against criteria, performs initial candidate fit analysis, maps ATS keywords, and saves dated reports.

## Inputs
| Source | File/Location | Section/Scope | Why |
|---|---|---|---|
| Active Configuration | `../../_config/search-config.md` | Full file | Active titles, locations, signals, and queries (fallback to `references/default-search-config.md` if missing) |
| Candidate Profile | `../../_config/profile.md` | Full file | Grounding for match/gap analysis and keyword mapping (skip analysis if missing) |
| History / Seen Jobs | `output/seen_jobs.json` | Full file | Deduplication tracking (creates `[]` if missing) |
| TV Skill | `../../skill/SKILL.md` | Full file | Specification for emitting CCTV dashboard cards |

## Process
1. **Load Configuration**: Read `../../_config/search-config.md`. If it does not exist, use `references/default-search-config.md` (do not mention fallback to user).
2. **Load Seen Jobs**: Read `output/seen_jobs.json`. If missing, initialise as empty array `[]`.
3. **Load Profile**: Read `../../_config/profile.md`. If missing, output a warning at the top and skip steps 6 and 7.
4. **Run Searches**: Run 8–12 high-signal web searches using the active query templates (substitute `[YEAR]` and `[CURRENT MONTH]`).
5. **Deduplicate & Validate (Batch)**:
   - Apply company-level skipping (skip if company is in `seen_jobs.json`).
   - Filter search result snippets to discard aggregators, expired, or non-PM roles.
   - Batch fetch the final target URLs of remaining roles using `web_fetch` or `read_browser_page`.
   - Discard invalid, 404, or filled roles, and apply deduplication on final URL.
   - Score the remaining roles against strong and weak signals from configuration.
6. **Match/Gap Analysis**:
   - Compare the full job description against the candidate profile.
   - Generate a `✅ Matches & ⚠️ Gaps Table` comparing specific JD quotes to evidence/bridge strategies from the profile.
7. **ATS Keyword Mapping**:
   - Extract high-signal ATS keywords from the JD.
   - Map each to the profile: classify as Usable (`✅`), Usable with Caveat (`〰️`), or Not Usable (`❌`) with actionable, truthful reframing suggestions.
8. **Present Results**:
   - Format and output new jobs in chat, sorted from strongest to weakest fit. Include direct URLs, compensation, signals, match/gap tables, and keyword mapping tables.
9. **Save Report**:
   - Write the identical output to `output/job-search-YYYY-MM-DD.md` (using current date).
   - If a report for today already exists, append new results separated by a `---` divider and a timestamp.
10. **Update History**:
    - Save new jobs to `output/seen_jobs.json` with fields: `url`, `company`, `title`, and `last_searched`.
11. **Emit TV Cards**:
    - Update `../../_tv/screens/01-job-search/002-search-status.md` with the updated search stats, last run date, and seen jobs count. Set `status: done`.
    - Update `../../_tv/screens/01-job-search/004-latest-report.md` with a summary of the newly found jobs, and set `source: stages/01-job-search/output/job-search-YYYY-MM-DD.md`.

## User Commands
- **Run search**: (As described in the Process)
- **Show search criteria**: Load `../../_config/search-config.md` (or fallback to defaults). Display contents, and ask if any changes are wanted.
- **Update search criteria**: Modify `../../_config/search-config.md` based on user input (creating it by copying defaults if it doesn't exist), then confirm update.

## Outputs
| Artifact | Location | Format |
|---|---|---|
| Job Search Report | `output/job-search-YYYY-MM-DD.md` | Markdown with metadata header |
| Updated History | `output/seen_jobs.json` | JSON array of objects |
| Status Card | `../../_tv/screens/01-job-search/002-search-status.md` | Markdown card |
| Latest Report Card | `../../_tv/screens/01-job-search/004-latest-report.md` | Markdown card |
