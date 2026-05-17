# IT303: IT Project Management — Steering the Longship Through Digital Seas

**Program:** Bachelor of Information Technology, Year 3  
**Credits:** 4 ECTS  
**Prerequisites:** IT201, IT203  
**Instructor:** Prof. Gunnhildr Torvaldsdottir, PMP, PRINCE2 Practitioner, CSM  
**Office:** Heorot Hall, Room 312  
**Semester:** Spring 2041  

> *"A longship does not reach its destination by the strength of one rower, nor by the vision of one steersman alone — but by the coordinated rhythm of the entire crew."* — From *The Havamal of Project Management*, Yggdrasil Press, 2039

---

## Course Description

IT Project Management bridges the chasm between technical expertise and organisational delivery. Every IT initiative — whether a cloud migration, a security compliance programme, or a new application deployment — succeeds or fails not on the quality of the code, but on the quality of the project management that governed its execution. This course teaches the frameworks (Agile, Scrum, Kanban, PRINCE2, PMBOK), the tools (Jira, Linear, MS Project, Asana, Monday.com), and the human skills (stakeholder communication, conflict resolution, negotiation) that distinguish a technically competent IT professional from one who reliably delivers value. Students will manage a simulated 12-week IT project from charter through retrospective, encountering injected surprises — scope creep, personnel churn, vendor failures — that mirror the realities of 2040 enterprise IT.

---

## Lecture 1: The Project Management Landscape in 2040 IT

### Why IT Projects Fail, Still

The Standish Group's CHAOS Report has tracked IT project outcomes since 1994, and by 2040 the pattern remains stubbornly consistent: approximately 31% of IT projects succeed outright (on time, on budget, with satisfactory results), 50% are "challenged" (late, over budget, or with reduced scope), and 19% fail entirely (cancelled or delivered but never used). These figures have improved only marginally from the 2015 benchmark (29%/52%/19%), despite three decades of methodological refinement, tooling advancement, and lessons-learned databases. Why? The root causes have shifted in character but not in essence: unclear requirements remain the top failure driver, followed by changing organisational priorities, inadequate stakeholder engagement, and insufficient risk management.

The 2040 landscape introduces new failure modes. **AI-generated project plans**, while fast to produce, may embed hallucinations — invented dependencies, non-existent APIs, or unrealistic timeline estimates — that go undetected until execution stalls. **Distributed autonomous teams** modelled on DAOs (Decentralised Autonomous Organisations) can fragment without strong governance. **Quantum-accelerated schedule optimisation** produces plans that are mathematically perfect but operationally brittle — a single vendor delay cascades through thousands of optimised dependencies. The lesson across all eras: project management is fundamentally a human discipline, and tools amplify human judgment rather than replace it.

### The Triple Constraint and Its 2040 Extensions

The classical Iron Triangle of project management — Scope, Time, Cost — has been extended in 2040 practice to the **Project Management Hexagon**:

```
                  Scope
                    /\
                   /  \
      Quality     /    \   Time
                 /      \
                /________\
       Risk             Cost
                \        /
                 \      /
                  \    /
                   \  /
                    \/
              Stakeholder Satisfaction
```

- **Scope**: The work to be delivered (features, deliverables, outcomes)
- **Time**: The schedule and milestones
- **Cost**: Budget, including personnel, tools, and infrastructure
- **Quality**: Acceptance criteria, defect rates, performance SLAs
- **Risk**: Uncertainty management — threats and opportunities
- **Stakeholder Satisfaction**: The ultimate metric; a project can meet scope/time/cost and still fail if stakeholders are dissatisfied

In 2040 IT, **Sustainability** has also emerged as a seventh dimension — the environmental impact of cloud compute, e-waste from hardware refresh cycles, and energy consumption of AI training runs. The EU's Corporate Sustainability Reporting Directive (CSRD) now mandates project-level carbon accounting for IT initiatives exceeding €5M.

### Required Reading

- Standish Group, *CHAOS Report 2040*, Executive Summary.
- Project Management Institute, *PMBOK Guide*, 8th Edition (2039), Chs. 1-2.
- Axelos, *PRINCE2 2040: Managing Successful Projects*, Introduction.

### Discussion Questions

1. The CHAOS Report shows stubbornly stable failure rates across decades. Is this a measurement artifact, or are there genuinely intractable sources of IT project failure?
2. How does the addition of AI-generated project plans change the project manager's role in requirement validation?
3. Should sustainability be a formal dimension of project success, or is it a constraint within the existing hexagon?

---

## Lecture 2: Project Initiation and the Project Charter

### From Idea to Authorised Initiative

Every project begins with an idea — but an idea becomes a project only when it receives formal authorisation through a **project charter**. The charter is the project's birth certificate: it names the project manager, defines the high-level scope, identifies key stakeholders, establishes the budget envelope, articulates the business case, and grants the project manager authority to expend organisational resources. Without a charter, a project is a "zombie initiative" — consuming resources without legitimate governance, vulnerable to cancellation at any leadership whim.

The 2040 charter has evolved beyond the static document. Modern charters are living documents stored in collaborative platforms (Confluence, Notion, GitBook) with versioned updates. They include **AI-generated risk pre-assessments** — a language model analysis of the charter text against a database of 50,000 historical IT project post-mortems, flagging phrases like "we'll figure out the architecture later" or "the team will be hired once the project starts" that correlate strongly with failure. They also include a **decision rights matrix** (RACI — Responsible, Accountable, Consulted, Informed) that prevents the "everyone is responsible, therefore no one is accountable" anti-pattern.

