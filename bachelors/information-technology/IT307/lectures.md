# IT307: IT Service Management — The Stewardship of Digital Services

**Program:** Bachelor of Information Technology, Year 3  
**Credits:** 4 ECTS  
**Prerequisites:** IT201, IT203  
**Instructor:** Prof. Björn Haraldsson, ITIL 4 Master, ISO 20000 Lead Auditor  
**Office:** Heorot Hall, Room 318  
**Semester:** Spring 2041  

> *"A service is not a server. It is not an application. It is the co-creation of value between a provider and a consumer, facilitated by technology but defined by outcomes."* — From *ITIL 4: The Service Value System*, Axelos, 2040

---

## Course Description

IT Service Management (ITSM) is the discipline of designing, delivering, managing, and improving the way IT services are consumed by the business. This course teaches the global standard framework — ITIL 4 — alongside complementary practices: ISO/IEC 20000 (the international standard for service management), DevOps integration, Site Reliability Engineering (SRE), and the emerging AIOps paradigm where machine learning augments service desk, monitoring, and incident management. Students will configure a service desk tool (Jira Service Management, ServiceNow), define a service catalogue, author SLAs and OLAs, design a change management workflow, and build a continual improvement register — the practical toolkit of the 2040 ITSM professional.

---

## Lecture 1: What Is a Service? The ITIL 4 Service Value System

### Beyond the Server Room

The foundational shift in ITSM thinking — crystallised in ITIL 4 (2019, updated through 2040) — is from managing "IT assets" to orchestrating "service value." A service is a means of enabling value co-creation by facilitating outcomes that customers want to achieve, without the customer having to manage specific costs and risks. Yggdrasil Health does not want "a PostgreSQL database with 99.99% availability." It wants "clinicians can access patient records instantly, from any location, with data integrity guaranteed." The database is a component; the service is the outcome.

The ITIL 4 **Service Value System (SVS)** describes how all the organisation's components and activities work together to facilitate value creation. Its five core elements:

1. **Guiding Principles** — Universal recommendations that guide decision-making: Focus on Value, Start Where You Are, Progress Iteratively with Feedback, Collaborate and Promote Visibility, Think and Work Holistically, Keep It Simple and Practical, Optimise and Automate.
2. **Governance** — How the organisation is directed and controlled. The governing body evaluates, directs, and monitors the SVS.
3. **Service Value Chain** — The operating model: six activities (Plan, Improve, Engage, Design & Transition, Obtain/Build, Deliver & Support) that can be combined in value streams.
4. **Continual Improvement** — Ongoing effort to improve products, services, and practices at all levels.
5. **Practices** — 34 management practices grouped into General Management, Service Management, and Technical Management. Key practices include Incident Management, Change Enablement, Service Desk, Problem Management, Service Level Management, and Monitoring & Event Management.

### The Service Value Chain in Action

For Yggdrasil Health's telemedicine service:

```
[Demand: Clinician needs remote patient consultation capability]
         |
    [Engage] ← Stakeholder needs captured
         |
    [Plan]   ← Service design, resource planning, risk assessment
         |
    [Design & Transition] ← Telemedicine platform architected, built, tested
         |                   (FHIR API, video conferencing, EHR integration)
    [Obtain/Build]      ← Platform deployed to production
         |
    [Deliver & Support] ← Service live; incident management, monitoring, support
         |
    [Improve] ← Feedback from clinicians drives iterative enhancements
         |
    [Value: Remote consultations reduce patient travel by 40%]
```

### Required Reading

- Axelos, *ITIL 4 Foundation: Service Value System*, 2040 Edition, Chs. 1-3.
- Axelos, *ITIL 4: Drive Stakeholder Value*, Ch. 1.
- Van Haren, *ITIL 4: A Pocket Guide*, 2039.

### Discussion Questions

1. How does the ITIL 4 emphasis on "value co-creation" change the conversation between IT and business stakeholders compared to an asset-management mindset?
2. Apply the seven Guiding Principles to a scenario where the business demands a new service in four weeks that IT estimates requires twelve weeks.
3. What is the difference between a "value stream" and a "process"? Why does this distinction matter?

---

## Lecture 2: The Service Desk and Incident Management

### The Front Line of IT

The service desk is the single point of contact between service providers and users. In 2040, the service desk has evolved from a phone-and-email operation into an omnichannel, AI-augmented engagement centre:

- **Tier 0 (Self-Service)**: AI chatbots, virtual agents, knowledge base articles, and automated remediation scripts resolve 65-75% of user contacts without human intervention. Natural language understanding (NLU) has advanced to the point where "my email is broken" triggers a diagnostic workflow that checks SMTP connectivity, mailbox quota, and client configuration, resolving the issue or gathering diagnostic data before a human sees the ticket.
- **Tier 1 (Service Desk Analysts)**: Handle incidents not resolved by Tier 0. The 2040 Tier 1 analyst is a diagnostician, not a script-reader — they use AI-suggested resolution steps but exercise judgement when the suggestion is inappropriate.
- **Tier 2 (Technical Specialists)**: Deeper technical expertise; handle escalated incidents and fulfil service requests requiring privileged access.
- **Tier 3 (Vendor/Development)**: Vendor support or development team engagement for software bugs and complex configuration issues.

