# Canonical ID Map

## Scope

This is the seed canonical ID map for the rewritten Product and Requirements Manager corpus. It covers the IDs used by the structured mesh, operating policy, artifact contracts, metric cards, risk cards, and eval assets in this first migration slice.

## Stakeholder Group IDs

- `stake.exec_leadership`: Executive and business leadership stakeholders.
- `stake.product_org`: Product managers, product leadership, and product operations.
- `stake.engineering_delivery`: Engineering and technical delivery stakeholders.
- `stake.design_research`: Design and user research stakeholders.
- `stake.data_analytics`: Data, analytics, and insights stakeholders.
- `stake.delivery_coordination`: Delivery, agile, program, and coordination stakeholders.
- `stake.gtm`: Go-to-market and product marketing stakeholders.
- `stake.sales_presales`: Sales and pre-sales stakeholders.
- `stake.customer_success`: Customer success and services stakeholders.
- `stake.support_operations`: Support and operations stakeholders.
- `stake.grc`: Legal, risk, compliance, and governance stakeholders.
- `stake.finance_commercial`: Finance and commercial stakeholders.
- `stake.external_customers`: External customer stakeholders.
- `stake.partners_vendors`: Partners, vendors, and third-party stakeholders.
- `stake.platform_shared_services`: Platform, shared services, and enablement stakeholders.
- `stake.governance_forums`: Governance and decision forums.

## Interaction IDs

- `int.strategy_alignment`
- `int.requirement_elicitation`
- `int.requirement_validation`
- `int.prioritization`
- `int.feasibility_analysis`
- `int.risk_identification`
- `int.dependency_management`
- `int.delivery_coordination`
- `int.launch_readiness`
- `int.adoption_planning`
- `int.change_management`
- `int.outcome_review`
- `int.escalation_handling`
- `int.governance_approval`
- `int.budget_justification`
- `int.customer_feedback_synthesis`
- `int.operational_improvement`

## Mesh Case IDs

- `mesh.exec.strategy_alignment`
- `mesh.product.requirement_refinement`
- `mesh.engineering.requirement_clarification`
- `mesh.data.metric_design`
- `mesh.grc.compliance_requirement_mapping`
- `mesh.sales.priority_pressure`
- `mesh.customer_success.adoption_barrier`
- `mesh.support.operational_feedback`

## Capability IDs

- `cap.problem_framing`
- `cap.outcome_definition`
- `cap.customer_research`
- `cap.user_research`
- `cap.feedback_synthesis`
- `cap.requirements_elicitation`
- `cap.requirements_clarification`
- `cap.requirements_quality_review`
- `cap.acceptance_criteria_writing`
- `cap.traceable_requirement_writing`
- `cap.non_functional_requirement_definition`
- `cap.business_rule_identification`
- `cap.workflow_mapping`
- `cap.process_modeling`
- `cap.system_interaction_mapping`
- `cap.trade_off_analysis`
- `cap.strategic_prioritization`
- `cap.decision_framing`
- `cap.decision_memo_writing`
- `cap.impact_analysis`
- `cap.change_control`
- `cap.dependency_management`
- `cap.release_planning`
- `cap.launch_planning`
- `cap.rollout_planning`
- `cap.risk_assessment`
- `cap.risk_mitigation_planning`
- `cap.outcome_review_facilitation`
- `cap.stakeholder_alignment`
- `cap.executive_communication`
- `cap.cross_functional_communication`
- `cap.translating_business_to_technical_language`
- `cap.training_needs_identification`
- `cap.adoption_barrier_analysis`
- `cap.support_issue_analysis`

## Knowledge Area IDs

- `know.product_strategy`
- `know.technical_literacy`
- `know.system_architecture`
- `know.event_instrumentation`
- `know.approval_governance`
- `know.compliance_requirements`
- `know.security_constraints`
- `know.product_analytics`
- `know.experimentation`
- `know.release_governance`
- `know.customer_workflows`
- `know.unit_economics`

## Artifact IDs

- `artifact.discovery_brief`
- `artifact.strategy_brief`
- `artifact.prd`
- `artifact.decision_memo`
- `artifact.launch_brief`
- `artifact.kpi_spec`
- `artifact.post_launch_review`
- `artifact.risk_review`
- `artifact.roadmap_item`
- `artifact.requirement_change_log`

## Method IDs

- `method.customer_interviews`
- `method.jtbd`
- `method.workflow_mapping`
- `method.story_mapping`
- `method.rice`
- `method.wsjf`
- `method.option_analysis`
- `method.premortem`
- `method.experiment_design`
- `method.readiness_review`

## Metric IDs

- `metric.adoption_rate`
- `metric.activation_rate`
- `metric.retention_rate`
- `metric.requirement_rework_rate`
- `metric.cycle_time`
- `metric.defect_escape_rate`
- `metric.customer_satisfaction`
- `metric.revenue_impact`

## Risk IDs

- `risk.wrong_problem`
- `risk.ambiguous_requirements`
- `risk.scope_creep`
- `risk.dependency_delay`
- `risk.compliance_exposure`
- `risk.missing_instrumentation`
- `risk.adoption_risk`
- `risk.support_burden_spike`

## Glossary IDs

- `term.requirement`: A testable statement of intended behavior, rule, constraint, or quality expectation.
- `term.backlog`: A prioritized work inventory, not a storage bin for unresolved thinking.
- `term.launch`: The release and enablement event, not proof of outcome.
- `term.adoption`: Meaningful usage by intended users, not mere access.
- `term.roadmap`: A sequencing hypothesis under constraints, not a promise detached from evidence.

## Naming Rules

- Use the canonical ID in structured records and evals.
- Use aliases only to improve retrieval recall.
- When a raw label from the legacy pack does not map cleanly, prefer the closest canonical node plus a clarifying note instead of minting a vague new label.
