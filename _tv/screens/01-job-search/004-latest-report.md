---
id: 004-latest-report
title: Latest Search Report
type: interactive
stage: 1
source: stages/01-job-search/output/job-search-2026-06-23.md
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
    
    .tab-bar {
      display: flex;
      border-bottom: 1px solid var(--border-dark);
      margin-bottom: 12px;
      gap: 4px;
      flex-shrink: 0;
    }
    
    .tab-btn {
      background: transparent;
      border: 1px solid transparent;
      border-bottom: none;
      color: var(--text-muted);
      padding: 8px 16px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      border-radius: 6px 6px 0 0;
      transition: all 0.15s ease;
    }
    
    .tab-btn.active {
      color: var(--accent-yellow);
      background-color: var(--panel-dark);
      border-color: var(--border-dark);
      border-bottom: 1px solid var(--panel-dark);
      margin-bottom: -1px;
    }
    
    .content-panel {
      flex: 1;
      background-color: var(--panel-dark);
      border: 1px solid var(--border-dark);
      border-radius: 0 0 8px 8px;
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

  <div class="tab-bar">
    <button class="tab-btn active" id="btn-0">Experian — CrossCore</button>
  </div>

  <!-- TAB 0: Experian CrossCore -->
  <div class="content-panel" id="panel-0">
    <div class="role-header">
      <div>
        <h3 class="role-title">Senior Platform Product Manager – CrossCore</h3>
        <div class="role-meta">
          <span class="meta-item">Company: <strong>Experian</strong></span>
          <span class="meta-item">Location: <strong>London, UK (Hybrid)</strong></span>
          <span class="meta-item">Salary: <strong>£95k–£120k GBP (est.)</strong></span>
          <span class="meta-item">Freshness: <strong>Confirmed (within 6 days)</strong></span>
        </div>
      </div>
      <div>
        <button class="action-btn" onclick="startPrep('experian-senior-platform-pm-crosscore')">Prep for Role</button>
      </div>
    </div>

    <div class="grid-2">
      <div class="info-card">
        <h4>Strong Signals</h4>
        <ul class="signals-list">
          <li><strong>API-first / Developer-Facing</strong>: API-led identity and fraud solutions</li>
          <li><strong>Technical complexity</strong>: Third-party system integrations & workflow engine</li>
          <li><strong>Infrastructure layer</strong>: CrossCore core verification platform</li>
          <li><strong>Domain alignment</strong>: Direct fintech/identity/fraud ecosystem match</li>
        </ul>
      </div>
      <div class="info-card">
        <h4>Weak Signals & Flags</h4>
        <div>
          <span class="flag-pill">⚠️ Hybrid Working Model</span>
          <p style="margin: 6px 0 0; font-size: 11.5px; color: var(--text-muted);">Requires consistent London office presence (deviates from preferred remote-first work model).</p>
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
            <td>"Manage API products and integrated services that utilize workflows on the CrossCore platform"</td>
            <td>Managed external API gateway (Apigee) and API design governance across all SWIFT and Metro Bank external APIs.</td>
            <td><span class="pill strong">Strong</span></td>
            <td>Showcase deep technical expertise in API gateways, caching, rate-limiting, and lifecycle management.</td>
          </tr>
          <tr>
            <td>"Identify, evaluate, and prioritize integration opportunities with third-party systems, onboard new partners"</td>
            <td>Ran SWIFT partner API approvals and corporate cash reporting pilot onboarding processes for TMS vendors.</td>
            <td><span class="pill strong">Strong</span></td>
            <td>Highlight partner-relations, vendor/supplier management, and developer experience onboarding strategies.</td>
          </tr>
          <tr>
            <td>"Manage API-led identity and fraud solutions"</td>
            <td>Implemented Open Banking security profiles using OAuth and OpenID Hybrid Flow with eIDAS certificates for client verification.</td>
            <td><span class="pill partial">Partial</span></td>
            <td>Bridge by focusing on identity authentication, audit logs, and tracking scraping traffic patterns.</td>
          </tr>
          <tr>
            <td>"Apply Agile project management practices and align with PLM process"</td>
            <td>Line-managed 6 API developers leading delivery through Scrum and a DevOps-style automated testing approach.</td>
            <td><span class="pill strong">Strong</span></td>
            <td>Point to team leadership and DevOps deployment automation frameworks.</td>
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
            <td><strong>API Platform & Integrations</strong></td>
            <td><span class="pill usable">Usable</span></td>
            <td>Owned Apigee API platform and third-party partner integrations at Metro Bank, KAO, and SWIFT.</td>
          </tr>
          <tr>
            <td><strong>Identity & Fraud (ID&F)</strong></td>
            <td><span class="pill caveat">Caveat</span></td>
            <td>Connect security API deployments (OAuth, OpenID) and identity certificate validation frameworks.</td>
          </tr>
          <tr>
            <td><strong>Agile & PLM</strong></td>
            <td><span class="pill usable">Usable</span></td>
            <td>Led Scrum development teams and automated CI/CD routes-to-live.</td>
          </tr>
          <tr>
            <td><strong>Customer Discovery</strong></td>
            <td><span class="pill usable">Usable</span></td>
            <td>Handled pilot programs, webinars, presented panels (Sibos), and ran customer working groups.</td>
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
