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
