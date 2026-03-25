# Risk Card: Security Boundary Drift

```yaml
id: risk.security_boundary_drift
risk_name: Security boundary drift
definition: A change quietly expands or blurs a trust boundary without the intended controls, evidence, or design decision being made explicit.
trigger_signals:
  - data or identity crosses new service boundaries
  - a mitigation depends on implied control behavior rather than approved rules
  - service responsibilities are still under debate during security review
impact_area:
  - security posture
  - auditability
  - residual-risk clarity
likelihood_notes: Likelihood rises when architecture and security reviews run in parallel but do not agree on the final boundary model.
mitigation_actions:
  - name the reviewed boundary explicitly
  - document required controls and missing evidence
  - hand off to architecture when the unresolved issue is a design decision rather than a review judgment
escalation_path:
  - escalate to architecture and engineering when service or interface boundaries are not settled
  - escalate to product when a boundary rule depends on undefined actor or policy intent
related_metric_ids:
  - metric.remediation_lead_time
  - metric.evidence_coverage
```

## Common Failure Mode

Security concerns are acknowledged informally, but the team keeps moving while the boundary model is still unresolved.
