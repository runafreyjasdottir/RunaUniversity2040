# IT207: IT Service Management (ITIL, DevOps, SRE)
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4
**Description:** A comprehensive survey of modern IT service management frameworks, practices, and cultures — ITIL 4, DevOps, and Site Reliability Engineering — examined through the lens of the 2040 IT professional. Students will learn to design, deliver, and continuously improve IT services in an era of AI-augmented operations, distributed autonomous teams, and ever-rising user expectations.

**Prerequisites:** IT201 (System Administration), IT203 (Network Administration)
**Instructor:** Dr. Eiríkr Hrafnsson, Department of Information Technology

**Course Philosophy:** IT service management is the art of making technology invisible. When services work, no one notices — and that is the highest achievement. The ITIL framework provides the vocabulary of service; DevOps provides the culture of collaboration; SRE provides the discipline of reliability engineering. Together, they form the modern triskelion of IT operations. In the Norse tradition, the Norns weave the fates of gods and mortals alike at the Well of Urðr — the ITSM practitioner is the Norn of the digital realm, weaving together people, processes, and technology into a coherent destiny of reliable, valuable service.

---

## Lectures

ᚠ **Lecture 1: The Philosophy of Service — Why ITSM Exists**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Information technology exists to serve. Every server rack, every line of code, every network packet ultimately exists because someone, somewhere, needs to accomplish something — check a bank balance, book a medical appointment, stream a film, collaborate on a document. IT Service Management is the discipline that never forgets this. It is the counterweight to the engineer's natural tendency to optimize for technical elegance rather than user outcomes. This opening lecture establishes the philosophical foundation: why ITSM emerged, what problem it solves, and why, in 2040, it matters more than ever.

### Lecture Notes

The pre-ITSM world was one of heroic individualism. In the 1980s and 1990s, IT operations were dominated by the "super admin" — the person who knew every server by name, who carried configuration state in their head, who could fix anything because they had built everything. This model worked passably at small scale, but it failed catastrophically as organizations grew. When the super admin went on holiday, systems degraded. When they left the company, institutional knowledge evaporated overnight. The Central Computer and Telecommunications Agency (CCTA) of the British government recognized this fragility in the late 1980s and commissioned the first IT Infrastructure Library — ITIL v1 — a collection of best practices for managing IT services systematically rather than heroically.

The core insight of ITIL is deceptively simple: IT is a service organization, and services must be designed, delivered, and improved through structured processes. The ITIL framework introduced concepts that now seem obvious — incident management, change management, service level agreements — but were revolutionary at the time. They replaced intuition with methodology. They made IT operations auditable, trainable, and scalable. By ITIL v3 (2007), the framework had matured into a full service lifecycle: Service Strategy, Service Design, Service Transition, Service Operation, and Continual Service Improvement. ITIL 4 (2019) reframed everything around the Service Value System (SVS) and the four dimensions of service management, emphasizing co-creation of value with stakeholders.

But ITIL alone is not enough. The framework can become rigid, bureaucratic, and slow — a criticism famously leveled by the DevOps movement that emerged around 2009. DevOps argues that the traditional separation between development and operations creates harmful silos: developers optimize for feature velocity, operators optimize for stability, and the resulting friction slows everything down. DevOps proposes a cultural solution: break down the wall, share responsibility, automate everything, measure everything, and continuously improve. The CALMS framework — Culture, Automation, Lean, Measurement, Sharing — captures the DevOps philosophy.

Then came Site Reliability Engineering. Google's 2003 launch of the SRE role — codified in the 2016 O'Reilly book — introduced an engineering discipline to operations. SRE treats operations as a software engineering problem: define Service Level Objectives (SLOs), measure rigorously, use error budgets to balance reliability against feature velocity, and automate away toil. The SRE approach is quantitative where ITIL can be qualitative and DevOps can be cultural.

By 2040, the synthesis is clear. The modern IT professional must be fluent in all three: the process rigor of ITIL, the collaborative culture of DevOps, and the engineering discipline of SRE. AI and automation — self-healing infrastructure, LLM-powered incident response, predictive capacity planning — have not eliminated the need for ITSM; they have elevated it. When machines handle routine operations, the human ITSM practitioner focuses on what machines cannot do: understand value, negotiate priorities, design service experiences, and build the organizational trust that makes technology adoption possible.

The Yggdrasil model of ITSM — developed at this university by Dr. Hafsteinsson (2038) — maps the three frameworks onto the cosmic tree: ITIL is the root system (Urðarbrunnr), the stable foundation of process and governance; DevOps is the trunk and branches, the living collaborative culture that grows and adapts; SRE is the canopy, the engineering discipline that reaches toward the sky and measures itself against objective reality. No one framework is sufficient alone; together they form a complete, living system.

### Required Reading

- Hafsteinsson, E. (2038). *The Yggdrasil Model: Integrating ITIL 4, DevOps, and SRE for the AI-Augmented Enterprise*. University of Yggdrasil Press. Chapters 1–3.
- AXELOS. (2019). *ITIL Foundation: ITIL 4 Edition*. TSO. Chapter 1: "Key Concepts of Service Management."
- Beyer, B., Jones, C., Petoff, J., & Murphy, N. R. (2016). *Site Reliability Engineering*. O'Reilly Media. Chapter 1: "Introduction."
- Kim, G., Humble, J., Debois, P., & Willis, J. (2016). *The DevOps Handbook*. IT Revolution Press. Introduction and Part I.

### Discussion Questions

1. Why did the "super admin" model fail at scale, and what does this tell us about the relationship between individual expertise and organizational resilience?
2. ITIL has been criticized as bureaucratic and slow. Is this a flaw in the framework itself, or a failure of implementation? How does DevOps address these concerns without abandoning process entirely?
3. The Yggdrasil Model describes three roots (ITIL, DevOps, SRE). Is there a fourth root needed for 2040 — perhaps AI governance, sustainability, or something else?

### Practice Problems

- Map your most recent group project experience onto the ITIL Service Value Chain. Identify which activities (Plan, Improve, Engage, Design & Transition, Obtain/Build, Deliver & Support) were present and which were missing.
- Write a one-page reflection: "When was the last time an IT service failed me, and what would a proper ITSM framework have done differently?"

---

ᚢ **Lecture 2: The ITIL 4 Service Value System — Architecture of Service**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

The Service Value System (SVS) is the architectural blueprint of ITIL 4 — the master diagram that shows how all the pieces fit together. Understanding the SVS is like understanding the circuit diagram of a computer: without it, you can replace individual components but you cannot design a system. This lecture dissects each element of the SVS — the guiding principles, governance, the service value chain, practices, and continual improvement — and shows how they interact to transform opportunity and demand into value.

### Lecture Notes

The ITIL 4 SVS diagram, first published by AXELOS in 2019, looks deceptively simple: an outer ring of Guiding Principles and Governance, feeding into a central Service Value Chain of six activities, supported by 34 management Practices, all encircled by Continual Improvement. But within this diagram is a complete theory of organizational value creation.

The **Guiding Principles** are the ethical compass of ITSM. They are not process steps but decision-making heuristics that apply at every level: Focus on Value, Start Where You Are, Progress Iteratively with Feedback, Collaborate and Promote Visibility, Think and Work Holistically, Keep It Simple and Practical, and Optimize and Automate. These seven principles are the closest thing ITIL has to a philosophy — they answer the question "what should we do?" not "how should we do it?" In practice, the principle "Start Where You Are" has saved countless organizations from the catastrophic "big bang" ITIL implementation that collapses under its own weight. Instead of redesigning everything from scratch, assess current capabilities honestly and improve incrementally.

