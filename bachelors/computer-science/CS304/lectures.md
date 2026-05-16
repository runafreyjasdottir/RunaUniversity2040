# CS304: Quantum Computing Fundamentals
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4  
**Prerequisites:** CS201 (Data Structures & Algorithms II), MATH202 (Linear Algebra)  
**Description:** Qubits, gates, entanglement, Shor's, Grover's, Qiskit

---

## Lectures

ᛟ **Lecture 1: From Classical Bits to Quantum Bits — The Foundations of Quantum Information**

**Course:** CS304 — Quantum Computing Fundamentals  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

This lecture introduces the fundamental unit of quantum information: the qubit. We begin with the limitations of classical bits, establish the mathematical framework of quantum states as vectors in Hilbert space, and explore how superposition enables quantum parallelism. The goal is not merely to define qubits mechanically but to develop genuine intuition for why quantum information is fundamentally different from classical information — and why that difference matters for computation.

By 2040, quantum computing has transitioned from laboratory curiosity to engineering discipline. Google's Sycamore processor demonstrated quantum supremacy in 2019; IBM's Eagle and Osprey processors pushed qubit counts past 1,000; and the University of Yggdrasil's own Hliðskjálf Quantum Lab operates a 4,000-qubit superconducting processor available to all CS students. Understanding quantum information is no longer optional for computer scientists — it is as fundamental as understanding binary arithmetic was in the 1950s.

### Key Topics

- **The Classical Bit and Its Limitations**: Why classical information processing hits fundamental physical limits
- **The Qubit**: State vectors in ℂ², the Bloch sphere representation, and the meaning of superposition
- **Dirac Notation**: Bras, kets, and the elegance of quantum notation
- **Physical Qubits vs. Logical Qubits**: Error rates, decoherence, and why we need error correction
- **The Quantum Measurement Postulate**: Collapsing superposition and extracting classical information
- **No-Cloning Theorem**: Why you cannot copy an unknown quantum state — and why it matters
- **The 2040 Hardware Landscape**: Superconducting, trapped-ion, photonic, and topological qubits

### Lecture Notes

A classical bit is defined by its state: either 0 or 1. A qubit, by contrast, is defined by its state vector in a two-dimensional complex Hilbert space ℂ². We write:

```
|ψ⟩ = α|0⟩ + β|1⟩
```

where α, β ∈ ℂ and |α|² + |β|² = 1. The normalization condition ensures that the probabilities of measuring 0 and 1 sum to 1 — there is no "missing" probability in a quantum measurement.

The **Bloch sphere** provides the most intuitive geometric representation of a single qubit. Any pure state |ψ⟩ can be written as:

```
|ψ⟩ = cos(θ/2)|0⟩ + e^(iφ) sin(θ/2)|1⟩
```

where θ ∈ [0, π] is the polar angle and φ ∈ [0, 2π) is the azimuthal angle. This maps every pure qubit state to a point on the unit sphere. The north pole (θ=0) is |0⟩, the south pole (θ=π) is |1⟩, and the equator represents equal superposition states. The phase φ, invisible to measurement of a single qubit in the computational basis, becomes critically important when qubits interact through multi-qubit gates — it is the engine of quantum interference.

**Dirac notation** (pronounced "bracket") is the standard notation for quantum states. |ψ⟩ is a "ket" — a column vector. ⟨ψ| is a "bra" — a row vector, the conjugate transpose of the ket. The inner product ⟨φ|ψ⟩ gives the probability amplitude for state |ψ⟩ to be found in state |φ⟩. The outer product |ψ⟩⟨φ| is an operator. This notation is not merely decorative — it makes quantum calculations dramatically more tractable than matrix notation alone. Master it early.

**The No-Cloning Theorem** (Wootters and Zurek, 1982; Dieks, 1982) states that there is no unitary operation that can create an exact copy of an arbitrary unknown quantum state. The proof is elegant: suppose a cloning machine U exists such that U|ψ⟩|0⟩ = |ψ⟩|ψ⟩ for all |ψ⟩. Then for two different states |α⟩ and |β⟩:

```
U|α⟩|0⟩ = |α⟩|α⟩
U|β⟩|0⟩ = |β⟩|β⟩
```

Taking the inner product of both sides:

```
⟨α|β⟩·⟨0|0⟩ = ⟨α|β⟩·⟨α|β⟩
⟨α|β⟩ = ⟨α|β⟩²
```

This implies ⟨α|β⟩ = 0 or ⟨α|β⟩ = 1. In other words, the cloner only works for orthogonal or identical states — not for arbitrary states. The no-cloning theorem has profound consequences: it prevents eavesdropping in quantum key distribution (QKD), it makes quantum error correction fundamentally different from classical error correction (we cannot copy qubits to protect them, we must encode them), and it underlies the security of quantum money schemes.

**Physical qubits** are the actual quantum systems — superconducting transmon qubits, trapped ions, photons in optical cavities, or topological anyons. Each platform has different characteristics:

- **Superconducting qubits** (IBM, Google, UoY Hliðskjálf): Fast gate times (~20ns for single-qubit, ~200ns for two-qubit), but require millikelvin temperatures. Gate fidelities ~99.9% single-qubit, ~99.5% two-qubit (as of 2040).
- **Trapped ions** (IonQ, Quantinuum): Longer coherence times (seconds to minutes), high gate fidelities (>99.99%), but slower gate speeds (~μs) and harder to scale.
- **Photonic qubits** (Xanadu, PsiQuantum): Room-temperature operation, natural for quantum networking, but probabilistic gates and no quantum memory.
- **Topological qubits** (Microsoft): Theoretically immune to local errors, but still largely experimental. The Majorana fermion approach has had well-publicized setbacks.

**Logical qubits** are error-corrected qubits built from multiple physical qubits. The surface code, the leading error correction scheme, requires approximately 1,000 physical qubits per logical qubit at current error rates. This means a 4,000-physical-qubit processor like Hliðskjálf can support roughly 4 logical qubits — enough for quantum error correction demonstrations but not yet for algorithmic advantage. The "quantum advantage threshold" (sometimes called the "quantum utility threshold") is estimated at 50-100 logical qubits, which would require roughly 50,000-100,000 physical qubits. Current projections place this milestone in the 2043-2047 timeframe.

### Required Reading

- Nielsen, M.A., Chuang, I.L. (2010). *Quantum Computation and Quantum Information*. Cambridge University Press. Chapters 1.1-1.3, 2.1-2.2.
- Wootters, W.K., Zurek, W.H. (1982). "A Single Quantum Cannot Be Cloned." *Nature* 299.
- Preskill, J. (2018). "Quantum Computing in the NISQ Era and Beyond." *Quantum* 2:79.

### Discussion Questions

1. The Bloch sphere represents pure states as points on a sphere. What about mixed states? Where do they live? How does the representation change?
2. The no-cloning theorem prohibits copying unknown quantum states. Does this mean quantum computers cannot store data? How do quantum RAM (QRAM) and quantum memories work around this limitation?
3. Current superconducting qubits have coherence times of ~100μs and gate times of ~20ns. How many gates can be executed before decoherence destroys the computation? What does this imply for the depth of quantum circuits we can run?

### Practice Problems

- Write a Python function using NumPy that constructs the state vector for an arbitrary qubit |ψ⟩ = α|0⟩ + β|1⟩ given complex numbers α and β (checking normalization).
- Implement the Bloch sphere visualization for a qubit state. Given θ and φ, compute the Cartesian coordinates on the sphere.
- Prove that any single-qubit unitary can be decomposed as a rotation around the Z-axis, followed by a rotation around the X-axis, followed by another rotation around the Z-axis (the Z-X-Z decomposition).

---

ᛏ **Lecture 2: Quantum Gates — The Logic of Quantum Circuits**

**Course:** CS304 — Quantum Computing Fundamentals  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

