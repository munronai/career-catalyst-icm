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
