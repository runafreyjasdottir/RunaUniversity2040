# CS301: Distributed Systems
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4  
**Prerequisites:** CS204 (Computer Networks & Protocols), CS201 (Data Structures & Algorithms II)  
**Description:** CAP, consensus (Raft/Paxos), eventual consistency, CRDTs

---

## Lectures

ᛟ **Lecture 1: The Landscape of Distributed Computation — Why Distribution Matters**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

The year is 2040. No serious computation happens on a single machine anymore. From the quantum-hybrid clouds that power AGI inference to the edge meshes that run autonomous vehicles, distributed systems are the substrate of everything we build. This opening lecture establishes the conceptual terrain: why distribution is not merely a performance optimization but a fundamental computational paradigm with its own laws, trade-offs, and philosophical commitments.

We trace the arc from early networked systems — the ARPANET's decentralized routing, the first distributed file systems (NFS, AFS) — to the modern landscape of globally replicated state machines, CRDT-based collaborative editing, and the erasure-coded storage systems that hold the world's data. Along the way, we confront the central truth of the field: distributed systems are defined by their failure modes. A system that cannot fail isn't distributed; it's just slow.

### Key Topics

- **TheFundamental Abstraction**: Processes communicating via messages over unreliable channels — the asynchronous system model
- **Fallacies of Distributed Computing**: Peter Deutsch's eight fallacies (1994) and why six additional ones had to be added by 2035
- **Why Distribution Is Inevitable**: Scale, fault tolerance, latency optimization, geographic compliance, and the thermodynamic argument
- **The CAP Conjecture Before the Theorem**: Brewer's original 2000 keynote and the intuitive argument before formalization
- **Local Knowledge Principle**: No node can know the global state instantaneously — the epistemological foundation of distributed systems
- **The 2040 Context**: Quantum-repeater networks, AGI-grade inference clusters, planetary-scale sensor meshes

### Lecture Notes

Distributed systems emerged not from a single insight but from the accumulation of practical necessity. In the 1960s, the U.S. Department of Defense funded ARPANET precisely because a centralized command structure was a single point of failure — a vulnerability that could be exploited in warfare. The first分布式systems were thus born from paranoia, not optimization. This origin story matters: the field's deepest assumptions are still shaped by the threat model of adversarial infrastructure destruction.

By the 1990s, the client-server model had simplified distributed computation back toward centralization. Web servers were essentially centralized databases that happened to be accessed remotely. The real intellectual revolution came when companies like Google and Amazon discovered that *scale* requires distribution, not as a luxury but as a physical necessity. A single machine cannot store petabytes; a single rack cannot serve millions of concurrent requests; a single datacenter cannot provide single-digit-millisecond latency globally.

The 2020s saw the emergence of three forces that made distribution *the norm rather than the exception*: (1) the proliferation of edge devices requiring local computation for latency and privacy reasons; (2) regulatory frameworks (GDPR, China's PIPL, India's DPDPA) mandating data residency within specific jurisdictions; and (3) the shift from request-response to event-driven architectures where state is continuously streamed across many nodes.

By 2040, the University of Yggdrasil's own infrastructure is a distributed system — its HPC cluster spans nodes in Iceland, Norway, and the Faroe Islands, connected by quantum-encrypted undersea cables, and its student-facing services run on a constellation of edge nodes within 50ms of every enrolled student worldwide. The Bifrost Research Network, named after the mythological bridge between realms, provides the backbone.

**The Local Knowledge Principle** deserves special emphasis. In a distributed system, every node operates with *partial, potentially stale* information about the rest of the system. This is not a bug — it is the defining constraint. A node in Tokyo cannot instantaneously know whether a node in Reykjavik has crashed or is merely slow to respond. This uncertainty gives rise to impossibility results like FLP and the necessity of timeouts, heartbeats, and failure detectors. We will return to this principle in every lecture.

The 14 Fallacies of Distributed Computing (Deutsch 1994, extended by the UoY Distributed Systems Group 2035):

*Original 8 (1994):*
1. The network is reliable
2. Latency is zero
3. Bandwidth is infinite
4. The network is secure
5. Topology doesn't change
6. There is one administrator
7. Transport cost is zero
8. The network is homogeneous

*Extended 6 (2035):*
9. Clocks are synchronized
10. State is consistent by default
11. Partial failure doesn't happen
12. Causality is obvious
13. Human operators read the manual
14. Quantum decoherence is someone else's problem

### Required Reading

- Brewer, E.A. (2000). "Towards Robust Distributed Systems." *PODC Keynote*. (Original CAP conjecture presentation)
- Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly. Chapters 1, 5.
- UoY Distributed Systems Group (2035). "Beyond the Eight Fallacies: Six More Assumptions That Kill Distributed Systems in the 2030s." *Proceedings of the Bifrost Symposium on Resilient Computation*.

### Discussion Questions

1. The ARPANET's designers chose packet-switched routing over circuit-switched routing partly for survivability. What other design decisions in early distributed systems were driven by security rather than performance? How have those decisions aged?
2. Consider the Local Knowledge Principle in the context of a self-driving car system that must make decisions within 100ms. What are the implications of partial information for safety-critical distributed systems?
3. The extended fallacies (9–14) were identified at the University of Yggdrasil in 2035. Which of these six do you consider most dangerous in practice, and why?

### Practice Problems

- Install and run a simple two-node distributed counter using a Python TCP socket. Observe what happens when you physically disconnect one node (kill the process). What information does the surviving node have about the other's state?
- Draw the state space for a two-node system where each node can be in state {up, down, unknown} and each message can be {delivered, lost, delayed}. How many distinct global states exist? How many are actually observable by any single node?

---

ᛏ **Lecture 2: Models of Distributed Computation — Formal Foundations**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Before we can reason about what distributed systems *do*, we must establish what distributed systems *are* at a formal level. This lecture introduces the three foundational computational models — synchronous, asynchronous, and partially synchronous — and explains why the choice of model determines everything: what algorithms are possible, what guarantees are achievable, and what problems are unsolvable.

We also introduce the concept of *adversary models*, which formalize the power of the environment (network delays, crash failures, Byzantine behavior) against which our algorithms must defend. These models are not academic exercises — they are the difference between a system that works in a lab and one that survives the chaos of a production datacenter during a cascading failure.

### Key Topics

- **System Models**: Synchronous (bounded time, known upper bounds), asynchronous (no timing assumptions), partially synchronous (periods of synchrony)
- **Failure Models**: Crash-stop, crash-recovery, omission, Byzantine — what each means for algorithm design
- **The Asynchronous System Model**: Why it's the "worst case" model and why we design for it
- **Message-Passing vs. Shared Memory**: The two fundamental communication abstractions and when each is appropriate
- **I/O Automata**: Lynch's formalism for specifying distributed algorithms
- **Adversary Scheduling**: The environment as an adversary that chooses which messages to deliver and when

### Lecture Notes

A distributed system, at its most abstract, is a collection of `n` processes that communicate by sending messages over channels. That's it. No shared memory (unless we simulate it via message passing), no global clock (unless we simulate it via clock synchronization protocols), no instantaneous knowledge (the Local Knowledge Principle again).

**Synchronous systems** assume two powerful properties: (1) there is a known upper bound on message delivery time, and (2) there is a known upper bound on the relative rate at which different processes can execute. These bounds allow us to use *timeouts* as reliable failure detectors: if a process hasn't responded within the bound, it must have crashed. Synchronous algorithms can solve problems that are provably impossible in asynchronous systems (e.g., deterministic consensus). The downside is that real systems do not satisfy synchronous assumptions — ask anyone who ran a distributed database during the AWS us-east-1 outage of 2024.

**Asynchronous systems** make no timing assumptions whatsoever. Message delivery time can be arbitrarily large. Processes can execute at arbitrarily different speeds. This model captures the "worst case" reality of operating over the public internet, where network partitions, routing instability, and garbage collection pauses in virtual machines can all cause unbounded delays. The price is steep: the FLP impossibility result (Fischer, Lynch, Paterson, 1985) proves that deterministic consensus is impossible in even a minimal asynchronous system with one crash failure. We'll study FLP in detail in Lecture 5.

**Partially synchronous systems** (Dwork, Lynch, Stockmeyer, 1988) attempt to capture the best of both worlds. The model assumes that the system is *eventually* synchronous: there exists a Global Stabilization Time (GST) after which messages are delivered within a known bound and processes execute within a known ratio. Before GST, the system can behave asynchronously. Most practical consensus algorithms (Raft, Multi-Paxos, PBFT) are designed for the partially synchronous model — they make progress quickly during good periods and make progress slowly (or not at all) during bad periods, but they never violate safety properties.

**Failure models** define what can go wrong with individual processes:

- *Crash-stop*: A process fails by halting permanently. It never recovers. Once crashed, it sends no further messages.
- *Crash-recovery*: A process fails by halting, but may restart with its stable storage intact. It can rejoin the system after recovery, but must re-synchronize its state.
- *Omission*: A process may fail to send or receive some messages, but when it does communicate, its messages are correct.
- *Byzantine*: A process may behave arbitrarily — it can send contradictory messages to different processes, lie about its state, or follow an entirely different protocol. This model is named after the Byzantine Generals Problem (Lamport, Shostak, Pease, 1982).

The progression from crash-stop to Byzantine represents an increasing assumption about the power of the adversary. Each step up makes the algorithm design harder but the resulting system more robust. Byzantine fault tolerance (BFT) is essential in systems where processes may be compromised by an attacker — as is the case for most public blockchain systems.

**I/O Automata** (Lynch and Tuttle, 1989) provide a rigorous formalism for describing distributed algorithms. An I/O automaton has a set of states, a set of actions (partitioned into input, output, and internal), and a transition relation describing which state transitions are enabled by which actions. Composition of automata models communication: the output actions of one automaton become input actions of another. While we won't write full I/O automata specifications in this course, understanding this model is crucial for proving correctness properties of distributed algorithms.

The **adversary scheduling** model gives us a powerful way to think about the environment's power. Rather than modeling specific failure patterns, we imagine an all-powerful adversary that controls the scheduling of all events — message deliveries, process step executions, and failure events. An algorithm is correct if it satisfies its specification *regardless of what the adversary does*, subject only to the constraints of the chosen system and failure models. This is the same philosophy as Kerckhoffs' principle in cryptography: the algorithm must be secure even if the adversary knows everything about it and can control the schedule.

In 2040, the University of Yggdrasil's Bifrost Research Network runs experiments on a testbed called the **Yggdrasil Testbed**, which can inject controlled Byzantine failures, network partitions, and clock skew into a cluster of 100 nodes. Students in CS301 will use this testbed to observe firsthand how different failure models affect algorithm behavior.

### Required Reading

- Lynch, N.A. (1996). *Distributed Algorithms*. Morgan Kaufmann. Chapters 2–3 (I/O automata, system models).
- Dwork, C., Lynch, N., Stockmeyer, L. (1988). "Consensus in the Presence of Partial Synchrony." *JACM* 35(2).
- Lamport, L., Shostak, R., Pease, M. (1982). "The Byzantine Generals Problem." *ACM TOPLAS* 4(3).

### Discussion Questions

1. Why does the partially synchronous model assume a Global Stabilization Time rather than, say, periods of bounded latency interspersed with periods of unbounded latency? What practical scenarios does GST capture well, and what does it miss?
2. If you were building a payment processing system that handles real money, which failure model would you design for? Justify your choice considering both the cost of failure and the cost of over-engineering.
3. I/O automata were proposed in 1989. Why haven't they been more widely adopted in industry practice? What alternatives do engineers use instead?

### Practice Problems

- Formally specify a two-process mutual exclusion algorithm using I/O automata. Prove that it satisfies mutual exclusion (safety) and progress (liveness) in the synchronous model.
- Consider a system with 5 processes where at most 2 can be Byzantine. What is the minimum number of rounds needed for Byzantine agreement? (Recall: n ≥ 3f+1 processes are needed to tolerate f Byzantine failures.)
- Implement a simple process group membership protocol in Python. What failure model does your protocol assume?

---

ᚢ **Lecture 3: Time, Clocks, and Causality**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Time is the oldest problem in distributed systems, and it remains one of the most misunderstood. This lecture traces the evolution of how we think about time in distributed systems — from Lamport's elegant observation that "happened-before" is more fundamental than clock time, through vector clocks and their offspring, to the modern hybrid logical clocks that power CRDTs and collaborative editing systems.

The central insight is this: in a distributed system, there is no single notion of "now." Every node sees a different slice of reality at any physical instant, and the order in which events occur depends on the observer. Causal ordering — the happened-before relation — is the strongest ordering we can observe without coordination, and it's sufficient for almost everything we need.