### Incident Management

An incident is an unplanned interruption to a service or a reduction in service quality. Incident management aims to restore normal service operation as quickly as possible and minimise adverse impact on business operations. Key concepts:

| Concept | Definition | Yggdrasil Health Example |
|---------|------------|--------------------------|
| **Incident** | Unplanned service disruption | Telemedicine video conferencing fails during a patient consultation |
| **Priority** | Impact × Urgency | P1: Critical — affects patient care, immediate response |
| **Major Incident** | Highest impact; requires separate procedure | EHR database corruption; entire hospital affected |
| **Incident Model** | Predefined steps for handling recurring incidents | "VPN connection failure" incident model |
| **Swarming** | Collaborative approach where specialists converge on complex incidents | Cross-team response to performance degradation across multiple services |

The 2040 incident management workflow is heavily automated. An observability platform (Datadog, New Relic, Grafana) detects an anomaly → creates a ticket in the ITSM tool (ServiceNow, Jira Service Management) → enriches the ticket with relevant configuration items from the CMDB, recent changes, and related incidents → pages the on-call engineer via PagerDuty/Opsgenie → the engineer acknowledges and begins diagnosis. Mean Time to Detect (MTTD) and Mean Time to Resolve (MTTR) are the core metrics.

### Required Reading

- Axelos, *ITIL 4 Practice Guide: Service Desk*, 2040 Edition.
- Axelos, *ITIL 4 Practice Guide: Incident Management*, 2040 Edition.
- Kim, G., Behr, K. & Spafford, G. (2039), *The Visible Ops Handbook: Implementing ITIL in Four Practical Steps*, 3rd ed., IT Revolution Press.

### Discussion Questions

1. If Tier 0 resolves 70% of contacts, what skills does the remaining Tier 1 workforce need that differentiate them from what an AI can do?
2. A major incident is declared. Compare the "swarming" approach to a hierarchical escalation model. Which produces faster resolution?
3. What is the difference between MTTD and MTTR? Which is typically harder to reduce, and why?

---

## Lecture 3: Problem Management and Root Cause Analysis

### Incidents vs. Problems

ITIL distinguishes between an **incident** (the symptom — service is degraded) and a **problem** (the cause — a memory leak in the application code). Incident management restores service. Problem management prevents recurrence. The two practices are complementary but must be organisationally separated: the incident manager is optimising for speed of restoration; the problem manager is optimising for thoroughness of root cause identification. Expecting the same person to do both creates a conflict of interest — the urgency of restoration will always trump the patience of root cause analysis.

Problem management operates in three phases:

1. **Problem Identification**: Detect problems through: incident trend analysis (five similar incidents in a week), major incident review (every P1 incident triggers a problem record), proactive detection (monitoring data reveals a growing memory leak before it causes an outage), and supplier/vendor notifications.
2. **Problem Control**: Root cause analysis using techniques such as:
   - **5 Whys**: Iteratively ask "why?" until the root cause emerges (not the first technical cause)
   - **Ishikawa (Fishbone) Diagram**: Categorise potential causes (People, Process, Technology, Suppliers, Environment, Data)
   - **Kepner-Tregoe Analysis**: Structured problem-solving that separates problem definition from solution generation
   - **Chronological Analysis**: Reconstruct the timeline of events leading to the incident
3. **Error Control**: When the root cause is identified, a **Known Error** record is created. Workarounds are documented (for incidents that recur before permanent fix). A **Change Request** is raised to implement the permanent fix. The Known Error Database (KEDB) becomes a searchable repository of known issues and workarounds, reducing future incident resolution time.

### Practical Root Cause Analysis

```
Incident: Telemedicine video calls drop after 12 minutes for 30% of sessions.

5 Whys:
1. Why do calls drop? → The WebRTC connection times out.
2. Why does WebRTC time out? → The STUN/TURN server stops responding.
3. Why does the STUN/TURN server stop responding? → Memory exhaustion on the TURN server.
4. Why memory exhaustion? → TURN server does not release allocated ports for completed sessions.
5. Why are ports not released? → A bug in the TURN server software (version 4.2.1); fixed in 4.2.3.

Root Cause: Unpatched TURN server software with known port leak bug.
Known Error: KE-2021-047 — TURN Server Port Leak, versions <4.2.3.
Workaround: Restart TURN server every 8 hours (reduces frequency but not eliminated).
Permanent Fix: Upgrade TURN server to 4.2.3 (Change Request CR-2847).
```

### Required Reading

- Axelos, *ITIL 4 Practice Guide: Problem Management*, 2040 Edition.
- Kepner, C. & Tregoe, B. (1965/2039), *The New Rational Manager*, updated edition, Kepner-Tregoe Inc.
- Dekker, S. (2038), *The Field Guide to Understanding Human Error*, 4th ed., CRC Press.