### Charter Components for an IT Project

For a representative 2040 IT project — migrating Yggdrasil Health's on-premises electronic health record (EHR) system to a HIPAA-compliant multi-cloud architecture — the charter includes:

| Component | Content |
|-----------|---------|
| **Project Title** | Yggdrasil Health EHR Cloud Migration (Project YHEHR-CM-2041) |
| **Project Manager** | Astrid Bjornsdottir, PMP |
| **Sponsor** | Dr. Erik Magnusson, CIO |
| **Business Case** | Reduce infrastructure TCO by 34%, eliminate single-DC vulnerability, enable AI diagnostic integration |
| **High-Level Scope** | Migrate FHIR data store, patient portal, and AI diagnostic module to AWS/Azure; decommission on-premises DC |
| **Budget** | €4.2M (€3.1M cloud migration services, €800K personnel, €300K contingency) |
| **Timeline** | 14 months (March 2041 – May 2042) |
| **Key Stakeholders** | CIO, CISO, Chief Medical Officer, Compliance Officer, EHR Vendor, AWS/Azure account teams |
| **Success Criteria** | Migration complete <14 months; ≤1 hour total patient-facing downtime; all 147 HIPAA controls revalidated |
| **Risks** | Vendor API incompatibility, data integrity during migration, regulatory re-certification delay |

### Required Reading

- PMI, *PMBOK Guide*, 8th Ed., Ch. 4: Project Integration Management.
- Axelos, *PRINCE2 2040*, Ch. 3: Starting Up a Project.
- Hall, E. (2038), "The Zombie Project Problem: Why Charters Matter," *Harvard Business Review*, Digital Edition.

### Discussion Questions

1. What organisational dysfunctions does a formal project charter prevent, and what dysfunctions does it NOT prevent?
2. The Yggdrasil Health charter includes a RACI matrix. Who should be Accountable (the "A") for the security compliance workstream — the project manager, the CISO, or the compliance officer? Justify your answer.
3. If the business case projects a 34% TCO reduction, what happens to the project's legitimacy if that number is revised to 12% at the three-month mark?

---

## Lecture 3: Requirements Gathering and Scope Definition

### The Hardest Conversation in IT

Requirements gathering is deceptively simple: ask stakeholders what they need. In practice, it is the hardest conversation in IT. Stakeholders often cannot articulate their needs precisely. What they express as requirements are frequently solutions they have already designed in their heads ("we need a dashboard with three charts") rather than the underlying problems they need solved ("we cannot quickly assess patient wait times across clinics"). The project manager's skill lies in asking "what problem are you trying to solve?" persistently and gracefully until the real requirement emerges.

The 2040 toolkit for requirements elicitation includes traditional techniques (structured interviews, facilitated workshops, user observation, document analysis) augmented by AI. **Natural Language Processing (NLP) analysis of stakeholder meeting transcripts** can identify implicit requirements — things stakeholders assume but never state aloud. **Digital twin simulations** allow stakeholders to "use" a proposed system before it is built, surfacing requirement gaps that written specifications miss. **Competitive teardown analysis** uses public documentation and API contracts to infer requirements from competing products, ensuring parity or differentiation is a conscious choice.

### From Requirements to Scope

Requirements are what stakeholders want. Scope is what the project commits to deliver. The gap between requirements and scope is where project management happens. Formal scope definition uses:

- **Work Breakdown Structure (WBS)**: A hierarchical decomposition of all deliverables into work packages. The 100% rule states that the WBS must capture 100% of the project scope — nothing omitted, nothing added.
- **Requirements Traceability Matrix (RTM)**: A table that maps each requirement to a design element, a test case, and a deliverable. The RTM ensures nothing is lost in translation from "the business wants X" to "the build team built X."
- **MoSCoW Prioritisation**: Must have, Should have, Could have, Won't have (this time). Prevents the "everything is critical" anti-pattern.
- **User Stories and Acceptance Criteria**: For Agile projects, requirements are expressed as user stories ("As a physician, I want to view patient lab results from the past 12 months so I can assess treatment trends") with concrete, testable acceptance criteria.

### Required Reading

- Wiegers, K. & Beatty, J. (2038), *Software Requirements*, 4th ed., Microsoft Press, Chs. 5-8, 14.
- Cohn, M. (2037), *User Stories Applied*, 2nd ed., Addison-Wesley.
- IIBA, *Business Analysis Body of Knowledge (BABOK)*, v4.0, §§4-5.

### Discussion Questions

1. A stakeholder insists on a specific technical solution rather than describing the problem. How do you navigate this without alienating them?
2. Compare MoSCoW prioritisation to Kano model analysis. When would you use each?
3. For Yggdrasil Health's EHR migration, identify three implicit requirements that a stakeholder might never state but that a skilled analyst should uncover.

---

## Lecture 4: Scheduling, Estimation, and the Planning Fallacy

### Why We Are Bad at Estimating

The planning fallacy — the systematic tendency to underestimate the time, cost, and risks of future actions while overestimating their benefits — is the most expensive cognitive bias in IT. Nobel laureate Daniel Kahneman documented that even when people are aware of the planning fallacy and have access to historical data showing their estimates are consistently optimistic, they still believe "this time is different." The 2040 project manager combats this not with better estimation techniques (though those help) but with institutional processes that remove the incentive to be optimistic: **reference class forecasting**, where estimates are based on actual outcomes from a class of similar projects rather than on bottom-up task estimates; and **planning poker with historical calibration**, where team estimates are adjusted by a factor derived from that team's historical accuracy.

