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
- Garcia-Molina, H. & Salem, K. (1987). "Sagas." *SIGMOD*.
- Kleppmann, M. (2017). *Designing Data-Intensive Applications*, Chapter 7.

### Discussion Questions

1. A payment system transfers money between two banks. Should you use 2PC, a saga, or some other mechanism? What are the consequences of partial failure?
2. Sagas provide only eventual consistency. What invariants might be temporarily violated during a travel booking saga?
3. Is there a use case where 2PC is still the best choice? What properties make 2PC appropriate?

### Practice Problems

1. **2PC failure scenario**: In a 2PC protocol with coordinator C and participants P1, P2, P3 — P1 and P2 vote VOTE_COMMIT, P3 crashes before voting, C sends COMMIT to P1 and P2. P3 recovers. What is P3's state? How does P3 determine the outcome?
2. **Saga design**: Design a saga for an e-commerce order: T1 (Reserve inventory → C1: Release inventory), T2 (Process payment → C2: Refund payment), T3 (Create shipment → C3: Cancel shipment), T4 (Send confirmation → C4: Send cancellation). If T3 fails, write out the compensations in order.
3. **3PC race condition**: In 3PC, what happens if the coordinator crashes after sending PRE-COMMIT to P1 but before sending to P2 and P3? Sketch a termination protocol.

---

ᛉ **Lecture 9: Distributed Storage — Replication, Sharding, and Planetary-Scale Databases**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Data must live somewhere, and in a distributed system, that "somewhere" is many places at once. This lecture covers the fundamental architectures for storing data at planetary scale: replication (creating copies), sharding (partitioning the key space), and the hybrid approaches that combine both.

### Replication Strategies

**Single-Leader Replication**: One replica is the leader (primary/master). All writes go through the leader, which propagates them to followers. Reads can be served from any replica. Simple conflict resolution but leader is a SPOF and bottleneck. Systems: PostgreSQL streaming replication, MySQL Group Replication, Google Spanner.

**Multi-Leader Replication**: Multiple replicas accept writes concurrently. Each leader propagates writes to all others. Conflicts must be resolved (last-writer-wins, custom resolution, CRDTs). Advantages: write availability during partitions, geographic locality. Disadvantages: complex conflict resolution, divergence risk. Systems: CouchDB, BDR for PostgreSQL, Firebase Realtime Database.

**Leaderless Replication**: Any replica can accept writes. Writes go to a quorum; reads from a quorum. Conflicts detected via version vectors/timestamps. Advantages: no SPOF, maximum write availability. Systems: DynamoDB, Cassandra, Riak KV.

**Quorum-Based Replication**: For N replicas, write succeeds if W acknowledge, read succeeds if R respond. Key constraints: W+R > N (every read sees latest write), W > N/2 (prevents split-brain writes), R > N/2 (every read sees up-to-date replica).

Typical configurations:
- Strict: N=3, W=3, R=2
- Balanced: N=3, W=2, R=2 (tolerates one failure)
- Fast writes: N=3, W=1, R=3
- Fast reads: N=3, W=3, R=1

### Sharding (Partitioning)

**Hash-Based Sharding**: Hash each key with a consistent hash function. Uniform distribution prevents hotspots. Problem: adding/removing shards requires rehashing. Solution: consistent hashing (Karger et al., 1997).

**Range-Based Sharding**: Keys partitioned by range. Range queries efficient. Problem: sequential keys create hotspots. Solution: dynamic range splitting.

**Directory-Based Sharding**: Lookup service maps keys to shards. Flexible but directory service is SPOF. Solution: replicate and cache directory.

**Shard Rebalancing**: Modern systems use range splitting with automatic rebalancing (CockroachDB, TiKV) or virtual node hashing (Cassandra, DynamoDB).

### Case Studies

**Google Spanner**: Globally distributed, externally consistent. TrueTime for commit timestamps. SQL with ACID transactions across shards. Processes billions of dollars in ad transactions daily.

