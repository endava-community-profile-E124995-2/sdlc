# Good Example: Operability Review

## Runtime scope reviewed

Reviewed the prelaunch operating posture for the notification-service release targeting EU production.

## Readiness expectations

The service is only ready if the new delivery-latency dashboard, pager rule, rollback steps, and on-call owner are all confirmed before launch.

## Monitoring and alerting status

The dashboard and pager rule exist and were verified against staging traffic yesterday. Alert routing still depends on the EU on-call schedule being updated before launch.

## Runbook and support ownership status

The new delivery-failure runbook exists and links to the rollback steps. Support ownership is assigned to the EU messaging on-call lead, but the backup escalation contact is still missing.

## Gaps and risks

The current gap is support ownership completeness, not tooling. This is a support-ownership risk because the backup responder is still undefined for the first launch window.

## Recommendation

Operational readiness is conditionally adequate only if the EU on-call rotation and backup escalation contact are confirmed before launch. If those stay open, pause the release and hand the blocker to the owning support manager.