### Discussion Questions

1. An organisation has 500 open problem records and assigns one part-time problem manager. Diagnose the organisational issue.
2. When is 5 Whys an inadequate technique for root cause analysis? What are its limitations?
3. How would you convince an incident-focused IT director to invest in problem management, given the near-term pressure to resolve incidents?

---

## Lecture 4: Service Level Management and the Service Catalogue

### The Contract Between IT and Business

Service Level Management (SLM) negotiates, documents, and monitors the agreements between IT service providers and their customers. The hierarchy of agreements:

- **Service Level Agreement (SLA)**: An agreement between the service provider and the customer. Describes the service, its service level targets (availability, performance, response times), responsibilities, and remedies for breach. For Yggdrasil Health: "EHR Service Availability: 99.99% (excluding planned maintenance windows, maximum 4 hours/month, scheduled 48 hours in advance)."
- **Operational Level Agreement (OLA)**: An agreement between internal support groups that underpin the SLA. For the EHR SLA: "Database Team commits to 99.995% database availability; Network Team commits to <1ms latency between application and database tiers."
- **Underpinning Contract (UC)**: A contract with an external supplier that underpins the SLA. "AWS commits to 99.99% availability for the EHR RDS instance (multi-AZ deployment)."

SLAs must be SMART: Specific (exactly which service), Measurable (quantifiable metric), Achievable (realistic), Relevant (to business outcomes), and Time-bound (measured over a defined period — typically monthly or quarterly). An SLA that guarantees "99.999% availability" but takes two weeks to measure and report breaches is operationally useless.

### Service Catalogue

The **Service Catalogue** is the single source of truth for all IT services delivered to the business. It has two views:

- **Business Service Catalogue**: Services described in business language. "Clinical Desktop — provides clinicians with access to patient records, lab results, and clinical decision support from any hospital workstation. Available 24/7. Supported by Service Desk at extension 4500."
- **Technical Service Catalogue**: The technical components that deliver the business service. "Clinical Desktop depends on: EHR Application (EKS-hosted, PostgreSQL RDS), Active Directory (authentication), Citrix Virtual Desktop (presentation layer), Hospital LAN (connectivity), and Workstation Hardware (Dell Optiplex 9040)."

The 2040 Service Catalogue is a living application (ServiceNow CSDM, Jira Service Management Assets, or a custom CMDB) that dynamically links services to their constituent configuration items (CIs), showing real-time health status, recent changes, open incidents, and SLA performance. When a network switch fails, the Service Catalogue immediately surfaces which business services are impacted.

### Required Reading

- Axelos, *ITIL 4 Practice Guide: Service Level Management*, 2040 Edition.
- Axelos, *ITIL 4 Practice Guide: Service Catalogue Management*, 2040 Edition.
- Brooks, P. (2039), *Metrics for IT Service Management: ITSM Library*, Van Haren.

### Discussion Questions

1. An SLA promises "99.9% availability." The service was down for 45 minutes on a Tuesday at 03:00 and for 45 minutes on a Wednesday at 14:00. Was the SLA breached? Should both outages be treated equally?
2. Design the SLA structure for Yggdrasil Health's telemedicine service. What are the appropriate availability, performance, and support response targets?
3. How does a dynamic, CMDB-linked Service Catalogue change incident response compared to a static document?

---

## Lecture 5: Change Enablement and Release Management

### From Change Control to Change Enablement

ITIL 4 renamed "Change Management" to "Change Enablement," reflecting a philosophical shift from gatekeeping ("we must control all changes to prevent risk") to enablement ("we must ensure changes deliver value with acceptable risk"). The 2040 Change Enablement practice balances three competing forces:

- **Speed**: The business demands rapid deployment of new features and fixes. DevOps pipelines deploy multiple times per day.
- **Stability**: Every change introduces risk. The 2038 Google DORA report found that 23% of production incidents were caused by changes.
- **Compliance**: Regulated industries (healthcare, finance) require auditable change records with formal authorisation.

The resolution lies in a risk-based change model:

| Change Type | Risk Profile | Authorisation | Example |
|-------------|-------------|---------------|---------|
| **Standard** | Low, pre-assessed | Pre-authorised; no additional approval | Monthly OS patching (automated), user password reset |
| **Normal — Low Risk** | Medium-low | Peer review; automated testing gate | Application feature deployment via CI/CD |
| **Normal — High Risk** | Medium-high | Change Advisory Board (CAB) or Change Authority | Database schema migration, firewall rule change |
| **Emergency** | Varies (urgency) | Emergency CAB (eCAB) or post-implementation review | Critical security patch for actively exploited vulnerability |

### Release Management

Release management plans, schedules, and controls the build, test, and deployment of releases. The 2040 release management patterns:

