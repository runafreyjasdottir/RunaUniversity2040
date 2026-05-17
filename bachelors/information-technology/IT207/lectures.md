# IT207: IT Service Management (ITIL, DevOps, SRE)
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4  
**Prerequisites:** IT201 — System Administration; IT205 — Cybersecurity Fundamentals (recommended)  
**Description:** A comprehensive study of the frameworks, practices, and cultures that enable the reliable delivery of IT services at scale. Covers ITIL 4 (the de facto global standard for service management), DevOps (the integration of development and operations), Site Reliability Engineering (SRE, Google's approach to scaling operations), and the emerging AIOps paradigm of 2040. Students learn to design service value streams, manage incidents and changes, measure reliability through service level objectives (SLOs), and implement continuous improvement cycles. The course culminates in a capstone project where students design an IT service management system for a simulated enterprise.

**Instructor:** Prof. Baldr Hákonarson, Senior Lecturer in Service Operations  
**Lab:** Frigg Operations Centre, Room 112 (Simulated NOC/SOC environment)  
**Office Hours:** Wednesdays, 10:00-12:00, via Yggdrasil Service Portal

---

## Lectures

ᚠ **Lecture 1: The Service Economy — Why IT Service Management Matters**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

Information Technology is no longer a back-office function; it is the primary value delivery mechanism of modern organizations. This lecture establishes the foundational premise of IT service management: that IT must be managed as a **service** — a means of enabling value for customers through the facilitation of outcomes — rather than as a collection of technologies. We examine the evolution from "IT as cost center" to "IT as strategic partner," the economic logic of service management, and the cultural shifts required to move from reactive firefighting to proactive service excellence. By 2040, every organization is a technology organization; service management is the discipline that ensures technology delivers business value reliably, efficiently, and securely.

### Key Topics

- **The Service Paradigm:** A service is a means of delivering value to customers by facilitating outcomes they want to achieve without the ownership of specific costs and risks. IT services include: infrastructure services (compute, storage, network), application services (email, ERP, CRM), business services (student registration, financial reporting), and enabling services (security operations, service desk, training). The service provider's job is not to manage technology but to **co-create value** with customers by understanding their needs and designing services that meet them.
- **IT Service Management (ITSM) Evolution:** From the 1980s mainframe era (centralized IT departments, waterfall project management) through the 1990s process standardization (ITIL v1/v2, CCTA, process maturity models), the 2000s alignment frameworks (COBIT, ISO 20000, balanced scorecards), the 2010s agile and DevOps revolutions (breaking down silos, continuous delivery, automation), to the 2020s-2040s platform engineering and AIOps era (self-service platforms, AI-assisted operations, autonomous remediation). Each evolution added capabilities without fully replacing previous paradigms; modern organizations use hybrid models.
- **The Four Dimensions of Service Management:** ITIL 4 organizes service management into four dimensions: **Organizations and People** (culture, skills, roles, communication), **Information and Technology** (services, information, knowledge, supporting technologies), **Partners and Suppliers** (relationships, contracts, integration, multi-sourcing), and **Value Streams and Processes** (activities, workflows, controls, deliverables). No single dimension is sufficient; effective service management balances all four.
- **The Cost of Downtime:** By 2040, the global cost of IT downtime exceeds $10 trillion annually. The direct costs (lost revenue, recovery expenses, regulatory fines) are dwarfed by indirect costs (reputational damage, customer churn, employee burnout). High-profile outages: the 2032 CloudStrike DNS failure (taking down 40% of Fortune 500 websites for 6 hours), the 2035 Nordic Banking Network collapse (3-day payment system outage affecting 20 million customers), and the 2037 Yggdrasil Learning Platform outage (final exam week, 48 hours offline, requiring manual examination procedures). These cases demonstrate that service management is not academic theory; it is business continuity.

### Lecture Notes

The central insight of IT service management is that **technology is not the product; value is.** A student does not want a database; they want to register for courses. A researcher does not want a server; they want to run simulations. A clinician does not want a network; they want to access patient records. The service provider who understands this distinction designs services around outcomes, not components. The service provider who does not understand it delivers technically perfect systems that fail to meet user needs.

**The ITSM profession** has matured from a back-office function to a strategic discipline. The modern ITSM practitioner is part technologist, part business analyst, part psychologist, and part diplomat. They must understand cloud architecture, negotiate with vendors, mediate between development and operations teams, and translate business requirements into technical specifications. The Yggdrasil ITSM program emphasizes this interdisciplinary approach: students take courses in business communication, project management, and organizational psychology alongside technical subjects.

**Service culture** is the hardest aspect of ITSM to implement. Technical staff often view service management processes as bureaucratic overhead: "Why do I need a change request to restart a server?" The answer: because in a complex system, a seemingly simple action can have cascading effects. The 2034 Yggdrasil research prefix leak (Lecture 1 of IT107) was caused by an unapproved configuration change. The change would have taken 30 minutes to review; the outage lasted 20 minutes; the reputational damage persisted for months. Service management processes exist to prevent such failures by ensuring that changes are assessed, authorized, and communicated.

### Required Reading

- AXELOS. (2036). *ITIL 4 Foundation*, 3rd Edition. TSO. Chapters 1-3.
- Orand, B. (2035). *IT Service Management: A Guide for the Modern Era*. Yggdrasil University Press. Chapters 1-2.
- IDC. (2040). "The Global Cost of IT Downtime: 2040 Report." (Read the executive summary and sector analysis.)

### Discussion Questions

1. A developer argues that ITIL processes slow down innovation and that "move fast and break things" is the correct philosophy. How do you respond? Under what circumstances is each philosophy appropriate, and how do you balance them?
2. The "service paradigm" defines a service as facilitating outcomes without transferring ownership of costs and risks. But in cloud computing, customers do bear some risks (data breaches, vendor lock-in). Is cloud computing truly a service under this definition? What are the implications?
3. A 6-hour outage costs a company $100 million in lost revenue. The CEO proposes investing $50 million in redundancy to prevent future outages. Is this a good investment? What analytical framework would you use to evaluate it?

---

ᚢ **Lecture 2: ITIL 4 — The Service Value System and Guiding Principles**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

ITIL (Information Technology Infrastructure Library) is the most widely adopted framework for IT service management, with over 5 million certified practitioners by 2040. ITIL 4, released in 2019 and updated through 2040, represents a paradigm shift from process-centric service management to **value-centric service management**. This lecture covers the ITIL 4 Service Value System (SVS): the guiding principles, governance, service value chain, practices, and continual improvement model that together enable organizations to co-create value with stakeholders.

### Key Topics

- **The Seven Guiding Principles:** (1) **Focus on value** — everything the organization does should link back to value for stakeholders; (2) **Start where you are** — assess current state honestly before implementing change; (3) **Progress iteratively with feedback** — avoid big bang transformations; deliver value in small increments; (4) **Collaborate and promote visibility** — break down silos; share information across teams; (5) **Think and work holistically** — no service component exists in isolation; optimize the whole, not the parts; (6) **Keep it simple and practical** — eliminate waste; do only what adds value; (7) **Optimize and automate** — automate standard tasks to free humans for complex judgment. These principles are universal: they apply to ITSM, DevOps, agile, and any organizational improvement effort.
- **The Service Value System (SVS):** ITIL 4's core model. The SVS receives **inputs** (opportunities and demands from stakeholders) and produces **outputs** (value in the form of products and services). Components: **Guiding Principles** (recommendations for all decisions), **Governance** (evaluation, direction, and monitoring of the organization), **Service Value Chain** (the set of activities required to create value), **Practices** (resources for performing work), and **Continual Improvement** (embedded in all components). The SVS is not a linear process; it is an ecosystem where components interact dynamically.
- **The Service Value Chain:** Six activities that form the core workflow: **Plan** (ensuring shared understanding of vision and status), **Improve** (ensuring continual improvement), **Engage** (understanding stakeholder needs), **Design & Transition** (ensuring products and services meet expectations), **Obtain/Build** (ensuring service components are available), and **Deliver & Support** (ensuring services are delivered and supported). These activities are not sequential; they form a flexible chain where any activity can trigger any other. The value chain is implemented through **value streams** — specific combinations of activities for particular scenarios (e.g., "respond to incident" or "onboard new employee").
- **Governance in ITIL 4:** Governance is the means by which an organization is directed and controlled. ITIL 4 defines three governance activities: **Evaluate** (assessing the organization's strategy, portfolio, and performance), **Direct** (setting policies, priorities, and resources), and **Monitor** (measuring performance and ensuring compliance). Governance is not separate from management; it is the framework within which management operates. The Yggdrasil University Council provides governance for IT services through the Digital Strategy Committee, which evaluates proposals, directs investment, and monitors outcomes.

### Lecture Notes

ITIL 4 is not a cookbook; it is a **philosophy of service**. Unlike ITIL v3, which prescribed 26 processes with rigid inputs, activities, and outputs, ITIL 4 provides principles and models that organizations adapt to their context. This flexibility is both ITIL 4's strength and its criticism: adherents praise its adaptability; detractors argue it is too vague to implement without external consulting. The truth is that ITIL 4, like any framework, requires intelligent adaptation to organizational culture, size, and maturity.

**The guiding principles** are deceptively simple. "Focus on value" seems obvious, yet many IT organizations measure themselves by technical metrics (server uptime, ticket resolution time) rather than business outcomes (student satisfaction, research output, administrative efficiency). The Yggdrasil IT Service Desk shifted from measuring "tickets closed per hour" to "student success rate" (did the student achieve their goal?) and saw satisfaction scores increase by 40%.

**The service value chain** replaces ITIL v3's linear process model with a flexible activity network. This better reflects modern service delivery, where activities are not sequential but interleaved. A DevOps team simultaneously plans sprints, engages with users, designs features, builds code, delivers releases, and improves based on feedback — all within a two-week iteration. The value chain model captures this reality without forcing it into artificial process boundaries.

### Required Reading

- AXELOS. (2036). *ITIL 4 Foundation*, 3rd Edition. TSO. Chapters 4-6.
- Cannon, D. (2035). "From ITIL v3 to ITIL 4: A Critical Analysis." *Journal of Service Management*. (Read the section on value chain vs. process model.)

### Discussion Questions

1. ITIL 4's flexibility allows adaptation but also permits "ITIL in name only" implementations where organizations adopt the vocabulary without the substance. How do you assess whether an organization has genuinely implemented ITIL 4 or is merely performing compliance theater?
2. The guiding principle "start where you are" conflicts with the common consulting impulse to rip and replace. When is incremental improvement appropriate, and when is transformational change necessary? What criteria determine the approach?
3. The service value chain includes "Engage" as a core activity. In a large university with 50,000 students, how do you "engage" effectively at scale? What mechanisms exist for understanding stakeholder needs without being overwhelmed by noise?

---

ᚦ **Lecture 3: Service Design and Architecture — Designing for Reliability**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

Reliability is not an accident; it is the result of intentional design. This lecture covers the principles of **service design**: translating business requirements into technical specifications, designing for maintainability, scalability, and resilience, and creating service architectures that degrade gracefully under stress. We examine design patterns for reliability (redundancy, failover, circuit breakers, bulkheads, rate limiting), the role of architecture decision records (ADRs) in capturing design rationale, and the tension between design perfection and time-to-market. The Yggdrasil Student Information System serves as a case study: designed in 2028 for 30,000 students, now serving 52,000 with 99.99% uptime.

### Key Topics

- **Service Design Processes:** ITIL 4's Design & Transition practice encompasses: requirement gathering (functional and non-functional), service level design (availability, capacity, performance targets), technical architecture (infrastructure, application, data, network), operational model (support structure, monitoring, backup), and service acceptance criteria (how we know the service is ready for production). The design process must balance competing constraints: cost vs. performance, time-to-market vs. quality, flexibility vs. standardization. The Yggdrasil Architecture Review Board evaluates all designs against the Yggdrasil Security Baseline, Cost Efficiency Policy, and Sustainability Charter.
- **Design Patterns for Reliability:** **Redundancy** (N+1, N+2 configurations; no single point of failure); **Failover** (automatic detection of failure and redirection to backup systems); **Circuit Breakers** (preventing cascading failures by stopping requests to failing downstream services); **Bulkheads** (isolating failures to prevent them from spreading — the compartmentalization principle from naval architecture); **Rate Limiting** (preventing overload by throttling requests); **Graceful Degradation** (reducing functionality rather than failing entirely — e.g., showing cached data when real-time data is unavailable); and **Chaos Engineering** (deliberately injecting failures to test resilience). The Yggdrasil Cloud Platform implements all of these patterns by default.
- **Service Level Objectives (SLOs) and Error Budgets:** SRE philosophy (developed at Google, adopted globally by 2040) defines reliability targets as SLOs: "the service will respond to 99.9% of requests within 200ms." The **error budget** is the complement: 0.1% of requests may exceed 200ms. If the error budget is exhausted, new feature development halts until reliability improves. This aligns incentives: product teams want to ship features; SRE enforces quality gates. The Yggdrasil Learning Platform SLO: 99.95% availability during term time, 99.9% during breaks; error budgets are reviewed weekly by the Platform Engineering Team.
- **Architecture Decision Records (ADRs):** Every significant architectural decision is documented in an ADR: context (what problem are we solving?), decision (what did we choose?), consequences (what are the trade-offs?), status (proposed, accepted, deprecated), and alternatives considered. ADRs create organizational memory, prevent repeated debates, and enable new team members to understand why the system is built the way it is. The Yggdrasil Architecture Repository contains 800+ ADRs spanning a decade of decisions.

### Lecture Notes

Service design is where the abstract meets the concrete. A business requirement ("students must be able to register for courses") becomes a technical architecture (web frontend, API gateway, registration microservice, database, payment processor, notification service), which becomes an operational reality (monitoring, alerting, on-call rotations, runbooks, capacity planning). The designer's job is to anticipate how the service will behave under load, under attack, under failure, and under growth — and to make choices that are resilient to all of these.

**The reliability paradox:** Users want 100% availability, but achieving it is exponentially expensive. 99% availability allows 3.65 days of downtime per year; 99.9% allows 8.76 hours; 99.99% allows 52.6 minutes; 99.999% allows 5.26 minutes. Each additional "9" requires more redundancy, more monitoring, more automation, and more operational discipline. The SLO framework forces explicit conversation: "We can achieve 99.99% for $500,000 per year, or 99.999% for $2,000,000. Is the extra reliability worth the cost?" The Yggdrasil Learning Platform targets 99.95% because the cost of the final 0.04% exceeds the benefit.

**Chaos engineering** is the ultimate test of design. By deliberately injecting failures — killing servers, corrupting network packets, saturating CPU — teams discover weaknesses that testing cannot reveal. Netflix's Chaos Monkey (pioneered 2011) evolved into sophisticated failure injection platforms by 2040. The Yggdrasil Chaos Engineering Program runs monthly "game days" where failure scenarios are injected into production systems (during low-risk windows) to validate resilience. The rule: if you haven't tested it, it doesn't work.

### Required Reading

- Beyer, B. et al. (2036). *Site Reliability Engineering*, 2nd Edition. O'Reilly. Chapters 2-4, 7.
- Nygard, M.T. (2035). *Release It!*, 3rd Edition. Pragmatic Bookshelf. Chapters 2-5, 9-10.
- Yggdrasil Architecture Team. (2040). "The Yggdrasil SLO Handbook: Defining, Measuring, and Enforcing Reliability Targets." *UoY Technical Report* TR-2040-05.

### Discussion Questions

1. A product team wants to ship a new feature that increases revenue by 10% but violates the error budget, reducing availability from 99.9% to 99.5%. The SRE team blocks the release. Who is right? What decision framework resolves this conflict?
2. Chaos engineering injects failures into production. A game day causes an unexpected cascade failure that affects real users. Was the game day irresponsible, or is this an acceptable risk? What safeguards should exist?
3. ADRs document decisions but can become stale as technology evolves. An ADR from 2028 mandates a monolithic architecture; the team now wants microservices. Should the ADR be updated, deprecated, or preserved as historical record? What is your ADR lifecycle policy?

---

ᚨ **Lecture 4: Service Transition and Change Management — Controlled Evolution**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

Change is the leading cause of IT service disruption: 80% of outages are caused by changes, not by spontaneous failures. This lecture covers **service transition** — the process of moving new or changed services into production — and **change management** (or change enablement, in ITIL 4 terminology) — the governance process that ensures changes are assessed, authorized, and implemented with minimal risk. We examine change models (standard, normal, emergency), the CAB (Change Advisory Board) structure, automated change validation, and the DevOps approach to high-velocity change. The goal: enabling rapid innovation without sacrificing stability.

### Key Topics

- **Change Types and Models:** ITIL 4 defines three change types: **Standard Changes** (low risk, pre-authorized, well-understood — e.g., adding a new user, deploying a routine patch); **Normal Changes** (require assessment and authorization — most changes fall here, assessed by the Change Advisory Board); and **Emergency Changes** (urgent fixes requiring expedited authorization — e.g., security patches for actively exploited vulnerabilities). The 2040 evolution: **automated standard changes** (self-service portals where users deploy pre-approved blueprints with automatic compliance checking), **data-driven normal changes** (machine learning models that assess change risk based on historical data, test coverage, and blast radius), and **war-room emergency changes** (pre-authorized emergency protocols with mandatory post-implementation review).
- **The Change Advisory Board (CAB):** The CAB is a cross-functional team that reviews, assesses, and authorizes changes. Membership: IT operations (can we support this?), development (what are we changing?), security (what are the risks?), business representatives (what is the impact on users?), and finance (what does it cost?). The CAB evaluates: business justification, technical impact, risk assessment, rollback plan, testing evidence, and communication plan. By 2040, many organizations use **virtual CABs** (asynchronous review via workflow tools) and **automated CABs** (AI-assisted risk scoring with human oversight for high-risk changes). The Yggdrasil CAB meets weekly for normal changes and operates a 24/7 virtual queue for emergency changes.
- **Release and Deployment Management:** The technical process of packaging, testing, and deploying changes. **Release pipelines** (CI/CD — Continuous Integration/Continuous Deployment) automate build, test, and deployment: developers commit code → automated tests run → code is reviewed → deployed to staging → integration tests run → deployed to production (with canary or blue-green deployment). **Deployment strategies:** big bang (all at once — risky), rolling (gradual replacement — moderate risk), blue-green (parallel environments — low risk, high cost), and canary (deploy to 1% of users, monitor, then expand — lowest risk). The Yggdrasil Platform uses canary deployments for all production changes, with automatic rollback if error rates exceed SLOs.
- **Testing and Validation:** Changes must be tested before deployment. Test types: unit tests (individual components), integration tests (component interactions), end-to-end tests (full user workflows), performance tests (load, stress, soak), security tests (SAST, DAST, penetration testing), and chaos tests (failure injection). **Test coverage** is not merely line coverage but behavioral coverage: does the test suite exercise error handling, edge cases, and concurrent access? The Yggdrasil deployment policy requires 80% line coverage, 100% coverage of critical paths, and passing security scans as prerequisites for CAB approval.

### Lecture Notes

Change management is the most politically fraught process in ITSM. Developers resent it as bureaucratic obstruction; operations teams depend on it for stability; business leaders are frustrated when urgent changes are delayed. The art of change management is not to prevent change but to **enable safe change** — providing guardrails that allow speed without recklessness.

**The DevOps critique of traditional change management** is that it creates a adversarial relationship between development and operations. Developers want to ship code; operations wants to prevent outages; change management becomes the battlefield. The DevOps solution: **automated governance**. Instead of a human CAB reviewing every change, the "CAB" is a set of automated checks: tests must pass, security scans must be clean, SLOs must not be violated. If the automated checks pass, the change deploys automatically. Human review is reserved for changes that fail checks or exceed risk thresholds. The Yggdrasil Platform Engineering team implements this model: 70% of changes are fully automated; 25% require automated risk scoring with human approval; 5% require full CAB review.

**Emergency changes** are the exception that tests the rule. When a critical vulnerability is announced (e.g., Log4Shell, Heartbleed, or their 2040 equivalents), speed is essential: every minute of delay is a minute of exposure. But speed without control creates new risks. The Yggdrasil emergency change protocol: (1) pre-authorized war room activation, (2) impact assessment within 30 minutes, (3) patch deployment to staging within 2 hours, (4) automated testing within 4 hours, (5) production deployment within 6 hours, (6) continuous monitoring for 48 hours, and (7) mandatory post-incident review within 1 week. This protocol balances urgency with discipline.

### Required Reading

- Humble, J. & Farley, D. (2036). *Continuous Delivery*, 2nd Edition. Addison-Wesley. Chapters 1-3, 10-12.
- Kim, G. et al. (2035). *The DevOps Handbook*, 2nd Edition. IT Revolution Press. Chapters 8-10.
- AXELOS. (2036). *ITIL 4: Direct, Plan and Improve*. TSO. Chapter 4: "Change Enablement."

### Discussion Questions

1. A developer submits a change to the CAB with no tests, no rollback plan, and no security review. They argue the change is "simple" and the process is "overkill." How do you respond? What is the minimum viable change documentation, and who defines it?
2. Automated change governance requires trust in automated tests. But tests can have false negatives (missing bugs) and false positives (blocking good changes). How do you maintain confidence in the automated gate without making it so strict that it blocks innovation?
3. The 2032 CloudStrike outage was caused by a configuration change that bypassed the normal change process as an "emergency." How do you prevent emergency change protocols from becoming a loophole for normal changes? What checks and balances exist?

---

ᚱ **Lecture 5: Service Operation — Incident, Problem, and Event Management**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

Even perfectly designed services fail. When they do, operational practices determine whether the failure is a minor blip or a catastrophic outage. This lecture covers the core ITIL operational practices: **incident management** (restoring normal service as quickly as possible), **problem management** (identifying and eliminating root causes of incidents), and **event management** (monitoring and responding to automated alerts). We examine the 2040 operational landscape, where AIOps (Artificial Intelligence for IT Operations) handles routine events, human operators focus on complex incidents, and problem management uses predictive analytics to prevent failures before they occur.

### Key Topics

- **Incident Management:** An incident is an unplanned interruption or reduction in quality of an IT service. The incident management process: **detection** (automated monitoring, user reports), **logging** (recording time, symptoms, affected services), **categorization** (matching to known patterns), **prioritization** (impact × urgency), **diagnosis** (identifying cause), **resolution** (fixing or circumventing), **closure** (confirming restoration and documenting lessons), and **communication** (keeping stakeholders informed). Key metrics: Mean Time To Detect (MTTD), Mean Time To Respond (MTTR), Mean Time To Resolve (MTTR-sometimes distinguished from respond), and incident frequency. The Yggdrasil Service Desk targets MTTD <5 minutes (via automated alerting) and MTTR <30 minutes for critical incidents.
- **Problem Management:** A problem is the underlying cause of one or more incidents. **Reactive problem management** (identifying root causes after incidents occur) uses techniques: 5 Whys (iterative questioning), Ishikawa diagrams (fishbone diagrams mapping causes to categories), fault tree analysis (top-down logical decomposition), and formal methods (model checking, static analysis). **Proactive problem management** (preventing problems before they cause incidents) uses trend analysis (identifying patterns in incident data), capacity planning (preventing resource exhaustion), and chaos engineering (discovering weaknesses). The Yggdrasil Problem Management Team reviews all major incidents (Priority 1 and 2) and conducts root cause analysis within 72 hours.
- **Event Management:** An event is any detectable occurrence in the IT infrastructure. Events are classified: **informational** (routine status updates — logged but not alerted), **warning** (threshold approaching — logged and may trigger proactive action), and **exception** (failure or breach — logged and alerted immediately). By 2040, **AIOps platforms** (Moogsoft, BigPanda, Dynatrace Davis) use machine learning to: correlate related events into incidents (reducing alert noise by 90%), identify anomalous patterns (detecting failures before they impact users), and suggest remediation actions (auto-remediating routine issues). The Yggdrasil AIOps platform processes 100,000 events per minute, auto-remediates 40% of routine issues, and escalates 5% to human operators.
- **Major Incident Management:** A major incident is a high-impact, urgent disruption requiring extraordinary response. The major incident process: activate the **Major Incident Team** (cross-functional war room with technical, communications, and business leads), establish **command and control** (clear roles: incident commander, scribe, communications lead, technical lead), implement **stakeholder communication** (regular status updates to executives, users, and regulators), and conduct **post-incident review** (blameless retrospective focusing on systemic improvements). The Yggdrasil Major Incident Protocol requires executive notification within 15 minutes, user communication within 30 minutes, and a blameless post-mortem within 5 business days.

### Lecture Notes

Operational excellence is invisible. When services work, nobody notices the operations team; when they fail, everyone blames them. The operations professional's job is to make the invisible infrastructure reliable, to respond to failures with calm competence, and to learn from every incident. It is a discipline of vigilance, humility, and continuous improvement.

**Incident management vs. problem management** is the most commonly confused distinction in ITSM. Incident management is about **speed**: restore service now, investigate later. Problem management is about **depth**: understand why the incident happened and prevent recurrence. These are separate processes with different metrics: incident management is measured by MTTR (faster is better); problem management is measured by recurrence rate (fewer repeat incidents is better). An organization with fast incident response but no problem management is a firefighting culture — heroic but unsustainable.

**Blameless post-mortems** are the cultural innovation that separates learning organizations from punitive ones. When an outage occurs, the natural human response is to find who is at fault and punish them. This response destroys psychological safety and drives incidents underground (people hide mistakes to avoid blame). The blameless post-mortem focuses on **systemic factors**: what about our processes, tools, or assumptions allowed this mistake to happen? The 2034 Yggdrasil prefix leak post-mortem identified not "the engineer who made the typo" but "the lack of automated configuration validation that would have caught the typo before deployment."

### Required Reading

- Allspaw, J. (2035). "Blameless PostMortems and a Just Culture." *Yggdrasil Operations Review*. (The foundational essay on blameless incident analysis.)
- AXELOS. (2036). *ITIL 4: Create, Deliver and Support*. TSO. Chapters 3-5.
- Gartner. (2040). "The State of AIOps: From Hype to Production." (Read the maturity model and adoption statistics.)

### Discussion Questions

1. An engineer accidentally deletes a production database during maintenance. The incident is restored from backup within 2 hours, but 4 hours of data is lost. The engineer is terrified of punishment. How do you conduct the post-mortem? What do you say to the engineer? What systemic changes do you implement?
2. AIOps auto-remediates routine issues but sometimes makes incorrect decisions (e.g., restarting a service that is intentionally paused for maintenance). How do you build trust in automated remediation? What human oversight is appropriate?
3. MTTR is a common operational metric, but it can be gamed: teams close incidents quickly by applying workarounds rather than fixes, leading to recurring incidents. How do you measure operational effectiveness without perverse incentives?

---

ᚲ **Lecture 6: DevOps — Culture, Automation, and Measurement**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

DevOps is not a tool, a team, or a job title — it is a **cultural and professional movement** that stresses communication, collaboration, and integration between software developers and IT operations professionals. This lecture covers the three pillars of DevOps: **culture** (shared ownership, blamelessness, learning from failure), **automation** (infrastructure as code, CI/CD pipelines, automated testing), and **measurement** (deployment frequency, lead time, change failure rate, MTTR — the DORA metrics). We trace DevOps from its 2009 origins through the 2010s "DevOps toolchain" era to the 2040 "platform engineering" era, where internal developer platforms abstract infrastructure complexity and enable self-service deployment.

### Key Topics

- **The CALMS Model:** Culture (shared goals, psychological safety, blameless post-mortems), Automation (eliminating toil through scripting and tooling), Lean (eliminating waste, optimizing flow), Measurement (data-driven decision making), and Sharing (openness, collaboration, knowledge transfer). The CALMS model provides a holistic framework for DevOps adoption: organizations that focus only on automation (buying CI/CD tools without cultural change) fail; organizations that address all five dimensions succeed. The Yggdrasil Platform Engineering Team uses CALMS as a maturity assessment tool, scoring each dimension quarterly.
- **The DORA Metrics:** The DevOps Research and Assessment (DORA) team's four key metrics predict software delivery performance: **Deployment Frequency** (how often deployments occur — elite teams deploy on demand, multiple times per day), **Lead Time for Changes** (time from code commit to production — elite teams: <1 hour), **Change Failure Rate** (percentage of changes causing production failures — elite teams: <5%), and **Time to Restore Service** (MTTR after failure — elite teams: <1 hour). The 2040 state of practice: elite teams deploy 50+ times per day with <2% change failure rate. The Yggdrasil Student Portal deploys 30 times per day on average, with a 1.5% change failure rate.
- **Infrastructure as Code (IaC):** Managing infrastructure (servers, networks, databases, load balancers) through machine-readable definition files rather than manual configuration. Tools: Terraform (declarative, multi-cloud), Pulumi (programmatic, general-purpose languages), Ansible (imperative, agentless), and CloudFormation (AWS-native). IaC enables: version control (infrastructure changes are code-reviewed), reproducibility (identical environments across dev/staging/prod), and automated testing (static analysis, policy-as-code, compliance scanning). The Yggdrasil infrastructure is 100% defined as code; no manual server configuration is permitted.
- **CI/CD and GitOps:** Continuous Integration (automated build and test on every code commit) and Continuous Delivery (automated deployment to production after passing tests). **GitOps** (pioneered by Weaveworks, ubiquitous by 2040) uses Git as the single source of truth for infrastructure and application state: operators commit desired state to Git; automated agents (ArgoCD, Flux) reconcile the live system with the Git state. GitOps provides: full audit trail (who changed what, when), easy rollback (revert the Git commit), and drift detection (alerts when live state diverges from Git). The Yggdrasil Platform uses GitOps for all Kubernetes workloads, with ArgoCD managing 2,000+ application deployments.

### Lecture Notes

DevOps is the most significant operational innovation since the assembly line. Before DevOps, software development and IT operations were separate organizations with conflicting goals: developers were measured by features shipped; operations was measured by uptime. The inevitable result: developers threw code "over the wall" to operations, who struggled to deploy and maintain it. DevOps breaks down this wall by making both teams responsible for the full lifecycle: "you build it, you run it."

**The "you build it, you run it" principle** is transformative but challenging. Developers who run their own services gain direct feedback from production (they feel the pain of their own design decisions), but they also acquire operational responsibilities that may not align with their skills or interests. The platform engineering model addresses this: a platform team builds internal developer platforms that abstract operational complexity (deployment, monitoring, security scanning, incident response) behind self-service APIs and GUIs. Developers "run" their services in the sense that they are responsible for them, but the platform handles the mechanical operations.

**Toil** is the operational work that is manual, repetitive, automatable, tactical, devoid of enduring value, and that scales linearly with service growth. Examples: manually provisioning user accounts, manually deploying code, manually rotating logs, manually responding to routine alerts. DevOps demands that teams measure their toil and systematically eliminate it through automation. Google's SRE book sets a target: no more than 50% of an engineer's time should be spent on toil; the rest should be spent on engineering (improving systems, building automation, reducing future toil). The Yggdrasil Platform Engineering team tracks toil metrics and prioritizes automation projects that eliminate the most toil per engineering hour invested.

### Required Reading

- Kim, G. et al. (2035). *The DevOps Handbook*, 2nd Edition. IT Revolution Press. Chapters 1-4, 11-14.
- Forsgren, N. et al. (2036). *Accelerate: The Science of Lean Software and DevOps*, Updated Edition. IT Revolution Press. (Read the DORA metrics research and case studies.)
- Limoncelli, T.A. et al. (2035). *The Site Reliability Workbook*. O'Reilly. Chapters 1-3.

### Discussion Questions

1. DevOps requires cultural change, but culture cannot be mandated by management. How do you cultivate DevOps culture in an organization with deeply entrenched silos? What are the leverage points for cultural transformation?
2. "You build it, you run it" makes developers responsible for operations. But developers may lack operational expertise, leading to poorly maintained services. Is platform engineering the solution, or does it reintroduce the wall between dev and ops under a different name?
3. A team argues that their manual deployment process is "simple" and "works fine," resisting CI/CD automation. They deploy once per month with few failures. How do you make the business case for automation? What metrics demonstrate the cost of manual processes?

---

ᚷ **Lecture 7: Site Reliability Engineering (SRE) — Google’s Approach to Scaling**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

Site Reliability Engineering (SRE) is what you get when you treat operations as a software problem and staff it with software engineers. Developed at Google in the early 2000s and codified in the *Site Reliability Engineering* book (2016), SRE has become the dominant operational paradigm for large-scale technology organizations by 2040. This lecture covers the core SRE practices: **error budgets** (balancing reliability and innovation), **toil reduction** (automating operational work), **service level objectives** (quantifying reliability), **on-call engineering** (humans + automation for incident response), and **capacity planning** (ensuring sufficient resources without wasteful over-provisioning). We examine how SRE differs from traditional operations and from DevOps, and how organizations adopt SRE practices at different scales.

### Key Topics

- **Error Budgets and Reliability Trade-offs:** SRE's central innovation: product development and SRE agree on an availability target (SLO), which implies an error budget (100% - SLO). If the service is 99.9% available, the error budget is 0.1% downtime per year (8.76 hours). When the error budget is healthy, product teams can launch new features. When the error budget is exhausted, launches freeze until reliability improves. This **aligns incentives**: product teams are motivated to build reliable features (because unreliable features cost them launch velocity), and SRE teams are motivated to enable launches (because overly conservative SLOs unnecessarily block innovation). The Yggdrasil Learning Platform has a term-time SLO of 99.95% (4.38 hours error budget per year) and a break-time SLO of 99.9% (8.76 hours).
- **Toil and Engineering Time:** SRE teams spend their time on two categories: **toil** (manual, repetitive, automatable work) and **engineering** (improving systems, building automation, developing new capabilities). Google's rule: SRE teams should spend no more than 50% of their time on toil; if toil exceeds 50%, the team stops taking on new operational responsibilities until toil is reduced through automation or process improvement. The Yggdrasil SRE team tracks toil quarterly: currently 35% toil, 65% engineering, with a target of 25% toil by 2042.
- **Service Level Objectives, Indicators, and Agreements:** **SLIs** (Service Level Indicators) are quantitative measures of service quality (e.g., request latency, error rate, throughput). **SLOs** (Service Level Objectives) are target values for SLIs (e.g., "99% of requests complete in <200ms"). **SLAs** (Service Level Agreements) are contracts with consequences: if the service fails to meet the SLO, the provider pays penalties or offers credits. SRE focuses on SLOs, not SLAs: internal operational targets that drive engineering decisions. The Yggdrasil Platform defines SLIs for every service, with tier-based SLOs (Tier 1: 99.99%, Tier 2: 99.95%, Tier 3: 99.9%).
- **On-Call and Incident Response:** SRE teams rotate on-call responsibilities, with strict limits on burden: no more than one incident per 12-hour shift requiring human intervention, and compensation for on-call work (time off or pay). On-call engineers are supported by **playbooks** (documented procedures for common incidents), **automated remediation** (self-healing systems that resolve routine issues), and **escalation paths** (senior engineers and subject matter experts available for complex incidents). The Yggdrasil SRE rotation is one week in four, with automated systems handling 80% of alerts without waking the on-call engineer.
- **Capacity Planning and Load Testing:** Capacity planning ensures that services have sufficient resources to handle demand without excessive waste. Methods: **demand forecasting** (extrapolating from historical growth and planned launches), **load testing** (simulating peak traffic to identify bottlenecks), and **auto-scaling** (automatically adding or removing resources based on real-time demand). The 2040 approach: **predictive auto-scaling** (ML models forecast demand 30-60 minutes ahead, pre-warming resources before traffic arrives) and **bin packing optimization** (efficiently distributing workloads across servers to minimize cost). The Yggdrasil Cloud Platform uses predictive auto-scaling for all Tier 1 services, reducing over-provisioning by 30%.

### Lecture Notes

SRE is not a job title; it is a **way of thinking about operations**. The SRE practitioner is a software engineer who happens to work on operational problems. They write code to automate toil, design systems for reliability, and use data to make decisions. The SRE book's subtitle — "How Google Runs Production Systems" — is descriptive, not prescriptive: SRE principles apply to organizations of any size, though implementation details vary.

**Error budgets** are the mechanism by which SRE resolves the traditional conflict between development and operations. Without error budgets, development wants to launch features (risking reliability) and operations wants to block launches (preserving reliability). The debate is subjective and political. With error budgets, the debate becomes objective and data-driven: "We agreed on 99.9% availability. We have used 80% of the error budget this quarter. We can launch one more feature, but then we freeze until the next quarter." This removes emotion from the decision and aligns both teams around a shared goal.

**Toil is the enemy of engineering.** Every hour an SRE spends manually restarting servers, copying log files, or updating configuration is an hour not spent improving the system. Toil compounds: as the service grows, the toil grows linearly, consuming an ever-larger fraction of the team's capacity. The only sustainable response is automation: writing software that eliminates the toil permanently. The Yggdrasil SRE team maintains a "toil budget": each quarter, they allocate 20% of engineering capacity to toil-reduction projects, ensuring that operational work does not consume the entire team.

### Required Reading

- Beyer, B. et al. (2036). *Site Reliability Engineering*, 2nd Edition. O'Reilly. Chapters 1-4, 7, 10, 15.
- Beyer, B. et al. (2035). *The Site Reliability Workbook*. O'Reilly. Chapters 1-3, 7-9.
- Jones, C. et al. (2036). "SRE at Scale: Lessons from Organizations Beyond Google." *ACM Queue*. (Case studies from Netflix, Amazon, and Yggdrasil.)

### Discussion Questions

1. Error budgets create a "shared pain" model where product teams feel the consequences of unreliable features. But what if the product team disagrees with the SLO? They might argue that 99.99% is unnecessarily conservative. How do you negotiate SLOs? What data informs the negotiation?
2. Google's "50% toil" rule assumes that toil can always be automated. What about operational work that requires human judgment (e.g., investigating novel security incidents, mediating complex customer issues)? Is this toil or engineering? How do you categorize it?
3. SRE was developed at Google, which has a single monolithic code repository and a unified infrastructure stack. How do you adapt SRE practices to an organization with heterogeneous technologies, legacy systems, and siloed teams? What compromises are necessary?

---

ᚹ **Lecture 8: Monitoring, Observability, and AIOps**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

You cannot manage what you cannot measure, and you cannot measure what you cannot see. This lecture covers the three pillars of operational visibility: **monitoring** (knowing when something is wrong based on predefined thresholds and alerts), **observability** (understanding why something is wrong based on telemetry exploration), and **AIOps** (using artificial intelligence to augment human operational capabilities). By 2040, the distinction between monitoring and observability has blurred: modern platforms provide both, using high-cardinality telemetry (metrics, logs, traces) and AI-assisted analysis to detect, diagnose, and remediate issues faster than humanly possible.

### Key Topics

- **Metrics, Logs, and Traces (The Three Pillars):** **Metrics** are numerical measurements over time (CPU usage, request latency, error rate — typically stored in time-series databases like Prometheus, InfluxDB, or M3). **Logs** are timestamped records of events (application logs, system logs, audit logs — typically stored in Elasticsearch, Loki, or Splunk). **Traces** follow requests across distributed systems (OpenTelemetry spans, Jaeger traces, Zipkin traces), enabling identification of latency bottlenecks in microservices architectures. The 2040 standard: unified telemetry pipelines that collect all three types, correlate them automatically, and present them through a single interface.
- **Observability vs. Monitoring:** Monitoring asks "Is the system healthy?" based on known indicators. Observability asks "Why is the system behaving this way?" based on exploratory analysis of telemetry. Monitoring is sufficient for stable systems with known failure modes; observability is necessary for complex distributed systems where novel failures emerge constantly. The shift from monitoring to observability reflects the shift from monoliths to microservices: in a monolith, you can predict what will fail; in a distributed system, you cannot. The Yggdrasil Platform uses both: monitoring for known conditions, observability for unknown unknowns.
- **AIOps Platforms:** AIOps applies machine learning to operational data for: **anomaly detection** (identifying unusual patterns without predefined thresholds), **event correlation** (grouping thousands of alerts into a small number of actionable incidents), **root cause analysis** (suggesting probable causes based on historical patterns), **predictive maintenance** (forecasting failures before they occur), and **automated remediation** (executing runbooks without human intervention). Leading platforms: Dynatrace Davis, Datadog Watchdog, Moogsoft, and the open-source OpenTelemetry Collector with ML plugins. The Yggdrasil AIOps platform reduces alert noise by 95% and auto-remediates 40% of routine issues.
- **Distributed Tracing and OpenTelemetry:** In a microservices architecture, a single user request may traverse 20+ services. When the request is slow, which service is the bottleneck? Distributed tracing assigns a unique trace ID to each request and propagates it across service boundaries, creating a detailed latency map. **OpenTelemetry** (CNCF project, standard by 2030) provides vendor-neutral APIs, SDKs, and collectors for traces, metrics, and logs. By 2040, OpenTelemetry is the de facto standard; vendor-specific agents are deprecated. The Yggdrasil Platform auto-instruments all services with OpenTelemetry, with trace sampling rates adjusted by service criticality.
- **SLI/SLO Monitoring and Alerting:** Alerts should be based on SLOs, not symptoms. "CPU > 90%" is a symptom alert — it may or may not affect users. "Error rate > 0.1% for 5 minutes" is an SLO-based alert — it directly measures user impact. Google's alerting philosophy: pages should be **urgent, actionable, and user-facing**. If an alert is not urgent (can wait until morning), not actionable (no clear response), or not user-facing (internal metric with no customer impact), it should be a ticket, not a page. The Yggdrasil on-call rotation receives ~3 pages per week, all of which meet the urgent-actionable-user-facing criteria.

### Lecture Notes

Operational visibility is the foundation of reliability. An organization with perfect architecture but no visibility is flying blind: failures go undetected, degradation goes unnoticed, and improvements are unmeasured. The evolution from monitoring to observability to AIOps reflects the increasing complexity of systems: as systems become more complex, human operators need more sophisticated tools to understand them.

**High-cardinality metrics** are the technical enabler of modern observability. Traditional monitoring systems struggled with cardinality: a metric with many unique label combinations (e.g., `http_requests_total{method="GET",endpoint="/api/users",status="200",user_id="12345"}`) would overwhelm the time-series database. Modern systems (Thanos, Cortex, Mimir, VictoriaMetrics) use columnar storage and aggregation techniques to handle billions of time series. The Yggdrasil observability platform stores 50 million active time series with 30-day retention, queried through a Prometheus-compatible API.

**The danger of over-alerting** is well-documented: an on-call engineer woken by 20 false-positive alerts per night will soon stop responding to alerts entirely (alert fatigue). The solution is not to add more alerts but to add **better** alerts: SLO-based, symptom-oriented, and carefully tuned. The Yggdrasil SRE team maintains a "alert quality score": (true positives) / (true positives + false positives). Alerts with a score <50% are revised or removed. The team target is 90% alert quality.

### Required Reading

- Majors, C., Fong-Jones, L., & Wilk, G. (2036). *Observability Engineering*. O'Reilly. Chapters 1-4, 7-9.
- Gartner. (2040). "Market Guide for AIOps Platforms." (Read the capability assessment and vendor landscape.)
- OpenTelemetry Project. (2040). *OpenTelemetry Documentation*. https://opentelemetry.io/docs/ (Read the introduction and instrumentation guides.)

### Discussion Questions

1. AIOps promises to reduce operational burden, but it also creates dependency on opaque ML models. When an AIOps system makes an incorrect remediation decision, who is responsible? How do you maintain human accountability in an AI-augmented operation?
2. Distributed tracing adds overhead to every request (propagating trace IDs, recording spans). For a high-throughput service processing 100,000 requests per second, this overhead can be significant. How do you balance observability completeness against performance cost? What sampling strategies exist?
3. An executive demands a real-time dashboard showing "system health" as a single green/yellow/red indicator. You argue that such a simplification is misleading. How do you communicate the complexity of distributed system health? What visualization approaches convey nuance without overwhelming?

---

ᚺ **Lecture 9: Agile, Lean, and IT Service Delivery**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

Agile and Lean are not software development methodologies; they are **philosophies of work** that emphasize iterative delivery, customer collaboration, and waste elimination. This lecture examines how agile and lean principles intersect with IT service management: agile development (Scrum, Kanban, SAFe), lean IT (value stream mapping, kaizen, just-in-time delivery), and the 2040 evolution toward **flow-based delivery** (continuous flow of value from idea to production, managed through WIP limits, cycle time metrics, and pull-based scheduling). We address the tension between agile's embrace of change and ITIL's emphasis on control, and how modern organizations reconcile them.

### Key Topics

- **Agile Fundamentals:** The Agile Manifesto (2001) values: individuals and interactions over processes and tools, working software over comprehensive documentation, customer collaboration over contract negotiation, responding to change over following a plan. Scrum (2-week sprints, product backlog, daily standups, sprint reviews) and Kanban (visual workflow, WIP limits, continuous flow) are the dominant agile frameworks. By 2040, **agile maturity** has evolved: most organizations practice "agile" (small iterations, cross-functional teams); fewer practice "Agile" (rigid Scrum ceremonies); and the leading edge practices **flow-based delivery** (no sprints, just continuous prioritization and delivery).
- **Lean IT and Value Stream Mapping:** Lean (originating in Toyota Production System) focuses on eliminating waste (muda): overproduction, waiting, transport, over-processing, inventory, motion, defects, and unused talent. **Value stream mapping** visualizes the end-to-end flow of value from customer request to delivered service, identifying wait times, handoffs, and rework. The Yggdrasil IT Value Stream Mapping Program identified that 70% of "lead time" for new services was spent waiting: waiting for approval, waiting for resources, waiting for testing environments. By eliminating these waits, the average service delivery time dropped from 6 months to 3 weeks.
- **SAFe and Enterprise Agile:** The Scaled Agile Framework (SAFe) attempts to apply agile practices to large enterprises with hundreds of teams. Critics argue SAFe is "agile in name only" — too prescriptive, too top-down, and too focused on process over people. Proponents argue it provides necessary coordination for large-scale delivery. By 2040, the enterprise agile landscape has diversified: Spotify's squad model (autonomous teams with weak coordination), Team Topologies (organizing teams into stream-aligned, platform, enabling, and complicated-subsystem types), and unSAFe (enterprise agility without SAFe's prescriptive framework). The Yggdrasil IT organization uses Team Topologies: 12 stream-aligned teams, 3 platform teams, and 2 enabling teams.
- **Agile and ITIL Integration:** The perceived conflict: ITIL emphasizes process control, change approval, and documentation; agile emphasizes speed, autonomy, and minimal documentation. The resolution: **right-sized process**. Standard changes (low risk, pre-approved) flow through agile pipelines without CAB review. Normal changes (higher risk) require CAB approval but use agile ceremonies for assessment. Emergency changes use pre-authorized protocols. Documentation is automated (architecture decisions in ADRs, runbooks generated from code, compliance evidence collected automatically). The Yggdrasil ITSM-Agile Integration Guide defines 12 integration patterns for common scenarios.

### Lecture Notes

Agile and ITIL are not enemies; they are **complements that address different concerns**. Agile answers "How do we build the right thing quickly?" ITIL answers "How do we ensure what we built works reliably?" An organization that is agile without ITIL ships features quickly but suffers from outages and technical debt. An organization that is ITIL without agile ships reliable services that fail to meet evolving user needs. The modern organization needs both: agile for innovation, ITIL for stability, and DevOps/SRE as the bridge between them.

**Flow-based delivery** is the 2040 synthesis of agile and lean. Instead of two-week sprints with batch planning, teams work from a continuously prioritized backlog, pulling work when they have capacity. WIP (Work In Progress) limits ensure that teams do not start more work than they can finish, reducing context switching and improving cycle time. Cycle time (time from start to finish) and throughput (items completed per week) replace velocity (story points per sprint) as the primary metrics. The Yggdrasil Platform Engineering team uses flow-based delivery with a WIP limit of 3 items per engineer, achieving an average cycle time of 4 days for standard features.

**Team Topologies** is the organizational design framework that enables agile at scale. The insight: not all teams should be structured the same way. **Stream-aligned teams** (also called "product teams") own a stream of work from idea to production and are aligned to business domains. **Platform teams** provide internal services (deployment platforms, monitoring tools, security scanning) that reduce cognitive load for stream-aligned teams. **Enabling teams** (experts in security, compliance, performance) help stream-aligned teams overcome specific obstacles. **Complicated-subsystem teams** own complex components (machine learning models, low-level networking) that require deep expertise. The Yggdrasil IT reorganization of 2035 used Team Topologies to reduce cross-team dependencies by 60%.

### Required Reading

- Beck, K. et al. (2001/2035). *The Agile Manifesto*. (The original manifesto; read with the 2035 retrospective on agile evolution.)
- Skelton, M. & Pais, M. (2035). *Team Topologies*, 2nd Edition. IT Revolution Press. Chapters 1-4, 7.
- Poppendieck, M. & Poppendieck, T. (2035). *Lean Software Development*, Updated Edition. Addison-Wesley. Chapters 1-3, 6.

### Discussion Questions

1. SAFe is widely adopted by large enterprises but criticized by agile purists as "waterfall in agile clothing." Is SAFe a legitimate scaling framework or a cargo cult? Under what circumstances does it succeed or fail?
2. Team Topologies defines four team types, but real organizations have messy boundaries. A team starts as stream-aligned but gradually accumulates platform responsibilities. How do you prevent "platform drift"? When and how do you split teams?
3. The integration of agile and ITIL requires compromise. A strict ITIL practitioner insists on full CAB review for every production change; an agile coach insists on continuous deployment without gates. How do you mediate? What is the minimum viable governance for continuous delivery?

---

ᚻ **Lecture 10: Continuous Improvement and Service Measurement**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

Continuous improvement is the engine that drives service excellence. Without it, services stagnate: technical debt accumulates, user needs evolve unchecked, and operational practices become outdated. This lecture covers the frameworks, metrics, and cultural practices that enable sustained improvement: **ITIL's Continual Improvement Model** (identify, plan, execute, evaluate), **kaizen** (incremental daily improvement), **Six Sigma** (statistical quality control), **balanced scorecards** (measuring across financial, customer, process, and learning dimensions), and the **metrics-driven culture** of high-performing IT organizations. We examine the danger of vanity metrics and the importance of actionable metrics that drive behavioral change.

### Key Topics

- **The ITIL Continual Improvement Model:** A structured approach: (1) **What is the vision?** (align improvement with organizational strategy), (2) **Where are we now?** (baseline current performance), (3) **Where do we want to be?** (define measurable targets), (4) **How do we get there?** (plan initiatives), (5) **Take action** (execute improvements), (6) **Did we get there?** (measure results), (7) **How do we keep the momentum going?** (embed improvements, iterate). The model is not a one-time project but a perpetual cycle. The Yggdrasil Continual Improvement Office coordinates improvement initiatives across IT, with quarterly reviews and an annual improvement strategy.
- **Kaizen and Daily Improvement:** Kaizen (Japanese: "change for better") emphasizes small, daily improvements by frontline workers rather than large top-down initiatives. Examples: a service desk analyst suggesting a knowledge base article template that reduces ticket resolution time by 2 minutes; a developer refactoring a test that takes 30 seconds to run into one that takes 5 seconds. Cumulatively, these micro-improvements produce macro results. The Yggdrasil "Improvement Monday" program dedicates the first Monday of each month to team-identified improvements, with no feature development scheduled.
- **Metrics and Measurement:** Good metrics are: **comparative** (show change over time), **understandable** (clear to all stakeholders), **ratios or rates** (rather than absolute numbers, which scale with organization size), and **actionable** (drive behavioral change). Bad metrics are vanity metrics (total page views — up because you bought ads, not because the product improved) or gaming targets (support tickets closed per hour — up because agents close tickets without resolving issues). The Yggdrasil IT Balanced Scorecard measures: financial (IT cost per student, cloud spend efficiency), customer (student satisfaction, faculty NPS), process (deployment frequency, change failure rate, MTTR), and learning (training hours, certification attainment, internal mobility).
- **Benchmarking and Maturity Models:** Benchmarking compares organizational performance against peers or industry standards. The **CMMI** (Capability Maturity Model Integration) defines five maturity levels: Initial (chaotic), Managed (projects controlled), Defined (organization-wide standards), Quantitatively Managed (metrics-driven), and Optimizing (continuous improvement). By 2040, most organizations target Level 3-4; Level 5 is rare and often not cost-effective. The Yggdrasil IT organization achieved CMMI Level 4 in 2037, with quantitative management of all core service delivery processes.

### Lecture Notes

Continuous improvement is the antidote to organizational entropy. Left to themselves, systems become more complex, processes become more bureaucratic, and services become less aligned with user needs. Improvement requires intention: dedicated time, clear metrics, and a culture that rewards learning from failure rather than punishing it.

**The metrics paradox** is that measuring something changes behavior — often in unintended ways. When a hospital measured "time to see a doctor," doctors began treating simple cases first to reduce average wait time, leaving complex cases waiting longer. When a software team measures "lines of code written," developers write verbose code. The solution: **measure outcomes, not outputs**. Measure "student success rate" (did the student achieve their goal?) rather than "tickets closed" (how many interactions occurred?). Measure "deployment frequency" (how often can we deliver value?) rather than "hours worked" (how busy were we?).

**Benchmarking** provides valuable context but dangerous comparison. Knowing that your MTTR is 2 hours while the industry median is 4 hours is useful context. But concluding that you are "better" than the industry is misleading: your systems may be simpler, your incidents less severe, or your measurement methodology different. The Yggdrasil IT benchmarking program uses the **Experience Level Framework** (XLF): comparing metrics only with peer institutions of similar size, complexity, and mission. Comparisons with Google or Amazon are discouraged as uninformative.

### Required Reading

- AXELOS. (2036). *ITIL 4: Direct, Plan and Improve*. TSO. Chapters 1-3, 5-6.
- Imai, M. (2035). *Gemba Kaizen*, 2nd Edition. McGraw-Hill. Chapters 1-3.
- Pande, P.S. et al. (2035). *The Six Sigma Way*, Updated Edition. McGraw-Hill. Chapters 1-2, 5.

### Discussion Questions

1. A team identifies 20 improvement opportunities but has capacity for 3. How do they prioritize? What framework evaluates impact, effort, risk, and strategic alignment?
2. "Improvement Monday" dedicates one day per month to improvements. A product manager argues that this slows feature delivery. How do you justify the investment? What evidence supports (or refutes) the value of dedicated improvement time?
3. A metric intended to improve service quality ("average resolution time") inadvertently causes agents to rush complex cases, reducing quality. How do you design metrics that cannot be gamed? What combination of metrics captures both speed and quality?

---

ᚾ **Lecture 11: Platform Engineering — The Future of Internal Infrastructure**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

As organizations adopt cloud-native technologies, Kubernetes, microservices, and DevOps, the complexity faced by application developers has exploded. **Platform engineering** is the discipline of building internal platforms that abstract this complexity, enabling developers to deploy, monitor, and operate services through self-service interfaces without needing expertise in the underlying infrastructure. This lecture covers: the platform engineering model (platform teams as product teams serving internal customers), the internal developer platform (IDP) architecture (backstage, service catalog, golden paths, infrastructure APIs), and the 2040 frontier of **platform as a product** (treating internal platforms with the same rigor as customer-facing products: user research, product roadmaps, and NPS scores).

### Key Topics

- **Platform Teams and Team Topologies:** In the Team Topologies model, **platform teams** provide internal services that reduce cognitive load for stream-aligned teams. The platform team's customers are internal developers; their product is the developer experience. This reframe is crucial: a platform team that builds what they think developers need (without asking) produces tools that are ignored; a platform team that researches developer pain points and builds solutions produces tools that are adopted. The Yggdrasil Platform Engineering Team conducts quarterly developer experience surveys and maintains a public roadmap prioritized by developer NPS scores.
- **Internal Developer Platforms (IDPs):** An IDP is a layer of abstraction between developers and infrastructure: developers interact with the platform (via CLI, GUI, or GitOps) rather than directly with AWS, Kubernetes, or Terraform. Key components: **Service Catalog** (a directory of all services with ownership, dependencies, and documentation — Backstage is the leading open-source solution), **Golden Paths** (pre-approved, best-practice templates for common tasks: "create a new web service," "add a database," "set up monitoring"), **Self-Service Infrastructure** (developers provision resources through the platform, with guardrails enforced automatically), and **Developer Portal** (a unified interface for all developer tools and documentation). The Yggdrasil Developer Portal (built on Backstage) serves 800+ developers with 50+ golden paths.
- **Golden Paths and Guardrails:** A golden path is a supported, best-practice approach to accomplishing a task. It is not the only approach — developers can "go off-road" if needed — but the golden path is the easiest, fastest, and safest option. Guardrails (enforced by the platform) prevent common mistakes: all golden-path services include automated security scanning, all databases are encrypted by default, all deployments use canary rollouts. The platform does not prevent customization; it makes the safe choice the default. The Yggdrasil golden path for "new web service" provisions: a Git repository with CI/CD, a Kubernetes namespace with resource quotas, a monitoring dashboard, a logging pipeline, and a security scan — all in under 5 minutes.
- **Platform as a Product:** The 2040 evolution treats the internal platform as a product with dedicated product managers, user researchers, and roadmaps. The platform team measures: **adoption rate** (percentage of teams using golden paths), **time-to-service** (how long to deploy a new service), **developer satisfaction** (NPS, CSAT), and **incident reduction** (fewer production issues from misconfigured infrastructure). The Yggdrasil Platform Engineering team publishes quarterly "State of the Platform" reports with metrics, roadmap updates, and case studies — treated with the same seriousness as customer-facing product announcements.

### Lecture Notes

Platform engineering is the response to a genuine crisis: the operational complexity of modern infrastructure has exceeded the cognitive capacity of individual developers. A developer in 2010 needed to know a programming language, a framework, and a database. A developer in 2040 needs to know Kubernetes, service meshes, observability, security scanning, GitOps, infrastructure as code, cloud networking, and cost optimization — in addition to programming. This is unsustainable. Platform engineering restores developer productivity by providing paved roads through the complexity.

**The "you build it, you run it" principle** (from DevOps) is correct in intent but incomplete in practice. Developers should own their services, but they should not need to become experts in every layer of the stack. The platform team handles the infrastructure expertise; developers handle the application expertise. The boundary is negotiated: the platform provides compute, storage, networking, and observability; the developer provides code, configuration, and business logic. Both collaborate on security, reliability, and cost.

**Golden paths are not golden cages.** A common criticism of platform engineering is that it stifles innovation by forcing all teams into the same mold. The Yggdrasil response: golden paths are defaults, not mandates. Teams can request exceptions ("we need a GPU-enabled node for ML training"), which the platform team evaluates and either supports (adding the capability to the platform) or denies (with explanation). This negotiation ensures that the platform evolves to meet real needs while maintaining standards. Over time, many "exceptions" become new golden paths.

### Required Reading

- Team Topologies. (2035). *Platform Engineering: What You Need to Know Now*. IT Revolution Press. Chapters 1-3, 5.
- Spotify. (2035). *Backstage: The Open Platform for Developer Portals*. https://backstage.io/docs/ (Read the overview and architecture sections.)
- Yggdrasil Platform Engineering Team. (2040). "The Yggdrasil Developer Platform: A Case Study in Internal Product Management." *UoY Technical Report* TR-2040-11.

### Discussion Questions

1. Platform teams serve internal developers, not external customers. How does this difference affect product management practices? What remains the same, and what must be adapted?
2. A team requests an infrastructure configuration that violates the platform's security baseline (e.g., a public database with no encryption). The team argues they are building a prototype and will fix it later. How does the platform team respond? What is the balance between enabling experimentation and enforcing standards?
3. Golden paths can create dependency on the platform team. If the platform team is slow to add new capabilities, stream-aligned teams may "go rogue" and build their own infrastructure. How do you prevent platform team bottlenecks? What organizational structures enable platform scalability?

---

ᛁ **Lecture 12: The Capstone — Designing an Enterprise Service Management System**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

The IT207 capstone challenges students to design a comprehensive IT service management system for a fictional enterprise: a 5,000-person Nordic healthcare technology company ("NordicHealth") launching a remote patient monitoring platform. Working in teams of 4-5, students define service catalogs, design value streams, establish SLOs, create change management processes, design monitoring and observability architectures, and present a governance framework. The project is evaluated on comprehensiveness, feasibility, alignment with business objectives, and innovation. The final deliverable is a 50-page service management design document and a 20-minute presentation to a panel of ITSM practitioners.

### Key Topics

- **Project Scope and Constraints:** NordicHealth's platform monitors patients with chronic conditions using wearable IoT devices, cloud analytics, and a clinician dashboard. Constraints: HIPAA-equivalent compliance (Nordic Data Compact), 99.99% availability requirement (lives depend on it), 6-month time-to-market, $2 million IT budget, and a hybrid cloud architecture (on-premises patient data, cloud analytics). Students must balance these constraints while designing a service management system that is neither under-engineered (risking outages and compliance failures) nor over-engineered (consuming budget and delaying launch).
- **Service Catalog and Value Streams:** Students define 8-10 IT services (e.g., "Patient Data Ingestion," "Clinician Dashboard," "Alert Notification," "Compliance Reporting") with service owners, SLAs, and dependencies. They design value streams for three scenarios: new patient onboarding, software release, and security incident response. The value stream maps must include: activities, responsible teams, tools, handoffs, wait times, and improvement opportunities.
- **SLOs and Error Budgets:** Students define quantitative reliability targets for each service, with justification based on business impact. They calculate error budgets and design policies for feature freezes, emergency changes, and degradation strategies. They also design a monitoring and alerting architecture (metrics, logs, traces, SLO-based alerts) and an incident response framework (severity levels, escalation paths, communication templates).
- **Governance and Continuous Improvement:** Students design a governance structure (CAB composition, meeting cadence, escalation paths), a change model (standard, normal, emergency), and a continual improvement process (quarterly reviews, improvement backlog, success metrics). They also address organizational design: team structures (stream-aligned, platform, enabling), roles and responsibilities, and skill development plans.

### Lecture Notes

The capstone is where the abstract frameworks of ITIL, DevOps, and SRE become concrete decisions. A student who has memorized the ITIL service value chain must now apply it: "How does 'Engage' work when the customer is a chronically ill patient who may not understand technology?" A student who understands SLOs must now negotiate them: "Is 99.99% availability worth the cost, or should we accept 99.95% and invest the savings in better clinician training?"

**The design constraint exercise** is intentionally challenging. Students consistently discover that they cannot have everything: they must choose between speed and reliability, between compliance and usability, between centralization and autonomy. These trade-offs are the essence of service management. The team that acknowledges trade-offs explicitly and justifies their choices wins higher marks than the team that promises everything.

**The presentation to practitioners** is the capstone's most valuable component. Students present to a panel of CISOs, SRE leads, and IT directors who ask hard questions: "How would you handle a ransomware attack during a pandemic surge?" "What happens when your error budget is exhausted during a regulatory audit?" "How do you justify a $200,000 observability investment to a CFO who sees it as 'nice to have'?" These questions simulate the real pressures of IT leadership and teach students to think on their feet.

### Required Reading

- AXELOS. (2036). *ITIL 4: Direct, Plan and Improve*. TSO. (Reference for governance and improvement design.)
- Beyer, B. et al. (2036). *Site Reliability Engineering*, 2nd Edition. O'Reilly. (Reference for SLO and error budget design.)
- Kim, G. et al. (2035). *The DevOps Handbook*, 2nd Edition. IT Revolution Press. (Reference for value stream and team design.)

### Discussion Questions

1. Your capstone team disagrees on the availability target for the clinician dashboard. One member insists on 99.999% (5 minutes downtime per year); another argues 99.9% is sufficient and the cost difference ($800,000) should fund additional nurses. How do you resolve this? What evidence do you gather?
2. The CIO of NordicHealth demands that all changes be approved by her personally. This creates a bottleneck: changes wait 2 weeks for approval. How do you propose an alternative governance model that maintains accountability without paralysis?
3. Six months into the project, a critical vendor (the IoT device manufacturer) goes bankrupt. The platform depends on their proprietary API. What is your contingency plan? How does your service management system detect and respond to supplier failure?

---

## Final Examination Preparation

The IT207 final examination assesses both theoretical understanding and practical application of service management principles.

### Written Component (90 minutes, closed book)

**Section A: Short Answer (30%)**
- Define the ITIL 4 Service Value System and explain how the service value chain differs from the ITIL v3 process model.
- What are the four DORA metrics? Explain how each metric predicts organizational performance and how they interact.
- Describe the error budget concept. How does it resolve the traditional conflict between development velocity and operational stability?

**Section B: Problem Solving (40%)**
- A SaaS company has a 99.9% availability SLO but has experienced three major outages in the past quarter, exhausting the error budget. The product team wants to launch a major new feature at the end of the quarter. The SRE team argues for a feature freeze. As the VP of Engineering, what is your decision? What data do you need, and what compromises do you propose?
- Design a change management process for an organization that deploys 50 times per day. The process must balance speed (no deployment delays) with safety (no production outages from bad changes). What is automated, what is human-reviewed, and what are the escalation paths?
- A service desk receives 10,000 tickets per month. The average resolution time is 4 hours, but customer satisfaction is low (NPS: -10). Analysis shows that 60% of tickets are for password resets. Design a self-service and automation strategy that improves both efficiency and satisfaction.

**Section C: Essay (30%)**
- Choose one:
  1. "Platform engineering is the natural evolution of DevOps, not its replacement." Evaluate this claim. What does platform engineering add to DevOps, and what does it risk losing?
  2. ITIL is criticized as bureaucratic and anti-agile. Is this criticism fair? Can ITIL 4 and agile coexist, or are they fundamentally incompatible? Use evidence from the course to support your argument.
  3. AIOps promises to automate operational decision-making. In what areas is AIOps most effective, and where does human judgment remain essential? What are the risks of over-automation in IT operations?

### Practical Assessment (Take-home project, 1 week)

Students receive a case study of a fictional organization with documented IT service management challenges. Deliverables:
1. A service catalog with 5-7 services, including owners, SLAs, and dependencies.
2. A value stream map for one scenario (e.g., onboarding a new employee) with identified waste and improvement recommendations.
3. A proposed SLO framework with SLIs, targets, error budgets, and alerting rules for the organization's critical service.
4. A 2-page executive summary for the CIO explaining the current state, proposed improvements, and expected outcomes.

### Sample Practice Problems

1. An organization measures "tickets closed per hour" as a key performance indicator for the service desk. Over time, ticket closure rates increase but customer satisfaction decreases. What is happening? What metrics would better capture service desk effectiveness?
2. A DevOps team deploys 20 times per day with 1% change failure rate. An ITIL practitioner argues this proves DevOps is reckless. How do you demonstrate that this team's performance is actually superior to a traditional team deploying monthly with 0% failure rate?
3. Design an on-call rotation for a team of 6 engineers that ensures 24/7 coverage, limits on-call burden to one week in four, and provides compensation (time off or pay). Include escalation paths and handoff procedures.

---

*"Service management is the art of making technology serve human needs. The frameworks are tools; the people are the purpose. Master the tools, never forget the purpose, and you will build services that endure." — Prof. Baldr Hákonarson, IT207 Opening Lecture, 2040*
