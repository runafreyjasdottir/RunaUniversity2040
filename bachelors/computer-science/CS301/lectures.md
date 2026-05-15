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

This insight — that time itself is a negotiated agreement in distributed systems — shapes every algorithm, every protocol, every design decision that follows.

### Historical Arc

The genealogy of distributed systems traces back to the earliest networked computers:

- **1969**: ARPANET connects four nodes (UCLA, SRI, UCSB, Utah). The problem of routing messages across unreliable links is born.
- **1978**: Lamport's paper on logical clocks establishes the formal foundation for reasoning about distributed events.
- **1982**: Lamport, Shostak, and Pease publish "The Byzantine Generals Problem," defining the class of failures where nodes may lie — not just crash, but actively deceive.
- **1985**: Fischer, Lynch, and Patterson prove the FLP impossibility result: in an asynchronous system, no deterministic algorithm can guarantee consensus if even one process may crash. This is not a limitations of engineers; it is a theorem about the nature of the problem.
- **1989**: Lamport publishes Paxos, a consensus algorithm that achieves safety under all conditions and liveness when the system is sufficiently synchronous. Written as a fictional parliamentary procedure on the island of Paxos, it would not be widely understood for another decade.
- **1990s**: The rise of the Internet transforms distributed computing from an academic curiosity into a commercial necessity. Web servers, databases, and application layers must scale across machines.
- **2000**: Brewer presents the CAP theorem at PODC, articulating the tension between Consistency, Availability, and Partition tolerance. Gilbert and Lynch formalize it in 2002.
- **2006**: Amazon publishes the Dynamo paper, demonstrating that carefully managed inconsistency (eventual consistency) can power massive-scale production systems. CRDTs begin their ascent from theory to practice.
- **2012**: Diego Ongaro and John Ousterhout publish the Raft consensus algorithm, designed for understandability — a direct response to Paxos's notorious complexity.
- **2013-2020**: Cloud-native computing becomes the default. Kubernetes, microservices, and service meshes make distributed systems infrastructure accessible to every developer.
- **2024-2040**: The convergence of edge computing, quantum networking precursors, and AI-driven fault management transforms distributed systems from human-designed protocols to adaptive ecosystems. Self-healing consensus groups, AI-predicted partition recovery, and formally verified distributed kernels define the modern landscape.

### The 2040 Context

At the University of Yggdrasil, we teach distributed systems not as a historical survey but as a living discipline. Our students will build systems that:

- **Run across planetary distances** — The Mars colony's data synchronization with Earth requires protocols that tolerate 4-44 minute round-trip times.
- **Coordinate autonomous agents** — Self-driving vehicles, drone swarms, and robotic construction crews are distributed systems where the "nodes" move through physical space.
- **Maintain privacy in a hostile world** — Zero-knowledge proofs and homomorphic encryption allow distributed computation without revealing secrets.
- **Survive Byzantine failures** — In a world of adversarial AI, some nodes in your system may be actively malicious, not merely crashed.

### Course Structure

This course proceeds through twelve lectures that build from fundamental impossibility to practical triumph:

1. **Lecture 1** (this lecture): Why distributed systems matter — the nature of distribution, partial ordering, and the landscape of challenges.
2. **Lecture 2**: Time, clocks, and causality — logical clocks, vector clocks, and the impossibility of perfect synchrony.
3. **Lecture 3**: Failure models and Byzantine agreement — crash failures, omission failures, Byzantine failures, and the boundaries of what can be achieved.
4. **Lecture 4**: Consensus protocols — Paxos, Raft, and the art of making machines agree.
5. **Lecture 5**: The CAP theorem and its consequences — consistency, availability, and partition tolerance; why you can't have all three.
6. **Lecture 6**: Consistency models — from linearizability to eventual consistency and every model in between.
7. **Lecture 7**: Conflict-free Replicated Data Types (CRDTs) — how to let data converge without coordination.
8. **Lecture 8**: Distributed transactions — two-phase commit, three-phase commit, sagas, and the illusion of atomicity across machines.
9. **Lecture 9**: Distributed storage — replication, sharding, and the architecture of planetary-scale databases.
10. **Lecture 10**: Fault tolerance and self-healing — crash recovery, leader election, and AI-assisted failure prediction.
11. **Lecture 11**: Security in distributed systems — Byzantine fault tolerance, zero-knowledge proofs, and distributed authentication.
12. **Lecture 12**: The future — quantum networks, AI-managed consensus, and the convergence of physics and computation.

### Key Terminology

- **Node**: An independent computing entity participating in the distributed system. May be a physical machine, a virtual machine, a container, or a logical process.
- **Message**: The fundamental unit of communication between nodes. Messages are the only way nodes learn about each other's state.
- **Latency**: The time delay between sending a message and receiving it. Includes propagation delay, processing time, and queueing delays.
- **Process**: A logical unit of computation. A node may host multiple processes.
- **Consensus**: The problem of getting all non-faulty nodes to agree on a value.
- **Consistency**: The property that all nodes observe the same state (or a well-defined approximation thereof).
- **Availability**: The property that every request receives a response (not an error).
- **Partition tolerance**: The property that the system continues operating despite network partitions.
- **Fault model**: The assumptions about how components can fail — crash, omission, timing, or Byzantine.
- **Idempotence**: The property that performing an operation multiple times has the same effect as performing it once. Critical for handling duplicate messages.