- **Continuous Delivery**: Every commit that passes automated tests is deployable. Releases are a business decision, not a technical event. Deployments use blue/green or canary strategies.
- **Feature Flags**: Code is deployed dark (disabled) and gradually enabled for users. Separates deployment (technical) from release (business). If a feature causes problems, it is disabled via flag, not rolled back via deployment — reducing MTTR from hours to seconds.
- **Change Scheduling**: Maintenance windows and change freezes (e.g., no non-emergency changes during the last week of the fiscal year) are managed via a Forward Schedule of Change (FSC), visible to all stakeholders.

```yaml
# Example: Deployment pipeline with canary release and automated rollback
# (Argo Rollouts configuration)
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: patient-api
spec:
  replicas: 6
  strategy:
    canary:
      steps:
      - setWeight: 10    # 10% of traffic to new version
      - pause: {duration: 5m}  # Wait 5 minutes, monitor error rate
      - setWeight: 50    # 50% traffic if healthy
      - pause: {duration: 10m}
      - setWeight: 100   # Full rollout
      autoPromotionEnabled: false  # Manual promotion gate
```

### Required Reading

- Axelos, *ITIL 4 Practice Guide: Change Enablement*, 2040 Edition.
- Axelos, *ITIL 4 Practice Guide: Release Management*, 2040 Edition.
- Humble, J. & Farley, D. (2039), *Continuous Delivery: Reliable Software Releases Through Build, Test, and Deployment Automation*, 3rd ed., Addison-Wesley.

### Discussion Questions

1. "Change Advisory Board" evokes a committee meeting that delays everything. How does the 2040 CAB differ from the ITIL v3 CAB, and is it still necessary?
2. A feature flagged to 5% of users shows a 2% increase in checkout abandonment. What is your response as release manager?
3. How should change enablement differ for a SaaS provider deploying hourly vs. a hospital deploying quarterly?

---

## Lecture 6: Configuration Management and the CMDB

### The Map of the IT Estate

Configuration management ensures that accurate and reliable information about the configuration of services and the CIs (Configuration Items) that support them is available when and where it is needed. A CI is any component that needs to be managed to deliver an IT service: servers, applications, databases, network devices, cloud resources, licences, documentation, and — critically — the relationships between them.

The **Configuration Management Database (CMDB)** is the repository that stores CI records and their relationships. The 2040 CMDB (ServiceNow CMDB, Device42, or a graph database like Neo4j with a custom discovery layer) is automatically populated by **discovery tools** — agents, cloud API calls, and network scans that detect what exists in the environment and reconcile it with what the CMDB says exists. Manual CMDB maintenance has been proven impossible at scale; the only viable 2040 CMDB is a discovered, auto-reconciled CMDB.

The CMDB enables critical ITSM processes:
- **Incident Management**: "Which services are affected by this failed server?"
- **Change Enablement**: "What other CIs depend on this database we are about to migrate?"
- **Problem Management**: "Which CIs share this software version with the known vulnerability?"
- **Asset Management**: "How many Windows Server 2036 licences are in use, and where?"

### The Configuration Model

A well-designed CMDB uses a **Common Service Data Model (CSDM)** — a standardised way of representing services, their components, and their relationships. For Yggdrasil Health, the model might include CI classes: Business Application, Application Service, Database, Server (Physical/Virtual/Cloud), Network Device, Storage Volume, Software Licence, and Document. Each CI has attributes: name, unique identifier, status (Operational, Degraded, Maintenance, Retired), owner, location, criticality, and relationships (Runs On, Depends On, Connects To, Is Part Of).

### Required Reading

- Axelos, *ITIL 4 Practice Guide: Service Configuration Management*, 2040 Edition.
- ServiceNow, *Common Service Data Model (CSDM) 5.0*, Documentation.
- O'Hanlon, C. (2039), *Configuration Management: Theory and Practice for the Cloud Era*, Apress.

### Discussion Questions

1. If the CMDB is auto-discovered, what is the role of the configuration manager compared to a manually maintained CMDB?
2. A server is retired but its CI record persists in the CMDB for six months. What are the operational consequences?
3. How does a graph database (Neo4j) representation of the CMDB differ from a relational database representation in practice?

---

## Lecture 7: Monitoring, Event Management, and AIOps

### The Sensor Network of IT

Monitoring and Event Management observes services and the infrastructure that supports them, detecting conditions that may indicate an issue. The 2040 monitoring stack follows the "three pillars of observability":

- **Metrics**: Numerical measurements collected at regular intervals (CPU utilisation, request latency, error rate, queue depth). Stored in time-series databases (Prometheus, InfluxDB, VictoriaMetrics). Visualised in dashboards (Grafana). Alert thresholds trigger when metrics cross defined boundaries.
- **Logs**: Immutable, timestamped records of discrete events. Structured logging (JSON format, OpenTelemetry standard) enables automated parsing. Centralised log aggregation (Elasticsearch, Loki, Splunk). Full-text search enables forensic investigation.
- **Traces**: Records of a request's journey through distributed systems. Each service adds a span; spans form a trace. Essential for debugging microservices architectures. Jaeger, Zipkin, and cloud-native tools (AWS X-Ray, Google Cloud Trace) visualise trace data.

