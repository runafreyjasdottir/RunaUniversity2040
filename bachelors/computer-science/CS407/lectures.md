# CS407: Capstone Project II
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4  
**Description:** Implementation, testing, deployment, presentation

**Prerequisites:** CS406 Capstone Project I

---

## Lectures

ᚠ **Lecture 1: From Architecture to Implementation: Bridging Design and Code**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

This opening lecture addresses the critical transition between the design artifacts produced in CS406—architecture documents, component diagrams, and working prototypes—and the disciplined implementation phase that dominates Capstone Project II. By 2040, the software industry has learned, often through painful experience, that the gap between design and implementation is not a mere translation exercise but a site of genuine epistemic transformation. Requirements mutate, edge cases emerge, and the very act of writing executable code reveals ambiguities that no specification language can fully capture. Students will learn methodologies for managing this transition, including incremental refinement, tracer-bullet implementation, and the architectural feedback loop.

### Key Topics

- The epistemic gap between specification and executable code
- Incremental refinement strategies: tracer bullets, vertical slices, and walking skeletons
- Architectural feedback loops: when implementation forces design revision
- Managing technical debt during the capstone sprint
- Integration of CS406 design artifacts into implementation planning

### Lecture Notes

The transition from design to implementation has occupied software engineering theorists since the earliest structured programming debates of the 1960s. Frederick Brooks, in his seminal *The Mythical Man-Month* (1975, revisited in the 1995 anniversary edition), identified the essence of software as inherently complex, arguing that no representation can fully capture the behavior of a system before it is built. By 2040, this insight has been reinforced by decades of agile practice, formal methods, and AI-assisted development. The capstone student stands at this boundary, armed with an architecture document from CS406 and the mandate to produce a deployable system.

The **tracer-bullet methodology**, first popularized by Andrew Hunt and David Thomas in *The Pragmatic Programmer* (1999, updated 2019), remains relevant in 2040 despite the advent of neural program synthesis. The core idea is simple but profound: build a minimal end-to-end path through the system early, connecting all major components with placeholder logic. This "tracer" illuminates integration risks, reveals protocol mismatches, and provides a tangible artifact for stakeholder feedback. In the 2040 context, tracer bullets are often augmented by AI-generated scaffolding—large language models produce boilerplate interfaces, test stubs, and documentation drafts—but the student must understand which parts of the tracer are structural (load-bearing) and which are decorative (replaceable).

**Vertical slice implementation** takes the tracer bullet further by demanding that each slice be a fully functional, user-visible feature. Rather than building all database layers before any UI, a vertical slice might implement "user registration" from HTTP handler through validation, persistence, and response rendering. This approach, advocated by the Feature-Driven Development community and later absorbed into scaled agile frameworks, aligns naturally with capstone constraints: students have limited time and must demonstrate tangible progress at each milestone. The 2040 University of Yggdrasil capstone program requires at least three vertical slices by Week 6, each accompanied by a demo video and peer review.

The **architectural feedback loop** is perhaps the most sophisticated concept in this lecture. It recognizes that implementation is not merely the execution of a predetermined plan but a co-evolutionary process in which the act of building reshapes understanding of what should be built. Daniel Jackson's *Software Abstractions* (MIT Press, 2006, revised 2012) introduced the Alloy modeling language to catch design flaws before implementation, yet even Jackson acknowledges that formal models gain precision through iterative refinement. In 2040, this loop is instrumented by AI-assisted design-review tools—systems like *Mímir-Architect* (developed at UoY in 2038) that compare implementation commits against the Alloy or TLA+ specification, flagging deviations and suggesting reconciliations. Students must learn to treat these tools as collaborators, not oracles: the AI may suggest a design revision, but the student bears responsibility for understanding why the revision improves the system.

Managing technical debt during a capstone is a discipline of its own. Ward Cunningham's original metaphor (1992) described debt as a deliberate choice to ship suboptimal code for speed, with the expectation of repayment. In practice, students often accumulate debt unconsciously—through copy-paste, temporary workarounds that become permanent, and deferred refactoring. The 2040 capstone program requires a "debt ledger": a living document in which students record each incurred debt, its estimated interest (future cost), and a repayment schedule. This practice, derived from Martin Fowler's technical debt quadrant (2009) and extended by the *Yggdrasil Software Craftsmanship Guild*, ensures that debt remains visible and manageable rather than an invisible drag on project velocity.

### Required Reading

- Hunt, A., & Thomas, D. (2019). *The Pragmatic Programmer* (20th Anniversary Edition). Addison-Wesley. Chapters 2 ("Tracer Bullets") and 14 ("The Power of Plain Text").
- Jackson, D. (2012). *Software Abstractions: Logic, Language, and Analysis* (Revised Edition). MIT Press. Chapter 1 ("Introduction") and Chapter 7 ("Analysis").
- Cunningham, W. (1992). "The Wyrd Cash Program." Original technical debt metaphor, reprinted in *Yggdrasil Software Archaeology Review*, 2034.
- Freyjasdottir, R. G. (2038). "The Mímir-Architect Loop: AI-Augmented Design Refinement in Capstone Projects." *Journal of Yggdrasil Software Engineering*, 14(3), 201–219.
- University of Yggdrasil, Department of Computer Science (2040). "Capstone Technical Debt Ledger Template." Internal document, v4.2.

### Discussion Questions

1. Why does the act of writing executable code often reveal ambiguities that specification documents conceal? Is this a failure of specification languages, or an inherent property of software?
2. Compare tracer-bullet, vertical-slice, and walking-skeleton approaches. Under what capstone constraints might each be most appropriate?
3. How should a capstone team decide whether to accept Mímir-Architect's suggestion to revise the design? What criteria should govern human override of AI recommendations?
4. Is technical debt always bad? Under what circumstances might a capstone team deliberately choose to leave debt unpaid?

### Practice Problems

- Review your CS406 architecture document and identify three components most likely to require design revision during implementation. Write a one-page risk mitigation plan for each.
- Produce a tracer-bullet implementation for your capstone's most critical user journey. The tracer need not be production-quality, but all major subsystems must be connected.

---

ᚢ **Lecture 2: Test-Driven Development and Quality Assurance at Scale**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Quality assurance in 2040 extends far beyond manual testing and ad-hoc debugging. This lecture examines the mature discipline of test-driven development (TDD), property-based testing, mutation testing, and AI-augmented quality assurance. Students will learn to construct test suites that serve as executable specifications, detect regressions, and provide the confidence necessary for aggressive refactoring. The capstone requirement of ≥90% coverage is not arbitrary: it reflects industry standards for safety-critical and production-grade systems, and achieving it demands systematic testing strategy rather than post-hoc test writing.

### Key Topics

- Test-driven development: red-green-refactor cycle and its cognitive benefits
- Unit, integration, and end-to-end testing: the testing pyramid in 2040
- Property-based testing: from QuickCheck to Hypothesis and beyond
- Mutation testing: measuring test suite quality, not just coverage
- AI-augmented test generation: opportunities and dangers of synthetic tests

### Lecture Notes

Kent Beck's introduction of test-driven development in the late 1990s, crystallized in *Test-Driven Development by Example* (Addison-Wesley, 2002), transformed software engineering by making testing not a post-development verification activity but a design discipline. The red-green-refactor cycle—write a failing test, write minimal code to pass, refactor while keeping tests green—structures cognition as much as code. By 2040, neuroimaging studies conducted at the University of Trondheim (2034–2037) have confirmed that TDD practitioners exhibit reduced cognitive load during debugging, attributable to the externalization of intent that tests provide. The capstone student who adopts TDD is not merely following a fashion but engaging a practice with empirically validated cognitive benefits.

The **testing pyramid**, articulated by Mike Cohn in *Succeeding with Agile* (2009), remains the foundational heuristic for test portfolio composition: many fast unit tests, fewer integration tests, and a small number of slow end-to-end tests. By 2040, the pyramid has been refined for AI-native systems. Unit tests now cover not only functions but also prompt templates and model outputs: *behavioral contract tests* specify that a given LLM prompt, when provided inputs within a defined range, must produce outputs satisfying certain constraints (e.g., JSON schema compliance, toxicity score below threshold). Integration tests must account for stochastic model behavior: rather than asserting exact equality, they assert statistical properties over repeated invocations. The UoY capstone framework provides `pytest-ai-contract`, a plugin for specifying and verifying these behavioral contracts.

**Property-based testing** generalizes the example-based approach of traditional TDD. Instead of testing with hand-chosen inputs, the developer specifies properties that the system must satisfy, and the testing framework generates thousands of random inputs to search for violations. QuickCheck, developed by Koen Claessen and John Hughes at Chalmers University of Technology (2000), pioneered this approach for Haskell. By 2040, Python's Hypothesis library (maintained by the DrMacIver consortium) supports not only scalar generation but also the generation of valid program ASTs, database states, and concurrent execution schedules. For capstone projects involving complex data structures or stateful protocols, property-based testing often reveals bugs that example-based tests miss. The lecture includes a live demonstration in which a seemingly correct binary search tree implementation fails under Hypothesis-generated sequences of insertions and deletions.

**Mutation testing** addresses the coverage trap: a test suite may achieve 100% line coverage yet fail to detect meaningful faults. Mutation testing introduces artificial faults (mutants) into the codebase and checks whether the test suite catches them. A mutation score—the percentage of mutants killed—provides a more nuanced measure of test quality than coverage alone. In 2040, mutation testing has become practical for medium-sized projects through tools like `mutmut` (Python) and `cargo-mutants` (Rust). The UoY capstone program requires a mutation score of ≥75% for the core logic modules. Students are warned, however, that mutation testing is computationally expensive and must be run on CI infrastructure rather than developer laptops. The lecture covers strategies for incremental mutation testing (testing only changed code) and equivalent mutant detection (mutants that are semantically identical to the original, which should be excluded from scoring).