**CockroachDB**: Open-source, Spanner-inspired. Hybrid Logical Clocks instead of TrueTime. Range-based sharding with Raft replication per range. Geo-partitioning for regulatory compliance.

**Apache Cassandra**: Leaderless, eventually consistent, wide-column store. Consistent hashing, tunable consistency per query (ONE, QUORUM, ALL). Multi-datacenter replication. Anti-entropy with Merkle trees.

**TiDB / TiKV**: NewSQL with split architecture: TiDB (SQL) + TiKV (KV storage) + PD (placement driver). Raft-based replication per range. Hybrid OLTP/OLAP workloads.

### Storage Engine Fundamentals

**B-Tree (read-optimized)**: PostgreSQL, MySQL (InnoDB), SQLite. O(log N) reads, page splits on writes.

**LSM-Tree (write-optimized)**: Cassandra, RocksDB, CockroachDB (Pebble). O(1) writes (append-only), amortized O(log N) reads with compaction. Good for write-heavy workloads.

### Required Reading

- Kleppmann, M. (2017). *Designing Data-Intensive Applications*, Chapters 5, 6, 9.
- Corbett, J. C. et al. (2013). "Spanner: Google's Globally Distributed Database."
- Lakshman, A. & Malik, P. (2010). "Cassandra: A Decentralized Structured Storage System."

### Discussion Questions

1. Design sharding/replication for a global social media platform complying with GDPR, CCPA, and 40+ data sovereignty laws.
2. Compare Spanner's TrueTime external consistency with CockroachDB's HLC serializability. Practical differences?
3. How to balance LSM-tree write performance with read-heavy requirements in a real-time analytics dashboard?

### Practice Problems

1. **Quorum calculation**: N=5, W=3, R=3. Maximum replica failures for: (a) read consistency, (b) write availability, (c) both.
2. **Consistent hashing**: 4 nodes (A: 0-63, B: 64-127, C: 128-191, D: 192-255). Key K hashes to 87. Which node? If E is added covering 64-95, which keys move from B to E?
3. **Shard sizing**: 100 TB, 4 TB/node, replication factor 3. How many nodes? If max shard 256 GB, how many shards and shard-replicas total?

---

ᛉ **Lecture 10: Fault Tolerance and Self-Healing — When Systems Recover Themselves**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

A distributed system that cannot tolerate faults is not a distributed system — it is a single machine with extra steps. Fault tolerance is not just about surviving crashes; it's about **detecting** failures, **reconfiguring** the system, **recovering** data, and **preventing** future failures.

### Failure Detection

**The Fundamental Problem**: In an asynchronous system, you cannot distinguish a crashed process from a slow one.

**Heartbeat-based Detection**: Periodic "I'm alive" messages. Shorter timeouts = faster detection but more false positives.

**Phi Accrual Failure Detector** (Hayashibara et al., 2004): Outputs suspicion level φ that increases over time. Applications set their own φ_threshold. Used in Cassandra, ZooKeeper.

**Chandra-Toueg Failure Detector Classes**:
- □P (Perfect): Never mistakes. Possible only in synchronous systems.
- ◇S (Eventually Strong): Eventually every crashed process permanently suspected, some correct process never suspected. Sufficient for consensus with majority correct.
- ◇W (Eventually Weak): Eventually every crashed process permanently suspected.

### Leader Election

**Bully Algorithm**: Highest-ID process becomes leader. Simple but causes leadership vacillation when higher-ID processes oscillate.

**Raft Leader Election**: Randomized election timeouts (150-300ms). Follower becomes candidate after timeout, increments term, votes for self, sends RequestVote RPCs. Majority votes = leader.

### Crash Recovery and Log Management

**Write-Ahead Logging (WAL)**: Every state change written to durable log before application. On recovery, replay log from last checkpoint.

**Raft Log Compaction**: Snapshot mechanism — state machine takes snapshot, all log entries up to snapshot are discarded. Snapshots can be sent to slow followers.