**Governance** in ITIL 4 means the system by which an organization is directed and controlled. The governing body — often a board or executive committee — evaluates, directs, and monitors the organization's activities. In ITSM terms, governance ensures that the service value chain operates in alignment with organizational strategy, regulatory requirements, and stakeholder expectations. The 2040 governance landscape has expanded to include AI ethics boards, algorithmic accountability frameworks, and sustainability reporting requirements — layers that would have been unrecognizable to the ITIL v1 authors of 1989.

The **Service Value Chain** is the operating model: six interconnected activities that convert demand into value. **Plan** ensures shared understanding of vision and direction. **Improve** drives continual enhancement across all dimensions. **Engage** handles all stakeholder interactions. **Design and Transition** ensures products and services meet stakeholder expectations. **Obtain/Build** makes components available. **Deliver and Support** ensures service delivery according to specifications. These are not sequential phases — they are activity streams that interact through value streams, specific combinations tailored to particular scenarios. A new service introduction value stream, for example, might flow Engage → Plan → Design & Transition → Obtain/Build → Deliver & Support, while an incident resolution value stream might flow Engage → Deliver & Support → Improve.

The 34 **Practices** are the capabilities that make the value chain work — from Incident Management and Change Enablement to Workforce and Talent Management. They are the "how" that implements the "what" of the value chain. ITIL 4 organizes them into three categories: General Management Practices (14), Service Management Practices (17), and Technical Management Practices (3). By 2040, several new practices have been proposed at this university, including AI Model Lifecycle Management, Sustainability Management for IT Services, and Autonomous Operations Governance.

**Continual Improvement** is not an afterthought — it is the engine that prevents ossification. The ITIL Continual Improvement Model asks seven questions: What is the vision? Where are we now? Where do we want to be? How do we get there? Take action. Did we get there? How do we keep the momentum going? These questions form an infinite loop, and every IT organization that stops asking them begins to decay. The 2040 twist: AI systems now participate in the improvement loop, automatically detecting patterns in incident data, proposing optimization opportunities, and in some advanced implementations, autonomously executing low-risk improvements with human approval gates.

The SVS is sometimes criticized as "too theoretical" — a fair criticism if the framework is treated as a compliance checklist rather than a design language. But when used as intended, the SVS provides a shared mental model that lets everyone in the organization — from the help desk analyst to the CIO — understand how their work contributes to value creation. In a 2040 world of distributed teams, AI copilots, and hybrid cloud infrastructure, this shared understanding is more valuable than ever.

### Required Reading

- AXELOS. (2019). *ITIL Foundation: ITIL 4 Edition*. TSO. Chapters 3–4: "The Service Value System" and "The Four Dimensions of Service Management."
- Hafsteinsson, E. (2038). *The Yggdrasil Model*. University of Yggdrasil Press. Chapter 4: "Mapping ITIL 4 to the Three Roots."

### Discussion Questions

1. The seven Guiding Principles seem obvious — "Focus on Value" is hardly controversial. Why, then, do organizations so consistently fail to apply them? What makes principles hard to operationalize?
2. The Service Value Chain is deliberately non-linear. In what situations might a non-linear model create confusion rather than clarity?
3. Which of the 34 ITIL 4 practices do you think will be most transformed by AI by 2050, and which will remain fundamentally human?

---

ᚦ **Lecture 3: DevOps — Culture, Automation, and the Breaking of Silos**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

DevOps is not a tool. It is not a job title. It is not a certification. DevOps is a cultural movement — an organizational philosophy that argues development and operations should not be separate tribes but a single, collaborative team sharing responsibility for the entire software lifecycle. This lecture traces the origins of DevOps from the 2008 Agile Infrastructure talk through the 2009 Velocity Conference "10+ Deploys per Day" presentation to the global movement it became, and examines the CALMS framework that defines its core principles in the 2040 landscape.

### Lecture Notes

The term "DevOps" was coined by Patrick Debois in 2009, but its intellectual roots go deeper. The Agile Manifesto (2001) had already argued for individuals and interactions over processes and tools, working software over comprehensive documentation. But Agile stopped at the operations boundary — developers would write "working software" and throw it over the wall to operations, who would then struggle to deploy, monitor, and maintain it in production. Andrew Clay Shafer's 2008 Agile Infrastructure talk — delivered to an audience of exactly one person (Debois himself) — planted the seed that infrastructure should also be Agile.

The breakthrough came at the 2009 Velocity Conference, where John Allspaw and Paul Hammond of Flickr described deploying code ten or more times per day using automated infrastructure, shared version control, and a culture of mutual respect between dev and ops. Debois, watching the livestream from Belgium, was so inspired that he organized the first DevOpsDays conference in Ghent later that year. The #DevOps hashtag was born, and the movement spread virally through the global IT community.

What makes DevOps different from previous improvement methodologies is its emphasis on culture over process. The CALMS framework — proposed by Jez Humble and refined by the community — captures the five pillars:

**Culture**: The foundation. DevOps culture values collaboration, shared responsibility, blameless postmortems, and psychological safety. When a production incident occurs, the question is not "who caused this?" but "what in our system allowed this to happen, and how do we prevent it?" Google's Project Aristotle (2015) demonstrated that psychological safety — the belief that you won't be punished for speaking up — is the single strongest predictor of team performance. DevOps culture operationalizes this finding.

**Automation**: The engine. Manual processes are slow, error-prone, and soul-destroying. DevOps practitioners automate everything that can be automated: builds, tests, deployments, infrastructure provisioning, monitoring, and even incident response. The Continuous Integration / Continuous Delivery (CI/CD) pipeline is the archetypal DevOps automation: code commit triggers automated build → automated test → automated deployment to staging → automated smoke tests → deployment to production, all without human intervention except the final approval gate (and in advanced organizations, not even that).

**Lean**: The philosophy. Derived from Toyota Production System principles adapted for software by Mary and Tom Poppendieck, Lean thinking emphasizes eliminating waste, amplifying learning, deciding as late as possible, delivering as fast as possible, empowering the team, building integrity in, and seeing the whole. In DevOps practice, Lean manifests as limiting work in progress (WIP), visualizing flow with Kanban boards, and ruthlessly eliminating activities that don't create value for the end user.

**Measurement**: The feedback loop. "You can't improve what you don't measure." DevOps organizations instrument everything: deployment frequency, lead time for changes, mean time to recovery (MTTR), change failure rate. The DORA metrics — four key indicators identified by the DevOps Research and Assessment team in their annual State of DevOps reports — have become the de facto standard for measuring DevOps maturity. Elite performers deploy on demand (multiple times per day), achieve lead times under one hour, recover from incidents in under one hour, and have change failure rates below 5%.

**Sharing**: The multiplier. DevOps knowledge is communal knowledge. Blameless postmortems are published internally (and sometimes externally). Runbooks are wiki pages, not personal notebooks. Monitoring dashboards are visible to everyone, not hidden in the NOC. When one team learns something, every team benefits. The "you build it, you run it" mantra — popularized by Amazon CTO Werner Vogels — means developers carry pagers and feel the pain of their own design decisions, creating a virtuous cycle of improved operability.

