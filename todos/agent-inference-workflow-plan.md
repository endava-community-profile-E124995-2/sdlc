# End-to-End Agent Inference Workflow Test

## Summary

- Use the canonical lifecycle: intake and requirements -> architecture and execution -> quality -> release -> operate.
- Keep this test in shared-workspace mode because no project is registered.
- Standardize every transition as `Inbox -> role processing -> zipped handoff bundle -> Codex critique/refine gate -> next Inbox or upstream return`.

## Handoff Bundle Contract

Each stage emits one `.zip` handoff bundle containing:

- `plan.md`: target role, trigger, known facts, open questions, requested action, unblock criteria
- `artifacts/`: only artifacts owned by the current role
- `evidence/`: supporting sources, validation output, or release evidence produced so far
- `critique.md`: Codex gate findings and refinements applied
- `status.md`: one of `forward`, `revise_current_role`, or `return_upstream`

Expected role-owned artifacts:

- Product: discovery or requirements artifacts, acceptance criteria, dependency and risk summary
- Architecture: feasibility brief, ADR, interface/dependency notes, engineering execution plan
- Implementation: code/test/change bundle tied to the execution plan
- Quality: quality/security/governance notes and Release Gate Memo
- Deployment: Rollout Plan and Operations Handoff Note
- Operate: Operational Follow-up Note, optional Product outcome-review handoff

## Workflow

1. Human Inbox: raw client request enters a shared-workspace intake mailbox.
2. Human Outbox: Product-guided questionnaire produces a confirmed plan with scope, exclusions, rules, success criteria, and open questions locked or explicitly flagged.
3. Codex intake gate: critique/refine the Human Outbox plan against all four roles; if coherent and role-correct, package and deliver to Product Inbox.
4. Product Inbox: Product and Requirements Manager creates discovery/requirements artifacts only, plus a handoff plan to Architecture.
5. Codex product gate: critique/refine the Product bundle; if acceptance criteria, business rules, or scope are incomplete, return to Product; otherwise deliver to Architecture Inbox.
6. Architecture Inbox: Architecture and Engineering Manager creates feasibility, ADR, interface/dependency notes, and an engineering execution plan; unresolved business intent hands back to Product.
7. Codex architecture gate: critique/refine the Architecture bundle; if design is sufficient, hand to the implementation/build stage.
8. Codex implementation/build stage: Codex or a human-in-the-loop engineer executes the approved execution plan and produces the change set, test results, traceability notes, and a release-candidate bundle.
9. Codex implementation gate: critique/refine the implementation bundle for completeness and evidence quality; if it passes, deliver to Quality Inbox.
10. Quality Inbox: Quality and Security and Governance Manager produces the Quality Review Note, Security Review Note or Governance Mapping Note as needed, plus a Release Gate Memo. If the blocker is missing product policy or unresolved architecture boundaries, hand back to the owning upstream role.
11. Codex quality gate: critique/refine the Quality bundle; if the gate outcome is ship-eligible or the unblock path is clearly operational, deliver to Deployment Inbox.
12. Deployment Inbox: Deployment and Operations Manager creates the Rollout Plan, rollback/monitoring/support expectations, and Operations Handoff Note when runtime ownership transfer is required.
13. Codex release gate: verify rollout package completeness against the Release Gate Memo; if complete, execute release and mark the change as shipped.
14. Operate loop: Deployment and Operations Manager collects post-release signals and produces an Operational Follow-up Note or Operability Review.
15. Codex post-release gate: summarize operational signals and package a feedback bundle for Product when outcome review, metric interpretation, or next-cycle prioritization is needed.
16. Product outcome review: Product and Requirements Manager turns post-release evidence into a metrics/outcome review and either closes the request or seeds the next Human Inbox item.

## Test Plan

- Run one happy-path request through every stage and confirm each bundle contains the required handoff fields and only role-owned artifacts.
- Run a product-gap case where acceptance criteria are incomplete and confirm Architecture is blocked and the bundle returns to Product.
- Run a quality-gap case where evidence is insufficient and confirm Quality produces a blocking Release Gate Memo instead of forwarding to release.
- Run an operability-gap case where rollback or monitoring ownership is unclear and confirm Quality hands forward to Deployment only with explicit no-ship unblock criteria.
- Run a post-release case with mixed signals and confirm the workflow produces an Operational Follow-up Note and a Product outcome-review handoff.

## Assumptions

- The test includes a distinct implementation/build stage because "shipped product" requires more than manager-only planning.
- The workflow ends with the operate/feedback loop, not just deployment.
- The same Codex automation pattern applies after every role: critique, refine, boundary-check, package, then either forward, return to current role, or hand back upstream.
- Because the workspace currently has no registered projects, this test should run in shared-workspace mode; once a project exists, map artifacts to the canonical `hub/product`, `hub/technology`, `hub/decisions`, `hub/issues`, and `hub/analytics` locations.