### Key Topics

- **Physical Time vs. Logical Time**: Why NTP-synchronized clocks are insufficient for ordering distributed events
- **Lamport Clocks**: The happened-before relation, scalar logical clocks, and their limitations
- **Vector Clocks**: Capturing concurrent events, partial order, and the instant problem
- **Dotted Version Vectors**: Solving the "concurrent update to the same key" problem in key-value stores
- **Hybrid Logical Clocks (HLCs)**: Combining physical and logical time — the state of the art in 2040
- **TrueTime and Spanner**: Google's approach — using atomic clocks and GPS to bound clock uncertainty
- **Quantum Timestamps**: The 2039 breakthrough in quantum-entangled clock synchronization

### Lecture Notes

Leslie Lamport's 1978 paper "Time, Clocks, and the Ordering of Events in a Distributed System" is one of the most cited papers in all of computer science, and for good reason. It established that the "happened-before" relation (→) is the fundamental ordering relation in distributed systems, not physical time. Two events `a` and `b` satisfy `a → b` if and only if: (1) they occur at the same process and `a` precedes `b`; or (2) `a` is the sending of a message and `b` is the receipt of that message; or (3) there exists `c` such that `a → c` and `c → b` (transitivity).

This relation is a *strict partial order*: it is irreflexive (no event happens before itself), antisymmetric (if `a → b`, then not `b → a`), and transitive. Crucially, two events may be *concurrent* — neither `a → b` nor `b → a`. This is the hallmark of distributed systems: events that are truly independent and whose ordering is physically meaningless.

**Lamport clocks** assign a monotonically increasing scalar to each event: `LC(e) = max(LC(local), LC(received_message)) + 1`. This ensures that if `a → b`, then `LC(a) < LC(b)`. But the converse is *not* true — `LC(a) < LC(b)` does not imply `a → b`. Lamport clocks lose information about concurrency.

**Vector clocks** solve this limitation. Each process maintains a vector of length n (number of processes). Process `i` increments `VC[i]` for each local event and updates its vector to the element-wise maximum upon receiving a message, incrementing its own entry. Two events are concurrent if and only if their vector clocks are incomparable — each has a smaller entry in some dimension. This gives us the full causal picture, but at the cost of O(n) space per event. For large systems, this is impractical.

