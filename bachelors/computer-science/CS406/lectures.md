# CS406: Capstone Project I — Design, Architecture, and Prototype
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4
**Prerequisites:** All required 100–300 level CS courses; CS405 — Research Methods (co-requisite).
**Description:** The first semester of the two-semester CS capstone sequence. Students work in teams of 3–5 to scope, design, architect, and prototype a substantial software or hardware-software system. Emphasis on requirements engineering, system architecture, iterative prototyping, user-centered design, team collaboration, and professional software development practices. By semester's end, each team delivers a working prototype, a detailed architecture document, a sprint retrospective, and a project plan for CS408 (Capstone II: Implementation). The capstone is the culminating experience of the B.Sc. in Computer Science — the bridge from academic exercise to professional practice.

---

## Lecture 1: The Capstone Mindset — From Student to Engineer

*"The apprentice smith, after years at the bellows, is finally handed the hammer and told: 'Make something that will outlast you.'"*

The capstone is the transition point. For three years, you have solved well-defined problems with known solutions — implement this data structure, optimize that algorithm, prove this theorem. The capstone is different: the problem is yours to define, the solution is yours to design, and no one knows in advance whether what you propose will work. This is not a bug; it's the feature. Engineering is the discipline of making things work under uncertainty, with incomplete information, on a deadline, with a team of human beings who have different strengths, different schedules, and different opinions. Welcome.

The capstone mindset has three pillars. First, **ownership**: this is *your* project, not your professor's. The teaching team provides guidance, feedback, and guardrails, but the vision, the decisions, and the accountability are yours. When the prototype crashes during the demo, you don't say "the framework has a bug" — you say "we didn't test that edge case, and here's our plan to fix it." Second, **pragmatism**: perfection is the enemy of done. The capstone is 14 weeks long. You cannot build the platonic ideal of your system. You must make trade-offs — which features are essential for the prototype? Which can be faked with wizard-of-oz techniques? Which can be deferred to CS408? The skill of *scoping* — choosing the right amount of ambition — is what separates projects that ship from projects that stall. Third, **reflection**: the capstone is a learning experience, not just a product. Your grade depends partly on the quality of your prototype, but equally on the quality of your *process* — how well you documented decisions, how thoughtfully you responded to feedback, how honestly you assessed what went wrong and what you'd do differently.

By 2040, capstone projects at Yggdrasil have produced startups (three YC-backed companies began as CS406 prototypes), published papers (eight capstone projects have appeared at top conferences after refinement in CS408), and open-source tools used by thousands (the Yggdrasil Experiment Tracker began as a 2040 capstone). Your project might join that lineage. But even if it doesn't, the capstone will teach you more about professional software development than any lecture course — because you will learn by doing, by failing, by fixing, and by shipping.

The deliverables for CS406 are concrete. By Week 14, your team must produce: (1) a **Project Proposal** (Week 2) — 2 pages defining the problem, proposed solution, and success criteria; (2) a **Requirements Document** (Week 4) — functional and non-functional requirements, user stories, acceptance criteria; (3) an **Architecture Document** (Week 8) — system architecture diagram, component descriptions, technology stack rationale, data model; (4) a **Working Prototype** (Week 12) — a functional system demonstrating the core user journey, deployed on the Yggdrasil Capstone Cloud; (5) a **Sprint Retrospective** (Week 14) — what worked, what didn't, what you'll do differently in CS408; (6) a **CS408 Project Plan** (Week 14) — a detailed plan for completing the full system in the second semester. Every deliverable is graded on both content and professional presentation.

**Required Reading:**
- Brooks, F.P. (1995). *The Mythical Man-Month: Essays on Software Engineering* (Anniversary ed.). Addison-Wesley. Chapters 1–3, 16 ("No Silver Bullet").
- Ousterhout, J. (2018). *A Philosophy of Software Design*. Yaknyam Press. Chapters 1–5.
- University of Yggdrasil Capstone Office (2040). *CS406/CS408 Capstone Handbook 2040–2041*. Contains rubrics, milestone dates, and past project examples.
- Rúnþjófr, E. (2039). *The First Hammer-Blow: A Guide to Your CS Capstone*. Yggdrasil Technical Report YTR-2039-12.

**Discussion Questions:**
1. Brooks' Law states: "Adding manpower to a late software project makes it later." If your capstone team of four is behind schedule in Week 10, what should you do? What *can* you do?
2. What's the difference between a project that's "done" and a project that's "good enough"? How do you define "good enough" for your capstone — what are your non-negotiable requirements?
3. A teammate proposes building a distributed system with microservices. Your capstone is 14 weeks. What questions would you ask to determine if this architecture is appropriate for your project's scope and team's experience?

---

## Lecture 2: Project Scoping and Requirements Engineering

*"A ship built without knowing its destination will find every shore — and call none home."*

The most common cause of capstone failure is not technical difficulty — it's scope creep. Teams start with boundless ambition ("we'll build a platform for...") and by Week 8 are drowning in half-implemented features, none of which work end-to-end. The antidote is rigorous scoping and requirements engineering — the discipline of figuring out *exactly* what you're building *before* you start building it.

**Scoping** is the process of deciding what's in and what's out. The tool is the **MoSCoW framework**: Must have (non-negotiable, the system fails without it), Should have (important but not critical, can be deferred if necessary), Could have (desirable but not essential), and Won't have (explicitly excluded from this version). For CS406, your prototype must deliver all "Must have" features, most "Should have" features, and as many "Could have" features as time permits. The "Won't have" list is just as important — it protects you from feature creep by making exclusion explicit and consensual. When your stakeholder (the instructor, your client, your future self) asks "can we add X?" you can point to the MoSCoW and say "X is on our Won't have list for CS406; we can consider it for CS408."

**Requirements engineering** translates stakeholder needs into a specification the team can build against. The standard artifact is the **Software Requirements Specification (SRS)** , which the IEEE 830 standard defines as a document describing *what* the system should do (functional requirements) and *how well* it should do it (non-functional requirements). Functional requirements are specific behaviors: "The system shall allow users to upload PDF documents and extract text via OCR." Non-functional requirements include performance ("OCR must complete within 2 seconds for a 10-page document"), reliability ("system uptime must exceed 99.5% during demo week"), security ("all user data must be encrypted at rest and in transit"), usability ("a new user must be able to upload and search a document within 5 minutes without documentation"), and maintainability ("the codebase must have ≥80% test coverage and pass linting with zero warnings"). Each requirement must be **verifiable** — you must be able to test whether it's met. "The system shall be fast" is not a requirement; "The system shall return search results within 200 ms at p95 under 100 concurrent users" is.

