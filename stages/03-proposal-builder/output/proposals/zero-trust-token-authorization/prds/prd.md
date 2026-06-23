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
