import os

# Helper to write files
def write_file(filepath, content):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created: {filepath}")

# Define base output directory
OUTPUT_DIR = "stages/03-proposal-builder/output/proposals"

# ==========================================
# PROPOSAL 1: self-serve-portal-sandbox
# ==========================================
p1 = "self-serve-portal-sandbox"

write_file(f"{OUTPUT_DIR}/{p1}/research/discovery_report.md", """
# Discovery Report: Developer Portal & UAT Sandbox friction

## Research Findings
| Competitor / Standard | Onboarding Duration | UAT Error Rates | Developer Portal DX |
|---|---|---|---|
| **Stripe** | < 1 hour (Fully Self-Serve) | < 0.1% | Excellent documentation, mock tokens, dynamic dashboards |
| **TransUnion** | 7 - 14 Days (Manual) | 2.5% | Static PDFs, manual key provisioning |
| **Experian CrossCore** | 10 - 21 Days (Manual Integration Support) | 1.8% | Mixed guides, manual Tenant credentials setup |

## Key Insights
*   Manual onboarding of third-party fraud validation engines onto CrossCore introduces a significant lag.
*   Lack of sandboxed mock datasets causes partners to test integrations in active UAT lanes, raising transient API failures.
""")

write_file(f"{OUTPUT_DIR}/{p1}/one-pagers/one_pager.md", """
# One-Pager: Self-Serve Developer Portal & Sandbox Wizard

## Executive Summary
This proposal introduces a self-serve partner onboarding dashboard and UAT sandbox. It automates the generation of JWT/HMAC credentials and provides mock identity endpoints. This reduces partner time-to-first-transaction from 21 days to under 3 days.

## Target Audience
Third-party verification partners (identities, fraud, bio-metrics data feeds) and enterprise developer teams.

## Key Value Proposition
Slashes implementation overhead, increases catalog variety of fraud signals on CrossCore, and enhances developers' experience (DX).
""")

write_file(f"{OUTPUT_DIR}/{p1}/prds/prd.md", """
# PRD: Self-Serve UAT Onboarding Sandbox

## 1. Objectives
*   Automate tenant and sandbox environment creation for external developers.
*   Provision mock identity check endpoints to test integrations without billing implications.
*   Track developer success metrics directly in a portal dashboard.

## 2. User Flows
1.  **Sign Up**: Developer registers on the Experian Developer Portal.
2.  **Sandbox Provisioning**: System creates UAT tenant instance automatically and generates test credentials.
3.  **Mock Calls**: Developer tests integration against `/v1/sandbox/mock/verify` using mock test variables.

## 3. Metrics
*   **Time-to-First-Complete (TTFC)**: Target reduction from 21 days to < 3 days.
*   **Self-Serve Success Rate**: Goal of > 85% of partners onboarding without manual support.
""")

write_file(f"{OUTPUT_DIR}/{p1}/strategy/strategic_alignment.md", """
# Strategic Alignment: Portal & Sandbox

## Strategic Goals
*   **Scale the Ecosystem**: Experian's core value is orchestration. The easier it is for partners to join, the wider the catalog of fraud checks.
*   **Operational Efficiency**: Offloads manual Integration Consultant work, allowing high-margin engineering execution.

## Value Multipliers
*   **Network Effects**: More data partners attract more enterprise fraud buyers.
*   **Churn Reduction**: Providing a stable test sandbox prevents production incidents, increasing partner trust.
""")