### From Reactive to Proactive: AIOps

AIOps (Artificial Intelligence for IT Operations) applies machine learning to observability data to: detect anomalies that static thresholds miss (a metric that is "normal" but trending differently from its historical pattern), correlate events across siloed monitoring tools ("the database slowdown coincided with a network latency spike and a load balancer configuration change"), predict incidents before they occur (disk full in X hours at current growth rate), and suggest or automate remediation (runbook automation triggered by specific alert patterns). The 2040 IT operations professional configures and tunes AIOps platforms (Moogsoft, BigPanda, ServiceNow ITOM, Splunk IT Service Intelligence) rather than manually inspecting dashboards.

```python
# Example: Prometheus alerting rule for EHR service latency
# If 95th percentile latency exceeds 500ms for 5 minutes, fire alert
alert: EHRHighLatency
expr: histogram_quantile(0.95, rate(ehr_request_duration_seconds_bucket[5m])) > 0.5
for: 5m
labels:
  severity: warning
  service: ehr-api
annotations:
  summary: "EHR API latency > 500ms (95th percentile)"
  description: "EHR API is experiencing elevated latency. Value: {{ $value }}s"
  runbook_url: "https://wiki.yggdrasil-health.no/runbooks/ehr-high-latency"
```

### Required Reading

- Axelos, *ITIL 4 Practice Guide: Monitoring and Event Management*, 2040 Edition.
- Beyer, B. et al. (2039), *Site Reliability Workbook: Practical Ways to Implement SRE*, O'Reilly, Chs. 5-8.
- Turnbull, J. (2040), *The Art of Monitoring in the AIOps Era*, Turnbull Press.

### Discussion Questions

1. What is the difference between an "event," an "alert," and an "incident" in ITIL 4? Why does conflating them cause alert fatigue?
2. AIOps promises to reduce alert noise. What new risks does AI-augmented incident detection introduce?
3. Design the monitoring strategy for Yggdrasil Health's telemedicine service. What are the critical metrics, log sources, and traces?

---

## Lecture 8: IT Asset Management and Software Licence Compliance

### Knowing What You Have

IT Asset Management (ITAM) manages the full lifecycle of IT assets — hardware, software, cloud resources, and associated contracts — from acquisition through disposal. The 2040 ITAM practice is driven by:

- **Financial Control**: Enterprises spend 3-8% of revenue on IT; ITAM ensures this spend is optimised. Cloud FinOps is the fastest-growing ITAM sub-discipline.
- **Compliance**: Software licence audits (by vendors like Oracle, Microsoft, IBM) can result in seven-figure true-up payments. Licence compliance is not optional.
- **Security**: Unmanaged assets (shadow IT) cannot be patched, monitored, or secured. You cannot protect what you do not know exists.
- **Sustainability**: Asset disposal must meet e-waste regulations (EU WEEE Directive 2040 update); cloud carbon accounting requires asset-to-carbon mapping.

The asset lifecycle: **Request** → **Procure** → **Deploy** → **Manage** (patch, monitor, support) → **Refresh** (upgrade or replace) → **Retire** (secure disposal, licence reclamation, CMDB update). At each stage, the asset record is updated. The 2040 ITAM toolchain (ServiceNow ITAM, Flexera, Snow Software) integrates with: procurement systems (for purchase data), discovery tools (for deployment verification), endpoint management (for configuration and patching status), and cloud provider APIs (for real-time cloud resource inventory).

### Software Asset Management (SAM)

SAM specifically manages software licences, ensuring compliance with vendor terms and optimising licence spend. Complexity drivers in 2040:

- **Cloud-native licensing**: Pay-per-use, pay-per-transaction, and tiered models that differ radically from traditional per-core or per-user licensing.
- **Open-source compliance**: Organisations must track which open-source components are in use, under which licences (GPL, MIT, Apache, BSL), and whether usage complies with licence terms — particularly the SSPL and BSL licences that restrict cloud provider use.
- **AI model licensing**: Foundation models have their own licensing terms (commercial use restrictions, output ownership, data usage policies). The ITAM function must track which models are deployed, under which terms.

### Required Reading

- Axelos, *ITIL 4 Practice Guide: IT Asset Management*, 2040 Edition.
- ISO/IEC 19770-1:2040, *Information Technology — IT Asset Management — Part 1: ITAM Management Systems*.
- Flexera, *State of ITAM Report 2040*.

### Discussion Questions

1. A cloud engineer spins up a GPU cluster for ML training and forgets to terminate it. The monthly bill is €47,000 above forecast. What ITAM and FinOps controls would have prevented this?
2. How does open-source licence compliance differ from proprietary licence compliance in practice?
3. What is the relationship between CMDB and ITAM — are they the same system? If not, how should they integrate?

---

## Lecture 9: Capacity Management and Demand Management

### Balancing Supply and Demand

Capacity management ensures that services have sufficient resources to meet current and agreed future demands, cost-effectively. It operates across three sub-processes:

