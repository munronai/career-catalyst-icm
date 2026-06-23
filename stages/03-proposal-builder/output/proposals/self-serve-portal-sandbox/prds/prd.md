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