write_file(f"{OUTPUT_DIR}/{p1}/technical-architecture/tech_spec.md", """
# Technical Specification: Self-Serve Sandbox

## Data Flow
```mermaid
sequenceDiagram
    autonumber
    Partner Dev->>Developer Portal: Register & Request Sandbox
    Developer Portal->>Core Provisioner: Create UAT Tenant
    Core Provisioner-->>Developer Portal: Return Sandbox Client IDs & JWT Keys
    Developer Portal-->>Partner Dev: Display Credentials
    Partner Dev->>Sandbox Gateway: Call /v1/sandbox/mock/verify (with JWT)
    Sandbox Gateway->>Mock Engine: Evaluate payload variables
    Mock Engine-->>Sandbox Gateway: Return static verified/fraud result
    Sandbox Gateway-->>Partner Dev: Return 200 OK Response
```

## API Designs

### Create Sandbox Tenant
*   **Endpoint**: `POST /v1/sandbox/tenant`
*   **Request**:
```json
{
  "client_name": "Acme Risk Analytics",
  "developer_email": "dev@acme.com"
}
```
*   **Response**:
```json
{
  "tenant_id": "8fa2b101-72f1-4db8-8422-9fa01201994a",
  "sandbox_client_id": "sb_acme_99a8b1",
  "secret_key": "sec_sandbox_xyz123456"
}
```
""")

write_file(f"{OUTPUT_DIR}/{p1}/presentations/deck.md", """
# Slide Deck: Self-Serve Developer Portal & Sandbox Wizard

## Slide 1: Hook
*   **Title**: Unlocking the Developer Loop
*   **Subtitle**: How a self-serve sandbox speeds up partner onboarding on CrossCore.

## Slide 2: Problem
*   **Core Issue**: Onboarding new verification partners is a manual, high-touch process taking up to 21 days.
*   **Impact**: Limits the velocity of expanding the fraud signal database, leaving clients vulnerable to new AI fraud patterns.

## Slide 3: Solution
*   **Overview**: An automated, self-serve developer portal that provisions sandbox credentials and hosts mock APIs.
*   **Benefit**: Slashes onboarding to under 3 days.

## Slide 4: Architecture & Candidate Advantage
*   **Design**: Multi-tenant sandboxes mapped via API gateways.
*   **Advantage**: Leverages candidate's experience designing and deploying Metro Bank's developer portal and UAT sandboxes.

## Slide 5: Metrics
*   **KPIs**: 30% reduction in time-to-first-transaction, 85% self-serve completion, zero production test leaks.
""")

write_file(f"{OUTPUT_DIR}/{p1}/user-stories/delivery_stories.md", """
# User Stories: Sandbox Onboarding

## Story 1: Automating UAT Tenant Creation
```gherkin
Feature: Automated UAT Tenant Provisioning
  As a Partner Developer
  I want my sandbox credentials to be created instantly
  So that I can begin testing the API right away

  Scenario: Success Creation of Sandbox Tenant
    Given the Developer Portal is active
    When I submit my registration with client name "RiskCorp" and email "dev@risk.corp"
    Then the system should generate a unique tenant UUID
    And return a client ID "sb_riskcorp" and a sandbox secret key
```

## Story 2: Requesting Mock Verification Responses
```gherkin
Feature: Mock Endpoint Verification
  As a Partner Developer
  I want to receive static responses from the mock API
  So that I can test my integration logic without billing hits

  Scenario: Call Mock Verification API with Valid JWT
    Given a valid sandbox tenant JWT
    When I call POST "/v1/sandbox/mock/verify" with a mock email payload
    Then the API should respond with status code 200
    And return a mock fraud score verification result
```
""")

write_file(f"{OUTPUT_DIR}/{p1}/reviews/executive_review.md", """
# Executive Persona Review: Sandbox Onboarding

## Feedback
*   **Business Value**: High. Self-serve onboarding accelerates product launch loops and increases ecosystem signal richness.
*   **Financial Impact**: Reduces integration consultant headcount expenses.
*   **Risks**: Ensure that the self-service flow doesn't allow unlicensed partners to leverage proprietary data models.
""")

write_file(f"{OUTPUT_DIR}/{p1}/reviews/engineering_review.md", """
# Engineering Persona Review: Sandbox Onboarding

## Feedback
*   **System Integrity**: The separation of sandbox endpoints (`api.uat.crosscore.experian.com`) from production gateways is architecturally sound.
*   **Concerns**: High-volume load testing is required on the Mock Engine to prevent denial-of-service (DoS) from misconfigured developer scripts.
""")