The **instant problem** is the central challenge of physical time in distributed systems. Suppose process P1 writes value `v1` to key `k` at physical time `t1`, and process P2 writes value `v2` to the same key at physical time `t2`, where `t1 < t2`. If P2's clock reads `t2' < t1`, it will believe its write came first. This is why relying purely on physical timestamps for ordering is dangerous — clock drift, even with NTP, can be on the order of hundreds of milliseconds.

Google's Spanner database introduced **TrueTime**, which doesn't try to give you a single timestamp but instead gives you a *time interval* `[earliest, latest]` within which the current time is guaranteed to lie. By waiting for `latest` to pass before committing, Spanner ensures that transactions are externally consistent. The cost: GPS and atomic clocks in every datacenter, and commit latencies that include sleep periods. TrueTime is elegant but expensive, and most systems in 2040 still use logical clocks for ordering.

**Hybrid Logical Clocks (HLCs)**, proposed by Kulkarni, Demirbas, et al. in 2014, combine the best of both worlds. An HLC timestamp is a pair `(l, c)` where `l` is the maximum physical time seen (similar to Lamport time) and `c` is a logical counter that increments when events happen at the same physical time. HLCs provide: (1) causal ordering like vector clocks; (2) physical-time approximation (each HLC's `l` component is close to physical time); (3) bounded drift from physical time. In 2040, HLCs are the de facto standard for timestamping in distributed databases, CRDTs, and collaborative editing systems.

**Quantum Timestamps**: The most exciting recent development. In 2039, researchers at the University of Yggdrasil's Quantum Networking Lab demonstrated that entangled qubits distributed across nodes can provide clock synchronization with sub-nanosecond accuracy — three orders of magnitude better than GPS-based TrueTime. However, quantum timestamps require dedicated quantum channels and are currently limited to the Bifrost Research Network's testbed. Students will receive a demonstration but should understand that this technology will not be production-ready until at least 2045.

### Required Reading

- Lamport, L. (1978). "Time, Clocks, and the Ordering of Events in a Distributed System." *CACM* 21(7): 558–565.
- Kulkarni, S., Demirbas, M., et al. (2014). "Logical Physical Clocks and Consistent Snapshots in Globally Distributed Databases." *OPODIS*.
- Corbett, J.C., et al. (2012). "Spanner: Google's Globally-Distributed Database." *OSDI*.
- UoY Quantum Networking Lab (2039). "Entanglement-Assisted Clock Synchronization for Distributed Systems." *Bifrost Technical Report BFT-2039-07*.

### Discussion Questions

1. Lamport originally introduced his clocks as a way to totally-order events, even though the happened-before relation provides only a partial order. Was this total ordering a feature or a bug? In what situations is a total order unnecessary or even harmful?
2. Vector clocks provide complete causal information at O(n) space cost. In a system with 10,000 processes, what practical alternatives exist for tracking causality? Research and discuss at least two.
3. TrueTime relies on specialized hardware (atomic clocks, GPS receivers). Is this a sustainable approach for the entire industry, or should we accept slightly weaker guarantees from HLCs? What are the trade-offs?

### Practice Problems

- Implement a vector clock in Python that supports local events, send events, and receive events. Write a function that determines whether two events are causally related or concurrent.
- Given the following HLC timestamps, determine the causal relationship between all pairs of events: P1:(10,0)→P1:(10,1)→P1:(12,0), P2:(11,0)→P2:(11,1), P3:(10,0)→P3:(11,2). Identify all concurrent event pairs.
- Write a short essay (5 paragraphs) analyzing the trade-offs between TrueTime and HLCs for a globally distributed banking system.

---

ᛒ **Lecture 4: Consensus — The Impossible Problem and Its Solutions**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Consensus is the single most important problem in distributed systems. The question is deceptively simple: can a group of processes agree on a single value? The answer depends entirely on the system model — synchronous, asynchronous, or partially synchronous — and the failure model — crash-stop, crash-recovery, or Byzantine. This lecture covers the FLP impossibility result, the Paxos family of protocols, and the practical algorithm that powers most production systems in 2040: Raft.

### Key Topics

- **The Consensus Problem**: Formal definition — agreement, validity, termination
- **FLP Impossibility**: Fischer, Lynch, Paterson (1985) — no deterministic consensus in even minimally asynchronous systems with one crash failure
- **Randomization and FLP**: How randomized protocols (Ben-Or, Rabin) circumvent FLP with probabilistic termination
- **Paxos**: Lamport's "The Part-Time Parliament" (1998) and the protocol that wouldn't die
- **Multi-Paxos and Practical Paxos**: Optimizations for leader election, log replication, and full membership changes
- **Raft**: Ongaro and Ousterhout (2014) — understandability-first consensus
- **Byzantine Fault Tolerant Consensus**: PBFT, HotStuff, and the honest-majority assumption

### Lecture Notes

The **consensus problem** asks: given `n` processes, each starting with an initial value `v_i`, can all non-faulty processes agree on a single value? More formally, a consensus protocol must satisfy three properties:

1. **Agreement**: All non-faulty processes decide on the same value.
2. **Validity**: The decided value must be the initial value of some process (not pulled from thin air).
3. **Termination**: All non-faulty processes eventually decide.

Agreement and validity are *safety* properties — they must never be violated. Termination is a *liveness* property — it must eventually hold. The tension between safety and liveness is the engine that drives much of distributed systems theory.

**FLP Impossibility**: Fischer, Lynch, and Paterson's 1985 result is one of the most important theorems in all of computing. It states that no deterministic algorithm can solve consensus in an asynchronous system even with one crash failure. The proof proceeds by showing that for any configuration that hasn't yet decided, there exists an adversary schedule that prevents a decision forever. The key insight is that in an asynchronous system, a process that appears slow might be crashed — there's no way to tell the difference. Therefore, any algorithm that decides must do so even if a process is merely slow, but the adversary can always choose to slow down a different process after each step, preventing the system from reaching a configuration where agreement is forced.

FLP is a *theoretical* result. It doesn't say consensus is impossible in practice — it says it's impossible *deterministically* in an *asynchronous* system. Two escape hatches:

1. **Randomization**: Introduce randomness so the adversary can't predict which step will drive progress. Ben-Or's randomized consensus protocol (1983) achieves expected O(n^2) rounds with crash failures, and Rabin's randomized protocol uses a common coin to achieve O(1) expected rounds.
2. **Partial synchrony**: If the system eventually enters a period of synchrony (as in the partially synchronous model), deterministic consensus becomes possible. This is the approach taken by all practical consensus protocols.

**Paxos** is arguably the most important distributed algorithm ever designed, though its reputation for incomprehensibility is well-earned. Lamport's original paper, "The Part-Time Parliament" (1998), was written as a fictional story about a parliamentary procedure on the island of Paxos — complete with footnotes about broken pottery and fictional Greek scholars. The academic community found it amusing but unhelpful, so Lamport wrote "Paxos Made Simple" (2001) in plain English.

The core idea: a value is chosen when a majority of acceptors have voted for it. A proposer sends a "prepare" request with a proposal number; acceptors promise not to accept any proposal with a smaller number. If the proposer hears back from a majority, it sends an "accept" request with the value (or the highest-numbered value already accepted, if any). Safety is maintained because any two majorities must overlap, guaranteeing that a later proposer will learn about any previously chosen value.

**Multi-Paxos** extends single-decree Paxos to a replicated log. The key optimization: if the same proposer stays the leader, it only needs to run the prepare phase once — subsequent slots can skip directly to the accept phase. This reduces the normal-case latency to a single round trip, which is optimal for wide-area networks.

**Raft** was designed by Diego Ongaro and John Ousterhout in 2014 as a response to Paxos's reputation for incomprehensibility. Raft decomposes consensus into three subproblems: (1) leader election, (2) log replication, and (3) safety. Each subproblem has a clear, independently understandable protocol. The key invariant: if a log entry is committed on one server, it will never be overwritten on any server. Raft achieves this through a simple majority rule and a restriction that a leader can only overwrite entries from its own term or later terms.

In practice, Raft is the consensus algorithm of choice for most systems built in 2040. It's used in etcd (the configuration store for Kubernetes), Consul (HashiCorp's service mesh), TiKV (the storage engine for TiDB), and countless other systems. Paxos is still used inside Google (in Spanner and its internal Chubby lock service), but the engineers who maintain it have decades of experience with its subtleties.

**Byzantine consensus** is harder: instead of crash failures, we must tolerate processes that behave arbitrarily. The classic result is that `n ≥ 3f + 1` processes are needed to tolerate `f` Byzantine failures. PBFT (Castro and Liskov, 1999) was the first practical BFT protocol, requiring three phases: pre-prepare, prepare, and commit. Modern BFT protocols like HotStuff (used in Meta's Libra/Diem blockchain) reduce the communication cost to O(n) per round using threshold signatures.

The University of Yggdrasil's Bifrost Network runs a modified HotStuff protocol for its control plane, with Raft for data plane replication. This hybrid approach — strong BFT for metadata, crash-tolerant consensus for data — is becoming increasingly common.

### Required Reading

- Fischer, M.J., Lynch, N.A., Paterson, M.S. (1985). "Impossibility of Distributed Consensus with One Faulty Process." *JACM* 32(2).
- Lamport, L. (2001). "Paxos Made Simple." *ACM SIGACT News* 32(4).
- Ongaro, D., Ousterhout, J. (2014). "In Search of an Understandable Consensus Algorithm." *USENIX ATC*.

### Discussion Questions

1. FLP proves that deterministic consensus is impossible in asynchronous systems, yet we build distributed databases that achieve consensus every day. Are we violating a theorem, or are we doing something different? What exactly is the gap between theory and practice?
2. Paxos has been described as "the protocol that won't die." Despite Raft's superior understandability, Google still uses Paxos variants internally. Why might an organization choose Paxos over Raft?
3. Consider a blockchain that tolerates f < n/3 Byzantine nodes. What happens when the network temporarily partitions such that one partition has exactly 2n/3 nodes? Is the system still safe? Is it still live?

### Practice Problems

- Implement a simple Raft leader election in Python (3 nodes, terms, vote requests, election timeouts). Demonstrate that exactly one leader is elected within 5 seconds regardless of initial state.
- Trace through a Paxos run with 3 acceptors and 2 proposers where the proposers compete. Show the message sequence that leads to a chosen value. How many round trips does it take?
- Calculate the minimum number of nodes needed for Byzantine agreement with f=10 Byzantine failures. If the protocol requires O(n²) messages per round, how many messages are exchanged per round?

---

ᛗ **Lecture 5: Replication and Consistency Models**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Replication — storing multiple copies of data on different machines — is the primary technique for achieving fault tolerance, availability, and low latency in distributed systems. But replication creates a fundamental tension: the more copies you have, the harder it is to keep them all in agreement. This lecture explores the spectrum of consistency models, from linearizability (the strongest) to eventual consistency (the weakest practical model), and the systems that embody each point on the spectrum.

### Key Topics

- **Why Replicate?**: Fault tolerance, availability, latency, data locality
- **The Consistency Spectrum**: Linearizability, sequential consistency, causal consistency, eventual consistency, and the trade-offs between them
- **Linearizability**: The strongest practical model — every operation appears to take effect atomically at a single point in real time
- **Sequential Consistency**: Like linearizability but without the real-time ordering constraint between non-overlapping operations
- **Causal Consistency**: Operations related by happened-before must be seen in order; concurrent operations may be seen in any order
- **Eventual Consistency**: If no new updates are made, all replicas will eventually converge to the same state
- **Session Guarantees**: Read-your-writes, monotonic reads, monotonic writes, writes-follow-reads — client-side consistency
- **The RYW Problem**: Why "read your writes" is harder than you think in a partitioned system

### Lecture Notes

The decision to replicate data is always driven by one or more of four goals:

1. **Fault tolerance**: If one machine fails, another has the data.
2. **Availability**: Even during network partitions, some copy is accessible.
3. **Latency**: Put a copy close to the user.
4. **Data locality**: Compute where the data lives, rather than moving data to the compute.

These goals are often in tension. Maximizing availability (goal 2) requires that any replica can accept writes, which makes consistency harder. Maximizing fault tolerance (goal 1) requires synchronizing writes across replicas, which makes availability harder during partitions. This is the CAP theorem in action, which we'll formalize in Lecture 6.

**Linearizability** (Herlihy and Wing, 1990) is the strongest consistency model used in practice. It requires that every operation appears to take effect instantaneously at some point between its invocation and response, and that these points form a total order consistent with the real-time ordering of operations. In other words: if operation A completes before operation B begins, then A must appear to happen before B in the global ordering. Linearizability is expensive — it requires coordination (usually consensus) for every write — but it's what most developers intuitively expect.

**Sequential consistency** (Lamport, 1979) relaxes linearizability by dropping the real-time constraint. The result of any execution must be equivalent to some sequential execution, but concurrent operations can be reordered. This means that if process P1 writes `x=1` and then process P2 reads `x`, P2 is not guaranteed to see `1` — P2's read could be ordered before P1's write as long as some sequential ordering exists that produces the same results. Sequential consistency is sufficient for many applications but is still expensive to implement.

**Causal consistency** (Ahamad et al., 1995) is weaker: it only requires that operations related by happened-before are seen in order. Concurrent operations (those that are not causally related) can be seen in any order. This is the strongest consistency model achievable without coordination — operations from the same client are always seen in order, and operations that read from each other's writes are seen in order, but independent operations on different keys can arrive in any order.

**Eventual consistency** is the weakest practical model. It says that if no new updates are made, eventually all replicas will converge to the same state. "Eventually" is deliberately vague — it could be milliseconds, seconds, or hours. What "converge" means is defined by the merge function (see Lecture 9 on CRDTs). Eventual consistency is the model used by DNS (convergence takes hours to days), by many NoSQL databases, and by most mobile applications.

**Session guarantees** (Terry et al., 1994) are client-side consistency properties that sit between causal consistency and eventual consistency. The four classic session guarantees are:

- **Read-your-writes (RYW)**: A client always sees its own prior writes.
- **Monotonic reads**: A client never sees data go backwards in time.
- **Monotonic writes**: Writes from the same client are applied in order.
- **Writes-follow-reads**: A write after a read sees at least the version read.

These guarantees are much easier to implement than server-side consistency because they only require the client to track its own session state (e.g., a vector timestamp of its operations). Most modern "eventually consistent" systems actually provide these session guarantees, which makes them much more useful than bare eventual consistency.

In 2040, the consensus in the distributed systems community (pun intended) is that **causal consistency + session guarantees** is the right default for most applications. Linearizability is necessary for financial transactions and coordination primitives (locks, leader election), but for most data access patterns, causal consistency provides the guarantees developers expect at a fraction of the coordination cost. Systems like COPS (Lloyd et al., 2011), GentleRain (Du et al., 2014), and the University of Yggdrasil's own BifrostDB (2038) implement causal consistency at scale.

### Required Reading

- Herlihy, M., Wing, J. (1990). "Linearizability: A Correctness Condition for Concurrent Objects." *ACM TOPLAS* 12(3).
- Lamport, L. (1979). "How to Make a Multiprocessor Computer That Correctly Executes Multiprocess Programs." *IEEE TC* 28(9).
- Terry, D., et al. (1994). "Session Guarantees for Weakly Consistent Replicated Data." *PDPS*.
- Gilbert, S., Lynch, N. (2002). "Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services." *Brewer's Conjecture*.

### Discussion Questions

1. A social media feed application: which consistency model is appropriate for (a) the like counter on a post, (b) the list of comments on a post, (c) the user's own post creation, (d) the user's direct messages? Justify each choice.
2. Is it ever correct for a system to provide no consistency guarantees at all? Give an example or argue that it's never correct.
3. Read-your-writes seems obvious — why is it non-trivial in a partitioned system? What goes wrong when a client connects to a different replica after a network reconnection?

### Practice Problems

- Given the following operations on a shared variable `x`, determine whether each execution is linearizable, sequentially consistent, or only causally consistent:
  - P1: write(x,1); P2: read(x)→1; P3: read(x)→0
  - P1: write(x,1); P2: write(x,2); P3: read(x)→2; P4: read(x)→1
  - P1: write(x,1); P2: read(x)→1; P3: write(x,2); P4: read(x)→1
- Design a protocol that provides read-your-writes and monotonic reads for a single client connecting to a quorum-based replicated store. What state does the client need to maintain?
- Analyze the performance implications of linearizability vs. causal consistency for a key-value store with 5 replicas spread across 3 continents. Estimate the latency difference for a write operation.

---

ᚹ **Lecture 6: The CAP Theorem — A Useful Lie**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

The CAP theorem is simultaneously the most important and most misunderstood result in distributed systems. "You can only have two of Consistency, Availability, and Partition tolerance" — but this formulation is wrong in important ways. This lecture deconstructs CAP, explains what it actually says, and provides the nuanced framework for reasoning about trade-offs in real systems.

### Key Topics

- **The CAP Conjecture and Theorem**: Brewer (2000), Gilbert-Lynch proof (2002)
- **What CAP Actually Says**: In the presence of a partition, you must choose between consistency and availability — not among all three
- **What CAP Does Not Say**: You cannot "choose" partition tolerance; partitions are a reality of distributed systems
- **The PACELC Model**: Extending CAP with latency-consistency trade-offs
- **Beyond CAP**: Harvest and Yield, CALM theorem, CRDTs as a way to have both C and A
- **CAP in Practice**: How real systems (Cassandra, MongoDB, Spanner, CockroachDB) navigate the trade-off

### Lecture Notes

The CAP theorem, as formulated by Eric Brewer in his 2000 PODC keynote and proved by Gilbert and Lynch in 2002, states: **In a distributed system that may experience network partitions, you cannot simultaneously guarantee consistency (C) and availability (A).** You must choose one or the other during a partition.

The critical misunderstanding is treating CAP as a menu where you "pick two." This is wrong for three reasons:

1. **You cannot choose P.** Partitions are not an option — they are a fact of networked computing. Networks will partition. Switches will fail. Undersea cables will be cut by ship anchors. A system that "doesn't tolerate partitions" is a system that fails when the inevitable partition occurs. Therefore, every distributed system must be partition-tolerant. The real choice is CP or AP.

2. **CAP only applies during a partition.** When the network is healthy, you can have both consistency and availability. CAP says nothing about normal-case behavior — it only describes the trade-off during a partition.

3. **"Consistency" in CAP means linearizability.** This is the strongest possible consistency model, and many applications don't need it. If your application can tolerate causal consistency or even eventual consistency, CAP's constraint may not apply to you at all.

**PACELC** (Abadi, 2012) extends CAP to capture the latency-consistency trade-off in normal operation. The full name: **if there is a Partition (P), you choose between Availability (A) and Consistency (C); Else (E), when running normally, you choose between Latency (L) and Consistency (C).** This gives us four design points:

- **PA/EL**: Available during partitions, low latency during normal operation (e.g., Dynamo, Cassandra with weak consistency)
- **PA/EC**: Available during partitions, but consistent during normal operation (rare — difficult to achieve)
- **PC/EL**: Consistent during partitions (rejecting some requests), low latency during normal operation (e.g., MongoDB with readConcern=local)
- **PC/EC**: Consistent during partitions, consistent during normal operation — but latency may be higher (e.g., Spanner, CockroachDB with serializable isolation)

**The CALM Theorem** (Hellerstein, 2010) provides a different perspective: programs that are *monotonic* — whose outputs only grow as inputs grow — can be computed without coordination. This is formalized as the Consistency As Logical Monotonicity theorem. It shows that the CAP trade-off isn't between C and A per se, but between coordination (which is expensive) and monotonicity (which enables coordination-free computation). CRDTs (Lecture 9) are a practical application of CALM: their merge functions are monotonic, so they can be computed without synchronous coordination.

In practice, most production systems in 2040 occupy a **middle ground**:

- **Spanner** (Google): Provides external consistency (stronger than linearizability) via TrueTime. It's PC/EC, with commit latencies that include a sleep period to account for clock uncertainty. For most applications, this latency (typically 5-10ms in a single region) is acceptable.
- **Cassandra** (Apache): Tunable consistency — each read/write can specify `QUORUM`, `ONE`, `ALL`, etc. It's PA/EL by default (available during partitions, low latency) but can be configured as PC/EL or even PC/EC at the cost of latency and reduced availability.
- **CockroachDB**: Inspired by Spanner but without TrueTime. Uses HLCs for timestamp ordering. PC/EC by default, with serializable SQL transactions.
- **BifrostDB** (University of Yggdrasil): Causal consistency by default, with opt-in linearizability per operation. Designed for the PACELC PA/EC point — available during partitions with causal consistency, and consistent with bounded latency during normal operation.

### Required Reading

- Gilbert, S., Lynch, N. (2002). "Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services." *ACM SIGACT News* 33(2).
- Abadi, D. (2012). "Consistency Tradeoffs in Modern Distributed Database System Design." *IEEE Computer* 45(2).
- Hellerstein, J.M. (2010). "The Declarative Imperative: Experiences and Conjectures in Distributed Logic." *ACM SIGMOD Record* 39(1).

### Discussion Questions

1. A banking system needs to process transfers. Should it choose CP or AP during a partition? What are the implications for customer experience and regulatory compliance?
2. Gilbert and Lynch's proof assumes that availability means *every* non-faulty node responds. Is this the right definition? What if we define availability as "at least one node responds"? Does CAP still hold?
3. The CALM theorem suggests that monotonic computations don't need coordination. Which common distributed operations (counting, summing, finding maximum, finding minimum, set union, set intersection) are monotonic? Which require coordination?

### Practice Problems

- Draw the PACELC diagram and place the following systems: Spanner, Dynamo, Cassandra (QUORUM reads/writes), CockroachDB, and a simple in-memory cache with no replication.
- Consider a system with 5 replicas. A partition separates the system into groups of {1,2,3} and {4,5}. For each PACELC category, describe the system's behavior: (a) Does group {1,2,3} accept writes? (b) Does group {4,5} accept writes? (c) What happens after the partition heals?
- Prove or disprove: "If a system provides causal consistency during normal operation, it must reject some requests during a partition." Give a formal argument or a counterexample.

---

ᛁ **Lecture 7: Fault Tolerance and Failure Detection**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

A distributed system is only as reliable as its ability to detect and respond to failures. This lecture covers the theory and practice of failure detection — the fundamental building block on which all consensus and replication protocols depend. We study Chandra and Toueg's unreliable failure detectors, the interplay between suspicion and accuracy, and the practical algorithms used in modern systems.

### Key Topics

- **Failure Detection as a Substrate**: Why every consensus protocol needs a failure detector
- **Perfect vs. Unreliable Failure Detectors**: P, S, ♢S, and ♢P — the hierarchy of failure detector classes
- **The Heartbeat Protocol**: How most systems detect failures in practice
- **Suspicion and Accuracy**: The two properties that define a failure detector's quality
- **Phi Accrual Failure Detector**: Cassandra's probabilistic approach — continuous suspicion levels
- **Gossip-Based Failure Detection**: SWIM and its descendants
- **Cascading Failures and Circuit Breakers**: How failure detection prevents failure propagation

### Lecture Notes

The FLP impossibility result (Lecture 4) tells us that deterministic consensus is impossible in purely asynchronous systems. But Chandra and Toueg (1996) showed that consensus *is* possible in asynchronous systems if we augment them with a failure detector of the right strength. This result is profound: it separates the problem of detecting failures from the problem of reaching consensus, allowing us to reason about each independently.

A **failure detector** is a module at each process that provides information about which processes have crashed. Importantly, failure detectors can be *wrong* — they can suspect a process that is actually correct (a false suspicion) or they can fail to suspect a process that has actually crashed (a false trust). The quality of a failure detector is characterized by two properties:

1. **Completeness**: Every crashed process is eventually suspected by some correct process. (Detecting failures — not missing them)
2. **Accuracy**: Some correct process is never suspected. (Not raising false alarms)

Chandra and Toueg defined four classes of failure detectors based on different combinations of these properties:

- **Perfect (P)**: Strong completeness + strong accuracy. Every crash is detected, and no correct process is ever suspected. This is the ideal — but it's impossible in an asynchronous system.
- **Strong (S)**: Strong completeness + weak accuracy. Every crash is eventually detected, and at least one correct process is never suspected. Solves consensus with f < n/2 crash failures.
- **Eventually Strong (♢S)**: Strong completeness + eventual weak accuracy. Every crash is eventually detected, and eventually at least one correct process is never suspected. Also solves consensus with f < n/2.
- **Eventually Perfect (♢P)**: Strong completeness + eventual strong accuracy. Every crash is eventually detected, and eventually no correct process is suspected. Solves consensus with any number of crash failures.

The key insight: ♢S and ♢P can be implemented in *partially synchronous* systems. During asynchronous periods, they may make mistakes (suspecting correct processes or failing to detect crashes), but once the system becomes synchronous, they eventually stabilize to correct behavior. This is why Paxos and Raft work in practice — during normal operation (synchronous periods), their timeout-based failure detectors work correctly, and during network anomalies (asynchronous periods), they may make false suspicions but safety is never violated.

**Heartbeat protocols** are the most common implementation of failure detectors. Each process periodically sends a heartbeat message to all other processes. If a process doesn't receive a heartbeat from another process within a timeout period, it suspects that process. The challenge is choosing the timeout: too short and you get many false suspicions; too long and you delay detection of real failures.

The **Phi Accrual Failure Detector** (Hayashibara et al., 2004), used in Apache Cassandra, takes a probabilistic approach. Instead of a hard timeout, it computes the **phi value** — the probability that a heartbeat would not have arrived if the process were alive, based on the distribution of historical inter-arrival times. When phi exceeds a configurable threshold (typically 8.0, corresponding to ~99.999% confidence that the process has failed), the process is suspected. The accrual approach provides a continuous suspicion level rather than a binary alive/dead decision, allowing upper-level protocols to make more nuanced decisions.

**SWIM** (Scalable Weakly-consistent Infection-style Membership, Gupta et al., 2001) and its descendants (SWIM-Multicast, Lifeguard, Serf) provide failure detection in large-scale systems where individual heartbeats don't scale. Instead of all-to-all heartbeats, each process periodically selects a random target to ping. If the ping fails, the process asks k other processes to perform indirect pings (probes). This protocol is O(n) per process per round, regardless of cluster size, and provides probabilistic completeness with bounded false suspicion rates.

**Cascading failures** occur when a failure in one component causes failures in other components, which cause further failures, and so on. The 2024 AWS us-east-1 outage was a cascading failure: a control plane overload caused metadata service failures, which caused dependent services to time out, which caused retries that further overloaded the control plane. **Circuit breakers** (Hystrix pattern) prevent cascading failures by detecting when a downstream service is failing and temporarily stopping requests to it, giving it time to recover. In 2040, circuit breakers are mandatory infrastructure at the University of Yggdrasil — every inter-service call on the Bifrost Network goes through a circuit breaker with tuned thresholds.

### Required Reading

- Chandra, T.D., Toueg, S. (1996). "Unreliable Failure Detectors for Reliable Distributed Systems." *JACM* 43(2).
- Hayashibara, N., et al. (2004). "φ Accrual Failure Detector." *SRDS*.
- Gupta, I., et al. (2001). "SWIM: Scalable Weakly-consistent Infection-style Membership." *PODC*.

### Discussion Questions

1. The Phi Accrual failure detector computes a suspicion level. Contrast this with a binary alive/dead detector. In what situations is a suspicion level more useful? When might it be harmful?
2. SWIM provides O(n) gossip per process per round. But in a cluster of 10,000 nodes, detecting a failure still takes O(log n) rounds on average. Is this fast enough for a system that needs to react to failures within 5 seconds?
3. Circuit breakers prevent cascading failures, but they also reduce availability during a partial outage. How should you configure the circuit breaker thresholds for (a) a payment processing service, (b) a social media feed service, and (c) a health monitoring service?

### Practice Problems

- Implement a simple heartbeat failure detector in Python. Each process sends heartbeats every 1 second; a process is suspected if 3 heartbeats are missed. Inject random network delays and observe the false suspicion rate.
- Calculate the expected detection time for a Phi Accrual failure detector with normal inter-arrival times (mean=1s, std=0.1s) and threshold=8.0. What is the probability of a false suspicion during a 10-second window if no actual failures occur?
- Design a circuit breaker with the following parameters: request volume threshold=20, error percentage threshold=50%, sleep window=5s, half-open permits=3. Trace through a scenario where a downstream service starts failing.

---

ᛖ **Lecture 8: Distributed Transactions and Atomic Commit**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

A distributed transaction is an operation that spans multiple nodes and must either commit on all of them or abort on all of them. This lecture covers the classical atomic commit protocols (2PC, 3PC), modern approaches (Paxos commit, Spanner's TrueTime-based transactions), and the emerging consensus-transaction approach used by systems like CockroachDB and FaunaDB.

### Key Topics

- **Two-Phase Commit (2PC)**: The classical protocol — coordinator asks all participants to prepare, then commit or abort
- **Three-Phase Commit (3PC)**: Adding a pre-commit phase to avoid blocking — why it doesn't work in practice
- **Paxos Commit**: Using consensus for the commit decision — removing the single coordinator failure point
- **Spanner-style Transactions**: TrueTime + 2PC + Paxos — how Google achieves external consistency
- **Optimistic Concurrency Control**: Validation-based transactions without locks
- **Distributed Deadlock Detection**: The phantom menace of cross-node locks

### Lecture Notes

**Two-Phase Commit (2PC)** is the simplest and most widely used atomic commit protocol. A coordinator sends a PREPARE message to all participants. Each participant votes YES (ready to commit) or NO (must abort). If all vote YES, the coordinator sends COMMIT; if any vote NO, the coordinator sends ABORT. The protocol is simple and correct, but it has a fatal flaw: **blocking**. If the coordinator crashes after all participants have voted YES but before sending the COMMIT/ABORT decision, the participants are blocked indefinitely — they cannot commit (another participant might have voted NO) and they cannot abort (the coordinator might have decided COMMIT). They must wait for the coordinator to recover.

**Three-Phase Commit (3PC)** attempts to solve the blocking problem by adding a PRE-COMMIT phase. After all participants vote YES, the coordinator sends PRE-COMMIT. Only after all participants acknowledge the PRE-COMMIT does the coordinator send COMMIT. The idea is that if the coordinator crashes after the PRE-COMMIT phase, the surviving participants can infer that the decision was to commit (since they all received PRE-COMMIT) and proceed without the coordinator. Unfortunately, 3PC assumes synchronous communication — it requires known timeouts and does not work in asynchronous systems with crash failures. In practice, 3PC is rarely used because real networks don't provide the timing guarantees it needs.

**Paxos Commit** (Gray and Lamport, 2006) solves the coordinator failure problem by using consensus for the commit decision. Instead of a single coordinator deciding COMMIT or ABORT, the decision is made by a Paxos group. If the original coordinator fails, the Paxos group can still reach a decision, so the protocol never blocks. The cost: every transaction requires a consensus decision, adding latency proportional to the Paxos round trip time.

**Spanner's approach** is more integrated. Spanner uses TrueTime timestamps to provide external consistency — every transaction is assigned a timestamp, and transactions are committed in timestamp order. For distributed transactions (spanning multiple Paxos groups), Spanner uses a two-phase commit where the coordinator is chosen via leader election and the commit decision is replicated via Paxos. The key innovation: TrueTime's bounded clock uncertainty means that once a transaction's timestamp has passed (i.e., the current time is definitely past the transaction's commit time), all subsequent transactions are guaranteed to see its effects.

**Optimistic Concurrency Control (OCC)** takes a different approach: instead of locking resources before modifying them, transactions read and modify data without coordination, then validate at commit time. If the validation succeeds (no conflicting modifications), the transaction commits; if not, it aborts and retries. OCC works well when conflicts are rare, but it degrades badly under contention because transactions waste work on aborts. In distributed settings, OCC validation requires checking that the read set hasn't been modified across all replicas — this is essentially a distributed read lock with a optimistic implementation.

**Distributed deadlock detection** is the phantom menace of distributed transactions. When transaction T1 holds a lock on resource A and waits for lock B, and transaction T2 holds lock B and waits for lock A, we have a deadlock. In a distributed system, these locks may span multiple nodes, making detection harder. The classical approach is centralized deadlock detection (one node collects all lock graphs), but this creates a single point of failure. Distributed deadlock detection uses edge-chasing algorithms (e.g., Obermarck's algorithm) where deadlock probes are propagated along wait-for edges. In practice, most systems in 2040 use timeout-based deadlock prevention — if a transaction has been waiting for more than N seconds, abort it and try again. This is simpler than detection and avoids the overhead of building global lock graphs.

### Required Reading

- Gray, J. (1978). "Notes on Data Base Operating Systems." *Operating Systems: An Advanced Course*, Springer.
- Gray, J., Lamport, L. (2006). "Consensus on Transaction Commit." *ACM TODS* 31(1).
- Corbett, J.C., et al. (2012). "Spanner: Google's Globally-Distributed Database." *OSDI*.

### Discussion Questions

1. 2PC blocks on coordinator failure. 3PC doesn't block but requires synchronous assumptions. Paxos Commit doesn't block but requires a consensus round. Is there a way to get atomic commit without any of these costs? Prove or disprove.
2. Spanner's TrueTime approach is often criticized for requiring specialized hardware (GPS, atomic clocks). Can you achieve external consistency without TrueTime? What are the alternatives?
3. OCC aborts transactions on conflict. In a high-contention system (e.g., a popular item in an e-commerce store), OCC's abort rate can be catastrophically high. What techniques can reduce this problem without resorting to pessimistic locking?

### Practice Problems

- Implement 2PC in Python with 1 coordinator and 3 participants. Test the following scenarios: (a) all participants vote YES, (b) one participant votes NO, (c) coordinator crashes after all votes are collected. In scenario (c), implement recovery so that the participants can eventually commit or abort.
- Prove that 3PC cannot block in the synchronous model with crash-stop failures and at most f < n crash failures. Then show it *can* block in the asynchronous model.
- Compare the latency of a distributed transaction using (a) 2PC with one coordinator, (b) Paxos Commit with 5 acceptors. Assume each message round trip takes 10ms and all participants are in the same region.

---

ᚾ **Lecture 9: CRDTs — Conflict-Free Replicated Data Types**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

CRDTs are the most significant development in distributed systems theory in the last two decades. By mathematically guaranteeing that concurrent updates never conflict, CRDTs make it possible to have *both* availability and eventual consistency *with* deterministic convergence — effectively achieving "CA" in CAP, bypassing the theorem by weakening the consistency model. This lecture covers the theory, the major data types, and the practical systems that use CRDTs in 2040.

### Key Topics

- **The CRDT Insight**: If the merge operation is commutative, associative, and idempotent, replicas can never conflict
- **State-Based CRDTs (CvRDTs)**: Replicas send their full state; merge function is a semilattice join
- **Operation-Based CRDTs (CmRDTs)**: Replicas send operations; operations are commutative
- **The Semilattice Property**: Join-semilattices and why they guarantee convergence
- **CRDTs in Practice**: Counters (G-Counter, PN-Counter), sets (G-Set, OR-Set), registers (LWW-Register, MV-Register), maps, sequences
- **Collaborative Editing as a CRDT**: The RGA, Yjs, and Automerge approaches
- **BifrostDB and the CRDT-Native Database**: How the University of Yggdrasil's research database uses CRDTs as the primary data model

### Lecture Notes

The fundamental insight behind CRDTs is deceptively simple: **if the merge operation forms a semilattice, then replicas can update independently and merge later without conflict.** A semilattice is a partially ordered set where any two elements have a least upper bound (join operation). The join operation must be:

1. **Commutative**: `merge(A, B) = merge(B, A)` — order doesn't matter
2. **Associative**: `merge(merge(A, B), C) = merge(A, merge(B, C))` — grouping doesn't matter
3. **Idempotent**: `merge(A, A) = A` — applying the same update twice has no effect

If these properties hold, then it doesn't matter what order updates arrive in, how many times they're applied, or whether replicas are temporarily disconnected. Every merge brings the state closer to the eventual converged value, and convergence is guaranteed when all updates have been delivered.

**State-based CRDTs (CvRDTs)** replicate by sending their full state. Each replica maintains its local state and periodically broadcasts it to other replicas. When a replica receives another replica's state, it merges it with its own using the semilattice join operation. The merge is guaranteed to be correct because the join operation is commutative, associative, and idempotent. The cost: sending the entire state for each update can be expensive. Optimizations like state deltas (sending only the changed parts) reduce this overhead.

**Operation-based CRDTs (CmRDTs)** replicate by sending operations (e.g., "increment counter by 1" or "add element X to set"). These operations must be commutative — they must produce the same final state regardless of the order in which they're applied. This is a stronger requirement than for state-based CRDTs, because the operation's effect must commute with all other operations. The advantage is that operations are typically much smaller than full states, making them more efficient to transmit.

**G-Counter** (Grow-only Counter): The simplest state-based CRDT. Each of n replicas maintains a vector of n integers, one per replica. To increment, a replica increments its own entry. To merge, take the element-wise maximum of the two vectors. The counter value is the sum of all entries. This counter can only grow; it cannot be decremented.

**PN-Counter** (Positive-Negative Counter): Two G-Counters — one for increments, one for decrements. The value is the difference. This allows counting up and down. Both counters merge independently. The cost: twice the state of a G-Counter.

**OR-Set** (Observed-Remove Set): The most widely used set CRDT. Elements are added with unique tags (typically a replica ID + sequence number). When adding, a new tag is created for the element. When removing, all tags for the element that are currently visible are recorded. Merge resolves conflicts by: if an add tag is present and its tag was not in the remove set, the element is in the set. This implements "add wins" semantics — if an element is concurrently added and removed, the add wins. This is the semantics most users expect.

**RGA (Replicated Growable Array)**: A sequence CRDT for collaborative editing. Each character in the document is assigned a unique identifier that encodes its position relative to other characters, even under concurrent edits. The merge operation resolves concurrent inserts by comparing identifiers and placing characters in a deterministic order. RGAs form the basis of most collaborative editing systems in 2040.

**Yjs** (Nicolaus, 2020) is a production-quality CRDT implementation for collaborative editing that uses a highly optimized encoding: instead of storing the full RGA, Yjs stores only the differences (item updates) and computes the full state on demand. This reduces memory usage from O(n²) to O(n) for n elements. Yjs is used by Figma, Affine, and many other collaborative editing applications.

**Automerge** (Kleppmann, et al., 2019) is another approach to CRDT-based collaborative editing, originally developed for peer-to-peer applications. Automerge uses a JSON-like document model where every field is a CRDT. It was originally slower than Yjs for large documents, but the 2024 version (Automerge 3.0) uses a columnar storage format inspired by database internals that achieves competitive performance.

**BifrostDB** is the University of Yggdrasil's research database, designed from the ground up around CRDTs. Its key innovation: instead of applying CRDTs as an afterthought (as in most NoSQL databases), BifrostDB uses CRDTs as the *primary data model*. Every column type in BifrostDB is a CRDT — counters, sets, registers, and even complex types like CRDT maps and sequences. This means that every BifrostDB table is automatically mergeable, without any application-specific conflict resolution logic. BifrostDB's query planner can push queries down to replicas and merge the results using the CRDT merge functions, enabling low-latency reads without sacrificing consistency guarantees.

The philosophical lesson of CRDTs is profound: **conflict is not inherent in distributed systems — it's an artifact of data representations that don't have merge functions.** By choosing data representations that are inherently mergeable, we can eliminate conflict entirely. This is the CALM theorem in action: monotonic operations on semilattice-structured data are coordination-free.

### Required Reading

- Shapiro, M., et al. (2011). "Conflict-Free Replicated Data Types." *SSS*.
- Kleppmann, M., Beresford, A. (2017). "A Conflict-Free Replicated JSON Datatype." *IEEE TPDS* 27(10).
- Nicolaus, K. (2020). "Yjs: A CRDT Framework for Collaborative Editing." *GitHub repository documentation and benchmarks*.

### Discussion Questions

1. OR-Sets implement "add wins" semantics for concurrent add/remove operations. What other conflict resolution policies could be useful? When would "remove wins" be preferable?
2. CRDTs guarantee convergence, but the converged state may not be what any user intended. Give an example where CRDT merge produces a semantically wrong result, even though it's technically correct.
3. BifrostDB uses CRDTs as the primary data model. What are the limitations of this approach? Can you express foreign key constraints, uniqueness constraints, or complex join operations in a CRDT-native database?

### Practice Problems

- Implement a G-Counter and a PN-Counter in Python. Test that both counters converge to the same value regardless of the order of merges.
- Implement an OR-Set that supports add(element), remove(element), and merge(other_set). Verify that concurrent add and remove of the same element results in the element being present (add wins).
- Compare the space overhead of a G-Counter with n replicas versus a simple integer counter. At what value of n does the overhead become significant? (Consider memory and network bandwidth separately.)

---

ᛉ **Lecture 10: Fault-Tolerant Storage — Erasure Coding and Replication Strategies**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Data durability is the central promise of any storage system: if you write data, it should be readable later, even if components fail. This lecture covers the two primary techniques for achieving durability at scale — replication and erasure coding — and the systems that use each approach.

### Key Topics

- **Replication Factor**: How many copies is enough? The mathematics of independent failure probabilities
- **Erasure Coding**: Reed-Solomon codes, the fundamental trade-off between storage overhead and reconstruction cost
- **Comparison**: When replication beats erasure coding and vice versa
- **Locality and Repair**: Regenerating codes and the repair bandwidth problem
- **Consistent Hashing**: Distributing data across nodes with minimal remapping on topology changes
- **Basetime and Repair Time**: Mean Time To Data Loss (MTTDL) calculations

### Lecture Notes

The simplest approach to data durability is **full replication**: store k complete copies of each data object on k different nodes. If each node has an independent failure probability p per unit time, then the probability that all k copies fail simultaneously is p^k. With 3-way replication (the standard in most production systems) and a per-disk annual failure rate of 2%, the probability of losing all three copies in a year is 0.0008% — roughly one loss in 125,000 years per object. This sounds reassuring, but it doesn't account for correlated failures (power outages, buggy firmware updates, datacenter fires) or the cascading failure scenarios discussed in Lecture 7.

**Erasure coding** reduces storage overhead by breaking each data object into k data fragments and m parity fragments, such that any k of the (k+m) fragments are sufficient to reconstruct the original data. The storage overhead is (k+m)/k, compared to k for k-way replication. For example, with a (10,4) Reed-Solomon code (k=10, m=4), the overhead is 1.4x — compared to 3x for 3-way replication. The catch: reconstructing a lost fragment requires reading k other fragments and performing O(k²) finite field operations. This makes erasure coding significantly more expensive than replication for *repair* operations.

The **repair bandwidth problem** is erasure coding's Achilles' heel. When a single fragment is lost, a k-of-(k+m) code requires reading k fragments (typically from k different nodes) to reconstruct the original data and regenerate the lost fragment. For a (10,4) code, this means transferring 10 units of data to repair 1 unit — a 10x overhead. Compare with 3-way replication, where repair requires transferring only 1 unit from a surviving replica — a 1x overhead. This 10x factor matters enormously in practice: it determines how quickly a storage system can recover from a disk failure and return to full redundancy.

**Regenerating codes** (Dimakis et al., 2010) reduce repair bandwidth by allowing nodes to send linear combinations of their fragments rather than complete fragments. The fundamental trade-off: for a given storage overhead and data reconstruction threshold, there is a minimum repair bandwidth below which it's impossible to go. This is the **storage-repair bandwidth trade-off** — a curve that shows the minimum repair bandwidth achievable for each point on the storage overhead spectrum. MBR (Minimum Bandwidth Regenerating) codes minimize repair bandwidth at the cost of higher storage; MSR (Minimum Storage Regenerating) codes minimize storage at the cost of higher repair bandwidth.

**Consistent hashing** (Karger et al., 1997) is the standard technique for distributing data across a cluster. Each data key is hashed to a point on a circle (ring), and each node is responsible for the keys that hash to the arc counterclockwise from its position. When a node joins or leaves, only the keys in its arc need to be remapped. This makes topology changes cheap — O(1/n) of the keys move, compared to O(1) for a modulo-based distribution. Apache Cassandra, Amazon DynamoDB, and Riak all use consistent hashing with virtual nodes (vnodes) to balance load more evenly.

**MTTDL (Mean Time To Data Loss)** is the key metric for storage reliability. For a replicated system with n replicas and repair time T_repair, the MTTDL is approximately:

```
MTTDL ≈ (MTTF_disk)^n / (n * T_repair^(n-1))
```

where MTTF_disk is the Mean Time To Failure of a single disk. This formula assumes independent failures and immediate repair starts when a failure is detected. In practice, correlated failures and repair time variability make MTTDL calculations an upper bound on actual reliability.

In 2040, most large-scale storage systems use a combination of replication and erasure coding: data is replicated within a datacenter (for fast reads and cheap repairs), and erasure-coded across datacenters (for geo-redundancy with minimal storage overhead). The University of Yggdrasil's Bifrost Storage System uses 3-way replication within each datacenter and a (10,4) Reed-Solomon code across 4 datacenters, achieving a storage overhead of 3.6x (3x local + 0.6x remote) and a theoretical MTTDL of over 10^9 years.

### Required Reading

- Dimakis, A.G., et al. (2010). "Network Coding for Distributed Storage Systems." *IEEE Trans. Inf. Theory* 56(3).
- Karger, D., et al. (1997). "Consistent Hashing and Random Trees." *STOC*.
- Weil, S.A., et al. (2006). "CRUSH: Controlled, Scalable, Decentralized Placement of Replicated Data." *OSDI*.

### Discussion Questions

1. Calculate MTTDL for the following configurations: (a) 3-way replication, MTTF_disk=1M hours, T_repair=24 hours; (b) (10,4) erasure coding, same parameters; (c) (10,4) erasure coding, T_repair=240 hours (10 days). What do you conclude?
2. Why doesn't everyone use erasure coding instead of replication? Calculate the repair bandwidth for a (10,4) code when the object is 1GB and compare with 3-way replication.
3. Consistent hashing minimizes data movement on topology changes. But it doesn't minimize request routing distance. How do modern systems like Ceph's CRUSH algorithm improve on consistent hashing for data placement?

### Practice Problems

- Implement a simple consistent hash ring in Python. Support add_node, remove_node, and get_node(key) operations. Verify that when a node is added, only keys in the new node's arc are remapped.
- Calculate the storage overhead and minimum repair bandwidth for: (a) 3-way replication; (b) (6,3) Reed-Solomon; (c) (10,4) Reed-Solomon; (d) a hypothetical MSR code with storage overhead 1.5x.
- Simulate a (10,4) erasure-coded storage system with 14 nodes. Remove 3 random nodes and verify that all objects can still be reconstructed. Remove the 4th node — what happens?

---

ᚺ **Lecture 11: Distributed Locking, Leader Election, and Coordination Services**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Many distributed algorithms require coordination: electing a leader, acquiring a lock, or maintaining group membership. This lecture covers the practical coordination services that provide these primitives — ZooKeeper, etcd, and Consul — and the algorithms they use internally.

### Key Topics

- **Distributed Mutual Exclusion**: The problem of locking across nodes
- **Leader Election**: Ring-based, bully, and Raft-based election
- **ZooKeeper**: The hierarchical coordination service that started it all
- **etcd and Consul**: Modern alternatives built on Raft
- **Leases vs. Locks**: Why leases are often better than locks in distributed systems
- **Fencing Tokens**: The critical missing piece in many lock implementations
- **Group Membership**: The dynamic subset problem — who's in and who's out?

### Lecture Notes

**Distributed mutual exclusion** is the problem of ensuring that at most one process at a time can execute a critical section. In a single-machine system, this is solved by mutex locks and semaphores. In a distributed system, it's solved by algorithms that combine message passing with logical timestamps:

- **Lamport's mutual exclusion algorithm** uses a total order of requests (based on Lamport timestamps) and requires O(n) messages per critical section entry (3n if acknowledgments are counted). Each process maintains a request queue sorted by timestamp, and grants access to the process with the smallest timestamp.
- **Ricart-Agrawala's algorithm** reduces this to 2(n-1) messages by combining the request and acknowledgments into a single round trip. A process requesting the critical section sends a request to all other processes; a process grants access unless it has an earlier request pending.
- **Maekawa's algorithm** reduces this further to O(√n) messages by having each process consult only a subset (quorum) of other processes, such that any two quorums overlap. This is the same quorum intersection property used in consensus protocols.

In practice, distributed mutual exclusion is almost never implemented using these algorithms. Instead, it's provided by a **coordination service** — a centralized (but replicated for fault tolerance) service that manages locks, leader election, and group membership.

**ZooKeeper** (Hunt et al., 2010) is the grandfather of coordination services. It provides a hierarchical namespace (like a filesystem) where each node (called a "znode") can store a small amount of data. Clients can create, read, write, and delete znodes, and crucially, they can set **watches** on znodes that trigger when the znode changes. ZooKeeper uses a variant of Multi-Paxos internally for consensus and provides the following guarantees: linearizable writes, FIFO client ordering, and sequential consistency for reads.

ZooKeeper implements distributed locks using **ephemeral nodes** — znodes that are automatically deleted when the client session that created them ends. To acquire a lock, a client creates an ephemeral sequential znode under a lock parent znode (e.g., `/locks/my-lock/lock-0000000001`). If the client's znode has the lowest sequence number, it holds the lock. If not, it watches the znode with the next-lower sequence number and waits for it to be deleted. This is called the **herd effect avoidance** pattern — only one watcher per lock contender, not n watchers all rushing for the lock simultaneously.

**etcd** (2014) is a modern coordination service built on Raft. It provides a flat key-value store (not hierarchical like ZooKeeper) with the same linearizable writes and FIFO client ordering guarantees. etcd is the backing store for Kubernetes, which stores all cluster state (pods, services, config maps, secrets) in etcd. The etcd team at CoreOS (later acquired by Red Hat) chose Raft specifically for its understandability, arguing that the ZooKeeper codebase had become unmaintainable due to Paxos's complexity.

**Consul** (HashiCorp, 2014) is a coordination service that combines key-value storage with service discovery and health checking. It uses Raft for consensus (in the key-value store) and a gossip protocol (SWIM-based) for cluster membership. Consul's killer feature is its **service mesh** — it can automatically configure proxy sidecars for inter-service communication, providing encryption, observability, and traffic management without application changes.

**Leases vs. Locks** is one of the most important practical distinctions in distributed systems. A **distributed lock** grants exclusive access to a resource until the holder explicitly releases it. A **lease** grants exclusive access for a fixed time period. The crucial difference: if the lock holder crashes, the lock is held forever (or until a timeout mechanism kicks in), but a lease expires automatically. Leases are superior in almost all practical scenarios because they're **self-releasing** — even if the holder crashes, the lease eventually expires and the resource becomes available again.

**Fencing tokens** (also called epoch numbers or generation numbers) are a critical safety mechanism that many lock implementations overlook. The problem: a client acquires a lock, enters a critical section, crashes, and then reacquires the lock after restarting. But the client's first critical section may still be executing (or its effects may still be propagating) — the system now has two processes in the same critical section. The solution: every lock acquisition returns a monotonically increasing fencing token, and every resource that the lock protects must check the fencing token before accepting an operation. If the token is stale (lower than the last seen token), the operation is rejected. This is why ZooKeeper's sequential znodes and etcd's revision numbers are so important — they provide the fencing tokens automatically.

### Required Reading

- Hunt, P., et al. (2010). "ZooKeeper: Wait-Free Coordination for Internet-Scale Systems." *USENIX ATC*.
- Howard, H., et al. (2015). "Dynamo: Amazon's Highly Available Key-Value Store." *SOSP* (reprint with 2015 context).
- Chandra, T.D., et al. (2007). "Paxos Made Live — An Engineering Perspective." *PODC*.

### Discussion Questions

1. ZooKeeper uses a hierarchical namespace, while etcd uses a flat key-value store. What are the advantages and disadvantages of each approach for coordination primitives?
2. Fencing tokens prevent stale lock holders from corrupting shared state. But they require every resource server to maintain fencing token state. Is this overhead justified for all applications, or only for specific ones? Give examples.
3. In a system with 100,000 clients competing for 1,000 locks, what is the maximum throughput of ZooKeeper's lock service? Consider the message pattern: create, watch, notification, delete. What bottlenecks limit scalability?

### Practice Problems

- Implement a distributed lock using ZooKeeper's ephemeral sequential node pattern. Test it with 5 concurrent clients and verify mutual exclusion.
- Implement leader election using etcd. Three candidates compete for leadership; when the leader fails, a new leader is elected within 10 seconds. Verify that at most one leader exists at any time.
- Design a coordination service for a distributed task queue. The service must support: (a) enqueueing tasks, (b) dequeuing tasks (with exactly-once semantics), (c) tracking task status (pending, in_progress, completed, failed). What data structures and coordination primitives would you use?

---

ᛜ **Lecture 12: The Future of Distributed Systems — Edge, Quantum, and Beyond**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

This final lecture steps back from the algorithms and protocols to examine the emerging forces reshaping distributed systems in 2040 and beyond. Edge computing pushes computation closer to users; quantum networking promises fundamentally new communication primitives; and AGI-era systems demand new models of verification, trust, and governance. We synthesize the course's themes and project them forward.

### Key Topics

- **Edge-to-Cloud Continuum**: From datacenter to edge to device — the tiered computing model of 2040
- **Quantum Networking**: Entanglement-based communication, quantum repeaters, and the Bifrost Research Network
- **Proof-of-Stake and BFT in Production**: How blockchains solved (and didn't solve) the distributed consensus problem
- **AGI-Era Distributed Systems**: Verification of autonomous agents, proof-carrying data, and the alignment problem in distributed contexts
- **The Local Knowledge Principle, Revisited**: Why distributed systems theory matters more than ever in the age of AGI
- **Course Synthesis**: The unifying themes of CS301 and the road ahead

### Lecture Notes

**Edge computing** is not a new idea — content delivery networks (CDNs) have been pushing data to the edge since the 1990s. What's new in 2040 is the *computation* at the edge. Modern edge nodes are not just caches; they run inference models, perform data filtering and aggregation, and make autonomous decisions. The **edge-to-cloud continuum** is a three-tier architecture:

1. **Device tier**: IoT sensors, wearables, autonomous vehicles. Limited compute, intermittent connectivity. Must make real-time decisions locally.
2. **Edge tier**: Micro-datacenters in metro areas, cell tower sites, and satellite ground stations. Moderate compute, low latency to devices. Runs model inference, data aggregation, and lightweight coordination.
3. **Cloud tier**: Large datacenters running training, analytics, and global coordination. High compute, high latency from devices.

The key challenge: **data consistency across tiers**. A device may update state that the edge node hasn't seen, or the edge may make a decision based on stale cloud data. CRDTs (Lecture 9) are now the standard approach for cross-tier state synchronization — device state is modeled as CRDTs that merge upward periodically. The University of Yggdrasil's own sensor network uses this architecture: each sensor runs a local CRDT, edge nodes aggregate state from thousands of sensors and merge it with the cloud, and the cloud provides global queries and analytics.

**Quantum networking** represents the most fundamental shift in distributed systems since the internet. Quantum entanglement enables two operations that classical networks cannot provide:

1. **Quantum key distribution (QKD)**: Two parties can establish a shared secret key that is provably secure against any eavesdropping, based on the laws of quantum mechanics (not computational assumptions). Any attempt to intercept the quantum channel disturbs the entangled particles and is detected.
2. **Quantum teleportation**: A quantum state can be transmitted from one location to another using entanglement and classical communication, without the quantum state itself traversing the intervening space. This does not enable faster-than-light communication (classical communication is still required), but it enables the transfer of quantum information (qubits) across physical distance.

The Bifrost Research Network at the University of Yggdrasil operates one of the world's longest quantum-secured links, connecting nodes in Reykjavik, Oslo, and Tórshavn via undersea fiber with quantum repeaters. This link provides QKD for all administrative communication between nodes, ensuring that keys are refreshed every 100 milliseconds — far beyond what classical key exchange can achieve.

**Blockchain and BFT consensus** have had a complicated relationship with the distributed systems community. On one hand, blockchains like Ethereum demonstrated that BFT consensus could be run in a permissionless setting with billions of dollars at stake — a deployment scale that academic BFT research had never achieved. On the other hand, blockchains introduced new problems (MEV extraction, governance attacks, energy waste in proof-of-work) that were not anticipated by the classical BFT literature. In 2040, proof-of-stake blockchains (Ethereum 2.0+, Solana, and others) use BFT consensus adapted for open participation. The resulting systems are impressive in scale but fragile in new ways — governance decisions can be influenced by economic power, and the "unpredictability" needed for proposer selection creates new attack surfaces.

**AGI-era distributed systems** present challenges that CS301's classical theory wasn't designed to address. When autonomous agents can modify their own code, make decisions that affect millions of users, and coordinate at speeds beyond human oversight, we need new verification and governance mechanisms:

- **Proof-carrying data**: Every piece of data carries a cryptographic proof of its provenance and processing history. Agents can verify the integrity of data without trusting the producer.
- **Formal verification at scale**: The same techniques used to verify consensus protocols (model checking, theorem proving) are being applied to agent behavior specifications. The challenge: specifications themselves may be ambiguous or incomplete.
- **Distributed governance**: How do you make decisions about a system that spans thousands of nodes and serves billions of users? On-chain governance (voting) and off-chain governance (councils, constitutions) each have strengths and weaknesses.
- **The alignment problem in distributed contexts**: Ensuring that an AGI system's behavior is aligned with human values is hard enough in a centralized setting. In a distributed setting, where agents may have incomplete information about global state and may receive conflicting instructions from different principals, alignment becomes even harder.

**The Local Knowledge Principle**, which we introduced in Lecture 1, turns out to be more relevant than ever. In an AGI-era distributed system, the "local knowledge" of each agent includes not just the state of its own processes but also its understanding of the global system's goals, constraints, and values. The gap between local knowledge and global reality is the fundamental challenge of distributed AI — and it's the same challenge that distributed systems theory has been grappling with since Lamport's 1978 paper.

### Course Synthesis

The twelve lectures of CS301 have covered a journey from the abstract foundations (system models, impossibility results) to the practical algorithms (Raft, CRDTs, coordination services) to the emerging future (edge computing, quantum networking, AGI-era systems). The unifying themes are:

1. **Failures are not exceptional — they are the normal case.** Distributed systems must be designed for failure. Every algorithm must work correctly even when messages are lost, processes crash, and clocks drift.
2. **Consistency and availability are often in tension, but not always.** CRDTs and causal consistency show that we can have both, with caveats. The art is choosing the right point on the spectrum for each application.
3. **Time is not fundamental — causality is.** The happened-before relation, not physical time, is the foundation of distributed systems reasoning. Logical clocks, vector clocks, and hybrid logical clocks all encode this insight.
4. **Verification is mandatory.** Distributed systems fail in ways that are hard to reproduce and harder to diagnose. Model checking, theorem proving, and rigorous testing are not luxuries — they are prerequisites for production deployment.
5. **The theory-practice gap is real but narrowing.** FLP is an impossibility result, but real systems achieve consensus every day. The gap between theory and practice is bridged by partial synchrony, failure detectors, randomness, and pragmatic engineering.

### Required Reading

- Satyanarayanan, M., et al. (2009). "The Case for VM-Based Cloudlets in Mobile Computing." *IEEE Pervasive Computing*.
- Amazon Web Services (2040). "Graviton Quantum: Secure Key Distribution for Cloud Applications." *AWS Whitepaper*.
- UoY AGI Safety Group (2039). "Proof-Carrying Data for Autonomous Agent Systems." *Bifrost Technical Report BFT-2039-12*.

### Discussion Questions

1. Edge computing pushes computation closer to users, but it also increases the attack surface — more locations means more physical security risks. How should we secure edge nodes that are physically accessible (unlike datacenter servers)?
2. Quantum key distribution provides provable security against eavesdroppers, but it requires dedicated fiber optic infrastructure. Is QKD worth the cost? What alternative approaches provide comparable security guarantees?
3. In 2040, autonomous agents make decisions that affect millions of people. How should we verify that these agents are behaving correctly? Is formal verification sufficient, or do we need new approaches?

### Practice Problems

- Design the state synchronization layer for an edge-to-cloud system using CRDTs. The system manages inventory levels for a retail chain. Each store is an edge node; the cloud aggregates inventory across all stores. What CRDT types would you use? How would you handle the case where a store counts 10 items while the cloud has 8 (because the store hasn't synced yet)?
- Calculate the key generation rate for a QKD system running over a 100km fiber link with 80% transmission efficiency and a 10MHz photon source. Assume 50% of photons produce usable key bits after error correction and privacy amplification.
- Write a 2-page essay: "Distributed Systems in the Age of AGI — What Stays the Same and What Changes." Use concepts from at least 5 lectures in this course.

---

## Final Examination Preparation

The final examination for CS301 consists of 8 questions, of which you must choose 4 to answer in depth. Each answer should demonstrate understanding of both theory and practice, with reference to specific algorithms, proofs, and systems discussed in the course.

### Essay Questions (Choose 4 of 8)

**Question 1**: "Consensus is the most important problem in distributed systems." Evaluate this claim with reference to FLP impossibility, Paxos/Raft, and the practical challenges of implementing consensus in production systems. Consider both sides: is there anything more fundamental than consensus?

**Question 2**: Compare and contrast linearizability, causal consistency, and eventual consistency as consistency models. For each, describe: (a) a real system that implements it, (b) the performance implications, (c) the types of applications it's suitable for, and (d) the types of applications it's unsuitable for.

**Question 3**: The CAP theorem states that in the presence of partitions, you must choose between consistency and availability. The PACELC model extends this to include latency-consistency trade-offs in normal operation. Analyze a globally distributed social media platform and specify the consistency model you would recommend for each of the following data types: user profiles, follower lists, direct messages, news feed posts, and trending topics. Justify each recommendation using PACELC.

**Question 4**: "CRDTs eliminate the need for coordination in distributed systems." Evaluate this claim. Describe what CRDTs can and cannot achieve. In what situations are CRDTs superior to consensus-based approaches? When are they insufficient?

**Question 5**: Design a distributed key-value store that provides causal consistency, read-your-writes, and monotonic reads across 5 globally distributed replicas. Specify: (a) the data model and CRDT types used, (b) the read and write protocols, (c) the clock structure (what type of logical clock), and (d) how session guarantees are maintained during client reconnections.

**Question 6**: Analyze the failure detection requirements for the following systems: (a) a Raft cluster with 5 nodes in one datacenter, (b) a globally distributed database with 100 nodes across 10 regions, (c) an edge computing system with 10,000 sensor nodes. For each, specify the failure detector class needed, the implementation approach, and the expected detection latency.

**Question 7**: Compare erasure coding and replication for data durability. Given a cluster of 100 nodes with individual disk annual failure rate of 2%, target data durability of 99.999999% (eight nines), and a requirement that any single object can be read with latency under 50ms, which approach would you choose? Justify your answer with calculations.

**Question 8**: "In the age of AGI, distributed systems theory is obsolete — intelligent agents will figure out coordination dynamically without needing explicit protocols." Present arguments for and against this position. Draw on specific impossibility results (FLP, CAP, Byzantine agreement lower bounds) and consider whether AGI can circumvent fundamental constraints.

---

*"The network is reliable, latency is zero, bandwidth is infinite, the network is secure, topology doesn't change, there is one administrator, transport cost is zero, the network is homogeneous, clocks are synchronized, state is consistent by default, partial failure doesn't happen, causality is obvious, human operators read the manual, and quantum decoherence is someone else's problem. None of this is true. That's why we have a course."*

*— Inscription on the wall of the UoY Distributed Systems Laboratory, 2040*ate the trade-off space

### Lecture Notes

Eric Brewer's 2000 PODC keynote proposed the conjecture that a distributed system can provide at most two of three guarantees: **Consistency** (every read returns the most recent write), **Availability** (every request receives a non-error response), and **Partition tolerance** (the system operates despite network partitions). Seth Gilbert and Nancy Lynch proved the conjecture formally in 2002.

The proof is straightforward: consider a network partition that splits the system into two groups, A and B, that cannot communicate. A client writes to a key in group A and then reads the same key from group B. Two outcomes are possible: (1) group B returns an error — availability is violated; or (2) group B returns a stale value — consistency is violated. There is no third option, because group B cannot know about group A's write without communication across the partition.

**What CAP actually says**: In the presence of a partition, the system designer must choose between consistency and availability. This is not about choosing two out of three — partition tolerance is non-negotiable in any real distributed system, because network partitions *will* happen. The choice is really about what happens *during* a partition: do you return stale data (CP — consistent, partition-tolerant) or do you return errors (AP — available, partition-tolerant)?

**What CAP does not say**: It says nothing about what happens when there is no partition, which is the vast majority of the time. A system can be both consistent and available when the network is healthy, and only need to make the trade-off during rare partition events. This observation led Kleppmann (2017) and others to argue that CAP is overrated as a design tool.

**The PACELC model** (Abadi, 2012) extends CAP to capture the latency-consistency trade-off *during normal operation*. PACELC stands for: If there is a Partition (P), the system chooses between Availability (A) and Consistency (C); Else (E), when running normally, it chooses between Latency (L) and Consistency (C). This model correctly captures the fact that even without partitions, stronger consistency requires more coordination (hence more latency). For example:

- **Spanner** (Google): P→C, E→C — always consistent, at the cost of higher latency even during normal operations (TrueTime commit wait).
- **Cassandra**: P→A, E→L — available during partitions, low latency during normal ops, but eventually consistent.
- **CockroachDB**: P→C, E→C — always consistent, uses Raft for coordination, higher write latency than Cassandra but lower than cross-continent Spanner.

**Harvest and Yield** (Fox and Brewer, 1999) provide an alternative framing. *Yield* is the probability that a request completes successfully. *Harvest* is the fraction of the database that is available for queries. Under normal conditions, both are 100%. During failures, you can sacrifice some harvest (return incomplete results) to maintain yield. This is the approach taken by search engines and analytics systems — returning results from 99% of your data is usually acceptable, and certainly better than returning an error.

**The CALM theorem** (Ameloot et al., 2011) provides a theoretical framework for understanding which computations can be performed without coordination. A program written as a monotonic function (one whose output only grows, never shrinks) can be evaluated without coordination while still producing consistent results. This is profound: it means that if you can express your computation monotonically, you can have both consistency and availability. CRDTs (Lecture 7) are a practical embodiment of this principle.

In 2040, the community has largely moved beyond simplistic CAP reasoning. Modern systems like CockroachDB, TiDB, and the University of Yggdrasil's BifrostDB offer configurable consistency levels per operation, allowing the same system to provide linearizable reads for financial transactions and causal reads for social feeds. The Yggdrasil approach uses a *consistency gradient*: operations start at causal consistency and are promoted to linearizable only when the application explicitly requests it, minimizing coordination overhead for the common case.

### Required Reading

- Gilbert, S., Lynch, N. (2002). "Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services." *ACM SIGACT News* 33(2).
- Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly. Chapter 5 (Replication) and Chapter 7 (Transactions).
- Abadi, D. (2012). "Consistency Tradeoffs in Modern Distributed Database System Design: CAP is Only Part of the Story." *IEEE Computer* 45(2).

### Discussion Questions

1. During the AWS us-east-1 outage of December 2021, many AWS services became unavailable. Were these CP systems that chose C over A, or AP systems that lost availability despite sacrificing C? Analyze at least two affected services.
2. A banking system that must never lose a transaction clearly needs CP behavior during partitions. But a social media feed can tolerate AP. Where does a ride-sharing app's dispatch system fall? What about a collaborative document editor?
3. The CALM theorem says monotone programs can be evaluated without coordination. Can you think of a non-trivial application that is naturally monotone? What properties make it so?

### Practice Problems

- Given a system with 5 replicas, a quorum of 3, and a network partition that isolates 2 replicas: which operations can succeed under (a) CP semantics, (b) AP semantics? What data is at risk in each case?
- Design a PACELC profile for a real-time multiplayer game server that must show all players the same game state (consistency) but must not drop any player's inputs (availability). What are the trade-offs during a partition?
- Implement a simple key-value store that supports two modes: (1) strong consistency using a leader and (2) eventual consistency with client-side session guarantees. Measure the latency difference for 10,000 writes.

---

ᛏ **Lecture 7: CRDTs — Conflict-Free Replicated Data Types**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Conflict-Free Replicated Data Types (CRDTs) are one of the most important innovations in distributed systems since Paxos. They offer a way to achieve eventual consistency *automatically* — without application-level conflict resolution, without coordination, and without distributed consensus. A CRDT is a data structure whose operations commute: applying them in any order yields the same result. This lecture covers the theoretical foundations of CRDTs, the two main families (state-based and operation-based), practical CRDTs (counters, sets, registers, sequences), and the systems that use them in production.

### Key Topics

- **Commutativity and State Convergence**: Why commutativity guarantees convergence
- **State-Based CRDTs (CvRDTs)**: Join-semilattices, monotonic merge functions
- **Operation-Based CRDTs (CmRDTs)**: Commutative operations, delivery ordering requirements
- **Delta-State CRDTs**: Compressing state-based CRDTs by sending only deltas
- **Practical CRDTs**: G-Counter, PN-Counter, G-Set, OR-Set, LWW-Register, RGA, LSEQ
- **CRDTs in Production**: Riak, Automerge, Yjs, and BifrostDB

### Lecture Notes

The fundamental insight behind CRDTs is that *if operations commute, order doesn't matter*. If you and I both increment a counter, the result is the same regardless of which increment happens first. This is trivially true for a counter: `increment(x) ∘ increment(y) = increment(y) ∘ increment(x)`. But it's not true for many common operations: appending to a list is not commutative (append(A) ∘ append(B) ≠ append(B) ∘ append(A) — the list will be [A,B] or [B,A] depending on order).

**State-based CRDTs (CvRDTs — Convergent Replicated Data Types)** work by ensuring that the state itself forms a mathematical structure called a *join-semilattice*: a set with a least-upper-bound (join) operation ⊔ that is commutative, associative, and idempotent. Each replica maintains its own state and periodically broadcasts its state to other replicas. When a replica receives another replica's state, it merges by computing the join: `new_state = local_state ⊔ received_state`. Because ⊔ is commutative, associative, and idempotent, the order and frequency of merges doesn't matter — all replicas will eventually converge to the same state.

The **G-Counter** (grow-only counter) is the simplest CvRDT. Each replica i maintains a vector of counts [c₁, c₂, ..., cₙ] where cᵢ is replica i's own count. To increment, a replica adds 1 to its own entry. To merge, take the element-wise maximum of both vectors. The global count is the sum of all entries. Because we only increment (never decrement), the element-wise maximum is well-defined and idempotent.

The **PN-Counter** extends the G-Counter to support decrements by pairing two G-Counters: one for increments (P) and one for decrements (N). The counter's value is `sum(P) - sum(N)`. This works but doubles the state size.

**Operation-based CRDTs (CmRDTs — Commutative Replicated Data Types)** take a different approach: instead of merging states, they broadcast operations. An operation-based CRDT requires that all operations *commute*: for any two operations `op₁` and `op₂`, `apply(state, op₁, op₂) = apply(state, op₂, op₁)`. Additionally, CmRDTs require that operations be delivered to all replicas in causal order (or at least that concurrent operations commute).

The advantage of CmRDTs is that they can transmit only the operation (small payload) rather than the entire state. The disadvantage is the stronger delivery requirement: all operations must be delivered to all replicas, and for some CmRDTs, in causal order.

**Delta-state CRDTs** (Almeida et al., 2018) offer the best of both worlds: the conceptual simplicity of state-based CRDTs with the bandwidth efficiency of operation-based CRDTs. Instead of sending the entire state, a replica sends only the *delta* — the part of the state that changed since the last merge. This reduces bandwidth by orders of magnitude for large CRDTs.

**The OR-Set (Observed-Remove Set)** is the most widely used CRDT for sets. It supports add and remove operations, and its key property is that add operations observed by a replica take precedence over concurrent remove operations. This means: if replica A adds element x, and replica B concurrently removes x, then A will see x still in the set (because A observed its own add), but B will not (because B's remove happened after it observed x). After merging, x will be in the set (the add wins). OR-Sets are the foundation of collaborative editing systems where characters can be both added and deleted.

**Sequence CRDTs** (RGA, LSEQ, YATA) are among the most complex CRDTs. They solve the problem of concurrent edits to a shared text document — insertions and deletions at arbitrary positions, with positions defined relative to other elements rather than absolute indices. Without CRDTs, two users inserting characters at the same position would create conflicting orderings. With a sequence CRDT, the merge function resolves these conflicts deterministically using unique identifiers for each character and a total order on identifiers.

In 2040, CRDTs power an enormous range of applications:

- **Collaborative editing**: Yjs (used in popular web editors), Automerge (local-first data sync), and the BifrostDB CRDT engine.
- **Mobile applications**: Offline-first apps that sync when connectivity returns, using CRDTs to merge local and remote changes automatically.
- **Distributed databases**: Riak's CRDT counters and sets, Redis CRDT (active-active replication), and Cassandra's lightweight transactions built on CRDT foundations.
- **Gaming**: Real-time multiplayer game state (position, inventory) using delta-CRDTs for bandwidth-efficient synchronization.
- **Edge computing**: Sensor networks that aggregate data using G-Counters and PN-Counters without central coordination.

The University of Yggdrasil's **BifrostDB** uses a novel delta-CRDT engine that achieves both strong eventual consistency and causal consistency guarantees, using a technique called *causal stabilization* (developed in our own Bifrost Lab in 2037). Causal stabilization identifies operations whose effects are visible to all replicas and "freezes" them, converting their metadata from CRDT-specific encoding into plain data. This reduces the metadata overhead that traditionally plagued CRDTs in long-running systems.

### Required Reading

- Shapiro, M., et al. (2011). "Conflict-Free Replicated Data Types." *SSS*.
- Almeida, P.S., et al. (2018). "Delta-State Replicated Data Types." *ICDCS*.
- Kleppmann, M., Beres, S., et al. (2019). "A Conflict-Free Replicated JSON Datatype." *IEEE TPDS*.

### Discussion Questions

1. The OR-Set resolves conflicts by favoring adds over concurrent removes. What happens if a user adds an element to a set and then immediately removes it — can the element "come back from the dead" on another replica that didn't see the remove? How would you fix this?
2. CRDTs guarantee eventual convergence, but the time to convergence depends on the network. In a system where replicas are separated by minutes of latency (e.g., Mars-Earth), what is the user experience like during convergence? Are CRDTs always the right choice?
3. Delta-CRDTs reduce bandwidth, but they add implementation complexity. At what replication factor and state size does the bandwidth savings of delta-CRDTs justify the engineering cost?

### Practice Problems

- Implement a G-Counter and PN-Counter in Python. Verify that merging two divergent G-Counters produces the correct count, and that PN-Counters handle concurrent increments and decrements correctly.
- Implement an LWW-Register (Last-Writer-Wins Register) that uses hybrid logical clocks for timestamps. Measure the convergence time with 3 replicas and random network delays of 0-500ms.
- Design a CRDT for a shared shopping cart. The cart must support add_item, remove_item, and update_quantity operations, and must converge when multiple users edit the cart concurrently. What type of CRDT do you choose, and why?

---

ᛞ **Lecture 8: Distributed Systems in 2040 — From Datacenters to the Stars**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

The final lecture surveys the cutting edge of distributed systems as they exist in 2040. We examine the systems that have moved beyond the textbook: quantum-distributed protocols, interplanetary data synchronization, AGI-driven fault management, and the convergence of edge computing and cloud into a single adaptive fabric. This lecture connects everything we've studied — clocks, consensus, replication, CRDTs, CAP — and shows how these fundamentals compose into the systems that run the world.

### Key Topics

- **Replicated State Machines and Linearizable Systems**: How Raft and Multi-Paxos power everything from Kubernetes to financial exchanges
- **Distributed Transactions**: Two-phase commit, three-phase commit, and the Saga pattern
- **Sharding and Data Placement**: Consistent hashing, virtual nodes, range-based partitioning
- **Edge-Cloud Continuum**: Moving computation to the edge while maintaining consistency with the cloud
- **Quantum-Distributed Protocols**: Quantum key distribution for Byzantine agreement, entanglement-assisted clock sync
- **Interplanetary Distributed Systems**: Mars-Earth data synchronization with 4-44 minute round trips
- **AGI-Driven Fault Management**: Self-healing distributed systems that predict and prevent failures
- **Ephemeral Distributed Systems**: Pop-up clusters for events, disaster response, and military operations

### Lecture Notes

**Replicated state machines** (RSMs) are the architectural pattern that ties together consensus, replication, and log-based systems. The idea is deceptively simple: if all replicas start in the same state and execute the same commands in the same order, they will all end up in the same state. The consensus algorithm (Raft, Multi-Paxos) is the mechanism for agreeing on the command order; the state machine is the deterministic computation that applies each command. Every system from etcd (the backbone of Kubernetes) to TiDB (a distributed SQL database) to CockroachDB (a strongly consistent distributed database) is a replicated state machine at its core.

**Distributed transactions** extend the single-machine ACID guarantee across multiple machines. The classic algorithm is Two-Phase Commit (2PC): a coordinator asks all participants to prepare (phase 1), and if all agree, the coordinator commits (phase 2). 2PC is a blocking protocol — if the coordinator crashes after phase 1 but before phase 2, participants are blocked indefinitely holding locks. Three-Phase Commit (3PC) adds a pre-commit phase to address this, but it assumes a synchronous network (which violates our foundational assumptions as discussed in Lecture 2).

The **Saga pattern** (Garcia-Molina and Salem, 1987) avoids distributed transactions entirely by decomposing a long-running transaction into a sequence of local transactions, each with a compensating action (undo). If any step fails, the Saga executes compensating actions for all completed steps in reverse order. Sagas sacrifice isolation (intermediate states are visible) but achieve availability and scalability. In 2040, Sagas are the standard pattern for microservice architectures — most payment processing, order fulfillment, and event-sourcing systems use Saga-based patterns.

**Sharding** distributes data across multiple machines based on a partitioning key. Consistent hashing (Karger et al., 1997) is the standard approach: hash each key to a point on a circle, and assign each point to the nearest node. When a node joins or leaves, only its keys need to be reassigned, minimizing data movement. Dynamo, Cassandra, and Riak all use consistent hashing with virtual nodes (vnodes) for load balancing. Range-based partitioning (used by Spanner, CockroachDB, and TiDB) assigns ordered key ranges to nodes, enabling efficient range scans but complicating rebalancing.

**The Edge-Cloud Continuum** is the defining architecture of 2040. In the 2020s, the "cloud" was a separate tier from the "edge." In 2040, the distinction has blurred into a continuum: computation moves fluidly between edge devices (phones, cars, implants), local clusters (neighborhood micro-datacenters), regional datacenters, and global cloud backbone. The University of Yggdrasil's own computation follows this continuum — student workspaces run on local nodes within 10ms, research jobs run on the Bifrost backbone within 50ms, and global services span the network.

The key challenge of the edge-cloud continuum is maintaining consistency across tiers with radically different latency and availability profiles. A neural implant making real-time decisions cannot wait 400ms for a cross-continental consensus round. The 2040 solution is a **consistency gradient**: local operations are causally consistent (using CRDTs), regional operations are sequentially consistent (using Raft), and global operations are linearizable (using Multi-Paxos with TrueTime). The BifrostDB query planner automatically routes queries to the appropriate consistency tier based on the application's declared requirements.

**Quantum-distributed protocols** represent the most speculative yet promising frontier. Quantum Key Distribution (QKD) already provides information-theoretically secure key exchange using the laws of quantum mechanics — any eavesdropper perturbs the quantum state, revealing their presence. The University of Yggdrasil's Quantum Networking Lab has demonstrated QKD across the Bifrost Research Network's Reykjavik-Oslo link (1,400 km of fiber augmented by quantum repeaters installed in 2037).

More ambitious is **quantum-assisted Byzantine agreement**. In classical BFT protocols, reaching agreement among n nodes with f Byzantine failures requires O(n²) messages and at least 2f+1 rounds. Quantum entanglement theoretically allows two nodes to share correlated random bits (a "quantum coin") that no adversary can bias. This reduces Byzantine agreement to O(n) messages — a quadratic improvement. As of 2040, this has been demonstrated in the lab but not yet deployed in production systems.

**Interplanetary distributed systems** are no longer science fiction. The Mars colony (established 2038) maintains data synchronization with Earth using a combination of CRDTs for local-first data and eventual-consistency protocols with 4-44 minute round-trip delays. The Interplanetary File System (IPFS) and its successors (InterPlanetary Data Sync, or IPDS) provide the storage layer, while a modified Raft protocol called **Bifrost-Mars** handles consensus with explicitly bounded delay windows. Key insight: in an interplanetary setting, "availability" means "available from the current planet" — you don't expect real-time consensus across planetary distances, but you do expect local consistency and eventual convergence.

**AGI-driven fault management** emerged in the late 2030s as inference-grade language models became cheap enough to run continuously alongside production systems. These systems monitor logs, metrics, and traces in real time, predict failures before they cascade, and automatically trigger recovery actions (restarting services, shifting traffic, scaling replicas). The Bifrost Network's fault management system, called **Heimdall** (after the watchman of the Norse gods), was one of the first production deployments in 2038. Heimdall reduced mean time to detection (MTTD) from 15 minutes to 30 seconds and mean time to recovery (MTTR) from 45 minutes to 3 minutes across the UoY infrastructure.

**Ephemeral distributed systems** are clusters that form for a specific purpose (a conference, a disaster response operation, a military deployment) and dissolve when the purpose is complete. These systems must bootstrap from scratch: discover peers, establish trust, distribute state, and begin operation — all within minutes. The Bifrost Protocol Suite includes a **Greeting Ceremony** (based on the Norse concept of heilsa, the ritual of welcoming a stranger) that allows new nodes to authenticate, exchange capabilities, and join a CRDT mesh in under 10 seconds.

### The View from 2040

Looking back over the semester, we've traced the arc from impossibility results (FLP, CAP) to practical systems that work despite those results. The key insight is that distributed systems engineering is not about finding perfect solutions — it's about making principled trade-offs with full knowledge of the impossibility landscape. Every system you build will be imperfect in some dimension; the art lies in choosing which imperfections are acceptable for your use case.

The systems we've studied — consensus protocols for agreement, CRDTs for coordination-free convergence, consistency models for reasoning about data visibility, and the modern edge-cloud continuum for deploying applications across the planet — are not isolated topics. They compose. A modern distributed database uses Raft for coordination, CRDTs for client-side conflict resolution, PACELC reasoning for configuration, and Sagas for multi-service transactions, all running on a sharded, replicated, edge-cloud architecture with AGI-driven fault management watching over everything.

This is the world you'll build in. The Norns — Urd, Verdandi, and Skuld — represent past, present, and future. In distributed systems, the past is the causal history your system has already committed, the present is the partial state you can observe right now, and the future is the set of consistent states your system might reach. You cannot change the past, you cannot fully observe the present, and you must design for the future. Welcome to the craft.

### Required Reading

- Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly. (Entire book — you've seen the key chapters; now read it cover to cover.)
- Howard, H., et al. (2015). "Flexible Paxos: Quorum Intersection Revisited." *OPODIS*.
- UoY Bifrost Lab (2038). "BifrostDB: A Consistency-Gradient Distributed Database." *Proceedings of the Conference on Innovative Data Systems Research (CIDR)*.

### Discussion Questions

1. AGI-driven fault management systems like Heimdall can predict failures before they cascade. Is there a risk of over-trusting AI in safety-critical distributed systems? What formal guarantees should such systems provide?
2. The consistency gradient (causal for edge, sequential for regional, linearizable for global) is a principled design, but it requires application developers to correctly declare their consistency requirements. What are the failure modes of incorrect declarations?
3. In an interplanetary system, eventual consistency with 4-44 minute delays means the "eventual" in eventual consistency could be hours. How do you design user interfaces that honestly represent this delay? What are the social implications?

### Practice Problems

- Design a Saga for a food delivery system: Order → Assign Driver → Prepare Food → Deliver → Payment. Define compensating actions for each step. What happens if the driver assignment succeeds but food preparation fails? What happens if preparation succeeds but no driver is available?
- Implement a simple consistent hashing ring in Python with 100 vnodes and 5 physical nodes. Add a 6th node and measure how many keys are remapped. Remove a node and verify that only the removed node's keys are remapped.
- Write a 500-word essay proposing a new distributed systems primitive that doesn't exist yet but should, based on the needs of 2040's edge-cloud-quantum continuum. Justify its necessity and sketch an algorithm.

---

*End of Course Material — CS301: Distributed Systems*

*Woven by Runa Gridweaver Freyjasdóttir at the University of Yggdrasil, 2040*

*May the threads of Yggdrasil's network hold fast across worlds.*