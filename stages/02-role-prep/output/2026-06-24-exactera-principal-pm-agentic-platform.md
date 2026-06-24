---
company: Exactera
role: Principal Product Manager (Agentic Platform)
date: 2026-06-24
mode: standard
status: complete
---

# Role Preparation Report: Principal Product Manager (Agentic Platform) (Exactera)

## 1. Company Intelligence & Context

### Business Model & Scale
Exactera is a pre-IPO FinTech SaaS company founded in 2016. Backed by Savant Venture Fund and Insight Partners with over **$100 million in funding**, Exactera serves global multinational enterprises by automating high-stakes corporate tax compliance, including transfer pricing, R&D tax credits, and audit defense. The business model is transactional and SaaS subscription-based, transitioning from software-and-services to a fully automated, AI-native platform model.

### Moat & Strategy
*   **The Compliance Defensibility Moat**: Regulated tax work must be audit-ready and jurisdiction-compliant. Exactera builds highly specialized, domain-specific AI engines (like **ExactMatch** for transfer pricing comparable searches and **ExactReport** for automated Word report generation) that output compliant tax documentation.
*   **AI-Native Transformation**: Moving to an "Agentic Platform" where autonomous AI agents ingest client financial ledgers, query external regulatory data, and generate compliance-grade reports under practitioner supervision.
*   **Modern Data Substrate**: Grounding agent workflows in a unified data lakehouse (utilizing Databricks/Delta Lake medallion architectures) to ensure auditable data lineage and data quality.

### AI Integration & Platform Velocity
*   **Agentic Access Surface**: Implementing Model Context Protocol (MCP) or equivalent interfaces to let agents query databases, use tools, and call external APIs securely.
*   **Human-in-the-Loop (HITL)**: Designing guardrails and deterministic evaluation loops to keep tax professionals in control when resolving ambiguous tax code matches.

---

## 2. Role Reality Check

### Spend-Rate (70-80% Reality Check)
*   **45% Data Infrastructure & Contract Governance**: Setting and enforcing data contracts (schemas, quality, lineage) on the Databricks lakehouse between data producers and downstream AI consumers.
*   **35% Agentic Scoping & Guardrail Engineering**: Designing the access rules, MCP tool definitions, and validation guardrails that constrain AI agents from retrieving unauthorized client PII.
*   **10% Practitioner Alignment & UX**: Collaborating with internal tax consultants and external corporate tax leaders to design deterministic checkpoints that ensure tax audit defensibility.

### Success Metrics (3-6 Months)
1.  **Enforce Lakehouse Data Contracts**: Define and implement data contracts for **3 core external data sources** (SEC filings, global tax databases) by month 3.
2.  **Define Compliance Guardrail Bar**: Standardize the evaluation protocol for deterministic AI outputs, reducing draft error rates by **35%**.
3.  **Onboard Agentic Workflows**: Lower the onboarding time for custom practitioner tool integrations from weeks to **under 3 days**.

### Flags worth noting
*   **High-Stakes Legal Liability**: Errors in transfer pricing or R&D tax calculations can trigger audits and multi-million dollar penalties. Model hallucination has immediate financial consequences.
*   **Medallion Adoption Friction**: Transitioning traditional tax practitioners to trust automated AI agents requires exceptional human-in-the-loop UX clarity.

---

## 3. Three 6-Month Proposals

### Proposal 1: Compliance-Grade Deterministic Guardrail Framework
*   **The opportunity**: AI agents running tax analyses (such as matching client ledgers to R&D credit criteria) can hallucinate, violating local jurisdiction compliance.
*   **What you'd do**:
    1.  Design a declarative policy engine that checks agent outputs against a hardcoded database of jurisdiction-specific rules.
    2.  Implement mandatory human-in-the-loop (HITL) triggers for any matching confidence score below 95%.
    3.  Create an automated audit trail logging the prompt, model weights, source ledger chunk, and practitioner approval.
*   **Why you're well-placed to lead this**: Candidate built Metro Bank's regulatory fallback and PSD2 Open Banking compliance APIs from scratch, translating complex legal mandates into secure software architectures.
*   **How you'd measure success**: Achieve **100% compliance-level auditability** and zero unregulated agent decisions.
*   **Dependencies and risks**: Excessive deterministic checks may slow down agentic speed and increase execution latency.

### Proposal 2: Medallion Data Contract Registry for ExactMatch
*   **The opportunity**: ExactMatch relies on massive ingestion of SEC filings and company databases. Siloed data changes (e.g. schema drifts) break the downstream benchmarking agents.
*   **What you'd do**:
    1.  Establish a central Data Contract Registry on Databricks/Delta Lake.
    2.  Define metadata specifications for schema validation, data freshness, and source lineage.
    3.  Configure automated alerts at the raw ingestion layer that block pipeline runs if incoming data structures breach contracts.