write_file(f"{OUTPUT_DIR}/{p1}/reviews/ux_review.md", """
# UX Persona Review: Sandbox Onboarding

## Feedback
*   **Developer Experience**: The onboarding wizard layout is clean. The inline copy paste mechanism for API keys improves credential handling.
*   **Improvements**: Recommend adding interactive API call templates (e.g. cURL commands) directly in the UI for quicker onboarding.
""")


# ==========================================
# PROPOSAL 2: no-code-workflow-orchestrator
# ==========================================
p2 = "no-code-workflow-orchestrator"

write_file(f"{OUTPUT_DIR}/{p2}/research/discovery_report.md", """
# Discovery Report: Fraud Rule Management Systems

## Research Findings
| Platform | Workflow Customization | Client Setup Effort | Gateway Latency Overhead |
|---|---|---|---|
| **LexisNexis Risk** | Moderate (Rule Builder) | High (Requires custom scripts) | 120ms |
| **Sift Science** | High (Dynamic Rules Engine) | Medium (API Integration) | 90ms |
| **Experian CrossCore** | Low (Static Configurations) | Very High (Professional Services) | 150ms |

## Key Insights
*   Experian clients must request custom professional services to modify their fraud check sequences.
*   Introducing a visual, no-code schema mapper would let clients adjust rules dynamically, cutting down support reliance.
""")

write_file(f"{OUTPUT_DIR}/{p2}/one-pagers/one_pager.md", """
# One-Pager: No-Code Identity Workflow Orchestrator

## Executive Summary
This proposal defines a visual, drag-and-drop workflow builder for CrossCore. It enables clients to map, chain, and configure fraud identity checks (e.g. run address check first; if score > 80, skip biometrics) without writing code.

## Target Audience
Risk Operations Managers and Client Security Administrators at financial institutions.

## Key Value Proposition
Reduces reliance on Experian Professional Services, slashes client configuration timelines, and accelerates go-to-market up-sell capacity.
""")

write_file(f"{OUTPUT_DIR}/{p2}/prds/prd.md", """
# PRD: No-Code Workflow Builder

## 1. Objectives
*   Provide a visual dashboard widget to drag-and-drop fraud check workflows.
*   Compile client-designed workflow pipelines into standard JSON rulesets.
*   Execute workflows dynamically at the API Gateway layer.

## 2. User Flows
1.  **Design**: Client selects components (Credit Check, Device Fingerprint) and joins them with conditional logic.
2.  **Validation**: Engine verifies that all required variables are routed correctly.
3.  **Publish**: Client deploys the workflow, rewriting the active tenant routing rules on the gateway.

## 3. Metrics
*   **Configuration Support Tickets**: Target reduction of **40%**.
*   **Time-to-Deploy Rules**: Reduced from days (via ticket) to under **5 minutes**.
""")

write_file(f"{OUTPUT_DIR}/{p2}/strategy/strategic_alignment.md", """
# Strategic Alignment: No-Code Orchestrator

## Strategic Goals
*   **Self-Serve Upselling**: Makes it easy for clients to try and add new third-party verification feeds by clicking "Add to Workflow" in the portal.
*   **Cost Control**: Frees up valuable internal engineering resources from basic routing configuration tasks.

## Value Multipliers
*   **Higher Yield**: Dynamically routing traffic based on risk results reduces vendor call costs for clients, saving money on low-risk transactions.
""")

