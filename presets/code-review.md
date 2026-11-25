# Preset: Code & Architecture Review (`code-review`)

Activate this preset when the user asks the Silent Council to review source code, a pull request, a database schema, or a system architecture.

## Closed-Door Role Overrides
- **The Skeptic:** Attacks hidden assumptions in edge cases (null inputs, race conditions, network timeouts, empty states).
- **The First-Principles Architect:** Attacks tight coupling, N+1 queries, stateful bottlenecks, and premature abstractions.
- **The Risk & Security Auditor:** Hunts for injection flaws (SQLi/XSS/SSRF), broken auth/RLS, hardcoded secrets, and unbounded API loops.
- **The Pragmatist:** Identifies dead code, over-engineered patterns, and refactors that add complexity without measurable business value.
- **The Impatient End-User (Developer Experience):** Attacks unreadable naming, missing error messages, fragile API contracts, and undocumented magic behavior.
- **The Post-Mortem Futurist:** Diagnoses what breaks 12 months from now during a traffic spike, dependency deprecation, or team handoff.

## Chief Arbiter Scoring Bias
- Double-check `architecture` and `security_risk`. Any unauthenticated write endpoint, missing RLS policy, or exposed secret automatically caps `security_risk` at `2/10` (triggering an immediate VETO).
