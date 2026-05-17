# IT207: IT Service Management
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4  
**Description:** IT Service Management (ITIL, DevOps, SRE)

---

## Lectures

ᚠ **Lecture 1: The IT Service Management Mindset**

**Course:** IT207 — IT Service Management  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

IT Service Management (ITSM) is the discipline of designing, delivering, managing, and improving the way information technology is used within organizations. By 2040, ITSM has evolved from a process-centric framework (ITIL) to a culture of continuous improvement that integrates DevOps practices and Site Reliability Engineering (SRE). This lecture establishes the foundational mindset: IT exists not for its own sake but to enable business outcomes, and every technical decision must be evaluated through the lens of service value.

### Key Topics

- The service mindset: IT as a service provider, not a cost center
- The evolution from ITIL v3 to ITIL 4 and beyond
- DevOps: breaking down silos between development and operations
- SRE: applying software engineering to operations problems
- The 2040 landscape: AI-assisted service management, autonomous remediation, and human-AI collaboration

### Lecture Notes

**The service mindset** reframes IT's role in the organization. Rather than viewing IT as a technical function that implements requests, ITSM treats IT as a service provider that co-creates value with the business. Every service has a **service value chain**: planning, improvement, engagement, design and transition, obtain/build, and deliver/support. The lecture introduces the **Service Value System (SVS)** from ITIL 4, which connects organizational inputs (opportunity, demand) to outputs (value) through guided principles, governance, service value chain activities, and continual improvement.

**ITIL (Information Technology Infrastructure Library)** originated in the UK government (1980s) and became the dominant ITSM framework. **ITIL v3** (2007) organized ITSM around five lifecycle stages: Service Strategy, Service Design, Service Transition, Service Operation, and Continual Service Improvement. **ITIL 4** (2019) shifted to a more holistic, flexible approach, emphasizing the Service Value System, the four dimensions of service management (Organizations and People, Information and Technology, Partners and Suppliers, Value Streams and Processes), and the guiding principles (Focus on Value, Start Where You Are, Progress Iteratively with Feedback, Collaborate and Promote Visibility, Think and Work Holistically, Keep It Simple and Practical, Optimize and Automate). By 2040, **ITIL 5** (2032) has integrated AI governance, quantum-safe service design, and planetary-scale service architectures.

**DevOps** emerged from the Agile software movement (late 2000s) to address the dysfunction between development (measured by feature velocity) and operations (measured by stability). DevOps integrates these goals through shared responsibility, automated pipelines, and cultural change. The **CALMS model** (Culture, Automation, Lean, Measurement, Sharing) summarizes DevOps principles. By 2040, **Platform Engineering** has emerged as the evolution of DevOps: internal developer platforms abstract infrastructure complexity, enabling developers to self-service while maintaining governance.

**SRE (Site Reliability Engineering)**, pioneered by Google (2003, publicized 2016), applies software engineering practices to operations. SRE teams write code to automate toil (repetitive manual work), design for reliability, and manage error budgets. The **error budget** is a revolutionary concept: rather than requiring 100% uptime (which stifles innovation), SRE defines an acceptable level of unreliability (e.g., 99.9% uptime = 0.1% error budget). When the error budget is exhausted, feature launches pause until reliability improves. By 2040, **AI SREs** (covered in IT301) handle routine toil, but human SREs remain essential for architectural decisions and incident command.

**The 2040 landscape** integrates AI into every aspect of service management. **AIOps** (Artificial Intelligence for IT Operations) uses machine learning to correlate alerts, predict failures, and suggest remediations. **Autonomous remediation** (self-healing systems) resolves common issues without human intervention. **Human-AI collaboration** means that AI handles routine decisions (scaling, routing, patching) while humans handle novel, high-stakes decisions (architecture changes, security incidents, ethical dilemmas). The lecture emphasizes that AI augments but does not replace human judgment in ITSM.

### Required Reading

- Axelos (2019). *ITIL Foundation: ITIL 4 Edition*. TSO. (Updated for 2040 context.)
- Kim, G., et al. (2016). *The DevOps Handbook*. IT Revolution Press.
- Beyer, B., et al. (2016). *Site Reliability Engineering*. O'Reilly.
- Yggdrasil ITSM Team (2032). "ITIL 5: Service Management in the Age of AI." *UoY ITSM Research Report*.

### Discussion Questions

1. ITIL 5 integrates AI governance. Should AI decision-making in ITSM be auditable and explainable, or is black-box optimization acceptable for routine operations?
2. The error budget concept accepts some unreliability for innovation speed. For a hospital's patient monitoring system, is any error budget ethically acceptable?
3. Platform Engineering abstracts infrastructure but can create dependency on the platform team. How should organizations balance self-service with platform reliability?
4. AIOps promises to reduce alert fatigue, but can also create complacency. How should organizations maintain human situational awareness when AI handles most routine alerts?

### Practice Problems

- Map the service value chain for a fictional e-commerce platform. Identify inputs, activities, and outputs for each stage. Propose metrics that demonstrate value creation.
- Calculate an error budget for a service with 99.95% SLO. Determine how much downtime is permitted per month and how feature velocity should be adjusted when the budget is exhausted.

---

ᚢ **Lecture 2: ITIL Practices: Service Strategy and Design**

**Course:** IT207 — IT Service Management  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

ITIL 4 defines 34 management practices organized into three categories: service management, technical management, and general management. This lecture covers the practices most relevant to service strategy and design: service portfolio management, service level management, capacity management, availability management, and service design coordination.

### Key Topics

- Service portfolio: pipeline, catalog, and retired services
- Service level management: SLAs, OLAs, and UCs
- Capacity and performance management: demand forecasting and resource planning
- Availability management: HA architectures, resilience, and recovery
- Service design: the four Ps (People, Products, Processes, Partners)

### Lecture Notes

**Service portfolio management** maintains the complete set of services across three states. **Service pipeline**: proposed and in-development services. **Service catalog**: live services available to customers. **Retired services**: decommissioned services with archived data. The portfolio ensures that IT investments align with business strategy and that resources are allocated to the highest-value initiatives. By 2040, **AI portfolio optimization** models the ROI of service investments, accounting for risk, strategic alignment, and resource constraints.

**Service level management** defines, agrees upon, and monitors service targets. **SLAs (Service Level Agreements)** are contracts between IT and customers specifying measurable targets (availability, response time, resolution time). **OLAs (Operational Level Agreements)** are internal agreements between IT teams (e.g., network team promises 4-hour response to server team). **UCs (Underlying Contracts)** are agreements with third-party suppliers. The lecture covers **SLA design**: targets must be achievable, measurable, and meaningful. Unrealistic SLAs (e.g., 99.999% uptime without redundancy) create false expectations. **Penalty clauses** and **credits** enforce SLA compliance, but excessive penalties can strain the IT-business relationship.

**Capacity and performance management** ensures that services have sufficient resources to meet demand. **Demand management** influences customer behavior to smooth demand (e.g., encouraging off-peak usage). **Resource modeling** predicts future capacity needs based on growth trends, seasonality, and planned changes. **Performance tuning** optimizes existing resources (covered in IT203 for databases, and in this lecture for application and infrastructure capacity). By 2040, **predictive capacity management** uses AI to forecast demand 72 hours in advance, automatically provisioning resources before shortages occur.