In 2040, requirements are increasingly expressed as **user stories** following the format: "As a [user role], I want [goal] so that [reason]." User stories are accompanied by **acceptance criteria** — a checklist of conditions that must be met for the story to be considered done. Example: "As a researcher, I want to search my document library by keyword so that I can find relevant papers quickly. Acceptance criteria: (1) Search returns results within 200 ms for libraries up to 10,000 documents. (2) Results are ranked by relevance, with exact matches first. (3) Search supports Boolean operators (AND, OR, NOT). (4) Empty search returns all documents sorted by date." The user story + acceptance criteria format keeps requirements grounded in user value and provides a clear "definition of done."

**Stakeholder analysis** is the human side of requirements. Who cares about this system? Your direct users, obviously. But also: system administrators (who must deploy and maintain it), data providers (whose APIs or datasets you depend on), regulators (if your system handles personal data), and future developers (including your CS408 selves — you are a stakeholder of your own code). Each stakeholder has different needs and constraints. A common capstone mistake: designing for the ideal user (tech-savvy, motivated, with perfect data) and ignoring the edge cases (the user on a slow connection, the user who doesn't read documentation, the data that's messy and incomplete). The best capstones emerge from teams that spend real time with real users before writing a single line of code.

**Required Reading:**
- IEEE Std 830-1998. "IEEE Recommended Practice for Software Requirements Specifications."
- Cohn, M. (2004). *User Stories Applied: For Agile Software Development*. Addison-Wesley. Chapters 1–6.
- Wiegers, K. & Beatty, J. (2013). *Software Requirements* (3rd ed.). Microsoft Press. Chapters 1–4, 10.
- Yggdrasil Capstone Office (2040). *SRS Template and Rubric for CS406*. Includes annotated examples from prior capstones.
- Þórsdóttir, G. (2037). *Stakeholder Voices: A Field Guide to Requirements Elicitation in 2040*. Yggdrasil University Press.

**Discussion Questions:**
1. Your team proposes a capstone: "An AI-powered study assistant for university students." Apply MoSCoW: what are the Must, Should, Could, and Won't have features for a 14-week prototype?
2. A stakeholder says "the system should be user-friendly." Rewrite this as three verifiable, testable non-functional requirements.
3. Your team spends 3 weeks building a feature that, during user testing, no one uses. What went wrong in your requirements process? How could you have discovered this earlier?

---

## Lecture 3: System Design and Architecture

*"A longhouse is not built by stacking logs at random. The central beam bears the roof; every other timber knows its place. So too must your system have a spine."*

System architecture is the set of *significant design decisions* that shape a software system — the choices that are hard to change later. These include: the overall structure (monolith, microservices, serverless, event-driven), the data storage strategy (SQL, NoSQL, vector database, blockchain), the communication patterns (REST, gRPC, GraphQL, message queues, WebSockets), the deployment model (cloud VM, container orchestration, edge devices), and the cross-cutting concerns (authentication, logging, monitoring, error handling). Architecture is not just a diagram; it's the set of constraints that enable or restrict everything that follows.

The **C4 model** (Context, Containers, Components, Code) provides a structured way to describe architecture at multiple levels of abstraction. **Level 1: System Context** — a single diagram showing your system as a box in the center, surrounded by users and external systems it interacts with. **Level 2: Containers** — the high-level technical building blocks: a web app, a mobile app, an API server, a database, a message queue, a file store. **Level 3: Components** — within each container, the major structural components: within the API server, you might have controllers, services, repositories, and authentication middleware. **Level 4: Code** — class diagrams or module structure, generated from the actual codebase (not drawn by hand). The C4 model's insight is that different audiences need different levels: your stakeholder wants Level 1; your CS408 teammates want Level 3; your compiler wants Level 4. For CS406, you must produce Levels 1–3; Level 4 will emerge naturally from your implementation in CS408.

**Architectural patterns** are reusable solutions to recurring design problems. The patterns that matter most for capstone projects in 2040 include: **Model-View-Controller (MVC)** and its web-era variants (Model-View-ViewModel, Model-View-Presenter) — separating data, presentation, and user input; **Hexagonal Architecture (Ports and Adapters)** — the core business logic is isolated from infrastructure (databases, web frameworks, external APIs) through interfaces (ports) and implementations (adapters), enabling easy testing and technology swapping; **Event-Driven Architecture** — components communicate through events published to a message broker, enabling loose coupling and asynchronous processing (essential for systems with real-time features); **CQRS (Command Query Responsibility Segregation)** — separating read and write models, useful when read patterns (complex queries, aggregations) differ significantly from write patterns (simple creates and updates); and **Microkernel / Plugin Architecture** — a minimal core with extensibility through plugins, appropriate for tools, IDEs, and platforms that need third-party extensibility.

Architecture is fundamentally about managing **trade-offs**. Every architectural decision has pros and cons, and the skill is choosing the right trade-offs for your specific context. A monolith is simpler to develop, test, and deploy — but harder to scale and to split across multiple teams. Microservices enable independent deployment and technology diversity — but introduce network latency, distributed debugging complexity, and data consistency challenges. A NoSQL database offers flexible schema and horizontal scalability — but loses ACID transactions and rich querying. For a 14-week capstone prototype, the right answer is usually the simplest architecture that can plausibly evolve into the full system in CS408. Over-engineering a capstone prototype (Kubernetes cluster for a 3-user app, event sourcing for a todo list) is a classic failure mode. Start simple, and let complexity be *earned* by demonstrated need.

In 2040, architectural decisions increasingly involve **AI components** — should your system embed a language model? Call an external AI API? Train a custom model? These decisions have architectural implications: latency (API calls add 200–800 ms), cost (API calls cost money per request), reliability (external APIs can fail or change), privacy (user data sent to external APIs), and vendor lock-in (your system depends on a specific provider). The CS406 architecture document must justify AI-related architectural choices with the same rigor as database or framework choices.

**Required Reading:**
- Brown, S. (2018). *The C4 Model for Visualising Software Architecture*. leanpub.com/visualising-software-architecture.
- Richards, M. & Ford, N. (2020). *Fundamentals of Software Architecture: An Engineering Approach*. O'Reilly. Chapters 1–7.
- Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley. Chapters 1, 3 (creational patterns), 5 (behavioral patterns).
- Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly. Chapters 1–3, 5.
- Yggdrasil Architecture Review Board (2040). *Capstone Architecture Requirements and Rubric*. YGG-ARB-2040-02.

**Discussion Questions:**
1. Your capstone is a real-time collaborative code editor. Evaluate three architectural alternatives: (a) monolith with WebSocket connections, (b) microservices with a message broker, (c) a serverless architecture with a real-time database. What are the trade-offs for a 14-week prototype?
2. Draw a Level 2 C4 diagram for your proposed capstone project. What's the most uncertain container — the one you're least sure about the technology choice for? How will you de-risk it?
3. "AI components" are increasingly embedded in capstone projects. What are three architectural pitfalls of calling an external LLM API from your backend, and how would you mitigate them?

---

