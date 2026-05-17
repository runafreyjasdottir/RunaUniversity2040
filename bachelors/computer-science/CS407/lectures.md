# CS407: Capstone Project II — Implementation, Testing, Deployment & Presentation
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4  
**Prerequisites:** CS406 — Capstone Project I (Design, Architecture & Prototype), senior standing  
**Description:** The second semester of the two-semester CS capstone sequence. Students take the working prototypes built in CS406 and carry them through full implementation, comprehensive testing, production deployment, and formal public presentation. Emphasis on software craftsmanship, automated quality assurance, DevOps practices, stakeholder communication, and the transition from prototype to product. Each team delivers a production-ready system with CI/CD pipelines, monitoring, documentation, and a live demo at the Yggdrasil Capstone Symposium.

**Instructor:** Dr. Sigrún Véfreyjasdottir, Senior Lecturer in Software Engineering & Capstone Coordinator  
**Lab:** YggLab Capstone Studio, Ground Floor, Muninn Computing Centre  
**Symposium:** Final week of semester, Þingvellir Hall, Yggdrasil Main Campus  
**Office Hours:** By appointment via Yggdrasil Student Portal

---

## Lectures

ᚠ **Lecture 1: From Prototype to Production — The Architecture of Completion**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

The prototype you built in CS406 was a proof of possibility — a demonstration that your idea could work, given generous assumptions, simplified inputs, and a forgiving environment. This lecture addresses the chasm between prototype and production: the architectural decisions, engineering practices, and psychological shifts required to transform a demonstration into a system that real users can depend upon. We examine the concept of **gradual hardening** — the process of replacing assumptions with guarantees, mock data with real data, and manual steps with automated processes. The lecture introduces the Production Readiness Checklist (PRC) used at Yggdrasil, adapted from the Google Site Reliability Engineering framework and refined through a decade of capstone deployments.

### Key Topics

- **The Prototype-Production Gap:** Why prototypes are not products. The assumptions that prototypes make (single user, clean data, fast network, small datasets, forgiving error handling) and how each must be systematically challenged and hardened. The concept of **invariant-driven engineering** — identifying the properties your system must always maintain and designing mechanisms that enforce them.
- **Gradual Hardening Strategy:** A systematic approach to productionization: (1) Data layer — replace mock data with real schemas, add validation, migration paths, and backup strategies; (2) Concurrency layer — move from single-threaded to multi-user, add session management, authentication, and authorization; (3) Error layer — replace panics and exceptions with structured error handling, circuit breakers, and graceful degradation; (4) Performance layer — measure, profile, and optimize the critical path; (5) Operations layer — add logging, metrics, health checks, and deployment automation.
- **The Production Readiness Checklist (PRC):** Yggdrasil's 48-item checklist covering data integrity, security, scalability, observability, documentation, and maintainability. The PRC is not a gate — it is a guide. Teams that treat it as a bureaucratic hurdle produce brittle systems; teams that treat it as a thinking tool produce resilient ones.
- **When to Refactor vs. When to Rewrite:** The hardest decision in production engineering. Signals that a prototype architecture can be evolved: clean separation of concerns, test coverage above 60%, well-understood dependencies. Signals that a rewrite may be necessary: fundamental scaling bottlenecks, unsafe dependencies, untestable core logic. The capstone constraint: you have one semester, so evolutionary refactoring is almost always the right choice.

### Lecture Notes

The prototype-to-production transition is where most student projects founder — not because of technical limitations, but because of psychological ones. The prototype *worked*. You demoed it to your advisor and she nodded approvingly. There is a powerful temptation to believe that the remaining work is "just polish" — adding a few features, cleaning up the UI, writing some tests. This belief is catastrophically wrong.

Production software is defined not by what it does when everything goes right, but by what it does when things go wrong. A prototype assumes the database is always reachable; production software must handle network partitions, slow queries, and corrupted data. A prototype assumes the user is benign; production software must validate every input, authenticate every request, and sanitize every output. A prototype runs on your laptop; production software runs on infrastructure you do not control, shared with other applications, subject to patching, reboots, and resource contention.

The Norse metaphor is apt: the prototype is the sword forged in calm waters — beautiful, balanced, but untested. Production is the sword that must survive the battle — the edge that must hold against mail, the grip that must not slip when drenched in rain and blood. The smith who forged it must now temper it, harden it, and test it against every adversity the battlefield can offer. Gradual hardening is that tempering process.

**Invariant-driven engineering** deserves particular attention. An invariant is a property that must always be true, regardless of what operations occur. For a banking system: "account balance never goes negative." For a chat system: "messages are delivered exactly once, in order, or not at all." For your capstone: you must identify the invariants that matter to your domain and then design mechanisms that make violation impossible — not merely unlikely. Database constraints, type systems, formal verification (for critical components), and careful API design are all tools for invariant preservation.

The decision to refactor or rewrite is emotionally charged. Teams that have struggled with a prototype often fantasize about a clean rewrite that will solve all their problems. In the capstone context, this fantasy is almost always fatal. A rewrite consumes the first half of the semester, leaving no time for testing, deployment, or presentation. The disciplined approach is to identify the three most problematic components, refactor them incrementally, and accept that some technical debt will remain. Technical debt is not shameful — unmanaged technical debt is. Document your debt in a TECHDEBT.md file, prioritize it, and address it when you have capacity.

### Required Reading

- UoY Capstone Handbook (2040 Edition), Chapters 8-10: "From Prototype to Product," "The Production Readiness Checklist," "Refactoring vs. Rewriting."
- Humble, J. & Farley, D. (2038). *Continuous Delivery: Reliable Software Releases Through Build, Test, and Deployment Automation*, 3rd Edition. Addison-Wesley. Chapters 1-3.
- Beyer, B., Jones, C., Petoff, J., & Murphy, N. (2036). *Site Reliability Engineering: How Google Runs Production Systems*, 2nd Edition. O'Reilly. Part I: "The SRE Mindset."

### Discussion Questions

1. What assumptions did your CS406 prototype make that are guaranteed to be violated in production? For each assumption, what is the cheapest mechanism that would turn a violation from a crash into a handled exception?
2. The PRC contains 48 items. If you could only complete 12 of them before shipping, which 12 would you choose, and why? What is your prioritization framework?
3. Your teammate argues passionately for a rewrite of the core engine. You believe refactoring is safer. What evidence would you gather to make this decision objectively? What would convince you to change your position?

---

ᚢ **Lecture 2: Test-Driven Development at Scale — From Unit Tests to System Verification**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

Testing is not a phase — it is a continuous practice woven into every line of code you write. This lecture covers the full testing spectrum from fast, isolated unit tests to slow, comprehensive end-to-end system tests, with particular attention to the testing strategies that matter for capstone projects: regression testing (ensuring that new features do not break old ones), integration testing (verifying that components interact correctly), property-based testing (generating thousands of random inputs to find edge cases), and manual exploratory testing (the creative art of breaking your own system). We introduce the Test Pyramid as an organizing framework and discuss why capstone teams typically over-invest in manual testing and under-invest in automated testing — and how to correct this imbalance.

### Key Topics

- **The Test Pyramid:** Unit tests (fast, many, cheap) at the base; integration tests (fewer, slower, more expensive) in the middle; end-to-end tests (few, slow, expensive, brittle) at the top. The 70/20/10 heuristic: 70% of tests should be unit tests, 20% integration, 10% end-to-end. Why violating this pyramid leads to slow, unreliable test suites that teams stop running.
- **Test-Driven Development (TDD) in Legacy Code:** TDD is easy when you start from scratch; it is harder when you inherit a prototype with no tests. The **characterization test** technique: write a test that captures the current behavior (even if the behavior is wrong), verify it passes, then refactor. The **seam** concept (Feathers, 2004): find places where you can inject test doubles (mocks, stubs, fakes) without changing the production code.
- **Property-Based Testing:** Instead of writing example-based tests ("input 5 produces output 25"), write property-based tests ("for all inputs x, f(x) ≥ 0"). The **Hypothesis** framework for Python and **fast-check** for TypeScript generate thousands of random inputs and shrink failing cases to minimal reproducible examples. Property-based testing finds bugs that example-based testing misses — boundary conditions, integer overflow, unexpected interactions — but requires a different mental model: thinking about invariants rather than examples.
- **Mutation Testing:** A technique for evaluating test suite quality. Mutation testing tools (like **Cosmic Ray** for Python or **Stryker** for JavaScript) automatically introduce small bugs into your code (change `+` to `-`, replace `true` with `false`) and check whether your tests catch them. A test suite that passes all mutation tests is genuinely strong; one that misses many mutants has false confidence. Mutation testing is computationally expensive but reveals the difference between "tests that run" and "tests that actually verify correctness."
- **Contract Testing for Microservices:** If your capstone involves multiple services, **Pact** and similar contract-testing frameworks verify that service A's expectations of service B's API match service B's actual behavior. This prevents the most common integration failure: "we changed our API and broke the frontend."