If qubits are the data, quantum gates are the operations. This lecture covers the complete set of single-qubit and multi-qubit gates, their matrix representations, and the universality results that tell us which gate sets are sufficient to approximate any quantum computation. We also introduce the circuit model — the standard way to express quantum algorithms visually and algebraically.

### Key Topics

- **Single-Qubit Gates**: Pauli matrices (X, Y, Z), Hadamard (H), phase (S), and arbitrary rotations (Rθ)
- **Multi-Qubit Gates**: CNOT, CZ, SWAP, Toffoli, and the controlled-unitary family
- **Universal Gate Sets**: {H, S, CNOT, T} as a universal set; Solovay-Kitaev theorem for approximation
- **The Circuit Model**: Quantum circuits as directed acyclic graphs of gates
- **Gate Decomposition**: Breaking arbitrary unitaries into elementary gates
- **Quantum Circuit Cost Models**: Depth, width, T-count, and why different metrics matter

### Lecture Notes

Every quantum gate is a **unitary transformation** — a linear map U on ℂ²ⁿ (for n qubits) satisfying U†U = I, where U† is the conjugate transpose. Unitarity implies that quantum gates are reversible (U⁻¹ = U†) and preserve the norm of state vectors (probability is conserved). This reversibility constraint is not a limitation — it is a fundamental property of quantum mechanics that any quantum computation can be reversed by applying the inverse gates in reverse order.

**Single-qubit gates** operate on one qubit and are represented by 2×2 unitary matrices:

- **Pauli-X** (NOT gate): X = [[0,1],[1,0]]. Flips |0⟩ ↔ |1⟩. The quantum analog of the classical NOT gate.
- **Pauli-Y**: Y = [[0,-i],[i,0]]. Rotates around the Y-axis of the Bloch sphere by π.
- **Pauli-Z**: Z = [[1,0],[0,-1]]. Applies a phase of -1 to |1⟩. Rotates around the Z-axis by π.
- **Hadamard** H = (1/√2)[[1,1],[1,-1]]. Creates equal superposition: H|0⟩ = |+⟩ = (|0⟩+|1⟩)/√2, H|1⟩ = |-⟩ = (|0⟩-|1⟩)/√2. The Hadamard gate is the workhorse of quantum algorithms — it creates superposition from classical states.
- **Phase** S = [[1,0],[0,i]]. Applies a phase of i to |1⟩. Together with H, forms a universal single-qubit gate set.
- **T gate** (π/8 gate): T = [[1,0],[0,e^(iπ/4)]]. Applies a π/4 phase to |1⟩. Crucial for universal quantum computation — without T gates, we can only implement the Clifford group, which is efficiently simulable classically (Gottesman-Knill theorem).
- **Arbitrary rotations**: Rₓ(θ), Rᵧ(θ), R_z(θ) rotate the Bloch vector around the respective axis by angle θ.

**Multi-qubit gates** operate on two or more qubits:

- **CNOT** (Controlled-NOT): A two-qubit gate where the state of the "control" qubit determines whether an X gate is applied to the "target" qubit. Matrix: flips |10⟩ ↔ |11⟩ while leaving |00⟩ and |01⟩ unchanged. CNOT is the most important two-qubit gate — it creates entanglement (see Lecture 3) and is the primary workhorse of quantum circuits.
- **CZ** (Controlled-Z): Similar to CNOT but applies a Z gate to the target. CZ = CNOT with Hadamards on the target before and after. Equivalent to CNOT up to single-qubit rotations.
- **SWAP**: Exchanges two qubits. |01⟩ ↔ |10⟩. Decomposable into 3 CNOTs.
- **Toffoli** (CCNOT): A three-qubit gate that flips the target only when both controls are |1⟩. Universal for classical reversible computation (can implement AND, OR, NOT). Not universal for quantum computation without additional single-qubit gates.

**Universality** is the question of which gate sets can approximate any unitary to arbitrary precision. The most important result is:

**Theorem (Universal Gate Set)**: The set {H, S, CNOT, T} is universal for quantum computation. Any n-qubit unitary can be approximated to precision ε using O(logᶜ(1/ε)) gates from this set, where c ≈ 2 for the Solovay-Kitaev construction.

The Solovay-Kitaev theorem (1997) guarantees that we can efficiently decompose any desired unitary into gates from a universal set. The key insight is that the group of unitaries generated by H, S, CNOT, and T is dense in the unitary group (for approximate universality) or, more precisely, that we can get within ε of any target unitary using O(log^3.97(1/ε)) gates from the set.

This has practical implications: any quantum algorithm, no matter how complex, can be expressed as a sequence of these four basic gates. When we say a quantum algorithm "uses" a particular gate, we always mean that it can be decomposed into these elementary gates.

**The T-count** of a quantum circuit is the number of T gates used. This metric is critically important because T gates are expensive to implement in most fault-tolerant schemes — they require "magic state distillation," a resource-intensive process that accounts for the majority of the overhead in error-corrected quantum computation. In the surface code, each logical T gate costs approximately 100× more than a logical Clifford gate. This means that the T-count, not the total gate count, is often the primary cost metric for quantum algorithms.

**Circuit depth** is the number of time steps required to execute a circuit, assuming that gates acting on different qubits can be executed in parallel. Shallow circuits are more resilient to decoherence (they finish before the qubits lose coherence), but some algorithms inherently require deep circuits. The trade-off between depth and width (number of qubits used) is a central concern in quantum algorithm design.

### Required Reading

- Nielsen, M.A., Chuang, I.L. (2010). *Quantum Computation and Quantum Information*. Chapters 4.1-4.5.
- Dawson, C.M., Nielsen, M.A. (2006). "The Solovay-Kitaev Algorithm." *Quantum Information and Computation* 6(1).
- Amy, M., et al. (2013). "NCPolynomial: An Open-Source Package for Optimization over the Clifford Hierarchy." (T-count optimization reference)

### Discussion Questions

1. CNOT creates entanglement, but SWAP does not. Yet SWAP is composed of 3 CNOTs. How can a gate composed of entangling operations be non-entangling? Resolve this apparent paradox.
2. The Clifford group (generated by {H, S, CNOT}) can be efficiently simulated on a classical computer (Gottesman-Knill theorem). Does this mean that adding just the T gate is what makes quantum computing powerful? Or is this an artifact of our gate decomposition?
3. Why is the T gate so expensive in fault-tolerant quantum computing? Trace the connection from T gate → magic state distillation → surface code resource overhead.

### Practice Problems

- Implement the following gates in NumPy: X, Y, Z, H, S, T, CNOT. Verify that each is unitary (U†U = I) and compute their action on |0⟩ and |1⟩.
- Decompose the SWAP gate into 3 CNOTs. Verify by matrix multiplication that CNOT₁₂ · CNOT₂₁ · CNOT₁₂ = SWAP.
- Construct the Toffoli gate from elementary gates. How many CNOTs does your decomposition require? (Optimal known: 6 CNOTs.)
- Given the gate sequence H-T-H on |0⟩, compute the resulting state vector. Express it in the computational basis.

---

ᚢ **Lecture 3: Entanglement — Quantum Correlation Beyond Classical Explanation**

**Course:** CS304 — Quantum Computing Fundamentals  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Entanglement is the most distinctive feature of quantum mechanics — and the most misunderstood. This lecture provides a rigorous treatment of entanglement: what it is, how to detect it, how to quantify it, and why it is a resource for quantum computation. We trace the history from EPR's 1935 objection through Bell's 1964 theorem to the 2022 Nobel Prize in Physics for experimental verification of Bell inequality violations.

### Key Topics