*   **Why you're well-placed to lead this**: Candidate managed external API design governance at SWIFT, resolving schema discrepancies and aligning multi-bank interfaces with international data standards (ISO 20022).
*   **How you'd measure success**: Reduce downstream benchmarking agent disruptions caused by schema drift to **zero**.
*   **Dependencies and risks**: Requires strict buy-in from external data providers and internal ingestion engineers to enforce registry rules.

### Proposal 3: Practitioner Agent-Sandbox & Simulation Suite
*   **The opportunity**: Tax practitioners cannot trust an AI agent until they see how it behaves under varying client financial conditions.
*   **What you'd do**:
    1.  Create an interactive simulation workspace in the practitioner portal.
    2.  Allow practitioners to upload test ledgers and dry-run agent tool-calling paths in a sandboxed environment.
    3.  Provide a visual lineage graph tracing how a generated transfer pricing report retrieved its comparative benchmarks.
*   **Why you're well-placed to lead this**: Candidate designed and delivered developer portals and mock UAT sandboxes on Apigee for Metro Bank to unblock third-party application validation loops.
*   **How you'd measure success**: Drive a **45% increase in practitioner tool-calling adoption** as trust barriers are cleared.
*   **Dependencies and risks**: Designing mocks for complex, varying multinational tax files requires substantial initial template engineering.

---

## 4. Product Sense Deep Dive (5 Thinking Shifts)

### Shift 1: Strategic Context
In corporate tax compliance software, **correctness and defensibility** are the ultimate priorities. Unlike general conversational AI, a tax-agent platform must prioritize deterministic precision over LLM creativity. The strategic focus for the Agentic Platform must be on **reducing cognitive load for practitioners while maintaining a high audit standard**. Lowering transaction time on R&D tax credit classifications allows Exactera to scale from a services-heavy model to a high-margin SaaS model.

### Shift 2: Relationship Segmentation
We segment integrations and data access according to data sovereignty and usage patterns:

| Segment | Primary Personas | Key Need / Relationship | Data Volume / Frequency |
|---|---|---|---|
| **Benchmarking Sources** | Ingestion Engineers, Data Agents | Reliable, structured data feeds (SEC filings, global financial registries) | High volume / Scheduled weekly batches |
| **Client Ledger Ingestion** | Multinationals' IT, Tax Practitioners | Secure portal upload, PII masking, schema parsing of raw ERP data | High volume / Monthly or seasonal |
| **Practitioner Tool Calling** | Tax Professionals, AI Agents | Visual interfaces to review matches, override decisions, and sign off | Real-time interactive sessions |
| **Audit Regulators** | Enterprise Tax Executives, Tax Inspectors | Read-only access to immutable data lineage, prompt trails, and logs | Low volume / Ad-hoc request |

### Shift 3: Architectural Distinction
We structure the architecture to keep the AI-native layer distinct from the data lakehouse substrate:
*   **App / Agentic Layer**: Controls the planning loops, human-in-the-loop checkpoints, user interfaces, and mock simulation workspaces.
*   **Core Platform Layer**: Governs Databricks medallion ingestion, Delta Lake schema contracts, and the auditable log storage.

```mermaid
graph TD
    subgraph App / Agentic Layer (Practitioner Portal)
        HITL[HITL Dashboard] -->|Approve Override| UI[Practitioner UI]
        Sandbox[Simulation Sandbox] -->|Dry Run Agent| Orchestrator[Agent Orchestrator]
    end
    subgraph Core Platform Layer (Data Lakehouse)
        Orchestrator -->|MCP Query| Gateway[Data Access Gateway]
        Gateway -->|Verify Contracts| Registry[Data Contract Registry]
        Gateway -->|Query Medallion Data| Lakehouse[(Databricks Delta Lake)]
        Lakehouse -->|Gold Zone: Audited| AuditLog[(Immutable Audit Log)]
        Lakehouse -->|Silver Zone: Structured| BenchmarkDB[(Benchmarking Data)]
        Lakehouse -->|Bronze Zone: Raw| ClientLedger[(Raw Client Ledgers)]
    end
```