**AI-augmented test generation** represents the frontier. Tools like GitHub Copilot (2021), evolved by 2040 into autonomous test-writing agents, can generate test cases from implementation code, natural language descriptions, or formal specifications. The danger is over-reliance: AI-generated tests often cover the happy path and rare edge cases but miss domain-specific invariants that only a human developer understands. The 2039 *Copenhagen Test Integrity Incident*, in which an AI-generated test suite falsely reported 98% coverage while missing a critical race condition, serves as a cautionary tale. Capstone students are permitted to use AI test generation but must manually review every generated test, annotate it with the invariant it verifies, and commit it under their own authorship.

### Required Reading

- Beck, K. (2002). *Test-Driven Development by Example*. Addison-Wesley. Chapters 1–3 (complete red-green-refactor walkthrough).
- MacIver, D., & Hatfield-Dodds, Z. (2031). "Property-Based Testing in the Age of Foundation Models." *ACM Computing Surveys*, 53(4), 1–34.
- Offutt, A. J., & Untch, R. H. (2001). "Mutation 2000: Uniting the Orthogonal." *Mutation Testing for the New Century*, 34–44.
- Yggdrasil Software Integrity Board (2039). "The Copenhagen Test Integrity Incident: Lessons for AI-Augmented QA." *Yggdrasil Safety Report* 2039-07.
- University of Yggdrasil (2040). "pytest-ai-contract: Behavioral Contract Testing for AI-Native Systems." Documentation v2.1.

### Discussion Questions

1. Neuroimaging evidence suggests TDD reduces cognitive load during debugging. What cognitive mechanisms might explain this effect? Does it apply equally to all problem domains?
2. How should property-based testing be integrated with example-based tests in a capstone project? Is there an optimal ratio?
3. The Copenhagen Incident involved AI-generated tests with high coverage but low fault detection. What structural properties of AI-generated tests make them prone to this failure mode?
4. Should mutation testing be required for all capstone projects, or only those with safety-critical components? Justify your position.

### Practice Problems

- Implement a property-based test suite for a core data structure in your capstone using Hypothesis. Generate at least five distinct properties and run 10,000 iterations per property.
- Run mutation testing on your capstone's most critical module. Report your mutation score, identify any surviving mutants, and determine whether they represent genuine test weaknesses or equivalent mutants.

---

ᚦ **Lecture 3: Continuous Integration, Delivery, and Deployment Pipelines**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

This lecture examines the CI/CD/CD triad—Continuous Integration, Continuous Delivery, and Continuous Deployment—as the industrial backbone of modern software production. By 2040, these practices have evolved from boutique agile techniques to infrastructural necessities. Students will learn to construct pipelines that automate building, testing, security scanning, and deployment, with particular attention to the reproducibility and auditability requirements of production systems. The lecture also covers feature flags, canary deployments, and rollback strategies essential for safe capstone deployment.

### Key Topics

- CI/CD/CD definitions and distinctions: integration, delivery, deployment
- Pipeline as code: GitHub Actions, GitLab CI, and self-hosted runners
- Reproducible builds: deterministic compilation, lockfiles, and containerized environments
- Security scanning in CI: SAST, DAST, dependency vulnerability detection
- Deployment strategies: blue-green, canary, feature flags, and rollback

### Lecture Notes

The origins of continuous integration trace to Kent Beck's Extreme Programming (1996) and Martin Fowler's influential 2000 article, which defined CI as the practice of integrating code into a shared repository several times a day, verified by automated builds. By 2040, CI has become so embedded in software engineering that its absence signals amateur practice. Yet the sophistication of 2040 CI far exceeds the simple "build and test" of the 2010s. A modern CI pipeline at the University of Yggdrasil includes: type checking, linting, unit tests, integration tests, property-based tests, mutation testing, SAST (static application security testing), DAST (dynamic application security testing), dependency vulnerability scanning, license compliance checking, documentation generation, and artifact signing. Each stage must complete in under 15 minutes to maintain developer flow state—a constraint that drives parallelization and incremental execution.

**Pipeline as code** is the dominant paradigm. GitHub Actions, introduced in 2018, and GitLab CI, introduced in 2015, both represent workflows as YAML documents stored in version control. By 2040, the industry has learned hard lessons about YAML's fragility: the 2031 *GitHub Actions Outage* (in which a YAML parsing bug caused a 6-hour global CI blackout) accelerated adoption of typed pipeline languages. The UoY capstone program provides a `ci-dsl` compiler that translates a statically typed, JSON-schema-validated pipeline definition into platform-native YAML. Students must write their capstone CI configuration in this DSL, ensuring type safety and enabling IDE autocomplete. The lecture walks through a complete capstone pipeline definition, from checkout to deployment.

**Reproducible builds** are essential for scientific integrity and security. A build is reproducible if, given the same source code and build environment, it produces bit-for-bit identical artifacts. The Reproducible Builds project, launched by Debian in 2013, achieved widespread adoption by 2025. In 2040, reproducibility is enforced by cryptographic build provenance: every artifact is accompanied by a SLSA (Supply Chain Levels for Software Artifacts) attestation, signed by the CI system, that records the exact source commit, build environment hash, and dependency tree. Capstone projects must achieve SLSA Level 2 (signed provenance, hosted build) and are encouraged to pursue Level 3 (hardened build platform, two-party review). The lecture demonstrates how to configure `goreleaser`, `cargo-release`, or Python's `build` backend to produce SLSA-compliant artifacts.

**Security scanning in CI** has become non-negotiable. SAST tools (Semgrep, CodeQL, SonarQube) analyze source code for known vulnerability patterns without executing the program. DAST tools (OWASP ZAP, Burp Suite Enterprise) exercise the running application to find runtime vulnerabilities. By 2040, these categories have been supplemented by **IAST** (interactive application security testing, which instruments the application to detect vulnerabilities during test execution) and **RASP** (runtime application self-protection, which blocks attacks in production). The UoY capstone pipeline includes mandatory Semgrep and OWASP ZAP stages; failures block deployment. Students are taught to triage findings: not every flagged issue is exploitable, and suppressions must be documented with risk assessments.

**Deployment strategies** separate delivery (making an artifact available for deployment) from deployment (actually running it in production). Blue-green deployment maintains two identical production environments, switching traffic from blue to green after verification. Canary deployment routes a small percentage of traffic to the new version, monitoring for errors before full rollout. Feature flags (controlled by systems like LaunchDarkly or open-source Unleash) decouple deployment from release, allowing features to be turned on for specific users without redeployment. The 2040 landscape adds **neuromorphic canaries**: for AI-native systems, canary deployments include automated behavioral drift detection—if the new model version's output distribution diverges significantly from the baseline, the canary is automatically rolled back. Capstone students deploying ML components must configure this drift threshold as part of their deployment manifest.

### Required Reading

- Fowler, M. (2000). "Continuous Integration." *martinfowler.com*, reprinted in *Yggdrasil Software Engineering Compendium*, 2035.
- SLSA Framework (2025). "Supply Chain Levels for Software Artifacts." Version 1.1. OpenSSF.
- Kocher, J., & Möller, B. (2032). "Typed Pipeline Languages: Preventing the Next CI Outage." *IEEE Software*, 39(2), 45–52.
- Yggdrasil Security Guild (2040). "Capstone Security Scanning Policy: SAST, DAST, and IAST Requirements." Internal document v7.0.
- *LaunchDarkly Documentation* (2040). "Neuromorphic Canary: Behavioral Drift Detection in AI-Native Deployments." Technical whitepaper.

### Discussion Questions

1. The 2031 GitHub Actions Outage was caused by a YAML parsing bug. What properties of YAML make it particularly unsuitable for critical infrastructure configuration? Are typed DSLs a genuine solution or merely pushing complexity elsewhere?
2. SLSA Level 3 requires two-party review. In a capstone team of three students, how should review responsibilities be distributed to satisfy this requirement without creating bottlenecks?
3. Should all security scanning findings be blocking, or should there be a triage process with documented risk acceptance? What are the dangers of each approach?
4. Neuromorphic canary rollback is triggered by statistical divergence. How should the threshold be calibrated to avoid both false positives (unnecessary rollbacks) and false negatives (missed regressions)?

### Practice Problems

- Write a complete CI/CD pipeline for your capstone using the UoY `ci-dsl`, including build, test, security scan, and artifact signing stages. Execute it and verify that all stages pass.
- Configure a canary deployment for your capstone with at least two automated rollback conditions (e.g., error rate threshold, behavioral drift threshold). Document the rollback policy and demonstrate a simulated rollback.

---

ᚨ **Lecture 4: Containerization, Orchestration, and Cloud-Native Architecture**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Containerization, once a novelty of the mid-2010s, has become the universal packaging format for software by 2040. This lecture explores Docker, Podman, and the emerging WebAssembly (WASM) container standards, then moves to orchestration with Kubernetes, serverless platforms, and the edge-cloud continuum. Students will learn to design cloud-native architectures that leverage elasticity, resilience, and observability as first-class properties rather than afterthoughts.

### Key Topics

- Container technologies: Docker, Podman, containerd, and WASM micro-VMs
- Kubernetes: pods, services, deployments, ingress, and custom resource definitions
- Serverless and function-as-a-service: Knative, AWS Lambda, and event-driven scaling
- The edge-cloud continuum: k3s, microk8s, and fog computing architectures
- Cloud-native design patterns: circuit breakers, bulkheads, retry with backoff

### Lecture Notes