- **Product States vs. Entangled States**: When the whole equals the sum of its parts (product) and when it doesn't (entangled)
- **Bell States (EPR Pairs)**: The four maximally entangled two-qubit states
- **Bell's Theorem and Bell Inequalities**: No local hidden variable theory can reproduce all quantum predictions
- **CHSH Inequality**: The most commonly tested Bell inequality
- **Entanglement Measures**: Von Neumann entropy, concurrence, and entanglement of formation
- **Quantum Teleportation**: Using entanglement to transmit quantum states without physical transfer
- **Superdense Coding**: Using entanglement to send 2 classical bits with 1 qubit
- **LOCC and Entanglement Distillation**: Creating high-fidelity entanglement from noisy pairs

### Lecture Notes

A **product state** (also called a separable state) is one that can be written as a tensor product of individual qubit states:

```
|ψ⟩ = (α|0⟩ + β|1⟩) ⊗ (γ|0⟩ + δ|1⟩) = αγ|00⟩ + αδ|01⟩ + βγ|10⟩ + βδ|11⟩
```

Product states are "unentangled" — the state of each qubit is well-defined, and measuring one qubit tells you nothing about the other.

An **entangled state** is one that *cannot* be written as a tensor product. The prototypical example is the Bell state:

```
|Φ+⟩ = (|00⟩ + |11⟩)/√2
```

This state cannot be decomposed — there is no way to assign individual states to qubits 1 and 2 such that their tensor product yields |Φ+⟩. Measuring either qubit yields a random outcome (|0⟩ or |1⟩ with equal probability), but the outcomes are perfectly correlated: if qubit 1 yields |0⟩, qubit 2 is guaranteed to yield |0⟩, and vice versa. This correlation holds regardless of the distance between the qubits.

There are four **Bell states** (also called EPR pairs, after Einstein, Podolsky, and Rosen), forming a basis for the two-qubit Hilbert space:

```
|Φ+⟩ = (|00⟩ + |11⟩)/√2    (even parity, positive phase)
|Φ-⟩ = (|00⟩ - |11⟩)/√2    (even parity, negative phase)
|Ψ+⟩ = (|01⟩ + |10⟩)/√2    (odd parity, positive phase)
|Ψ-⟩ = (|01⟩ - |10⟩)/√2    (odd parity, negative phase)
```

Each Bell state is maximally entangled: measuring either qubit in any basis yields a random outcome, and the other qubit's state is determined with certainty. The Bell states can be created through a simple circuit: H on qubit 1, followed by CNOT with qubit 1 as control and qubit 2 as target.

The **EPR paradox** (1935) was Einstein's objection to quantum mechanics. He argued that if measuring qubit 1 instantly determines the state of qubit 2 (regardless of distance), then either (a) quantum mechanics is incomplete (there are hidden variables that determine the outcomes), or (b) there is "spooky action at a distance" (faster-than-light influence). Einstein preferred option (a); Bohr defended option (b) by emphasizing that measurement outcomes cannot be used to transmit information (no signaling).

**Bell's theorem** (1964) resolved this debate definitively — not in favor of quantum mechanics per se, but against hidden variables. Bell derived an inequality that any local hidden variable theory must satisfy. Quantum mechanics violates this inequality. The contradiction is not a matter of interpretation — it is a mathematical fact about the statistics of measurement outcomes.

The **CHSH inequality** (Claude, Horne, Shimony, Holt, 1969) is the most commonly tested form of Bell's inequality. It involves four measurements (A₀, A₁, B₀, B₁) on two particles, each yielding ±1. The inequality states:

```
|E(A₀B₀) + E(A₀B₁) + E(A₁B₀) - E(A₁B₁)| ≤ 2
```

where E(AB) is the expectation value of the product of outcomes when Alice measures setting A and Bob measures setting B. Quantum mechanics predicts a maximum value of 2√2 ≈ 2.828, known as the **Tsirelson bound**. Experiments have consistently confirmed violations of the CHSH inequality, with the 2022 Nobel Prize awarded to Aspect, Clauser, and Zeilinger for their experimental demonstrations.

**Quantum teleportation** uses entanglement to transmit a quantum state from one location to another, using only classical communication. The protocol:

1. Alice and Bob share a Bell pair |Φ+⟩. Alice holds qubit A, Bob holds qubit B.
2. Alice wants to send an unknown qubit |ψ⟩ = α|0⟩ + β|1⟩ (qubit C) to Bob.
3. Alice performs a Bell measurement on qubits A and C, obtaining one of four classical outcomes (00, 01, 10, or 11).
4. Alice sends the two classical bits to Bob.
5. Depending on the classical bits, Bob applies one of four corrections to his qubit B, recovering |ψ⟩.

The key insight: the quantum state is not "teleported" instantaneously — Bob needs the two classical bits (which arrive at light speed) to correct his qubit. Without these bits, Bob's qubit is in a maximally mixed state, which carries no information about |ψ⟩. Teleportation does not violate no-signaling.

**Superdense coding** is the reverse: using one qubit to send two classical bits. Alice and Bob share a Bell pair. Alice applies one of four operations to her qubit (I, X, Z, or iY), transforming the shared pair into one of the four Bell states. She then sends her qubit to Bob. Bob performs a Bell measurement on the two qubits, recovering Alice's two classical bits. This is the quantum equivalent of sending 2 bits over a 1-bit channel — made possible by the pre-shared entanglement.

### Required Reading

- Nielsen, M.A., Chuang, I.L. (2010). *Quantum Computation and Quantum Information*. Chapters 2.3, 2.4.
- Bell, J.S. (1964). "On the Einstein Podolsky Rosen Paradox." *Physics* 1(3).
- Aspect, A. (2022). "Nobel Lecture: Entanglement, from Theory to Technology." *Reviews of Modern Physics*.

### Discussion Questions

1. Teleportation "transmits" a quantum state using classical bits and pre-shared entanglement. What are the practical limitations of this for building a quantum internet? How does entanglement distribution limit the rate of quantum communication?
2. Bell inequality violations have been confirmed experimentally many times. Yet some physicists argue about "loopholes" (locality loophole, detection loophole, freedom-of-choice loophole). What are these loopholes, and have they all been closed?
3. If entanglement is a resource, can it be quantified? How much entanglement does one Bell pair contain? How about two Bell pairs? Is there a standard "unit" of entanglement?

### Practice Problems

- Prove that the Bell state |Φ+⟩ cannot be written as a tensor product of two single-qubit states. (Hint: assume it can and derive a contradiction.)
- Implement quantum teleportation in Qiskit. Verify that the final state matches the original state |ψ⟩ for several test inputs.
- Calculate the maximum CHSH violation achievable by quantum mechanics. Show that it equals 2√2. (This is the Tsirelson bound.)
- Two parties share 100 copies of a Werner state: ρ = p|Φ+⟩⟨Φ+| + (1-p)I/4, where I/4 is the maximally mixed state. For what values of p does the state violate the CHSH inequality?

---

ᛒ **Lecture 4: Quantum Algorithms I — The Query Model and Deutsch-Jozsa**

**Course:** CS304 — Quantum Computing Fundamentals  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

We now have the tools — qubits, gates, entanglement, measurement — to start asking the fundamental question: what can quantum computers do that classical computers cannot? This lecture begins the algorithms sequence with the simplest quantum advantage: the Deutsch-Jozsa algorithm, which solves a black-box problem with exponentially fewer queries than any classical algorithm. While the problem itself is contrived, the structure of the solution — create superposition, apply oracle, interfere, measure — is the template for all quantum algorithms.

### Key Topics

- **The Oracle (Black-Box) Model**: How we formalize "calling a function" in quantum computation
- **The Deutsch Problem**: Determining whether a function is constant or balanced with a single query
- **The Deutsch-Jozsa Algorithm**: Extending Deutsch's result to n-bit functions
- **Quantum Parallelism**: Evaluating a function on all inputs simultaneously
- **The Role of Interference**: Why quantum parallelism alone is not enough — we must interfere the results
- **The Phase Oracle**: Converting a classical oracle into a quantum phase oracle

### Lecture Notes