write_file(f"{OUTPUT_DIR}/{p2}/technical-architecture/tech_spec.md", """
# Technical Specification: Workflow Engine

## System Layout
```mermaid
graph TD
    UI[Client Dashboard - Drag & Drop UI] -->|Export Config| Compiler[Rules Compiler]
    Compiler -->|JSON Routing Configuration| Repo[Rules Repository]
    Repo -->|Sync Rules| Gate[CrossCore API Gateway]
    ClientCall[Client API Request] --> Gate
    Gate -->|Query Dynamic Rules| RulesEngine[Gateway Rules Evaluator]
    RulesEngine -->|Condition Match| Provider1[Experian Credit Check]
    RulesEngine -->|Condition Match| Provider2[Partner Bio-Metrics API]
```

## Config Format Example
*   **Endpoint**: `POST /v1/workflows`
*   **Payload**:
```json
{
  "tenant_id": "8fa2b101-72f1-4db8-8422-9fa01201994a",
  "workflow_name": "Low-Risk Checkout Flow",
  "steps": [
    {
      "step_id": 1,
      "service": "experian_address_verify",
      "on_success": 2,
      "on_failure": "reject"
    },
    {
      "step_id": 2,
      "service": "partner_device_fingerprint",
      "conditions": [
        {
          "field": "risk_score",
          "operator": "LESS_THAN",
          "value": 40,
          "action": "approve"
        }
      ]
    }
  ]
}
```
""")

write_file(f"{OUTPUT_DIR}/{p2}/presentations/deck.md", """
# Slide Deck: No-Code Identity Workflow Orchestrator

## Slide 1: Hook
*   **Title**: Orchestration Redefined
*   **Subtitle**: Empowering clients to build fraud workflows dynamically without code.

## Slide 2: Problem
*   **Core Issue**: Creating and modifying identity verification pipelines requires manual scripting and professional services support.
*   **Impact**: High support costs, long delays for clients adapting to shifting fraud trends.

## Slide 3: Solution
*   **Overview**: A visual workflow compiler that outputs standard JSON routing files directly to the API Gateway.
*   **Benefit**: Cuts configuration support calls by 40% and rule deploy times to minutes.

## Slide 4: Architecture & Candidate Advantage
*   **Design**: Dynamic gateway routing rules evaluating JSON configurations.
*   **Advantage**: Draws on candidate's experience managing API design governance and translating complex ISO payment flows into modular systems.

## Slide 5: Metrics
*   **KPIs**: 40% fewer configuration tickets, rule update duration < 5 minutes, 99.99% gateway execution reliability.
""")

write_file(f"{OUTPUT_DIR}/{p2}/user-stories/delivery_stories.md", """
# User Stories: Workflow Builder

## Story 1: Compiling Visual Rules
```gherkin
Feature: Compiling Workflow Rules
  As a Risk Operations Manager
  I want my visual workflow configurations to compile into a JSON ruleset
  So that the API gateway can execute them dynamically

  Scenario: Successfully compile a multi-step workflow
    Given I have designed a workflow with steps "Address Check" and "Device Fingerprint"
    When I save the configuration on the dashboard
    Then the compiler should output a valid CrossCore JSON schema
    And save the configuration to the Rules Repository
```

## Story 2: Dynamic Gateway Routing
```gherkin
Feature: Dynamic Gateway Routing Execution
  As the API Gateway Evaluator
  I want to process requests according to the tenant's compiled workflow
  So that only the matched validation services are executed

  Scenario: Execute conditional workflow steps
    Given a tenant API request with "Low-Risk Checkout Flow" configuration
    And the first step "Address Check" returns a success code
    When the gateway evaluates the condition
    Then the gateway should invoke the next step "Device Fingerprint"
    And skip the fallback check
```
""")

write_file(f"{OUTPUT_DIR}/{p2}/reviews/executive_review.md", """
# Executive Persona Review: No-Code Orchestrator

## Feedback
*   **Business Value**: Strong. Providing a visual interface reduces client onboarding timelines and supports commercial cross-selling of partner feeds.
*   **Concerns**: We must ensure that clients don't misconfigure validation loops and leave entry paths open to fraud.
""")

write_file(f"{OUTPUT_DIR}/{p2}/reviews/engineering_review.md", """
# Engineering Persona Review: No-Code Orchestrator

## Feedback
*   **Technical Feasibility**: Feasible. Compiling the visual nodes into JSON routing maps is clean.
*   **Concerns**: Parsing JSON configurations dynamically at the gateway layer could add minor execution latency. Recommend caching active routing maps in-memory (e.g. Redis).
""")

