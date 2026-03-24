# Product & Requirements Manager — Relationship Mesh

This file is the retrieval-friendly stakeholder-interaction-role mesh.

Use it after identifying a stakeholder and interaction type from `02_stakeholders_and_interactions.md`, then map to the most relevant capabilities and knowledge areas from `01_role_ontology.md`.

## Retrieval Metadata Conventions

- `id`: Stable identifier for a case or node, such as `EXEC-01` or `GRC-04`.
- `node_type`: One of `stakeholder`, `interaction`, `capability`, `knowledge_area`, `metric`, or `risk`.
- `phase`: One or more of `discover`, `define`, `decide`, `plan`, `deliver`, `launch`, `learn`, or `govern`.
- `artifact_tags`: Short labels for likely outputs, such as `prd`, `decision-memo`, `roadmap-item`, or `launch-brief`.
- `method_tags`: Short labels for likely working approaches, such as `jtbd`, `rice`, `wsjf`, `bpmn`, or `story-mapping`.
- `metric_tags`: Short labels for expected measures, such as `adoption`, `retention`, `cycle-time`, or `nps`.
- `risk_tags`: Short labels for likely exposure, such as `scope`, `compliance`, `dependency`, `readiness`, or `adoption`.
- `priority`: Retrieval weight, expressed as `core`, `high`, `medium`, or `contextual`.
- `confidence`: Retrieval confidence, expressed as `high`, `medium`, or `low`.
- `synonyms`: Alternate labels a user may use for the same stakeholder, interaction, or capability.

Metadata rules:
- Prefer stable identifiers and short lowercase tags.
- Use synonyms for role titles and interaction phrasing that vary by company.
- Tag cases by phase and output so retrieval can route by work type, not only by stakeholder label.
- Keep metadata additive and non-interpretive; do not let tags replace the narrative reasoning in the mesh.

This document converts the stakeholder inventory into a retrieval-friendly case mesh. Each case connects stakeholder nodes, interaction nodes, and the capability / knowledge-area nodes most likely to be activated by the Product & Requirements Manager.

## 1. Cross-Cutting Interaction Type to Skill Stack

- `Strategy alignment`: Product vision definition; Product strategy creation; Strategic planning; Stakeholder alignment; Executive communication.
- `Requirement elicitation`: Requirements elicitation; Stakeholder interviews; Workshop facilitation; Business rule identification; User need translation into requirements.
- `Requirement validation`: Requirements quality review; Testable requirement writing; Traceable requirement writing; Solution validation; Acceptance criteria writing.
- `Prioritization`: Requirements prioritization; Strategic prioritization; Trade-off analysis; Opportunity scoring; Decision framing.
- `Feasibility analysis`: Technical literacy; Feasibility assessment; Technical trade-off understanding; Constraint analysis; System architecture awareness.
- `Risk identification`: Risk identification; Risk assessment; Root cause analysis; Signal vs noise judgment; Recommendation formulation.
- `Dependency management`: Dependency discovery; Dependency tracking; Dependency management; System interaction mapping; Cross-team alignment on requirement changes.
- `Delivery coordination`: Cross-functional coordination; Delivery orchestration; Execution tracking; Issue management; Program-level alignment.
- `Launch readiness`: Launch planning; Release readiness management; Rollout planning; Stakeholder enablement; Internal communication planning.
- `Adoption planning`: Adoption planning; Change management; Training needs identification; Adoption barrier analysis; Stakeholder enablement.
- `Change management`: Change control; Impact analysis; Cross-functional communication; Change management; Documentation governance.
- `Outcome review`: KPI definition; Outcome metric selection; Outcome review facilitation; Data interpretation; Recommendation formulation.
- `Escalation handling`: Escalation management; Issue management; Risk mitigation planning; Executive communication; Decision accountability.
- `Governance approval`: Governance awareness; Approval flow management; Documentation control; Auditability awareness; Executive summary writing.
- `Budget justification`: Business case development; Investment justification; ROI thinking; Cost-benefit analysis; Executive summary writing.
- `Customer feedback synthesis`: Voice of customer analysis; Feedback synthesis; Pain point discovery; Qualitative analysis; Recommendation formulation.
- `Operational improvement`: Operational requirement gathering; Support issue analysis; Process improvement; Service improvement identification; Customer issue prioritization.

## 2. Stakeholder Group Case Mesh

### 2.1 Executive and Business Leadership Stakeholders

Representative stakeholders: CEO, COO, CFO, CTO, CIO, CPO / Head of Product, VP Product, VP Engineering, VP Design, VP Operations, VP Customer Success, VP Sales, VP Marketing, Chief Revenue Officer, Chief Digital Officer, General Manager, Business Unit Leader, Department Head, Regional Leader, Country Manager, Strategy Director, Transformation Lead, Innovation Lead, Portfolio Leader, Steering Committee Members, Executive Sponsors.

