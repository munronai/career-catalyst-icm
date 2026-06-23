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