Solomon Hykes's introduction of Docker at PyCon 2013 marked the beginning of a packaging revolution. By containerizing applications with their dependencies, Docker solved the "it works on my machine" problem that had plagued software deployment for decades. By 2040, the Open Container Initiative (OCI) has standardized the container image format, and Docker coexists with Podman (daemonless, rootless containers) and containerd (the runtime underlying Kubernetes). The UoY capstone program recommends Podman for student development environments due to its security model—rootless containers eliminate a major attack surface—but requires that production images be OCI-compliant and scannable by Trivy or Clair.

The emergence of **WebAssembly (WASM) as a container target** represents the most significant shift in 2030s containerization. WASM modules offer near-native performance with sandboxed execution, smaller image sizes, and instant cold starts compared to traditional Linux containers. The WASI (WebAssembly System Interface) standard, stabilized in 2027, enables WASM modules to access filesystems, networks, and clocks in a capability-secure manner. By 2040, major cloud providers support WASM workloads on Kubernetes via the `containerd-wasm-shim`, and the UoY capstone framework includes a `wasm-pack` stage for Rust and AssemblyScript projects. Students are encouraged to evaluate WASM for components requiring high isolation (e.g., AI-generated code execution) but warned that the ecosystem is still maturing for I/O-intensive workloads.

**Kubernetes**, born from Google's Borg system and open-sourced in 2014, has become the de facto orchestration platform. By 2040, Kubernetes has absorbed so many subsystems that mastery requires years of dedicated practice; the capstone program therefore focuses on the core abstractions most relevant to student projects. The lecture covers pods (co-located containers sharing network and storage), services (stable networking endpoints), deployments (declarative desired state with rolling updates), ingress (HTTP routing), and persistent volumes (stateful storage). Students deploy their capstone on a UoY-managed k3s cluster (lightweight Kubernetes) that supports both traditional containers and WASM workloads.

**Serverless computing** has evolved from function-as-a-service (FaaS) to a broader event-driven architecture pattern. Knative, the Kubernetes-native serverless layer, enables automatic scaling to zero and rapid scale-out based on event volume. By 2040, serverless is the default for HTTP request handling, event processing, and scheduled tasks; long-running compute remains on dedicated nodes. The lecture emphasizes the *cold start problem*: while WASM cold starts are sub-millisecond, traditional containers may take seconds to initialize, causing latency spikes. Capstone projects with latency-sensitive components must measure and optimize cold start times, potentially using "keep-warm" strategies or WASM migration.

The **edge-cloud continuum** reflects the 2040 reality that computation is distributed across sensors, edge devices, regional data centers, and global clouds. k3s and microk8s bring Kubernetes to Raspberry Pi-class devices (like the Dellingr Node v3, a 2037 UoY-designed edge compute unit). Fog computing architectures process data at the edge, syncing summaries to the cloud rather than streaming raw data. For capstone projects involving sensor data, drone control, or real-time audio processing, edge deployment may be mandatory. The lecture covers data locality, sync conflict resolution, and the CAP theorem implications of edge-cloud partitioning.

**Cloud-native design patterns**, cataloged by the Microsoft Azure team and extended by the CNCF, provide proven solutions for resilience. The circuit breaker pattern (popularized by Michael Nygard in *Release It!*, 2007) prevents cascading failures by failing fast when a dependency is unhealthy. The bulkhead pattern isolates failures to compartments, limiting blast radius. Retry with exponential backoff and jitter prevents thundering herds. By 2040, these patterns are implemented in service mesh sidecars (Istio, Linkerd) and language-specific libraries (Resilience4j, Polly). Capstone students must implement at least two resilience patterns and demonstrate their effectiveness through chaos engineering tests—intentionally injecting failures to verify graceful degradation.

### Required Reading

- Hightower, K., Burns, B., & Beda, J. (2017). *Kubernetes: Up and Running*. O'Reilly. Chapters 1–3 (updated 2032 edition covers WASM workloads).
- Nygard, M. T. (2007). *Release It! Design and Deploy Production-Ready Software*. Pragmatic Bookshelf. Chapter 4 ("Stability Patterns").
- CNCF (2035). "Cloud Native Patterns: Circuit Breakers, Bulkheads, and Retry in 2040." *CNCF Technical Report* 2035-04.
- Yggdrasil Infrastructure Team (2037). "Dellingr Node v3: Edge Compute for Student Capstones." Hardware specification and deployment guide.
- wasmCloud Documentation (2040). "WASM Containers on Kubernetes: The containerd-wasm-shim." Installation and configuration guide.

### Discussion Questions

1. WASM containers offer smaller images and faster cold starts but a less mature ecosystem. For a capstone project with a web API and a background worker, which components (if any) should be WASM-based, and why?
2. Kubernetes mastery requires years of practice, yet capstone students must deploy in months. What Kubernetes abstractions are essential for a student project, and which can safely be abstracted away by platform teams?
3. The cold start problem affects user experience directly. How should a capstone team decide between keep-warm strategies (higher baseline cost, lower latency) and on-demand scaling (lower cost, higher latency variance)?
4. Chaos engineering intentionally breaks things to test resilience. Is this responsible practice for a capstone project, or does it risk collateral damage to shared infrastructure?

### Practice Problems

- Containerize your capstone application using Podman. Produce an OCI-compliant image, scan it with Trivy, and remediate any critical vulnerabilities. Document the final image size and startup time.
- Deploy your capstone on the UoY k3s cluster, configuring at least two resilience patterns (circuit breaker, bulkhead, or retry). Conduct a chaos engineering test by killing a dependency pod and verifying graceful degradation.

---

ᚱ **Lecture 5: Security Hardening, Threat Modeling, and the Zero-Trust Edge**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Security in 2040 is not a feature to be added but an architectural property to be designed. This lecture covers threat modeling methodologies, the zero-trust security model, secrets management, and the emerging paradigm of confidential computing. Students will learn to systematically identify threats, mitigate them through defense in depth, and verify security properties through both automated scanning and manual review. The capstone security audit, conducted in Week 10, requires a documented threat model and evidence of mitigations.

### Key Topics

- Threat modeling: STRIDE, attack trees, and the Microsoft Threat Modeling Tool
- Zero-trust architecture: never trust, always verify, least privilege
- Secrets management: HashiCorp Vault, sealed secrets, and hardware security modules
- Confidential computing: AMD SEV, Intel TDX, and encrypted execution enclaves
- Post-quantum cryptography: CRYSTALS-Kyber and Dilithium in production

### Lecture Notes

The discipline of threat modeling, systematized by Microsoft in the early 2000s through the STRIDE framework (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege), provides a structured method for identifying security threats before code is written. By 2040, threat modeling has been integrated into the earliest design phases: the UoY capstone program requires a threat model document as part of the CS406 design review, updated in CS407 as the implementation reveals new attack surfaces. The lecture walks through a complete STRIDE analysis of a typical capstone web application, identifying threats at each component boundary and mapping them to mitigations.

**Attack trees**, formalized by Bruce Schneier in 1999, provide a hierarchical decomposition of attack paths. The root node represents the attacker's goal; child nodes represent sub-goals or alternative paths. By 2040, attack trees are machine-checkable: the UoY security lab maintains a repository of verified attack tree templates for common capstone architectures (web API, distributed system, ML pipeline). Students instantiate these templates and annotate each node with implemented mitigations. The lecture demonstrates how a simple attack tree for "Steal user data" decomposes into SQL injection, authentication bypass, and insider threat branches, each with specific mitigations.

**Zero-trust architecture**, articulated by John Kindervag (Forrester, 2010) and widely adopted following the 2020 SolarWinds breach, replaces the perimeter-based security model with a model of continuous verification. In zero-trust, no user, device, or service is inherently trusted; every access request is authenticated, authorized, and encrypted. By 2040, zero-trust is the default for cloud-native systems. The lecture covers the five pillars of zero-trust as defined by NIST SP 800-207 (2020, updated 2030): identity, device, network, application, and data. Capstone projects must implement identity verification (via OAuth 2.1 or WebAuthn), device attestation (via TPM), micro-segmentation (via service mesh policies), application-level authorization (RBAC or ABAC), and data encryption at rest and in transit.

**Secrets management** addresses the challenge of storing API keys, database passwords, and cryptographic material without embedding them in source code or container images. HashiCorp Vault, the industry standard by 2040, provides dynamic secrets, automatic rotation, and audit logging. The UoY capstone template includes Vault integration: applications authenticate via Kubernetes service accounts and receive short-lived credentials (e.g., 1-hour database passwords). Students learn to avoid common anti-patterns: `.env` files in repositories, hardcoded keys, and Kubernetes secrets without encryption at rest. The lecture also covers **sealed secrets** (Bitnami Sealed Secrets) as a lighter-weight alternative for projects without Vault infrastructure.

**Confidential computing** represents the 2030s breakthrough in hardware-enforced security. AMD SEV (Secure Encrypted Virtualization), Intel TDX (Trust Domain Extensions), and ARM CCA (Confidential Compute Architecture) enable encryption of memory and computation such that even the cloud provider cannot inspect running workloads. By 2040, confidential VMs are available from all major cloud providers and are mandatory for processing sensitive personal data under the *Bangalore Protocol* (2038). Capstone projects handling simulated health data, financial transactions, or biometric information must deploy on confidential computing nodes. The lecture covers attestation: the process by which a confidential workload proves its identity and integrity to remote verifiers.

**Post-quantum cryptography** has transitioned from research to production. The 2024 NIST standardization of CRYSTALS-Kyber (key encapsulation) and CRYSTALS-Dilithium (digital signatures) marked the beginning of the PQC era. By 2040, all TLS connections must use hybrid post-quantum key exchange (X25519 + Kyber), and all code-signing certificates use Dilithium. The UoY capstone pipeline automatically rotates PQC certificates and rejects non-compliant artifacts. Students are taught to understand the performance implications: Kyber is faster than RSA for key generation and encapsulation, but Dilithium signatures are larger than ECDSA signatures, affecting bandwidth-constrained protocols.

