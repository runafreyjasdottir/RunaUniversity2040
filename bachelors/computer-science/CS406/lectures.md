# CS406: Capstone Project I — Design, Architecture, and Prototyping
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4
**Prerequisites:** CS301 (Algorithms), CS303 (Software Engineering), CS304 (Distributed Systems), CS405 (Research Methods in CS)
**Corequisite:** CS407 (Capstone Project II) taken in the following term
**Description:** The first half of the year-long capstone sequence. Students form teams, identify a significant computing problem, survey existing solutions, design a system architecture, and build a working prototype. Emphasis on the design process, trade-off analysis, team collaboration, and the translation of research findings into engineering decisions.

**Instructor:** Dr. Eiríkr Hafsteinn, D.Phil. (Oxon.), Professor of Computational Epistemology
**Project Mentor Pool:** Faculty from across the CS department, assigned by project domain
**Studio Sessions:** Tuesdays & Thursdays, 10:00–12:00, The Forge (Yggdrasil Hall, Level B1)

---

## Lectures

---

ᚠ **Lecture 1: The Capstone Vision — From Student to Practitioner**

**Course:** CS406 — Capstone Project I
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

The capstone is not another assignment — it is the bridge between your education and your career. In this lecture we establish the philosophical and practical foundations of the capstone experience: what distinguishes a capstone project from a coursework project, how to choose a problem worth spending a year on, and what success looks like — not just in grades but in the portfolio you'll carry into interviews, the open-source contributions you might make, and the intellectual confidence you'll build.

### Key Topics

