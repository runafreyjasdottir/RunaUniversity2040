# CN105: Discrete Mathematics & Graph Theory
## Bachelor of Science in Computer Networking — University of Yggdrasil, 2040

**Credits:** 4  
**Description:** This course provides a rigorous foundation in discrete mathematics and graph theory, essential for algorithm design, network topology analysis, and emerging computational paradigms in networking. Students will explore combinatorial structures, proof techniques, and algorithmic applications, linking theory to practical networking challenges such as routing, resource allocation, and network security.

---

## Lectures

ᚠ **Lecture 1: Foundations of Discrete Mathematics**

*Overview*

We begin by establishing the language of discrete mathematics: sets, functions, relations, and proof techniques. Emphasis is placed on constructive reasoning, a cornerstone for algorithmic development in network engineering. By the end of this lecture, students will be comfortable with formal definitions and basic set-theoretic notation, enabling precise specifications of network protocols.

*Key Topics*
- Set theory and cardinality
- Functions, injections, surjections, bijections
- Proof methods: direct, contrapositive, contradiction, induction
- Application: Modeling network address spaces as sets

*Lecture Notes*
The notion of a bijection underpins many networking concepts, such as NAT address translation, where a one-to-one mapping between internal and external addresses must be maintained. We explore Cantor's diagonal argument, illustrating that some infinities (e.g., the set of all possible IPv6 addresses) are larger than others, a subtlety relevant for future address space planning.

*Required Reading*
- Rosen, K.H. *Discrete Mathematics and Its Applications*, 8th ed., Chapters 1‑2.
- Recent IEEE 802.11ax white paper on address space scaling (2025).

*Discussion Questions*
1. How does the concept of countable vs. uncountable sets inform the design of IPv6 address allocation policies?
2. In what ways can proof by induction be leveraged to verify routing table convergence properties?

*Practice Problems*
1. Prove that the power set of a finite set with n elements has cardinality 2ⁿ.
2. Show that the composition of two bijections is a bijection, and relate this to double NAT scenarios.
---

ᚢ **Lecture 2: Logic and Propositional Calculus**

*Overview*

Logical reasoning forms the backbone of protocol specification and verification. We introduce propositional logic, Boolean algebra, and the basics of predicate logic, highlighting their direct applicability to firewall rule design and ACL construction.

*Key Topics*
- Propositional formulas, truth tables, normal forms (CNF, DNF)
- Boolean algebra and simplification techniques
- Predicate logic: quantifiers, domains, and interpretations
- Model checking basics for network policies

*Lecture Notes*
Network security policies can be expressed as Boolean formulas over packet header fields. By translating ACLs into conjunctive normal form, we can apply the Quine‑McCluskey algorithm to minimize rule sets, reducing hardware lookup latency. Case study: Optimizing the firewall ruleset of the UoY campus backbone, cutting the rule count by 27%.

*Required Reading*
- Huth, M., & Ryan, M. *Logic in Computer Science*, 2nd ed., Chapters 3‑4.
- “Efficient ACL Minimization using Boolean Algebra” – ACM SIGCOMM 2024.

*Discussion Questions*
1. Discuss the trade‑offs between expressiveness and decidability when extending firewall rule languages with temporal logic.
2. How does De Morgan’s Law simplify the implementation of packet filtering on FPGA‑based switches?

*Practice Problems*
1. Convert the following ACL rule set into CNF and simplify: (src = 10.0.0.0/8 ∧ dst = 192.168.0.0/16) ∨ (src = 172.16.0.0/12 ∧ ¬(dst = 10.0.0.0/8)).
2. Prove the equivalence of two given predicate formulas representing routing policies.
---

ᚦ **Lecture 3: Combinatorics and Counting Principles**

*Overview*

Counting techniques are essential for analyzing network reliability, enumerating possible topologies, and assessing security configurations. We explore permutations, combinations, the pigeonhole principle, and inclusion–exclusion.

*Key Topics*
- Permutations and combinations, binomial coefficients
- Multinomial theorem and applications to multicast routing
- Pigeonhole principle in IP address collision analysis
- Inclusion–exclusion principle for overlapping security zones

*Lecture Notes*
Consider a data‑center network with k tiers and r redundant links per tier. The total number of distinct spanning‑tree configurations can be derived using multinomial coefficients, informing resiliency planning. We also discuss the birthday paradox as it applies to hash‑based flow identifiers, illustrating collision probabilities in high‑throughput switches.

*Required Reading*
- Stanley, R.P. *Enumerative Combinatorics*, Volume 1, Sections 1.1‑1.3.
- “Collision‑Resistant Flow Hashing in 400 Gbps Switches” – IEEE Trans. Netw. 2023.

