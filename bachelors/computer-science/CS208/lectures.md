# CS208: Formal Methods & Verification
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4
**Prerequisites:** CS102 — Discrete Mathematics for CS; CS103 — Programming Fundamentals; CS105 — Data Structures & Algorithms I
**Description:** This course is a journey into the art of mathematical certainty in software — the discipline of proving, beyond any doubt, that a program does what it claims. Beginning with propositional and first-order logic as the scaffolding of all verification, the course proceeds through Hoare logic (proving programs correct line by line), model checking (exhaustively exploring every reachable state), type theory (encoding specifications as types that the compiler enforces), SAT/SMT solving (automated reasoning at industrial scale), abstract interpretation (sound over-approximation of program behaviour), and the proof assistants Coq and Lean 4 — tools that allow the programmer to write proofs as programs and programs as proofs, in the spirit of the Curry-Howard correspondence. The course culminates in industrial case studies: the CompCert verified C compiler, the seL4 verified microkernel, Amazon's TLA⁺-verified AWS protocols, and the DeepSpec project's vision of a fully verified software stack. By the end of CS208, students will understand that formal methods are not an academic curiosity but the scaffolding on which the 2040 software infrastructure — autonomous agents, quantum compilers, and AGI safety protocols — relies for its integrity. The runes teach: **a thing half-carved is a thing half-broken** — and a specification half-proved is a specification half-false.

---

## Lectures

ᚠ **Lecture 1: The Why of Formal Verification — Bugs, Proofs, and the Limits of Testing**

**Course:** CS208 — Formal Methods & Verification
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Software testing is a statistical argument. A test suite exercises a finite number of paths through a program of potentially infinite behaviours; passing all tests demonstrates that the program works correctly on the tested inputs, but says nothing about the untested ones. Edsger Dijkstra put it bluntly in 1972: "Program testing can be used to show the presence of bugs, but never to show their absence." Formal verification is the alternative: a mathematical proof that a program satisfies its specification for **all** possible inputs, for **all** possible interleavings of concurrent threads, for **all** possible environmental conditions. It replaces statistical confidence with deductive certainty.

The cost of absent verification is measured not in dollars but in lives and epochs. The THErac-25 radiation therapy machine (1985–1987) killed three patients and severely injured three others because a race condition — a concurrency bug invisible to testing — allowed the electron beam to fire at full power without the tungsten target in place. The Ariane 5 rocket exploded 37 seconds into its maiden flight (1996) at a cost of $370 million, because a 64-bit floating-point value was cast to a 16-bit signed integer without overflow checking — a type error that testing missed because the offending code was reused from Ariane 4, where it had never been exercised. The Knight Capital trading glitch (2012) lost $440 million in 45 minutes when a deployment script failed to copy updated software to one of eight servers, causing that server to run obsolete code that executed millions of erroneous trades. Each of these disasters was a bug that testing missed; each could have been prevented by formal verification of the relevant property — mutual exclusion for the THErac, type safety and overflow checking for Ariane, deployment integrity for Knight.

The 2040 landscape raises the stakes further. Autonomous vehicles make braking decisions in milliseconds; a formal guarantee that the perception pipeline correctly identifies pedestrians in all lighting conditions is not a luxury — it is a precondition for deployment. AGI-adjacent systems with tool-use capabilities can execute arbitrary code; formal verification of the sandbox and capability boundaries is the only defence against unintended escalation. Quantum compilers generate circuits that run on error-prone hardware; formal proof of circuit equivalence is necessary to trust that the compiled circuit implements the specified algorithm. Post-quantum cryptographic protocols protect data against adversaries with access to cryptographically relevant quantum computers; a proof of security in the quantum random oracle model is required before the protocol can be deployed in production. Formal methods have moved from the margins to the centre — from a niche interest of theoreticians to an engineering necessity.

This course teaches the tools and the mindset. We begin not with the tools (Coq, Lean, Z3, TLA⁺) but with the question: **what does it mean to prove something about a program?** A proof is a chain of logical deductions that starts from axioms and arrives at a conclusion; a program proof is a proof that a particular property (safety, liveness, functional correctness, security) holds for a particular program under a particular execution model. The property is expressed in a **specification language** (first-order logic, temporal logic, type theory); the proof is constructed using a **proof system** (natural deduction, sequent calculus, tactic language); and the construction is checked by a **proof checker** (a small, trusted kernel that verifies each deduction step). The entire edifice rests on **logic** — the unshakeable foundation on which all formal reasoning is built.

**Key Topics:**
- The limits of testing: why passing N tests guarantees nothing about input N+1
- Historical case studies of verification failures (THErac-25, Ariane 5, Knight Capital, Heartbleed, Spectre/Meltdown)
- The 2040 verification imperative: autonomous systems, AGI safety, quantum compilation, PQC
- The formal verification workflow: specification → proof → proof checking
- The role of logic as the foundation of all formal reasoning
- Soundness and completeness: a proof system is sound if every provable statement is true; complete if every true statement is provable
- Gödel's first incompleteness theorem and its implication: any sufficiently powerful logic is either incomplete or inconsistent — but for practical program verification, we work in decidable or semi-decidable fragments

**Required Reading:**
- John Rushby, "Formal Methods and the Certification of Critical Systems" (SRI CSL Technical Report, 1993/2040 revision)
- Nancy Leveson, *Safeware: System Safety and Computers* (1995/2040), chs. 1–4 (Therac-25, the limits of testing)
- Jean-Raymond Abrial, "Faultless Systems: Yes We Can!" *IEEE Computer* 42:9 (2009): 30–36
- Xavier Leroy, "Formal Verification of a Realistic Compiler" *Communications of the ACM* 52:7 (2009): 107–115 — the CompCert story
- Gerwin Klein et al., "seL4: Formal Verification of an OS Kernel" *Communications of the ACM* 53:6 (2010): 107–115
- Course Reader: "What Gödel's Theorems Do and Do Not Mean for Program Verification" (UoY, 2040)

**Discussion Questions:**
1. Dijkstra wrote that testing can show the presence of bugs but never their absence. If this is true, why does the software industry still rely on testing as its primary quality assurance mechanism — and what would need to change for formal verification to become the default?
2. The THErac-25's race condition was reproduced during the investigation but was never observed during testing. Could model checking have found it? What property would you specify?
3. Gödel's incompleteness theorem shows that no consistent formal system can prove all true statements about arithmetic. Does this mean that formal verification of programs is fundamentally limited, or are the limitations irrelevant in practice?

---

ᚢ **Lecture 2: Propositional and First-Order Logic — The Language of Specification**

---

### Overview

Formal methods speak in logic. Before we can verify a program, we must write its specification, and before we can write a specification, we must understand the language in which specifications are written. That language is **mathematical logic** — the calculus of truth, the grammar of proof, the alphabet of certainty that has remained unchanged since Aristotle and was formalised by Frege, Russell, Peano, and Hilbert in the decades surrounding 1900.

**Propositional logic** is the simplest layer. It deals with **propositions** — statements that are either true or false — and the **logical connectives** that combine them: ¬ (not), ∧ (and), ∨ (or), → (implies), ↔ (equivalent). The meaning of each connective is given by its **truth table**: a function from the truth values of its arguments to the truth value of the result. The formula (A ∧ B) → C is true in exactly those worlds where either A is false, or B is false, or C is true. A formula that is true in **all** possible assignments of truth values to its variables is a **tautology** (e.g., A ∨ ¬A, the law of excluded middle); a formula that is true in **some** assignment is **satisfiable**; a formula that is true in **no** assignment is **unsatisfiable** (a contradiction, e.g., A ∧ ¬A). The **SAT problem** — given a propositional formula, is it satisfiable? — is the canonical NP-complete problem, and SAT solvers are the workhorses of modern formal verification, routinely solving formulas with millions of variables and tens of millions of clauses.

**First-order logic (FOL)** extends propositional logic with **quantifiers** (∀, ∃) that range over **individuals** in a **domain** (e.g., natural numbers, strings, states of a program), and with **predicates** and **functions** that express relations and transformations. The formula ∀x. ∃y. y > x says "for every number x, there exists a larger number y" — a true statement about the natural numbers. The formula ∀x. ∀y. (x ≤ y) ∨ (y ≤ x) says "any two numbers are comparable" — true for the reals, false for complex numbers (which are not totally ordered). First-order logic is expressive enough to encode most program specifications — preconditions, postconditions, invariants, safety properties, liveness properties — but it is **undecidable**: there is no algorithm that determines whether an arbitrary first-order formula is valid. This undecidability is the theoretical limit that forces us into decidable fragments (propositional logic, linear arithmetic, bit-vectors, arrays) and semi-decidable proof systems.

The **syntax** of first-order logic is defined by an inductive grammar: terms are built from variables and function symbols; atomic formulas are built from predicate symbols applied to terms; compound formulas are built from atomic formulas using connectives and quantifiers. The **semantics** is defined by an **interpretation** (a domain of discourse, an assignment of concrete functions and predicates to the function and predicate symbols), and the **satisfaction relation** ⊨ (read "models" or "satisfies"): M ⊨ φ means that formula φ is true in interpretation M. A formula is **valid** (⊨ φ) if it is true in all interpretations; it is **satisfiable** if it is true in at least one interpretation. The central theorem of first-order logic is **Gödel's completeness theorem**: a formula is valid if and only if it is provable in a suitable deductive system (e.g., natural deduction with the standard introduction and elimination rules). Completeness says that truth and provability coincide — for every valid formula, there exists a finite proof.

The standard proof system for first-order logic is **natural deduction** (Gentzen, 1935; Prawitz, 1965), which mirrors the way humans reason. Each connective has an **introduction rule** (how to prove a formula with that connective) and an **elimination rule** (how to use a formula with that connective as a premise). To prove A → B, assume A and derive B (→I). To use A → B and A, conclude B (→E, modus ponens). To prove ∀x. P(x), prove P(c) for an arbitrary fresh constant c (∀I). To use ∀x. P(x), instantiate it to any term t (∀E). The rules are purely syntactic — they manipulate formulas without reference to meaning — but they are **sound** (every provable formula is valid) and **complete** (every valid formula is provable). The proof is a **tree** whose leaves are axioms or assumptions and whose root is the conclusion.