- **What Makes a Capstone Different:** A coursework project has known solutions, specified constraints, and a single evaluator — your instructor. A capstone project has unknown solutions, negotiated constraints, and multiple stakeholders — your team, your mentor, your users, and ultimately the wider computing community. The capstone demands that you *define the problem*, not just solve it. It demands that you make trade-offs with incomplete information. It demands that you work in a team through disagreement, scheduling conflicts, and the inevitable moment when the architecture you designed in Week 3 proves inadequate in Week 10. These are not flaws in the educational design — they are the educational design. Professional practice is exactly this.
- **Choosing a Project — The Sweet Spot:** The best capstone projects live at the intersection of three circles: (1) *something you care about* (you'll spend ~400 hours on this — if you don't find it compelling, neither will anyone else); (2) *something technically challenging* (it should stretch your abilities — if you already know how to build it, it's not a capstone, it's practice); (3) *something demonstrably useful* (it should solve a real problem for real people, even if those people are a niche community). Avoid: projects that are "a better version of X" without a clear value proposition; projects whose primary challenge is administrative rather than technical; projects that depend on access you don't currently have (proprietary APIs that might change, datasets you haven't secured, hardware you haven't budgeted for).
- **The Capstone Portfolio — What Employers and Graduate Schools Actually Look For:** When a hiring manager asks about your capstone, they're not assessing whether you solved the problem — they're assessing *how you think about problems*. They want to hear: (1) you can articulate why the problem matters and who it affects; (2) you can explain your design choices with reference to alternatives you considered and rejected; (3) you can describe a technical challenge that genuinely stumped you, how you diagnosed it, and how you resolved it; (4) you can reflect on what you'd do differently with the benefit of hindsight. The capstone is your most substantial evidence that you can do the job — treat its documentation and presentation accordingly.
- **The Year-Long Arc:** CS406 (this term) covers inception through prototype: problem definition, requirements gathering, literature review, architecture design, technology selection, and an initial working prototype that demonstrates feasibility. CS407 (next term) covers production: implementation, testing, deployment, documentation, and final presentation. The relationship between the two is not sequential but iterative — prototyping in CS406 will reveal flaws in your CS406 architecture that you'll fix before CS407 implementation begins. This is normal and expected. The architecture document you submit at the end of CS406 is a *living document*, not a contract set in stone.
- **Team Formation and Dynamics:** Teams of 3–4, self-selected but with instructor approval to ensure balanced skill sets. The ideal team has complementary strengths: a systems thinker (architecture, infrastructure), a user advocate (requirements, interface, testing with real users), an algorithm specialist (the hard computational core), and an integrator (the person who makes everything work together, even when the pieces don't fit). The reality: you'll all need to do some of everything, and the hardest skill to learn isn't any technical one — it's *collaboration*. We'll cover team contracts, conflict resolution, and the agile rituals that keep teams aligned in Lecture 3.

### Required Reading

- Dawson, C.W. (2020). *Projects in Computing and Information Systems: A Student's Guide* (3rd ed.). Pearson. (Chapters 1–3)
- Pólya, G. (1945). *How to Solve It*. Princeton University Press. (Pages 1–30 — surprisingly relevant to system design)
- UoY Capstone Archive. (2035–2039). "Exemplary Capstone Projects: Annotated Collection." [Internal resource — review at least three projects from prior years]
- Hafsteinn, E. (2039). "What We Learned from 15 Years of Capstone Projects: Patterns of Success and Failure." *UoY Computing Education Research*, 2(1), 1–22.

### Discussion Questions

1. What's the difference between a capstone project and a startup idea? Should your capstone aim to be commercially viable, or is that the wrong metric?
2. You have three project ideas. One is technically fascinating but has no clear users. One solves a genuine problem but uses only straightforward CRUD technology. One is technically interesting and useful but requires access to a dataset you might not get. How do you decide?
3. In professional practice, you rarely get to choose your project — you're assigned to a team with a mandate. Is the freedom to choose your own capstone project a luxury, a burden, or a crucial educational experience?

---

ᚢ **Lecture 2: Problem Definition and Requirements Engineering**

**Course:** CS406 — Capstone Project I
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

The most expensive mistake in software engineering is building the wrong thing. This lecture covers the discipline of requirements engineering: how to identify stakeholders, elicit their actual (not stated) needs, distinguish functional from non-functional requirements, and write specifications that are precise enough to build from but flexible enough to survive discovery. We also cover the capstone-specific requirement: the *research requirement* — what your project must demonstrate beyond mere functionality.

### Key Topics

- **Stakeholder Identification and Analysis:** Who cares about this system, and what do they care about? Direct users (the people who will click the buttons), indirect users (the people who receive reports generated by the system), operational stakeholders (the people who will deploy and maintain it), and institutional stakeholders (the people who fund, approve, or regulate it). For each: what are their goals, what are their pain points with current solutions, what constraints do they impose, and how will you validate that you've met their needs? The "onion model" of stakeholders — start from the core (direct users) and work outward, but don't stop until you've identified everyone who could block or champion your project.
- **Elicitation Techniques:** Stakeholders don't know what they need — they know what frustrates them about what they currently have. Your job is to translate frustration into requirements. Techniques: semi-structured interviews (start broad: "walk me through a typical day using the current system"), contextual inquiry (watch them work, in their environment, and ask questions about what you observe), surveys (to reach more stakeholders — but only after initial interviews have generated good questions), and competitor analysis (what do existing solutions get right and wrong?). In 2040: AI-assisted requirements elicitation — tools that analyse recorded stakeholder conversations and suggest candidate requirements — but always with human verification.
- **Functional Requirements:** What the system *does*. "The system shall allow users to upload a dataset in CSV, JSON, or Parquet format." "The system shall generate a dependency graph for any Python project with more than 100 modules." Requirements should be specific, testable (how would you verify this requirement is met?), and prioritised (MoSCoW: Must have, Should have, Could have, Won't have this time). The capstone requirement: identify at least one *research-level functional requirement* — something your system must do that no existing system does, and that requires novel computational techniques to achieve.
- **Non-Functional Requirements:** How the system *is*. Performance (response time, throughput, startup time), scalability (how does performance degrade as data/users grow?), reliability (uptime, mean time between failures, recovery time objective), usability (learnability, efficiency, error rate, satisfaction — measured with SUS or equivalent), security (threat model, authentication, authorisation, data protection), maintainability (code quality standards, documentation, test coverage), and deployability (target platforms, installation process, dependencies). NFRs are often where capstone projects distinguish themselves — it's easy to build something that works on your laptop; it's harder to build something that works for 1,000 concurrent users on heterogeneous hardware.
- **The Requirements Document:** A living artefact, not a one-time deliverable. Structure: (1) Project vision — one paragraph that anyone can understand. (2) Stakeholder map. (3) Use cases or user stories (we recommend the "As a ___, I want to ___ so that ___" format, with acceptance criteria). (4) Functional requirements, prioritised. (5) Non-functional requirements, with measurable targets. (6) Domain model or glossary. (7) Assumptions and dependencies. (8) Open questions — things you know you don't know yet, with a plan for resolving them. Version the document; update it as you learn. The Week 12 version should be substantively different from the Week 2 version — and that's a sign of learning, not failure.

### Required Reading

- Wiegers, K. & Beatty, J. (2013). *Software Requirements* (3rd ed.). Microsoft Press. (Chapters 1–10)
- Robertson, S. & Robertson, J. (2012). *Mastering the Requirements Process* (3rd ed.). Addison-Wesley. (Chapters 1–5)
- Pohl, K. (2010). *Requirements Engineering: Fundamentals, Principles, and Techniques*. Springer. (Chapters on elicitation and specification)
- Nielsen, J. (2038). "Usability Engineering in the 2040s: Benchmarks for Modern Applications." *Nielsen Norman Group Research Report*.
- University of Yggdrasil Capstone Office. (2040). "CS406 Requirements Document Template and Exemplars."

### Discussion Questions

1. "Stakeholders don't know what they want until they see it." If this is true, what's the point of upfront requirements engineering? Defend your answer.
2. Choose a system you use daily (IDE, social media platform, version control tool). Reverse-engineer 5 functional and 5 non-functional requirements that you believe guided its design.
3. Your capstone team disagrees about whether a feature is "Must have" or "Should have." How do you resolve the disagreement?

### Practice Problems

- Conduct a 15-minute contextual inquiry with a fellow student about a task they find frustrating. Transcribe key observations and derive 3 functional requirements, 2 non-functional requirements, and 1 open question.
- Draft a one-page requirements document for your capstone idea. Exchange with another team for critique: are the requirements specific and testable?

---

ᚦ **Lecture 3: Team Collaboration — Agile Rituals, Tools, and Conflict Resolution**

**Course:** CS406 — Capstone Project I
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

The technical challenges of a capstone project are rarely what cause teams to fail. Teams fail because of broken communication, unclear expectations, unresolved conflict, and the slow erosion of trust that occurs when team members consistently fail to deliver on commitments. This lecture is practical: how to set up your team for success, establish working agreements, run effective meetings, choose collaboration tools, track progress transparently, and — when it inevitably happens — resolve conflict without destroying the team.

### Key Topics

- **The Team Charter:** Before you write a single line of code, write a team charter. This is a social contract, not a legal one, but it's the most important document your team will create. Elements: (1) *Team values:* what principles guide your work? (Examples: "We review all code before merging," "We don't work in silos — major decisions are discussed," "We respect each other's time and communicate absences early.") (2) *Roles and responsibilities:* who is the primary point of contact for what? (Not "who does all the work in that area" but "who ensures that area doesn't fall through the cracks.") (3) *Communication norms:* what channels for what purposes? When is it acceptable to message someone outside agreed working hours? (4) *Decision-making process:* how are technical disagreements resolved? (We recommend: discuss → prototype both approaches if feasible → use data, not ego → if still deadlocked, escalate to mentor.) (5) *Meeting cadence:* daily standup (15 min max), weekly planning/review, ad-hoc design sessions. (6) *Conflict resolution protocol:* what happens when someone isn't pulling their weight, or when two people fundamentally disagree?
- **Agile for Capstone Teams:** You don't have a product manager, a scrum master, and a dedicated QA team — you have 3–4 peers and a mentor. Adapt agile accordingly. We recommend a lightweight Kanban or Scrum-ban approach: a board with columns (Backlog, Ready, In Progress, In Review, Done), work items sized to approximately 1–3 days, a weekly planning session where you pull items from the backlog, daily 15-minute standups (what did you do yesterday, what will you do today, what's blocking you?), and a weekly retrospective (what went well, what didn't, what will we change?). Sprints of 1–2 weeks. The key: the board must reflect reality. If a task is "In Progress" for two weeks without movement, that's a signal — not a reason to shame anyone, but a reason to ask "is this task too large? Is there a hidden dependency? Does someone need help?"
- **Collaboration Tools in 2040:** Git (with a branching strategy — we recommend trunk-based development with short-lived feature branches and PR-based code review). Project management: Linear, Notion, GitHub Projects, or the UoY Capstone Portal. Communication: a team chat platform (Discord, Slack, or Matrix) with channels for different purposes. Documentation: a shared wiki or Markdown repository (treat docs as code — version, review, and update them). Pair programming: live-share tools (VS Code Live Share, JetBrains Code With Me, Tuple) for remote collaboration. CI/CD: GitHub Actions, GitLab CI, or Jenkins for automated testing, linting, and deployment.
- **Conflict — Types, Causes, and Responses:** Task conflict (disagreement about what to do) can be productive if managed well — it surfaces assumptions and improves decisions. Relationship conflict (disagreement rooted in personal friction) is almost always destructive. Process conflict (disagreement about how to work) falls between — it can improve efficiency or degenerate into blame. The Thomas-Kilmann conflict modes: competing (I win, you lose), accommodating (you win, I lose), avoiding (nobody wins, everybody loses), compromising (we both lose a bit), and collaborating (we find a solution that satisfies both our core concerns). Collaboration is the ideal but is time-intensive — sometimes compromising is the pragmatic choice. Steps for resolving capstone conflicts: (1) acknowledge the conflict directly and privately, (2) each person states their perspective without interruption, (3) identify the underlying interests (not positions), (4) brainstorm solutions, (5) agree on a course of action with a timeline for review, (6) if unresolved, involve the mentor.
- **Giving and Receiving Feedback:** Code review is feedback about code. Team retrospectives are feedback about process. Both require the same skills: be specific ("the `UserAuth` module doesn't handle token expiry" not "your code is sloppy"), be timely (feedback a month later is useless), focus on the work not the person, and assume good intent. As the receiver: listen, don't defend immediately; ask clarifying questions; separate the feedback from your emotional reaction; and thank the giver — even if you disagree, they've given you information you didn't have before. The "Radical Candor" framework (Scott, 2017): care personally AND challenge directly. The other three quadrants — ruinous empathy (care without challenging), obnoxious aggression (challenge without caring), and manipulative insincerity (neither) — are all traps.

### Required Reading

- Beck, K. et al. (2001). *Manifesto for Agile Software Development*. [agilemanifesto.org]
- Derby, E. & Larsen, D. (2006). *Agile Retrospectives: Making Good Teams Great*. Pragmatic Bookshelf.
- Scott, K. (2017). *Radical Candor: Be a Kick-Ass Boss Without Losing Your Humanity*. St. Martin's Press. (Chapters 1–4 on feedback)
- West, M.A. (2012). *Effective Teamwork: Practical Lessons from Organizational Research* (3rd ed.). Wiley-Blackwell. (Chapters on conflict and decision-making)
- Hafsteinn, E. (2039). "The Capstone Post-Mortem Database: What 200 Teams Taught Us About Why Teams Fail." *UoY Technical Report* TR-2039-04.

### Discussion Questions

1. Your team member consistently delivers code that works but is poorly documented and hard for others to maintain. How do you give this feedback constructively?
2. Is the "daily standup" genuinely useful for a 3-person capstone team, or is it cargo-cult process? What's the minimum viable meeting structure?
3. You and a teammate have a fundamental disagreement about technology choice (e.g., React vs. Svelte for the frontend). Both options are defensible. How do you break the deadlock?

### Practice Problems

- With your capstone team, draft a team charter covering all six elements above. Submit it and revisit it at the Week 6 and Week 12 retrospectives — what changed?
- Role-play a conflict scenario: one team member has missed three deadlines in a row. Practice giving feedback using the SBI model (Situation, Behaviour, Impact).

---

ᚨ **Lecture 4: Literature Review for Capstone — Finding Your Project's Intellectual Foundation**

**Course:** CS406 — Capstone Project I
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Your capstone doesn't exist in a vacuum. Somewhere, someone has tried to solve a related problem, published a relevant algorithm, built a system with similar constraints, or written a critique that will save you months of heading down the wrong path. The literature review for a capstone project is not an academic exercise — it's competitive intelligence. It tells you what's been tried, what worked, what didn't, and — most importantly — where the genuine gap is that your project can fill.

### Key Topics

- **The Purpose of the Capstone Literature Review:** Different from a thesis literature review in scope and depth, but similar in rigour. Your goals: (1) demonstrate that your project addresses a real, unsolved (or inadequately solved) problem; (2) identify existing tools, libraries, and datasets you can build upon rather than rebuilding; (3) learn from others' mistakes — if three papers tried approach X and concluded it doesn't scale, you'd better have a good reason to try approach X again; (4) establish the intellectual context that makes your design decisions legible to reviewers. A capstone that ignores prior work and "starts from scratch" is not impressive — it's naive.
- **Search Strategy:** Where to look: ACM Digital Library, IEEE Xplore, arXiv (cs.* categories), DBLP (for author/topic tracing), Google Scholar (for forward citation tracking — who cited the key paper, and what did they say?), and GitHub (for implementations, not just papers). Search terms: combine your problem domain with your technical approach ("distributed consensus" + "edge computing", "program synthesis" + "type systems"). Snowballing: start with 3–5 high-quality papers, follow their references backward (who did they cite?) and forward (who cited them?). The UoY Huginn Research Raven can accelerate this, but always verify AI-generated summaries against primary sources.
- **Evaluating Sources:** Not all papers are equal. A paper in *Communications of the ACM*, *ACM Transactions on...*, *IEEE Transactions on...*, or a top conference (NeurIPS, ICML, SOSP, PLDI, CHI, etc.) has passed rigorous peer review. A preprint on arXiv has not — it may be ground-breaking, or it may be wrong, or it may be both. An industry white paper may contain valuable practical wisdom or may be marketing. Evaluate: who wrote it (are they established in this field?), where was it published (peer-reviewed venue or self-published?), when was it written (is it still current?), what evidence does it provide (theoretical proof, empirical benchmarks, user studies, or just assertions?), and what do other papers say about it (has it been cited approvingly, critically, or not at all?).
- **The Literature Review Document:** 8–12 pages, structured: (1) Problem context — what is the problem, and why does it matter? (2) Scope — what literature did you include and exclude, and why? (3) Thematic synthesis — organise papers by approach, not chronologically. "Approaches to distributed consensus fall into three categories: leader-based (Paxos, Raft, Zab), leaderless (EPaxos, Gryff, Accord), and quorum-based (NOPaxos, CURP)." For each category: what's the core idea, what are its strengths, what are its limitations, and what open problems remain? (4) Gap analysis — synthesise findings into a specific, defensible statement of where your project fits. "While leader-based consensus protocols provide strong consistency guarantees, no existing protocol simultaneously achieves (a) sub-millisecond latency in single-region deployments, (b) graceful degradation under network partitions, and (c) compatibility with heterogeneous hardware accelerators. Our capstone, YggdrasilDB, addresses this gap by..." (5) Tools and datasets survey — what can you reuse?
- **Writing the Review:** Use a reference manager (Zotero, Paperpile, or the UoY academic toolchain). Cite as you write — don't leave references "for later." Use direct quotes sparingly; paraphrase and cite instead. Be critical, not dismissive — "Smith et al. (2037) achieved 94% accuracy on benchmark X, but their evaluation used a dataset that has since been shown to contain significant label noise (Jones, 2039)" is better than "Smith et al. (2037) is bad." Your literature review will be part of your final CS407 thesis — write it to that standard now and you'll save yourself weeks later.

### Required Reading

- Fink, A. (2019). *Conducting Research Literature Reviews: From the Internet to Paper* (5th ed.). SAGE. (Chapters 1–4)
- Keshav, S. (2007). "How to Read a Paper." *ACM SIGCOMM Computer Communication Review*, 37(3), 83–84. (The three-pass method — still relevant in 2040)
- University of Yggdrasil Library. (2040). "CS Literature Search Guide." [Updated termly]
- Review the literature review sections of 3 exemplary capstone theses from the UoY Capstone Archive.

### Discussion Questions

1. How do you know when you've read enough? What's the signal that your literature review is "complete"?
2. You find a 2038 paper that describes exactly your project idea. Is this a disaster, an opportunity, or both?
3. How should capstone teams handle the fact that some of the most relevant "literature" is actually open-source code on GitHub rather than formal publications?

### Practice Problems

- For your capstone topic, conduct a systematic search across ACM DL and arXiv, identify 10–15 relevant papers, and write a one-page gap analysis.
- Take a key paper in your area and apply Keshav's three-pass method. Write a 200-word critical summary.

---

ᚱ **Lecture 5: System Architecture — The Bones of Your Design**

**Course:** CS406 — Capstone Project I
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Architecture is the set of design decisions that are hardest to change later. It's not the same as design (which covers lower-level structures), and it's not the same as infrastructure (which is about deployment and operations). This lecture covers architectural thinking: how to decompose a system into components, define their interfaces, and make the trade-offs — performance vs. maintainability, consistency vs. availability, simplicity vs. feature-richness — that will shape everything that follows.

### Key Topics

- **What Architecture Is (and Isn't):** Architecture answers the question "what are the parts, and how do they communicate?" More formally: the set of principal design decisions about a system, including the structure (components and connectors), the behaviour (how components interact at runtime), and the rationale (why these choices, and what alternatives were rejected). Architecture is not about code structure (that's design) or about servers and containers (that's deployment). It's about the high-level organisation that constrains everything else. "Architectural decisions are those that, if you get them wrong, will cause you to rewrite significant portions of the system."
- **Architectural Patterns:** The catalogue of proven solutions to recurring architectural problems. *Layered architecture* (presentation → business logic → data access): simple, widely understood, but can become rigid. *Microservices* (independent services communicating over the network): scalability, independent deployability, but operational complexity and network latency. *Event-driven architecture* (components communicate via events): loose coupling, responsiveness, but harder to reason about and debug. *Pipe-and-filter* (data flows through sequential transformations): natural for data processing pipelines. *Model-View-Controller* (and its descendants MVVM, MVP, MVI): the dominant pattern for interactive applications. *Hexagonal architecture* (ports and adapters): the business logic at the centre, everything else as pluggable adapters — excellent for testability and flexibility. For capstones: choose the simplest pattern that meets your non-functional requirements. Most capstone projects don't need microservices.
- **Architectural Decision Records (ADRs):** A lightweight practice with outsized value. For every significant architectural decision, create a short document (1–2 pages) recording: (1) *Title:* a short noun phrase ("ADR-001: Use PostgreSQL for persistent storage"). (2) *Status:* proposed, accepted, deprecated, or superseded. (3) *Context:* what is the issue we're addressing? (4) *Decision:* what did we decide? (5) *Consequences:* what becomes easier, what becomes harder, what are the risks? (6) *Alternatives considered:* what else did we evaluate, and why was it rejected? ADRs create an audit trail of your architectural reasoning. When a future teammate (or your future self) asks "why did we use PostgreSQL instead of MongoDB?", the answer is in ADR-001, not lost in a Slack thread from six months ago. For capstone: aim for 8–15 ADRs by end of CS406.
- **The Architecture Document:** The capstone architecture document describes your system's high-level design. Structure: (1) System overview — a "4+1 view" (Kruchten, 1995) adapted for capstones: *logical view* (major components and their responsibilities), *process view* (concurrency, communication, state management), *development view* (module organisation, package structure), *physical view* (deployment topology, even if it starts as "developer laptop"), and *scenarios* (how key use cases trace through the architecture). (2) Technology stack, with justification. (3) Key interfaces (APIs, data formats, protocols). (4) Data model (entities, relationships, storage strategy). (5) Cross-cutting concerns (authentication, logging, error handling, configuration). (6) Architectural decisions (the ADRs, summarised). The document should be comprehensible to a new team member joining in Week 10 — if it isn't, it's incomplete.
- **Trade-Off Analysis:** Every architectural decision involves trade-offs. The "ilities": scalability, availability, reliability, performance, security, maintainability, testability, deployability, usability, and so on. You cannot maximise all of them simultaneously. The CAP theorem is the canonical example: in a distributed data store, you can have Consistency (all nodes see the same data at the same time) or Availability (every request receives a response) under network Partition — but not both simultaneously. Similar tensions exist throughout architecture: abstraction vs. performance (layers add overhead), flexibility vs. simplicity (configuration options increase complexity), security vs. usability (authentication adds friction). Document your trade-offs explicitly: "We chose X over Y because ___, accepting the cost of ___." This demonstrates architectural maturity far more than "we used the latest trendy framework."
- **Architecture in the Age of AI-Assisted Development:** By 2040, AI tools (Copilot X, Codex, Devin, and the UoY's own Mímir Assistant) can generate significant amounts of code from natural language descriptions. This shifts the architect's role: less time writing boilerplate, more time thinking about the structures that AI-generated code must fit within. An AI can generate a React component; it cannot decide whether your system should be event-driven or request-response. Architecture remains a fundamentally human activity because it requires making value judgments about uncertain futures. Use AI to accelerate implementation; don't use it to think for you.

### Required Reading

- Bass, L., Clements, P., & Kazman, R. (2013). *Software Architecture in Practice* (3rd ed.). Addison-Wesley. (Chapters 1–5, 15)
- Richards, M. & Ford, N. (2020). *Fundamentals of Software Architecture*. O'Reilly. (Chapters 1–8, 21 on ADRs)
- Kruchten, P. (1995). "Architectural Blueprints — The '4+1' View Model of Software Architecture." *IEEE Software*, 12(6), 42–50.
- Nygard, M. (2039). "Architecture Decision Records in the Age of AI: A 2040 Practitioner's Guide." *ThoughtWorks Technology Radar*.
- Review the architecture documents of 2 exemplary capstone projects from the UoY Capstone Archive.

### Discussion Questions

1. "Microservices" is often the default architectural choice in industry. For a capstone project with a 3-person team and a 6-month timeline, when (if ever) is microservices the right choice?
2. How do you decide when a decision warrants an ADR? What's the threshold of significance?
3. How should architecture documentation change when AI tools are generating significant portions of the codebase?

### Practice Problems

- For a system of your choice (your capstone idea, or a well-known system like GitHub or Spotify), draw the logical view: identify 5–8 major components, their responsibilities, and their interfaces.
- Write an ADR for a technology decision your team has already made (language, framework, database). Include context, decision, consequences, and at least two alternatives considered and rejected.

---

ᚲ **Lecture 6: Technology Selection — Choosing Your Stack with Intention**

**Course:** CS406 — Capstone Project I
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

"Which language/framework/database should we use?" is simultaneously the most asked and most poorly answered question in student projects. The default answer — "whatever I already know" — is sometimes right but rarely examined. This lecture provides a framework for technology evaluation: how to identify the requirements that should drive technology choice, how to evaluate options against those requirements, and how to avoid the twin traps of resume-driven development (choosing technologies to impress employers) and novelty-chasing (choosing the newest thing regardless of maturity).

### Key Topics

- **The Technology Selection Framework:** (1) Identify the *architecturally significant requirements* — not every requirement influences technology choice. The ones that do: performance characteristics (latency targets, throughput requirements), data model complexity, concurrency model, deployment constraints, team expertise, ecosystem maturity, and long-term maintenance expectations. (2) Weight these requirements — is performance more important than developer productivity? Is ecosystem maturity more important than cutting-edge features? (3) Identify candidate technologies — typically 3–5 options per major decision (language, framework, database, deployment platform). (4) Evaluate each candidate against each requirement, using evidence (benchmarks, case studies, community metrics) not opinion. (5) Make a decision and document it as an ADR. (6) Spike/prototype the riskiest technology choice to validate it before committing.
- **Programming Language Choice:** By Year 4 of a CS degree, you know several languages. Criteria for capstone selection: problem domain fit (Python for data/ML, Rust/Go for systems, TypeScript/JavaScript for web, C++ for performance-critical, Kotlin/Swift for mobile), ecosystem (libraries, tooling, community), team expertise (a language you all know but is suboptimal often beats a theoretically better language only one team member knows), and learning goals (it's legitimate to choose a language you want to learn — but be honest about the productivity cost). The 2040 landscape: Rust has matured into a mainstream systems language; TypeScript dominates web development; Python remains the lingua franca of AI/ML; Go is strong in cloud infrastructure; Zig, Mojo, and Jakt are emerging. The safe bet: use what lets you build fastest, unless performance constraints demand otherwise.
- **Database Choice:** The question is not "SQL or NoSQL?" — that's the wrong framing. The question is: what is your data shaped like, and what access patterns do you need? Relational databases (PostgreSQL, SQLite, MySQL) excel when data is structured, relationships are important, and you need ACID transactions. Document databases (MongoDB, CouchDB) work well for semi-structured data with varying schemas. Key-value stores (Redis, DynamoDB) for simple lookups at high speed. Graph databases (Neo4j, Dgraph) when relationships are the primary query pattern. Time-series databases (InfluxDB, TimescaleDB) for temporal data. For most capstones: start with PostgreSQL. It handles relational, JSON, full-text search, and (via extensions) time-series and geospatial data. You can always add specialised stores later — but you probably won't need to.
- **Frontend vs. Backend vs. Full-Stack Frameworks:** If your project has a user interface, you need to decide: server-rendered (Django, Rails, Phoenix LiveView, Laravel) or client-rendered (React, Svelte, Vue, Solid)? Server-rendered is simpler to develop and deploy, works without JavaScript (accessibility), and is often sufficient. Client-rendered provides richer interactivity, feels more like a native application, and separates frontend and backend concerns cleanly. The 2040 middle ground: meta-frameworks like Next.js, SvelteKit, and Remix that offer server-side rendering with client-side hydration. For capstones: if your interface is primarily forms and data display, server-rendered is fine. If it involves real-time collaboration, complex visualisations, or offline capability, client-rendered with an API backend is appropriate.
- **Deployment Platform:** Where will your capstone run during development? Where will it run for the final demonstration? Options: local development (everyone's laptop — simplest, but "it works on my machine" syndrome), Docker Compose (consistent environment across team members, simulates production topology), cloud platforms (AWS Free Tier, Google Cloud, Azure for Students, or the UoY Research Cloud — good for demonstrating scalability), edge deployment (for IoT/mobile capstones, deploying to Raspberry Pi or similar). Principle: your development environment should resemble your demonstration environment as closely as possible. If you're developing on MacBooks and demonstrating on a Linux server, you will discover environment-specific bugs at the worst possible time. Containerise from Week 1.

### Required Reading

- Seibel, P. (2009). *Coders at Work: Reflections on the Craft of Programming*. Apress. (Interviews on language choice and decision-making)
- Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly. (Chapters 1–3 on data models and storage)
- ThoughtWorks. (2040). *Technology Radar, Vol. 42*. [Published quarterly — review the current edition for technology assessments]
- UoY Capstone Archive. (2038–2040). "Technology Stack Survey: What 100 Capstone Teams Used and What They'd Do Differently."

### Discussion Questions

1. "Use boring technology" (Dan McKinley, 2015). Does this principle apply to capstone projects, or should capstones embrace novelty?
2. Your team wants to use Rust because "it's the future." Only one team member knows Rust well. The project involves a web backend. What's your recommendation and why?
3. How should the fact that your capstone will be evaluated by faculty (who may not know your chosen stack) influence your technology decisions?

### Practice Problems

- For your capstone idea, apply the technology selection framework to at least one major technology choice (language, framework, or database). Document your evaluation as an ADR.
- Research a technology stack from a successful open-source project in your domain. What did they choose, and why? What would you choose differently?

---

ᚷ **Lecture 7: Prototyping — From Whiteboard to Working Software**

**Course:** CS406 — Capstone Project I
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

The prototype is the proof that your architecture isn't just a pretty diagram. This lecture covers the prototyping phase: how to scope an initial prototype that demonstrates feasibility without attempting to build the entire system, how to structure your code for the inevitable refactoring, and how to use the prototype to validate (or invalidate) your architectural assumptions before you're too invested to change course.

### Key Topics

- **What a Prototype Is (and Isn't):** A prototype is a working subset of your system that demonstrates a critical path through your architecture. It is not a half-finished product — it's a complete vertical slice that proves the architecture can support the most technically risky aspect of your project. Characteristics: (1) It works — you can demonstrate it end-to-end, even if only for a narrowly defined scenario. (2) It exercises the most architecturally significant components — if your architecture includes real-time WebSocket communication, your prototype must include it. (3) It reveals the unknown unknowns — the things your architecture diagram didn't capture, like the impedance mismatch between your chosen ORM and your actual query patterns, or the fact that your event bus has 200ms of latency that breaks your user experience assumptions. (4) It is not a product — prototype code may be discarded or heavily refactored. This is by design.
- **Scoping the Prototype — The Tracer Bullet:** Hunt and Thomas's metaphor: a tracer bullet illuminates the path from trigger to target. In software: implement a single, narrow feature end-to-end, through every layer of your architecture, to prove that the layers connect correctly. For a data visualisation capstone: implement exactly one chart type, connected to exactly one data source, rendered in the browser via exactly one API endpoint. If all the layers work for this narrow case, they'll work for the broader case (with appropriate scaling work, but the architectural risk is addressed). The alternative — building all the UI components first, then all the API endpoints, then the database, then trying to connect them — is how prototypes fail.
- **Code Structure for Prototyping:** Write prototype code as if you'll keep it, because sometimes you will. Principles: (1) Separate the "happy path" from the edge cases — implement the core logic cleanly, and use comments or TODO markers for missing error handling, input validation, and corner cases. This makes it clear what's intentionally incomplete vs. what's buggy. (2) Use dependency injection from the start — swapping a mock database for a real one should require changing configuration, not rewriting classes. (3) Write tests for the things that would be catastrophic if they broke, even in prototype phase — authentication, data integrity, payment processing. (4) Document what the prototype doesn't do — maintain a "known limitations" section in your README that grows as you discover gaps. This prevents team members from wasting time debugging behaviour that was never implemented.
- **Prototyping Tools and Techniques:** By 2040, the prototyping toolkit is rich. (1) Low-fidelity: paper prototypes, wireframes (Figma, Penpot, Excalidraw), user flow diagrams — quick to create, quick to discard. (2) Medium-fidelity: interactive mockups without real backend (Figma prototypes, Framer, or HTML/CSS with hardcoded data). (3) High-fidelity: working code with simplified functionality. (4) API mocking: tools like MSW (Mock Service Worker), json-server, or the UoY's own MockRaven system for simulating backend services. (5) AI-assisted prototyping: tools like v0, Bolt, or Claude Artifacts that generate UI from descriptions — use them for inspiration and rapid iteration, but don't submit generated code you don't understand. The line: using AI to generate a starting point that you then modify and understand is fine; submitting AI output without comprehension is academic dishonesty.
- **Prototype Evaluation — Go/No-Go:** The prototype phase ends with a formal evaluation. Does the prototype demonstrate that the architecture is viable? Specific criteria: (1) The tracer bullet works end-to-end. (2) The architecturally significant components function correctly (even if not optimally). (3) The technology choices have been validated — the database can handle the query patterns, the framework doesn't have a showstopping limitation, the deployment target is reachable. (4) The team understands the architecture well enough to estimate remaining effort. If the prototype reveals that the architecture is fundamentally wrong — the database can't support the required query patterns, the real-time framework has unacceptable latency, the chosen language lacks critical libraries — this is a *successful prototype outcome*. Discovering this in CS406 Week 8 is infinitely better than discovering it in CS407 Week 3. Go/no-go decision: continue with current architecture, pivot to a revised architecture, or (rarely) restart with a different problem entirely.

### Required Reading

- Hunt, A. & Thomas, D. (2019). *The Pragmatic Programmer* (20th Anniversary Edition). Addison-Wesley. (Chapter on "Tracer Bullets" and "Prototypes and Post-it Notes")
- Nielsen, J. (1993). *Usability Engineering*. Academic Press. (Chapters on prototyping and iterative design — principles that survive technology changes)
- Hartson, R. & Pyla, P. (2019). *The UX Book: Agile UX Design for a Quality User Experience* (2nd ed.). Morgan Kaufmann. (Chapters on prototyping techniques)
- Ries, E. (2011). *The Lean Startup*. Crown Business. (The Build-Measure-Learn loop — adapted for capstone projects)
- UoY Capstone Archive. (2040). "Prototype Exemplars: What a Good CS406 Prototype Looks Like." [Annotated examples with mentor commentary]

### Discussion Questions

1. How do you know when your prototype is "done enough" to move on to full implementation? What's the risk of over-investing in a prototype?
2. Your prototype reveals that your chosen database can't handle your query patterns at scale. The team is divided: half want to switch databases, half want to "just make it work." How do you decide?
3. Is it ethical to use AI-generated code in your capstone prototype? Where is the line between legitimate tool use and academic dishonesty?

### Practice Problems

- Identify the single riskiest architectural assumption in your capstone design. Design a minimal prototype (a tracer bullet) that would validate or invalidate that assumption within one week.
- Build a paper prototype or wireframe for the most complex user interaction in your system. Test it with one potential user (not on your team). What did you learn?

---

ᚹ **Lecture 8: User Interface and User Experience Design — Making Your System Usable**

**Course:** CS406 — Capstone Project I
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

A system that works but can't be used might as well not work. This lecture introduces user-centred design: how to understand your users, design interfaces that match their mental models, and evaluate your designs empirically — not by asking "do you like it?" but by watching people use it and measuring where they succeed and where they fail.

### Key Topics

- **User Research for Capstones:** Who are your actual users, and what do they actually need? Personas: not demographic stereotypes but behavioural archetypes based on real observations. "Alex is a graduate student who analyses large environmental datasets. She's comfortable with Python but not with SQL. She needs to explore data visually before deciding which statistical tests to run." Scenarios: stories of use in context. "It's 11pm. Alex has a grant deadline tomorrow. She needs to quickly identify outliers in a new dataset and generate a summary report." Task analysis: break down what users actually do into steps, and identify where current tools fail them. This is not speculative — talk to at least three potential users before designing your interface.
- **Interaction Design Principles:** (1) Visibility: make the system state and available actions obvious. If a user has to remember what state the system is in, the design has failed. (2) Feedback: every action should produce an immediate, perceivable response. If a computation takes more than 0.1 seconds, show a progress indicator. (3) Constraints: prevent errors by design. A date picker is better than a free-text date field. (4) Consistency: similar things should look and behave similarly. If clicking a row opens a detail view in one part of your application, it should do the same everywhere. (5) Affordance: a button should look clickable; a text field should look editable. (6) Error prevention and recovery: the best error is one that can't happen. The second best is one that the system fixes automatically. The third best is an error message that tells the user what happened, why, and what to do about it — in plain language, not a stack trace.
- **Design Systems and Component Libraries:** Don't design every button from scratch. By 2040, mature design systems exist: Material Design (Google), Fluent (Microsoft), Ant Design, shadcn/ui, Radix UI. Choose one and use it consistently. Benefits: (1) faster development — you're composing, not inventing; (2) built-in accessibility — these systems have been tested with screen readers, keyboard navigation, and WCAG compliance; (3) visual coherence — your application looks professional, not like a collage of different styles. The trade-off: your application will look like other applications built with the same system. For a capstone, this is almost always the right trade-off.
- **Accessibility:** Not optional, not an afterthought. At minimum: (1) all interactive elements are keyboard-navigable (tab order, focus indicators); (2) all images have meaningful alt text; (3) colour is not the only way to convey information (use patterns, labels, or icons as well); (4) text has sufficient contrast ratio (WCAG AA: 4.5:1 for normal text, 3:1 for large text); (5) forms have properly associated labels; (6) the page has a logical heading structure; (7) dynamic content changes are announced to screen readers (ARIA live regions). Tools: axe DevTools, Lighthouse accessibility audit, WAVE. If you don't know whether your interface is accessible, it isn't. Test with a screen reader at least once — the experience of navigating your own interface without sight is humbling and educational.
- **Usability Testing:** Not the same as "showing someone your app and asking if they like it." A usability test has: (1) a specific task ("find the average temperature for Reykjavík in July 2039 and export it as a CSV"), (2) observation (watch what they do, don't guide them), (3) measurement (did they complete the task? how long did it take? how many errors?), and (4) a post-task debrief (what was confusing?). You don't need a lab — test with 3–5 representative users (not your teammates), using a prototype or early build. Nielsen's insight from 2000: 5 users will find ~85% of usability problems. Testing with 3 users, fixing the problems they reveal, then testing with 3 more is more effective than testing with 10 users once.

### Required Reading

- Norman, D. (2013). *The Design of Everyday Things* (Revised ed.). Basic Books. (Chapters 1–4)
- Krug, S. (2014). *Don't Make Me Think, Revisited: A Common Sense Approach to Web Usability*. New Riders.
- Nielsen, J. (2000). "Why You Only Need to Test with 5 Users." *Nielsen Norman Group*. [Article — foundational and still correct]
- W3C. (2038). *Web Content Accessibility Guidelines (WCAG) 3.0*. [Working draft — review the core principles]
- UoY Digital Accessibility Office. (2040). "Accessibility Checklist for Student Projects."

### Discussion Questions

1. "The user is not like me." Why is this the hardest lesson for CS students to internalise, and what specific practices help overcome it?
2. Is it better to design for mobile first (because mobile is constrained and forces prioritisation) or desktop first (because your capstone's primary users are on desktop)?
3. Your usability test reveals that users consistently misunderstand a core interaction in your application. Fixing it requires significant architectural changes. What do you do?

### Practice Problems

- Conduct a heuristic evaluation of an existing application in your domain using Nielsen's 10 usability heuristics. Document at least 5 violations with severity ratings.
- Design and run a usability test with 3 participants for a prototype (yours or a public application). Report findings with specific, actionable recommendations.

---

ᚺ **Lecture 9: Testing Strategy — Quality Assurance from Day One**

**Course:** CS406 — Capstone Project I
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Testing is not something you do after the code is written — it's an integral part of development that shapes your design, documents your assumptions, and provides the safety net that enables refactoring. This lecture covers testing strategy for capstone projects: what to test, how to test it, when to write the tests, and how to integrate testing into your team's workflow so that it accelerates rather than impedes development.

### Key Topics

- **The Testing Pyramid:** Mike Cohn's model, still valid in 2040: many unit tests (fast, isolated, testing individual functions and classes), fewer integration tests (testing how components work together, including database and network interactions), and few end-to-end tests (testing complete user journeys through the full system). The capstone adaptation: write unit tests for your algorithmic core (the code that would be hardest to debug by inspection), integration tests for your API and database access (the code where "it works on my machine" most often fails), and at least 3–5 end-to-end tests for your critical user journeys (the paths that, if broken, make your system unusable). Testing is risk management: test more where failures are more catastrophic or harder to detect.
- **Unit Testing:** Testing individual functions, methods, or classes in isolation. Principles: (1) test one thing per test; (2) name tests descriptively — `test_parse_datetime_rejects_missing_timezone()` not `test_parse_3()`; (3) follow Arrange-Act-Assert (AAA): set up the test data, call the function under test, verify the result; (4) test edge cases — empty input, maximum values, null/None, boundary conditions; (5) tests should be deterministic — no random numbers, no network calls, no file system dependencies (use mocks); (6) treat test code as production code — refactor it, review it, maintain it. Frameworks: pytest (Python), JUnit (Java), Jest/Vitest (JavaScript/TypeScript), Rust's built-in test framework. By 2040: AI-assisted test generation can produce good first drafts of unit tests — use them, but always verify that the generated tests actually test the right behaviour.
- **Integration and API Testing:** Testing the seams where components meet. For a web backend: test that API endpoints return correct responses for valid requests, appropriate error codes for invalid requests, and behave correctly under concurrent access. For database interactions: test that queries return expected results, that transactions roll back correctly on failure, that migrations don't corrupt data. Tools: pytest + requests/httpx for API testing, Testcontainers for spinning up real databases in test environments. The integration test database should be separate from development and production databases — set up schema, insert test data, run tests, tear down, repeat.
- **Test-Driven Development (TDD) — When and Why:** Write the test first, watch it fail, write the minimal code to make it pass, refactor. TDD is not a dogma; it's a tool that is most valuable when: (1) you're writing algorithmic code with clear inputs and outputs (the test acts as a specification); (2) you're fixing a bug (write a test that reproduces the bug, then fix it — the test prevents regression); (3) the design isn't clear yet (writing the test first forces you to think about the interface before the implementation). TDD is less valuable for UI code (where the "correct output" is visual), exploratory code (where you're discovering what's possible), or glue code (where you're wiring together well-tested components). For capstone: use TDD for your algorithmic core; use test-after for integration tests; use manual testing for UI polishing.
- **Continuous Integration (CI):** Every push to the main branch (or every PR) triggers an automated test suite. If tests fail, the team is notified immediately — and the social contract is that the person who broke the build fixes it before doing anything else. CI setup: GitHub Actions (recommended for capstone — free for public repos, included in GitHub Student Pack), GitLab CI, or Jenkins. Your CI pipeline should run: linting/formatting checks, unit tests, integration tests (if they can run in CI — use SQLite for testing if PostgreSQL isn't feasible in CI), and ideally a build step that proves your system compiles/packages correctly. The goal: you should never discover that the build is broken during a demo or submission.

### Required Reading

- Beck, K. (2003). *Test-Driven Development: By Example*. Addison-Wesley. (Part I: The Money Example)
- Meszaros, G. (2007). *xUnit Test Patterns: Refactoring Test Code*. Addison-Wesley. (Chapters on test smells and patterns)
- Freeman, S. & Pryce, N. (2009). *Growing Object-Oriented Software, Guided by Tests*. Addison-Wesley. (Chapters 1–5)
- Humble, J. & Farley, D. (2010). *Continuous Delivery*. Addison-Wesley. (Chapters on CI and testing strategy)
- Fowler, M. (2038). "The Practical Test Pyramid — 2040 Update." *martinfowler.com*. [Online article]

### Discussion Questions

1. "We don't have time to write tests — we have to finish the features." When is this argument valid, and when is it self-defeating?
2. How much test coverage is "enough" for a capstone project? Is 100% code coverage a meaningful goal?
3. Your integration tests pass locally but fail in CI because of a database version mismatch. How should your team handle this?

### Practice Problems

- Take a module from your capstone codebase with less than 50% test coverage. Write unit tests to bring it above 80%, focusing on the most critical paths.
- Set up a CI pipeline for your capstone repository that runs linting and unit tests on every push. Document the process for your team.

---

ᚾ **Lecture 10: Documentation — Making Your Work Understandable and Maintainable**

**Course:** CS406 — Capstone Project I
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Documentation is the interface between your past self and your future self — and between you and everyone who will ever use, maintain, or evaluate your system. This lecture covers the documentation that a capstone project needs: API documentation, developer guides, user manuals, and the architectural documentation that explains not just *what* the system does but *why* it's built the way it is.

### Key Topics

- **The Documentation Portfolio:** A capstone requires multiple documentation types for different audiences. (1) *README:* the front door — what is this project, why does it exist, how do I install it, how do I run it, how do I contribute? This is the first thing your evaluators and potential employers will see. (2) *Architecture documentation:* for future maintainers (including your CS407 selves). (3) *API documentation:* for developers integrating with your system. (4) *Developer guide:* for new team members — how to set up the development environment, coding conventions, Git workflow, testing procedures. (5) *User documentation:* for end users — how to accomplish common tasks. (6) *Project wiki or knowledge base:* for decisions, meeting notes, research findings that don't fit elsewhere. Not all of these need to be exhaustive — but all should exist, even if briefly.
- **README-Driven Development:** A practice adapted from Tom Preston-Werner (2010): write the README first. Not the entire README — but enough to answer: What is this? Why would anyone care? How do you use it? Writing the README first clarifies your vision in a way that's harder to achieve with code. If you can't write a compelling README, you might not have a compelling project. The README should include: project name and one-line description, badges (build status, test coverage, license), a screenshot or demo GIF (if applicable), installation instructions (exact commands, not "install dependencies"), usage examples (realistic, copy-paste-able), API overview (if applicable), contribution guidelines, license, and acknowledgments.
- **API Documentation:** For any system that exposes an API (REST, GraphQL, gRPC, or library API), documentation is the API's user interface. Standards: OpenAPI (formerly Swagger) for REST APIs — a machine-readable specification that can generate interactive documentation, client libraries, and test suites. Write the OpenAPI spec alongside (or before) implementing the endpoints. Tools: Swagger UI, Redoc, Scalar for interactive docs; Postman collections for sharing and testing. For library APIs: docstrings in the source code (JSDoc for JavaScript, docstrings for Python, `///` comments for Rust), extracted with documentation generators (JSDoc, Sphinx, rustdoc). The standard: every public function, class, and method should have a docstring describing its purpose, parameters, return value, and (for non-obvious behaviour) a usage example.
- **Writing Good Documentation:** Principles from *The Good Docs Project* and Write the Docs community: (1) Task-oriented — organise by what users want to accomplish, not by system architecture. (2) Concrete — use realistic examples, not abstract descriptions. "To filter the dataset by date range: `GET /api/data?start=2039-01-01&end=2039-12-31`" is better than "The `/api/data` endpoint accepts optional query parameters." (3) Up-to-date — treat documentation as part of the product. When the API changes, the docs must change simultaneously. Automate where possible (OpenAPI spec drives both implementation validation and documentation). (4) Reviewed — have someone who didn't write the code follow your documentation to set up and run the system. If they can't do it, the documentation is incomplete. (5) Versioned — documentation lives in the same repository as the code, versioned together. Users of version 1.0 should be able to read version 1.0's documentation.
- **The CS406 Documentation Deliverables:** By end of term, your team must submit: (1) README (comprehensive); (2) Architecture Document (from Lecture 5, updated to reflect prototype findings); (3) API documentation (for any endpoints your prototype exposes); (4) Developer setup guide (a new team member should be able to clone the repo, run one script, and have a working development environment); (5) Meeting notes and ADRs (organised in the repo, not scattered across chat apps); (6) CS406 Progress Report — a 3–5 page narrative describing what you built, what you learned, what changed from your initial plan, and what your plan is for CS407. This report is the primary basis for your CS406 grade.

### Required Reading

- Aghajani, E. et al. (2019). "Software Documentation Issues Unveiled." *Proceedings of ICSE 2019*, 1199–1210. (The research on what makes documentation fail)
- The Good Docs Project. (2038). *Documentation Templates and Best Practices*. [thegooddocsproject.dev]
- OpenAPI Initiative. (2021). *OpenAPI Specification v3.1.0*. [openapis.org — the current standard]
- UoY Capstone Archive. (2040). "Exemplary Documentation: Annotated Examples from High-Scoring Capstone Projects."
- Preston-Werner, T. (2010). "Readme Driven Development." [Online — the original essay]

### Discussion Questions

1. Is it better to have documentation that's comprehensive but sometimes outdated, or documentation that's sparse but always accurate?
2. Your team uses a chat platform for daily coordination. A critical design decision is documented there, not in the repository. Is this a problem, and how would you fix it?
3. How much documentation does a capstone project *actually* need — at what point does documentation effort become diminishing returns?

### Practice Problems

- Audit a popular open-source project's README against the checklist above. What's missing, and what's exemplary?
- Write an OpenAPI specification for one endpoint in your capstone prototype. Generate interactive documentation and verify that a teammate can understand your API from the docs alone.

---

ᚨ (Ansuz) **Lecture 11: Mentor Relationship and Progress Communication**

**Course:** CS406 — Capstone Project I
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Your capstone mentor is not your boss, not your client, and not a mind-reader. The most successful capstone teams are those that manage their mentor relationship well: communicating progress clearly, surfacing problems early, and using mentor meetings as working sessions rather than status reports. This lecture covers the practical skills of professional communication — skills that will serve you throughout your career.

### Key Topics

- **The Mentor's Role:** Your mentor is a domain expert, a process guide, and an advocate — but not a project manager, not a technical lead, and not a therapist. They can: help you evaluate technical approaches, connect you with relevant resources and experts, identify risks you're not seeing, and advocate for your team if grading disputes arise. They cannot: write your code, manage your schedule, resolve your team conflicts (though they can advise), or guarantee you a good grade. The most common capstone mistake: waiting until the weekly meeting to reveal that you've been stuck for six days. Your mentor can't help with problems they don't know about. Surface problems in your team chat or by email within 24 hours of identifying them.
- **Effective Mentor Meetings:** A 30-minute weekly meeting is precious — don't waste it. Before the meeting: send a brief agenda (3–5 bullet points) at least 24 hours in advance. Include: what you accomplished since last meeting, what you're stuck on (specific questions, not general anxiety), and what you plan to accomplish before next meeting. During the meeting: start with the stuck items — if your mentor can unblock you in 10 minutes, you've saved days of floundering. Take notes — preferably one team member designated as note-taker per meeting, rotating. End with explicit action items: "By next week, we'll have the database migration working and the first API endpoint tested. Eiríkr will send us the contact for the dataset we need." After the meeting: send a brief summary to your mentor confirming action items — this creates a paper trail and prevents misunderstandings.
- **Progress Reporting:** Your mentor evaluates you partly on process, not just product. Demonstrate good process by: (1) maintaining an up-to-date Kanban board that reflects reality (if you're not updating it, it's not a process tool — it's theatre); (2) writing brief weekly progress reports (½ page: what we did, what we learned, what's next, what we need help with); (3) keeping the repository in a reviewable state — your mentor should be able to pull your code, run the tests, and see the prototype working; (4) communicating changes of plan — if you pivot from Plan A to Plan B, explain why (with evidence from prototyping or research), don't just show up with a different project. Your mentor's trust is built on transparency, not on uninterrupted success. A team that consistently reports problems honestly is more trusted than a team that only reports smooth sailing.
- **Handling Bad News:** At some point, something will go wrong. A team member will drop out. A critical dependency will be deprecated. Your prototype will reveal that your core algorithm doesn't scale. The wrong response: hiding the problem and hoping it resolves itself. The right response: (1) Acknowledge the problem to your team immediately. (2) Assess the impact: what deliverables are affected, and by how much? (3) Identify options: can we pivot? Can we descope? Can we substitute a simpler approach? (4) Present the problem and your proposed solution to your mentor — don't just drop the problem in their lap. "Our real-time sync approach using WebSockets adds 200ms latency per message, which breaks the collaborative editing experience. We've identified two options: (a) switch to WebRTC for peer-to-peer sync with <50ms latency but more complex NAT traversal, or (b) accept the latency and frame the product as asynchronous collaboration instead of real-time. We recommend (b) because..." This demonstrates professional maturity far more than never having problems.
- **The CS406 Final Submission and Presentation:** End-of-term deliverables: the prototype (demonstrable, even if incomplete), the updated architecture document, ADRs, the progress report (3–5 pages), and a 15-minute presentation to your mentor and one external reviewer. The presentation is not a demo — it's a narrative: what problem did you set out to solve, what did you learn (from literature, from prototyping, from users), what did you build, and what's your plan for CS407? Practise the presentation at least twice. The most common presentation failure: spending 12 minutes on background and 3 minutes on actual results. Flip it — 3 minutes on background, 12 on what you did and learned.

### Required Reading

- UoY Capstone Handbook. (2040). "Section 4: Mentor Relationship Guidelines." [Updated annually]
- Rackham, N. (1988). *SPIN Selling*. McGraw-Hill. (Chapter on "Situation, Problem, Implication, Need-Payoff" questions — applicable to structuring mentor conversations)
- Review the CS406 final presentations of 2 exemplary past capstones from the UoY Capstone Archive.
- Hafsteinn, E. (2039). "What Mentors Wish Students Knew: An Analysis of 200 Capstone Mentoring Relationships." *UoY Computing Education Research*, 2(2), 45–62.

### Discussion Questions

1. Your mentor suggests a technical approach that your team disagrees with. How do you handle this respectfully?
2. A teammate hasn't contributed meaningfully in two weeks. You've spoken to them privately and nothing changed. Do you tell your mentor? Why or why not?
3. What's the difference between a productive mentor relationship and an unhealthy dependency? Where's the line?

### Practice Problems

- Draft a sample weekly progress email for your capstone team, following the format above. Have a peer critique it: is it clear, specific, and actionable?
- Role-play a "bad news" conversation: your key algorithm doesn't perform as expected. Practise presenting the problem, the impact, and your proposed solution in 3 minutes.

---

ᛞ **Lecture 12: The CS406 → CS407 Transition — From Prototype to Production**

**Course:** CS406 — Capstone Project I
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

The final lecture of CS406 is a bridge to CS407. We synthesise the term's lessons into a concrete plan for the implementation term: what must be accomplished, what must be decided, and what must be documented before the prototyping phase ends and the building phase begins. This is also a moment for reflection — what kind of engineer are you becoming, and what does your capstone reveal about that journey?

### Key Topics

- **The CS407 Readiness Checklist:** Before CS406 ends, your team should have: (1) a validated architecture (prototype demonstrates that the major components can work together); (2) a prioritised backlog of features for CS407 implementation, estimated to the nearest week; (3) a test strategy and CI pipeline that are operational; (4) documentation that would allow a new team member to become productive within one week; (5) a clear, specific, written plan for CS407 Week 1 — what will the first sprint deliver? Teams that enter CS407 without this checklist waste the first 2–3 weeks re-establishing context, and those weeks are almost never recovered.
- **Estimating the Remaining Work:** Estimation is hard, and CS students systematically underestimate by a factor of 2–3. Techniques to improve accuracy: (1) Decompose features into tasks smaller than 3 days — a task estimated at "2 weeks" is not decomposed enough. (2) Use historical data — how long did similar tasks take during the prototype phase? That's your baseline, not your wishful thinking. (3) Identify the "unknown unknowns" — tasks whose difficulty you can't estimate because you've never done anything like them before. These are your highest-risk items. Spike them first in CS407. (4) Build buffer into your schedule — plan to have all core features implemented by CS407 Week 8, leaving Weeks 9–12 for testing, polishing, documentation, and the unexpected. (5) Track actual vs. estimated time from day one of CS407 — this data will improve your estimates as the term progresses, and it's exactly what professional teams do.
- **Technical Debt from Prototyping:** Prototype code accumulates shortcuts — hardcoded values, missing error handling, "TODO: implement properly," performance optimisations deferred. Before CS407 implementation begins, catalogue your technical debt: create issues in your project tracker for every known shortcut, tagged "tech-debt." Prioritise them: tech-debt that would cause data corruption or security vulnerabilities must be addressed immediately; tech-debt that affects developer productivity (build times, test flakiness) should be addressed early; tech-debt that only affects edge cases can wait. The trap: "we'll rewrite the prototype code properly in CS407." The reality: you'll keep the prototype code and fix the worst of it, because rewriting from scratch has its own risks and timeline. Be strategic about which modules to rewrite and which to refactor incrementally.
- **The Capstone Thesis Outline:** CS407 requires a written thesis (typically 30–50 pages) documenting your project. By the end of CS406, draft the thesis outline — not the content, but the structure: Introduction, Background and Related Work (your literature review, updated), System Design (your architecture document, updated), Implementation, Evaluation, Discussion (limitations, future work), Conclusion. Having the outline now means that as you implement in CS407, you'll naturally collect material for each section — screenshots, performance measurements, design rationale. The alternative — finishing the code and then writing the thesis from scratch in the final week — produces poor theses and miserable students.
- **Reflection — What the Capstone Teaches Beyond the Code:** The capstone is designed to teach things that coursework cannot: (1) *Ambiguity tolerance* — real problems don't have a single correct answer. (2) *Self-directed learning* — you will encounter technologies, concepts, and challenges that no instructor anticipated. (3) *Collaborative persistence* — working through frustration with people you depend on and who depend on you. (4) *Communication of complex ideas* — to technical and non-technical audiences, in writing and in person. (5) *Professional judgment* — when to push forward, when to pivot, when to ask for help. These are the competencies that distinguish a CS graduate from a programmer. The code you write for your capstone will likely be obsolete within five years. The judgment you build will last your entire career.
- **Closing — The Forge and the Smith:** The University of Yggdrasil's motto, carved above the entrance to The Forge: *Smiðr smíðar sik sjálfan* — "The smith forges himself." The capstone is not just about the system you build. It's about the engineer you become through the process of building it. The frustrations, the dead ends, the moments of clarity, the 2am debugging sessions, the pride of demonstration — all of it is the hammer and the anvil. In CS407, you will ship a system. In CS406, you have begun to ship yourself.

### Required Reading

- Brooks, F.P. (1995). *The Mythical Man-Month* (Anniversary Edition). Addison-Wesley. (Chapters 1–3, 16 — "No Silver Bullet")
- McConnell, S. (2006). *Software Estimation: Demystifying the Black Art*. Microsoft Press. (Chapters on estimation techniques and calibration)
- Hunt, A. & Thomas, D. (2019). *The Pragmatic Programmer* (20th Anniversary Edition). Addison-Wesley. (Chapter on "Technical Debt")
- UoY Capstone Archive. (2040). "CS406-to-CS407 Transition Plans: Annotated Exemplars."
- Hafsteinn, E. (2039). "The Forge and the Smith: A Philosophy of Capstone Education." *Communications of the ACM*, 62(10), 38–40.

### Discussion Questions

1. Your prototype code is a mess — it works, but it's embarrassing. Your team is split: half wants to rewrite from scratch in CS407, half wants to refactor incrementally. What would you advise?
2. You estimated 6 weeks for the core implementation. Your mentor says it'll take 12. How do you reconcile this difference?
3. What is the most important thing you personally want to learn or demonstrate through your capstone — beyond "getting a good grade"?

### Practice Problems

- Create a prioritised backlog for your CS407 implementation, with each item estimated and decomposed into tasks of ≤3 days.
- Draft your capstone thesis outline (sections and subsections). For each section, note what material you already have and what you'll need to collect during CS407.
- Write a one-page personal reflection: what kind of engineer do you want to be, and how does your capstone contribute to that vision?

---

---

## Final Examination Preparation

CS406 is assessed through a portfolio, not a sit-down examination:

### Assessment Components

**1. Prototype Demonstration (30%)**
A 20-minute live demonstration of your working prototype to your mentor and one external reviewer. The prototype must demonstrate a complete vertical slice (tracer bullet) through your architecture. You will be assessed on: (a) does it work? (b) does it demonstrate the architecturally significant aspects? (c) can you explain what it does and doesn't do, and why?

**2. Architecture Document (25%)**
Your architecture document (from Lecture 5), updated to reflect prototype findings. Must include: system overview (4+1 views), technology stack justification, key interfaces, data model, cross-cutting concerns, and ADRs for all significant architectural decisions. Assessed on clarity, rigour, and evidence of iterative improvement.

**3. Progress Report (20%)**
A 3–5 page narrative answering: What problem did you set out to solve? What did you learn from your literature review and prototyping? What changed from your initial plan? What is your concrete plan for CS407? Assessed on honesty, specificity, and quality of reflection.

**4. Process and Professionalism (25%)**
Assessed through: team charter (did you create and follow one?), Kanban/agile practice (does the board reflect reality?), mentor communication (regular, structured, proactive), repository hygiene (README, developer guide, CI pipeline, organized commits), and peer evaluation (confidential teammate assessments). This component rewards process quality — a team with a modest but well-run project can score higher here than a team with ambitious but chaotic work.

| Criterion | Weight | Excellent (A) | Good (B) | Adequate (C) | Insufficient (D/F) |
|-----------|--------|---------------|----------|--------------|---------------------|
| Prototype functionality | 30% | Working, demonstrates architectural viability, well-scoped | Mostly working, minor gaps | Partially working, significant gaps | Non-functional or trivial |
| Architecture quality | 25% | Clear, rigorous, justified, updated from feedback | Solid but some gaps in justification | Present but superficial | Missing or incoherent |
| Progress report quality | 20% | Insightful, specific, honest about challenges | Clear but generic | Superficial, glosses over problems | Missing or dishonest |
| Process quality | 25% | Excellent team practice, communication, repository hygiene | Good practice, some gaps | Inconsistent practice | Chaotic or absent process |

---

*Woven in The Forge, University of Yggdrasil, 2040. The smith forges the blade, and the blade forges the smith. May your capstone be worthy of both traditions.*