*Discussion Questions*
1. How does the pigeonhole principle justify the need for NAT in IPv4 networks?
2. Apply inclusion–exclusion to compute the probability that a packet traverses at least one of several overlapping security zones.

*Practice Problems*
1. Compute the number of distinct simple paths of length 4 in a complete graph K₆, and discuss implications for multi‑path routing.
2. Using the inclusion–exclusion principle, determine the number of packets that satisfy at least one of three overlapping firewall rules.
---

ᚨ **Lecture 4: Graph Theory Fundamentals**

*Overview*

Graphs model networks at every layer, from physical topologies to abstract dependency graphs. We cover definitions, walks, connectivity, trees, and planar graphs, establishing a vocabulary for later protocol‑specific analysis.

*Key Topics*
- Graph terminology: vertices, edges, degree, adjacency
- Paths, cycles, walks, and connectivity
- Trees, spanning trees, and minimum‑weight trees (Kruskal, Prim)
- Planarity, Kuratowski’s theorem, and network embedding

*Lecture Notes*
Spanning‑tree protocols (RSTP, MSTP) rely on the existence of a minimum‑weight spanning tree. We derive the cut property and show how edge weights derived from link latency produce optimal broadcast domains. Planarity constraints become critical when designing on‑chip network‑on‑chip (NoC) fabrics, where crossing wires incurs area penalties.

*Required Reading*
- West, D.B. *Introduction to Graph Theory*, 3rd ed., Chapters 2‑4.
- “NoC Layout Optimization Using Planar Embedding” – IEEE TCAD 2025.

*Discussion Questions*
1. Why is a tree a natural model for hierarchical routing protocols like OSPF area design?
2. Discuss the challenges of embedding non‑planar network topologies onto silicon wafers.

*Practice Problems*
1. Prove that a graph with n vertices and n − 1 edges that is connected must be a tree.
2. Given a weighted graph representing a data‑center fabric, apply Kruskal’s algorithm to find the minimum spanning tree and compute its total weight.
---

ᚱ **Lecture 5: Network Topologies and Graph Algorithms**

*Overview*

We map classic networking topologies (bus, ring, mesh, hypercube, fat‑tree) to graph structures and explore algorithms for shortest paths, flow, and cut‑capacity, directly tying theory to routing and load balancing.

*Key Topics*
- Topology families as special graph classes
- Dijkstra’s and Bellman‑Ford shortest‑path algorithms
- Max‑flow min‑cut theorem and its relevance to bandwidth allocation
- Spectral graph theory basics for network resilience

*Lecture Notes*
The fat‑tree topology, popular in modern data‑centers, can be modeled as a hierarchical graph with varying edge capacities. Applying the max‑flow min‑cut theorem reveals the bandwidth guarantees between leaf servers and aggregation switches. Spectral analysis of the Laplacian matrix yields insight into community detection for fault isolation.

*Required Reading*
- Cormen, T.H. et al. *Introduction to Algorithms*, 4th ed., Chapters 24‑26.
- “Spectral Methods for Data‑Center Load Balancing” – SIGCOMM 2024.

*Discussion Questions*
1. How does the choice of topology affect the worst‑case latency in a distributed storage system?
2. Explain how the max‑flow min‑cut theorem underlies QoS guarantees in MPLS traffic engineering.

*Practice Problems*
1. Compute the shortest path from node A to node F in the provided weighted graph using Dijkstra’s algorithm.
2. For a given network graph, determine the minimum cut separating a set of critical servers from the rest of the network.
---

ᚴ **Lecture 6: Coloring, Scheduling, and Conflict‑Free Assignments**

*Overview*

Graph coloring models resource allocation problems such as frequency assignment, time‑slot scheduling, and register allocation in compilers for network‑function virtualization (NFV).

*Key Topics*
- Vertex coloring and chromatic number
- Edge coloring and applications to wavelength‑division multiplexing (WDM)
- Greedy and backtracking coloring algorithms
- Approximation algorithms and Lovász local lemma

*Lecture Notes*
In WDM optical networks, each wavelength can be treated as a color on edges; edge‑coloring ensures no two adjacent links use the same wavelength on a shared fiber. We analyze the Vizing theorem to bound the number of wavelengths needed, and discuss how graph‑coloring heuristics achieve near‑optimal spectrum utilization.

*Required Reading*
- Jensen, T.R., & Toft, B. *Graph Coloring Problems*, Wiley, Chapter 3.
- “Dynamic Spectrum Allocation via Edge Coloring” – Optics Express 2025.

*Discussion Questions*
1. Relate the vertex‑coloring problem to the assignment of VLAN IDs in a campus network.
2. How does the Lovász local lemma provide probabilistic guarantees for conflict‑free scheduling in 5G slicing?

