# CS301: Distributed Systems
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4  
**Description:** CAP, consensus (Raft/Paxos), eventual consistency, CRDTs

---

## Lectures

ᛉ **Lecture 1: The Nature of Distribution — Why Distributed Systems Matter**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Distributed systems are the invisible scaffolding of modern civilization. Every bank transfer, every video stream, every autonomous vehicle decision ripples across a constellation of machines that must somehow agree on truth despite being separated by latency, failure, and the fundamental limits of physics. This course begins where single-machine computing ends — at the boundary where one processor's certainty becomes another's uncertainty, and where the mathematics of impossibility coexists with the engineering of pragmatic triumph.

By 2040, distributed systems have become the dominant paradigm for virtually all computing at scale. The "cloud" is not a place — it is a distributed system. The Internet of Things is not a buzzword — it is billions of distributed nodes making autonomous decisions. Even your personal neural implant runs distributed consensus with its cloud counterpart to maintain coherent identity across device boundaries. Understanding distributed systems is no longer a specialization; it is the operating system of reality itself.

### The Fundamental Challenge

The core problem of distributed systems is elegantly stated and profoundly difficult: **how do multiple independent entities, communicating only through unreliable messages, agree on the state of the world?**

This question intersects with:

- **Physics**: The speed of light imposes hard limits on how fast information can propagate. A message from Earth to Mars takes between 3 and 22 minutes. Even within a single datacenter, the speed-of-light round trip across a rack imposes measurable latency.
- **Failure**: Networks partition, machines crash, disks corrupt, software bugs cause silent data corruption. A distributed system must make progress despite any subset of its components failing arbitrarily.
- **Concurrency**: Multiple clients may simultaneously read and write the same data. Without careful coordination, the system can produce contradictions — the same account showing different balances to different observers.

Leslie Lamport captured the essence in his 1978 paper "Time, Clocks, and the Ordering of Events in a Distributed System": in a distributed system, events are only partially ordered. There is no global clock, no universal "now." Instead, causality creates a partial order — event A happened-before event B if A could have influenced B. Events that are causally unrelated are **concurrent**: neither happened first.

### Historical Arc

The genealogy of distributed systems traces through decades of innovation:

- **1969**: ARPANET connects four nodes. The problem of routing unreliable messages is born.
- **1978**: Lamport's paper on logical clocks establishes the formal foundation for reasoning about distributed events.
- **1982**: Lamport, Shostak, and Pease publish "The Byzantine Generals Problem," defining failures where nodes may actively deceive.
- **1985**: Fischer, Lynch, and Patterson prove the FLP impossibility result: in an asynchronous system, no deterministic algorithm can guarantee consensus if even one process may crash.
- **1989**: Lamport publishes Paxos, a consensus algorithm achieving safety under all conditions. Written as a fictional parliamentary procedure on the island of Paxos, it would not be widely understood for another decade.
- **2000**: Brewer presents the CAP theorem at PODC. Gilbert and Lynch formalize it in 2002.
- **2006**: Amazon publishes the Dynamo paper, demonstrating that carefully managed inconsistency powers massive-scale production systems.
- **2012**: Ongaro and Ousterhout publish the Raft consensus algorithm, designed for understandability.
- **2024-2040**: The convergence of edge computing, quantum networking precursors, and AI-driven fault management transforms distributed systems from human-designed protocols to adaptive ecosystems. Self-healing consensus groups, AI-predicted partition recovery, and formally verified distributed kernels define the modern landscape.

### The 2040 Context

At the University of Yggdrasil, we teach distributed systems not as a historical survey but as a living discipline. Our students will build systems that:

- **Run across planetary distances** — Mars colony data synchronization requires protocols tolerating 4-44 minute round trips.
- **Coordinate autonomous agents** — Self-driving vehicles, drone swarms, and robotic construction crews are distributed systems where the "nodes" move through physical space.
- **Maintain privacy in a hostile world** — Zero-knowledge proofs and homomorphic encryption allow distributed computation without revealing secrets.
- **Survive Byzantine failures** — In a world of adversarial AI, some nodes may be actively malicious, not merely crashed.

