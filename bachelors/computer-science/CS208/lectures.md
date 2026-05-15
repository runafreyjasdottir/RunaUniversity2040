# CS208: Formal Methods & Verification
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4  
**Prerequisites:** CS102 — Discrete Mathematics for CS; CS201 — Data Structures & Algorithms II  
**Description:** Rigorous introduction to formal methods for specifying, verifying, and proving correctness of software and hardware systems. Covers propositional and first-order logic, model checking (CTL, LTL, SPIN, NuSMV), type theory (simply-typed lambda calculus, dependent types), and proof assistants (Coq, Lean 4). Students learn to write machine-checked proofs and specifications, bridging the gap between mathematical rigour and engineering practice. Lab work uses the Yggdrasil Mimir Verification Cluster.

---

## Lecture 1: Why Formal Methods? — Correctness, Complexity, and the Cost of Failure

The history of computing is, in large part, a history of bugs. The Year 2000 problem cost an estimated $300 billion worldwide. The Ariane 5 explosion on 4 June 1996 — thirty-seven seconds after launch, destroyed by an overflow in a 64-bit floating-point number converted to a 16-bit signed integer — cost $500 million and years of investigation. The Therac-25 radiation therapy machine killed six patients between 1985 and 1987 because a race condition allowed the electron beam to operate at full power with the treatment table in the wrong position. These are not edge cases or theoretical curiosities; they are the inevitable consequences of building systems whose complexity exceeds our ability to reason informally about them.

Formal methods respond to this pattern with a radical proposition: we should *prove* that our systems are correct, not merely test them. Testing, as Dijkstra observed in his 1970 Turing Award lecture "The Humble Programmer," can show the presence of bugs but never their absence. Formal verification replaces probabilistic confidence with mathematical certainty — or rather, it replaces one kind of uncertainty (does the program behave correctly on untested inputs?) with another (does the formal specification capture what we actually want?). This tradeoff is the central dialectic of the field, and understanding it is the prerequisite for all that follows.

A **formal method** is a mathematically rigorous technique for specifying, developing, and verifying systems. The "formal" in "formal methods" contrasts with "informal" or "semi-formal" approaches: a formal specification is written in a language with precisely defined syntax and semantics, leaving no room for ambiguity. Where a natural-language requirement might say "the system shall respond within a reasonable time," a formal specification says "∀s ∈ States, ∀r ∈ Requests, response_time(s, r) ≤ T_max." The formal version is checkable by machine; the informal version requires human interpretation.

The formal methods landscape in 2040 has consolidated around three major paradigms. **Model checking** (Clarke, Emerson, and Sistla, 1986) verifies that a finite-state model of a system satisfies a temporal-logic specification. It is fully automated: the model checker explores all reachable states and either confirms the property holds or produces a concrete counterexample trace. **Theorem proving** (de Bruijn's Automath, 1968; Milner's LCF, 1972) constructs a mathematical proof that a system satisfies its specification, typically requiring human guidance but achieving far greater generality. **Type theory** (Howard, 1969; Martin-Löf, 1971) expresses correctness properties as types, so that a well-typed program is *ipso facto* correct — the Curry-Howard correspondence makes types into propositions and programs into proofs.

Each paradigm has characteristic strengths. Model checking handles concurrent systems naturally (it enumerates all interleavings), produces counterexamples when properties fail, and requires comparatively little expertise. Theorem proving scales to infinite-state systems and parameterised families, and can verify rich mathematical properties (correctness of sorting algorithms, properties of real-number arithmetic). Type-theoretic verification integrates with the programming language itself, so verification happens as part of compilation — there is no separate verification step. The modern synthesis, epitomised by proof assistants like Coq and Lean 4, draws on all three: dependent types encode specifications, tactics automate proof construction, and extraction produces verified code.

The **Curry-Howard correspondence** is the philosophical foundation. It states that proofs are programs and propositions are types. Under this reading, a proof of implication A → B is a function that takes a proof of A and returns a proof of B; a proof of conjunction A ∧ B is a pair of proofs; a proof of disjunction A ∨ B is a tagged union. The correspondence is not merely analogical — it is an isomorphism between systems of logic and systems of types. Intuitionistic propositional logic corresponds to the simply-typed lambda calculus; first-order logic corresponds to dependent function types (Π-types); second-order logic corresponds to polymorphic types (System F). Understanding this correspondence transforms verification from an external activity (proving things *about* programs) into an internal one (writing programs that *are* proofs).

Yggdrasil's verification culture runs deep. The Mimir Research Cluster is named for the being who guards the well of wisdom — an apt metaphor for a system that guards against incorrect computation. The Department of Computer Science has mandated formal verification for all safety-critical code in autonomous vehicles since 2038, following the Reykjavik Protocol — an international agreement that requires machine-checked proofs of safety properties for any self-driving system operating on public roads. Students in CS208 will learn to write such proofs.

**Required Reading:**
- Clarke, Emerson & Sistla, "Automatic Verification of Finite-State Concurrent Systems Using Temporal Logic Specifications," *ACM TOPLAS* 8:2 (1986): 244–263
- Dijkstra, "The Humble Programmer," *CACM* 15:10 (1972): 859–866
- Wadler, "Propositions as Types," *Communications of the ACM* 58:12 (2015): 75–84
- Yggdrasil Verification Lab: Introduction to the Mimir Cluster (2040)

**Discussion Questions:**
1. Dijkstra claimed that testing can only show the presence of bugs, never their absence. Is this argument decisive, or are there cases where testing provides stronger guarantees than formal methods?
2. The Ariane 5 failure arose from reusing Ariane 4 code without verifying its assumptions in the new context. How does formal specification address this class of errors, and what are its limitations?
3. The Curry-Howard correspondence suggests that programming and proving are the same activity. Why, then, is verified software not the default in industry?

---

## Lecture 2: Propositional and First-Order Logic — The Language of Specification

Propositional logic is the simplest non-trivial formal system: a language of atomic propositions connected by logical connectives (¬, ∧, ∨, →, ↔) with a well-defined notion of truth (valuation) and derivation (proof system). A **proposition** is a declarative statement that is either true or false. The connectives are truth-functional: ¬A is true iff A is false; A ∧ B is true iff both A and B are true; A ∨ B is true iff at least one of A, B is true; A → B is true iff A is false or B is true (the material conditional). These definitions are captured in truth tables, and every propositional formula has a unique truth value for each assignment of truth values to its atomic propositions.

**Satisfiability** asks whether there exists an assignment making the formula true. **Validity** (tautology) asks whether the formula is true under *all* assignments. These are dual: a formula is satisfiable iff its negation is not valid; a formula is valid iff its negation is not satisfiable. The SAT problem (determining satisfiability of a propositional formula in conjunctive normal form) is the canonical NP-complete problem (Cook-Levin, 1971). Modern SAT solvers — MiniSat, Glucose, CryptoMiniSat — use conflict-driven clause learning (CDCL) with watched literals, unit propagation, and heuristic branching to solve instances with millions of variables. The practical success of SAT solving is one of the great engineering achievements of computer science: theoretically exponential, yet routinely fast on real-world instances.

**First-order logic** (FOL) extends propositional logic with quantifiers (∀, ∃) and predicates over a domain of individuals. FOL formulas have the form ∀x. P(x) → Q(x) or ∃x. ∀y. R(x,y), where x and y range over some domain D and P, Q, R are predicates. FOL is far more expressive: it can state properties like "every natural number has a successor" (∀n. ∃m. S(n,m)) that propositional logic cannot express. This expressiveness comes at a cost: the validity problem for FOL is undecidable (Church, 1936; Turing, 1936) — there is no algorithm that, given an arbitrary FOL formula, determines whether it is valid. However, FOL is *semi-decidable*: if a formula is valid, a proof can be found; if it is not, the search may run forever.