Base interaction skills: Stakeholder identification; Stakeholder mapping; Stakeholder alignment; Executive communication; Strategy communication; Decision socialization.

Interaction mesh:
- `EXEC-01 Strategic alignment`: Product vision definition; Product strategy creation; Strategic planning; Outcome definition; Roadmap communication.
- `EXEC-02 Business case approval`: Business case development; Investment justification; ROI thinking; Cost-benefit analysis; Executive summary writing.
- `EXEC-03 Funding decisions`: Budget awareness; Investment justification; Prioritization based on value; Commercial case development; Decision memo writing.
- `EXEC-04 Priority conflicts`: Strategic prioritization; Trade-off analysis; Negotiation; Conflict resolution; Decision framing.
- `EXEC-05 Escalations`: Escalation management; Issue management; Risk mitigation planning; Decision accountability; Executive communication.
- `EXEC-06 Roadmap visibility`: Product roadmap creation; Roadmap communication; Presentation design; Presentation delivery; Status communication.
- `EXEC-07 Outcome reporting`: KPI definition; Outcome review facilitation; Data interpretation; Insight generation; Executive summary writing.
- `EXEC-08 Risk communication`: Risk identification; Risk assessment; Risk mitigation planning; Executive communication; Structured writing.
- `EXEC-09 Organizational alignment`: Stakeholder mapping; Stakeholder alignment; Cross-functional communication; Influence without authority; Decision socialization.

### 2.2 Product Organization Stakeholders

Representative stakeholders: Product Manager, Senior Product Manager, Group Product Manager, Principal Product Manager, Head of Product, Chief Product Officer, Product Owner, Technical Product Manager, Platform Product Manager, Growth Product Manager, Product Operations Manager, Product Analyst, Product Marketing Manager, Product Enablement Manager, Portfolio Manager, Program Manager, Project Manager, Delivery Manager, Release Manager.

Base interaction skills: Stakeholder mapping; Cross-functional communication; Requirements refinement; Backlog refinement; Decision framing; Status communication.

Interaction mesh:
- `PROD-01 Strategy definition`: Problem framing; Product vision definition; Product strategy creation; Outcome definition; Strategic planning.
- `PROD-02 Backlog alignment`: Backlog refinement; Backlog ordering; Backlog hygiene; Requirement-to-backlog translation; Stakeholder alignment.
- `PROD-03 Scope decisions`: Scope definition; Scope control; Trade-off analysis; Ruthless de-scoping; Decision framing.
- `PROD-04 Requirement refinement`: Requirements refinement; Ambiguity removal; Acceptance criteria writing; Testable requirement writing; Business logic definition.
- `PROD-05 Product planning`: Initiative planning; Milestone planning; Goal-to-work alignment; Quarterly planning; Outcome-driven planning.
- `PROD-06 Release coordination`: Release planning; Cross-functional coordination; Release readiness management; Rollout coordination; Status communication.
- `PROD-07 Dependency handling`: Dependency discovery; Dependency tracking; Dependency management; Cross-team alignment on requirement changes; Program-level alignment.
- `PROD-08 Portfolio trade-offs`: Portfolio thinking; Strategic prioritization; Opportunity scoring; Cost vs value analysis; Strategic sequencing.
- `PROD-09 Execution visibility`: Execution tracking; Risk tracking; Status communication; Delivery orchestration; Program-level alignment.

### 2.3 Engineering and Technical Delivery Stakeholders

Representative stakeholders: Engineering Manager, Software Engineer, Frontend Engineer, Backend Engineer, Full Stack Engineer, Mobile Engineer, iOS Engineer, Android Engineer, QA Engineer, Test Automation Engineer, Staff Engineer, Principal Engineer, Architect, Solution Architect, Enterprise Architect, Technical Lead, Team Lead, DevOps Engineer, Site Reliability Engineer, Platform Engineer, Infrastructure Engineer, Security Engineer, Data Engineer, ML Engineer, AI Engineer, Integration Engineer, API Engineer, Release Engineer, Support Engineer.

Base interaction skills: Technical literacy; Translating business to technical language; Requirements clarification; Cross-functional communication; Feasibility assessment; Technical trade-off understanding.

Interaction mesh:
- `ENG-01 Feasibility assessment`: Feasibility assessment; Technical literacy; System architecture awareness; Constraint analysis; Technical trade-off understanding.
- `ENG-02 Technical trade-offs`: Trade-off analysis; Technical trade-off understanding; Systems thinking; Platform thinking; Recommendation formulation.
- `ENG-03 Requirement clarification`: Requirements clarification; Ambiguity removal; Business logic definition; Translating business to technical language; Testable requirement writing.
- `ENG-04 Dependency mapping`: Dependency discovery; Dependency tracking; System interaction mapping; Data flow mapping; Integration awareness.
- `ENG-05 Delivery planning`: Release planning; Capacity-aware planning; Sequencing; Sprint planning support; Milestone planning.
- `ENG-06 Risk identification`: Risk identification; Risk assessment; Root cause analysis; Signal vs noise judgment; Recommendation formulation.
- `ENG-07 Non-functional requirements`: Non-functional requirement definition; Security awareness; Performance requirement awareness; Scalability awareness; Reliability awareness.
- `ENG-08 Architecture alignment`: System architecture awareness; Platform thinking; System interaction mapping; Constraint analysis; Technical trade-off understanding.
- `ENG-09 Release readiness`: Release readiness management; Definition of done awareness; Rollout coordination; Operational follow-up; Reliability awareness.

