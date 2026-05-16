# CS406: Capstone Project I — Design, Architecture, and Prototype
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4
**Instructor:** Prof. Björn Þorbjarnarson, Ph.D.
**Office:** Mjölnir Engineering Centre, Room 212
**Email:** b.thorbjarnarson@yggdrasil.edu
**Semester:** Spring 2040
**Prerequisites:** All CS 300-level courses or concurrent enrolment in final 300-level requirements.

**Description:** The first semester of the two-semester capstone sequence. Students form teams of 3–5, identify a substantial computing problem, conduct a feasibility study, produce a detailed system architecture and design document, and deliver a working prototype demonstrating core technical feasibility. This course bridges academic learning and professional practice — you leave it ready to build, not just to study. CS407 (Capstone Project II) continues the project to completion.

**Required Texts:**
- Fox, A. & Patterson, D. (2038). *Engineering Software as a Service: An Agile Approach Using Cloud Computing*, 4th ed. Strawberry Canyon LLC.
- Osterwalder, A. & Pigneur, Y. (2036). *Value Proposition Design for Technical Products*. Wiley.
- Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley. (Still the foundation, supplemented by modern distributed systems patterns.)

**Assessment:** Project proposal (15%), feasibility study (15%), architecture document (25%), design review presentation (15%), working prototype (30%).

---

## Lecture 1: The Capstone Mindset — From Student to Practitioner

*"The difference between a student project and a real system is that someone actually needs the real system to work."* — Prof. Björn Þorbjarnarson, 2040

Welcome to the threshold. For three years, you have been a student of computer science — learning algorithms other people discovered, implementing systems other people designed, solving problems other people posed. The capstone is different. For the first time, you will identify a problem yourself, design a system yourself, make architectural tradeoffs yourself, and be accountable for the result yourself. This is less a course and more a rite of passage.

The capstone mindset has three pillars. **First: ownership.** Your project is not an assignment to be completed for a grade. It is a system you are choosing to build because you believe it should exist. When you encounter a difficult bug at 11 p.m., the grade will not motivate you to continue — but genuine belief in the problem you're solving will. Choose a project you care about, not a project that seems easy to implement. The easiest project, if you don't care about it, will be the hardest to finish.

**Second: scope discipline.** The most common capstone failure mode is over-ambition: "We're going to build a fully decentralised social network with end-to-end encryption, content moderation AI, and VR support — in one semester." No, you're not. A good capstone project has one core technical challenge — one thing that, if you solve it, makes the project a success. Everything else is scaffolding. Identify that one thing, build it first, and only add features if time permits. The minimum viable product (MVP) is not an admission of weakness; it is the mark of a professional.

**Third: team as first system.** Before you build any software system, you must build your team system. How will you communicate? (Daily standups? Slack? Discord? In-person? — choose one primary channel and use it.) How will you make decisions when you disagree? (Consensus? Vote? Team lead decides? — agree on this in Week 1, not when the argument is already happening.) How will you divide work? (By component? By feature? Pair programming throughout? — there is no single right answer, but there must be an answer.) How will you handle a teammate who is not contributing? (This is the hardest question, and you must answer it before it happens.) The capstone is as much about collaborative engineering as it is about technical engineering.

The lecture closes with a survey of exemplary capstone projects from past years: an open-source fuzzer that found 23 previously unknown bugs in the Linux kernel, a VR physiotherapy platform adopted by two regional hospitals, a distributed computing framework that reduced ML training costs by 40% for a campus research lab, a browser extension that detected misinformation with 94% accuracy. Notice what these have in common: they solved a specific problem for specific users. No project succeeded by being "generally useful." They succeeded by being specifically useful to someone in particular.

**Required Reading:**
- Fox & Patterson (2038), Chapter 1: "Introduction to SaaS and Agile Development."
- Brooks, F. P. (1975, updated 2035). *The Mythical Man-Month: Essays on Software Engineering*, Anniversary Edition. Chapter 2: "The Mythical Man-Month."
- Yggdrasil Capstone Archive. Browse at least 5 past projects from capstone.yggdrasil.edu/archive.

**Discussion Questions:**
1. What is the difference between a project you *can* build and a project you *should* build? How do you evaluate whether a problem is worth solving?
2. Your teammate proposes a project that would require learning three new frameworks. What questions do you ask about scope and risk before saying yes?
3. A successful capstone project from three years ago built a campus event discovery app. Why would building the same app today be a poor choice? What changes would make it novel again?

---

## Lecture 2: Problem Discovery — Finding a Dragon Worth Slaying

*"If I had an hour to solve a problem, I'd spend 55 minutes thinking about the problem and 5 minutes thinking about solutions."* — Often attributed to Einstein

The hardest part of the capstone is not the coding — it's the choosing. What problem should you solve? This lecture provides structured methods for problem discovery, drawn from design thinking, entrepreneurial practice, and research methodology.

**The pain-point method.** Start with frustration rather than inspiration. What computing task makes you, your peers, or your potential users angry or exhausted? Pain points are better project foundations than "cool ideas" because they come with built-in motivation and a clear success criterion: does the pain go away? Interview 20 people in a target user group (students, researchers, small business owners, accessibility-needing populations, community organisations). Ask: "What's the most frustrating part of your computing workflow?" Listen for repeated themes. A problem mentioned by 8 of 20 interviewees is worth investigating. A problem mentioned by 2 is probably idiosyncratic.

**The technology-enablement method.** Sometimes a new technology creates possibilities that didn't exist before, and the problem is finding the killer application. Edge AI on microcontrollers (2038), verified compilation for Rust (2039), and open-weight language models running locally (2040) are current examples. The question is not "what problem exists?" but "what problem can this technology solve that couldn't be solved before?" This approach is riskier — you may build a solution looking for a problem — but it can also produce the most innovative projects. Validate early: show a prototype to potential users within the first three weeks and ask "would you use this?" If they say "maybe, if..." and trail off, you don't have product-market fit. If they say "When can I have it?" you might.

**The gap-in-the-literature method** (for research-oriented projects). Survey the recent literature in a subfield of computing you find interesting — program analysis, HCI, distributed systems, ML systems, whatever. Where do the papers all say "future work should address X"? Where do you see a pattern of papers working around a problem rather than solving it? A capstone that fills a genuine research gap, even partially, can become a workshop paper, a conference poster, or the seed of a graduate research programme. This method requires more upfront reading but produces projects with clearer intellectual contributions.