The 2040 estimation toolkit includes:
- **Three-point estimation (PERT)**: Optimistic (O), Most Likely (M), Pessimistic (P) → Expected = (O + 4M + P) / 6
- **Monte Carlo simulation**: Run the schedule model thousands of times with probabilistic inputs to produce a distribution of completion dates. The project manager commits not to "April 15" but to "April 15 with 85% confidence."
- **AI schedule risk scoring**: A model trained on 100,000+ IT project schedules flags tasks whose estimates are statistical outliers compared to similar tasks in the reference database.

### Scheduling Techniques

**Critical Path Method (CPM)**: Identify the longest sequence of dependent tasks through the project. Any delay on the critical path delays the entire project. The 2040 project manager uses CPM-aware tools (MS Project, Smartsheet, LiquidPlanner) that automatically recalculate the critical path when task durations change and flag when the critical path shifts — a common scenario where the team chases the old critical path while a new one has silently emerged.

**Agile Velocity Tracking**: In Scrum and Kanban contexts, estimation shifts from hours to story points — a relative measure of effort. Velocity (story points completed per sprint) stabilises after 3-4 sprints and becomes the basis for release planning. The project manager watches for "velocity inflation" — the tendency for story point values to drift upward over time, masking a decrease in actual throughput.

```python
# Example: Monte Carlo simulation for project completion date
import numpy as np
from datetime import date, timedelta

# Task estimates in days: (optimistic, most_likely, pessimistic)
tasks = {
    "Data migration": (15, 25, 45),
    "API integration": (10, 18, 30),
    "Security audit": (8, 12, 20),
    "UAT": (10, 15, 25),
    "Go-live prep": (5, 8, 14),
}

def pert_sample(o, m, p, samples=10000):
    # PERT distribution via modified beta
    mu = (o + 4*m + p) / 6
    sigma = (p - o) / 6
    alpha = ((mu - o) / (p - o)) * 4 + 1
    beta_param = ((p - mu) / (p - o)) * 4 + 1
    return np.random.beta(alpha, beta_param, samples) * (p - o) + o

total_durations = np.zeros(10000)
for o, m, p in tasks.values():
    total_durations += pert_sample(o, m, p)

print(f"Median completion: {np.median(total_durations):.0f} days")
print(f"85th percentile: {np.percentile(total_durations, 85):.0f} days")
print(f"95th percentile: {np.percentile(total_durations, 95):.0f} days")
```

### Required Reading

- Kahneman, D. & Tversky, A. (1979/2037), *Prospect Theory: Decision Making Under Risk*, annotated reissue, Cambridge.
- Flyvbjerg, B. (2039), *How Big Things Get Done*, 2nd ed., Crown Business, Chs. 3-5.
- PMI, *Practice Standard for Project Estimating*, 3rd Ed. (2038).

### Discussion Questions

1. If everyone knows about the planning fallacy, why does it persist in IT project estimation? What organisational changes could reduce its impact?
2. A Monte Carlo simulation shows that your project has only a 60% chance of hitting the sponsor's target date. How do you communicate this?
3. Compare Critical Path Method to Critical Chain Project Management (Goldratt). Which handles uncertainty better?

---

## Lecture 5: Agile, Scrum, and Kanban in IT Projects

### The Agile Manifesto at Age 40

The Agile Manifesto was published in 2001 by seventeen software practitioners at Snowbird, Utah. By 2040, it has reached middle age — refined, extended, debated, and in some quarters, ossified into the very ritualistic compliance it was meant to replace. The four values remain sound:

- **Individuals and interactions** over processes and tools
- **Working software** over comprehensive documentation
- **Customer collaboration** over contract negotiation
- **Responding to change** over following a plan

But the 2040 critique observes that "Agile" has become an industry of certifications, tooling vendors, and "Agile coaches" who have never shipped software. The 2040 project manager distinguishes between **ceremonial Agile** (standups as status theatre, retrospectives as complaint sessions, story points as performance metrics) and **substantive Agile** (fast feedback loops, empowered teams, continuous delivery, genuine inspect-and-adapt cycles).

### Scrum: The Framework

Scrum remains the dominant Agile framework, structured around:
- **Roles**: Product Owner (what to build), Scrum Master (how to build it well), Development Team (builds it)
- **Events**: Sprint Planning, Daily Scrum (standup), Sprint Review, Sprint Retrospective
- **Artifacts**: Product Backlog, Sprint Backlog, Increment (potentially shippable product)
- **Timeboxes**: Sprints of 1-4 weeks; in 2040 IT, 2-week sprints are standard

For IT projects (as distinct from software development), Scrum adapts: infrastructure sprints include "Definition of Done" criteria like "all Terraform modules pass Checkov scanning" or "monitoring dashboards deployed and alerting verified." The Product Backlog may include operational items (patch cycles, certificate renewals, capacity upgrades) alongside feature work.

### Kanban: Continuous Flow

