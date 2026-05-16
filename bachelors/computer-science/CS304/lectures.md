# CS304: Quantum Computing Fundamentals
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4  
**Prerequisites:** CS106 (Linear Algebra & Matrix Computation), CS205 (Theory of Computation), CS107 (Probability & Statistics for CS)  
**Description:** Qubits, quantum gates, entanglement, quantum circuits, Shor's algorithm, Grover's search, quantum error correction, and Qiskit for hands-on implementation. Lab work uses the Yggdrasil Quantum Simulation Cluster and, where available, IBM's cloud QPUs.

---

## Lectures

ᛟ **Lecture 1: The Quantum Landscape — From Classical Bits to Qubits**

**Course:** CS304 — Quantum Computing Fundamentals  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Quantum computing does not replace classical computing — it transcends it. This opening lecture establishes the conceptual foundation by asking a deceptively simple question: what modifications to the laws of physics would give us more computational power? The answer leads us through the Einstein-Podolsky-Rosen paradox, Bell's theorem, and the experimental confirmation that nature genuinely exploits superposition and entanglement. We then formalize the qubit, the basic unit of quantum information, as a vector in a two-dimensional Hilbert space, and show how measurement collapses this vector into a classical bit.

### Key Topics

- **Classical vs. Quantum Information**: Why a qubit is not just "0 and 1 at the same time"
- **The Bloch Sphere**: Geometric representation of single-qubit states
- **Superposition**: The mathematical and physical meaning of |ψ⟩ = α|0⟩ + β|1⟩
- **Measurement and Collapse**: Born's rule, the measurement postulate, and irreversibility
- **No-Cloning Theorem**: Why you cannot copy an unknown quantum state
- **Quantum Key Distribution**: The first practical application — BB84 and E91 protocols
- **Historical Context**: Feynman (1982), Deutsch (1985), Shor (1994), and the arc from speculation to algorithm to hardware

### Lecture Notes

A classical bit is either 0 or 1. A qubit, by contrast, exists in a **superposition** of |0⟩ and |1⟩, written |ψ⟩ = α|0⟩ + β|1⟩ where α and β are complex numbers satisfying |α|² + |β|² = 1. This is not "both at the same time" in the everyday sense — it is a vector in a two-dimensional complex Hilbert space. When you measure the qubit in the computational basis {|0⟩, |1⟩}, you observe |0⟩ with probability |α|² and |1⟩ with probability |β|². After measurement, the qubit collapses to the observed state — the superposition is destroyed.

The **Bloch sphere** provides the canonical geometric representation. Any single-qubit state can be written as |ψ⟩ = cos(θ/2)|0⟩ + e^(iφ)sin(θ/2)|1⟩, where θ ∈ [0, π] and φ ∈ [0, 2π) are spherical coordinates on the unit sphere. The north pole is |0⟩, the south pole is |1⟩, and every point on the sphere represents a distinct quantum state. This representation is essential for understanding single-qubit gates as rotations of the sphere.