The semantics of FOL require a **structure** (or interpretation) consisting of a domain D and interpretations for each predicate, function, and constant symbol. A formula is *valid* if it is true in every structure; *satisfiable* if true in some structure; *unsatisfiable* if true in no structure. Natural deduction and the sequent calculus provide complete proof systems for FOL (Gödel's completeness theorem, 1929): a formula is provable iff it is valid. This is a remarkable result — it means that the syntactic notion of provability and the semantic notion of truth coincide for first-order logic.

For specification, we care about specific theories. **Equality** (the theory of equality with uninterpreted functions, QF_UF) is decidable and forms the basis for most SMT solvers. **Linear arithmetic** over integers (QF_LIA) and reals (QF_LRA) is decidable and essential for verifying numerical properties. **Arrays** (QF_AX) axiomatised via McCarthy's select and store operations support reasoning about data structures. SMT solvers — Z3 (Microsoft Research, 2007), CVC5 (2022), Yggdrasil's own Mimir-SMT (2039) — combine these theories in a Nelson-Oppen framework: each theory solver handles its own literals, and the combination is sound and complete for disjoint theories. The DPLL(T) architecture extends CDCL with theory propagation: the SAT solver reasons about Boolean structure while theory solvers check consistency of the current assignment against background theories.

In practice, specifications are written in domain-specific languages built atop these logical foundations. The **Z notation** (Spivey, 1989) uses Zermelo-Fraenkel set theory and schema calculus to specify state-based systems. **Alloy** (Jackson, 2002) uses a relational first-order logic with transitive closure, analysable via SAT solving. **TLA+** (Lamport, 1999) specifies concurrent and distributed systems in a temporal logic of actions. **Dafny** (Leino, 2010) embeds verification conditions directly in an imperative programming language. Each of these represents a different point in the design space between expressiveness and automation.

**Required Reading:**
- Huth & Ryan, *Logic in Computer Science: Modelling and Reasoning about Systems* (2nd ed., 2004/2040), chs. 1–2
- Kroening & Strichman, *Decision Procedures: An Algorithmic Point of View* (2nd ed., 2016/2040), chs. 1–3
- de Moura & Bjørner, "Z3: An Efficient SMT Solver," *TACAS '08* (2008): 337–340
- Barrett et al., "CVC5: A Versatile and Industrial-Strength SMT Solver," *CAV '22* (2022)

**Discussion Questions:**
1. SAT solving is NP-complete in theory but fast in practice. What properties of real-world instances explain this gap? Is it a coincidence or a deep structural fact about the problems we care about?
2. First-order logic is semi-decidable: we can find proofs of valid formulas but cannot always refute invalid ones. How do proof assistants like Coq work around this fundamental limitation?
3. If SAT solvers are already practical for million-variable instances, why do we need richer logics like LTL, CTL, or dependent types? What can they express that SAT cannot?

---

## Lecture 3: Temporal Logic — Reasoning About Time and Change

Programs are not static objects — they execute over time, and their correctness often depends on the *sequence* of states they traverse. A sorting algorithm is correct if it *eventually* produces a sorted array; a mutual exclusion algorithm is correct if it *never* allows two processes in the critical section simultaneously; a liveness property guarantees that something *eventually* happens. Classical logic, which reasons about truth at a single point, cannot express these properties directly. **Temporal logic** extends classical logic with operators that quantify over time: ◇φ (eventually φ), □φ (always φ), ○φ (next φ), φ U ψ (φ until ψ).

**Linear Temporal Logic** (LTL, Pnueli, 1977) interprets formulas over infinite sequences of states (traces). Each state assigns truth values to atomic propositions, and the temporal operators quantify over positions in the trace: □p means p holds at every position; ◇p means p holds at some future position; ○p means p holds at the next position; p U q means p holds at every position before q first holds, and q eventually holds. The **expansion laws** provide the semantic recursion: □φ ≡ φ ∧ ○□φ (always means now and forever next); ◇φ ≡ φ ∨ ○◇φ (eventually means now or sometime next); φ U ψ ≡ ψ ∨ (φ ∧ ○(φ U ψ)). These laws underpin both the intuition and the automata-theoretic verification of LTL.

**Computation Tree Logic** (CTL, Clarke & Emerson, 1981) interprets formulas over branching-time structures — Kripke frames representing all possible executions from a given initial state. CTL quantifies over paths with path quantifiers A (for all paths) and E (there exists a path), paired with temporal operators. AFp means "on all paths, p eventually holds"; EGp means "there exists a path on which p holds globally." The eight basic CTL operators — AX, EX, AF, EF, AG, EG, AU, EU — provide different kinds of branching-time quantification. CTL is strictly less expressive than LTL: CTL cannot express "p holds at every even step" (a property LTL expresses trivially as G(p → X(X(p)))), while LTL cannot express "there exists a path on which p holds forever" (which CTL expresses as EGp). The combination **CTL*** subsumes both, allowing arbitrary nesting of path quantifiers and temporal operators. CTL* model checking is PSPACE-complete; LTL model checking is also PSPACE-complete; CTL model checking is in P — a practically significant gap.

The relationship between LTL and CTL is subtle. A property expressible in both (e.g., □p ≡ AGp when interpreted on a single structure) may have different model-checking procedures. CTL model checking iterates a fixpoint computation: AFp is computed as the least fixpoint of the operator Z ↦ p ∨ AX(Z), which converges in at most |S| iterations where |S| is the number of states. LTL model checking proceeds via the automata-theoretic approach: given an LTL formula φ, construct a Büchi automaton A_¬φ that accepts precisely the traces violating φ, then check whether the product of the system model M with A_¬φ has an accepting run. If it does, the run is a counterexample; if not, φ holds. The Büchi automaton for an LTL formula φ has size exponential in |φ| in the worst case (the liveness to safety reduction introduces an exponential blowup), which is the source of PSPACE-completeness.

**ACTL** (Action-based CTL) and **undoability logic** extend CTL with action labels, enabling specifications like "every request is eventually followed by a response along the same path." **Metric temporal logic** (MTL) adds time bounds: ◇[0,5]p means "p holds within 5 time units." **Alternating-time temporal logic** (ATL, Alur et al., 2002) reasons about strategic ability: ⟨⟨1⟩⟩◇p means "agent 1 has a strategy to ensure p eventually holds, regardless of what other agents do." ATL is natural for multi-agent systems, security games, and contract-based specification — and it connects directly to model checking of security protocols, a major application at Yggdrasil's security lab.

The practical impact of temporal logic extends well beyond academic verification. In 2040, TLA+ is used at Amazon Web Services to specify and verify distributed consensus protocols (Raft, Paxos variants). The SPIN model checker verified the plan-switching logic of the Mars Curiosity rover. The NuSMV model checker is embedded in the European Train Control System specification. The Yggdrasil verification team uses temporal logic to specify liveness and safety properties for the Mimir Cluster's job scheduling system, ensuring that every submitted verification task eventually completes (◇(task_done)) and that no two tasks access the same resource simultaneously (□¬(access₁ ∧ access₂)).

**Required Reading:**
- Pnueli, "The Temporal Logic of Programs," *FOCS '77* (1977): 46–57
- Clarke, Emerson & Sistla, "Automatic Verification of Finite-State Concurrent Systems Using Temporal Logic Specifications," *ACM TOPLAS* 8:2 (1986): 244–263
- Baier & Katoen, *Principles of Model Checking* (MIT Press, 2008/2040), chs. 5–6
- Alur et al., "Alternating-Time Temporal Logic," *Journal of the ACM* 49:5 (2002): 672–713

**Discussion Questions:**
1. LTL and CTL are incomparable in expressiveness. Give an example of a property expressible in LTL but not CTL, and vice versa. Which is more natural for specifying concurrent protocols?
2. Model checkers produce counterexamples when properties fail. How do you validate that a counterexample represents a real bug rather than a modelling error?
3. The automata-theoretic approach to LTL model checking constructs an exponential-sized Büchi automaton. Why is this acceptable in practice? What techniques mitigate the worst case?

---

## Lecture 4: Model Checking — Algorithms, Data Structures, and the State Explosion Problem

Model checking is the automatic verification that a finite-state model M satisfies a temporal-logic specification φ, written M ⊨ φ. The core algorithm depends on the logic. For CTL, the algorithm computes the set of states satisfying each subformula bottom-up, using fixpoint characterisations: AGφ is the greatest fixpoint of Z ↦ φ ∧ AX(Z), AFφ is the least fixpoint of Z ↦ φ ∨ AX(Z). Each fixpoint iteration requires at most |S| steps, and there are |φ| subformulas, so the overall complexity is O(|M| × |φ|) — polynomial in both model and specification size.

For LTL, the automata-theoretic approach constructs the Büchi automaton A_¬φ for the negation of the specification, then checks whether the language of the product automaton M × A_¬φ is empty. Emptiness is equivalent to the non-existence of an accepting run, which is checked via nested depth-first search or SCC (strongly connected component) decomposition. The Büchi automaton for an LTL formula φ can be exponentially smaller than for the equivalent CTL* formula, but its construction is exponential in |φ|. The overall complexity is O(|M| × 2^|φ|), which is EXPTIME in the specification and linear in the model — acceptable because specifications are typically small while models are large.

The **state explosion problem** is the central challenge of model checking. A system with n Boolean variables has 2^n reachable states; a system with k concurrent processes, each with m local states, has up to m^k global states. Even moderate systems easily exceed 10^20 states, far beyond the reach of explicit-state enumeration. Three families of techniques address this.

**Symbolic model checking** (BDD-based, McMillan, 1993) represents state sets as Boolean functions rather than explicit enumeration. **Ordered Binary Decision Diagrams** (BDDs, Bryant, 1986) compactly represent Boolean functions as directed acyclic graphs with canonical form and efficient operations (conjunction, disjunction, negation, existential quantification). The transition relation is represented as a BDD, and the fixpoint computation operates on BDDs rather than explicit state sets. Symbolic model checking can handle systems with 10^20 reachable states if their transition relation has a compact BDD representation — which many realistic systems do, because the transition relation is typically a conjunction of local constraints. The canonical example is the 64-bit counter, whose 2^64 states are represented by a small BDD.

**Partial order reduction** (POR, Godefroid, 1996; Valmari, 1991) exploits the independence of concurrent transitions. Two transitions α and β are independent if they can execute in either order with the same result; the reduced state space need explore only one interleaving per independent set. POR preserves stutter-equivalence (for LTL without the next operator) and can reduce the state space by orders of magnitude for highly concurrent systems. Stubborn sets, ample sets, and sleep sets are the main POR algorithms, each with different precision-efficiency tradeoffs.

**Abstraction and counterexample-guided abstraction refinement** (CEGAR, Clarke et al., 2000) attack systems too large even for symbolic methods. The idea: construct an over-approximation Â of the concrete model A, model check Â, and if Â ⊨ φ, conclude A ⊨ φ (sound). If Â ⊭ φ, analyse the counterexample: if it is spurious (infeasible in the concrete model), refine the abstraction to eliminate it and repeat. CEGAR converges because each refinement strictly increases the precision of the abstraction, and there are finitely many predicates to add. The **Predicate abstraction** variant (Graf & Saïdi, 1997) tracks only the truth values of a set of predicates, reducing the abstract state space to 2^|P|. The SLAM tool (Microsoft, 2004) used CEGAR with predicate abstraction to verify device drivers; the BLAST tool (Henzinger et al., 2003) extended it with lazy predicate abstraction.

The Mimir Verification Cluster at Yggdrasil runs NuSMV (symbolic, BDD-based and SAT-based bounded model checking), SPIN (explicit-state with POR), and CBMC (bounded model checking for C programs). A typical verification workflow: specify the system in the modelling language, encode properties in temporal logic, run the model checker, and if a counterexample appears, trace it back to the model, confirm it is genuine, and either fix the model or refine the specification. If the checker says the property holds, the result is mathematically guaranteed — within the model. The gap between model and reality is where formal methods meets engineering judgement.

**Required Reading:**
- Clarke et al., *Model Checking* (2nd ed., MIT Press, 2018/2040), chs. 1–4
- McMillan, *Symbolic Model Checking* (Kluwer, 1993)
- Clarke et al., "Counterexample-Guided Abstraction Refinement," *CAV '00* (2000): 154–169
- Bryant, "Graph-Based Algorithms for Boolean Function Manipulation," *IEEE Trans. Computers* 35:8 (1986): 677–691

**Discussion Questions:**
1. Symbolic model checking with BDDs can handle 2^100 states, yet some systems still exceed its capacity. What properties of a system make BDDs blow up, and how can you detect this before investing verification effort?
2. CEGAR refines abstractions when counterexamples are spurious. What happens when the counterexample is genuine — does the refinement loop terminate? Under what conditions?
3. Model checking verifies properties of a model, not of the system itself. How do you bridge this gap? What assurance does model checking provide that testing does not?

---

## Lecture 5: The Simply-Typed Lambda Calculus — Types as Simple Specifications

The **lambda calculus** (Church, 1936) is the atomic theory of computation: a formal system with three constructs — variable reference x, function definition λx.M, and function application M N — that is Turing-complete. Its operational semantics is β-reduction: (λx.M) N → M[x := N]. The untyped lambda calculus admits self-application (ω = λx.x x) and non-terminating computation (Ω = ω ω), making it logically inconsistent as a proof system (by Curry's paradox, a term that reduces to itself encodes a circular proof).

The **simply-typed lambda calculus** (STLC, Church, 1940; Curry & Feys, 1958) restricts the untyped calculus by assigning simple types to terms. Types are built from base types (ι, ο, ...) and the arrow constructor: if A and B are types, so is A → B. A term λx:A. Mx. is a function from A to B. The typing judgement Γ ⊢ t : A reads "in context Γ, term t has type A." The typing rules are:

- **Var:** Γ, x:A ⊢ x : A (variables are looked up in the context)
- **Abs:** If Γ, x:A ⊢ M : B, then Γ ⊢ λx:A. M : A → B (abstraction introduces an arrow type)
- **App:** If Γ ⊢ M : A → B and Γ ⊢ N : A, then Γ ⊢ M N : B (application eliminates an arrow type)

STLC satisfies two fundamental properties. **Type safety** (progress + preservation): well-typed terms never get stuck — they either reduce or are values. **Strong normalisation**: every well-typed term terminates — there are no infinite reduction sequences. Strong normalisation follows because every β-reduction decreases the type complexity (specifically, the number of arrows in the types of subterms). This means STLC is *not* Turing-complete; it is a language of total functions — exactly what we want for verification, where non-termination is a bug, not a feature.

The **Curry-Howard correspondence** for STLC maps types to propositions of intuitionistic propositional logic and terms to proofs. A → B corresponds to implication; A × B to conjunction; A + B to disjunction. The typing derivation Γ ⊢ t : A is read as "t is a proof that the proposition A follows from assumptions Γ." **Proof normalisation** corresponds to β-reduction: simplifying a proof corresponds to evaluating a program. This correspondence is not merely analogical — it is a mathematical isomorphism. The algorithm for extracting the computational content of a proof (removing "detours" where an implication is introduced and immediately eliminated) is exactly β-reduction. This is the insight that makes type-theoretic verification possible: if we can express specifications as types, then verifying a program is the same as type-checking it.

**Principal types** and **type inference** (Hindley, 1969; Milner, 1978; Damas & Milner, 1982) extend STLC with polymorphism. The Hindley-Milner type system (Algorithm W) infers the most general (principal) type of a term without any type annotations. The key insight: unify type variables across the term, then generalise over variables that appear only in the type (not in the context). ML-family languages (Standard ML, OCaml, Haskell without extensions) use this system. Type inference makes it practical to write programs that the compiler verifies without programmer-supplied annotations — a major engineering advantage.

**Subtyping** (Cardelli, 1984) extends STLC with a subtype relation A ≤ B (read "A is a subtype of B," meaning any term of type A can be used where a term of type B is expected). Subtyping on record types models object-oriented inheritance; subtyping on function types is contravariant in the argument and covariant in the result: if A' ≤ A and B ≤ B', then A → B ≤ A' → B'. This seemingly simple extension introduces significant complexity: subtyping with bounded quantification (F<:) is undecidable (Pierce, 1994), and even without quantifiers, subtyping on recursive types requires coinductive definitions. The practical lesson: every addition to the type system must be justified against the decidability and tractability of type inference.

**Required Reading:**
- Pierce, *Types and Programming Languages* (MIT Press, 2002/2040), chs. 9–12 (STLC), chs. 22–23 (subtyping)
- Girard, Lafont & Taylor, *Proofs and Types* (Cambridge UP, 1989), chs. 1–4
- Barendregt, "Lambda Calculi with Types," *Handbook of Logic in Computer Science* vol. 2 (1992): 117–309
- Wadler, "Propositions as Types," *Communications of the ACM* 58:12 (2015): 75–84

**Discussion Questions:**
1. STLC is not Turing-complete. Is this a bug or a feature? In what circumstances would you prefer a total language over a Turing-complete one?
2. Type inference is undecidable for sufficiently rich type systems (e.g., System F with subtyping). At what point does the cost of type annotations outweigh the benefit of verification?
3. The Curry-Howard correspondence maps STLC to intuitionistic propositional logic. What logic corresponds to the untyped lambda calculus, and why is it inconsistent?

---

## Lecture 6: Dependent Types — Propositions as Types, Programs as Proofs

The simply-typed lambda calculus can express implication and conjunction. **Dependent types** extend this to full first-order logic and beyond, allowing types to depend on values. A dependent function type Π(x:A). B(x) — read "for all x of type A, B(x)" — is both a universal quantifier (in the logical reading) and a dependent function type (in the computational reading). A dependent pair type Σ(x:A). B(x) — read "there exists x of type A such that B(x)" — is both an existential quantifier and a dependent record. This is the Curry-Howard correspondence in full generality: types are propositions, terms are proofs, and the type checker is the proof checker.

**Dependent function types** (Π-types) generalise arrow types. Where A → B bundles a function that takes any A and returns a B, Π(x:A). B(x) allows the return type to depend on the specific argument value. The classic example: the type of length-indexed vectors Vec A n, where n is a natural number. The cons function has type Π(n:ℕ). A → Vec A n → Vec A (n+1) — the output vector's length is one more than the input's, and this is enforced by the type system. A function that appends vectors has type Π(m n:ℕ). Vec A m → Vec A n → Vec A (m+n) — the result's length is the sum of the arguments' lengths, verified by the type checker. This is verification by construction: the well-typedness of the program *proves* the length property.

**Dependent pair types** (Σ-types) generalise product types. Where A × B bundles a value of type A with a value of type B, Σ(x:A). B(x) bundles a value x of type A with a proof that B(x) holds. A sorted list is Σ(l:List A). IsSorted(l) — a list together with a proof of sortedness. A verified search function returns Σ(i:ℕ). (i < length l) × (l[i] = target) — the index together with proofs that it is in bounds and points to the target. Each of these is both a data structure and a specification, intertwined at the type level.

The **calculus of inductive constructions** (CIC, Coquand & Huet, 1988) is the type theory underlying Coq. CIC extends the calculus of constructions (Coquand, 1985) with inductive types — strictly positive datatypes with associated recursion and induction principles. Inductive types are defined by their introduction rules (constructors) and their elimination rules (recursors / pattern matching). The natural numbers Nat is defined by two constructors: O : Nat and S : Nat → Nat. Lists are defined by nil : List A and cons : A → List A → List A. The associated induction principle for Nat is Π(P : Nat → Prop). P O → (Π(n:Nat). P n → P (S n)) → Π(n:Nat). P n — the familiar principle of mathematical induction, arising automatically from the inductive definition.

**Universe levels** address Girard's paradox (the type-theoretic analogue of Russell's paradox). If we had Type : Type (the type of all types is a type), we could encode an inconsistent system. Instead, CIP has a tower of universes: Type₀ : Type₁ : Type₂ : ..., where Typeᵢ is the type of types of level at most i. A term of type Typeᵢ is a type (or proposition) in universe i; terms of type Typeᵢ are themselves classified by Typeᵢ₊₁. This stratification is invisible in practice (most programming happens in Type₀ and Type₁) but essential for consistency.

**Lean 4** (de Moura et al., 2021) is a dependent-type proof assistant and programming language built on the calculus of inductive constructions with quotient inductive types and a procedural tactic language. Lean 4 compiles to efficient C code, supports metaprogramming via monadic tactics, and integrates with VS Code via the Lean Language Server. Its key innovation for verification practice is the **mathlib** library: over 1.5 million lines of verified mathematics, from category theory to analysis to combinatorics. When verifying a program property, one can leverage lemmas from mathlib rather than proving everything from scratch. Yggdrasil's verification courses use Lean 4 from 2039 onward, in preference to Coq, for this reason: the tooling is more polished, the metaprogramming story is cleaner, and mathlib provides unparalleled mathematical infrastructure.

**Required Reading:**
- The Coq Development Team, *The Coq Reference Manual* (2024), chs. 1–4
- Avigad, de Moura & Roesner, *Theorem Proving in Lean 4* (2024/2040), chs. 1–4
- Norell, "Dependently Typed Programming in Agda," *AFP '08* (2008)
- Coquand & Huet, "The Calculus of Constructions," *Information and Computation* 76:2–3 (1988): 95–120

**Discussion Questions:**
1. In a dependently-typed language, types can depend on values. What are the practical implications for type inference? Can we infer dependent types, or must they always be annotated?
2. Girard's paradox shows that Type : Type is inconsistent. But Python and JavaScript have a "top type" (object or any). Why doesn't this cause inconsistency in those languages?
3. mathlib in Lean has over 1.5 million lines of verified mathematics. Does it make sense to call a library "verified" when it depends on a kernel that might have bugs? What is the trust base of a proof assistant?

---

## Lecture 7: Proof Assistants — Constructing Machine-Checked Proofs

A **proof assistant** is an interactive environment for constructing formal proofs that are mechanically verified by a small, trusted kernel. The kernel implements the type-checking rules of the underlying type theory (CIC for Coq, CIC + quotients for Lean 4); every proof ultimately reduces to a term that the kernel type-checks. This architecture limits the **trust base** — the code that must be correct for the proof to be valid — to a few thousand lines. Coq's kernel is approximately 15,000 lines of OCaml; Lean 4's kernel is approximately 5,000 lines of C++. The rest of the system — tactic engines, automation, libraries — can contain bugs without affecting proof validity, because the kernel re-checks every proof term.

**Tactics** are the primary interface for constructing proofs in Coq and Lean. Rather than writing proof terms directly (which is tedious and error-prone for large proofs), the user issues *tactical commands* that manipulate proof obligations. A proof in Lean 4:

```lean
theorem add_comm : ∀ (n m : ℕ), n + m = m + n := by
  intro n m
  induction n with
  | zero => simp [Nat.zero_add]
  | succ n ih => simp [Nat.succ_add, ih]
```

The `by` keyword enters tactic mode. `intro` introduces hypotheses. `induction` performs structural induction. `simp` applies a set of equational lemmas automatically. The tactic engine constructs a proof term behind the scenes; the kernel then verifies it. If the kernel accepts, the theorem is proved — regardless of any bugs in the tactic engine, the simplifier, or any other automation.

The **tactic language** in Lean 4 is a monadic term language with backtracking (via `alternative`), state management, and reflection. Custom tactics are programs that manipulate the proof state, and they can be written in Lean itself (unlike Coq's Ltac, which is a separate DSL). This metaprogramming capability has led to powerful automation: `linarith` (linear arithmetic), `ring` (ring equalities), `omega` (Presburger arithmetic), `aesop` (best-first search), `cvodd` (decision procedure for bitvectors). The key insight: tactics are programs that construct proofs; the kernel verifies the result; this separation of concerns allows aggressive automation without sacrificing soundness.

**Refinement** (top-down proof construction) and **synthesis** (bottom-up proof construction) are the two modes. In refinement, the user states a goal (the desired theorem) and issues tactics that progressively decompose it into subgoals. In synthesis, the user provides a term and the type checker verifies it. In practice, most proofs interleave both: high-level structure is specified by tactics, and low-level details are filled in by automation. The **proof engineering** challenge is managing proof brittleness — proofs that break when the definitions they depend on change. Robust proofs use abstract lemmas and interface specifications rather than implementation details, following the same design principles as modular software.

**Extraction** translates verified proof assistants into executable code. Coq can extract OCaml, Haskell, and Scheme from verified developments; Lean 4 compiles directly to C. The extraction removes proof terms (which are computationally irrelevant) and produces efficient code. The CompCert verified C compiler (Leroy, 2009) is the landmark example: 100,000+ lines of Coq specify and verify a C compiler, from parsing through optimisation to code generation. Each optimisation pass is proved to preserve semantics; the compiler as a whole is proved correct (for a subset of C, with well-defined undefined-behaviour treatment). CompCert proved that formal verification of production-scale software is achievable — it is used commercially by AbsInt and has been integrated into the Yggdrasil verification toolchain since 2037.

**Proof relevance vs. proof irrelevance** is a crucial design choice. In Coq, proofs are first-class terms — you can compute with them, pattern-match on them, and prove that two proofs of the same proposition are different. In Lean 4, propositions live in `Prop` (proof-irrelevant: any two proofs of the same proposition are definitionally equal) and data live in `Type` (proof-relevant). This design prevents accidental dependency on proof terms (which can change without affecting the computational result), while still allowing proof-relevant types when needed (e.g., in verified algorithms that use proof terms as certificates). The distinction between Prop and Type is the single most common source of confusion for students transitioning from Coq to Lean or vice versa.

**Required Reading:**
- Leroy, "Formal Verification of a Realistic Compiler," *CACM* 52:7 (2009): 107–115
- Avigad, de Moura & Roesner, *Theorem Proving in Lean 4* (2024/2040), chs. 5–7
- The Coq Development Team, *The Coq Reference Manual* (2024), "Proof Handling" and "Tactics"
- Carneiro, "Lean 4: A Programming Language and Theorem Prover," *Lean Together '22* (2022)

**Discussion Questions:**
1. The kernel of a proof assistant is the trusted computing base — if it has a bug, all proofs are potentially invalid. How do you increase confidence in the kernel without reducing productivity?
2. CompCert is verified but only for a subset of C. What is the value of verifying a subset, and how do you handle the gap between the verified subset and the full language?
3. Proof scripts are brittle — small changes to definitions can break large proofs. What design principles make proofs more robust?

---

## Lecture 8: Model Checking in Practice — SPIN, NuSMV, and the Verification Workflow

SPIN (Simple PROMELA INterpreter, Holzmann, 1991–2004) is a model checker for asynchronous concurrent systems. Its input language, **PROMELA** (Process Meta-Language), specifies communicating finite-state machines as concurrent processes with message channels (FIFO or rendezvous), shared variables, and non-deterministic guards. A PROMELA model of a client-server protocol:

```promela
mtype = { request, response }
chan service = [2] of { mtype, byte };

active proctype Client() {
  byte id;
  do
  :: id = (id + 1) % 256;
     service ! request, id;
     service ? response, id
  od
}

active proctype Server() {
  byte req_id;
  do
  :: service ? request, req_id;
     service ! response, req_id
  od
}
```

SPIN verifies properties expressed in LTL (never claims, always claims) and basic CTL. It supports both depth-first search (DFS) for exhaustive verification and nested DFS for liveness checking (acceptance cycles that violate ◇p). The partial order reduction algorithm (stubborn sets) reduces the state space by exploring only one interleaving per independent transition set. When a property is violated, SPIN produces a concrete counterexample trace that can be replayed step by step. Yggdrasil's concurrency lab uses SPIN to verify mutual exclusion protocols, leader election algorithms, and the Two-Phase Commit protocol for distributed transactions.

**NuSMV** (Cimatti et al., 2002) is a symbolic model checker supporting both BDD-based and SAT-based model checking. Its input language specifies finite-state machines as sets of mutually recursive variable assignments. The NuSMV model of a 3-bit counter with overflow detection:

```
MODULE main
  VAR
    bit0 : boolean;
    bit1 : boolean;
    bit2 : boolean;
  ASSIGN
    init(bit0) := FALSE;
    init(bit1) := FALSE;
    init(bit2) := FALSE;
    next(bit0) := !bit0;
    next(bit1) := bit0 XOR bit1;
    next(bit2) := (bit0 & bit1) XOR bit2;
  LTLSPEC
    F (bit0 & bit1 & bit2)   -- "eventually, all bits are 1"
  CTLSPEC
    AG EF (bit0 & !bit1 & !bit2)   -- "for all states, it is possible to reach state 001"
```

NuSMV's symbolic engine represents the transition relation as a BDD and computes fixpoints symbolically. Its bounded model checking (BMC) engine encodes the transition relation and property as a SAT formula; if the property is violated within k steps, the SAT solver finds a satisfying assignment that is the counterexample. BMC is incomplete (it only checks up to k steps) but scales to much larger models by leveraging the power of SAT solvers. A typical workflow: run BMC for increasing k until resources are exhausted; if no counterexample is found, switch to BDD-based model checking for completeness. The nuXmv extension (2014) adds SMT-based infinite-state model checking and IC3/PDR (property-directed reachability) for safety properties.

**CBMC** (C Bounded Model Checker, Clarke et al., 2004) verifies C and C++ programs directly, without manual modelling. It unwinds loops and recursion up to a bound, encodes the resulting straight-line program as a SAT/SMT formula, and checks for assertions, array bounds violations, pointer safety, and integer overflow. CBMC is the most practical verification tool for working programmers: it requires no special modelling language, runs on production C code with minimal annotation, and produces clear counterexample traces. Its limitations are bounded loops (it cannot verify that a loop terminates, only that it is safe for the bound) and the state-space explosion for programs with many variables. Yggdrasil's systems programming students use CBMC to verify memory safety and assertion correctness in C assignments.

The **verification workflow** in practice follows a disciplined cycle: (1) Model the system in a suitable formalism (PROMELA, NuSMV, or directly in the programming language). (2) Specify properties in temporal logic (LTL for linear-time properties, CTL for branching-time properties). (3) Run the model checker. (4) If a counterexample is produced: (a) validate it on the model (is the trace feasible?), (b) confirm it corresponds to a real bug in the system (is the model accurate?), (c) fix the bug and re-verify. (5) If no counterexample is produced: (a) check resource limits (was the analysis exhaustive?), (b) increase the bound (for BMC) or provide more predicates (for CEGAR), (c) if truly exhaustive, the property is verified. (6) Repeat with additional properties.

The counterexample validation step is crucial and often overlooked. A spurious counterexample — one that is feasible in the abstract model but not in the concrete system — indicates a modelling error or an imprecise abstraction. CEGAR addresses this automatically, but manual modelling requires manual validation. At Yggdrasil, we teach students always to trace counterexamples back to the original specification, not just the model: a bug in the specification is as dangerous as a bug in the implementation, and the model checker cannot tell the difference.

**Required Reading:**
- Holzmann, *The SPIN Model Checker: Primer and Reference Manual* (Addison-Wesley, 2003/2040)
- Cimatti et al., "NuSMV 2: An Open-Source Tool for Symbolic Model Checking," *CAV '02* (2002): 359–364
- Kroening & Torel, "CBMC: C Bounded Model Checker," *TACAS '14* (2014)
- Clarke et al., "A Tool for Checking ANSI-C Programs," *TACAS '04* (2004): 168–176

**Discussion Questions:**
1. SPIN uses explicit-state verification while NuSMV uses symbolic (BDD-based) verification. For what classes of systems is each approach superior? Can you predict which will perform better before running both?
2. CBMC can only verify bounded programs. In what sense is this verification, and how does it compare in assurance level to unbounded verification?
3. A counterexample from a model checker may reveal a bug in the model, not the system. How do you distinguish modelling errors from genuine system bugs?

---

## Lecture 9: Program Logics — Hoare Logic, Separation Logic, and Verification Conditions

**Hoare logic** (Hoare, 1969) is the foundational framework for verifying imperative programs. The Hoare triple {P} C {Q} states: if the precondition P holds and command C terminates, then the postcondition Q holds. The assignment axiom {P[E/x]} x := E {P} captures the essence of assignment: to prove a postcondition P after assigning E to x, prove P with x replaced by E before the assignment. The sequencing rule {P} C₁ {R} ∧ {R} C₂ {Q} ⟹ {P} C₁;C₂ {Q} introduces an intermediate assertion R. The conditional rule {P ∧ b} C₁ {Q} ∧ {P ∧ ¬b} C₂ {Q} ⟹ {P} if b then C₁ else C₂ {Q} splits on the condition. The loop rule {P ∧ b} C {P} ⟹ {P} while b do C {P ∧ ¬b} requires a loop invariant P that is preserved by the body and, combined with the negated condition, implies the desired postcondition.

Hoare logic is *partial* by default: it says nothing about non-terminating programs. **Total correctness** Hoare logic adds a termination proof: [P] C [Q] means "if P holds, C terminates and Q holds." Proving termination requires a variant (well-founded measure) that strictly decreases on each iteration. For the simple loop while i < n do i := i + 1, the variant i is natural-number-valued and bounded below by n, so termination follows from the well-foundedness of < on ℕ. For complex loops, finding the variant can be as hard as finding the program itself.

**Weakest preconditions** (Dijkstra, 1975) provide a calculational approach. wp(C, Q) is the weakest assertion P such that {P} C {Q} holds. For assignment: wp(x := E, Q) = Q[E/x]. For sequence: wp(C₁;C₂, Q) = wp(C₁, wp(C₂, Q)). For conditional: wp(if b then C₁ else C₂, Q) = (b ∧ wp(C₁, Q)) ∨ (¬b ∧ wp(C₂, Q)). For loops, wp(while b do C, Q) is the least fixed point of the equation P = (¬b ∧ Q) ∨ (b ∧ wp(C, P)), which exists because the predicate transformer is monotone and continuous. Weakest preconditions turn verification from backward reasoning (finding a precondition that works) into forward calculation (computing the weakest precondition and checking that it is implied by the given precondition). This is more amenable to automation.

**Verification condition generation** (VCGen) is the engine that drives automatic verification. Given a program annotated with preconditions, postconditions, and loop invariants, VCGen produces a set of verification conditions (VCs) — mathematical formulas whose validity implies the correctness of the program. The key VCs are: (1) the invariant is established on loop entry, (2) the invariant is preserved by the loop body, (3) the invariant and exit condition imply the postcondition, and (4) all array accesses are in bounds. These VCs are discharged by SMT solvers (Z3, CVC5) or sent to interactive proof assistants when the solver times out. Yggdrasil's VCGen produces Lean 4 obligations that students can prove interactively when the solver cannot.

**Separation logic** (Reynolds, 2002; O'Hearn & Ishtiaq, 2001) extends Hoare logic to reason about pointer programs with mutable state. The key connective is the **separating conjunction** P * Q, which asserts that the heap can be split into two disjoint parts, one satisfying P and the other Q. The Hoare triple {P} C {Q} in separation logic guarantees that C only accesses the heap described by P (the **footprint** of C) — the **frame rule** {P} C {Q} ⟹ {P * R} C {Q * R} allows local reasoning: provably, C does not affect any heap outside its footprint. This is a radical departure from classical Hoare logic, where every assertion implicitly quantifies over the entire heap. Separation logic makes modular reasoning about pointer programs tractable.

The **frame rule** is the central innovation. In classical Hoare logic, verifying a procedure requires specifying its effect on *every* heap cell, even those it does not touch. In separation logic, specifying the footprint suffices — the frame rule discharges the rest automatically. For a procedure that swaps two integers: {p ↦ v * q ↦ w} swap(p, q) {p ↦ w * q ↦ v}. The specification mentions only the two cells p and q; the frame rule guarantees that no other cell is affected. This is not just convenient — it is essential for scaling verification to large programs.

**Concurrent separation logic** (CSL, O'Hearn, 2004; Brodsky & O'Hearn, 2016) extends the frame rule to concurrent programs with the **parallel composition rule**: {P} C₁ {Q} ∧ {R} C₂ {S} ⟹ {P * R} C₁ || C₂ {Q * S}. The separating conjunction in the precondition guarantees that C₁ and C₂ access disjoint regions of the heap, and therefore cannot interfere. The **critical region rule** allows shared mutable state protected by locks, with the invariant transferred between the lock and the thread that holds it. **Iris** (Jung et al., 2015–2023) is the state of the art in concurrent separation logic, providing a higher-order, impredicative, step-indexed logical relation that supports reasoning about higher-order state, concurrency, and laziness. Iris has been mechanised in Coq and Lean 4 and is used for verifying optimising compilers, concurrent data structures, and distributed systems protocols at Yggdrasil.

**Required Reading:**
- Hoare, "An Axiomatic Basis for Computer Programming," *CACM* 12:10 (1969): 576–580
- Reynolds, "Separation Logic: A Logic for Shared Mutable Data Structures," *LICS '02* (2002): 55–74
- O'Hearn, "Resources, Concurrency and Local Reasoning," *CONCUR '04* (2004): 49–67
- Jung et al., "Iris from the Ground Up: A Modular Foundation for Higher-Order Concurrent Separation Logic," *J. Functional Programming* 28 (2018): e20
- Dijkstra, *A Discipline of Programming* (Prentice-Hall, 1976/2040), chs. 1–4

**Discussion Questions:**
1. The frame rule in separation logic allows local reasoning about pointer programs. What assumptions does it make about the programming language (e.g., no pointer arithmetic, no dangling pointers)?
2. Hoare logic proves partial correctness; total correctness requires termination proofs. How do you prove termination of a loop with a non-obviously decreasing measure? Can this be automated?
3. Iris mechanises concurrent separation logic in Coq. What is the cost of mechanisation — how much effort does it add compared to paper-and-pencil proofs? When is the cost justified?

---

## Lecture 10: Type Systems and Program Correctness — Refinement Types, Liquid Types, and Gradual Verification

**Refinement types** (Freeman & Pfenning, 1991; Xi & Pfenning, 1998) enrich ordinary types with logical predicates that restrict the set of values inhabiting the type. The type {x : Int | x ≥ 0} is the type of non-negative integers — a refinement of Int with the predicate x ≥ 0. The type {x : List Int | length x = n} is the type of lists of length n (parameterised by n). Refinement types enable lightweight verification without leaving the programming language: the type checker verifies that every operation respects the refinements, and if it cannot, it rejects the program.

**Liquid types** (Rondon, Kawaguchi & Jhala, 2008; Vazou et al., 2014–2018) make refinement types practical by inferring the refinement predicates via **abstract interpretation** and **Horn clause solving**. Given a function with type signature but no annotations, Liquid Haskell or Liquid Fixpoint (the SMT-based inference engine) synthesises the weakest refinements that make the program type-check. The inference works by generating constraints: for each function application, the argument type must be a subtype of the parameter type; for each conditional branch, the guard refines the variable in each branch. These constraints are collected as Horn clauses and solved by fixed-point iteration over a predefined set of templates (k-satisfiable predicates). If the solver finds a solution, the program is verified; if not, the solver produces a type error with a counterexample.

The **liquid type** inference algorithm proceeds in four steps: (1) generate subtype constraints from the program's type signatures and control flow; (2) instantiate each constraint with a template of the form λv. c₁v₁ + ... + cₙvₙ + c₀, where the cᵢ are unknown integer coefficients; (3) solve the resulting system of linear constraints over the cᵢ using an SMT solver; (4) if all constraints are satisfied, the synthesised refinements are correct. The templates are parameterised by a qualification Q of relevant variables that can appear in the refinement — typically the function's parameters and global constants. The expressiveness of the inferred refinements is bounded by Q, which the user controls. This makes liquid types a sweet spot between annotation burden (too high for fully dependent types) and expressiveness (too low for simple type systems).

**Gradual verification** (Bader et al., 2019; Greenberg, 2024) applies the principles of gradual typing (Siek & Taha, 2006) to formal verification. In gradual typing, the type Any is compatible with every concrete type — a gradual guarantee ensures that removing annotations only reduces the static guarantees, never introducing new runtime errors. In gradual verification, the proposition Learned is compatible with every logical predicate — a verified function can call an unverified function by treating its postcondition as Learned (unknown but not violated), and an unverified function can call a verified function by treating verified invariants as assumed. The runtime enforcement uses **definite assignment checks** and **assertion checks** at verification boundaries, similar to how gradual typing uses casts at type boundaries.

The practical impact for working programmers is significant. **F*** (Swamy et al., 2016) is a verification-oriented language with refinement types, effects, and a weakest-precondition calculus that generates verification conditions for Z3. **Dafny** (Leino, 2010) is a verification-aware imperative language with built-in specifications, loop invariants, and SMT-based verification. **Frama-C** (Cuoq et al., 2012) verifies C programs using ACSL (ANSI/ISO C Specification Language) annotations. Each of these tools occupies a different point on the annotation burden / automation / expressiveness spectrum: F* is more expressive but requires more annotations; Dafny provides good defaults but less expressiveness; Frama-C targets legacy C code but requires significant specification effort.

At Yggdrasil, the verification pragmatism course (CS407) uses Liquid Haskell for functional verification and Dafny for imperative verification, teaching students to choose the right tool for the job. The key lesson: verification is not an all-or-nothing proposition. Partial verification (checking some properties) is orders of magnitude cheaper than full verification (checking all properties) and still provides significant assurance. The **verification grand challenge** (Hoare, 2003) called for a verified program of significant size; 20 years later, the community has produced verified compilers (CompCert), verified operating system kernels (seL4), verified cryptographic libraries (HACL*), and verified database systems. Each of these projects chose which properties to verify and which to assume, and each represents a pragmatic engineering decision about where to invest verification effort.

**Required Reading:**
- Xi & Pfenning, "Dependent Types in Practical Programming," *POPL '99* (1999): 214–227
- Rondon, Kawaguchi & Jhala, "Liquid Types," *PLDI '08* (2008): 159–169
- Vazou et al., "Liquid Haskell: Experience with Refinement Types in the Real World," * Haskell Symposium '18* (2018)
- Swamy et al., "F*: A Higher-Order Effectful Language Designed for Program Verification," *ESOP '22* (2022)
- Leino, "Accessible Software Verification with Dafny," *IEEE Software* 34:6 (2017): 94–97

**Discussion Questions:**
1. Liquid types infer refinements from a fixed template language. When does this template language become too restrictive? Give an example of a property that liquid types cannot express.
2. Gradual verification allows mixing verified and unverified code. What guarantees does it provide, and what are the failure modes? Is a partially verified program more trustworthy than an unverified one?
3. The verification grand challenge is 20+ years old. Are we closer to a "verified world" than we were in 2003? What has changed, and what hasn't?

---

## Lecture 11: Verification of Concurrent and Distributed Systems — Atomicity, Consensus, and Consistency

Concurrent and distributed systems are the hardest class of software to get right, and therefore the most important class to verify. The difficulty arises from **non-determinism**: concurrent processes interleave their executions in exponentially many ways, and the set of reachable states grows super-exponentially with the number of processes. A system with n processes, each with m local states, has up to mⁿ × n! interleavings (the factorial accounts for the ordering of local transitions within a global state). Testing covers a vanishingly small fraction of these; formal verification is the only viable approach.

**Linearisability** (Herlihy & Wing, 1990) is the standard correctness condition for concurrent data structures. A concurrent object is linearisable if every operation appears to take effect instantaneously at some point between its invocation and its response — the **linearisation point**. This means the concurrent execution is equivalent to some sequential execution respecting the real-time ordering of non-overlapping operations. Linearisability composes: if each object in a system is linearisable, the system as a whole is linearisable. This compositionality is essential for modular verification.

Proving linearisability requires: (1) identifying a linearisation point for each operation, (2) showing that the concurrent execution is equivalent to the sequential specification at that point, and (3) showing that the linearisation points respect the real-time order. For fine-grained lock-free data structures, the linearisation point may be a single CAS (compare-and-swap) instruction, and the proof must account for the possibility that intervening operations may read stale values. The Michael-Scott lock-free queue, the lock-free skip list, and RCU (read-copy-update) linked lists are landmark examples that have been mechanically verified in Iris.

The **consensus problem** (Fischer, Lynch & Paterson, 1985; Dwork, Lynch & Stockmeyer, 1988) asks: can n asynchronous processes agree on a value? The FLP impossibility result shows that deterministic consensus in an asynchronous system is impossible even with one faulty process. The proof constructs an infinite execution in which no process decides, by showing that any purportedly deciding configuration can be delayed (by an adversarial scheduler) to produce a new undecided configuration. This result is foundational: it explains why distributed consensus protocols (Paxos, Raft, PBFT) require either synchrony assumptions, randomisation, or failure detection.

**Paxos** (Lamport, 1998) solves consensus in an asynchronous system with crash failures, assuming a majority of processes remain connected (the quorum requirement). Each Paxos instance proceeds in two phases: Phase 1 (prepare/promise) ensures that no higher-numbered proposal exists; Phase 2 (accept/learn) commits the chosen value. The safety proof (no two processes decide different values) follows from the quorum intersection property: any two quorums share at least one process, and that process remembers the highest-numbered proposal it has seen. Paxos is famously difficult to understand; Lamport's "Part-Time Parliament" paper (1998) was initially rejected because reviewers found it too obscure. Lamport's later "Paxos Made Simple" (2001) provides a clearer exposition, but the protocol remains subtle enough that multiple verified implementations have found bugs in published pseudo-code.

**Raft** (Ongaro & Ousterhout, 2014) is designed for understandability: it decomposes consensus into leader election, log replication, and safety, each of which can be understood, implemented, and verified independently. The formal verification of Raft spans TLA+ specifications (checked with the TLC model checker), Isabelle/HOL proofs (by Peter van Roosmalen, 2017), and Coq proofs (by Doug Woos et al., 2016). Each verification found subtle bugs in the original Raft protocol and its implementations, confirming Dijkstra's dictum: testing can only find bugs in the places you thought to test; verification can find bugs in the places you didn't.

The **CAP theorem** (Brewer's conjecture, proved by Gilbert & Lynch, 2012) states that a distributed system can provide at most two of: Consistency (linearisability), Availability (every request receives a response, not an error), and Partition tolerance (the system continues to operate despite network partitions). Since partitions are inevitable in large-scale systems, the practical choice is between CP (consistent, unavailable during partitions) and AP (available, but potentially inconsistent). Yggdrasil's distributed systems course (CS407) uses TLA+ specifications to formalise and verify these tradeoffs.

**Required Reading:**
- Herlihy & Wing, "Linearizability: A Correctness Condition for Concurrent Objects," *ACM TOPLAS* 12:3 (1990): 463–492
- Lamport, "Paxos Made Simple," *ACM SIGACT News* 32:4 (2001): 18–25
- Ongaro & Ousterhout, "In Search of an Understandable Consensus Algorithm," *USENIX ATC '14* (2014): 305–319
- Jung et al., "Iris from the Ground Up," *J. Functional Programming* 28 (2018): e20
- Gilbert & Lynch, "Perspectives on the CAP Theorem," *IEEE Computer* 45:2 (2012): 30–36

**Discussion Questions:**
1. The FLP impossibility result shows that deterministic asynchronous consensus is impossible. How do real-world systems (Paxos, Raft, ZooKeeper) circumvent this result? What assumptions do they make?
2. Linearisability requires every operation to appear atomic. But many practical systems settle for weaker consistency models (sequential consistency, eventual consistency, causal consistency). When is linearisability necessary, and when can we accept weaker guarantees?
3. Raft was designed for understandability, yet its formal verification still found bugs. What does this tell us about the relationship between understandability and correctness?

---

## Lecture 12: The Verified Future — Proof Assistants in Practice, Industry, and Ethics

The landscape of verified software in 2040 looks very different from 2010. CompCert (verified C compiler), seL4 (verified operating system kernel), HACL* (verified cryptographic library), and Bedrock (verified database engine) have demonstrated that full functional correctness is achievable for production-scale systems. The seL4 verification (Klein et al., 2009–2014) is the most comprehensive to date: 200,000+ lines of Isabelle/HOL proofs verify functional correctness, security enforcement (integrity and confidentiality), and absence of crashes for a microkernel with 8,700 lines of C. The proofs cover the refinement from an abstract specification through intermediate designs to the concrete C implementation — a four-level refinement chain that guarantees every behaviour of the C code is permitted by the abstract specification.

The cost of verification is the elephant in the room. The seL4 verification took approximately 20 person-years, or roughly 25 lines of proof per line of code. CompCert required approximately 10 person-years. HACL* required approximately 5 person-years for a 30,000-line library. These costs are coming down as tooling improves, but they remain an order of magnitude higher than conventional development. The key question for the next decade is whether verification costs can approach development costs through automation — and the evidence from Liquid Types, SMT-based verification, and LLM-assisted theorem proving is cautiously optimistic.

**LLM-assisted theorem proving** has made significant strides since 2023. Models like AlphaProof (DeepMind, 2024), LeanDojo (Yang et al., 2023), and ReProver (Mathlib, 2038) use large language models to generate proof steps from natural-language sketches, search, and hammer tactics. These models are far from autonomous theorem provers — they hallucinate type errors and produce incorrect proof strategies — but they dramatically reduce the time to find the right lemma decomposition and tactic sequence. The Yggdrasil verification group's internal benchmark shows a 40% reduction in proof-writing time for routine lemmas when using LLM assistance, but a 0% reduction for novel or structurally complex proofs. The current sweet spot: use LLM assistance for "obvious but tedious" lemmas, and invest human effort in the novel insights that define the proof architecture.

**Verified AI and ML systems** are an emerging frontier. The HALO project (Yggdrasil, 2038) verifies the training pipeline of neural networks: data preprocessing, gradient computation, and weight update are each specified in Lean 4 and verified against the implementation. The result is not a proof that the trained model is correct (that depends on the data), but a proof that the training algorithm is correctly implemented — no silent data corruption, no numerical overflow, no dropout of gradients. Analogous efforts verify the inference pipeline: the compiled model correctly implements the trained weights. The challenge of verifying the model's *behaviour* (robustness, fairness, interpretability) remains open, though techniques from robust optimisation and formal verification of neural networks (complete verification via mixed-integer programming, incomplete verification via abstract interpretation) are advancing rapidly.

**Ethics of formal verification** raises questions that go beyond technical correctness. A verified system is correct *relative to its specification*. But who writes the specification, and whose interests does it serve? The Therac-25 specification stated that the electron beam energy must not exceed the treatment table's tolerance — but it did not specify what should happen when the operator makes an error in entering treatment parameters. The specification was verified; the human factors were not. seL4's specification guarantees that the kernel enforces the access control policy — but who sets the policy? A verified system can enforce an unjust policy just as rigorously as a just one. The ethics of verification is the ethics of specification: what we choose to verify reflects what we value, and what we omit reflects what we overlook.

The Yggdrasil approach to this problem is the **verification pledge**: every verified system, as a condition of its verification certificate, must include a document describing (1) what properties are verified, (2) what properties are assumed but not verified, and (3) what properties are deliberately excluded from the specification and why. This pledge does not make verification ethical; it makes the scope of verification transparent. The 2038 Reykjavik Protocol for autonomous vehicles requires this pledge for all safety-critical verification submissions. It is a small step, but an important one: it forces engineers and stakeholders to confront what they have chosen not to verify.

The future of formal methods in 2040 is not a world where all software is verified. It is a world where critical components — compilers, kernels, cryptographic libraries, consensus protocols, medical device controllers — are verified as a matter of course, where the cost of verification is amortised over the lifetime of the system, and where the verification infrastructure (proof assistants, SMT solvers, model checkers) is itself trusted because it has been scrutinised by thousands of eyes. The goal is not perfection; it is the *systematic reduction of the space of possible errors*. Formal methods compress that space from "whenever a human might make a mistake" to "whenever a specification might be wrong" — a smaller, more tractable, and more honest space.

**Required Reading:**
- Klein et al., "seL4: Formal Verification of an OS Kernel," *SOSP '09* (2009): 207–220
- Leroy, "Formal Verification of a Realistic Compiler," *CACM* 52:7 (2009): 107–115
- Zinzindohoué et al., "HACL*: A Verified Modern Cryptographic Library," *CCS '17* (2017): 1789–1806
- First et al., "Toward Verified AI," *CACM* 67:2 (2024): 46–55
- Hoare, "The Verifying Compiler: A Grand Challenge for Computing Research," *JACM* 50:1 (2003): 63–69

**Discussion Questions:**
1. seL4 required 20 person-years of verification effort. Is this a reasonable investment? At what scale does verification become cost-effective?
2. The verification pledge requires engineers to state what they have chosen not to verify. Is this sufficient to address the ethical concerns, or is it merely performative transparency?
3. LLM-assisted theorem proving reduces proof-writing time for routine lemmas but not for novel proofs. Will this change, or is novelty fundamentally outside the scope of statistical pattern matching?

---

## Final Examination Preparation

The final examination for CS208 consists of eight questions of which you must choose four. Each question requires a substantive essay (800–1200 words) demonstrating deep understanding of the course material. The examination is open-book but not open-internet; you may bring printed notes and the course textbook.

**Sample Examination Questions:**

1. "Formal methods can only verify that a system is correct with respect to its specification." Discuss the implications of this statement for the assurance provided by formal verification. Under what circumstances is a verified system trustworthy, and under what circumstances is it not? Draw on the Therac-25 and seL4 examples to illustrate your argument.

2. Compare and contrast model checking and theorem proving as verification paradigms. For each paradigm, describe: (a) the class of systems and properties it handles well, (b) its automation level and required human expertise, (c) a real-world application where it outperforms the other, and (d) a fundamental limitation that motivates the other paradigm.

3. Explain the Curry-Howard correspondence and its significance for program verification. How does it transform the relationship between programming and proving? Trace the correspondence from STLC (propositions as types) through dependent types (quantifiers as dependent function types) to proof assistants (verification by type checking).

4. The state explosion problem is the central challenge for model checking. Describe three techniques for combating state explosion (symbolic model checking, partial order reduction, and CEGAR), explain the theoretical basis for each, and give a concrete example of a system where each technique provides the greatest benefit.

5. Separation logic extends Hoare logic with the separating conjunction and the frame rule for modular reasoning about pointer programs. Explain the frame rule and its significance for scalability. Then explain how concurrent separation logic (CSL) and Iris extend this to concurrent programs, focusing on the parallel composition rule and the treatment of shared state.

6. Discuss the role of SMT solvers in modern verification. Starting from DPLL(T) and Nelson-Oppen, explain how SMT solvers combine decision procedures for different theories. Then describe how they are used in at least three different verification contexts (e.g., VCGen, refinement type inference, bounded model checking).

7. The FLP impossibility result shows that deterministic consensus is impossible in an asynchronous system with one faulty process. Explain the proof strategy and its implications. Then describe how practical consensus protocols (Paxos, Raft) circumvent this impossibility. What assumptions do they make, and what properties do they guarantee?

8. "Verification by construction" (writing programs in dependently-typed languages so that well-typed programs are correct) and "verification by analysis" (verifying an existing program against a specification after the fact) represent two approaches to verified software. Compare their strengths and weaknesses. Under what circumstances would you recommend each approach? Consider cost, expressiveness, maintenance, and adoption.

---

*ᛟ End of Course Materials — CS208: Formal Methods & Verification — University of Yggdrasil, 2040*