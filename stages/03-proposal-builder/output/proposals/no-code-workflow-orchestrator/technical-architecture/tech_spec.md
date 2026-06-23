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