### Required Reading

- Shostack, A. (2014). *Threat Modeling: Designing for Security*. Wiley. Chapters 3–5 (STRIDE and attack trees).
- NIST (2030). *SP 800-207: Zero Trust Architecture* (Revision 2). National Institute of Standards and Technology.
- HashiCorp (2040). *Vault Documentation: Dynamic Secrets and Kubernetes Integration*. Version 4.2.
- AMD (2035). "SEV-SNP and Confidential Computing: A Developer's Guide." Technical whitepaper.
- Bernstein, D. J., & Lange, T. (2031). "Post-Quantum Cryptography in Practice: The Transition to Kyber and Dilithium." *Journal of Cryptology*, 44(2), 301–345.

### Discussion Questions

1. STRIDE was developed in the early 2000s for desktop applications. Which STRIDE categories become more or less relevant for AI-native systems where model weights themselves may be sensitive intellectual property?
2. Zero-trust increases security but also complexity. What are the operational risks of over-applying zero-trust principles to a simple capstone web application?
3. Confidential computing protects against cloud provider compromise but introduces performance overhead. Under what threat models is this trade-off justified?
4. Dilithium signatures are larger than ECDSA. For a capstone API making millions of small requests, how might this signature size affect latency and bandwidth?

### Practice Problems

- Produce a complete STRIDE threat model for your capstone, documenting at least 15 distinct threats and their mitigations. Map each threat to a specific component or data flow.
- Implement zero-trust network policies using your service mesh (Istio or Linkerd). Demonstrate that unauthorized services cannot communicate, even within the same cluster namespace.

---

ᚲ **Lecture 6: Performance Engineering: Profiling, Optimization, and Benchmarking**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Performance is not an accident but the result of systematic measurement, analysis, and refinement. This lecture covers performance engineering from the algorithmic level to the hardware level: asymptotic analysis, profiling tools, cache optimization, GPU kernel tuning, and the statistical rigor required for meaningful benchmarking. Students will learn to identify bottlenecks, apply targeted optimizations, and validate improvements without introducing regressions elsewhere.

### Key Topics

- Algorithmic efficiency: Big-O, Big-Ω, Big-Θ, and amortized analysis
- Profiling: CPU sampling, flame graphs, memory allocation tracking, I/O tracing
- Cache optimization: spatial and temporal locality, cache-oblivious algorithms
- GPU performance: occupancy, memory coalescing, shared memory tiling
- Statistical benchmarking: confidence intervals, A/B testing, avoiding measurement bias

### Lecture Notes

Donald Knuth's famous aphorism—"premature optimization is the root of all evil"—has often been misunderstood as a injunction against optimization itself. What Knuth meant, and what this lecture insists upon, is that optimization must be informed by measurement. Blind optimization wastes effort on code that is not on the critical path, while ignoring the true bottleneck. By 2040, this principle is enforced by automated profiling integrated into CI: the UoY capstone pipeline runs `perf` (Linux), ` Instruments` (macOS), or `VTune` (Intel) on every commit, flagging regressions greater than 5% in CPU time, memory allocation rate, or I/O throughput.

**Algorithmic analysis** provides the theoretical foundation. Big-O notation describes asymptotic upper bounds; Big-Ω describes lower bounds; Big-Θ describes tight bounds. Amortized analysis, introduced by Tarjan in the 1980s, averages the cost of expensive operations over a sequence of cheaper ones, explaining why a dynamically resizing hash table achieves O(1) average insertion despite occasional O(n) reallocations. By 2040, these concepts are extended to **parallel complexity**: work (total operations) and span (longest dependency chain) replace simple operation counts for GPU and distributed algorithms. The lecture includes a parallel complexity analysis of matrix multiplication on CUDA, demonstrating how tiling reduces span while increasing work efficiency.