### Lecture Notes

The testing mindset is the engineering mindset: every claim you make about your code should be verifiable, and every verification should be repeatable. Manual testing is not verifiable — different people test differently, and the same person tests differently on Tuesday versus Friday. Automated testing is verifiable: the test either passes or fails, and if it passes today it should pass tomorrow unless the code changed.

The tragedy of capstone testing is that teams spend the final two weeks in a "testing crunch" — frantically clicking through the UI, hoping nothing breaks during the demo. This is not testing; this is prayer. The teams that deliver reliable systems are the ones that wrote their first automated test in Week 1 and added tests with every feature thereafter. By Week 10, they have 200 tests that run in two minutes and give them confidence to refactor. By Week 14, they can add a new feature on Tuesday and deploy it on Thursday because their test suite catches regressions before they reach production.

**Property-based testing** is particularly powerful for capstone projects because student code is full of hidden assumptions. You assume the user will enter a number between 1 and 100; Hypothesis generates 0, -1, 10⁹, and `NaN`. You assume a list is non-empty; Hypothesis generates the empty list. You assume two events happen in order; Hypothesis generates the reverse order. These are not malicious inputs — they are the inputs that real systems encounter in the wild. The student who has never seen property-based testing will spend hours debugging a crash that Hypothesis would have found in seconds.

**Mutation testing** is the final arbiter of test quality. A team that claims "we have 90% code coverage" may have tests that execute every line but verify nothing. Mutation testing reveals this deception: if changing a critical comparison from `<` to `≤` does not cause a test failure, your tests are theater, not engineering. The goal is not 100% mutation coverage (which is often impossible for infrastructure code), but rather that every business-critical path has tests strong enough to catch realistic bugs.

### Required Reading