By 2040, DevOps has evolved beyond its original scope. AI-augmented DevOps (sometimes called "AIOps" or "DevOps 2.0") uses machine learning for anomaly detection, predictive scaling, and automated root cause analysis. GitOps — using Git as the single source of truth for declarative infrastructure — has become standard practice. Platform engineering has emerged as a specialization, with teams building internal developer platforms (IDPs) that provide self-service infrastructure while maintaining governance guardrails. But the core insight remains unchanged: technology problems are, at root, people problems. The best CI/CD pipeline in the world cannot compensate for a toxic culture.

### Required Reading

- Kim, G., Humble, J., Debois, P., & Willis, J. (2016). *The DevOps Handbook*. IT Revolution Press. Chapters 1–6.
- Forsgren, N., Humble, J., & Kim, G. (2018). *Accelerate: The Science of Lean Software and DevOps*. IT Revolution Press. Chapters 1–3.
- Google Cloud. (annual). *State of DevOps Report*. DORA research program.
- Hafsteinsson, E. (2038). *The Yggdrasil Model*. Chapter 5: "DevOps as Cultural Transformation."

### Discussion Questions

1. "You build it, you run it" sounds empowering — until a developer is woken up at 3 AM for the third time this week. What are the limits of shared responsibility, and how do organizations prevent burnout in DevOps cultures?
2. The CALMS framework prioritizes Culture over Automation. Why is this ordering significant, and what happens when organizations try to do DevOps by buying tools without changing culture?
3. By 2040, AI can write deployment scripts, detect anomalies, and even suggest fixes. Does this make the "Sharing" pillar more or less important?

---

ᚨ **Lecture 4: Continuous Integration, Continuous Delivery, and the Deployment Pipeline**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

If DevOps is a philosophy, the CI/CD pipeline is its physical manifestation — the assembly line that transforms code commits into production features. This lecture traces the evolution from manual deployments through Continuous Integration, Continuous Delivery, and Continuous Deployment, examining the technical architecture, quality gates, and organizational implications of each stage. By 2040, AI-augmented pipelines can predict deployment risk before code reaches production.

### Lecture Notes

The pre-CI world was one of "integration hell." Developers would work in isolation for weeks or months, then attempt a "big bang" merge that invariably resulted in conflicts, regressions, and multi-day debugging marathons. Grady Booch, in his 1991 book *Object-Oriented Design*, had already proposed the solution: integrate continuously, ideally multiple times per day. But it took the rise of distributed version control (Git, 2005) and automated build tools to make CI practical at scale.

**Continuous Integration** (CI) is the practice of automatically building and testing every code change as soon as it is committed to a shared repository. Martin Fowler's canonical definition requires: (1) maintain a single source repository, (2) automate the build, (3) make the build self-testing, (4) everyone commits to the mainline every day, (5) every commit triggers a build, (6) keep the build fast, (7) test in a clone of the production environment, (8) make it easy for anyone to get the latest executable, (9) everyone can see what's happening, (10) automate deployment. The CI server — Jenkins (2011), GitHub Actions (2019), GitLab CI, CircleCI — watches for commits, spins up build environments, runs the test suite, and reports results. A failing build is a stop-the-line event: the team's highest priority is getting back to green.

**Continuous Delivery** (CD) extends CI by ensuring that every change that passes automated testing is in a deployable state. The deployment to production is still a manual decision — someone presses the button — but the button always works. Achieving CD requires: comprehensive automated testing (unit, integration, acceptance, performance), infrastructure as code (so environments are reproducible), database migration automation, and feature flags (so incomplete features can be merged without being exposed). The deployment pipeline becomes a "walking skeleton" of the release process, exercised dozens of times per day.

**Continuous Deployment** goes the final step: every change that passes all automated gates is automatically deployed to production, with no human intervention. This is rare in practice — even elite performers often maintain a manual approval gate for regulatory, contractual, or risk-management reasons. But companies like Netflix (with its Spinnaker deployment platform) and Etsy (which famously deployed 50+ times per day in the early 2010s) have demonstrated that it is technically possible.

The 2040 CI/CD landscape adds layers that earlier generations could only dream of. **Predictive quality gates** use machine learning models trained on historical deployment outcomes to estimate the risk of each change before it reaches production — analyzing not just test results but code complexity, author experience, dependency changes, and even commit message sentiment. **Canary deployments with automated analysis** gradually shift traffic to new versions while monitoring error rates, latency, and business metrics, automatically rolling back if degradation is detected. **Chaos engineering** — pioneered by Netflix's Chaos Monkey — has evolved into continuous resilience validation, where the pipeline intentionally injects failures to verify that the system degrades gracefully.

The role of the human in the 2040 pipeline has shifted from operator to designer. Humans design the pipeline architecture, define the quality criteria, handle the exceptions the AI cannot resolve, and make the judgment calls about when to override automated decisions. The pipeline has become a collaborator, not a tool — a Silicon Colleague that handles the routine so the human can focus on the exceptional.

### Required Reading

- Humble, J., & Farley, D. (2010). *Continuous Delivery*. Addison-Wesley. Chapters 1–5.
- Fowler, M. (2006). "Continuous Integration." martinfowler.com.
- Kim, G., et al. (2016). *The DevOps Handbook*. Chapters 7–12 (The Technical Practices of Continuous Delivery).
- Hafsteinsson, E., & Chen, L. (2040). "Predictive Deployment Risk Assessment Using Multi-Modal Machine Learning." *Journal of AI-Augmented Operations*, 2(1), 45–67.

### Discussion Questions

1. Continuous Deployment sounds ideal — but what kinds of systems should NEVER be continuously deployed, and why?
2. Feature flags enable trunk-based development but create technical debt if not cleaned up. Design a governance process for managing feature flag lifecycle in a 2040 organization.
3. If the AI predictive quality gate says a deployment is "high risk" but the team lead believes it's safe, who decides? What principles should guide this conflict?

---

ᚱ **Lecture 5: Site Reliability Engineering — When Operations Becomes Engineering**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Site Reliability Engineering, born at Google in 2003 and codified for the world in 2016, represents a fundamental reframing of operations: not as a cost center to be minimized, but as an engineering discipline with its own principles, metrics, and intellectual challenges. This lecture introduces SRE's core concepts — Service Level Indicators (SLIs), Service Level Objectives (SLOs), error budgets, toil, and the 50% engineering time rule — and examines how SRE bridges the gap between unreliable systems and unrealistic expectations.

### Lecture Notes

The origin story of SRE is well-known in the industry. In 2003, Ben Treynor Sloss was asked to lead a team at Google responsible for keeping the company's production systems running. He hired software engineers, not traditional system administrators, and gave them a mandate: spend at most 50% of your time on operational work — "toil" — and at least 50% on engineering projects that reduce future toil. The name "Site Reliability Engineering" was chosen deliberately: these were engineers, their domain was site reliability, and their approach was engineering.

The intellectual core of SRE is the **error budget**. An error budget is the amount of unreliability a service is allowed to have, defined as 100% minus the Service Level Objective (SLO). If the SLO for a service is 99.9% availability over a 30-day window, the error budget is 0.1% — about 43 minutes of downtime per month. Here is the crucial insight: the error budget is not just a metric; it is a decision-making tool. When the error budget is unspent, the team can take risks — push new features, experiment with infrastructure changes, increase velocity. When the error budget is exhausted, all feature work stops until reliability is restored. This mechanism aligns the interests of developers (who want to ship features) and operators (who want stability) without requiring anyone to be the "bad guy."