*Practice Problems*
1. Determine the chromatic number of the provided conflict graph for channel assignment.
2. Apply Vizing’s theorem to compute the upper bound on the number of wavelengths required for the given optical network.
---

ᚼ **Lecture 7: Trees, Hierarchies, and Routing Protocols**

*Overview*

Tree structures are ubiquitous in routing protocols (spanning‑tree, BGP‑AS‑path). We study rooted trees, binary trees, and balanced trees, connecting them to hierarchical addressing and aggregation.

*Key Topics*
- Rooted trees, ancestors, depth, height
- Binary search trees and AVL/Red‑Black balancing
- BGP AS‑path as a directed tree of policy decisions
- Hierarchical IP address aggregation using prefix trees (tries)

*Lecture Notes*
BGP route‑aggregation reduces the size of routing tables by collapsing contiguous prefixes. We model this as a trie compression problem, deriving the optimal trade‑off between aggregation granularity and path specificity. AVL‑tree rotations are analogous to route‑flap damping mechanisms that re‑balance path selection after instability.

*Required Reading*
- Heine, A. *Routing Protocols and Algorithms*, 2nd ed., Chapter 5 (BGP).
- “Trie‑Based Prefix Aggregation for Scalable Internet Routing” – NSDI 2024.

*Discussion Questions*
1. How does tree balancing in data structures inform the design of route‑flap damping algorithms?
2. Discuss the impact of prefix aggregation on traffic engineering flexibility.

*Practice Problems*
1. Given a set of IPv6 prefixes, construct a minimal prefix trie and compute the number of aggregated entries.
2. Perform an AVL‑tree insertion and demonstrate the required rotations; map each rotation to a BGP policy adjustment.
---

ᚽ **Lecture 8: Planarity, Embedding, and Network Layout**

*Overview*

Physical network layout constraints often require planar embeddings to avoid cable crossings. We explore planar graphs, Kuratowski’s theorem, and algorithms for graph drawing.

*Key Topics*
- Planar graphs, faces, Euler’s formula
- Kuratowski’s theorem: K₅ and K₃,₃ as non‑planar minors
- Planarity testing algorithms (Hopcroft‑Tarjan)
- Force‑directed layout methods for network visualization

*Lecture Notes*
When designing a campus fiber backbone, minimizing crossings reduces installation cost and signal interference. We apply the Hopcroft‑Tarjan linear‑time planarity test to propose a crossing‑free layout for a given topology, and then use force‑directed algorithms to generate a visual schematic for the operations team.

*Required Reading*
- Diestel, R. *Graph Theory*, 5th ed., Chapter 3 (Planarity).
- “Automated Planarity Testing for Fiber‑Optic Network Planning” – IEEE Network 2025.

*Discussion Questions*
1. Why are K₅ and K₃,₃ fundamental obstacles in the physical design of PCB trace routing?
2. Discuss the trade‑offs between aesthetic network diagrams and algorithmic planarity constraints.

*Practice Problems*
1. Test the planarity of the provided network graph using the Hopcroft‑Tarjan algorithm (outline steps).
2. Produce a planar embedding for a small campus network topology and calculate its face count using Euler’s formula.
---

ᚾ **Lecture 9: Matching, Hall’s Theorem, and Resource Allocation**

*Overview*

Matching theory provides tools for optimal assignment of resources such as ports, frequencies, and virtual network functions (VNFs).

*Key Topics*
- Bipartite graphs and matchings
- Hall’s marriage theorem and its corollaries
- Maximum matching algorithms (Hungarian method)
- Applications: port‑to‑VLAN assignment, VNF placement

*Lecture Notes*
In a data‑center, assigning VNFs to physical servers can be modeled as a bipartite matching problem where each VNF requires certain resources. We apply the Hungarian algorithm to minimize total latency while respecting capacity constraints, illustrating how combinatorial optimization directly improves service‑level agreements (SLAs).

*Required Reading*
- Berge, C. *Graphs and Matching*, 1973, Chapters 1‑2.
- “Optimizing VNF Placement with Bipartite Matching” – ACM SIGCOMM 2024.

*Discussion Questions*
1. How does Hall’s theorem guarantee the existence of a feasible port‑VLAN assignment in a switch with limited ports?
2. Discuss the impact of edge weights representing latency on the optimality of VNF placement.

*Practice Problems*
1. Determine whether a perfect matching exists in the given bipartite graph using Hall’s condition.
2. Solve a small VNF placement instance using the Hungarian method; report total cost.
---

ᚿ **Lecture 10: Connectivity, Cuts, and Network Reliability**

*Overview*