**Availability management** maximizes service uptime. **Availability** is calculated as: (Total Time - Downtime) / Total Time. **Mean Time Between Failures (MTBF)** measures reliability; **Mean Time To Repair (MTTR)** measures recoverability. High availability requires redundancy: **N+1** (one spare component), **N+2** (two spares), **2N** (fully duplicated). **Recovery objectives**: **RTO (Recovery Time Objective)**—maximum acceptable downtime; **RPO (Recovery Point Objective)**—maximum acceptable data loss. By 2040, **autonomous availability management** (self-healing systems, predictive failure replacement) has reduced MTTR from hours to minutes for common failures.

**Service design** creates new or changed services. The **four Ps** ensure comprehensive design: **People** (skills, roles, training), **Products** (technology, tools, infrastructure), **Processes** (workflows, procedures, metrics), and **Partners** (suppliers, vendors, outsourced functions). The lecture covers **design coordination**: managing dependencies between design activities, ensuring that changes to one component do not break others. By 2040, **digital twins** (virtual models of services) enable design validation in simulation before deployment.

### Required Reading

- Axelos (2019). *ITIL 4: Direct, Plan and Improve*. TSO.
- Axelos (2019). *ITIL 4: Create, Deliver and Support*. TSO.
- Yggdrasil Capacity Management (2035). "Predictive Capacity Management at UoY: From Reactive to Proactive." *UoY Operations Report*.

### Discussion Questions

1. AI portfolio optimization can recommend canceling low-ROI services that have political support. How should organizations balance data-driven recommendations with stakeholder relationships?
2. SLA penalties can incentivize performance but may cause IT to prioritize SLA metrics over genuine service quality. What complementary metrics prevent gaming?
3. Predictive capacity management reduces waste but requires accurate forecasting. For a new service with no historical data, what baseline capacity should be provisioned?
4. Digital twins enable design validation but add modeling overhead. For a simple CRUD application, is twin modeling justified?

### Practice Problems

- Design an SLA for a university learning management system. Define: availability target, response time targets for different request types, support hours, escalation paths, and penalty/credit structure. Ensure targets are achievable given the existing infrastructure.
- Build a capacity forecast for a service expecting 50% user growth over 6 months. Model CPU, memory, storage, and bandwidth requirements. Specify when additional resources should be provisioned to avoid performance degradation.

---

ᚦ **Lecture 3: ITIL Practices: Service Transition and Change Management**

**Course:** IT207 — IT Service Management  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Service transition moves services from design to live operation. This lecture covers change management, release management, deployment management, and the practices that ensure changes are introduced safely and predictably. By 2040, continuous deployment has shortened transition cycles from months to minutes, but the principles of risk management and testing remain essential.

### Key Topics

- Change management: types of change (standard, normal, emergency), CAB, and change models
- Release management: release packaging, scheduling, and communication
- Deployment management: blue-green, canary, feature flags, and rollback
- Knowledge management: documentation, runbooks, and wikis
- Testing: unit, integration, system, acceptance, and chaos engineering

### Lecture Notes

**Change management** controls the lifecycle of changes. **Standard changes**: low-risk, pre-authorized changes (patching, password resets). **Normal changes**: require assessment and authorization by the Change Advisory Board (CAB). **Emergency changes**: rapid authorization for critical fixes (e.g., security patches). By 2040, **AI change risk assessment** analyzes historical data to predict the risk of a change, enabling low-risk changes to be auto-approved and high-risk changes to receive additional scrutiny.

**The CAB (Change Advisory Board)** reviews and authorizes changes. Traditional CABs meet weekly, reviewing all proposed changes. By 2040, **virtual CABs** (asynchronous review via collaboration platforms) and **AI-assisted CABs** (auto-approving low-risk changes, flagging conflicts) have replaced most in-person meetings. However, **major changes** (architecture overhauls, datacenter migrations) still require human deliberation.

**Release management** packages and schedules changes. **Major releases** (quarterly, containing many changes) have given way to **continuous delivery** (daily or hourly small releases). **Release notes** document changes for users and support staff. **Communication plans** ensure stakeholders are informed of upcoming changes. By 2040, **automated release notes** (generated from commit messages, ticket descriptions, and AI summarization) accompany every deployment.

**Deployment management** introduces changes into production. **Blue-green deployment** maintains two identical environments, switching traffic from the old (blue) to the new (green). **Canary deployment** routes a small percentage of traffic to the new version, monitoring for errors before full rollout. **Feature flags** (toggles) enable code to be deployed without being activated, allowing gradual feature rollouts and instant rollback. **Rollback procedures** restore the previous version if the new deployment fails. By 2040, **progressive delivery** (automated canary analysis using AI-driven anomaly detection) is standard for critical services.