### Required Reading

- Lamport, L. (1978). "Time, Clocks, and the Ordering of Events in a Distributed System." *Communications of the ACM*, 21(7), 558–565.
- Coulouris, G., Dollimore, J., Kindberg, T., & Blair, G. (2012). *Distributed Systems: Concepts and Design* (5th ed.). Addison-Wesley.
- Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly Media. Chapters 5 and 7 (replication and transactions).

### Discussion Questions

1. Consider a Mars-Earth distributed system with 4-22 minute one-way latency. Can such a system achieve strong consistency? Under what conditions?
2. The FLP impossibility result seems to doom all consensus algorithms. Yet production systems achieve consensus daily. How is this paradox resolved?
3. Is a web browser interacting with a web server a "distributed system"? Where do we draw the boundary?

### Practice Problems

1. **Event ordering**: Given the following events across three processes P1, P2, P3, identify which events are concurrent and which are causally related:
   - P1: send(m1), send(m2), receive(m5)
   - P2: receive(m1), send(m3), receive(m4)
   - P3: send(m4), receive(m2), receive(m3)
   Draw the partial order using Lamport's happened-before relation.

2. **Latency calculation**: A distributed system spans three datacenters: DC1 (New York), DC2 (London), DC3 (Tokyo). Speed-of-light one-way latencies are: NY↔London ≈ 28ms, NY↔Tokyo ≈ 78ms, London↔Tokyo ≈ 92ms. What is the minimum possible round-trip time for a three-phase commit across all three sites?

3. **Failure classification**: For each of the following behaviors, classify the failure type (crash, omission, timing, Byzantine):
   - A server that stops responding to all messages
   - A router that drops every third packet
   - A process that responds with its state but 500ms late
   - A compromised node that sends contradictory values to different peers

---

ᛉ **Lecture 2: Time, Clocks, and Causality — The Architecture of Ordering**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Time is the most precious resource in distributed systems — not because it's scarce, but because it's impossible to agree on. In a single machine, the CPU's clock provides a total ordering of events: instruction A happened before instruction B if A's timestamp is less than B's. But across machines, clock drift means that physical timestamps cannot be trusted to order events. A 2025 study by the University of Cambridge measured clock skew across NTP-synced servers in a single datacenter at up to 32ms — an eternity by CPU standards.

This lecture explores the foundational insight that in distributed systems, **causality replaces time** as the ordering principle. We study Lamport clocks, vector clocks, and their modern descendants, along with the practical consequences for system design.

### Lamport Clocks: Logical Ordering

Lamport's 1978 paper introduced one of the most elegant ideas in computer science: a **logical clock** that captures causal ordering without requiring synchronized physical clocks.

**Algorithm:**
1. Each process Pi maintains a counter Ci, initialized to 0.
2. Before executing an event, Pi increments Ci := Ci + 1.
3. When Pi sends a message m, it includes the timestamp Ci.
4. When Pj receives a message m with timestamp Ct, it updates: Cj := max(Cj, Ct) + 1.

This simple mechanism guarantees: **if event A happened-before event B, then C(A) < C(B).**

The converse does NOT hold: C(A) < C(B) does not imply A → B. Two concurrent events may have timestamps that happen to be ordered numerically. This asymmetry is fundamental — Lamport clocks capture causality but do not detect concurrency.

**Why this matters in practice**: Distributed databases use Lamport-style timestamps for conflict detection and resolution. Google's Spanner uses TrueTime (interval-based physical clocks) to provide external consistency, but the underlying logic remains rooted in Lamport's framework.

### Vector Clocks: Detecting Concurrency

To detect whether two events are concurrent (neither happened-before the other), we need **vector clocks** — one timestamp per process.

A vector clock VC is an array [C1, C2, ..., Cn] where Ci represents process Pi's knowledge of its own event count. The comparison rules:

- VC(A) < VC(B) iff ∀i: VC(A)[i] ≤ VC(B)[i] AND ∃j: VC(A)[j] < VC(B)[j]
- VC(A) || VC(B) (concurrent) iff neither VC(A) ≤ VC(B) nor VC(B) ≤ VC(A)

**Update rules:**
1. Before executing a local event, Pi increments VC[i].
2. When sending message m, Pi attaches VC to m.
3. When Pj receives message m with attached Vm, Pj updates: Vj[k] := max(Vj[k], Vm[k]) for all k, then increments Vj[j].

Vector clocks allow us to detect conflicts: if two versions of the same data have concurrent vector clocks, both updates happened independently, and we need conflict resolution.

**Real-world usage**: Amazon DynamoDB uses vector clocks (actually, a variant called "dotted version vectors") to track causality between replicas. When a conflict is detected, the application can resolve it — or DynamoDB can serve both versions for client-side resolution.