Reliability analysis hinges on connectivity concepts: vertex‑ and edge‑connectivity, cuts, and network flow. We study Menger’s theorem and reliability polynomials.

*Key Topics*
- Vertex‑connectivity κ(G) and edge‑connectivity λ(G)
- Menger’s theorem and its network‑design implications
- Cut‑sets, minimal cuts, and network survivability
- Reliability polynomial and Monte‑Carlo estimation

*Lecture Notes*
The spine‑leaf architecture used in modern data‑centers achieves a high edge‑connectivity (λ = 2) between leaf switches, ensuring single‑link failure tolerance. We model this using cut‑set analysis and compute the reliability polynomial for a small example network, then compare analytical results with Monte‑Carlo simulations.

*Required Reading*
- Bollobás, B. *Modern Graph Theory*, Cambridge University Press, Chapter 5.
- “Monte‑Carlo Reliability Estimation for Large‑Scale Networks” – Reliability Engineering International 2023.

*Discussion Questions*
1. How does increasing edge‑connectivity from 2 to 3 affect the required number of spare links in a spine‑leaf design?
2. Compare deterministic cut‑set analysis with stochastic Monte‑Carlo for assessing network uptime.

*Practice Problems*
1. Compute κ(G) and λ(G) for the provided graph; identify a minimum vertex cut.
2. Derive the reliability polynomial of a simple triangle network with independent link failure probability p = 0.01.
---

ᚾ **Lecture 11: Graph Coloring Revisited – Advanced Topics**

*Overview*

We revisit coloring with a focus on list coloring, choosability, and applications to frequency‑division multiplexing in 6G.

*Key Topics*
- List coloring and choosability number
- Edge‑list coloring for wavelength assignment
- Applications to cognitive radio spectrum sharing
- Approximation algorithms for large‑scale networks

*Lecture Notes*
Cognitive radio systems must assign frequencies dynamically while respecting interference constraints. This can be modeled as a list‑coloring problem where each link has a list of admissible frequencies depending on local interference measurements. We explore algorithmic strategies for online list coloring and their performance bounds.

*Required Reading*
- Kostochka, A. “List Coloring of Graphs” – Journal of Graph Theory 2022.
- “Dynamic Spectrum Allocation via Online List Coloring” – IEEE JSAC 2025.

*Discussion Questions*
1. How does list coloring differ from traditional coloring in the context of adaptive spectrum allocation?
2. Discuss the computational challenges of online list‑coloring in ultra‑dense 6G networks.

*Practice Problems*
1. Given a small interference graph with assigned frequency lists, produce a feasible list coloring.
2. Analyze the worst‑case number of colors needed for a planar graph under list‑coloring constraints.
---

ᛡ **Lecture 12: Synthesis and Capstone Review**

*Overview*

In the final lecture we synthesize the discrete mathematics and graph‑theory concepts, revisiting how they interlock with real‑world networking design, security, and performance. Students present a capstone mini‑project: designing a resilient, low‑latency topology for a hypothetical edge‑computing cluster, justifying each design decision with theorems and algorithms covered.

*Key Topics*
- Integrated design using spanning‑tree, flow, and coloring techniques
- Trade‑off analysis: latency vs. redundancy vs. cost
- Presentation of capstone designs and peer review

*Lecture Notes*
Students will construct a weighted graph representing the edge‑computing cluster, apply Kruskal’s algorithm for a cost‑effective spanning tree, evaluate edge‑connectivity for resilience, and allocate wavelengths via edge‑list coloring. The capstone demonstrates the full pipeline from abstract theory to concrete engineering.

*Required Reading*
- Review of all previous lecture notes.
- Selected case studies from IEEE Communications Magazine 2024‑2025 on edge‑computing network design.

*Discussion Questions*
1. How would you modify your design if the network must support both deterministic ultra‑low‑latency traffic and best‑effort traffic?
2. Identify at least three theorems from this course that most directly influence your topology choices.

*Practice Problems*
1. Complete the capstone design worksheet (provided in the course repository) and submit a short report (≤ 1000 words).
2. Perform a brief Monte‑Carlo reliability assessment of your proposed topology under a 0.5% link‑failure probability.
---

## Assignments

### Assignment 1: Proof‑Writing Exercise
Develop a rigorous proof for Hall’s marriage theorem and apply it to a realistic switch‑port allocation scenario.

### Assignment 2: Algorithm Implementation
Implement Dijkstra’s algorithm in Python for a weighted network graph and benchmark its performance on a synthetic 10 k‑node topology.

### Assignment 3: Graph‑Based Network Design Project
Design a small‑scale data‑center topology (≤ 30 nodes) that satisfies given latency, redundancy, and cost constraints. Provide a written justification referencing at least five theorems covered in the course.

---
