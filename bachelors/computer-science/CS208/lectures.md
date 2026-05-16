# CS208: Formal Methods & Verification
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4
**Semester:** Year 2, Semester 2
**Prerequisites:** CS105 (Discrete Mathematics & Logic), CS107 (Data Structures & Algorithms)
**Instructor:** Dr. Brynjar Lǫgsǫgumaðr, Faculty of Computational Arts

> *"The rune-carver does not guess whether the stave is true. She proves it — by the laws of the wood, the blade, and the word. So too must the programmer prove, lest the system speak lies with the voice of truth."* — Brynjar Lǫgsǫgumaðr, *Rúnarprófun: The Art of Proof* (2036)

---

## Course Description

Formal Methods & Verification teaches students to reason about programs with the same rigor that mathematicians reason about theorems. A program is not merely code that "seems to work" — it is a mathematical object with a precise specification, and we can *prove* that the program satisfies its specification. This course covers the three pillars of modern formal methods: **model checking** (exhaustive exploration of state spaces), **type theory** (proofs encoded in the type system itself), and **interactive theorem proving** (human-guided machine-checked proofs in Coq, Lean, and Agda).

The Norse metaphor threading this course is the *lawspeaker's craft* — the lögsǫgumaðr who recited the entire law from memory at the Alþingi. The law must be consistent, complete, and unambiguous; a single contradiction could unravel justice. So too with formal verification: a single uncaught edge case can unravel an entire system. By 2040, formal methods have moved from academic curiosity to industrial necessity — verified compilers (CompCert), verified operating system kernels (seL4), verified cryptographic protocols, and AI-assisted proof synthesis.

---

## Lectures

### ᚠ Lecture 1: Why Prove? — The Lawspeaker's Imperative

**Date:** Week 1, Session 1

#### Overview

This opening lecture establishes the philosophical foundation of formal verification. Why do we prove things about programs when testing seems sufficient? What kinds of bugs escape even the most exhaustive test suites? We examine three historical catastrophes — the Ariane 5 Flight 501 disaster (1996, integer overflow), the Therac-25 radiation overdoses (1985-1987, concurrency race condition), and the Knight Capital trading meltdown (2012, dead code activation) — each of which would have been caught by formal methods. The lecture then introduces the Norse legal tradition: the *lögsǫgumaðr* (lawspeaker) who memorized and recited the entire body of law, serving as a human proof checker for the legal system. What if our software had a lawspeaker?

#### Lecture Notes

Testing can demonstrate the *presence* of bugs, but never their *absence* — this is Dijkstra's dictum, and it remains as true in 2040 as it was in 1970. A test suite, no matter how comprehensive, exercises a finite number of paths through an infinite space of possible inputs and states. Formal methods offer something fundamentally different: a *proof* that a property holds for all possible inputs, all possible executions, all possible interleavings of concurrent threads.

The Ariane 5 disaster illustrates the gap between testing and proof. The inertial reference system software — reused from Ariane 4 — performed a conversion from a 64-bit floating-point value to a 16-bit signed integer. On Ariane 4, the value never overflowed. On Ariane 5's different trajectory, it did. The software had been tested exhaustively... on Ariane 4's flight envelope. A formal proof that the conversion was safe for *all possible inputs* would have revealed the vulnerability immediately. The rocket, valued at $370 million, self-destructed 37 seconds after launch.

The Therac-25 radiation therapy machine killed at least three patients through massive radiation overdose. The bug was a race condition: if the operator entered a treatment plan, then edited it within a specific 8-second window, the machine would deploy the high-power electron beam without the metal flattening filter — delivering 100+ times the intended dose directly to the patient. Testing missed this because the window was narrow and non-deterministic. A model checker exploring all possible interleavings of the operator interface and beam controller would have found the bug in minutes.

**Two Approaches to Truth.** Formal verification encompasses two broad families: *automated* (model checking, SMT solving, abstract interpretation) and *interactive* (theorem proving in Coq, Lean, Isabelle/HOL). Automated methods are push-button but limited to decidable fragments — you can check all reachable states of a cache coherence protocol, but you cannot automatically prove the correctness of quicksort. Interactive methods require human guidance but can prove arbitrarily deep properties — CompCert, a verified C compiler, required 6 person-years but guarantees that the compiled assembly behaves exactly as specified by the C semantics.

**The Lawspeaker's Role.** In medieval Iceland, the *lögsǫgumaðr* recited one-third of the entire law code at each annual Alþingi, over his three-year term. The law was not written — it was *spoken*, and the lawspeaker was the living proof that the law was consistent and complete. When a legal question arose, the lawspeaker was consulted; his recitation carried the force of proof. This is the role formal methods play in modern software engineering: a proof is a *recitation* of the program's behavior that any checker can verify independently.

**2040 Context.** By 2040, the landscape has transformed. Amazon Web Services uses TLA+ to verify core distributed systems; Meta's Infer static analyzer runs on every commit; the Rust type system prevents entire classes of memory-safety bugs at compile time; and AI-assisted proof synthesis (powered by models like DeepSeek-Prover) can generate Coq proofs for moderate-complexity lemmas automatically. Yet the *craft* — knowing what properties to prove, how to decompose a system into provable components, and where formal methods are worth their cost — remains a human skill. This course teaches that craft.

#### Required Reading
- Dijkstra, E.W. (1970). *Notes on Structured Programming*. Sections on testing and correctness.
- Lions, J.L. et al. (1996). *Ariane 5 Flight 501 Failure — Report by the Inquiry Board*. ESA.
- Leveson, N.G. & Turner, C.S. (1993). "An Investigation of the Therac-25 Accidents." *IEEE Computer*, 26(7).
- Brynjar Lǫgsǫgumaðr (2036). *Rúnarprófun: The Art of Proof*, Chapter 1: "The Lawspeaker's Oath."

#### Discussion Questions
1. If formal verification had been applied to the Therac-25, what specific property would need to be proven to prevent the overdose bug?
2. The Ariane 5 bug was introduced by *reuse without re-verification*. How do formal specifications help mitigate this risk?
3. In what contexts is testing *preferable* to formal proof, and why?

---

### ᚢ Lecture 2: Propositional and Predicate Logic — The Runes of Reason

**Date:** Week 2, Session 1

#### Overview

Before we can prove anything about programs, we must have a language in which to state our proofs. This lecture reviews propositional and first-order predicate logic — the fundamental grammar of formal reasoning. We cover syntax, semantics, natural deduction, and the relationship between truth (semantic consequence, ⊨) and provability (syntactic derivability, ⊢). The Norse runic analogy: just as the Elder Fuþark encodes meaning through the structured combination of staves, logic encodes reasoning through the structured combination of connectives and quantifiers.

#### Lecture Notes

Propositional logic deals with atomic propositions (p, q, r) combined with connectives: negation (¬), conjunction (∧), disjunction (∨), implication (→), and biconditional (↔). Its semantics is truth-functional — the truth of a compound formula depends only on the truth of its components. This makes propositional logic *decidable*: truth tables provide a mechanical decision procedure for validity, though the procedure is exponential in the number of variables (the SAT problem is NP-complete, but modern SAT solvers like Z3 and CaDiCaL routinely handle formulas with millions of variables by 2040).