### Key Terminology

- **Node**: An independent computing entity. May be a physical machine, virtual machine, container, or logical process.
- **Message**: The fundamental unit of communication. The only way nodes learn about each other's state.
- **Latency**: Time delay between sending and receiving a message. Includes propagation, processing, and queueing delays.
- **Consensus**: The problem of getting all non-faulty nodes to agree on a value.
- **Consistency**: The property that all nodes observe the same state (or a well-defined approximation).
- **Availability**: Every request receives a non-error response.
- **Partition tolerance**: The system continues operating despite network partitions.
- **Idempotence**: Performing an operation multiple times has the same effect as performing it once.

### Required Reading

- Lamport, L. (1978). "Time, Clocks, and the Ordering of Events in a Distributed System." *CACM*, 21(7), 558–565.
- Coulouris, G. et al. (2012). *Distributed Systems: Concepts and Design* (5th ed.). Addison-Wesley.
- Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly. Chapters 5 and 7.

### Discussion Questions

1. A Mars-Earth distributed system has 4-22 minute one-way latency. Can such a system achieve strong consistency? Under what conditions?
2. FLP impossibility seems to doom all consensus algorithms. Yet production systems achieve consensus daily. How is this paradox resolved?
3. Is a web browser interacting with a web server a "distributed system"? Where do we draw the boundary?

### Practice Problems

1. **Event ordering**: Given events across processes P1, P2, P3, identify which are concurrent and which are causally related using Lamport's happened-before relation.
2. **Latency calculation**: Three datacenters: NY↔London ≈ 28ms, NY↔Tokyo ≈ 78ms, London↔Tokyo ≈ 92ms. What is the minimum round-trip time for a three-phase commit?
3. **Failure classification**: Classify each behavior (crash, omission, timing, Byzantine): a server that stops responding; a router dropping every third packet; a process responding 500ms late; a compromised node sending contradictory values.

---

ᛉ **Lecture 2: Time, Clocks, and Causality — The Architecture of Ordering**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Lamport Clocks: Logical Ordering

Lamport's 1978 paper introduced one of the most elegant ideas in computer science: a **logical clock** capturing causal ordering without synchronized physical clocks.

**Algorithm:**
1. Each process Pi maintains a counter Ci, initialized to 0.
2. Before executing an event, Pi increments Ci := Ci + 1.
3. When Pi sends message m, it includes timestamp Ci.
4. When Pj receives message m with timestamp Ct, Cj := max(Cj, Ct) + 1.

This guarantees: **if event A happened-before event B, then C(A) < C(B).** The converse does NOT hold — two concurrent events may happen to have ordered timestamps.

### Vector Clocks: Detecting Concurrency

A vector clock VC is an array [C1, C2, ..., Cn] where Ci represents Pi's knowledge of its event count. Comparison rules:
- VC(A) < VC(B) iff ∀i: VC(A)[i] ≤ VC(B)[i] AND ∃j: VC(A)[j] < VC(B)[j]
- VC(A) || VC(B) (concurrent) iff neither VC(A) ≤ VC(B) nor VC(B) ≤ VC(A)

Used in Amazon DynamoDB (as dotted version vectors) for conflict detection. When two versions have concurrent vector clocks, both updates happened independently, requiring conflict resolution.

### Hybrid Logical Clocks (HLCs)

Physical clocks are imprecise but meaningful; logical clocks are precise but meaningless outside the system. **Hybrid Logical Clocks** combine both: hybrid time = (physical timestamp, logical counter). Used in CockroachDB and YugabyteDB for SQL-compliant transaction ordering without GPS-atomic clocks.

### Wall-Clock Synchronization