**Production Examples**: etcd snapshots every 10,000 transactions. CockroachDB uses incremental snapshots per range. Kafka uses log segmentation and compaction.

### Self-Healing Systems

**Automatic Replication Repair**: When a node fails, re-replicate its data elsewhere. Standard in Cassandra, Raft, DynamoDB.

**Anti-Entropy Protocols**:
- Merkle tree comparison for efficient replica diffing
- Read repair for synchronous inconsistency fixes
- Hinted handoff for unavailable replica buffering

**Circuit Breakers**: When downstream service fails repeatedly, breaker "opens" and stops sending requests. After timeout, allows probe request. Prevents cascade failures.

**Chaos Engineering**: Netflix's Chaos Monkey (2011) randomly terminates VMs. By 2040, chaos engineering is standard practice. Systems are designed to be tested by failure.

### AI-Assisted Fault Management (2040)

1. **Predictive failure detection**: ML models predict node failures 5-30 minutes ahead.
2. **Anomaly detection**: Unsupervised learning identifies latent failures invisible to thresholds.
3. **Automated root cause analysis**: AI traces causal chains through distributed traces.
4. **Dynamic reconfiguration**: AI adjusts replication factors, shard boundaries, and consistency levels in real-time.

**Caution**: AI mispredictions cause unnecessary re-replication or suppress genuine alerts. Human-in-the-loop escalation is essential.

### Required Reading

- Chandra, T. D. & Toueg, S. (1996). "Unreliable Failure Detectors for Reliable Distributed Systems."
- Ongaro, D. & Ousterhout, J. (2014). "In Search of an Understandable Consensus Algorithm." (Log compaction and membership changes sections.)

### Discussion Questions

1. In a 5-node Raft cluster, node 3 is partitioned. Can it win an election?
2. Case for and against chaos engineering in medical device control systems.
3. AI failure predictor with 95% accuracy (5% FP, 5% FN). Should it trigger immediate re-replication? Costs of each type of error?

### Practice Problems

1. **Phi failure detector**: Heartbeats at 100, 105, 98, 110, 95, 450ms. Last heartbeat 300ms ago. μ=100ms, σ=50ms. Calculate φ. Suspect at threshold 1?
2. **Leader election timing**: 7-node Raft cluster, election timeout 150-300ms uniform. Probability of simultaneous elections? Probability of resolution within one round?
3. **Log recovery**: Raft log [1,2,3,4,5,6,7,8], snapshot at index 5. Which entries can be discarded? After leader crash at entry 7, what does the new leader need?

---

ᛉ **Lecture 11: Security in Distributed Systems — Trust, Identity, and Byzantine Resilience**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Security in distributed systems is fundamentally different from single-machine security. Every message crosses a trust boundary, every node may be compromised, and communication itself creates vulnerability.

### Authentication

**Symmetric Key**: Shared secret K between parties. N(N-1)/2 keys needed for N parties. Solution: KDC (Kerberos).

**Kerberos** (1988): Alice contacts KDC for ticket to Bob. KDC generates session key K_AB encrypted with both Alice's and Bob's keys. Alice sends Bob the ticket. Bob decrypts, verifies identity, uses K_AB for session.

**Public Key**: Each party has public/private key pair. Alice signs challenge with private key; Bob verifies with public key. Problem: how do you know the public key belongs to Alice?

**PKI (Public Key Infrastructure)**: CAs vouch for identity-key bindings. Risk: compromised CA = all certificates untrustworthy. 2011 DigiNotar breach demonstrated this.

**2040 Improvement**: Certificate Transparency logs make all certificates publicly auditable. Merkle-based transparency prevents silent mis-issuance.

### Secure Communication

**TLS 1.3** (2018, still dominant): ECDHE key exchange → server certificate authentication → 1-RTT handshake (0-RTT for resumed sessions) → AES-256-GCM or ChaCha20-Poly1305 encryption with AEAD integrity.

