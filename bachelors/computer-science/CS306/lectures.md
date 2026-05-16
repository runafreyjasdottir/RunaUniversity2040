# CS306: Software Testing & Quality Assurance
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4
**Prerequisites:** CS201 — Data Structures & Algorithms II; CS203 — Database Systems; CS206 — Software Engineering Principles
**Description:** Software testing is the act of trading time for confidence. Every test you write today is a bet: a bet that the time spent writing and maintaining the test will be less than the time you would lose finding and fixing the bug it catches. This course transforms students from programmers who "test sometimes" into disciplined practitioners who test strategically, systematically, and continuously. It covers the full spectrum of testing — from unit tests (the foundation) through integration tests (the glue) to end-to-end tests (the contract), from property-based testing (the algorithm's best friend) to fuzz testing (the security scryer), from mutation testing (the test of the tests) to performance testing (the scaler's crucible). Students learn to wield the testing tools of 2040: pytest with advanced plugins, property-based testing with Hypothesis, fuzzing with LibFuzzer and AFL++, contract testing with Pact, mutation testing with MutPy, and the continuous integration pipelines (GitHub Actions, GitLab CI) that enforce quality gates. The course also covers the organisational dimensions of quality — code review, static analysis, technical debt management, and the psychology of bug prevention. The Norse framing is the *Gjallarhorn* — a horn whose sound reveals what is hidden. Testing is a continuous blowing of the horn on our own code, revealing the hidden bugs before they reach the user.

---

## Lecture 1: The Economics of Testing — Why We Test, When We Test, and When We Don't

Testing is not a technical activity; it is an economic one. Every test is an investment: you spend time writing it today in order to save time (or money, or reputation, or lives) later. The economics of testing determine the optimal amount of testing for a given system — and the answer varies wildly depending on what the system does.

The **cost of defect curve** has been known since the 1970s (Boehm, 1976): the cost of fixing a bug increases exponentially as it moves through the development lifecycle. A bug caught during requirements analysis costs $100 to fix. A bug caught during design costs $500. A bug caught during coding costs $1,000. A bug caught during testing costs $5,000. A bug caught in production costs $10,000–$100,000. For safety-critical systems (avionics, medical devices, autonomous vehicles), a production bug can cost lives and billions of dollars — the Boeing 737 MAX disasters (2018–2019) cost over $20 billion and 346 lives, traced to a software flaw that better testing might have caught.

The **testing pyramid** (Cohn, 2009) provides a framework for allocating testing effort:
- **Base — Unit tests (70%):** Test individual functions, methods, or classes in isolation. Fast (milliseconds), reliable, and cheap to write. Provide the foundation of test coverage.
- **Middle — Integration tests (20%):** Test interactions between components — APIs, database queries, service boundaries. Slower (seconds) but test the "glue."
- **Top — End-to-end (E2E) tests (10%):** Test the full system, from UI to backend to database. Slow (minutes), fragile, and expensive. Test the most valuable user journeys.

The pyramid is a heuristic, not a law. For a microservices architecture, integration tests may dominate (because the service boundaries are where most bugs live). For a data-processing pipeline, unit tests on the transformation functions may dominate. The art is knowing when to deviate from the pyramid.

**Code coverage** is the most commonly abused metric in software engineering. Line coverage, branch coverage, path coverage, and condition coverage each measure a different aspect of "how much code is exercised by the tests." A team that targets 100% line coverage will inevitably write surface-level tests that tick boxes without finding bugs. A team that targets meaningful behavioural coverage — covering the edge cases, the error paths, the boundary conditions — will find bugs even at 60% line coverage. The lesson: coverage is a diagnostic, not a target.

**Shift-left testing** is the practice of moving testing earlier in the development lifecycle: test requirements (with specification-based testing), test design (with architectural testability reviews), test code during development (with TDD, incremental testing), and test deployments (with canary releases and blue-green deployments). Shift-left reduces the cost of defects by catching them when they are cheapest to fix.

**Required Reading:**
- Barry W. Boehm, *Software Engineering Economics* (Prentice-Hall, 1981), chs. 3–4 — the cost of defect curve
- Mike Cohn, *Succeeding with Agile: Software Development Using Scrum* (Addison-Wesley, 2009), ch. 10 — the testing pyramid
- Cem Kaner, James Bach & Bret Pettichord, *Lessons Learned in Software Testing* (Wiley, 2001), lessons 1–15
- Lisa Crispin & Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams* (Addison-Wesley, 2009), chs. 1–5
- UoY Testing Economics Simulator: Calculate the optimal test investment for different project types (2040)

**Discussion Questions:**
1. The testing pyramid recommends 70/20/10 split for unit/integration/E2E tests. Under what circumstances would you deviate from this ratio — and what evidence would convince you to change?
2. Code coverage is widely used as a quality gate in CI pipelines. What are the strongest arguments for and against mandating a minimum coverage percentage?
3. Shift-left testing moves testing earlier, but it also moves testing to earlier *phases of understanding* — requirements may be incomplete, design may be unsettled. How do we test what we don't yet understand?