**Automated theorem proving** for first-order logic is the domain of **resolution** (Robinson, 1965) and **superposition** (Bachmair and Ganzinger, 1994). The key idea is to convert the formula to **clausal normal form** (a conjunction of clauses, where each clause is a disjunction of literals) and apply the **resolution rule**: from clauses C₁ ∨ L and C₂ ∨ ¬L, infer C₁ ∨ C₂. Resolution is refutation-complete: if the original formula is unsatisfiable, resolution will eventually derive the empty clause (a contradiction). Modern first-order theorem provers (E, Vampire, Zipperposition) combine superposition with sophisticated heuristics for clause selection and term ordering, and they can prove thousands of theorems that would challenge trained mathematicians. The **TPTP** (Thousands of Problems for Theorem Provers) library provides over 20,000 benchmark problems, and the annual **CASC** (CADE ATP System Competition) tracks the state of the art.

**Key Topics:**
- Propositional logic: syntax, truth tables, tautologies, satisfiability, SAT, NP-completeness
- The Davis-Putnam-Logemann-Loveland (DPLL) algorithm and Conflict-Driven Clause Learning (CDCL)
- First-order logic syntax: terms, formulas, free vs. bound variables, substitution
- First-order semantics: interpretations, satisfaction, validity, satisfiability, logical consequence
- Natural deduction: introduction and elimination rules for each connective and quantifier
- Gödel's completeness theorem and the relationship between semantics and syntax
- Resolution and superposition: automated proof search for first-order logic
- The undecidability of first-order logic (Church, 1936; Turing, 1936) and its implications

**Required Reading:**
- David Gries and Fred B. Schneider, *A Logical Approach to Discrete Math* (1993/2040), chs. 1–6 (Propositional and Predicate Calculus)
- Mordechai Ben-Ari, *Mathematical Logic for Computer Science* (3rd ed., 2012/2040), chs. 1–5, 7
- John Harrison, *Handbook of Practical Logic and Automated Reasoning* (2009/2040), chs. 1–3
- Martin Davis, "The Early History of Automated Deduction" (2001), in *Handbook of Automated Reasoning*, vol. 1
- Yggdrasil Logic Lab: Natural Deduction Proofs in Lean 4, SAT Encoding in MiniSat/Z3 (2040)

**Discussion Questions:**
1. Propositional logic is decidable (SAT is NP-complete) but first-order logic is undecidable. Where exactly does the jump in complexity occur — and what fragment of first-order logic is decidable? (Hint: consider Presburger arithmetic and monadic first-order logic.)
2. Natural deduction is a "natural" proof system in that it mirrors human reasoning. But it is not the most efficient for automated proof search. Why is resolution preferred for automation, and what is lost (in human readability) when we use resolution?
3. The DPLL algorithm with CDCL can solve SAT instances with millions of variables. What properties of real-world SAT instances (from hardware and software verification) make them tractable despite the theoretical NP-completeness?

---

ᚦ **Lecture 3: Hoare Logic — Proving Programs Correct**

---

### Overview

**Hoare logic** (C.A.R. Hoare, 1969) is the calculus of imperative programs — a set of inference rules that allow us to prove that a program fragment satisfies a specification expressed as a **Hoare triple**: {P} C {Q}, read "if P holds before executing command C, then Q holds after C terminates." P is the **precondition**, Q the **postcondition**, and C the command. Hoare logic treats programs as mathematical objects subject to the same kind of rigorous reasoning as numbers, sets, and functions — and it provides the intellectual foundation for all subsequent work on program verification.

The heart of Hoare logic is the **assignment axiom**: {Q[E/x]} x := E {Q}. This says that to guarantee Q after assigning E to x, we need Q[E/x] — the formula obtained by substituting E for every free occurrence of x in Q — to hold before the assignment. For example, {y + 1 > 0} x := y + 1 {x > 0}. The assignment axiom works "backwards": we compute the precondition from the postcondition and the assignment. This backward reasoning is characteristic of Hoare logic and of the **weakest precondition (WP)** calculus (Dijkstra, 1976), which we explore in Lecture 4.