- **Business Capacity Management**: Forecasts future business demand. "The telemedicine service currently handles 500 consultations/day. The business plan projects 2,000/day within 18 months."
- **Service Capacity Management**: Monitors service performance against SLA targets. "Current average video call connection time: 1.8 seconds. SLA target: <3 seconds. Headroom: 40%."
- **Component Capacity Management**: Monitors individual infrastructure components. "TURN server CPU utilisation: 45% at peak. Current capacity sufficient for 2.2x growth before SLA breach risk."

The 2040 capacity plan is a dynamic model, not a static annual document. Cloud auto-scaling makes capacity elastic — but elasticity is not infinite. AWS accounts have service quotas (maximum number of EC2 instances per region). Kubernetes clusters have resource limits. Database connection pools have maximum sizes. The capacity manager identifies these hard limits and ensures they are raised (or architected around) before they become incidents.

### Demand Management

Demand management influences customer demand for services to align with capacity. Techniques include:
- **Differential pricing**: Charge more for peak-time compute to incentivise off-peak usage
- **Throttling and rate limiting**: Protect services from demand spikes (API gateway rate limiting at 1,000 requests/second per tenant)
- **Service level tiering**: Platinum tier gets guaranteed capacity; Standard tier gets best-effort
- **User education**: "Schedule large data exports during off-peak hours (02:00-06:00 UTC)"

### Required Reading

- Axelos, *ITIL 4 Practice Guide: Capacity and Performance Management*, 2040 Edition.
- Allspaw, J. (2038), *The Art of Capacity Planning: Scaling Web Resources in the Cloud*, 3rd ed., O'Reilly.
- Hightower, K. (2039), *Kubernetes Capacity Planning*, O'Reilly.

### Discussion Questions

1. Cloud auto-scaling creates an illusion of infinite capacity. What are the real physical and economic limits?
2. How should capacity management change for a SaaS provider where the customer base doubles every six months?
3. What is the relationship between capacity management and FinOps? Where do they overlap, and where do they conflict?

---

## Lecture 10: Continual Improvement and the CSI Register

### The Engine of Evolution

Continual Service Improvement (CSI) is the practice of aligning services with changing business needs through the ongoing identification and implementation of improvements. It is not a phase that happens after everything else; it is a thread woven through every practice, every value stream, every service. The ITIL 4 **Continual Improvement Model** defines seven steps:

1. **What is the vision?** — The business objectives the improvement serves
2. **Where are we now?** — Baseline assessment (current state metrics, user satisfaction, cost)
3. **Where do we want to be?** — Target state with measurable improvement targets
4. **How do we get there?** — Improvement plan: actions, resources, timeline, risks
5. **Take action** — Execute the improvement
6. **Did we get there?** — Evaluate results against targets
7. **How do we keep the momentum going?** — Embed the improvement; identify next opportunity

The **Continual Improvement Register (CIR)** is the repository of all improvement opportunities — a backlog maintained by the service owner, prioritised by business value and effort. Every retrospective, every major incident review, every customer satisfaction survey feeds the CIR.

### Practical CSI: Reducing Telemedicine Call Setup Time

```
Vision: Telemedicine consultations are as seamless as in-person visits.
Current State: Average call setup time 8.2 seconds; 95th percentile 22 seconds.
Target State: Average < 3 seconds; 95th percentile < 6 seconds.
Plan: 
  - Upgrade WebRTC signalling infrastructure (2-week project)
  - Move TURN server to edge locations (closer to users) (4-week project)
  - Optimise authentication token exchange (1-week project)
Action: Execute projects in sequence; measure after each.
Evaluation: After 8 weeks — average 2.7s, 95th percentile 5.4s. Target met.
Momentum: Next improvement → reduce call drop rate from 0.8% to <0.2%.
```

### Required Reading

- Axelos, *ITIL 4 Practice Guide: Continual Improvement*, 2040 Edition.
- Imai, M. (1986/2039), *Kaizen: The Key to Competitive Success*, 2nd digital ed., McGraw-Hill.
- Rother, M. (2038), *Toyota Kata: Managing People for Improvement, Adaptiveness, and Superior Results*, 3rd ed., McGraw-Hill.

### Discussion Questions

1. An organisation has a Continual Improvement Register with 200 items, none actioned in 18 months. Diagnose the problem.
2. How do you measure the ROI of a service improvement that reduces user frustration but has no direct cost saving?
3. What is the difference between "continuous" and "continual" improvement, and why did ITIL choose the latter?

---

## Lecture 11: Service Integration and Management (SIAM)

### Managing the Multi-Vendor Ecosystem

Service Integration and Management (SIAM) is the practice of coordinating multiple service providers to deliver a seamless service to the business. In 2040, few IT organisations are single-provider. Yggdrasil Health's IT ecosystem includes:

- **Cloud Providers**: AWS (EHR platform), Azure (Office 365, Active Directory), GCP (AI/ML workloads)
- **SaaS Vendors**: Workday (HR), Salesforce (patient relationship management), ServiceNow (ITSM)
- **Managed Service Providers (MSPs)**: Network operations outsourced to an MSP; security operations co-managed with an MSSP
- **Internal IT**: Service desk, application support, architecture, data engineering

SIAM ensures that these providers operate as a coherent ecosystem rather than a set of silos with finger-pointing between them. The SIAM model can be:

- **Internal SIAM**: The enterprise retains the integration function. Yggdrasil Health employs a SIAM team that manages provider relationships, integrates processes (unified incident management across providers), and maintains the end-to-end service view.
- **External SIAM**: A third-party SIAM provider manages the ecosystem on behalf of the enterprise. Used when the enterprise lacks the scale or expertise.
- **Hybrid SIAM**: Strategic governance remains internal; operational integration is external.

### The SIAM Tooling Layer

SIAM requires a tooling layer that integrates provider data: a single Configuration Management System (CMS) that federates CMDB data from each provider; a unified monitoring dashboard that aggregates alerts from each provider's tools; and an end-to-end service model that shows which provider is responsible for each component. Without this tooling layer, SIAM is a governance aspiration, not an operational reality.

### Required Reading

- Axelos, *ITIL 4 Practice Guide: Service Integration and Management*, 2040 Edition.
- Scopism, *SIAM Foundation Body of Knowledge*, 3rd Ed. (2039).
- Goldstein, M. (2040), *Multi-Sourcing: The SIAM Playbook*, ITSM Press.

### Discussion Questions

1. When a telemedicine outage occurs and three providers are potentially responsible, how does SIAM prevent a "war room of finger-pointing"?
2. Compare internal SIAM vs. external SIAM. What capabilities must the enterprise retain even with an external SIAM provider?
3. How does SIAM change the service level management practice compared to a single-provider environment?

---

## Lecture 12: The ITSM Professional — Synthesis and the Service Ethos

### The Modern ITSM Professional

The 2040 ITSM professional is not a process enforcer but a service architect, a diagnostician, and a business partner. The role synthesises:

- **Framework fluency**: ITIL 4, ISO 20000, COBIT, DevOps, SRE — not as religions but as toolkits from which the professional selects the right practice for the context
- **Technical literacy**: Not necessarily a hands-on engineer, but capable of understanding architecture diagrams, reading monitoring dashboards, querying logs, and asking technically credible questions
- **Business acumen**: Understanding the business's value streams, revenue drivers, regulatory obligations, and competitive landscape — and translating these into service requirements
- **Communication skill**: Translating between "the database response time has increased by 300ms" and "clinicians are experiencing delays in accessing patient records during consultations"
- **Ethical grounding**: Managing services that affect patient health, financial stability, public safety, or national infrastructure demands ethical awareness beyond technical competence

### The Service Ethos — A Heathen Reflection

The Old Norse concept of *þjónusta* (service) carried connotations of mutual obligation — the servant served the master, but the master had reciprocal duties of protection and provision. The ITSM professional serves the business, but the professional's obligation includes speaking truth to power when a demanded service level is technically impossible, when a requested change carries unacceptable risk, or when chronic underinvestment will inevitably cause a service failure. This is not insubordination; it is professional integrity.

The Norns' weaving offers a final metaphor for ITSM: every incident thread, every change thread, every improvement thread is woven into the fabric of service. The ITSM professional does not control the Wyrd — the unexpected will happen, the server will fail, the vendor will have an outage — but ensures that the weaving is resilient: that incidents are detected quickly, that changes are made safely, that improvements are pursued diligently, and that the users' experience of the service, whatever the underlying chaos, is one of reliability and trust.

The 2040 ITSM professional is not measured by the absence of incidents — that is an impossible standard — but by the grace and speed with which service is restored, the depth with which root causes are understood and addressed, and the demonstrable improvement of services over time. This is the service ethos: competence, curiosity, and care.

### Required Reading

- Axelos, *ITIL 4: Direct, Plan, Improve*, 2040 Edition, Chs. 7-9.
- Kim, G., Humble, J., Debois, P., Willis, J. & Forsgren, N. (2039), *The DevOps Handbook: How to Create World-Class Agility, Reliability, & Security*, 3rd ed., IT Revolution Press.
- Brooks, F. (1975/2040), *The Mythical Man-Month: Essays on Software Engineering, 50th Anniversary Edition*, Addison-Wesley, Ch. 16, "No Silver Bullet — Refined and Revisited."

### Discussion Questions

1. What differentiates a great ITSM professional from an adequate one? Identify at least three specific behaviours.
2. How should the ITSM professional respond when directed to implement a service level that is technically impossible with the current infrastructure budget?
3. The Norn metaphor suggests that incidents are inevitable. Does this mindset risk creating complacency ("incidents happen, nothing we can do"), or does it enable healthier incident response?

---

## Final Examination Preparation

The final examination for IT307 consists of two components:

### Component A: Written Examination (60%)

Choose **four** of the following eight essay questions.