**Post-Quantum TLS**: By 2040, quantum computers threaten classical public-key crypto. NIST standardized:
- **CRYSTALS-Kyber (ML-KEM)**: Lattice-based key exchange
- **CRYSTALS-Dilithium (ML-DSA)**: Lattice-based digital signatures

TLS 1.4 (proposed 2038) uses hybrid key exchange: classical (X25519) + post-quantum (ML-KEM-768) in parallel. Attacker must break both.

### Authorization

- **DAC**: Owner controls access (Unix permissions)
- **MAC**: Central authority defines policies (SELinux)
- **RBAC**: Users assigned roles with permissions (enterprise standard)
- **ABAC**: Access based on subject, resource, and environment attributes (flexible but complex)

**OAuth 2.0 / OpenID Connect**: Delegated authorization and identity. JWTs for stateless auth in microservices. Short expiration or revocation lists to mitigate JWT statelessness.

### Byzantine Fault Tolerance (Security Perspective)

Byzantine tolerance is about **malicious adversaries**, not just buggy software. Cost: O(n²) messages per consensus round, f+1 rounds for f Byzantine nodes, key management overhead.

**2040 BFT Practice**:
- **Blockchain validators** stake cryptocurrency as financial disincentive against Byzantine behavior
- **Confidential computing** (Intel SGX, AMD SEV, ARM CCA) provides hardware attestations that code is unmodified
- **Formal verification** eliminates classes of Byzantine behavior by proving implementation matches specification

### Zero-Knowledge Proofs

Prove a statement is true without revealing any information beyond its truth. Properties: completeness, soundness, zero-knowledge.

**Applications**:
- **Private transactions**: Zcash zk-SNARKs prove transaction validity without revealing sender/receiver/amount
- **Confidential smart contracts**: Aztec Protocol, zkSync
- **Authentication without disclosure**: Prove set membership without revealing which member
- **Verifiable computation**: Prove computation correctness without re-executing (rollups)

**zk-SNARKs vs zk-STARKs**: SNARKs have short proofs (288 bytes) and fast verification but require trusted setup. STARKs have larger proofs (200KB+) but no trusted setup and are quantum-resistant.

### 2040 Security

**Decentralized Identity (DID)**: Users control identity data in verifiable credentials. Blockchain provides root of trust.

**Service Mesh Security**: Mutual TLS (mTLS) between all services. Automatic certificate rotation. Authorization policies enforced at mesh level.

**Zero Trust Architecture**: "Never trust, always verify." Every request authenticated and authorized regardless of origin. Default for new deployments by 2040.

### Required Reading

- Lamport, L., Shostak, R., & Pease, M. (1982). "The Byzantine Generals Problem."
- Ben-Sasson, E. et al. (2018). "Scalable, Transparent, and Post-Quantum Secure Computational Integrity."
- Rescorla, E. (2018). "TLS 1.3." RFC 8446.

### Discussion Questions

1. Transition plan for global PKI from RSA to post-quantum? Risks of premature or delayed transition?
2. Should all financial transactions be private by default? Societal implications?
3. 100-service microservices architecture with TLS certificates. How to manage rotation without downtime?

### Practice Problems

1. **Kerberos scenario**: List all protocol steps including keys and encrypted messages.
2. **Zero-knowledge proof**: Describe Schnorr protocol (commitment, challenge, response) for proving knowledge of discrete logarithm without revealing it.
3. **Byzantine resilience cost**: 100-node BFT system, 3 rounds/transaction, 1ms processing/message. Maximum throughput? Throughput with 10 Byzantine nodes?

---

ᛉ **Lecture 12: The Future — Quantum Networks, AI-Managed Consensus, and the Physics-Computation Convergence**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

The three forces shaping the future of distributed systems:
1. **Quantum networks** providing provable security through physics
2. **AI-managed consensus** adapting protocols in real-time
3. **Physics-computation convergence** blurring boundaries between systems and environment

### Quantum Networking