In the **query model** (also called the black-box or oracle model), we are given an oracle — a "black box" that implements a function f: {0,1}ⁿ → {0,1}. We can query the oracle on any input and receive the output, but we cannot inspect its internal implementation. The goal is to determine some property of f (e.g., is it constant? balanced? what is its period?) with as few oracle queries as possible.

In the classical setting, each query reveals one bit of information about f. To determine whether f is constant (all 0s or all 1s) or balanced (equal number of 0s and 1s), a deterministic classical algorithm must query at least 2^(n-1) + 1 of the 2ⁿ possible inputs in the worst case. The reason: until the algorithm has seen more than half the inputs, it cannot be sure they're all the same value. A randomized classical algorithm can do better — with probability at least 1/2, it can answer correctly after k random queries if f is constant and all k queries return the same value. But this requires O(1) queries only in the average case; the worst case remains O(2ⁿ).

**The Deutsch problem** (1985) was the first demonstration of quantum advantage. For a function f: {0,1} → {0,1}, determine whether f is constant (f(0) = f(1)) or balanced (f(0) ≠ f(1)). Classically, this requires two queries (f(0) and f(1)). Quantumly, Deutsch showed that it requires only one query. The algorithm is:

1. Prepare |0⟩ and apply H to get |+⟩ = (|0⟩ + |1⟩)/√2.
2. Apply the oracle U_f (which maps |x⟩ → (-1)^(f(x))|x⟩ for phase oracle, or |x⟩|y⟩ → |x⟩|y⊕f(x)⟩ for bit oracle).
3. Apply H again.
4. Measure. If the result is |0⟩, f is constant; if |1⟩, f is balanced.

The key insight: by applying H before the oracle, we query f on both inputs simultaneously (quantum parallelism). By applying H after the oracle, we interfere the results, causing the constant and balanced cases to produce distinguishable outcomes.

**The Deutsch-Jozsa algorithm** (1992) extends Deutsch's result to n-bit functions. Given f: {0,1}ⁿ → {0,1}, promised to be either constant or balanced, determine which. Classically, this requires O(2ⁿ) queries in the worst case. Quantumly, it requires exactly one query. The algorithm follows the same structure:

1. Prepare n qubits in |0⟩ and one ancilla in |1⟩.
2. Apply H to all qubits (creating superposition over all 2ⁿ inputs).
3. Apply the oracle U_f.
4. Apply H to the first n qubits.
5. Measure. If all n qubits yield |0⟩, f is constant; otherwise, f is balanced.

The analysis relies on the Hadamard transform: H^(⊗n)|x⟩ = (1/√2ⁿ) Σ_z (-1)^(x·z)|z⟩, where x·z is the bitwise inner product. After the oracle and second Hadamard, the amplitude of the |0⟩^(⊗n) state is proportional to Σ_x (-1)^(f(x)), which is +2ⁿ for constant f and 0 for balanced f. This is a perfect separation — the algorithm succeeds with probability 1 on a single query.

**The phase oracle** is the natural form for many quantum algorithms. A classical function f is converted into a quantum oracle in one of two ways:

- **Bit oracle**: U_f|x⟩|y⟩ = |x⟩|y ⊕ f(x)⟩. This requires an extra qubit (the output register).
- **Phase oracle**: U_f|x⟩ = (-1)^(f(x))|x⟩. This encodes the function value as a phase flip, requiring no extra qubit.

