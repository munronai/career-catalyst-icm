---
id: 004-latest-report
title: Latest Search Report
type: interactive
stage: 1
source: stages/01-job-search/output/job-search-2026-06-24.md
updated: 2026-06-24T10:58:59
---
<div class="dashboard-wrapper">
  <style>
    :root {
      --bg-dark: #0f1011;
      --panel-dark: #161819;
      --border-dark: #2a2d30;
      --accent-yellow: #f1c40f;
      --text-main: #f5f6f7;
      --text-muted: #95a5a6;
      --tag-green: rgba(46, 204, 113, 0.15);
      --tag-green-text: #2ecc71;
      --tag-yellow: rgba(241, 196, 15, 0.15);
      --tag-yellow-text: #f1c40f;
      --tag-red: rgba(231, 76, 60, 0.15);
      --tag-red-text: #e74c3c;
    }
    
    body {
      margin: 0;
      padding: 0;
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      font-size: 13px;
      line-height: 1.5;
    }
    
    .dashboard-wrapper {
      padding: 12px;
      display: flex;
      flex-direction: column;
      height: calc(100vh - 24px);
      box-sizing: border-box;
    }
    
    .content-panel {
      flex: 1;
      background-color: var(--panel-dark);
      border: 1px solid var(--border-dark);
      border-radius: 8px;
      padding: 16px;
      overflow-y: auto;
      box-sizing: border-box;
    }
    
    .role-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 16px;
      border-bottom: 1px solid var(--border-dark);
      padding-bottom: 12px;
    }
    
    .role-title {
      font-size: 17px;
      font-weight: 700;
      margin: 0 0 4px 0;
      color: #fff;
    }
    
    .role-meta {
      display: flex;
      gap: 12px;
      font-size: 11.5px;
      color: var(--text-muted);
    }
    
    .meta-item strong {
      color: var(--text-main);
    }
    
    .action-btn {
      background-color: var(--accent-yellow);
      color: #000;
      border: none;
      border-radius: 4px;
      padding: 6px 12px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      transition: background-color 0.15s ease;
    }
    
    .action-btn:hover {
      background-color: #d4ac0d;
    }
    
    .grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-bottom: 16px;
    }
    
    .info-card {
      background-color: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border-dark);
      border-radius: 6px;
      padding: 12px;
    }
    
    .info-card h4 {
      margin: 0 0 8px 0;
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--accent-yellow);
    }
    
    .signals-list {
      margin: 0;
      padding-left: 16px;
    }
    
    .signals-list li {
      margin-bottom: 4px;
    }
    
    .table-container {
      margin-bottom: 16px;
      overflow-x: auto;
    }
    
    .section-title {
      font-size: 13px;
      font-weight: 700;
      margin: 16px 0 8px 0;
      color: var(--accent-yellow);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 12px;
      margin-bottom: 8px;
    }
    
    th, td {
      border: 1px solid var(--border-dark);
      padding: 8px 10px;
      text-align: left;
      vertical-align: top;
    }
    
    th {
      background-color: rgba(255, 255, 255, 0.04);
      color: #fff;
      font-weight: 600;
    }
    
    tr:nth-child(even) td {
      background-color: rgba(255, 255, 255, 0.01);
    }
    
    .pill {
      display: inline-block;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
    }
    
    .pill.strong {
      background-color: var(--tag-green);
      color: var(--tag-green-text);
    }
    
    .pill.partial {
      background-color: var(--tag-yellow);
      color: var(--tag-yellow-text);
    }
    
    .pill.usable {
      background-color: var(--tag-green);
      color: var(--tag-green-text);
    }
    
    .pill.caveat {
      background-color: var(--tag-yellow);
      color: var(--tag-yellow-text);
    }
    
    .pill.gap {
      background-color: var(--tag-red);
      color: var(--tag-red-text);
    }
    
    .flag-pill {
      background-color: var(--tag-red);
      color: var(--tag-red-text);
      padding: 2px 6px;
      border-radius: 4px;
      font-weight: 600;
      font-size: 11px;
    }
    
    #ack-msg {
      margin-top: 8px;
      font-size: 12px;
      font-weight: 600;
      color: var(--tag-green-text);
      min-height: 1.2em;
    }
  </style>

  <div class="content-panel">
    <div class="role-header">
      <div>
        <h3 class="role-title">Principal Product Manager (Agentic Platform)</h3>
        <div class="role-meta">
          <span class="meta-item">Company: <strong>Exactera</strong></span>
          <span class="meta-item">Location: <strong>Remote (London Office)</strong></span>
          <span class="meta-item">Salary: <strong>Not listed</strong></span>
          <span class="meta-item">Freshness: <strong>Confirmed (Posted 2 days ago)</strong></span>
        </div>
      </div>
      <div>
        <button class="action-btn" onclick="startPrep('exactera-principal-pm-agentic-platform')">Prep for Role</button>
      </div>
    </div>

    <div class="grid-2">
      <div class="info-card">
        <h4>Strong Signals</h4>
        <ul class="signals-list">
          <li><strong>API-first / Developer-Facing</strong>: Agentic platform interface, tool-calling, MCP</li>
          <li><strong>Infrastructure & Platforms</strong>: Data lakehouse, medallion patterns, contracts, lineage</li>
          <li><strong>AI-native Company</strong>: Building automated agent tax pipelines</li>
          <li><strong>Scale & Scope</strong>: pre-IPO startup with $100M+ funding, Principal PM scope</li>
        </ul>
      </div>
      <div class="info-card">
        <h4>Weak Signals & Flags</h4>
        <div>
          <span class="pill usable" style="background-color: var(--tag-green); color: var(--tag-green-text); font-weight: 700; text-transform: uppercase;">No Flags</span>
          <p style="margin: 6px 0 0; font-size: 11.5px; color: var(--text-muted);">Fully aligns with platform focus, remote/UK hybrid policies, and technical complexity.</p>
        </div>
      </div>
    </div>

    <div class="section-title">Matches & Gaps Analysis</div>
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th style="width: 25%">Requirement / JD Quote</th>
            <th style="width: 35%">Candidate Fit Evidence</th>
            <th style="width: 10%">Fit Level</th>
            <th style="width: 30%">Bridge Strategy / Comments</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>"10+ years in product management, with significant time on technical platform, data, or ML products."</td>
            <td>15+ years experience. Shipped SWIFT cash reporting (6 years) and Metro Bank (2.5 years) API/developer portals, KAO (9.5 years) ERP integrations.</td>
            <td><span class="pill strong">Strong</span></td>
            <td>Highlight SWIFT platform governance and Metro Bank Developer Portals.</td>
          </tr>
          <tr>
            <td>"Able to set product direction across a modern data platform... Lakehouse and medallion patterns, data contracts, quality, and lineage."</td>
            <td>Grounded in deep data schema mapping (SWIFT ISO 20022 schemas to JSON REST APIs, KAO ERP data synchronization).</td>
            <td><span class="pill partial">Partial</span></td>
            <td>Bridge by focusing on setting schema standards, data contracts, and client-side data interface models.</td>
          </tr>
          <tr>
            <td>"Strong understanding of agentic AI systems and the data access they require: retrieval, tool calling, MCP or equivalent."</td>
            <td>Conceptual and operational depth in API calling structures, OAuth security delegation, and JSON schemas.</td>
            <td><span class="pill strong">Strong</span></td>
            <td>Leverage OAuth access control models and JSON schema mapping designs.</td>
          </tr>
          <tr>
            <td>"Experience with AI systems where correctness and defensibility matter. You have worked on evaluation, guardrails, or human-in-the-loop design..."</td>
            <td>Extensive history in bank-grade, audit-logged transaction architectures under PSD2 and SWIFT.</td>
            <td><span class="pill strong">Strong</span></td>
            <td>Highlight PSD2 fallback compliance-grade security and auditable payment message designs.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="section-title">ATS Keyword Mapping</div>
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th style="width: 25%">ATS Keyword</th>
            <th style="width: 15%">Classification</th>
            <th style="width: 60%">Evidence & Framing Suggestion</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Data contracts / schemas</strong></td>
            <td><span class="pill usable">Usable</span></td>
            <td>Mapped corporate ISO 20022 data objects and managed schemas across banking counterparties at SWIFT.</td>
          </tr>
          <tr>
            <td><strong>Compliance-Grade Systems</strong></td>
            <td><span class="pill usable">Usable</span></td>
            <td>Designed audit logs and security profiles with eIDAS certificate tracking under PSD2.</td>
          </tr>
          <tr>
            <td><strong>Tool Access Guardrails</strong></td>
            <td><span class="pill usable">Usable</span></td>
            <td>Designed OAuth 2.0 / OpenID OIDC security profiles and role-based access frameworks at Metro Bank.</td>
          </tr>
          <tr>
            <td><strong>Agentic AI & LLMs</strong></td>
            <td><span class="pill caveat">Caveat</span></td>
            <td>Frame as active area of development, drawing analogies from rule engine orchestrators.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div id="ack-msg"></div>
</div>

<script>
  function startPrep(slug) {
    respond({ action: 'prep', roleSlug: slug });
  }

  window.onResponded = function(e) {
    if (e.value && e.value.action === 'prep') {
      const formatted = e.value.roleSlug.replace(/-/g, ' ');
      document.getElementById('ack-msg').innerHTML = '✓ Role prep request saved for: <strong style="text-transform: capitalize;">' + formatted + '</strong>. Let the agent know in chat to begin researching!';
    }
  };
</script>