The **rule of composition** connects sequential commands: if {P} C₁ {R} and {R} C₂ {Q}, then {P} C₁; C₂ {Q}. The intermediate assertion R is the "glue" that links the two commands — it describes the state between them. The **rule of consequence** allows us to strengthen the precondition or weaken the postcondition: if P ⇒ P', {P'} C {Q'}, and Q' ⇒ Q, then {P} C {Q}. This rule lets us adapt a verified program to a slightly different specification without re-proving it — if we can prove that the new precondition implies the old, and the old postcondition implies the new, the verification carries over.

The **conditional rule** handles if-then-else: if {P ∧ B} C₁ {Q} and {P ∧ ¬B} C₂ {Q}, then {P} if B then C₁ else C₂ {Q}. Both branches must establish the same postcondition Q, but they work under different assumptions: the "then" branch assumes B is true, the "else" branch assumes B is false. The **while rule** is the most subtle: if {P ∧ B} C {P}, then {P} while B do C {P ∧ ¬B}. The assertion P is the **loop invariant** — a property that holds before the loop begins and is preserved by each iteration. When the loop terminates (B becomes false), we know both P and ¬B hold. The loop invariant is the creative heart of Hoare-logic verification: finding the right invariant is the intellectual challenge; once found, the proof is mechanical.

A classic example: verifying a program that computes the factorial of n. Let C be:
```
x := 1; i := 1;
while i ≤ n do
  x := x * i;
  i := i + 1
```
The loop invariant is P: x = (i-1)! ∧ i ≤ n+1. Before the loop: x = 1, i = 1, so P holds (x = 0! = 1). During the loop: if P holds and i ≤ n, then after x := x*i and i := i+1, we have x = (i-1)! and i ≤ n+1 — P is preserved. After the loop: P holds and i > n, so x = (i-1)! and i = n+1, hence x = n!. The precondition {n ≥ 0} and postcondition {x = n!}. The entire proof follows mechanically from the invariant.

Hoare logic extends naturally to **arrays** and **pointers** through the **substitution rule for arrays**: {Q[a[i ↦ E] / a]} a[i] := E {Q}, where a[i ↦ E] is the array that agrees with a everywhere except at index i, where it has the value E. For pointers, **separation logic** (Reynolds, 2002; O'Hearn, 2001) extends Hoare logic with the **separating conjunction** P ∗ Q, which asserts that the heap can be split into two disjoint parts — one satisfying P and the other Q. Separation logic is the basis of the seL4 verification and of modern tools like VeriFast and Viper. We return to separation logic in Lecture 8.

**Key Topics:**
- The Hoare triple {P} C {Q} and its interpretation: partial correctness (if P holds and C terminates, then Q holds)
- The assignment axiom and backward substitution
- The rule of composition (sequential), consequence (strengthening/weakening), conditional (if-then-else), and while (loop invariant)
- Total correctness: partial correctness plus termination — expressed by a **variant** (a measure that strictly decreases on each iteration and is bounded below)
- Finding loop invariants: the hardest part of Hoare-logic verification
- Extending Hoare logic to arrays, records, and pointers
- Mechanising Hoare logic: early systems (Gypsy, Stanford Pascal Verifier) to modern systems (Frama-C, Dafny, VeriFast)
- The connection to separation logic and modern heap verification

**Required Reading:**
- C.A.R. Hoare, "An Axiomatic Basis for Computer Programming" *Communications of the ACM* 12:10 (1969): 576–580, 583
- Krzysztof R. Apt, Frank S. de Boer, and Ernst-Rüdiger Olderog, *Verification of Sequential and Concurrent Programs* (3rd ed., 2009/2040), chs. 1–3
- David Gries, *The Science of Programming* (1981/2040), chs. 7–12 (Loops and Invariants)
- Edsger W. Dijkstra, *A Discipline of Programming* (1976/2040), chs. 1–5 (Weakest Preconditions, Guarded Commands)
- John C. Reynolds, "Separation Logic: A Logic for Shared Mutable Data Structures" *LICS 2002*: 55–74
- Yggdrasil Verification Lab: Proving Simple Programs in Dafny, Finding Loop Invariants (2040)

**Discussion Questions:**
1. Hoare logic proves partial correctness: if the program terminates, the postcondition holds. Why is termination a separate concern, and how does the **variant** method for proving termination relate to the loop invariant?
2. The loop invariant is the creative step in Hoare-logic verification. For the program that computes the greatest common divisor (Euclid's algorithm), what is the loop invariant — and how would you discover it systematically?
3. Separation logic's separating conjunction P ∗ Q ensures that P and Q refer to disjoint parts of the heap. Why is this disjointness crucial for modular verification, and how does it prevent the "frame problem" that plagues classical Hoare logic with pointers?

---

ᚨ **Lecture 4: Weakest Precondition Calculus and Automated Verification Condition Generation**

---

### Overview

Dijkstra's **weakest precondition (WP) calculus** (1976) reframes program verification from "given P and C, find Q such that {P} C {Q}" to "given C and Q, find the weakest P such that {P} C {Q}." The **weakest liberal precondition** wp(C, Q) is the weakest predicate P such that {P} C {Q} holds (for partial correctness). "Weakest" means "most general" — wp(C, Q) is the precondition that imposes the fewest constraints while still guaranteeing Q after C. To verify {P} C {Q}, we compute wp(C, Q) and check that P ⇒ wp(C, Q). This reduces program verification to **logical implication** — a formula that can be checked by an automated theorem prover.

The WP calculus defines wp recursively over the structure of C:

- **Assignment**: wp(x := E, Q) = Q[E/x]
- **Sequence**: wp(C₁; C₂, Q) = wp(C₁, wp(C₂, Q))
- **Conditional**: wp(if B then C₁ else C₂, Q) = (B ⇒ wp(C₁, Q)) ∧ (¬B ⇒ wp(C₂, Q))
- **While loop**: This is the hard case. The WP of a loop is defined as the weakest predicate P such that (P ∧ B) ⇒ wp(C, P) (P is invariant) and (P ∧ ¬B) ⇒ Q (at loop exit). Finding P requires an invariant — the WP calculus cannot compute it automatically. In practice, the programmer supplies the loop invariant, and the verifier checks that it is inductive.

The WP calculus is the engine of **Verification Condition Generation (VCG)** — the process of translating a program with its specifications (preconditions, postconditions, loop invariants) into a set of first-order logic formulas (the **verification conditions**, or VCs) whose validity implies the correctness of the program. A VCG reads the program, computes WP at each statement, and emits the implications that must be proved. The VCs are then passed to an automated theorem prover (Z3, CVC5, Alt-Ergo, Vampire) for discharge. This is the architecture of Dafny, Frama-C, Why3, and Viper — the programmer writes the code with annotations (invariants, pre/post), the VCG generates the VCs, and the SMT solver proves them. The programmer never writes a proof tree; they write annotations that are rich enough to guide the solver.

A concrete VCG example: verifying the factorial program with the invariant x = (i-1)! ∧ i ≤ n+1. The VCG generates three VCs:

1. **Initialisation VC**: n ≥ 0 ⇒ wp(x:=1; i:=1, Inv) — does the precondition establish the invariant? Computed: n ≥ 0 ⇒ (1 = 0! ∧ 1 ≤ n+1) — true.

2. **Preservation VC**: (Inv ∧ i ≤ n) ⇒ wp(x:=x*i; i:=i+1, Inv) — does the loop body preserve the invariant? Computed: (x = (i-1)! ∧ i ≤ n+1 ∧ i ≤ n) ⇒ (x*i = i! ∧ i+1 ≤ n+1) — true by simplification.

3. **Postcondition VC**: (Inv ∧ ¬(i ≤ n)) ⇒ (x = n!) — does the invariant at loop exit imply the postcondition? Computed: (x = (i-1)! ∧ i ≤ n+1 ∧ i > n) ⇒ (x = n!) — i = n+1, so x = n! — true.

All three VCs are valid, so the program is correct. The entire reasoning is automatic once the invariant is supplied.

The **SMT (Satisfiability Modulo Theories)** solver is the engine that discharges VCs. SMT extends SAT solving with **decision procedures for theories**: linear arithmetic (Presburger), bit-vectors, arrays, uninterpreted functions, algebraic datatypes, and combinations thereof (Nelson-Oppen combination). Z3 (Microsoft Research, 2008–present) is the dominant SMT solver, with CVC5 (Stanford/Iowa) and Yices (SRI) as strong competitors. An SMT solver takes a formula involving both Boolean structure and theory-specific atoms (e.g., x + y < 5, a[i] = 3, f(x) = g(y)) and determines satisfiability. For verification, we check unsatisfiability of the negation of the VC — if the negation is unsatisfiable, the VC is valid. Modern SMT solvers can discharge VCs with thousands of quantified variables and millions of theory atoms in seconds, making them practical for industrial verification.

**Key Topics:**
- The weakest precondition (WP) calculus: definition, properties, and recursive computation
- The relationship between Hoare logic and WP: {P} C {Q} iff P ⇒ wp(C, Q)
- Verification Condition Generation (VCG): from annotated program to logical formulas
- The architecture of a modern program verifier: parser, type checker, VCG, SMT solver
- SMT solving: theories (linear arithmetic, arrays, bit-vectors, algebraic datatypes), DPLL(T) algorithm, quantifier instantiation (E-matching, MBQI)
- Practical VCG tools: Dafny (Microsoft), Frama-C/WP (CEA), Why3 (Inria), Viper (ETH Zurich)
- The annotation burden: what the programmer must provide (invariants, pre/post) vs. what is automatic
- Limitations: loops require invariants; recursion requires induction hypotheses; complex data structures require framing conditions

**Required Reading:**
- Edsger W. Dijkstra, *A Discipline of Programming* (1976/2040), chs. 1–4 (WP Calculus, Guarded Commands)
- K. Rustan M. Leino, "Dafny: An Automatic Program Verifier for Functional Correctness" *LPAR-16* (2010): 348–370
- Jean-Christophe Filliâtre and Andrei Paskevich, "Why3 — Where Programs Meet Provers" *ESOP 2013*: 125–128
- Leonardo de Moura and Nikolaj Bjørner, "Z3: An Efficient SMT Solver" *TACAS 2008*: 337–340
- Clark Barrett et al., "CVC5: A Versatile and Industrial-Strength SMT Solver" *TACAS 2022*: 415–432
- Yggdrasil Verification Lab: Dafny Exercises (factorial, binary search, sorting, graph algorithms) (2040)

**Discussion Questions:**
1. The WP calculus computes preconditions automatically for all constructs except loops (which require invariants) and recursion (which requires induction hypotheses). Why are these the hard cases — and could machine learning (e.g., LLM-generated invariants) bridge the gap?
2. Dafny's architecture places the programmer in the role of annotation author, not proof author. What is lost — and what is gained — by replacing proof trees with SMT-solved VCs?
3. SMT solvers use heuristics for quantifier instantiation (E-matching, MBQI). These heuristics are incomplete: they may fail to find a proof even when one exists. Is this incompleteness a fatal flaw for verification, or a pragmatic compromise?

---

ᚱ **Lecture 5: Temporal Logic and Model Checking — Exploring the State Space**

---

### Overview

Hoare logic proves properties of **sequential** programs. For **reactive** and **concurrent** systems — operating systems, network protocols, hardware circuits, distributed algorithms — the relevant properties are **temporal**: not "what is the result?" but "what eventually happens?" and "what never happens?" **Temporal logic** (Pnueli, 1977) extends propositional and first-order logic with modalities that express the ordering of events in time, and **model checking** (Clarke and Emerson, 1981; Queille and Sifakis, 1982) is the algorithmic verification technique that exhaustively explores the state space to determine whether a temporal logic property holds.

A **Kripke structure** is the mathematical model: a directed graph where each node (state) is labelled with the atomic propositions true in that state, and edges represent possible transitions. The structure is a **transition system** — every possible execution of the concurrent system is a path through the graph. The state space may be finite (a circuit with n latches has 2ⁿ states) or infinite (software with unbounded recursion and dynamic allocation). Model checking works on **finite** state spaces, typically by constructing a symbolic representation of the Kripke structure from a program description and then verifying properties against it.

**Linear Temporal Logic (LTL)** (Pnueli, 1977) expresses properties of individual executions — paths through the Kripke structure. The temporal modalities are:

- **□ φ** ("always φ" or "globally φ"): φ holds at every state on the path. □ ¬(crash) says "the system never crashes."
- **◇ φ** ("eventually φ" or "finally φ"): φ holds at some future state on the path. ◇ (leader_elected) says "a leader is eventually elected."
- **○ φ** ("next φ"): φ holds at the next state. ○ (x = 5) says "x will be 5 at the next step."
- **φ 𝒰 ψ** ("φ until ψ"): φ holds continuously until some state where ψ holds. (¬granted) 𝒰 (request ∧ granted) says "no grant occurs until a request is made and then granted."

LTL formulas are evaluated on infinite paths (for reactive systems, there is no "termination" — the system runs forever). An LTL property holds of a Kripke structure if it holds on **every** path starting from every initial state. The classic LTL model checking algorithm (Vardi and Wolper, 1986) translates the LTL formula into a **Büchi automaton** — a finite automaton on infinite words that accepts exactly those paths that satisfy the formula — and then checks whether the product of the Kripke structure and the Büchi automaton has an accepting path. If no accepting path exists, the property holds; if one exists, it is a **counterexample** — a concrete execution trace that violates the property.

**Computation Tree Logic (CTL)** (Clarke and Emerson, 1981) takes a different perspective: instead of reasoning about paths, CTL reasons about the **branching structure** of the computation tree. CTL path quantifiers are:

- **A φ** ("for all paths"): φ holds on all paths from the current state
- **E φ** ("there exists a path"): φ holds on some path from the current state

Combined with the temporal operators (X, F, G, U), we get eight basic CTL modalities: AG φ ("invariant" — φ holds on all reachable states), EF φ ("reachability" — φ is reachable from some path), AF φ ("inevitability" — on all paths, φ eventually holds), EG φ ("possibility" — there is a path where φ always holds), and their duals. CTL model checking is simpler than LTL model checking: it can be done by a bottom-up traversal of the formula over the state space, labelling each state with the subformulas that hold there. The running time is O(|M| · |φ|) — linear in the size of the Kripke structure and the length of the formula.

The fundamental challenge of model checking is the **state explosion problem**: the number of states grows exponentially with the number of components. A system with n Boolean variables has 2ⁿ states; a system with n concurrent processes, each with k local states, has kⁿ states. **Symbolic model checking** (McMillan, 1993) addresses this by representing sets of states and transition relations as **Binary Decision Diagrams (BDDs)** — canonical, compressed representations of Boolean functions. A BDD for a set with 10²⁰ states may have only a few thousand nodes if the set has a regular structure. Symbolic model checking with BDDs can handle state spaces of 10²⁰ to 10⁵⁰ states — far beyond explicit enumeration. **Bounded model checking** (Biere et al., 1999) takes a different approach: it unrolls the transition relation k times into a propositional formula and checks for counterexamples of length k using a SAT solver. BMC is incomplete (it finds bugs up to bound k but cannot prove correctness for unbounded traces) but is highly effective at finding shallow bugs — most real-world bugs manifest in a small number of steps.

**Key Topics:**
- Kripke structures: states, transitions, atomic propositions, paths, traces
- Linear Temporal Logic (LTL): syntax, semantics on paths, Büchi automata
- Computation Tree Logic (CTL): path quantifiers, branching time, labelling algorithm
- LTL vs. CTL: expressiveness comparison (LTL and CTL are incomparable; CTL* subsumes both)
- Explicit-state model checking: SPIN (Holzmann), on-the-fly verification, partial order reduction
- Symbolic model checking: BDDs, fixed-point characterisation of CTL operators, NuSMV
- Bounded model checking: SAT-based, incremental unrolling, k-induction
- The state explosion problem and mitigation strategies: symmetry reduction, abstraction, compositional reasoning

**Required Reading:**
- Edmund M. Clarke, Orna Grumberg, and Doron Peled, *Model Checking* (1999/2040), chs. 1–6
- Amir Pnueli, "The Temporal Logic of Programs" *FOCS 1977*: 46–57 — the paper that introduced temporal logic to CS
- Gerard J. Holzmann, *The SPIN Model Checker: Primer and Reference Manual* (2004/2040), chs. 1–4
- Kenneth L. McMillan, *Symbolic Model Checking* (1993/2040), chs. 1–3 (BDDs, Fixed Points)
- Armin Biere et al., "Bounded Model Checking" *Advances in Computers* 58 (2003): 117–148
- Yggdrasil Model Checking Lab: LTL and CTL specifications in SPIN, counterexample analysis (2040)

**Discussion Questions:**
1. LTL and CTL are incomparable in expressiveness: there are LTL properties that cannot be expressed in CTL (e.g., ◇□p, "eventually always p") and CTL properties that cannot be expressed in LTL (e.g., AF AG p, "eventually p holds forever on all paths"). Give examples of each and explain the intuitive difference between the linear-time and branching-time perspectives.
2. The state explosion problem is the central obstacle to model checking. Why does symbolic model checking with BDDs mitigate explosion for hardware but less so for software — and what about software structure makes it harder to compress?
3. Bounded model checking can find bugs but cannot prove correctness (for unbounded traces). How does **k-induction** extend BMC to proofs — and what is the relationship to mathematical induction?

---

ᚲ **Lecture 6: The Curry-Howard Correspondence and Type Theory as Logic**

---

### Overview

The **Curry-Howard correspondence** (Curry, 1934; Howard, 1969) is the observation that there is a deep structural isomorphism between **logic** and **computation**: propositions correspond to types, proofs correspond to programs, and proof simplification (cut elimination) corresponds to program evaluation (β-reduction). The correspondence is not a metaphor — it is a precise mathematical isomorphism that has been formalised in multiple settings (natural deduction ↔ simply typed λ-calculus, intuitionistic logic ↔ λP2, second-order logic ↔ System F, higher-order logic ↔ Calculus of Constructions). The correspondence means that **programming in a dependently typed language is proving theorems**, and **type checking is proof checking**. A program that type-checks is a proof of the proposition encoded by its type.

The simplest instance: in the **simply typed λ-calculus** (λ→), the type A → B corresponds to the logical implication A ⇒ B. A term of type A → B is a function that, given a proof of A, constructs a proof of B — exactly the introduction rule for implication (→I). The product type A × B corresponds to conjunction A ∧ B — a proof of A × B is a pair of proofs, one for A and one for B (∧I). The sum type A + B corresponds to disjunction A ∨ B — a proof of A + B is either a proof of A (left injection) or a proof of B (right injection) (∨I). The empty type ⊥ corresponds to falsity — there are no closed terms of type ⊥, just as there is no proof of falsity (ex falso quodlibet: from ⊥, anything follows, which corresponds to the elimination rule for ⊥: any type is inhabited in an inconsistent context).

The correspondence extends to **dependent types** — types that depend on values. The dependent function type Π(x : A). B(x) corresponds to universal quantification ∀x : A. B(x) — a proof of ∀x. B(x) is a function that, given any x of type A, produces a proof of B(x). The dependent pair type Σ(x : A). B(x) corresponds to existential quantification ∃x : A. B(x) — a proof of ∃x. B(x) is a pair (x, p) where x is a witness and p is a proof of B(x). The **Calculus of Constructions** (Coquand and Huet, 1988) extends this to a full higher-order logic, and **Coq** (the proof assistant) implements the Calculus of Inductive Constructions (CIC) — the Calculus of Constructions enriched with inductive types, pattern matching, and guarded recursion.

In Coq (and Lean 4, Agda, Idris 2), the programmer writes both programs and proofs in the same language. A theorem is a type, and a proof is a term of that type. The proof assistant provides a **tactic language** — a set of commands that construct proof terms interactively — because writing raw proof terms is tedious. Tactics like `intros` (introduce hypotheses), `apply` (use an implication), `induction` (perform induction), `rewrite` (substitute equals), and `auto` (automated proof search) allow the programmer to build proofs incrementally, with the proof assistant displaying the remaining subgoals at each step. The final proof term is checked by a **small kernel** (the type checker, typically a few thousand lines of code) — the kernel is the trusted computing base (TCB); if the kernel is correct, every proof it accepts is valid. This **de Bruijn criterion** (named after N.G. de Bruijn, the creator of Automath) is the gold standard for proof assistant design: keep the trusted code small enough that it can be verified by inspection.

The Curry-Howard correspondence has profound implications. It means that **type systems are logics** — the type system of a programming language is a particular logic, and type checking is proof checking in that logic. Java's type system corresponds to a weak logic (no dependent types, no higher-order quantification), while Coq's corresponds to a very strong logic (higher-order, impredicative, with inductive types). The **expressiveness** of a type system — what properties it can encode as types — is directly tied to the logical strength of the corresponding logic. This is why dependently typed languages can express functional correctness as types (e.g., a sorting function with type `∀(xs : List ℕ). Σ(ys : List ℕ). sorted(ys) ∧ permutation(xs, ys)`) while Java can only express "this function returns a List."

**Key Topics:**
- The simply typed λ-calculus (λ→) and its correspondence with intuitionistic propositional logic
- The product type (×) as conjunction, sum type (+) as disjunction, function type (→) as implication, empty type (⊥) as falsity
- Dependent types: Π-types as universal quantification, Σ-types as existential quantification
- The Calculus of Constructions and the Calculus of Inductive Constructions
- Curry-Howard in practice: writing proofs as programs in Coq / Lean 4 / Agda
- The de Bruijn criterion: small trusted kernel, proof terms as certificates
- The limits of Curry-Howard: classical logic (excluded middle) requires control operators (call/cc); linear logic requires linear types; modal logic requires modal types
- Proof irrelevance vs. proof relevance: in some type theories, all proofs of a proposition are considered equal (irrelevance); in others, proofs carry computational content (relevance)

**Required Reading:**
- William A. Howard, "The Formulae-as-Types Notion of Construction" (1969/1980), in *To H.B. Curry: Essays on Combinatory Logic, Lambda Calculus and Formalism*
- Philip Wadler, "Propositions as Types" *Communications of the ACM* 58:12 (2015): 75–84 — an accessible modern overview
- Benjamin C. Pierce, *Types and Programming Languages* (2002/2040), chs. 9 (Simply Typed λ-Calculus), 23 (Universal Types), 30 (Higher-Order Polymorphism)
- Yves Bertot and Pierre Castéran, *Interactive Theorem Proving and Program Development: Coq'Art* (2004/2040), chs. 1–4
- The Coq Reference Manual, chs. 1–3 (Gallina specification language, the Calculus of Inductive Constructions)
- Yggdrasil Coq Lab: Proving Simple Theorems in Coq (∧, ∨, →, ∀, ∃, induction on ℕ, lists) (2040)

**Discussion Questions:**
1. The Curry-Howard correspondence is often described as "programs are proofs." But is every program a proof? What about a program that diverges (infinite loop) — does it correspond to a proof? (Hint: consider the consistency requirement — a logic in which ⊥ is inhabited is inconsistent.)
2. Coq's kernel is small (≈20k lines of OCaml) but not formally verified. What would it mean to verify the kernel — and would this eliminate the TCB entirely, or is there always something that must be trusted (hardware, the human reading the specification)?
3. Dependent types allow us to express functional correctness as a type. Why hasn't dependently typed programming replaced traditional programming — what are the practical costs (in programmer effort, compile time, runtime efficiency) of encoding specifications in types?

---

ᚷ **Lecture 7: Interactive Theorem Proving in Coq — Building Proofs by Hand**

---

### Overview

**Coq** (Inria, 1989–present) is the most mature interactive proof assistant. It implements the Calculus of Inductive Constructions (CIC) — a dependently typed λ-calculus with inductive types, coinductive types, and a hierarchy of predicative universes (Type₀ : Type₁ : Type₂ : ...). Coq is used for mathematics (the Four Colour Theorem, the Odd Order Theorem — Feit-Thompson) and for verified software (CompCert C compiler, VST — Verified Software Toolchain, CertiKOS hypervisor). This lecture is a hands-on introduction to proving theorems in Coq, from simple propositional logic to inductive proofs on natural numbers and lists.

The Coq workflow is interactive: you state a theorem (`Theorem`, `Lemma`, `Goal`), and Coq enters **proof mode**, displaying the current goal — the statement to be proved — and the context (the hypotheses available). You apply **tactics** to transform the goal into subgoals, recursively proving each subgoal until no subgoals remain. The sequence of tactics constitutes a **proof script**; when Coq accepts the script, it constructs a proof term (a λ-term in CIC) and checks it with the kernel. The proof term can be inspected and is the ultimate certificate of correctness.

The essential tactics:

- `intros` (or `intro`): move hypotheses and universally quantified variables from the goal into the context. For goal `∀ x, P(x) → Q(x)`, `intros x H` introduces `x` and hypothesis `H : P(x)`, leaving goal `Q(x)`.
- `apply H`: if the goal matches the conclusion of hypothesis `H`, apply `H` and replace the goal with `H`'s premises. For `H : A → B` and goal `B`, `apply H` changes the goal to `A`.
- `exact H` (or `assumption`): if the goal matches a hypothesis exactly, prove it immediately.
- `split`: for a goal `A ∧ B`, split it into two subgoals: `A` and `B`.
- `left` / `right`: for a goal `A ∨ B`, choose which disjunct to prove.
- `exists e`: for a goal `∃ x, P(x)`, provide witness `e` and leave goal `P(e)`.
- `induction n`: perform induction on `n : ℕ`. For `P(n)`, generate two subgoals: base case `P(0)` and inductive step `∀ n, P(n) → P(S n)`.
- `simpl`: simplify the goal by computing (β-reduction, unfolding definitions).
- `rewrite H`: if `H : a = b`, replace `a` with `b` (or vice versa with `rewrite ← H`) in the goal.
- `reflexivity`: prove a goal of the form `t = t` (trivial equality).
- `discriminate`: prove inequality of distinct constructors (e.g., `0 ≠ S n`).
- `auto`: attempt to prove the goal automatically using a database of hints.

A complete example: proving that addition is commutative in Coq. First, we define natural numbers (if not using the standard library):

```
Inductive nat : Set :=
  | O : nat
  | S : nat → nat.

Fixpoint plus (n m : nat) : nat :=
  match n with
  | O ⇒ m
  | S n' ⇒ S (plus n' m)
  end.
```

Now the theorem and proof:

```
Theorem plus_comm : ∀ n m : nat, plus n m = plus m n.
Proof.
  induction n as [| n' IH].
  - (* Base case: n = O *)
    intros m. simpl. rewrite <- plus_n_O. reflexivity.
  - (* Inductive step: n = S n' *)
    intros m. simpl. rewrite IH. rewrite <- plus_n_Sm. reflexivity.
Qed.
```

The proof uses two auxiliary lemmas — `plus_n_O : ∀ n, plus n O = n` (adding zero on the right is the identity) and `plus_n_Sm : ∀ n m, plus n (S m) = S (plus n m)` — both proved by induction. The structure is typical: the main theorem reduces to lemmas, each lemma is proved by induction, and the proofs compose.

Coq's **inductive types** are the workhorse of specification. They define not just data structures (ℕ, lists, trees) but also **relations** (inductive propositions). For example, the "less than or equal" relation on ℕ:

```
Inductive le (n : nat) : nat → Prop :=
  | le_n : le n n
  | le_S : ∀ m, le n m → le n (S m).
```

This defines `le n m` as the smallest relation closed under two rules: `le n n` (reflexivity) and `le n m → le n (S m)` (monotonicity). This is a **logic program** as much as a data type — Coq can prove statements like `le 3 7` by repeatedly applying the constructors. The **inversion** tactic (`inversion H`) decomposes an inductive hypothesis `H` into the possible ways it could have been constructed — essential for reasoning about relations.

**Key Topics:**
- The Coq proof assistant: Gallina (specification language), Ltac (tactic language), the kernel
- Essential tactics: intros, apply, split, induction, simpl, rewrite, reflexivity, auto
- Inductive types as data (ℕ, lists, trees) and as relations (≤, sorted, permutation)
- Structural induction: the primary proof technique for inductive types
- The `inversion` tactic: case analysis on inductive hypotheses
- Equality in Coq: `=`, `eq`, `eq_rect` (Leibniz equality)
- Automation: `auto`, `eauto`, `omega` (Presburger arithmetic), `ring` (algebraic simplification), `lia` (linear integer arithmetic)
- Ltac programming: writing custom tactics for domain-specific automation
- The CompCert verified C compiler: a 300,000-line Coq development proving that the compiler preserves the semantics of the source program

**Required Reading:**
- Benjamin C. Pierce et al., *Software Foundations, Volume 1: Logical Foundations* (online, 2024/2040 edition), chs. Basics, Induction, Lists, Poly, Tactics, Logic — the standard Coq textbook, freely available
- Yves Bertot and Pierre Castéran, *Interactive Theorem Proving and Program Development: Coq'Art* (2004/2040), chs. 5–8
- Adam Chlipala, *Certified Programming with Dependent Types* (2013/2040), chs. 1–4 (available online at http://adam.chlipala.net/cpdt/)
- Xavier Leroy, "Formal Verification of a Realistic Compiler" *Communications of the ACM* 52:7 (2009): 107–115
- The Coq Standard Library documentation: `Coq.Arith`, `Coq.Lists`, `Coq.Logic`
- Yggdrasil Coq Lab: Software Foundations exercises (Basics through Logic), proving sorting correctness (2040)

**Discussion Questions:**
1. Coq's tactic language (Ltac) allows automation but obscures the underlying proof term. When is automation harmful — and could a Coq proof that relies heavily on `auto` be less trustworthy than one built with explicit tactics?
2. The CompCert compiler is verified in Coq: it proves that the generated assembly code behaves identically to the source C program. But CompCert's parser, assembler, and linker are not verified. Does this compromise the end-to-end guarantee — and what would a fully verified toolchain look like?
3. Coq's kernel is small but written in OCaml, whose runtime and garbage collector are unverified. Is this a practical concern, or is the TCB small enough to trust? (Consider the DeepSpec project's vision of a verified kernel running on verified hardware.)

---

ᚹ **Lecture 8: Lean 4 — A Modern Proof Assistant for Mathematics and Software**

---

### Overview

**Lean 4** (Microsoft Research, 2021–present; de Moura and Ullrich, 2021) is the newest major proof assistant, designed to unify interactive theorem proving with general-purpose programming. Unlike Coq (which separates the specification language Gallina from the tactic language Ltac), Lean 4 is a single language where terms, types, tactics, and metaprograms are all first-class. Lean 4 is implemented in Lean 4 (self-hosting), has a fast C code generator (producing binaries competitive with handwritten C), and features a powerful **metaprogramming framework** that allows users to write custom tactics, decision procedures, and domain-specific automation — all in Lean itself. Lean 4 is the engine behind the **Mathlib** project, a community-driven library aiming to formalise all of undergraduate mathematics (and significant portions of graduate mathematics) in a single, coherent, dependently typed foundation.

Lean 4's type theory, **Lean's Type Theory** (TTₗ), is a variant of the Calculus of Inductive Constructions with:
- A countable hierarchy of non-cumulative universes `Sort u` (where `Type u = Sort (u+1)` and `Prop = Sort 0`)
- Impredicative `Prop` (proof-irrelevant, any quantification over `Type u` can be used in `Prop`)
- Definitional proof irrelevance: any two proofs of the same proposition are definitionally equal
- Quotient types (by any relation) with computation rules — a rare and powerful feature
- Bounded natural numbers `Fin n` as primitive (not derived from ℕ)
- Structures (records), typeclasses (for overloading and canonical instances), and a powerful `simp` tactic for rewriting with a configurable set of lemmas

The Lean 4 proof workflow is similar to Coq's (state a theorem, apply tactics until the goal is closed), but with modern conveniences: the `calc` block for chained equalities, `by` blocks for inline tactic proofs, `termination_by` annotations for recursive functions, and the `aesop` tactic for automated proof search à la Isabelle's `auto`. The **Lean 4 Language Server** provides real-time feedback in VS Code — error messages, goal display, tactic state — making the experience feel like programming with an exceptionally strict type checker rather than proving with a separate tool.

A comparison of the same proof in Coq and Lean 4. In Coq:

```coq
Theorem plus_comm : forall n m, n + m = m + n.
Proof. induction n; intros m; simpl; [rewrite Nat.add_0_r | rewrite IHn, Nat.add_succ_r]; reflexivity. Qed.
```

In Lean 4:

```lean4
theorem add_comm (n m : Nat) : n + m = m + n := by
  induction n with
  | zero => simp
  | succ n ih => simp [ih, Nat.add_succ_comm]
```

The Lean 4 version is more compact because `simp` (the simplifier) knows many arithmetic identities by default, and the `Nat` library is extensively tagged with `@[simp]` lemmas. The `by` block introduces tactic mode; `induction` is a tactic that works like Coq's `induction`; `simp` uses the simplifier. The Lean 4 proof is also a valid Lean 4 term — there is no separation between the language of terms and the language of proofs.

Lean 4's **metaprogramming** is the killer feature. Tactics are first-class Lean 4 functions of type `TacticM Unit`, and they can be written using the same language as the rest of the program. The `elab` command allows users to extend the elaborator — to define new syntactic forms that are elaborated into core Lean terms. This makes Lean 4 extensible in a way that Coq (with Ltac2) and Isabelle (with Eisbach and ML) are not: everything is in one language, one type system, one abstraction stack. Domain-specific languages for verification (e.g., separation logic, temporal logic, probabilistic reasoning) can be implemented as Lean 4 libraries that provide custom syntax, custom tactics, and custom automation — all without leaving Lean.

Mathlib (mathlib4 on GitHub) is the largest repository of formalised mathematics in the world, with over 1.5 million lines of Lean code covering algebra, analysis, topology, number theory, representation theory, algebraic geometry (schemes! — the Liquid Tensor Experiment proved a theorem about condensed mathematics in Lean), and more. The Mathlib community has developed an unusually consistent library design, with a few key typeclasses (`Semiring`, `Ring`, `Field`, `Module`, `TopologicalSpace`) that capture mathematical structures at the right level of generality. The **Liquid Tensor Experiment** (2021–2022) was a landmark: a team led by Peter Scholze (Fields Medalist) and Johan Commelin formalised a theorem that Scholze needed for his work on condensed mathematics, demonstrating that proof assistants are now capable of contributing to cutting-edge research mathematics.

**Key Topics:**
- Lean 4's type theory: universes, impredicative Prop, quotients, definitional proof irrelevance
- The Lean 4 programming model: dependent pattern matching, `where` clauses, `termination_by`, monadic IO
- Tactic-mode proofs in Lean 4: `by` blocks, `induction`, `cases`, `apply`, `have`, `calc`, `simp`, `omega`, `positivity`, `aesop`
- Metaprogramming: `elab` for custom syntax, `TacticM` for custom tactics, `Macro` for transformations
- Mathlib: the architecture of a large-scale formalised mathematics library, typeclasses, canonical instances
- The Liquid Tensor Experiment: formalising cutting-edge mathematics in Lean
- Lean 4 vs. Coq vs. Isabelle vs. Agda: a comparative analysis of design choices
- Code extraction: compiling Lean programs to C for high-performance verified software

**Required Reading:**
- Leonardo de Moura and Sebastian Ullrich, "The Lean 4 Theorem Prover and Programming Language" *CADE-28* (2021): 625–635
- *Theorem Proving in Lean 4* (online textbook, https://leanprover.github.io/theorem_proving_in_lean4/), chs. 1–5 (Dependent Type Theory, Propositions and Proofs, Quantifiers, Tactics, Induction)
- *Mathematics in Lean* (online textbook, https://leanprover-community.github.io/mathematics_in_lean/), chs. 1–4
- *Functional Programming in Lean* (online textbook, https://leanprover.github.io/functional_programming_in_lean/), chs. 1–3
- Kevin Buzzard, "The Rise of Formalism in Mathematics" (2023 ICM talk, 2024), in *Proceedings of the ICM 2022*, vol. 7
- Johan Commelin et al., "The Liquid Tensor Experiment" (blog post and Lean code, 2022), https://xenaproject.wordpress.com/
- Yggdrasil Lean Lab: Proving propositions and induction proofs in Lean 4, formalising a small mathematical theory (2040)

**Discussion Questions:**
1. Lean 4 unifies programming and proving in one language, while Coq separates Gallina (terms) from Ltac (tactics). What are the advantages and disadvantages of each approach — and is the unification in Lean 4 a net positive or does it blur important distinctions?
2. Mathlib's use of typeclasses allows Lean to find canonical instances automatically (e.g., the fact that ℝ is a topological space). How does this compare to Coq's canonical structures and Isabelle's type classes — and what are the pitfalls of typeclass resolution (e.g., diamond problems, non-termination)?
3. The Liquid Tensor Experiment proved that proof assistants can contribute to research mathematics. But the formalisation took a team of experts over a year. When — if ever — will formalisation be fast enough to be part of the daily workflow of working mathematicians?

---

ᚺ **Lecture 9: SAT and SMT Solving — Automated Reasoning at Scale**

---

### Overview

The SAT solver is the silent engine of modern verification. Every time a program verifier checks a verification condition, every time a model checker explores a state, every time a hardware design is checked for equivalence — a SAT solver (or its more powerful cousin, the SMT solver) is doing the heavy lifting, solving Boolean formulas with millions of variables and tens of millions of clauses in seconds. Understanding how SAT solvers work is understanding how formal verification works at industrial scale.

The **SAT problem** — given a propositional formula in conjunctive normal form (CNF), is there a satisfying assignment? — is the canonical NP-complete problem (Cook, 1971; Levin, 1973). Every problem in NP reduces to SAT, and every SAT instance can be encoded as a CNF. A CNF is a conjunction of **clauses**, each a disjunction of **literals** (variables or their negations). The formula (A ∨ ¬B) ∧ (¬A ∨ C ∨ ¬D) ∧ (B ∨ ¬C) is a CNF with three clauses. The goal is to assign each variable true or false such that every clause has at least one true literal.

Modern SAT solvers are based on the **Conflict-Driven Clause Learning (CDCL)** algorithm (Marques-Silva and Sakallah, 1996; Moskewicz et al., 2001 — the Chaff solver). CDCL extends the older **DPLL** (Davis-Putnam-Logemann-Loveland, 1962) with:

1. **Unit propagation**: If a clause has only one unassigned literal, that literal must be true for the clause to be satisfied. The solver assigns it and propagates the consequences. Unit propagation is the workhorse — it is applied exhaustively after every decision.

2. **Decision heuristics**: When no unit propagation is possible, the solver chooses an unassigned variable and assigns it a value (true or false). The **VSIDS** heuristic (Variable State Independent Decaying Sum), introduced in Chaff, chooses variables based on how frequently they appear in recent conflicts — variables involved in conflicts are prioritised, on the theory that they are central to the hard part of the problem.

3. **Conflict analysis and clause learning**: If unit propagation leads to a conflict (a clause becomes false — all its literals are false), the solver analyses the **implication graph** to identify the assignments that caused the conflict. It then learns a new clause (the **conflict clause**) that rules out the conflicting assignment and all assignments that share the same root cause. The learned clause is added to the clause database, and the solver backtracks to the earliest decision that can be flipped.

4. **Restarts**: Periodically, the solver discards its current assignment and starts over, keeping the learned clauses. Restarts help the solver escape from unfruitful parts of the search space. The restart policy (frequency, strategy) is heavily tuned.

5. **Clause deletion**: The clause database grows without bound as new clauses are learned. Periodically, the solver deletes learned clauses that are long, infrequently used, or low in "activity" — freeing memory and speeding up unit propagation.

The CDCL algorithm has transformed SAT from a problem of theoretical interest into a practical tool. A typical industrial SAT instance — verifying that two versions of a microprocessor circuit are equivalent — may have 10⁶ variables and 10⁷ clauses, and a modern SAT solver (CaDiCaL, Kissat, Glucose) solves it in minutes. The reasons for this success are partly algorithmic (CDCL is remarkably effective) and partly structural: industrial SAT instances have **hidden structure** — they encode real circuits, real programs, real constraints — that CDCL exploits through variable ordering, clause learning, and restarts.

**SMT (Satisfiability Modulo Theories)** extends SAT with decision procedures for background theories. An SMT solver takes a formula involving both Boolean structure and theory atoms — e.g., `(x + y < 5) ∧ (x > 2 ∨ a[i] = 3) ∧ (f(x) ≠ f(y))` — and determines satisfiability. The theories include:

- **Linear arithmetic (LA)**: Presburger (integer) and real arithmetic — solved by the Simplex algorithm (Dutertre and de Moura, 2006) or Fourier-Motzkin elimination.
- **Bit-vectors (BV)**: fixed-width machine integers — solved by bit-blasting (translate to SAT) or specialised word-level procedures.
- **Arrays**: `select(a, i)` and `store(a, i, v)` — solved by instantiating array axioms.
- **Uninterpreted functions (UF)**: `f(x) = f(y) → x = y` — solved by congruence closure (Nelson and Oppen, 1980).
- **Algebraic datatypes (ADT)**: constructors, pattern matching — solved by acyclicity and injectivity axioms.
- **Quantifiers**: `∀x. P(x)` — solved by E-matching (instantiate `∀x. P(x)` with terms that match `P(x)`) or MBQI (Model-Based Quantifier Instantiation, Ge and de Moura, 2009).

The standard architecture is **DPLL(T)** (or its modern successor, CDCL(T)): the SAT solver handles the Boolean structure, and theory solvers handle the theory atoms. When the SAT solver proposes a Boolean assignment, the theory solvers check whether the assignment is consistent in the theory; if not, they produce a **theory lemma** (a clause that rules out the inconsistent assignment), which is added to the SAT solver's clause database. This architecture separates concerns cleanly and allows theory solvers to be developed independently.

Z3 (Microsoft Research), CVC5 (Stanford/Iowa), and Yices (SRI) are the leading SMT solvers. Z3 in particular has become the standard back-end for program verifiers (Dafny, Frama-C, Why3, Viper), model checkers, symbolic execution engines (KLEE, Triton), and program synthesis tools. Z3 processes over a billion queries per day across Microsoft's product lines (Windows, Azure, Office, GitHub) for tasks ranging from driver verification to security analysis to test generation.

**Key Topics:**
- The SAT problem, CNF encoding, Tseitin transformation (converting any formula to CNF in linear time)
- DPLL: the ancestor of modern SAT — unit propagation, pure literal elimination, splitting
- CDCL: conflict analysis, implication graph, 1-UIP (first Unique Implication Point) learning, backjumping
- VSIDS heuristic: activity-based variable selection, exponential decay, phase saving
- Restarts and clause deletion: practical strategies for managing search and memory
- DPLL(T): the architecture that combines SAT with theory solvers
- Theory decision procedures: linear arithmetic (Simplex), bit-vectors (bit-blasting), arrays (instantiation), UF (congruence closure)
- Quantifier instantiation: E-matching, triggers, MBQI, the challenges of quantifier-heavy VCs
- SAT competition and incremental improvements: the annual SAT Competition tracks solver progress; solvers have improved by orders of magnitude since 2000

**Required Reading:**
- Armin Biere, Marijn Heule, Hans van Maaren, and Toby Walsh (eds.), *Handbook of Satisfiability* (2nd ed., 2021/2040), chs. 1 (History), 4 (CDCL), 26 (SMT)
- João Marques-Silva and Karem Sakallah, "GRASP: A Search Algorithm for Propositional Satisfiability" *IEEE Transactions on Computers* 48:5 (1999): 506–521
- Matthew Moskewicz et al., "Chaff: Engineering an Efficient SAT Solver" *DAC 2001*: 530–535
- Leonardo de Moura and Nikolaj Bjørner, "Satisfiability Modulo Theories: Introduction and Applications" *Communications of the ACM* 54:9 (2011): 69–77
- Bruno Dutertre and Leonardo de Moura, "A Fast Linear-Arithmetic Solver for DPLL(T)" *CAV 2006*: 81–94
- Yggdrasil SAT/SMT Lab: Encoding puzzles as SAT, verifying simple programs with Z3, analysing solver logs (2040)

**Discussion Questions:**
1. CDCL solvers routinely solve instances with millions of variables, despite SAT being NP-complete. Does this mean that P = NP for "practical" instances — or is there a more nuanced characterisation of where the hardness lies?
2. SAT solvers use heuristics (VSIDS, restarts, clause deletion) that are engineered, not proved. Is the resulting solver still a "formal method" — or does the reliance on unproved heuristics undermine the guarantee of correctness?
3. SMT with quantifiers is a hard problem: E-matching is brittle (small changes to triggers can cause proofs to fail), and MBQI can be slow. What would a robust, predictable quantifier instantiation strategy look like — and is it even possible given the undecidability of first-order logic?

---

ᚾ **Lecture 10: Abstract Interpretation — Sound Over-Approximation of Program Behaviour**

---

### Overview

**Abstract interpretation** (Cousot and Cousot, 1977) is a theory of sound approximation of program semantics. The idea is elegant: instead of computing the exact behaviour of a program (which may be undecidable — the halting problem), we compute an **over-approximation** — a superset of the possible behaviours — that is guaranteed to contain all actual behaviours. If the over-approximation satisfies a safety property (e.g., "no division by zero," "no null pointer dereference"), then the actual program satisfies it. If the over-approximation does not satisfy the property, the property may or may not hold — the analysis produces a **false alarm** (a reported bug that cannot actually occur). The art of abstract interpretation is designing abstract domains that are precise enough to avoid false alarms while remaining computable and efficient.

The mathematical framework: a **concrete semantics** is a function F from concrete states to concrete states — the collecting semantics that maps each program point to the set of all states that can reach that point. An **abstract semantics** is a function F♯ from abstract states to abstract states that over-approximates F. Formally, there is a **Galois connection** (α, γ) between the concrete domain (sets of states, ordered by inclusion ⊆) and the abstract domain (elements of an abstract lattice, ordered by the abstract ordering ⊑). The abstraction function α maps a set of concrete states to the abstract state that best over-approximates it; the concretisation function γ maps an abstract state to the set of concrete states it represents. The soundness condition is: for any concrete set S, S ⊆ γ(α(S)) — the abstract state represents at least all the concrete states. And for the abstract transfer function: F(S) ⊆ γ(F♯(α(S))) — applying the abstract transfer function and concretising yields at least all states reachable by applying the concrete semantics and abstracting.

The simplest abstract domain is the **sign domain**: abstract values are {⊥, neg, zero, pos, ⊤} (bottom = unreachable, neg = all negative integers, zero = {0}, pos = all positive integers, ⊤ = all integers). Addition in the sign domain: `pos + pos = pos`, `pos + neg = ⊤`, `zero + x = x`, `⊥ + x = ⊥`. If we abstract a program using the sign domain and compute `x := a * b; y := x + c`, we can conclude that if `a` and `b` are both `pos`, then `x` is `pos`; if `c` is `neg`, then `y` is `⊤` (could be anything). This is crude but sound — the sign domain proves that `x / y` never divides by zero if `y` is `pos` or `neg`, but it cannot prove anything if `y` is `⊤`.

The **interval domain** generalises signs: abstract values are intervals [l, u] where l and u are integers (or -∞, +∞). Addition: [a, b] + [c, d] = [a+c, b+d]. Multiplication: the product of two intervals is the interval from the minimum to the maximum of the four products a*c, a*d, b*c, b*d. The interval domain can prove that `x ∈ [1, 10]` and `y ∈ [5, 20]` implies `x + y ∈ [6, 30]`, which is more precise than `⊤`. But intervals cannot track relationships between variables — they are **non-relational**. If we know `x ∈ [0, 10]` and `y = -x`, the interval domain loses the relationship and deduces `y ∈ [-10, 0]` (which is correct) but then `x + y ∈ [-10, 10]` — it cannot deduce that `x + y = 0` because it has forgotten that `y = -x`.

The **polyhedra domain** (Cousot and Halbwachs, 1978) is relational: abstract states are convex polyhedra (intersections of linear inequalities). If we know `x ≥ 0`, `x ≤ 10`, `y = -x`, the polyhedron is `{ (x, y) | 0 ≤ x ≤ 10, y = -x }`, and it can deduce `x + y = 0`. Polyhedra are more precise than intervals but more expensive — the convex hull operation (joining two polyhedra at control-flow merges) can be exponential. The **octagon domain** (Miné, 2001) is a compromise: it tracks constraints of the form `±x ± y ≤ c`, which captures relationships between pairs of variables at reasonable cost (O(n³) for n variables). The octagon domain is used in Astrée, the static analyser that proved the absence of runtime errors in the primary flight control software of the Airbus A380.

**Widening** is the mechanism that ensures termination of abstract interpretation in the presence of loops. Without widening, analysing a loop might require an infinite ascending chain of abstract states — at each iteration, the abstract state becomes more precise but never stabilises. Widening `▽` is an operator that accelerates convergence by jumping to a limit: for an ascending chain `X₀ ⊑ X₁ ⊑ X₂ ⊑ ...`, the widened chain `Y₀ = X₀`, `Y_{i+1} = Y_i ▽ X_{i+1}` must stabilise after finitely many steps. For the interval domain, widening typically sets unstable bounds to ±∞: if the lower bound of an interval decreases on an iteration, widening sets it to -∞; if the upper bound increases, widening sets it to +∞. This guarantees termination but loses precision. **Narrowing** can then recover some precision by iterating the transfer function from the widened result, using the fact that the abstract semantics is monotonic and the widened state is above the least fixed point.

**Key Topics:**
- The abstract interpretation framework: concrete semantics, abstract semantics, Galois connections, soundness
- The sign domain, interval domain, and the tension between precision and cost
- Relational domains: polyhedra, octagons, the reduced product of domains
- Widening and narrowing: ensuring termination without sacrificing all precision
- Astrée: verifying absence of runtime errors in Airbus flight control software — a landmark success of abstract interpretation
- Applications: dataflow analysis in compilers (reaching definitions, live variables), shape analysis (inferring heap invariants), termination analysis, worst-case execution time (WCET) analysis
- Abstract interpretation in modern tools: Polyspace (MathWorks), Frama-C Value Analysis, Infer (Facebook/Meta), CodeSonar (GrammaTech)
- Limitations: false alarms, difficulty with dynamic dispatch and concurrency, the annotation burden

**Required Reading:**
- Patrick Cousot and Radhia Cousot, "Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints" *POPL 1977*: 238–252
- Flemming Nielson, Hanne Riis Nielson, and Chris Hankin, *Principles of Program Analysis* (1999/2040), chs. 1–4
- Antoine Miné, "The Octagon Abstract Domain" *Higher-Order and Symbolic Computation* 19:1 (2006): 31–100
- Bruno Blanchet et al., "A Static Analyzer for Large Safety-Critical Software" *PLDI 2003*: 196–207 — the Astrée paper
- Francesco Logozzo and Manuel Fähndrich, "Pentagon Abstract Domain" in *SAS 2010*, and "Static Contract Checking with Abstract Interpretation" *FoVeOOS 2010*
- Yggdrasil Abstract Interpretation Lab: Implementing a Sign Analysis, Widening for Loop Invariants (2040)

**Discussion Questions:**
1. Abstract interpretation is sound by construction: every reported error is a real error (no false negatives), but not every reported error is real (false positives are possible). Is this the right trade-off for safety-critical software — and would a different trade-off (no false positives, possible false negatives) ever be appropriate?
2. Widening forces termination by losing precision. Could machine learning predict a precise invariant from a few iterations of the concrete semantics, avoiding widening entirely — and would the resulting analysis still be "formal"?
3. Astrée proved the absence of runtime errors in Airbus A380 flight control software — a program with over 100,000 lines of C. But Astrée took years of tuning to eliminate false alarms. What would it take to make abstract interpretation "one-click" — usable by programmers without PhDs in static analysis?

---

ᚾ (alt) **Lecture 11: Separation Logic — Reasoning About Mutable State and Concurrency**

---

### Overview

**Separation logic** (Reynolds, 2002; O'Hearn, Ishtiaq, and Reynolds, 2001) is the logic of mutable state — a Hoare-logic extension that makes reasoning about pointers, heap-allocated data structures, and concurrent access modular and compositional. The key innovation is the **separating conjunction** P ∗ Q ("P and separately Q"), which asserts that the heap can be partitioned into two **disjoint** sub-heaps — one satisfying P, the other Q. Because the sub-heaps are disjoint, reasoning about P does not interfere with reasoning about Q — there is no aliasing, no overlapping, no shared state. This is the **frame rule**: if {P} C {Q} and C does not modify any variables free in R, then {P ∗ R} C {Q ∗ R}. The frame rule says: if a command works on a small piece of the heap, it also works on a larger heap — it does not touch the extra part. This is the essence of **local reasoning**.

Separation logic extends Hoare logic with new atomic commands for heap manipulation: **allocation** (x := cons(E₁, ..., Eₙ) — allocate n consecutive heap cells, initialise them with E₁...Eₙ, and assign the address of the first to x), **lookup** (x := [E] — read the value at heap address E into x), **mutation** ([E₁] := E₂ — write E₂ to heap address E₁), and **deallocation** (dispose(E) — free the heap cell at E). The axiomatic semantics:

- `{emp} x := cons(E) {x ↦ E}` — from an empty heap, allocation produces a single-cell heap with x pointing to E.
- `{E ↦ _} [E] := F {E ↦ F}` — mutation updates the value at address E.
- `{E ↦ _} dispose(E) {emp}` — deallocation frees the cell at E.
- `{E ↦ F} x := [E] {x = F ∧ (E ↦ F)}` — lookup reads the value and leaves the heap unchanged.

The **separating implication** (or magic wand) P −∗ Q ("P minus-star Q") is the right adjunct of ∗: (P ∗ Q) ⊢ R if and only if P ⊢ (Q −∗ R). Intuitively, P −∗ Q is a resource that, when combined with any heap satisfying P, yields a heap satisfying Q. Magic wands are used to specify data structures: for a linked list from x to nil, we can write `list(x, nil)`, which is defined recursively, and the magic wand captures the "if I have the head of the list, I can get the tail" relationship.

The canonical example: verifying in-place reversal of a singly linked list. The list predicate `list(x, y)` means "there is a linked list segment from x to y." The reversal algorithm:

```
j := nil;
while i ≠ nil do
  k := [i+1];  (* next pointer *)
  [i+1] := j;
  j := i;
  i := k
```

The loop invariant: `∃α, β. list(i, nil) ∗ list(j, nil) ∧ rev(α) = β · rev(γ)`, where α is the original list, β is the already-reversed prefix, and γ is the remaining suffix. The separating conjunction ensures that the `list(i, nil)` segment and the `list(j, nil)` segment are disjoint — no cycles, no sharing — so the reversal is safe. The proof follows from the invariant and the loop condition.

**Concurrent separation logic** (O'Hearn, 2007) extends separation logic to concurrent programs with shared memory. The key new construct is the **resource invariant** — an assertion that describes the shared state protected by a lock. When a thread acquires a lock, it gains the resource invariant (which it can use and modify, as long as it re-establishes the invariant before releasing). The rule is:

```
{(P ∗ R) ∧ B} C {Q ∗ R}  (* R is the resource invariant, B is the condition, C modifies shared state *)
---------------------------------------
{P} with r when B do C {Q}
```

The thread must own P (its private state) and R (the shared state) when it acquires the lock; after executing C, it must re-establish R before releasing. This is the basis of the **CSL (Concurrent Separation Logic)** that was used to verify the safety and liveness of concurrent programs in Coq (VST — Verified Software Toolchain) and in the **Caper** tool.

**Iris** (Jung et al., 2015–present) is a modern separation logic framework implemented in Coq. Iris extends concurrent separation logic with **invariants** (persistent assertions that hold globally), **ghost state** (auxiliary state used in proofs but not present at runtime), and **modalities** (later `▷`, persistently `□`) for reasoning about step-indexed models. Iris has been used to verify subtle concurrent algorithms (lock-free stacks, concurrent hash maps, RCU — Read-Copy-Update) and to build **logical relations** for type-safety proofs of programming languages (RustBelt — proving the safety of unsafe Rust code).

**Key Topics:**
- Separation logic syntax: emp (empty heap), E ↦ F (points-to), P ∗ Q (separating conjunction), P −∗ Q (magic wand)
- The frame rule and local reasoning: verifying a procedure once and composing its specification with any caller
- The list segment predicate: inductive definition, properties, application to list reversal
- Concurrent separation logic: locks, resource invariants, the rule of the lock
- The Iris framework: step-indexing, invariants, ghost state, modalities
- RustBelt: verifying the safety of unsafe Rust using Iris — proving that safe Rust code cannot exhibit undefined behaviour
- Applications: seL4 microkernel verification (20,000 lines of C verified against a formal specification in Isabelle/HOL using separation logic), CertiKOS verified hypervisor

**Required Reading:**
- John C. Reynolds, "Separation Logic: A Logic for Shared Mutable Data Structures" *LICS 2002*: 55–74
- Peter O'Hearn, "Resources, Concurrency, and Local Reasoning" *Theoretical Computer Science* 375:1–3 (2007): 271–307
- Ralf Jung et al., "Iris: Monoids and Invariants as an Orthogonal Basis for Concurrent Reasoning" *POPL 2015*: 637–650
- Gerwin Klein et al., "Comprehensive Formal Verification of an OS Microkernel" *ACM Transactions on Computer Systems* 32:1 (2014): 1–70 — the full seL4 paper
- Ralf Jung et al., "RustBelt: Securing the Foundations of the Rust Programming Language" *POPL 2018*: 1–34
- Yggdrasil Separation Logic Lab: Verifying linked list operations (reversal, insertion, deletion) in Dafny or VeriFast (2040)

**Discussion Questions:**
1. The separating conjunction P ∗ Q requires that the sub-heaps be disjoint. Why is disjointness the key to modular reasoning — and what happens when two threads need to share a data structure? (Hint: consider CSL's resource invariants.)
2. Iris is implemented in Coq, which means Iris proofs are Coq proofs — checked by Coq's kernel. But Iris itself is defined in Coq, not proved correct. Is this a problem — and what would it mean to verify Iris itself?
3. RustBelt proved that safe Rust code cannot exhibit undefined behaviour, assuming unsafe Rust code is correctly annotated. But the unsafe code in Rust's standard library is annotated by humans — and humans make mistakes. Does this limit the practical guarantee of RustBelt?

---

ᛃ **Lecture 12: Industrial-Grade Verification — CompCert, seL4, TLA⁺, and the DeepSpec Vision**

---

### Overview

Formal verification has moved from academic curiosity to industrial practice. This lecture surveys four landmark projects that demonstrate the viability — and the limits — of applying formal methods to real-world systems. Each project chose a different verification approach and a different target, and each taught the community something about what works, what doesn't, and what the future holds.

**CompCert** (Leroy, 2006–present) is a verified C compiler. Written in Coq, CompCert takes a subset of C (CompCert C, covering most of C99 with the exception of variable-length arrays and some obscure features) and produces PowerPC, ARM, RISC-V, or x86 assembly. The compiler is structured as a sequence of **translation passes** (20+ passes, from C to C#minor to Cminor to RTL to LTL to Mach to assembly), and each pass is proved correct: for every source program, the generated assembly code has exactly the same observable behaviour as the source program (or the source program has undefined behaviour, in which case the compiler can do anything — this is C's "undefined behaviour licence"). The proof is 45,000 lines of Coq (not counting the specification and the algorithms), and it took approximately 6 person-years. CompCert is now maintained at Inria and used in industry (Airbus for DO-178C avionics certification). The key lesson of CompCert: **compilers can be verified**, and the verification is robust enough to catch real bugs — random testing of CompCert against GCC and LLVM found no miscompilation bugs in the verified parts of CompCert, while finding hundreds in GCC and LLVM.

**seL4** (Klein et al., 2009–present) is a verified microkernel — approximately 10,000 lines of C, running on ARM and x86-64, with a formal specification in Isabelle/HOL and a proof that the C implementation refines the specification. The verification includes: functional correctness (the kernel behaves exactly as specified), integrity (no user can modify kernel data without permission), confidentiality (no user can read kernel data without permission), and the worst-case execution time of all kernel operations is bounded. The proof is approximately 200,000 lines of Isabelle/HOL, and it took approximately 25 person-years. seL4 is now maintained by the Trustworthy Systems group at UNSW and is used in defence applications (autonomous helicopters, drones) where a kernel compromise would be catastrophic. The key lesson of seL4: **operating system kernels can be verified**, but the cost is high — the verification effort exceeds the implementation effort by a factor of 10–50.

**TLA⁺** (Lamport, 1999–present) is a specification language based on temporal logic and set theory, designed for describing concurrent and distributed systems at a high level. TLA⁺ is not a programming language and not a proof assistant — it is a **design tool** that allows engineers to write precise, unambiguous specifications of protocols, state machines, and algorithms, and to model-check them for safety and liveness properties. TLA⁺ has been used at Amazon since 2011 for verifying critical AWS services (S3, DynamoDB, EBS, and others). Amazon engineers report that TLA⁺ model checking found subtle bugs in designs — race conditions, deadlocks, data loss scenarios — that would have been extremely difficult to find through testing. The key lesson of TLA⁺: **specification alone is valuable** — even without an implementation proof, the act of writing a precise specification and model-checking it catches design bugs early, when they are cheap to fix. TLA⁺ has also been used at Microsoft (Azure Cosmos DB), Oracle (database algorithms), and Elastic (Elasticsearch).

The **DeepSpec** project (Appel et al., 2017–present) is a multi-institution effort to build a **verified software stack** — from the hardware (verified RISC-V processor) through the operating system (verified kernel, verified file system, verified network stack) to the compiler (verified C compiler) and the application (verified cryptographic library, verified web server). The vision is a computer system where every layer has a machine-checked proof of correctness, and the proofs compose — the proof that the application satisfies its specification relies on the proof that the OS satisfies its specification, which relies on the proof that the hardware satisfies its specification. DeepSpec has demonstrated the feasibility of this vision at small scale (a verified HTTP server running on a verified OS, compiled with a verified compiler, on verified hardware), but the full stack — from transistors to TLS — remains a research goal. The key lesson of DeepSpec: **verified components can compose**, but the specifications must be designed for composition — matching the interfaces between layers is as hard as verifying the layers themselves.

The 2040 horizon: formal methods are transitioning from "possible" to "expected" for safety-critical and security-critical software. Standards bodies (ISO 26262 for automotive, DO-178C for avionics, IEC 61508 for industrial control, Common Criteria for security) are incorporating formal verification as a recommended or required activity. The Verified Software Initiative (Hoare, 2003) and the DeepSpec project have set the goal of a fully verified general-purpose computing platform by 2040. Whether that goal is met remains to be seen, but the trajectory is clear: formal verification is the infrastructure of trust for the software-defined world.

**Key Topics:**
- CompCert: the architecture of a verified compiler, the translation validation methodology, the role of undefined behaviour, the cost and scalability of compiler verification
- seL4: the specification, the refinement proof, the integrity and confidentiality properties, the binary verification (proving that the compiled binary matches the C source), the performance cost of verification
- TLA⁺: the language (TLA⁺, PlusCal), the TLC model checker, the Apalache symbolic model checker, industrial adoption at Amazon
- DeepSpec: the vision, the interaction trees (ITrees) and VST (Verified Software Toolchain) approaches, the composition challenge, the hardware-software interface
- The cost of verification: $$$ per line of verified code, the annotation burden, the skill barrier
- The 2040 landscape: formal methods in standards, verified AI components, formal verification of AGI safety protocols
- Future directions: AI-assisted proof (LLM-generated invariants, tactic prediction), modular verification at scale, lightweight formal methods (property-based testing with proofs), continuous verification in CI/CD

**Required Reading:**
- Xavier Leroy, "Formal Verification of a Realistic Compiler" *Communications of the ACM* 52:7 (2009): 107–115
- Gerwin Klein et al., "seL4: Formal Verification of an OS Kernel" *Communications of the ACM* 53:6 (2010): 107–115
- Leslie Lamport, *Specifying Systems: The TLA+ Language and Tools for Hardware and Software Engineers* (2002/2040), chs. 1–4
- Chris Newcombe et al., "How Amazon Web Services Uses Formal Methods" *Communications of the ACM* 58:4 (2015): 66–73
- Andrew W. Appel et al., "The DeepSpec Vision" (2017), https://deepspec.org/
- C.A.R. Hoare, "The Verifying Compiler: A Grand Challenge for Computing Research" *Journal of the ACM* 50:1 (2003): 63–69
- Yggdrasil Verification Lab: Writing a TLA⁺ specification and model-checking it, Reading CompCert or seL4 proof excerpts (2040)

**Discussion Questions:**
1. CompCert is proved correct, but its parser, assembler, and linker are not verified, and the C standard itself has ambiguities. Does the "verified" label create a false sense of security — and what would a truly end-to-end verified compilation pipeline look like?
2. TLA⁺ at Amazon found design bugs that testing missed. But TLA⁺ specifications are not implementations — the implementation can diverge from the specification. Does this limit the value of specification-only verification, or is it "good enough" for most practical purposes?
3. The DeepSpec vision of a fully verified stack from hardware to application is inspiring but has taken decades. Is this effort worth the investment — or would the same resources, spent on better testing and monitoring, produce safer systems faster?

---

## Appendix: Course Resources

### Primary Textbooks
- Michael Huth and Mark Ryan, *Logic in Computer Science: Modelling and Reasoning about Systems* (2nd ed., 2004/2040)
- Aaron R. Bradley and Zohar Manna, *The Calculus of Computation: Decision Procedures with Applications to Verification* (2007/2040)
- Benjamin C. Pierce et al., *Software Foundations* (online, continuously updated), vols. 1–6

### Software Tools
- **Coq 8.20** (Inria) — interactive proof assistant with the CIC type theory
- **Lean 4** (Microsoft Research) — modern proof assistant with metaprogramming
- **Z3 4.13** (Microsoft Research) — SMT solver
- **Dafny** (Microsoft Research) — program verifier with automatic VC generation
- **TLA⁺ Toolbox** (Microsoft Research / INRIA) — specification and model checking
- **NuSMV / nuXmv** (FBK) — symbolic model checker
- **SPIN 6.5** (Bell Labs / NASA JPL) — explicit-state LTL model checker

### Assessment
- **30%** — Weekly Coq/Lean proof exercises (submitted as `.v` / `.lean` files)
- **30%** — Midterm: formal verification of a simple concurrent protocol in Dafny or TLA⁺
- **40%** — Final project: formalise and verify a non-trivial algorithm or protocol (student's choice, in Coq, Lean, Dafny, or TLA⁺)

### Instructor's Note
*This course is the gateway to the Verification and Security specialisation. The concepts are deep, the tools are powerful, and the mindset — that code is not correct until it is proved correct — will serve you for a lifetime, whether you build compilers, kernels, blockchains, or the AI systems of 2045. The runes teach: **ᚹ** (Wunjo) is the joy of right action — and there is no joy more pure than the certainty of a proved program.*

— Yggdrasil Department of Computer Science, 2040