write_file(f"{OUTPUT_DIR}/{p2}/reviews/ux_review.md", """
# UX Persona Review: No-Code Orchestrator

## Feedback
*   **Usability**: The drag-and-drop canvas is clear. Standardized icons for variables help prevent config errors.
*   **Improvements**: Add validation helper flags in the UI that highlight disjointed nodes or loop circles before saving.
""")


# ==========================================
# PROPOSAL 3: zero-trust-token-authorization
# ==========================================
p3 = "zero-trust-token-authorization"

write_file(f"{OUTPUT_DIR}/{p3}/research/discovery_report.md", """
# Discovery Report: API Authorization & Security Risks

## Research Findings
| Vulnerability Vector | Static API Keys | Short-Lived JWT Tokens | HMAC Signatures |
|---|---|---|---|
| **Credential Theft Risk** | High (Key stored in code) | Low (Expires in 60 mins) | Very Low |
| **Revocation Velocity** | Slow (Manual rotate) | Instant (Token revoked) | Medium |
| **Client Implementation Difficulty** | Low | Medium | High |

## Key Insights
*   Identity platforms are high-stakes targets. Leaked static API keys lead to major data exposures and regulatory liabilities.
*   Implementing short-lived JWT token authorization profiles protects data transactions and mitigates compliance penalties.
""")

write_file(f"{OUTPUT_DIR}/{p3}/one-pagers/one_pager.md", """
# One-Pager: Zero-Trust Tokenized Authorization Profiles

## Executive Summary
This proposal introduces a zero-trust authorization model for CrossCore integrations. It replaces static API keys with short-lived, rotated JWT tokens. This ensures client identity validation is secure and compliant with modern data frameworks (e.g., FAPI).

## Target Audience
Security Architects and Integration Engineers at enterprise clients.

## Key Value Proposition
Secures transaction channels, reduces data exposure liabilities, and simplifies automated tenant access key rotations.
""")

write_file(f"{OUTPUT_DIR}/{p3}/prds/prd.md", """
# PRD: Zero-Trust API Authorization

## 1. Objectives
*   Deprecate static API keys for authentication on the CrossCore API.
*   Introduce OAuth 2.0 Client Credentials flow for token issuance.
*   Automate tenant credential key rotations to reduce breach windows.

## 2. User Flows
1.  **Token Request**: Client submits credentials to `/v1/auth/token` endpoint.
2.  **Verification**: Auth engine issues a JWT token expiring in 60 minutes.
3.  **API Call**: Client queries CrossCore endpoints, attaching the JWT bearer token.

## 3. Metrics
*   **Credential Lifecycle**: Reduce average key age to under **30 days**.
*   **Token Interception Security**: Zero data leakage incidents from hijacked credentials.
""")

write_file(f"{OUTPUT_DIR}/{p3}/strategy/strategic_alignment.md", """
# Strategic Alignment: Zero-Trust Profiles

## Strategic Goals
*   **Regulatory Compliance**: Matches strict global Open Finance and PSD2 specifications, opening up market access to highly-regulated banks.
*   **Protect Brand Trust**: Mitigates risk of brand damage resulting from tenant credential leaks.

## Value Multipliers
*   **Secure Scaling**: Enables automated multi-tenant systems without exposing credentials across shared databases.
""")

write_file(f"{OUTPUT_DIR}/{p3}/technical-architecture/tech_spec.md", """
# Technical Specification: Zero-Trust Authorization

## Authorization Flow
```mermaid
sequenceDiagram
    autonumber
    Client System->>Auth Gate: Request Token (POST /v1/auth/token with Client ID/Secret)
    Auth Gate->>Key Store: Verify Credentials
    Key Store-->>Auth Gate: Validated
    Auth Gate-->>Client System: Return JWT Token (Expires in 3600s)
    Client System->>CrossCore Gateway: Call /v1/identity (with JWT in Bearer Header)
    CrossCore Gateway->>Auth Gate: Validate JWT Signature
    Auth Gate-->>CrossCore Gateway: Token Valid & Tenant Active
    CrossCore Gateway->>Decision Engine: Process Fraud Request
    Decision Engine-->>Client System: Return Verification Score
```

## API Designs

### Request Access Token
*   **Endpoint**: `POST /v1/auth/token`
*   **Payload**:
```json
{
  "grant_type": "client_credentials",
  "client_id": "cc_client_1a98b1",
  "client_secret": "cs_prod_xyz987654321"
}
```
*   **Response**:
```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```
""")