First-order predicate logic adds quantifiers (∀, ∃), predicates, functions, and a domain of discourse. This enriched expressiveness comes at a cost: first-order logic is *semi-decidable* — if a formula is valid, there exists a proof, but if it is invalid, the search for a proof may run forever (Church's Theorem, 1936). This is the fundamental limitation that shapes all of formal verification: we trade expressiveness for decidability, choosing the weakest logic that can express the property we need to prove.

**Natural Deduction.** Gerhardt Gentzen's system of natural deduction (1935) provides introduction and elimination rules for each connective:
- ∧-intro: from A and B, derive A ∧ B
- ∧-elim: from A ∧ B, derive A (or B)
- →-intro: if assuming A allows deriving B, derive A → B
- →-elim (modus ponens): from A → B and A, derive B

These rules mirror how humans actually reason. A proof in natural deduction is a tree of rule applications. In 2040, we have tools that can fill in the gaps — Coq's `tauto` tactic solves propositional tautologies, and `firstorder` extends to the decidable fragment of first-order logic.

**The Soundness-Completeness Duality.** A proof system is *sound* if everything provable is true (⊢ φ ⇒ ⊨ φ). It is *complete* if everything true is provable (⊨ φ ⇒ ⊢ φ). Propositional natural deduction is both sound and complete (Gödel, 1929). First-order natural deduction is sound and complete in the semantic sense, but the incompleteness theorems (Gödel, 1931) show that no recursively axiomatizable system can capture all truths of arithmetic — there will always be true statements that cannot be proven within the system. This is the *skuggi* (shadow) that haunts all formal reasoning: some truths resist formal capture.

**The Runic Analogy.** The 24 runes of the Elder Fuþark encode a complete writing system through the combinatorial arrangement of vertical staves and diagonal branches. Each rune is a *type*; the combination of runes into words is a *term*; a runic inscription is a *proposition*. Just as a single miscarved stave turns a blessing into a curse (consider the Skåäng runestone's ambiguous phrasing), a single misplaced quantifier in a formal specification can license behavior the specifier never intended. Logic is the discipline of carving precisely.

#### Required Reading
- Huth, M. & Ryan, M. (2004). *Logic in Computer Science*, Chapters 1-2.
- Gentzen, G. (1935). "Untersuchungen über das logische Schließen." *Mathematische Zeitschrift*, 39. (English translation in Szabo, 1969).
- Smullyan, R. (1995). *First-Order Logic*. Dover.

#### Discussion Questions
1. Why is propositional logic decidable while first-order logic is not? What specific feature introduces undecidability?
2. Give an example of a true arithmetic statement that Gödel's theorem suggests cannot be proven in Peano Arithmetic.
3. How does the soundness-completeness duality map to the distinction between *under-approximation* and *over-approximation* in program analysis?

---

### ᚦ Lecture 3: Model Checking — Exhausting the State-Space

**Date:** Week 3, Session 1

#### Overview

Model checking is the brute-force hero of formal verification: given a finite-state model of a system and a temporal logic specification, the model checker exhaustively explores every reachable state to determine whether the specification holds. This lecture introduces Kripke structures, Linear Temporal Logic (LTL), Computation Tree Logic (CTL), and the basic model checking algorithms. We also cover the state explosion problem and the symbolic techniques (BDDs, SAT-based bounded model checking, IC3/PDR) that have made model checking practical for industrial-scale systems by 2040.

#### Lecture Notes

A **Kripke structure** M = (S, S₀, R, L) consists of a finite set of states S, a set of initial states S₀ ⊆ S, a transition relation R ⊆ S × S, and a labeling function L that assigns to each state the set of atomic propositions true in that state. This is a *model* of the system — an abstraction that captures the behaviors we care about while omitting irrelevant detail. The art of model checking is choosing the right abstraction: include too much, and the state space explodes; omit too much, and the verification becomes unsound.

**Temporal Logics.** LTL formulas describe properties of individual execution paths:
- □p ("always p"): p holds in every state along the path
- ◇p ("eventually p"): p holds in some state along the path
- p U q ("p until q"): p holds until q becomes true
- ○p ("next p"): p holds in the next state

CTL adds path quantifiers to reason about *all possible* futures from a state:
- A□p: along all paths, p always holds
- E◇p: there exists some path where p eventually holds

The classic LTL model checking algorithm converts the negation of the property into a Büchi automaton, computes the product with the system model, and checks for emptiness — if the product automaton accepts any word, the system has a counterexample trace. CTL model checking uses a simpler recursive labeling algorithm that runs in time O(|M| · |φ|) — linear in both the model size and the formula size. This is one of the most beautiful algorithms in computer science.

**The State Explosion Problem.** A system with n Boolean state variables potentially has 2ⁿ states. A simple cache coherence protocol with 3 processors, each with 5 control states and a shared bus, produces ~10⁶ states. Model checking it explicitly is feasible. A protocol with 8 processors and directory-based coherence produces ~10¹⁵ states — far beyond explicit enumeration.

The solution is **symbolic model checking**, introduced by Ken McMillan in his 1992 thesis. Instead of enumerating states one by one, symbolic model checking represents sets of states and the transition relation as Boolean formulas, manipulated using Binary Decision Diagrams (BDDs). BDDs exploit the structure of the state space: many states are symmetric, and the BDD for "all states where processor 3 has the cache line in shared state" is often compact. Symbolic model checking enabled the verification of the IEEE Futurebus+ cache coherence protocol (1992) — the first industrial-scale application of model checking.

By 2040, the dominant symbolic technique is **IC3/PDR** (Property Directed Reachability), developed by Aaron Bradley in 2011. IC3 incrementally strengthens an inductive invariant by learning lemmas from failed reachability attempts. It has largely supplanted BDD-based methods for hardware verification and is widely used at Intel, AMD, and NVIDIA for pre-silicon validation.

**2040 Integration.** The UoY's own **YggdrasilCheck** platform, built on the Hermes AI OS framework, integrates model checking into the CI/CD pipeline. When a developer pushes a commit to a distributed systems course project, YggdrasilCheck automatically extracts a TLA+ model, model-checks safety properties (no deadlock, no data loss), and attaches a verification certificate to the commit. Failed checks block the merge. This is the 2040 realization of the lawspeaker's role: every commit is recited and verified before it enters the law.

#### Required Reading
- Clarke, E.M., Grumberg, O., & Peled, D. (1999). *Model Checking*. MIT Press. Chapters 1-3.
- McMillan, K.L. (1992). *Symbolic Model Checking*. PhD Thesis, Carnegie Mellon.
- Bradley, A.R. (2011). "SAT-Based Model Checking without Unrolling." *VMCAI*.
- Newcombe, C. et al. (2015). "How Amazon Web Services Uses Formal Methods." *CACM*, 58(4).

#### Discussion Questions
1. Explain the difference between LTL and CTL in terms of the branching structure of time. Give a property that can be expressed in CTL but not LTL.
2. Why does the state explosion problem limit explicit-state model checking to systems with roughly 10⁸ states, even in 2040?
3. How does symbolic model checking exploit the structure of concurrent systems to achieve compression?

---

### ᚦ Lecture 4: Temporal Logic in Depth — LTL, CTL, and the Runes of Time

**Date:** Week 4, Session 1

#### Overview

This lecture dives deeper into temporal logic, moving beyond the basic operators to cover fairness constraints, liveness vs. safety, the limitations of LTL and CTL, and CTL* (which subsumes both). We also explore the philosophical connection to the Norse conception of time: the Norns weave the threads of past, present, and future at the Well of Urðr — a branching temporal structure that resonates with CTL's distinction between "along all paths" and "along some path."

#### Lecture Notes

**Safety vs. Liveness.** A safety property asserts that "something bad never happens" — it is violated by a finite prefix of an execution, after which no extension can make the property true again. Mutual exclusion (two processes never simultaneously in the critical section) is a safety property. A liveness property asserts that "something good eventually happens" — it can only be violated by an infinite execution that perpetually defers the good thing. Starvation freedom (every requesting process eventually enters the critical section) is a liveness property.

This distinction matters practically: safety properties can be checked with bounded methods (counterexample is always finite), while liveness requires reasoning about infinite behaviors — the counterexample is an infinite trace that perpetually avoids the desired state. In model checking, this means liveness requires fairness constraints: "if a process is infinitely often enabled, it is infinitely often executed." Without fairness, a model checker would report a spurious counterexample where the scheduler simply ignores a ready process forever.

**Fairness Constraints.** There are three classical notions of fairness:
- **Weak fairness:** Every continuously enabled action eventually occurs. If a process is *always* ready to enter its critical section, it must eventually do so.
- **Strong fairness:** Every infinitely-often enabled action eventually occurs. If a process is repeatedly ready, even if not continuously, it must eventually run.
- **Unconditional fairness:** Every action occurs infinitely often, regardless of enablement. Rarely used in practice.

LTL model checking under fairness uses a modified algorithm: the Büchi automaton for the negated property is intersected with the fairness-constrained system, and emptiness is checked on the resulting automaton. The accepting condition is refined so that a run is accepting only if it visits the fairness set infinitely often.

**CTL* — The Unified Logic.** CTL* (Emerson and Halpern, 1986) subsumes both LTL and CTL by allowing arbitrary nesting of path quantifiers and temporal operators. The formula E□◇p ("there exists a path where p is true infinitely often") cannot be expressed in CTL (the EGAF combination doesn't work) but is naturally expressible in CTL*. The price is complexity: CTL* model checking is PSPACE-complete (same as LTL), compared to polynomial for CTL — but in practice, modern symbolic tools handle CTL* specifications for systems up to ~10⁶ states.

**The Norse Temporal Frame.** In Vǫluspá, the vǫlva describes time not as a simple line but as a tree growing from the Well of Urðr — nourished by the waters of what-has-been, branching into what-may-be. The three Norns — Urðr (that which became), Verðandi (that which is becoming), and Skuld (that which shall become) — carve runes into the tree, shaping the branches. This is precisely the branching-time model of temporal logic: at each state, multiple futures are possible, and properties can assert things about *all* futures or *some* future.

The insight is not merely decorative. It shapes how we think about verification: a safety property checked under *all possible scheduling interleavings* (A□, along all paths) produces a guarantee that holds regardless of the operating system's thread scheduler. A liveness property that asserts "eventually the message is delivered" must be paired with fairness assumptions — if the network can drop every packet, no liveness property holds. This is Skuld's domain: of all that shall become, some paths are fair, some are not.

#### Required Reading
- Emerson, E.A. (1990). "Temporal and Modal Logic." *Handbook of Theoretical Computer Science*, Vol. B.
- Lamport, L. (2002). *Specifying Systems*. Chapters 2-4. (TLA+ notation for LTL.)
- Alpern, B. & Schneider, F.B. (1985). "Defining Liveness." *Information Processing Letters*, 21(4).
- Vǫluspá, stanzas 19-20 (the Norns at the Well of Urðr). Translation by Larrington (2014).

#### Discussion Questions
1. Can every CTL formula be expressed as an equivalent LTL formula? If not, provide a counterexample.
2. Why is fairness necessary for verifying liveness properties? What happens if we omit fairness?
3. How does CTL*'s expressiveness increase the burden on the specifier? Is more expressiveness always better?

---

### ᚨ Lecture 5: Binary Decision Diagrams — Compression of the State-Space

**Date:** Week 5, Session 1

#### Overview

Binary Decision Diagrams (BDDs) are the data structure that made symbolic model checking possible. A BDD is a canonical, compressed representation of a Boolean function. This lecture covers the construction of BDDs from Boolean formulas, the reduction rules that produce canonical forms, the efficient implementation of Boolean operations (∧, ∨, ¬, ∃), and the variable ordering problem that determines whether a BDD is compact or explodes. The runic analogy: a BDD is a *bind-rune* — a compression of multiple staves into a single, unambiguous symbol.

#### Lecture Notes

A Binary Decision Diagram represents a Boolean function f(x₁, ..., xₙ) as a directed acyclic graph. Each non-terminal node is labeled with a variable xᵢ and has two outgoing edges: the *then* edge (xᵢ = 1) and the *else* edge (xᵢ = 0). Terminal nodes are labeled 0 or 1. To evaluate f for a given assignment, start at the root and follow the appropriate edge for each variable.

A BDD is **ordered** (OBDD) if variables appear in the same order along every path from root to terminal. It is **reduced** (ROBDD) if it additionally satisfies:
1. **Uniqueness:** No two distinct nodes have the same variable and same children.
2. **Non-redundancy:** No node has identical then and else children (such nodes can be eliminated).

The magic of ROBDDs: for a fixed variable ordering, every Boolean function has a *unique* canonical ROBDD representation. Checking whether two Boolean formulas are equivalent reduces to checking whether their ROBDDs are identical — which is O(1) with a hash table. This is what makes symbolic model checking efficient: the fixpoint computation that computes reachable states manipulates BDDs, and termination is detected when the BDD for the new state set equals the BDD for the old state set.

**Operations on BDDs.** The key operation is `apply(op, BDD₁, BDD₂)`, which computes the BDD for f₁ op f₂ where op ∈ {∧, ∨, ⊕, →, ...}. The algorithm, due to Bryant (1986), uses dynamic programming: it recursively computes the result for each pair of sub-BDDs, caching results in a hash table. The time complexity is O(|BDD₁| · |BDD₂|) — quadratic in the worst case, but often much better in practice due to structural sharing.

Existential quantification is the operation that makes model checking work: ∃x·f(x, y) = f(0, y) ∨ f(1, y). In BDD terms, this replaces all nodes labeled x with an OR of their children. Repeated quantification implements the relational composition needed for computing the set of states reachable in one step: `Reached' = ∃s·(Reached(s) ∧ Transition(s, s'))[s←s']`.

**The Variable Ordering Problem.** The size of a BDD is extremely sensitive to variable ordering. The function f(x₁,...,xₙ) = (x₁ ∧ x₂) ∨ (x₃ ∧ x₄) ∨ ... ∨ (x_{n-1} ∧ xₙ) has a BDD of size O(n) under the natural ordering, but a BDD of size O(2ⁿ) under a bad ordering. Finding the optimal ordering is NP-complete. In practice, heuristics based on the circuit structure (closeness of variables in the netlist) produce orderings within a factor of 2-5 of optimal. Dynamic variable reordering (sifting), introduced by Rudell (1993), periodically reorders variables during BDD construction and has enabled verification of designs with thousands of state variables.

**2040 Update: AIGs and SAT-Sweeping.** By 2040, And-Inverter Graphs (AIGs) have largely supplanted BDDs for many verification tasks. An AIG is a structural representation of a circuit — essentially a netlist of AND gates with inverters — that is more compact than BDDs and supports efficient SAT-solving on the represented function. The ABC tool from UC Berkeley performs SAT-sweeping: it uses a SAT solver to prove equivalences between AIG nodes, merging equivalent nodes and drastically simplifying the representation. Modern hardware verification pipelines combine BDDs (for reachability), AIGs (for equivalence checking), and SAT (for bounded model checking) — choosing the right hammer for each nail.

#### Required Reading
- Bryant, R.E. (1986). "Graph-Based Algorithms for Boolean Function Manipulation." *IEEE Transactions on Computers*, C-35(8).
- Andersen, H.R. (1997). "An Introduction to Binary Decision Diagrams." Lecture notes, IT University of Copenhagen.
- Brayton, R.K. & Mishchenko, A. (2010). "ABC: An Academic Industrial-Strength Verification Tool." *CAV*.

#### Discussion Questions
1. Explain why the canonical property of ROBDDs is crucial for fixpoint detection in symbolic model checking.
2. Given a fixed variable ordering, what is the worst-case BDD size for an n-bit multiplier function? Why?
3. When might you prefer AIGs over BDDs for equivalence checking?

---

### ᚲ Lecture 6: SAT and SMT — The Oracles at the Crossroads

**Date:** Week 6, Session 1

#### Overview

SAT (Boolean satisfiability) and SMT (Satisfiability Modulo Theories) solvers are the silent engines under the hood of virtually all modern formal verification tools. A SAT solver determines whether a propositional formula is satisfiable; an SMT solver extends this to first-order theories (arithmetic, arrays, bit-vectors, uninterpreted functions). This lecture covers the DPLL and CDCL algorithms, conflict-driven clause learning, and the theory combination framework of SMT. The Norse framing: the SAT solver is the Vǫlva's *spá* (prophecy) — given a question, it answers "possible" or "impossible" with a witnessing or refuting oracle.

#### Lecture Notes

The SAT problem — given a propositional formula in CNF, is there a satisfying assignment? — is the canonical NP-complete problem (Cook, 1971). For decades, it was considered practically unsolvable for interesting sizes. The revolution came with the Chaff solver (Moskewicz et al., 2001), which introduced watched literals and conflict-driven clause learning with non-chronological backtracking. Modern SAT solvers like CaDiCaL and Kissat (Biere, 2020) routinely solve industrial instances with millions of variables and tens of millions of clauses — not by magic, but through the accumulation of clever heuristics refined over two decades.

**CDCL Algorithm.** Conflict-Driven Clause Learning works as follows:
1. **Decide:** Pick an unassigned variable, assign it true or false (decision heuristic: VSIDS, LRB, or CHB).
2. **Propagate:** Use unit propagation (Boolean Constraint Propagation, BCP) to deduce forced assignments. Watched literals make BCP extremely fast — only clauses with a newly-falsified watched literal are checked.
3. **Conflict:** If propagation leads to a falsified clause, analyze the implication graph to find the *conflict clause* — a learned clause that is a logical consequence of the original formula and prevents the conflicting assignment.
4. **Backtrack:** Jump back to the decision level where the learned clause becomes unit, undoing intervening decisions. This is non-chronological — we may jump back multiple levels.
5. **Restart:** Periodically abandon the current partial assignment and start over, retaining learned clauses. Counterintuitively, this dramatically improves performance by escaping unfruitful search regions.

**SMT: Satisfiability Modulo Theories.** SAT solves Boolean formulas. But real verification problems involve arithmetic, arrays, bit-vectors, and other theories. SMT solvers like Z3 (Microsoft Research) and CVC5 (Stanford/Iowa) combine a SAT solver with theory-specific decision procedures using the Nelson-Oppen framework for combining theories.

The key idea: the SMT solver treats the formula's atoms as Boolean variables, feeds them to a SAT solver, and when the SAT solver proposes a satisfying assignment, the *theory solver* checks whether that assignment is consistent in the theory. If not, the theory solver returns a *theory lemma* — a clause that rules out the inconsistent assignment — which the SAT solver learns and continues. This is the DPLL(T) architecture: a SAT solver augmented with theory solvers.

**Example.** Consider verifying that a C program never accesses an array out of bounds. The SMT formula encodes the program's semantics as bit-vector operations over symbolic inputs and asserts that an out-of-bounds access occurs. Z3 processes this formula and either returns "unsat" (the program is safe) or "sat" with a model showing the specific input values that trigger the bug. This is the core of symbolic execution engines like KLEE and the industrial tool Infer.

**2040 Landscape.** By 2040, SMT solvers are embedded everywhere: in compilers (optimization validity checking), in IDEs (real-time verification annotations), in CI pipelines (per-commit bounded model checking for critical properties), and in AI systems (DeepSeek-Prover uses SMT as its reasoning backbone). The UoY's **RúnarSMT** platform wraps Z3 in a Norse-themed IDE that shows proof obligations as rune-staves that illuminate green (proved) or red (counterexample found). This visual language turns abstract logic into a physical-feeling craft.

#### Required Reading
- Biere, A., Heule, M., van Maaren, H., & Walsh, T. (2009). *Handbook of Satisfiability*. Chapters 1-4.
- De Moura, L. & Bjørner, N. (2008). "Z3: An Efficient SMT Solver." *TACAS*.
- Moskewicz, M.W. et al. (2001). "Chaff: Engineering an Efficient SAT Solver." *DAC*.
- Óðinn's self-sacrifice on Yggdrasil (Hávamál, stanzas 138-141) — the acquisition of the runes through ordeal, as metaphor for the NP-hard search.

#### Discussion Questions
1. Why is non-chronological backtracking more powerful than chronological backtracking in SAT solving?
2. How does the DPLL(T) architecture cleanly separate Boolean reasoning from theory reasoning?
3. What makes SMT solving more powerful than SAT solving for software verification?

---

### ᚷ Lecture 7: Interactive Theorem Proving — The Hammer and the Anvil

**Date:** Week 7, Session 1

#### Overview

When model checking and SMT hit their limits — when the state space is infinite, or the property is undecidable in the relevant theory — we turn to interactive theorem proving. In an interactive proof assistant, the human guides the proof while the machine checks every step. This lecture introduces Coq, Lean, and their underlying type theories: the Calculus of Inductive Constructions (CIC) and dependent type theory. The Norse metaphor: the smith at the anvil, shaping the blade with deliberate, guided strikes — each blow (tactic) is checked by the eye (type checker), and the result is a weapon that will not break.

#### Lecture Notes

Interactive theorem proving rests on the **Curry-Howard isomorphism**: propositions are types, proofs are programs, and proof checking is type checking. In a dependently-typed language, the type `∀ n:ℕ, n + 0 = n` is inhabited by a function that, given any natural number n, produces a proof that n + 0 = n. The proof assistant verifies that the function is well-typed — if it type-checks, the proposition is proved.

**Coq's Calculus of Inductive Constructions.** Coq's type theory, the CIC, provides:
- **Dependent function types:** Πx:A. B(x) — the type of functions where the return type depends on the argument. This generalizes ∀ and →.
- **Inductive types:** User-defined types with constructors. Natural numbers, lists, trees, and even entire logics are defined inductively. The elimination rule for inductive types provides structural induction.
- **Universes:** Type₀ : Type₁ : Type₂ : ... — needed to avoid Girard's paradox.
- **Coinductive types:** For infinite data structures like streams, with guarded co-recursion.

A Coq proof is a script of *tactics*: `intros` moves hypotheses into the context; `induction n` generates the base case and inductive step; `simpl` simplifies expressions by computation; `rewrite H` uses an equality hypothesis; `apply H` uses an implication hypothesis. Under the hood, tactics construct a proof term in CIC — the `Qed` command type-checks this term against the stated theorem.

**Lean 4 — The 2040 Standard.** Lean 4, released in 2021 by Leonardo de Moura, has become the dominant proof assistant in the 2040 University curriculum. Its advantages:
- **Metaprogramming in Lean itself:** Tactics are written in Lean, not in a separate ML language. This means students can write custom automation without switching languages.
- **`simp` and `aesop`:** Powerful automation tactics that can solve many goals without human guidance. In 2040, AI-augmented tactics like `deepseek` automatically discharge 60-80% of subgoals in typical undergraduate proofs.
- **Mathlib4:** The largest unified library of formalized mathematics, with over 1.5 million theorems by 2040. If you need to prove something about groups, rings, topology, or measure theory, Mathlib4 almost certainly has the lemma you need.
- **Imperative features:** Lean 4 supports `do` notation, mutable variables, and monadic code — students can write proofs and programs in the same language.

**The seL4 Verification.** The most impressive industrial achievement of interactive theorem proving is seL4 — the formally verified microkernel developed at NICTA (now CSIRO). Starting in 2004, the seL4 team wrote an abstract specification (~200 lines), a concrete executable specification (~2,000 lines), and a C implementation (~8,700 lines), then proved in Isabelle/HOL that the C implementation *refines* the abstract specification — meaning every behavior of the C code is a behavior allowed by the abstract spec. The proof took approximately 25 person-years and revealed ~160 bugs in the C code (including 16 that would have survived conventional testing). The resulting kernel has never had a reported bug in its verified components.

**2040: The CompCert-Verified Toolchain.** The CompCert C compiler, verified in Coq by Xavier Leroy's team, guarantees that the compiled assembly preserves the semantics of the C source. By 2040, the **YggdrasilChain** extends this to a full verified toolchain: verified editor (guaranteed no information leakage through autocomplete), verified compiler (CompCert), verified kernel (seL4), and verified network stack — all running on verified RISC-V hardware designs. This is the vision of *end-to-end verification*: from the keystroke to the wire, every transformation is proven correct.

#### Required Reading
- Pierce, B.C. et al. (2024). *Software Foundations*, Vol. 1: Logical Foundations. (Interactive Coq textbook, freely available.)
- de Moura, L. & Ullrich, S. (2021). "The Lean 4 Theorem Prover and Programming Language." *CADE-28*.
- Klein, G. et al. (2009). "seL4: Formal Verification of an OS Kernel." *SOSP*.
- Leroy, X. (2009). "Formal Verification of a Realistic Compiler." *CACM*, 52(7).

#### Discussion Questions
1. How does the Curry-Howard isomorphism unify programming and proving? What are the implications for bug detection?
2. Why did the seL4 verification reveal bugs that testing missed? What classes of bugs are particularly amenable to formal proof?
3. Compare the effort-to-coverage tradeoff between model checking and interactive theorem proving.

---

### ᚹ Lecture 8: Dependent Type Theory — When Types Tell the Truth

**Date:** Week 8, Session 1

#### Overview

Dependent types are the philosophical core of modern proof assistants: a type that depends on a *value*. The type `Vec ℕ n` is the type of vectors of natural numbers of length n — the length is part of the type, so the type checker can prove that `head` is never called on an empty vector. This lecture develops dependent type theory from first principles: identity types, Σ-types, Π-types, and the induction principles that make them practical. The metaphor: a dependent type is a rune-stave whose meaning depends on the wood it is carved upon — the type adapts to the value, ensuring that no ill-formed binding can exist.

#### Lecture Notes

In simply-typed λ-calculus, types classify terms by their *shape*: `int → int` means "takes an integer, returns an integer." In dependently-typed λ-calculus, types can mention terms: `(n : ℕ) → Vec ℕ n → ℕ` means "given a number n and a vector of length n, return a natural number." The return type `ℕ` doesn't depend on n, but the domain type `Vec ℕ n` does — this argument's type *depends* on the value of the first argument.

**The Identity Type.** The identity type `a = b` (written `Eq A a b` or `a ≡ b`) is the proposition that a and b are equal. Its introduction rule, `refl : a = a`, says that everything equals itself. Its elimination rule is the J-rule (based on the contractibility of singletons), which enables substitution of equals for equals. In Homotopy Type Theory (HoTT), the identity type is interpreted as the space of paths between a and b — equality becomes a topological notion, and proofs of equality are paths that can be composed, reversed, and manipulated geometrically.

**Σ-Types (Dependent Pairs).** A Σ-type `Σ (x : A), B x` is the type of pairs `(a, b)` where `a : A` and `b : B a`. The second component's type depends on the first component. This generalizes both product types (when B doesn't depend on x) and existential quantification (when A is a proposition and B x is a proposition). The type of "a list together with a proof that it is sorted" is a Σ-type: `Σ (l : List ℕ), sorted l`.

**Π-Types (Dependent Functions).** A Π-type `Π (x : A), B x` is the type of functions that, given `a : A`, return a value of type `B a`. This generalizes both function types (when B doesn't depend on x) and universal quantification. The type of "a sorting function that returns a sorted permutation of the input" is: `Π (l : List ℕ), Σ (l' : List ℕ), (sorted l' × permutation l l')`.

**Inductive Families.** Inductive families are the most powerful feature of dependent type theory. The type `Vec A n` is defined as an inductive family indexed by n:
```
inductive Vec (A : Type) : ℕ → Type where
  | nil  : Vec A 0
  | cons : A → Vec A n → Vec A (n+1)
```
The constructors are type-checked so that `nil` only inhabits `Vec A 0`, and `cons` adds exactly 1 to the length. A function `head : Vec A (n+1) → A` is *total* — the type system guarantees that it can never be called with an empty vector, because `Vec A 0` is not a subtype of `Vec A (n+1)`.

**2040: Full-Spectrum Dependence.** By 2040, languages descended from Idris and Lean have brought dependent types into the programming mainstream. The **Hǫðr** language, developed at UoY, uses dependent types for: array bounds checked at compile time, config-free serialization (the type contains the protocol), zero-cost network packet parsing, and verified smart contracts. A Hǫðr program that compiles is guaranteed free of: null pointer dereferences, array bounds violations, integer overflow (unless explicitly wrapped), and protocol mismatches. The type system is the lawspeaker.

#### Required Reading
- Martin-Löf, P. (1984). *Intuitionistic Type Theory*. Bibliopolis. (The foundational text.)
- The Univalent Foundations Program (2013). *Homotopy Type Theory*. Chapters 1-2.
- Brady, E. (2017). *Type-Driven Development with Idris*. Manning.

#### Discussion Questions
1. How does the `Vec` type prevent the classic "head of empty list" error at compile time?
2. What is the relationship between Σ-types and existential quantification under Curry-Howard?
3. Why might a programmer resist dependent types despite their safety guarantees? What are the ergonomic costs?

---

### ᚺ Lecture 9: Abstract Interpretation — The Norns' Calculus of Approximation

**Date:** Week 9, Session 1

#### Overview

Abstract interpretation is a framework for static program analysis that reasons about *all possible* executions of a program by computing over *abstract* domains — approximations that capture the properties we care about while sacrificing precision. This lecture introduces the Galois connection framework, the interval and polyhedra abstract domains, the widening/narrowing operators that ensure termination, and the application to industrial static analyzers like Astrée (which proved the absence of runtime errors in the Airbus A380 flight control software). The Norse metaphor: the Norns carve the threads of fate into Yggdrasil — they don't know every leaf's exact position, but they know the shape of the tree.

#### Lecture Notes

Abstract interpretation, invented by Patrick and Radhia Cousot in 1977, is the mathematical theory of approximation. The core idea: given a concrete semantics that defines the exact behavior of every program point (often an infinite set of possible states), construct an *abstract semantics* over a simpler domain that is:
- **Sound:** The abstract result includes all concrete behaviors (over-approximation). We may get false positives, but never false negatives.
- **Computable:** Abstract operations terminate in finite time.
- **Sufficiently precise:** The over-approximation is tight enough to prove the properties we care about.

**Galois Connections.** The relationship between the concrete domain C and abstract domain A is formalized as a Galois connection: an abstraction function α: C → A and a concretization function γ: A → C such that α(c) ⊑ a iff c ⊆ γ(a). The abstract domain is a complete lattice with a partial order ⊑ representing precision (lower = more precise). The conditions ensure that abstract operations are *safe approximations* of concrete operations.

**The Interval Domain.** The simplest useful abstract domain: each integer variable is represented by an interval [l, u]. The abstract semantics for x = y + z computes the interval for x as [ly+lz, uy+uz]. This catches buffer overflows (if the index interval exceeds [0, N-1]) but fails on relationships between variables: after `if (x == y)`, the interval domain loses the fact that x and y are equal.

**The Polyhedra Domain.** The polyhedra domain (Cousot & Halbwachs, 1978) tracks linear relationships between variables: each abstract state is a convex polyhedron defined by linear inequalities. After `if (x == y)`, the polyhedron includes the constraint x - y = 0. This is far more precise than intervals but at higher computational cost — operations on polyhedra are worst-case exponential in the number of variables.

**Widening and Narrowing.** The concrete state space may have infinite ascending chains — a loop can increment a counter forever. To ensure termination, abstract interpretation uses *widening* (∇): a binary operator that jumps to a safe over-approximation, sacrificing precision to guarantee convergence. After the fixpoint is reached, *narrowing* (Δ) refines the result back toward precision. The classic widening for intervals: if the new upper bound exceeds the old, jump to +∞. This guarantees the loop analysis terminates after at most one widening step per variable.

**The Astrée Achievement.** Astrée, developed by the Cousots' team, applied abstract interpretation to prove the *absence of runtime errors* (division by zero, buffer overflow, integer overflow, null pointer dereference) in the primary flight control software of the Airbus A380 — 132,000 lines of C with no dynamic memory allocation, no recursion, but heavy use of floating-point and intricate control logic. The analysis time was approximately 3 hours on a 2004 workstation. Astrée found several subtle bugs that had survived conventional testing, including a floating-point rounding issue that could cause a control surface to oscillate at a specific frequency. The A380 entered service without a single in-flight runtime error in its verified components.

**2040 Integration.** At UoY, **YggdrasilAbstract** provides continuous abstract interpretation as part of the CI pipeline. Every commit to a critical-systems project is analyzed with: interval + congruence domain for C code, TaintCheck for information flow, and NuAccel for floating-point precision. The results are displayed as *rune-vision* — an augmented code view where green runes mark verified-safe lines, yellow runes mark lines that need annotation, and red runes mark lines with potential runtime errors. The goal: zero red runes at merge time.

#### Required Reading
- Cousot, P. & Cousot, R. (1977). "Abstract Interpretation: A Unified Lattice Model for Static Analysis." *POPL*.
- Blanchet, B. et al. (2002). "Design and Implementation of a Special-Purpose Static Program Analyzer for Safety-Critical Real-Time Embedded Software." *The Essence of Computation*, Springer.
- Cousot, P. (2022). *Principles of Abstract Interpretation*. MIT Press. (The definitive textbook, at last.)

#### Discussion Questions
1. Explain why widening is necessary for termination in abstract interpretation. What does it sacrifice?
2. The interval domain cannot prove that x ≥ 0 after `x = y * y`. What abstract domain could?
3. Compare abstract interpretation to model checking: which is better suited for infinite-state systems, and why?

---

### ᚾ Lecture 10: Separation Logic — The Laws of Memory

**Date:** Week 10, Session 1

#### Overview

Separation Logic (Reynolds, O'Hearn, 2000-2002) extends Hoare logic to reason about programs that manipulate pointers and mutable heap-allocated data structures. Its key innovation is the *separating conjunction* (∗): P ∗ Q asserts that the heap can be split into two *disjoint* parts, one satisfying P and the other Q. This lecture develops the semantics of separation logic, its frame rule, and its application to concurrent separation logic (CSL), which enabled the verification of fine-grained concurrent data structures. The Norse metaphor: the rune-carver's field — you can carve in one section without disturbing the glyphs already carved in another.

#### Lecture Notes

Hoare logic (1969) revolutionized reasoning about sequential programs with its triples {P} C {Q} — if P holds before executing C, then Q holds afterward, provided C terminates. But Hoare logic struggles with pointers: aliasing (two pointers to the same location) breaks the rule of constancy, and manual reasoning about disjointness is error-prone.

Separation logic addresses this with a new logical connective: the **separating conjunction** P ∗ Q, read "P and separately Q." In the heap model, a heap h satisfies P ∗ Q if h can be partitioned into two *disjoint* heaps h₁ and h₂ such that h₁ ⊨ P and h₂ ⊨ Q. The disjointness is the crucial part — P and Q reason about different parts of memory, and nothing in P can interfere with Q.

**The Frame Rule.** The frame rule is separation logic's killer feature:
```
{P} C {Q}
----------------- (modifies(C) ∩ free(R) = ∅)
{P ∗ R} C {Q ∗ R}
```
If a command C transforms a state satisfying P into one satisfying Q, and R describes some *disjoint* portion of the heap that C doesn't modify, then C preserves R. The frame rule enables *local reasoning*: to verify a procedure, you only need to reason about the heap cells it actually touches. The rest of the heap is automatically preserved.

**Example: Tree Insertion.** To verify a function that inserts a node into a binary search tree:
- Precondition: `tree(root)` — root points to a valid BST.
- The function traverses the tree and creates a new leaf node.
- Postcondition: `tree(root) ∗ node(new_leaf)` — the tree is still valid, and the new node is somewhere in it.
- Frame rule: if we call the function with additional disjoint state `other_data`, that state is preserved — we don't need to re-prove anything.

**Concurrent Separation Logic (CSL).** O'Hearn (2007) extended separation logic to concurrent programs. The key idea: *ownership* — a thread that owns the permission to access a heap cell can operate on it; no other thread has simultaneous permission. Ownership can be transferred between threads through synchronization primitives. CSL has been used to verify fine-grained concurrent data structures including lock-free stacks, Michael-Scott queues, and B-trees — structures where traditional testing is famously inadequate because interleaving bugs appear only under specific scheduling.

**2040: Automated Separation Logic.** By 2040, tools like Infer (Meta), VeriFast (KU Leuven), and the UoY's own **RúnarSep** automatically verify separation logic specifications for C and Rust programs. The Rust borrow checker is itself a form of separation logic — ownership and borrowing enforce heap disjointness at compile time. In the 2040 curriculum, students write verified concurrent data structures in Rust and have their separation logic proofs checked automatically — a dramatic advance from 2020, when such proofs were exclusively manual and took PhD-level expertise.

#### Required Reading
- Reynolds, J.C. (2002). "Separation Logic: A Logic for Shared Mutable Data Structures." *LICS*.
- O'Hearn, P.W. (2007). "Resources, Concurrency, and Local Reasoning." *Theoretical Computer Science*, 375(1-3).
- Calcagno, C. et al. (2011). "Moving Fast with Software Verification." *NASA Formal Methods*. (Facebook Infer overview.)

#### Discussion Questions
1. How does the separating conjunction differ from ordinary conjunction? Why is disjointness essential for local reasoning?
2. Explain the frame rule with a specific example: verifying a list-reversal function.
3. How does Rust's ownership system approximate separation logic reasoning at compile time?

---

### ᛃ Lecture 11: Verified Systems Architecture — From Kernel to Cloud

**Date:** Week 11, Session 1

#### Overview

Formal verification is not merely for toy examples — by 2040, entire systems have been verified end-to-end. This lecture surveys the landscape of verified systems: seL4 (microkernel), CompCert (C compiler), CertiKOS (hypervisor), Ironclad Apps (verified distributed applications), and the DeepSpec project's vision of a fully-verified web server stack. The Norse framing: the *garðr* (enclosure) — the verified system creates a sacred boundary within which unsafe code cannot trespass, like the Miðgarðr wall that protects the human realm from the chaos beyond.

#### Lecture Notes

**seL4 — The Trust Anchor.** The seL4 microkernel is the gold standard of system verification. Its proof chain spans four levels:
1. **Abstract specification:** What the kernel does — written in Isabelle/HOL as a set of pre/post-conditions.
2. **Executable specification:** How the kernel does it — a Haskell prototype that is automatically translated to Isabelle/HOL and proved to refine the abstract spec.
3. **C implementation:** The actual running code — ~8,700 lines of C99, with a proof in Isabelle/HOL that it refines the executable spec.
4. **Binary verification (partial):** The compiled ARM machine code — a proof that the compiler output corresponds to the C semantics.

The verification covers: no null pointer dereferences, no buffer overflows, no code injection, all kernel calls terminate, and the access control model (capabilities) is correctly enforced. The only unverified component is the boot sequence and the TLB/cache management — the rest is proven correct.

**CompCert — The Trustworthy Transformer.** Xavier Leroy's CompCert formally verifies that a C compiler preserves semantics: the generated assembly code behaves exactly as specified by the C semantics. The proof covers 8 intermediate languages (C → Clight → C#minor → Cminor → ... → PPC assembly) and 11 compilation passes. Critically, the compiler is verified, not the compiled program — but when you feed verified C code (like seL4) through CompCert, the resulting binary is also verified. This closes the verification gap between source and machine.

**DeepSpec — The End-to-End Vision.** The DeepSpec project (NSF Expedition, 2016-2026) aimed to build a fully-verified web server stack: verified hardware (RISC-V processor), verified kernel (seL4), verified compiler (CompCert), verified network stack, verified TLS implementation, and verified application. By 2040, this vision has been realized in the **YggdrasilStack** — the University's own fully-verified server infrastructure. All student web applications run on YggdrasilStack, meaning: if a student's application passes type-checking, it is guaranteed free of memory-safety bugs, information leaks through the network stack, and timing side-channels in cryptographic operations.

**2040: The Garðr Principle.** The Norse cosmology divides the world into Miðgarðr (the human enclosure), Ásgarðr (the gods' realm), and Útgarðr (the chaotic outer realm). The Miðgarðr wall, built from the eyebrows of the primordial giant Ymir, protects humanity from the chaos beyond. Verified systems architecture follows the *Garðr Principle*: build a verified boundary (the wall), and within that boundary, less formal assurance suffices. The verified kernel + verified compiler form the wall; applications within the wall can be developed with conventional testing, secure in the knowledge that no application bug can compromise the kernel. This layered approach makes formal verification economically feasible — you verify the small core, not the entire system.

#### Required Reading
- Klein, G. et al. (2014). "Comprehensive Formal Verification of an OS Microkernel." *ACM TOCS*, 32(1).
- Leroy, X. (2009). "Formal Verification of a Realistic Compiler." *CACM*, 52(7).
- Gu, R. et al. (2016). "CertiKOS: An Extensible Architecture for Building Certified Concurrent OS Kernels." *OSDI*.
- Appel, A.W. et al. (2017). "The DeepSpec Vision for Verified Systems." Position paper.

#### Discussion Questions
1. What is the "trusted computing base" (TCB) of the seL4 verification? Which components do you still need to trust?
2. Why is CompCert's verification more impactful than verifying a single program?
3. How does the Garðr Principle make full-system verification economically feasible?

---

### ᚨ Lecture 12: The Future of Formal Methods — AI, Quantum, and the Unproven

**Date:** Week 12, Session 1

#### Overview

The final lecture surveys the frontier of formal methods in 2040. AI-assisted proof synthesis is revolutionizing interactive theorem proving — models like DeepSeek-Prover and AlphaProof can now generate fully formal proofs for IMO-level problems and moderately complex software specifications. Quantum computing raises new verification challenges: how do you prove a quantum program correct? Certified AI systems — guaranteeing that an AI agent's behavior respects a formal specification — is the grand challenge of the 2040s. The Norse framing: the unproven is the *Ginnungagap* — the primordial void. Formal methods push back the void, inch by inch, establishing islands of certainty in the sea of the unknown.

#### Lecture Notes

**AI-Assisted Proof Synthesis.** By 2040, AI has transformed interactive theorem proving. DeepSeek-Prover (DeepSeek AI, 2025) demonstrated that large language models fine-tuned on formal mathematics can generate complete Lean proofs for ~45% of the Mathlib test suite. AlphaProof (DeepMind, 2026) combined a language model with a symbolic search engine (inspired by AlphaZero) to solve 4 out of 6 IMO problems in Lean — achieving a silver-medal performance. By 2040, the combination of neural proof search and symbolic verification has pushed automated proof rates to ~80% for standard undergraduate-level theorems.

The implications for software verification are profound. The **RúnarProver**, UoY's AI-augmented proof assistant, works as follows:
1. The developer writes a function annotated with pre/post-conditions.
2. RúnarProver's AI generates a proof sketch — a sequence of high-level tactics.
3. The proof sketch is refined by the symbolic engine, filling in the details.
4. The complete proof is checked by Lean's kernel — the ultimate arbiter.
5. If the proof fails, the AI iterates, guided by the type error.

This loop converges within seconds for simple properties and minutes for moderate ones. The developer's role shifts from *writing proofs* to *guiding provers* — choosing which properties to prove, providing lemmas, and inspecting counterexamples.

**Quantum Program Verification.** Quantum programs pose unique verification challenges: superposition, entanglement, and measurement create state spaces that are exponential in the number of qubits. Model checking a 100-qubit system is physically impossible — the state space has 2¹⁰⁰ dimensions. The approach by 2040 combines:
- **Quantum Hoare logic:** Ying's quantum Hoare logic extends classical Hoare triples with quantum predicates (Hermitian operators with eigenvalues in [0,1]).
- **Symbolic quantum simulation:** Q-SAT solvers that reason about quantum circuits symbolically, using the ZX-calculus for graphical rewriting.
- **Error-corrected guarantees:** For error-corrected quantum computers, verification focuses on the *logical* level — prove that the logical circuit is correct, and rely on the error correction code to handle physical noise.

**Certified AI — The Grand Challenge.** As AI agents take on increasingly autonomous roles — driving cars, managing power grids, trading securities — the question of *guaranteed behavior* becomes urgent. Formal methods offer a path: **certified AI** systems that come with machine-checked proofs of key safety properties. The challenges:
- **Specification:** What does it mean for an AI to "act safely"? How do we write a formal specification for human values?
- **Verification of learned components:** Neural networks are opaque — their specifications are implicit in their training data. Techniques from abstract interpretation (interval bound propagation, zonotope domains) can provide robustness guarantees for small networks, but scaling to large language models remains open.
- **Compositional verification:** If we verify individual agent components, does the composition preserve safety? This is the territory of assume-guarantee reasoning and contract-based design.

**The Ginnungagap.** In Norse cosmology, Ginnungagap is the primordial void that existed before creation — the gap between the realms of fire (Múspellsheimr) and ice (Niflheimr). Formal methods are our bridge-building over the Ginnungagap. Every proved theorem, every verified system, is a stone laid across the void. The void will never be fully bridged — Gödel guarantees that — but every stone extends the reach of certainty. The 2040 practitioner of formal methods inherits this tradition: the lögsǫgumaðr who recites the law, the rune-carver who carves true, the smith who forges the blade. The work continues.

#### Required Reading
- Lample, G. et al. (2022). "HyperTree Proof Search for Neural Theorem Proving." *NeurIPS*.
- DeepSeek-AI (2025). "DeepSeek-Prover: Advancing Theorem Proving through Large Language Models." Preprint.
- Ying, M. (2011). "Floyd-Hoare Logic for Quantum Programs." *ACM TOPLAS*, 33(6).
- Seshia, S.A. et al. (2022). "Toward Certified AI: A Formal Methods Perspective." *CACM*, 65(3).

#### Discussion Questions
1. Does AI-assisted proof synthesis change the nature of mathematical understanding? If an AI proves a theorem, have we *understood* it?
2. What new verification challenges does quantum computing introduce that classical formal methods cannot address?
3. Is formal verification of a general-purpose AI agent possible in principle, or does the specification problem render it intractable?

---

## Final Examination Preparation

### Format

The final examination is a **4-hour take-home assessment** consisting of:
- **Part A: Theory (40%)** — Four short-answer questions on model checking, temporal logic, type theory, and abstract interpretation. Answer all four.
- **Part B: Proof (40%)** — Two proof problems in Lean 4, covering inductive proofs on data structures and program verification with separation logic. Both must be submitted as `.lean` files that compile against Mathlib4.
- **Part C: System Design (20%)** — One essay question on verified systems architecture. Choose from three prompts.

### Sample Part A Questions

1. **Model Checking.** Explain the state explosion problem and describe how symbolic model checking addresses it. Compare BDDs and IC3/PDR as approaches. (500-750 words)

2. **Temporal Logic.** Given the CTL formulas AG(p → EF q) and AG(p → AF q), explain the semantic difference. Provide a Kripke structure that satisfies one but not the other. (500 words)

3. **Type Theory.** In the Calculus of Inductive Constructions, explain how the elimination rule for the identity type (the J-rule) enables substitution. Why is `refl` sufficient as the only constructor? (500 words)

4. **Abstract Interpretation.** Define a Galois connection between the concrete domain ℘(ℤ) and the interval domain. Show that interval addition is a sound abstraction of concrete addition. What precision is lost? (500 words)

### Sample Part B Problems

1. **List Reversal.** In Lean 4, define the function `reverse : List α → List α` and prove `reverse (reverse l) = l` by induction. You may use the lemma `reverse_append` if you prove it first.

2. **Balanced Tree Insertion.** Given the inductive type `AVLTree` with height annotations, define `insert` and prove that insertion preserves the balancing invariant: `balanced t → balanced (insert x t)`. Submit as a `.lean` file.

### Sample Part C Prompts (choose one)

1. **The Garðr Principle.** Discuss the layered verification philosophy exemplified by the seL4 + CompCert + application stack. What are the economic and engineering arguments for verifying a small core rather than the entire system? What security properties does this guarantee, and what does it leave unverified? (1500 words)

2. **AI and Formal Proof.** Evaluate the claim: "AI-assisted proof synthesis will make manual interactive theorem proving obsolete by 2050." Consider the role of human intuition, the specification problem, and the Gödelian limits on automated reasoning. (1500 words)

3. **Design a Verification Plan.** You are the verification lead for a new distributed key-value store. Design a verification strategy: what properties would you model-check? What would you prove interactively? What components would you test conventionally? Justify each choice with reference to the methods covered in this course. (1500 words)

---

## Required Reading — Full Course Bibliography

- Alpern, B. & Schneider, F.B. (1985). "Defining Liveness." *IPL*, 21(4).
- Andersen, H.R. (1997). "An Introduction to Binary Decision Diagrams." ITU Copenhagen.
- Appel, A.W. et al. (2017). "The DeepSpec Vision for Verified Systems."
- Biere, A. et al. (2009). *Handbook of Satisfiability*. IOS Press.
- Blanchet, B. et al. (2002). "Design and Implementation of a Special-Purpose Static Analyzer." *The Essence of Computation*.
- Bradley, A.R. (2011). "SAT-Based Model Checking without Unrolling." *VMCAI*.
- Brady, E. (2017). *Type-Driven Development with Idris*. Manning.
- Brayton, R.K. & Mishchenko, A. (2010). "ABC: An Academic Industrial-Strength Verification Tool." *CAV*.
- Bryant, R.E. (1986). "Graph-Based Algorithms for Boolean Function Manipulation." *IEEE TC*, C-35(8).
- Calcagno, C. et al. (2011). "Moving Fast with Software Verification." *NASA Formal Methods*.
- Clarke, E.M., Grumberg, O., & Peled, D. (1999). *Model Checking*. MIT Press.
- Cousot, P. & Cousot, R. (1977). "Abstract Interpretation: A Unified Lattice Model." *POPL*.
- Cousot, P. (2022). *Principles of Abstract Interpretation*. MIT Press.
- De Moura, L. & Bjørner, N. (2008). "Z3: An Efficient SMT Solver." *TACAS*.
- de Moura, L. & Ullrich, S. (2021). "The Lean 4 Theorem Prover and Programming Language." *CADE-28*.
- DeepSeek-AI (2025). "DeepSeek-Prover: Advancing Theorem Proving through LLMs."
- Dijkstra, E.W. (1970). *Notes on Structured Programming*.
- Emerson, E.A. (1990). "Temporal and Modal Logic." *Handbook of TCS*, Vol. B.
- Gentzen, G. (1935). "Untersuchungen über das logische Schließen." *Math. Zeitschrift*, 39.
- Gu, R. et al. (2016). "CertiKOS: An Extensible Architecture for Certified Concurrent OS Kernels." *OSDI*.
- Huth, M. & Ryan, M. (2004). *Logic in Computer Science*. Cambridge.
- Klein, G. et al. (2009). "seL4: Formal Verification of an OS Kernel." *SOSP*.
- Klein, G. et al. (2014). "Comprehensive Formal Verification of an OS Microkernel." *ACM TOCS*, 32(1).
- Lamport, L. (2002). *Specifying Systems*. Addison-Wesley.
- Lample, G. et al. (2022). "HyperTree Proof Search for Neural Theorem Proving." *NeurIPS*.
- Leroy, X. (2009). "Formal Verification of a Realistic Compiler." *CACM*, 52(7).
- Leveson, N.G. & Turner, C.S. (1993). "An Investigation of the Therac-25 Accidents." *IEEE Computer*, 26(7).
- Lǫgsǫgumaðr, B. (2036). *Rúnarprófun: The Art of Proof*. Yggdrasil University Press.
- Martin-Löf, P. (1984). *Intuitionistic Type Theory*. Bibliopolis.
- McMillan, K.L. (1992). *Symbolic Model Checking*. PhD Thesis, CMU.
- Moskewicz, M.W. et al. (2001). "Chaff: Engineering an Efficient SAT Solver." *DAC*.
- Newcombe, C. et al. (2015). "How Amazon Web Services Uses Formal Methods." *CACM*, 58(4).
- O'Hearn, P.W. (2007). "Resources, Concurrency, and Local Reasoning." *TCS*, 375(1-3).
- Pierce, B.C. et al. (2024). *Software Foundations*, Vol. 1: Logical Foundations.
- Reynolds, J.C. (2002). "Separation Logic: A Logic for Shared Mutable Data Structures." *LICS*.
- Seshia, S.A. et al. (2022). "Toward Certified AI: A Formal Methods Perspective." *CACM*, 65(3).
- Smullyan, R. (1995). *First-Order Logic*. Dover.
- The Univalent Foundations Program (2013). *Homotopy Type Theory*. Princeton.
- Vǫluspá & Hávamál. Translations by Carolyne Larrington (2014), *The Poetic Edda*. Oxford.
- Ying, M. (2011). "Floyd-Hoare Logic for Quantum Programs." *ACM TOPLAS*, 33(6).

---

*This course is one thread in the great weave of the Bachelor of Science in Computer Science. May your proofs be sound, your models finite, and your abstractions precise. — Dr. Brynjar Lǫgsǫgumaðr, Summer 2040.*