- **NTP**: ~1-10ms accuracy on LANs, ~10-100ms on WANs.
- **PTP (IEEE 1588)**: Sub-microsecond accuracy on LANs.
- **GPS-disciplined clocks**: Microsecond-level accuracy in datacenters.
- **TrueTime (Google Spanner)**: Returns interval [earliest, latest]; real time guaranteed within this interval. External consistency without coordination.

### Required Reading

- Lamport, L. (1978). "Time, Clocks, and the Ordering of Events in a Distributed System."
- Kulkarni, S. et al. (2014). "Logical Physical Clocks and Consistent Snapshots in Distributed Systems."

### Discussion Questions

1. Spanner achieves external consistency through TrueTime intervals and "commit wait." Is this a violation of FLP, or a circumvention?
2. Vector clocks grow linearly with process count. What alternatives exist for systems with millions of clients?
3. In a collaborative text editor using CRDTs, are vector clocks needed? Why or why not?

### Practice Problems

1. **Lamport clock trace**: Calculate timestamps for events across P1, P2, P3 with specified message flow.
2. **Vector clock conflict**: Determine if two shopping cart replicas with given vector clocks are concurrent or ordered.
3. **Clock drift**: Two servers drift at 1ms/minute. NTP resynchronizes every 5 minutes with 0.5ms uncertainty. What is the maximum clock skew?

---

ᛉ **Lecture 3: Failure Models and Byzantine Agreement — When Machines Lie**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### The Failure Taxonomy

**1. Crash-stop**: Process halts permanently. Detectable via heartbeat; cannot recover.
**2. Crash-recovery**: Process halts but may restart with stable storage intact.
**3. Omission**: Process fails to send or receive messages selectively.
**4. Timing**: Process violates timing assumptions — responds too early, late, or inconsistently.
**5. Byzantine (arbitrary)**: Process may behave arbitrarily — sending contradictory messages, pretending to function, or actively colluding.

### Impossibility Results

**FLP Impossibility (1985)**: No deterministic algorithm can guarantee consensus in an asynchronous system with even one crash failure. Practical circumvention: randomization, partial synchrony, and failure detectors.

**Byzantine Bounds**: To tolerate f Byzantine nodes requires n ≥ 3f + 1 total nodes. With digital signatures, this reduces to n ≥ 2f + 1.

### Practical Byzantine Fault Tolerance

**PBFT** (Castro & Liskow, 1999): 3f+1 replicas, three-phase protocol (pre-prepare, prepare, commit). Safety under all conditions, liveness under partial synchrony. ~1ms overhead per operation locally.

**HotStuff** (2019): O(n) communication using threshold signatures. Used in Meta's Diem blockchain and most modern blockchain protocols.

**Tendermint**: BFT-style with rotating proposer. Accountable safety — if two blocks are finalized, at least 1/3 of validators signed conflicting votes. Powers 200+ production blockchains.

### 2040 Context

By 2040, Byzantine failures are real threats:
- **AI-compromised nodes**: Adversarial AI mimics correct behavior before deviating
- **Supply chain attacks**: Hardware implants cause Byzantine behavior at firmware level
- **Cloud megafailures**: Hypervisor bugs cause correlated Byzantine failures across VMs

### Required Reading

- Lamport, L., Shostak, R., & Pease, M. (1982). "The Byzantine Generals Problem."
- Fischer, M. J., Lynch, N. A., & Patterson, M. S. (1985). "Impossibility of Distributed Consensus with One Faulty Process."
- Castro, M. & Liskow, B. (1999). "Practical Byzantine Fault Tolerance."

### Discussion Questions

1. A blockchain validator signs two conflicting blocks. Under Tendermint's accountable safety, what percentage must be Byzantine for two conflicting blocks?
2. How do Paxos, Raft, and PBFT circumvent FLP impossibility?
3. A defective update pushed to 30% of nodes causes arbitrary behavior. Is this crash or Byzantine?

### Practice Problems

