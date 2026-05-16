# CS307: Parallel & Distributed Computing
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4
**Prerequisites:** CS201 — Data Structures & Algorithms II; CS205 — Theory of Computation; CS302 — Compiler Design & Code Generation
**Description:** The era of free lunch is over. For three decades (1985–2015), programs automatically doubled in speed every 18 months as clock frequencies increased. That era ended: frequency scaling hit physical limits (power density, heat dissipation), and the industry pivoted to multicore processors. Now, performance gains come only through parallelism — writing programs that do multiple things simultaneously. This course covers the two major paradigms of concurrent computation: **shared-memory parallelism** (multithreading, locks, lock-free data structures, transactional memory, GPU computing) and **distributed computing** (message passing, consensus, fault tolerance, distributed storage, distributed consensus algorithms like Raft and Paxos, and the CAP theorem). Students learn to write parallel programs in C++ (OpenMP, threads, atomics) and Python (multiprocessing, asyncio, Dask), and distributed systems in Go or Rust with message-passing libraries. The course also covers the theoretical foundations — Amdahl's law, Gustafson's law, the PRAM model, the FLP impossibility result (consensus in asynchronous systems is impossible with one faulty process), and the CAP theorem (consistency, availability, partition tolerance — choose two). The Norse framing is the *Ásbrú* (the divine bridge) — the Rainbow Bridge Bifröst that connects Midgard to Ásgarðr. Parallelism is a bridge: the program must be disassembled into concurrent parts, sent across the bridge, and reassembled on the other side, correctly, without loss or corruption.

---

## Lecture 1: The End of Free Lunch — Why We Must Parallelise

From 1985 to 2005, programmers watched their software get faster without lifting a finger. Moore's law (transistor density doubles every 18 months) combined with Dennard scaling (power density remains constant as transistors shrink) meant that each new generation of processors ran at higher clock frequencies while consuming the same power. The result: single-threaded programs doubled in performance every 18–24 months.

Dennard scaling broke around 2005. At 90nm process nodes, leakage current became significant, and power density no longer remained constant. Clock frequencies peaked at ~4 GHz for commodity CPUs and began to decline (or at best stagnate). The industry's response was the **multicore pivot**: instead of making one core faster, put multiple cores on a single chip. Clock frequency gains stopped; core counts rose from 2 (2005) to 64+ (2025) and beyond.

**Amdahl's law** (Gene Amdahl, 1967) captures the fundamental limit of parallelism: if a fraction P of a computation is parallelisable, and a fraction (1−P) must remain serial, the maximum speedup with N processors is:

Speedup(N) = 1 / ((1−P) + P/N)

As N → ∞, the speedup approaches 1/(1−P). If 5% of the computation is serial, the maximum speedup is 20×, regardless of how many processors we throw at it. Amdahl's law is a sobering reminder: parallelism is not a silver bullet — it only accelerates what can be parallelised.

**Gustafson's law** (John Gustafson, 1988) offers a more optimistic perspective. Gustafson argued that the problem size should scale with the number of processors. If we fix the *execution time* (rather than the problem size), the scaled speedup is:

Scaled Speedup(N) = (1−P) + N·P

where P is the parallel fraction when run on N processors. Gustafson's law captures the intuition behind "strong scaling" (fixed problem size, as many processors as needed) vs "weak scaling" (problem size grows with processor count, keeping work per processor constant). Most real applications fall between the two extremes.

**The parallel computation model** is the PRAM (Parallel Random Access Machine), an idealised model where N processors share a global memory and all operations are synchronised. The PRAM is a useful theoretical device (for reasoning about parallel algorithms) but a poor representation of real hardware, where memory access times are non-uniform (NUMA), caches are not coherent across sockets, and synchronisation costs are significant. More realistic models include the **BSP** (Bulk Synchronous Parallel) model and the **LogP** model.