**Feasibility triage.** Once you have a shortlist of 3–5 candidate problems, run the FAST filter (Feasibility, Ambition, Stakeholders, Timeline): (1) Can the core technical challenge be reduced to something solvable in 10 weeks of part-time work? (2) Is the project ambitious enough to demonstrate the skills of a graduating CS student? (3) Are there real stakeholders who want this and will provide feedback? (4) Can you deliver a meaningful prototype by the mid-semester design review? A project that fails any of these is a risk. A project that fails two is a crisis in waiting.

**Required Reading:**
- Osterwalder & Pigneur (2036), Chapters 1–2: "Customer Profile" and "Value Map."
- Yggdrasil Capstone Handbook (2040), Section 2: "Problem Selection and Validation."
- Ries, E. (2037). *The Lean Startup for Technical Products*, 4th ed. Chapters 1–3 on validated learning.

**Discussion Questions:**
1. Apply the pain-point method to your own experience as a CS student. List five computing frustrations. For each, estimate how many people share it and whether a solution already exists.
2. Your team wants to build "a better to-do app." Using the FAST filter, evaluate this project idea. Which criteria does it fail? Can it be rescued by narrowing the scope?
3. Interview three non-CS students about their computing frustrations. What did you learn that you wouldn't have guessed from your own experience?

---

## Lecture 3: The Feasibility Study — Proving It Can Be Done Before You Start

*"Weeks of coding can save you hours of planning."* — Anonymous (and wrong)

Before you architect a solution, you must prove — with evidence, not optimism — that a solution is possible. The feasibility study is a structured investigation that answers four questions: (1) Can we build it? (Technical feasibility.) (2) Should we build it? (Value feasibility.) (3) Can we build it within constraints? (Resource feasibility.) (4) Are we the right people to build it? (Team feasibility.) A good feasibility study saves months of wasted effort; a skipped feasibility study is the most common reason capstone projects fail to deliver.

**Technical feasibility.** Identify the core technical challenge — the one thing that, if unsolved, kills the project. Build a "tracer bullet" (Hunt & Thomas, 1999): a minimal end-to-end implementation that proves the critical path works. If your project is a real-time collaborative code editor, the tracer bullet is not a beautiful UI — it's two browser windows editing the same document in real time without conflict. If that works, everything else is decoration. If it doesn't, you have your answer. For AI/ML projects, the feasibility question is often about data: do you have access to a dataset of sufficient size, quality, and representativeness to train or fine-tune your model? "We'll find a dataset later" is not a plan — it's a hope dressed in planning language.

**Value feasibility.** Who wants this, and how badly? For open-source tools, measure community interest: are there GitHub issues with 50+ thumbs-up reactions requesting exactly this? For research projects, would the result be publishable? For commercial-adjacent projects, would someone pay for this, and if so, how much? The value feasibility study does not require a business plan, but it requires evidence of genuine demand. Interview at least 10 potential users. Show them a mockup or a concept video. Ask: "If this existed today, how would it change your workflow?" If they say "That's interesting" and change the subject, the value is low. If they ask specific questions about implementation details, pricing, or timeline, the value is real.

**Resource feasibility.** What resources do you need, and do you have them? Compute resources (GPU hours for ML projects, cloud credits for distributed systems), data resources (access to proprietary APIs, proprietary datasets), human resources (do you need a domain expert who isn't on your team?), and most importantly, time resources (10 weeks of 10–15 hours per person per week = 500–750 person-hours total — what can you actually accomplish in that budget?). A project requiring 2,000 GPU-hours on A100s when your team has access to 200 hours of T4 credits is not feasible. A project requiring expertise in quantum error correction when nobody on your team has taken a quantum computing course is not feasible.

**Team feasibility.** Does your team have — or can your team acquire — the necessary skills? This is not about current skills; it's about learnability. A team of four who all know Python and web development building a web application is low risk. The same team building a compiler in Rust with LLVM backend is high risk — someone needs to learn Rust, someone needs to learn LLVM, and these are not weekend projects. That doesn't mean you shouldn't do it — ambitious learning is part of the capstone — but you must budget learning time explicitly (40+ hours per new major technology) and build a fallback plan (if the Rust compiler proves too hard, what's the MVP in Python?).

**Required Reading:**
- Yggdrasil Capstone Handbook (2040), Section 3: "The Feasibility Study."
- Fox & Patterson (2038), Chapter 3: "SaaS Architecture and Planning."
- Hunt, A. & Thomas, D. (1999, updated 2039). *The Pragmatic Programmer*, 3rd ed. Tip 22: "Use Tracer Bullets to Find the Target."

**Discussion Questions:**
1. Your team proposes building a privacy-preserving contact tracing app using Bluetooth and differential privacy. Walk through the four feasibility questions. Which one is hardest to answer and why?
2. What is the difference between a tracer bullet and a prototype? When would you build each?
3. Your feasibility study reveals a 60% chance of technical success within the semester. Is this acceptable? How would you communicate this uncertainty to stakeholders?

---

## Lecture 4: Requirements Engineering — What Must the System Do, Exactly?

*"The hardest single part of building a software system is deciding precisely what to build."* — Fred Brooks, 1987

Requirements are the contract between your team and reality. Get them wrong, and you will build the wrong system, no matter how elegant your architecture or how clean your code. This lecture teaches modern requirements engineering for capstone-scale projects — not the heavyweight IEEE 830 standard for defence contractors, but the practical discipline that separates successful student projects from "we built something cool that nobody uses."

**User stories and epics.** The agile approach to requirements organises functionality around user goals rather than system features. A user story follows the Connextra template: "As a [type of user], I want [some goal] so that [some reason]." The key word is "so that" — it forces you to articulate the value, not just the mechanic. Good: "As a teaching assistant, I want to batch-download all submissions for an assignment so that I can run them through a plagiarism checker." Bad: "As a user, I want a download button." The difference is context. User stories are organised into epics (groups of related stories) and themes (groups of epics). A capstone project typically has 1–2 epics (e.g., "Collaborative Editing," "Version History") with 8–15 stories each.