## Lecture 4: Technology Selection and Trade-off Analysis

*"A warrior does not choose the heaviest sword or the sharpest — she chooses the one that fits her hand and the battle she faces."*

Technology selection is a decision-making skill, not a trivia contest. The student who picks Rust "because it's fast" without considering whether their team knows Rust, whether the ecosystem has the libraries they need, or whether garbage collection is actually their bottleneck is not making an architectural decision — they're expressing a preference. Technology selection must be systematic, explicit, and documented.

The **Architecture Decision Record (ADR)** is the tool of choice. An ADR is a short document (1–2 pages) that records a specific architectural decision, the context in which it was made, the options considered, the rationale for the chosen option, and the consequences (both positive and negative). The format is simple: **Title** (e.g., "ADR-003: Choose PostgreSQL over MongoDB for user data storage"), **Status** (proposed / accepted / deprecated / superseded), **Context** (what's the situation? what constraints apply?), **Decision** (what did we choose?), **Consequences** (what becomes easier? what becomes harder?), and **Alternatives Considered** (what else did we evaluate and why was it rejected?). ADRs create an institutional memory of *why* decisions were made — invaluable when, six months later in CS408, someone asks "why did we choose X?" and no one remembers. CS406 requires at least three ADRs in your architecture document.

A **technology comparison matrix** is useful for decisions with multiple comparable options. List your options as rows and your evaluation criteria as columns. Criteria should include *functional fit* (does it do what we need?), *learning curve* (how long for the team to become productive?), *ecosystem maturity* (are there libraries, tutorials, and community support?), *performance* (does it meet our latency/throughput requirements?), *operational complexity* (how hard to deploy, monitor, and debug?), *licensing and cost* (open source? paid? usage-based pricing?), *team familiarity* (does anyone already know it?), and *longevity* (will it still be maintained in 2 years?). Score each option on each criterion (1–5 scale, weighted if some criteria matter more). The matrix won't make the decision for you, but it will make your reasoning explicit and expose disagreements early.

The **stack components** for a typical web-based capstone in 2040 include: **Frontend** — React, Svelte, Vue, or HTMX (for simpler projects); **Backend** — Node.js/Express, Python/FastAPI, Go/Gin, Rust/Actix; **Database** — PostgreSQL (relational), MongoDB (document), Neo4j (graph), Pinecone/Weaviate (vector, for AI projects); **Authentication** — Auth0, Clerk, Supabase Auth, or the Yggdrasil Single Sign-On (YSSO); **Hosting** — the Yggdrasil Capstone Cloud (free for students), Vercel, Fly.io, or a Raspberry Pi cluster for IoT/edge projects; **CI/CD** — GitHub Actions or the Yggdrasil Forge CI; **Monitoring** — Sentry (errors), Grafana (metrics), or the Yggdrasil Observatory. The stack is a means, not an end. Choose the simplest stack that meets your requirements and that your team can operate. A capstone that ships with a boring stack is infinitely better than a capstone that fails with an exciting stack.

**Required Reading:**
- Nygard, M. (2017). *Documenting Architecture Decisions*. ThoughtWorks. [The original ADR proposal — short and essential.]
- Keeling, M. (2017). *Design It! From Programmer to Software Architect*. Pragmatic Bookshelf. Chapters 3–5 (architecture drivers, quality attributes, technology choices).
- Ford, N., Parsons, R., & Kua, P. (2017). *Building Evolutionary Architectures*. O'Reilly. Chapters 1–2.
- Yggdrasil Technology Advisory (2040). *Approved Technology Stack for CS406/CS408 Capstones*. Lists supported platforms, libraries, and services with free student access.
- Gaulthildr, H. (2039). *The Weighted Blade: Technology Selection for Capstone Projects*. Yggdrasil Technical Note YTN-2039-04.

**Discussion Questions:**
1. Your team is evenly split between choosing Python (FastAPI) and Go (Gin) for a backend API. Construct an ADR for this decision. What's your recommendation, and what's the strongest argument for the option you rejected?
2. A teammate wants to use a new JavaScript framework released 3 months ago with 500 GitHub stars. The alternative is React, with 200K+ stars and a decade of ecosystem maturity. When is it appropriate to bet on a new technology in a capstone? When is it reckless?
3. Your capstone requires storing and querying vector embeddings for semantic search. Evaluate: (a) PostgreSQL with pgvector extension, (b) Pinecone, (c) ChromaDB (self-hosted). What are the trade-offs for a student team with zero budget?

---

## Lecture 5: Prototyping and Iterative Development

*"The first keel you lay will not be the ship that sails — but without it, no ship will ever sail."*

Prototyping is the engine of the capstone. A prototype is a concrete, functional artifact that tests a hypothesis about your system — "can we do this?" "will users understand this?" "does this architecture hold up under load?" Prototyping is not building half the system sloppily; it's building a thin vertical slice of the system well enough to learn from it. The difference is the difference between a draft (written to be revised) and an outline (written to be filled in). A prototype is a draft — it works, it's testable, it's throwaway or evolve-able.

The **prototyping spectrum** ranges from low-fidelity to high-fidelity. **Paper prototypes** (sketches on paper, wireframes in Figma) are for testing user flows and information architecture — fast, cheap, and surprisingly effective at uncovering usability problems. **Wizard-of-Oz prototypes** simulate AI or backend functionality with a human behind the curtain — essential for testing AI-powered features before the AI is built. **Horizontal prototypes** implement a thin layer across all major features — useful for validating the architecture and demonstrating scope. **Vertical prototypes** implement one feature end-to-end, from UI to database — useful for validating the technology stack and uncovering integration issues. For CS406, your deliverable should be a **functional vertical prototype** — one complete user journey that demonstrates your core value proposition, built on the actual technology stack with real (not mocked) backend logic for that journey.

**Iterative development** is the rhythm of prototype → evaluate → learn → revise. The unit of iteration is the **sprint** — a fixed timebox (typically 1–2 weeks for capstones) in which the team commits to completing specific, concrete tasks. At sprint's end: demo what was built, gather feedback (from users, from the teaching team, from automated tests), reflect on what went well and what didn't (the sprint retrospective), and plan the next sprint. The agile manifesto's values apply: *individuals and interactions over processes and tools, working software over comprehensive documentation, customer collaboration over contract negotiation, responding to change over following a plan.* "Agile" is not a set of rituals (standups, story points, burndown charts) — it's a mindset of continuous learning and adaptation. The rituals serve the mindset, not the reverse.

The **fail-fast principle** is the prototyping corollary to risk management. If a technical decision is risky — a new library, a performance-critical algorithm, an integration with an unfamiliar API — address it in the *first* sprint, not the last. If it's going to fail, you want to know in Week 3, not Week 13, when you still have time to pivot. The capstone teams that succeed are not the ones that avoid failure — they're the ones that fail early, cheaply, and learn from each failure. The teams that struggle are the ones that spend 10 weeks in planning meetings and then discover in Week 11 that their core assumption was wrong.

In 2040, prototyping is accelerated by AI-assisted development: LLMs generate boilerplate, suggest implementations, and write tests. But AI assistance introduces a new prototyping pitfall: **the illusion of progress**. An LLM can generate 5,000 lines of plausible-looking code in minutes, but plausible is not correct. The prototype must be *understood* by the team, not just generated. A prototype you don't understand is a prototype you can't debug, can't extend, and can't learn from. Use AI tools as accelerators, not as substitutes for comprehension. Every line of AI-generated code in your capstone must be code-reviewed, tested, and understood by at least one human teammate.

**Required Reading:**
- Ries, E. (2011). *The Lean Startup*. Crown Business. Chapters 4–6 (the Build-Measure-Learn loop).
- Knapp, J., Zeratsky, J., & Kowitz, B. (2016). *Sprint: How to Solve Big Problems and Test New Ideas in Just Five Days*. Simon & Schuster.
- Rubin, K.S. (2012). *Essential Scrum: A Practical Guide to the Most Popular Agile Process*. Addison-Wesley. Chapters 3–7.
- Nielsen, J. (1994). *Usability Engineering*. Morgan Kaufmann. Chapter 5 (heuristic evaluation).
- Yggdrasil Capstone Office (2040). *Prototyping Guidelines for AI-Intensive Projects*. Includes guidance on LLM usage and disclosure requirements.

**Discussion Questions:**
1. Your team's capstone involves a novel recommendation algorithm. Design a Week 1–3 prototyping plan that de-risks this algorithm. What's the simplest possible experiment to test whether your approach has merit?
2. You show your prototype to three users. Two love it. One is confused and frustrated. Do you change the design? How do you decide?
3. An LLM generates a working prototype of your core feature in 2 hours. Your team could spend the remaining 12 weeks polishing it. What risks are you accepting with this approach? How do you mitigate them?

---

## Lecture 6: User-Centered Design and Usability Testing

*"Ask the farmer, not the blacksmith, whether the plow is well-made."*

A system that no one can use is a system that no one uses. User-centered design (UCD) is the methodology that places actual users — their needs, their contexts, their cognitive models — at the center of the design process. This is not "making things pretty" (that's visual design); it's making things *usable* — learnable, efficient, error-tolerant, and satisfying. For capstone projects, usability is often the difference between a prototype that impresses the review panel and one that provokes the question "but would anyone actually use this?"

The **UCD process** is iterative: **research** (understand users and their tasks), **design** (create interface concepts), **prototype** (build testable representations), **evaluate** (test with users), repeat. The research phase uses methods from CS405: interviews, observations, surveys, contextual inquiry (watching users work in their actual environment). The output is **personas** (fictional but evidence-based user archetypes — "Maya, the time-pressed graduate student who needs to find papers quickly, often on her phone during her commute") and **scenarios** (narrative descriptions of how personas accomplish goals with your system). Personas prevent the design-by-self problem: "I'd use it this way, so everyone will." (They won't.)

**Usability heuristics** (Nielsen, 1994) provide a quick, cheap evaluation method: (1) Visibility of system status — the user always knows what's happening. (2) Match between system and real world — use language and concepts familiar to users. (3) User control and freedom — undo, redo, clear exits. (4) Consistency and standards — the same thing looks and works the same way everywhere. (5) Error prevention — design so errors are hard to make. (6) Recognition rather than recall — don't make users remember things from one screen to the next. (7) Flexibility and efficiency of use — shortcuts for experts, guidance for novices. (8) Aesthetic and minimalist design — every element serves a purpose. (9) Help users recognize, diagnose, and recover from errors — clear error messages with recovery paths. (10) Help and documentation — even though the goal is to need none. A heuristic evaluation — where 3–5 evaluators independently review the interface against these heuristics — catches 80% of usability problems before a single user touches the system.

**Usability testing** observes real users attempting real tasks with your system. The protocol: recruit 5 users (Nielsen's rule of thumb: 5 users catch ~85% of problems; more users find diminishing returns per person), give them specific tasks ("find a paper on neuromorphic computing published after 2038 and save it to your reading list"), observe silently (don't explain, don't help — you're testing the system, not the user), and record what they do, where they struggle, and what they say (the "think-aloud" protocol — ask them to verbalize their thoughts). After: identify severity ratings for each problem (cosmetic / minor / major / catastrophic), prioritize fixes, and retest. A single round of usability testing with 5 users typically reveals 30–50 problems, many of which the developers never anticipated.

**Accessibility** is usability for people with disabilities — and it's not optional. The **Web Content Accessibility Guidelines (WCAG) 2.2** (updated 2040) define four principles: **Perceivable** (information must be presentable to all senses — alt text for images, captions for video), **Operable** (all functionality must be available from a keyboard, sufficient time to read and use content), **Understandable** (text must be readable, interfaces must behave predictably), and **Robust** (content must be compatible with assistive technologies like screen readers). In 2040, Yggdrasil University requires all student-facing software to meet WCAG 2.2 Level AA. Your capstone must pass automated accessibility checks (using axe-core or the Yggdrasil A11y Auditor) and should include at least one test with a screen reader (VoiceOver, NVDA, or Orca).

**Required Reading:**
- Norman, D. (2013). *The Design of Everyday Things* (Revised ed.). Basic Books. Chapters 1–4.
- Nielsen, J. (1994). "10 Usability Heuristics for User Interface Design." *Nielsen Norman Group*.
- Krug, S. (2014). *Don't Make Me Think, Revisited: A Common Sense Approach to Web Usability* (3rd ed.). New Riders. Chapters 1–7.
- W3C (2023, updated 2040). *Web Content Accessibility Guidelines (WCAG) 2.2*. W3C Recommendation.
- University of Yggdrasil Accessibility Office (2040). *Software Accessibility Requirements for Student Projects*. YGG-A11Y-2040-01.

**Discussion Questions:**
1. Your capstone is a dashboard for visualizing climate data. Conduct a heuristic evaluation of the concept: go through Nielsen's 10 heuristics and identify at least one potential violation for each.
2. During usability testing, a user spends 3 minutes trying to find the "export" button. They eventually give up. What's your severity rating for this problem? What design changes would you consider?
3. Your team says "we'll make it accessible later, during CS408." Why is this a bad strategy? What accessibility issues are architectural (hard to retrofit) versus cosmetic (easy to fix later)?

---

## Lecture 7: Team Dynamics and Agile Project Management in 2040

*"A shield-wall holds not because every warrior is the strongest, but because each trusts the one beside them."*

The capstone is a team sport. The technical challenges are real, but the human challenges — communication, coordination, conflict resolution, motivation — are what sink most capstone projects. This lecture is about making your team work.

**Team composition** matters, but diversity matters more than individual brilliance. The ideal capstone team has a mix of skills (frontend, backend, design, project management, domain expertise) and a mix of working styles (the visionary who generates ideas, the pragmatist who asks "but how?", the detail-oriented tester who finds edge cases, the communicator who documents and presents). A team of five brilliant backend engineers will build a beautiful API that no one can use. A team of five designers will produce gorgeous mockups with no working code. The CS406 team formation process (Week 1) includes a skills inventory and a "working style" self-assessment (based on Belbin's team roles). Use these intentionally — don't just team up with your friends.

**Agile project management** provides the operational rhythm. The core practices: **sprint planning** (at the start of each sprint, the team commits to a set of tasks, estimated in story points or hours, based on velocity from previous sprints), **daily standup** (15 minutes max; each person answers: what did I do yesterday? what will I do today? what's blocking me?), **sprint review** (at sprint's end, demo working software to stakeholders), **sprint retrospective** (team-only meeting: what went well? what went wrong? what will we change next sprint?). The retrospective is the most important and most neglected practice. It's the team's mechanism for self-improvement. A good retro produces 1–3 concrete action items ("we'll enforce code review before merge," "we'll update the README after every feature"), not vague resolutions ("we'll communicate better").

**Conflict** is inevitable and, handled well, productive. Task conflict (disagreement about what to build or how to build it) improves outcomes when the team has psychological safety — the shared belief that it's safe to take interpersonal risks, to admit mistakes, to ask questions, to disagree openly. Relationship conflict (personal friction, resentment, blame) destroys teams. The distinction matters. When a teammate says "I think the microservices approach adds unnecessary complexity for our timeline," that's task conflict — engage with the substance. When a teammate says "your code is always a mess and you never listen," that's relationship conflict — address the dynamic, not the code. The ground rule: critique ideas, not people. "This design has a problem with X" is constructive; "you always design things wrong" is destructive.

**Remote and hybrid teams** are the norm in 2040, thanks to tools that make distributed collaboration as rich as co-located work. The Yggdrasil Capstone Cloud provides persistent virtual workspaces — shared terminals, collaborative editors, always-on video portals. But remote work amplifies communication challenges: you lose the ambient awareness of who's working on what, the quick hallway conversations that resolve small issues before they become big ones, the social bonding that makes conflict survivable. Compensate with **overcommunication** — when in doubt, say more, not less. Use asynchronous updates (a team Slack/Discord channel with end-of-day summaries) so that members in different time zones stay informed. Schedule synchronous time (at least 2 hours per week of real-time collaboration, not just status updates) for the creative work that benefits from rapid back-and-forth. And explicitly invest in social connection — a team that has shared a meal (even virtually) or played a game together handles stress better than a team that only interacts through pull requests.

**Required Reading:**
- Edmondson, A.C. (1999). "Psychological Safety and Learning Behavior in Work Teams." *Administrative Science Quarterly*, 44(2), 350–383.
- Lencioni, P. (2002). *The Five Dysfunctions of a Team: A Leadership Fable*. Jossey-Bass.
- Sutherland, J. & Sutherland, J.J. (2014). *Scrum: The Art of Doing Twice the Work in Half the Time*. Crown Business.
- Google re:Work (2017). "Guide: Understand Team Effectiveness." [The Project Aristotle findings on psychological safety.]
- Yggdrasil Capstone Office (2040). *Team Charter Template and Conflict Resolution Protocol*. Includes escalation paths when internal resolution fails.

**Discussion Questions:**
1. A teammate consistently misses deadlines, and their code quality is below the team's standards. As a peer (not a manager), how do you address this? What would you say in a one-on-one conversation?
2. Your team's sprint retrospective produces the same "we need to communicate better" action item for the third sprint in a row. What's going wrong, and how would you break the cycle?
3. You and a teammate disagree fundamentally about the project's architecture. You favor a monolith; they favor microservices. Neither will convince the other. What's your next step? At what point should you escalate to the teaching team?

---

## Lecture 8: Version Control, CI/CD, and DevOps for Capstone Projects

*"A runemaster who carves without recording the stroke will, in time, forget even her own spells."*

Professional software development in 2040 is unimaginable without the DevOps toolchain: version control, continuous integration, continuous delivery, infrastructure as code, monitoring, and observability. The capstone is where you learn to use these tools not as course requirements but as force multipliers — they protect you from yourself, from each other, and from the chaos of 14 weeks of concurrent development.

**Version control** with Git is the foundation. Beyond the basics (clone, add, commit, push, pull), your team must adopt a **branching strategy**. For capstone projects, **trunk-based development** is strongly recommended: all developers work on short-lived feature branches (≤ 2 days) that merge to `main` frequently. This minimizes merge conflicts — the bane of student projects, where three teammates work in isolation for two weeks and then spend a weekend resolving a 200-line conflict. The discipline: pull the latest `main` before starting work, keep branches small (one feature, one bug fix, one refactor), open a pull request (PR) before merging, require at least one teammate's review and approval, and never merge your own PR without review. The `main` branch must always be deployable — a green CI pipeline, passing tests, no known regressions. This is the **"always be shippable"** principle.

**Continuous Integration (CI)** automates the verification that your code works. On every push and every PR, the CI pipeline runs: linting (code style, static analysis), unit tests (fast, isolated), integration tests (slower, tests interactions between components), build (does the project compile/package?), and sometimes security scans (dependency vulnerabilities, secret detection). If any step fails, the pipeline is "red" — fixing it is the team's top priority. A red pipeline that stays red for days normalizes failure and defeats the purpose of CI. The Yggdrasil Forge CI (based on GitHub Actions) is pre-configured for common capstone stacks — one click sets up linting, testing, and deployment. There is no excuse for a capstone project without CI in 2040.

**Continuous Delivery (CD)** extends CI by automating deployment. On every merge to `main`, the CD pipeline builds a deployable artifact (Docker image, static site bundle, compiled binary), runs any remaining tests (end-to-end, performance), and deploys to a staging environment. Deployment to production may be automatic (continuous deployment) or require a manual approval step (continuous delivery). For capstones, the Yggdrasil Capstone Cloud provides one-click CD with automatic HTTPS, database provisioning, and monitoring dashboards. Setting up CD takes 30 minutes and pays back hours of manual deployment effort over the semester — not to mention preventing the "it worked on my machine" demo disaster.

**Infrastructure as Code (IaC)** treats server configuration as version-controlled source code. Instead of SSH-ing into a server and running commands, you write configuration files (Docker Compose, Terraform, Ansible, Pulumi) that declaratively specify the desired state. The CD pipeline applies these configurations automatically. Benefits: your infrastructure is reproducible (spin up an identical environment for testing), auditable (every change is in Git with a commit message and reviewer), and recoverable (if your server dies, redeploy from the IaC files, not from someone's memory). For capstone projects, a `docker-compose.yml` plus environment-specific `.env` files is usually sufficient — resist the temptation to introduce Kubernetes for a prototype serving 3 users.

**Required Reading:**
- Chacon, S. & Straub, B. (2014). *Pro Git* (2nd ed.). Apress. Chapters 3 (branching), 5 (distributed workflows), 6 (GitHub).
- Humble, J. & Farley, D. (2010). *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*. Addison-Wesley. Chapters 1–4, 15.
- Forsgren, N., Humble, J., & Kim, G. (2018). *Accelerate: The Science of Lean Software and DevOps*. IT Revolution Press.
- Yggdrasil Forge CI Documentation (2040). *Capstone CI/CD Quickstart Guide*. 15-minute setup for React, FastAPI, Go, or Svelte stacks.
- Mímisdóttir, S. (2039). *Git for Teams: A Capstone Survival Guide*. Yggdrasil Technical Note YTN-2039-08.

**Discussion Questions:**
1. Your team's CI pipeline has been red for 4 days. No one has fixed it because "it's probably just a flaky test." What's the actual cost of this? What would you propose as a team policy?
2. A teammate pushes a commit directly to `main`, bypassing PR review. The commit introduces a bug. What's your response? What process change would prevent this from recurring?
3. Your capstone uses three external APIs (payment, AI inference, file storage). How would you configure your CD pipeline to handle API keys and secrets? What must *never* be committed to Git?

---

## Lecture 9: Technical Writing for Capstone Documentation

*"A deed unwitnessed fades. A saga unrecorded dies. Your code without documentation is a ghost — real to you, invisible to everyone else."*

Documentation is code's ambassador to the future — to your CS408 selves, to the teaching team evaluating your work, to anyone who might use, extend, or maintain your system. This lecture covers the specific documentation artifacts required for CS406 and the writing principles that make them effective.

The **Architecture Document** (due Week 8) is the most substantial CS406 writing deliverable. It must include: **Executive Summary** (1 page — what does the system do, for whom, and what makes it interesting?), **System Context** (Level 1 C4 diagram with explanation), **Container Architecture** (Level 2 C4 diagram, with each container described: technology, responsibilities, interfaces, data storage), **Component Architecture** (Level 3 for at least one container — the most architecturally interesting one), **Architecture Decision Records** (minimum 3 ADRs, following the format from Lecture 4), **Data Model** (entity-relationship diagram or document schema, with rationale for database choice), **Security Considerations** (authentication flow, authorization model, data protection, threat model summary), **Deployment Architecture** (how the system is deployed, including CI/CD pipeline), and **Risks and Mitigations** (what are the top 3 technical risks, and what's your plan for each?). The document should be 12–20 pages, professionally formatted, with diagrams (Mermaid markdown is acceptable and version-controllable), and written for an audience of technically literate peers (assume your reader has CS background but no prior knowledge of your project).

**Writing principles** for technical documentation: (1) **Be specific, not vague.** "The system uses a database" → "The system uses PostgreSQL 16 with the pgvector extension for semantic search." (2) **Explain the why, not just the what.** "We chose PostgreSQL because our data is highly relational (users, projects, documents with foreign-key relationships), and pgvector eliminates the need for a separate vector database." (3) **Use diagrams, but don't let them do all the work.** Every diagram must have a caption and at least one paragraph of prose explaining what the reader should notice. (4) **Be honest about limitations.** Acknowledging what your system doesn't do — "the current prototype does not handle concurrent edits; this is planned for CS408" — is a sign of maturity, not weakness. (5) **Write for skimming.** Use clear headings, bullet points for key information, and bold for emphasis. A reviewer should understand your architecture in 5 minutes of skimming, then dive into sections of interest.

The **Sprint Retrospective** (due Week 14) is a different genre: reflective, personal, analytical. It should answer: (1) What went well? (Be specific — "our CI/CD pipeline caught 12 bugs before they reached production" not "CI was helpful.") (2) What went poorly? (Be honest, but constructive — "we underestimated the learning curve for WebRTC, which delayed the real-time collaboration feature by 3 weeks" not "WebRTC is terrible.") (3) What will we do differently in CS408? (Concrete, actionable changes — "we will allocate one sprint to learning unfamiliar technologies before committing to them.") (4) Individual reflections from each team member (1 paragraph each — what did you learn? what would you do differently?). The retrospective is not graded on whether your project was successful; it's graded on whether you learned from it. A retrospective that says "everything went perfectly" when the prototype is barely functional is a failure of reflection, not of engineering.

**Required Reading:**
- Brown, S. (2018). *The C4 Model for Visualising Software Architecture*. The chapter on writing architecture descriptions.
- Clements, P., Bachmann, F., Bass, L., Garlan, D., Ivers, J., Little, R., Merson, P., Nord, R., & Stafford, J. (2010). *Documenting Software Architectures: Views and Beyond* (2nd ed.). Addison-Wesley. Chapters 1, 3, 9.
- Yggdrasil Capstone Office (2040). *Architecture Document Template and Annotated Example*. Includes a gold-standard capstone architecture doc from 2039.
- Yggdrasil Writing Center (2040). *Technical Writing Guide for Computer Science Capstones*. Covers common grammar issues, diagram best practices, and citation format.

**Discussion Questions:**
1. Read the executive summary of a classmate's architecture document (anonymized). Can you explain what their system does to someone else? If not, what's missing?
2. Your architecture document says "the system will scale to millions of users." Your prototype serves 3 concurrent users. Is this statement appropriate? How would you rephrase it honestly?
3. A student writes in their retrospective: "We failed because we chose the wrong framework." What's wrong with this analysis? How would you write a more insightful reflection on the same experience?

---

## Lecture 10: Mid-Project Review — Pivoting and Course Correction

*"The wise navigator does not curse the wind that blows her off course. She adjusts the sail and finds a new heading."*

By Week 7–8, your capstone is at a decision point. You've built enough to know what's working and what isn't. The mid-project review (MPR) is a structured checkpoint where you present your current state to the teaching team, receive candid feedback, and decide: stay the course, adjust scope, pivot the design, or — in rare cases — restart with a different project. This lecture prepares you for that conversation.

The **MPR presentation** (15 minutes + 10 minutes Q&A) should cover: (1) **Reminder of the vision** — what problem are you solving, for whom? (1 slide.) (2) **Current state** — demo the working prototype; show what's functional, not mockups. (2) **What's working** — technical wins, features that shipped, positive user feedback. (3) **What's not working** — technical blockers, features that were descoped, negative user feedback, team issues. This is the most important slide. Honesty here earns respect; spin earns skepticism. (4) **Revised plan** — based on what you've learned, what will you deliver by Week 14? What's deferring to CS408? (5) **Request for help** — what specific guidance, resources, or connections do you need from the teaching team?

**Types of course correction.** (1) **Scope adjustment**: the most common. You planned 8 features; by Week 7 you've built 3. You reduce the CS406 target to 5 features and defer the rest. This is normal and expected — almost every capstone adjusts scope at MPR. (2) **Design pivot**: user testing revealed that your core interaction model doesn't work. You keep the same problem and users but change the solution approach. This is a bigger change but often leads to a better outcome than stubbornly building the wrong thing. (3) **Technology pivot**: a chosen technology is not working out — too buggy, too slow, too hard to learn. You swap it for an alternative. The cost is high (possibly weeks of rework), but less than continuing with a broken foundation. (4) **Project restart**: extremely rare, requires teaching team approval. Only appropriate when the original problem was fundamentally misconceived or the team is completely dysfunctional. A restart resets the clock — you have the remaining weeks to deliver a new project, usually with reduced expectations.

**The psychology of pivoting** is hard. Teams get attached to their original vision. Admitting that something isn't working feels like failure. But in professional software development (and in startups especially), pivoting is a sign of intelligence, not weakness. The famous "pivot" in the Lean Startup methodology is precisely this: a structured course correction based on validated learning. The question to ask is not "are we failing?" but "are we learning fast enough to succeed?" If the answer is yes, even a messy mid-project state is recoverable. If the answer is no — if you're stuck making no progress and learning nothing — that's when an intervention is needed.

After the MPR, the team must produce a **revised project plan** within 48 hours, incorporating the feedback. This plan becomes the contract for the remainder of CS406. It should include: updated MoSCoW priorities, a sprint-by-sprint plan for Weeks 9–14, a risk register (top 5 risks with mitigation plans), and a clear statement of what constitutes "done" for CS406 (the minimum bar for a passing grade) versus "stretch" (what you hope to achieve). The teaching team signs off on the revised plan, and from that point forward, you are graded against *this* plan, not the original proposal. This is not lowering standards; it's acknowledging that plans made in ignorance (Week 1) are less reliable than plans made with evidence (Week 8).

**Required Reading:**
- Ries, E. (2011). *The Lean Startup*. Chapters 7–8 (on pivoting).
- Osterwalder, A. & Pigneur, Y. (2010). *Business Model Generation*. Wiley. The "Business Model Canvas" as a tool for visualizing pivots.
- Yggdrasil Capstone Office (2040). *MPR Rubric and Preparation Guide*. Includes the evaluation criteria and common feedback patterns.
- University of Yggdrasil (2039). *Pivot Case Studies: Five Capstone Projects That Changed Direction and Succeeded*. Internal document with anonymized project histories.

**Discussion Questions:**
1. Your team's MPR reveals that your core feature (a novel ML model) achieves only 62% accuracy, far below the 85% target. The model training was 60% of your effort. What kind of pivot would you propose, and what would you do with the remaining 6 weeks?
2. A teammate insists "we can still hit all our original goals if we just work harder." The evidence (velocity data, unfinished sprint tasks) suggests otherwise. How do you facilitate a realistic conversation without demoralizing the team?
3. What's the difference between a "pivot" (good) and "flailing" (bad)? How does a team know which they're doing?

---

## Lecture 11: Mentorship, Code Review, and Professional Feedback

*"Even the All-Father sought wisdom at Mímir's well. No smith forges alone."*

The capstone is the first time many students work on a project where no one knows the "right answer" in advance. This makes mentorship and feedback not just helpful but essential — they are your compass in ambiguous terrain. This lecture covers how to seek, receive, and give feedback in professional software contexts.

**Mentorship** in CS406 comes from multiple sources. Your **faculty advisor** (assigned in Week 1) meets with your team biweekly to discuss progress, unblock technical issues, and provide strategic guidance. They are not a project manager — they won't assign tasks or track your hours — but they are your most experienced resource. Use them. The teams that get the most from their advisor are the ones that come to meetings with specific questions ("we're considering these two authentication libraries — can you help us think through the trade-offs?") rather than general updates ("we're making progress"). Your advisor has seen dozens of capstone projects and can often spot risks you don't see — but only if you're transparent about your challenges.

**Code review** is the primary mechanism for technical feedback within the team. Effective code review is not about finding bugs (though that's a side benefit) — it's about knowledge sharing, design discussion, and maintaining a consistent codebase. A good code review: is timely (within 24 hours of PR submission — stale PRs block momentum), is focused (review for correctness, design, readability, and test coverage — not for personal style preferences), is specific ("this loop has O(n²) complexity because of the nested `includes` on line 47; could we use a Set instead?" vs. "this is slow"), is kind (frame suggestions as questions: "what do you think about extracting this function?" vs. "this should be a function"), and acknowledges what's good ("nice test coverage on the edge cases"). The PR author's responsibilities: keep PRs small (<400 lines — large PRs get superficial reviews), write clear PR descriptions (what, why, how tested, screenshots if UI), and respond to all comments (implement the change or explain why not — but never leave a comment unaddressed).

**Receiving feedback** is a skill that must be practiced. The natural human response to criticism is defensiveness — and that response kills learning. The counter-intuitive practice: when receiving feedback, your first job is to *understand*, not to *respond*. Listen fully. Ask clarifying questions. Summarize back what you heard ("so you're concerned that this design couples the payment logic too tightly to Stripe's API — is that right?"). Only then, after you've demonstrated understanding, do you engage with the substance. Separate the feedback from the delivery — even poorly delivered feedback may contain valid points. And remember: code review is about the code, not about you. "This function is too complex" is not "you are a bad programmer." The teams that thrive on code review are those where members trust each other's good intentions and share the goal of building something excellent.

**Giving feedback** requires equal skill. The SBI model (Situation-Behavior-Impact) provides structure: describe the specific Situation ("in yesterday's sprint planning..."), the observable Behavior ("...when you committed to the authentication feature but didn't break it into subtasks..."), and the Impact ("...the rest of the team couldn't see your progress, and we ended the sprint with an incomplete feature"). SBI keeps feedback concrete and depersonalized — it's about a specific action in a specific context, not about character. For positive feedback, be equally specific: "Your PR description with the architecture diagram was excellent — I understood the design intent in 2 minutes." Specific positive feedback teaches what to keep doing; vague positive feedback ("good job") teaches nothing.

**Required Reading:**
- Bacchelli, A. & Bird, C. (2013). "Expectations, Outcomes, and Challenges of Modern Code Review." *ICSE 2013*.
- Google Engineering Practices Documentation (2020). "How to Do a Code Review." [The standard reference for code review practices.]
- Stone, D. & Heen, S. (2014). *Thanks for the Feedback: The Science and Art of Receiving Feedback Well*. Viking. Chapters 1–5.
- Yggdrasil Capstone Office (2040). *Peer Evaluation Rubric for CS406*. Used for the confidential teammate evaluation at semester's end.
- Hlínardóttir, Á. (2038). *Mímir's Well: Mentorship and Feedback in Software Teams*. Yggdrasil Technical Note YTN-2038-11.

**Discussion Questions:**
1. You submit a PR that implements a complex feature. A teammate leaves a single comment: "LGTM" (looks good to me). Is this a good code review? What would a better review look like?
2. In a sprint retrospective, a teammate says they feel their contributions aren't being recognized. Using the SBI model, formulate a piece of positive feedback you could have given them during the sprint.
3. Your advisor suggests a completely different architectural approach than what your team has spent 4 weeks building. How do you evaluate this feedback without being defensive?

---

## Lecture 12: Capstone I Deliverables — Reporting, Demo, and Hand-off to CS408

*"The ship is built. Now it must face the sea — and the judgment of those who watch from the shore."*

The final weeks of CS406 are about landing the plane: completing the prototype, preparing the deliverables, delivering the final presentation, and setting up your CS408 self for success. This lecture walks through each component and the standards by which they're evaluated.

**Final deliverables checklist.** By the end of Week 14, your team must submit: (1) **Working prototype** deployed on the Capstone Cloud, accessible via a public URL, with test credentials for evaluators. The prototype must implement at least one complete user journey from end to end. (2) **Architecture Document** (final version, incorporating feedback from the mid-project review and advisor meetings). (3) **Sprint Retrospective** (team-level analysis of the semester, plus individual reflections from each member). (4) **CS408 Project Plan** — a detailed plan for the second semester, including: refined feature scope (MoSCoW), sprint schedule (14 weeks), technology stack (with rationale, acknowledging any planned changes), risk register, and a milestone-based grading proposal (what specific deliverables, at what quality level, correspond to what grade in CS408?). (5) **Demo video** — a 3-minute screen recording demonstrating the prototype's core features, narrated to explain what the viewer is seeing and why it matters. The video is for the teaching team and external reviewers; it must stand alone (assume the viewer hasn't read your documentation).

The **final presentation** (20 minutes + 10 minutes Q&A) is a public event — all CS406 teams present on the same day, with external reviewers from industry and academia invited. The presentation should tell a story: (1) The problem and why it matters (2 minutes), (2) What we built — live demo (6 minutes — the centerpiece), (3) How we built it — key architectural decisions and what we learned (5 minutes), (4) What's next — the CS408 plan (3 minutes), (5) Acknowledgments (1 minute). The live demo is the highest-risk, highest-reward element. Tips: rehearse the demo at least three times in the actual presentation venue; have a backup video of the demo in case of network failure; script the demo to show the most visually impressive and technically substantive features; and end with something memorable — the "wow" moment that makes reviewers remember your project.

**Grading in CS406** is holistic but roughly weighted: prototype quality and functionality (30%), architecture document (20%), sprint retrospective and team process (20%), CS408 plan (15%), final presentation (10%), and teammate peer evaluation (5% — individual component). The peer evaluation is confidential; each team member rates every other team member on contribution, communication, reliability, and technical quality. A teammate who coasted while others did the work will be reflected in their peer eval score. Conversely, a teammate who carried an outsized load should be recognized. The peer eval is not a popularity contest — it's a professional assessment, and you should be honest and fair.

**Hand-off to CS408.** The CS408 plan you write now becomes the starting point for your second semester. But there's a gap — the 2–4 month break between semesters. Mitigate the "what were we thinking?" problem by: (1) ensuring all code is well-documented (docstrings, README, architecture decision records), (2) recording a "project onboarding" video for your future selves (a 10-minute walkthrough of the codebase), (3) writing a "state of the project" document that honestly assesses what's working, what's broken, what's hacky, and what needs to be rewritten, (4) ensuring all credentials, API keys, and environment configurations are documented and accessible (but not committed to Git), and (5) scheduling a CS408 kickoff planning session before the semester break — even a 1-hour call makes a dramatic difference in CS408 momentum. The worst CS408 experiences are those where teams spend the first 3 weeks just figuring out what they built in CS406.

**Required Reading:**
- Yggdrasil Capstone Office (2040). *CS406 Final Deliverable Rubric*. Detailed grading criteria for each component.
- Yggdrasil Capstone Office (2040). *Demo Day Guidelines and Tips*. Includes technical setup instructions, backup plans, and advice from past presenters.
- Yggdrasil Capstone Office (2040). *CS408 Project Plan Template*. The standard format for the hand-off document.
- Rúnþjófr, E. (2039). *The Second Hammer-Blow: Preparing for CS408*. Yggdrasil Technical Report YTR-2039-14.

**Discussion Questions:**
1. Your prototype works well but the code is messy — lots of commented-out code, inconsistent naming, minimal tests. How honestly should your retrospective and CS408 plan address this? What specific actions should the CS408 plan include?
2. During the final demo, the live system crashes. You have a backup video. How do you handle this moment professionally? What do you say to the audience?
3. Your team has a member who contributed significantly less than others. The peer evaluation is anonymous. How do you rate them fairly while distinguishing between "contributed less" (effort issue) and "contributed less because they were struggling" (skill issue)?

---

## Final Examination Preparation

CS406 has no traditional final examination. The final deliverables (prototype, architecture document, retrospective, CS408 plan, demo video, and final presentation) constitute the summative assessment. However, the following reflection prompts are provided to help you prepare for the retrospective and the CS408 transition:

### Sample Reflection Prompts (address in your Sprint Retrospective):

1. **Technical reflection:** What was the hardest technical challenge your team faced, and how did you resolve it? If you could go back to Week 1 with the knowledge you have now, what would you do differently in your technology choices or architecture?

2. **Process reflection:** Analyze your team's development process. Did your sprint cadence work? Did code review happen consistently? Did CI/CD catch bugs? What one process change would have the biggest positive impact on CS408?

3. **Team reflection:** How did your team handle conflict, communication, and coordination? What team practices (standups, retrospectives, pair programming, documentation) were most valuable? If you could change one thing about how your team worked together, what would it be?

4. **Personal reflection:** What did you learn about yourself as an engineer this semester? What skill did you develop most? What skill gap did you discover that you want to address before CS408?

5. **Project reflection:** Is your project worth continuing? Has the prototype validated your core hypothesis? What is the single biggest risk to CS408 success, and what's your plan to address it?

6. **Ethical reflection:** Consider the broader implications of your project. Who benefits? Who might be harmed? What ethical considerations should guide the CS408 development? Address dual-use, bias, privacy, accessibility, and environmental impact as relevant.

7. **CS408 vision:** What does "done" look like at the end of CS408? Paint a concrete picture of the system you want to have built. What would make you proud to show it to a potential employer or graduate school?

8. **Lessons for the next cohort:** If you could give one piece of advice to next year's CS406 students, what would it be? Be specific, honest, and constructive.

---

*This course was woven at the University of Yggdrasil, 2040 — where the capstone is not the end of learning, but the beginning of building.*