1. Critically evaluate the ITIL 4 Service Value System as a framework for managing IT services in a cloud-native, DevOps-oriented 2040 enterprise. What does the SVS capture that DevOps alone does not? What does DevOps capture that the SVS under-emphasises?

2. Yggdrasil Health experiences a major incident: the EHR system is unavailable for 4 hours, affecting all clinical operations. Write the complete incident management response, from detection through resolution to post-incident review. Address: incident categorisation, communication plan, technical diagnosis and resolution, problem management initiation, and stakeholder debrief.

3. Design the Service Level Management framework for Yggdrasil Health. Define: at least five services with SLAs (specifying availability, performance, and support targets), the OLAs underpinning one of those SLAs (at least three support groups), the SLA reporting cadence, and the service review meeting structure.

4. Compare and contrast Change Enablement in a traditional ITIL environment (weekly CAB meetings, manual approval workflows) with Change Enablement in a DevOps environment (continuous delivery, automated testing gates, feature flags). Is the CAB still relevant in 2040? Justify your position.

5. The Yggdrasil Health CMDB contains 12,000 CIs with an estimated 40% accuracy rate. Design a CMDB remediation programme covering: discovery tool selection, reconciliation process, data ownership model, and ongoing maintenance strategy. Address how you would prioritise CI classes for remediation.

6. Select three ITIL 4 practices (beyond Incident, Change, and Problem Management) and analyse their application in a healthcare IT context. For each practice: describe the practice purpose, apply it to a specific Yggdrasil Health scenario, and identify potential implementation pitfalls.

7. Yggdrasil Health operates with four external service providers (AWS, Azure, an MSSP, and a network MSP). Design the SIAM model covering: the SIAM structural model (internal/external/hybrid), the governance framework (provider management, performance monitoring, dispute resolution), the tooling integration architecture, and the end-to-end service reporting approach.

8. Evaluate the impact of AIOps on the ITSM profession. Which ITSM roles will be augmented, which will be transformed, and which (if any) will be made obsolete? What new skills will the 2040 ITSM professional need that the 2020 professional did not?

### Component B: Practical ITSM Configuration (40%)

Students will configure a service desk instance (Jira Service Management or ServiceNow Developer Instance) to support Yggdrasil Health's IT operations, including:

1. **Service Catalogue**: Configure at least five business services with descriptions, SLAs, and support team assignments
2. **Incident Management**: Configure incident workflows, priority matrix, major incident procedure, and automated notifications
3. **Change Enablement**: Configure change types (standard, normal, emergency), CAB approval workflow, and change calendar
4. **Knowledge Base**: Create at least five knowledge articles linked to service catalogue items
5. **Dashboard**: Build a service performance dashboard showing incident volumes, MTTR, SLA compliance, and change success rate

### Grading Rubric

| Criterion | Weight | Excellent (A) | Good (B) | Adequate (C) | Insufficient (D/F) |
|-----------|--------|---------------|----------|--------------|-------------------|
| ITSM framework mastery | 30% | ITIL 4 applied accurately and insightfully | Minor framework errors; generally sound | Basic understanding; formulaic | ITIL misunderstood or ignored |
| Practical operational design | 30% | Designs are specific, realistic, and implementable | Mostly practical; some abstraction | Generic answers without operational detail | Vague or impractical |
| Analytical depth | 20% | Critical analysis; trade-offs evaluated; non-obvious insights | Good analysis; some synthesis | Surface-level only | Descriptive; no analysis |
| Communication | 20% | Clear, well-structured, professional tone | Minor clarity issues | Disorganised but readable | Incoherent |

---

## Course Resources

### Primary Textbooks
- Axelos (2040), *ITIL 4 Foundation*, 2040 Edition.
- Axelos, *ITIL 4 Practice Guides* (34 practice guides), 2040 Editions.
- Van Haren, *ITIL 4: A Pocket Guide*, 2039.

### Supplemental Texts
- Kim, G. et al. (2039), *The DevOps Handbook*, 3rd ed., IT Revolution Press.
- Beyer, B. et al. (2039), *Site Reliability Workbook*, O'Reilly.
- Turnbull, J. (2040), *The Art of Monitoring in the AIOps Era*.
- ISO/IEC 20000-1:2040, *Service Management System Requirements*.
- Brooks, P. (2039), *Metrics for IT Service Management*, Van Haren.

### Tools
- **ITSM Platforms**: ServiceNow, Jira Service Management, BMC Helix, Freshservice
- **Monitoring**: Prometheus, Grafana, Datadog, New Relic, Splunk
- **CMDB Discovery**: ServiceNow Discovery, Device42, AWS Config, Azure Resource Graph
- **AIOps**: Moogsoft, BigPanda, Splunk ITSI, ServiceNow ITOM
- **Automation**: Ansible, Terraform, Rundeck (runbook automation)

---

*ᛏ — Týr er einhendr áss.* Tyr is the one-handed god — sacrifice for the greater order.

*Course designed and maintained by the Faculty of Information Technology, University of Yggdrasil, 2040.*