The phase oracle is more convenient for many algorithms (including Deutsch-Jozsa and Grover's search) because it directly encodes information in the phase, which can then be interfered using the Hadamard transform. Converting between the two forms is straightforward: apply H to the output qubit of a bit oracle to convert it to a phase oracle.

**Quantum parallelism** — the ability to evaluate f on all 2ⁿ inputs simultaneously — is necessary but not sufficient for quantum advantage. The problem is that we cannot extract all 2ⁿ values from the superposition — measurement collapses the state to a single outcome. The art of quantum algorithm design is in arranging the interference pattern so that the desired information is concentrated in the measurement outcomes.

### Required Reading

- Deutsch, D. (1985). "Quantum Theory, the Church-Turing Principle and the Universal Quantum Computer." *Proc. R. Soc. Lond. A* 400.
- Deutsch, D., Jozsa, R. (1992). "Rapid Solution of Problems by Quantum Computation." *Proc. R. Soc. Lond. A* 439.
- Nielsen, M.A., Chuang, I.L. (2010). *Quantum Computation and Quantum Information*. Chapter 1.4.

### Discussion Questions

1. The Deutsch-Jozsa problem has "promised" input — f is guaranteed to be either constant or balanced. What happens if this promise is violated? Can the algorithm detect a violation?
2. Quantum parallelism evaluates f on all inputs simultaneously, but we can only read one output. Is quantum parallelism really "computing all answers at once," or is it something more subtle?
3. The Deutsch-Jozsa algorithm achieves an exponential quantum advantage, but the problem is contrived. Is there any practical scenario where this advantage matters?

### Practice Problems

- Implement the Deutsch-Jozsa algorithm in Qiskit for n=3. Test it on both constant and balanced functions. Verify that it always outputs the correct answer with a single oracle query.
- Prove that the classical deterministic query complexity of Deutsch-Jozsa is 2^(n-1) + 1. Why can't a classical algorithm do better?
- Compute the output of the Deutsch-Jozsa circuit step by step for n=2, f(x) = x₁ ⊕ x₂ (the XOR function, which is balanced). Show that the measurement yields a non-zero result.

---

ᚹ **Lecture 5: Quantum Algorithms II — Simon's Problem and the Quantum Fourier Transform**

**Course:** CS304 — Quantum Computing Fundamentals  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

This lecture introduces two crucial stepping stones toward Shor's factoring algorithm. Simon's problem (1994) demonstrated an exponential quantum-classical separation for a problem that is not contrived — it relates directly to the hidden subgroup problem, a generalization that encompasses both Shor's and many other quantum algorithms. The Quantum Fourier Transform (QFT) is the engine that powers Shor's algorithm and many others; we develop it fully and study its circuit implementation.

### Key Topics

- **Simon's Problem**: Finding the period of a 2-to-1 function with exponential quantum advantage
- **The Hidden Subgroup Problem (HSP)**: Generalizing Simon, Shor, and many quantum algorithms
- **The Quantum Fourier Transform (QFT)**: Quantum analog of the discrete Fourier transform
- **QFT Circuit**: The recursive decomposition and its O(n²) gate complexity
- **Phase Estimation**: Using QFT to estimate eigenvalues of unitaries
- **The Approximate QFT**: Truncating the QFT circuit for practical implementations

### Lecture Notes

**Simon's problem** (1994) asks: given a function f: {0,1}ⁿ → {0,1}ⁿ that is promised to be 2-to-1 with a hidden period s (i.e., f(x) = f(y) iff x ⊕ y = s), find s. The promise means that f(x) = f(x ⊕ s) for all x, and that if f(x) = f(y), then y = x ⊕ s.

Classically, finding s requires O(2^(n/2)) queries (by the birthday paradox — you need to find a collision). Quantumly, Simon's algorithm finds s with only O(n) quantum queries, giving an exponential separation.

Simon's algorithm works as follows:

1. Prepare a superposition over all inputs: (1/√2ⁿ) Σ_x |x⟩.
2. Apply the oracle: (1/√2ⁿ) Σ_x |x⟩|f(x)⟩.
3. Measure the second register, obtaining some value f(x₀). This collapses the first register to (1/√2)(|x₀⟩ + |x₀ ⊕ s⟩).
4. Apply H^(⊗n) to the first register. The result is a superposition over all z such that z · s = 0 (mod 2).
5. Measure, obtaining a random z perpendicular to s.
6. Repeat O(n) times to collect n-1 linearly independent equations z_i · s = 0.
7. Solve the system of linear equations to find s.

The key step is the Hadamard transform, which converts the period-finding structure of the oracle into a system of linear equations. This is the same structural trick that Shor's algorithm uses, generalized to the **hidden subgroup problem** (HSP).

**The Hidden Subgroup Problem (HSP)**: Given a group G, a subgroup H ≤ G, and a function f: G → X that is constant on cosets of H and distinct on different cosets (i.e., f(g₁) = f(g₂) iff g₁H = g₂H), find H (or a generating set for H). Simon's problem is HSP over Z₂ⁿ; Shor's algorithm is HSP over Z_N (integers mod N).

The HSP captures an enormous range of problems:
- Simon: HSP over Z₂ⁿ (period finding over binary groups)
- Shor: HSP over Z_N (period finding over cyclic groups → factoring)
- Discrete logarithm: HSP over Z_N × Z_M
- Pell's equation: HSP over R (requires quantum algorithms for continuous groups)

Efficient quantum algorithms for HSP exist for all finite abelian groups. For non-abelian groups (which are relevant to graph isomorphism and shortest vector problems), the situation is more complex — efficient algorithms are known for some groups but not all.

**The Quantum Fourier Transform (QFT)** over Z₂ⁿ is the unitary transformation:

```
QFT|j⟩ = (1/√2ⁿ) Σ_k e^(2πijk/2ⁿ) |k⟩
```

This is exactly the discrete Fourier transform, but implemented as a quantum operation on a superposition of states. The QFT maps the computational basis to the Fourier basis, transforming periodic structures in the input into peaks in the output — precisely what we need for period finding.

The QFT circuit over n qubits requires only O(n²) gates, compared to O(n2ⁿ) for the classical FFT. This exponential improvement in circuit depth is the source of quantum advantage in Shor's algorithm. The circuit decomposes as:

1. Apply H to qubit 1.
2. For each subsequent qubit k (k=2,...,n), apply a controlled-R_m gate (phase rotation by 2π/2^m) from qubit k to qubit 1, for m=2,...,k.
3. Recursively apply the same pattern to qubits 2 through n.
4. Perform a SWAP of qubits (reverse the order) at the end.

This recursive structure gives an O(n²) gate count (n(n-1)/2 CNOTs and n Hadamards), which is exponentially more efficient than the classical FFT's O(n2ⁿ).

**Quantum Phase Estimation (QPE)** uses the QFT to estimate the eigenvalue (phase) of an eigenvector of a unitary operator U. Given |ψ⟩ such that U|ψ⟩ = e^(2πiφ)|ψ⟩, QPE approximates φ to n bits of precision using O(2ⁿ) applications of controlled-U operations and an inverse QFT. QPE is a fundamental subroutine in many quantum algorithms, including Shor's algorithm and quantum simulation.

### Required Reading

- Simon, D. (1994). "On the Power of Quantum Computation." *FOCS*.
- Nielsen, M.A., Chuang, I.L. (2010). *Quantum Computation and Quantum Information*. Chapters 5.1-5.2.
- Coppersmith, D. (2002). "An Approximate Fourier Transform Useful in Quantum Factoring." *IBM Research Report RC19642*.

### Discussion Questions

1. Simon's problem has an exponential quantum advantage, but it's still an oracle problem. Why are oracle separations considered less "real" than computational separations? What would change if we could find a natural (non-oracle) problem with exponential quantum advantage?
2. The QFT has O(n²) gate complexity but the classical FFT has O(n2ⁿ). The QFT only works on quantum data — you can't input classical data and get a classical FFT output faster. Why is this quantum advantage still useful?
3. QPE requires controlled-U operations where U might be a very expensive gate (e.g., modular exponentiation in Shor's). How does the cost of implementing controlled-U affect the overall algorithm cost?

### Practice Problems

- Implement Simon's algorithm in Qiskit for n=4. Choose a random secret s and verify that the algorithm finds s.
- Implement the QFT over 3 qubits in Qiskit. Verify that QFT†·QFT = I (the identity).
- Apply the QFT to the state |3⟩ (|011⟩ in binary) on 3 qubits. Compute the output state by hand and verify your calculation with Qiskit.

---

ᛁ **Lecture 6: Shor's Algorithm — Breaking RSA and the Quantum Threat**

**Course:** CS304 — Quantum Computing Fundamentals  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Shor's algorithm (1994) is the most famous quantum algorithm and the primary motivation for quantum computing investment worldwide. It factors integers in polynomial time, breaking RSA and other public-key cryptosystems that underpin internet security. This lecture provides a complete treatment of the algorithm, from the number-theoretic reduction to the quantum period-finding subroutine, and discusses the practical implications for cryptography in 2040.

### Key Topics

- **The Factoring Problem and RSA**: Why factoring is hard classically and how RSA depends on this hardness
- **Number-Theoretic Reduction**: Factoring reduces to order-finding (period-finding)
- **Order Finding**: Given a and N, find the smallest r such that a^r ≡ 1 (mod N)
- **The Quantum Period-Finding Subroutine**: QFT + modular exponentiation
- **Classical Post-Processing**: Continued fractions to extract the period from QFT measurements
- **Shor's Algorithm for Discrete Logarithms**: Breaking Diffie-Hellman and elliptic curve cryptography
- **Post-Quantum Cryptography**: Lattice-based, code-based, and hash-based alternatives

### Lecture Notes

**The factoring problem**: Given a composite integer N, find its prime factorization. For RSA-2048 (a 2048-bit number), the best known classical algorithm (the General Number Field Sieve) requires approximately 2^112 operations — infeasible with any foreseeable classical computer. Shor's algorithm performs the same task in O((log N)³) quantum operations — polynomial time.

**The reduction from factoring to order-finding** is elegant and entirely classical:

1. Choose a random a ∈ {2, ..., N-1}.
2. Compute gcd(a, N). If gcd(a, N) > 1, we've found a factor. (Small probability.)
3. Find the order r of a modulo N: the smallest positive integer such that a^r ≡ 1 (mod N). This is the quantum part.
4. If r is even, compute x = a^(r/2) mod N. If x ≠ ±1 (mod N), then gcd(x-1, N) and gcd(x+1, N) are non-trivial factors of N.
5. If r is odd or x ≡ ±1, try again with a different a.

The probability of success in one try is at least 1/2 for each random a, so O(1) repetitions suffice. The critical quantum step is step 3: finding the order r.

**Order-finding as period-finding**: The function f(j) = a^j mod N is periodic with period r. Specifically, f(j) = f(j+r) for all j. So finding the order r is equivalent to finding the period of f.

**The quantum subroutine** uses the QFT to find this period:

1. Prepare the superposition: (1/√Q) Σ_j |j⟩, where Q is chosen to be a power of 2 with Q > N².
2. Apply the modular exponentiation oracle: (1/√Q) Σ_j |j⟩|a^j mod N⟩.
3. Measure the second register, obtaining some value a^(j₀) mod N. This collapses the first register to a superposition over j values that are congruent to j₀ mod r.
4. Apply the QFT to the first register. The result has peaks at integer multiples of Q/r.
5. Measure, obtaining a value k that is close to a multiple of Q/r.
6. Use continued fractions to extract r from k/Q ≈ j/r.

The modular exponentiation step (step 2) is the most expensive part. Computing a^j mod N requires O((log N)³) quantum gates, but it can be done in O((log N)² log log N · log log log N) time using efficient modular multiplication circuits. The QFT adds another O((log N)²) gates. The total is polynomial in log N — precisely the quantum advantage.

**Shor's algorithm for discrete logarithms** works similarly. Given g^x mod p, find x. The classical best algorithm (number field sieve) runs in subexponential time. Shor's quantum algorithm runs in O((log p)³) time, breaking Diffie-Hellman key exchange and elliptic curve cryptography (ECC). This means that **all currently deployed public-key cryptography is vulnerable to quantum attack**.

**Post-quantum cryptography** (PQC) is the field of developing cryptographic algorithms that are resistant to quantum computers. The NIST Post-Quantum Cryptography Standardization Process (2016-2024) selected four algorithms for standardization:

- **ML-KEM (CRYSTALS-Kyber)**: Lattice-based key encapsulation mechanism.
- **ML-DSA (CRYSTALS-Dilithium)**: Lattice-based digital signature.
- **SLH-DSA (SPHINCS+)**: Hash-based digital signature (conservative backup).
- **FN-DSA (FALCON)**: Lattice-based digital signature (compact signatures).

As of 2040, the migration from RSA/ECC to post-quantum algorithms is well underway but far from complete. The University of Yggdrasil's Bifrost Network has used ML-KEM for all internal communication since 2037, but many legacy systems still rely on RSA-2048 or ECC-256. The "harvest now, decrypt later" threat — adversaries recording encrypted traffic today in anticipation of future quantum computers — makes this migration urgent.

### Required Reading

- Shor, P.W. (1994). "Algorithms for Quantum Computation: Discrete Logarithms and Factoring." *FOCS*.
- Shor, P.W. (1997). "Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer." *SIAM J. Comput.* 26(5).
- NIST (2024). "Post-Quantum Cryptography Standardization." *FIPS 203, 204, 205*.

### Discussion Questions

1. Shor's algorithm requires a quantum computer with roughly 2n logical qubits to factor an n-bit number. With current error rates, this requires approximately 1,000× more physical qubits (surface code overhead). When do you estimate factoring RSA-2048 will become feasible? What are the key uncertainties?
2. If a large-scale quantum computer were built tomorrow, which systems would be immediately vulnerable? Which would have some lead time for migration? What would be the impact on the global financial system?
3. Lattice-based cryptography (the foundation of ML-KEM/ML-DSA) has no known quantum attacks that break it efficiently. But this is a "no known attack" security proof, not a "provably secure" proof. How comfortable should we be with this level of assurance?

### Practice Problems

- Walk through Shor's algorithm step by step for N = 15, a = 7. Find the order r, compute a^(r/2) mod N, and show that gcd(a^(r/2) - 1, N) or gcd(a^(r/2) + 1, N) yields a non-trivial factor.
- Implement the QFT over 4 qubits in Qiskit. Apply it to the state |5⟩ and verify the output matches the theoretical prediction.
- For RSA-2048, estimate the number of logical qubits and physical qubits needed for Shor's algorithm, assuming a surface code with 1,000 physical qubits per logical qubit. Compare with current quantum hardware capabilities.

---

ᛖ **Lecture 7: Grover's Algorithm — Quantum Search and Its Applications**

**Course:** CS304 — Quantum Computing Fundamentals  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Grover's algorithm (1996) provides a quadratic speedup for unstructured search problems. While the speedup is more modest than Shor's exponential advantage, Grover's algorithm is far more broadly applicable — any problem that can be formulated as searching an unsorted database can benefit. This lecture covers the algorithm, its optimalwow菌, its application to NP-complete problems, and its limitations.

### Key Topics

- **Unstructured Search**: Searching an unordered database of N items for a marked item
- **The Oracle for Search**: Marking the solution with a phase flip
- **The Grover Iteration**: Reflection about the mean — the geometric intuition
- **Optimal Number of Iterations**: π/(4√N) iterations for maximum success probability
- **Amplitude Amplification**: Generalizing Grover's to arbitrary success probability
- ** Grover's for Optimization**: Finding the maximum (quantum minimum finding)
- **Limitations**: Why Grover's cannot beat O(√N) — the BBBV lower bound

### Lecture Notes

The **unstructured search problem**: Given a function f: {0,1}ⁿ → {0,1} where f(x) = 1 for exactly one input x* and f(x) = 0 for all others, find x*. Classically, this requires O(N) = O(2ⁿ) queries in the worst case and O(N/2) on average. Quantumly, Grover's algorithm finds x* with only O(√N) = O(2^(n/2)) queries.

The **oracle** for Grover's search is a phase oracle that marks the solution: U_f|x⟩ = (-1)^(f(x))|x⟩. This flips the phase of the solution state |x*⟩ by -1 while leaving all other states unchanged. The phase flip may seem like a small perturbation, but Grover's algorithm amplifies it through iterative reflections.

**The Grover iteration** (also called the Grover operator) consists of two steps:

1. **Oracle step**: Apply U_f, flipping the phase of |x*⟩.
2. **Diffusion step**: Apply the "reflection about the mean" operator D = 2|ψ⟩⟨ψ| - I, where |ψ⟩ = H^(⊗n)|0⟩^(⊗n) is the uniform superposition.

Each iteration rotates the state vector by an angle 2θ closer to the solution, where sin(θ) = 1/√N. After approximately π/(4θ) ≈ π√N/4 iterations, the_amplitude of the solution state is nearly 1, and measurement yields x* with high probability.

The **geometric intuition** is powerful: think of the state vector as living in a two-dimensional plane spanned by |x*⟩ (the solution) and |x⊥⟩ (the uniform superposition of all non-solution states). Each Grover iteration rotates the state vector by 2θ toward |x*⟩. We want to rotate until the vector is nearly aligned with |x*⟩, which takes (π/2 - θ)/(2θ) ≈ π/(4θ) ≈ π√N/4 iterations.

The crucial insight: we must stop iterating at the right point. If we continue past the optimal number of iterations, the state vector overshoots |x*⟩ and begins rotating away. The success probability oscillates sinusoidally — peaking near 1 after approximately π√N/4 iterations, dipping back toward 0 after π√N/2 iterations, and so on. This means that **knowing when to stop** is critical. If we don't know N (the number of solutions) in advance, we must estimate it or use a more sophisticated approach (quantum counting).

**Multiple solutions**: If there are M solutions instead of 1, the number of iterations decreases to approximately π√(N/M)/4. This makes Grover's algorithm particularly effective for problems with few solutions — the relative speedup is largest when M ≪ N.

**Amplitude amplification** (Brassard et al., 2002) generalizes Grover's to the case where we have an arbitrary initial success probability p (not necessarily 1/N). Instead of the diffusion operator D, which assumes a uniform initial distribution, amplitude amplification uses a generalized reflection that works for any initial state. The number of iterations required is approximately π/(4√p), which gives Grover's original result when p = 1/N.

**Quantum minimum finding** (Dürr and Høyer, 1996) uses Grover's as a subroutine to find the minimum element in an unsorted database. The algorithm: (1) pick a random element as the current minimum y; (2) use Grover's search to find an element x < y; (3) if found, set y = x and repeat; (4) if not found (with high probability, no smaller element exists), output y. This runs in O(√N) time, a quadratic improvement over the classical O(N) minimum finding algorithm.

**The BBBV lower bound** (Bennett, Bernstein, Brassard, Vazirani, 1997) proves that O(√N) queries are optimal for unstructured search — Grover's algorithm cannot be improved beyond the quadratic speedup. The proof shows that any quantum algorithm that makes o(√N) queries to the oracle has a vanishing probability of identifying the solution. This is a fundamental limit, not a limitation of our techniques.

### Required Reading

- Grover, L.K. (1996). "A Fast Quantum Mechanical Algorithm for Database Search." *STOC*.
- Bennett, C.H., et al. (1997). "Strengths and Weaknesses of Quantum Computing." *SIAM J. Comput.* 26(5).
- Brassard, G., et al. (2002). "Quantum Amplitude Amplification and Estimation." *AMS Contemporary Mathematics* 305.

### Discussion Questions

1. Grover's provides a quadratic speedup over classical search, which is modest compared to Shor's exponential speedup. Is a quadratic speedup worth the overhead of building a quantum computer? Under what conditions (i.e., for what problem sizes) does the quantum advantage outweigh the constant factors?
2. The BBBV bound proves O(√N) is optimal for unstructured search. Does this mean NP-complete problems can receive at best a quadratic quantum speedup? What are the implications for quantum computing's impact on computational complexity?
3. In practice, most real search problems are not truly unstructured — there are heuristics, structure, and prior information. How does this affect the applicability of Grover's algorithm?

### Practice Problems

- Implement Grover's algorithm in Qiskit for a 3-qubit search problem (N=8). Use a marked state of your choice. Observe how the success probability oscillates with the number of iterations. What is the optimal number of iterations?
- Implement Grover's for N=8 with M=2 solutions. Verify that the optimal number of iterations is approximately half what it is for M=1.
- Prove the BBBV lower bound intuition: show that after k oracle queries, the total amplitude on the solution state is at most O(k/√N). (Hint: use hybrid argument.)

---

ᚾ **Lecture 8: Quantum Error Correction — Protecting Quantum Information**

**Course:** CS304 — Quantum Computing Fundamentals  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Quantum error correction (QEC) is the single most important enabling technology for practical quantum computing. Without it, decoherence and gate errors would make any computation longer than a few microseconds useless. This lecture covers the fundamental codes — Shor's 9-qubit code, the 7-qubit Steane code, and the surface code — and the threshold theorem that guarantees scalable quantum computation is possible in principle.

### Key Topics

- **Quantum Errors**: Bit flips, phase flips, and the general error model
- **The No-Cloning Barrier and Its Resolution**: Why redundancy must be more subtle than copying
- **Shor's 9-Qubit Code**: The first quantum error-correcting code
- **Stabilizer Formalism**: The mathematical framework for QEC
- **The 7-Qubit Steane Code**: A more efficient CSS code
- **The Surface Code**: The leading practical QEC scheme and the path to fault-tolerant quantum computing
- **The Threshold Theorem**: If error rates are below a threshold, arbitrarily long computations are possible

### Lecture Notes

Quantum errors come in three types for a single qubit:

1. **Bit flip** (X error): |0⟩ → |1⟩, |1⟩ → |0⟩. The quantum analog of a classical bit flip.
2. **Phase flip** (Z error): |0⟩ → |0⟩, |1⟩ → -|1⟩. No classical analog — this error changes the relative phase between |0⟩ and |1⟩.
3. **Bit-phase flip** (Y error): |0⟩ → i|1⟩, |1⟩ → -i|0⟩. Equivalent to an X error followed by a Z error (up to a global phase).

A general single-qubit error is a combination of no error (I), bit flip (X), phase flip (Z), and bit-phase flip (Y), with arbitrary weights. The remarkable result of quantum error correction is that we can correct arbitrary errors by correcting just these three basis errors — any error can be decomposed into a linear combination of I, X, Y, Z on each qubit, and correcting the basis errors corrects the superposition as well.

**The no-cloning barrier**: We cannot protect quantum information by simply copying it (as we do classically with triple modular redundancy), because the no-cloning theorem prohibits copying an unknown quantum state. The resolution: **quantum error-correcting codes encode logical information across multiple physical qubits in a way that allows error detection and correction without ever copying the logical state**.

**Shor's 9-qubit code** (1995) encodes 1 logical qubit into 9 physical qubits and corrects any single-qubit error. The encoding concatenates two simpler codes:

1. A 3-qubit bit-flip code: |0⟩ → |000⟩, |1⟩ → |111⟩. This protects against bit-flip (X) errors by majority voting on the three copies.
2. A 3-qubit phase-flip code: |+⟩ → |+++⟩, |-⟩ → |---⟩, where |+⟩ = (|0⟩+|1⟩)/√2 and |-⟩ = (|0⟩-|1⟩)/√2. This protects against phase-flip (Z) errors by encoding in the Hadamard basis.

Together, the 9-qubit code encodes:

```
|0⟩_L = (|000⟩ + |111⟩)(|000⟩ + |111⟩)(|000⟩ + |111⟩) / (2√2)
|1⟩_L = (|000⟩ - |111⟩)(|000⟩ - |111⟩)(|000⟩ - |111⟩) / (2√2)
```

Error detection uses parity checks: compare qubits 1 and 2, 2 and 3, 4 and 5, 5 and 6, 7 and 8, 8 and 9 for bit-flip errors; compare the sign of blocks 1-3 vs 4-6, and 4-6 vs 7-9 for phase-flip errors. Any single-qubit error (X, Y, or Z) on any of the 9 qubits can be detected and corrected.

**The stabilizer formalism** (Gottesman, 1997) provides a powerful framework for QEC. A stabilizer code is defined by its stabilizer group S — the set of Pauli operators that fix every codeword. The code space is the simultaneous +1 eigenspace of all stabilizers. Errors are detected by measuring the stabilizers; the pattern of measurement outcomes (the syndrome) identifies the error. The number of logical qubits is k = n - log₂(|S|), where n is the number of physical qubits and |S| is the size of the stabilizer group.

**The 7-qubit Steane code** encodes 1 logical qubit into 7 physical qubits, correcting any single-qubit error. It is a CSS (Calderbank-Shor-Steane) code, constructed from the classical [7,4,3] Hamming code. The Steane code's stabilizers are: 3 X-type stabilizers (from the Hamming code's parity check matrix) and 3 Z-type stabilizers (same matrix, but with Z operators). The code has distance d=3, meaning it can correct any 1-qubit error (or detect any 2-qubit error).

**The surface code** is the leading candidate for practical QEC in 2040. It encodes logical qubits in a 2D lattice of physical qubits with nearest-neighbor interactions — perfectly suited for superconducting qubit architectures. Key properties:

- **Encoding**: A distance-d surface code on a d×d lattice encodes 1 logical qubit into roughly 2d² physical qubits (including ancillas).
- **Error threshold**: Approximately 1% per gate for the surface code (one of the highest thresholds of any QEC code).
- **Rate**: 1 logical qubit per ~2d² physical qubits for distance d.
- **Decoding**: Minimum-weight perfect matching (MWPM) is the standard decoding algorithm for the surface code.

The **threshold theorem** (Aharonov and Ben-Or, 1997; Kitaev, 1997) is the theoretical guarantee that makes large-scale quantum computation possible. It states: if the error rate per physical gate is below a threshold p_th (approximately 1% for the surface code), then arbitrarily long quantum computations can be performed with arbitrarily low error by increasing the code distance (using more physical qubits per logical qubit). The resource overhead scales as O(log(1/ε) · poly(log log(1/ε))) per logical gate, where ε is the target logical error rate.

In 2040, the University of Yggdrasil's Hliðskjálf processor achieves single-qubit gate fidelities of 99.97% and two-qubit gate fidelities of 99.5%. This is still above the threshold (meaning errors are too frequent for direct fault-tolerant computation), but the gap is narrowing. Projections suggest that 99.9% two-qubit gate fidelity — the point at which surface-code QEC becomes efficient enough for practical use — may be achieved by 2043.

### Required Reading

- Shor, P.W. (1995). "Scheme for Reducing Decoherence in Quantum Computer Memory." *Physical Review A* 52(4).
- Steane, A. (1996). "Error Correcting Codes in Quantum Theory." *Physical Review Letters* 77(5).
- Fowler, A.G., et al. (2012). "Surface Codes: Towards Practical Large-Scale Quantum Computation." *Physical Review A* 86(3).

### Discussion Questions

1. The surface code has a threshold of ~1% per gate. Current two-qubit gate fidelities are around 99.5% (0.5% error rate). How many physical qubits per logical qubit would be needed to achieve a logical error rate of 10⁻¹⁵? Calculate the overhead.
2. Shor's 9-qubit code protects against any single-qubit error. What about two-qubit errors? Can it detect them? Correct them? What is the minimum code distance needed to correct t errors?
3. The threshold theorem assumes independent errors. In practice, errors are often correlated (e.g., cosmic ray hits cause simultaneous errors on many qubits). How does this affect QEC? What techniques exist to handle correlated errors?

### Practice Problems

- Construct the encoding circuit for Shor's 9-qubit code. Show that applying an X error to qubit 1 produces a syndrome that uniquely identifies the error.
- Prove that the Steane code has distance d=3. (Hint: show that any two codewords differ in at least 3 positions, and that there exists a pair of codewords that differ in exactly 3 positions.)
- Calculate the number of physical qubits needed to encode 10 logical qubits with distance d=11 (enough to correct 5 errors) using the surface code. Estimate the total resource count for running Shor's algorithm on a 2048-bit number with this level of error correction.

---

ᛉ **Lecture 9: Quantum Key Distribution and Quantum Cryptography**

**Course:** CS304 — Quantum Computing Fundamentals  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

While Shor's algorithm threatens classical cryptography, quantum mechanics also provides new cryptographic primitives that are provably secure against any attack — classical or quantum. This lecture covers quantum key distribution (QKD), quantum money, and quantum secure direct communication, with emphasis on the security proofs and practical implementations that make these technologies viable in 2040.

### Key Topics

- **BB84 Protocol**: The first QKD protocol — creating shared secret keys from quantum states
- **E91 Protocol**: Entanglement-based QKD using Bell states
- **Security Proofs**: Why QKD is information-theoretically secure (not just computationally secure)
- **Device-Independent QKD**: Security even with untrusted devices
- **Quantum Money**: Unforgeable currency based on quantum no-cloning
- **Quantum Secure Direct Communication**: Transmitting messages without a shared key
- **Practical QKD Systems**: Fiber-based and free-space implementations in 2040

### Lecture Notes

**BB84** (Bennett and Brassard, 1984) is the simplest and most widely deployed QKD protocol. Alice sends random qubits to Bob, encoded in one of two bases (computational Z-basis or Hadamard X-basis). Bob measures each qubit in a randomly chosen basis. After transmission, Alice and Bob publicly announce their bases (but not their measurement outcomes) and keep only the bits where their bases matched. This yields a shared secret key (the "sifted key"). Error estimation and privacy amplification transform the sifted key into a final secret key that is information-theoretically secure.

The security of BB84 rests on two quantum properties:

1. **Measurement disturbance**: An eavesdropper (Eve) who measures a qubit in the wrong basis disturbs the state, introducing errors that Alice and Bob can detect.
2. **No-cloning**: Eve cannot copy the qubits and measure them later, because the no-cloning theorem prohibits copying unknown quantum states.

**E91** (Ekert, 1991) uses entanglement for key distribution. Alice and Bob share Bell pairs and each measure their qubit in one of three bases. By testing a subset of their results against the CHSH inequality, they can verify that their qubits are genuinely entangled — and therefore that no eavesdropper has disturbed the state. The remaining results form the shared key. E91's advantage over BB84 is that security is directly tied to the violation of a Bell inequality, providing a device-independent security guarantee.

**Security proofs** for QKD establish that the secret key rate (bits of secret key per bit of sifted key) is lower-bounded by:

```
r ≥ 1 - H(e) - H(e)
```

where H is the binary entropy function and e is the quantum bit error rate (QBER). If the QBER is below approximately 11% (for BB84 with one-way post-processing), positive secret key rates are achievable. This threshold assumes the most general attack allowed by quantum mechanics — including collective attacks and coherent attacks that entangle all exchanged qubits.

**Device-independent QKD** (DI-QKD) goes further: security holds even if the quantum devices (sources and detectors) are manufactured by an adversary. The security proof relies solely on the observed Bell inequality violation, which certifies the presence of entanglement and rules out any classical (or even quantum) manipulation by the device manufacturer. DI-QKD is the gold standard for security, but practical implementations in 2040 require very high detection efficiency (>90%) and are still limited to laboratory demonstrations.

**Quantum money** (Wiesner, 1983; Aaronson and Christiano, 2012) is a fascinating application of quantum no-cloning. Wiesner's original scheme encodes each banknote as a set of qubits in random BB84 states. The bank knows the basis sequence (the "serial number") and can verify the banknote by measuring in the correct bases. A counterfeiter, who doesn't know the bases, cannot clone the qubits (by no-cloning) and therefore cannot produce two valid copies. The scheme is information-theoretically secure — no amount of computation, classical or quantum, can successfully counterfeit the banknote.

In practice, Wiesner's scheme is difficult to implement because quantum states decohere. The banknotes must maintain their quantum states for the entire time between issuance and verification, which is challenging for physical qubits with coherence times of milliseconds. In 2040, the University of Yggdrasil is experimenting with a hybrid approach: quantum money that uses a small number of qubits (protecting against replication) combined with classical digital signatures (protecting against tampering). The qubits are refreshed every 24 hours using entanglement-assisted regeneration.

**Quantum secure direct communication (QSDC)** transmits messages directly without a shared key, using quantum states to encode the message and entanglement for eavesdropping detection. The ping-pong protocol (Bost
---

## Midterm Exam Topics (Week 8)

The midterm covers Lectures 1–4 and Labs 1–3. Format: 2-hour written exam, no notes.

**Section A — Short Answer (40%)**: Definitions and brief explanations of key concepts: qubit states on the Bloch sphere, unitary gates and their properties, no-cloning theorem, Bell states, CHSH inequality, Deutsch-Jozsa algorithm, Grover's search geometry.

**Section B — Calculations (30%)**: Matrix representations of gates (H, X, Z, CNOT); computing measurement probabilities given state vectors; tracing out subsystems for reduced density matrices; calculating entanglement entropy.

**Section C — Proofs (15%)**: No-cloning theorem proof; universality of {H, T, CNOT}; BBBV optimality proof outline.

**Section D — Circuit Design (15%)**: Given an algorithm description, draw the circuit diagram. Given a circuit diagram, compute the output state. Typical tasks: prepare Bell states, implement Deutsch-Jozsa for a given oracle, compute Grover's iteration count.

---

## Final Exam Topics (Week 16)

The final covers all 8 lectures and all 7 labs. Format: 3-hour written exam, one page of notes permitted.

**Section A — Short Answer (25%)**: Key definitions from all lectures, including error correction codes (Shor, Steane, surface), QFT circuit structure, NISQ algorithms (VQE, QAOA), hardware platforms.

**Section B — Calculations (25%)**: Extended calculations spanning multiple topics: Shor's algorithm period-finding for a given N; surface code logical error rate estimation; quantum repeater fidelity calculations; QAOA parameter optimization.

**Section C — Proofs (20%)**: Threshold theorem outline; Shor's algorithm correctness (why factoring reduces to period-finding); QFT correctness; teleportation protocol verification.

**Section D — Design and Analysis (20%)**: Design a quantum circuit from specification; analyze error budgets; compare hardware platforms for a given application; design a QKD protocol for a given network topology.

**Section E — Essay (10%)**: Choose one of three prompts on the societal, ethical, or philosophical implications of quantum computing (e.g., "Will quantum computing create a new digital divide? How should universities prepare for the post-quantum world?").

---

## Final Project Guidelines

The final project is an individual implementation of a quantum algorithm or protocol not covered in depth in class. Students must submit a proposal (Week 10), a progress report (Week 13), and a final presentation (Week 16).

**Example Projects**:
- Implementation of Quantum Walk algorithms for graph search
- Quantum Counting: estimating the number of marked items using QPE + Grover
- Quantum Error Correction on the Yggdrasil QPU: comparing the Steane [[7,1,3]] code vs. the Shor [[9,1,3]] code under realistic noise
- Quantum Random Walk on a line and a cycle: comparing hitting times with classical random walks
- VQE for larger molecules (BeH₂, N₂) with noise mitigation on real hardware
- Quantum Money: implementing the Aaronson-Christiano quantum money scheme and analyzing its security
- Quantum State Discrimination: optimal measurement strategies for non-orthogonal states
- Quantum Zeno Effect: simulating frequent measurement dynamics and demonstrating Zeno stabilization
