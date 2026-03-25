# Good Example: Rollout Plan

## Release scope and target environment

Release the checkout-service fix to production for the `payments-api` cluster, starting with the canary shard and then the full US region.

## Rollout sequence and checkpoints

1. Deploy to canary shard at 10:00 UTC.
2. Hold for 30 minutes while error rate, latency, and queue depth stay within normal thresholds.
3. Expand to the remaining US production shards only after the release manager and on-call SRE both confirm the hold-point checks.

## Rollback readiness

The prior container image is pinned and rollback can be executed by the release manager within the same deployment pipeline. The database change is additive only. Assumption: no emergency schema backfill is needed if the app version is reverted.

## Monitoring and communication plan

Watch the checkout success dashboard, payment timeout alert, and queue-depth panel during the canary window. Post checkpoint updates in `#release-payments` at start, hold-point exit, and full rollout completion.

## Owners, dependencies, and hold points

Release manager owns sequencing. On-call SRE owns dashboard and alert review. Support lead owns customer-facing incident intake. Hold full rollout if payment timeout alert fires or if support reports checkout failure patterns during the canary.

## Open operational risks and handoffs

The rollback path is ready, but the support macros for card-decline false positives still need final review before full rollout. If that slips, keep the release in canary until support confirms readiness.