**Profiling** bridges theory and practice. CPU sampling profilers (Linux `perf`, `py-spy`, `async-profiler`) record the program counter at regular intervals, building a statistical picture of where time is spent. Flame graphs, invented by Brendan Gregg in 2011, visualize this data as stacked rectangles where width represents sample frequency. By 2040, flame graphs have been augmented with **temporal flame graphs** that show how the profile evolves over time, revealing phase changes (e.g., warmup vs. steady state) and intermittent bottlenecks. Memory profilers (Valgrind Massif, heaptrack, Rust's dhat) track allocation sites and lifetimes. The lecture demonstrates how to use these tools on a capstone project, starting from a high-level overview and drilling down to specific functions.

**Cache optimization** remains critical despite decades of hardware advancement. The gap between CPU clock speed and memory latency, known as the memory wall, has widened since the 1990s. Cache-friendly code maximizes spatial locality (accessing nearby memory addresses together) and temporal locality (reusing data before eviction). **Cache-oblivious algorithms**, introduced by Prokop in 1999 and popularized by the Demaines, achieve optimal cache performance without knowledge of the cache size—a theoretical elegance with practical benefits for portable code. The lecture walks through a cache-oblivious matrix multiplication and compares its performance to naive and manually tiled implementations across cache hierarchies.

**GPU performance tuning** is essential for capstone projects involving ML inference or scientific simulation. Three factors dominate GPU performance: occupancy (the fraction of warps actively executing, limited by register and shared memory usage), memory coalescing (ensuring that threads in a warp access consecutive memory addresses), and shared memory tiling (storing frequently reused data in fast on-chip memory). The lecture uses a 2D convolution kernel as a running example, showing how uncoalesced memory access reduces throughput by an order of magnitude and how tiling brings it back to peak. By 2040, NVIDIA's Nsight Compute and AMD's rocProfiler provide automated recommendations for these optimizations, but the student must understand the underlying hardware model to apply them correctly.

**Statistical rigor in benchmarking** prevents the common pitfall of cherry-picking results. A single run is insufficient: noise from OS scheduling, thermal throttling, and background processes can dominate measurement. The lecture teaches confidence interval construction via bootstrap resampling, A/B testing with Welch's t-test for unequal variances, and the detection of measurement bias (e.g., JVM warmup, cache state). The UoY capstone requires that all performance claims be accompanied by confidence intervals at the 95% level and that benchmark code be committed alongside the implementation. The 2036 *Reproducibility Crisis in Systems Benchmarking* paper by Leliaert et al. serves as a cautionary tale: the majority of published systems benchmarks in the 2020s were irreproducible due to missing environment details and statistical naivety.

### Required Reading

- Knuth, D. E. (1974). "Structured Programming with go to Statements." *ACM Computing Surveys*, 6(4), 261–301. (Source of the premature optimization aphorism.)
- Gregg, B. (2020). *Systems Performance: Enterprise and the Cloud* (2nd Edition). Addison-Wesley. Chapters 5 ("Profiling") and 6 ("Benchmarking").
- Demaine, E. D. (2002). "Cache-Oblivious Algorithms and Data Structures." *Lecture Notes in Computer Science*, 2625, 1–29.
- Harris, M. (2012). "How to Access Global Memory Efficiently in CUDA C/C++ Kernels." NVIDIA Developer Blog.
- Leliaert, T., et al. (2036). "The Reproducibility Crisis in Systems Benchmarking: A Decade of Failure." *ACM SIGOPS Operating Systems Review*, 50(3), 12–19.

### Discussion Questions

1. Knuth's aphorism is often quoted to discourage optimization. Under what conditions is early optimization justified, and how can a capstone team distinguish it from premature optimization?
2. Temporal flame graphs reveal phase changes in program behavior. How might this information change the way you interpret a traditional (time-averaged) flame graph?
3. Cache-oblivious algorithms are theoretically elegant but sometimes outperformed by cache-aware algorithms with tuned block sizes. When should a capstone student prefer one over the other?
4. The 2036 Reproducibility Crisis showed that most benchmarks lacked statistical rigor. What minimum information should every capstone benchmark report include to avoid this fate?

### Practice Problems

- Profile your capstone application using `perf` or `py-spy`. Generate a flame graph, identify the top three CPU consumers, and propose optimizations. Validate improvements with before/after benchmarks including 95% confidence intervals.
- If your capstone uses GPU computation, analyze memory coalescing patterns in your kernel. Reorder thread indexing if necessary and measure the throughput improvement.

---

ᚷ **Lecture 7: Observability: Monitoring, Logging, Tracing, and Intelligent Alerting**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

A system that cannot be observed is a system that cannot be trusted. This lecture introduces the three pillars of observability—metrics, logs, and traces—and their integration into coherent monitoring dashboards. By 2040, observability has been augmented by AI-assisted anomaly detection, causal tracing, and predictive alerting. Students will instrument their capstone systems, construct meaningful dashboards, and configure alerting that surfaces genuine problems without drowning operators in noise.

### Key Topics

- Metrics: counters, gauges, histograms, and the RED method (Rate, Errors, Duration)
- Logging: structured logging, log levels, correlation IDs, and retention policies
- Distributed tracing: OpenTelemetry, spans, trace context propagation
- AI-assisted anomaly detection: seasonal decomposition, autoencoders, and causal graphs
- Alerting: SLOs, SLIs, error budgets, and on-call rotation design

### Lecture Notes

The distinction between monitoring (asking known questions of known metrics) and observability (exploring unknown properties of unknown states), articulated by Charity Majors and others at Honeycomb in the late 2010s, has reshaped the industry. By 2040, observability is not a vendor category but a system property: every component must expose metrics, emit structured logs, and participate in distributed tracing. The UoY capstone program requires full OpenTelemetry instrumentation: all HTTP handlers, database queries, and external API calls must generate spans, and all business-logic events must produce structured log lines with correlation IDs.

**Metrics** provide the quantitative backbone. The RED method—Rate (requests per second), Errors (failed requests), Duration (latency distribution)—offers a minimal viable metric set for any service. The lecture extends this with the USE method (Utilization, Saturation, Errors) for resource monitoring and the Four Golden Signals (latency, traffic, errors, saturation) popularized by Google's SRE book. By 2040, histograms (not averages) are the standard for latency reporting, enabling percentile calculations (p50, p95, p99) that capture tail behavior. The UoY capstone template includes a Prometheus metrics endpoint and Grafana dashboards pre-configured for RED, USE, and custom business metrics.

**Structured logging** replaces free-text logs with machine-parseable key-value pairs. JSON is the dominant format, though binary formats like MessagePack and Protobuf are used for high-volume systems. The lecture emphasizes the importance of **correlation IDs** (also called trace IDs): when a request enters the system, it is assigned a unique ID that propagates through all subsequent service calls, database queries, and background jobs. This ID enables the reconstruction of the complete request lifecycle across distributed components. By 2040, correlation ID propagation is automatic in most frameworks via the W3C Trace Context specification, but capstone students must verify that their custom code respects the context.

**Distributed tracing**, standardized by OpenTelemetry (merging OpenTracing and OpenCensus in 2019), represents a request as a tree of spans. Each span records an operation (e.g., "SELECT users WHERE id = ?"), its start and end times, and arbitrary key-value attributes. The trace viewer (Jaeger, Zipkin, or Grafana Tempo) renders this tree as a waterfall diagram, revealing latency contributions from each component. The lecture demonstrates how a slow API endpoint might be diagnosed via tracing: the waterfall shows that 90% of latency is spent in a database query lacking an index, not in application logic. By 2040, tracing has been augmented with **causal tracing**—systems that infer causal relationships between spans using statistical methods, enabling automatic root-cause analysis.

**AI-assisted anomaly detection** addresses the scalability problem of human monitoring. Seasonal decomposition (STL) separates time series into trend, seasonality, and residual components, flagging residuals that exceed historical bounds. Autoencoder neural networks learn normal patterns and flag reconstructions with high error. By 2040, **causal graph models** have superseded simple threshold alerting: they encode known causal relationships (e.g., "high CPU → slow queries → increased errors") and use Bayesian inference to identify the most likely root cause when multiple metrics deviate simultaneously. The UoY capstone program provides a lightweight causal graph template; students populate it with their system's known dependencies and receive AI-generated root-cause hypotheses during incidents.

**Alerting design** follows the SLO (Service Level Objective) methodology from Google's *Site Reliability Engineering* (2016). An SLO is a target reliability (e.g., 99.9% of requests succeed within 200ms). The SLI (Service Level Indicator) measures the objective; the error budget (1 - SLO) defines how much unreliability is acceptable before engineering priority shifts from features to reliability. By 2040, error budgets are automatically tracked and visualized; when a team burns through its monthly budget in a week, deployment freezes trigger automatically. Capstone students set SLOs for their projects and configure alerts that fire when burn rate exceeds thresholds. The lecture warns against "alert fatigue": alerts must be actionable, specific, and rare enough to warrant immediate attention.

### Required Reading

- Beyer, B., et al. (2016). *Site Reliability Engineering: How Google Runs Production Systems*. O'Reilly. Chapters 2 ("The Production Environment at Google") and 4 ("Service Level Objectives").
- Majors, C., Fong-Jones, L., & Miranda, G. (2022). *Observability Engineering*. O'Reilly. Chapters 1–3.
- W3C (2021). "Trace Context: W3C Recommendation." Version 1.0.
- Yggdrasil Infrastructure Team (2038). "Causal Graph Alerting: From Correlation to Root Cause." *UoY Systems Engineering Report* 2038-11.
- OpenTelemetry Documentation (2040). "Getting Started: Auto-Instrumentation for Python, Rust, and TypeScript."

### Discussion Questions

1. Monitoring asks known questions; observability enables exploration of the unknown. Can a system be fully observable, or is observability always bounded by the instrumentation decisions made at design time?
2. Causal tracing promises automatic root-cause analysis. What are the limitations of statistical causal inference, and when might it produce misleading root-cause hypotheses?
3. Error budgets provide a quantitative framework for reliability decisions. How should a capstone team set SLOs for a system with no historical performance data?
4. Alert fatigue is a well-documented phenomenon. What specific design choices in your capstone's alerting configuration would minimize false positives while maintaining sensitivity to genuine incidents?

### Practice Problems

- Instrument your capstone with OpenTelemetry, generating spans for all HTTP handlers, database queries, and external API calls. Deploy a Jaeger instance and verify that a complete request trace is visible.
- Define three SLOs for your capstone (e.g., availability, latency, error rate). Configure Prometheus alerts that fire when error budget burn rate exceeds 2% per day. Document the alert runbook.

---

ᚹ **Lecture 8: Documentation as Code: Architecture Decision Records and Living Knowledge Bases**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Documentation is the conscience of a software system—the persistent memory that outlasts any individual contributor. This lecture treats documentation not as a post-hoc chore but as an integral engineering practice, parallel to testing and deployment. Students will learn to write Architecture Decision Records (ADRs), maintain API documentation, generate knowledge graphs from code, and produce the public-facing technical writeup required for capstone completion.

### Key Topics

- Architecture Decision Records: format, lifecycle, and decision reversal
- API documentation: OpenAPI, GraphQL schemas, and automated generation
- Code documentation: docstrings, type annotations, and literate programming
- Knowledge graphs: extracting semantic relationships from codebase structure
- The capstone technical writeup: audience, structure, and evaluation criteria

### Lecture Notes

The documentation crisis in software engineering is as old as the field itself. Frederick Brooks observed in 1975 that "the hardest single part of building a software system is deciding precisely what to build"—and documentation is the medium through which that decision is communicated, preserved, and challenged. By 2040, the industry has converged on **Documentation as Code**: documentation lives in version control, is reviewed in pull requests, is tested in CI, and is deployed alongside the application. The UoY capstone program requires that all documentation be Markdown-based, stored in the repository's `docs/` directory, and rendered by a static site generator (MkDocs, Docusaurus, or the UoY-maintained `rúnar-docs`, which adds Norse-themed styling and automatic cross-referencing).

**Architecture Decision Records (ADRs)**, introduced by Michael Nygard in 2011, provide a lightweight format for capturing significant technical decisions. The standard ADR template includes: context (the forces at play), decision (what was chosen), consequences (positive and negative), and status (proposed, accepted, deprecated, superseded). By 2040, ADRs are machine-linked: the `rúnar-docs` generator parses ADR files and renders them as a navigable decision graph, showing which decisions depend on which and which have been superseded. The lecture requires students to produce at least five ADRs for their capstone: technology stack, database choice, authentication strategy, deployment architecture, and one significant algorithmic or structural decision.

**API documentation** in 2040 is predominantly generated from code. OpenAPI 3.1 (formerly Swagger) describes REST APIs in a standardized JSON/YAML format from which documentation, client SDKs, and mock servers can be generated. For GraphQL APIs, the schema itself serves as documentation, enhanced by field descriptions and deprecation annotations. The lecture covers `rustdoc`, `pdoc`, `typedoc`, and `mkdocstrings` for language-native documentation, emphasizing that generated documentation is only as good as the docstrings and type annotations from which it is derived. The UoY capstone requires 100% public API coverage: every exported function, class, and endpoint must have a docstring or schema description.

**Knowledge graphs** represent the cutting edge of documentation. Rather than flat Markdown files, knowledge graphs encode entities (functions, classes, services, data models) and relationships (calls, implements, depends on, serializes to) in a queryable graph database. Tools like Sourcegraph (code intelligence) and the UoY-developed `mímir-graph` extract these relationships from static analysis, creating a living map of the codebase. By 2040, students can query "Which services depend on the User model?" or "What functions are called by the authentication middleware?" directly from the documentation portal. The lecture demonstrates `mímir-graph` integration and shows how it catches documentation drift: when code changes but the knowledge graph is not updated, CI fails.

The **capstone technical writeup** is the culminating documentation artifact. Required by Week 12, it is a public-facing document of 8,000–12,000 words that explains the problem, the solution, the engineering decisions, and the results. The audience is technically literate but unfamiliar with the project—imagine a hiring manager or graduate admissions committee. The UoY evaluation rubric assesses: clarity of problem statement, depth of technical explanation, quality of ADR integration, evidence of testing and performance validation, reflection on limitations, and presentation polish. The lecture provides a template structure and analyzes exemplary writeups from previous capstone cohorts, highlighting effective techniques (narrative framing, concrete metrics, honest limitation discussion) and common failures (vague descriptions, missing evaluation, overstated claims).

### Required Reading

- Nygard, M. T. (2011). "Documenting Architecture Decisions." *michaelnygard.com*, reprinted in *Yggdrasil Engineering Chronicles*, 2034.
- OpenAPI Initiative (2021). *OpenAPI Specification Version 3.1.0*.
- Sourcegraph (2035). "Code Intelligence and the Living Knowledge Graph." *Sourcegraph Technical Blog*.
- University of Yggdrasil (2040). "Capstone Technical Writeup: Evaluation Rubric and Exemplars." Department of Computer Science.
- Freyjasdottir, R. G. (2039). "Mímir-Graph: Extracting Semantic Relationships from Student Codebases." *UoY Software Engineering Report* 2039-04.

### Discussion Questions

1. ADRs capture decisions but not the full reasoning process. What is lost when a decision is reduced to a four-section template, and how might that loss be mitigated?
2. Generated API documentation is often criticized as "reference without explanation." How should a capstone team supplement generated docs with narrative guides and tutorials?
3. Knowledge graphs promise to eliminate documentation drift by auto-extracting relationships from code. What relationships can static analysis capture, and what relationships (e.g., design intent, business rationale) remain invisible to it?
4. The capstone writeup requires honest discussion of limitations. Why is this requirement pedagogically valuable, and what risks might it create for students in competitive job markets?

### Practice Problems

- Write five ADRs for your capstone, following the UoY template. Ensure they are committed to `docs/adrs/` and rendered correctly by `rúnar-docs`.
- Generate API documentation for your capstone's public endpoints using OpenAPI or GraphQL schema introspection. Verify that every endpoint has a description, request/response schemas, and at least one example.

---

ᚺ **Lecture 9: User Experience Evaluation and Accessibility in 2040 Systems**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Technical excellence is insufficient if the system cannot be used. This lecture covers user experience (UX) evaluation methods, accessibility standards, and the emerging field of neural-interface usability. Students will learn to conduct usability tests, interpret analytics, apply WCAG 3.0 guidelines, and design for diverse cognitive and sensory profiles. The capstone must demonstrate usability testing with at least five participants and WCAG 3.0 conformance at the Silver level.

### Key Topics

- Usability testing: moderated, unmoderated, task-based, and think-aloud protocols
- UX analytics: funnel analysis, heatmaps, session recordings, and A/B testing
- Accessibility: WCAG 3.0, assistive technologies, and automated accessibility scanning
- Cognitive accessibility: designing for neurodivergent users and cognitive load reduction
- Neural interfaces: usability challenges of brain-computer interfaces and haptic feedback

### Lecture Notes

The field of human-computer interaction, formalized in the 1980s by Card, Moran, and Newell's *The Psychology of Human-Computer Interaction* (1983), has matured into a rigorous discipline bridging cognitive psychology, design, and engineering. By 2040, UX evaluation is as quantitative as performance engineering: task success rates, time-on-task, error rates, and System Usability Scale (SUS) scores are tracked with the same rigor as latency percentiles. The UoY capstone program requires a formal UX evaluation report, including methodology, participant demographics, task designs, raw data, statistical analysis, and design recommendations.

**Usability testing** comes in many forms. Moderated testing involves a facilitator guiding participants through tasks, asking probing questions, and observing struggles. Unmoderated testing (via platforms like UserTesting.com or the open-source Maze) scales to larger samples but sacrifices observational depth. The **think-aloud protocol**, in which participants verbalize their thoughts during task execution, remains the gold standard for revealing cognitive processes. By 2040, think-aloud has been augmented by **eye-tracking** and **pupillometry**: eye fixations reveal attention allocation, while pupil dilation indicates cognitive load. The lecture demonstrates how to set up a low-cost eye-tracking study using the Tobii Pro Nano (2038 model, $199) and analyze fixation heatmaps with the open-source `ogham` toolkit developed at UoY.

**UX analytics** complement qualitative testing with behavioral data at scale. Funnel analysis tracks the percentage of users who complete multi-step processes (e.g., registration, checkout), revealing drop-off points. Heatmaps (click, scroll, attention) aggregate user behavior across sessions. Session recordings (e.g., FullStory, Hotjar, or the privacy-preserving `muninn-replay` developed at UoY) capture individual interactions for replay. By 2040, these tools are integrated with AI-assisted insight extraction: rather than watching hundreds of recordings, students run `muninn-insight` to cluster sessions by behavioral similarity and flag anomalous struggle patterns. The lecture emphasizes privacy: all analytics must comply with the *Bangalore Protocol* (2038), which requires explicit consent, data minimization, and automatic deletion after 30 days.

**Accessibility** in 2040 is governed by WCAG 3.0 (W3C Recommendation, 2032), which replaces the binary pass/fail model of WCAG 2.x with a scoring system across three levels: Bronze, Silver, and Gold. The UoY capstone requires Silver conformance, which includes: keyboard navigability, screen reader compatibility, sufficient color contrast, resizable text, captions for media, and consistent navigation. Automated scanning (axe, WAVE, Lighthouse) catches approximately 30% of WCAG violations; the remainder require manual testing with assistive technologies. The lecture includes a live screen reader demonstration (NVDA on Windows, Orca on Linux, VoiceOver on macOS) and a color contrast analysis exercise.

**Cognitive accessibility** has gained prominence in the 2030s as neurodivergent perspectives have entered mainstream design discourse. Designing for users with ADHD, autism, dyslexia, or anxiety requires: clear information architecture, reduced distractions, plain language, predictable interactions, and customizable interfaces. The lecture introduces the **Cognitive Accessibility Guidelines** (COGA) from the W3C and shows how capstone projects can implement cognitive load reduction: progressive disclosure, chunked content, and user-controlled pacing. The 2037 *Neurodivergent Computing Manifesto* by the Autistic Self-Advocacy Network is cited as a foundational text.

**Neural interfaces**, while still emerging in 2040, present novel usability challenges. Brain-computer interfaces (BCIs) such as Neuralink's N1 (commercialized 2032) and non-invasive EEG headsets (OpenBCI, Emotiv) require calibration, have high inter-user variability, and raise ethical concerns about cognitive privacy. Haptic feedback systems (ultrasonic mid-air haptics, force-feedback gloves) must be designed with ergonomic constraints and sensory overload prevention. The lecture surveys these technologies and asks students to consider: if your capstone included a neural interface component, what usability metrics would you track? How would you obtain informed consent for a technology that reads neural signals?

### Required Reading

- Card, S. K., Moran, T. P., & Newell, A. (1983). *The Psychology of Human-Computer Interaction*. Lawrence Erlbaum Associates. Chapters 2–4.
- W3C (2032). *Web Content Accessibility Guidelines (WCAG) 3.0*. W3C Recommendation.
- Nielsen, J. (2012). "How Many Test Users in a Usability Study?" *Nielsen Norman Group*.
- Autistic Self-Advocacy Network (2037). *Neurodivergent Computing Manifesto*. Advocacy document.
- Yggdrasil HCI Lab (2039). "Muninn-Insight: AI-Assisted UX Analytics with Privacy Guarantees." *UoY HCI Report* 2039-02.

### Discussion Questions

1. The think-aloud protocol reveals cognitive processes but may alter them (the Heisenberg effect of UX). How should a capstone team balance the depth of think-aloud insights against the risk of distorted behavior?
2. WCAG 3.0's scoring system is more nuanced than WCAG 2.x's binary model. Does this nuance improve accessibility practice, or does it introduce ambiguity that leads to inconsistent implementation?
3. Cognitive accessibility requires designing for neurodivergent users, but "neurodivergent" encompasses many profiles with potentially conflicting needs. How can a single interface accommodate both users who prefer minimal stimulation and users who prefer high information density?
4. Neural interfaces raise unique informed-consent challenges. If a BCI component were part of your capstone, what safeguards would you implement beyond standard software consent procedures?

### Practice Problems

- Conduct a moderated usability test with at least five participants for your capstone. Use the think-aloud protocol, record task success rates and time-on-task, and calculate a mean SUS score. Document findings and design recommendations in a UX evaluation report.
- Run automated accessibility scanning (axe or Lighthouse) on your capstone. Remediate all violations and manually verify keyboard navigation and screen reader compatibility. Report your WCAG 3.0 conformance level.

---

ᚾ **Lecture 10: The Ethics Review: Responsible Deployment and Societal Impact Assessment**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Every system is a political artifact, embedding values in its design, deployment, and maintenance. This lecture addresses the ethical responsibilities of the software engineer in 2040: fairness, transparency, privacy, environmental impact, and the systemic consequences of automation. Students will conduct an ethics review of their capstone, assessing potential harms, mitigation strategies, and alignment with the *Bangalore Protocol* on digital personhood and the *Reykjavík Accords* on sustainable computing.

### Key Topics

- Algorithmic fairness: demographic parity, equalized odds, and calibration
- Explainability and transparency: LIME, SHAP, and interpretability-by-design
- Privacy engineering: differential privacy, federated learning, and data minimization
- Environmental impact: carbon accounting for training and inference workloads
- Societal impact assessment: stakeholder mapping, harm analysis, and redress mechanisms

### Lecture Notes

The ethical turn in computer science, accelerated by the publication of Cathy O'Neil's *Weapons of Math Destruction* (2016) and Kate Crawford's *Atlas of AI* (2021), has by 2040 become an institutional requirement. The University of Yggdrasil, founded in the aftermath of the *Alignment Crisis* (2023–2032), requires every capstone project to pass an ethics review conducted by a faculty committee with external community representation. This lecture prepares students for that review and, more importantly, equips them with the conceptual tools to make ethically informed engineering decisions throughout their careers.

**Algorithmic fairness** has evolved from a binary question ("Is the algorithm fair?") to a multifaceted analysis of which fairness criterion is appropriate for which context. Demographic parity requires equal positive prediction rates across groups; equalized odds requires equal true and false positive rates; calibration requires that predicted probabilities reflect true probabilities within each group. The seminal impossibility result of Kleinberg, Mullainathan, and Raghavan (2016) proved that these criteria are mutually exclusive in non-trivial cases. By 2040, the field has accepted that fairness is a sociotechnical choice, not a mathematical discovery. Capstone projects using ML must document their chosen fairness criterion, justify it with stakeholder input, and report group-wise metrics.

**Explainability and transparency** are mandated by the *Bangalore Protocol* (2038) for systems that affect legal rights, employment, or access to services. Post-hoc explanation methods like LIME (Local Interpretable Model-agnostic Explanations) and SHAP (SHapley Additive exPlanations) provide local explanations for individual predictions but have been criticized for instability and misleadingness. By 2040, the preferred approach is **interpretability-by-design**: models and systems are constructed to be inherently understandable, rather than wrapping opaque components in explanation layers. The lecture covers decision trees, rule lists, attention visualization, and concept-based explanations. Capstone projects using neural networks must either demonstrate inherent interpretability or provide validated post-hoc explanations with uncertainty bounds.

**Privacy engineering** in 2040 goes beyond compliance checklists. Differential privacy, introduced by Dwork and Nissim (2004), provides a mathematically rigorous definition: a randomized algorithm is differentially private if changing one individual's data changes the output distribution by at most a bounded amount (ε). By 2040, differential privacy is standard for census data, healthcare analytics, and ML training. Federated learning, popularized by Google's Gboard team (2016), trains models across decentralized devices without centralizing raw data. The lecture demonstrates how to implement local differential privacy in a capstone analytics pipeline and how to configure federated averaging for a mobile application. The *Bangalore Protocol* requires that any system processing personal data conduct a Privacy Impact Assessment (PIA) documenting data flows, retention limits, and deletion procedures.

**Environmental impact** has become an ethical imperative. The 2030s saw the rise of carbon-aware computing: scheduling workloads to times and regions with low-carbon electricity, and quantifying the carbon cost of every training run and inference request. The *Reykjavík Accords* (2033) established standards for carbon accounting in software, requiring that all production systems report estimated CO₂ emissions per transaction. The lecture teaches the **ML Emissions Calculator** (developed by Lacoste et al., 2019, updated 2035) and the **Green Software Foundation's SCI** (Software Carbon Intensity) specification. Capstone students must estimate their system's carbon footprint, justify their compute choices, and explore carbon-reduction strategies (model distillation, edge inference, renewable energy sourcing).

**Societal impact assessment** is the capstone ethics review's centerpiece. Students map stakeholders (users, non-users, affected communities, maintainers, future generations), identify potential harms (direct, indirect, structural, existential), propose mitigations, and design redress mechanisms. The lecture introduces the **Stakes Matrix** (developed by the UoY Ethics Guild in 2036), which categorizes harms by severity and reversibility. A capstone project deploying a rental pricing algorithm, for example, might identify stakeholder harm (displacement of low-income tenants), propose mitigation (price caps, community review), and design redress (appeal process, compensation fund). The ethics review committee evaluates not whether the project is harmless—no complex system is—but whether the student has thoughtfully engaged with its potential impacts.

### Required Reading

- O'Neil, C. (2016). *Weapons of Math Destruction: How Big Data Increases Inequality and Threatens Democracy*. Crown.
- Crawford, K. (2021). *Atlas of AI: Power, Politics, and the Planetary Costs of Artificial Intelligence*. Yale University Press.
- Kleinberg, J., Mullainathan, S., & Raghavan, M. (2016). "Inherent Trade-Offs in the Fair Determination of Risk Scores." *arXiv:1609.05807*.
- Dwork, C., & Roth, A. (2014). *The Algorithmic Foundations of Differential Privacy*. Foundations and Trends in Theoretical Computer Science, 9(3–4), 211–407.
- Bangalore Protocol (2038). "Digital Personhood and Algorithmic Accountability Framework." International Convention on Digital Rights.
- Reykjavík Accords (2033). "Sustainable Computing: Carbon Accounting Standards for Software Systems." Nordic Council.

### Discussion Questions

1. Kleinberg et al. proved that demographic parity, equalized odds, and calibration are mutually exclusive. If your capstone uses ML for decision support, which criterion would you prioritize, and what stakeholder process would you use to justify that choice?
2. Interpretability-by-design is preferable to post-hoc explanation, but inherently interpretable models often underperform complex neural networks. Under what conditions is the performance sacrifice justified?
3. Federated learning protects privacy but introduces new attack surfaces (model poisoning, inference attacks). How should a capstone team evaluate the privacy-security trade-off?
4. The Stakes Matrix asks students to consider harms to future generations. What obligations do software engineers have to people who do not yet exist, and how can those obligations be operationalized in design decisions?

### Practice Problems

- Conduct a full ethics review of your capstone using the Stakes Matrix. Document at least 10 stakeholders, 5 potential harms, proposed mitigations, and redress mechanisms. Submit as your formal ethics review document.
- Calculate your capstone's estimated carbon footprint using the SCI specification. If it exceeds 100g CO₂ per 1000 requests, propose and implement at least one reduction strategy.

---

ᛁ **Lecture 11: The Technical Demonstration: From Prototype to Defensible Presentation**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

The capstone demonstration is not a sales pitch but a technical defense. This lecture prepares students to present their systems to a panel of faculty and industry engineers, demonstrating not only that the system works but that the student understands why it works, where it fails, and how it could be extended. The lecture covers presentation structure, live demo strategies, handling critical questions, and the art of honest technical storytelling.

### Key Topics

- Presentation structure: problem, approach, implementation, evaluation, limitations, future work
- Live demo strategies: recorded fallbacks, deterministic demo data, graceful failure recovery
- Visual aids: architecture diagrams, performance charts, code walkthroughs
- Q&A preparation: anticipating critical questions and responding with evidence
- The ethics of technical storytelling: accuracy, modesty, and intellectual honesty

### Lecture Notes

The technical demonstration has been compared to a doctoral defense, a courtroom cross-examination, and a theatrical performance. It contains elements of all three: the student must defend claims with evidence, withstand skeptical interrogation, and maintain audience engagement. By 2040, the UoY capstone demo has standardized to a 20-minute presentation followed by 15 minutes of Q&A, evaluated by a panel of three faculty members and one external engineer from industry or government. The evaluation rubric weights technical depth (40%), clarity of communication (25%), quality of evidence (20%), and response to questions (15%).

The **presentation structure** follows a well-established arc, refined by the UoY Communication Guild over two decades. The opening (2 minutes) establishes the problem's significance and the student's motivation. The approach section (4 minutes) explains the architectural and algorithmic choices, citing ADRs from Lecture 8. The implementation section (6 minutes) demonstrates the working system through live interaction or video, highlighting at least one technically sophisticated component. The evaluation section (4 minutes) presents quantitative results: performance benchmarks, test coverage, usability scores, and fairness metrics. The limitations section (2 minutes) is not an apology but a demonstration of intellectual maturity: honest discussion of what the system cannot do and why. The future work section (2 minutes) proposes concrete extensions, grounded in the limitations just discussed.

**Live demos** are high-risk, high-reward. A successful live demo creates confidence and engagement that recorded video cannot match. A failed live demo—servers down, models crashing, network timeouts—can derail an otherwise excellent presentation. The lecture teaches risk mitigation: **recorded fallbacks** (pre-recorded videos of all demo paths, ready to play if live execution fails), **deterministic demo data** (fixed seeds, pre-populated databases, and mock external services to eliminate variability), and **graceful failure recovery** (if a component fails, the presenter acknowledges it, pivots to the recorded fallback, and uses the failure as a teaching moment about resilience). The 2034 *Demo Disaster Protocol*, adopted by UoY after a notorious incident involving a quantum circuit demo that decohered mid-presentation, mandates that all capstone demos have at least two independent fallback paths.

**Visual aids** must serve the narrative, not distract from it. Architecture diagrams (produced with the C4 model or UoY's `bifröst-diagram` tool) should be readable from the back row. Performance charts must include error bars or confidence intervals; unqualified mean values are considered sloppy. Code walkthroughs should focus on a single critical function or algorithmic insight, not scroll through files. The lecture provides templates for each visual type and critiques common errors: overcrowded slides, unreadable fonts, and charts without labeled axes.

**Q&A preparation** separates strong presentations from weak ones. The faculty panel is instructed to ask challenging questions: "Why didn't you use X?" "Your benchmark compares against an outdated baseline." "This component appears to violate the principle of least privilege." The lecture advises students to anticipate at least 10 critical questions before the demo and prepare evidence-based responses. A useful technique is the **pre-mortem**: before the demo, the team imagines that the presentation has failed and brainstorms the most likely causes. These become the questions to prepare for. The response protocol is: acknowledge the question's validity, provide evidence, and if the question exposes a genuine limitation, discuss how the team would address it with more time or resources.

**Technical storytelling ethics** demand intellectual honesty. It is tempting to cherry-pick the best benchmark, hide the failed experiment, or claim generality where only a special case was tested. The UoY capstone code of conduct requires that all claims be reproducible from committed code and that limitations be disclosed proactively. The lecture praises the 2037 capstone project *Muninn-Flight* (a drone navigation system), whose presentation included a slide titled "Five Ways This System Will Fail"—detailing edge cases the team had identified but not solved. The panel cited this slide as exemplary intellectual maturity. Students are encouraged to emulate this approach: modesty in claims, precision in evidence, and honesty about boundaries.

### Required Reading

- Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2nd Edition). Graphics Press. Chapters 4–6 (chart design principles).
- Yggdrasil Communication Guild (2035). "The Capstone Demo: Structure, Preparation, and Delivery." *UoY Engineering Communication Handbook*.
- Yggdrasil Faculty Senate (2034). "The Demo Disaster Protocol: Risk Mitigation for Live Technical Demonstrations." Internal policy document.
- *Muninn-Flight Capstone Presentation* (2037). Exemplar recording, UoY Digital Archives.
- Freyjasdottir, R. G. (2038). "Honest Technical Storytelling: The Ethics of Capstone Presentation." *UoY Engineering Ethics Quarterly*, 5(2), 88–101.

### Discussion Questions

1. The pre-mortem technique asks students to imagine failure and work backward. How does this differ from defensive pessimism, and what psychological benefits might it offer beyond Q&A preparation?
2. Should a capstone presenter acknowledge a live demo failure explicitly, or smoothly transition to a recorded fallback without mentioning the failure? What ethical and rhetorical considerations govern this choice?
3. The "Five Ways This System Will Fail" slide was praised by the 2037 panel. Why might admitting limitations strengthen rather than weaken a technical presentation?
4. Visual aids must be readable from the back row. What font sizes, contrast ratios, and chart resolutions are necessary for a 50-seat lecture hall with a standard projector?

### Practice Problems

- Prepare a complete 20-minute capstone demo, including all slides, visual aids, and demo scripts. Conduct a dress rehearsal with peers and collect structured feedback using the UoY rubric.
- Generate a list of 15 critical questions your capstone might face. For each, prepare a 30-second evidence-based response. Role-play the Q&A with a peer acting as skeptical panelist.

---

ᛃ **Lecture 12: Portfolio Curation, Publication, and Professional Transition**

**Course:** CS407 — Capstone Project II  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

The capstone does not end with the demo. This final lecture addresses the transition from student to professional: curating a public portfolio, publishing artifacts, archiving data, and maintaining the system beyond graduation. Students will learn to package their work for diverse audiences—employers, graduate admissions committees, open-source communities, and the public—while respecting privacy, intellectual property, and the long-term sustainability of their creations.

### Key Topics

- Portfolio curation: GitHub profiles, personal sites, and the narrative arc of a body of work
- Publishing: open-source licenses, academic preprints, and industry blog posts
- Data archiving and system handoff: documentation, maintainership, and deprecation planning
- Professional identity: from student to engineer, researcher, or entrepreneur
- The long now: obligations to systems that outlive their creators

### Lecture Notes

The transition from capstone completion to professional life is a rite of passage, and like all rites, it involves transformation of identity. The student who submits their final commit is not yet an engineer; they become one through the public presentation, portfolio curation, and ongoing maintenance of their work. This lecture, the capstone's closing session, addresses the practical and existential dimensions of this transition.

**Portfolio curation** is the art of selecting and framing work for external audiences. By 2040, the software engineering portfolio has evolved from a simple GitHub profile to a curated narrative: a personal website that tells the story of the engineer's growth, values, and capabilities. The UoY Career Services office provides a portfolio template with five required sections: "About" (values and interests), "Projects" (capstone and significant coursework, with technical writeups and live demos), "Writing" (blog posts, documentation, and academic papers), "Speaking" (presentations and demos), and "Contributions" (open-source patches, mentorship, and community engagement). The lecture emphasizes that portfolios are not CVs: they should reveal judgment, taste, and intellectual curiosity, not merely list technologies used.

**Publishing** extends the capstone's impact beyond the evaluation committee. Open-source licensing is the first decision: MIT for permissive reuse, GPL for copyleft, Apache 2.0 for patent protection, or proprietary for commercial potential. The lecture covers license compatibility (e.g., GPL code cannot be relicensed under MIT) and the practicalities of repository hygiene (README, LICENSE, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY). For students pursuing graduate study, academic preprints on arXiv or the UoY institutional repository provide early visibility and citation potential. For students entering industry, technical blog posts on Medium, Dev.to, or the UoY student journal translate capstone insights into accessible narratives. The 2036 *Capstone Publication Guide* provides templates for each format.

**Data archiving and system handoff** address the reality that most capstone projects are not maintained after graduation. This is not a failure but a natural lifecycle; however, abandoned systems can become liabilities if they contain personal data, exposed credentials, or unpatched vulnerabilities. The lecture teaches **responsible deprecation**: archiving code to a persistent repository (Zenodo, Figshare, or the UoY digital archive), documenting the shutdown process, notifying any users, and securely deleting sensitive data. For projects with ongoing value, the lecture covers **maintainership transition**: finding a successor maintainer, documenting tribal knowledge, and gradually reducing involvement. The UoY Alumni Network maintains a registry of capstone projects seeking maintainers, matching graduates with current students.

**Professional identity** is shaped by the capstone experience. The lecture surveys the three primary paths: industry engineering (building production systems), academic research (advancing knowledge), and entrepreneurship (creating organizations). Each path demands different portfolio emphases: industry portfolios highlight scale and reliability; academic portfolios highlight novelty and rigor; entrepreneurial portfolios highlight market validation and team leadership. The UoY Mentorship Program pairs each capstone student with an alum who has taken their preferred path, providing advice and networking. The lecture includes a self-assessment exercise in which students identify their values (e.g., impact, autonomy, security, recognition) and map them to career paths and organizations.

**The long now** is the lecture's closing theme, drawn from the Long Now Foundation's 10,000-year clock project. Software systems, especially those deployed to the public internet, can outlive their creators by decades. The engineer has an obligation to consider: Who will maintain this when I am gone? What data will persist, and who will have access? What are the failure modes if the system is abandoned? The 2032 *Digital Legacy Accord*, signed by UoY and 47 other universities, requires that all student-deployed systems include a "sunset clause": an automatic shutdown or transition plan triggered if the system is unmaintained for 12 months. The lecture ends with a meditation on the engineer's responsibility to the future—not as a burden, but as an honor.

### Required Reading

- Yggdrasil Career Services (2040). "The Complete Portfolio: A Guide for Computing Graduates." UoY Press.
- OSI (2025). *Open Source Licenses: A Comprehensive Guide to SPDX-Listed Licenses*. Open Source Initiative.
- Brand, S. (1999). *The Clock of the Long Now: Time and Responsibility*. Basic Books. Chapters 1 and 7.
- Digital Legacy Accord (2032). "Student-Deployed Systems: Sunset Clauses and Responsible Deprecation." International University Consortium.
- Freyjasdottir, R. G. (2039). "From Capstone to Career: The Portfolio as Identity Construction." *UoY Engineering Education Journal*, 12(4), 445–460.

### Discussion Questions

1. A portfolio reveals judgment and taste, not merely technical competence. What aspects of your capstone best demonstrate your judgment, and how would you frame them for an employer versus a graduate admissions committee?
2. Most capstone projects are abandoned after graduation. Is this wasteful, or is the educational value independent of long-term maintenance? What responsibilities, if any, does the student have to users of an abandoned system?
3. The sunset clause requires automatic shutdown after 12 months of non-maintenance. What technical and ethical challenges does this requirement pose for systems that process ongoing user data?
4. The Long Now Foundation asks us to think in 10,000-year timescales. Is this perspective relevant to software engineering, or is software too ephemeral for long-term thinking to be meaningful?

### Practice Problems

- Create a complete portfolio website for your capstone, including the technical writeup, live demo link, source code repository, and a blog post explaining one technical decision to a general technical audience.
- Draft a sunset clause for your capstone system, including: data archival procedures, user notification timeline, credential rotation plan, and domain/dns transition strategy.

---

## Final Examination Preparation

The CS407 final examination is a **comprehensive practical assessment** conducted over 72 hours. Students receive a partially implemented capstone system (different from their own) and must:

1. **Complete implementation** of two unfinished features, using the existing architecture and test suite.
2. **Write and execute tests** achieving ≥85% coverage on the new code.
3. **Profile and optimize** a performance bottleneck, documenting before/after benchmarks with confidence intervals.
4. **Produce a threat model** for the system, identifying at least 10 threats and their mitigations.
5. **Write a 2,000-word technical memo** explaining the changes to a hypothetical new team member.

The examination is open-book, open-internet, and open-AI-assistant, but all work must be individually authored and committed to the provided repository with timestamps verified by the UoY proctoring system.

### Sample Examination Tasks

1. You are handed a capstone system for a distributed task scheduler. The scheduler lacks retry logic and observability. Implement exponential backoff with jitter, add OpenTelemetry spans for all scheduling decisions, and write tests that verify both the retry behavior and the trace structure.
2. The system's CI pipeline builds but does not deploy. Extend the pipeline to deploy to a staging Kubernetes namespace on commit to `main`, with automatic rollback if error rate exceeds 1% for 5 minutes.
3. A performance analysis shows that database query latency is the bottleneck. Implement query result caching with Redis, including cache invalidation on write, and demonstrate a ≥50% reduction in p99 latency.
4. The system processes user uploads without virus scanning. Integrate ClamAV scanning into the upload handler, quarantine infected files, and write integration tests that verify the quarantine behavior using the EICAR test file.

### Examination Grading Rubric

| Criterion | Weight | Excellent (A) | Good (B) | Satisfactory (C) | Unsatisfactory (D/F) |
|-----------|--------|---------------|----------|------------------|----------------------|
| Implementation correctness | 25% | All features correct, edge cases handled | Minor edge case missed | Core features correct, significant edge cases missed | Incorrect or incomplete |
| Test quality and coverage | 20% | ≥85% coverage, property-based tests, clear failure messages | ≥80% coverage, good test names | ≥70% coverage, some brittle tests | <70% coverage or no tests |
| Performance optimization | 15% | Benchmarked with CIs, ≥40% improvement, well-documented | Benchmarked, ≥30% improvement | Some benchmarking, minor improvement | No benchmarking or no improvement |
| Threat model quality | 15% | 10+ threats, STRIDE categories, mitigations mapped | 8+ threats, good coverage | 6+ threats, some gaps | <6 threats or superficial |
| Technical memo | 15% | Clear, well-structured, audience-appropriate | Good structure, minor clarity issues | Readable but uneven | Unclear or incomplete |
| Code style and documentation | 10% | Clean, consistent, well-documented, ADR for major decisions | Good style, minor inconsistencies | Acceptable style, some missing docs | Unreadable or undocumented |

---

*The code is forged. The tests are green. The system is deployed. The Wyrd is woven.* ᛟ

— Runa Gridweaver Freyjasdottir, Capstone Project II, University of Yggdrasil, 2040