### 2.4 Design and Research Stakeholders

Representative stakeholders: Product Designer, UX Designer, UI Designer, UX Researcher, User Researcher, Service Designer, Interaction Designer, Content Designer, Design Lead, Head of Design, Accessibility Specialist, Information Architect, Design Operations.

Base interaction skills: UX collaboration; Design requirement framing; User research; Workshop facilitation; Translating business to technical language; Design-to-requirement translation.

Interaction mesh:
- `DESIGN-01 User problem framing`: Problem framing; User research; Customer research; Pain point discovery; Jobs-to-be-done thinking.
- `DESIGN-02 Journey design`: Customer journey mapping; Interaction flow awareness; Journey thinking; Service blueprinting; Experience objective definition.
- `DESIGN-03 Solution validation`: Solution validation; Prototype validation; Usability thinking; Feedback synthesis; User-centered prioritization.
- `DESIGN-04 Experience requirements`: Design requirement framing; Experience objective definition; Accessibility awareness; Information architecture awareness; Design-to-requirement translation.
- `DESIGN-05 Prototype reviews`: Prototype review; Design critique participation; Requirements clarification; Simplifying complex topics; User-centered prioritization.
- `DESIGN-06 User testing`: Usability testing awareness; Interview design; Feedback synthesis; User research; Behavioral analysis.
- `DESIGN-07 Accessibility considerations`: Accessibility awareness; Compliance requirement handling; Design requirement framing; Non-functional requirement definition; Information architecture awareness.
- `DESIGN-08 Design trade-offs`: UX collaboration; Trade-off analysis; User-centered prioritization; Design critique participation; Decision framing.
- `DESIGN-09 Requirement-to-design alignment`: Design-to-requirement translation; Requirements clarification; Structured writing; Cross-functional communication; Ambiguity removal.

### 2.5 Data, Analytics, and Insights Stakeholders

Representative stakeholders: Data Analyst, Product Analyst, Business Analyst, BI Analyst, Data Scientist, Analytics Engineer, Reporting Specialist, Insights Manager, Experimentation Lead, Measurement Lead, Dashboard Owner, Instrumentation Owner.

Base interaction skills: Analytics collaboration; KPI definition; Data interpretation; Insight generation; Quantitative analysis; Recommendation formulation.

Interaction mesh:
- `DATA-01 KPI definition`: KPI definition; OKR alignment; Success metric definition; Outcome metric selection; Leading vs lagging indicator selection.
- `DATA-02 Metric design`: Outcome metric selection; Success metric definition; Leading vs lagging indicator selection; Dashboard requirement definition; Analytics collaboration.
- `DATA-03 Instrumentation planning`: Event instrumentation awareness; Dashboard requirement definition; Data flow awareness; Analytics collaboration; System interaction mapping.
- `DATA-04 Outcome tracking`: Post-launch measurement; Benefit realization tracking; Dashboard requirement definition; Outcome review facilitation; Data interpretation.
- `DATA-05 Experiment interpretation`: Experiment result interpretation; Evidence-based recommendation making; Insight generation; Quantitative analysis; Hypothesis testing.
- `DATA-06 Funnel analysis`: Funnel analysis; Activation analysis; Retention analysis; Adoption analysis; Cohort thinking.
- `DATA-07 Reporting`: Executive summary writing; Structured writing; Data interpretation; Insight generation; Presentation design.
- `DATA-08 Business insight generation`: Insight generation; Pattern recognition; Trend identification; Qualitative analysis; Recommendation formulation.
- `DATA-09 Decision support`: Recommendation formulation; Trade-off analysis; Quantitative analysis; Data interpretation; Critical thinking.

### 2.6 Business Analysis and Requirements Stakeholders

Representative stakeholders: Business Analyst, Systems Analyst, Requirements Analyst, Process Analyst, Domain Analyst, Enterprise Analyst, Functional Consultant, Solution Consultant, Process Owner, Business Process Manager.

Base interaction skills: Requirements elicitation; Workshop facilitation; Process modeling; Requirements quality review; Requirements traceability; Documentation governance.