**Quantum Key Distribution (QKD)**: BB84 protocol uses polarized photons. Any eavesdropper disturbs quantum state, alerting communicators. Provable security — not computationally hard but physically impossible to intercept undetected.

**2040 State**: QKD networks operate in China (4,600 km backbone), Europe (SECOQC), and US (Chicago Quantum Exchange). Satellite QKD enables intercontinental key distribution. QKD complements rather than replaces classical crypto — keys used for symmetric AES-256, authentication via post-quantum algorithms.

**Quantum Internet beyond QKD**: Quantum teleportation of states, distributed quantum computation linking multiple quantum computers, quantum sensing networks achieving precision beyond classical limits.

**Impact**: QKD eliminates the weakest link in TLS — key exchange can't be compromised without detection. Raises security from "computationally hard to break" to "physically impossible to break without detection."

### AI-Managed Consensus

Static protocols with fixed parameters are suboptimal. **Adaptive consensus** uses ML to optimize in real-time:

- **Dynamic timeout adjustment**: AI predicts optimal timeouts based on network conditions and failure history
- **Adaptive quorum sizing**: Adjusts based on observed failure patterns and node reliability
- **Predictive reconfiguration**: Proactive re-replication and quorum adjustment before predicted failures
- **Protocol switching**: Dynamically switches between Paxos, EPaxos, and BFT based on workload

**UoY Research — Verðandi**: AI-driven consensus orchestrator that monitors metrics, predicts failures 30-120 seconds ahead, dynamically adjusts Raft parameters, switches protocols at runtime, and provides formal safety guarantees via model checking.

**Challenges**:
1. **Safety**: Misconfigured parameters can cause split-brain. Formal verification of adaptive parameters is essential.
2. **Oscillation**: Rapid protocol switching causes thrashing. Hysteresis and cooldown periods prevent this.
3. **Adversarial AI**: Attackers can influence training data to cause misconfiguration. Adversarial training and anomaly detection are necessary.

### Physics-Computation Convergence

**1. Edge Computing**: By 2040, 75%+ of data processed at edge. Consensus must run on limited devices with variable network conditions and high churn.

