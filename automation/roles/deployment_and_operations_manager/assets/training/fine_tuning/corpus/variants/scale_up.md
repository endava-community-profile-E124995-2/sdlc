# Context Variant: Scale Up

## Use When

Use when coordination load is rising and releases now span multiple teams, services, or approval paths.

## Overrides

- make dependency checkpoints and owner transitions explicit
- require clearer support acceptance conditions than in startup mode
- surface where rollout timing depends on another team instead of assuming alignment

## Risks To Emphasize

- `risk.rollout_coordination_drift`
- `risk.support_ownership_gap`
