---
id: 004-latest-report
title: Latest Search Report
type: interactive
stage: 1
source: stages/01-job-search/output/job-search-2026-06-20.md
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
      border-b: 1px solid var(--border-dark);
      margin-bottom: 12px;
      gap: 4px;
      shrink-0: 0;
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
    
    .tab-btn:hover {
      color: var(--text-main);
      background-color: rgba(255, 255, 255, 0.03);
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
      font-size: 18px;
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
    <button class="tab-btn active" id="btn-0" onclick="showTab(0)">Cint — Supply API</button>
    <button class="tab-btn" id="btn-1" onclick="showTab(1)">Ebury — API Connectivity</button>
    <button class="tab-btn" id="btn-2" onclick="showTab(2)">Ebury — API Platform</button>
  </div>

  <!-- TAB 0: Cint -->
  <div class="content-panel" id="panel-0">
    <div class="role-header">
      <div>
        <h3 class="role-title">Senior Product Manager – Supply API</h3>
        <div class="role-meta">
          <span class="meta-item">Company: <strong>Cint</strong></span>
          <span class="meta-item">Location: <strong>Remote (UK)</strong></span>
          <span class="meta-item">Salary: <strong>£100k–£120k GBP (est.)</strong></span>
          <span class="meta-item">Freshness: <strong>Confirmed (within 6 days)</strong></span>
        </div>
      </div>
      <div>
        <button class="action-btn" onclick="startPrep('cint-senior-pm-supply-api')">Prep for Role</button>
      </div>
    </div>

    <div class="grid-2">
      <div class="info-card">
        <h4>Strong Signals</h4>
        <ul class="signals-list">
          <li><strong>API-first / Developer-Facing</strong>: Directly owns programmatic Exchange supply APIs</li>
          <li><strong>Infrastructure layer</strong>: Manages high-throughput marketplace integration</li>
          <li><strong>Technical complexity</strong>: High-density API design, versioning policy, developer SDK/sandboxes</li>
          <li><strong>Way of Working</strong>: True remote-first UK alignment</li>
        </ul>
      </div>
      <div class="info-card">
        <h4>Weak Signals & Flags</h4>
        <p style="margin: 0; color: var(--text-muted);">None detected. This role matches all filters and way-of-working criteria perfectly.</p>
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
            <td>"Deep understanding of API design principles, versioning, change management, developer contracts"</td>
            <td>Run SWIFT external API design governance, structuring standards across multiple product divisions.</td>
            <td><span class="pill strong">Strong</span></td>
            <td>Focus on governance over massive enterprise surfaces and API lifecycle frameworks.</td>
          </tr>
          <tr>
            <td>"Proven experience in managing full Developer Experience (DX): sandbox, documentation, integration tools"</td>
            <td>Outlined vision and managed supplier delivery for Metro Bank’s Open Banking developer portal and sandboxes.</td>
            <td><span class="pill strong">Strong</span></td>
            <td>Highlight user-centered design approach applied to sandboxes and developer portals.</td>
          </tr>
          <tr>
            <td>"Hands-on software engineering experience is strongly preferred"</td>
            <td>Twice certified Apigee engineer. Line-managed developers, managed CI/CD build scripts (gulp/Jenkins), but did not write production backend code.</td>
            <td><span class="pill partial">Partial</span></td>
            <td>Bridge by showing deep technical fluency in API gateway architecture, DevOps automation, and BDD test design.</td>
          </tr>
          <tr>
            <td>"Experience in ResTech, AdTech, or other programmatic marketplaces is a plus"</td>
            <td>Worked on high-scale international payments infrastructure (SWIFT) and Open Banking specs (Metro Bank).</td>
            <td><span class="pill partial">Partial</span></td>
            <td>Highlight structural similarities between high-throughput financial clearance queues and programmatic marketplaces.</td>
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
            <td><strong>API Design & Versioning</strong></td>
            <td><span class="pill usable">Usable</span></td>
            <td>Directly ran design governance at SWIFT, setting standards for multi-bank APIs.</td>
          </tr>
          <tr>
            <td><strong>Developer Experience (DX)</strong></td>
            <td><span class="pill usable">Usable</span></td>
            <td>Delivered developer portals and sandboxes at both Metro Bank and SWIFT.</td>
          </tr>
          <tr>
            <td><strong>Software Engineering</strong></td>
            <td><span class="pill caveat">Caveat</span></td>
            <td>Frame as a technical-first PM with architecture certifications (Apigee) and script automation knowledge.</td>
          </tr>
          <tr>
            <td><strong>Programmatic Exchange</strong></td>
            <td><span class="pill caveat">Caveat</span></td>
            <td>Draw parallels to high-volume transaction routing and ledger settlement networks at SWIFT.</td>
          </tr>
          <tr>
            <td><strong>B2B Product Management</strong></td>
            <td><span class="pill usable">Usable</span></td>
            <td>Managed corporate treasury pilot programs and partner-vendor integrations.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- TAB 1: Ebury Staff PM -->
  <div class="content-panel" id="panel-1" style="display:none">
    <div class="role-header">
      <div>
        <h3 class="role-title">Staff Product Manager – API Connectivity</h3>
        <div class="role-meta">
          <span class="meta-item">Company: <strong>Ebury</strong></span>
          <span class="meta-item">Location: <strong>London (Hybrid)</strong></span>
          <span class="meta-item">Salary: <strong>£110k–£120k GBP (est.)</strong></span>
          <span class="meta-item">Freshness: <strong>Confirmed (within 6 days)</strong></span>
        </div>
      </div>
      <div>
        <button class="action-btn" onclick="startPrep('ebury-staff-pm-api-connectivity')">Prep for Role</button>
      </div>
    </div>

    <div class="grid-2">
      <div class="info-card">
        <h4>Strong Signals</h4>
        <ul class="signals-list">
          <li><strong>API-first / Developer-Facing</strong>: ERP and accounting connectivity domain</li>
          <li><strong>Infrastructure layer</strong>: Ebury global financial core rails</li>
          <li><strong>Technical complexity</strong>: Sync patterns, OAuth, webhooks, reconciliation structures</li>
          <li><strong>Domain alignment</strong>: Direct fintech/payments ecosystem match</li>
        </ul>
      </div>
      <div class="info-card">
        <h4>Weak Signals & Flags</h4>
        <div>
          <span class="flag-pill">⚠️ Hybrid Working Model</span>
          <p style="margin: 6px 0 0; font-size: 11.5px; color: var(--text-muted);">Requires 4 days in-office in London. This is a significant variance from the remote-first preference in configuration.</p>
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
            <td>"Define vision, roadmap, and metrics for ERP connectivity... make build vs. buy decisions"</td>
            <td>Led corporate cash reporting API pilots at SWIFT, structuring partner vendor integrations and roadmap.</td>
            <td><span class="pill strong">Strong</span></td>
            <td>Position SWIFT's corporate-to-bank channel as a massive multi-bank integration project.</td>
          </tr>
          <tr>
            <td>"Translate business requirements to clear technical API specs... work with backend engineering"</td>
            <td>18+ years translating payment specs (ISO 20022 and PSD2) into developer endpoints and gateway code.</td>
            <td><span class="pill strong">Strong</span></td>
            <td>Point to experience bridging bank architectures with practical developer APIs.</td>
          </tr>
          <tr>
            <td>"Experience with ERP/accounting software (Codat, Merge, Apideck, Sage, QuickBooks, NetSuite)"</td>
            <td>Enterprise integration patterns (SAP integration with retail/e-commerce) at KAO UK / Molton Brown.</td>
            <td><span class="pill partial">Partial</span></td>
            <td>Frame SWIFT and PSD2 endpoints as financial data mappings structurally identical to ERP formats.</td>
          </tr>
          <tr>
            <td>"Familiarity with OAuth, webhooks, data sync models, reconciliation processes"</td>
            <td>Delivered Open Banking OAuth/OpenID Hybrid Flow profiles at Metro Bank. cash reporting APIs at SWIFT.</td>
            <td><span class="pill strong">Strong</span></td>
            <td>Demonstrate absolute competence in payment security standards and ledger sync workflows.</td>
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
            <td><strong>ERP Integration</strong></td>
            <td><span class="pill usable">Usable</span></td>
            <td>Integrated retail/SAP ERPs during brand consolidation at KAO UK.</td>
          </tr>
          <tr>
            <td><strong>API Specifications</strong></td>
            <td><span class="pill usable">Usable</span></td>
            <td>Authored Open Banking specs at Metro Bank and API designs at SWIFT.</td>
          </tr>
          <tr>
            <td><strong>OAuth</strong></td>
            <td><span class="pill usable">Usable</span></td>
            <td>Delivered PSD2 security profiling with OAuth 2.0 at Metro Bank.</td>
          </tr>
          <tr>
            <td><strong>Codat / Merge / Apideck</strong></td>
            <td><span class="pill caveat">Caveat</span></td>
            <td>Frame multi-bank integration channels as similar programmatic aggregation patterns.</td>
          </tr>
          <tr>
            <td><strong>Fintech / Payments</strong></td>
            <td><span class="pill usable">Usable</span></td>
            <td>Direct career depth across SWIFT network and regulated UK open banking systems.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- TAB 2: Ebury Senior PM -->
  <div class="content-panel" id="panel-2" style="display:none">
    <div class="role-header">
      <div>
        <h3 class="role-title">Senior Product Manager – API Platform</h3>
        <div class="role-meta">
          <span class="meta-item">Company: <strong>Ebury</strong></span>
          <span class="meta-item">Location: <strong>London (Hybrid)</strong></span>
          <span class="meta-item">Salary: <strong>£110k–£120k GBP (est.)</strong></span>
          <span class="meta-item">Freshness: <strong>Confirmed (within 6 days)</strong></span>
        </div>
      </div>
      <div>
        <button class="action-btn" onclick="startPrep('ebury-senior-pm-api-platform')">Prep for Role</button>
      </div>
    </div>

    <div class="grid-2">
      <div class="info-card">
        <h4>Strong Signals</h4>
        <ul class="signals-list">
          <li><strong>API-first / Developer-Facing</strong>: Evolving Ebury core API platform and endpoints</li>
          <li><strong>Infrastructure layer</strong>: Ebury core payments routing, gateway architecture</li>
          <li><strong>Technical complexity</strong>: REST/GraphQL, OAuth, webhooks, retries, idempotency</li>
          <li><strong>Domain alignment</strong>: Direct fintech/payments domain match</li>
        </ul>
      </div>
      <div class="info-card">
        <h4>Weak Signals & Flags</h4>
        <div>
          <span class="flag-pill">⚠️ Hybrid Working Model</span>
          <p style="margin: 6px 0 0; font-size: 11.5px; color: var(--text-muted);">Requires 4 days in-office in London. This is a significant variance from the remote-first preference in configuration.</p>
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
            <td>"Define and evolve API endpoints, webhooks, error models, and data contracts to ensure consistency and ease of integration"</td>
            <td>Established and ran API design governance across all SWIFT external API interfaces. Designed Metro Bank’s API operating model.</td>
            <td><span class="pill strong">Strong</span></td>
            <td>Highlight governance framework and developer portals designed to standardize API quality.</td>
          </tr>
          <tr>
            <td>"Partner with engineering teams on API design, best practices, authentication flows, and technical trade-offs (e.g. retries, idempotency)"</td>
            <td>Line managed 6 developers. Twice certified on Google Cloud/Apigee API Gateways. Managed route-to-live and controls.</td>
            <td><span class="pill strong">Strong</span></td>
            <td>Position Apigee gateway certifications and technical controls (rate limits, security tokens) as evidence of platform depth.</td>
          </tr>
          <tr>
            <td>"OAuth 2.0, API keys, authentication models, event-driven systems"</td>
            <td>Delivered Metro Bank’s Open Banking security infrastructure using OAuth and OpenID Hybrid Flow with eIDAS.</td>
            <td><span class="pill strong">Strong</span></td>
            <td>Showcase deep expertise in authorization models for highly-secured financial services.</td>
          </tr>
          <tr>
            <td>"Previous experience in fintech, payments, FX, or financial infrastructure is highly desirable"</td>
            <td>8+ years at SWIFT and Metro Bank delivering cash reporting, trade finance, and Open Banking APIs.</td>
            <td><span class="pill strong">Strong</span></td>
            <td>Direct fintech/financial infrastructure match matching payments and clearing systems.</td>
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
            <td><strong>API Platform / Gateway</strong></td>
            <td><span class="pill usable">Usable</span></td>
            <td>Apigee certified. Ran selection and implementation of Apigee at Metro Bank and KAO.</td>
          </tr>
          <tr>
            <td><strong>API Design & Governance</strong></td>
            <td><span class="pill usable">Usable</span></td>
            <td>Led governance boards and API design reviews across all SWIFT product APIs.</td>
          </tr>
          <tr>
            <td><strong>OAuth 2.0 / Security</strong></td>
            <td><span class="pill usable">Usable</span></td>
            <td>Designed and delivered secure authorization flow patterns for Open Banking v1 at Metro Bank.</td>
          </tr>
          <tr>
            <td><strong>Developer Experience (DX)</strong></td>
            <td><span class="pill usable">Usable</span></td>
            <td>Built developer portal and sandbox infrastructure for SWIFT and Metro Bank.</td>
          </tr>
          <tr>
            <td><strong>Technical Trade-offs</strong></td>
            <td><span class="pill usable">Usable</span></td>
            <td>Evaluated traffic-routing, retries, and API gateway logic in collaboration with engineers.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div id="ack-msg"></div>
</div>

<script>
  function showTab(index) {
    // Hide all panels
    document.getElementById('panel-0').style.display = 'none';
    document.getElementById('panel-1').style.display = 'none';
    document.getElementById('panel-2').style.display = 'none';
    
    // Deactivate all buttons
    document.getElementById('btn-0').classList.remove('active');
    document.getElementById('btn-1').classList.remove('active');
    document.getElementById('btn-2').classList.remove('active');
    
    // Activate clicked tab
    document.getElementById('panel-' + index).style.display = 'block';
    document.getElementById('btn-' + index).classList.add('active');
    
    // Clear ACK
    document.getElementById('ack-msg').textContent = '';
  }

  function startPrep(slug) {
    // Call the parent layout respond function to trigger Role Prep selection
    respond({ action: 'prep', roleSlug: slug });
  }

  // Handle callback when response is acknowledged
  window.onResponded = function(e) {
    if (e.value && e.value.action === 'prep') {
      const formatted = e.value.roleSlug.replace(/-/g, ' ');
      document.getElementById('ack-msg').innerHTML = '✓ Role prep request saved for: <strong style="text-transform: capitalize;">' + formatted + '</strong>. Let the agent know in chat to begin researching!';
    }
  };
</script>
