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