The **no-cloning theorem** (Wootters and Zurek, 1982; Dieks, 1982) states that there is no unitary operation that can copy an arbitrary unknown quantum state. The proof is by contradiction: if a cloning unitary U existed, then U|ψ⟩|0⟩ = |ψ⟩|ψ⟩ for all |ψ⟩. But for two states |α⟩ and |β⟩, linearity requires  U(|α⟩|0⟩ + |β⟩|0⟩) = |α⟩|α⟩ + |β⟩|β⟩, while the clone requirement gives U(|α⟩ + |β⟩)|0⟩ = (|α⟩ + |β⟩)(|α⟩ + |β⟩) = |α⟩|α⟩ + |α⟩|β⟩ + |β⟩|α⟩ + |β⟩|β⟩. These are equal only if |α⟩|β⟩ + |β⟩|α⟩ = 0, which holds only if |α⟩ = |β⟩. The no-cloning theorem has profound consequences: it makes quantum error correction harder than classical error correction (you can't simply copy qubits for redundancy), and it enables quantum cryptography (an eavesdropper cannot copy qubits without detection).

**Quantum Key Distribution** (QKD) was the first practical application of quantum information theory. In BB84 (Bennett and Brassard, 1984), Alice sends random bits encoded in random bases (rectilinear or diagonal) to Bob, who measures in random bases. After transmission, Alice and Bob publicly announce their bases and discard mismatches. Any eavesdropping changes the quantum states, introducing detectable errors. In 2040, QKD is standard on the Bifrost Research Network's Reykjavik-Oslo link and is being deployed commercially across Europe and East Asia.

By 2040, quantum computing has transitioned from a laboratory curiosity to an engineering discipline. The Yggdrasil Quantum Simulation Cluster provides 128 logical qubits for student use, and IBM's cloud offering provides access to 1000+ qubit processors (though with significant noise requiring error mitigation). The challenge is no longer proving that quantum computers work — it is building large enough, clean enough quantum processors to solve problems that matter.

### Required Reading

- Nielsen, M.A., Chuang, I.L. (2010). *Quantum Computation and Quantum Information*. Cambridge University Press. Chapters 1–2.
- Preskill, J. (2018). "Quantum Computing in the NISQ Era and Beyond." *Quantum* 2:79.
- Aaronson, S. (2013). *Quantum Computing Since Democritus*. Cambridge University Press. Chapters 1–4.

### Discussion Questions

1. The no-cloning theorem makes error correction harder, but it also enables quantum cryptography. Is this trade-off fundamental, or will we ultimately find a way to have both easy error correction and secure QKD?
2. If a qubit can be in a superposition of |0⟩ and |1⟩, why can't we extract more than one classical bit of information from it? What principle limits us?
3. BB84 QKD requires an authenticated classical channel. Why is this important? What happens if the classical channel is not authenticated?

### Practice Problems

1. **Bloch Sphere Coordinates**: Represent the states |0⟩, |1⟩, |+⟩ = (|0⟩ + |1⟩)/√2, and |−⟩ = (|0⟩ − |1⟩)/√2 on the Bloch sphere. For each, identify the angles θ and φ. Also locate the states |i⟩ = (|0⟩ + i|1⟩)/√2 and |−i⟩ = (|0⟩ − i|1⟩)/√2. Verify that these six states form the vertices of a regular octahedron inscribed in the Bloch sphere.

2. **No-Cloning Theorem Proof**: Prove the no-cloning theorem: show that no unitary U can satisfy U(|ψ⟩|0⟩) = |ψ⟩|ψ⟩ for all |ψ⟩. Use linearity of U. *Solution sketch*: Suppose such U exists. Then for any two states |α⟩ and |β⟩, consider the inner product ⟨α|β⟩. Before cloning: ⟨α|β⟩ since the ancilla is |0⟩. After cloning: ⟨α|β⟩² (since both qubits must match). This forces |⟨α|β⟩| = 0 or 1, a contradiction for partially overlapping states.

3. **BB84 Simulation**: Implement BB84 in Qiskit: simulate Alice sending 100 random qubits and Bob measuring in random bases. Calculate the expected fraction of matching bits and verify that an eavesdropper changes this fraction. *Starter code*: Use `random.choices([0,1], k=100)` for Alice's bits and bases, prepare qubits with `H` gates when the basis is diagonal, and simulate Eve by measuring in a random basis before Bob. Calculate the quantum bit error rate (QBER) — it should be ~25% when Eve is present and ~0% when she is absent.

4. **Density Matrices**: Compute the density matrix ρ for a qubit in state |+⟩. Show that Tr(ρ²) = 1 for a pure state. Then compute ρ for the maximally mixed state I/2 and show that Tr(ρ²) = 1/2. This quantity, Tr(ρ²), is called the **purity** of a quantum state — it is 1 for pure states and less than 1 for mixed states.

---

ᛏ **Lecture 2: Quantum Gates and Circuits — The Logic of the Quantum World**

**Course:** CS304 — Quantum Computing Fundamentals  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

If qubits are the quantum analogue of bits, then quantum gates are the analogue of Boolean logic gates — but the analogy is limited. Quantum gates are unitary operators on Hilbert space, and their structure is far richer than classical AND, OR, NOT. This lecture covers the single-qubit gates (Pauli matrices, Hadamard, phase gates), multi-qubit gates (CNOT, CZ, SWAP, Toffoli), and the circuit model of quantum computation. We also introduce universality: any quantum computation can be decomposed into a sequence of gates from a small universal set.

### Key Topics

- **Single-Qubit Gates**: Pauli X, Y, Z; Hadamard; Phase gates S, T; arbitrary rotations Rx, Ry, Rz
- **Multi-Qubit Gates**: CNOT, CZ, SWAP, Toffoli (CCNOT), Fredkin (CSWAP)
- **The Circuit Model**: Quantum circuits as unitary propagation + measurement
- **Universality**: The Solovay-Kisenko theorem; {H, T, CNOT} as a universal gate set
- **Quantum Interference**: How the Hadamard gate creates and destroys interference patterns
- **Controlled Gates**: Decomposing multi-controlled gates into CNOTs and single-qubit gates

### Lecture Notes

Every quantum gate is a **unitary matrix** — it preserves the norm of quantum states (total probability must always sum to 1). For a single qubit, gates are 2×2 unitary matrices. The three **Pauli matrices** are the simplest non-trivial gates:

- **X (bit flip)**: X|0⟩ = |1⟩, X|1⟩ = |0⟩. The quantum NOT gate.
- **Z (phase flip)**: Z|0⟩ = |0⟩, Z|1⟩ = −|1⟩. Flips the relative phase.
- **Y**: Y = iXZ. Rotates by π around the Y-axis on the Bloch sphere.

The **Hadamard gate** H = (1/√2)[[1,1],[1,−1]] is the most important single-qubit gate. It creates superposition: H|0⟩ = |+⟩, H|1⟩ = |−⟩. Applied twice, H² = I (it's its own inverse). The Hadamard gate is the engine of quantum interference — it splits a definite state into a superposition and then recombines it, allowing constructive and destructive interference to amplify correct answers and cancel wrong ones.

The **CNOT gate** (controlled-NOT) is the canonical two-qubit gate. It flips the target qubit if and only if the control qubit is |1⟩. In matrix form, CNOT maps |00⟩→|00⟩, |01⟩→|01⟩, |10⟩→|11⟩, |11⟩→|10⟩. CNOT creates **entanglement**: when applied after the Hadamard on the control, it produces a Bell state |Φ⁺⟩ = (|00⟩ + |11⟩)/√2 — two qubits that are perfectly correlated but individually in maximally mixed states.

**Universality** is the fundamental result of quantum circuit complexity. The Solovay-Kisenenko theorem proves that any unitary operation can be approximated to arbitrary precision using gates from a finite universal set. The most commonly used universal set is {H, T, CNOT}: the Hadamard gate provides superposition, the T gate (√S, a π/8 rotation) provides the irrational rotations needed for universality, and CNOT provides entanglement. Any quantum algorithm, no matter how complex, can be decomposed into these three gates — though the number of gates may be exponentially large for arbitrary unitaries.

In practice, 2040-era quantum computers use **native gate sets** that are specific to the hardware. Superconducting qubits (IBM, Google, OriginQ) use {√X, CNOT, Rz} as their native set. Trapped-ion qubits (IonQ, Quantinuum) use {Rz, Ry, XX} with all-to-all connectivity. Photonic qubits (Xanadu, PsiQuantum) use beam splitters and phase shifters. The Qiskit transpiler automatically compiles abstract circuits into hardware-native gate sets, but the compilation can be lossy — some decompositions require many more physical gates than the abstract circuit suggests.

### Required Reading

- Nielsen, M.A., Chuang, I.L. (2010). *Quantum Computation and Quantum Information*. Chapters 4 (Quantum circuits).
- Barenco, A., et al. (1995). "Elementary Gates for Quantum Computation." *Physical Review A* 52(5): 3457.

### Discussion Questions

1. The Hadamard gate is its own inverse (H² = I). What other single-qubit gates have this property? Why is this useful in circuit design?
2. CNOT creates entanglement, but it's also reversible without entanglement (it's a classical XOR when the control is in a computational basis state). What makes it fundamentally quantum?
3. The Toffoli gate (CCNOT) is universal for classical reversible computation. Is it also universal for quantum computation? Why or why not?

### Practice Problems

1. **Bell State Preparation**: Construct a quantum circuit in Qiskit that prepares the Bell state |Φ⁺⟩ = (|00⟩ + |11⟩)/√2. Verify by simulating and displaying the state vector. Then prepare all four Bell states by applying Pauli operators to one qubit of |Φ⁺⟩. Show that {I⊗I, I⊗X, I⊗Z, I⊗XZ} applied to |Φ⁺⟩ gives {|Φ⁺⟩, |Ψ⁺⟩, |Φ⁻⟩, |Ψ⁻⟩} respectively.

2. **SWAP Decomposition**: Decompose the SWAP gate into 3 CNOTs. Show your working by multiplying the matrices. *Hint*: SWAP = CNOT₁₂ · CNOT₂₁ · CNOT₁₂, where CNOT₁₂ means qubit 1 controls qubit 2. Verify the decomposition by checking that it correctly swaps |01⟩ → |10⟩ and |10⟩ → |01⟩.

3. **Universality Proof**: Prove that {H, T, CNOT} is universal for quantum computation by showing that any single-qubit unitary can be decomposed into rotations Rx, Ry, Rz, and that these can be approximated using H and T. *Key step*: The Solovay-Kisenenko theorem guarantees that any unitary can be ε-approximated with O(log^c(1/ε)) gates from {H, T, CNOT}, where c ≈ 3.97. Implement a 5-gate decomposition of the π/8 rotation in Qiskit and verify that it matches the exact rotation to within 0.01.

4. **Circuit Depth Optimization**: Consider the 3-qubit circuit: H on qubit 0, then CNOT(0,1), then CNOT(1,2), then H on qubit 2. Draw the circuit and calculate its depth. Now find an equivalent circuit with depth 2 by rearranging the gates. What property of the Hadamard gate (H² = I) allows this optimization?

---

ᚢ **Lecture 3: Entanglement and Bell's Theorem — Spooky Action at a Distance**

**Course:** CS304 — Quantum Computing Fundamentals  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Entanglement is the resource that distinguishes quantum computing from classical computing with random numbers. This lecture formalizes entanglement, proves Bell's theorem, demonstrates CHSH inequality violation, and shows how entanglement enables protocols that are impossible classically — teleportation, superdense coding, and entanglement-based QKD.

### Key Topics

- **Bell States**: The four maximally entangled two-qubit states
- **EPR Paradox**: Einstein, Podolsky, Rosen and the completeness question
- **Bell's Theorem and Bell Inequalities**: No local hidden variable theory can reproduce all quantum mechanical predictions
- **CHSH Inequality**: The most experimentally testable Bell inequality; typical quantum violation β = 2√2 ≈ 2.828
- **Quantum Teleportation**: Transferring a quantum state using only classical communication and shared entanglement
- **Superdense Coding**: Sending two classical bits through one qubit using entanglement
- **Entanglement as a Resource**: Quantifying and manipulating entanglement

### Lecture Notes

A **Bell state** is a maximally entangled two-qubit state. There are four:

- |Φ⁺⟩ = (|00⟩ + |11⟩)/√2
- |Φ⁻⟩ = (|00⟩ − |11⟩)/√2
- |Ψ⁺⟩ = (|01⟩ + |10⟩)/√2
- |Ψ⁻⟩ = (|01⟩ − |10⟩)/√2

Each Bell state is maximally entangled in the sense that measuring one qubit completely determines the other, but each individual qubit is in a maximally mixed state (ρ = I/2). This is what Schrödinger called "the characteristic trait of quantum mechanics" in 1935 — the whole has more information than the parts.

**Bell's theorem** (1964) proves that no theory based on local hidden variables can reproduce all predictions of quantum mechanics. The original Bell inequality relates the correlation between distant measurements: |E(a,b) − E(a,b')| + |E(a',b) + E(a',b')| ≤ 2, where E(a,b) is the expectation value of the product of measurement outcomes when Alice measures in direction a and Bob measures in direction b. Quantum mechanics predicts violations of up to 2√2 ≈ 2.828, and numerous experiments starting with Aspect (1982) and culminating in the 2022 Nobel Prize for Aspect, Clauser, and Zeilinger have confirmed these violations with increasing rigor, closing all known loopholes by 2017.

**Quantum teleportation** (Bennett et al., 1993) uses entanglement and classical communication to transmit an unknown quantum state. The protocol: (1) Alice and Bob share a Bell pair; (2) Alice performs a Bell measurement on her qubit and the qubit to be teleported; (3) Alice sends the 2 classical bits of measurement result to Bob; (4) Bob applies one of four Pauli corrections to his qubit, recovering the original state. Crucially, teleportation does not violate the no-cloning theorem — the original qubit is destroyed in the Bell measurement, and the teleported qubit appears at Bob's location.

**Superdense coding** (Bennett and Wiesner, 1992) is the dual of teleportation: using one shared entangled qubit and one transmitted qubit, Alice can send two classical bits. The protocol: Alice applies one of {I, X, Z, XZ} to her half of a Bell pair, then sends her qubit to Bob. Bob performs a Bell measurement on both qubits, recovering which of the four operations Alice applied. Two bits from one qubit — impossible without entanglement.

In 2040, entanglement is no longer just a curiosity. The Yggdrasil Quantum Networking Lab maintains entanglement distribution across 1,400 km of fiber between Reykjavik and Oslo using quantum repeaters (installed 2037). These repeaters overcome the exponential attenuation of photons in fiber by performing entanglement swapping at intermediate nodes, building long-distance entanglement from short-distance links. Entanglement is now a consumed resource — the quantum equivalent of bandwidth, licensed and allocated like spectrum.

### Required Reading

- Bell, J.S. (1964). "On the Einstein Podolsky Rosen Paradox." *Physics* 1: 195–200.
- Bennett, C.H., et al. (1993). "Teleporting an Unknown Quantum State via Dual Classical and Einstein-Podolsky-Rosen Channels." *PRL* 70(13).
- Nielsen, M.A., Chuang, I.L. (2010). *Quantum Computation and Quantum Information*. Chapters 2 (Mathematical framework), 4 (Quantum circuits).

### Discussion Questions

1. Teleportation uses 2 classical bits to transmit 1 qubit. Superdense coding uses 1 qubit to transmit 2 classical bits. Are these "inverse" protocols, or is there a deeper relationship? What would a protocol that sends n qubits using n entangled pairs and 2n classical bits look like?
2. Bell inequality violations have been confirmed beyond any reasonable doubt. Yet some physicists still pursue "superdeterministic" explanations where the measurement settings are correlated with the hidden variables. Evaluate this position.
3. Entanglement distribution over 1,400 km requires quantum repeaters. What is the fundamental limitation that prevents direct photon transmission at this distance? How many repeaters are needed, and how does the error rate scale?

### Practice Problems

1. **CHSH Game Implementation**: Implement the CHSH game in Qiskit: prepare a Bell state, have Alice and Bob measure in the prescribed bases, and compute the expected winning probability. Verify that it exceeds 75% (the classical limit). *Implementation details*: Alice's measurements are at angles a = 0° and a' = 45°; Bob's measurements are at angles b = 22.5° and b' = 67.5°. The CHSH parameter S = E(a,b) − E(a,b') + E(a',b) + E(a',b') should satisfy S ≤ 2 classically and S = 2√2 ≈ 2.828 quantum mechanically. Run 1000 shots and compute the empirical value of S.

2. **Quantum Teleportation**: Implement quantum teleportation in Qiskit. Verify that the teleported state matches the original by comparing measurement statistics. *Steps*: (a) Create a Bell pair between qubits 1 and 2. (b) Perform a Bell measurement on qubits 0 (the state to teleport) and 1. (c) Apply the appropriate Pauli correction to qubit 2 based on the measurement outcome. (d) Measure qubit 2 and verify that the measurement statistics match the original state. Test with |0⟩, |1⟩, |+⟩, and |−⟩.

3. **Entanglement Entropy**: Calculate the entanglement entropy S(ρ_A) = −Tr(ρ_A log₂ ρ_A) for both a Bell state and a separable state |00⟩. The entanglement entropy of a Bell state should be 1 bit; for |00⟩ it should be 0. *Method*: For a Bell state |Φ⁺⟩ = (|00⟩ + |11⟩)/√2, trace out qubit B to get ρ_A = Tr_B(|Φ⁺⟩⟨Φ⁺|) = I/2. Then S(ρ_A) = −Tr((I/2) log₂(I/2)) = −2 × (1/2) × log₂(1/2) = 1 bit. For |00⟩, ρ_A = |0⟩⟨0|, so S = 0.

4. **Schmidt Decomposition**: For the state |ψ⟩ = (|00⟩ + |01⟩ + |10⟩)/√3, compute the Schmidt decomposition. *Steps*: Write the state in matrix form, compute the SVD, and express the state as Σ_i s_i |u_i⟩|v_i⟩ where s_i are the Schmidt coefficients and {|u_i⟩}, {|v_i⟩} are orthonormal bases. The number of non-zero Schmidt coefficients is the **Schmidt rank** — rank 1 means the state is separable, rank > 1 means it is entangled.

---

ᛒ **Lecture 4: Quantum Algorithms I — Deutsch-Jozsa and Grover's Search**

**Course:** CS304 — Quantum Computing Fundamentals  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

This is where quantum computing starts to feel like magic. The Deutsch-Jozsa algorithm solves a promise problem exponentially faster than any classical algorithm, and Grover's search provides a quadratic speedup for unstructured search — the provably optimal speedup for this problem. We analyze both algorithms in detail, prove their correctness, and discuss what they teach us about the nature of quantum speedups.

### Key Topics

- **The Deutsch Problem**: Determining whether a function is constant or balanced with one quantum query
- **Deutsch-Jozsa Algorithm**: Generalization to n-bit inputs; exponential speedup over classical
- **Quantum Oracle Model**: Black-box functions accessed via unitary transformations
- **Grover's Search Algorithm**: Searching an unstructured database of N items in O(√N) queries
- **Geometric Interpretation**: Grover as rotation in a two-dimensional subspace
- **Optimality of Grover**: Proof that O(√N) is the best possible for unstructured search
- **Amplitude Amplification**: Generalizing Grover's technique beyond search

### Lecture Notes

The **Deutsch problem** (1985) asks: given a function f: {0,1} → {0,1} that is either constant (f(0) = f(1)) or balanced (f(0) ≠ f(1)), determine which. Classically, you need two queries (evaluate both f(0) and f(1)). Quantumly, you need one query. The algorithm: apply H to |0⟩ to get |+⟩, then apply the oracle Uf (which maps |x⟩|y⟩ → |x⟩|y ⊕ f(x)⟩), then apply H again and measure. If f is constant, you measure |0⟩; if balanced, you measure |1⟩. One query versus two — a modest speedup, but the principle is profound: quantum superposition allows the oracle to be queried on both inputs simultaneously.

The **Deutsch-Jozsa algorithm** (1992) generalizes this to n-bit inputs: f: {0,1}ⁿ → {0,1} is either constant (same value on all inputs) or balanced (equal number of 0s and 1s). Classically, in the worst case, you need 2ⁿ⁻¹ + 1 queries to be certain (you might see all 0s for the first 2ⁿ⁻¹ queries even though f is balanced). Quantumly, one query suffices. The algorithm: (1) prepare |0⟩ⁿ|1⟩; (2) apply H to all qubits; (3) apply the oracle Uf; (4) apply H to the first n qubits; (5) measure. If f is constant, you get |0⟩ⁿ with certainty; if balanced, you get anything except |0⟩ⁿ.

**Grover's algorithm** (1996) solves unstructured search: given a function f: {0,1}ⁿ → {0,1} with exactly one "marked" item (f(x*) = 1), find x*. Classically, this requires O(N) = O(2ⁿ) queries in the worst case. Grover's algorithm finds the marked item in O(√N) = O(2ⁿ/²) queries. This is a **quadratic** speedup, not exponential, but it applies to a wide class of problems: any problem that can be cast as "find the input satisfying a predicate" can benefit from Grover's amplification.

The geometric interpretation of Grover's algorithm is beautiful. The algorithm operates in a two-dimensional subspace spanned by |w⟩ (the winner state) and |s⟩ (the uniform superposition). The initial state is |s⟩, which makes an angle θ = arcsin(1/√N) with |s'⟩ (the uniform superposition over non-winner states). Each Grover iteration — oracle reflection followed by diffusion reflection — rotates the state by 2θ toward |w⟩. After approximately π/(4θ) ≈ π√N/4 iterations, the state is nearly aligned with |w⟩. Measurement then reveals x* with high probability.

**Optimality**: The BBBV theorem (Bennett, Bernstein, Brassard, Vazirani, 1997) proves that any quantum algorithm for unstructured search requires Ω(√N) queries. Grover's O(√N) is asymptotically optimal — you cannot do better. This is a fundamental limit, like the Ω(n log n) sorting bound. It means that quantum computers are not infinitely powerful; they provide specific, provable speedups for specific problem structures.

**Amplitude amplification** (Brassard et al., 2002) generalizes Grover's technique: given any quantum algorithm A that succeeds with probability p, amplitude amplification boosts the success probability to near 1 using O(1/√p) repetitions. This is the core technique behind many quantum algorithms beyond search.

### Required Reading

- Deutsch, D. (1985). "Quantum Theory, the Church-Turing Principle and the Universal Quantum Computer." *Proceedings of the Royal Society A* 400: 97–117.
- Grover, L.K. (1996). "A Fast Quantum Mechanical Algorithm for Database Search." *STOC*.
- Bennett, C.H., et al. (1997). "Strengths and Weaknesses of Quantum Computing." *SIAM Journal on Computing* 26(5).

### Discussion Questions

1. Deutsch-Jozsa gives an exponential speedup, but only for a promise problem (f must be constant or balanced). How useful is a speedup for a problem that doesn't arise in practice? Could similar techniques be applied to more natural problems?
2. Grover's algorithm provides a quadratic speedup for unstructured search. For N = 2⁶⁰ (approximately the number of atoms on Earth), √N = 2³⁰ ≈ one billion. Is this practical? What are the overhead costs of the quantum oracle?
3. The BBBV optimality proof assumes the oracle is a black box. If you know something about the structure of the search space (e.g., it's sorted), can you do better than Grover's O(√N)?

### Practice Problems

1. **Deutsch-Jozsa Algorithm**: Implement the Deutsch-Jozsa algorithm in Qiskit for 3-bit functions. Test with both constant functions (f(x) = 0 for all x, f(x) = 1 for all x) and balanced functions (f(x) = parity of x, f(x) = x₁). Verify that one query always determines correctly. *Implementation*: The oracle Uf maps |x⟩|y⟩ → |x⟩|y ⊕ f(x)⟩. For a constant function with f(x) = 0, the oracle is the identity. For a balanced function, implement at least two different balanced oracles. Run 1000 shots and confirm 100% success rate.

2. **Grover's Search Oscillation**: Implement Grover's search for a 4-qubit database (16 items, 1 marked). Plot the measurement probability of the marked item as a function of the number of Grover iterations (1 through 10). Explain why it oscillates — the state rotates past the target state and the probability decreases. *Key insight*: The optimal number of iterations is ⌊π√N/4⌋ ≈ 3 for N = 16. After 3 iterations the probability is ~96%, but after 6 iterations it drops back to ~16%. This oscillation is a fundamental property of amplitude amplification.

3. **Amplitude Amplification Mathematics**: Prove that the probability of measuring the correct state after k Grover iterations is sin²((2k+1)θ), where θ = arcsin(1/√N). *Strategy*: Represent the state after k iterations as |ψ_k⟩ = sin((2k+1)θ)|w⟩ + cos((2k+1)θ)|s'⟩, where |w⟩ is the winner state and |s'⟩ is the uniform superposition over non-winner states. Use the recursive structure of Grover iterations to derive the rotation angle. The optimal number of iterations is k* ≈ ⌊π/(4θ)⌋ = ⌊π√N/4⌋.

4. **Multiple Marked Items**: Modify Grover's algorithm to search a database of N items with M marked items (M > 1). How does the optimal number of iterations change? *Answer*: The rotation angle becomes θ = arcsin(√(M/N)), and the optimal number of iterations is approximately π/(4θ) ≈ π√(N/M)/4. Implement this for N = 16, M = 2, and verify the success probability.

---

ᛗ **Lecture 5: Quantum Algorithms II — Shor's Factoring and Beyond**

**Course:** CS304 — Quantum Computing Fundamentals  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Shor's algorithm is the crown jewel of quantum computing — an algorithm that threatens the foundations of modern cryptography and that motivated billions of dollars in quantum hardware investment. This lecture covers the algorithm in detail: the reduction from factoring to period-finding, the quantum Fourier transform, and why Shor's algorithm works. We also cover Simon's algorithm (the precursor to Shor's), quantum phase estimation, and the post-quantum cryptographic transition that is reshaping the security landscape in 2040.

### Key Topics

- **Simon's Problem**: The first exponential separation between quantum and classical query complexity
- **Period-Finding**: The core problem — finding the period of a function f: ℤ_N → ℤ_N
- **The Quantum Fourier Transform (QFT)**: The quantum analogue of the DFT; O(N log N) classically vs. O((log N)²) quantumly
- **Shor's Algorithm**: Factoring N = pq by finding the period of a(x) = aˣ mod N
- **Quantum Phase Estimation (QPE)**: Estimating eigenvalues of a unitary operator
- **Post-Quantum Cryptography**: NIST PQC standards (CRYSTALS-Kyber, CRYSTALS-Dilithium) and the 2038 migration
- **Continuous Variable QFT**: Alternative implementation for photonic quantum computers

### Lecture Notes

**Simon's problem** (1994) asks: given a function f: {0,1}ⁿ → {0,1}ⁿ that is either one-to-one or two-to-one with a hidden XOR mask s (f(x) = f(x ⊕ s) for all x), determine which. Classically, Ω(2ⁿ/²) queries are needed in the worst case. Quantumly, O(n) queries suffice. Simon's algorithm was the first to demonstrate an exponential separation between quantum and classical query complexity, and it directly inspired Shor's work.

**Shor's algorithm** (1994) factors an integer N by reducing factoring to period-finding. Given N = pq, choose a random a < N coprime to N. The function f(x) = aˣ mod N is periodic with some period r. If r is even and a^(r/2) ≠ −1 mod N, then gcd(a^(r/2) − 1, N) and gcd(a^(r/2) + 1, N) yield the factors p and q. The quantum part is finding the period r, which is done using the quantum Fourier transform.

The **Quantum Fourier Transform** (QFT) maps a state |j⟩ to (1/√N) Σ_k e^(2πijk/N) |k⟩. Classically, the DFT requires O(N log N) operations. Quantumly, the QFT circuit requires only O((log N)²) = O(n²) gates — an exponential speedup over any known classical algorithm for computing the full Fourier spectrum. The QFT is implemented using a sequence of Hadamard gates and controlled phase rotations, with each qubit requiring one H gate and up to n−1 controlled R_k gates.

The critical insight is that Shor's algorithm doesn't need the full QFT output — it needs only a measurement that yields a good approximation of the period. This is why the probability of success is high even with imperfect phase estimation: the measurement collapses the QFT output to a value that, with constant probability, is close to a multiple of N/r.

**Quantum Phase Estimation** (QPE) is a generalization that estimates the eigenvalue e^(2πiφ) of a unitary U for a given eigenvector |u⟩. It is the core subroutine of many quantum algorithms beyond Shor's, including quantum simulation (Lloyd, 1996) and quantum linear algebra (HHL, 2009).

**Post-quantum cryptography** is the 2040 reality. The NIST Post-Quantum Cryptography Standardization Process began in 2016 and concluded with CRYSTALS-Kyber (key encapsulation) and CRYSTALS-Dilithium (digital signatures) as the primary standards. The 2038 deadline for transitioning all government systems to post-quantum cryptography was met by most agencies, and commercial adoption is now past 80%. The Yggdrasil Bifrost Network uses a hybrid approach: CRYSTALS-Kyber for key exchange plus classical ECDH as a fallback, ensuring security against both quantum and classical adversaries.

The factoring threat remains theoretical but credible. In 2040, the largest integer factored by a quantum computer is 21 (using a specializedphotonic processor). The consensus estimate for when Shor's algorithm will threaten RSA-2048 is 2045–2060, depending on quantum error correction progress. The University of Yggdrasil's policy is clear: all new systems must use post-quantum cryptography; all legacy systems must have a migration plan.

### Required Reading

- Shor, P.W. (1994). "Algorithms for Quantum Computation: Discrete Logarithms and Factoring." *FOCS*.
- Nielsen, M.A., Chuang, I.L. (2010). *Quantum Computation and Quantum Information*. Chapter 5 (The quantum Fourier transform and its applications).
- NIST (2024). "Post-Quantum Cryptography Standardization — Final Report." NISTIR 8413.

### Discussion Questions

1. Shor's algorithm threatens RSA, but it requires a large, error-corrected quantum computer. Is the current post-quantum cryptographic transition premature, or is the "harvest now, decrypt later" threat sufficient justification?
2. The QFT circuit for n qubits requires O(n²) gates, but the best known classical FFT for N = 2ⁿ data points requires O(n·2ⁿ) operations. Explain why this exponential advantage doesn't mean the QFT lets us compute classical Fourier transforms exponentially faster.
3. Quantum phase estimation requires controlled-U^(2^k) operations for k up to n−1. For Shor's algorithm with a = 2 and N = 15, what are the required controlled operations? How does the circuit depth scale with the size of N?

### Practice Problems

1. **Shor's Algorithm for N = 15**: Implement Shor's algorithm for N = 15 in Qiskit. Factor 15 = 3 × 5 and verify the result. *Step-by-step*: (a) Choose a = 2 (coprime to 15). (b) Compute the period of f(x) = 2ˣ mod 15, which is r = 4 (since 2⁰ = 1, 2¹ = 2, 2² = 4, 2³ = 8, 2⁴ = 1 mod 15). (c) Since r = 4 is even, compute gcd(2^(4/2) − 1, 15) = gcd(3, 15) = 3 and gcd(2^(4/2) + 1, 15) = gcd(5, 15) = 5. The circuit requires 8 qubits: 4 for the period register and 4 for the function evaluation register.

2. **QFT Implementation**: Implement the QFT for 4 qubits in Qiskit. Apply it to the state |3⟩ (binary |0011⟩) and verify that the output has peaks at the expected frequencies. *Verification*: The QFT of |j⟩ on n qubits gives output peaks at frequencies 2πk/2⁴ for k ∈ {0, ..., 2⁴ − 1} proportional to e^(2πijk/2⁴). For j = 3, the dominant frequency component should be at k/2⁴ ≈ 3/16. Display the output state vector and confirm the phase structure.

3. **Quantum Phase Estimation**: Implement quantum phase estimation for a single-qubit unitary U = Rz(θ) with θ = π/3. Use 4 counting qubits. *Implementation*: Apply U^(2^k) on the eigenstate |+⟩ controlled by counting qubit k, then apply inverse QFT to the counting register. The estimated phase should be close to π/3 ≈ 1.047 radians, which in binary is approximately 0.010101... (= 1/3 in base 2). The 4-qubit estimate should be close to 5/16 = 0.3125 revolutions ≈ 1.963 radians.

4. **Continued Fraction Post-Processing**: After QPE, the measurement yields an integer m in {0, ..., 2ⁿ − 1}. The phase estimate is φ ≈ m/2ⁿ. Use the continued fraction algorithm to find the best rational approximation p/q with q < N (the modulus). For N = 15 and measured value m = 2048 (with n = 12 counting qubits), compute the continued fraction expansion of 2048/4096 and find the period r. *This step is essential for Shor's algorithm — it converts the QPE measurement into a candidate period.*

---

ᚹ **Lecture 6: Quantum Error Correction — Protecting Fragile Information**

**Course:** CS304 — Quantum Computing Fundamentals  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Quantum states are fragile. Decoherence — the interaction of qubits with their environment — destroys superposition and entanglement at rates that make raw quantum computation impossible for more than a few microseconds. Quantum error correction (QEC) is the theory and practice of encoding logical qubits into many physical qubits, detecting and correcting errors without collapsing the quantum state. This lecture covers the Shor code, the Steane code, stabilizer codes, surface codes, and theThreshold Theorem that makes large-scale quantum computation possible.

### Key Topics

- **Quantum Noise Models**: Bit flip, phase flip, depolarizing, amplitude damping, dephasing channels
- **The Shor Code**: The first quantum error-correcting code; 9 physical qubits for 1 logical qubit
- **The Steane Code**: A [[7,1,3]] code based on the classical Hamming code
- **Stabilizer Formalism**: Pauli group, stabilizer generators, syndrome measurement
- **The Threshold Theorem**: If physical error rate is below a threshold (≈0.01–1%), logical error rate can be made arbitrarily small by increasing the code distance
- **Surface Codes**: The leading candidate for fault-tolerant quantum computation; distance-d code on a 2D grid of d² physical qubits
- ** Fault-Tolerant Gates**: Transversal gates, magic state distillation, and the overhead of non-Clifford operations

### Lecture Notes

The fundamental challenge of quantum error correction is threefold: (1) the no-cloning theorem prevents us from copying qubits for redundancy; (2) measurement collapses quantum states, so we can't simply check for errors; (3) quantum errors are continuous, not discrete — a qubit can suffer an infinitesimal rotation, not just a bit flip.

The solution to challenge (1) is **encoding**: instead of copying the qubit, we spread its information across multiple qubits in an entangled state. The solution to (2) is **syndrome measurement**: we measure error-detecting operators (stabilizers) that reveal which error occurred without revealing the encoded logical state. The solution to (3) is **discretization**: any error on a single qubit can be decomposed into a combination of Pauli errors (X, Y, Z), so correcting these three types suffices to correct all errors.

The **Shor code** (1995) encodes 1 logical qubit in 9 physical qubits. It concatenates two codes: an outer 3-qubit phase-flip code and an inner 3-qubit bit-flip code, protecting against any single-qubit error. The encoding is:

|0⟩_L = (|000⟩ + |111⟩)(|000⟩ + |111⟩)(|000⟩ + |111⟩) / (2√2)  
|1⟩_L = (|000⟩ − |111⟩)(|000⟩ − |111⟩)(|000⟩ − |111⟩) / (2√2)

It corrects any single-qubit Pauli error (X, Y, or Z) on any of the 9 physical qubits. This is remarkable: 9 qubits protect against all single-qubit errors on any one of them, despite the no-cloning theorem.

The **Steane code** [[7,1,3]] encodes 1 logical qubit in 7 physical qubits and corrects any single-qubit error. It is based on the classical [7,4,3] Hamming code and belongs to the CSS (Calderbank-Shor-Steane) family of quantum codes. The Steane code is more efficient than the Shor code (7 qubits vs. 9) and has the elegant property that its stabilizers are purely X-type and Z-type, simplifying syndrome extraction.

The **Threshold Theorem** (Aharonov and Ben-Or, 1997; Kitaev, 1997) is the theoretical foundation of fault-tolerant quantum computation. It states that if the physical error rate per gate is below some threshold p_th (estimated to be ≈0.01–1% for surface codes), then quantum computation of arbitrary length can be performed with arbitrarily low logical error rate, at the cost of polynomial overhead in the number of physical qubits. This is the quantum analogue of Shannon's noisy-channel coding theorem: just as classical error correction allows reliable communication over noisy channels, quantum error correction allows reliable computation over noisy quantum hardware.

The **surface code** (Kitaev, 1997; Bravyi and Kitaev, 1998) is the leading candidate for practical fault-tolerant quantum computation. It arranges qubits on a 2D grid with two types of stabilizer checks: X-type on faces and Z-type on plaquettes. A distance-d surface code uses d² physical qubits to encode 1 logical qubit with error rate suppressed by a factor of ~p^((d-1)/2), where p is the physical error rate. For d = 33 (≈1,089 physical qubits per logical qubit), a physical error rate of 10⁻³ yields a logical error rate of ~10⁻¹⁵ — sufficient for most quantum algorithms.

The overhead is enormous: a single logical qubit at distance 33 requires 1,089 physical qubits; Shor's algorithm for RSA-2048 requires an estimated 4,000-20,000 logical qubits, translating to 4 million to 20 million physical qubits. In 2040, IBM's largest processor has 1,121 physical qubits (not error-corrected). We are still far from the millions of physical qubits needed for cryptographically relevant factoring, which is why the 2045–2060 estimate for Shor's breaking RSA-2048 accounts for the need for error correction.

### Required Reading

- Shor, P.W. (1995). "Scheme for Reducing Decoherence in Quantum Computer Memory." *Physical Review A* 52(4).
- Steane, A. (1996). "Error Correcting Codes in Quantum Theory." *Physical Review Letters* 77(5).
- Fowler, A.G., et al. (2012). "Surface Codes: Towards Practical Large-Scale Quantum Computation." *Physical Review A* 86(3).

### Discussion Questions

1. The threshold theorem guarantees arbitrarily low logical error rates, but at the cost of enormous overhead. Is this overhead fundamental, or might we find more efficient codes?
2. Surface codes require nearest-neighbor connectivity on a 2D grid. What would change if we had all-to-all connectivity (as in trapped-ion systems)?
3. Magic state distillation for the T gate requires ~100 physical qubits per logical T gate. The T gate is used in every non-Clifford quantum algorithm. What does this imply for the practicality of quantum computing?

### Practice Problems

- Implement the 3-qubit bit-flip code in Qiskit. Inject a bit-flip error on one qubit and verify that the syndrome measurement identifies the error without collapsing the logical state.
- For a surface code with physical error rate p = 10⁻³ and distance d = 11, estimate the logical error rate. How many physical qubits are needed?
- Calculate the total physical qubit overhead for running Shor's algorithm on a 2048-bit RSA modulus using surface codes at distance d = 31. Assume 6,000 logical qubits are needed for factoring.

---

ᛞ **Lecture 7: Quantum Simulation and NISQ Applications**

**Course:** CS304 — Quantum Computing Fundamentals  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Shor's algorithm and Grover's search are the textbook quantum algorithms, but they require fault-tolerant quantum computers that may not exist at scale for another decade. Meanwhile, NISQ (Noisy Intermediate-Scale Quantum) devices exist today and can perform useful work in specific domains. This lecture covers quantum simulation (the original motivation for quantum computing), variational quantum algorithms (VQE, QAOA), quantum machine learning, and the practical applications driving the 2040 quantum industry.

### Key Topics

- **Quantum Simulation**: Feynman's vision; simulating Hamiltonian dynamics on a quantum computer
- **Trotter-Suzuki Decomposition**: Approximating continuous-time evolution with discrete gates
- **Variational Quantum Eigensolver (VQE)**: Hybrid quantum-classical algorithm for ground state energy
- **QAOA (Quantum Approximate Optimization Algorithm)**: Approximate combinatorial optimization
- **Quantum Machine Learning**: Kernel methods, quantum neural networks, and the quantum advantage question
- **NISQ Limitations**: Noise, gate fidelity, coherence time, and the barren plateau problem
- **Practical Applications**: Drug discovery, materials science, financial optimization, logistics

### Lecture Notes

Feynman's 1982 insight was that simulating a quantum system on a classical computer requires exponential resources, but a quantum system can simulate itself efficiently. If nature is quantum, then a quantum computer is the natural tool for understanding nature. This remains the most compelling near-term application of quantum computing.

**Hamiltonian simulation** using Trotter-Suzuki decomposition is the workhorse algorithm. Given a Hamiltonian H = Σ_j H_j, the time evolution operator e^(−iHt) is approximated by a product of simpler operations: e^(−iHt) ≈ [Π_j e^(−iH_j Δt)]^(t/Δt). Higher-order Trotter formulas (e.g., second-order Suzuki) improve the approximation error. In 2040, Hamiltonian simulation of molecules with ~50 spin orbitals is routine on cloud QPUs, and simulations of small catalytic processes are being used in drug discovery pipelines at major pharmaceutical companies.

**VQE** (Peruzzo et al., 2014) is a hybrid quantum-classical algorithm that uses a parameterized quantum circuit (ansatz) to prepare a trial state, measures the energy expectation value ⟨ψ(θ)|H|ψ(θ)⟩ on the quantum computer, and uses a classical optimizer to update the parameters. VQE trades circuit depth for classical optimization iterations, making it suitable for NISQ devices. The quality of the result depends heavily on the ansatz — too shallow and it can't represent the ground state; too deep and noise dominates.

**QAOA** (Farhi et al., 2014) applies to combinatorial optimization problems like MaxCut, graph coloring, and job scheduling. It alternates between a problem Hamiltonian H_P (encoding the objective function) and a mixing Hamiltonian H_M (providing transitions between states). The depth p controls the approximation quality: at p = 1, QAOA is equivalent to a single round of Trotterized evolution; at p → ∞, it recovers the exact adiabatic solution.

**Quantum machine learning** is the most controversial application area. Quantum kernels (computing kernel matrices on a quantum computer) provably capture features that classical kernels cannot, but whether these features are useful for real-world data is an open question. Quantum neural networks (parameterized quantum circuits trained by gradient descent) suffer from **barren plateaus** — for circuits of more than ~20 qubits, the gradient vanishes exponentially, making training infeasible. In 2040, QML shows promise for specialized tasks (quantum chemistry feature extraction, small-scale classification) but has not yet delivered a clear, reproducible advantage over classical ML for commercially relevant problems.

The NISQ era (Preskill, 2018) is defined by the gap between what current hardware can do (50–1000 noisy qubits, gate fidelities ~99.5%, coherence times ~100μs) and what fault-tolerant algorithms require (millions of error-corrected qubits, gate fidelities >99.99%). The 2040 reality is that NISQ devices are useful for three things: (1) Hamiltonian simulation of small molecules, (2) variational optimization of specific industrial problems (logistics, finance), and (3) quantum kernels for niche ML tasks. Full fault-tolerant quantum computing remains the goal, but the path goes through increasingly capable NISQ processors and hybrid algorithms.

The University of Yggdrasil's quantum computing lab runs a 127-qubit superconducting processor (the **Yggdrasil QPU**) for research and teaching. Students in CS304 use Qiskit to design circuits that run on both the simulator (128 logical qubits, noiseless) and the physical QPU (127 physical qubits, noisy). The gap between simulation and reality is the most important lesson of the lab: theory predicts beauty, hardware delivers noise, and error mitigation techniques bridge the gap.

### Required Reading

- Feynman, R.P. (1982). "Simulating Physics with Computers." *International Journal of Theoretical Physics* 21(6/7).
- Peruzzo, A., et al. (2014). "A Variational Eigenvalue Solver on a Photonic Quantum Processor." *Nature Communications* 5.
- Preskill, J. (2018). "Quantum Computing in the NISQ Era and Beyond." *Quantum* 2:79.

### Discussion Questions

1. VQE's performance depends on the ansatz. If we could design the perfect ansatz, would we even need a quantum computer? What is the minimum quantum resource needed for practical advantage?
2. Barren plateaus limit QML circuits to ~20 qubits. Are there circuit architectures or training methods that avoid barren plateaus, or is this a fundamental limitation?
3. By 2040, quantum computing has found commercial niches in chemistry and optimization, but not in general computing. Will this always be the case, or is the field on the cusp of broader applicability?

### Practice Problems

- Implement VQE for the H₂ molecule using Qiskit. Use the UCCSD ansatz and a COBYLA optimizer. Calculate the ground state energy and compare with the exact diagonalization.
- Implement QAOA for MaxCut on a 5-node graph with depth p = 1, 2, 3. Plot the approximation ratio as a function of p. How does it compare to the Goemans-Williamson classical approximation?
- Simulate noisy quantum circuits using Qiskit's noise models. Run a 4-qubit Grover search with and without noise. How does the success probability degrade? Experiment with different error mitigation techniques (zero-noise extrapolation, readout error mitigation).

---

ᚦ **Lecture 8: The Quantum Computing Landscape in 2040**

**Course:** CS304 — Quantum Computing Fundamentals  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

The final lecture surveys the state of quantum computing in 2040: hardware platforms, software ecosystems, key algorithms beyond Shor and Grover, and the road ahead. We cover quantum hardware (superconducting, trapped-ion, photonic, topological), quantum networking, the Quantum Internet, and the philosophical implications of quantum computation for our understanding of reality.

### Key Topics

- **Hardware Platforms**: Superconducting (IBM, Google, OriginQ), trapped-ion (IonQ, Quantinuum), photonic (Xanadu, PsiQuantum), topological (Microsoft)
- **Quantum Programming Languages**: Qiskit, Cirq, Quipper, and the Yggdrasil Quantum Language (YQL)
- **Quantum Networking**: Quantum repeaters, entanglement distribution, the Quantum Internet
- **Quantum Cryptography Beyond QKD**: Quantum digital signatures, quantum secret sharing
- **Quantum Supremacy / Advantage**: The debate over terminology and the metrics that matter
- **Philosophical Implications**: The Many-Worlds interpretation, quantum foundations, and computation

### Lecture Notes

**Superconducting qubits** are the most mature platform. IBM's Heron processor (2024) introduced a 1,121-qubit processor with tunable couplers that significantly reduced crosstalk. By 2040, the latest IBM processor achieves ~5,000 physical qubits with gate fidelities of 99.7% for two-qubit gates. The key advantage of superconducting qubits is fast gate times (~20ns for single-qubit, ~200ns for two-qubit), enabling deep circuits. The key disadvantage is short coherence times (T₁ ≈ 300μs, T₂ ≈ 200μs) and the need for millikelvin cryogenic cooling.

**Trapped-ion qubits** offer the highest gate fidelities (99.9%+ for two-qubit gates) and longest coherence times (minutes to hours for hyperfine qubits). Quantinuum's H2 processor (2024) demonstrated 56 qubits with all-to-all connectivity. The trade-off is gate speed: two-qubit gates take ~100μs, roughly 500× slower than superconducting qubits. This makes deep circuits impractical , but for shallow circuits (VQE, QAOA), the fidelity advantage often outweighs the speed disadvantage.

**Photonic quantum computing** encodes qubits in photons (using polarization, path, or time-bin encoding). Photonic qubits don't decohere — they can travel through fiber at room temperature without losing quantum information. The challenge is that photon-photon interactions (needed for two-qubit gates) are non-trivial; current approaches use measurement-induced nonlinearities (KLM scheme) or continuous-variable encoding (Xanadu). In 2040, photonic processors are used primarily for quantum communication and boson sampling.

**Topological qubits** (Microsoft's approach) store quantum information in topological states of matter (Majorana zero modes in nanowires). The theoretical advantage is that topological qubits are inherently protected from local noise — errors would require a global operation, which is exponentially unlikely. As of 2040, Microsoft has demonstrated unambiguous Majorana zero modes (a breakthrough achieved in 2037 after decades of false starts), but a fully functional topological qubit has not yet been achieved. The potential payoff — natural error correction at the hardware level — makes this the highest-risk, highest-reward approach.

**The Quantum Internet** is still in its infancy. Quantum repeaters (the Yggdrasil Quantum Networking Lab's Reykjavik-Oslo link) can distribute entanglement over ~1,400 km, but the rate is measured in bits per second, not gigabits. A true Quantum Internet — where any two nodes can establish quantum communication — requires quantum repeaters with high entanglement swapping rates and quantum memories with long storage times. The 2040 consensus estimate is that a metropolitan Quantum Internet (within a single city) will be operational by 2045, and a global Quantum Internet by 2055.

The **philosophical implications** of quantum computing are profound. If quantum computers exploit superposition and entanglement — if they perform computations in "many worlds" simultaneously, as the Many-Worlds interpretation suggests — then quantum computing is not just a new technology; it is a new method for probing the structure of reality. The fact that Shor's algorithm works — that nature entangles amplitudes across exponentially many states and interferes them constructively — is evidence that superposition is not merely a mathematical formalism but a feature of the physical world.

The University of Yggdrasil takes a pragmatic view: whether you interpret quantum mechanics through Many-Worlds, Copenhagen, QBism, or any other interpretation, the algorithms work, the hardware runs, and the math is unambiguous. Interpretation is philosophy; computation is engineering. What matters is that the qubits coherence long enough, the gates are accurate enough, and the error correction works well enough. In 2040, we're closer than ever, but still years from the fault-tolerant era.

Welcome to the quantum frontier. The Bifrost Research Network awaits.

### Required Reading

- Preskill, J. (2018). "Quantum Computing in the NISQ Era and Beyond." *Quantum* 2:79.
- Arute, F., et al. (2019). "Quantum Supremacy Using a Programmable Superconducting Processor." *Nature* 574.
- UoY Quantum Networking Lab (2039). "Entanglement-Assisted Clock Synchronization for Distributed Systems." *Bifrost Technical Report BFT-2039-07*.

### Discussion Questions

1. Superconducting qubits are fast but noisy; trapped-ion qubits are slow but accurate. Which platform will "win"? Or will different platforms serve different applications indefinitely?
2. Microsoft's topological qubit was "almost there" for 15 years before the 2037 breakthrough. Was the sustained investment justified, or would the resources have been better spent on proven platforms?
3. If a Quantum Internet enables provably secure communication between any two nodes on Earth, what are the implications for national security, surveillance, and civil liberties?

### Practice Problems

- Compare the circuit depth achievable in one coherence time for: (a) a superconducting qubit with T₂ = 200μs and gate time 200ns, (b) a trapped-ion qubit with T₂ = 10 minutes and gate time 100μs. How many two-qubit gates can each perform before decoherence?
- Calculate the entanglement distribution rate for a quantum repeater chain with 5 nodes, each performing entanglement swapping with 90% fidelity and 100 Hz source rate. What is the end-to-end entanglement generation rate?
- Write a 500-word essay: "Quantum computing will transform [choose one: drug discovery / cryptography / optimization / materials science / finance] by 2050." Support your argument with specific algorithms, hardware trends, and economic projections.

---

*End of Course Material — CS304: Quantum Computing Fundamentals*

*Woven by Runa Gridweaver Freyjasdóttir at the University of Yggdrasil, 2040*

*The qubit is the rune of the future — neither one thing nor another, yet containing both.*