---

## Lecture 2: Unit Testing — The Foundation

Unit testing is the practice of testing individual units of code — functions, methods, classes — in isolation from their dependencies. A unit test exercises one behaviour of one unit, running in milliseconds, with no network calls, no database queries, no file I/O. The **FIRST principles** (Object Mentor, 2006) define the properties of a good unit test:

- **Fast:** Tests run in milliseconds. If they take seconds, developers won't run them.
- **Isolated:** A test never depends on other tests. No shared state, no test ordering dependencies.
- **Repeatable:** A test produces the same result every time, on every machine. No flakiness from timing, network, or environment.
- **Self-verifying:** The test passes or fails based on its own assertions. No manual inspection of output.
- **Timely:** Tests are written before (TDD) or alongside (defensive testing) the production code.

**Test doubles** replace real dependencies in unit tests:
- **Stubs:** Provide canned answers to calls made during the test. "When you ask for the user's name, return 'Alice'."
- **Mocks:** Verify interactions — "Was this method called with these arguments?" Mocks assert on behaviour, not state.
- **Fakes:** Lightweight implementations of real dependencies (an in-memory database instead of PostgreSQL).
- **Spies:** Record calls for later verification without replacing the dependency's behaviour.
- **Dummies:** Passed but never actually used.

The **arrange-act-assert** pattern structures every test:
```python
def test_discount_for_loyal_customers():
    # Arrange
    customer = Customer("Alice", loyalty_years=10)
    calculator = DiscountCalculator()
    
    # Act
    discount = calculator.calculate(customer)
    
    # Assert
    assert discount == 0.15  # 15% for 10-year loyalty
```

**Property-based testing** (Claessen & Hughes, 2000) inverts the testing paradigm. Instead of writing specific examples, you write *properties* that must hold for all inputs, and the framework (Hypothesis in Python, QuickCheck in Haskell) generates test cases automatically. For example, the roundtrip property: for any list `xs`, `sorted(sorted(xs)) == sorted(xs)` (sorting is idempotent). Property-based testing excels at finding edge cases you never thought to test — a phenomenon called the **small-scope hypothesis**: most bugs have small counterexamples.

**Required Reading:**
- Roy Osherove, *The Art of Unit Testing* (3rd ed., Manning, 2020/2040), chs. 1–6
- Martin Fowler, "Mocks Aren't Stubs" (martinfowler.com, 2007)
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code* (Addison-Wesley, 2007)
- Koen Claessen & John Hughes, "QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs" (*ICFP*, 2000): 268–279
- Zac Hatfield-Dodds & David R. MacIver, "Hypothesis: A New Approach to Property-Based Testing" (*Journal of Open Source Software* 4:43, 2019): 1891
- UoY Unit Testing Lab: Write parameterised tests with pytest and property-based tests with Hypothesis (2040)

**Discussion Questions:**
1. Mocks assert on behaviour (was the method called?), while stubs supply data (what should the method return?). When is behavioural assertion appropriate — and when does it make tests brittle (the "change detector" problem)?
2. Property-based testing generates random inputs. How do you ensure that the generated inputs are realistic — and how do you shrink a failing test case to its minimal form?
3. The FIRST principle says tests must be fast. How fast is "fast" — and at what point does a 100ms test suite with 10,000 tests become too slow for the TDD cycle?

---

## Lecture 3: Test-Driven Development — Red, Green, Refactor

Test-Driven Development (TDD) is not a testing technique; it is a *design* technique that uses tests as a specification language. The mantra is **red, green, refactor**:

1. **Red:** Write a failing test. No production code exists yet for this feature. The test should fail for exactly one reason: the feature hasn't been implemented.
2. **Green:** Write the *simplest possible code* to make the test pass. Not the cleanest, not the most general — just the code that satisfies the test.
3. **Refactor:** Improve the code while keeping the tests green. Remove duplication, improve naming, extract methods, generalise.

The cycle length is 30–120 seconds. Each cycle adds one small behaviour. The cumulative effect after hundreds of cycles is a codebase that is:
- **Thoroughly tested:** Every behaviour has a test.
- **Cleanly designed:** The tests drive the design toward loosely coupled, high-cohesion modules — because tightly coupled modules are hard to test.
- **Safe to change:** The test suite is a safety net; change the code with confidence.

**Kent Beck** (who re-discovered TDD in the 1990s, building on earlier work by the Cleanroom Software Engineering community) describes TDD as "programming with the fear turned off." The test suite is not a burden — it is the foundation of courage.

**Red-green-refactor** applies at multiple levels:
- **Micro-level (TDD):** One test, one function. The classic cycle.
- **Meso-level (ATDD / Acceptance TDD):** One acceptance test, one user story. The acceptance test defines "done" for the story.
- **Macro-level (BDD — Behaviour-Driven Development):** Scenarios written in Gherkin syntax (`Given-When-Then`) define the system's behaviour. BDD tools (Cucumber, SpecFlow) parse the scenarios into executable tests.

