# Job Search Config

> This is the built-in default config. To customise it, copy this file to
> `~/job-search/search-config.md` and edit it there. Your version will be used
> automatically on every search run. Changes made via "update my search criteria"
> are saved to your copy, never to this file.

---

## Target Titles

Any of these titles qualify (exact match or close equivalent):

- Senior Product Manager
- Staff Product Manager
- Lead Product Manager
- Group Product Manager
- Principal Product Manager
- Head of Product (IC-track, not people management)

---

## Location

- Remote (UK-eligible — must be open to UK-based candidates without requiring relocation)
- London / UK-based (including hybrid)

Exclude roles that are US-only, require on-site outside the UK, or specify no-remote in a
UK context.

---

## Freshness

Only surface roles posted within the last **6 days**. Skip anything older.
If the posting date cannot be confirmed, include the role but flag it with ⚠️.

---

## Strong Signals — Prioritise

A role with 2 or more of these signals should be surfaced even if other signals are weak:

- **API-first or developer-facing** — the PM owns an API, platform, or developer experience
- **Infrastructure / transaction layer / core platform** — foundational systems, not feature-layer work
- **AI-native company** — AI is core to what the company builds, not bolted on after the fact
- **Series B or C startup** — enough scale to have real users and revenue, small enough to have real influence
- **Mission-driven or high-stakes domain** — energy transition, climate, fintech infrastructure, health, govtech
- **Technical complexity** — role requires comfort with engineering trade-offs and system design
- **API governance or standards** — PM is setting API strategy across an organisation, not just one team

---

## Weak Signals — Deprioritise (but don't exclude)

Roles with only these characteristics are less relevant but should still be included at the
bottom of the results, with a flag explaining why they're weaker:

- Pure consumer product with no developer or API surface
- Traditional retail banks as the employer (e.g. Barclays, HSBC, Lloyds, NatWest, Santander)
  → flag with: ⚠️ Traditional bank employer — may not be the right fit
- Junior or associate PM titles
- Contract or freelance roles (unless clearly senior-level and technically interesting)
- Roles with no meaningful technical component

---

## Search Query Templates

Run 8–12 searches per session. Use these as a starting point — vary angles to maximise
coverage across different job boards, ATS platforms, and company types.

### Platform / API / Infrastructure PM
```
"product manager" API platform infrastructure London OR "remote UK" [YEAR] -contract
"senior product manager" "API" OR "developer experience" OR "platform" London remote job [YEAR]
"lead product manager" "API governance" OR "API design" OR "developer platform" UK remote
site:ashbyhq.com "product manager" API platform UK remote [YEAR]
site:greenhouse.io "senior product manager" platform API London remote this week
site:lever.co "product manager" API OR developer platform UK remote posted [YEAR]
```

### AI-native / Infrastructure companies
```
"senior product manager" OR "lead PM" "AI-native" OR "AI infrastructure" London remote UK [YEAR]
"product manager" transaction infrastructure OR "core platform" UK remote job -bank [YEAR]
site:workatastartup.com "product manager" API OR platform UK remote
```

### Generalist boards
```
site:otta.com "senior product manager" London OR remote technical platform API
"lead product manager" OR "principal product manager" "remote UK" OR "London" job -junior [YEAR]
```

### Hacker News
```
site:news.ycombinator.com "who is hiring" "product manager" [CURRENT MONTH] [YEAR]
```

> `[YEAR]` and `[CURRENT MONTH]` should be substituted with the actual current values at
> search time to keep results fresh.