For IT operations and support projects where work arrives unpredictably (incident tickets, service requests, ad-hoc investigations), Kanban provides a continuous flow model:
- **Visualise the workflow** on a Kanban board with columns (To Do, In Progress, In Review, Done)
- **Limit Work in Progress (WIP)** — the most powerful lever; reducing WIP limits from 5 to 3 per column typically increases throughput by 20-35%
- **Measure flow metrics**: Cycle Time (time from start to finish), Throughput (items completed per week), and Work Item Age (how long has this item been in progress?)
- **Cumulative Flow Diagrams (CFD)** visualise WIP, throughput, and bottlenecks

### Required Reading

- Schwaber, K. & Sutherland, J. (2040), *The Scrum Guide*, 2040 Edition.
- Anderson, D. (2039), *Kanban: Successful Evolutionary Change for Your Technology Business*, 3rd ed.
- Fowler, M. & Highsmith, J. (2038), "The Agile Manifesto at 40: A Retrospective," *ThoughtWorks Perspectives*.

### Discussion Questions

1. "Scrum is a framework, not a methodology." What does this distinction mean in practice, and how does it affect implementation?
2. A team's velocity has been "15 story points per sprint" for six months. What questions would you ask to determine if this is healthy consistency or hidden stagnation?
3. For the Yggdrasil Health EHR migration, would you recommend Scrum, Kanban, or a hybrid? Justify.

---

## Lecture 6: Resource Management and Team Building

### The Resource Allocation Problem

IT projects consume five categories of resources: **personnel** (developers, admins, analysts, architects), **infrastructure** (cloud compute, storage, network), **software** (licences, SaaS subscriptions), **time** (the non-renewable resource), and **attention** (the scarcest resource of all in an era of continuous partial attention). Resource over-allocation — assigning a person to 150% utilisation across three concurrent projects — is a leading cause of project delay, yet it persists because organisations confuse "resource planning" (a spreadsheet exercise) with "capacity management" (a systemic discipline).

The 2040 project manager uses **resource levelling algorithms** in tools like Jira Advanced Roadmaps, Smartsheet Resource Management, and Kantata to detect over-allocations before they cause delays. But the algorithmic solution is insufficient without the human conversation: telling a sponsor that their project will be delayed because the critical resource is overallocated requires the project manager to have political capital, data, and alternatives ready.

### Team Dynamics and Tuckman's Model

Bruce Tuckman's 1965 model of team development — **Forming, Storming, Norming, Performing** — remains the most useful framework for understanding team dynamics. In 1977, Tuckman added **Adjourning** (later called Mourning). The 2040 project manager applies this model with particular attention to:

- **Forming**: The onboarding phase. New team members are polite but anxious. The PM provides clear structure, specific tasks, and psychological safety.
- **Storming**: Conflict emerges as team members assert ideas, challenge the PM's decisions, and compete for roles. This is a healthy sign — a team that never storms has never truly engaged. The PM's role is to surface conflicts constructively, not suppress them.
- **Norming**: The team establishes shared norms, communication patterns, and trust. The PM shifts from directive to facilitative leadership.
- **Performing**: The team operates with high autonomy and effectiveness. The PM focuses on removing obstacles and protecting the team from organisational noise.
- **Adjourning**: The project ends. The PM conducts a thorough retrospective, celebrates achievements, and ensures team members transition smoothly to new assignments.

For distributed teams — the norm in 2040 — additional dynamics apply: timezone friction, text-only communication bias, reduced social bonding, and the risk of "out of sight, out of mind" exclusion from organisational decision-making.

### Required Reading

- Tuckman, B. (1965/2035), "Developmental Sequence in Small Groups," *Psychological Bulletin*, annotated reissue.
- DeMarco, T. & Lister, T. (2039), *Peopleware: Productive Projects and Teams*, 4th ed., Addison-Wesley.
- Google re:Work, *Project Aristotle: Understanding Team Effectiveness*, 2038 findings.

### Discussion Questions

1. A project team is stuck in the Storming phase with two senior engineers in sustained conflict. What interventions are appropriate at the PM, sponsor, and HR levels?
2. How does resource levelling conflict with Agile principles of stable, dedicated teams?
3. Project Aristotle found that psychological safety was the strongest predictor of team performance. How would you measure and cultivate this in a distributed IT team?

---

## Lecture 7: Risk Management — Seeing the Rocks Before They See You

### The Risk Management Process

Risk management is the discipline of identifying, analysing, and responding to uncertainties that could affect project objectives. It is not a one-time exercise conducted at project initiation and then filed; it is a continuous process integrated into every project status review. The 2040 standard process follows six steps:

1. **Risk Identification** — What could go wrong? (And: what unexpected opportunities could arise?)
2. **Qualitative Analysis** — How likely is each risk? How severe would the impact be? → Probability × Impact matrix
3. **Quantitative Analysis** — For high-priority risks: expected monetary value, decision tree analysis, Monte Carlo simulation
4. **Response Planning** — For each risk above the threshold: avoid, mitigate, transfer, or accept
5. **Response Implementation** — Execute the response plans; allocate contingency reserves
6. **Monitor and Control** — Track identified risks, detect risk triggers, identify new risks, evaluate response effectiveness

For the Yggdrasil Health EHR migration, representative risks include:

| Risk | Probability | Impact | Score | Response |
|------|------------|--------|-------|----------|
| FHIR API version incompatibility with EHR vendor | 60% | High | 0.54 | Mitigate: prototype API integration in Sprint 2, reserve €200K for custom adapter |
| Production data corruption during migration | 15% | Critical | 0.12 | Mitigate: three-phase migration with validation gates; maintain rollback capability for 30 days post-cutover |
| Key engineer resigns mid-project | 25% | Medium | 0.10 | Mitigate: cross-train all team members; maintain documentation; engage contractor bench |
| Regulatory re-certification extends timeline by 3+ months | 40% | High | 0.36 | Mitigate: engage compliance officer from Day 1; pre-submit architecture to regulators for informal review |

