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
- **CAP in Practice**: How real systems (Cassandra, MongoDB, Spanner, CockroachDB) navig