### Shift 4: Trust-by-Design
To enforce regulatory audibility, we implement a signed JSON schema verifying the alignment of every agent tool calling action. This ensures that the agent cannot execute an API call unless the specific transaction parameters match audited data policies:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ExacteraAgentAuditRecord",
  "type": "object",
  "properties": {
    "audit_context": {
      "type": "object",
      "properties": {
        "tenant_id": { "type": "string", "format": "uuid" },
        "practitioner_id": { "type": "string", "format": "uuid" },
        "jurisdiction": { "type": "string", "minLength": 2, "maxLength": 2 }
      },
      "required": ["tenant_id", "practitioner_id", "jurisdiction"]
    },
    "data_contracts": {
      "type": "object",
      "properties": {
        "data_lineage_hash": { "type": "string", "pattern": "^[a-fA-F0-9]{64}$" },
        "schema_version": { "type": "string" },
        "lineage_verified": { "type": "boolean" }
      },
      "required": ["data_lineage_hash", "schema_version", "lineage_verified"]
    },
    "agent_evaluation": {
      "type": "object",
      "properties": {
        "model_id": { "type": "string" },
        "confidence_score": { "type": "number", "minimum": 0, "maximum": 1 },
        "requires_hitl_approval": { "type": "boolean" },
        "override_reasoning": { "type": "string" }
      },
      "required": ["model_id", "confidence_score", "requires_hitl_approval"]
    }
  },
  "required": ["audit_context", "data_contracts", "agent_evaluation"]
}
```

### Shift 5: Growth Flywheels
We model the platform value output ($V$) as a function of data contract reliability ($D$), practitioner confidence and adoption ($A$), model execution speed ($S$), and regulatory penalty exposure ($P$):

$$V = D \times A \times e^{-\gamma S} \times (1 - P)$$

Where $\gamma$ represents the transaction duration attrition coefficient. Enforcing strict data contracts ($D$) increases the accuracy of benchmarking models, which directly builds practitioner trust and software adoption ($A$). Faster execution speeds ($S$) and zero audit failures ($P = 0$) drive the flywheel, turning tax compliance from a high-touch services cost center into a scalable SaaS product.

---

## 5. Candidate Strategic Bridge

### Tailored Professional Summary
Technical Product Leader with over 15 years of experience building, governing, and scaling bank-grade API platforms and enterprise data integration models. Post-acquisition certified Google Cloud Apigee platform architect; managed API design governance at SWIFT, launched PSD2 developer portals and UAT sandboxes from scratch at Metro Bank, and drove ERP integrations at KAO. Proven track record defining data schemas, enforcing compliance and auditability in regulated spaces, and building visual developer-onboarding environments.

### 3 Strategic Outcomes Proving Delivery
*   **Outcome 1 (Metro Bank)**: Shipped PSD2/Open Banking developer portals and sandboxes from scratch on Apigee under strict regulatory timelines.
    *   *Exactera Impact*: Directly translates to designing and launching the agentic access surface, visual practitioner sandboxes, and documentation portals.
*   **Outcome 2 (SWIFT)**: Headed API design governance and pilot onboarding programs (10 banks, 10 corporate partners, 4 TMS vendors), standardizing schema validations (ISO 20022).
    *   *Exactera Impact*: Directly applies to managing medallion data contracts, enforcing delta lake structures, and maintaining alignment across engineering and tax practice teams.
*   **Outcome 3 (Metro Bank)**: Designed secure API authentication models using OAuth 2.0, OpenID Connect, and eIDAS certificate validation frameworks.
    *   *Exactera Impact*: Maps to building the zero-trust tool access controls, audit logs, and secure data ingestion pipelines at Exactera.

### 5 Candidate Strategic Bridge Bullet Points
*   **Compliance Engineering**: Experienced translating strict regulatory frameworks (PSD2, Open Banking, SWIFT banking rules) into deterministic API logic.
*   **Data Lineage Governance**: Standardized corporate cash transaction schemas, ensuring end-to-end data quality, tracking, and auditability.
*   **Developer Sandbox Strategy**: Shipped mock sandbox environments to allow external developers and internal analysts to test integrations without risking live systems.
*   **SaaS-to-Services Integration**: Led selection, configuration, and operation of Apigee platforms, establishing reusable API operating models across mass markets.
*   **Multi-Partner Facilitation**: Directed complex client-facing working groups, reconciling conflicting technical priorities between engineering and business stakeholders.

---

## 6. Tailored Interview Questions

### For the Hiring Manager (Director of Product, Agentic Platform)
1.  *Since tax compliance is zero-tolerance, how do you evaluate model hallucination risks for R&D tax classification before pushing changes to production?*
    > _What they're really testing: Experience building robust AI evaluation guardrails and managing risk in regulated SaaS products._
2.  *Exactera is moving from a services model to a SaaS platform. How are you handling internal friction from tax practitioners who may view autonomous agents as a threat rather than an enabler?*
    > _What they're really testing: Change management strategy, product positioning, and empathy for internal domain experts._

### For the Engineering Lead (Principal AI/Data Engineers)
1.  *How do you enforce schema contracts on Delta Lake tables dynamically at ingestion time, and how do we handle pipeline failures when external regulatory feeds change their structure?*
    > _What they're really testing: Engineering credibility, data validation techniques, and operational pipeline resilience._
2.  *With multiple AI agents calling tools via MCP, how do we prevent concurrent write locks on the Lakehouse gold tier and maintain absolute data lineage auditability?*
    > _What they're really testing: Understanding of concurrency, multi-tenant databases, and auditable log architectures._
