# IT405: Capstone Project I — Infrastructure Design
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4
**Description:** The first semester of the two-semester capstone sequence. Students propose, design, and begin implementation of a substantial infrastructure project demonstrating mastery of the IT program's core competencies. Emphasis on requirements analysis, architecture design, project planning, and professional practice.

**Prerequisites:** Senior standing, completion of all Year 1-3 IT core courses

**Instructor:** Prof. Björn Hǫggvason, Department of Information Technology, with individual faculty advisors

**Course Philosophy:** The capstone is where theory meets practice. After three years of coursework, students demonstrate their ability to conceive, design, and build a system that solves a real problem. This is not an academic exercise — it is professional preparation. The capstone should be something you would proudly show a future employer.

---

## Lectures

---

### Lecture 1: The Capstone Vision — What Makes a Great Project

**Course:** IT405 — Capstone Project I — Infrastructure Design
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

What distinguishes a great capstone from a mediocre one? This lecture establishes criteria: technical depth, real-world relevance, demonstrated mastery of core competencies, and professional-quality deliverables. Students explore past capstone examples and begin ideating their own projects.

#### Key Topics

- **Evaluation Criteria:** (1) **Technical depth** — does the project demonstrate advanced IT skills beyond basic CRUD applications? (2) **Real-world relevance** — does it solve an actual problem or address a genuine need? (3) **Core competency coverage** — does it span multiple domains (systems, networking, security, databases, automation)? (4) **Professional quality** — would you show this to an employer?
- **Project Categories:** (1) **Infrastructure automation** — building CI/CD pipelines, self-service platforms, monitoring systems; (2) **Security architecture** — zero-trust implementation, security operations platform, threat detection; (3) **Data platform** — database cluster with HA/DR, data pipeline, analytics platform; (4) **Edge/IoT system** — distributed sensor network with edge processing; (5) **Service management** — ITSM platform, automated incident management; (6) **Research** — empirical study of IT practices, novel architecture evaluation.
- **Past Exemplars:** (1) "Yggdrasil Monitor" — an AI-driven observability platform predicting failures in the university's infrastructure; (2) "Ragnarök Recovery" — automated DR orchestration achieving 4-minute RTO; (3) "Freyja's Firewall" — zero-trust microsegmentation for a simulated enterprise.

#### Required Reading

- UoY Capstone Archive. (2039). *Exemplary Capstone Projects 2035-2039*.

---

### Lecture 2: Requirements Discovery — Understanding What to Build

**Course:** IT405 — Capstone Project I — Infrastructure Design
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

The most common cause of project failure is building the wrong thing. This lecture covers requirements discovery: stakeholder interviews, user stories, use cases, functional and non-functional requirements, and the art of distinguishing needs from wants.

#### Key Topics

- **Requirements Elicitation Techniques:** (1) stakeholder interviews; (2) observation of current workflows; (3) document analysis; (4) competitive analysis of existing solutions; (5) prototyping and feedback. By 2040, AI-assisted requirements analysis suggests overlooked requirements based on similar projects.
- **Functional vs. Non-Functional Requirements:** Functional: what the system does. Non-functional: how well it does it — performance, reliability, security, scalability, maintainability, usability. Non-functional requirements are frequently neglected but often determine project success. Example: "The monitoring system shall detect anomalies within 30 seconds (non-functional) and provide root cause hypotheses with >85% accuracy (functional)."
- **Prioritization:** MoSCoW method: Must have, Should have, Could have, Won't have (this iteration). Forces explicit prioritization — everything can't be highest priority. Helps manage scope creep.

#### Required Reading

- Wiegers, K., & Beatty, J. (2038). *Software Requirements* (4th ed.). Microsoft Press.

---

### Lecture 3: Architecture Design — From Requirements to Blueprint

**Course:** IT405 — Capstone Project I — Infrastructure Design
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Architecture transforms requirements into a technical blueprint. This lecture covers architecture design: architectural drivers, design patterns, trade-off analysis, and the Architecture Decision Record (ADR) practice.