**Functional and non-functional requirements.** Functional requirements describe what the system does: "The system shall allow users to create accounts using their university SSO." Non-functional requirements describe how the system does it: "Account creation shall complete within 2 seconds for 95% of requests under a load of 100 concurrent users." Capstone projects often neglect non-functional requirements because they don't show up in demos — and then the system collapses under load during the final presentation. Minimum non-functional requirements for any capstone: performance (response time under expected load), availability (uptime during the evaluation period), security (authentication, authorisation, data protection), usability (can a non-team-member complete the primary user flow without instruction?), and maintainability (can a new team member understand the codebase within a week?).

**Prioritisation: MoSCoW.** Not all requirements are equal. The MoSCoW method classifies each requirement as Must-have (the system fails without it), Should-have (important but not critical for MVP), Could-have (nice to have if time permits), or Won't-have (explicitly deferred to CS407 or beyond). A disciplined team limits Must-haves to 40–50% of total requirements — any more and you're not prioritising, you're wish-listing. The Must-haves define your MVP; the Should-haves your target deliverable; the Could-haves your stretch goals. Write your MoSCoW list in Week 2, revisit it in Week 5 after the tracer bullet, and show it at every design review. Stakeholders seeing a MoSCoW list understand your priorities; stakeholders seeing an unprioritised list of 200 features understand only your ambition.

**Requirements validation.** Requirements are hypotheses about what users need. Validate them before building. For each Must-have user story, ask: can we test this with a paper prototype, a clickable mockup (Figma, Sketch), or a concierge MVP (manual behind-the-scenes work mimicking the automated system)? If you can validate 80% of your Must-haves with prototypes before writing production code, you have dramatically reduced the risk of building the wrong thing. The capstone is short — every week spent building the wrong feature is a week you cannot get back.

**Required Reading:**
- Fox & Patterson (2038), Chapter 4: "User Stories and Requirements."
- Wiegers, K. & Beatty, J. (2039). *Software Requirements*, 4th ed. Microsoft Press. Chapters 1–5.
- Cohn, M. (2037). *User Stories Applied for Agile Software Development*. Addison-Wesley. Chapter 1–4.

