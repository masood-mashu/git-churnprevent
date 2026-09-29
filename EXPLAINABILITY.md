# Explainability, Auditability & Decision Logic: GitChurnPrevent

This document details the transparent decision architecture, algorithmic criteria, data provenance, and operational boundaries of **GitChurnPrevent**, ensuring complete compliance with OpenGAP standards and Checkpoint 02 requirements.

---

## 1. Input Data and Data Sources Used

**GitChurnPrevent** ingests structured, machine-verifiable data artifacts from well-defined sources to ensure total repeatability:
- **Product**: Product analytics telemetry streams (Mixpanel, Segment, PostHog).
- **CRM**: CRM subscription records, renewal dates, and contract ARR tiers.
- **Customer**: Customer support ticket satisfaction ratings and NPS surveys.
- **OpenGAP Specification Manifests**: Ingests `agent.yaml`, `RULES.md`, and local state from `memory/MEMORY.md`.

All data sources are parsed deterministically without dynamic external unverified calls, ensuring that evaluations reflect the exact state of the repository at the moment of inspection.

---

## 2. How It Decides and Reasoning Process

The decision pipeline operates through a multi-stage validation sequence designed to eliminate subjective ambiguity:

1. **Syntax & Schema Verification**: Ingested inputs are first validated against strict JSON and YAML schemas defined in `tools/`. Any malformed payloads are immediately rejected.
2. **Deterministic Metric Extraction**:
   - **score_usage_velocity**: Uses `usage-velocity-scorer` to calculate computes rolling 14-day user active session velocity compared to previous period.
   - **classify_nps_sentiment**: Uses `net-promoter-classifier` to calculate classifies survey responses into standard nps categories (promoter, passive, detractor).
   - **select_retention_playbook**: Uses `retention-playbook-selector` to calculate selects targeted cs intervention playbook based on churn risk level and account tier.
3. **Policy Boundary Checks**: Extracted metrics are evaluated against the non-negotiable rules defined in `RULES.md`.
4. **Verdict Synthesis**:
   - **`APPROVED`**: Issued when all criteria strictly pass thresholds, zero compliance violations are detected, and data integrity is certified.
   - **`NEEDS_REVIEW`**: Issued when borderline metrics or ambiguous edge cases require human supervisor assessment.
   - **`BLOCKED`**: Issued immediately upon detecting any violation of zero-tolerance rules, severe risk factors, or non-compliant parameters.

When account telemetry is ingested, the agent executes usage_velocity_scorer, net_promoter_classifier, and retention_playbook_selector. If health is high and usage is stable, it issues APPROVED. If moderate telemetry drop-off is detected, it issues NEEDS_REVIEW. If critical user disengagement (> 60% drop) occurs within 60 days of renewal, it issues BLOCKED.

---

## 3. Constraints, Limitations, and Known Issues

To ensure reliable and safe operation, the following constraints and operational boundaries apply:
- **Operates**: Operates deterministically (temperature = 0.1) based on quantitative behavioral formulas.
- **Requires**: Requires at least 14 days of historical product telemetry for baseline velocity calculation.
- **Does**: Does not cancel subscriptions or execute refunds without explicit executive approval.
- **Deterministic Execution Constraint**: All model prompts and evaluations must run with low temperature (`0.1`) to ensure predictable, reproducible scoring and eliminate hallucinated findings.
- **Human Authority**: The agent cannot self-execute irreversible external mutations; final approval is reserved strictly for human authorities as specified in `DUTIES.md`.