#### Key Topics

- **Architecture Drivers:** (1) functional requirements; (2) quality attribute requirements (the "-ilities": reliability, scalability, security, maintainability); (3) constraints (budget, timeline, technology, compliance); (4) architectural principles and conventions. The architect's job: satisfy the drivers within the constraints.
- **Documenting Architecture:** (1) C4 model — Context (system in its environment), Container (high-level components), Component (within containers), Code (implementation details); (2) Architecture Decision Records (ADRs) — document significant decisions with context, options considered, rationale, and consequences; (3) Diagrams as code — use PlantUML, Mermaid, or Structurizr DSL so diagrams are version-controlled and reviewable.
- **Trade-off Analysis:** Every architectural decision involves trade-offs. The Architecture Trade-off Analysis Method (ATAM): (1) identify architectural approaches; (2) generate quality attribute utility tree; (3) analyze approaches against scenarios; (4) identify sensitivities (attributes affected by the decision), trade-offs (decisions that improve one attribute at the expense of another), and risks.

#### Required Reading

- Richards, M., & Ford, N. (2038). *Fundamentals of Software Architecture* (Updated ed.). O'Reilly Media.
- UoY Architecture Lab. (2039). *ADR Template and Examples*.

---

### Lecture 4: Technology Selection and Justification

**Course:** IT405 — Capstone Project I — Infrastructure Design
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Choosing the right technology is a core IT competency. This lecture covers technology evaluation: selection criteria, proof-of-concept prototyping, build-vs-buy analysis, and justifying choices with evidence.

#### Key Topics

- **Evaluation Criteria:** (1) functional fit — does it do what we need? (2) non-functional fit — performance, reliability, security; (3) operational fit — can we operate and maintain it? (4) ecosystem — community, documentation, support; (5) cost — licensing, hosting, personnel; (6) strategic fit — alignment with organizational direction; (7) risk — maturity, vendor stability, lock-in.
- **Proof of Concept (PoC):** Before committing, build a small prototype using the candidate technology to validate: (1) it works as advertised; (2) it integrates with other components; (3) performance meets requirements; (4) the team can work with it. Document PoC results as evidence for the technology choice.
- **The "Resume-Driven Development" Trap:** Choosing technologies because they're trendy or look good on a resume, rather than because they're appropriate for the problem. Guard against this with explicit evaluation criteria and documented rationale.

#### Required Reading

- UoY Tech Eval Lab. (2040). *Technology Selection Framework*.

---

### Lecture 5: Project Planning and Agile Methodology

**Course:** IT405 — Capstone Project I — Infrastructure Design
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Even the best architecture fails without execution. This lecture covers project planning: work breakdown structure, estimation, scheduling, risk management, and the agile practices that enable iterative delivery.

#### Key Topics

- **Work Breakdown Structure (WBS):** Decompose the project into manageable tasks. Principles: (1) each task is well-defined with clear completion criteria; (2) tasks are small enough to estimate reliably (1-5 days); (3) dependencies between tasks are identified; (4) the WBS covers 100% of project scope. By 2040, AI assists in generating initial WBS from requirements and architecture.
- **Agile for Infrastructure:** Infrastructure projects benefit from agile practices: (1) iterative delivery — build in small increments, get feedback, adjust; (2) user stories — "As a developer, I want to provision a database with one command so that I can focus on building features"; (3) sprints — 2-week iterations with demonstrable outcomes; (4) retrospectives — what went well, what to improve. Infrastructure as code makes agile infrastructure possible — changes are code, tested and deployed.
- **Risk Management:** Identify risks early: (1) risk register — name, description, probability, impact, mitigation; (2) review regularly — risks evolve; (3) have contingency plans — what if your chosen technology is deprecated mid-project? (4) communicate risks — don't hide bad news.

#### Required Reading

- Project Management Institute. (2039). *PMBOK Guide* (8th ed.). Selected chapters.