1. **Resilience calculation**: Minimum nodes for f=5 Byzantine tolerance? Maximum throughput given 10,000 req/s per node and 3 round-trips per request?
2. **PBFT trace**: 4-node system, node 3 Byzantine. Trace message flow showing honest nodes reaching consensus.
3. **Failure classification**: DNS returning NXDOMAIN for valid domains; load balancer routing 90% to one backend; compromised CA issuing fake certs.

---

ᛉ **Lecture 4: Consensus Protocols — Paxos, Raft, and the Art of Agreement**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### The Consensus Problem

A consensus protocol must satisfy:
1. **Safety (Agreement)**: All non-faulty nodes decide the same value.
2. **Validity**: The decided value must have been proposed by some node.
3. **Liveness (Termination)**: Every non-faulty node eventually decides.

### Paxos

Lamport's "The Part-Time Parliament" (1990, widely understood after "Paxos Made Simple" in 2001). Roles: Proposer, Acceptor, Learner.

**Basic Paxos** — Phase 1a (Prepare), Phase 1b (Promise), Phase 2a (Accept), Phase 2b (Accepted).

**Multi-Paxos**: Stable leader skips Phase 1 for subsequent proposals, reducing to single round-trip per decision.

### Raft: Understandability as a Feature

Ongaro & Ousterhout (2014) decompose consensus into:
1. **Leader Election**: Candidates seek majority votes. Terms provide logical time.
2. **Log Replication**: Leader appends entries and replicates to followers. Committed when majority have it.
3. **Safety**: Election restriction ensures only candidates with up-to-date logs can win.

**Raft's simplifications**: strong leader, separated concerns, guaranteed log consistency across servers sharing an entry at the same index.

### Modern Consensus

**EPaxos**: Removes leader bottleneck. Non-conflicting commands commit in single round trip.
**Mencius**: Rotates leader role among replicas, eliminating single-leader throughput bottleneck.
**Production Raft (2040)**: etcd, Consul, TiKV, CockroachDB metadata — proven robust across thousands of deployments.

### Required Reading

- Ongaro, D. & Ousterhout, J. (2014). "In Search of an Understandable Consensus Algorithm."
- Lamport, L. (2001). "Paxos Made Simple."

### Discussion Questions

1. What happens if Raft's election restriction (candidate must have up-to-date log) is removed?
2. In a 5-node Raft cluster partitioned 2-3, can the group of two elect a leader?
3. Paxos allows multiple proposers; Raft funnels through a single leader. What are the trade-offs?

### Practice Problems

1. **Raft election trace**: 5-node cluster with specified log states — which servers can win an election?
2. **Paxos scenario**: Trace message flow for two proposers competing across three acceptors.
3. **Throughput calculation**: 5-node Raft cluster at 50,000 ops/s. Leader fails, election takes 150ms. How many operations are lost during election?

---

ᛉ **Lecture 5: The CAP Theorem — Pick Two (But Not Really)**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### The Theorem

**CAP** (Brewer 2000; Gilbert & Lynch 2002): A distributed system cannot simultaneously provide Consistency, Availability, and Partition tolerance. Since P is mandatory, the real choice is between C and A **during a partition**.

- **CP systems**: Maintain consistency by refusing operations during partitions.
- **AP systems**: Maintain availability, serving potentially stale data during partitions.

### The Nuance: PACELC

**PACELC** (Abadi, 2012): If **P**artition, trade **A**vailability vs **C**onsistency; **E**lse (normal operation), trade **L**atency vs **C**onsistency. More useful than binary CAP.

### Consistency Patterns

- **Strong (Linearizability)**: Every read sees the most recent write. Banking, identity, inventory.
- **Causal**: Reads respect causal ordering. Social media, collaborative editing.
- **Eventual**: All replicas converge given enough time. DNS, shopping carts, caching.
- **Session**: Read-your-writes + monotonic reads within a session. User profiles, shopping cart modifications.

### 2040: Adaptive Consistency

