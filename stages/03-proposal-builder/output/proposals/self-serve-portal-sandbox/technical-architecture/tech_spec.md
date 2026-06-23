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