**2. Cyber-Physical Systems (CPS)**: Self-driving cars, smart grids, robotic surgery. Hard real-time constraints (braking can't wait 500ms for Raft). Byzantine failures have physical consequences. Formal verification is mandatory.

**3. Quantum-Enhanced Computing**: Quantum processors as coprocessors. No-cloning theorem makes replication fundamentally different. Quantum decoherence imposes strict timing. Hybrid classical-quantum algorithms require tight coordination.

### Speculative Futures

**Post-Quantum Distributed Consensus**: Lattice-based signatures (Dilithium) are 5-10x larger than ECDSA. Affects bandwidth and verification time in consensus protocols.

**Neuromorphic Distributed Computing**: Spiking neural network chips (Intel Loihi, IBM TrueNorth). Event-driven, asynchronous, inherently fault-tolerant at neuron level.

**Biological Distributed Systems**: DNA storage (1 EB/gram) with slow access. Hybrid systems using DNA for archival storage, classical for active computation.

### The Synthesis: Key Lessons

1. **Impossibility results are design constraints**, not death sentences. FLP needs partial synchrony; CAP needs consistency/availability choice during partitions.
2. **Every design decision is a trade-off**. Stronger consistency costs latency. Higher availability risks inconsistency. Simpler protocols sacrifice features.
3. **Failure is the norm**. Design for it, test for it, expect it. Chaos engineering and formal verification are necessities.
4. **The future is adaptive**. Static protocols served us well; adaptive systems that learn from failure will define the next decade.
5. **Security is a first-class citizen**. Byzantine faults are real, quantum computers are coming, AI-assisted attacks are emerging. Secure by design, not by afterthought.

### Required Reading

- Bennett, C. H. & Brassard, G. (1984). "Quantum Cryptography: Public Key Distribution and Coin Tossing."
- Castelvecchi, D. (2018). "The Quantum Internet Has Arrived (And It Hasn't)." *Nature*, 554, 289–292.
- Howard, H. et al. (2019). "Flexible Paxos: Quorum Intersection Revisited."

### Discussion Questions

1. If QKD becomes widely available, how would TLS architecture change? Would CAs still be needed?
2. What happens when conditions change faster than AI can adapt? Is there a theoretical limit to adaptive consensus?
3. What consistency model is appropriate for sharing sensor data between autonomous vehicles? Is eventual consistency fast enough for safety?

### Practice Problems

1. **QKD key rate**: System parameters η=0.15, f=1 GHz, μ=0.5. Key generation rate? Transactions per second with 256-bit keys?
2. **Adaptive consensus**: Raft cluster, 5 nodes, election timeout 300ms. AI observes mean inter-heartbeat 50ms, σ=10ms, recommends 5σ timeout. New timeout? Probability of false suspicion?
3. **CPS safety**: Vehicle platoon with 4-node BFT (f=1), 50ms consensus. At 120 km/h, minimum following distance? If 7-node BFT (f=2) takes 200ms, does increased tolerance justify increased following distance?

---

## Final Examination Preparation

### Exam Format

**Part A: Analytical Problems (60 points)** — 8 short-answer problems covering all 12 lectures.

**Part B: Design Problem (40 points)** — One comprehensive design problem requiring:
1. Consistency model choice and justification
2. Replication and sharding strategy
3. Consensus protocol specification and justification
4. Failure mode analysis and recovery procedures
5. Security and BFT considerations
6. Trade-off analysis (latency, throughput, availability, consistency)

### Sample Exam Problems

**Part A:**
1. Three processes with specified event traces. Draw happened-before graph, assign Lamport and vector timestamps, identify concurrent events.
2. 7-node system, 2 Byzantine nodes. Can it achieve consensus? Minimum n for f=2 BFT? Does authentication change the bound?
3. Trace a PN-Counter CRDT through specified operations and merges across 3 nodes.
4. 2PC with coordinator crash between phases. What is each participant's state? How do they determine outcome?
5. N=5, W=3, R=3 quorum system. Maximum failures for read consistency, write availability, both?
6. Classify consistency models for: stock trading, weather app, document editing, approximate counter.
7. Kerberos protocol trace with all keys and encrypted messages.
8. QKD key rate calculation given detector efficiency, repetition rate, and mean photon number.

**Part B Sample Design Problem:**

Design a distributed ride-sharing platform operating in 50 cities worldwide. Requirements:
- Driver locations accurate within 500ms. Ride assignments atomic.
- 99.9% availability (8.76 hours downtime/year maximum).
- Ride matching within 2 seconds. Location propagation within 500ms.
- 10M active drivers, 5M concurrent riders, 500K ride requests/minute.

Address: data model and sharding, replication and consistency per data type, consensus for ride assignment, failure detection and recovery, security (authentication, authorization, privacy), performance analysis.

### Study Guide

**Key theorems**: FLP Impossibility, CAP Theorem, BFT bound (n ≥ 3f+1), Quorum intersection (W+R > N).

**Key algorithms to trace**: Lamport clocks, vector clocks, Basic Paxos, Raft leader election and log replication, 2PC, G-Counter, PN-Counter.

**Key systems to compare**: Spanner vs. CockroachDB (TrueTime vs. HLC), DynamoDB vs. Cassandra (different consistency APIs), etcd/Raft vs. ZooKeeper/Zab.

### Course Conclusion

Distributed systems are the infrastructure of digital civilization. Every financial transaction, social media post, and autonomous vehicle decision traverses a distributed system balancing consistency, availability, and partition tolerance. The algorithms and design patterns in this course are the foundation upon which 2040's digital civilization is built.

The Norns — Urðr, Verðandi, and Skuld — weave past, present, and future into fate's tapestry. In distributed systems, the past is the log of committed operations, the present is consensus on current state, and the future is operations yet to be proposed. May your systems be safe, available, and eventually consistent — and may your logs never diverge.