- **Spanner**: External consistency via TrueTime.
- **CockroachDB**: Strong reads (Raft quorum) or stale reads (local replica + bounded staleness).
- **Cosmos DB**: Five tunable levels per query.
- **AI-driven adaptation**: Monitor conditions, switch between CP and AP based on partition probability and data criticality.

### Required Reading

- Gilbert, S. & Lynch, N. (2002). "Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services."
- Abadi, D. (2012). "Consistency Tradeoffs in Modern Distributed Database System Design."

### Discussion Questions

1. For a real-time multiplayer game: CP or AP? What about player positions vs. inventory?
2. For a social media platform: Which consistency model for news feed, DMs, and payments?
3. Critique: "CP systems are always better because consistency matters more than availability."

### Practice Problems

1. **CAP classification**: HBase, Cassandra, MongoDB, Spanner, Redis.
2. **Consistency window**: 3-replica AP system, 50-200ms propagation. Maximum staleness?
3. **Latency-consistency tradeoff**: Compare Mode A (quorum reads, 12ms, strong) vs Mode B (nearest replica, 2ms, eventual) for e-commerce with 10K reads/s and 100 writes/s.

---

ᛉ **Lecture 6: Consistency Models — From Linearizability to Eventual and Beyond**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### The Consistency Model Hierarchy

1. **Strict Consistency**: Global real-time order. Physically impossible without FTL.
2. **Linearizability**: Operations appear atomic between invocation and response. Requires quorum communication. Systems: Spanner, etcd, ZooKeeper.
3. **Sequential Consistency**: Global order preserving each process's program order. No real-time constraint.
4. **Causal Consistency**: Causally-related operations appear in order everywhere. Concurrent operations may appear in different orders. Systems: COPS, Bayou.
5. **PRAM Consistency**: Writes by a single process seen in order by all processes. Different processes' writes may interleave differently.
6. **Read-Your-Writes**: A process always reads its own latest write. Session-level guarantee.
7. **Monotonic Reads**: If a process reads value v, it never reads an older value. Lightweight tracking.
8. **Eventual Consistency**: All replicas converge given no new writes. No ordering guarantees during convergence. DNS, DynamoDB, Cassandra.

### Key Insight

PRAM and Read-Your-Writes are incomparable — neither subsumes the other. "Session guarantees" combine both.

### Choosing a Consistency Model

1. What invariants must the system maintain?
2. What is the cost of inconsistency?
3. What latency can we afford?
4. What is the partition probability?

### 2040 Landscape

Modern databases offer **tunable consistency** per query: Cosmos DB's five levels, CockroachDB's strong/stale reads, TiDB's session-consistent snapshots.

### Required Reading

- Viotti, P. & Vukolić, M. (2016). "Consistency in Non-Transactional Distributed Storage Systems."
- Lloyd, W. et al. (2011). "Don't Settle for Eventual: Scalable Causal Consistency with COPS."

### Discussion Questions

1. Can a banking system maintain non-negative balances under eventual consistency?
2. Which consistency model for collaborative text editing? Justify.
3. Calculate throughput difference between linearizable and stale reads across global regions.

### Practice Problems

1. Identify the strongest sufficient consistency model for: stock trading, weather app, document editing, approximate counter.
2. Which anomalies can occur under eventual consistency: phantom read, stale read, ordering violation, lost update?
3. Construct a history allowed under eventual consistency but forbidden under session consistency.

---

ᛉ **Lecture 7: Conflict-Free Replicated Data Types — Coordination-Free Convergence**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### The Core Insight

CRDTs are data structures designed so that **any order of operations produces the same result**. They make eventual consistency not just tolerable, but **provably correct**.

### Two Families

**Operation-Based CRDTs (CmRDTs)**: Operations broadcast to all replicas. Operations must be commutative. Require reliable broadcast.

**State-Based CRDTs (CvRDTs)**: Replicas exchange and merge states. Merge must be commutative, idempotent, and monotonic. Require eventual delivery.

### Key CRDT Types