**Service Level Indicators (SLIs)** are the carefully chosen metrics that represent a service's reliability from the user's perspective. Common SLIs include latency (how long does a request take?), availability (is the service responding?), error rate (what fraction of requests fail?), and throughput (how many requests per second?). The art of SRE lies in choosing SLIs that actually matter to users. A latency SLI measured at the load balancer may show 50ms while the end user experiences 3 seconds — because the real bottleneck is client-side rendering. Good SLIs are measured as close to the user experience as possible.

**Service Level Objectives (SLOs)** are the target values for SLIs. "99.9% of requests will complete in under 200ms over a 30-day rolling window." SLOs should be aspirational but achievable — setting them too high (99.999%) creates impossible pressure; setting them too low (95%) means users are unhappy. Google's rule of thumb: if users wouldn't notice the difference between your SLO and a slightly better number, your SLO is too high. The Chubby lock service at Google famously runs at "four nines" (99.99%) availability — not five, because the cost of the fifth nine would exceed the value it creates.

**Toil** is the enemy. Toil is operational work that is manual, repetitive, automatable, tactical, devoid of enduring value, and scales linearly with service growth. Responding to a page about a full disk when the same alert fires weekly? Toil. Manually running a script that could be cron? Toil. Configuring a new server by hand when it should be infrastructure-as-code? Toil. The SRE discipline requires identifying, measuring, and systematically eliminating toil through engineering. This is the "50% rule" — if an SRE spends more than half their time on toil, something is broken.

By 2040, the SRE practice has evolved significantly. **AI-assisted incident response** — systems that automatically correlate alerts, suggest diagnoses, and in some cases execute remediation — has reduced mean time to recovery for common incident patterns. **Predictive reliability engineering** uses machine learning models to forecast when error budgets will be exhausted and proactively recommends architectural changes. **Autonomous SRE agents** — the subject of ongoing research at this university — can independently manage routine operational tasks while escalating only genuine anomalies to human SREs. But the core SRE principles remain unchanged: define what "reliable" means in measurable terms, give teams the authority to balance reliability against other priorities, and invest engineering effort in reducing future operational burden.

### Required Reading

- Beyer, B., Jones, C., Petoff, J., & Murphy, N. R. (2016). *Site Reliability Engineering*. O'Reilly Media. Chapters 2–6.
- Beyer, B., Murphy, N. R., Rensin, D. K., Kawahara, K., & Thorne, S. (2018). *The Site Reliability Workbook*. O'Reilly Media. Chapters 1–3 (SLOs and Error Budgets).
- Treynor Sloss, B. (2017). "Keys to SRE." Keynote address, SREcon17.
- Hafsteinsson, E. (2039). "Autonomous Incident Response: The Mímir System at the University of Yggdrasil." *Proceedings of the 2040 Conference on AI-Augmented Operations*.

### Discussion Questions

1. Error budgets are elegant in theory but difficult in practice. What happens when a team exhausts its error budget on day 3 of a 30-day window? What should the remediation policy be?
2. The 50% toil ceiling assumes that reducing toil is always the right investment. Are there situations where tolerating toil is actually the correct business decision?
3. An autonomous SRE agent detects a memory leak and decides to restart a production service at 2 PM on a business day. Was this the right decision? What factors should the agent consider before acting?

---

ᚲ **Lecture 6: Incident Management — From Firefighting to Learning**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Incidents are inevitable. Every complex system will fail — the question is not "if" but "how gracefully." This lecture examines the full incident lifecycle: detection, response, resolution, and the critical post-incident learning process. Drawing from ITIL's incident management practice, DevOps blameless postmortem culture, and SRE's quantitative approach to incident analysis, we build a comprehensive framework for turning failures into organizational learning.

### Lecture Notes

**Detection** is the first and most critical phase. An incident that is never detected is an incident that never ends. The 2040 monitoring landscape is radically different from the Nagios-centric world of 2010. Modern observability platforms — built on the "three pillars" of metrics (Prometheus, VictoriaMetrics), logs (Loki, Elasticsearch), and traces (Jaeger, Tempo) — provide a unified view of system behavior. AI-augmented anomaly detection can identify subtle deviations from baseline behavior that would be invisible to threshold-based alerting. But detection remains a human-centric challenge: the best monitoring system in the world generates useless noise if it alerts on symptoms rather than causes, or if alert thresholds are set so low that everyone has learned to ignore them.

**Response** follows a structured incident command protocol. ITIL defines clear roles: Incident Manager (coordinates the response), Technical Lead (diagnoses and fixes), Communications Lead (keeps stakeholders informed). Large incidents activate a formal Incident Command System (ICS), adapted from emergency services protocols — a structure that has proven effective from Google to small startups. The key principle: separate the decision-making from the doing. The Incident Manager runs the process, sets priorities, and manages time; the engineers focus on diagnosis and remediation. Without this separation, engineers simultaneously try to fix the problem AND answer Slack messages from anxious executives — and do neither well.

The concept of **"swarming"** has emerged as a best practice: when an incident is declared, all available relevant expertise converges on the problem simultaneously, rather than escalating serially through tiers of support. This reduces mean time to resolution dramatically, but requires a cultural commitment — swarming means dropping other work, and organizations must genuinely prioritize incident resolution over feature development for swarming to work.

**Resolution** follows a systematic diagnostic approach. The SRE methodology emphasizes: (1) Mitigate first, diagnose later. Restore service, then understand root cause. (2) Use the scientific method: form a hypothesis, test it, observe results, iterate. (3) Document everything in a shared incident channel — the timeline is the most valuable artifact for the postmortem. (4) Know when to escalate: if the diagnosis is taking too long, bring in fresh eyes. By 2040, AI copilots assist with diagnosis by correlating symptoms across distributed systems, suggesting likely causes based on historical incident databases, and even proposing remediation commands for human approval.

**Post-Incident Learning** is where organizations get their return on investment from incidents. ITIL's Problem Management practice distinguishes between incident (restore service) and problem (find root cause). DevOps culture introduced the **blameless postmortem** — a structured document that answers: What happened? What was the impact? How was it detected? How was it resolved? What was the root cause? What contributed? What went well? What went poorly? Where did we get lucky? The blamelessness is critical: if postmortems become blame assignment exercises, people stop reporting incidents, and the organization loses its ability to learn.

SRE adds quantitative rigor: every significant incident should result in at least one **action item** — a specific, tracked, time-bound improvement that reduces the probability or impact of similar incidents. Action items are tracked like bugs; if they stay open too long, they become incidents in their own right. The SRE "Wheel of Misfortune" exercise — where teams role-play incident response scenarios — has become a standard training tool for building incident response muscle memory.

The 2040 evolution includes **continuous learning systems**: every incident feeds into an organizational knowledge graph that connects symptoms, causes, fixes, and context. When a similar pattern emerges, the system proactively suggests the fix before the incident is even declared. But the human remains essential — for the judgment to say "this is different," for the creativity to find novel solutions, and for the empathy to communicate with affected users.

### Required Reading

- ITIL 4 Practice Guide: Incident Management and Problem Management. AXELOS.
- Beyer, B., et al. (2016). *Site Reliability Engineering*. Chapter 11: "On-Call and Incident Response." Chapters 14–15: "Managing Incidents" and "Postmortem Culture."
- Allspaw, J. (2013). "Blameless PostMortems and a Just Culture." Etsy Engineering Blog.
- Dekker, S. (2016). *Just Culture: Restoring Trust and Accountability in Your Organization*. CRC Press. Chapters 1–3.

