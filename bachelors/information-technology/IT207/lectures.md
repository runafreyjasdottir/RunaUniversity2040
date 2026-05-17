# IT207: IT Service Management — ITIL, DevOps, SRE, and the Craft of Reliable Operations
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4  
**Prerequisites:** IT101 (Introduction to Information Technology), IT201 (System Administration)  
**Description:** A comprehensive examination of IT service management frameworks, operational philosophies, and organizational practices that ensure technology delivers value to the business. Students master ITIL 4 (the dominant service management framework), DevOps culture and practices, Site Reliability Engineering (SRE) methodologies, and the 2040 convergence of these traditions into unified "value stream management." The course emphasizes practical application: designing service catalogs, measuring reliability through SLOs, building CI/CD pipelines, and cultivating the cultural norms that make high-performing IT organizations possible.

**Instructor:** Prof. Einar Servicekeeper, Chair of IT Service Management  
**Lab:** YggLab Operations Studio, Muninn Computing Centre

---

## Lectures

ᚠ **Lecture 1: The Foundations of Service — What Is IT Service Management and Why Does It Matter?**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

Technology without purpose is mere machinery. IT Service Management (ITSM) is the discipline that connects technology to value — ensuring that computing resources, applications, and infrastructure serve the needs of users, customers, and the organization. This lecture establishes the foundational understanding of ITSM: what constitutes a "service," how services are designed and delivered, and why the frameworks, cultures, and metrics of service management distinguish high-performing IT organizations from chaotic technology accumulations.

We trace the evolution of ITSM from the mainframe era (where a single team controlled all computing) through the ITIL revolution (process-driven service management) to the DevOps movement (collaborative, automated delivery) and the SRE tradition (engineering reliability into systems). By 2040, these traditions have converged: ITIL provides the governance framework, DevOps provides the delivery mechanism, and SRE provides the reliability engineering. The IT professional of 2040 must be fluent in all three.

### Key Topics

- **The Service Concept:** A service as a means of enabling value co-creation — not merely delivering a product but facilitating outcomes that users desire
- **The Service Value Chain:** ITIL 4's core activity model: plan, improve, engage, design & transition, obtain/build, deliver & support
- **The Four Dimensions of Service Management:** Organizations & people, information & technology, partners & suppliers, value streams & processes
- **ITIL vs. DevOps vs. SRE:** Complementary rather than competing — ITIL governs, DevOps delivers, SRE operates
- **The 2040 Convergence:** Value Stream Management (VSM) platforms that integrate ITIL governance, DevOps automation, and SRE observability into unified workflows

### Lecture Notes

IT Service Management emerged from the recognition that technology departments were becoming ungovernable. In the 1970s–1980s, IT was a back-office function: a cost center that supported business operations but was not strategically integrated. The 1980s–1990s saw the rise of "IT governance" — frameworks like COBIT (1996) that attempted to bring financial-accounting rigor to technology investments. But governance without delivery is bureaucracy; delivery without governance is chaos. ITIL (Information Technology Infrastructure Library), developed by the UK government's Central Computer and Telecommunications Agency (CCTA) in the 1980s and refined through multiple versions (ITIL v2 2000, v3 2007, v4 2019, v4.5 2030), provided the missing operational framework: a comprehensive set of practices for designing, delivering, and improving IT services.

ITIL 4 (2019; updated 2030) is built around the Service Value System (SVS): inputs (opportunity and demand), activities (the Service Value Chain), enablers (practices, governance, continual improvement), and outputs (value). The Service Value Chain consists of six activities: **Plan** (ensuring shared understanding of vision and strategy), **Improve** (ensuring continual improvement of services and practices), **Engage** (understanding stakeholder needs and managing relationships), **Design & Transition** (ensuring services meet quality and cost expectations), **Obtain/Build** (ensuring service components are available and fit for purpose), and **Deliver & Support** (ensuring services are delivered and supported according to agreements). Unlike the rigid process flows of ITIL v3, the Service Value Chain is flexible: activities can be combined in any sequence appropriate to the work being done.

The Four Dimensions of Service Management remind practitioners that services are not merely technical constructs. **Organizations and People** addresses culture, skills, communication, and teamwork — the human dimension that frameworks often neglect. **Information and Technology** covers the tools, data, and knowledge that enable services. **Partners and Suppliers** recognizes that modern IT depends on a ecosystem of vendors, cloud providers, and open-source communities. **Value Streams and Processes** describes the workflows that convert demand into value. A service that is technically perfect but culturally rejected (e.g., imposed without user consultation) will fail; a service with excellent vendor contracts but poor data management will underperform. All four dimensions must be addressed.

DevOps, emerging from the Agile software development movement (2001) and the systems administration tradition, addresses the chronic dysfunction between "development" (who want to release frequently) and "operations" (who want stability). The 2009 Velocity Conference and the 2010 "DevOps Days" conferences formalized the movement. DevOps is not a methodology but a culture: shared ownership, blameless postmortems, automation of toil, and continuous feedback. The "Three Ways" of DevOps (Kim et al., 2013) are: **Flow** (optimizing the delivery pipeline from left to right), **Feedback** (creating fast feedback loops from right to left), and **Continual Learning** (cultivating a culture of experimentation and improvement). By 2040, DevOps practices (CI/CD, infrastructure as code, automated testing, observability) are standard across the industry — though the cultural transformation remains incomplete in many organizations.

Site Reliability Engineering (SRE), developed at Google (2003–present; publicized 2016), applies software engineering principles to operations. SRE teams write code that operates systems: automation, tooling, and platforms that reduce manual toil. The defining innovation of SRE is the **Service Level Objective (SLO)** — a quantitative reliability target (e.g., "99.9% of requests complete successfully within 200ms") that balances reliability against velocity. The **error budget** — the permissible unreliability (0.1% in the example) — provides a contractual mechanism for managing the tension between "don't break things" and "ship new features." When the error budget is exhausted, feature releases pause until reliability improves. By 2040, SRE practices (SLOs, error budgets, blameless postmortems, chaos engineering) have spread beyond Google to become standard at technology companies and increasingly at traditional enterprises.

The 2040 convergence of ITIL, DevOps, and SRE is driven by Value Stream Management (VSM) platforms (Plutora, ServiceNow, GitLab, and the UoY "Yggdrasil Value Stream" platform). These platforms integrate: ITIL service catalogs and change management, DevOps CI/CD pipelines and deployment automation, and SRE observability and reliability metrics. A service request flows through the platform: user submits request via service catalog → automated provisioning through CI/CD → monitoring via SLO dashboards → continual improvement via feedback loops. The platform provides visibility across the entire value stream, identifying bottlenecks (where do requests wait longest?) and measuring flow efficiency (what percentage of time is value-adding vs. waiting?).

### Required Reading

- AXELOS (2030). *ITIL 4: Foundation Edition*, 2nd Edition. TSO.
- Kim, G., et al. (2033). *The DevOps Handbook*, 3rd Edition. IT Revolution Press.
- Beyer, B., et al. (2035). *Site Reliability Engineering: How Google Runs Production Systems*, 2nd Edition. O'Reilly.
- UoY-IT-TR-2037-77: "Yggdrasil Value Stream: Integrated ITSM, DevOps, and SRE at University Scale."
- Kniberg, H. (2031). *Lean from the Trenches: Managing Large-Scale Projects with Kanban.* Pragmatic Bookshelf.

### Discussion Questions

1. ITIL is often criticized as bureaucratic and slow, while DevOps emphasizes speed and autonomy. Can ITIL governance coexist with DevOps velocity, or do they represent fundamentally incompatible worldviews?

2. SRE error budgets provide a mathematical framework for reliability trade-offs, but they require accurate measurement. For a service with poorly defined "success" (e.g., a research collaboration platform), can SLOs be meaningfully defined?

3. Value Stream Management platforms promise end-to-end visibility but require extensive integration effort. For a mid-size organization with 50 legacy systems, is VSM a realistic goal or an aspirational fantasy?

### Practice Problems

