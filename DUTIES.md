# Separation of Duties (SOD) & Operational Boundaries

To ensure robust compliance, security, and verification, **GitChurnPrevent** implements a strict tripartite Separation of Duties architecture.

---

### 1. Maker
* **Assigned Entity**: `GitChurnPrevent Automation Engine`
* **Responsibilities**:
  * Monitors customer telemetry events, aggregates feature adoption metrics, and computes risk scores.
  * Ingests raw repository data, configurations, and input artifacts.
  * Formulates candidate evaluations and structured recommendation summaries.
  * Records execution logs into `memory/audit.log`.

---

### 2. Checker
* **Assigned Entity**: `GitChurnPrevent Verification & Policy Enforcer`
* **Responsibilities**:
  * Validates customer renewal contract dates and verifies account ARR tier brackets.
  * Audits calculations, parameter boundary limits, and zero-tolerance rule compliance.
  * Asserts schema validity on all output manifests.
  * Issues preliminary assessment: `APPROVED`, `BLOCKED`, or `NEEDS_REVIEW`.

---

### 3. Approver
* **Assigned Entity**: `VP of Customer Success / Head of Growth (Reserved for human review).`
* **Responsibilities**:
  * Final sign-off authority for high-impact production actions.
  * Mandatory human oversight on security, legal, financial, or regulatory decisions.
  * Reviews unresolvable edge cases and policy override exceptions.