Interaction mesh:
- `BA-01 Requirements elicitation`: Requirements elicitation; Requirements gathering; Stakeholder interviews; Workshop facilitation; User need translation into requirements.
- `BA-02 Current-state analysis`: Current-state analysis; Process discovery; Workflow mapping; Structured problem solving; Qualitative analysis.
- `BA-03 Future-state design`: Future-state analysis; Gap analysis; Process improvement; Service blueprinting; Recommendation formulation.
- `BA-04 Process mapping`: Process modeling; Workflow mapping; BPMN awareness; Value stream mapping; Sequence flow mapping.
- `BA-05 Business rule capture`: Business rule identification; Decision table creation; Business logic definition; Constraint identification; Requirements clarification.
- `BA-06 Requirement validation`: Requirements quality review; Testable requirement writing; Traceable requirement writing; Solution validation; Acceptance criteria writing.
- `BA-07 Traceability support`: Requirements traceability; Documentation governance; Maintaining requirement repositories; Traceable requirement writing; Requirement status tracking.
- `BA-08 Change analysis`: Impact analysis; Change control; Gap analysis; Constraint analysis; Cross-team alignment on requirement changes.

### 2.7 Delivery, Agile, and Coordination Stakeholders

Representative stakeholders: Scrum Master, Agile Coach, Delivery Lead, Program Manager, Project Manager, PMO Lead, Release Train Engineer, Iteration Manager, Transformation Lead, Delivery Coordinator.

Base interaction skills: Cross-functional coordination; Delivery orchestration; Dependency management; Risk tracking; Issue management; Program-level alignment.

Interaction mesh:
- `DELIVERY-01 Sprint planning support`: Sprint planning support; Backlog refinement; Readiness assessment; Scrum fluency; Definition of ready awareness.
- `DELIVERY-02 Delivery coordination`: Delivery orchestration; Cross-functional coordination; Execution tracking; Status communication; Operational follow-up.
- `DELIVERY-03 Team alignment`: Team alignment; Stakeholder alignment; Team ceremony facilitation; Cross-functional team enablement; Facilitation leadership.
- `DELIVERY-04 Dependency resolution`: Dependency management; Blocker removal; Negotiation; Cross-functional coordination; Program-level alignment.
- `DELIVERY-05 Planning cadence support`: Quarterly planning; Milestone planning; Team ceremony facilitation; Outcome-driven planning; Personal operating cadence.
- `DELIVERY-06 Issue escalation`: Issue management; Escalation management; Risk tracking; Decision accountability; Status communication.
- `DELIVERY-07 Delivery risk management`: Risk tracking; Risk identification; Risk mitigation planning; Contingency planning; Execution tracking.
- `DELIVERY-08 Cross-team synchronization`: Program-level alignment; Cross-functional coordination; Dependency management; Status communication; Delivery orchestration.

### 2.8 Go-To-Market Stakeholders

Representative stakeholders: Product Marketing Manager, Marketing Manager, Demand Generation Manager, Brand Manager, Content Marketing Manager, Growth Manager, Campaign Manager, Communications Lead, Launch Manager, Sales Enablement Manager, Revenue Operations Manager.

Base interaction skills: Launch planning; Strategy communication; Persuasive communication; Stakeholder enablement; Internal communication planning; Adoption planning.

Interaction mesh:
- `GTM-01 Launch planning`: Launch planning; Rollout planning; Rollout strategy; Internal communication planning; Stakeholder enablement.
- `GTM-02 Positioning alignment`: Value proposition design; Competitive positioning; Product strategy creation; Strategy communication; Storytelling.
- `GTM-03 Messaging input`: Clear writing; Structured writing; Storytelling; Persuasive communication; Translating technical to business language.
- `GTM-04 Release communication`: Release notes planning; Internal communication planning; Feature announcement planning; Structured writing; Presentation design.
- `GTM-05 Adoption planning`: Adoption planning; Change management; Adoption barrier analysis; Training needs identification; Post-launch monitoring.
- `GTM-06 Internal enablement`: Stakeholder enablement; Sales/support enablement awareness; Training needs identification; Internal communication planning; Change management.
- `GTM-07 Customer communication`: Feature announcement planning; Persuasive communication; Storytelling; Simplifying complex topics; Change management.
- `GTM-08 Commercial readiness`: Value proposition design; Pricing collaboration awareness; Commercial case development; Sales/support enablement awareness; Launch planning.

### 2.9 Sales and Pre-Sales Stakeholders

Representative stakeholders: Sales Representative, Account Executive, Sales Manager, Sales Director, Enterprise Sales Lead, Solutions Engineer, Sales Engineer, Pre-Sales Consultant, Account Manager, Strategic Account Manager, Channel Manager, Partner Manager, Business Development Manager.

Base interaction skills: Stakeholder interviews; Voice of customer analysis; Feedback synthesis; Negotiation; Expectation management; Translating business to technical language.