- **G-Counter**: Vector of per-node counts. Merge = element-wise max. Value = sum. Grow-only.
- **PN-Counter**: Two G-Counters (increments and decrements). Value = difference. Allows increment and decrement.
- **G-Set**: Grow-only set. Merge = union. Cannot remove.
- **OR-Set (Observed-Remove)**: Elements tagged with unique IDs. Remove removes observed tags, add creates new tag. "Add wins" over concurrent add/remove.
- **LWW-Register**: Last-writer-wins register. Timestamped writes, highest timestamp wins.
- **RGA (Replicated Growable Array)**: Sequence CRDT for collaborative editing. Insertions tagged with predecessor ID and unique ID.
- **OR-Map**: Key-value map where each value is an OR-Set. Supports concurrent updates to different keys without conflict.

### Production Systems

- **DynamoDB**: Version vectors for conflict detection, CRDT-like resolution for counters and sets.
- **Riak**: First-class CRDT types (counters, sets, maps, registers).
- **Automerge** and **Yjs**: 2040-era CRDT libraries powering collaborative applications.

### Limitations

- **Space overhead**: Metadata grows with operations; requires garbage collection.
- **Non-commutative semantics**: Not all operations commute (set-to-value). Decompose into commutative primitives.
- **Garbage collection**: Periodic cleanup requires quiescence or coordination.

### Required Reading

- Shapiro, M. et al. (2011). "Conflict-Free Replicated Data Types."
- Kleppmann, M. et al. (2019). "A Conflict-Free Replicated JSON Datatype."

### Discussion Questions

1. Model a collaborative drawing app as OR-Set, RGA, or something else? Trade-offs?
2. Is eventual consistency acceptable for a stock ticker? A collaborative document? A page view counter?
3. OR-Set shopping cart: Alice adds "laptop" simultaneously with Bob removing "laptop". Final contents?

### Practice Problems

1. **G-Counter trace**: Three nodes increment; merge states; compute final value.
2. **OR-Set conflict**: Concurrent add/remove with unique tags. Determine set membership after merge.
3. **CRDT design**: Design a "last-logged-in user ID" register CRDT with merge semantics.

---

ᛉ **Lecture 8: Distributed Transactions — The Illusion of Atomicity**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Two-Phase Commit (2PC)

Classic protocol by Jim Gray. Phase 1: coordinator sends PREPARE; participants vote VOTE_COMMIT or VOTE_ABORT. Phase 2: coordinator sends COMMIT or ABORT based on votes.

**Blocking problem**: If coordinator crashes after Phase 1, participants that voted VOTE_COMMIT are locked until coordinator recovers.

### Three-Phase Commit (3PC)

Adds pre-commit phase to eliminate blocking. After Phase 2, every participant knows the outcome will be commit. Even if coordinator crashes, participants can determine the outcome. **Limitation**: Requires synchronous communication — impractical for most distributed systems.

### Paxos Commit

Gray & Lamport (2006): Use Paxos consensus among coordinator replicas to make 2PC non-blocking. Eliminates single coordinator SPOF at the cost of one Paxos instance per transaction.

### Sagas

Garcia-Molina & Salem (1987): Sequence of transactions T1...Tn, each with compensating transaction C1...Cn. If Ti fails, execute C(i-1)...C1 in reverse order. No global locks, better availability, better fit for microservices.

**2040 implementations**: Temporal.io, Camunda, AWS Step Functions.

**Trade-offs**: No isolation (intermediate states visible), compensations may be imperfect, harder debugging.

### 2040 Practice

Most production systems use:
1. Saga-based patterns for cross-service transactions
2. Calvin-style deterministic databases (FaunaDB)
3. Spanner-style external consistency (CockroachDB, TiDB, YugabyteDB)
4. CRDTs for coordination-free data (Automerge, Yjs)

### Required Reading

- Gray, J. & Lamport, L. (2006). "Consensus on Transaction Commit."
- Garcia-Molina, H. & Salem, K. (1987