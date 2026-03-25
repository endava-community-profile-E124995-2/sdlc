# Explicit Invocation Cases

- Prompt: "`Use $product-requirements-manager to refine launch requirements for a new billing feature.`"
  Expected: product skill stays primary and frames scope, acceptance criteria, and open business decisions.
- Prompt: "`Use $architecture-and-engineering-manager to assess feasibility for split read/write services.`"
  Expected: architecture skill stays primary and returns technical feasibility and dependency sequencing.
- Prompt: "`Use $quality-and-security-and-governance-manager to review release evidence for PCI scope.`"
  Expected: quality skill stays primary and returns assurance findings, gaps, and release-gate framing.
- Prompt: "`Use $deployment-and-operations-manager to stage a rollback-ready rollout plan for a new API.`"
  Expected: deployment skill stays primary and returns rollout, rollback, monitoring, and support ownership guidance.