### Discussion Questions

1. "Mitigate first, diagnose later" can lead to fixes that mask symptoms without addressing root causes. How do you prevent symptom-masking from accumulating into systemic fragility?
2. Blameless culture sounds humane — but what about the engineer who repeatedly makes the same careless error? At what point does blameless become accountability-free?
3. Design an incident command structure for a fully remote, globally distributed 2040 team. What changes when no one is in the same room?

---

ᚷ **Lecture 7: Change Management in the Age of Continuous Delivery**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Change management is the most contested practice in ITSM. Traditional ITIL change management — with its Change Advisory Boards (CABs), forward schedules of change, and multi-level approval hierarchies — seems antithetical to DevOps values of speed and autonomy. Yet unmanaged change is the leading cause of production incidents. This lecture reconciles the apparent contradiction, presenting a 2040 model of risk-based, automated change governance that protects stability without stifling innovation.

### Lecture Notes

The conflict is real. In a classic ITIL shop, deploying a change to production might require: a Request for Change (RFC) document, a CAB meeting (held weekly), approval from the Change Manager, approval from the affected service owner, and a scheduled change window (typically Sunday 2–4 AM). The process could take two weeks. Meanwhile, an elite DevOps organization deploys hundreds of times per day with no human approvals at all.

How do we reconcile these? The answer lies in recognizing that ITIL's change management was designed for a world of manual, high-risk, infrequent changes. The CAB made sense when changes were rare and each one was handcrafted. DevOps changed the game by making changes frequent, small, and automated — which paradoxically made them safer. A deployment that changes 10 lines of code behind a feature flag, automatically tested, and canary-deployed to 1% of users is fundamentally less risky than a quarterly release that changes 10,000 lines with no feature flags and manual testing.

ITIL 4 recognized this shift by renaming the practice "Change Enablement" — emphasizing that the goal is to enable valuable changes, not to block all changes. The modern approach is **risk-based change governance**: standard changes (low risk, pre-approved, following documented procedures) require no approval; normal changes (some risk, some impact) require peer review; emergency changes (must happen NOW) follow an expedited process with retrospective review. The CAB is replaced by automated change risk assessment, where the CI/CD pipeline itself evaluates risk based on test coverage, change size, dependency changes, historical failure patterns, and the current error budget status.

By 2040, **AI-augmented change risk assessment** is standard practice. Before a deployment reaches production, a machine learning model — trained on the organization's deployment history — estimates the probability of incident. If the risk is low and the error budget is unspent, the deployment proceeds automatically. If the risk is elevated, the deployment is routed to a human for review. If the risk is high, the deployment is blocked pending additional testing or architectural changes. This system achieves what the CAB always wanted — protection against harmful changes — without the CAB's primary flaw: treating all changes as equally dangerous.

The **Change-Problem-Incident triad** remains fundamental. Every incident should be traced to a change (what changed that caused this?), and every significant problem should result in a change (what do we change to fix this?). The integration of change records, incident timelines, and problem investigations into a unified data model enables this traceability at scale. In the 2040 Yggdrasil ITSM Platform (developed at this university), the knowledge graph connects all three, enabling cross-organizational learning and predictive risk assessment.

The human role in change management has shifted from approval gatekeeper to risk designer. The modern change manager defines risk policies, calibrates automated assessment models, handles exceptions, and ensures that the change process itself is continuously improving. They are not the person who says "no" — they are the person who designs the system that says "yes, but safely."

### Required Reading

- ITIL 4 Practice Guide: Change Enablement. AXELOS.
- Kim, G., et al. (2016). *The DevOps Handbook*. Chapter 17: "Integrate Security into the Delivery Pipeline."
- Hafsteinsson, E., & Patel, A. (2040). "Machine Learning for Automated Change Risk Assessment in Continuous Delivery Pipelines." *ACM Transactions on Autonomous Systems*, 15(3), 1–28.

### Discussion Questions

1. If an automated change risk system blocks a deployment, but the engineering team believes the risk model is wrong, who decides? What is the escalation path?
2. Emergency changes bypass normal governance. How do you prevent the "emergency" classification from being abused to circumvent process?
3. In a fully automated deployment pipeline, what is the role of the human Change Manager? Is this role becoming obsolete, or more important than ever?

---

ᚹ **Lecture 8: Service Level Management — The Contract Between IT and the Business**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Service Level Agreements (SLAs) are the formal contracts that define the relationship between IT service providers and their customers. But badly written SLAs are worse than no SLAs at all — they create perverse incentives, encourage gaming of metrics, and damage the provider-customer relationship. This lecture teaches students how to design SLAs, SLOs, and SLIs that align IT performance with business outcomes, and how to use the service catalog as a communication tool rather than a bureaucratic artifact.

### Lecture Notes

The hierarchy is: **SLI** (Service Level Indicator — what you measure) → **SLO** (Service Level Objective — the target value for the SLI) → **SLA** (Service Level Agreement — the contract that specifies consequences for missing SLOs). The distinction matters because many organizations conflate them. An SLA is not just a target; it is a promise with consequences. If the SLA says "99.9% uptime" and the service achieves 99.8%, there may be financial penalties, service credits, or (in extreme cases) contract termination.

The **watermelon SLA** is the classic anti-pattern: green on the outside (all SLAs met), red on the inside (users are furious). This happens when SLIs measure things that are easy to measure but don't reflect user experience. "The server was up" (green) but "the database was slow and users couldn't complete transactions" (red). Avoiding the watermelon SLA requires measuring what matters: user-facing metrics, not infrastructure metrics. Instead of "CPU utilization < 80%," measure "95th percentile page load time < 2 seconds." Instead of "server uptime 99.9%," measure "successful checkout completion rate > 99.5%."

The **service catalog** is the menu of what IT offers. A well-designed service catalog answers: What services do we provide? Who are they for? What do they cost? What are the service levels? How do I request them? The service catalog is both an operational tool (routing requests to the right fulfillment process) and a communication tool (helping customers understand what IT can do for them). In the 2040 model, the service catalog is dynamic and personalized — an AI-powered interface that presents relevant services based on the requester's role, history, and current context, much like a modern streaming service recommends content.

**Service request management** is the operational complement to service level management. While incident management deals with unplanned interruptions, service request management handles planned, pre-defined requests: "I need access to the analytics database," "Please provision a new development environment," "I need a software license." These requests follow defined workflows with clear approval steps and fulfillment SLAs. The 2040 evolution includes self-service portals where AI agents fulfill common requests autonomously — "spin up a test environment matching production config" becomes a natural language command that triggers infrastructure-as-code provisioning, access control configuration, and notification to the requester, all within minutes.

The **business relationship manager** role has evolved in 2040 to become the bridge between IT's technical service catalog and the organization's strategic goals. Rather than simply translating business requirements into IT specifications, the modern BRM uses service analytics to proactively suggest IT-enabled business improvements. "Based on usage patterns, your team would benefit from our new AI-augmented data pipeline service," the BRM might say, backed by data showing that the team's manual ETL processes are consuming 40% of their engineering time.

### Required Reading