**Knowledge management** captures and shares organizational knowledge. **Documentation**: architecture diagrams, API references, and configuration guides. **Runbooks**: step-by-step procedures for common operations (restarting a service, handling an alert). **Wikis** (Confluence, Notion, GitLab Wiki) enable collaborative knowledge creation. **AI knowledge assistants** (e.g., UoY's **Mímir Knowledge Engine**) answer operational questions by querying documentation, runbooks, and historical incidents. By 2040, **generative AI** creates first drafts of documentation from code and configuration, which human experts review and refine.

**Testing** validates that changes work as intended. **Unit tests** verify individual components. **Integration tests** verify component interactions. **System tests** verify end-to-end functionality. **Acceptance tests** verify that the service meets business requirements. **Chaos engineering** (Netflix pioneered) intentionally introduces failures (killing instances, injecting latency, corrupting data) to validate resilience. By 2040, **AI-generated test cases** create comprehensive test suites from requirements documents, and **autonomous chaos agents** continuously test production resilience.

### Required Reading

- Axelos (2019). *ITIL 4: Drive Stakeholder Value*. TSO.
- Humble, J., & Farley, D. (2010). *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*. Addison-Wesley.
- Beyer, B., et al. (2018). *The Site Reliability Workbook*. O'Reilly. Chapter 16 ("Chaos Engineering").
- Yggdrasil Release Engineering (2036). "Progressive Delivery at UoY: From Monthly Releases to Continuous Deployment." *UoY DevOps Report*.

### Discussion Questions

1. AI change risk assessment can auto-approve changes but may miss novel risks. Should all changes require human review, or is the efficiency gain of auto-approval worth the residual risk?
2. Canary deployments reduce blast radius but can expose a subset of users to bugs. How should organizations select canary populations (random, geographic, user segment) to balance risk and representativeness?
3. Generative AI creates documentation drafts, but inaccurate documentation is worse than none. What review processes ensure AI-generated documentation is trustworthy?
4. Chaos engineering intentionally breaks production. For a financial trading system, is chaos engineering reckless, or can it be done safely?

### Practice Problems

- Design a change management process for a cloud-native application. Define: change types, approval workflows, CAB composition, risk assessment criteria, and rollback procedures. Create a change request for a database schema update and walk it through the process.
- Implement a canary deployment pipeline. Deploy a new version to 5% of users, monitor error rates and latency, and automatically promote to 100% if metrics are healthy or rollback if thresholds are breached. Document the pipeline and monitoring dashboards.

---

ᚨ **Lecture 4: ITIL Practices: Service Operation and Incident Management**

**Course:** IT207 — IT Service Management  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Service operation maintains live services, responds to incidents, fulfills requests, and manages problems. This lecture covers incident management, request fulfillment, problem management, and the operational practices that keep services running smoothly.

### Key Topics

- Incident management: detection, logging, categorization, prioritization, diagnosis, resolution, and closure
- Request fulfillment: service requests, self-service portals, and automation
- Problem management: root cause analysis, known error database, and proactive problem prevention
- Event management: monitoring, alerting, and correlation
- Major incident management: war rooms, communication, and post-incident review

### Lecture Notes

**Incident management** restores normal service operation as quickly as possible. The lifecycle: **Detection** (automated alerts, user reports). **Logging** (creating a ticket with timestamp, description, affected service). **Categorization** (classifying by service and symptom). **Prioritization** (based on impact and urgency: Critical = widespread service outage; High = significant degradation; Medium = partial impact; Low = minor inconvenience). **Diagnosis** (identifying cause). **Resolution** (fixing or workaround). **Closure** (verifying restoration, documenting actions). By 2040, **AI incident triage** automatically categorizes, prioritizes, and routes incidents, and **autonomous resolution** handles common issues (disk full → clean temp files; service down → restart; high latency → scale up).

**Request fulfillment** handles routine service requests: password resets, software installations, access requests, and hardware provisioning. **Self-service portals** (ServiceNow, Jira Service Management, UoY's **Yggdrasil Portal**) enable users to submit and track requests. **Automation** handles standard requests without human intervention: **chatbots** resolve password resets; **workflow engines** provision accounts; **configuration management** deploys software. By 2040, **conversational AI** handles 80% of routine requests, escalating only complex or sensitive issues to human agents.

**Problem management** eliminates root causes of incidents. **Reactive problem management** investigates incidents after they occur. **Proactive problem management** identifies and fixes problems before they cause incidents (trend analysis, capacity planning, vulnerability remediation). **Known Error Database (KEDB)**: a repository of documented problems with workarounds and permanent fixes. By 2040, **AI problem prediction** identifies clusters of related incidents and suggests root causes, while **automated problem remediation** applies permanent fixes to prevent recurrence.

**Event management** monitors infrastructure and applications for abnormal conditions. **Events** (state changes) are categorized as **Informational** (normal operation), **Warning** (approaching threshold), and **Exception** (threshold breached). **Alerting** notifies operators of exceptions. **Correlation** groups related events to reduce noise (e.g., a network outage generates hundreds of alerts; correlation produces one "network down" alert). By 2040, **AIOps correlation** (covered in IT203 and IT301) uses ML to identify causal relationships between events, filtering 99% of noise.

**Major incident management** coordinates response to critical outages. **War rooms** (physical or virtual) assemble technical leads, communications, and business stakeholders. **Communication**: regular updates to users, executives, and regulators. **Post-incident review**: blameless analysis with improvement actions. By 2040, **AI war room assistants** (UoY's **Huginn Incident Assistant**) gather data, suggest hypotheses, and draft communications in real time.

### Required Reading

- Axelos (2019). *ITIL 4: Create, Deliver and Support*. TSO. Chapters 4–6.
- Allspaw, J. (2012). "Blameless Postmortems and a Just Culture." *Etsy Code as Craft*.
- Yggdrasil Operations (2039). "The AI War Room: Huginn Incident Assistant in Practice." *UoY Operations Report*.

### Discussion Questions

1. Autonomous incident resolution handles common issues but may apply inappropriate fixes to edge cases. What safeguards prevent AI from worsening incidents?
2. Self-service portals reduce workload but can frustrate users with complex issues. How should organizations design escalation paths that are visible and accessible?
3. Proactive problem management requires investing in fixes before incidents occur. How should organizations justify this preventive spending to budget-conscious leadership?
4. Major incident communication must balance transparency with avoiding panic. What communication cadence and content keep stakeholders informed without causing alarm?

### Practice Problems

- Design an incident management process for a cloud-native microservices platform. Define: severity levels, escalation paths, on-call rotations, communication templates, and post-incident review procedures. Create a runbook for a "database connection pool exhausted" incident.
- Implement a self-service portal for common IT requests. Automate at least three requests (password reset, software installation, access request) using a workflow engine. Measure user satisfaction and request resolution time.

---

ᚱ **Lecture 5: DevOps: Culture, Automation, and Measurement**

**Course:** IT207 — IT Service Management  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

DevOps is both a cultural movement and a set of technical practices. This lecture covers the DevOps lifecycle, the tools that enable it, and the metrics that measure its success. By 2040, DevOps has matured into Platform Engineering, but its core principles remain the foundation of modern IT delivery.

### Key Topics

- The DevOps infinity loop: plan, code, build, test, release, deploy, operate, monitor
- CI/CD pipelines: version control, automated builds, testing, and deployment
- Infrastructure as Code (IaC): Terraform, Ansible, and declarative configuration
- GitOps: version-controlled infrastructure and operations
- DevOps metrics: deployment frequency, lead time, MTTR, and change failure rate

### Lecture Notes

**The DevOps infinity loop** visualizes the continuous flow from planning to monitoring and back. **Plan**: requirements, prioritization, and sprint planning. **Code**: development, peer review, and branch management. **Build**: compilation, packaging, and artifact creation. **Test**: automated and manual validation. **Release**: approval, scheduling, and packaging. **Deploy**: moving artifacts to production. **Operate**: running and maintaining services. **Monitor**: observing behavior and feeding insights back to planning. By 2040, this loop is fully automated for standard changes, with human intervention only for architectural decisions and incident response.

**CI/CD pipelines** automate the build, test, and deployment process. **Version control** (Git, GitHub, GitLab) is the single source of truth. **Automated builds** compile code and create artifacts on every commit. **Automated testing** runs unit, integration, and security tests. **Deployment automation** moves tested artifacts to staging and production. **Pipeline as Code** (Jenkinsfile, GitLab CI, GitHub Actions) defines pipelines in version-controlled files. By 2040, **AI pipeline optimization** automatically parallelizes tests, selects optimal test subsets, and predicts deployment risk.

**Infrastructure as Code (IaC)** manages infrastructure through version-controlled configuration files. **Declarative IaC** (Terraform, CloudFormation, ARM templates) describes desired state; the tool converges actual state to match. **Imperative IaC** (Ansible, Chef, Puppet) executes commands to reach desired state. **Immutable infrastructure** (Packer, container images) replaces rather than modifies servers, eliminating configuration drift. By 2040, **AI-generated IaC** creates infrastructure definitions from natural language requirements, which engineers review and refine.

**GitOps** extends version control to operations. All infrastructure and application changes are made via Git pull requests. An automated agent (Flux, ArgoCD) watches the Git repository and converges the live system to match. GitOps provides: **auditability** (all changes tracked in Git), **reproducibility** (any state can be recreated from a commit), and **rollback** (reverting a commit rolls back the system). By 2040, **GitOps is the default** for Kubernetes and cloud-native deployments.

**DevOps metrics** (DORA metrics, from the DevOps Research and Assessment team) measure performance. **Deployment Frequency**: how often deployments occur (elite = multiple per day). **Lead Time for Changes**: time from commit to production (elite = less than one hour). **Mean Time to Recovery (MTTR)**: time to recover from failure (elite = less than one hour). **Change Failure Rate**: percentage of changes causing incidents (elite = less than 5%). By 2040, **AI-driven DORA dashboards** automatically calculate these metrics and benchmark against industry peers.

### Required Reading

- Kim, G., et al. (2016). *The DevOps Handbook*. IT Revolution Press. Chapters 1–4.
- Morris, K. (2020). *Infrastructure as Code* (2nd Edition). O'Reilly.
- Weaveworks (2040). *GitOps Documentation: Principles and Practices*. weave.works.
- Yggdrasil Platform Team (2037). "From DevOps to Platform Engineering: The UoY Journey." *UoY DevOps Report*.

### Discussion Questions

1. AI pipeline optimization can skip tests it deems unnecessary. What validation ensures that skipped tests do not hide regressions?
2. GitOps provides auditability but requires all changes to go through Git. For emergency fixes (e.g., production outage at 3 AM), is the GitOps overhead acceptable?
3. AI-generated IaC accelerates infrastructure creation but may produce suboptimal designs. Should AI-generated code be treated as a starting point or a final product?
4. DORA metrics benchmark against industry, but every organization is different. Should teams focus on absolute metrics or improvement trends?

### Practice Problems

- Build a CI/CD pipeline for a sample application. Include: automated build, unit tests, integration tests, security scan (SAST), and deployment to a staging environment. Measure pipeline duration and identify bottlenecks.
- Implement GitOps for a Kubernetes application. Store manifests in Git, configure ArgoCD or Flux for automatic synchronization, and demonstrate rollback by reverting a commit. Document the architecture and operational procedures.

---

ᚲ **Lecture 6: Site Reliability Engineering**

**Course:** IT207 — IT Service Management  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

SRE applies software engineering principles to operations problems. This lecture covers the core SRE practices: SLOs, error budgets, toil reduction, and reliability engineering. By 2040, SRE has evolved to include AI-assisted reliability, but the fundamental concepts of quantifying and managing reliability remain unchanged.

### Key Topics

- Service Level Objectives (SLOs): defining and measuring reliability
- Error budgets: balancing reliability and innovation
- Toil: identifying, measuring, and eliminating manual work
- Reliability engineering: graceful degradation, circuit breakers, and bulkheads
- On-call: rotation design, incident response, and burnout prevention

### Lecture Notes

**SLOs (Service Level Objectives)** quantify the desired reliability of a service. Unlike SLAs (external contracts), SLOs are internal targets that guide engineering decisions. An SLO is expressed as a percentage over a time window: "99.9% of requests in the last 30 days completed in under 200ms." SLOs should be **specific** (measurable), **achievable** (based on historical performance), **relevant** (aligned with user experience), and **time-bound** (evaluated over defined windows). The lecture covers **SLI (Service Level Indicator)**: the metric being measured (latency, error rate, throughput). **SLO**: the target value. **SLA**: the external contract (often less stringent than SLO to provide a buffer).

**Error budgets** are the key SRE innovation. If the SLO is 99.9%, the error budget is 0.1% (43.8 minutes of downtime per month). When the budget is consumed, feature launches halt until reliability improves. This aligns incentives: product managers want features, but they also want reliability; the error budget forces a data-driven trade-off. The lecture covers **burn rate**: how fast the error budget is consumed. A **burn rate alert** (e.g., "at current rate, error budget will be exhausted in 3 days") triggers proactive response. By 2040, **AI burn rate prediction** forecasts budget exhaustion 72 hours in advance.

**Toil** is repetitive, manual work that scales linearly with service growth. SRE mandates that each engineer spend no more than 50% of their time on toil (the rest on project work that improves the service). Toil examples: manual deployments, ticket-based provisioning, log analysis, and alert response. **Toil reduction**: automating repetitive tasks, building self-service tools, and improving reliability to reduce alert volume. By 2040, **AI toil elimination** handles routine tasks, but human SREs define what to automate and verify that automation works correctly.

**Reliability engineering** designs systems that fail gracefully. **Graceful degradation**: when overloaded, the system maintains core functionality while disabling non-essential features (e.g., a search engine returns basic results instead of rich snippets under load). **Circuit breakers**: when a dependency fails repeatedly, the circuit breaker stops calling it, allowing the dependency to recover (covered in IT107). **Bulkheads**: isolating failures to a subset of the system (e.g., per-tenant resource limits prevent one tenant from consuming all capacity). By 2040, **AI-driven reliability** automatically adjusts circuit breaker thresholds and bulkhead limits based on real-time conditions.

**On-call** is the operational responsibility of responding to alerts outside business hours. **Rotation design**: fair distribution among team members, with consideration for timezone and personal circumstances. **Incident response**: following runbooks, escalating when needed, and communicating status. **Burnout prevention**: limiting on-call frequency (Google recommends no more than one in four weeks), providing recovery time after incidents, and ensuring that on-call load decreases as automation improves. By 2040, **AI on-call assistants** handle initial triage, but human SREs retain authority for major incidents.

### Required Reading

- Beyer, B., et al. (2016). *Site Reliability Engineering*. O'Reilly. Chapters 2–4.
- Beyer, B., et al. (2018). *The Site Reliability Workbook*. O'Reilly. Chapters 1–3.
- Jones, C., et al. (2021). "SRE: Error Budgets and Toil Budgets." *ACM Queue*, 19(2).
- Yggdrasil SRE Team (2038). "AI Burn Rate Prediction: Preventing Budget Exhaustion Before It Happens." *UoY SRE Report*.

### Discussion Questions

1. AI burn rate prediction is accurate 85% of the time. For the 15% of false predictions, should teams trust the AI and reduce feature velocity, or maintain human judgment?
2. The 50% toil cap ensures project work but may be arbitrary for teams with naturally low toil. Should toil caps be team-specific?
3. Graceful degradation improves availability but reduces functionality. How should product managers define which features are essential vs. non-essential?
4. On-call burnout is a serious occupational hazard. What organizational policies (compensation, rotation limits, post-incident recovery) best prevent burnout?

### Practice Problems

- Define SLOs, SLIs, and error budgets for a university registration system. Calculate burn rates for different failure scenarios. Design an alert that fires when burn rate indicates budget exhaustion within 7 days.
- Identify toil in a provided operations workflow. Quantify the time spent on toil, propose automation, and estimate the time savings. Implement at least one automation and measure its impact.

---

ᚷ **Lecture 7: Monitoring, Observability, and AIOps**

**Course:** IT207 — IT Service Management  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

You cannot manage what you cannot see. This lecture covers the systems and practices that provide visibility into IT services: monitoring, logging, tracing, and the observability platforms that integrate them. By 2040, AIOps has transformed raw telemetry into actionable intelligence.

### Key Topics

- Monitoring: metrics, logs, and traces (the three pillars of observability)
- Observability platforms: Prometheus, Grafana, ELK, Jaeger, and Datadog
- SLI measurement: latency, error rate, throughput, and saturation
- Distributed tracing: OpenTelemetry, span context, and trace analysis
- AIOps: anomaly detection, root cause analysis, and predictive alerting

### Lecture Notes

**Monitoring** collects and displays data about system behavior. **Metrics** (numeric time-series data: CPU usage, request latency, error rate) are the foundation. **Logs** (textual event records) provide context for anomalies. **Traces** (request paths through distributed systems) reveal latency bottlenecks and dependencies. Together, these are the **three pillars of observability**. By 2040, **profiles** (CPU, memory, and I/O profiles) and **eBPF-based kernel events** have become a fourth pillar, providing deep system visibility without instrumentation.

**Observability platforms** integrate the three pillars. **Prometheus** (metrics collection and alerting). **Grafana** (visualization and dashboards). **ELK stack** (Elasticsearch, Logstash, Kibana for log analysis). **Jaeger** (distributed tracing). **Datadog** (commercial integrated platform). By 2040, **unified observability platforms** (OpenTelemetry-based) collect metrics, logs, and traces with a single agent and query language, replacing the fragmented toolchains of the 2020s.

**SLI measurement** requires careful metric selection. **Latency**: time to respond (distinguish average from tail latency—p95, p99). **Error rate**: percentage of failed requests. **Throughput**: requests per second. **Saturation**: how close to capacity (CPU, memory, disk, connections). The **four golden signals** (latency, errors, traffic, saturation) provide a minimal but effective monitoring set. By 2040, **user-centric SLIs** (page load time, transaction completion rate) supplement infrastructure metrics.

**Distributed tracing** follows requests across microservices. **OpenTelemetry** (CNCF project, merged OpenTracing and OpenCensus) provides vendor-neutral instrumentation. **Spans** represent individual operations; **traces** link spans across service boundaries via **context propagation** (trace IDs in headers). Trace analysis identifies: latency bottlenecks (which service is slow), error propagation (which service originated the error), and dependency mapping (which services call which). By 2040, **AI trace analysis** automatically identifies anomalous latency patterns and suggests optimizations.

**AIOps** applies AI to IT operations. **Anomaly detection**: ML models identify metrics that deviate from historical patterns (e.g., unusual CPU spikes, unexpected error rates). **Root cause analysis**: correlating anomalies across metrics, logs, and traces to identify the likely cause. **Predictive alerting**: forecasting failures before they occur (e.g., disk will be full in 3 days). By 2040, **causal AI** (distinguishing correlation from causation) has improved root cause accuracy from 60% to 85%, but human validation remains for critical decisions.

### Required Reading

- Newell, A. (2018). "The Three Pillars of Observability." *Honeycomb Blog*.
- OpenTelemetry (2040). *OpenTelemetry Documentation: Getting Started*. opentelemetry.io.
- Gartner (2038). *Market Guide for AIOps Platforms*. Gartner Research.
- Yggdrasil Observability Team (2039). "Causal AI for Root Cause Analysis: From Correlation to Causation." *UoY AIOps Report*.

### Discussion Questions

1. eBPF provides deep kernel visibility but requires privileged access. For multi-tenant environments, how should eBPF access be controlled?
2. Unified observability platforms reduce tool fragmentation but create vendor lock-in. Should organizations adopt open standards (OpenTelemetry) or commercial integrated platforms?
3. AI anomaly detection can identify subtle deviations but produces false positives. What tuning strategies balance sensitivity with alert fatigue?
4. Causal AI improves root cause analysis but is not perfect. For a critical incident where causal AI suggests a cause with 85% confidence, should engineers investigate alternative causes?

### Practice Problems

- Deploy a monitoring stack (Prometheus + Grafana) for a sample application. Define SLIs, create dashboards, and configure alerts. Measure alert accuracy (true positives vs. false positives) over one week.
- Implement distributed tracing with OpenTelemetry for a microservices application. Identify the slowest span in a trace, optimize it, and measure the latency improvement. Document the trace architecture and instrumentation points.

---

ᚹ **Lecture 8: Configuration Management and Asset Management**

**Course:** IT207 — IT Service Management  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Configuration management ensures that IT assets and their relationships are accurately documented and controlled. This lecture covers the Configuration Management Database (CMDB), configuration items, change control, and the practices that maintain configuration integrity. By 2040, automated discovery and AI-driven relationship mapping have replaced manual CMDB maintenance.

### Key Topics

- Configuration Management Database (CMDB): structure, data model, and maintenance
- Configuration Items (CIs): hardware, software, documentation, and people
- Discovery and mapping: automated asset scanning and dependency mapping
- Change control: versioning, baselines, and rollback
- Asset management: lifecycle, procurement, and disposal

### Lecture Notes

**The CMDB** is the authoritative repository of configuration information. It stores **Configuration Items (CIs)**: any component that needs to be managed (servers, network devices, applications, databases, licenses, documentation, even people in their roles). Each CI has **attributes** (name, version, location, owner) and **relationships** (depends on, connected to, part of). The CMDB enables **impact analysis** (what breaks if this server fails?), **change planning** (which CIs are affected by a proposed change?), and **incident diagnosis** (what changed before this failure?). By 2040, **graph-based CMDBs** (Neo4j, Amazon Neptune) replace relational CMDBs, enabling complex relationship queries.

**Configuration Items** span the entire IT ecosystem. **Hardware CIs**: servers, storage, network devices, workstations, mobile devices. **Software CIs**: operating systems, applications, middleware, patches. **Documentation CIs**: architecture diagrams, runbooks, procedures. **People CIs**: roles, teams, contact information. **Service CIs**: business services, technical services, SLAs. The lecture covers **CI granularity**: too coarse ("the datacenter") lacks actionable detail; too fine ("every process") creates maintenance overhead. The right level depends on the organization's size and complexity.

**Discovery and mapping** populate the CMDB automatically. **Network discovery** (nmap, SNMP scanning) identifies devices. **Agent-based discovery** (installed on endpoints) collects detailed software and hardware inventory. **Cloud discovery** (AWS Config, Azure Resource Graph, Google Cloud Asset Inventory) captures cloud resources. **Dependency mapping** traces connections between CIs (application A uses database B on server C). By 2040, **AI relationship inference** analyzes network traffic, logs, and configuration to discover dependencies without manual documentation.

**Change control** ensures configuration changes are authorized and traceable. **Versioning**: tracking CI state over time (Git for code, CMDB history for infrastructure). **Baselines**: approved configurations that serve as reference points. **Rollback**: restoring previous configurations when changes fail. The lecture covers **configuration drift**: unauthorized changes that deviate from the approved baseline. **Drift detection** (AWS Config Rules, Terraform plan, Chef InSpec) identifies and remediates drift automatically. By 2040, **self-healing configuration** automatically corrects drift within minutes.

**Asset management** tracks the financial and contractual aspects of IT assets. **Lifecycle**: procurement, deployment, operation, maintenance, and disposal. **Procurement**: vendor selection, purchasing, and licensing. **Disposal**: secure data destruction (cryptographic erasure, physical destruction) and environmental compliance (e-waste recycling). By 2040, **circular IT** (refurbishment, reuse, and sustainable disposal) is standard practice at UoY.

### Required Reading

- Axelos (2019). *ITIL 4: Direct, Plan and Improve*. TSO. Chapter 7 ("Configuration Management").
- Microsoft (2040). *Azure CMDB and Asset Management Documentation*. Microsoft Learn.
- AWS (2040). *AWS Config: Configuration and Compliance Monitoring*. AWS Documentation.
- Yggdrasil Asset Management (2037). "AI-Driven CMDB Maintenance: From Manual to Autonomous." *UoY Operations Report*.

### Discussion Questions

1. AI relationship inference can discover dependencies but may miss logical dependencies (e.g., two applications that must be upgraded together). How should CMDBs capture inferred vs. documented relationships?
2. Self-healing configuration corrects drift automatically but may override intentional emergency changes. What exceptions and approval workflows prevent inappropriate rollbacks?
3. Circular IT extends asset lifecycle but may increase support costs for older hardware. What is the optimal replacement cycle for a given total cost of ownership?
4. Graph-based CMDBs enable complex queries but require new skills. For organizations with relational CMDB expertise, is migration worth the learning curve?

### Practice Problems

- Design a CMDB data model for a university IT department. Define CIs, attributes, and relationships for: datacenter infrastructure, cloud resources, business applications, and user devices. Implement the model in a graph database and populate it with sample data.
- Implement automated discovery for a lab environment. Scan the network, collect hardware and software inventory, and map dependencies. Compare the discovered data to manually documented data and identify discrepancies.

---

ᚺ **Lecture 9: IT Governance and Policy**

**Course:** IT207 — IT Service Management  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Governance ensures that IT serves organizational objectives while managing risk and complying with regulations. This lecture covers IT governance frameworks, policy development, and the mechanisms that align IT decisions with business strategy. By 2040, AI governance has become a critical discipline as autonomous systems make increasingly consequential decisions.

### Key Topics

- IT governance frameworks: COBIT, ISO 38500, and NIST CSF
- Policy development: structure, lifecycle, and enforcement
- Risk governance: appetite, tolerance, and escalation
- Compliance governance: regulatory mapping, audit, and certification
- AI governance: explainability, accountability, and bias mitigation

### Lecture Notes

**IT governance** is the system by which organizations direct and control IT. **COBIT (Control Objectives for Information and Related Technologies)**, maintained by ISACA, provides a comprehensive framework for IT governance and management. **ISO 38500** provides principles for effective IT governance. **NIST CSF (Cybersecurity Framework)** organizes cybersecurity activities into five functions: Identify, Protect, Detect, Respond, Recover. The lecture maps these frameworks to practical activities: strategic planning, resource allocation, risk management, and performance measurement.

**Policy development** creates the rules that guide IT behavior. **Structure**: policy (high-level principle), standard (mandatory requirement), procedure (step-by-step process), and guideline (recommendation). **Lifecycle**: draft, review, approve, communicate, enforce, and retire. **Enforcement**: technical controls (configuration management, access controls), procedural controls (audits, reviews), and cultural controls (training, incentives). By 2040, **policy-as-code** (Rego, Open Policy Agent) embeds policies in infrastructure definitions, enabling automated enforcement.

**Risk governance** establishes the organization's approach to risk. **Risk appetite**: the amount of risk the organization is willing to accept (high appetite for innovation, low appetite for regulatory compliance). **Risk tolerance**: the acceptable deviation from risk appetite. **Escalation**: procedures for risks that exceed tolerance. By 2040, **AI risk modeling** (scenario simulation, Monte Carlo analysis) quantifies the probability and impact of complex risk combinations.

**Compliance governance** ensures adherence to laws, regulations, and standards. **Regulatory mapping**: identifying which regulations apply to which systems (GDPR for student data, HIPAA for health data, PCI-DSS for payment data). **Audit**: internal and external assessments of compliance. **Certification**: ISO 27001, SOC 2, and other attestations. By 2040, **continuous compliance monitoring** (automated scanning, policy-as-code, real-time dashboards) has replaced periodic audit cycles.

**AI governance** addresses the unique risks of AI systems. **Explainability**: the ability to understand how AI makes decisions (required by GDPR 2030 and EU AI Act). **Accountability**: assigning responsibility for AI decisions to human owners. **Bias mitigation**: detecting and correcting unfair outcomes. **Safety**: ensuring AI systems do not cause harm. By 2040, the UoY **AI Governance Board** reviews all AI systems before deployment, requiring explainability assessments, bias audits, and human oversight plans.

### Required Reading

- ISACA (2040). *COBIT 2020 Framework and Implementation Guide*. ISACA.
- ISO/IEC (2015). *ISO/IEC 38500:2015 Governance of IT for the Organization*. ISO.
- NIST (2035). *AI Risk Management Framework (AI RMF 1.0)*. NIST.
- Yggdrasil Governance Office (2038). "AI Governance at UoY: Principles, Processes, and Practices." *UoY Governance Report*.

### Discussion Questions

1. Policy-as-code enables automated enforcement but can create rigid rules that block necessary exceptions. How should organizations balance automation with flexibility?
2. AI risk modeling quantifies complex risks but relies on assumptions that may not hold. How should organizations validate AI risk models?
3. Explainability requirements for AI vary by risk level (high-risk AI requires full explainability; low-risk accepts partial). Who should determine the risk level, and what appeals process exists?
4. Continuous compliance monitoring reduces audit burden but increases operational overhead. For a small organization, is continuous compliance cost-effective?

### Practice Problems

- Develop an IT governance framework for a mid-sized company. Map COBIT processes to organizational roles, define decision rights, and create a RACI matrix for key IT decisions.
- Write a set of policies (acceptable use, data classification, incident response) using the policy structure (policy, standard, procedure, guideline). Ensure consistency, enforceability, and alignment with regulatory requirements.

---

ᚾ **Lecture 10: Supplier and Vendor Management**

**Course:** IT207 — IT Service Management  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Modern IT relies on external suppliers for hardware, software, cloud services, and professional services. This lecture covers the practices that manage these relationships: procurement, contract management, performance monitoring, and risk mitigation. By 2040, AI-driven vendor assessment has streamlined due diligence, but human judgment remains essential for strategic partnerships.

### Key Topics

- Supplier lifecycle: selection, onboarding, operation, and offboarding
- Contract management: SLAs, penalties, and exit clauses
- Performance monitoring: KPIs, scorecards, and business reviews
- Risk mitigation: multi-sourcing, vendor audits, and continuity planning
- Strategic partnerships: co-innovation, joint ventures, and ecosystem collaboration

### Lecture Notes

**Supplier selection** evaluates potential vendors against technical, financial, and cultural criteria. **Technical evaluation**: product capabilities, architecture, integration, and scalability. **Financial evaluation**: total cost of ownership, pricing models, and financial stability. **Cultural evaluation**: values alignment, communication style, and responsiveness. By 2040, **AI vendor assessment** analyzes vendor financials, security posture, and customer satisfaction from public and proprietary data, generating risk scores and recommendations.

**Contract management** formalizes the supplier relationship. **SLAs**: service targets, measurement methods, and remediation procedures. **Penalties**: financial consequences for SLA breaches (service credits, termination rights). **Exit clauses**: data portability, transition assistance, and termination fees. The lecture emphasizes **exit planning**: organizations must be able to leave a supplier without operational disruption. By 2040, **smart contracts** (blockchain-based self-executing agreements) automate penalty calculation and payment for measurable SLA breaches.

**Performance monitoring** ensures that suppliers deliver value. **KPIs**: quantitative metrics (uptime, response time, ticket resolution time). **Scorecards**: periodic assessments combining KPIs with qualitative factors (innovation, partnership, communication). **Business reviews**: quarterly or annual meetings to discuss performance, roadmap alignment, and improvement opportunities. By 2040, **continuous vendor monitoring** (real-time SLA dashboards, automated sentiment analysis of support interactions) supplements periodic scorecards.

**Risk mitigation** reduces dependency on individual suppliers. **Multi-sourcing**: using multiple suppliers for critical services (e.g., cloud providers, internet transit). **Vendor audits**: assessing supplier security, compliance, and operational practices. **Continuity planning**: procedures for supplier failure (switching to backup suppliers, activating internal capabilities). The 2033 *Yggdrasil Cloud Provider Outage*—in which a major cloud provider's 12-hour regional failure disrupted research computing—demonstrated the need for multi-cloud continuity.

**Strategic partnerships** go beyond transactional supplier relationships. **Co-innovation**: joint development of new technologies. **Joint ventures**: shared investment in specialized capabilities. **Ecosystem collaboration**: participating in industry consortiums and open-source communities. By 2040, the UoY **Nordic Tech Alliance** (a partnership with 12 universities and 8 technology companies) co-develops educational technology, sharing costs and intellectual property.

### Required Reading

- Axelos (2019). *ITIL 4: Direct, Plan and Improve*. TSO. Chapter 9 ("Supplier Management").
- Gartner (2037). *Magic Quadrant for IT Services and Vendor Management*. Gartner Research.
- Yggdrasil Procurement (2033). "The Cloud Provider Outage: Lessons in Multi-Cloud Continuity." *UoY Operations Postmortem*.
- Yggdrasil Partnership Office (2039). "The Nordic Tech Alliance: A Model for Academic-Industry Collaboration." *UoY Strategic Partnership Report*.

### Discussion Questions

1. AI vendor assessment streamlines due diligence but may miss qualitative factors (cultural fit, strategic vision). Should AI assessment be the primary input or a starting point?
2. Smart contracts automate penalty enforcement but are only as good as the data feeds (oracles) that trigger them. How should oracle reliability be ensured?
3. Multi-sourcing reduces dependency but increases complexity (multiple APIs, data models, and operational procedures). What is the optimal number of suppliers for a critical service?
4. Strategic partnerships create shared intellectual property. How should universities balance open research with proprietary commercial interests?

### Practice Problems

- Evaluate three cloud providers for a university workload. Create a scorecard with technical, financial, and cultural criteria. Assign weights, score each vendor, and recommend a primary and backup provider with justification.
- Design a supplier continuity plan for a critical SaaS application. Specify: backup provider selection criteria, data migration procedures, transition timeline, and fallback to manual processes if automation fails.

---

ᛁ **Lecture 11: Continuous Improvement and Lean IT**

**Course:** IT207 — IT Service Management  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

IT service management is never finished. This lecture covers the methodologies that drive ongoing improvement: Lean principles, Six Sigma, Kaizen, and the Plan-Do-Check-Act cycle. By 2040, AI-assisted improvement identifies optimization opportunities at scale, but human creativity remains the engine of innovation.

### Key Topics

- Lean IT: waste elimination, value stream mapping, and flow optimization
- Six Sigma: DMAIC, statistical process control, and defect reduction
- Kaizen: continuous small improvements and employee empowerment
- PDCA: Plan-Do-Check-Act cycle for iterative improvement
- AI-assisted improvement: pattern recognition, simulation, and recommendation

### Lecture Notes

**Lean IT** applies manufacturing lean principles to IT. **The seven wastes** (adapted from Toyota Production System): **defects** (errors, incidents), **overproduction** (unnecessary features, excess capacity), **waiting** (approval delays, handoff delays), **non-utilized talent** (underusing employee skills), **transportation** (unnecessary data movement), **inventory** (excess work in progress), **motion** (unnecessary context switching), and **extra-processing** (redundant reviews, duplicate data entry). **Value stream mapping**: visualizing the end-to-end process from request to delivery, identifying waste and bottlenecks. **Flow optimization**: reducing batch sizes, eliminating queues, and parallelizing work. By 2040, **AI value stream analysis** automatically identifies waste from process mining data.

**Six Sigma** reduces process variation and defects. **DMAIC**: **Define** (problem, scope, goals), **Measure** (current performance), **Analyze** (root causes), **Improve** (solutions), **Control** (sustain improvements). **Statistical process control**: monitoring process metrics to detect deviation from normal. **Defect reduction**: reducing errors to 3.4 per million opportunities (Six Sigma level). By 2040, **AI Six Sigma** automatically detects process variation, suggests root causes, and simulates improvement scenarios.

**Kaizen** (Japanese for "improvement") empowers employees to make small, continuous improvements. Unlike top-down transformation, Kaizen encourages frontline workers to identify and fix problems in their immediate environment. **Kaizen events**: intensive workshops (typically 3–5 days) focused on a specific process. **Suggestion systems**: formal mechanisms for employees to propose improvements. By 2040, **AI suggestion systems** analyze operational data to recommend improvements, but human judgment selects and implements them.

**PDCA (Plan-Do-Check-Act)** is the iterative improvement cycle. **Plan**: identify an opportunity and design a change. **Do**: implement the change on a small scale. **Check**: measure the results against expectations. **Act**: standardize the change if successful, or iterate if not. PDCA applies to all ITSM processes: incident management (plan a new triage workflow, pilot it, measure resolution times, roll out or refine), change management (plan a new CAB structure, test it, measure change success rates, adjust). By 2040, **AI PDCA automation** runs thousands of micro-experiments in parallel, accelerating improvement cycles.

**AI-assisted improvement** uses machine learning to identify optimization opportunities. **Pattern recognition**: detecting recurring issues, seasonal trends, and systemic weaknesses. **Simulation**: modeling the impact of proposed changes before implementation. **Recommendation**: suggesting improvements based on benchmarks and best practices. The lecture emphasizes that AI suggests, but humans decide: improvement requires understanding organizational context, stakeholder needs, and cultural factors that AI cannot model.

### Required Reading

- Womack, J. P., & Jones, D. T. (2003). *Lean Thinking*. Free Press.
- Pyzdek, T., & Keller, P. (2014). *The Six Sigma Handbook* (4th Edition). McGraw-Hill.
- Imai, M. (1997). *Gemba Kaizen: A Commonsense Approach to a Continuous Improvement Strategy*. McGraw-Hill.
- Yggdrasil Process Improvement (2038). "AI-Assisted PDCA: Running 10,000 Micro-Experiments at UoY." *UoY Operations Report*.

### Discussion Questions

1. AI value stream analysis identifies waste but may miss human factors (morale, creativity, collaboration). How should organizations supplement AI analysis with human judgment?
2. Six Sigma targets 3.4 defects per million, which may be excessive for IT processes where 99% is often sufficient. Is Six Sigma appropriate for all IT processes, or should defect targets be context-specific?
3. Kaizen empowers employees but requires time away from operational duties. How should organizations balance improvement activities with service delivery?
4. AI PDCA automation accelerates improvement but may run experiments that affect live users. What safeguards ensure that automated experiments do not degrade user experience?

### Practice Problems

- Map the value stream for a software deployment process. Identify waste, measure lead time and defect rate, and propose Lean improvements. Implement at least one improvement and measure the impact.
- Apply DMAIC to a recurring IT problem (e.g., slow ticket resolution, frequent password resets). Define the problem, measure current state, analyze root causes, implement improvements, and establish controls to sustain gains.

---

ᛃ **Lecture 12: ITSM in 2040: The Future of Service Management**

**Course:** IT207 — IT Service Management  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

The final lecture synthesizes the course's themes and projects ITSM into the future. By 2040, AI manages routine operations, but human judgment remains essential for strategy, ethics, and innovation. Students will learn to embrace automation while cultivating the skills that make them irreplaceable: creativity, empathy, and ethical reasoning.

### Key Topics

- The autonomous IT organization: AI-managed services, self-healing systems, and human oversight
- The evolving IT professional: from technician to architect, from operator to strategist
- Ethics in ITSM: automation bias, accountability, and the human cost of optimization
- Sustainability: green IT, circular economy, and carbon-aware computing
- The enduring principles: value creation, continuous improvement, and service excellence

### Lecture Notes

**The autonomous IT organization** uses AI to manage routine service management tasks. **AI service desks** handle 90% of incidents without human intervention. **Self-healing systems** detect and correct failures automatically. **Autonomous capacity management** scales resources based on predicted demand. **AI change advisory boards** approve low-risk changes instantly. By 2040, the UoY IT department operates with 60% fewer operational staff than in 2020, but the remaining staff are higher-skilled architects, strategists, and ethicists.

**The evolving IT professional** must adapt to this transformation. **Technicians** who performed routine tasks (patching, provisioning, password resets) have been automated out of existence. **Architects** who design systems, integrate platforms, and optimize workflows are in high demand. **Strategists** who align IT with business goals, manage vendor relationships, and govern AI systems are essential. **Ethicists** who ensure that AI decisions are fair, transparent, and accountable are a new and growing role. The lecture provides a career roadmap: master one technical domain deeply, develop architectural thinking, cultivate business acumen, and engage with ethical questions.

**Ethics in ITSM** addresses the human impact of optimization. **Automation bias**: the tendency to trust AI decisions without critical evaluation. The 2036 *Yggdrasil Routing Incident*—in which an AI system routed all student traffic through a single network path to minimize cost, causing a 4-hour outage during enrollment—demonstrated automation bias. **Accountability**: when AI makes a bad decision, who is responsible? The AI vendor, the IT department, or the executive who approved the system? **Human cost of optimization**: automation can eliminate jobs, deskill workers, and create stress for those who remain. The lecture argues that ITSM must optimize for human flourishing, not just efficiency.

**Sustainability** is an increasingly critical ITSM concern. **Green IT**: reducing energy consumption through efficient hardware, virtualization, and AI-optimized cooling. **Circular economy**: extending hardware life, refurbishing equipment, and recycling e-waste. **Carbon-aware computing**: scheduling workloads during periods of low-carbon energy availability. By 2040, UoY's **Sustainable IT Policy** requires all new services to include a carbon impact assessment and a mitigation plan.

**The enduring principles** of ITSM remain relevant regardless of technology. **Value creation**: IT exists to enable business outcomes, not for its own sake. **Continuous improvement**: services can always be better, faster, cheaper, or more reliable. **Service excellence**: meeting and exceeding customer expectations is the ultimate measure of IT success. The lecture concludes with the **Service Professional's Pledge**, adapted by the UoY IT Guild in 2036: "I pledge to create value through technology, to improve continuously, to respect the humans I serve, and to balance efficiency with empathy, automation with wisdom, and progress with sustainability."

### Required Reading

- Brynjolfsson, E., & McAfee, A. (2014). *The Second Machine Age*. W.W. Norton.
- Yggdrasil Ethics Board (2036). "Automation Bias and Accountability in AI-Driven ITSM." *UoY Ethics Report*.
- Yggdrasil Sustainability Office (2039). "Carbon-Aware Computing: Scheduling Workloads for Planetary Health." *UoY Sustainability Report*.
- Yggdrasil IT Guild (2036). "The Service Professional's Pledge." *UoY IT Ethics Manual*.

### Discussion Questions

1. Autonomous IT organizations require fewer operational staff. What responsibilities do organizations have to retrain or support workers displaced by automation?
2. Automation bias is a cognitive tendency, not a technical failure. Can training programs reduce automation bias, or is it an inherent human limitation?
3. Carbon-aware computing shifts workloads to times and locations with cleaner energy. For latency-sensitive services (e.g., real-time collaboration), is carbon awareness compatible with performance requirements?
4. The Service Professional's Pledge balances efficiency with empathy. For an organization facing financial pressure, is this balance achievable, or does economics override empathy?

### Practice Problems

- Design an autonomous IT service desk for a university. Specify: AI capabilities, human escalation triggers, knowledge base integration, and metrics. Address ethical concerns (automation bias, job displacement, accountability).
- Conduct a carbon impact assessment for a university data center. Estimate current emissions, identify reduction opportunities (efficiency, renewable energy, workload scheduling), and propose a 5-year sustainability roadmap.

---

## Final Examination Preparation

The IT207 final examination is a **comprehensive practical and written assessment** conducted over 48 hours. Students must complete **three of five** challenges:

1. **Service Design**: Design a new IT service for a university department. Define the service value chain, create SLAs and OLAs, design the CMDB structure, and specify monitoring and reporting requirements.
2. **DevOps Transformation**: Transform a traditional IT operations team into a DevOps/SRE model. Specify: cultural changes, CI/CD pipeline design, SLO definitions, error budget policies, and toil reduction plan.
3. **Incident Command**: Lead a simulated major incident (e.g., datacenter outage, ransomware attack). Manage the war room, coordinate technical response, communicate with stakeholders, and conduct a blameless postmortem.
4. **Governance Framework**: Develop an IT governance framework for a multi-national organization. Map regulatory requirements, define policies, create risk assessment methodology, and specify compliance monitoring.
5. **Continuous Improvement Project**: Apply Lean, Six Sigma, or Kaizen to an IT process. Map the value stream, identify waste, measure baseline performance, implement improvements, and demonstrate sustained improvement with statistical evidence.

### Evaluation Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Technical depth | 25% | Accurate application of ITSM frameworks, tools, and practices |
| Strategic thinking | 25% | Alignment of IT decisions with business objectives and risk appetite |
| Communication | 20% | Clear documentation, stakeholder communication, and process design |
| Ethics and sustainability | 15% | Responsible consideration of human impact, bias, and environmental cost |
| Innovation | 15% | Creative or insightful approaches to emerging challenges |

---

*The service never sleeps. The pager rings, the alert fires, and the professional responds—not because they must, but because they have chosen the path of service. In the quiet hours before dawn, when the systems hum and the metrics glow green, there is honor in this vigil.* ᛟ

— Runa Gridweaver Freyjasdottir, IT Service Management, University of Yggdrasil, 2040