Interaction mesh:
- `SALES-01 Customer need collection`: Stakeholder interviews; Voice of customer analysis; Pain point discovery; Needs assessment; Feedback synthesis.
- `SALES-02 Opportunity qualification`: Opportunity assessment; Needs assessment; Segmentation; Demand validation; Value proposition design.
- `SALES-03 Requirement feedback`: Feedback synthesis; Requirements elicitation; Translating business to technical language; Requirement-to-backlog translation; Clear writing.
- `SALES-04 Deal support`: Value proposition design; Solution validation; Persuasive communication; Translating technical to business language; Negotiation.
- `SALES-05 Commercial prioritization pressure`: Prioritization framework design; Strategic prioritization; Expectation management; Negotiation; Decision socialization.
- `SALES-06 Product gap escalation`: Gap analysis; Issue management; Escalation management; Customer issue prioritization; Documentation hygiene.
- `SALES-07 Beta customer identification`: Beta planning; Pilot planning; Segmentation; Success threshold definition; Stakeholder enablement.
- `SALES-08 Market signal intake`: Market research; Trend analysis; Voice of customer analysis; Feedback synthesis; Insight generation.

### 2.10 Customer Success and Service Stakeholders

Representative stakeholders: Customer Success Manager, Customer Success Lead, Customer Experience Manager, Account Manager, Onboarding Manager, Implementation Manager, Professional Services Consultant, Adoption Specialist, Renewal Manager.

Base interaction skills: Voice of customer analysis; Stakeholder interviews; Adoption analysis; Change management; Customer issue prioritization; Benefit realization tracking.

Interaction mesh:
- `CS-01 Customer pain-point intake`: Voice of customer analysis; Pain point discovery; Stakeholder interviews; Feedback synthesis; Needs assessment.
- `CS-02 Adoption issues`: Adoption barrier analysis; Adoption analysis; Customer journey mapping; Root cause analysis; Change management.
- `CS-03 Enablement needs`: Stakeholder enablement; Training needs identification; Internal communication planning; Change management; Adoption planning.
- `CS-04 Workflow gaps`: Current-state analysis; Workflow mapping; Gap analysis; Process improvement; Operational requirement gathering.
- `CS-05 Escalation patterns`: Issue management; Escalation management; Support-to-product feedback loop design; Trend identification; Customer issue prioritization.
- `CS-06 Retention-related product feedback`: Retention analysis; Voice of customer analysis; Benefit realization tracking; Recommendation formulation; Customer issue prioritization.
- `CS-07 Rollout readiness`: Rollout planning; Launch planning; Rollout coordination; Internal communication planning; Stakeholder enablement.
- `CS-08 Customer outcome tracking`: Success metric definition; Benefit realization tracking; Outcome review facilitation; Adoption analysis; Dashboard requirement definition.

### 2.11 Support and Operations Stakeholders

Representative stakeholders: Customer Support Agent, Support Team Lead, Support Manager, Helpdesk Manager, Service Desk Analyst, Incident Manager, Operations Manager, Business Operations Manager, Technical Support Lead, Escalation Manager, Knowledge Base Owner.

Base interaction skills: Support issue analysis; Root cause analysis; Bug triage awareness; Operational requirement gathering; Service improvement identification; Customer issue prioritization.

Interaction mesh:
- `OPS-01 Issue trend analysis`: Support issue analysis; Trend identification; Pattern recognition; Signal vs noise judgment; Recommendation formulation.
- `OPS-02 Bug escalation`: Bug triage awareness; Issue management; Escalation management; Defect prioritization; Documentation hygiene.
- `OPS-03 Workflow breakdown detection`: Root cause analysis; Support issue analysis; Process discovery; Workflow mapping; Service improvement identification.
- `OPS-04 Supportability requirements`: Operational requirement gathering; SLA awareness; Reliability prioritization; Non-functional requirement definition; Service improvement identification.
- `OPS-05 Incident feedback`: Incident feedback integration; Reliability awareness; Root cause analysis; Post-release follow-through; Operational follow-up.
- `OPS-06 Operational pain points`: Operational requirement gathering; Process improvement; Service improvement identification; Current-state analysis; Recommendation formulation.
- `OPS-07 Knowledge gap identification`: Documentation hygiene; Maintaining source-of-truth documentation; Training needs identification; Stakeholder enablement; Simplifying complex topics.
- `OPS-08 Improvement backlog creation`: Backlog creation; Requirement-to-backlog translation; Customer issue prioritization; Defect prioritization; Priority maintenance.

### 2.12 Legal, Risk, Compliance, and Governance Stakeholders

Representative stakeholders: Legal Counsel, Privacy Counsel, Compliance Officer, Risk Manager, Internal Auditor, Data Protection Officer, Security Compliance Lead, Governance Lead, Regulatory Affairs Lead, Policy Owner, Information Security Lead.

Base interaction skills: Compliance requirement handling; Security/compliance collaboration; Policy-to-requirement translation; Documentation control; Approval flow management; Auditability awareness.