### Contingency vs. Management Reserve

The PMBOK distinguishes between **contingency reserve** (for identified risks — "known unknowns") and **management reserve** (for unidentified risks — "unknown unknowns"). In the Yggdrasil Health project, the contingency reserve might be €250K (16% of the non-personnel budget), calculated via expected monetary value analysis of the risk register. The management reserve is typically 5-10% of total budget, held by the sponsor, and released only through a formal change request. The 2040 project manager does not view contingency draw-down as failure — unused contingency suggests the risk register was either too pessimistic or the project was lucky; neither is a reliable basis for future planning.

### Required Reading

- PMI, *PMBOK Guide*, 8th Ed., Ch. 11: Project Risk Management.
- Hillson, D. (2038), *Managing Risk in Projects*, 2nd ed., Gower.
- Taleb, N.N. (2036), *Antifragile in IT: Building Systems That Gain from Disorder*, adapted edition, Random House.

### Discussion Questions

1. What is the difference between a risk, an issue, and an assumption? Why does confusing these three categories cause project management failures?
2. A sponsor refuses to approve a contingency reserve of 16%, calling it "padding." How do you make the case?
3. How should risk management differ for a fixed-price contract vs. a time-and-materials contract vs. an internal IT project?

---

## Lecture 8: Stakeholder Management and Communication

### The Stakeholder Ecosystem

A stakeholder is anyone who can affect or be affected by the project. The 2040 project manager maps stakeholders using a **Power-Interest Grid**:

```
High Power  |  Keep Satisfied          |  Manage Closely
            |  (CISO, Compliance       |  (CIO, CMO,
            |   Officer, EHR Vendor)   |   AWS Account Team)
            |                          |
Low Power   |  Monitor                 |  Keep Informed
            |  (End users,             |  (Development team,
            |   Help desk staff)       |   QA team, Operations)
            |
            +---------------------------------------
               Low Interest             High Interest
```

The grid determines engagement strategy: high-power, high-interest stakeholders require face-to-face briefings and decision-making involvement; low-power, high-interest stakeholders need regular status updates; high-power, low-interest stakeholders need concise summaries timed to when they need to exercise their power (budget approvals, gate reviews); low-power, low-interest stakeholders need minimal communication unless the project affects them directly.

### Communication Planning

A project communication plan defines: who needs what information, in what format, at what frequency, and through what channel. The 2040 template includes:

| Stakeholder | Information Need | Format | Frequency | Channel |
|-------------|-----------------|--------|-----------|---------|
| CIO | Budget status, milestone health, critical risks | Executive dashboard + 15-minute verbal | Monthly | In-person + email |
| CISO | Security control status, vulnerability findings | Detailed report with CVSS scores | Bi-weekly | Secure portal |
| Development Team | Sprint goals, backlog priorities, blocker resolution | Sprint board + daily standup | Daily/Per-sprint | Jira + Slack |
| End Users | Training schedule, downtime notifications, new features | FAQ + short video | As needed | Internal wiki + email |
| Regulator | Compliance evidence, audit trail | Formal submission package | Quarterly | Regulatory portal |

### Required Reading

- PMI, *PMBOK Guide*, 8th Ed., Ch. 13: Project Stakeholder Management.
- Bourne, L. (2038), *Stakeholder Relationship Management*, 3rd ed., Gower.
- Carnegie, D. (1936/2039), *How to Win Friends and Influence People in the Digital Age*, adapted edition.

### Discussion Questions

1. A powerful stakeholder is disengaged but becomes hostile when decisions are made without their input. How do you manage this pattern?
2. What communication strategies work for distributed teams across 8+ time zones?
3. How do you handle a stakeholder who consistently provides requirements verbally but refuses to approve written specifications?

---

## Lecture 9: Budgeting, Procurement, and Vendor Management

### IT Budgeting in the Cloud Era

IT project budgeting in 2040 differs fundamentally from the capital-expenditure (CapEx) model of the on-premises era. Cloud computing transformed infrastructure costs from CapEx (buy servers, depreciate over 3-5 years) to Operational Expenditure (OpEx — pay per second/minute/hour of usage). This shift reduces upfront costs but introduces budget variability: a misconfigured auto-scaling group, a forgotten test environment, or a cryptocurrency mining attack on a compromised account can generate six-figure monthly cloud bills. The 2040 project manager budgets cloud costs using:
- **Pricing calculators** (AWS Pricing Calculator, Azure Pricing Calculator, GCP Pricing Calculator)
- **Reserved capacity analysis**: 1-year or 3-year commitments reduce costs by 30-60% vs. on-demand
- **FinOps practices**: Tagging all resources by project, environment, and cost centre; setting budget alerts at 50%, 80%, and 100% of monthly allocation
- **Architecture cost optimisation**: Right-sizing instances, implementing auto-scaling based on actual load patterns, using spot/preemptible instances for fault-tolerant workloads

### Procurement and Vendor Management