- Design a service catalog for a university IT department with 10 services (email, file storage, VPN, compute cluster, database, web hosting, etc.). For each service, define: description, request process, fulfillment time, SLAs, and escalation path.
- Implement a simple CI/CD pipeline for a sample application using GitLab CI, GitHub Actions, or Jenkins. Include: automated build, unit tests, integration tests, SAST scan, and deployment to a staging environment. Document the pipeline and measure lead time (commit to deploy).

---

ᚢ **Lecture 2: ITIL in Practice — Service Design, Transition, and Operation**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

ITIL is not merely a framework to be memorized but a toolkit to be applied. This lecture covers the practical application of ITIL practices across the service lifecycle: designing services that meet user needs, transitioning them into production without disruption, and operating them reliably while continuously improving. We examine each phase not as an abstract process but as a set of concrete activities, roles, and deliverables that IT professionals use daily.

By 2040, ITIL practices have been refined by decades of application and enriched by integration with Agile, DevOps, and SRE. The lecture emphasizes modern interpretations: change management as "change enablement" (facilitating rather than blocking), incident management integrated with SRE practices, and problem management driven by observability data rather than manual analysis.

### Key Topics

- **Service Design:** Service Level Management (SLM), availability design, capacity planning, security by design, and supplier management
- **Service Transition:** Change enablement, release management, deployment management, knowledge management, and the "shift left" of testing and validation
- **Service Operation:** Incident management, problem management, request fulfillment, event management, and the 2040 "autonomous operations" that use AI to handle routine incidents
- **Continual Improvement:** The continual improvement register, the PDCA (Plan-Do-Check-Act) cycle, and Kaizen-inspired micro-improvements
- **ITIL Practices in 2040:** How 34 ITIL practices map to modern tooling: ServiceNow, Jira Service Management, Freshservice, and the UoY "Mímir Service Desk"

### Lecture Notes

Service Design ensures that services are fit for purpose and fit for use before they enter production. **Service Level Management (SLM)** negotiates targets with customers: not merely uptime percentages but multi-dimensional agreements covering availability, performance, security, and user experience. By 2040, SLAs have evolved into **XLA (Experience Level Agreements)** that measure user sentiment ("How satisfied are you with the service?") alongside technical metrics. **Availability Design** uses techniques like redundancy, failover, and graceful degradation to meet availability targets. **Capacity Planning** forecasts demand and ensures resources can meet it — a discipline transformed by cloud computing (elastic scaling) but still essential for budgeting and reserved capacity. **Security by Design** embeds security requirements from the outset (discussed in IT205, Lecture 8). **Supplier Management** governs relationships with vendors and cloud providers, ensuring their services meet university standards.

Service Transition moves services from design to live operation. **Change Enablement** (formerly "Change Management") evaluates proposed changes for risk and coordinates implementation. By 2040, the "change advisory board" (CAB) model — where all changes are reviewed in weekly meetings — has been replaced by "automated change enablement": standard changes (low risk, well understood) are pre-approved and automated; normal changes trigger automated risk assessment; emergency changes are expedited but post-hoc reviewed. The UoY "Mímir Service Desk" implements this model: 80% of changes are fully automated, 15% require automated risk assessment with human review, and 5% (major infrastructure changes) require full CAB review. **Release Management** coordinates the bundling of changes into releases; **Deployment Management** executes the technical delivery. The "shift left" of testing — running integration, performance, and security tests in pre-production environments — catches issues before they reach users.

Service Operation maintains services in production. **Incident Management** restores normal service as quickly as possible, minimizing business impact. By 2040, AI-assisted incident management (the UoY "Sleipnir" platform, mentioned in IT103 and IT205) handles 60% of routine incidents automatically: password resets, account unlocks, VPN configuration issues. Human service desk staff handle complex, novel, or sensitive incidents. **Problem Management** investigates root causes of incidents to prevent recurrence. The traditional model — manual analysis of incident patterns — has been enhanced by observability: when an incident occurs, automated systems correlate it with infrastructure changes, deployment times, and metric anomalies, suggesting root causes within minutes. **Request Fulfillment** handles service requests ("I need a new laptop," "Please grant me access to the research database") through self-service portals and automated provisioning. **Event Management** monitors infrastructure events (CPU spikes, disk warnings) to detect issues before they become incidents.

Continual Improvement is the engine that drives service evolution. The PDCA cycle (Plan-Do-Check-Act, originally developed by Walter Shewhart and popularized by W. Edwards Deming) provides a simple but powerful model: plan an improvement, implement it, measure results, and standardize or adjust. By 2040, "Kaizen"-inspired micro-improvements — small, frequent changes suggested by frontline staff — complement larger strategic improvements. The UoY "Improvement Register" captures all improvement ideas, prioritizes them by impact/effort, and tracks implementation. In 2039, the register contained 1,200 ideas, of which 400 were implemented, generating estimated annual savings of €2.3 million and significant user satisfaction improvements.

### Required Reading

- AXELOS (2030). *ITIL 4: Direct, Plan and Improve.* TSO.
- AXELOS (2030). *ITIL 4: Create, Deliver and Support.* TSO.
- UoY-IT-TR-2038-41: "From CAB to Automation: Modernizing Change Management at University of Yggdrasil."
- UoY-IT-TR-2037-89: "The Improvement Register: Kaizen in Academic IT."
- ServiceNow (2039). "Service Desk Automation: AI-Assisted Incident Resolution."

### Discussion Questions

1. Automated change enablement reduces bureaucracy but requires trust in automation. What safeguards should exist to prevent automated approval of changes that turn out to be high-risk?

2. Experience Level Agreements (XLAs) measure user satisfaction, but satisfaction can be manipulated (e.g., by making the service flashy rather than reliable). How should organizations balance XLAs with objective technical metrics?

3. AI handles 60% of routine incidents at UoY, but the remaining 40% are disproportionately complex. Are service desk jobs becoming more interesting (handling complex problems) or more stressful (higher complexity without higher pay)?

### Practice Problems

- Design a Change Enablement process for a mid-size organization. Define: change categories (standard, normal, emergency), risk assessment criteria, approval workflows, and rollback procedures. Create a flowchart and a RACI matrix.
- Analyze three months of incident data (provided dataset) to identify problem patterns. Use Pareto analysis (80/20 rule) to identify the top 20% of incident causes generating 80% of impact. Propose targeted problem management initiatives.

---

ᚦ **Lecture 3: DevOps Culture and Practice — Breaking Down Walls**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

The wall between development and operations is one of the most destructive organizational barriers in IT. Developers write code and throw it over the wall; operators struggle to deploy and maintain code they did not write, did not test, and do not understand. DevOps is the movement that tears down this wall — not by eliminating roles but by creating shared ownership, shared tools, and shared goals. This lecture covers DevOps culture, practices, and tools in depth, with emphasis on the human dimensions that determine whether DevOps succeeds or fails.

By 2040, DevOps has evolved from a niche movement to standard practice, but the cultural transformation remains incomplete. Many organizations have adopted DevOps tools (CI/CD, containers, Kubernetes) without embracing DevOps culture (shared ownership, psychological safety, continuous learning). This "cargo cult DevOps" — imitating the form without the substance — produces disappointment and cynicism. The lecture emphasizes that DevOps is fundamentally about people, not tools.

### Key Topics

- **The Three Ways:** Flow (optimizing delivery), Feedback (creating learning loops), and Continual Learning (cultivating experimentation)
- **The CALMS Model:** Culture, Automation, Lean, Measurement, Sharing — the five pillars of DevOps
- **CI/CD Pipelines:** Continuous Integration (automated builds and tests), Continuous Delivery (automated deployment to staging), and Continuous Deployment (automated release to production)
- **Infrastructure as Code:** Terraform, Pulumi, Ansible, and the 2040 "platform engineering" model where infrastructure is a self-service product
- **Observability-Driven Development:** Building systems with observability as a first-class requirement, not an afterthought
- **DevOps Metrics:** DORA metrics (Deployment Frequency, Lead Time for Changes, Change Failure Rate, Mean Time to Recovery) and the 2040 "flow metrics" (work in progress, throughput, cycle time)

### Lecture Notes