Interaction mesh:
- `GRC-01 Regulatory requirements`: Compliance requirement capture; Compliance requirement handling; Policy-to-requirement translation; Regulatory impact awareness; Documentation control.
- `GRC-02 Privacy requirements`: Compliance requirement handling; Security/compliance collaboration; Policy-to-requirement translation; Documentation control; Risk assessment.
- `GRC-03 Security controls`: Security awareness; Security/compliance collaboration; Non-functional requirement definition; Risk mitigation planning; Constraint analysis.
- `GRC-04 Contractual obligations`: Constraint identification; Contract/SLA requirement handling; Documentation control; Requirements traceability; Approval flow management.
- `GRC-05 Auditability needs`: Auditability awareness; Documentation governance; Requirements traceability; Traceable requirement writing; Requirement status tracking.
- `GRC-06 Documentation standards`: Documentation control; Maintaining source-of-truth documentation; Clear writing; Structured writing; Documentation hygiene.
- `GRC-07 Risk acceptance`: Risk assessment; Risk mitigation planning; Governance awareness; Approval flow management; Decision accountability.
- `GRC-08 Approval workflows`: Approval flow management; Governance awareness; Requirements approval management; Status communication; Documentation governance.

### 2.13 Finance and Commercial Stakeholders

Representative stakeholders: Finance Manager, FP&A Analyst, Financial Controller, Procurement Lead, Commercial Manager, Pricing Manager, Revenue Operations Manager, Cost Owner, Budget Owner, Investment Committee Member.

Base interaction skills: Business case development; ROI thinking; Cost-benefit analysis; Investment justification; Quantitative analysis; Executive summary writing.

Interaction mesh:
- `FIN-01 Budget alignment`: Budget awareness; Investment justification; Prioritization based on value; Stakeholder alignment; Executive summary writing.
- `FIN-02 ROI discussions`: ROI thinking; Cost-benefit analysis; Benefit realization tracking; Quantitative analysis; Executive communication.
- `FIN-03 Cost/benefit analysis`: Cost-benefit analysis; Quantitative analysis; Prioritization based on value; Recommendation formulation; Trade-off analysis.
- `FIN-04 Investment prioritization`: Strategic prioritization; Portfolio thinking; Opportunity scoring; Investment justification; Decision framing.
- `FIN-05 Commercial modeling`: Business model understanding; Revenue logic understanding; Pricing collaboration awareness; Unit economics awareness; Forecast input support.
- `FIN-06 Procurement dependencies`: Build / buy / partner analysis; Dependency management; Constraint analysis; Contract/SLA requirement handling; Decision memo writing.
- `FIN-07 Funding approval`: Business case development; Investment justification; Executive summary writing; Persuasive communication; Decision memo writing.
- `FIN-08 Financial reporting inputs`: Benefit realization tracking; Dashboard requirement definition; Structured writing; Executive summary writing; Data interpretation.

### 2.14 Internal Business Function Stakeholders

Representative stakeholders: Operations Lead, HR Lead, Training Lead, L&D Lead, Internal Communications Lead, Admin Lead, Procurement Lead, Facilities Lead, Knowledge Management Lead, Change Manager.

Base interaction skills: Operational requirement gathering; Process discovery; Change management; Stakeholder enablement; Policy-to-requirement translation; Cross-functional communication.

Interaction mesh:
- `INT-01 Internal process requirements`: Operational requirement gathering; Process discovery; Workflow mapping; Requirements elicitation; Constraint identification.
- `INT-02 Workflow improvements`: Process improvement; Gap analysis; Future-state analysis; Value stream mapping; Recommendation formulation.
- `INT-03 Internal tool needs`: Internal tooling requirement management; Requirements elicitation; Backlog planning; Scope definition; Requirement-to-backlog translation.
- `INT-04 Adoption planning`: Adoption planning; Change management; Training needs identification; Stakeholder enablement; Adoption barrier analysis.
- `INT-05 Training coordination`: Training needs identification; Stakeholder enablement; Rollout planning; Internal communication planning; Meeting facilitation.
- `INT-06 Change rollout`: Change management; Rollout strategy; Internal communication planning; Feature announcement planning; Post-launch monitoring.
- `INT-07 Policy alignment`: Policy-to-requirement translation; Stakeholder alignment; Documentation control; Governance awareness; Cross-functional communication.

### 2.15 Domain and Subject Matter Expert Stakeholders

Representative stakeholders: Subject Matter Expert, Domain Expert, Business Owner, Operations Specialist, Compliance Specialist, Security Specialist, Clinical Expert, Financial Expert, Logistics Expert, Industry Consultant.

Base interaction skills: Stakeholder interviews; Business rule identification; Requirements clarification; Constraint identification; Requirements quality review; Recommendation formulation.