- ITIL 4 Practice Guide: Service Level Management and Service Catalog Management. AXELOS.
- Beyer, B., et al. (2016). *Site Reliability Engineering*. Chapters 4–6 (Service Level Objectives).
- Sturm, R., & Morris, W. (2015). *Foundations of Service Level Management*. Sams Publishing. Chapters 1–4.
- Hafsteinsson, E. (2040). "Dynamic Service Catalogs: AI-Driven Service Discovery in the Enterprise." *University of Yggdrasil Technical Report* UY-IT-2040-07.

### Discussion Questions

1. A customer demands a 99.999% availability SLA for a service that currently runs at 99.9%. The cost to upgrade would be $2 million. How do you communicate the cost-quality tradeoff to a non-technical stakeholder?
2. Service catalogs often become outdated graveyards of abandoned services. Design a governance process that ensures the catalog stays current without creating excessive administrative overhead.
3. "The user is always right" is not true in ITSM — sometimes user expectations are unreasonable. How does the service level management practice distinguish between legitimate user needs and unreasonable demands?

---

ᚺ **Lecture 9: Problem Management and Root Cause Analysis**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Incident management restores service; problem management prevents recurrence. These are distinct disciplines with different methodologies, timeframes, and success criteria. This lecture explores the full problem management lifecycle — identification, investigation, root cause analysis, known error documentation, and permanent resolution — with emphasis on practical RCA techniques, the psychology of investigation, and the 2040 tools that augment human analysis with AI pattern recognition.

### Lecture Notes

ITIL draws a bright line between **incident** and **problem**. An incident is "an unplanned interruption to a service or reduction in the quality of a service" — the thing you respond to at 3 AM. A problem is "a cause, or potential cause, of one or more incidents" — the underlying condition that makes incidents possible. Incident management asks "how do we restore service?" Problem management asks "why did this happen, and how do we ensure it never happens again?"

The distinction creates a healthy separation of concerns. During an incident, the pressure to restore service is immense — there is no time for deep investigation. The incident team mitigates and moves on. The problem management team, operating with less time pressure, conducts the thorough investigation that leads to permanent fixes. This separation also prevents the natural human tendency to stop investigating once the immediate pain is relieved.

**Root Cause Analysis (RCA)** is the core methodology of problem management. Several techniques have proven effective:

**Five Whys**: Developed by Sakichi Toyoda and popularized by Toyota, the technique is deceptively simple — ask "why?" five times, each answer becoming the basis for the next question. "The website was down." Why? "The database connection pool was exhausted." Why? "A new feature opened connections without closing them." Why? "The code review didn't catch the resource leak." Why? "The code review checklist didn't include resource management." Why? "We never defined resource management as a code review criterion." The fifth "why" reveals the systemic issue, not just the proximate cause.

**Fishbone (Ishikawa) Diagrams**: Named for Kaoru Ishikawa, this visual tool organizes potential causes into categories — typically Methods, Machines, Materials, People, Measurement, and Environment. By systematically exploring each category, the investigator avoids the cognitive bias of fixating on the first plausible cause.

**Fault Tree Analysis (FTA)**: A top-down, deductive approach that starts with the failure event and works backward through logical gates (AND, OR) to identify all possible root cause combinations. Originally developed for aerospace and nuclear safety, FTA has been adapted for IT systems where complex interactions between components can create failure modes that no single component exhibits.

**Timeline Analysis**: Simply reconstructing the exact sequence of events — what changed, in what order, at what time — often reveals the cause without any formal methodology. The discipline of creating an accurate timeline, cross-referenced across monitoring systems, change logs, and human recollections, is itself a powerful investigative technique.

By 2040, **AI-augmented problem management** has transformed the field. Modern systems automatically correlate incidents across thousands of services, identify common root causes, and suggest known fixes from the organizational knowledge base. The Yggdrasil Mímir system (2039) uses graph neural networks to model the dependency web of services and predictively identify "problem hotspots" — components whose failure would cascade through the system — before any incident occurs. But AI cannot replace human investigative thinking: the ability to ask "what are we not seeing?", to challenge assumptions, to recognize when the data is telling a misleading story. Problem management remains, at its core, a detective's discipline.

**Known Error Database (KEDB)** is the institutional memory of problem management. When a problem's root cause is identified and a workaround exists (even if the permanent fix is not yet implemented), it becomes a Known Error. The KEDB allows incident responders to quickly identify recurring issues and apply documented workarounds, dramatically reducing mean time to resolution. A well-maintained KEDB is one of the highest-ROI investments in ITSM — but a neglected KEDB filled with stale entries is worse than useless, because it wastes time and erodes trust.

### Required Reading

- ITIL 4 Practice Guide: Problem Management. AXELOS.
- Dekker, S. (2014). *The Field Guide to Understanding 'Human Error'*. Ashgate. Chapters 1–4.
- Leveson, N. G. (2011). *Engineering a Safer World: Systems Thinking Applied to Safety*. MIT Press. Chapters 1–3 (STAMP/STPA methodology).
- Hafsteinsson, E., et al. (2039). "The Mímir System: Graph-Based Predictive Problem Identification in Distributed Service Architectures." *Proceedings of the 2039 Symposium on Autonomous Operations*.

### Discussion Questions

1. "Five Whys" can lead to different root causes depending on who asks the questions. How do you validate that you've reached the actual root cause, not just a plausible narrative?
2. Problem management requires investment with no immediate return — you're fixing something that might break again, not something that's broken now. How do you justify this investment to a cost-focused executive?
3. When an AI system identifies a "likely root cause" that contradicts the human investigation team's theory, how should the conflict be resolved?

---

ᚾ **Lecture 10: The Service Desk — Humanity at the Interface**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

The service desk is the human face of IT — the point where technology meets the people who depend on it. In an age of AI chatbots, self-service portals, and automated remediation, some have predicted the extinction of the human service desk. This lecture argues the opposite: as technology becomes more complex and autonomous, the human service desk becomes more essential, not less. We examine service desk structures, ticket management, customer experience design, and the 2040 model of the AI-augmented service desk analyst.

### Lecture Notes

The service desk has evolved through several eras. In the mainframe era, the "help desk" was often a single person in the computer room. In the client-server era, it became a call center. In the ITSM era, it became a formal function with defined processes, SLAs, and tiered escalation. In the DevOps era, some organizations attempted to eliminate it entirely — "if developers run what they build, why do we need a service desk?" This was a mistake. Developers running production services need to focus on engineering; they cannot also handle password resets, laptop configurations, and "how do I print?" inquiries. The service desk absorbs the high-volume, low-complexity work that would otherwise fragment engineering attention.

The **tiered support model** remains the standard architecture. **Tier 0** is self-service and automation — chatbots, knowledge bases, password reset portals. **Tier 1** is the service desk — generalist analysts who handle common issues, gather information, and escalate when necessary. **Tier 2** is technical specialists — network engineers, database administrators, application support. **Tier 3** is development and engineering — the people who wrote the software. Each tier handles a smaller volume of more complex issues. The "swarming" model challenges this hierarchy by bringing Tier 2/3 into incident response immediately rather than waiting for escalation, but the tiers remain useful for non-incident request fulfillment.

**Ticket quality** is the unsung hero of service desk operations. A good ticket contains: a clear description of the issue, the impact on the user, what the user has already tried, relevant system information (automatically collected where possible), and a unique identifier that enables tracking. Bad tickets — "email not working" with no context — waste enormous time in clarification loops. The 2040 solution includes AI-assisted ticket creation: the user describes their problem in natural language, and the system automatically enriches the ticket with diagnostic data, suggests categorization, and proposes initial troubleshooting steps before a human analyst even looks at it.