The origins of DevOps lie in the Agile Manifesto (2001), which challenged the waterfall model of software development. But Agile addressed only development; operations remained stuck in slow, risk-averse processes. The 2009 presentation "10+ Deploys Per Day: Dev and Ops Cooperation at Flickr" by John Allspaw and Paul Hammond is often cited as the birth of DevOps: it demonstrated that development and operations could collaborate to achieve rapid, reliable deployment. The 2010 "DevOps Days" conferences in Ghent and Sydney formalized the movement, and the 2013 book *The Phoenix Project* by Gene Kim popularized it.

The CALMS model (Jez Humble, 2015) defines five pillars:

- **Culture:** Shared ownership, blameless postmortems, psychological safety, and trust. Culture is the foundation: without it, automation merely accelerates dysfunction.
- **Automation:** Replacing manual, repetitive work with automated processes. Automation reduces toil, eliminates human error, and frees people for creative work.
- **Lean:** Eliminating waste (waiting, rework, unnecessary features) and optimizing flow. Lean principles from manufacturing (Toyota Production System) apply directly to software delivery.
- **Measurement:** Using data to drive decisions. What gets measured gets managed — but measuring the wrong things creates perverse incentives.
- **Sharing:** Creating transparency across teams and organizations. Shared dashboards, open postmortems, and cross-team rotations build empathy and understanding.

CI/CD (Continuous Integration/Continuous Delivery/Continuous Deployment) is the technical backbone of DevOps. **Continuous Integration** means that every code change is automatically built and tested. Developers merge to main frequently (multiple times per day), ensuring that integration problems are caught immediately. **Continuous Delivery** means that every successful build can be deployed to production automatically — but deployment requires a human decision (the "button push"). **Continuous Deployment** means that successful builds are deployed to production automatically, without human intervention. By 2040, continuous deployment is standard for web applications and microservices but remains rare for safety-critical systems (medical devices, aircraft control) where human review is mandated.

Infrastructure as Code (IaC), discussed in IT103 (Lecture 9), treats infrastructure provisioning as a software engineering problem. By 2040, "platform engineering" has evolved from IaC: platform teams build internal developer platforms that abstract infrastructure complexity into self-service APIs. Developers request a database through a portal; the platform provisions it automatically, applying security policies, backup schedules, and monitoring. This model — pioneered by Netflix, Spotify, and Google — is now standard at technology-forward organizations. The UoY "Jötunn Platform" (named for the Jötunn IDE from CS407) provides self-service provisioning for compute, storage, databases, and Kubernetes namespaces, with guardrails that prevent unsafe configurations.

Observability-Driven Development (ODD) extends test-driven development (TDD) to production systems. Traditional TDD writes tests before code; ODD defines observability requirements before implementation: "This service must emit metrics for request rate, error rate, and latency." "This service must generate distributed traces for all user-facing operations." "This service must log at INFO level for normal operations and ERROR level for failures." By defining observability contracts upfront, ODD ensures that services are monitorable from day one, rather than retrofitting instrumentation after deployment. The UoY "Observability Review" — a mandatory checkpoint in the service design process — verifies that observability requirements are met before production deployment.

DORA metrics (DevOps Research and Assessment, founded by Nicole Forsgren, Jez Humble, and Gene Kim) provide evidence-based benchmarks for software delivery performance. The four key metrics: **Deployment Frequency** (how often deployments occur), **Lead Time for Changes** (time from commit to production), **Change Failure Rate** (percentage of deployments causing failures), and **Mean Time to Recovery** (time to recover from failures). By 2040, DORA has expanded to include **Reliability** (meeting SLOs) and **Availability** (uptime). The 2039 DORA report (analyzing 45,000 professionals globally) found that elite performers deploy on-demand (multiple times per day), have lead times under 1 hour, change failure rates below 5%, and recovery times under 1 hour. The report also found that culture (psychological safety, generative culture) is the strongest predictor of performance — more than tooling, cloud adoption, or automation.

### Required Reading

- Kim, G., et al. (2033). *The DevOps Handbook*, 3rd Edition. IT Revolution Press.
- Humble, J., & Farley, D. (2031). *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*, 2nd Edition. Addison-Wesley.
- Forsgren, N., et al. (2039). *Accelerate: The Science of Lean Software and DevOps*, 2nd Edition. IT Revolution Press.
- UoY-IT-TR-2037-77: "Jötunn Platform: Self-Service Infrastructure for Academic Research."
- UoY-IT-TR-2038-55: "Observability-Driven Development: From Concept to Production."

### Discussion Questions

1. DORA metrics show that elite performers deploy frequently with low failure rates, but correlation is not causation. Does frequent deployment cause high performance, or do high-performing organizations simply deploy more because they can?

2. Platform engineering abstracts infrastructure complexity, but abstraction can hide performance problems and cost overruns. How should platform teams balance developer autonomy against governance?

3. Psychological safety is the strongest predictor of DevOps performance, but it cannot be mandated by policy. How can leaders cultivate psychological safety in organizations with histories of blame and fear?

### Practice Problems

- Build a CI/CD pipeline for a sample application that includes: automated unit tests, integration tests, SAST, container image scanning, deployment to a staging environment, smoke tests, and promotion to production. Measure and report the DORA metrics (deployment frequency, lead time, change failure rate, MTTR) over a simulated 2-week sprint.
- Conduct a "culture assessment" of a hypothetical IT department using the Westrum organizational typology (pathological, bureaucratic, generative). Identify specific behaviors, processes, and structures that characterize each type. Propose three interventions to move the organization toward a generative culture.

---

ᚨ **Lecture 4: Site Reliability Engineering — Engineering Reliability**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

Reliability is not the absence of failure but the presence of trust. Users trust that services will be available when needed, that data will be preserved, that transactions will complete correctly. Site Reliability Engineering (SRE) is the discipline of engineering that trust into systems — not through heroic firefighting but through methodical design, measurement, and automation. This lecture covers SRE principles, practices, and organizational models in depth, with emphasis on the quantitative frameworks (SLOs, error budgets, toil budgets) that distinguish SRE from traditional operations.

By 2040, SRE has spread from Google to become a standard practice at technology companies and increasingly at traditional enterprises. The UoY SRE team (founded 2032, now 45 engineers) manages the university's most critical services: authentication, learning management, research data platforms, and the Yggdrasil Cloud. This lecture draws extensively on their practices and lessons learned.

### Key Topics

- **SRE Principles:** Embracing risk, SLOs and SLIs, eliminating toil, monitoring distributed systems, and automation
- **Service Level Objectives (SLOs):** Defining quantitative reliability targets, measuring Service Level Indicators (SLIs), and the negotiation between reliability and velocity
- **Error Budgets:** The mathematical framework for balancing reliability against feature development
- **Toil Management:** Identifying and eliminating operational toil (repetitive, manual work) through automation and platformization
- **Chaos Engineering:** Deliberately injecting failures to validate resilience (Netflix Chaos Monkey, Gremlin, and the UoY "Fimbulwinter" platform)
- **Incident Management:** On-call rotations, incident command, blameless postmortems, and the "incident response as a skill" philosophy

### Lecture Notes

SRE was born at Google in 2003, when Ben Treynor Sloss was tasked with making Google's production systems reliable. His insight: "What happens when you ask a software engineer to design an operations function?" The answer was SRE: an engineering discipline that applies software engineering rigor to operations problems. SRE teams spend 50% of their time on engineering (building tools, automation, and platforms) and 50% on operations (on-call, incident response, manual work) — though the goal is to shift the ratio toward engineering by eliminating toil.

The core concept of SRE is the Service Level Objective (SLO). An SLO is a quantitative reliability target: "99.9% of API requests complete successfully within 200ms over a 30-day window." The Service Level Indicator (SLI) is the metric being measured (request success rate, latency). The Service Level Agreement (SLA) is the contractual commitment to customers — typically stricter than the SLO, with financial penalties for violation. SLOs must be: (1) **Specific** — clearly defined and unambiguous; (2) **Measurable** — based on observable data; (3) **Achievable** — realistically attainable given resources; (4) **Relevant** — aligned with user needs; (5) **Time-bound** — measured over defined windows. A poorly defined SLO ("the system should be fast") is useless; a well-defined SLO ("99th percentile latency < 500ms for user-facing requests") drives engineering decisions.

