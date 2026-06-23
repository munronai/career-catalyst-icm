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