### Hybrid Logical Clocks (HLCs)

Physical clocks are imprecise but meaningful (they tell wall-clock time). Logical clocks are precise but meaningless outside the system. **Hybrid Logical Clocks** (Kulkarni, 2014) combine both:

- Hybrid time = (physical timestamp, logical counter)
- The physical timestamp is close to wall-clock time (within the clock uncertainty bound)
- The logical counter provides ordering within the same physical timestamp
- Hybrid time is monotonically increasing and causally consistent

HLCs are used in CockroachDB and YugabyteDB — both distributed SQL databases designed for global consistency. The hybrid approach allows them to provide SQL-compliant transaction ordering without GPS-atomic clocks (unlike Spanner's TrueTime).

### Wall-Clock Synchronization

For systems that need physical time (billing, logging, auditing), the standard synchronization protocols are:

- **NTP (Network Time Protocol)**: Achieves ~1-10ms accuracy on LANs, ~10-100ms on WANs. Uses hierarchical server strata and statistical filtering.
- **PTP (Precision Time Protocol, IEEE 1588)**: Achieves sub-microsecond accuracy on LANs. Used in financial trading, telecommunications, and industrial control.
- **GPS-disciplined clocks**: Atomic clocks synchronized with GPS satellites. Provide microsecond-level accuracy. Used in datacenters for Spanner-style consensus.
- **TrueTime (Google Spanner)**: Returns a time interval [earliest, latest] rather than a point. The real time is guaranteed to be within this interval. Operations wait until the interval's uncertainty has passed, ensuring external consistency.

At UoY, our distributed systems lab uses GPS-disciplined clocks feeding PTP grandmaster clocks, giving each workstation sub-microsecond time agreement — sufficient for Spanner-style consistency without Google's infrastructure.

### The Impossibility of Perfect Synchronization

A fundamental result: **no distributed system can achieve both perfect clock synchronization and asynchronous communication.** This is because:

1. Clock synchronization requires message exchange (NTP, PTP, or similar)
2. Message latency is variable and unbounded in asynchronous networks
3. Any synchronization protocol must make assumptions about latency bounds
4. Those assumptions can be violated by network congestion, routing changes, or deliberate attacks

In practice, systems achieve "good enough" synchronization by:
- Using dedicated time networks (separate from data networks)
- Statistical filtering to reject outliers
- Hardware timestamping (marking packets at the NIC layer, not the OS layer)
- Accepting bounded uncertainty rather than demanding perfection

### Causality and Application Design

Understanding causal ordering changes how we design applications:

- **Collaborative editing**: Google Docs uses operational transformation (OT) — an application of causal ordering to document edits. Each edit is tagged with a vector clock, and the server determines the canonical order.
- **Social media feeds**: If Alice comments on Bob's post, and Bob replies, the reply causally depends on the comment. A news feed must show the comment before the reply, even if the datacenter received them in a different order.
- **Financial transactions**: A transfer must be processed before the resulting balance change is visible. Sequential consistency is the minimum requirement for banking systems.

### Required Reading

- Lamport, L. (1978). "Time, Clocks, and the Ordering of Events in a Distributed System." *CACM*, 21(7), 558–565.
- Mattern, F. (1989). "Virtual Time and Global States of Distributed Systems." *Parallel and Distributed Algorithms*, 215–226.
- Kulkarni, S., Demirbas, M., Madappa, D., & Avva, B. (2014). "Logical Physical Clocks and Consistent Snapshots in Distributed Systems." *CRAFT*.

### Discussion Questions

1. Spanner achieves external consistency through TrueTime intervals and "commit wait." Is this a violation of the FLP impossibility result, or a clever circumvention? Explain.
2. Vector clocks grow linearly with the number of processes. In a system with millions of clients (not servers), this is impractical. What alternatives exist?
3. Consider a collaborative text editor (like Google Docs) that uses CRDTs instead of operational transformation. Does it need vector clocks? Why or why not?

### Practice Problems

1. **Lamport clock trace**: Three processes execute the following events:
   - P1: a→send(m1)→b→receive(m3)→c
   - P2: receive(m1)→d→send(m2)→e→receive(m4)→f
   - P3: receive(m2)→g→send(m3)→h→send(m4)→i
   Calculate Lamport clock values for each event (a through i).

2. **Vector clock conflict**: Two replicas of a shopping cart have the following vector clocks:
   - Replica A: item "laptop" with VC = [2, 3, 1]
   - Replica B: item "phone" with VC = [3, 1, 2]
   Are these concurrent or is one an update of the other? What conflict resolution strategy would you use?

3. **Clock drift**: Two servers have clocks that drift at 1ms/minute relative to each other. NTP resynchronizes every 5 minutes with a 0.5ms uncertainty per sync. What is the maximum clock skew between two events that each server considers "simultaneous"?

---

ᛉ **Lecture 3: Failure Models and Byzantine Agreement — When Machines Lie**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Every distributed system algorithm lives or dies by its failure model — the assumptions it makes about how components can misbehave. A system designed for crash failures will collapse under Byzantine faults. A system designed for Byzantine faults will be over-engineered (and slow) for environments where crashes are the worst case. Choosing the right model is the most consequential design decision you will make.

This lecture maps the taxonomy of failures from the simplest to the most devious, and explores the theoretical limits of what can be achieved under each model.

### The Failure Taxonomy

**1. Crash-stop (fail-stop)**
The process halts and never recovers. This is the simplest model — a node is either working correctly or it is permanently gone.
- *Detection*: A watchdog timer or heartbeat can detect crash-stop failures with certainty (given bounded message delay).
- *Recovery*: Impossible by definition. The system must reconfigure itself without the failed node.
- *Example*: A server whose power supply fails. It doesn't send conflicting messages; it sends nothing.

**2. Crash-recovery**
The process halts but may restart with stable storage intact. It "forgets" its in-memory state but can recover persisted data.
- *Detection*: Same as crash-stop, but detection is less urgent because the node may recover.
- *Recovery*: Requires a recovery protocol — the process must replay its actions from a durable log or obtain the current state from its peers.
- *Example*: A server that runs out of memory, crashes, and restarts. Its disk is intact.

**3. Omission**
The process fails to send or receive messages. It may selectively drop messages while otherwise acting correctly.
- *Detection*: Cannot be distinguished from slow processes in an asynchronous system.
- *Recovery*: Retransmission, acknowledgments, and timeouts handle most omission failures.
- *Example*: A network interface that occasionally drops packets due to buffer overflow.

**4. Timing**
The process violates timing assumptions — it responds too early, too late, or with inconsistent timing.
- *Detection*: Requires a synchronous system model with known timing bounds.
- *Recovery*: Timeout adjustment and adaptive waiting.
- *Example*: A process running on an overloaded machine that takes 10x longer than expected to respond.

**5. Byzantine (arbitrary)**
The process may behave arbitrarily — it may send contradictory messages to different peers, pretend to be functioning when it is not, or actively collude with other Byzantine processes. This is the most general and most dangerous failure model.
- *Detection*: Fundamentally difficult. Byzantine processes can perfectly mimic correct behavior until the moment they choose to deviate.
- *Recovery*: Requires redundancy — specifically, 3f+1 nodes to tolerate f Byzantine faults.
- *Example*: A compromised server running malicious firmware that sends different transaction values to different replicas.

### Impossibility Results

**FLP Impossibility (Fischer, Lynch, Patterson, 1985)**
In a fully asynchronous system (no timing assumptions), no deterministic algorithm can solve consensus if even one process may crash. The proof works by showing that any decider can be kept ambiguous indefinitely — a process that is "slow" cannot be distinguished from one that has crashed, so the algorithm can never safely commit to a decision.

**Practical resolution**: FLP is theoretically absolute but practically circumvented:
- **Randomized algorithms**: Ben-Or's randomized consensus and subsequent protocols introduce probability. They terminate with probability 1 (eventually) but not with certainty.
- **Partial synchrony**: Dwork, Lynch, and Stockmeyer (1988) showed that consensus is solvable under "partially synchronous" conditions — if the system eventually becomes synchronous for long enough, consensus can be achieved.
- **Failure detectors**: Chandra and Toueg (1996) showed that unreliable failure detectors (which may suspect correct processes or fail to suspect crashed ones) can be used to solve consensus. The key insight: a failure detector of class ♦S (eventually strong) is sufficient.

**Byzantine Agreement Lower Bounds**
- **Resilience**: To tolerate f Byzantine nodes, you need at least n ≥ 3f + 1 total nodes. (Proof: the Byzantine nodes can make two groups of correct nodes disagree.)
- **Communication**: Byzantine agreement requires at least f + 1 synchronous rounds. (Linear lower bound.)
- **Authentication**: With digital signatures (authenticated Byzantine agreement), the resilience requirement drops to n ≥ 2f + 1, because nodes cannot forge messages from other nodes.

### Practical Byzantine Fault Tolerance

**PBFT (Castro and Liskow, 1999)** remains the most influential practical BFT protocol:
- Requires 3f + 1 replicas to tolerate f Byzantine faults
- Uses a three-phase protocol: pre-prepare, prepare, commit
- Achieves safety under all conditions (even asynchronous)
- Achieves liveness under partial synchrony
- Performance: ~1ms overhead per operation in a local cluster

**HotStuff** (used in Meta's Diem/Libra blockchain, 2019):
- Improves PBFT's communication complexity from O(n²) to O(n) using threshold signatures
- Linear communication makes it practical for hundreds or thousands of validators
- Three-phase: prepare, pre-commit, commit
- The basis for most modern blockchain consensus protocols

**Tendermint** (used in Cosmos ecosystem):
- BFT-style consensus with a rotating proposer
- Two rounds: pre-vote and pre-commit
- Accountable safety: if two blocks are finalized, at least 1/3 of validators signed conflicting votes (evidence of misbehavior)
- Used by over 200 production blockchains as of 2040

### The Byzantine Generals Problem in 2040

By 2040, Byzantine failures are no longer theoretical:
- **AI-compromised nodes**: An adversarial AI can mimic correct behavior for arbitrarily long periods before deviating, making detection nearly impossible.
- **Supply chain attacks**: Hardware implants (一如 the 2018 Bloomberg "Supermicro" allegations, though disputed) can cause Byzantine behavior at the firmware level.
- **Cloud megafailures**: When thousands of VMs share a hypervisor, a single hypervisor bug can cause correlated Byzantine failures across seemingly independent nodes.

The lesson: **design for the failure model that matches your threat, not the one that's most convenient.** If your system processes money, identity, or safety-critical decisions, Byzantine fault tolerance is not paranoia — it's engineering responsibility.

### Required Reading

- Lamport, L., Shostak, R., & Pease, M. (1982). "The Byzantine Generals Problem." *ACM Transactions on Programming Languages and Systems*, 4(3), 382–401.
- Fischer, M. J., Lynch, N. A., & Patterson, M. S. (1985). "Impossibility of Distributed Consensus with One Faulty Process." *Journal of the ACM*, 32(2), 374–382.
- Castro, M. & Liskow, B. (1999). "Practical Byzantine Fault Tolerance." *OSDI '99*.
- Yin, M., Malkhi, D., Reiter, M. K., Gueta, G., & Abraham, I. (2019). "HotStuff: BFT Consensus with Linearity and Responsiveness." *ACM PODC*.

### Discussion Questions

1. A blockchain validator node is caught signing two conflicting blocks. Under Tendermint's accountable safety, what percentage of validators must be Byzantine for the system to finalize two conflicting blocks? Explain the mathematical proof.
2. FLP impossibility states that no deterministic protocol can guarantee consensus in asynchronous systems. Yet production consensus protocols (Raft, Paxos, PBFT) work reliably. How do they circumvent FLP?
3. Consider a system where nodes are not compromised by attackers but can have arbitrary software bugs (e.g., a defective update pushed to 30% of nodes). Is this a crash model or a Byzantine model? Why does the distinction matter?

### Practice Problems

1. **Resilience calculation**: A BFT system must tolerate 5 Byzantine nodes. What is the minimum number of total nodes required? If each node can process 10,000 requests/second, what is the system's maximum throughput assuming the BFT protocol adds 3 round-trips per request?
2. **PBFT trace**: In a PBFT system with 4 nodes (f=1), trace the message flow for a client request through all three phases. Assume node 3 is Byzantine and sends conflicting pre-prepare messages. Show how the honest nodes (0, 1, 2) reach consensus despite node 3's misbehavior.
3. **Failure classification**:
   - A DNS server that returns NXDOMAIN for valid domains: What failure type?
   - A load balancer that routes 90% of traffic to one backend: What failure type?
   - A compromised certificate authority that issues fake certs: What failure type?

---

ᛉ **Lecture 4: Consensus Protocols — Paxos, Raft, and the Art of Agreement**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Consensus is the beating heart of every distributed system that must maintain consistent state. Whether it's a database deciding the next write, a blockchain validator agreeing on the next block, or a cluster choosing which node leads, the fundamental problem is the same: **how do a group of unreliable participants agree on a single value?**

This lecture covers the two most influential consensus protocols in distributed computing history: Paxos (the mathematical foundation) and Raft (the practical implementation). We also examine their 2040 descendants — Adaptive Paxos, EPaxos, and Raft-based systems in production.

### The Consensus Problem

A consensus protocol must satisfy three properties:

1. **Safety (Agreement)**: All non-faulty nodes decide on the same value. No two correct nodes decide differently.
2. **Validity**: The decided value must have been proposed by some node. You can't decide on a value that nobody proposed.
3. **Liveness (Termination)**: Every non-faulty node eventually decides.

FLP impossibility tells us we can't guarantee all three under full asynchrony with crash failures. The practical resolution: assume partial synchrony, use randomization, or accept "with probability 1" termination.

### Paxos: The Theoretical Complete

Leslie Lamport wrote "The Part-Time Parliament" in 1990, presenting Paxos as a fictional parliamentary procedure on the ancient Greek island of Paxos. The academic community, unfamiliar with the parable style, largely ignored it. Lamport eventually rewrote it as "Paxos Made Simple" (2001), acknowledging that "the algorithm is simple, but the presentation was not."

**Paxos roles** (a single process may play multiple roles):
- **Proposer**: Proposes a value for consensus
- **Acceptor**: Votes on proposals and stores the decided value
- **Learner**: Learns the decided value

**Basic Paxos (single-decree):**

Phase 1a: Proposer sends `Prepare(n)` with proposal number n to all acceptors.
Phase 1b: Each acceptor promises not to accept proposals numbered less than n. If it has already accepted a proposal, it returns that proposal's number and value.
Phase 2a: Proposer sends `Accept(n, v)` where v is the value from the highest-numbered accepted proposal it heard, or its own value if no acceptor had accepted anything.
Phase 2b: Each acceptor accepts the proposal unless it has promised to a higher number.

**Multi-Paxos**: In practice, we need to agree on a sequence of values (a log). Multi-Paxos optimizes by electing a stable leader that skips Phase 1 for subsequent proposals, reducing the protocol to a single round-trip per decision.

**Key insight**: Paxos achieves safety even during network partitions — two groups of acceptors cannot decide different values. Liveness requires a stable leader and message delivery.

### Raft: Understandability as a Feature

Diego Ongaro and John Ousterhout designed Raft (2014) with an explicit goal: **understandability**. Where Paxos was notoriously difficult to understand and implement correctly, Raft decomposes consensus into independent subproblems:

1. **Leader Election**: Nodes participate in elections. A candidate becomes leader if it receives votes from a majority. Terms provide logical time — each election starts a new term.
2. **Log Replication**: The leader appends entries to its log and replicates them to followers. An entry is "committed" when a majority have it in their logs.
3. **Safety**: If a log entry is committed on one server, it will be present on all future leaders. This is enforced by the election restriction: a candidate must have an up-to-date log to win election.

**Raft's key simplifications over Paxos**:
- **Strong leader**: All log entries flow from leader to followers. No competing proposers.
- **Leader election is separate from log replication**: Decomposing the problem makes each piece tractable.
- **State space reduction**: Raft guarantees that if any two logs share an entry at the same index, all prior entries are identical. This dramatically simplifies log reconciliation.

**The Raft consensus flow:**

1. Client sends command to leader
2. Leader appends command to its log as entry X
3. Leader sends AppendEntries RPCs to all followers
4. Followers append entry X
5. Followers respond with success
6. Once a majority respond, leader commits entry X
7. Leader applies entry X to state machine
8. Leader responds to client

If the leader crashes, followers notice the lack of heartbeats, start an election, and the candidate with the most up-to-date log wins. The system self-heals.

### Modern Consensus: EPaxos and Beyond

**Egalitarian Paxos (EPaxos)** removes the leader bottleneck. Commands are naturally commutative (like increment operations) and don't need total ordering. EPaxos achieves fast-path commit in a single communication step for non-conflicting commands. For conflicting commands, it falls back to a three-step slow path.

Command dependencies are tracked explicitly: each command records which other commands it depends on. If all dependencies have already been committed, a command can be committed in a single round trip.

**Mencius** rotates the leader role among all replicas, eliminating the single-leader throughput bottleneck. Each replica proposes commands in round-robin order. The cost: any slow replica blocks progress for its slots (solvable with skip requests).

**Raft in Production (2040)**: etcd (Kubernetes' datastore), Consul (HashiCorp's service mesh), TiKV (distributed key-value store), and CockroachDB's metadata layer all use Raft. The protocol has proven remarkably robust — Google's Chubby lock service, Apache ZooKeeper (Zab protocol), and virtually every coordination service implements a Raft or Paxos variant.

### Consensus at the University of Yggdrasil

Our distributed systems lab runs a 9-node Raft cluster that students use for hands-on experimentation. Students can:
- Inject network partitions and observe leader election
- Crash leaders and watch the cluster recover
- Introduce Byzantine behavior and measure system degradation
- Implement a simple key-value store on top of Raft's log

This practical experience — watching consensus algorithms fail, recover, and adapt — is worth a thousand pages of lecture notes.

### Required Reading

- Ongaro, D. & Ousterhout, J. (2014). "In Search of an Understandable Consensus Algorithm." *USENIX ATC*.
- Lamport, L. (2001). "Paxos Made Simple." *ACM SIGACT News*, 32(4), 18–25.
- Moraru, I., Andersen, D. G., & Kaminsky, M. (2013). "There is More Consensus in Egalitarian Parliaments." *SOSP*.

### Discussion Questions

1. Raft's leader election requires that a candidate's log be at least as up-to-date as any other node's. What would happen if this restriction were removed? Construct a scenario where two clients receive different responses for the same query.
2. In a Raft cluster of 5 nodes, two nodes are permanently partitioned from the other three. Can the partitioned group of two elect a leader? Can the group of three? What happens when the partition heals?
3. Paxos allows multiple proposers to propose simultaneously; Raft funnels all proposals through a single leader. What are the trade-offs in throughput, latency, and failure handling?

### Practice Problems

1. **Raft election trace**: A 5-node Raft cluster has the following log state at the start of an election:
   - S1: [X, Y, _]
   - S2: [X, Y, Z]
   - S3: [X, Y, Z]
   - S4: [X, Y, _]
   - S5: [X, _, _]
   S2 and S3 have the most complete logs. If S1 starts an election with term 4, can S1 win? If not, which servers can win an election, and why?

2. **Paxos scenario**: Three acceptors (A1, A2, A3) and two proposers (P1, P2). P1 sends Prepare(3) and gets responses from A1 and A2. P2 sends Prepare(4) and gets responses from A2 and A3. P1 then sends Accept(3, "v1") - does it succeed? Trace through the protocol and explain each step.

3. **Throughput calculation**: A Raft cluster of 5 nodes processes 50,000 operations/second. The leader fails and a new election takes 150ms. How many operations are lost (not processed) during the election? If the average client round-trip time is 10ms, what is the effective throughput during normal operation?

---

ᛉ **Lecture 5: The CAP Theorem — Pick Two (But Not Really)**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

The CAP theorem is simultaneously the most famous and most misunderstood result in distributed systems. Eric Brewer stated it as a conjecture at PODC 2000; Seth Gilbert and Nancy Lynch proved it in 2002. The theorem states:

**A distributed system cannot simultaneously provide all three of:**
- **Consistency (C)**: Every read returns the most recent write or an error.
- **Availability (A)**: Every request receives a non-error response (not guaranteed to be the most recent write).
- **Partition tolerance (P)**: The system continues operating despite network partitions.

The theorem is often stated as "pick two of three," but this is misleading. In reality, **you always need P** because network partitions are a fact of distributed systems. The real choice is between C and A **during a partition**:

- **CP systems**: Maintain consistency by refusing reads/writes during a partition. Clients may receive errors or timeouts.
- **AP systems**: Maintain availability by serving reads/writes during a partition, even if the data may be stale. Conflicts are resolved when the partition heals.

### The Formal Proof

Gilbert and Lynch's proof is elegant:

1. Assume a network partition splits the system into two groups: G1 and G2.
2. A client in G1 writes a value v1.
3. A client in G2 writes a value v2.
4. If the system is **consistent**, G1 and G2 cannot both return their local values (they must agree).
5. If the system is **available**, both G1 and G2 must respond to reads (not return errors).
6. If both C and A hold, then G1 returns v1 and G2 returns v2 — a contradiction with C.
7. Therefore, C and A cannot both hold during a partition.

### The Nuance: It's Not Binary

The CAP theorem as stated is an asymptotic result — it applies in the limit, during partitions. In practice, the real questions are:

- **How long is the partition?** Most network partitions last milliseconds to seconds. The choice between C and A may be different for a 100ms partition vs. a 24-hour partition.
- **How stale is "stale"?** An AP system might serve data that's only seconds old, which is perfectly acceptable for many applications.
- **Can we get eventual consistency?** AP systems can guarantee that once the partition heals, all replicas will converge to the same state. The window of inconsistency is bounded.

**The PACELC theorem** (Abadi, 2012) generalizes CAP:
- If there is a **P**artition: how does the system trade off **A**vailability vs. **C**onsistency?
- **E**lse (normal operation): how does the system trade off **L**atency vs. **C**onsistency?

This is a much more useful framework. In normal operation (no partition), the trade-off is between latency and consistency — reading from a quorum of replicas is slower but more consistent than reading from the nearest replica.

### Consistency Patterns in Practice

**Strong Consistency (Linearizability)**
Every read sees the most recent write. Requires coordination — typically a quorum read and write. Used in:
- Financial systems (bank balances)
- Identity management (user credentials)
- Inventory systems (preventing overselling)

**Causal Consistency**
Reads respect causal ordering but allow concurrent writes to be seen in different orders. Used in:
- Social media (comment replies always appear after the original comment)
- Collaborative editing (edit order respects causality)

**Eventual Consistency**
Given enough time without new writes, all replicas converge. Used in:
- DNS (updates propagate over hours)
- Shopping carts (Amazon's DynamoDB)
- Caching layers (CDN content)

**Session Consistency**
Within a single client session, reads are consistent with that client's writes. Used in:
- User profile updates (you always see your own writes)
- Shopping cart modifications

### 2040 Perspective: Adaptive Consistency

By 2040, the most sophisticated systems don't choose a single point on the CAP spectrum — they **adapt dynamically** based on workload and conditions:

- **Google Spanner's TrueTime**: During normal operation, provides external consistency (stronger than linearizability). If TrueTime uncertainty bounds are exceeded, transactions block rather than risk inconsistency.
- **CockroachDB's "consistent reads, stale reads"**: Strong reads use Raft quorums; stale reads serve from local replicas with bounded staleness.
- **Cosmos DB's consistency levels**: Five configurable levels (strong, bounded staleness, session, consistent prefix, eventual) that let different operations use different consistency settings.
- **AI-driven consistency adaptation**: Some systems monitor network conditions and workload patterns, automatically switching between CP and AP modes based on predicted partition probability and data criticality.

### Required Reading

- Gilbert, S. & Lynch, N. (2002). "Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services." *ACM SIGACT News*, 33(2), 51–59.
- Abadi, D. (2012). "Consistency Tradeoffs in Modern Distributed Database System Design." *IEEE Computer*, 45(2), 37–42.
- Kleppmann, M. (2017). *Designing Data-Intensive Applications*, Chapters 5 and 9.

### Discussion Questions

1. You're building a real-time multiplayer game. Should you choose CP or AP? What consistency model makes the most sense for player position updates vs. inventory updates?
2. A social media platform has three features: news feed, direct messages, and payment processing. Which consistency model is appropriate for each? Can a single database serve all three?
3. Critique the claim: "CP systems are better than AP systems because data consistency is always more important than availability." Give two concrete counterexamples.

### Practice Problems

1. **CAP classification**: Classify each of the following systems as CP, AP, or neither:
   - HBase (Hadoop database)
   - Cassandra
   - MongoDB (default configuration)
   - Google Spanner
   - Redis (single master with replicas)

2. **Consistency window**: An AP system with 3 replicas receives a write at time T. Replica propagation takes between 50ms and 200ms. What is the maximum staleness (in milliseconds) a read can observe? Under what conditions would a read observe a value from T-500ms?

3. **Latency-consistency trade-off**: A system can be configured in two modes:
   - Mode A: Read from quorum (3 of 5 replicas) — 12ms average latency, strong consistency
   - Mode B: Read from nearest replica — 2ms average latency, eventual consistency
   An e-commerce site does 10,000 reads/second and 100 writes/second. The cost of serving stale inventory data is estimated at $0.01 per stale read (lost sales from overselling). The revenue impact of 10ms higher latency is $500/hour. Which mode is more profitable?

---

ᛉ **Lecture 6: Consistency Models — From Linearizability to Eventual and Beyond**

**Course:** CS301 — Distributed Systems  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

If the CAP theorem tells us we must choose between consistency and availability during partitions, consistency models tell us **exactly what we're choosing between**. A consistency model is a contract between the distributed system and its clients — it specifies what values a read operation may return, given the history of preceding writes.

This lecture provides a precise taxonomy of consistency models, from the strongest (linearizability) to the weakest (eventual consistency), and examines the performance, complexity, and applicability trade-offs at each level.

### The Consistency Model Hierarchy

Consistency models form a partial order — each model provides guarantees that are strictly stronger than (or incomparable to) other models. From strongest to weakest:

**1. Strict Consistency (Atomic Consistency)**
Every read returns the value of the most recent write, where "most recent" is defined by a global real-time order. This is the strongest possible model and is unimplementable without instantaneous communication (i.e., it requires FTL signaling). Useful as a theoretical bound, but physically impossible in distributed systems.

**2. Linearizability (Atomic Consistency in Practice)**
Every operation appears to take effect atomically at some point between its invocation and response. The global order is consistent with real-time ordering: if operation A completes before operation B starts, then A appears before B in the linearization order.

- **Implementation cost**: Requires communication with a quorum of replicas for every operation. Typical latency: 2-4 round trips within a datacenter.
- **Use cases**: Distributed locks, unique ID generation, configuration updates.
- **Systems**: Google Spanner, etcd, ZooKeeper.

**3. Sequential Consistency**
The result of any execution is equivalent to a sequential execution where operations of each process appear in program order. Unlike linearizability, there is no real-time constraint — operations can be reordered as long as each process's order is preserved.

- **Key difference from linearizability**: Two concurrent writes may appear to different processes in different orders, as long as each process sees a consistent sequential history.
- **Implementation cost**: Still requires coordination, but allows more aggressive optimization than linearizability.
- **Use cases**: Shared memory models, some database transactions.

**4. Causal Consistency**
Operations that are causally related (A → B, meaning A could have influenced B) appear in the same order on all processes. Concurrent operations may appear in different orders on different processes.

- **Implementation cost**: Requires tracking causality (vector clocks or similar), but does not require global coordination for concurrent operations.
- **Use cases**: Social media feeds, collaborative documents, messaging systems.
- **Systems**: COPS, Bolt-on Causal Consistency.

**5. PRAM (Pipeline Random Access Memory) Consistency**
Writes by a single process are seen by all processes in the order they were issued. Writes from different processes can be seen in different orders by different observers.

- **Implementation cost**: Only requires FIFO message ordering between each pair of processes.
- **Use cases**: Low-latency replication where process-local ordering suffices.

**6. Read-Your-Writes Consistency**
A process always reads at least the latest value it wrote. This is session consistency — it only applies within a single client session.

- **Implementation cost**: Session-level tracking only. No cross-session coordination needed.
- **Use cases**: User profile updates (you always see your own latest changes).

**7. Monotonic Reads**
If a process reads value v at time t, it will never read an older value at any time after t. Reads are monotonic — they only move forward in time.

- **Implementation cost**: Lightweight — just track the highest timestamp seen by each client.
- **Use cases**: Leaderboard displays, version-controlled documents.

**8. Eventual Consistency**
If no new writes are made, eventually all replicas will converge to the same value. No ordering guarantees during the convergence window.

- **Implementation cost**: Minimal — just propagate updates asynchronously. No coordination needed.
- **Use cases**: DNS, caching, shopping carts, any system that tolerates temporary inconsistency.

### The Consistency Lattice

The relationships between these models form a lattice:

```
Strict ← Linearizable ← Sequential ← Causal ← PRAM
                                          ↓
                                   Read-Your-Writes ← Monotonic Reads
                                          ↓
                                   Eventual Consistency
```

Models on the same path provide stronger guarantees. Models on different branches are incomparable (neither subsumes the other) — for example, PRAM and Read-Your-Writes are incomparable, which is why "session guar