Most IT projects involve external vendors: cloud providers, SaaS subscriptions, professional services, hardware suppliers, and software licensors. The 2040 project manager manages these relationships through:
- **Request for Proposal (RFP) process**: Define requirements, issue RFP, evaluate responses against weighted criteria (cost, technical fit, vendor stability, support SLA, security posture), negotiate, contract
- **Service Level Agreements (SLAs)**: Availability commitments (99.9%, 99.99%, 99.999%), response times (P1: 15 min, P2: 1 hr, P3: 4 hrs, P4: 24 hrs), credit mechanisms for SLA breaches
- **Vendor risk assessment**: Financial stability, security certifications (SOC 2 Type II, ISO 27001, FedRAMP), data residency compliance, subcontractor management, and exit strategy (how do we get our data back?)

### Required Reading

- Fuller, M., Crawford, J. & Shafer, A. (2039), *Cloud FinOps: Collaborative, Real-Time Cloud Financial Management*, O'Reilly.
- PMI, *PMBOK Guide*, 8th Ed., Ch. 12: Project Procurement Management.
- ISACA, *Vendor Risk Management in the Cloud Era*, 2040.

### Discussion Questions

1. A cloud migration's monthly costs are running 40% above budget due to a misconfigured Kubernetes cluster. Walk through your response as project manager.
2. Your primary vendor declares bankruptcy mid-project. What provisions should have been in the contract?
3. Compare the RFP process for a cloud migration (professional services) vs. a SaaS subscription (standardised product). How does the procurement approach differ?

---

## Lecture 10: Monitoring, Control, and Earned Value Management

### Beyond "Green/Yellow/Red"

Project status reporting that relies on subjective "green/yellow/red" traffic-light indicators is the bane of effective project control. Green means "on track" — but by whose assessment? Yellow means "at risk" — but which risk, how severe, and what is the mitigation? Red means "in trouble" — but what specific corrective action is underway? The 2040 project manager replaces traffic lights with quantitative metrics, the most rigorous of which is **Earned Value Management (EVM)**.

### Earned Value Management

EVM integrates scope, schedule, and cost into three core metrics:

- **Planned Value (PV)**: The budgeted cost of work scheduled to be completed by this date
- **Earned Value (EV)**: The budgeted cost of work actually completed
- **Actual Cost (AC)**: The actual cost incurred for the work performed

From these, four variance and index metrics are derived:

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| Schedule Variance (SV) | EV - PV | Positive = ahead of schedule |
| Cost Variance (CV) | EV - AC | Positive = under budget |
| Schedule Performance Index (SPI) | EV / PV | >1.0 = ahead; <1.0 = behind |
| Cost Performance Index (CPI) | EV / AC | >1.0 = under budget; <1.0 = over budget |

For the Yggdrasil Health migration at Month 6:

```
PV (budget for planned work at Month 6) = €1,800,000
EV (budget for completed work)           = €1,620,000
AC (actual cost incurred)                = €1,950,000

SV = 1,620,000 - 1,800,000 = -€180,000 (behind schedule)
CV = 1,620,000 - 1,950,000 = -€330,000 (over budget)
SPI = 1,620,000 / 1,800,000 = 0.90 (90% of planned schedule rate)
CPI = 1,620,000 / 1,950,000 = 0.83 (spending €1.20 for every €1.00 of value)

Estimate at Completion (EAC) = Budget / CPI = €4,200,000 / 0.83 = €5,060,000
```

The project is 10% behind schedule and 17% over budget. Without corrective action, it will complete at €5.06M — €860K over the original budget. The project manager presents these hard numbers at the steering committee, rather than a vague "project is yellow," and proposes specific corrective actions (crash the testing phase by adding two QA contractors; fast-track the API integration by overlapping design and build phases, accepting the risk of rework).

### Required Reading

- PMI, *Practice Standard for Earned Value Management*, 3rd Ed. (2039).
- Fleming, Q. & Koppelman, J. (2038), *Earned Value Project Management*, 5th ed., PMI.
- PMI, *PMBOK Guide*, 8th Ed., Ch. 7: Project Cost Management.

### Discussion Questions

1. EVM requires detailed task-level cost and schedule tracking. Is this overhead justified for a 3-month, 3-person IT project?
2. If SPI = 1.05 and CPI = 0.78, what is the most likely project situation, and what corrective actions are appropriate?
3. Why might a project with "green" traffic-light status have an SPI of 0.75? What does this reveal about traffic-light reporting?

---

## Lecture 11: Change Management and Organisational Adoption

### The ITIL Change Management Framework

IT projects deliver technical changes — new systems, migrated data, reconfigured networks, automated workflows. But technical change without organisational adoption is waste. The ITIL 4 Change Management practice (evolved from the ITIL v3 Change Management process) structures changes into three categories:

- **Standard Changes**: Pre-authorised, low-risk, routine. Follow a defined procedure (e.g., monthly patching, user provisioning). No additional approval needed.
- **Normal Changes**: Non-standard, need assessment and authorisation through a Change Advisory Board (CAB) or automated change authority. Most project changes fall here.
- **Emergency Changes**: Urgent changes needed to restore service or prevent imminent harm. Expedited CAB (eCAB) review, possibly retrospective.

For the Yggdrasil Health EHR migration, the go-live cutover is a **major normal change** requiring: a detailed change plan, rollback procedure, communication plan, CAB approval, and a defined change window (Saturday 02:00-06:00 UTC, the lowest-traffic period). Post-implementation review (PIR) occurs 72 hours after cutover to confirm the change achieved its objectives without unintended consequences.

### The Human Side: ADKAR and Kotter