The **TDD debate** has raged for two decades: proponents claim TDD reduces defect density by 40–90% (based on studies at IBM, Microsoft, and others); opponents argue that the evidence is confounded (TDD teams also tend to write more tests overall, measure coverage, and have better design). The most honest summary: TDD is a practice, not a silver bullet. It works when it becomes a habit — and it becomes a habit only if you practise it for several weeks until the cycle is automatic.

**Required Reading:**
- Kent Beck, *Test-Driven Development: By Example* (Addison-Wesley, 2002) — the definitive book
- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship* (Prentice-Hall, 2008), chs. 9–10
- David Astels, *Test-Driven Development: A Practical Guide* (Prentice-Hall, 2003)
- Laurie Williams & Robert L. Kessler, *Pair Programming Illuminated* (Addison-Wesley, 2002) — TDD and pair programming often go together
- UoY TDD Dojo: Practise the red-green-refactor cycle with coding katas (2040)

**Discussion Questions:**
1. TDD is often described as a "design technique, not a testing technique." What does the design come from — and how does the need for testability drive better design?
2. The "simplest possible code" in the green phase is rarely the final code. How do you balance the need for speed (get green quickly) with the need for quality (don't paint yourself into a corner)?
3. TDD works well for greenfield development. How do you apply TDD to legacy code — where you can't write a test without breaking existing behaviour?

---

## Lecture 4: Integration Testing — The Glue That Holds Systems Together

Unit tests verify individual components in isolation. Integration tests verify that components work together — that the API returns the right status code, that the database query returns the right rows, that the message queue delivers the right payload. Integration testing is where most real-world bugs live: the component interactions.

**Test doubles for integration** are different from unit test doubles. At the integration level, you typically use:
- **Containerised dependencies:** Docker-compose or Testcontainers spin up real PostgreSQL, Redis, Kafka containers for the duration of the test suite.
- **API mocking tools:** WireMock, MockServer, or Mountebank simulate HTTP APIs with configurable responses, delays, and failures.
- **Service virtualization:** Simulate entire third-party services (payment gateways, email providers, authentication providers) with realistic behaviour.

**The contract test** (a.k.a. consumer-driven contract test, CDC) tests the agreement between a service consumer and a service provider. Pact is the leading contract-testing framework: the consumer defines a contract (an interaction), Pact records it, and the provider replays the contract to verify it still fulfils the agreement. Contract tests are faster and more reliable than full end-to-end tests — they test the boundary without deploying the whole system.

**Database integration testing** requires special care. Tests must:
- Be **isolated:** Each test starts with a known database state (usually via transactions that are rolled back after the test).
- Be **fast:** In-memory databases (H2, SQLite) provide speed at the cost of fidelity (SQLite is not PostgreSQL).
- Be **repeatable:** No test must depend on the side effects of another test.
- Cover **schema migrations:** Tests verify that the application works with both the old and new schema during a rolling deployment.

The **Testcontainers** library (Python, Java, Go, .NET) provides lightweight, throwaway instances of common databases, message queues, and web servers. A Testcontainers test starts a container before the test suite and destroys it afterward — ensuring a clean environment for every run.

**Required Reading:**
- Martin Fowler, "Integration Test" (martinfowler.com, 2003)
- Richard Rodger, *The Tao of Microservices* (Manning, 2017), chs. 4–5
- Beth Skurrie & Ronald Holshausen, *Pact: Consumer-Driven Contract Testing* (docs.pact.io, continuously updated)
- Richard Älvebrand & Oleg Šelajev, *Testcontainers* (testcontainers.com, continuously updated)
- UoY Integration Testing Lab: Write contract tests with Pact and database tests with Testcontainers (2040)

**Discussion Questions:**
1. Contract tests are positioned as the "sweet spot" between unit and E2E tests. Under what circumstances do contract tests give a false sense of security (because they miss behavioural differences that only manifest in full deployment)?
2. Testcontainers spins up real dependencies, which introduces latency and resource consumption. At what point does the integration test suite become too slow — and what strategies mitigate this?
3. Database integration tests with in-memory databases (SQLite) vs containerized databases (PostgreSQL in Testcontainers) — what is the cost of using the wrong one?

---

## Lecture 5: End-to-End Testing — The Full Stack, the Full User Journey

End-to-end (E2E) testing exercises the entire system — UI, API, database, external services — as a user would. E2E tests are the most realistic and the most expensive: they take minutes, they are fragile (a network timeout, a CSS class change, or a database hiccup can cause a spurious failure), and they hard to debug. But they are the only tests that verify the system works as a whole.

**UI test automation** frameworks simulate user interactions in a real browser:
- **Playwright** (Microsoft, 2020) is the leading framework as of 2040. It supports Chromium, Firefox, and WebKit with auto-waiting (the framework waits for elements to be ready before interacting), network interception, and mobile emulation.
- **Cypress** (2017) provides a developer-friendly API with time-travel debugging (you can see every command's screenshot and DOM snapshot).
- **Selenium** (2004) is the grandparent — still widely used but losing ground to Playwright's speed and reliability.

E2E test design follows the **page object model (POM)** — each page of the application is represented as a class that encapsulates the page's elements and interactions:
```python
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.submit = page.locator("button[type='submit']")
    
    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.submit.click()
        return DashboardPage(self.page)
```

**Data-driven E2E tests** run the same scenario with different input data and expected outcomes. The test itself stays the same; only the data changes. This separates test logic from test data, making tests more maintainable.

**Visual regression testing** compares screenshots of the application with baselines. Percy and Applitools are the leading tools. Visual regression catches layout bugs, colour changes, and font issues that would slip through functional tests. The challenge is managing baselines — when a change is intentional, the baseline must be updated, and false positives from browser rendering differences must be minimised.

**Required Reading:**
- Playwright Documentation (playwright.dev, continuously updated) — the canonical reference
- Martin Fowler, "Page Object" (martinfowler.com/bliki/PageObject.html)
- Angie Jones, *Test Automation Fundamentals* (Online course/self-published, 2023/2040)
- UoY E2E Testing Lab: Write a Playwright test suite for a sample web application (2040)

**Discussion Questions:**
1. E2E tests are slow and fragile. How do you decide which user journeys to cover with E2E tests vs integration tests vs unit tests — and what is the cost-benefit threshold for adding one more E2E test?
2. Visual regression testing compares screenshots pixel-by-pixel. How do you handle intentional UI changes, cross-browser rendering differences, and dynamic content (animations, loading spinners)?
3. Page objects encapsulate page structure but add maintenance overhead. What are the alternatives — and when would you prefer a more lightweight approach?

---

## Lecture 6: Fuzz Testing — Finding the Unfindable

Fuzz testing (or "fuzzing") is the art of feeding a program with invalid, unexpected, or random data and observing whether it crashes. Fuzzing is the most effective technique for finding security vulnerabilities and memory safety bugs — Google's OSS-Fuzz project has found over 50,000 bugs in open-source software since 2016, including critical vulnerabilities in OpenSSL, libpng, and the Linux kernel.

**Black-box fuzzing** generates random inputs with no knowledge of the program's internal structure. Tools like the classic BSD `fuzz` tool (Barton Miller, 1990) and `zzuf` generate random byte streams. Black-box fuzzing is simple but inefficient — most random inputs are rejected early by input parsers.

**Coverage-guided fuzzing** (the dominant paradigm since AFL, 2013) uses code coverage feedback to guide input generation:
1. Start with a **seed corpus** of valid inputs.
2. Mutate a seed input (bit flips, byte insertions/deletions, arithmetic mutations).
3. Run the mutated input through the program, instrumented to measure code coverage.
4. If the mutated input covers new code (new basic blocks, new edges in the control-flow graph), add it to the seed corpus.
5. Repeat until no new coverage is found.

**AFL++** and **LibFuzzer** are the leading coverage-guided fuzzers. LibFuzzer links the test harness directly into the target function, enabling extremely fast fuzzing (thousands of inputs per second). For Python, the **Atheris** fuzzer (Google) instruments Python bytecode for coverage-guided fuzzing.

**Structure-aware fuzzing** generates inputs that respect the grammar of the input format. Instead of randomly mutating bytes, the fuzzer mutates the abstract syntax tree of the input. This is essential for formats with complex structures (PDF, ELF, network protocols). **Grammartech** and **NAUTILUS** (for network protocols) generate valid mutants of complex inputs.

**Required Reading:**
- Michael Zalewski, *American Fuzzy Lop* (lcamtuf.coredump.cx/afl/, 2013) — the canonical coverage-guided fuzzer
- Patrice Godefroid, "Fuzzing: Hack, Art, and Science" (*Communications of the ACM* 63:2, 2020): 70–76
- Barton P. Miller, "Fuzz Testing of Application Reliability" (University of Wisconsin, 1990–present) — the origin of fuzzing
- Jonathan Metzman et al., "OSS-Fuzz: Google's Continuous Fuzzing Service for Open Source Software" (*Proceedings of the 2021 Annual Computer Security Applications Conference*)
- UoY Fuzzing Lab: Set up LibFuzzer for a C library and Atheris for a Python parser (2040)

**Discussion Questions:**
1. Coverage-guided fuzzing relies on code coverage feedback. What kinds of bugs are invisible to coverage-guided fuzzing — what would never be found even with infinite fuzzing time?
2. Fuzzing finds buffer overflows, use-after-free, null-pointer dereferences. How do you prioritise which fuzzer-discovered bugs to fix — especially when the fix may itself introduce new bugs?
3. Structure-aware fuzzing requires knowing the input grammar. For a protocol with an undocumented binary format, how would you build a fuzzer?

---

## Lecture 7: Mutation Testing — Testing the Tests

Mutation testing is the ultimate meta-test: it evaluates the quality of your test suite by introducing bugs (mutations) into your code and checking whether the tests catch them. A mutation is a small syntactic change, such as:
- Replacing `>` with `>=`
- Swapping `true` for `false`
- Deleting a method call
- Replacing `a + b` with `a - b`
- Changing a constant value

A test suite's **mutation score** is the percentage of detected mutations. A score of 100% means your tests catch every possible simple mistake — the tests are thorough. A score of 80% means 20% of simple bugs would slip through — there are gaps in the test coverage that need attention.

**MutPy** and **Cosmic Ray** are the leading mutation testing tools for Python. MutPy generates mutants, runs the test suite against each mutant (in parallel), and reports the mutation score. For a codebase with 10,000 lines of code and a test suite that takes 30 seconds, mutation testing with MutPy takes approximately (number of mutants) × 30 seconds — which can be hours for large codebases. **Incremental mutation testing** (run mutants only on changed code) and **parallel execution** (run mutants in parallel across multiple cores or machines) are essential for making mutation testing practical.

**Equivalent mutants** are a long-standing problem: some mutants are semantically equivalent to the original code — they always produce the same output — but are syntactically different. For example, replacing `if (x < 10)` with `if (x <= 9)` produces the same behaviour for integers, but the mutation tool cannot determine this automatically (the problem is undecidable in general). Equivalent mutants inflate the mutation score denominator, making it harder to reach 100%. Detecting equivalent mutants requires human review — and is one of the main reasons mutation testing is difficult to adopt at scale.

**Pit mutation testing** (Jansen & Hovemeyer, 2020) addresses the performance problem by running mutants in a subset of the test suite (only tests that cover the mutated code). If a code line is covered by 5 tests, why run all 10,000 tests on that mutant? This optimisation reduces mutation testing time from hours to minutes.

**Required Reading:**
- Yue Jia & Mark Harman, "An Analysis and Survey of the Development of Mutation Testing" (*IEEE Transactions on Software Engineering* 37:5, 2011): 649–678
- Alex Groce et al., "You Are the Only Possible Oracle: Effective Test Selection for End Users of Interactive Machine Learning Systems" (*IEEE Transactions on Software Engineering*, 2020) — mutation testing for ML
- Goran Petrović & Marko Ivanković, "Mutation Testing at Google" (*ICSE*, 2018) — industrial experience report
- UoY Mutation Testing Lab: Measure the mutation score of your own test suite with MutPy (2040)

**Discussion Questions:**
1. Mutation testing is the most rigorous way to evaluate test quality, but it is computationally expensive. For a CI pipeline that deploys 50 times a day, is mutation testing feasible — and what trade-offs would you accept to make it so?
2. Equivalent mutants are undetectable in general. In practice, what patterns of equivalent mutants are most common — and how would you design a mutation operator set that minimises equivalents?
3. A high mutation score (95%+) gives confidence, but does it give *correctness* confidence? What kinds of bugs would a mutation-tested suite still miss?

---

## Lecture 8: Performance Testing and Scalability Verification

Performance testing verifies that a system meets its non-functional requirements for responsiveness, throughput, and resource consumption. Performance bugs are harder to detect than functional bugs because they manifest only under load and often require statistical analysis (rather than a pass/fail assertion) to identify.

**Load testing** applies a simulated workload to the system and measures response times, throughput, error rates, and resource utilisation. Tools:
- **Locust** (Python): Define user behaviour as Python code; Locust spawns fake users and reports response percentiles (p50, p95, p99).
- **k6** (JavaScript/Go): Script-based load testing with excellent CI integration.
- **Gatling** (Scala): High-performance, DSL-based load testing with detailed HTML reports.

**Stress testing** finds the system's breaking point — the load at which response times increase non-linearly, error rates spike, or the system crashes. The **knee point** (or tipping point) in the response-time curve is the critical metric: it tells you the system's true capacity.

**Endurance testing** (a.k.a. soak testing) applies a moderate load for an extended period (hours to weeks) to identify memory leaks, connection pool exhaustion, and resource accumulation bugs. A system that passes a 5-minute load test may fail after 6 hours of sustained load because of a subtle memory leak.

**Scalability testing** verifies that adding resources (horizontal scaling: more servers; vertical scaling: more CPU/RAM) proportionally improves performance. The **speedup** is measured as:

Speedup(N) = Latency(1) / Latency(N)

where N is the number of servers (or CPU cores). **Amdahl's law** predicts the theoretical maximum speedup given a fraction P of parallelisable work:

Speedup_max = 1 / ((1−P) + P/N)

In practice, scalability is limited by contention for shared resources (database connections, locks, caches) and by coordination overhead (consensus protocols, cache coherence).

**Profiling** identifies performance bottlenecks at the code level. Tools like py-spy (Python), perf (Linux), and Intel VTune sample the call stack of a running program, building a flame graph that shows which functions consume the most CPU time. Donald Knuth's maxim — "premature optimisation is the root of all evil" — means that profiling, not intuition, should drive optimisation efforts.

**Required Reading:**
- Brendan Gregg, *Systems Performance: Enterprise and the Cloud* (2nd ed., Addison-Wesley, 2020/2042)
- Martin L. Abbott & Michael T. Fisher, *The Art of Scalability* (Addison-Wesley, 2009)
- Gene Amdahl, "Validity of the Single Processor Approach to Achieving Large-Scale Computing Capabilities" (*AFIPS*, 1967) — Amdahl's law
- UoY Performance Testing Lab: Load-test a REST API with Locust and profile the bottlenecks (2040)

**Discussion Questions:**
1. Load testing requires generating realistic workloads. How do you model user behaviour — and what are the consequences of an unrealistic workload model?
2. The p99 response time is a common SLO. Why is p99 more informative than the average — and what makes p99 so hard to stabilise?
3. Amdahl's law limits parallel speedup. How do you identify the non-parallelisable fraction P in a complex distributed system?

---

## Lecture 9: Static Analysis and Code Quality

Static analysis (a.k.a. linting) finds bugs, code smells, and security vulnerabilities *without running the code*. The best time to find a bug is before you run the code — static analysis makes that possible.

**Linters** (flake8, pylint, ESLint, Clippy for Rust) enforce coding style and catch common mistakes:
- Unused variables
- Unreachable code
- Import errors
- Formatting violations

**S**tatic application security testing (SAST) tools (Bandit for Python, Semgrep for multi-language, SonarQube for enterprise) detect security vulnerabilities:
- SQL injection: concatenating user input into SQL queries
- XSS: inserting user input into HTML without escaping
- Hardcoded credentials: passwords, API keys, tokens
- Path traversal: constructing file paths from user input

**Abstract interpretation-based analysers** (Astrée, Frama-C Value Analysis, Infer) go beyond pattern matching. They track the possible values of variables across the program and prove the absence of certain classes of bugs — no array-out-of-bounds, no division-by-zero, no null-pointer dereference. The cost is false alarms: the analyser may report a potential bug that cannot occur in practice.

**Code reviews** are the most effective known method for finding bugs. Studies consistently show that code review finds 60–90% of the bugs in a change, more than any automated tool. But code review is expensive — it takes time from senior developers. The most effective code reviews are:
- **Small:** Changes under 200 lines get 2–3× more thorough review than changes over 500 lines.
- **Focused:** A review that checks one thing (logic, security, performance) is more effective than a review that checks everything.
- **Supported by automation:** Linters, formatters, and static analysis should catch the trivial issues before the human sees the code.

**Required Reading:**
- Michael Fagan, "Design and Code Inspections to Reduce Errors in Program Development" (*IBM Systems Journal* 15:3, 1976): 182–211 — the origin of code inspection
- Andrew Binstock, "Integration of Static Analysis into the CI Pipeline" (*Communications of the ACM* 63:6, 2020): 42–44
- Paul Anderson, "Static Code Analysis in Practice" (*IEEE Security & Privacy* 5:5, 2007): 53–57
- UoY Static Analysis Lab: Configure Semgrep rules for a Python project and run Astrée on a C program (2040)

**Discussion Questions:**
1. Static analysis tools produce false alarms. What false-positive rate is acceptable — and how do you design a triage workflow for false positives so they don't accumulate?
2. Code review is more effective than any automated tool, yet many organisations struggle to maintain code review discipline. What organisational practices — and tool support — make code review sustainable?
3. Abstract interpretation can prove the *absence* of certain bugs, but only for specific properties. For a safety-critical system, how do you decide which properties must be proved (at high cost) vs which can be tested (at lower cost but less certainty)?

---

## Lecture 10: Continuous Integration and Quality Gates

Continuous Integration (CI) is the practice of merging code changes into a shared mainline multiple times per day, with each merge triggering an automated build and test suite. The goal is to detect integration problems early — before they compound into the "merge hell" that plagued the era of monthly releases.

The **CI pipeline** typically stages:
1. **Lint:** Static analysis (fast, <30 seconds)
2. **Build:** Compile or package the code
3. **Unit tests:** Fast, reliable (<2 minutes)
4. **Integration tests:** Slower, test component interactions (<10 minutes)
5. **Static analysis (SAST):** Security and quality checks (<5 minutes)
6. **Package and deploy:** Build the deployable artifact
7. **End-to-end tests (optional):** Full-stack tests on the deployed artifact
8. **Performance tests (optional):** Load test on the deployed artifact

**Quality gates** are automated checks that must pass before a change can proceed to the next stage — or be deployed. A quality gate is a binary pass/fail check on a measurable property:
- Test coverage ≥ 80%
- Mutation score ≥ 90%
- No critical or high-severity static analysis violations
- No known vulnerabilities in dependencies (checked by Dependabot, Snyk)
- E2E tests — all pass

The key to effective quality gates is **tuning**: if a gate is too strict (blocks good changes), developers will work around it. If it is too lenient (passes bad changes), it provides no value. The art of the CI engineer is finding the thresholds that catch real problems without blocking productive work.

**Trunk-based development** is the CI-compatible branching strategy: developers commit directly to `main` (or `trunk`) in small batches, using feature flags to hide incomplete features. Long-lived branches (the GitFlow-style `feature` branch that lives for weeks) are antithetical to CI — they accumulate integration risk that pops when the branch merges.

**Required Reading:**
- Jez Humble & David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation* (Addison-Wesley, 2010), chs. 4–6
- Paul Duvall, Steve Matyas & Andrew Glover, *Continuous Integration: Improving Software Quality and Reducing Risk* (Addison-Wesley, 2007)
- Nicole Forsgren, Jez Humble & Gene Kim, *Accelerate: The Science of Lean Software and DevOps* (IT Revolution, 2018) — evidence-based insights on CI/CD
- UoY CI Lab: Set up a GitHub Actions pipeline with lint, test, build, and deploy stages (2040)

**Discussion Questions:**
1. A CI pipeline that takes 60 minutes discourages developers from committing. A pipeline that takes 5 minutes may miss bugs that only manifest in longer-running tests. How do you balance speed and thoroughness?
2. Trunk-based development requires feature flags. What is the operational cost of maintaining feature flags — and how do you clean up flags once a feature is fully rolled out?
3. Quality gates create a tension between velocity and safety. How do you measure the *effectiveness* of a quality gate — and how do you tune gates when the first measurement shows they are blocking good changes?

---

## Lecture 11: Testing in Production — Canaries, Experiments, and Observability

"Testing in production" sounds reckless — and sometimes it is. But for systems that cannot be faithfully replicated in a staging environment (because of the complexity of real-world data, traffic patterns, or service dependencies), testing in production is the only way to gain confidence.

**Canary deployments** gradually route a small percentage of production traffic to a new version:
1. Deploy the new version to 1% of servers.
2. Monitor error rates, latency, and business metrics for 10 minutes.
3. If metrics are healthy, increase to 10% of servers.
4. Continue up to 100% (or roll back if metrics degrade).

The **analysis of canary results** requires statistical rigour. The metrics from the canary group and the control group are compared using hypothesis testing (Student's t-test, Mann–Whitney U). Because the number of comparisons is large (thousands of metrics), **multiple hypothesis correction** (Bonferroni, Benjamini-Hochberg) is essential to avoid false positives.

**A/B testing** (a.k.a. online experimentation for product features) is different from canary testing: it tests the business effect of a feature, not its technical correctness. An A/B test compares two groups of users — one exposed to the new feature, one not — and measures the difference in a business metric (conversion rate, engagement, revenue). A/B testing requires careful statistical design: sample size calculation, randomisation, minimisation of cross-contamination (two groups interacting).

**Observability** (as distinct from monitoring) is the practice of making a system's internal state *queryable* without deploying new code:
- **Logs:** Structured, indexed, queryable records of events (ELK stack, Loki).
- **Metrics:** Numeric measurements aggregated over time (Prometheus, Grafana).
- **Traces:** End-to-end request flows across service boundaries (Jaeger, OpenTelemetry).

**Brendan Gregg's USE method** (Utilisation, Saturation, Errors) is a systematic approach to performance troubleshooting:
- For every resource (CPU, memory, disk, network), check its utilisation (busyness), saturation (queued work), and error count.

**Required Reading:**
- Charity Majors, Liz Fong-Jones & George Miranda, *Observability Engineering* (O'Reilly, 2022/2042)
- Brendan Gregg, "The USE Method" (brendangregg.com, 2012)
- Kohavi, Tang & Xu, *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing* (Cambridge, 2020)
- UoY Observability Lab: Set up Prometheus + Grafana + Jaeger for a microservices application (2040)

**Discussion Questions:**
1. Canary deployments depend on the assumption that the canary group is representative of the full user population. When does this assumption break — and how do you detect a biased canary?
2. A/B testing requires careful statistical design. What are the most common statistical mistakes in A/B testing — and how do the tools of 2040 help avoid them?
3. Observability is often described as three pillars (logs, metrics, traces). Is this taxonomy still useful in 2040 — or does the rise of streaming analytics, eBPF, and AI-driven anomaly detection demand a new paradigm?

---

## Lecture 12: Quality Culture — The Psychology and Sociology of Bug Prevention

The best testing in the world cannot prevent bugs. Bug prevention is a cultural problem — it requires an organisation that values quality, gives engineers the time to write good tests, and learns from failures without assigning blame.

**The psychology of testing** is the most underappreciated dimension of quality assurance. Humans are terrible at testing their own work (the **author bias problem**). We read what we intended to write, not what we actually wrote. We unconsciously avoid the edge cases that would embarrass us. The most effective testing strategies *separate the author from the tester*: pair testing, independent QA, code review by someone else, and adversarial testing (a "tiger team" tasked with breaking the system).

**Blameless postmortems** (SRE culture, Google) are the standard practice for incident analysis. A postmortem is not a witch hunt — it is a fact-finding mission that answers "what happened, why did it happen, and how do we prevent it from happening again?" The five whys technique (Toyota Production System) digs past the proximate cause to the systemic root cause. The output of a postmortem is a set of **action items** — specific, measurable changes to processes or systems — that prevent the same class of incident from recurring.

**Technical debt** is the gap between the ideal state of the code and its current state. "If it's not tested, it's broken" is the most honest measure of technical debt. Untested code is debt that will come due — as a production incident, a security vulnerability, or a missed deadline. The **interest** on technical debt compounds: untested code is hard to refactor, so it accumulates more untested code, and eventually the codebase becomes impossible to change safely.

**The "right to test"** is an organisational practice: every engineer has the right — and the responsibility — to add tests to any code they touch. Even if the code belongs to another team. Even if the change is "trivial." Testing is not an optional polish step; it is a core development practice. The most effective quality organisations are those where testing is not a separate phase but an integral part of every coding session.

**Required Reading:**
- John Allspaw, "Blameless PostMortems and a Just Culture" (kitchensoap.com, 2012)
- Martin Fowler, "Technical Debt" (martinfowler.com/bliki/TechnicalDebt.html)
- James Reason, *Human Error* (Cambridge, 1990) — the foundational text on human factors in safety-critical systems
- Sidney Dekker, *The Field Guide to Understanding Human Error* (CRC Press, 2006) — the modern view of human error as a symptom of systemic problems
- UoY Quality Culture Workshop: Practice blameless postmortems on simulated incidents (2040)

**Discussion Questions:**
1. Blameless postmortems are widely recommended but rarely practised. Why are organisations so reluctant to adopt blameless postmortems — and what is the most effective way to start?
2. Technical debt is a metaphor borrowed from finance. How useful is the metaphor — and what are its limitations? (When does "refactoring to reduce technical debt" become a distraction from shipping value?)
3. The "right to test" is an organisational policy. How do you implement it in practice — and how do you prevent it from becoming a source of friction between teams (when Team A adds tests to Team B's code)?

---

## Final Examination Preparation

The final examination for CS306 assesses your ability to design, implement, and evaluate a testing strategy for a realistic software system — from unit tests and property-based tests through integration, E2E, fuzz, and performance testing, and including the organisational practices that sustain quality.

**Sample Essay Questions (Choose 4 of 8):**

1. **The Testing Strategy.** You are the QA lead for a microservices-based e-commerce platform with 50 services, 200 developers, and a deployment cadence of 100 times per day. Design the testing strategy — what types of tests, in what proportion, with what quality gates, and with what CI pipeline. Justify your decisions with references to testing economics and the testing pyramid.

2. **TDD: Design Technique or Testing Technique?** Defend the claim that TDD is primarily a design technique, not a testing technique. What design properties does TDD encourage — and how do they improve code quality beyond what is captured by test coverage metrics?

3. **The Limits of Automated Testing.** Describe three classes of bugs that automated testing (unit, integration, E2E, fuzz, mutation) systematically struggles to find. For each class, propose a complementary approach (human review, formal methods, or organisational practice) that could catch them.

4. **Fuzz for Security.** Explain how coverage-guided fuzzing finds security vulnerabilities. Walk through the process of setting up LibFuzzer for a C library — seed corpus, instrumentation, crash triage. What are the limitations of fuzzing for security (buffer overflows that do not crash — can they still be exploitable?)?

5. **Mutation Testing in Practice.** Design a mutation testing workflow for a CI pipeline. Address: how to handle the computational cost, how to deal with equivalent mutants, how to present results to developers, and how to set quality gates based on mutation scores.

6. **Testing in Production.** You are tasked with introducing canary deployments and observability to a team that has never tested in production. Design the rollout plan — what metrics to monitor, what statistical techniques to use, what failure criteria to define, and how to convince the team that testing in production is safe when done correctly.

7. **Quality Culture.** Your organisation ships buggy software with exhausting "crunch" periods before every release. Design a cultural intervention — not a tool or a process, but a change in organisational norms — that would sustainably improve quality without burning out the engineers.

8. **The Future of Testing (2040).** Speculate on how AI will change software testing in the next decade. Will AI write tests automatically? Will AI generate test oracles from natural-language specifications? What risks does AI-generated testing introduce — and how do we mitigate them while capturing the benefits?

**Practical Project Option:** Choose an open-source project with at least 1,000 lines of code and design a testing improvement plan. Your plan must include: (1) analysis of the current test suite (coverage, mutation score, gaps), (2) a set of new tests covering the identified gaps (unit, property-based, integration, or fuzz), (3) a CI pipeline configuration implementing quality gates, and (4) a reflection on what was systematic about the bugs you found and what could prevent them.