- Martin, R.C. (2037). *Clean Code: A Handbook of Agile Software Craftsmanship*, 2nd Edition. Prentice Hall. Chapters 9-10: "Unit Tests" and "Test-Driven Development."
- Feathers, M. (2034). *Working Effectively with Legacy Code*, Revised Edition. Prentice Hall. Chapters 1-4, 13-16.
- Claessen, K. & Hughes, J. (2000/2035). "QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs." *ACM SIGPLAN Notices*. (The foundational paper; Yggdrasil's testing curriculum uses Hypothesis, which adapts these ideas to Python.)

### Discussion Questions

1. Your team has 500 unit tests, 50 integration tests, and 5 end-to-end tests. Is this the right ratio? What would you change, and what metrics would you use to justify the change?
2. You inherit a prototype with zero tests. Where do you start? Write a concrete plan for the first week: which components get characterization tests first, which seams do you target, and what is your coverage goal for Week 4?
3. Mutation testing reveals that your "comprehensive" test suite misses 40% of injected bugs in the payment processing module. Your teammate says "mutation testing is too strict — real bugs aren't that subtle." How do you respond? What evidence would you gather?

---

ᚦ **Lecture 3: Continuous Integration and Deployment — The Pipeline as Product**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

The continuous integration and continuous deployment (CI/CD) pipeline is the circulatory system of modern software engineering — it moves code from developer machines to production environments with speed, reliability, and auditability. This lecture covers the design and operation of CI/CD pipelines for capstone projects, from the simplest GitHub Actions workflow to multi-environment deployment strategies. We address the philosophy of **pipeline-as-code** (treating the build and deployment process as a first-class artifact, version-controlled and reviewed like any other code), the mechanics of container-based deployment (Docker, Docker Compose, and the university's internal container registry), and the critical practice of **immutable deployments** (never modifying a running server; always replace it with a new instance). The lecture concludes with the Yggdrasil deployment standard: every capstone must deploy to the university's staging environment by Week 6 and to production by Week 10.

### Key Topics

- **Pipeline-as-Code:** The CI/CD configuration is not an afterthought — it is a critical engineering artifact. Version-control your `.github/workflows/`, your Dockerfiles, your Terraform configurations, and your deployment scripts. Review pipeline changes in pull requests, just like application code. The pipeline is the product — if the pipeline is broken, no product can ship.
- **The Build Stage:** Compilation, linting, type checking, and security scanning (dependency vulnerability checks, static analysis for secrets). The build must be **reproducible**: the same commit hash must produce the same artifact, every time, on any machine. Techniques for reproducible builds: lock files (package-lock.json, Cargo.lock, poetry.lock), pinned base images (not `node:latest` but `node:20.11.0-alpine`), and build isolation (Docker multi-stage builds, Nix).
- **The Test Stage:** Automated test execution with parallelization, coverage reporting, and flaky-test detection. A flaky test (one that passes and fails non-deterministically) is worse than no test — it destroys trust in the pipeline. Strategies for flakiness: retry with backoff (treating the symptom), root-cause analysis (treating the cause: race conditions, external dependencies, time-dependent logic), and quarantine (removing the test from the critical path until it is fixed).
- **The Deploy Stage:** Blue-green deployments (two identical environments, switching traffic atomically), canary releases (gradual traffic shifting to detect problems early), and feature flags (decoupling deployment from release). For capstone projects, blue-green is usually sufficient; canary requires more sophisticated infrastructure. The key principle: **deployments must be rollbackable**. If a deployment causes an outage, you must be able to revert to the previous version in under 60 seconds.
- **Environment Strategy:** Development (local, mutable), Staging (shared, production-like, auto-deployed from main branch), and Production (shared, production, manually promoted from staging). The staging environment must mirror production in architecture, though not in scale. "It works on my machine" is unacceptable; "it works in staging" is the minimum standard.

### Lecture Notes

The CI/CD pipeline is where software engineering becomes infrastructure engineering. You are no longer just writing code; you are designing a system that builds, tests, and deploys code automatically, reliably, and observably. The quality of your pipeline determines the velocity of your team: a fast, reliable pipeline enables experimentation and iteration; a slow, brittle pipeline forces conservatism and risk aversion.

The build stage is the foundation. If your build is not reproducible, your team will waste hours debugging "why does it work on my laptop but fail in CI?" The answer is almost always: different dependency versions, different environment variables, or different base images. Pin everything. Use lock files. Use exact version numbers. The cost of a slightly outdated dependency is trivial compared to the cost of a mysterious build failure the night before the demo.

Flaky tests are a pipeline cancer. A single flaky test that fails 10% of the time will cause developers to ignore CI failures, leading to a culture where red builds are treated as "probably fine." This culture destroys quality. The correct response to a flaky test is immediate investigation: add logging, run it 100 times locally, identify the race condition or external dependency, and fix it. If it cannot be fixed immediately, quarantine it — remove it from the CI pipeline and create a high-priority ticket. Never allow a flaky test to remain in the critical path.

**Immutable deployments** are the single most important operational practice for capstone projects. The traditional approach — SSH into the server, pull the latest code, restart the service — is a recipe for disaster. It is non-repeatable (what if the restart fails halfway through?), non-auditable (who changed what, when?), and non-rollbackable (the old code is gone). The container-based approach — build a new image, push it to a registry, update the deployment to reference the new image, let the orchestrator roll it out — is repeatable, auditable, and rollbackable. If the new version fails, change one line (the image tag) and redeploy. The old image is still in the registry; the rollback is instant.

The Yggdrasil deployment standard exists because capstone teams historically treated deployment as a final-week activity, leading to catastrophic demos where the "working" system could not be reached from the reviewer's machine. By requiring staging deployment in Week 6, we force teams to confront networking, DNS, SSL, environment configuration, and database migrations while there is still time to fix them. By requiring production deployment in Week 10, we ensure that the final two weeks are spent on polish and presentation, not infrastructure archaeology.

### Required Reading

- Humble, J. & Farley, D. (2038). *Continuous Delivery*, 3rd Edition. Chapters 4-7: "Build," "Test," "Deploy," and "Infrastructure."
- Kim, G., Humble, J., Debois, P., & Willis, J. (2036). *The DevOps Handbook*, 2nd Edition. IT Revolution Press. Part II: "Where to Start."
- Yggdrasil DevOps Standards v3.1 (2040). "Capstone Deployment Requirements and Environment Provisioning." Available via Yggdrasil Internal Documentation Portal.

### Discussion Questions

1. Your build takes 45 minutes, mostly because of integration tests that spin up a real database. What strategies would you use to reduce build time without sacrificing confidence? Be specific about which tests you would move, parallelize, or replace.
2. A teammate proposes using `node:latest` in the Dockerfile "so we always get security patches." What are the risks? What is a better policy, and how do you automate it?
3. Your staging deployment succeeded, but production deployment fails with a database migration error. The migration ran partially before failing. What is your recovery procedure? How do you prevent this class of failure in the future?

---

ᚨ **Lecture 4: Performance Engineering — Measurement, Profiling, and Optimization**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

Performance is not an accident — it is the outcome of deliberate measurement, targeted analysis, and surgical optimization. This lecture covers the complete performance engineering lifecycle: establishing performance requirements (what does "fast enough" mean for your system?), measurement methodology (how to collect trustworthy performance data), profiling techniques (finding where the time goes), optimization strategies (fixing the right bottlenecks), and regression prevention (ensuring that tomorrow's commit does not undo today's gains). We emphasize the **scientific method** in performance work: hypothesis, experiment, measurement, conclusion. Capstone projects typically optimize the wrong things — micro-optimizing a loop that accounts for 1% of runtime while ignoring a database query that accounts for 60% — and this lecture provides the framework for avoiding that trap.

### Key Topics

- **Performance Requirements and SLIs:** A Service Level Indicator (SLI) is a quantitative measure of service quality: latency (p50, p95, p99), throughput (requests per second), error rate, and availability. A Service Level Objective (SLO) is a target for an SLI: "p99 latency < 200ms." A Service Level Agreement (SLA) is a contract with consequences: "if availability drops below 99.9%, we refund customers." Capstone projects should define at least two SLOs and measure against them continuously.
- **Measurement Methodology:** The difference between **benchmarking** (controlled, repeatable measurement of a specific operation) and **monitoring** (continuous measurement of production systems). Benchmarking tools: `hyperfine` for command-line programs, `pytest-benchmark` for Python, `criterion.rs` for Rust. Monitoring tools: Prometheus metrics, Grafana dashboards, distributed tracing (Jaeger, Zipkin). The **coordinated omission problem**: if your load generator pauses when the system is slow, you systematically under-report latency. The **statistical rigor** problem: performance varies; you need enough samples to distinguish signal from noise.
- **Profiling Techniques:** CPU profiling (where does the program spend its time? tools: `perf`, `py-spy`, `pprof`, `flamegraph`), memory profiling (where does the memory go? tools: `heaptrack`, `memray`, `massif`), and I/O profiling (where are the blocking operations? tools: `iotop`, `eBPF` programs). The **flame graph**: a visualization where the width of each bar represents the proportion of time spent in that function, and the stack represents the call chain. Flame graphs make bottlenecks immediately visible — the wide bar is the problem.
- **Optimization Strategies:** Amdahl's Law (the speedup of a system is limited by the fraction of time spent in the unoptimized part), the **ninety-ninety rule** (the first 90% of performance takes 10% of the effort; the last 10% takes 90%), and the **mechanical sympathy** principle (understanding how hardware works — CPU caches, branch prediction, SIMD, memory hierarchy — and writing code that cooperates with it). The optimization hierarchy: algorithmic improvements > data structure changes > reducing I/O > parallelization > micro-optimizations.
- **Performance Regression Testing:** Automated benchmarks that run in CI and fail if performance degrades beyond a threshold. **Criterion.rs** and **pytest-benchmark** both support this. The challenge: performance is noisy, so thresholds must be statistically robust (e.g., fail only if p95 latency increases by >10% across 5 consecutive runs).

### Lecture Notes

Performance engineering is often misunderstood as "making code faster." It is not. Performance engineering is **making the right code faster** — identifying the operations that actually matter to users and improving those, while leaving everything else alone. Premature optimization — optimizing before measurement — is the root of much evil: complex code, subtle bugs, and negligible real-world impact.

The scientific method is essential. When someone says "the system is slow," your first response should be "define slow." Slow compared to what? Slow for which operation? Slow under what load? Once you have a specific, measurable claim, you can form a hypothesis ("I believe the bottleneck is the database query in `get_user_profile`"), design an experiment ("I will profile the system under 100 concurrent requests"), collect data ("the query takes 450ms, 80% of total request time"), and reach a conclusion ("the query lacks an index on `user_id`; adding the index reduces latency to 12ms").

**Flame graphs** are the most powerful visualization in performance engineering. A typical web application flame graph shows a wide bar for `database_query`, a narrower bar for `json_serialize`, and a thin bar for `business_logic`. The naive optimizer might spend days optimizing JSON serialization, achieving a 2× speedup on 5% of runtime. The sophisticated optimizer adds a database index, achieving a 30× speedup on 80% of runtime. The flame graph makes the right choice obvious.

**Amdahl's Law** is humbling. If your system spends 70% of its time in database queries and 30% in business logic, even a theoretically infinite speedup of business logic can only improve total performance by 30%. The corollary: always optimize the biggest bottleneck first. If database queries are 70% of time, a 2× improvement there yields more total speedup than a 10× improvement anywhere else.

The **coordinated omission problem** is insidious. Many benchmarking tools, including some popular ones, pause their timers when the system is under load. The result: as the system gets slower, the benchmark reports *better* latency, because it is not counting the time the requests spent waiting in a queue. This is not a theoretical concern — it has led to wildly incorrect performance claims in published research. Always use benchmarking tools that account for coordinated omission, or design your experiments to avoid it (fixed-rate load generation rather than fixed-concurrency).

### Required Reading

- Gregg, B. (2037). *Systems Performance: Enterprise and the Cloud*, 2nd Edition. Addison-Wesley. Chapters 1-4, 6-7.
- Gregg, B. (2016/2035). "The Flame Graph." *ACM Queue*. (The original flame graph paper; essential reading for understanding visualization.)
- Hoefler, T. & Belli, R. (2035). "Scientific Benchmarking of Parallel Computing Systems." *IEEE TPDS*. (On measurement rigor and statistical methodology.)

### Discussion Questions

1. Your teammate spent a week rewriting a sorting algorithm in assembly, achieving a 3× speedup. The sort accounts for 0.3% of total runtime. How do you have this conversation without destroying team morale? What process would have prevented this misallocation of effort?
2. A load test shows p50 latency of 50ms and p99 of 2000ms. The p50 is acceptable; the p99 is not. Where do you focus your investigation? What tools and visualizations would you use?
3. You add a caching layer and reduce average latency from 100ms to 10ms. But under cache warmup (when the cache is empty), latency spikes to 5000ms and the system times out. What went wrong? How do you design a cache that improves the common case without destroying the worst case?

---

ᚱ **Lecture 5: Security Hardening — Threat Modeling, Defense in Depth, and the Adversarial Mind**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

Security is not a feature you add at the end — it is a property you design in from the beginning and validate at every step. This lecture introduces **threat modeling**, the systematic practice of identifying what could go wrong and designing mitigations before attackers do. We cover the STRIDE framework (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege), **defense in depth** (multiple independent security controls so that the failure of one does not mean total compromise), and the **principle of least privilege** (every component should have only the permissions it needs, and no more). The lecture includes a hands-on threat modeling session where each team analyzes their own capstone system, identifies the three most likely attacks, and designs countermeasures. We also cover the OWASP Top 10 for 2040, the most common vulnerability classes in modern web applications, and practical techniques for preventing each.

### Key Topics

- **Threat Modeling with STRIDE:** A structured approach to identifying threats. For each component in your system, ask: How could an attacker spoof identity here? How could they tamper with data? How could they deny service? The output is a threat model document — a living artifact that evolves as the system changes. Tools: Microsoft's Threat Modeling Tool, OWASP Threat Dragon, or simple whiteboard diagrams with annotated trust boundaries.
- **Defense in Depth:** No single security control is perfect. Authentication prevents unauthorized access — but what if it fails? Authorization limits what authorized users can do — but what if it has a bug? Encryption protects data in transit — but what if the key is compromised? Defense in depth means layering controls: a WAF (Web Application Firewall) in front of the application, input validation at the API boundary, parameterized queries to prevent SQL injection, Content Security Policy headers to prevent XSS, and least-privilege database accounts so that a compromised application cannot drop tables.
- **The OWASP Top 10 (2040 Edition):** The most critical web application security risks. By 2040, the list has evolved: injection attacks (SQL, NoSQL, command, LDAP) remain #1; broken authentication and session management is #2; sensitive data exposure is #3; XML external entities (XXE) and insecure deserialization are #4; broken access control is #5; security misconfiguration is #6; cross-site scripting (XSS) is #7; insecure direct object references are #8; insufficient logging and monitoring is #9; and API-specific vulnerabilities (mass assignment, excessive data exposure, lack of rate limiting) round out #10.
- **Cryptographic Hygiene:** Never roll your own crypto. Use established libraries (libsodium, OpenSSL, NaCl) for encryption, hashing, and key derivation. Use **bcrypt** or **Argon2** for password hashing, never SHA-256 or MD5. Use authenticated encryption (AES-GCM, ChaCha20-Poly1305), not unauthenticated modes (AES-CBC without HMAC). Generate random tokens with cryptographically secure random number generators (`secrets` in Python, `crypto.randomBytes` in Node.js), not `Math.random()`. Rotate keys regularly and have a revocation plan.
- **Secrets Management:** API keys, database passwords, and private keys must never be committed to version control. Use environment variables for configuration, a secrets manager (HashiCorp Vault, AWS Secrets Manager, or the university's internal Yggdrasil Secret Vault) for credentials, and ** sealed secrets** or **SOPS** for encrypted secrets in Git. Scan your repository with `git-secrets` or `truffleHog` to detect accidentally committed credentials.

### Lecture Notes

The adversarial mindset is the security engineer's core competence: the ability to look at a system and ask not "how is this supposed to work?" but "how could I break this?" This mindset does not come naturally to most developers, who are trained to build things that work. Security requires you to temporarily become the enemy — to think like someone who wants to steal data, disrupt service, or gain unauthorized access.

**Threat modeling** is the formalization of this mindset. It is not about paranoia; it is about systematic imagination. Every threat model begins with a diagram: what are the components? What are the data flows? Where are the trust boundaries? Then, for each component and each flow, you apply STRIDE and ask the six questions. The result is not a guarantee of security — no system is perfectly secure — but it is a guarantee that you have thought about the most likely attacks and made them harder.

The capstone context adds a specific challenge: your system is new, your team is inexperienced, and your adversaries are not nation-states but curious users, automated scanners, and occasionally malicious actors on the open internet. You do not need military-grade security; you need **adequate security** — security proportional to the value of what you are protecting and the sophistication of the likely attackers. A student project that stores no financial data and has no authentication requirements does not need the same defenses as a banking system. But every system that handles user data has a duty of care, and negligence is not excused by "it's just a student project."

**Defense in depth** is the answer to the inevitability of bugs. Your code has bugs. Your dependencies have bugs. Your infrastructure has bugs. If your entire security posture rests on "our authentication code is correct," you are one bug away from total compromise. But if you have authentication AND input validation AND least-privilege database accounts AND encryption at rest AND a WAF AND logging, then an attacker must chain multiple exploits to succeed — and each additional exploit reduces the probability of success and increases the probability of detection.

The OWASP Top 10 is a living document that evolves as attackers find new techniques and defenders find new mitigations. The 2040 edition reflects the shift toward API-first architectures, AI-generated attacks (LLMs that can craft sophisticated phishing emails and fuzzing inputs), and the increased importance of supply chain security (compromised dependencies, as with the 2037 `xz` backdoor incident). The lesson is not to memorize the list but to understand the underlying patterns: trust boundaries, input validation, output encoding, and the principle that all input is malicious until proven otherwise.

### Required Reading

- Shostack, A. (2036). *Threat Modeling: Designing for Security*, 2nd Edition. Wiley. Chapters 1-5, 8-9.
- OWASP Foundation. (2040). *OWASP Top 10 — 2040 Edition*. https://owasp.org/Top10_2040/
- Wheeler, D.A. (2035). *Secure Programming HOWTO*. Available via Yggdrasil Security Library.

### Discussion Questions

1. Your capstone system has no authentication because "it's just a demo." A user discovers it, uploads inappropriate content, and the URL is shared publicly. Who is responsible? What design decisions would have prevented this?
2. Threat model your own capstone: identify the three most likely attacks and the three highest-impact attacks. Are they the same? What mitigations would you implement, and what is your prioritization?
3. A teammate wants to store user passwords with SHA-256 "because it's fast and we're not a bank." What is the actual risk? How do you explain why bcrypt/Argon2 matters even for low-value targets?

---

ᚲ **Lecture 6: Observability — Logging, Metrics, Traces, and the Illuminated System**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

A system that cannot be observed is a system that cannot be trusted. **Observability** — the property of a system that allows you to infer its internal state from its external outputs — is the foundation of reliable operations. This lecture covers the three pillars of observability: **logs** (discrete events: "user 42 logged in at 14:03"), **metrics** (numeric time-series: "HTTP request latency, p95, over the last hour"), and **traces** (end-to-end request flows: "request /api/order/123 passed through the load balancer, the API gateway, the order service, the payment service, and the database, taking 340ms total"). We discuss structured logging (JSON logs with consistent schemas), log levels and when to use them, metric naming conventions, distributed tracing with OpenTelemetry, and the construction of dashboards that tell a story rather than merely displaying numbers. The lecture includes a lab session where each team instruments their capstone with structured logging and a health-check endpoint.

### Key Topics

- **Structured Logging:** Plain text logs (`INFO: user logged in`) are human-readable but machine-hostile. Structured logs (`{"level":"info","event":"user_login","user_id":42,"timestamp":"2040-03-15T14:03:00Z"}`) are machine-parseable and enable powerful queries: "show me all login events for user 42 in the last 24 hours." Standards: ECS (Elastic Common Schema), OpenTelemetry Log Data Model. Every log entry should include: timestamp, severity, service name, trace ID (for correlation), and event-specific fields.
- **Log Levels and Discipline:** TRACE (extremely detailed, rarely enabled), DEBUG (development detail), INFO (normal operation), WARN (something unexpected but not fatal), ERROR (a failure that prevented an operation from completing), FATAL (the process is crashing). The discipline: INFO logs should allow you to reconstruct what the system did; ERROR logs should tell you exactly what failed and why; DEBUG logs should help you trace execution during development. In production, run at INFO; enable DEBUG only for specific components during investigations.
- **Metrics and Time-Series:** Counters (monotonically increasing: total requests), gauges (point-in-time values: current memory usage), and histograms (distributions: request latency buckets). The **RED method** for service health: Rate (requests per second), Errors (error rate), Duration (request latency). The **USE method** for resource health: Utilization (how busy is it?), Saturation (how much work is queued?), Errors (how often does it fail?). Tools: Prometheus for collection, Grafana for visualization.
- **Distributed Tracing:** A single user request may touch a dozen services. Without tracing, you cannot answer "where did the time go?" A **trace** is a tree of **spans**, each representing one operation in one service. Standards: W3C Trace Context, OpenTelemetry. Every outgoing request should propagate the trace context; every incoming request should start or continue a span. The result: a complete picture of request flow, latency breakdown by service, and identification of bottlenecks.
- **Alerting and On-Call:** Alerts should be actionable ("the database connection pool is exhausted — add connections or investigate leaks"), not informational ("CPU usage is high" — so what?). The **alert hierarchy**: page (wake someone up) for SLO violations; ticket (create a task) for anomalies; log (review in dashboard) for trends. Capstone projects do not need 24/7 on-call, but they should have at least one alert: "the system is down."

### Lecture Notes

Observability is the difference between "the system is broken and I have no idea why" and "the system is broken, and I can see that the database connection pool was exhausted at 14:03 after a burst of requests from the marketing campaign." The first situation leads to panic, guesswork, and hours of frustration. The second leads to a targeted fix: increase the pool size, add connection pooling to the cache layer, and set an alert for pool exhaustion.

**Structured logging** is the single most impactful observability practice for capstone projects. It requires almost no infrastructure (write JSON to stdout, collect with a simple log shipper) and pays enormous dividends. When a user reports a bug, you can search for their user ID and see every operation they performed. When an error occurs, you can find every log entry with the same trace ID and reconstruct the request path. When you need to understand performance, you can aggregate log entries by endpoint and compute latency distributions.

The discipline of log levels is often neglected. Teams that log everything at INFO produce noise that obscures signal. Teams that log errors but no context produce alerts that cannot be investigated. The correct approach: be generous with structured fields (include user IDs, request IDs, and relevant parameters) but disciplined with levels. An ERROR should always indicate a failure that requires human attention; if you can handle it automatically (retry, fallback, circuit breaker), it is a WARN at most.

**Distributed tracing** is essential for any capstone with more than one service. Even a frontend + backend + database architecture benefits from tracing: you can see how long the frontend spends rendering, how long the backend spends processing, and how long the database spends querying. Without tracing, these times are lumped into a single "page load time" metric, and you cannot tell whether the problem is in the JavaScript, the API, or the SQL.

The art of dashboard design is underappreciated. A good dashboard tells a story: "here is the health of the system, here is the trend over time, here is the detail you need when something goes wrong." A bad dashboard is a wall of numbers that requires expert interpretation. The Yggdrasil standard capstone dashboard has four panels: request rate and error rate (RED), latency distribution (p50/p95/p99), resource utilization (CPU/memory), and the most recent errors with links to traces. This is enough to answer 90% of operational questions.

### Required Reading

- Majors, C., Fong-Jones, L., & Miranda, G. (2037). *Observability Engineering: Achieving Production Excellence*. O'Reilly. Chapters 1-4, 7-8.
- OpenTelemetry Project. (2040). *OpenTelemetry Documentation*. https://opentelemetry.io/docs/
- Yggdrasil DevOps Standards v3.1 (2040). "Observability Requirements for Capstone Projects."

### Discussion Questions

1. Your logs are all plain text. You need to answer "how many users encountered error X in the last hour?" How long does this take? What would structured logging change?
2. You have 100 metrics but no alerts. During the demo, the system fails silently — requests timeout, but no one notices until a user complains. What is the minimum viable alerting setup for your capstone?
3. A trace shows that 90% of request latency is in the database. But the database metrics show low CPU and no slow queries. What could explain this discrepancy? How do you investigate?

---

ᚷ **Lecture 7: Documentation and Technical Communication — The Craft of Explanation**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

Code that cannot be explained cannot be maintained. Documentation is not an afterthought — it is an act of empathy for your future self, your teammates, your successors, and your users. This lecture covers the full documentation lifecycle: README files that explain what the system does and how to run it, architecture decision records (ADRs) that capture why the system is built the way it is, API documentation that enables integration, operational runbooks that guide incident response, and the final capstone report that synthesizes a semester of work into a coherent narrative. We emphasize **documentation-driven development** — writing the README and API docs before writing the code, ensuring that the system is explainable from the start.

### Key Topics

- **The README as Contract:** Every repository must have a README that answers, in order: What is this? (one sentence), What does it do? (one paragraph), How do I run it? (copy-paste commands), How do I configure it? (environment variables, config files), How do I contribute? (development setup, test commands), and Where do I get help? (issue tracker, contact). The README is the first impression; if it is wrong or incomplete, users will abandon the project before they discover its merits.
- **Architecture Decision Records (ADRs):** Short documents (1-2 pages) that capture a significant architectural decision: the context (what problem were we solving?), the decision (what did we choose?), the consequences (what do we gain and lose?), and the status (accepted, superseded). ADRs live in `docs/adr/` and are numbered sequentially. They prevent the endless re-debate of settled questions and provide newcomers with the historical context they need to understand the codebase.
- **API Documentation:** For REST APIs, OpenAPI (Swagger) specifications that define every endpoint, parameter, request body, response schema, and error code. For GraphQL APIs, schema documentation with descriptions for every type and field. For library APIs, inline documentation (JSDoc, rustdoc, Sphinx) that generates searchable HTML. The standard: every public function, class, and endpoint must be documented; every parameter must have a type and description; every error response must be listed.
- **Operational Runbooks:** Step-by-step guides for common operational tasks: "how to deploy a new version," "how to restore from backup," "how to add a new user," "how to respond to alert X." Runbooks are not substitutes for automation — they are scaffolding for automation. Every runbook should include: prerequisites, exact commands, expected output, rollback procedure, and escalation path.
- **The Capstone Report:** The final deliverable: a 20-30 page document that tells the story of the project. Structure: Abstract (what we built and why), Introduction (problem domain and motivation), Related Work (what exists and how we differ), Design (architecture and key decisions), Implementation (technologies and challenges), Evaluation (performance, user testing, SLO achievement), Discussion (lessons learned, limitations, future work), and Conclusion. The report is not a dump of everything you did; it is a curated narrative that demonstrates engineering judgment.

### Lecture Notes

Documentation is the most undervalued skill in software engineering. Brilliant coders who cannot explain their work find their influence limited; competent coders who write clearly find their work adopted, maintained, and extended. The ability to explain complex technical ideas in accessible prose is rarer than the ability to write complex code, and it is more valuable in the long run.

**Documentation-driven development** flips the typical workflow. Instead of writing code and then documenting it, you write the documentation first — the API specification, the README, the setup instructions — and then write code that satisfies the documentation. This ensures that the system is explainable: if you cannot explain what a function does before writing it, you do not understand what it should do. It also ensures that documentation stays current: when the code changes, the documentation is already there as a reference, and discrepancies are obvious.

The README is the most important document in the repository. It is the contract between the authors and the users. A README that says "clone and run `npm start`" when the actual command is `docker-compose up --build` has breached that contract, and the user's trust is damaged. The README should be tested like code: have a fresh machine (or a CI job) follow the instructions exactly and verify that the system comes up. If the instructions fail, it is a bug — fix it with the same urgency as a production outage.

**ADRs** are the institutional memory of the project. Every significant decision — "we chose PostgreSQL over MongoDB," "we adopted GraphQL over REST," "we moved from AWS to the university's private cloud" — should be recorded. The format is simple: Context, Decision, Consequences, Status. The value is enormous: six months later, when a new team member asks "why didn't we use X?", you point them to ADR-0007 and the conversation is over. Without ADRs, teams re-litigate the same decisions endlessly, wasting energy and creating conflict.

The capstone report is a specific genre: it is not a research paper (no literature review of 200 sources), not a user manual (no step-by-step screenshots), and not a blog post (no casual anecdotes). It is an engineering narrative: here is a problem, here is how we approached it, here is what we built, here is how well it works, here is what we learned. The best reports read like stories with technical depth: the reader understands not just what the team did, but why they made each choice and what they would do differently.

### Required Reading

- Nygard, M. (2036). *Documenting Software Architectures: Views and Beyond*, 2nd Edition. Addison-Wesley. Chapters 1-3, 7-8.
- Yggdrasil Capstone Handbook (2040 Edition), Chapter 12: "The Capstone Report — Structure, Style, and Submission."
- Orwell, G. (1946/2035). "Politics and the English Language." (A classic essay on clear writing; assigned in every Yggdrasil technical communication course.)

### Discussion Questions

1. Your README has not been updated since Week 2. The setup instructions no longer work. A new teammate spends three hours trying to follow them before asking for help. What process would prevent this? What is the cost of out-of-date documentation?
2. Your team is debating whether to use PostgreSQL or MongoDB. Write a one-page ADR that captures this decision. What belongs in the Consequences section?
3. The capstone report has a 30-page limit. You have 50 pages of material. What do you cut, and what criteria do you use? Is depth or breadth more important?

---

ᚹ **Lecture 8: User Experience and Interface Polish — The Human at the Center**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

A system that works perfectly but is painful to use will not be used. **User experience (UX)** is the craft of designing systems that are not merely functional but delightful — intuitive, responsive, accessible, and aesthetically coherent. This lecture covers the intersection of engineering and design: performance as UX (perceived vs. actual speed), error messaging (turning failures into guidance), accessibility (designing for users with disabilities), responsive design (adapting to devices and contexts), and the **polish** that transforms a working system into a professional product. We introduce the **heuristic evaluation** method — a structured review of a UI against established usability principles — and conduct a peer evaluation of each team's interface.

### Key Topics

- **Performance as Perception:** Actual speed and perceived speed are different. A page that loads in 2 seconds feels instant if it shows a skeleton screen immediately and streams content progressively. A page that loads in 500ms feels slow if it shows a blank screen until everything is ready. Techniques: skeleton screens, progressive enhancement, optimistic UI (showing the result before the server confirms), and perceived performance budgets (the user should see something meaningful within 200ms of interaction).
- **Error Messaging as Guidance:** Errors are inevitable; how you present them determines whether users recover or abandon. A good error message explains: what happened (in plain language), why it happened (the root cause, not the symptom), and what to do next (a specific action). Compare "Error 500" (bad) with "We couldn't save your document because the server is temporarily overloaded. Your changes are safe in local storage. Please try again in 30 seconds." (good). Never blame the user ("you entered invalid data"); blame the system ("we couldn't process that format").
- **Accessibility (a11y):** Designing for users with visual, auditory, motor, and cognitive disabilities. Standards: WCAG 2.2 AA (the minimum legal standard in most jurisdictions by 2040). Practices: semantic HTML (screen readers depend on it), keyboard navigation (every interactive element must be reachable without a mouse), color contrast (4.5:1 for normal text, 3:1 for large text), alt text for images, focus indicators, and ARIA labels where semantics are insufficient. Accessibility is not a feature — it is a civil right.
- **Responsive and Adaptive Design:** The system must work on desktops, tablets, phones, and (increasingly in 2040) AR/VR headsets and automotive displays. Responsive design uses fluid grids and media queries to adapt layout; adaptive design serves different experiences based on device capabilities. The capstone standard: the system must be usable on a phone and a desktop without horizontal scrolling or unreadable text.
- **Polish and Micro-interactions:** The details that signal professionalism: consistent spacing and typography, hover states that confirm clickability, loading indicators that show progress, transitions that orient the user, and empty states that guide rather than confuse. The "delight" layer: easter eggs, personalized greetings, and small moments of personality that make the system feel crafted rather than generated.

### Lecture Notes

Engineers often dismiss UX as "making things pretty" — a superficial layer applied after the real work is done. This is a catastrophic misunderstanding. UX is the **human interface** to your engineering, and if the interface is hostile, the engineering might as well not exist. The most sophisticated backend system, the most elegant algorithm, the most robust infrastructure — all are worthless if users cannot figure out how to accomplish their goals.

**Perceived performance** is the battleground of modern UX. By 2040, users expect immediate feedback. The 200ms threshold is well-established: any interaction that takes longer than 200ms without feedback feels broken. But actual computation often takes longer than 200ms. The solution is to separate feedback from completion: show the user that their action was received immediately (button press animation, optimistic state update), then complete the work asynchronously. The user perceives speed; the system preserves correctness.

Error messaging is where engineering empathy is most visible. A system that crashes with a stack trace is saying "I failed, and I don't care if you understand why." A system that explains the failure and guides recovery is saying "I failed, but I'm on your side, and here's how we fix it together." The difference is not technical — both require catching the exception — but it is the difference between a tool and a companion.

**Accessibility** is non-negotiable in 2040. Regulatory frameworks (the European Accessibility Act, the U.S. Section 508 refresh, and Yggdrasil's own accessibility pledge) require digital services to be usable by people with disabilities. But accessibility is not just compliance — it is good design. A system that works with a keyboard is more robust. A system with good color contrast is more readable in sunlight. A system with semantic HTML is more maintainable. The curb-cut effect: accessibility features benefit everyone.

Polish is the final 10% that takes 50% of the time — and it is time well spent. A system that works but looks amateur undermines trust. Users unconsciously generalize from visual quality to functional quality: if the interface is sloppy, they assume the code is sloppy. The inverse is also true: a polished interface creates confidence. The "it just works" feeling comes not from absence of bugs but from the accumulation of small correct details.

### Required Reading

- Krug, S. (2037). *Don't Make Me Think: A Common Sense Approach to Web Usability*, 4th Edition. New Riders. (A classic; the principles remain unchanged even as the technologies evolve.)
- Wachter-Boettcher, S. (2035). *Technically Wrong: Sexist Apps, Biased Algorithms, and Other Threats of Digital Inclusivity*. Beacon Press.
- W3C. (2040). *Web Content Accessibility Guidelines (WCAG) 2.2*. https://www.w3.org/WAI/WCAG22/

### Discussion Questions

1. Your system has a 3-second API call. The UI currently shows a spinner. How would you redesign this to feel faster without actually making the API faster?
2. A user with a screen reader reports that your form is unusable. You have never used a screen reader. What is your debugging process? What tools do you use?
3. Your teammate says "accessibility is not our priority — we have too many features to finish." What evidence and arguments would you use to change their mind? What is the minimum viable accessibility effort for the capstone?

---

ᚺ **Lecture 9: Release Engineering and Deployment Strategies — Shipping with Confidence**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

Releasing software is a ritual — a sequence of steps that transforms code into a running system that users can access. This lecture covers the engineering of that ritual: release versioning (semantic versioning and its discontents), release notes (communicating change), deployment strategies (blue-green, canary, rolling, feature flags), database migrations (the most dangerous operation in software deployment), rollback procedures (the safety net), and the **deployment checklist** (a final verification before go-live). We emphasize that deployment is not the end of development but the beginning of operations — the moment when the system faces real users, real data, and real failure modes.

### Key Topics

- **Semantic Versioning (SemVer):** A version number of `MAJOR.MINOR.PATCH` communicates compatibility: increment MAJOR for breaking changes, MINOR for backward-compatible features, PATCH for backward-compatible fixes. The controversy: what counts as "breaking"? Removing a deprecated endpoint is breaking; changing the sort order of an undocumented field is arguably not. Capstone projects should use `0.x.y` during development and `1.0.0` for the first stable release at the symposium.
- **Release Notes:** A communication artifact that tells users and stakeholders what changed, why it matters, and what they need to do. Structure: summary (one paragraph), new features (with examples), improvements (performance, reliability), bug fixes (with issue references), breaking changes (with migration guidance), and deprecations (with replacement recommendations). Release notes are not changelogs (which are exhaustive lists of commits); they are curated narratives that respect the reader's time.
- **Database Migrations:** The operation that cannot be rolled back instantly. Migration strategies: backward-compatible migrations (add columns before removing them, support both old and new schemas during transition), the expand-contract pattern (deploy code that writes to both schemas, migrate data, deploy code that reads from the new schema, remove old schema), and the **migration safety checklist**: backup before migrate, test migrate on a copy of production data, verify application compatibility, monitor for errors post-migrate, and have a rollback plan (which, for schema changes, often means restoring from backup rather than reversing the migration).
- **Feature Flags:** Decoupling deployment from release. A feature flag is a configuration toggle that enables or disables a feature without deploying new code. This allows: gradual rollout (5% of users see the new feature), A/B testing (measure engagement between variants), instant rollback (disable a feature that causes errors without redeploying), and trunk-based development (merge incomplete features to main without exposing them). Tools: LaunchDarkly, Unleash, or simple configuration files for capstone scale.
- **The Deployment Checklist:** A final verification before go-live: all tests pass, the build is reproducible, the database is backed up, the monitoring is active, the runbook is current, the rollback procedure is tested, and the team is available for incident response. The checklist is not bureaucracy — it is the accumulated wisdom of every deployment that went wrong because someone forgot one of these steps.

### Lecture Notes

Release engineering is the discipline of making deployment boring — so routine and reliable that it becomes unremarkable. The goal is that anyone on the team can deploy at any time with confidence. This requires automation (no manual steps that can be forgotten), verification (tests that confirm the deployment succeeded), and observability (monitoring that detects problems before users do).

**Semantic versioning** is simple in theory and complex in practice. The core ambiguity is "breaking change." A change that breaks one user's workflow may not affect another. The pragmatic rule: if a change could break any reasonable usage of the API, it is breaking. When in doubt, bump the major version. The cost of a major version bump is trivial; the cost of breaking a user's integration is significant.

**Database migrations** are the most dangerous part of deployment because they are the least reversible. Code can be rolled back by changing a configuration or redeploying an old container. Schema changes require careful choreography. The expand-contract pattern is the gold standard: never remove a column in the same deployment that stops using it. Instead, deploy code that writes to both old and new columns, run a data migration to backfill the new column, deploy code that reads from the new column, and only then remove the old column. This pattern requires patience (three deployments instead of one) but eliminates the risk of data loss.

**Feature flags** are transformative for capstone projects because they allow incremental delivery. A team that cannot use feature flags must complete an entire feature before merging it, leading to long-lived branches and painful integrations. A team that uses feature flags can merge partial features to main, deploy them disabled, and enable them when ready. If a feature causes problems at the demo, it can be disabled in seconds without a code change.

The deployment checklist is insurance against optimism. Every team believes "this deployment will be fine" — and most are right, until they aren't. The checklist forces a pause: have we backed up? Are the alerts working? Does everyone know the rollback command? This pause takes five minutes and can save hours of outage.

### Required Reading

- Humble, J. & Farley, D. (2038). *Continuous Delivery*, 3rd Edition. Chapters 8-10: "Versioning," "Releasing," and "Database Migrations."
- Naur, P. & Randell, B. (1968/2035). "Software Engineering: Report of a Conference." (The original concept of "software engineering"; read the section on "the programming process" for historical context.)
- Yggdrasil DevOps Standards v3.1 (2040). "Release Management and Database Migration Safety."

### Discussion Questions

1. Your team wants to remove a deprecated API endpoint. A partner team still uses it. What is your migration timeline? How do you communicate the change? What tools ensure they receive the message?
2. A migration fails halfway through, leaving the database in an inconsistent state. The backup is from six hours ago. What is your recovery procedure? What would have prevented this?
3. Feature flags sound useful, but your teammate worries they add complexity and "if code is ready, we should just release it." What are the specific risks of always coupling deployment and release? When is it safe to release without a flag?

---

ᚾ **Lecture 10: Team Dynamics Under Pressure — Collaboration When It Matters Most**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

The final weeks of a capstone project are the most demanding — and the most revealing. Under pressure, team dynamics either strengthen or fracture. This lecture addresses the human side of software engineering: managing conflict, giving and receiving feedback, making decisions under uncertainty, supporting teammates who are struggling, and maintaining psychological safety when stakes are high. We draw on research from organizational psychology, the software engineering literature on team performance, and the accumulated wisdom of a decade of Yggdrasil capstone cohorts. The lecture includes a retrospective workshop where each team reflects on their collaboration patterns and identifies one concrete change for the final sprint.

### Key Topics

- **Psychological Safety:** The belief that the team is safe for interpersonal risk-taking — asking questions, admitting mistakes, disagreeing with the majority. Google's Project Aristotle (2012-2015) found that psychological safety was the single strongest predictor of team effectiveness, outperforming every other factor. Practices: explicit permission to be wrong, celebration of "good failures" (experiments that produced learning), and no punishment for honest mistakes.
- **Constructive Feedback:** The art of delivering criticism that helps rather than harms. The **SBI model** (Situation-Behavior-Impact): "In yesterday's code review [situation], you dismissed my performance concern without examining the benchmark [behavior], which made me feel that my contributions weren't valued [impact]." Contrast with destructive feedback: "you never listen." The goal is behavior change, not venting.
- **Decision-Making Under Pressure:** The cognitive biases that emerge when deadlines loom: sunk cost fallacy ("we've invested too much to change course"), groupthink ("everyone agrees, so I won't dissent"), and optimism bias ("we'll figure it out"). Countermeasures: the **premortem** (imagine it is two weeks after the deadline and the project failed; what went wrong?), the **devil's advocate** (assign someone to argue against the preferred option), and **timeboxing** ("we will decide in 30 minutes, then commit").
- **Supporting Struggling Teammates:** The signs of burnout (irritability, withdrawal, declining quality, missed meetings) and how to respond. The conversation: private, non-judgmental, specific ("I've noticed you've missed the last three standups; is everything okay?"), and offering concrete support ("can I take the frontend tasks for this week?"). The boundary: you are a teammate, not a therapist. Know when to involve the instructor or university support services.
- **The Final Sprint:** The last two weeks require a different rhythm: daily standups, clear ownership of critical paths, explicit "no new features" policy after a certain date, and a shared understanding that the goal is "done and demoable," not "perfect." The **definition of done** for the capstone: code is committed, tests pass, documentation is current, the system is deployed, and the presentation is rehearsed.

### Lecture Notes

Software engineering is a team sport, and the capstone is the championship game. The teams that succeed are not necessarily the ones with the most talented individual contributors; they are the ones that collaborate most effectively. Collaboration is a skill, and like any skill, it can be learned, practiced, and improved.

**Psychological safety** is the foundation. In a team with high psychological safety, a junior member can say "I don't understand why we chose PostgreSQL" without fear of being labeled stupid. In a team without it, that question goes unasked, and the team may spend months with the wrong database because no one felt safe to challenge the initial decision. The instructor's role is to model and enforce psychological safety; the team members' role is to practice it daily.

**Constructive feedback** is the lubricant of team improvement. Without it, teams repeat the same mistakes. With destructive feedback, teams fracture and members withdraw. The SBI model works because it is specific and non-accusatory. It describes behavior rather than character ("you did X" not "you are X") and explains impact rather than assigning blame. The recipient's responsibility is to listen, ask clarifying questions, and commit to a specific change. Feedback is a gift — but it must be wrapped carefully.

The **premortem** is a powerful technique for capstone teams because it legitimizes doubt. In normal team culture, expressing concerns about success can be seen as negativity. The premortem reframes it: "we are going to imagine we failed, and we are going to be very specific about why." This surfaces risks that optimism suppresses and gives the team time to mitigate them. The team that conducts a premortem in Week 10 and discovers "our database migration has never been tested on real data" can fix that problem with time to spare. The team that skips the premortem discovers the same problem on demo day.

**Burnout** is real and common in capstone projects. The combination of high stakes, tight deadlines, and unclear boundaries ("I should just work one more hour") pushes students beyond sustainable effort. The signs are visible if you know to look: a teammate who was enthusiastic becomes cynical; a reliable contributor starts missing deadlines; quality declines in someone who previously cared deeply. The response must be early and supportive, not punitive. The best teams redistribute work before burnout becomes crisis.

### Required Reading

- Edmondson, A. (2036). *The Fearless Organization: Creating Psychological Safety in the Workplace*, 2nd Edition. Wiley.
- Dweck, C. (2035). *Mindset: The New Psychology of Success*, Updated Edition. Ballantine Books. (On growth mindset and response to failure; assigned across Yggdrasil's engineering curriculum.)
- UoY Student Wellness Office. (2040). "Recognizing and Responding to Burnout: A Guide for Team Members." Available via Yggdrasil Student Portal.

### Discussion Questions

1. Your team is divided on a major architectural decision. Two members want to refactor; two want to ship the current design. The deadline is in three weeks. How do you resolve this? What decision-making process do you use, and how do you ensure the dissenting members remain engaged?
2. You notice a teammate is increasingly withdrawn and irritable. Their code quality has dropped. How do you approach this conversation? What do you say, and what do you avoid saying?
3. The premortem reveals that your biggest risk is "the demo fails because of an untested integration." What specific actions do you take in the next 48 hours to mitigate this risk? What do you deprioritize to make time?

---

ᛁ **Lecture 11: The Final Presentation — Communicating Technical Work to Any Audience**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

The capstone symposium is the culmination of eight months of work — and the presentation is how that work is received, understood, and remembered. This lecture covers the craft of technical presentation: audience analysis (who are you speaking to and what do they care about?), narrative structure (telling a story, not reciting features), demonstration technique (live demos that impress rather than embarrass), visual design (slides that support rather than distract), and Q&A handling (responding to challenge with grace). We analyze recordings of past symposium presentations — both exemplary and cautionary — and each team rehearses their presentation in front of the cohort.

### Key Topics

- **Audience Analysis:** The symposium audience includes faculty (who care about engineering rigor), industry mentors (who care about feasibility and market fit), fellow students (who care about cool features and lessons learned), and family members (who care about what you actually did in plain language). A single presentation cannot serve all audiences equally. The solution: a primary audience (usually faculty and industry mentors) with layered detail that serves secondary audiences.
- **Narrative Structure:** The story arc: Hook (why does this matter?), Problem (what pain did you address?), Approach (how did you tackle it?), Demo (show, don't tell), Challenges (what went wrong and how did you adapt?), Results (what did you achieve?), and Future (what would you do next?). The anti-pattern: feature recitation ("we have a login page, and a dashboard, and a settings page..."). The pattern: transformation ("users used to spend hours on X; now they spend minutes").
- **Live Demonstration Technique:** The demo is the most memorable part of the presentation — and the riskiest. Rules: never demo unrehearsed paths, have a video backup (record the demo in advance, in case of network failure), practice the exact clicks and typing, and narrate what you are doing ("I am logging in as a test user..."). The "wow moment": one feature that surprises and delights the audience, demonstrated with flair.
- **Visual Design:** One idea per slide. Minimal text (no more than 25 words per slide). Large, legible fonts (minimum 24pt). High-contrast color schemes. Diagrams over bullet points. The slide is a visual aid, not a teleprompter. If you are reading from your slides, your slides are too verbose.
- **Q&A Handling:** The question period is not an interrogation — it is a conversation. Listen fully before answering. If you don't know, say so ("that's an excellent question that we didn't investigate; our hypothesis would be..."). If a question is hostile, respond to the substance, not the tone ("I understand the concern about scalability; our load testing showed..."). Never argue with a questioner; engage with their point.

### Lecture Notes

The presentation is not a summary of your report — it is a performance designed to create understanding and emotional engagement. The best presentations leave the audience thinking not "that was competent" but "that was compelling — I want to know more."

**Audience analysis** determines every other choice. A presentation to faculty should emphasize methodology, evaluation, and engineering trade-offs. A presentation to investors should emphasize market need, user validation, and competitive differentiation. A presentation to family should emphasize the human impact ("we built a system that helps teachers save hours of grading time"). The capstone symposium requires a hybrid: enough technical depth to satisfy faculty, enough user focus to satisfy industry mentors, and enough narrative clarity that non-technical attendees follow along.

The **narrative arc** is what separates memorable presentations from forgettable ones. Humans are story-shaped; we remember narratives, not lists. The story of your capstone is: there was a problem, you tried to solve it, you encountered obstacles, you adapted, and you achieved a result. This is the hero's journey, and your system — or your team — is the hero. Do not be afraid to discuss failure: "our initial architecture couldn't handle concurrent users, so we redesigned the session layer" is more impressive than "everything worked perfectly from the start." Adaptation demonstrates engineering maturity.

**Live demos** are high-risk, high-reward. A successful demo creates a visceral sense of "this is real" that no slide can match. A failed demo destroys credibility. The golden rule: demo only what you have rehearsed, on the exact hardware and network you will use. Have a fallback video. Have a local copy that does not depend on external services. The audience does not care that "the Wi-Fi was slow"; they care that your demo failed.

**Slide design** is a form of respect for your audience. A slide crowded with 50 words says "I don't care if you can read this." A slide with a single powerful diagram says "I have thought about how to communicate this clearly." The 25-word limit forces you to distill your message to its essence. If you cannot explain an idea in 25 words, you do not understand it well enough to present it.

The Q&A is where depth is revealed. A presenter who can answer technical questions with precision and conceptual questions with clarity demonstrates mastery. A presenter who deflects, bluffs, or becomes defensive undermines everything that came before. The correct posture: grateful for the question, honest about limits, and eager to engage. "I don't know, but here's how I would find out" is a stronger answer than a fabricated certainty.

### Required Reading

- Duarte, N. (2036). *Resonate: Present Visual Stories that Transform Audiences*, 2nd Edition. Wiley.
- Yggdrasil Capstone Handbook (2040 Edition), Chapter 13: "The Symposium Presentation — Preparation, Rehearsal, and Delivery."
- Reynolds, G. (2035). *Presentation Zen: Simple Ideas on Presentation Design and Delivery*, 3rd Edition. New Riders.

### Discussion Questions

1. Your presentation is 15 minutes. You have 30 minutes of material. What do you cut? What is your prioritization framework?
2. A faculty member asks a deeply technical question about an algorithmic choice you made in Week 3. You don't remember the details. How do you respond without losing credibility?
3. Your live demo depends on an external API that is rate-limited. During rehearsal, it works. During the actual presentation, you hit the rate limit. What is your backup plan? How do you communicate the failure to the audience?

---

ᛃ **Lecture 12: Reflection and Professional Growth — The Engineer You Are Becoming**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

The capstone ends, but the learning continues. This final lecture is a meditation on the journey from student to engineer — not the technical skills (which you have demonstrated) but the professional identity (which you are forming). We reflect on the capstone experience: what you built, what you learned, what you would do differently, and how this project fits into the larger arc of your career. The lecture introduces the concept of the **engineering portfolio** (a curated collection of work that demonstrates competence over time), the **personal retrospective** (a periodic self-assessment of skills, goals, and growth), and the **professional network** (the relationships you build that outlast any single project). The goal is not closure but commencement — the beginning of a career defined by continuous learning, ethical practice, and the craft of building things that matter.

### Key Topics

- **The Engineering Portfolio:** Your capstone is the centerpiece, but it is not the only piece. A strong portfolio includes: the project (with live demo and source code), the process (documentation, ADRs, test coverage reports), the presentation (symposium recording), and the reflection (what you learned). The portfolio is not a static document; it evolves as you gain new skills and complete new projects. The Yggdrasil Digital Portfolio Standard v2.0 provides a structured format that is recognized by employers and graduate programs across the Nordic tech sector.
- **Personal Retrospective:** A periodic (monthly or quarterly) self-assessment: what did I learn? What skills did I use? What skills do I need to develop? What patterns do I notice in my work (strengths, weaknesses, preferences)? The retrospective is private, honest, and actionable. It transforms experience into self-knowledge. Format: four questions from the agile retrospective — What went well? What could have gone better? What did I learn? What will I focus on next?
- **Ethical Engineering:** The responsibilities of the software engineer: building systems that respect user privacy, designing algorithms that do not amplify bias, considering the environmental impact of compute, and refusing to build systems that cause harm. The **Hippocratic Oath for Engineers** (various formulations; the Yggdrasil version emphasizes: "I will prioritize human welfare over technical elegance, I will be transparent about limitations and risks, I will respect the autonomy and dignity of those affected by my work").
- **Lifelong Learning:** The half-life of technical knowledge is shortening. A framework or library that is dominant today may be obsolete in five years. The engineer who survives is not the one who memorizes the most APIs but the one who learns how to learn: reading documentation, reading source code, experimenting with new technologies, and maintaining intellectual curiosity. The Yggdrasil alumni network provides continuing education resources, mentorship, and community for graduates.
- **The Norse Framing:** The capstone is not merely an academic requirement — it is a rite of passage, like the Viking youth who builds his first ship and sails it across the fjord. The ship will not be perfect; the voyage will not be smooth. But the builder has demonstrated that he can conceive, design, construct, and navigate a vessel of his own making. That demonstration is what transforms a learner into a practitioner. The Norns have woven this thread into your wyrd; what you do with it is yours to choose.

### Lecture Notes

The final lecture is not about code. It is about who you are becoming. The capstone has tested your technical skills, your collaboration, your resilience, and your communication. It has revealed your strengths and your growth edges. The question now is: what will you do with this knowledge?

**The engineering portfolio** is your professional narrative in material form. When you apply for a job, employers do not care about your GPA; they care about what you can build. A portfolio with a live demo, clean code, comprehensive tests, and thoughtful documentation says "I can build production software" more convincingly than any transcript. Maintain it. Update it. Treat it as a living artifact that represents your best self.

**Personal retrospectives** are the engine of growth. Most people repeat their mistakes because they never reflect on them. The retrospective forces reflection: why did that bug take three days to find? Why did that argument with my teammate escalate? Why did I procrastinate on that feature? The answers are not always comfortable, but they are always valuable. The engineer who retrospects monthly improves faster than the engineer who retrospects never.

**Ethical engineering** is not optional. The software you build shapes the world. A recommendation algorithm that amplifies extremism, a facial recognition system that misidentifies minorities, a social network that exploits psychological vulnerabilities — these are not neutral technologies. They are moral agents, and you are their author. The Yggdrasil curriculum embeds ethics throughout because technical skill without ethical judgment is dangerous. The engineer who can build anything but lacks the wisdom to choose what to build is a threat, not an asset.

**Lifelong learning** is the defining characteristic of the best engineers. The field changes too fast for static expertise. The goal is not to know everything but to know how to find out, to evaluate what you find, and to integrate it into your practice. Curiosity is the virtue that sustains a career. The engineer who stops learning becomes obsolete; the engineer who never stops learning becomes invaluable.

The Norse framing is not mere decoration — it is a worldview. The Vikings did not seek comfort; they sought competence. They did not fear failure; they feared cowardice. The capstone has been your voyage across the fjord. The ship you built may leak, the wind may have been against you, and you may have rowed more than you sailed. But you crossed. And on the far shore, you are no longer the person who watched ships from the beach. You are the person who builds them.

### Required Reading

- Sennett, R. (2035). *The Craftsman*. Yale University Press. (A philosophical meditation on craft, skill, and the human meaning of making things well.)
- UoY Ethics Committee. (2040). "The Engineer's Responsibility: A Yggdrasil Framework for Ethical Technology." Available via Yggdrasil Student Portal.
- Alumni Network. (2040). "Lifelong Learning Resources for Yggdrasil Graduates." Available via Yggdrasil Alumni Portal.

### Discussion Questions

1. Write your personal retrospective for the capstone: What went well? What could have gone better? What did you learn? What will you focus on in your next project?
2. You are offered a job building a system that you believe will cause social harm. The pay is excellent. Your team needs the income. What do you do? What principles guide your decision?
3. In five years, what do you want your portfolio to demonstrate? What projects, skills, and relationships do you need to build to get there?

---

## Final Examination Preparation

The CS407 final assessment is not a traditional examination. Instead, students submit a **Capstone Portfolio** and deliver a **Symposium Presentation** (20 minutes plus 10 minutes Q&A). The portfolio comprises:

1. **Production System:** The deployed, running application with CI/CD pipeline, monitoring, and documentation.
2. **Technical Report:** The capstone report (20-30 pages) documenting design, implementation, evaluation, and reflection.
3. **Source Code:** The complete codebase with tests, ADRs, and README.
4. **Process Evidence:** Git history, pull request discussions, team meeting notes, and the Capstone Contract from CS406.
5. **Individual Reflection:** A 5-page personal essay on what the student learned, how they contributed, and how they grew.

### Sample Portfolio Evaluation Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Functional Completeness | 20% | Does the system work? Are the core features implemented and demonstrable? |
| Engineering Quality | 20% | Is the code well-structured, tested, and documented? Are ADRs present and thoughtful? |
| Production Readiness | 15% | Is the system deployed? Is there CI/CD, monitoring, and a rollback plan? |
| Team Collaboration | 15% | Is there evidence of effective teamwork? Are conflicts resolved constructively? |
| Communication | 15% | Is the report clear? Is the presentation compelling? Are technical explanations accessible? |
| Growth & Reflection | 15% | Does the individual reflection demonstrate genuine learning and self-awareness? |

### Sample Essay Questions (Choose 4 of 8)

1. Compare your initial CS406 architecture with your final CS407 architecture. What changed, and why? What would you have done differently if you had known then what you know now?
2. Describe a significant technical failure during the capstone and how your team responded. What did you learn about resilience, both technical and human?
3. The Production Readiness Checklist contains 48 items. Which five items do you believe are most critical for a student capstone, and which five are least critical? Justify your selections with specific examples.
4. Your capstone system will be used by real people after the symposium. What is your responsibility to those users? How does your design reflect that responsibility?
5. Analyze your team's collaboration using the concepts from Lecture 10. What patterns of psychological safety, feedback, and decision-making were present? What would you change?
6. Choose one lecture from CS407 and explain how its content directly influenced a decision your team made. Be specific about the lecture, the decision, and the outcome.
7. The software industry in 2040 is grappling with AI-generated code, autonomous systems, and algorithmic accountability. How does your capstone fit into this landscape? What ethical considerations guided your design?
8. Imagine you are mentoring next year's capstone team. What is the single most important piece of advice you would give them, and what is the single most common mistake you would warn them against?

---

*"The ship is built not when the last plank is nailed, but when the builder trusts it to carry them across the sea." — Yggdrasil Capstone Tradition*
