# Artifact Contract: Release Gate Memo

```yaml
id: artifact.release_gate_memo
artifact_name: Release Gate Memo
purpose: Make the current gate recommendation explicit by tying blockers, evidence, exceptions, and handoffs to a release boundary.
required_sections:
  - gate_scope
  - decision_and_rationale
  - blocking_issues
  - evidence_and_exception_status
  - required_handoffs
  - unblock_criteria
optional_sections:
  - review_inputs
  - time_bound_conditions
  - release_recheck_trigger
minimum_quality_bar: A serious release gate memo states the release scope, the gate recommendation, the evidence and exception status, the blocking issues, and the exact conditions required to unblock.
common_failure_modes:
  - the memo implies "ship with caution" instead of making a decision
  - blockers are listed without explaining why they affect the gate
  - evidence gaps are hidden inside generic risk language
  - handoffs are vague and have no unblock criteria
good_example_ref: corpus/examples/release_gate_memo_good_block_with_unblockers.md
bad_example_ref: corpus/examples/release_gate_memo_bad_ship_it_anyway.md
```

## Template

1. Gate scope
2. Decision and rationale
3. Blocking issues
4. Evidence and exception status
5. Required handoffs
6. Unblock criteria
