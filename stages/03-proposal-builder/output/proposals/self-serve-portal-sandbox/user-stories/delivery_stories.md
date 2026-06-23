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