Technical change succeeds only when people change their behaviour. Two frameworks guide the 2040 project manager:

**ADKAR (Prosci)**:
- **Awareness** of the need for change
- **Desire** to participate and support the change
- **Knowledge** of how to change (training, documentation)
- **Ability** to implement required skills and behaviours
- **Reinforcement** to sustain the change (recognition, measurement, correction)

**Kotter's 8-Step Model**:
1. Create urgency
2. Build a guiding coalition
3. Form a strategic vision
4. Enlist a volunteer army
5. Enable action by removing barriers
6. Generate short-term wins
7. Sustain acceleration
8. Institute change

For IT projects, resistance is not a moral failing. It is a predictable response to loss of autonomy, competence threat, and uncertainty. The project manager addresses resistance through transparency ("here is exactly what will change and when"), participation ("here is how you can influence the design"), and support ("here is the training and help desk that will support you").

### Required Reading

- Axelos, *ITIL 4: Change Enablement Practice Guide*, 2040 Edition.
- Hiatt, J. (2038), *ADKAR: A Model for Change in Business, Government, and Our Community*, 5th ed., Prosci.
- Kotter, J. (2039), *Leading Change in the Exponential Age*, Harvard Business Review Press.

### Discussion Questions

1. What is the difference between a Change Advisory Board (CAB) and a change authority? When would you use automated change approval?
2. ADKAR and Kotter both describe change management. What does ADKAR capture that Kotter misses, and vice versa?
3. Physicians at Yggdrasil Health resist the new EHR system, claiming it adds 90 seconds to each patient consultation. How do you respond?

---

## Lecture 12: Project Closure, Retrospective, and the Living Legacy

### The Forgotten Phase

Project closure is the most neglected phase of the project lifecycle. Teams are exhausted; sponsors have moved their attention to the next crisis; the pressure to declare victory and disperse is intense. Yet disciplined closure is where organisational learning occurs and where the project's value is formally confirmed or refuted. The 2040 closure process includes:

1. **Formal acceptance**: The sponsor (or designated acceptance authority) signs off that all deliverables meet acceptance criteria. This is a contractual and governance moment — until acceptance, the project is not "done" regardless of what the team believes.
2. **Administrative closure**: Contracts are closed, vendor final payments are processed, team members are released to their next assignments, project-specific cloud resources that are no longer needed are deprovisioned (the most commonly forgotten step — orphaned resources accumulate cloud costs indefinitely).
3. **Financial closure**: Final actual costs are reconciled against budget. The project manager produces a variance analysis explaining deviations >10%.
4. **Knowledge transfer**: Operational documentation, runbooks, architecture diagrams, and access credentials are formally handed over to the operational team. The project manager verifies that the ops team can perform at least one full cycle of each operational procedure (patching, backup restore, incident response) without project team assistance.
5. **Benefits realisation plan**: Defines who will measure what benefits, at what intervals, for how long. Three months post-go-live, the project manager (or PMO) reviews: is the 34% TCO reduction materialising?

### The Retrospective

The retrospective (or post-mortem, or lessons learned session) is the project's final gift to the organisation. Conducted as a facilitated workshop with the full project team and key stakeholders, it addresses:

- **What went well?** — Practises to preserve and propagate
- **What went badly?** — Problems whose root causes should be addressed
- **What surprised us?** — Unknown unknowns that became known; update the risk identification checklist
- **What would we do differently?** — Specific, actionable recommendations for future projects

The 2040 retrospective is recorded in a searchable lessons-learned database (Confluence, Notion, or a dedicated LLR tool like Retrium or Parabol) tagged by technology domain, project size, and failure pattern. An AI system analyses new project charters against this database and surfaces relevant lessons — but the human PM retains responsibility for judging applicability.

### The Heathen Reflection: A Ship Well Sailed

The Old Norse conception of a successful voyage was not that nothing went wrong — storms will come, oars will break, navigational stars will be obscured — but that the crew responded with skill, coordination, and courage. The same is true of IT projects. The measure of a project manager is not the absence of problems but the quality of the response to problems. A project that encountered five major risks, activated contingency plans for all five, and delivered with a 12% budget overrun may represent far better project management than a project that encountered no risks, had no contingency plans, and delivered on budget through sheer luck.

The longship analogy compresses the entire course into a single image: the project manager is the steersman, navigating by the stars of the business case and the shoreline of stakeholder expectations, adjusting course as winds shift (scope changes) and currents shift (organisational politics), maintaining the rhythm of the rowers (team motivation and velocity), and ultimately delivering the crew (the project team) and the cargo (the project deliverables) safely to the destination — or, when the destination changes mid-voyage, communicating that the new destination requires new provisions, and negotiating for them before the crew perishes of exhaustion.

### Required Reading

- PMI, *PMBOK Guide*, 8th Ed., Ch. 4: Close Project or Phase.
- Derby, E. & Larsen, D. (2039), *Agile Retrospectives: Making Good Teams Great*, 3rd ed., Pragmatic Bookshelf.
- Kerth, N. (2037), *Project Retrospectives: A Handbook for Team Reviews*, 2nd ed., Dorset House.

### Discussion Questions

1. Why is project closure systematically neglected, and what organisational incentives would change this?
2. A retrospective surfaces that "the vendor promised X but delivered Y." The lesson is clear but the vendor has a monopoly on the technology. How do you make this lesson actionable?
3. What metrics would you use to evaluate whether a project achieved its benefits — one year after closure? Who should be accountable for this measurement?