---

### Lecture 6: Infrastructure as Code — Building Reproducible Systems

**Course:** IT405 — Capstone Project I — Infrastructure Design
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Your capstone infrastructure must be reproducible — someone should be able to deploy it from your repository with a single command. This lecture covers IaC best practices, testing infrastructure code, and the GitOps workflow.

#### Key Topics

- **IaC Principles:** (1) everything in version control — no manual configuration; (2) declarative over imperative — specify desired state, not steps; (3) idempotent — apply multiple times safely; (4) modular and composable — reusable components; (5) tested — infrastructure changes validated before deployment.
- **IaC Tools:** Terraform/OpenTofu for cloud infrastructure, Ansible for configuration management, Pulumi for infrastructure in general-purpose languages, Crossplane for Kubernetes-native infrastructure. Choose the right tool for your project's scope and complexity.
- **Testing Infrastructure:** (1) linting (terraform validate, ansible-lint); (2) unit tests for modules (terratest); (3) integration tests — deploy to a test environment and verify; (4) policy checks (Open Policy Agent, Checkov) — security and compliance validation before deployment.

#### Required Reading

- Brikman, Y. (2038). *Terraform: Up and Running* (4th ed.). O'Reilly Media.

---

### Lecture 7: CI/CD Pipelines — Automating Quality

**Course:** IT405 — Capstone Project I — Infrastructure Design
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Continuous Integration and Continuous Delivery ensure that every change is automatically tested and deployable. This lecture covers CI/CD pipeline design, integration with IaC, and the practices that make automation reliable.

#### Key Topics

- **Pipeline Stages:** (1) **Lint** — code style, IaC validation; (2) **Build** — compile, package, containerize; (3) **Unit test** — test individual components; (4) **Integration test** — test components together; (5) **Security scan** — SAST, dependency scanning, container scanning; (6) **Deploy to staging** — automated deployment; (7) **Smoke test** — verify staging deployment; (8) **Deploy to production** — with approval gate for critical systems.
- **Pipeline as Code:** Define pipelines in version-controlled files (GitHub Actions, GitLab CI, Jenkinsfile). Benefits: version history, code review, reuse across projects. The capstone project must include a working CI/CD pipeline.
- **Progressive Delivery:** (1) canary deployments — roll out to a subset, monitor, expand; (2) blue-green — two environments, switch traffic; (3) feature flags — deploy code dark, toggle on for users.

#### Required Reading

- Humble, J., & Farley, D. (2038). *Continuous Delivery* (3rd ed.). Chapters on deployment pipelines.

---

### Lecture 8: Monitoring, Observability, and SLOs for Your Project

**Course:** IT405 — Capstone Project I — Infrastructure Design
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Your capstone must be observable — you must demonstrate that it works, measure its performance, and define what "working" means. This lecture covers instrumenting your project, defining SLOs, and building dashboards that tell the system's story.

#### Key Topics

- **The Three Pillars for Your Project:** (1) **Metrics** — Prometheus for time-series metrics, instrument your application and infrastructure; (2) **Logs** — structured logging (JSON), centralized with Loki or Elasticsearch; (3) **Traces** — distributed tracing with OpenTelemetry to understand request flows.
- **Defining Project SLOs:** What does success look like? Define SLOs that matter: (1) "99.9% of API requests complete within 200ms"; (2) "Backup verification succeeds daily"; (3) "Deployment pipeline completes within 15 minutes." Measure SLOs and demonstrate compliance in your final presentation.
- **Dashboards That Tell a Story:** A good dashboard answers: (1) is the system healthy? (2) how is it performing? (3) are SLOs being met? (4) are there any anomalies? Build dashboards (Grafana) that a non-technical stakeholder could understand.

#### Required Reading

- OpenTelemetry. (2040). *Getting Started Guide*.

---

### Lecture 9: Professional Communication — Documentation, Presentations, and Demos