The error budget is the permitted unreliability: 100% minus the SLO. For a 99.9% SLO, the error budget is 0.1% — approximately 43 minutes of downtime per month. The error budget provides a contractual mechanism for managing the reliability-velocity trade-off. When the error budget is healthy (most of the 43 minutes remaining), the team can launch new features aggressively. When the error budget is exhausted (all 43 minutes used), feature releases pause until reliability improves. This replaces the traditional "ops vs. dev" conflict with a mathematical framework: both sides agree on the SLO, and the error budget objectively determines when to prioritize reliability over features. The UoY "Budget Board" — a dashboard visible to all engineering teams — displays real-time error budget consumption for every service.

Toil is the repetitive, manual work that scales linearly with system size: provisioning servers, applying patches, responding to routine alerts, managing credentials. SRE teams measure toil as a percentage of engineering time and aim to keep it below 50% — ideally below 33%. Toil reduction strategies: automation (scripts and pipelines replace manual steps), self-service platforms (users provision their own resources), and elimination (removing unnecessary services or processes). The UoY SRE team maintains a "Toil Register" — a backlog of toil reduction projects, prioritized by impact (hours saved per month) and effort (engineering days to implement). In 2039, the team eliminated 1,200 hours/month of toil through automation, equivalent to 7.5 full-time engineers.

Chaos Engineering is the practice of deliberately injecting failures into production systems to validate resilience. Netflix pioneered this approach with Chaos Monkey (2011), which randomly terminated production instances to ensure that services could survive instance failures. By 2040, Chaos Engineering has matured into a comprehensive discipline: **Chaos Monkey** (instance failure), **Latency Monkey** (introduces network delays), **Chaos Gorilla** (simulates availability zone failures), and the UoY "Fimbulwinter" platform (named for the Norse "mighty winter" that precedes Ragnarök) which simulates compound failures: simultaneous network partition, database failover, and DDoS attack. Chaos experiments are conducted during business hours with full team awareness, using automated rollback mechanisms. The goal is not to cause outages but to discover weaknesses before they cause real outages.

Incident management in SRE is treated as a skill to be developed, not a burden to be endured. On-call rotations are designed for sustainability: no more than one week in four, mandatory handoffs with written context, and "follow-the-sun" rotations across global offices. Incident command follows the ICS model (discussed in IT103, Lecture 12): clear roles, structured communication, and post-incident improvement. Blameless postmortems focus on systemic factors: "What about our systems made this failure possible?" "What signals did we miss?" "How can we prevent recurrence?" The UoY SRE team conducts approximately 200 postmortems annually, with a "postmortem of the month" selected for broader organizational learning.

### Required Reading

- Beyer, B., et al. (2035). *Site Reliability Engineering: How Google Runs Production Systems*, 2nd Edition. O'Reilly.
- Beyer, B., et al. (2033). *The Site Reliability Workbook: Practical Ways to Implement SRE.* O'Reilly.
- Rosenthal, C., et al. (2038). *Chaos Engineering: System Resiliency in Practice*, 2nd Edition. O'Reilly.
- UoY-IT-TR-2038-67: "The Budget Board: Quantifying Reliability Trade-offs at University of Yggdrasil."
- UoY-IT-TR-2037-91: "Fimbulwinter: Chaos Engineering for Compound Failure Scenarios."

### Discussion Questions

1. Error budgets require accurate SLO measurement, but some services (e.g., batch data pipelines) have ambiguous "success" definitions. How should SRE teams define SLOs for services where user impact is indirect or delayed?

2. Chaos Engineering deliberately introduces failures in production, which could cause real user impact. Under what conditions is this risk justified, and what safeguards should exist?

3. SRE mandates that teams spend 50% of time on engineering, but management often pressures teams to focus on operational firefighting. How can SRE teams protect their engineering time?

### Practice Problems

- Define SLOs, SLIs, and error budgets for three hypothetical services: a student registration API, a research data repository, and a campus WiFi network. Justify your targets based on user needs and business impact.
- Design a chaos experiment for a sample application. Identify the failure to inject (e.g., database latency spike), the expected behavior (e.g., graceful degradation with cached data), the rollback mechanism, and the success criteria. Document the experiment plan and hypothetical results.

---

ᚲ **Lecture 5: Value Stream Management — Integrating ITIL, DevOps, and SRE**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

ITIL provides governance. DevOps provides delivery. SRE provides reliability. But these traditions, born in different contexts and championed by different communities, can fragment rather than unite. Value Stream Management (VSM) is the emerging discipline that integrates them — providing end-to-end visibility, measurement, and optimization of the flow from idea to value. This lecture covers VSM principles, platforms, and practices, with emphasis on the 2040 reality where ITSM is not a choice between frameworks but a synthesis of their strengths.