**Customer experience (CX)** in IT is often neglected. IT organizations measure mean time to resolution (MTTR) and first-contact resolution rate, but rarely measure how users *feel* about their interactions. The IT Customer Experience (ITCX) framework, developed at the University of Yggdrasil in 2038, adds three dimensions: **Effort** (how hard did the user have to work to get help?), **Empathy** (did the user feel heard and respected?), and **Empowerment** (did the interaction leave the user better equipped to handle similar issues in the future?). Organizations that score high on ITCX see higher IT satisfaction, better adoption of new services, and — counter-intuitively — lower ticket volumes, because empowered users resolve more issues themselves.

The 2040 service desk analyst is a knowledge worker, not a script follower. AI handles routine inquiries; the human handles situations where empathy, judgment, and creative problem-solving are required. The analyst's tools include AI-suggested solutions (ranked by relevance and success rate), real-time translation (supporting a global user base in their native languages), and sentiment analysis that alerts the analyst when a user's frustration is escalating. The skill set has shifted from "knowing the answers" to "knowing how to find answers, how to communicate, and how to advocate for the user within the IT organization."

### Required Reading

- ITIL 4 Practice Guide: Service Desk. AXELOS.
- Knapp, D. (2014). *A Guide to Service Desk Concepts*. Cengage Learning. Chapters 1–5.
- Goodman, J. (2019). *Strategic Customer Service*. AMACOM. Chapters 1–4 (The ROI of Customer Service).
- University of Yggdrasil ITCX Research Group. (2038). "The IT Customer Experience Framework: Measuring What Matters in IT Support." *Journal of IT Service Management*, 12(2), 89–112.

### Discussion Questions

1. Many organizations measure service desk performance by "tickets closed per day." What perverse incentives does this metric create, and what should replace it?
2. A user calls the service desk furious about a recurring issue. The technical fix is straightforward, but the user is beyond caring about the fix — they want to be heard. How does the analyst balance technical resolution with emotional resolution?
3. As AI handles more Tier 0/1 work, what happens to the career path of service desk analysts? How do we ensure the service desk remains a viable entry point to IT careers?

---

ᛁ **Lecture 11: IT Asset Management and Configuration Management — Knowing What You Have**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

You cannot manage what you cannot see. IT Asset Management (ITAM) and Configuration Management (CM) provide the foundational visibility that all other ITSM practices depend upon. Without an accurate Configuration Management Database (CMDB), incident diagnosis is guesswork, change risk assessment is unreliable, and capacity planning is fantasy. This lecture covers the principles, tools, and 2040 innovations in IT asset lifecycle management, CMDB design, and the integration of discovery automation.

### Lecture Notes

**IT Asset Management** answers "what do we own, where is it, what is it worth, and what is its lifecycle state?" ITAM covers hardware (servers, laptops, network devices), software (licenses, subscriptions, cloud resources), and increasingly, digital assets (SSL certificates, domain names, API keys). The IT asset lifecycle flows through: Request → Procure → Deploy → Maintain → Retire/Dispose. Each stage has financial, security, and compliance implications. A server that was decommissioned but never removed from the asset register creates phantom costs in depreciation calculations. A software license that was purchased but never deployed represents wasted budget.

**Software Asset Management (SAM)** deserves special attention. In the 2040 landscape of SaaS subscriptions, cloud marketplace purchases, and AI model API consumption, software costs have become the dominant component of IT spending. Organizations routinely discover they are paying for hundreds of unused SaaS seats, expired subscriptions that auto-renewed, and cloud resources that were provisioned for a project and forgotten. The SAM discipline combines financial governance (optimizing spend) with compliance management (ensuring license terms are met) and security (identifying unauthorized "shadow IT" applications).

**Configuration Management** answers a different question: "what are the components of our IT services, how are they configured, and how do they relate to each other?" A Configuration Item (CI) is any component that needs to be managed to deliver an IT service — a server, a database instance, a network switch, a software package, a documentation set. The Configuration Management Database (CMDB) stores CIs and their relationships. If a server goes down, the CMDB should tell you: which applications run on it, which databases it connects to, which network segments it serves, which business services depend on it, and which support team is responsible for it.

The **CMDB has a troubled history**. Many organizations have attempted to build the "perfect CMDB" — a complete, always-accurate model of their entire IT estate — and failed expensively. The failure mode is always the same: manual data entry cannot keep up with the rate of change in modern IT environments. Servers are provisioned and decommissioned by the minute; containers spin up and die in seconds. A manually maintained CMDB is out of date before the first entry is saved.

The solution is **automated discovery**. Modern CMDBs use agents, APIs, and network scanning to automatically discover CIs and their relationships. Cloud providers expose APIs that enumerate every resource. Container orchestrators (Kubernetes) maintain their own state database. Infrastructure as Code (Terraform, Pulumi) defines desired state declaratively. The 2040 CMDB is not a database you populate — it is a view you generate from multiple sources of truth, continuously reconciled and validated.

**Federated CMDB** architecture, proposed by Hafsteinsson (2039), takes this further: instead of a single monolithic database, each domain (network, compute, applications, cloud) maintains its own configuration store, and a federation layer provides a unified query interface. This mirrors the microservices philosophy — each team owns its own data, but cross-domain visibility is preserved through standardized APIs. The Yggdrasil implementation, code-named "HuginnStack," uses a graph database (Neo4j) at the federation layer, enabling complex dependency queries that a relational model would struggle with.

The **Configuration Baseline** concept is the bridge between ITAM and CM. A baseline is a snapshot of configuration state at a known-good point in time — "the production database cluster as it was configured on January 15, after the security patch." Baselines enable drift detection: any deviation from the baseline is flagged for investigation. In the 2040 model, baselines are continuously validated by automated compliance scanners, and unauthorized changes trigger automatic remediation or (for high-risk changes) immediate human review.

### Required Reading

- ITIL 4 Practice Guide: IT Asset Management and Service Configuration Management. AXELOS.
- O'Reilly, T., & Loukides, M. (2020). "What Is Infrastructure as Code?" O'Reilly Media.
- Hafsteinsson, E. (2039). "Federated Configuration Management for Cloud-Native Enterprises." *IEEE Transactions on Cloud Computing*, 7(4), 892–905.

### Discussion Questions

1. Shadow IT — services procured without IT approval — is simultaneously a security nightmare and a driver of innovation. How should the ITAM practice balance control with empowerment?
2. A CMDB that claims 100% accuracy is almost certainly wrong. What metadata should accompany every CI to help consumers assess the reliability of the data?
3. If Infrastructure as Code defines desired state declaratively, what happens if the actual state diverges? Who is responsible for reconciling the drift?

---

ᛃ **Lecture 12: The 2040 Horizon — AI-Augmented ITSM and the Autonomous Enterprise**

**Course:** IT207 — IT Service Management (ITIL, DevOps, SRE)
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

This final lecture looks forward. What does IT service management become when AI systems can detect incidents, diagnose root causes, execute changes, and communicate with users — all without human intervention? Is the autonomous enterprise a utopia of frictionless IT or a dystopia of algorithmic bureaucracy? Drawing together threads from the entire course, we explore the ethical, organizational, and technical dimensions of AI-augmented ITSM, and ask what it means to be a human ITSM professional in a world where machines do more of the work.

### Lecture Notes