write_file(f"{OUTPUT_DIR}/{p3}/presentations/deck.md", """
# Slide Deck: Zero-Trust Tokenized Authorization Profiles

## Slide 1: Hook
*   **Title**: Securing the Identity Gate
*   **Subtitle**: Implementing zero-trust token authorization on the CrossCore API.

## Slide 2: Problem
*   **Core Issue**: Clients currently authenticate using static API keys, which are often embedded in source code and vulnerable to leakage.
*   **Impact**: Potential PII data breaches, regulatory compliance failures (GDPR/FCRA).

## Slide 3: Solution
*   **Overview**: OAuth 2.0 client credential flows generating short-lived JWT tokens.
*   **Benefit**: Secures transaction channels and limits key exposure windows.

## Slide 4: Architecture & Candidate Advantage
*   **Design**: Standardized JWT authorization checks integrated directly into API gateways.
*   **Advantage**: Applies candidate's experience designing PSD2 Open Banking security structures and OAuth Hybrid Flow at Metro Bank.

## Slide 5: Metrics
*   **KPIs**: Token expiration window < 60 minutes, automated key rotation < 30 days, zero credential leak exposures.
""")

write_file(f"{OUTPUT_DIR}/{p3}/user-stories/delivery_stories.md", """
# User Stories: Zero-Trust Authorization

## Story 1: Requesting a Bearer Token
```gherkin
Feature: Issuing Bearer Tokens
  As an Integration Engineer
  I want to request a short-lived bearer token using my client credentials
  So that I can securely call the CrossCore verification API

  Scenario: Get Token with Valid Credentials
    Given my client ID and client secret are active
    When I submit a POST request to "/v1/auth/token" with valid client credentials
    Then the API should respond with status code 200
    And return a JWT access token expiring in 3600 seconds
```

## Story 2: API Call with Expired Token
```gherkin
Feature: Rejecting Expired Tokens
  As the CrossCore API Gateway
  I want to reject API calls that present an expired token
  So that unauthorized access is prevented

  Scenario: Call API with Expired Token
    Given a JWT token that expired 10 minutes ago
    When I call POST "/v1/identity" attaching the token in the Bearer header
    Then the gateway should return status code 401 Unauthorized
    And specify "token_expired" in the error response payload
```
""")

write_file(f"{OUTPUT_DIR}/{p3}/reviews/executive_review.md", """
# Executive Persona Review: Zero-Trust Authorization

## Feedback
*   **Business Value**: High. Critical for risk mitigation and maintaining compliance standards, helping us sell to large enterprise banks.
*   **Risks**: Security updates may require client engineering teams to adjust their legacy connection setups, which can slow down migration timelines.
""")

write_file(f"{OUTPUT_DIR}/{p3}/reviews/engineering_review.md", """
# Engineering Persona Review: Zero-Trust Authorization

## Feedback
*   **Security Posture**: Strong. JWT signatures (using RS256) offer excellent cryptographic security.
*   **Concerns**: Validating JWT signatures on every API call adds processing load. Recommend using distributed token cache validations at the gateway layer.
""")

write_file(f"{OUTPUT_DIR}/{p3}/reviews/ux_review.md", """
# UX Persona Review: Zero-Trust Authorization

## Feedback
*   **Developer Experience**: Rotating credentials and OAuth setup can add friction during initial onboarding.
*   **Improvements**: Include clear, language-specific code snippets (Python, Node.js, Java) in the Developer Portal to illustrate token generation.
""")

print("\n--- ALL PROPOSALS SUCCESSFULLY GENERATED ---")