By 2040, VSM has evolved from a manufacturing concept (Toyota's "value stream mapping") to the dominant paradigm for software and service delivery. The UoY "Yggdrasil Value Stream" platform integrates ITIL service requests, DevOps CI/CD pipelines, SRE observability, and business KPIs into a unified system that tracks every user request from submission to fulfillment, measuring flow efficiency and identifying bottlenecks.

### Key Topics

- **Value Stream Mapping:** Identifying the steps, wait times, and handoffs in a service delivery process
- **Flow Metrics:** Work in Progress (WIP), throughput, cycle time, lead time, and flow efficiency (value-adding time / total time)
- **Bottleneck Analysis:** Theory of Constraints applied to IT delivery — identifying and alleviating constraints that limit throughput
- **VSM Platforms:** Plutora, ServiceNow, GitLab, and the integration challenges of connecting disparate tools
- **Business-IT Alignment:** Translating business objectives into IT deliverables and demonstrating IT value through business outcomes
- **The 2040 "Unified Operations" Model:** Where service desk, DevOps platform, SRE observability, and business analytics converge into a single experience

### Lecture Notes

Value Stream Mapping (VSM) originated in lean manufacturing (Toyota Production System, 1950s) as a method for visualizing the flow of materials and information from raw materials to finished product. Applied to IT, VSM visualizes the flow of work from customer need to delivered value. The process: (1) **Select a Value Stream** — e.g., " provisioning a new research compute cluster"; (2) **Walk the Stream** — observe each step from request to delivery; (3) **Map the Current State** — document each step, its duration, and wait times between steps; (4) **Identify Waste** — waiting, rework, handoffs, unnecessary approvals; (5) **Design the Future State** — eliminate waste and optimize flow; (6) **Implement and Iterate** — execute improvements and measure results.

A typical IT value stream reveals shocking inefficiency. The UoY "Research Compute Provisioning" stream, mapped in 2036, showed: total lead time of 45 days, of which only 3 days were value-adding (provisioning the cluster). The remaining 42 days were waiting: request sitting in queue (5 days), security review scheduling (7 days), budget approval (10 days), vendor procurement (12 days), and manual configuration (8 days). By applying VSM principles — automating security review, pre-approving standard configurations, and implementing self-service procurement — the team reduced lead time to 6 days (with 2 days of value-adding work). Flow efficiency improved from 7% to 33% — still far from manufacturing standards (60–80%), but a dramatic improvement.

Flow metrics provide quantitative visibility into value stream health. **Work in Progress (WIP)** — the number of items being worked on simultaneously. High WIP indicates overload and context switching. **Throughput** — the number of items completed per unit time. **Cycle Time** — the time from starting work on an item to completing it. **Lead Time** — the time from customer request to delivery (includes waiting before work starts). **Flow Efficiency** — the percentage of lead time spent on value-adding activities (as opposed to waiting). By 2040, these metrics are automatically calculated by VSM platforms and displayed on team dashboards. The UoY "Flow Analytics" platform provides real-time flow metrics for 200+ value streams across the university.

Bottleneck analysis, derived from Eliyahu Goldratt's Theory of Constraints (1984), identifies the constraint that limits overall throughput. In a value stream, the bottleneck is the slowest step — improving any other step will not increase overall throughput until the bottleneck is addressed. The UoY "Research Compute Provisioning" bottleneck was budget approval: security review was faster than procurement, but items piled up waiting for budget sign-off. By implementing pre-approved budgets for standard configurations (delegating authority to department heads for requests under €10,000), the bottleneck shifted to manual configuration — which was then automated. The Theory of Constraints provides a systematic method for prioritizing improvement efforts: focus on the bottleneck, then identify the next bottleneck.

VSM platforms attempt to integrate the disparate tools of IT delivery. A typical university IT ecosystem includes: ITIL service desk (ServiceNow), DevOps platform (GitLab), SRE observability (Prometheus/Grafana), project management (Jira), and business intelligence (Tableau). VSM platforms (Plutora, ServiceNow with VSM module, GitLab with Value Stream Analytics) connect these tools via APIs, aggregating data into unified views. The integration challenge is significant: APIs have different data models, rate limits, and reliability characteristics. The UoY "Yggdrasil Value Stream" platform uses a "data lake" architecture: event streams from all tools are normalized into a common schema and stored in a time-series database, enabling cross-tool analytics without fragile point-to-point integrations.

Business-IT alignment remains the ultimate goal of VSM. Technology exists to serve business objectives: research output, student satisfaction, operational efficiency, regulatory compliance. VSM platforms translate business KPIs into IT metrics: "We need to increase research publication velocity by 20%" becomes "We need to reduce compute cluster provisioning time from 6 days to 2 days" and "We need to improve data pipeline reliability from 99% to 99.9%." The UoY "Strategic Alignment Dashboard" maps university strategic objectives (from the Rector's annual plan) to IT initiatives, value streams, and metrics, allowing the Board of Regents to trace IT investment to business outcomes.

### Required Reading

- Rother, M., & Shook, J. (2032). *Learning to See: Value Stream Mapping to Add Value and Eliminate MUDA*, 2nd Edition. Lean Enterprise Institute.
- Goldratt, E.M. (2030). *The Goal: A Process of Ongoing Improvement*, 4th Edition. North River Press.
- Plutora (2038). "Value Stream Management: Connecting Business Strategy to Software Delivery."
- UoY-IT-TR-2037-77: "Yggdrasil Value Stream: End-to-End Integration of ITIL, DevOps, and SRE."
- UoY-IT-TR-2038-73: "Flow Analytics: Measuring and Optimizing 200+ University Value Streams."

### Discussion Questions

1. Flow efficiency in IT (typically 5–15%) is far lower than in manufacturing (60–80%). Is this inherent to creative/knowledge work, or can IT achieve manufacturing-level efficiency?

2. VSM platforms require extensive tool integration, which creates maintenance burden. For a small IT department with 10 staff, is VSM worth the investment, or should they focus on improving specific tools?

3. Business-IT alignment sounds obvious but is difficult to measure. How should IT organizations demonstrate value when business outcomes (e.g., "student satisfaction") have many non-IT contributors?

### Practice Problems

- Map a value stream for a familiar IT process (e.g., onboarding a new employee, resolving a service request, or deploying a code change). Document each step, measure (or estimate) durations and wait times, calculate flow efficiency, and identify the top three bottlenecks. Propose improvements.
- Design a "Unified Operations" dashboard that integrates data from: ITIL service desk (ticket volume, resolution times), DevOps platform (deployment frequency, lead time), SRE observability (SLO compliance, error budget), and business metrics (user satisfaction, cost per transaction). Specify data sources, visualization types, and alert thresholds.

---

ᚷ **Lecture 6: Automation and AI in Service Management — The Self-Healing Organization**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

The Viking shipwright did not row the longship himself; he built a vessel that harnessed the wind. Similarly, the IT service manager does not manually resolve every incident or execute every deployment; they build systems that automate routine work, freeing humans for creative and strategic tasks. This lecture covers the automation landscape of 2040: robotic process automation (RPA), AI-powered service desks, autonomous remediation, and the emerging "self-healing" systems that detect, diagnose, and repair problems without human intervention.

By 2040, automation has permeated every aspect of IT service management. The UoY "Mímir Service Desk" resolves 60% of incidents autonomously; the "Jötunn Platform" provisions infrastructure without human touch; and the "Sleipnir" SRE platform predicts failures before they occur. But automation also creates new challenges: maintaining automation code, handling edge cases, managing the "automation paradox" (where over-reliance on automation erodes human skills), and ensuring that automated decisions are explainable and accountable.

### Key Topics

- **Robotic Process Automation (RPA):** UiPath, Automation Anywhere, and the automation of repetitive UI interactions
- **AIOps:** AI for IT Operations — anomaly detection, root cause analysis, predictive maintenance, and automated remediation
- **Chatbots and Virtual Agents:** NLP-powered service desk interfaces that handle routine requests and escalate complex issues
- **Autonomous Remediation:** Self-healing systems that detect failures and execute repair workflows without human approval
- **The Automation Paradox:** When automated systems fail, humans must intervene — but their skills may have atrophied from disuse
- **Governance of Automation:** Ensuring that automated decisions are auditable, explainable, and aligned with organizational policies

### Lecture Notes

Robotic Process Automation (RPA) automates interactions with legacy systems that lack APIs. An RPA bot logs into a web application, navigates menus, fills forms, and extracts data — mimicking human UI interactions. RPA is valuable for bridging legacy systems but brittle: a UI change (button moved, field renamed) breaks the bot. By 2040, RPA has evolved into "intelligent automation" — combining RPA with computer vision (interpreting UI elements semantically rather than by position) and NLP (reading documents to extract data). The UoY "Rune Bot" platform automates 40+ legacy administrative processes: student registration updates, financial aid verification, and research grant reporting — processes that would require expensive system modernization to automate natively.

AIOps (AI for IT Operations) applies machine learning to the massive data streams generated by IT infrastructure: metrics, logs, traces, and events. The four pillars of AIOps (Gartner, 2017; evolved by 2040): **Anomaly Detection** — identifying patterns that deviate from baselines (e.g., CPU usage spike at 3am); **Root Cause Analysis** — correlating anomalies across systems to identify underlying causes (e.g., the CPU spike was caused by a runaway backup job triggered by a cron misconfiguration); **Predictive Maintenance** — forecasting failures before they occur (e.g., disk SMART data predicts failure within 48 hours); **Automated Remediation** — executing repair actions without human intervention (e.g., killing the runaway backup, migrating data from predicted-failing disk). The UoY "Sleipnir" platform (mentioned in IT103 and IT205) handles all four pillars for the university's critical services.

Chatbots and virtual agents have transformed service desk interactions. The UoY "Huginn Assistant" (named for Odin's thought-raven) handles routine requests through natural language conversation: "Reset my password," "Grant me access to the chemistry lab database," "When is the next maintenance window?" Huginn understands context ("the chemistry lab database" refers to CHEM-DB-01), executes backend workflows, and confirms completion. Complex requests are escalated to human agents with full context: "User asked for access to CHEM-DB-01. They are a PhD student in the Chemistry Department. Their supervisor has approved access. I have prepared the provisioning request; please review and approve." By 2040, 60% of UoY service desk interactions are handled entirely by Huginn; 30% begin with Huginn and escalate to humans; 10% are routed directly to human experts.

Autonomous remediation is the most ambitious form of automation: systems that detect problems and fix them without human approval. Examples: a container that restarts when health checks fail; a load balancer that redirects traffic from a failing server; a database that fails over to a replica when the primary becomes unresponsive. By 2040, autonomous remediation handles approximately 80% of infrastructure failures at UoY — but the remaining 20% require human judgment. The "automation paradox" (Lisanne Bainbridge, 1983) warns that as automation becomes more reliable, human operators become less practiced at manual intervention — making the rare manual intervention more likely to fail. The UoY response: regular "manual override drills" where engineers practice hand-operating automated systems, ensuring skill retention.

Governance of automation ensures that automated systems act in accordance with organizational values and policies. Questions: Can an AI approve a budget? Can a bot grant access to sensitive data? Can an automated system shut down a research experiment to preserve infrastructure? The UoY "Automation Governance Framework" (2037) establishes: **Decision Rights** — which decisions can be fully automated, which require human approval, and which are human-only; **Explainability** — automated decisions must be explainable (why did the system take this action?); **Auditability** — all automated actions are logged and reviewable; **Override** — humans can override automated decisions in emergencies; **Learning** — automated systems improve through feedback, but humans validate major learning updates. The framework acknowledges that automation is not merely a technical choice but an ethical and organizational one.

### Required Reading

- Gartner (2038). *Market Guide for AIOps Platforms.*
- UiPath (2039). "Intelligent Automation: Beyond RPA."
- Bainbridge, L. (1983/2035 annotated). "Ironies of Automation." *Automatica*, 19(6), 775–779.
- UoY-IT-TR-2037-99: "Huginn Assistant: NLP-Powered Service Desk Automation."
- UoY-IT-TR-2038-81: "Automation Governance: Decision Rights and Ethical Frameworks for Autonomous Systems."

### Discussion Questions

1. RPA bridges legacy systems but creates technical debt (bots are brittle and hard to maintain). Should organizations invest in RPA as a permanent solution or use it only as a bridge to proper API-based integration?

2. Autonomous remediation handles 80% of failures, but the 20% requiring human judgment are often the most complex and consequential. Are we training operators for the wrong cases (routine failures that are automated) while under-preparing them for critical failures?

3. Should AI systems ever have the authority to make decisions with financial or legal consequences (e.g., approving procurement, terminating contracts)? If so, what safeguards ensure accountability?

### Practice Problems

- Design an AIOps dashboard for a hypothetical microservices application. Specify: metrics to monitor, anomaly detection algorithms, root cause analysis logic, and automated remediation actions. Document the architecture and data flows.
- Develop a chatbot workflow for a common service desk request (e.g., password reset, access request, or incident reporting). Define the conversation flow, backend integrations, escalation criteria, and fallback handling for unrecognized inputs.

---

ᚹ **Lecture 7: Organizational Culture and Change — The Human Dimension**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

Technology is easy; people are hard. The most elegant ITSM framework, the most sophisticated DevOps toolchain, and the most rigorous SLO will fail if the organizational culture rejects them. This lecture addresses the human dimension of service management: organizational culture, change management, team dynamics, and the leadership practices that enable high-performing IT organizations.

By 2040, the research on IT culture (Westrum, DORA, Google Aristotle) has crystallized into actionable knowledge. We know what makes teams effective: psychological safety, dependability, structure and clarity, meaning, and impact. We know what makes cultures generative: shared responsibility, continuous learning, and alignment between espoused values and practiced behaviors. The challenge is not knowing what to do but doing it — overcoming inertia, politics, and fear to create organizations where people thrive and technology serves.

### Key Topics

- **Organizational Culture:** Westrum's typology (pathological, bureaucratic, generative), Schein's levels of culture, and the "culture eats strategy for breakfast" principle
- **Psychological Safety:** Amy Edmondson's research — the shared belief that the team is safe for interpersonal risk-taking — and its relationship to innovation, learning, and performance
- **Change Management:** Kotter's 8-step model, ADKAR, and the 2040 "continuous change" approach where change is constant rather than episodic
- **Team Topologies:** Stream-aligned teams, platform teams, enabling teams, and complicated-subsystem teams — organizing teams for flow
- **Leadership in IT:** Servant leadership, transformational leadership, and the "technical leadership" model where leaders remain hands-on
- **Diversity and Inclusion:** The benefits of diverse teams for problem-solving and innovation, and the persistent underrepresentation of women and minorities in IT

### Lecture Notes

Organizational culture — "the way we do things around here" — is the invisible force that shapes every IT initiative. Ron Westrum's typology (1992, applied to safety-critical industries) distinguishes three culture types: **Pathological** (information is hoarded, failures are hidden, novelty is crushed), **Bureaucratic** (information flows through channels, failures are processed by rules, novelty is problematic), and **Generative** (information flows freely, failures are investigated, novelty is embraced). IT organizations often oscillate between bureaucratic (process-heavy, risk-averse) and pathological (blame-driven, siloed). The goal is generative: a culture where people feel safe to experiment, report problems, and suggest improvements.

Psychological safety, researched extensively by Amy Edmondson (Harvard Business School, 1999–present), is the foundation of generative culture. It is "a shared belief held by members of a team that the team is safe for interpersonal risk-taking" — speaking up with questions, concerns, or mistakes without fear of humiliation or retribution. Google's Aristotle project (2012–2015), which analyzed 180 teams to identify the factors driving effectiveness, found psychological safety to be the single most important factor — more than team composition, location, or tenure. By 2040, psychological safety is measured through team surveys and integrated into performance management: managers are evaluated partly on their teams' psychological safety scores. The UoY "Team Health Check" — a quarterly survey across all IT teams — measures psychological safety, workload sustainability, and alignment, with results reviewed by leadership.

Change management in IT has evolved from episodic projects ("we are implementing ITIL") to continuous adaptation ("we improve something every week"). Kotter's 8-step model (1996) — create urgency, form a guiding coalition, develop vision, communicate, remove obstacles, generate short-term wins, sustain acceleration, and anchor changes — remains relevant for major transformations. ADKAR (Prosci, 2003) focuses on individual transitions: Awareness, Desire, Knowledge, Ability, Reinforcement. By 2040, "continuous change" has supplemented these models: small, frequent improvements (Kaizen) reduce the need for large, disruptive transformations. The UoY "Change Canvas" — a one-page template for any improvement idea — ensures that even micro-changes are clearly communicated: what is changing, why, who is affected, and what support is available.

Team Topologies (Matthew Skelton and Manuel Pais, 2019; updated 2035) provides a model for organizing IT teams to optimize flow. Four team types: **Stream-aligned teams** (aligned to a value stream, e.g., "student onboarding platform team") — the primary team type, responsible for end-to-end delivery; **Platform teams** (provide internal platforms as services, e.g., "Kubernetes platform team") — reduce cognitive load on stream-aligned teams by abstracting infrastructure complexity; **Enabling teams** (help stream-aligned teams adopt new technologies, e.g., "observability coaching team") — temporary, mission-oriented; **Complicated-subsystem teams** (own complex components requiring specialized expertise, e.g., "payment processing team") — rare, used when deep expertise is needed. The UoY IT department reorganized along Team Topologies principles in 2034, reducing cross-team dependencies by 60% and improving deployment frequency by 3×.

Leadership in high-performing IT organizations differs from traditional command-and-control management. **Servant leadership** (Greenleaf, 1970) emphasizes supporting team members rather than directing them: removing obstacles, providing resources, and coaching growth. **Transformational leadership** (Bass, 1985) inspires through vision and intellectual stimulation. **Technical leadership** — leaders who remain hands-on with technology — is particularly valued in IT: teams respect leaders who understand the technical challenges they face. The UoY "Engineering Manager" role requires 20% hands-on engineering time: reviewing code, participating in architecture decisions, and staying current with technology. Managers who become purely administrative lose credibility and effectiveness.

Diversity and inclusion remain critical challenges. Despite decades of effort, women hold only 28% of IT positions globally in 2040 (up from 25% in 2020). Underrepresentation of ethnic minorities, people with disabilities, and older workers persists. The research is clear: diverse teams outperform homogeneous teams on complex problem-solving and innovation ( Page, 2007; replicated in 2030). The UoY "Valkyrie Initiative" — named for the Norse choosers of the slain, here reinterpreted as choosers of talent — implements: blind resume screening (removing names that signal gender/ethnicity), structured interviews (standardized questions scored on rubrics), mentorship programs, and inclusive team norms (ensuring all voices are heard in meetings). Progress is measurable but slow: the IT department reached 35% women in 2039, with a goal of 50% by 2045.

### Required Reading

- Westrum, R. (1992/2035 annotated). "Cultures with Requisite Imagination." In *Verification and Validation in Complex Systems.* Springer.
- Edmondson, A. (2030). *The Fearless Organization: Creating Psychological Safety in the Workplace for Learning, Innovation, and Growth.* Wiley, 2nd Edition.
- Skelton, M., & Pais, M. (2035). *Team Topologies: Organizing Business and Technology Teams for Fast Flow*, 2nd Edition. IT Revolution Press.
- Kotter, J.P. (2032). *Leading Change*, 2nd Edition. Harvard Business Review Press.
- UoY-IT-TR-2038-95: "The Valkyrie Initiative: Diversity and Inclusion in University IT."
- Google (2035). "Aristotle Revisited: Lessons from a Decade of Team Effectiveness Research."

### Discussion Questions

1. Psychological safety is essential for innovation but can be exploited by low performers who resist accountability. How should organizations balance safety with performance management?

2. Team Topologies recommends stream-aligned teams as the default, but many organizations struggle with "team sprawl" (too many small teams). What is the optimal team size and scope for stream-aligned teams?

3. The Valkyrie Initiative uses blind screening and structured interviews to reduce bias, but some argue these methods strip individuality and cultural fit. Is there a tension between meritocratic process and holistic evaluation?

### Practice Problems

- Assess the culture of a hypothetical IT department using Westrum's typology. Identify specific behaviors, processes, and structures that indicate pathological, bureaucratic, or generative characteristics. Propose three interventions to move toward a generative culture.
- Design a "Team Health Check" survey for an IT team. Include questions measuring: psychological safety, workload sustainability, clarity of goals, autonomy, and growth opportunities. Specify scoring, benchmarks, and action thresholds.

---

ᚺ **Lecture 8: Metrics, Measurement, and the Art of Improvement**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

What gets measured gets managed — but measuring the wrong things creates perverse incentives that damage organizations more than ignorance ever could. This lecture covers the principles and practices of IT measurement: selecting metrics that drive desired behaviors, avoiding metrics that encourage gaming, and using measurement as a tool for improvement rather than a weapon for punishment.

By 2040, the measurement landscape has matured significantly. The DORA metrics provide evidence-based benchmarks for software delivery. Flow metrics quantify value stream efficiency. Experience metrics (XLAs) capture user sentiment. Financial metrics (TCO, ROI, cost per transaction) justify IT investments. The challenge is not collecting data but deriving insight: understanding which metrics matter, how they interact, and how to act on them without creating unintended consequences.

### Key Topics

- **Good Metrics vs. Bad Metrics:** Vanity metrics (look good but drive no action) vs. actionable metrics; leading indicators (predict future outcomes) vs. lagging indicators (measure past outcomes); local optima (improving one metric at others' expense) vs. global optima
- **The DORA Metrics:** Deployment Frequency, Lead Time for Changes, Change Failure Rate, Mean Time to Recovery — and the 2040 extensions (reliability, availability, user satisfaction)
- **Flow Metrics:** WIP, throughput, cycle time, lead time, flow efficiency — and Little's Law (WIP = throughput × cycle time)
- **Experience Metrics:** XLAs, NPS (Net Promoter Score), CSAT (Customer Satisfaction), and the 2040 "emotional analytics" that detect user frustration from interaction patterns
- **Financial Metrics:** TCO (Total Cost of Ownership), ROI (Return on Investment), cost per transaction, and IT cost transparency
- **Metrics-Driven Improvement:** The "improvement Kata" (scientific method applied to organizations), A/B testing for process changes, and the "metrics review" ritual

### Lecture Notes

Metrics are powerful because they shape behavior. When a manager measures "lines of code written," developers write verbose, unmaintainable code. When a call center measures "average handle time," agents rush callers off the phone. When a security team measures "number of vulnerabilities patched," they patch low-risk vulnerabilities while ignoring critical ones that are harder to fix. These are "perverse incentives" — metrics that, by their very design, encourage undesired behavior. The antidote is careful metric design: measure outcomes, not outputs; measure system health, not individual activity; and always consider how a metric could be gamed.

Good metrics share several characteristics: they are **comparable** (can be tracked over time or across teams), **understandable** (clear meaning without complex explanation), ** actionable** (drive specific decisions), **timely** (available when needed), and **resistant to gaming** (difficult to manipulate without genuine improvement). The DORA metrics exemplify good metric design: deployment frequency is simple to measure and directly reflects delivery capability; lead time reveals process bottlenecks; change failure rate balances velocity against quality; MTTR measures recovery capability. Together, they provide a balanced scorecard of software delivery performance.

Flow metrics, derived from queuing theory and lean manufacturing, provide mathematical insight into IT delivery. **Little's Law** (John Little, 1961) states that WIP = throughput × cycle time — a deceptively simple relationship with profound implications. If a team has 20 items in progress (WIP) and completes 4 per week (throughput), the average cycle time is 5 weeks. To reduce cycle time, the team can either increase throughput (work faster) or reduce WIP (focus on finishing rather than starting). Reducing WIP is usually easier and more effective: by limiting work in progress (the Kanban principle), teams finish items faster, improve quality, and reduce context switching. The UoY "Flow Analytics" platform calculates flow metrics automatically and alerts teams when WIP exceeds capacity.

Experience metrics attempt to capture the subjective dimension of IT services. **CSAT (Customer Satisfaction)** surveys ask users to rate service on a scale. **NPS (Net Promoter Score)** asks "How likely are you to recommend this service?" — a measure of loyalty rather than mere satisfaction. By 2040, **XLAs (Experience Level Agreements)** have supplemented traditional SLAs: rather than merely promising "99.9% uptime," the service commits to "95% of users rate the service as 'excellent' in post-interaction surveys." The UoY "Emotional Analytics" platform goes further: it analyzes user interaction patterns (mouse movements, typing cadence, facial expressions for video calls) to detect frustration in real-time, automatically escalating to human support when users appear distressed. This raises privacy concerns that the platform addresses through explicit consent and data minimization.

Financial metrics connect IT to business value. **TCO (Total Cost of Ownership)** includes not merely acquisition cost but ongoing operational costs: maintenance, support, training, and eventual decommissioning. **ROI (Return on Investment)** compares benefits to costs, though measuring IT benefits is notoriously difficult (how do you quantify the value of "improved researcher productivity"?). **Cost per transaction** provides a concrete metric: "It costs €0.15 to process a student enrollment" or "It costs €2.30 to provision a research VM." By 2040, UoY IT provides "cost transparency" dashboards showing the full cost of every service, enabling data-driven decisions about investment, consolidation, and retirement.

The "improvement Kata" (Mike Rother, 2009; widely adopted by 2040) applies the scientific method to organizational improvement. The cycle: (1) **Understand the Direction** — what is the strategic challenge? (2) **Grasp the Current Condition** — where are we now? (3) **Establish the Next Target Condition** — what is the next step? (4) **Experiment Toward the Target** — run PDCA cycles, measuring results. Unlike top-down mandates, the improvement Kata empowers frontline teams to experiment and learn. The UoY "Kata Coaches" — trained improvement facilitators — support teams in running improvement cycles, ensuring scientific rigor and organizational alignment.

### Required Reading

- Forsgren, N., et al. (2039). *Accelerate: The Science of Lean Software and DevOps*, 2nd Edition. IT Revolution Press.
- Rother, M. (2035). *The Toyota Kata: Managing People for Improvement, Adaptiveness, and Superior Results*, 2nd Edition. McGraw-Hill.
- UoY-IT-TR-2038-102: "Emotional Analytics: Detecting User Frustration in Real-Time."
- UoY-IT-TR-2037-105: "Cost Transparency: Financial Metrics for Academic IT."
- Meyer, B. (2031). "The Perils of Metrics: How Measurement Can Destroy Value." *Communications of the ACM*, 64(3), 28–31.

### Discussion Questions

1. Emotional analytics detects user frustration but requires monitoring user behavior closely. Is the service improvement benefit worth the privacy intrusion?

2. Cost transparency can create political conflicts ("Your service costs 3× more than your colleague's"). Should cost data be fully transparent, or should organizations buffer teams from financial comparisons?

3. The improvement Kata requires time for experimentation, but many teams are fully allocated to feature delivery. How should organizations create "improvement capacity" without sacrificing delivery commitments?

### Practice Problems

- Design a balanced scorecard for a hypothetical IT department. Include: delivery metrics (DORA), operational metrics (SLOs), financial metrics (cost per transaction), and experience metrics (CSAT). Specify targets, measurement methods, and review frequencies.
- Run an improvement Kata cycle for a specific IT process (e.g., incident resolution, deployment, or access provisioning). Document: the strategic challenge, current condition, target condition, experiments conducted, results measured, and lessons learned.

---

ᚾ **Lecture 9: The Future of Service Management — 2045 and Beyond**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

The ITSM landscape of 2040 will seem primitive by 2050. This lecture examines emerging trends that will reshape service management: fully autonomous IT systems, the convergence of physical and digital service management, the role of IT in addressing climate change, and the philosophical question of what "service" means when AI can predict needs before humans articulate them.

We also address the enduring human dimensions: the purpose of work in an increasingly automated world, the ethics of algorithmic service delivery, and the responsibility of IT professionals to ensure that technology serves humanity rather than replacing it.

### Key Topics

- **Autonomous IT:** Self-designing, self-building, self-operating systems — the "no-ops" vision and its limitations
- **Physical-Digital Convergence:** ITSM for smart cities, autonomous transportation, and augmented reality services
- **Sustainable IT:** Carbon-aware computing, circular economy principles, and the role of IT in climate mitigation
- **Predictive Service:** AI that anticipates user needs before they are expressed — helpful assistance or creepy surveillance?
- **The Purpose of Service Work:** Meaning, craft, and human connection in an automated world

### Lecture Notes

Fully autonomous IT — the "no-ops" vision — posits that AI will eventually design, build, and operate systems without human intervention. By 2040, this vision is partially realized: AI generates code (GitHub Copilot, GPT-2040), AI designs architectures (the UoY "Jötunn Architect"), AI operates systems (Sleipnir, Huginn), and AI resolves incidents (autonomous remediation). But the "no-ops" label is misleading: humans remain essential for setting objectives, validating outcomes, handling novel situations, and ensuring ethical alignment. The future is not "no-ops" but "different-ops" — operations professionals who design automation, validate AI decisions, and handle exceptions. The UoY "Operations Architect" role (created 2035) exemplifies this evolution: senior operations engineers design self-healing systems rather than responding to pages.

Physical-digital convergence expands ITSM beyond software to the physical world. Smart city service management monitors traffic lights, water treatment, and waste management as "services" with SLOs and incident management. Autonomous vehicle fleets require ITSM at massive scale: provisioning vehicles, monitoring health, scheduling maintenance, and managing software updates over-the-air. Augmented reality (AR) services overlay digital information on physical spaces, requiring real-time infrastructure with stringent latency requirements. The UoY "Campus of the Future" initiative manages 50,000 IoT devices (sensors, actuators, displays) through the same ITSM platform that manages cloud services — a unified approach to physical and digital service management.

Sustainable IT addresses the environmental impact of computing. Data centers consume 2% of global electricity (2040); AI training workloads are increasingly carbon-intensive. "Carbon-aware computing" schedules workloads to times and locations with low-carbon electricity. The "circular economy" principle extends hardware lifecycle through refurbishment, reuse, and recycling. The UoY "Green IT" program (2034–present) has reduced the university's IT carbon footprint by 45% through: renewable energy procurement, server virtualization (reducing physical hardware), liquid cooling (improving efficiency), and hardware lifecycle extension (average server lifespan increased from 4 to 7 years). By 2040, all UoY IT procurement includes carbon impact evaluation; services with high carbon intensity require explicit justification.

Predictive service uses AI to anticipate user needs before they are expressed. A researcher's calendar shows a conference submission deadline; the system proactively provisions compute resources, schedules backups, and suggests collaborators. A student's grades show struggling; the system connects them with tutoring resources. A faculty member's publication rate drops; the system suggests grant opportunities. This is powerful and potentially helpful — but also raises profound concerns about autonomy, privacy, and the "filter bubble" effect (where predictive systems reinforce existing behaviors rather than enabling exploration). The UoY "Predictive Ethics Board" reviews all predictive service designs, ensuring they enhance rather than constrain human agency.

The purpose of service work in an automated world is a question of meaning. If AI handles routine incidents, what do human service desk staff do? The answer: they handle complex, emotional, and novel situations that AI cannot. They build relationships with users. They design better services. They ensure that technology serves human needs. The craft of service — understanding context, showing empathy, finding creative solutions — is irreducibly human. The UoY "Service Craft" initiative (2038) trains service professionals in these human skills, ensuring that automation augments rather than replaces human judgment.

### Required Reading

- UoY-IT-TR-2039-12: "The Operations Architect: Designing Self-Healing Systems for University Infrastructure."
- UoY-IT-TR-2038-110: "Campus of the Future: Unified Physical-Digital Service Management."
- UoY Sustainability Office (2039). "Green IT: Carbon-Aware Computing at University of Yggdrasil."
- UoY-IT-TR-2039-15: "Predictive Service: Enhancing or Constraining Human Agency?"
- Sennett, R. (2035). *The Craftsman in the Age of Automation.* Yale University Press.

### Discussion Questions

1. If AI can eventually design, build, and operate systems, what is the role of human IT professionals? Should we welcome liberation from routine work or fear obsolescence?

2. Predictive service can help users but also manipulates them. Where is the line between helpful anticipation and coercive nudging?

3. Sustainable IT requires trade-offs: longer hardware lifecycles may increase energy consumption from older, less efficient equipment. How should organizations balance hardware longevity against energy efficiency?

### Practice Problems

- Write a 2,000-word essay envisioning IT service management in 2050. Address: the balance of human and AI roles, the environmental sustainability of IT services, and the ethical governance of predictive systems.
- Design a "Green IT" assessment for a hypothetical data center. Calculate: carbon footprint (energy × carbon intensity), water usage, e-waste generation, and circular economy score. Propose three initiatives to improve sustainability.

---

## Final Examination Preparation

The final examination for IT207 consists of a **case study analysis** (40% of grade), a **practical assessment** (30%), and a **written examination** (30%).

### Case Study Analysis (40%)

Students analyze a provided case study of a struggling IT organization. The case includes: organizational structure, current metrics, recent incidents, user satisfaction surveys, and financial data. Students must:

1. Diagnose the root causes of underperformance using ITIL, DevOps, and SRE frameworks
2. Propose a restructuring plan including team topologies, cultural interventions, and metric changes
3. Design a 12-month improvement roadmap with milestones and success criteria
4. Address stakeholder concerns (executives fear cost; staff fear change; users fear continued poor service)

### Practical Assessment (30%)

Students work in teams to optimize a simulated value stream. Given a baseline process with documented metrics, teams must:

- Measure current flow efficiency and identify bottlenecks
- Implement at least three improvements (process, tooling, or cultural)
- Measure post-improvement metrics and calculate improvement
- Present results with data visualizations and retrospective analysis

### Written Examination — Sample Essay Questions (Choose 3 of 5)

1. Compare ITIL's Service Value Chain with DevOps' "Three Ways" and SRE's error budget model. How do these frameworks complement each other, and what tensions exist between them?

2. A university IT department has adopted DevOps tools (CI/CD, containers) but retains a blame culture and siloed teams. Analyze why "cargo cult DevOps" fails and propose interventions that address culture rather than tools.

3. Design an SLO framework for a research data repository. Define SLIs, SLOs, and error budgets. Address the challenge of measuring "reliability" for a service where "success" includes data integrity, availability, and retrieval performance.

4. The Theory of Constraints suggests focusing improvement on bottlenecks. Apply this theory to a provided value stream map, identifying the current bottleneck, proposing alleviation, and predicting the next bottleneck.

5. Autonomous IT systems promise efficiency but risk deskilling human operators. Drawing on the "automation paradox" and real-world examples, argue for or against increasing automation in critical IT services.

---

*"The finest longship is not the one with the most oars but the one where every oarsman rows in rhythm, trusting their shipmates, guided by a clear course, and sustained by a shared purpose. So it is with IT service management: not tools, not processes, but people in harmony, creating value."*  
— Prof. Einar Servicekeeper, IT207 Convocation Address, 2039