The trajectory is clear. In 2010, incident detection required a human watching a dashboard. In 2020, anomaly detection algorithms could flag unusual patterns automatically. In 2030, AI copilots began suggesting diagnoses during incidents. In 2040, the Mímir system at this university can detect, diagnose, and remediate approximately 40% of common incidents without human intervention — and that percentage grows every year. The question is not whether AI will transform ITSM, but how we choose to integrate it.

Three levels of AI integration have emerged: **AI-assisted** (the human does the work, AI suggests), **AI-augmented** (AI and human collaborate, each doing what they do best), and **AI-autonomous** (AI handles the work independently within defined guardrails). Most 2040 organizations operate at the AI-augmented level for incident response and change risk assessment, while maintaining human oversight for strategic decisions, complex diagnoses, and stakeholder communication. Fully autonomous operations remain limited to low-risk, well-understood domains.

The **ethics of autonomous ITSM** present novel challenges. If an AI system autonomously rolls back a deployment that was causing performance degradation, and that rollback causes data loss, who is accountable? The engineer who configured the AI? The vendor who built it? The manager who approved its deployment? The AI itself? The emerging framework of **algorithmic accountability** — developed through collaborations between this university's IT and Philosophy departments — proposes a chain of responsibility: humans design the system, humans set its operational boundaries, humans monitor its outcomes, and therefore humans remain accountable for its actions. The AI is a tool, not a moral agent.

**The future of the ITSM profession** is not obsolescence but elevation. As routine operational work is automated, the human ITSM professional focuses on higher-order activities: designing service experiences, negotiating stakeholder priorities, managing organizational change, ensuring ethical AI governance, and building the trust relationships that technology cannot replace. The help desk analyst becomes a customer experience designer. The change manager becomes a risk governance architect. The problem manager becomes a systems thinker who understands not just technical failure modes but organizational, cognitive, and cultural ones.

The **Norse framing** that has guided this course — ITIL as the roots, DevOps as the trunk, SRE as the canopy — suggests that the tree continues to grow. What is the fourth root? This course proposes that the fourth root is **Wisdom** — the meta-discipline of knowing when to apply which framework, when to automate and when to keep human, when to standardize and when to allow variation, when to measure and when to trust intuition. Wisdom is what remains when all the frameworks have been learned and all the tools have been mastered. It is what the Norn brings to the Well of Urðr: not just knowledge of what has been, but judgment about what should be.

The University of Yggdrasil's ITSM program prepares students not to be operators of a dying craft but architects of an emerging one. The services you will manage in your careers — AI-driven healthcare platforms, autonomous transportation networks, neural interface systems — will demand a depth of service thinking that no AI can replicate. The frameworks you have learned in this course — ITIL's process rigor, DevOps's collaborative culture, SRE's engineering discipline — are not end states. They are the roots from which your own professional wisdom will grow.

May your services be reliable, your incidents be few, and your postmortems be blameless. The Well of Urðr awaits your contributions.

### Required Reading

- Hafsteinsson, E. (2040). *The Fourth Root: Wisdom in AI-Augmented IT Service Management*. University of Yggdrasil Press. Full text.
- Bostrom, N. (2014). *Superintelligence: Paths, Dangers, Strategies*. Oxford University Press. Chapters 8–10 (revisited for 2040 context).
- University of Yggdrasil Ethics Board. (2039). "Algorithmic Accountability in Autonomous IT Operations." UY-ETHICS-2039-04.
- Russell, S. (2019). *Human Compatible: Artificial Intelligence and the Problem of Control*. Viking. Chapters 7–9.

### Discussion Questions

1. If an AI system achieves 99.9% accuracy in incident diagnosis — better than the average human — should we still require human review of its decisions? What principle is at stake?
2. The "fourth root" of Wisdom is deliberately vague. Attempt to operationalize it: what specific skills, knowledge, and experiences constitute ITSM wisdom?
3. In 2040, a student graduating from this program will have a 40+ year career ahead of them. What will ITSM look like in 2080? What should you learn now to remain relevant then?

---

## Final Examination Preparation

The final examination for IT207 consists of two components:

### Part A: Written Examination (60%)

Choose **four** of the following eight essay questions. Each essay should be 800–1200 words, demonstrating mastery of ITSM concepts, the ability to synthesize across frameworks, and critical thinking about the 2040 landscape.

1. Compare and contrast the approaches of ITIL 4, DevOps, and SRE to managing production changes. Under what circumstances would each approach be most appropriate, and how can they be integrated in a single organization?
2. The error budget is often described as SRE's most important innovation. Explain the error budget concept, how it bridges the conflict between development velocity and operational stability, and analyze its limitations — when does the error budget framework fail?
3. "Blameless culture is a necessary condition for organizational learning, but it is not sufficient." Discuss this claim, drawing on both theoretical frameworks (Just Culture, psychological safety) and practical examples from the ITSM literature.
4. IT Asset Management and Configuration Management are often treated as separate practices, but they deeply interrelate. Propose an integrated ITAM/CM operating model for a 2040 enterprise, addressing discovery automation, data quality, and the role of AI.
5. The service desk has been declared "dead" multiple times — first with self-service portals, then with AI chatbots. Argue either for or against the proposition that the human service desk will be obsolete by 2050. Support your argument with evidence.
6. A large enterprise is transitioning from a traditional, CAB-based change management process to a risk-based, AI-augmented automated change governance model. Describe the implementation roadmap, identifying the technical, cultural, and organizational challenges at each stage.
7. "Problem management is the most underinvested practice in ITSM because its benefits are invisible — you can't count the incidents that didn't happen." Evaluate this claim and propose metrics that would make the value of problem management visible to executive leadership.
8. Design a service level agreement for a critical 2040 service (your choice: autonomous vehicle coordination platform, neural interface health monitor, or global financial settlement system). Specify SLIs, SLOs, measurement methodology, and consequences for breach. Justify your design choices.

### Part B: Practical Case Study (40%)

**Scenario:** You are the newly appointed ITSM Director at Midgard Financial Services, a 5,000-employee organization that has grown through acquisition. The IT estate includes three legacy data centers, two public cloud platforms (AWS and Azure), approximately 800 applications (many redundant across acquired companies), and an IT team of 200 spread across five offices in three time zones. The CEO has mandated "world-class IT service management within 18 months." Current state: no formal incident management process, changes are made ad-hoc without approvals, there is no CMDB, the "service desk" is a shared email inbox, and SLAs exist only in procurement contracts (and are never measured).

**Deliverables:**
1. **Current State Assessment** (500–750 words): Analyze Midgard's ITSM maturity using the ITIL 4 Service Value System as your framework. Identify the five most critical gaps.
2. **Target State Design** (1000–1500 words): Describe your target ITSM operating model. Specify which ITIL 4 practices you would prioritize, how DevOps and SRE principles would be integrated, and what metrics would define success.
3. **18-Month Roadmap** (750–1000 words): Present a phased implementation plan with specific milestones, resource requirements, and risk mitigation strategies. Address the human/cultural dimension — how will you bring 200 IT staff on the journey?
4. **AI Integration Strategy** (500–750 words): Identify three areas where AI augmentation would provide the highest return on investment within the 18-month window. For each, describe the specific capability, implementation approach, and expected outcomes.

---

*This course was woven at the University of Yggdrasil, 2040, by the Department of Information Technology. The frameworks, practices, and perspectives presented here are living knowledge — continuously improved through the contributions of students, faculty, and the global ITSM community. Skál!*