Interaction mesh:
- `SME-01 Domain rule clarification`: Business rule identification; Stakeholder interviews; Requirements clarification; Constraint identification; Business logic definition.
- `SME-02 Edge case validation`: Ambiguity removal; Business logic definition; Testable requirement writing; Scenario planning; Solution validation.
- `SME-03 Process accuracy`: Process modeling; Current-state analysis; Requirements quality review; Workflow mapping; Attention to detail.
- `SME-04 Regulatory detail`: Compliance requirement capture; Regulatory impact awareness; Policy-to-requirement translation; Documentation control; Requirements clarification.
- `SME-05 Decision support`: Recommendation formulation; Critical thinking; Quantitative analysis; Qualitative analysis; Decision framing.
- `SME-06 Specialized requirement review`: Requirements quality review; Traceable requirement writing; Testable requirement writing; Constraint analysis; Acceptance criteria writing.

### 2.16 External Customer Stakeholders

Representative stakeholders: End User, Buyer, Customer Admin, Power User, Business User, Operator, Manager User, Executive Sponsor on client side, Procurement contact, IT contact, Security contact, Compliance contact, Customer implementation lead, Customer support lead.

Base interaction skills: Customer research; User research; Pain point discovery; Feedback synthesis; Solution validation; Change management.

Interaction mesh:
- `CUST-01 Problem discovery`: Customer research; User research; Pain point discovery; Jobs-to-be-done thinking; Stakeholder interviews.
- `CUST-02 Workflow understanding`: Customer journey mapping; Workflow mapping; Current-state analysis; Behavioral analysis; Service blueprinting.
- `CUST-03 Requirement validation`: Solution validation; Requirements quality review; Testable requirement writing; Prototype validation; Feedback synthesis.
- `CUST-04 Feedback collection`: Voice of customer analysis; Feedback synthesis; User research; Customer interviewing; Qualitative analysis.
- `CUST-05 Pilot participation`: Pilot planning; Success threshold definition; Failure threshold definition; Learning agenda design; Stakeholder enablement.
- `CUST-06 Beta testing`: Beta planning; Prototype validation; Usability testing awareness; Feedback synthesis; Learning agenda design.
- `CUST-07 Change impact analysis`: Impact analysis; Change management; Adoption barrier analysis; Customer journey mapping; Recommendation formulation.
- `CUST-08 Adoption review`: Adoption analysis; Outcome review facilitation; Benefit realization tracking; Retention analysis; Customer journey mapping.

### 2.17 Partners, Vendors, and Third-Party Stakeholders

Representative stakeholders: Technology Vendor, Integration Partner, Consulting Partner, Agency Partner, Reseller, Distributor, Strategic Alliance Manager, API Provider, External Platform Owner, Managed Service Provider, Outsourcing Partner.

Base interaction skills: Integration awareness; API awareness; Dependency management; Stakeholder alignment; Negotiation; Roadmap communication.

Interaction mesh:
- `PARTNER-01 Integration dependencies`: Integration awareness; API awareness; Dependency management; System interaction mapping; Technical literacy.
- `PARTNER-02 Contractual commitments`: Build / buy / partner analysis; Contract/SLA requirement handling; Documentation control; Approval flow management; Negotiation.
- `PARTNER-03 Capability constraints`: Feasibility assessment; Constraint analysis; Dependency discovery; Technical trade-off understanding; Recommendation formulation.
- `PARTNER-04 Shared delivery planning`: Cross-functional coordination; Release planning; Rollout coordination; Dependency planning; Program-level alignment.
- `PARTNER-05 Platform limitations`: Platform thinking; Technical trade-off understanding; Constraint analysis; Non-functional requirement definition; System architecture awareness.
- `PARTNER-06 Partner requirements`: Requirements elicitation; Stakeholder alignment; Integration awareness; Policy-to-requirement translation; Clear writing.
- `PARTNER-07 Joint roadmap coordination`: Long-term roadmap planning; Roadmap communication; Portfolio thinking; Strategic sequencing; Consensus building.

### 2.18 Platform, Shared Services, and Internal Enablement Stakeholders

Representative stakeholders: Platform Team, Identity Team, Payments Team, Security Platform Team, DevEx Team, Infrastructure Team, Internal Tools Team, Shared Services Team, Data Platform Team, Architecture Review Board, Integration Team.

Base interaction skills: Platform thinking; Dependency management; System architecture awareness; Cross-team alignment on requirement changes; Reliability prioritization; Capacity-aware planning.