---

## Final Examination Preparation

The final examination for IT303 consists of two components:

### Component A: Written Examination (60%)

Choose **four** of the following eight essay questions. Each essay should be 500-750 words and demonstrate synthesis across multiple lectures.

1. The Standish Group reports that IT project success rates have barely improved in 30 years. Analyse the systemic causes of this stagnation and propose three evidence-based interventions that could materially improve success rates by 2050.

2. You are appointed project manager for Yggdrasil Health's EHR cloud migration (as described throughout this course). Produce a complete project management plan covering: scope statement, WBS (at least Level 2), risk register (at least six risks with responses), stakeholder engagement strategy, and communication plan. Justify each element.

3. Compare and contrast Earned Value Management (EVM) with Agile velocity tracking as project control mechanisms. Under what circumstances would you use each? What does EVM capture that velocity misses, and vice versa?

4. A project is at Month 8 of a planned 14-month duration. EV = €2.1M, PV = €2.6M, AC = €2.4M. Calculate SV, CV, SPI, CPI, EAC, and Estimated Completion Date. Interpret each metric. What three specific corrective actions would you recommend to the sponsor?

5. Critically evaluate the claim that "Agile has become the new waterfall — a rigid, ceremony-heavy methodology imposed by management without genuine team empowerment." What evidence supports this critique, and what practices distinguish substantive Agile from ceremonial Agile?

6. The ADKAR model identifies five stages of individual change. Apply this model to the Yggdrasil Health physicians who will transition from a legacy EHR to the new cloud-based system. For each stage, describe specific interventions the project manager should implement.

7. Design a vendor selection process for choosing between three competing cloud migration consultancies. Define evaluation criteria, weighting, scoring methodology, and the decision-making framework. Address how you would handle a scenario where the highest-scoring vendor is 40% more expensive than the second-highest.

8. A project retrospective reveals that the primary cause of schedule delay was a "failure to escalate risks promptly." Analyse the organisational and psychological factors that inhibit risk escalation, and design a risk escalation protocol that would prevent recurrence.

### Component B: Simulation Exercise (40%)

Students participate in a 4-hour project simulation using a project management simulation platform (SimProject 2040 or equivalent). The simulation presents Yggdrasil Health's EHR migration with injected events:
- Month 3: The EHR vendor announces a mandatory API upgrade that invalidates 40% of completed integration work
- Month 6: The lead cloud architect resigns; replacement requires 6 weeks to hire
- Month 9: The CISO demands a full penetration test before go-live, adding 4 weeks to the schedule
- Month 11: A critical production incident requires diverting 50% of the migration team for 3 weeks

Students must respond to each event in real time, updating the project plan, communicating with simulated stakeholders, and making trade-off decisions. Assessment criteria: speed and appropriateness of response, quality of stakeholder communication, fiscal responsibility, and final project outcome.

### Grading Rubric

| Criterion | Weight | Excellent (A) | Good (B) | Adequate (C) | Insufficient (D/F) |
|-----------|--------|---------------|----------|--------------|-------------------|
| Framework application | 30% | Correct and nuanced use of PMBOK, Agile, ITIL frameworks | Mostly correct; minor framework errors | Basic understanding; formulaic application | Frameworks misapplied or absent |
| Quantitative analysis | 25% | Accurate EVM, Monte Carlo, or ROI calculations with interpretation | Minor calculation errors; reasonable interpretation | Significant calculation errors | No quantitative analysis |
| Stakeholder reasoning | 25% | Demonstrates understanding of stakeholder motivations, power dynamics, and communication needs | Adequate stakeholder consideration | Superficial stakeholder treatment | Ignores stakeholder dimension |
| Communication quality | 20% | Clear, professional, well-structured, persuasive | Clear but some organisational issues | Disorganised but comprehensible | Incoherent or unprofessional |

---

## Course Resources

### Primary Textbooks
- Project Management Institute (2039), *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*, 8th Edition.
- Axelos (2040), *PRINCE2 2040: Managing Successful Projects*.
- Schwaber, K. & Sutherland, J. (2040), *The Scrum Guide*, 2040 Edition.

### Supplemental Texts
- Flyvbjerg, B. (2039), *How Big Things Get Done*, 2nd ed., Crown Business.
- DeMarco, T. & Lister, T. (2039), *Peopleware*, 4th ed., Addison-Wesley.
- Fleming, Q. & Koppelman, J. (2038), *Earned Value Project Management*, 5th ed., PMI.
- Hiatt, J. (2038), *ADKAR*, 5th ed., Prosci.
- Derby, E. & Larsen, D. (2039), *Agile Retrospectives*, 3rd ed., Pragmatic Bookshelf.

### Tools
- **Planning & Scheduling**: Microsoft Project 2040, Smartsheet, Jira Advanced Roadmaps, LiquidPlanner
- **Agile/Kanban**: Jira Software, Linear, Trello, Azure DevOps, Monday.com
- **EVM & Analytics**: Deltek Cobra, EcoSys, custom Python/R dashboards
- **Communication**: Slack, Microsoft Teams, Zoom, Loom (async video)
- **Documentation**: Confluence, Notion, GitBook
- **Simulation**: SimProject 2040, @RISK (Monte Carlo), ProjectLibre

---

*ᚱ — Rétt skal stýra.* Steer true.

*Course designed and maintained by the Faculty of Information Technology, University of Yggdrasil, 2040.*