**Required Reading:**
- Herb Sutter, "The Free Lunch Is Over: A Fundamental Turn Toward Concurrency in Software" (*Dr. Dobb's Journal* 30:3, 2005): 16–20 — the seminal essay
- Gene Amdahl, "Validity of the Single Processor Approach to Achieving Large-Scale Computing Capabilities" (*AFIPS*, 1967) — Amdahl's law
- John L. Gustafson, "Reevaluating Amdahl's Law" (*Communications of the ACM* 31:5, 1988): 532–533
- Leslie G. Valiant, "A Bridging Model for Parallel Computation" (*Communications of the ACM* 33:8, 1990): 103–111 — the BSP model
- UoY Parallel Speedup Simulator: Explore Amdahl vs Gustafson laws interactively (2040)

**Discussion Questions:**
1. Amdahl's law states that the serial fraction (1−P) is the ultimate bottleneck. In a typical data-processing pipeline, what are the common sources of serialisation — and how can they be reduced or eliminated?
2. Gustafson's law argues that problem size should grow with processor count. For a web search engine indexing the web, is this natural — or are there fundamental limits to weak scaling?
3. The PRAM model assumes unit-cost memory access for all processors. In a NUMA machine, accessing memory on a remote socket costs 1.5–3× more than local memory. How does NUMA affect the design of parallel algorithms?

---

## Lecture 2: Shared-Memory Parallelism — Threads, Locks, and Atomics

Shared-memory parallelism is the dominant paradigm for multicore processors. Multiple threads (lightweight processes that share the same address space) execute concurrently on different cores, accessing and modifying shared data structures. The programmer's challenge is to ensure **correctness** (no thread sees an inconsistent state) while maximising **performance** (minimising synchronisation overhead).

**Thread creation** in C++ uses `std::thread`; in Python, the `threading` module (with the caveat that Python's GIL — Global Interpreter Lock — prevents true parallelism for CPU-bound tasks — use `multiprocessing` instead). A thread pool (or *executor*) amortises thread creation overhead by reusing a fixed pool of worker threads:
```cpp
std::vector<std::thread> pool;
for (int i = 0; i < num_threads; ++i)
    pool.emplace_back(worker_function, i);
for (auto &t : pool) t.join();
```

**Race conditions** occur when two threads access the same memory location simultaneously, at least one access is a write, and the accesses are not synchronised. The outcome depends on the timing of the scheduler — a **data race** is undefined behaviour in C++, leading to crashes, corrupted data, or (worst of all) correct behaviour that changes unpredictably.

**Mutexes** (mutual exclusion locks) protect critical sections — regions of code that access shared data:
```cpp
std::mutex mtx;
int counter = 0;
void increment() {
    std::lock_guard<std::mutex> lock(mtx);
    ++counter;
}
```
Mutexes serialise access, creating contention: when multiple threads contend for the same lock, they wait. High contention destroys parallelism (the threads spend more time waiting than working). **Lock striping** (multiple locks protecting different ranges of data), **reader-writer locks**, and **lock-free data structures** mitigate contention.

**Deadlocks** occur when two threads each hold a lock that the other needs. The classic four Coffman conditions (1971) are: mutual exclusion, hold-and-wait, no preemption, and circular wait. Deadlock prevention eliminates one condition; deadlock avoidance uses resource ordering (acquire locks in a fixed global order); deadlock detection and recovery is used in high-availability systems.

**Atomic operations** (`std::atomic` in C++, `atomic` in Python via the `multiprocessing` module) provide lock-free synchronisation for simple operations: load, store, compare-and-exchange (CAS), fetch-and-add. Atomic operations are the building blocks of **lock-free data structures** — data structures that guarantee system-wide progress even when any thread is suspended or delayed. Lock-free data structures avoid the problems of deadlock, priority inversion, and contention at the cost of increased algorithmic complexity.

**Required Reading:**
- Maurice Herlihy & Nir Shavit, *The Art of Multiprocessor Programming* (revised ed., Morgan Kaufmann, 2012/2042), chs. 1–8 — the definitive text on shared-memory concurrency
- Anthony Williams, *C++ Concurrency in Action* (2nd ed., Manning, 2019/2041), chs. 1–5
- Paul E. McKenney, "Is Parallel Programming Hard, and, If So, What Can You Do About It?" (kernel.org, continuously updated) — Linux kernel RCU primer
- E. G. Coffman, M. J. Elphick & A. Shoshani, "System Deadlocks" (*ACM Computing Surveys* 3:2, 1971): 67–78
- UoY Parallel Debugging Lab: Use ThreadSanitizer to detect data races in a C++ program (2040)

**Discussion Questions:**
1. Mutex contention reduces parallelism. Under what circumstances is a reader-writer lock (`std::shared_mutex`) more effective than a plain mutex — and when does it make performance worse?
2. Lock-free data structures offer progress guarantees but are notoriously difficult to implement correctly. For what applications is lock-free worth the complexity — and when is a well-tuned lock-based design a better choice?
3. Python's GIL prevents true parallel execution of Python bytecode. What workarounds exist (multiprocessing, C extensions, PyPy STM) — and what are their trade-offs?

---

## Lecture 3: The Memory Model — What Every Parallel Programmer Must Know

The **memory model** of a programming language or architecture defines the rules for how memory operations from different threads interact. Without a memory model, the compiler is free to reorder, eliminate, or merge memory operations, and the hardware is free to reorder load and store instructions — optimisations that are invisible in single-threaded code but catastrophic in concurrent code.

The **sequential consistency (SC)** model (Lamport, 1979) is the simplest and most intuitive: all memory operations appear to execute in a single, global order that respects each thread's program order. SC is the programmer's mental model — but it is also the most restrictive: both compilers and processors aggressively reorder memory operations for performance. No mainstream hardware implements SC for its memory subsystem (though some, like x86 with SSE/AVX, are closer than others).

The **total store order (TSO)** model (x86) allows store-to-load reordering: a write by one thread may become visible to other threads *after* subsequent reads from that thread. Store buffers cause this: a thread writes a value to its store buffer, and the write is not visible to other threads until the store buffer drains. TSO is stronger (less reordering) than the relaxed models of ARM and RISC-V (which allow load-load, load-store, store-load, and store-store reordering).

In C++ (since C++11), the memory model is defined in terms of **acquire-release semantics**:
- **Acquire semantics** (load-acquire): subsequent memory operations cannot be reordered before the acquire. An acquire operation synchronises with a release operation on the same atomic variable.
- **Release semantics** (store-release): prior memory operations cannot be reordered after the release.
- **Relaxed semantics** (`memory_order_relaxed`): no ordering guarantees — only atomicity. Use only when ordering is enforced by other means (e.g., the thread event counter handles synchronisation).

The **happens-before** relation (Leslie Lamport, 1978) is the fundamental ordering in concurrent programs: if operation A happens-before operation B, then every thread sees A before B. Happens-before is defined as the transitive closure of:
1. Program order within a thread
2. Synchronisation operations (acquire synchronises with release on the same atomic variable)
3. Thread creation (`std::thread::join`)
4. Fences (`std::atomic_thread_fence`)

**Data-race freedom** is the key guarantee: a program with no data races (all conflicting accesses are ordered by happens-before) executes as if it were sequentially consistent. A program with data races has undefined behaviour — the compiler can generate arbitrary code, including code that crashes, produces wrong results, or (the particularly insidious case) behaves correctly on the test machine but not on production hardware.

**Required Reading:**
- Leslie Lamport, "How to Make a Multiprocessor Computer That Correctly Executes Multiprocess Programs" (*IEEE Transactions on Computers* 28:9, 1979): 690–691 — sequential consistency
- Leslie Lamport, "Time, Clocks, and the Ordering of Events in a Distributed System" (*Communications of the ACM* 21:7, 1978): 558–565 — happens-before
- Hans-J. Boehm & Sarita V. Adve, "Foundations of the C++ Concurrency Memory Model" (*PLDI*, 2008): 68–78
- Paul E. McKenney, "Memory Ordering in Modern Microprocessors" (*Linux Journal*, 2005) — hardware memory models
- UoY Memory Model Simulator: Explore the effects of relaxed memory ordering on a small concurrent program (2040)

**Discussion Questions:**
1. Sequential consistency is the programmer's natural mental model, but it prohibits many compiler and hardware optimisations. Is SC implementable in modern processors — and what performance cost would it exact?
2. The `memory_order_relaxed` mode provides only atomicity, no ordering. Give a concrete example where relaxed atomics are safe and necessary for performance — and show how to verify correctness.
3. Java and C++ both have memory models, but they differ in important details (Java guarantees "out-of-thin-air" safety for data races; C++ does not). What are the practical consequences of this difference?

---

## Lecture 4: GPU Computing — Massively Parallel Throughput

Graphics Processing Units (GPUs) are not faster CPUs — they are different processors, designed for **data-parallel** workloads where the same operation is applied to millions of data elements. A modern GPU (NVIDIA H100, AMD MI300X) has 10,000–15,000 cores organised into streaming multiprocessors (SMs), with a memory hierarchy that includes global memory (up to 80 GB, HBM3), L2 cache, per-SM shared memory (up to 228 KB), and per-thread registers.

The **CUDA** programming model (NVIDIA, 2007) organises threads into a hierarchy:
- **Grid:** All threads launched by a single kernel invocation.
- **Block:** A group of threads (up to 1024) that execute on the same SM and share shared memory.
- **Warp:** A group of 32 threads that execute in lockstep on a single SM — the fundamental unit of execution on NVIDIA GPUs.

**Warp divergence** occurs when threads in the same warp take different execution paths (e.g., an if-else where some threads take the 'if' branch and others take the 'else'). The warp serialises the divergent paths, halving (or worse) the effective throughput. Performance-oriented GPU programming minimises warp divergence by organising data so that adjacent threads take the same path.

**Memory coalescing** is the other critical performance consideration: when adjacent threads access adjacent memory locations, the GPU can combine the accesses into a single large transaction. When threads access random, unrelated locations, each access requires a separate transaction — wasting memory bandwidth. Matrix multiplication libraries (cuBLAS) and deep learning frameworks (PyTorch, TensorFlow) are heavily optimised for coalesced access.

**CPU-GPU interaction** is the fundamental bottleneck of heterogeneous computing. Data must be transferred across the PCIe bus (or, for NVIDIA's Grace-Hopper, the NVLink-C2C interconnect) — a transfer that is orders of magnitude slower than GPU computation. **Zero-copy** and **unified memory** (CUDA 6, 2013) simplify programming by allowing the GPU to page data from CPU memory on demand, at the cost of unpredictable latency.

**Required Reading:**
- David B. Kirk & Wen-mei W. Hwu, *Programming Massively Parallel Processors: A Hands-on Approach* (3rd ed., Morgan Kaufmann, 2017/2042)
- NVIDIA CUDA C++ Programming Guide (docs.nvidia.com, continuously updated)
- Shane Cook, *CUDA Programming: A Developer's Guide* (Morgan Kaufmann, 2012)
- UoY GPU Computing Lab: Write and profile a simple matrix multiplication kernel with CUDA (2040)

**Discussion Questions:**
1. GPU cores run at lower clock speeds (~1.5 GHz) than CPU cores (~4 GHz). Why are GPUs still more efficient for parallel workloads — and at what point does the advantage diminish?
2. Shared memory on GPUs is limited (up to 228 KB per SM). How do you design algorithms that maximise shared-memory utilisation — and what are the techniques for tiling?
3. Warp divergence reduces throughput by serialising divergent paths. How do you detect warp divergence in a CUDA program — and what algorithmic restructuring avoids it?

---

## Lecture 5: Message Passing and the Distributed Systems Mindset

Distributed systems are those in which the failure of a computer you didn't even know existed can render your own computer unusable (Lamport's wry definition). In a distributed system, multiple independent computers (nodes) communicate by passing messages over a network. There is no shared memory, no shared clock, and no guarantee of reliable communication.

**The fallacies of distributed computing** (Peter Deutsch, 1994) are the assumptions that beginners make and experienced practitioners avoid:
1. The network is reliable.
2. Latency is zero.
3. Bandwidth is infinite.
4. The network is secure.
5. Topology doesn't change.
6. There is one administrator.
7. Transport cost is zero.
8. The network is homogeneous.

Every fallacy has bitten someone in production. The first falsity — the network is reliable — accounts for the most surprising and difficult-to-debug failures. A network partition (some nodes cannot reach others) can happen at any time, for any duration. The distinguishing fact of distributed systems programming is that you must design for the case where any message may be lost, duplicated, reordered, or delayed.

**The Message Passing Interface (MPI)** is the dominant communication library for high-performance computing (HPC). MPI defines point-to-point operations (`MPI_Send`, `MPI_Recv`) and collective operations (`MPI_Bcast`, `MPI_Reduce`, `MPI_Allreduce`). MPI programs follow the **single-program multiple-data (SPMD)** model: all nodes run the same program, but each node has a unique rank (0 to N−1) and operates on its portion of the data.

For distributed web services, **message queues** (Kafka, RabbitMQ, NATS) and **RPC frameworks** (gRPC, Thrift, Cap'n Proto) abstract away the details of network communication. gRPC uses Protocol Buffers for serialisation and HTTP/2 for transport, supporting streaming requests and responses, bidirectional streaming, and flow control. The interface is defined in a `.proto` file, from which gRPC generates client and server code in 11 languages.

**Required Reading:**
- Andrew S. Tanenbaum & Maarten van Steen, *Distributed Systems: Principles and Paradigms* (3rd ed., Pearson, 2017/2042), chs. 1–3
- Aron Deutsch, "The Eight Fallacies of Distributed Computing" (Sun Microsystems, 1994)
- William Gropp, Ewing Lusk & Anthony Skjellum, *Using MPI: Portable Parallel Programming with the Message-Passing Interface* (3rd ed., MIT Press, 2014/2042)
- UoY Distributed Systems Lab: Build a simple key-value store with gRPC (2040)

**Discussion Questions:**
1. The eight fallacies are well-known, yet distributed systems continue to fail in ways that trace back to these assumptions. What is the most common fallacy observed in production incidents — and why is it so hard to internalise?
2. MPI's `MPI_Bcast` is a collective operation — all processes participate. What happens if one process fails during a collective — and how does MPI manage failure?
3. gRPC uses HTTP/2 as its transport layer. What benefits does HTTP/2 provide over raw TCP sockets for RPC — and what are the costs in complexity and latency?

---

## Lecture 6: Time and Order in Distributed Systems

In a distributed system, there is no global clock. Each node has its own clock (drifting at a different rate from every other node), and messages take an unknown time to propagate. Establishing *order* in such a system is the foundational challenge.

**Lamport timestamps** (Leslie Lamport, 1978) provide a partial order (the happens-before relation, generalised from the shared-memory setting): if a message is sent before it is received, the send event happens-before the receive event. A Lamport clock is a monotonically increasing integer that each node maintains: increment on each event, send the current clock value with each message, and the receiver sets its clock to max(local, received)+1. Lamport clocks capture the causal order: if a happens-before b, then L(a) < L(b). However, L(a) < L(b) does NOT imply a happens-before b — Lamport clocks cannot detect concurrent events.

**Vector clocks** (Mattern, 1989; Fidge, 1988) extend Lamport clocks to detect concurrency. Each node maintains a vector of all nodes' clock values. If V₁ ≤ V₂ (componentwise), then event 1 happens-before event 2. If V₁ and V₂ are incomparable (some components larger, some smaller), the events are concurrent. Vector clocks are the gold standard for causal order, but they have a storage cost: O(N) per event, where N is the number of nodes — a significant burden for large systems.

**The physical clock problem** is even harder. Network Time Protocol (NTP) synchronises clocks to within 10 ms on a LAN and 50 ms on the WAN — good enough for most applications but not for causality. The **true time** approach (Google Spanner) uses GPS clocks and atomic clocks to provide genuine bounds on clock uncertainty with the **TrueTime API**: `TT.now()` returns an interval [earliest, latest] that is guaranteed to contain the actual time. Spanner uses TrueTime to provide **external consistency**: commits appear globally in timestamp order, enabling consistent snapshot reads across data centres without locking.

**Required Reading:**
- Leslie Lamport, "Time, Clocks, and the Ordering of Events in a Distributed System" (*Communications of the ACM* 21:7, 1978): 558–565
- Colin J. Fidge, "Timestamps in Message-Passing Systems That Preserve the Partial Ordering" (*Proceedings of the 11th Australian Computer Science Conference*, 1988): 56–66
- Friedemann Mattern, "Virtual Time and Global States of Distributed Systems" (*Parallel and Distributed Algorithms*, 1989)
- James C. Corbett et al., "Spanner: Google's Globally-Distributed Database" (*OSDI*, 2012) — TrueTime and external consistency
- UoY Vector Clock Lab: Implement the vector clock protocol in Go (2040)

**Discussion Questions:**
1. Lamport clocks give a total order that respects causality, but the total order is not unique (different observers may assign different total orders to concurrent events). Under what circumstances does this ambiguity cause correctness problems?
2. Vector clocks track causality precisely but require O(N) storage. For a system with 10,000 nodes, is this affordable — and what approximations exist?
3. Spanner's TrueTime API provides uncertainty-bounded physical time. How does the uncertainty bound affect the throughput of Spanner's commit protocol — and how would you minimise the bound?

---

## Lecture 7: Consensus and the FLP Impossibility

Consensus — making a group of distributed processes agree on a value — is the most fundamental and most challenging problem in distributed computing. Every replicated service, every distributed database, every fault-tolerant protocol ultimately reduces to a consensus problem.

The **FLP impossibility result** (Fischer, Lynch & Paterson, 1985) is the foundational theorem of distributed computing: in an *asynchronous* system (no bounds on message delay or process speed), no deterministic algorithm can guarantee consensus in the presence of even a single crash failure. The proof proceeds by arguing that any consensus algorithm can be forced into a **bivalent state** (both "decide 0" and "decide 1" are possible) — and that any step from a bivalent state either remains bivalent or is reachable only by two different decisions, leading to an infinite loop of indecision.

FLP is a theorem about impossibility, not practicality. Real systems circumvent FLP in several ways:
- **Failure detectors** (Chandra & Toueg, 1996): An **eventually perfect failure detector** (⋄P) provides the ability to detect failures with a finite, but unknown, bound on the detection time. With a failure detector, consensus becomes solvable.
- **Randomised consensus** (Ben-Or, 1983): Use randomness to break symmetry. Each round, a process proposes a value and runs a coin flip; if the coin is "heads," it adopts a default value; if "tails," it keeps proposing. Randomised consensus terminates with probability 1.
- **Partial synchrony** (Dwork, Lynch & Stockmeyer, 1988): Assume that the system is eventually synchronous — after an unknown global stabilisation time (GST), all message delays are bounded and all clocks are synchronised. In the "eventually synchronous" model, consensus is solvable (this is the model used by Paxos and Raft).

**Paxos** (Lamport, 1998) is the first practical consensus algorithm. It operates in three phases:
1. **Prepare:** The proposer chooses a unique proposal number N and sends a `prepare(N)` request to a majority of acceptors.
2. **Promise:** If an acceptor has not seen a proposal with number ≥ N, it promises to never accept any proposal with number < N, and returns the highest-numbered proposal it has accepted (if any).
3. **Accept:** The proposer sends an `accept(N, value)` to a majority of acceptors. If a majority accepts, the value is **chosen** (consensus reached).

Paxos is notoriously difficult to understand. Lamport's first paper was written as a parable about an ancient Greek parliament (The Part-Time Parliament) — a narrative so charming that readers missed the algorithm. Practical implementations (Chubby, Zookeeper's Zab) use a simplified variant (Mencius, Multi-Paxos) that amortises the prepare phase across multiple submissions.

**Required Reading:**
- Michael J. Fischer, Nancy A. Lynch & Michael S. Paterson, "Impossibility of Distributed Consensus with One Faulty Process" (*Journal of the ACM* 32:2, 1985): 374–382
- Leslie Lamport, "The Part-Time Parliament" (*ACM Transactions on Computer Systems* 16:2, 1998): 133–169 — Paxos
- Tushar D. Chandra & Sam Toueg, "Unreliable Failure Detectors for Reliable Distributed Systems" (*Journal of the ACM* 43:2, 1996): 225–267
- Leslie Lamport, "Paxos Made Simple" (*ACM SIGACT News* 32:4, 2001): 18–25 — the clearest Paxos explanation
- UoY Consensus Lab: Implement a simple consensus simulator in Go (2040)

**Discussion Questions:**
1. FLP shows that consensus is impossible in a purely asynchronous model with even one failure. Yet real systems reach consensus billions of times a day. How do real systems circumvent FLP — and are there conditions under which a real system *will* fail to reach consensus?
2. Paxos requires phases, each of which requires a majority. If a majority is lost (network partition), Paxos stops. How does Multi-Paxos (or Raft) handle leader election after a partition heals?
3. Randomised consensus terminates with probability 1, but the expected time can be large. Under what conditions would a randomised consensus be preferred over Paxos/Raft?

---

## Lecture 8: Raft — A Understandable Consensus Algorithm

**Raft** (Diego Ongaro & John Ousterhout, 2014) was designed with a single goal: "understandability." The authors observed that Paxos was correct but inscrutable — no student could implement it correctly without studying dozens of edge cases. Raft breaks consensus into three independently comprehensible pieces:

1. **Leader election:** A new leader is chosen when the existing leader fails. An election is triggered by an election timeout. Nodes vote for the candidate with the highest term number and the most recent log entry. The candidate wins if it receives a majority of votes. If no candidate wins (split vote), a new election is held after a random timeout.
2. **Log replication:** The leader receives client requests, appends them to its log as entries, and issues `AppendEntries` RPCs to followers. A majority of followers must acknowledge the entry before it is committed (applied to the state machine). The leader keeps track of the highest committed index and propagates it to followers.
3. **Safety:** The leader never overwrites committed entries (the leader completeness property: a leader must have all committed entries). Log matching ensures that if two logs contain the same entry at the same index, they are identical up to that index. If followers' logs diverge from the leader's log (network partition during a previous leader's term), the leader forces its log on the followers.

Raft's advantage over Paxos is not algorithmic (they are equivalent in expressiveness) but pedagogical. Raft's decomposition into independent modules, its concreteness (specific timeouts, specific RPCs, specific log structures), and its careful handling of the leader election edge case have made it the consensus algorithm of choice for systems like etcd (Kubernetes), Consul, and TiKV.

**The Raft security guarantee** is the most subtle part of the algorithm: the leader's log is always complete. This guarantee is enforced by the voting procedure: a candidate that lacks some committed entries cannot become leader because it cannot secure a majority (at least one node in any majority will have the committed entries and will refuse to vote for the candidate). The guarantee depends on exactly one invariant: election safety (at most one leader per term).

**Required Reading:**
- Diego Ongaro & John Ousterhout, "In Search of an Understandable Consensus Algorithm" (*USENIX ATC*, 2014) — the Raft paper
- Diego Ongaro, "Consensus: Bridging Theory and Practice" (PhD thesis, Stanford, 2014) — the full Raft specification
- Martin Kleppmann, *Designing Data-Intensive Applications* (O'Reilly, 2017), ch. 9 (Consensus)
- Raft Visualisation (raft.github.io) — interactive Raft simulation
- UoY Raft Lab: Implement Raft's leader election and log replication in Go or Rust (2040)

**Discussion Questions:**
1. Raft's leader election uses random timeouts (150–300 ms on a LAN). How would you tune these timeouts for a WAN deployment (round-trip 80 ms) vs a LAN deployment (round-trip 0.5 ms)?
2. When a new leader in Raft takes over and forces its log on followers, some uncommitted entries from the old leader may be discarded. What happens if a client is told that an entry is committed, but the entry is later discarded by the new leader — and how does Raft prevent this?
3. Raft's safety depends on the fact that a candidate missing committed entries cannot win an election. Is this guarantee ever vulnerable to timing or partial connectivity?

---

## Lecture 9: The CAP Theorem and Distributed Data

The **CAP theorem** (Eric Brewer, 2000; proven by Gilber & Lynch, 2002) states that a distributed data store can provide at most two of three properties simultaneously:
- **Consistency:** Every read returns the most recent write (linearisability).
- **Availability:** Every request eventually receives a response (not an error).
- **Partition tolerance:** The system continues to function despite network partitions (messages being lost or delayed).

Brewer's insight was not that partitions are rare — they are inevitable — so the real choice is between **CP** (sacrifice availability during partitions) and **AP** (sacrifice consistency during partitions). *Availability* in CAP is not the same as "uptime" — it means every node that is reachable continues to serve requests, even during a partition.

**Consistency models** span a spectrum:
- **Strict consistency (linearisability):** Operations appear instantaneous and ordered. The strongest model; impossible to achieve at Internet scale without sacrificing availability (CAP).
- **Sequential consistency:** Operations from each thread appear in program order, but the interleaving across threads is unspecified. Stronger than causal, weaker than linearisable.
- **Causal consistency:** Writes that are causally related are seen in the correct order. Writes that are concurrent may be seen in any order. Sufficient for many applications (e.g., social feeds).
- **Eventual consistency:** Given enough time without new updates, all replicas converge to the same state. The weakest model; widely used in CDNs and DNS.

**CRDTs (Conflict-free Replicated Data Types)** automatically resolve conflicts at the data-structure level without requiring consensus. A CRDT (Shapiro et al., 2011) is a data structure whose operations commute — in any order, applied to any starting state, they produce the same final state. Examples:
- **G-Counter (grow-only counter):** Each replica has its own count; the total is the sum across replicas.
- **PN-Counter (positive-negative counter):** Two G-counters, one for increments and one for decrements.
- **G-Set (grow-only set):** Add elements; the set is the union across replicas.
- **LWW-Register (last-writer-wins register):** Each write is timestamped; the register has the value from the latest timestamp.

**Required Reading:**
- Eric A. Brewer, "Towards Robust Distributed Systems" (*PODC*, 2000) — the CAP theorem keynote
- Seth Gilbert & Nancy A. Lynch, "Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services" (*ACM SIGACT News* 33:2, 2002): 51–59
- Martin Kleppmann, *Designing Data-Intensive Applications* (O'Reilly, 2017), ch. 9 — trade-offs between consistency models
- Marc Shapiro, Nuno Preguiça, Carlos Baquero & Marek Zawirski, "Conflict-Free Replicated Data Types" (*SSS*, 2011): 386–400
- UoY CRDT Lab: Build a collaborative text editor using CRDTs (2040)

**Discussion Questions:**
1. The CAP theorem does not say "choose 2 of 3." It says "when the network is partitioned, choose C or A." What happens during normal operation (no partition) — can the system be both C and A?
2. Eventual consistency is the weakest model. How long must a system wait before it is "eventually consistent" — and what is the bound on the inconsistency window?
3. CRDTs provide automatic conflict resolution, but the semantics can be unnatural (LWW-Register discards concurrent writes). How do you design application-layer conflict resolution (e.g., "last writer wins" is often wrong for collaborative editing) on top of CRDTs?

---

## Lecture 10: Distributed Transactions and Isolation

Transactions — groups of operations that execute atomically — are the fundamental abstraction for data integrity. In a distributed system, transactions span multiple nodes, adding the complexity of **atomic commit** (all nodes commit or all abort) and **distributed isolation** (concurrent transactions should not interfere).

**Two-phase commit (2PC)** is the classical atomic commit protocol:
1. **Vote phase:** The coordinator sends `prepare` to all participants. Each participant votes YES (can commit) or NO (must abort).
2. **Commit phase:** If all votes are YES, the coordinator sends `commit`; otherwise, `abort`.

2PC is a **blocking protocol**: if the coordinator crashes after the PREPARE phase but before the COMMIT phase, participants hold locks and resources until the coordinator recovers. This is the **blocking problem** — 2PC violates availability because a single failure can cause indefinite blocking. **Three-phase commit (3PC)** avoids blocking by adding a pre-commit phase, but it requires that network partitions are detectable (a strong assumption in practice).

**The isolation levels** (ANSI SQL, 1992) define how concurrent transactions interact:
- **Read uncommitted:** A transaction can see another transaction's uncommitted writes (dirty reads). Loses ACID.
- **Read committed:** A transaction sees only committed writes. Prevents dirty reads but allows non-repeatable reads (a read returns different values if repeated) and phantom reads (a query returns different rows if repeated).
- **Repeatable read:** A transaction sees the same values for rows it has read (snapshot isolation). Prevents non-repeatable reads but allows phantoms.
- **Serializable:** Transactions execute as if they ran one at a time. The strongest level, preventing all anomalies.

**Snapshot isolation** (Berenson et al., 1995) is the most common isolation level in modern databases (PostgreSQL, Oracle, MySQL with InnoDB). Each transaction reads from a consistent snapshot (a version of the database as of the transaction's start time). Writes are validated before commit: if two concurrent transactions write to the same row, the later one aborts (first-committer-wins). Snapshot isolation prevents dirty reads, non-repeatable reads, and phantoms, but it allows **write skew** — a class of anomalies where two transactions read overlapping state and write conflicting updates, each unaware of the other, producing a database state that no serial execution could produce.

**Required Reading:**
- Jim Gray & Andreas Reuter, *Transaction Processing: Concepts and Techniques* (Morgan Kaufmann, 1993), chs. 7–10 — the standard reference
- Hal Berenson et al., "A Critique of ANSI SQL Isolation Levels" (*SIGMOD*, 1995): 1–10 — snapshot isolation and its anomalies
- Michael Stonebraker, "The Case for Shared Nothing" (*Database Engineering Bulletin* 9:1, 1986): 4–9 — the architecture of distributed databases
- Pat Helland, "Life Beyond Distributed Transactions: An Apostate's Opinion" (*CIDR*, 2007) — the case against distributed transactions
- UoY Distributed Transactions Lab: Implement a simple distributed transaction coordinator (2040)

**Discussion Questions:**
1. Two-phase commit blocks indefinitely if the coordinator fails. In practice, how long can a 2PC "prepared" transaction hold resources — and what timeout mechanisms are safe?
2. Snapshot isolation prevents most anomalies but allows write skew. Can you construct a scenario where write skew leads to data corruption — and how would you prevent it without using serialisable isolation?
3. Helland's "Apostate's Opinion" argues that distributed transactions are infeasible at Internet scale. What alternatives (sagas, compensating transactions, event sourcing) do large-scale systems use — and what are their trade-offs?

---

## Lecture 11: Distributed Storage — From GFS to DynamoDB

Distributed storage systems are the infrastructure underpinning modern cloud computing. They must handle petabytes of data across thousands of machines, tolerate frequent failures, and provide useful guarantees to applications.

**The Google File System (GFS)** (Ghemawat, Gobioff & Leung, 2003) was the foundational distributed storage system that enabled Google's search index to scale to exabytes of data. GFS splits files into 64 MB chunks, replicates each chunk across three machines, and uses a single master to store metadata. The master is a single point of failure — a limitation that Google addressed in **Colossus** (GFSv2) by distributing the metadata across a Paxos cluster.

**Bigtable** (Chang et al., 2006) was the first distributed key-value/columnar storage system. It organises data into tables with row keys, column families, and timestamps (each cell can have multiple versions). Bigtable uses GFS for storage and Chubby (Paxos) for coordination. Bigtable was the foundation for Google's indexing system, Google Earth, Google Analytics, and Google Books.

**Amazon DynamoDB** (DeCandia et al., 2007) took the opposite design point: an **eventually consistent**, **always available** key-value store built on the **Dynamo architecture**. Dynamo sacrifices consistency for availability — a design captured by the CAP theorem. Key features:
- **Consistent hashing:** Data is partitioned across nodes using consistent hashing (Karger et al., 1997), minimising data movement when nodes join or leave.
- **Vector clocks for causal ordering:** Concurrent updates are reconciled using vector clocks (or discarded, with application-level conflict resolution).
- **Gossip-based membership:** Nodes learn about other nodes through periodic gossip (Epidemic protocols, Demers et al., 1987).

**DynamoDB** (2012) is Amazon's managed version of Dynamo, with additional features: secondary indexes, streams (change data capture), global tables (multi-region replication), and transactions (2018). DynamoDB is the most popular NoSQL database at Amazon, serving millions of requests per second for Alexa, Amazon.com's shopping cart, and AWS services.

**Required Reading:**
- Sanjay Ghemawat, Howard Gobioff & Shun-Tak Leung, "The Google File System" (*SOSP*, 2003)
- Fay Chang et al., "Bigtable: A Distributed Storage System for Structured Data" (*OSDI*, 2006)
- Giuseppe DeCandia et al., "Dynamo: Amazon's Highly Available Key-Value Store" (*SOSP*, 2007)
- Ion Stoica et al., "A Scalable, Decentralized Storage System for Structured Data" — the Chord DHT (David Karger et al., "Consistent Hashing and Random Trees", 1997)
- UoY Distributed Storage Lab: Build a consistent-hashing key-value store in Go (2040)

**Discussion Questions:**
1. GFS's single-master design is a bottleneck and a single point of failure. How did Google improve on this design with Colossus — and what are the trade-offs of a fully distributed metadata system?
2. Dynamo uses "sloppy quorums" and "hinted handoff" to maintain availability during node failures. What happens to consistency during sloppy quorum operations — and how does Dynamo restore it after the failure is repaired?
3. Consistent hashing distributes keys across nodes with minimal rebalancing when the cluster changes. What is the cost of this minimal rebalancing — how unbalanced can the key distribution become, and what techniques (virtual nodes, load-based partitioning) address this?

---

## Lecture 12: The Future of Parallel and Distributed Computing

By 2040, parallel and distributed computing has transformed every layer of the stack — from the chip (hundreds of cores, specialised accelerators, non-volatile memory) to the architecture (disaggregated storage, composable infrastructure, serverless computing) to the applications (distributed AI training, real-time stream processing, global-scale databases). The trajectory raises challenging questions about performance, programmability, and correctness.

**Hardware trends:** The end of Dennard scaling has not stopped innovation. Chiplets (small dies connected by advanced packaging) enable heterogeneous systems with hundreds of cores, GPUs, FPGAs, and custom accelerators (TPUs, IPUs, NPUs). The **memory wall** (the growing gap between processor and memory speed) is the dominant performance bottleneck, driving the adoption of **Compute Express Link (CXL)** for cache-coherent memory sharing across sockets and **non-volatile memory** (Intel Optane, Samsung Z-SSD) for large-scale persistent memory.

**The rise of serverless:** Functions-as-a-Service (AWS Lambda, Google Cloud Functions) abstract away the server entirely. The programmer writes a function; the platform takes care of scaling, fault tolerance, and resource management. Serverless simplifies deployment but introduces challenges: cold starts (the delay when a new instance is allocated), state management (functions are stateless by design), and cost unpredictability (bursty workloads can be expensive).

**Distributed training of AI models:** The largest neural networks (GPT-4 scale: 10¹²–10¹⁴ parameters) require training across thousands of GPUs for months. **Data parallelism** (each GPU processes a batch and synchronises gradients via all-reduce) and **model parallelism** (layers of the model are split across GPUs, each layer communicates activations to the next) are the two dominant paradigms. The **Megatron-LM** framework (NVIDIA) uses a combination of both, achieving near-linear scaling on 1024 GPUs.

**The correctness challenge:** As systems grow more complex, the probability of subtle concurrency bugs approaches certainty. The programming languages of the future (Rust, Go, OCaml, and the emerging **Verus** — Rust with formal verification) are designed with concurrency correctness as a primary goal: Rust's ownership system prevents data races at compile time; Go's channels provide structured concurrency; and formal verification of concurrent programs (using TLA+, Ivy, or Verus) is becoming practical for safety-critical systems.

**Required Reading:**
- Luiz André Barroso, Urs Hölzle & Parthasarathy Ranganathan, *The Datacenter as a Computer: Designing Warehouse-Scale Machines* (3rd ed., Morgan & Claypool, 2019/2041)
- Jonas Bonér, *Reactive Microservices Architecture* (O'Reilly, 2016)
- Mohammad Shoeybi et al., "Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism" (arXiv:1909.08053, 2019)
- Steve Klabnik & Carol Nichols, *The Rust Programming Language* (2nd ed., No Starch Press, 2023/2040), ch. 16 — fearless concurrency
- UoY Distributed Systems Capstone: Build a distributed key-value store from scratch (2040)

**Discussion Questions:**
1. Serverless computing promises "just deploy a function" — but the state management, cold starts, and orchestration overhead complicate the picture. For what class of applications is serverless truly a simplification?
2. Training 10¹⁴ parameter models requires parallelism across thousands of GPUs. What are the fundamental limits to scaling distributed training — Amdahl's law in gradient synchronisation, the bandwidth wall of all-reduce, or something else?
3. Rust's ownership system eliminates data races at compile time. If all new systems software were written in Rust, would the distributed computing research agenda change — and how?

---

## Final Examination Preparation

The final examination assesses your ability to design, analyse, and implement parallel and distributed systems — from multithreaded shared-memory programs through GPU kernels to fault-tolerant distributed consensus algorithms.

**Sample Essay Questions (Choose 4 of 8):**

1. **The Free Lunch and Its Aftermath.** Trace the trajectory from Dennard scaling (1985–2005) through the multicore pivot to the heterogeneous architectures of 2040. What does this imply for the future of software — and how should computer science education adapt?

2. **Happens-Before and Your Program.** Explain the happens-before relation, the memory model of C++ (or Java), and the guarantees that a programmer can rely on. Write a small concurrent program with a subtle data race and explain how to fix it, demonstrating both mutex-based and atomic-based solutions.

3. **Consensus: Theory and Practice.** Explain the FLP impossibility result and the reasons it does not prevent real systems from reaching consensus. Compare Paxos and Raft along the dimensions of understandability, safety, liveness, and performance under failure. Under what conditions would you choose one over the other?

4. **CAP in Practice.** A social-media company is designing a global feed service. Choose a point on the CAP trade-off spectrum and justify your choice. Explain the consistency model you would implement (causal? eventual? strong?), the replication strategy (leader-follower? multi-master?), and the conflict-resolution mechanism (CRDT? last-writer-wins? application-defined?).

5. **The GPU Revolution.** Describe the CUDA programming model (grids, blocks, warps, shared memory). Explain the performance factors (warp divergence, memory coalescing, occupancy) and how they interact. For what computational patterns is GPU parallelism unsuitable — and why?

6. **Distributed Transactions: Alive or Dead?** Debate the proposition: "Distributed transactions are the only correct way to maintain data integrity in a distributed system" and the counter-proposition: "Distributed transactions are too expensive and fragile — use saga patterns and compensating transactions instead." Provide concrete examples and cite the relevant papers.

7. **Design a Distributed Hash Table.** Design a distributed hash table (DHT) using consistent hashing, with replication, failure detection, and data migration. Explain your design choices for: replication factor, quorum sizes (write R, read W), failure detection mechanism, and data migration strategy. Analyse the behaviour under node additions and failures.

8. **The Future of Distributed Computing.** In 2040, what are the most important unsolved problems in distributed computing? Speculate on the impact of quantum networking, ultra-low-latency interconnects (CXL, NVLink), and AI-driven resource management. Will distributed systems become easier or harder to build correctly?

**Practical Project Option:** Implement a distributed key-value store from scratch. Your system must support (1) client get/put operations with at least two nodes, (2) partition-tolerant replication (either leader-follower or multi-master), (3) a failure detection mechanism, and (4) a protocol for rebalancing when nodes join or leave. Write your implementation in Rust, Go, or C++. Your report must analyse the correctness (does your system meet its consistency guarantees?) and performance (latency, throughput, scaling behaviour) of your implementation.