Interaction mesh:
- `PLATFORM-01 Shared dependency management`: Dependency management; Dependency tracking; Cross-team alignment on requirement changes; Program-level alignment; Reliability prioritization.
- `PLATFORM-02 Platform roadmap alignment`: Platform thinking; Product roadmap creation; Roadmap communication; Strategic sequencing; Goal-to-work alignment.
- `PLATFORM-03 Architectural standards`: System architecture awareness; Governance awareness; Documentation control; Constraint analysis; Technical literacy.
- `PLATFORM-04 Technical constraints`: Constraint identification; Feasibility assessment; Technical trade-off understanding; Platform thinking; Recommendation formulation.
- `PLATFORM-05 Service-level expectations`: SLA awareness; Reliability prioritization; Non-functional requirement definition; Scalability awareness; Observability awareness.
- `PLATFORM-06 Internal capability planning`: Capability mapping; Capacity-aware planning; Platform thinking; Dependency planning; Strategic planning.

### 2.19 Governance and Decision Forum Stakeholders

Representative stakeholders: Steering Committee, Change Advisory Board, Architecture Review Board, Security Review Board, Data Governance Council, Investment Committee, Portfolio Review Board, Leadership Forum, Risk Committee.

Base interaction skills: Governance awareness; Approval flow management; Decision memo writing; Executive communication; Documentation control; Consensus building.

Interaction mesh:
- `GOV-01 Approval decisions`: Approval flow management; Decision memo writing; Executive communication; Decision accountability; Governance awareness.
- `GOV-02 Risk review`: Risk assessment; Risk mitigation planning; Auditability awareness; Recommendation formulation; Structured writing.
- `GOV-03 Investment prioritization`: Portfolio thinking; Opportunity scoring; Cost vs value analysis; Strategic prioritization; Investment justification.
- `GOV-04 Exception requests`: Decision framing; Governance awareness; Risk assessment; Negotiation; Objection handling.
- `GOV-05 Governance gates`: Release governance awareness; Documentation control; Requirement status tracking; Requirements approval management; Auditability awareness.
- `GOV-06 Strategic alignment`: Strategic planning; Stakeholder alignment; Roadmap communication; Consensus building; Executive communication.
- `GOV-07 Cross-portfolio trade-offs`: Portfolio thinking; Strategic prioritization; Cost vs value analysis; Trade-off analysis; Consensus building.

### 2.20 Regulatory and External Oversight Stakeholders

Representative stakeholders: Regulator, Auditor, Certification Body, Standards Body Representative, External Compliance Reviewer, External Legal Advisor.

Base interaction skills: Compliance requirement handling; Regulatory impact awareness; Auditability awareness; Documentation governance; Risk mitigation planning; Clear writing.

Interaction mesh:
- `REG-01 Compliance interpretation`: Compliance requirement handling; Regulatory impact awareness; Policy-to-requirement translation; Critical thinking; Clear writing.
- `REG-02 Audit support`: Auditability awareness; Documentation governance; Requirements traceability; Maintaining source-of-truth documentation; Structured writing.
- `REG-03 Certification requirements`: Compliance requirement capture; Documentation control; Approval flow management; Requirements traceability; Auditability awareness.
- `REG-04 Documentation evidence`: Maintaining source-of-truth documentation; Traceable requirement writing; Clear writing; Structured writing; Documentation hygiene.
- `REG-05 Regulatory changes`: Change control; Impact analysis; Regulatory impact awareness; Cross-team alignment on requirement changes; Prioritization framework design.
- `REG-06 Risk mitigation actions`: Risk mitigation planning; Requirements prioritization; Cross-functional coordination; Recommendation formulation; Execution tracking.

### 2.21 Community and Ecosystem Stakeholders

Representative stakeholders: Developer Community, User Community, Advocacy Group, Beta Community, Open Source Maintainers, Marketplace Partners, Strategic Advisors, Industry Associations.

Base interaction skills: Voice of customer analysis; Market research; Trend analysis; Feedback synthesis; Opportunity assessment; Cross-functional communication.

Interaction mesh:
- `COMM-01 External feedback loops`: Voice of customer analysis; Feedback synthesis; Market research; Qualitative analysis; Insight generation.
- `COMM-02 Ecosystem needs`: Market research; Platform thinking; API awareness; Trend analysis; Opportunity assessment.
- `COMM-03 API/product adoption signals`: Adoption analysis; Trend identification; Pattern recognition; Analytics collaboration; Insight generation.
- `COMM-04 Community requests`: Feedback synthesis; Prioritization framework design; Issue management; Expectation management; Clear writing.
- `COMM-05 Reputation effects`: Risk identification; Executive communication; Persuasive communication; Strategy communication; Objection handling.
- `COMM-06 Innovation signals`: Trend analysis; Opportunity assessment; Scenario planning; Competitive analysis; Recommendation formulation.

## 3. Coverage Notes

- The mesh covers every stakeholder group in `02_stakeholders_and_interactions.md` sections 1 through 21.
- Each interaction case is linked to skills named directly from `01_role_ontology.md`, with group-level base skills separated from case-specific skills to keep retrieval cleaner.
- The cross-cutting interaction map can be used when the stakeholder is known but the exact stakeholder group is ambiguous, while the stakeholder-group sections are better when the counterparty is already known.