**Discussion Questions:**
1. Take a familiar system (e.g., your university's course registration portal) and write 10 user stories for it. Classify them with MoSCoW. What did you learn about what's truly essential?
2. A stakeholder says: "The system must be fast." Turn this vague requirement into a testable non-functional requirement with specific metrics.
3. Your team disagrees about whether a feature is Must-have or Should-have. What process do you use to resolve the disagreement? What evidence would change someone's classification?

---

## Lecture 5: System Architecture — The Bones of the Longhouse

*"Architecture represents the significant design decisions that shape a system, where significant is measured by cost of change."* — Grady Booch, 2006

Architecture is the set of decisions that are hard to change later. Choosing between a relational database and a document store is architectural — changing it six weeks in requires rewriting every data access layer. Choosing between React and Vue for your frontend is less architectural — you can (painfully) migrate a single-page app between frameworks. This lecture teaches architectural thinking at the capstone scale: big enough to matter, small enough to fit in one brain.

**Architectural drivers.** Every architecture serves multiple masters. The key is identifying which ones dominate for your project. The SEI quality attribute workshop method (Barbacci et al., 2003) generates a ranked list of quality attributes (performance, availability, security, modifiability, usability, testability, deployability) by having stakeholders vote on scenarios. For a capstone project, the "stakeholders" are your team, your advisor, and your target users. A typical capstone architecture is driven by 2–3 primary quality attributes. A real-time multiplayer game prioritises performance and availability; a healthcare data platform prioritises security and modifiability; a research prototype prioritises testability and deployability. Knowing your top two quality attributes focuses every architectural decision.

**Architectural patterns for capstone projects.** The most common patterns in 2040 capstone projects: (1) **Monolith with clean boundaries** — a single deployable with well-defined internal modules (controllers, services, repositories). Appropriate when your team is small, your domain is not yet well-understood, and deployment simplicity matters more than independent scalability. This is the right choice for 60% of capstone projects. (2) **Microservices lite** — 2–4 independently deployable services communicating via REST or gRPC. Appropriate when you have clear domain boundaries (e.g., a user service, a content service, an analytics service) and your team can handle the operational overhead. (3) **Event-driven architecture** — components communicate through an event bus (Kafka, RabbitMQ, Redis streams). Appropriate for projects involving real-time data processing, IoT sensor networks, or complex workflows. (4) **Serverless** — functions deployed on Functions-as-a-Service (AWS Lambda, Cloudflare Workers). Appropriate for event-driven, sporadically-used applications where you want to minimise operational burden.

**The C4 model for documenting architecture.** Simon Brown's C4 model (2011, updated 2038) provides four levels of architecture documentation, and capstone projects should produce at least the first three. **Level 1: System Context diagram** — your system as a box, users and external systems as boxes, interactions as labelled arrows. One diagram. **Level 2: Container diagram** — your system decomposed into high-level technical building blocks (web app, mobile app, API server, database, file store, message queue), with technology choices and communication protocols specified. **Level 3: Component diagram** — each container decomposed into components (e.g., the API server contains an auth component, a business logic component, a data access component), with interfaces specified. Level 4 (code-level class diagrams) is usually overkill for capstone documentation unless specifically requested by your advisor. Produce C4 diagrams using the Structurizr DSL or Mermaid — ASCII art in a wiki is better than no diagrams at all.

**Architecture Decision Records (ADRs).** Every non-trivial architectural decision should be documented in an ADR: a short markdown file in your repo's `docs/adr/` directory that records the context, the decision, the alternatives considered, and the consequences. ADR-001 might be "Use PostgreSQL as primary database" with alternatives MongoDB and CockroachDB discussed. ADR-002 might be "Use JWT for authentication" with alternatives session cookies and OAuth discussed. ADRs serve two purposes: they force you to articulate your reasoning (and thereby discover flaws), and they provide a historical record for your future selves and for the CS407 team that may inherit your project. A project with 5–10 ADRs is well-architected; a project with zero ADRs is flying blind, however beautiful the code.

**Required Reading:**
- Brown, S. (2038). *The C4 Model for Visualising Software Architecture*, 2nd ed. Leanpub. Chapters 1–4.
- Richards, M. & Ford, N. (2039). *Fundamentals of Software Architecture*. O'Reilly. Chapters 1–3.
- Gamma et al. (1994), selected patterns relevant to your project domain.

**Discussion Questions:**
1. Draw a C4 Level 1 System Context diagram for your proposed capstone project. What external systems does your system depend on? What happens if one of them is unavailable?
2. Your team is split between building a monolith (faster to develop) and microservices (cooler on a résumé). What architectural drivers would justify microservices? What would make them a bad choice?
3. Write an ADR for a significant architectural decision in your project (database choice, API protocol, authentication strategy). Show it to a classmate and ask: "Does this convince you that we made the right choice?"

---

## Lecture 6: Technology Selection — Choosing Your Weapons Wisely

*"A bad craftsman blames his tools. A good craftsman chooses his tools carefully."* — Adapted proverb

The technology stack you choose in Week 3 will define your daily experience for the next 10 weeks. Choose well and the tools disappear, leaving you free to focus on your domain problem. Choose poorly and every feature becomes a fight with your framework. This lecture provides a structured framework for technology evaluation and selection, informed by the realities of capstone development.

**The evaluation framework.** For each technology candidate, evaluate six criteria: (1) **Team familiarity** — does at least one team member know this technology well? If not, budget 20–40 hours for the learning curve. (2) **Community and ecosystem** — are there Stack Overflow answers, blog posts, and example projects for the problems you'll face? A technology with 10 active users and no documentation is a research project, not a tool. (3) **Maturity and stability** — is this a 1.0 release with a commitment to backward compatibility, or a 0.3 alpha that might change its API next week? For capstone projects, prefer boring technology: PostgreSQL over the new distributed NewSQL database, React over the framework released last month, Python over the language with the elegant type system that nobody on your team has used. (4) **Fit for purpose** — does this technology solve the specific problem you have, or are you using it because it's trendy? Graph databases are excellent for highly connected data (social graphs, recommendation engines) and terrible for tabular data (user accounts, transaction records). (5) **Integration complexity** — how hard is it to connect this technology to the rest of your stack? A technology that requires a custom bridge, a conversion layer, and a wrapper library adds invisible cost. (6) **Operational burden** — how hard is it to deploy, monitor, and debug this technology? A technology that requires a dedicated Kubernetes operator when your team has never used Kubernetes is a burden you don't need.

**The 2040 technology landscape — a sampling.** *Frontend:* React 22 with Server Components is the default for web UIs; Svelte 8 for performance-critical interactive UIs; Flutter 6 for cross-platform mobile. *Backend:* FastAPI (Python) and Actix-Web (Rust) dominate for API servers; Node.js 26 remains viable for I/O-bound services. *Databases:* PostgreSQL 21 for relational data with JSONB for flexible schemas; SQLite 4 for embedded and single-user applications; ClickHouse for analytics; Redis 9 for caching and real-time data structures. *AI/ML:* PyTorch 5 for research; ONNX Runtime for deployment; llama.cpp for local LLM inference; LangChain 4 for LLM application orchestration. *Infrastructure:* Docker for containerisation; GitHub Actions for CI/CD; Terraform for infrastructure-as-code; Kubernetes for multi-service orchestration (but consider whether you really need it). *Communication:* REST for simple CRUD; GraphQL for complex data fetching; gRPC for high-performance service-to-service; WebSocket for real-time bidirectional communication.

**The decision matrix.** Create a table: rows are candidate technologies, columns are the six evaluation criteria scored 1–5, with a weighted total. Make team familiarity weight 2× for capstone projects — the technology your team already knows is almost always the right choice unless there's a compelling reason to use something else. Share the decision matrix with your advisor. A decision matrix turns a subjective argument ("React is better!") into an objective discussion ("Let's see... your team has 15 combined years of Vue experience and zero React, and your project doesn't need React Server Components. Based on your own scoring, Vue is the better choice.").

**The sunk-cost trap.** A technology decision, once made, is not permanent — but it is expensive to change. If you discover in Week 5 that your chosen database cannot handle your query patterns, you face a choice: restructure your queries (cheap), add a caching layer (medium), or migrate databases (expensive). The right answer depends on how fundamental the mismatch is. A mismatch that affects one feature is a workaround. A mismatch that affects every feature is a migration. The key is recognising which situation you're in, and not letting "we already set up the database" prevent you from fixing a fundamental problem. This is the sunk-cost fallacy, and it has killed more capstone projects than any technical bug.

**Required Reading:**
- Fox & Patterson (2038), Chapter 5: "The SaaS Technology Stack."
- ThoughtWorks Technology Radar, latest edition (thoughtworks.com/radar). Pay attention to "Hold" items — technologies you should avoid.
- Yggdrasil Capstone Archive: technology selections of past projects, with post-mortems on what worked and what didn't.

**Discussion Questions:**
1. Your team is building a real-time dashboard. Evaluate three database choices (PostgreSQL, ClickHouse, InfluxDB) using the six criteria. Weight team familiarity at 2×. Which wins?
2. A teammate proposes using a brand-new Rust web framework (v0.2, 47 GitHub stars). Build the argument against this choice using the evaluation criteria. What would need to be true for this to actually be a good choice?
3. In Week 7, you discover your chosen framework doesn't support a feature that's a Must-have. The migration cost is estimated at 40 hours. Your remaining budget is 200 person-hours. Do you migrate? What factors influence your decision beyond the raw numbers?

---

## Lecture 7: Prototyping — Building to Learn, Not to Impress

*"The prototype is not the product. The prototype's purpose is to die."* — Prof. Björn Þorbjarnarson, 2040

A prototype is an instrument of learning. You build it not to demonstrate how clever you are, but to discover what you don't know. This lecture teaches prototyping as a research method — systematic, hypothesis-driven, and explicitly temporary.

**Types of prototypes.** *Proof-of-concept prototype:* answers the question "can this be done at all?" — e.g., can we render 10,000 data points on a mobile device at 60 fps? *Technical spike:* answers a specific, bounded technical question — e.g., can WebRTC establish a direct peer-to-peer connection between two browsers behind NAT? *User experience prototype:* answers the question "would someone want to use this?" — a clickable Figma mockup or a Wizard of Oz prototype where a human simulates the AI behind the scenes. *Integration prototype:* answers "do these three services actually work together?" — the tracer bullet from Lecture 3. *Performance prototype:* answers "will this be fast enough under load?" — a load test of the component most likely to be a bottleneck.

**Prototyping discipline.** The prototype must be built with the explicit understanding that it will be thrown away. This is hard — you will be tempted to keep the prototype and "iterate it into the product." Resist. Prototype code is written for speed of learning, not for maintainability, testability, or security. It skips error handling, hardcodes credentials, ignores edge cases, and optimises for the happy path. If you keep it, you will spend the rest of the semester fighting its limitations. The correct workflow is: prototype → learn → discard → build properly. A prototype that takes 20 hours to build might save 200 hours of building the wrong thing. A prototype that takes 200 hours defeats the purpose — you could have built the real thing in 200 hours. Budget 10–15% of total project time for prototyping. More than that, and your prototype has become your product without you noticing.

**Prototype evaluation.** Every prototype answers a question. Before you build, write down the question and the success criteria. "Can we achieve sub-100ms latency for collaborative editing on a local network?" — success is a measured 95th-percentile latency of 97ms. "Would teaching assistants use a batch download feature?" — success is 7 of 10 TAs shown the mockup saying "I would use this weekly." If the prototype fails, you have learned something valuable — ideally in Week 3 rather than Week 10. If it succeeds, you have evidence to support your architectural decisions. Either way, document the result: what you built, what you measured, what you concluded. This documentation becomes part of your final report and demonstrates methodological rigour.

**The capstone prototype requirement.** By the mid-semester design review (typically Week 7), you must present a working prototype that demonstrates your core technical feasibility. This is not a slide deck — it's a live demo of the one thing that makes your project work. For a distributed systems project, it's nodes communicating and reaching consensus. For an ML project, it's a model trained on representative data producing non-trivial results. For an HCI project, it's a clickable interface that real users can navigate. The prototype doesn't need to be pretty, fast, or complete — but it must work. A team that shows up to the design review with slides and no code has failed the prototyping phase. A team that shows up with a messy but functional demo of their core challenge has succeeded, even if everything else is still on paper.

**Required Reading:**
- Fox & Patterson (2038), Chapter 7: "Agile Development and Prototyping."
- Buxton, B. (2037). *Sketching User Experiences: Getting the Design Right and the Right Design*, 3rd ed. Morgan Kaufmann. Chapters on prototyping.
- Ries, E. (2037), Chapter 6: "Minimum Viable Product."

**Discussion Questions:**
1. Your team is building a music recommendation system. Describe three different types of prototypes you could build and what each would teach you. Which would you build first?
2. You've been working on a prototype for three weeks and it's starting to look pretty good. How do you decide whether to keep it or discard it? What signs indicate you should discard it even if it works?
3. Your prototype successfully demonstrates your core algorithm, but it's 500 lines of spaghetti code with no tests. A teammate says, "Let's just clean this up instead of rewriting." Make the argument for rewriting. Make the argument for cleaning up. Which is stronger for your specific situation?

---

## Lecture 8: Design Review — Presenting Your Vision to the Thing

*"If you can't explain it simply, you don't understand it well enough."* — Often attributed to Einstein

The design review is the midpoint ceremony of the capstone: you present your problem, your architecture, and your prototype to a panel of faculty and industry reviewers who will challenge every assumption you've made. This is not a punitive exercise — it is the most valuable feedback you will receive all semester. A good design review catches fatal flaws before they become unfixable. A great design review transforms your project.

**The design review presentation structure.** 15 minutes of presentation, 15 minutes of Q&A. Slide 1: Title, team, one-sentence project description. Slide 2: The problem — who has it, why it matters, what existing solutions miss. Slide 3: Your approach — the one-sentence technical insight that makes your solution different. Slide 4: System architecture (C4 Level 2 Container diagram). Slide 5: Key design decisions with rationale (ADR summary). Slide 6: Prototype demo (live, not recorded — live demos are harder but much more convincing). Slides 7–8: Technical challenges encountered and how you addressed them. Slide 9: Project plan for CS407: what will be built, on what timeline, with what risks. Slide 10: Request for guidance — what specific questions do you want the reviewers to answer? ("Should we use event sourcing or CRUD for our domain model?" is a good question. "Do you like our project?" is not.)

**Live demo survival.** Live demos fail. Plan for failure. Have a recorded backup (screen recording of the same demo running successfully) ready to play if the live demo crashes. Never say "It was working 10 minutes ago" — reviewers have heard this a thousand times. Instead: "We're experiencing a network issue; here's a recording of the same flow from this morning. We'll troubleshoot the live issue during Q&A if there's interest." Have a "demo script" — a specific sequence of actions that demonstrates your core capability. Do not free-explore your own prototype during the presentation. Have the script memorised. Practice the demo at least five times in the actual presentation environment (same machine, same network, same projector resolution). The demo that works perfectly in your dorm room will fail in the presentation room for a reason you never anticipated — the projector resolution breaks your CSS, the university Wi-Fi blocks your WebSocket port, your laptop goes to sleep during the introduction slide. Five practice runs will catch most of these.

**Receiving criticism.** The design review panel's job is to find problems. They will succeed. Your job is not to defend your decisions — it's to understand the criticism and use it. When a reviewer says "Your consistency model won't work under network partitions," do not argue that network partitions are unlikely. Instead ask: "Can you help us understand what scenario you're concerned about?" You might learn that your consistency model really is fine and the reviewer was thinking of a different use case — or you might learn about a failure mode you genuinely hadn't considered. Either way, you gain knowledge by asking, not by defending. Take notes during the review. Afterward, as a team, categorise every piece of feedback as: (1) Actionable now — fix before the semester ends. (2) Actionable in CS407 — add to the project plan. (3) Disagree — document why, for your final report. (4) Clarify — the reviewer misunderstood something; improve your communication, not your system.

**The review report.** Within one week of the design review, submit a 3–5 page review response document. For each major piece of feedback: restate the feedback in your own words (proving you understood it), describe what you did (or will do) in response, and explain your reasoning if you chose not to act on it. This document is the primary deliverable of the design review phase and demonstrates professional maturity.

**Required Reading:**
- Yggdrasil Capstone Handbook (2040), Section 5: "The Design Review."
- Reynolds, G. (2038). *Presentation Zen Design*, 4th ed. New Riders. Chapters on slide design.
- Watch recordings of at least 3 past capstone design reviews from the Yggdrasil archive.

**Discussion Questions:**
1. Watch a past design review recording. Identify the moment where the reviewers found the most significant problem. How did the team respond? What would you have done differently?
2. Your demo crashes 30 seconds in. Your backup recording is on a USB drive that your laptop can't read. What do you do in the remaining 14 minutes?
3. A reviewer says "This has already been done by Company X." You've never heard of Company X. How do you respond in the moment? What do you do after the review?

---

## Lecture 9: Team Dynamics — The Hidden Architecture

*"The major problems of our work are not so much technological as sociological in nature."* — Tom DeMarco and Timothy Lister, *Peopleware*, 1987

The team is the first system you build, and if it fails, everything else fails too. This lecture addresses the human architecture of the capstone project: how to organise work, resolve conflict, maintain motivation, and ensure that everyone contributes meaningfully.

**Work division strategies.** Three common models: *Component-based division* (each person owns one component — frontend, backend, database, ML pipeline), *Feature-based division* (each person owns complete features end-to-end), and *Pair-everything* (all work is done in rotating pairs). Component-based division maximises individual autonomy and minimises context-switching, but creates knowledge silos — if the backend person gets sick, nobody else can work on the backend. Feature-based division builds shared codebase knowledge and reduces silos, but increases coordination overhead — two people working on features that touch the same database table may conflict. Pair-everything produces the highest code quality and the best shared understanding, but cuts apparent velocity in half (though research consistently shows that pair programming actually reduces total time by catching bugs early). For capstone teams of 3–5, a hybrid model often works best: core infrastructure (database schema, API contracts, CI/CD) is pair-programmed, while feature work is done individually with code review.

**Conflict resolution.** Conflict is not a sign of a dysfunctional team — it's a sign that team members care about the project. The question is how you handle conflict. The Thomas-Kilmann model (1974) identifies five modes: competing (I win, you lose), accommodating (I lose, you win), avoiding (nobody deals with it), compromising (we both lose a bit), and collaborating (we find a solution that fully satisfies both). Collaborating takes the most time but produces the best outcomes for important decisions. Use collaborating for architectural decisions, technology choices, and design tradeoffs. Use compromising for less critical disagreements (code style, variable naming). Use competing only when a decision must be made immediately and you have genuine expertise the other person lacks. Never use avoiding — unresolved conflicts fester.

**The non-contributing teammate.** This is the hardest problem in any team project, and the capstone is no exception. The script: (1) Private conversation. "I've noticed you haven't been at the last three standups and your pull request has been open for two weeks. Is everything okay? How can we help?" Maybe they're struggling with the material, dealing with personal issues, or didn't realise they were falling behind. (2) If nothing changes: team conversation with clear expectations. "Here are the three specific things we need from you by Friday. Here's the help we're offering (pair programming, reduced scope, documented setup steps)." (3) If still nothing changes: involve your advisor. This is not tattling — it's project management. Your advisor can mediate, adjust scope, or in extreme cases, adjust individual grades to reflect contribution. Do not wait until Week 9 to address a problem that started in Week 3. The earlier you intervene, the more options you have.

**Motivation and burnout.** The capstone is a marathon, not a sprint. The team that works 60-hour weeks in Weeks 3–4 will burn out by Week 8. Sustainable pace: 10–15 hours per person per week, with at least one day completely off. Celebrate small wins: the first successful API call, the first passing integration test, the first positive user feedback. These moments are the emotional fuel that carries you through the frustrating debugging sessions. If morale is low, drop everything and ship something — even a tiny feature, even a cosmetic improvement. The psychological boost of "we made something work" often unlocks the energy to tackle the next hard problem.

**Required Reading:**
- DeMarco, T. & Lister, T. (2037). *Peopleware: Productive Projects and Teams*, 4th ed. Addison-Wesley. Chapters on team dynamics.
- Lencioni, P. (2035). *The Five Dysfunctions of a Team*, 3rd ed. Jossey-Bass. The fable section.
- Yggdrasil Capstone Handbook (2040), Section 6: "Team Management."

**Discussion Questions:**
1. Your team has 4 members. Two want component-based division, two want pair-everything. How do you resolve this? What experiment could you run to test which approach works better for your team?
2. A teammate consistently submits code that doesn't pass tests and requires extensive rewriting during code review. How do you address this without destroying their confidence or your relationship?
3. It's Week 6 and your team's motivation is flagging — standups have become perfunctory, nobody is excited about the project. What specific actions can you take to rebuild momentum?

---

## Lecture 10: Documentation — Writing It Down So Others Can Build On It

*"Documentation is a love letter that you write to your future self."* — Damian Conway, 2005

Documentation is not an afterthought — it is a deliverable. For the capstone, your documentation serves four audiences: (1) your current team, who need to onboard new members if someone joins late; (2) your future selves in CS407, who will have forgotten why you made certain decisions; (3) the faculty evaluating your project, who need to understand what you built and why; (4) the open-source community, if you choose to release your project. This lecture covers what to document, how to structure it, and how to keep it alive.

**The documentation portfolio.** Every capstone project must produce: (1) **README.md** — the front door. One paragraph describing what the project does, one paragraph on why it exists, one code block showing how to install and run it in under 2 minutes. If a new developer can't get your project running from the README in 10 minutes, the README has failed. (2) **CONTRIBUTING.md** — how to set up a development environment, how to run tests, how to submit changes, what coding standards you follow. (3) **Architecture document** (`docs/architecture.md`) — the C4 diagrams from Lecture 5, plus a narrative explaining the architectural drivers and key design decisions. (4) **ADR log** (`docs/adr/`) — 5–10 Architecture Decision Records. (5) **API documentation** — if your project exposes an API, document every endpoint with request/response examples. OpenAPI/Swagger is the standard; generate it from code annotations where possible. (6) **User guide** — a short document explaining the primary user flows, with screenshots. If a non-technical user can't understand how to use your system, your user guide needs work. (7) **Developer guide** — the internal documentation: how the code is organised, where to find things, what the key abstractions are. This is a map of the codebase for the next developer (including your future self).

**Documentation as part of the workflow.** Documentation that is written after the code is finished is documentation that will never be written — or worse, will be written badly in a panic the night before the deadline. Integrate documentation into your workflow: every pull request that adds a feature must update the relevant documentation. Every PR that changes an API must update the API docs. Every PR that makes an architectural decision must include an ADR. This sounds like overhead, but it's cheaper than trying to reconstruct decisions from memory months later. Use documentation-driven development for complex features: write the user-facing documentation *first*, then implement the feature to match the documentation. This ensures the API makes sense from the user's perspective before you commit to an implementation.

**Maintaining documentation quality.** Documentation rots. The code changes but the README still says "run `python app.py`" when you migrated to Docker six weeks ago. Combat documentation rot with automated checks: a CI step that verifies all documented commands actually work, a link checker for your documentation URLs, a screenshot comparison tool that flags UI changes. At minimum, schedule a "documentation audit" every two weeks: one team member spends an hour following every command in the README and user guide from scratch and files bugs for anything that doesn't work. This is tedious but essential — documentation that doesn't work is worse than no documentation at all, because it wastes time and erodes trust.

**Required Reading:**
- A successful open-source project's documentation (recommended: FastAPI, React, or Rust — all known for excellent documentation). Read the README, the Getting Started guide, and the API reference. What makes them effective?
- Google (2039). *Technical Writing Courses for Engineers*. Available free online. Complete "Technical Writing One" and "Technical Writing Two."
- Yggdrasil Capstone Archive: compare the documentation quality of the top-graded and bottom-graded projects. What patterns emerge?

**Discussion Questions:**
1. Open the README of a popular open-source project. Time yourself: how long until you can run the project and see it working? What obstacles did you encounter? What would you improve?
2. Your team's API documentation is out of date because nobody wants to update it manually. Research and propose an automated solution (e.g., OpenAPI generation, doc tests) appropriate for your tech stack.
3. Write the README for your capstone project as if explaining it to a CS sophomore. Then rewrite it as if explaining it to a potential employer. What changed? Why?

---

## Lecture 11: Ethics in Practice — Building Systems That Do No Harm

*"Technology is not neutral. We're inside of what we make, and it's inside of us."* — Donna Haraway, 1991

CS405 (Research Methods) covered research ethics; CS406 covers engineering ethics — the ethical considerations embedded in the systems you build, not just the studies you run. Every capstone project has ethical dimensions, whether you acknowledge them or not. This lecture helps you identify and address them.

**The ethical inventory.** For your project, answer these questions: (1) Who are all the stakeholders — not just users, but people affected by the system even if they never touch it? (Think of gig workers managed by algorithms they can't see, communities impacted by predictive policing trained on biased data, content moderators exposed to traumatic material.) (2) What data does your system collect, store, or process? If it's personal data, what are the GDPR/data protection implications? If it's behavioural data, can it be used to infer sensitive attributes? (3) Who might misuse your system? A facial recognition system for unlocking your phone can also be used for mass surveillance. A language model fine-tuned for code generation can also generate malware. You cannot prevent all misuse, but you can anticipate it and design mitigations. (4) Who is excluded? If your health monitoring app requires a $1,000 smartphone, you have excluded people who can't afford one. If your app only supports English, you have excluded billions. Exclusion is not always evil — every system has a target audience — but it should be intentional, not accidental. (5) What are the second-order effects? Your ride-sharing app reduces car ownership (good) but also destroys the taxi industry (harmful to taxi drivers). Your automated grading system saves TA time (good) but may systematically grade non-native English speakers lower (harmful). Second-order effects are hard to predict but essential to attempt.

**Practical mitigations.** For data privacy: minimise collection (do you really need that field?), encrypt at rest and in transit, delete data when no longer needed, and never log sensitive information. For fairness: test your system on diverse data, disaggregate your metrics by relevant demographic factors, and involve affected communities in design and testing — not as an afterthought but from the beginning. For accessibility: follow WCAG 3.0 guidelines for web interfaces, support screen readers, ensure keyboard navigability, and test with users who have disabilities — simulators are not substitutes. For security: use established authentication libraries rather than rolling your own, keep dependencies updated (Dependabot or Renovate), run static analysis (Semgrep, CodeQL), and conduct a threat model — even a simple STRIDE analysis on a whiteboard is better than nothing.

**The ethics section of the final report.** Your capstone final report must include an ethics section (minimum 500 words) addressing: (1) stakeholder analysis, (2) data practices and privacy protections, (3) potential for misuse and mitigations, (4) accessibility considerations, (5) fairness considerations if applicable, (6) environmental impact if applicable (what is the carbon footprint of training your model or running your service?). This section is graded — a generic "our project has no ethical concerns" will receive a failing grade for this component because it demonstrates either ignorance or dishonesty. Every project that involves data, users, or automation has ethical concerns — the question is whether you have the courage and rigour to confront them.

**Required Reading:**
- ACM (2038). *ACM Code of Ethics and Professional Conduct*. Focus on Principle 1: "Contribute to society and to human well-being."
- The Markkula Center for Applied Ethics (2036). *A Framework for Ethical Decision Making*. Available at scu.edu/ethics.
- Selbst, A. D. et al. (2019). "Fairness and Abstraction in Sociotechnical Systems." *Proceedings of FAT* '19.

**Discussion Questions:**
1. Conduct an ethical inventory for your capstone project using the five questions above. Which answer surprised you most? What mitigation did you add that you hadn't planned?
2. Your project collects user behaviour data to improve recommendations. A teammate says "Everyone does this, it's fine." Construct the argument that it might not be fine. What additional protections could you implement?
3. Evaluate the accessibility of your prototype. Can a blind user navigate it? A user with motor impairments? A user on a slow 3G connection in a rural area? What's the one most impactful accessibility improvement you could make?

---

## Lecture 12: Preparing for Capstone II — The Road from Prototype to Product

*"Plans are worthless, but planning is everything."* — Dwight D. Eisenhower, 1957

CS406 ends with a prototype; CS407 demands a finished product. This final lecture prepares you for the transition — what must happen between semesters, what changes in the second semester, and how to hit the ground running.

**The post-semester retrospective.** Before you disperse for the break, hold a 2-hour team retrospective. Three questions: What worked well that we should continue? What didn't work that we should change? What did we learn that we wish we'd known in Week 1? Document the answers. The retrospective is not a blame session — it's an honest assessment of process. "Our code review process was inconsistent — some PRs sat for 4 days without review" is a process problem. "Alice didn't review enough PRs" is a blame statement. Frame everything as process. The retrospective produces a short document (the "CS407 Prep Doc") that you will read on Day 1 of CS407 to remember who you were and what you learned.

**The CS407 project plan.** By the end of CS406, you must produce a detailed plan for CS407. This is not a Gantt chart fantasy — it's a realistic assessment of what remains to be built, who will build it, and on what timeline. The plan should decompose the remaining work into 1–2 week cycles (sprints), each with a clear goal: "Sprint 1 (Weeks 1–2): Complete the authentication system and user profile management. Sprint 2 (Weeks 3–4): Implement the core recommendation algorithm and basic UI." Each sprint should have a definition of done: "All tests pass, code is reviewed, feature is deployed to staging, documentation is updated, and at least 2 external users have tried it." The plan must include buffer time — at least 20% of the total schedule for unexpected problems. A plan with zero buffer is not a plan; it's a wish.

**Knowledge transfer.** If your team composition changes between CS406 and CS407 (someone drops, someone joins), you must onboard new members. Your documentation (Lecture 10) is the onboarding curriculum. Assign each new member a "buddy" — an existing team member who walks them through the codebase, answers questions, and reviews their first few PRs. Budget 10–15 hours of existing team members' time for onboarding. This is not wasted time — it's an investment in the team's capacity for CS407.

**The bridge work.** The break between semesters is not a vacation from the capstone — but neither is it a death march. The bridge work is the minimum necessary to keep momentum and prevent cold-start problems: each team member should review the CS407 Prep Doc, re-read the architecture documentation, and run the latest version of the code to confirm it still works. If possible, fix one small bug or add one small feature during the break — the psychological momentum of having *done something* before Day 1 is enormous. But do not attempt major features during the break. You need rest. A well-rested team in Week 1 of CS407 will outproduce a burned-out team that "worked through the break."

**Final words.** You entered CS406 as students. You leave as practitioners who have identified a real problem, proven its feasibility, architected a solution, built a prototype, defended your design before experts, and laid the groundwork for a complete system. The capstone is the story you will tell in job interviews and graduate school applications — the proof that you can do the thing, not just study the thing. What remains in CS407 is execution: building the rest of the system, testing it thoroughly, and delivering something you are proud to put your name on. You have the skills, the team, and the plan. Now build.

*"Þat er þá reynt, er þú at rúnum spyrr." — "It is proven when you inquire of the runes." Hávamál, st. 80*

**Required Reading:**
- Yggdrasil Capstone Handbook (2040), Section 8: "CS407 Preparation."
- Your team's own CS406 documentation. Re-read it as if you were a new team member. What's missing? Fill the gaps.
- Derbey, E. & Larsen, D. (2037). *Agile Retrospectives: Making Good Teams Great*, 3rd ed. Pragmatic Bookshelf. The retrospective activities section.

**Discussion Questions:**
1. Hold a 15-minute mini-retrospective with your team right now. What's the one thing you most need to change in your process for CS407?
2. Write a "Day 1 of CS407" checklist for your future self. What do you need to do in the first hour, the first day, the first week?
3. A year from now, you're describing your capstone in a job interview. What story do you want to tell? What would you need to achieve in CS407 to tell that story honestly?

---

## Final Examination / Deliverable

CS406 culminates in a **Portfolio Submission** rather than a written exam. Your portfolio consists of:

1. **Project Proposal** (submitted Week 3) — Problem statement, user research summary, feasibility study results, initial technology evaluation matrix.
2. **Architecture Document** (submitted Week 6) — C4 Level 1–3 diagrams, ADR log (minimum 5 decisions), non-functional requirements specification, technology stack with justification.
3. **Working Prototype** (demonstrated at Design Review, Week 7–8) — Source code repository, live demo, test suite demonstrating core functionality works.
4. **Design Review Materials** (Week 7–8) — Presentation slides, demo script, review response document.
5. **CS407 Project Plan** (submitted Week 10) — Sprint plan, task breakdown, risk register, onboarding guide.
6. **Reflection Essay** (1,500 words, submitted Week 10) — What did you learn about software engineering, teamwork, and yourself? What would you do differently? What are you most proud of?

### Grading Rubric

| Component | Weight | Key Criteria |
|-----------|--------|-------------|
| Project Proposal | 15% | Problem clarity, user need evidence, feasibility rigour |
| Architecture Document | 25% | Design quality, ADR depth, diagram clarity, technology justification |
| Working Prototype | 30% | Core functionality demonstrated, code quality, test coverage |
| Design Review | 15% | Presentation clarity, demo reliability, review response quality |
| CS407 Plan | 10% | Realism, specificity, risk awareness |
| Reflection Essay | 5% | Insightfulness, honesty, growth demonstrated |

---

## Course Summary

CS406 marks your transition from student of computing to practitioner of software engineering. You have learned to identify worthy problems, evaluate feasibility with evidence rather than optimism, architect systems with intentional tradeoffs, select technologies with structured reasoning, build prototypes that answer specific questions, present your work to expert audiences, manage team dynamics with professional maturity, document your work for future inheritors, confront the ethical dimensions of your creations, and plan the path from prototype to finished product. These are not academic exercises — they are the daily practices of professional software engineers, technical leads, and engineering managers. The capstone is hard by design, because the profession is hard. You are ready.

*Gangið ykkur vel, smiðir framtíðar. Go well, builders of the future.*
— Prof. Björn Þorbjarnarson

---

**Course Policies:**
- **Team contribution:** Individual grades may be adjusted based on peer evaluations. If a team member consistently under-contributes, address it early (see Lecture 9).
- **Late submissions:** 10% deduction per day. After 5 days, maximum grade is 50%.
- **Academic integrity:** All code must be original or properly attributed. Using open-source libraries is encouraged; using open-source projects as your entire capstone is plagiarism.
- **Office hours:** Mondays and Wednesdays 15:00–17:00, Mjölnir Engineering Centre 212. Team office hours by appointment.
- **Accommodations:** Contact the University Accessibility Office. We will work with you to ensure you can complete the capstone requirements.