**Course:** IT405 — Capstone Project I — Infrastructure Design
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Technical excellence without communication is invisible. This lecture covers professional communication for IT professionals: writing effective documentation, delivering compelling presentations, and demonstrating systems convincingly.

#### Key Topics

- **Documentation That Works:** (1) README — what the project is, how to deploy it, how to contribute; (2) Architecture document — diagrams, ADRs, rationale; (3) Operations guide — how to monitor, troubleshoot, and recover; (4) API documentation — if your project has an API, it must be documented. Apply the principle: "If it's not documented, it doesn't exist."
- **Presentation Skills:** (1) tell a story — problem → approach → solution → results; (2) know your audience — technical depth varies; (3) demonstrate, don't just describe; (4) anticipate questions and prepare answers; (5) practice — the first run-through is always rough.
- **Demo Preparation:** A failed demo undermines credibility: (1) prepare a script and rehearse; (2) have a backup (screenshots, recording) in case of live issues; (3) clean up your environment (no personal tabs, notifications); (4) start from a known state.

#### Required Reading

- UoY Communication Lab. (2039). *Technical Communication for IT Professionals*.

---

### Lecture 10: Milestone 1 Review — Proposal and Architecture

**Course:** IT405 — Capstone Project I — Infrastructure Design
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

First formal checkpoint: students present their project proposal and architecture to faculty advisors and peers for feedback. This is not a grade — it's an opportunity to identify issues early.

#### Deliverables

1. Project proposal (2-3 pages): problem statement, proposed solution, scope
2. Requirements document: functional and non-functional, prioritized
3. Architecture document: C4 diagrams, ADRs for key decisions, technology choices with rationale
4. Project plan: WBS, timeline, risk register
5. 15-minute presentation with Q&A

#### Success Criteria

Architecture is coherent, requirements are clear, scope is realistic, and the plan is credible. Faculty feedback focuses on: is the project ambitious enough? Is it achievable in two semesters? Are there obvious risks not addressed?

---

### Lecture 11: Milestone 2 Review — Proof of Concept

**Course:** IT405 — Capstone Project I — Infrastructure Design
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Second checkpoint: students demonstrate a working proof of concept — enough to validate the architecture and technology choices. This is the moment of truth: does the architecture actually work?

#### Deliverables

1. Working proof of concept (deployable from repository)
2. Infrastructure as code (Terraform/Ansible/etc.)
3. CI/CD pipeline (at minimum: lint, test, deploy to test environment)
4. Basic monitoring (metrics dashboard, health checks)
5. Updated architecture document (reflecting what was learned during implementation)
6. 15-minute demo with Q&A

#### Success Criteria

The PoC validates that the architecture works, the technology choices are viable, and the team can execute. Issues identified during Milestone 1 should be addressed.

---

### Lecture 12: End-of-Semester Submission and Looking Ahead to IT407

**Course:** IT405 — Capstone Project I — Infrastructure Design
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Final submission for IT405, and a look ahead to IT407 (Capstone II) where the project will be completed, tested, and presented publicly.

#### Deliverables for IT405 Final Submission

1. Complete architecture and design documentation
2. Functional CI/CD pipeline
3. Infrastructure as Code repository
4. Working proof of concept or initial implementation
5. Updated project plan for IT407
6. Self-assessment and lessons learned reflection

#### Looking Ahead to IT407

IT407 will focus on: (1) completing implementation; (2) thorough testing (functional, performance, security, chaos); (3) measuring against SLOs; (4) writing comprehensive documentation; (5) public presentation to faculty, peers, and industry guests. The work done in IT405 is the foundation — IT407 is where the project becomes something you're proud to show.

---

## Evaluation

- Milestone 1 (Proposal + Architecture): 20%
- Milestone 2 (Proof of Concept): 25%
- Final Documentation and Repository: 25%
- Presentation and Demo: 20%
- Peer Review and Participation: 10%

---

**Þǫkk — May your capstone be worthy of the All-Father's gaze.**
