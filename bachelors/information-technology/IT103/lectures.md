# IT103: Operating Systems for IT Professionals
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4  
**Prerequisites:** IT101  
**Description:** An intensive, practitioner-focused exploration of operating system internals as they apply to information technology operations. Students master process and memory management, file systems, I/O subsystems, security isolation mechanisms, and kernel debugging on both Linux and Windows Server. The course emphasises hands-on competence: every student manages a bare-metal server, debugs kernel behaviour, tunes performance under load, and implements security hardening. By the end, students can diagnose why a system is slow, secure it against common attacks, and explain their reasoning with precision.

**Instructor:** Prof. Björn Hrafnkelsson, Department of Information Technology  
**Lab:** YggLab Systems Studio, Muninn Computing Centre, Basement Level  
**Office Hours:** Tuesdays and Thursdays, 14:00-16:00 UTC

---

## Lectures

ᚠ **Lecture 1: The OS as the IT Professional's Domain**

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

This lecture establishes the operating system as the primary domain of the IT professional. Where developers interact with the OS through APIs and abstractions, IT professionals must understand the OS from the kernel upward: how it schedules processes, manages memory, handles I/O, enforces security, and exposes resources to users and applications. The lecture introduces the two dominant server operating systems of 2040 — Linux (in its myriad distributions) and Windows Server — and sets the expectation that every student will achieve fluency in both by semester's end.

### Key Topics

- **The OS as Abstraction and Reality:** The operating system abstracts hardware (CPU, memory, disk, network) into resources that programs can use. But for the IT professional, the abstraction is not opaque: when performance degrades, when security is breached, or when hardware fails, the professional must peer beneath the abstraction to understand what is really happening. The lecture introduces the dual perspective: the OS is both the interface that enables productivity and the mechanism that must be diagnosed, tuned, and secured.
- **Linux in 2040:** Linux dominates server infrastructure with 78% market share. The lecture covers the distribution landscape: enterprise (RHEL, SUSE Linux Enterprise Server, Ubuntu Pro), community (Debian, Fedora, Arch), and security-focused (YggdrasilOS, Qubes OS). The 2040 additions: immutable distributions (Fedora Silverblue, openSUSE MicroOS) where the base system is read-only and updates are atomic, and container-optimised distributions (Flatcar Container Linux, Bottlerocket) designed solely to run containers.
- **Windows Server in 2040:** Windows Server 2040 remains essential in enterprise environments with Active Directory, legacy .NET applications, and hybrid cloud integration. The lecture covers: Windows Server Core (minimal footprint, no GUI), Nano Server (container-only, even smaller), and Windows Subsystem for Linux (WSL) as the bridge technology that allows Linux tools on Windows. The 2040 reality: most enterprise IT environments are heterogeneous, requiring professionals to manage both Linux and Windows seamlessly.
- **The Unix Philosophy and Its 2040 Descendants:** The original Unix philosophy (small, composable tools; text streams as the universal interface; everything is a file) and how it manifests in modern Linux. The lecture contrasts this with Windows' object-oriented approach (PowerShell pipelines objects, not text) and discusses the strengths of each paradigm.
- **Course Laboratory Overview:** Each student is assigned a bare-metal server (Dell PowerEdge or HPE ProLiant, 16 cores, 64GB RAM, 2x 1TB NVMe) running both Linux (dual-boot or virtualised) and Windows Server (VM). The server is the student's responsibility: they install, configure, break, fix, and tune it throughout the course. The lecture concludes with the lab safety briefing: "Your server is yours to destroy. Destroy it, learn from it, rebuild it."

### Lecture Notes

The operating system is the IT professional's native territory. A developer may go years without understanding virtual memory; an IT professional cannot go a day. The sysadmin who receives a 3 AM alert about high load must immediately know whether the issue is CPU-bound (run queue), memory-bound (swapping), I/O-bound (disk wait), or network-bound (bandwidth saturation). This requires deep OS literacy.

Linux distributions in 2040 have fragmented into specialised variants. The enterprise distributions (RHEL, SLES, Ubuntu Pro) offer long-term support, security certifications, and vendor backing — essential for regulated industries. The immutable distributions represent a philosophical shift: rather than patching a running system, you replace the entire OS image atomically. If the new image fails, you roll back to the previous one. This eliminates an entire class of configuration drift issues but requires new operational workflows.

Windows Server's evolution reflects the same trend toward minimalism. Windows Server Core removes the GUI, reducing attack surface and resource consumption. Nano Server is even smaller, designed exclusively for container workloads. The 2040 Windows administrator manages servers primarily through PowerShell and Desired State Configuration (DSC), with GUI tools used only when absolutely necessary. WSL has blurred the Linux/Windows boundary to the point that many administrators use the same Bash and Python scripts on both platforms.

The laboratory component is the heart of this course. Textbook knowledge of memory management is inert until you have watched `vmstat 1` during a memory pressure event and seen the page fault rate spike. Theoretical understanding of file systems becomes visceral when you have accidentally corrupted a partition table and recovered it using `testdisk`. The IT professional's knowledge is embodied: it lives in their fingers, not just their minds.

### Required Reading

- Arpaci-Dusseau, R.H. & Arpaci-Dusseau, A.C. (2028). *Operating Systems: Three Easy Pieces*, 2nd Edition. Arpaci-Dusseau Books. Chapters 1-2.
- Love, R. (2033). *Linux Kernel Development*, 4th Edition. Addison-Wesley. Chapter 1.
- Russinovich, M.E., Solomon, D.A., & Ionescu, A. (2031). *Windows Internals*, 8th Edition. Microsoft Press. Part 1, Chapter 1.
- Yggdrasil Systems Lab Manual (2040). "Bare-Metal Server Setup and Safety Procedures."

### Discussion Questions

1. Compare the Unix text-stream philosophy with PowerShell's object pipeline. For an IT automation task (e.g., finding all stopped services and starting them), which approach produces more robust, maintainable code?
2. Immutable operating systems promise reduced configuration drift but require replacing the entire OS image for updates. What operational challenges does this create for organisations with complex custom configurations?
3. The Norse *húskarl* (household warrior) was responsible for the physical security of the longhouse and the wellbeing of its inhabitants. How does this protective, stewardship-oriented role inform the IT professional's relationship with the operating systems under their care?

---

ᚢ **Lecture 2: Process and Thread Management**

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

Processes are the fundamental unit of execution, and understanding their lifecycle, scheduling, and intercommunication is essential for IT operations. This lecture covers process creation (fork-exec on Linux, CreateProcess on Windows), thread models, scheduling algorithms, and the practical tools used to observe and manage processes in production environments. The hands-on component includes tracing process creation with `strace`, monitoring thread pools, and diagnosing runaway processes.

### Key Topics

- **Process Concepts:** A process as an instance of a running program, with its own address space, open files, and execution state. The process control block (PCB) and its contents. The five-state process model (new, ready, running, waiting, terminated) and the transitions between states. The lecture covers zombie processes (completed but not reaped by parent) and orphan processes (parent terminated before child), with practical cleanup techniques.
- **Process Creation:** The fork-exec model in Linux (copy-on-write semantics, `fork()`, `execve()`, `waitpid()`, `exit()`). The lecture includes a step-by-step walkthrough of what happens when you type a command in a shell: fork, exec, wait, and the return of control. On Windows: `CreateProcess`, `TerminateProcess`, job objects for process grouping, and the Windows Subsystem for Linux implementation of fork.
- **Threads and Concurrency:** Threads as lightweight execution contexts within a process. User-level threads (green threads, coroutines) versus kernel-level threads (1:1 threading model). The lecture covers thread pools (why creating a thread per request does not scale), thread-local storage, and the 2040 reality where async/await and structured concurrency have reduced the need for manual thread management in applications — but the OS still schedules kernel threads.
- **Scheduling Algorithms:** The Completely Fair Scheduler (CFS) in Linux (virtual runtime, red-black tree of runnable tasks, priority weighting) and the Windows thread scheduler (priority classes, time quantum, dynamic priority boosts). The lecture covers: real-time scheduling (SCHED_FIFO, SCHED_RR) and its dangers (a runaway real-time process can freeze the system), nice values and priority ranges, and CPU affinity (pinning processes to specific cores for cache locality or isolation).
- **Inter-Process Communication (IPC):** Pipes (anonymous and named), message queues, shared memory, semaphores, signals, sockets, and the 2040 additions: D-Bus for desktop and service communication, and gRPC for microservice IPC. The lecture covers the performance implications: shared memory is fastest but requires synchronisation; sockets are slower but provide natural isolation.
- **Practical Tools:** `ps`, `top`, `htop`, `pidstat` for process monitoring; `strace` (Linux) and Process Monitor (Windows) for system call tracing; `lsof` for open file inspection; `pstree` for process hierarchy visualization. The hands-on lab: trace the system calls made by `ls`, identify each call's purpose, and explain what would happen if a call failed.

### Lecture Notes

Process management is where the theoretical OS concepts become immediately practical. When a web server stops responding, the first diagnostic step is usually `ps` or `top`: is the process running? Is it consuming CPU? Is it blocked in I/O wait? Is the run queue saturated with runnable processes? These questions map directly to OS concepts.

The fork-exec model, inherited from UNIX in the 1970s, remains the foundation of Linux process creation. When a process forks, the OS creates a new PCB and duplicates the parent's address space — but modern systems use copy-on-write (COW), where pages are shared read-only until either process writes to them. This optimisation is critical: without COW, forking a large process (like a database server with 32GB of mapped memory) would require copying 32GB, taking seconds. With COW, the fork completes in microseconds. IT professionals must understand COW because it affects memory accounting: a process may appear to use 32GB of memory (RSS) but share most of it with its parent, making the actual marginal memory cost much smaller.

Scheduling is the OS function that most directly affects perceived performance. The CFS scheduler in Linux aims to give every runnable task a "fair" share of CPU time, weighted by priority. But "fair" does not mean "equal": a process with `nice -10` gets roughly twice the CPU time as one with `nice 0`, and a real-time process (`SCHED_FIFO`) can starve everything else if it never blocks. The lecture includes a demonstration: a `SCHED_FIFO` process running an infinite loop renders a Linux system completely unresponsive to SSH, requiring a hard reboot or physical console access. This is why real-time privileges are restricted to root and must be used with extreme caution.

Zombie processes are a classic operational nuisance. When a child process exits, it sends a `SIGCHLD` signal to its parent and enters a zombie state, retaining its PID and exit status until the parent calls `wait()` or `waitpid()`. A poorly written parent that never reaps its children will accumulate zombies, eventually exhausting the PID space. The solution is either fixing the parent or installing a `SIGCHLD` handler that reaps children automatically. On Windows, the equivalent issue is orphaned processes that outlive their job objects, though the Windows kernel handles cleanup more aggressively than Linux.

### Required Reading

- Arpaci-Dusseau, R.H. & Arpaci-Dusseau, A.C. (2028). *Operating Systems: Three Easy Pieces*, 2nd Edition. Chapters 4-6 (Processes, Process API, Direct Execution).
- Love, R. (2033). *Linux Kernel Development*, 4th Edition. Chapters 3-4 (Process Management, Process Scheduling).
- Russinovich, M.E. et al. (2031). *Windows Internals*, 8th Edition. Part 1, Chapters 2-3 (System Architecture, Processes and Threads).

### Discussion Questions

1. A server has 32 CPU cores but the load average is 180. What does this indicate about the process state? What would you expect to see in `vmstat` and `pidstat`? Design a tuning strategy.
2. Explain copy-on-write in the context of a database server that forks child processes to handle connections. If the child writes to a shared memory page, what happens? How does this affect memory accounting in `ps` and `top`?
3. The Norse *skipreiða* (ship levy) mobilised crews from across a district, each with their own vessel but operating under a single command. How does this distributed-but-coordinated structure parallel the relationship between parent processes and thread pools in a modern application server?

---

ᚦ **Lecture 3: Memory Management — The Invisible Battlefield**

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

Memory is the most contested resource in any computer system. This lecture covers virtual memory, paging, segmentation, the page replacement problem, memory pressure, and the practical diagnostics that reveal whether a system is memory-bound. Students learn to read `/proc/meminfo`, interpret `vmstat` output, and understand the OOM killer — the Linux kernel's last-resort mechanism for preventing total system collapse under memory pressure.

### Key Topics

- **Virtual Memory and Address Spaces:** The abstraction that gives each process the illusion of contiguous memory starting at address zero, while the physical memory is fragmented, shared, and possibly swapped to disk. The lecture covers: page tables (multi-level page tables on x86-64, inverted page tables on PowerPC), Translation Lookaside Buffers (TLBs, the cache of page table entries), and the overhead of page table walks. The 2040 reality on x86-64: 5-level page tables supporting 128-bit virtual address spaces (though 48 bits are typically used), and the performance implications of larger address spaces.
- **Paging and Page Replacement:** Physical memory is divided into fixed-size pages (typically 4KB on x86-64, with 2MB and 1GB huge pages for specific workloads). When physical memory is full, the OS must evict some pages to make room. The lecture covers page replacement algorithms: FIFO (simple but poor), LRU (optimal but expensive to implement precisely), clock (an approximation of LRU using an access bit), and the 2040 hybrid approaches that use machine learning to predict which pages are least likely to be accessed soon. The working set model and thrashing.
- **Memory Pressure and the OOM Killer:** When free memory drops below a threshold, the kernel activates the kswapd daemon to reclaim pages (dropping caches, swapping anonymous pages). If reclamation cannot keep pace with allocation, the system enters memory pressure: processes block waiting for pages, I/O wait increases, and performance collapses. The ultimate last resort is the OOM killer, which selects a process to terminate based on an `oom_score` that considers memory usage, runtime, and niceness. The lecture covers OOM killer tuning (`oom_adj`, `oom_score_adj`) and how to protect critical processes.
- **Swap and Zram:** Swap space (disk-based virtual memory extension) has a bad reputation but serves essential functions: it allows the kernel to reclaim anonymous pages that are rarely accessed, freeing RAM for active use. The lecture covers: swap partition vs. swap file, swappiness tuning (`vm.swappiness`), and the 2040 replacement of traditional swap with zram (compressed RAM-based swap) and zswap (compressed cache fronting traditional swap). On Windows: the pagefile, its sizing, and the ReadyBoost successor technologies.
- **Memory Diagnostics:** `/proc/meminfo` field by field (MemTotal, MemFree, MemAvailable, Buffers, Cached, Active, Inactive, Slab, SReclaimable, Committed_AS). `vmstat` memory columns (swpd, free, buff, cache, si, so — swap in/out). `sar -r` for historical memory usage. `smem` for per-process proportional set size (PSS). The hands-on lab: students run a memory-intensive program and observe the system transition from normal → cache pressure → swap activity → OOM.
- **Windows Memory Management:** The Windows Virtual Memory Manager, working set trimming, the standby and modified page lists, and the SuperFetch / Memory Compression features. The lecture covers Windows-specific tools: Resource Monitor, Performance Monitor (PerfMon), and the `Get-Process` PowerShell cmdlet with memory metrics.

### Lecture Notes

Memory management is the most technically complex area of operating systems, and the most important for IT operations. CPU problems are easy to understand (too much work, not enough cores); memory problems are subtle and cascading. A memory leak in one application can force the kernel to swap out pages from another application, making both slow. A database with an oversized buffer pool can starve the OS of page cache, making file I/O sluggish. Understanding these interactions requires deep knowledge of the memory subsystem.

The `/proc/meminfo` file is the Rosetta Stone of Linux memory diagnostics. `MemTotal` is the physical RAM installed. `MemFree` is the memory that is literally doing nothing — usually very small on a healthy system, because free memory is wasted memory. `MemAvailable` (introduced in Linux 3.14) is the key metric: it estimates how much memory is available for starting new applications without swapping, counting reclaimable caches. A common beginner mistake is to panic when `MemFree` is low; the professional knows to check `MemAvailable` and the ratio of active to inactive memory.

The OOM killer is a brutal but necessary mechanism. When memory is completely exhausted, something must die, or the entire system will hang. The OOM killer walks the process list, calculating a "badness score" for each, and terminates the highest-scoring process. By default, this is usually the process using the most memory — which might be your database server. IT professionals must configure `oom_score_adj` to protect critical processes (e.g., setting the database to -1000, making it unkillable) and to make sacrificial processes (e.g., batch jobs) more killable. The lecture includes a chilling case study: a 2037 cloud provider lost a customer's primary database because the OOM killer selected it during a memory pressure event; the customer had not set `oom_score_adj`, and the database was the largest process.

Swappiness is one of the most commonly misunderstood kernel parameters. Set to 60 by default, it controls the kernel's tendency to swap anonymous pages (process memory) versus reclaiming page cache (file-backed memory). A value of 0 means "do not swap unless absolutely necessary"; 100 means "swap aggressively." The 2040 best practice is: databases and latency-sensitive services use `swappiness=1` (minimal swapping); batch processing and development workstations use `swappiness=60` (default); and systems with zram use `swappiness=100` (since zram swap is fast and compresses well).

Huge pages (2MB and 1GB on x86-64) reduce TLB pressure for applications with large memory footprints. A database with 256GB of buffer pool, using 4KB pages, requires 67 million page table entries — and TLB misses become a major bottleneck. With 1GB huge pages, only 256 page table entries are needed, dramatically reducing TLB misses. The trade-off is internal fragmentation (wasted space within huge pages) and the complexity of huge page management. Transparent Huge Pages (THP) attempts to automate this but has caused performance regressions and memory bloat in some workloads; the 2040 recommendation is explicit huge pages for known workloads, THP disabled.

### Required Reading

- Arpaci-Dusseau, R.H. & Arpaci-Dusseau, A.C. (2028). *Operating Systems: Three Easy Pieces*, 2nd Edition. Chapters 12-22 (Memory Management through Paging Mechanisms).
- Love, R. (2033). *Linux Kernel Development*, 4th Edition. Chapters 12, 14, 16 (Memory Management, The Page Cache, Swapping).
- Gregg, B. (2032). *Systems Performance: Enterprise and the Cloud*, 2nd Edition. Addison-Wesley. Chapter 7 (Memory).

### Discussion Questions

1. A server's `MemFree` is 200MB but `MemAvailable` is 45GB. Explain this apparent contradiction. Is the system under memory pressure? What would you check next?
2. A database administrator sets `vm.swappiness=0` to prevent the database from being swapped. During a memory pressure event, the OOM killer terminates the database anyway. Explain why, and propose a better configuration that protects the database without disabling swap entirely.
3. The Norse *hof* (temple) had a sacred inner sanctum and outer public spaces. How does the concept of protected, hierarchically organised space inform the design of virtual memory and process isolation?

---

ᚨ **Lecture 4: File Systems — Persistence, Structure, and Integrity**

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

File systems are the mechanism by which the OS persists data beyond the lifetime of a process. This lecture covers the design and operation of file systems: the on-disk structures (superblocks, inodes, extents, journals), the in-memory caches (page cache, buffer cache, dentry cache), and the practical file systems used in 2040. Students examine file system internals using `debugfs`, benchmark different file systems under realistic workloads, and recover from simulated corruption.

### Key Topics

- **File System Fundamentals:** Files as named collections of bytes; directories as mappings from names to inodes; inodes as data structures containing metadata (size, permissions, timestamps, pointers to data blocks). The lecture covers: hard links (multiple directory entries pointing to the same inode) versus symbolic links (separate files containing paths), and the implications for backup and deletion semantics.
- **On-Disk Structures:** The superblock (file system metadata), the block group (ext4) or allocation group (XFS), the inode table, the data bitmap, and the data blocks. The lecture walks through what happens when you create a file: allocating an inode, updating the directory, allocating data blocks, and writing the journal. The 2040 file systems (Btrfs, ZFS) add copy-on-write, checksums, and snapshots, complicating but strengthening the on-disk structure.
- **Journaling and Consistency:** The problem of crash consistency: if the system crashes between writing metadata and writing data, the file system becomes inconsistent. Journaling (ext3/ext4) writes metadata changes to a journal before applying them, ensuring that the file system can recover to a consistent state after a crash. The lecture covers journaling modes: writeback (fast but unsafe for metadata), ordered (default: data written before metadata), and data (safest but slowest). ZFS and Btrfs use copy-on-write instead of journaling, which eliminates the need for `fsck` but requires more sophisticated space management.
- **The Page Cache and I/O Performance:** When a file is read, its data is copied from disk into the page cache (in RAM). Subsequent reads are served from RAM, dramatically improving performance. Writes are typically buffered in the page cache and flushed asynchronously. The lecture covers: `dirty` pages, the `pdflush`/`flush` kernel threads, `sync` and `fsync`, and the tension between performance (delayed writes) and durability (synchronous writes). The 2040 additions: `io_uring` for asynchronous I/O with reduced syscall overhead, and persistent memory file systems (ext2-DAX, NOVA) that bypass the page cache for byte-addressable NVM.
- **File System Selection in 2040:** ext4 (the default, well-understood, good performance for general workloads), XFS (excellent for large files and high concurrency, the default for RHEL), Btrfs (advanced features: snapshots, compression, RAID-like redundancy, but complex and historically brittle), ZFS (enterprise-grade: checksums, compression, snapshots, replication, but licensing complications on Linux), and NTFS/ReFS (Windows). The lecture covers selection criteria: workload characteristics (small files vs. large files, random vs. sequential I/O), required features (snapshots, compression, checksums), and organisational constraints (support contracts, staff expertise).
- **Corruption and Recovery:** The `fsck` family (e2fsck, xfs_repair), their limitations (they can verify structural consistency but not semantic correctness), and the 2040 reality that ZFS/Btrfs use continuous scrubbing (background verification of checksums) rather than periodic `fsck`. The lecture includes a recovery lab: students deliberately corrupt a test file system and practice recovery using `e2fsck -b` (using backup superblocks), `debugfs` (manual inode inspection), and `xfs_repair`.

### Lecture Notes

File systems are the most reliable and the most fragile part of the OS. Reliable because they have been refined over decades; fragile because a single bit flip in a superblock can render an entire volume unreadable. The IT professional must respect this duality: trust the file system for daily operations, but verify it with checksums, backups, and periodic scrubs.

The page cache is the single most important performance mechanism in Linux I/O. When an application reads a file, the data is copied from disk to the page cache and then to the application's buffer. The next read of the same data is served from RAM — a difference of microseconds versus milliseconds. This is why "free memory" is misleading: a system with 90% of RAM in page cache is not "almost out of memory"; it is "efficiently using free memory to cache frequently accessed files." The page cache is automatically reclaimed when applications need memory, making it a flexible buffer between disk and RAM.

Write caching is where durability and performance conflict. By default, Linux buffers writes in the page cache and flushes them every 30 seconds (`dirty_expire_centisecs`). This is fast — an application can "write" a gigabyte in milliseconds because it is only copying to RAM. But if the system crashes before the flush, the data is lost. Applications that require durability (databases, transaction logs) use `fsync()` or `O_DIRECT` to force synchronous writes. The lecture includes a benchmark: writing 1GB with buffered I/O (3 seconds), `fsync` every write (45 seconds), and `O_DIRECT` (8 seconds). The trade-off is stark, and the correct choice depends on the application's durability requirements.

ZFS deserves special attention as the file system of choice for enterprise storage in 2040. Designed at Sun Microsystems and ported to Linux via OpenZFS, it integrates volume management (RAID-Z), checksums (detecting silent data corruption), compression (transparent and fast with modern algorithms), snapshots (instantaneous, space-efficient), and replication (sending incremental snapshots to remote systems). The "ZFS parade" is a demonstration that every IT professional should witness: create a file, snapshot the pool, delete the file, and restore it from the snapshot in seconds. For data protection, ZFS is unmatched. The trade-offs are higher memory requirements (ZFS is memory-hungry, using RAM for the Adaptive Replacement Cache), licensing complexity (the CDDL license prevents distribution with the Linux kernel), and steeper learning curve.

NTFS remains the foundation of Windows storage, but ReFS (Resilient File System) has gained adoption for server workloads. ReFS provides integrity streams (checksums), copy-on-write, and automatic repair — features similar to ZFS but integrated into the Windows ecosystem. However, ReFS has limitations (no deduplication in the 2040 version, limited boot support) that prevent it from fully replacing NTFS.

### Required Reading

- Arpaci-Dusseau, R.H. & Arpaci-Dusseau, A.C. (2028). *Operating Systems: Three Easy Pieces*, 2nd Edition. Chapters 39-42 (File Systems: Implementation, Fast File System, FSCK and Journaling, Log-Structured File Systems).
- Love, R. (2033). *Linux Kernel Development*, 4th Edition. Chapters 13 (The Virtual Filesystem), 15 (The Page Cache).
- Lucas, M.W. (2031). *Absolute OpenBSD*, 3rd Edition. No Starch Press. Chapter 16 (Disks and File Systems). (For comparison perspective.)
- Yggdrasil Storage Operations Guide (2040). "File System Selection and Maintenance Standards."

### Discussion Questions

1. A developer reports that their application writes data to a file, but after a system crash, the file is empty. Explain the buffered write mechanism and what the developer must do to ensure durability. Benchmark the performance impact.
2. Compare ext4, XFS, and ZFS for a university research data store: 500TB, mixed workload (small metadata files and large instrument datasets), requires snapshots for reproducibility, and must detect bit rot over decades. Justify your recommendation.
3. The Norse *skald* composed poetry in rigid metrical forms that constrained but also enabled creativity. How does the structured, rule-based nature of file system metadata (inodes, directories, permissions) similarly constrain and enable data organisation?

---

ᚱ **Lecture 5: I/O Systems and Device Management**

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

Input/output is how the computer interacts with the world. This lecture covers the I/O subsystem: the path from a user's read request through the kernel to the physical device and back. Topics include device drivers, the block and character I/O layers, I/O schedulers, kernel bypass technologies (DPDK, RDMA), and the practical tools for I/O diagnostics. The hands-on lab includes benchmarking disk I/O with `fio`, tracing I/O with `blktrace`, and exploring the difference between buffered and direct I/O.

### Key Topics

- **The I/O Stack:** The layered architecture: user-space API (read/write, aio, io_uring), system call layer, VFS (Virtual File System, providing a unified interface across file systems), specific file system (ext4, XFS), page cache / buffer cache, generic block layer, I/O scheduler, SCSI/SATA/NVMe driver, and physical device. The lecture traces a read request through each layer, explaining the purpose and overhead of each.
- **Device Drivers:** The kernel modules that translate generic requests into device-specific commands. The lecture covers: kernel-space vs. user-space drivers, the Linux device model (devices as files in `/dev`, udev for dynamic device management), and driver stability (buggy drivers are a leading cause of kernel panics). The 2040 reality: many devices use kernel bypass (DPDK for networking, SPDK for storage) to achieve microsecond-level latency by avoiding the kernel stack entirely.
- **I/O Schedulers:** The algorithms that reorder and batch I/O requests to optimise disk performance. For rotational disks (still used for archival in 2040): CFQ (Completely Fair Queuing, default until ~2025), deadline (prioritises reads and prevents starvation), and noop (minimal overhead for SSDs). For SSDs: the mq-deadline and kyber schedulers in the multi-queue block layer. The lecture covers the fundamental difference: rotational disks benefit from request reordering to minimise seek time; SSDs benefit from parallelisation and wear levelling, making complex schedulers unnecessary.
- **NVMe and the Modern Storage Stack:** NVMe (Non-Volatile Memory Express) as the interface designed for SSDs, replacing the legacy AHCI/SATA stack designed for rotating disks. The lecture covers: NVMe queues (up to 64K per device, enabling massive parallelism), the NVMe-oF (NVMe over Fabrics) protocol for network-attached NVMe storage, and the performance implications (NVMe SSDs achieve 7GB/s and millions of IOPS, orders of magnitude beyond SATA SSDs). The 2040 frontier: NVMe-based persistent memory (Intel Optane successors) that blurs the line between storage and memory.
- **Kernel Bypass Technologies:** When the kernel I/O stack is too slow. DPDK (Data Plane Development Kit) for networking: user-space drivers that poll network interfaces directly, achieving millions of packets per second. RDMA (Remote Direct Memory Access) for high-performance computing: one server's NIC can read/write another server's memory without involving either OS. SPDK (Storage Performance Development Kit) for NVMe: user-space storage drivers. The lecture covers the trade-offs: kernel bypass sacrifices the kernel's abstraction, security, and resource management for raw performance, and requires applications to handle these concerns themselves.
- **I/O Diagnostics:** `iostat` (per-device I/O statistics: tps, kB_read/s, kB_wrtn/s, await, %util), `iotop` (per-process I/O usage), `fio` (flexible I/O benchmark: generate specified workloads and measure throughput/latency/IOPS), `blktrace` (block-level I/O tracing), and `bpftrace` (eBPF-based I/O analysis). The hands-on lab: students run `fio` with different patterns (random read, sequential write, mixed) and observe how the I/O scheduler, file system, and page cache affect performance.

### Lecture Notes

The I/O stack is the most performance-critical and the most diagnostically challenging part of the OS. A request passes through so many layers — application, libc, VFS, file system, page cache, block layer, scheduler, driver, controller, device — that a slowdown can originate at any point. The IT professional must be able to decompose I/O performance systematically, ruling out layers until the culprit is identified.

`iostat` is the first tool for I/O diagnosis. The key columns are: `r/s` and `w/s` (reads/writes per second), `rkB/s` and `wkB/s` (throughput), `await` (average wait time in milliseconds), and `%util` (percentage of time the device was busy). A device with `%util` near 100% and `await` > 50ms is saturated — either the workload exceeds device capacity, or the I/O pattern is inefficient (e.g., random small reads on a rotational disk). A device with low `%util` but high `await` may have a driver or controller issue. The lecture includes a diagnostic flowchart that maps `iostat` patterns to probable causes.

NVMe has revolutionised storage by making the storage stack parallel. AHCI (the SATA protocol) supports one queue with 32 commands; NVMe supports 64K queues with 64K commands each. This matters because modern SSDs are internally parallel — they have multiple NAND channels and controllers that can process requests simultaneously. With AHCI, the queue becomes a bottleneck; with NVMe, the SSD's internal parallelism is fully exploited. By 2040, all new server storage is NVMe, and SATA/SAS is relegated to cold archival.

Kernel bypass is a sharp tool. DPDK, used by telecom operators and high-frequency trading firms, achieves packet processing rates of 100 million packets per second per core — impossible through the kernel network stack. But it requires the application to handle everything the kernel normally provides: memory management, multi-threading, scheduling, and security. A bug in a DPDK application can crash the entire server, not just the application. The Yggdrasil guideline: use kernel bypass only when latency requirements genuinely demand it (< 10 microseconds), and always pair it with hardware-level isolation (SR-IOV, dedicated NICs).

### Required Reading

- Arpaci-Dusseau, R.H. & Arpaci-Dusseau, A.C. (2028). *Operating Systems: Three Easy Pieces*, 2nd Edition. Chapters 36-38 (I/O Devices, Hard Disk Drives, Redundant Arrays of Inexpensive Disks).
- Gregg, B. (2032). *Systems Performance: Enterprise and the Cloud*, 2nd Edition. Chapters 9-10 (Disks, Networking).
- Intel. (2033). *SPDK: Storage Performance Development Kit — Getting Started Guide*.

### Discussion Questions

1. A database server's I/O latency spikes every hour for 10 minutes. `iostat` shows 100% utilisation on the NVMe device, but throughput is only 20% of the device's rated capacity. What are three possible explanations, and what tools would you use to distinguish between them?
2. Compare kernel I/O (standard read/write syscalls) with io_uring and kernel bypass (DPDK/SPDK). For a web server handling 100,000 requests per second, which approach is appropriate? Justify your answer with latency and complexity trade-offs.
3. The Norse *knǫrr* (merchant ship) had to balance cargo capacity against speed and manoeuvrability. How does this optimisation problem parallel the design of I/O schedulers that must balance throughput, latency, and fairness?

---

ᚲ **Lecture 6: Linux Deep Dive — Boot, systemd, and Kernel Parameters**

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

Linux is the dominant server OS, and IT professionals must understand it at the administrative level. This lecture covers the Linux boot process (UEFI/BIOS → bootloader → kernel → init → services), systemd as the init system and service manager, kernel command-line parameters, sysctl tuning, and the proc filesystem. The hands-on lab includes breaking and fixing the boot process, creating systemd units, and tuning kernel parameters for specific workloads.

### Key Topics

- **The Boot Process:** Stage by stage: firmware (UEFI with Secure Boot, or legacy BIOS), bootloader (GRUB2: configuration, kernels, initramfs), kernel decompression and execution, initramfs (early userspace: loading drivers, mounting the root filesystem, pivoting to the real init), and systemd (PID 1, bringing up the rest of the system). The lecture covers UEFI variables (`efibootmgr`, `fwupd` for firmware updates), GRUB2 configuration (`/etc/default/grub`, `grub.cfg` generation), and initramfs debugging (breaking into a shell when the root filesystem cannot be mounted).
- **systemd:** The init system that has replaced SysV init on all major Linux distributions. The lecture covers: units (service, socket, target, timer, path, mount, automount, swap, slice, scope), dependencies (`Requires=`, `Wants=`, `After=`, `Before=`, `Conflicts=`), targets (graphical, multi-user, rescue, emergency), and the systemd toolbox (`systemctl`, `journalctl`, `hostnamectl`, `timedatectl`, `loginctl`). The 2040 reality: systemd has expanded far beyond init into logging (journald), networking (systemd-networkd), DNS resolution (systemd-resolved), and container management (systemd-nspawn, podman integration).
- **Kernel Parameters:** Passing options to the kernel at boot time (via GRUB2 or systemd-boot) or at runtime (via `sysctl`). The lecture covers: memory parameters (`vm.swappiness`, `vm.dirty_ratio`, `vm.vfs_cache_pressure`), network parameters (`net.core.somaxconn`, `net.ipv4.tcp_congestion_control`, `net.ipv4.ip_forward`), and security parameters (`kernel.randomize_va_space`, `kernel.kptr_restrict`). The hands-on lab: students tune `vm.swappiness` and measure the impact on a memory-intensive workload.
- **The proc and sys Filesystems:** `/proc` as the kernel's introspection interface (process information, hardware details, kernel parameters, interrupts, filesystems) and `/sys` as the structured device and driver interface. The lecture covers: reading and writing to `/proc/sys` (sysctl interface), `/proc/meminfo` and `/proc/cpuinfo`, `/proc/<pid>/` (per-process information), and `/sys/class/` (device classes and their attributes). The 2040 additions: `sysctl --system` for applying configuration from `/etc/sysctl.d/`, and `systemd-sysctl` for integration with systemd's early boot.
- **Kernel Modules:** Loading (`modprobe`, `insmod`), unloading (`rmmod`, `modprobe -r`), and managing dependencies (`depmod`, `modules.dep`). The lecture covers: module parameters (passing options at load time), blacklisting (preventing automatic loading), and the `dkms` framework for rebuilding out-of-tree modules when the kernel is updated. The 2040 reality: many enterprise features (ZFS, NVIDIA drivers, WireGuard) are delivered as kernel modules that must be carefully managed across kernel updates.

### Lecture Notes

The boot process is where the system transitions from firmware to operating system, and it is a common source of failures. A kernel update that forgets to regenerate the initramfs, a GRUB configuration that points to a deleted kernel, or a missing firmware file for a critical storage controller can render a system unbootable. The IT professional must be comfortable with boot rescue: chrooting from a live USB, rebuilding the initramfs with `dracut` or `mkinitramfs`, and manually editing GRUB entries to boot a specific kernel.

systemd is controversial among Linux veterans, many of whom preferred the simplicity of SysV init scripts. But by 2040, systemd is universal, and the professional must master it. The key insight is that systemd is not merely an init system; it is a system layer that provides a consistent API for service management, logging, resource control, and boot orchestration. A systemd service unit is declarative: you specify what the service needs (dependencies, environment, limits, sandboxing), and systemd ensures those conditions are met. This is more reliable than SysV init scripts, which were imperative and often failed to handle dependencies correctly.

The systemd journal (`journalctl`) replaces traditional syslog with a structured, indexed, binary log format. The advantages are powerful querying (`journalctl -u nginx --since "1 hour ago"`), automatic metadata (PID, UID, SELinux context, cgroup), and tamper-evident sealing (Forward Secure Sealing). The disadvantages are that traditional text-based log analysis tools (`grep`, `awk`) do not work directly on binary journals, and that journal corruption (rare but possible) requires specialised recovery. The Yggdrasil standard configuration exports journal data to both the binary journal and traditional syslog files, preserving the best of both worlds.

Kernel parameter tuning is a dark art. The defaults are chosen by kernel developers to work acceptably across the vast diversity of Linux deployments, but they are rarely optimal for specific workloads. A database server benefits from increased `vm.dirty_ratio` (allowing more dirty pages before forcing writeback) and `vm.swappiness=1` (minimising swap). A web server benefits from increased `net.core.somaxconn` (larger connection backlog) and `net.ipv4.tcp_tw_reuse` (reusing TIME_WAIT sockets). The lecture provides a "tuning cheat sheet" for common server roles, with warnings: always measure before and after, because a parameter that helps one workload may harm another.

### Required Reading

- Linux Foundation. (2034). *systemd System and Service Management*, 2nd Edition. Chapters 1-4, 7-8.
- Love, R. (2033). *Linux Kernel Development*, 4th Edition. Chapters 17 (Modules), 19 (Booting the Kernel).
- Garrels, M. (2030). *Linux System Administration: The Linux Documentation Project*. Chapters 3-4.

### Discussion Questions

1. A server fails to boot after a kernel update, displaying "VFS: cannot open root device." Walk through the boot process and identify at least three possible causes. What is your diagnostic sequence using a live USB?
2. systemd's service units support resource limits (`CPUQuota=`, `MemoryMax=`, `TasksMax=`). Design a systemd unit for a web application that should use no more than 2 CPU cores, 4GB RAM, and 1,024 concurrent threads. What happens if the service exceeds these limits?
3. The Norse *thing* (assembly) gathered free people to make decisions and settle disputes. How does the structured, rule-based governance of a *thing* parallel the declarative dependency management and resource allocation of systemd?

---

ᚷ **Lecture 7: Windows Server Deep Dive — Active Directory, PowerShell, and Services**

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

Windows Server remains a critical platform in enterprise IT. This lecture provides the deep Windows administrative knowledge that every IT professional needs, regardless of primary platform preference. Topics include Active Directory architecture (forests, domains, trees, trusts, organisational units), Group Policy, PowerShell automation, Windows services and service accounts, and the Windows security model. The hands-on lab includes deploying a domain controller, creating Group Policy objects, and automating administration with PowerShell.

### Key Topics

- **Active Directory Architecture:** The directory service that stores information about objects (users, computers, groups, printers) in a hierarchical structure. The lecture covers: forests (the top-level security boundary), domains (the primary administrative boundary), trees (contiguous namespaces), and trusts (authentication relationships between domains). The 2040 reality: hybrid identity (Azure AD Connect syncing on-premises AD with cloud Azure AD) is the default for enterprises, and cloud-native Azure AD Domain Services is increasingly replacing traditional AD for new deployments.
- **Group Policy:** The mechanism for centralised configuration management. Group Policy Objects (GPOs) linked to sites, domains, or OUs apply settings (security policies, software deployment, registry modifications, logon scripts) to target computers and users. The lecture covers: GPO processing order (LSDOU: Local, Site, Domain, OU), Group Policy Preferences (non-enforced settings), and troubleshooting (Resultant Set of Policy, `gpresult`, Group Policy Modelling). The 2040 additions: cloud-based Group Policy via Microsoft Intune and the shift toward MDM (Mobile Device Management) policies for hybrid environments.
- **PowerShell:** The object-oriented shell and scripting language that is the primary automation tool for Windows administration. The lecture covers: cmdlets (verb-noun naming: `Get-Process`, `Set-ADUser`), the pipeline (passing objects, not text), providers (filesystem, registry, certificate store, AD, SQL Server), remoting (WinRM, PowerShell Remoting, JEA — Just Enough Administration for constrained endpoints), and Desired State Configuration (DSC). The 2040 reality: PowerShell 7.x runs on Linux and is the cross-platform automation standard for hybrid environments.
- **Windows Services and Accounts:** Services as long-running processes that do not require user interaction. The lecture covers: service types (automatic, manual, disabled, delayed start), service accounts (Local System, Network Service, managed service accounts, group managed service accounts — gMSAs), and service hardening (reduced privileges, session 0 isolation, service control manager restrictions). The 2040 best practice: use gMSAs for services that need AD authentication; they provide automatic password rotation and delegation control.
- **Windows Security Model:** Security descriptors (DACLs and SACLs), access tokens (identifying the user and their privileges), impersonation (services acting on behalf of users), and User Account Control (UAC). The lecture covers: privilege escalation techniques (how attackers exploit Windows services and scheduled tasks), and defensive hardening (AppLocker for application whitelisting, Attack Surface Reduction rules, Credential Guard for isolating LSASS secrets).

### Lecture Notes

Windows administration is often underestimated by Linux-focused IT professionals, who view it as "point and click" compared to Linux's command-line power. This perception is decades out of date. Modern Windows Server administration is heavily automated: PowerShell, Group Policy, DSC, and Azure ARM templates handle configuration at scale. The Windows admin who clicks through GUIs is as obsolete as the Linux admin who only knows how to edit config files in vim without using configuration management.

Active Directory is the most widely deployed directory service in the world, and its architecture reflects 1990s design decisions that have proven remarkably durable. The forest-domain-OU hierarchy, the multimaster replication model, and the Kerberos-based authentication protocol have been extended and adapted but not replaced. Understanding AD is essential because so many enterprise applications depend on it: not just Windows logon, but Exchange, SharePoint, SQL Server, and thousands of third-party applications that use LDAP or Kerberos for authentication.

Group Policy is powerful but opaque. A user experiencing slow logon might be affected by dozens of GPOs, each applying registry settings, deploying software, running scripts, and mapping drives. The Resultant Set of Policy (RSoP) tools help, but they are read-only; predicting the effect of a new GPO before deployment requires Group Policy Modelling, a feature of the Group Policy Management Console. The lecture includes a case study: a university's logon time increased from 15 seconds to 4 minutes after a GPO was deployed that mapped 12 network drives via a PowerShell script running synchronously. The fix: switch to Group Policy Preferences for drive mapping, which runs asynchronously.

PowerShell's object-oriented pipeline is both its greatest strength and its steepest learning curve for Bash users. In Bash, `ls | grep foo` filters text; in PowerShell, `Get-Process | Where-Object {$_.Name -like "*foo*"}` filters objects by property. This is more powerful — you can filter by any property, sort by any property, and format output flexibly — but it requires understanding objects and properties rather than regular expressions. The 2040 PowerShell professional is fluent in both text-oriented and object-oriented paradigms, choosing the right tool for each task.

### Required Reading

- Stanek, W.R. (2033). *Windows Server 2040 Inside Out*. Microsoft Press. Chapters 1-4, 9-10.
- Jones, R. & Hicks, J. (2034). *PowerShell in Action*, 4th Edition. Manning. Chapters 1-3, 10-11.
- Microsoft. (2039). *Active Directory Administration Guide for Hybrid Environments*.

### Discussion Questions

1. A company has 5,000 Windows workstations and needs to deploy a new security configuration to all of them within 24 hours. Compare Group Policy, PowerShell DSC, and Microsoft Intune for this task. What are the trade-offs in speed, reliability, and auditability?
2. Explain the difference between a forest and a domain in Active Directory. Under what circumstances would an organisation need multiple forests rather than multiple domains within a single forest?
3. The Norse *jarl* (earl) ruled a district on behalf of the king, enforcing law and mustering levies. How does this delegated authority structure parallel the domain-OU-trust model of Active Directory?

---

ᚹ **Lecture 8: Security Isolation — SELinux, AppArmor, Namespaces, and cgroups**

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

Security isolation is the OS mechanism that prevents processes from interfering with each other or with the system. This lecture covers mandatory access control (SELinux, AppArmor), discretionary access control (Unix permissions, ACLs), Linux namespaces (the foundation of containers), and cgroups (resource control). Students implement SELinux policies, create container-like isolation with unshare, and use cgroups v2 to enforce resource limits.

### Key Topics

- **Discretionary Access Control (DAC):** The traditional Unix model where object owners control access (rwx permissions for user, group, other). The lecture covers: permission bits, the sticky bit, setuid/setgid, ACLs (Access Control Lists, extending permissions beyond the user/group/other model with `setfacl` and `getfacl`), and the umask. The limitations of DAC: a compromised process running as a user has all that user's permissions, and root is all-powerful.
- **Mandatory Access Control (MAC):** SELinux and AppArmor as MAC systems where the OS enforces a global security policy that users cannot override. The lecture covers: SELinux modes (enforcing, permissive, disabled), contexts (user:role:type:level), types (the primary enforcement mechanism: a process labeled `httpd_t` can only access files labeled `httpd_sys_content_t`), and policies (targeted, strict, MLS/MCS). AppArmor as a simpler alternative (path-based profiles rather than label-based types). The 2040 reality: all major Linux distributions ship with SELinux or AppArmor enabled by default; disabling them is considered a security anti-pattern.
- **Linux Namespaces:** The kernel feature that isolates process views of the system. The lecture covers the seven namespaces: PID (process IDs are isolated, enabling PID 1 in a container), Network (separate network interfaces, routing tables, firewall rules), Mount (separate filesystem views, enabling container images), UTS (separate hostname), IPC (separate shared memory and message queues), User (UID/GID mapping, enabling rootless containers), and Cgroup (isolated cgroup root). The `unshare` command for creating namespaces manually, and how Docker/Podman use them automatically.
- **cgroups v2:** The unified resource control mechanism in modern Linux. The lecture covers: the cgroup v2 hierarchy (single tree, no separate controllers), resource controls (cpu.max, memory.max, io.max, pids.max), the systemd integration (slices, scopes, and services as cgroups), and the OOM protection mechanisms (`memory.oom.group`, `memory.high` vs. `memory.max`). The hands-on lab: create a cgroup, run a CPU-intensive process inside it with `cpu.max="50000 100000"` (50% of one core), and observe the throttling.
- **Seccomp and Capabilities:** Seccomp (secure computing mode) as a syscall filter: a process can be restricted to a whitelist of syscalls, with violations causing termination. Capabilities as fine-grained privileges that replace the all-or-nothing root model (e.g., `CAP_NET_ADMIN` for network configuration without full root). The lecture covers: Docker's default seccomp profile (blocking 44 dangerous syscalls), capability dropping (`--cap-drop=ALL --cap-add=NET_BIND_SERVICE`), and the 2040 best practice of running containers with minimal capabilities.

### Lecture Notes

Security isolation is the difference between a sandbox and a shared playground. In the early days of multi-user Unix, the only isolation was DAC: your files were protected from other users by permission bits, but root could read everything, and a program running as you could do anything you could do. Modern OS security is defence in depth: DAC for basic protection, MAC for mandatory policy enforcement, namespaces for view isolation, cgroups for resource limits, seccomp for syscall filtering, and capabilities for privilege granularity.

SELinux has a reputation for being difficult, earned by its early versions where a misconfigured policy could prevent basic operations like SSH login. But by 2040, SELinux targeted policies are refined and well-integrated. The targeted policy restricts only specific daemon types (httpd, named, mysqld) while leaving user processes unconfined. For most servers, SELinux "just works" in enforcing mode. The IT professional must know how to read AVC denials (`ausearch -m avc`), generate policy modules (`audit2allow`), and troubleshoot boolean settings (`getsebool`, `setsebool`). The lecture includes a practical example: Apache cannot serve files from `/opt/web` because they lack the `httpd_sys_content_t` label; the fix is either `semanage fcontext` and `restorecon` or a custom file context mapping.

Namespaces are the technology behind containers, but they are not inherently about containers. You can use `unshare` to create a namespace manually: `unshare --pid --fork --mount-proc /bin/bash` gives you a shell where PID 1 is bash, and you cannot see the host's processes. This is useful for testing, debugging, and understanding what containers actually do. The lecture includes a "container from scratch" lab where students build a minimal container using only `unshare`, `mount` (for a root filesystem), and `chroot`.

cgroups v2 is a significant improvement over the v1 hierarchy. In v1, each controller (cpu, memory, blkio) had its own hierarchy, making resource management fragmented. In v2, there is a single unified hierarchy, and all controllers manage resources within it. The systemd integration is seamless: every service, user session, and VM is placed in a cgroup, and resource limits can be set declaratively in unit files (`CPUQuota=50%`, `MemoryMax=1G`). The OOM protection in cgroups v2 is also improved: `memory.high` is a throttle limit (soft, the kernel reclaims memory but does not kill), while `memory.max` is a hard limit (violations trigger OOM kill within the cgroup).

### Required Reading

- Vervloesem, K. (2032). *SELinux System Administration*, 3rd Edition. Packt Publishing. Chapters 1-4, 7.
- Kerrisk, M. (2034). *The Linux Programming Interface*, 2nd Edition. No Starch Press. Chapters 6-7 (Processes, Memory), Chapter 12 (Namespaces).
- Yggdrasil Security Hardening Guide (2040). "Container Isolation and Host Security."

### Discussion Questions

1. A web application running in a Docker container is compromised. The attacker has shell access inside the container. Evaluate the risk: can they escape to the host? What isolation mechanisms prevent or allow escape? How would you harden the container to minimise damage?
2. Compare SELinux (type enforcement) and AppArmor (path-based profiles) for a university web hosting environment with 500 student projects, each running as a separate user. Which is easier to configure? Which provides stronger security guarantees?
3. The Norse *borg* (fortified settlement) had multiple rings of defence: palisade, ditch, watchtower, and the armed inhabitants themselves. How does this layered defence architecture inform modern OS security design (DAC, MAC, namespaces, cgroups, seccomp)?

---

ᚺ **Lecture 9: Virtualisation and Containers — KVM, Docker, and Kubernetes Runtime**

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

Virtualisation is the abstraction of hardware resources, and it is the foundation of modern IT infrastructure. This lecture covers hardware virtualisation (KVM, Xen, VMware ESXi), operating-system virtualisation (containers via namespaces and cgroups), and the Kubernetes container runtime ecosystem (containerd, CRI-O, gVisor, Kata Containers). Students deploy VMs with KVM, build container images, and compare the isolation properties of VMs and containers.

### Key Topics

- **Hardware Virtualisation:** The hypervisor as a layer between hardware and guest OSes. Type 1 (bare-metal: KVM on Linux, Xen, VMware ESXi, Microsoft Hyper-V) and Type 2 (hosted: VirtualBox, VMware Workstation). The lecture covers: CPU virtualisation extensions (Intel VT-x, AMD-V), memory virtualisation (shadow page tables, extended page tables — EPT/NPT), I/O virtualisation (emulation, paravirtualisation, SR-IOV for direct device assignment), and storage virtualisation (QCOW2, RAW, VMDK, virtualised NVMe). The 2040 reality: KVM dominates open-source virtualisation; VMware dominates enterprise licensing.
- **KVM in Practice:** Kernel-based Virtual Machine as the Linux hypervisor. The lecture covers: `libvirt` and `virt-manager` for management, QEMU as the userspace component, `virsh` for command-line control, and the KVM networking models (NAT, bridge, macvtap). The hands-on lab: students create a VM, install a guest OS, configure bridged networking, and perform a live migration to another host.
- **Container Runtimes:** Docker as the container platform, and the OCI (Open Container Initiative) standards that ensure interoperability. The lecture covers: container images (layered filesystems, Dockerfiles, image registries), container execution (runC as the reference runtime, containerd as the daemon, CRI-O as the Kubernetes-native alternative), and rootless containers (Podman running containers without root privileges via user namespaces). The 2040 reality: Docker has been superseded by Podman in many enterprise contexts due to its daemonless, rootless architecture.
- **Container Security and Isolation:** The lecture reviews namespaces, cgroups, seccomp, and capabilities (from Lecture 8) in the container context. Additional topics: image scanning (Trivy, Clair, Grype for detecting CVEs in images), runtime security (Falco for detecting anomalous container behaviour), and supply chain security (Sigstore for signing images, SLSA for provenance verification). The 2040 additions: confidential computing containers (AMD SEV, Intel TDX — encrypting container memory from the hypervisor) and WebAssembly (Wasm) as a lighter sandbox alternative.
- **Kubernetes Runtime:** The Container Runtime Interface (CRI) that abstracts the runtime from the kubelet. The lecture covers: containerd as the default runtime in most Kubernetes distributions, CRI-O as the lightweight alternative for minimal nodes, and gVisor/Kata Containers for enhanced isolation (gVisor implements a user-space kernel; Kata runs containers in lightweight VMs). The 2040 trend: multi-tenancy Kubernetes clusters use gVisor or Kata to prevent tenant escape, while general-purpose clusters use containerd for performance.

### Lecture Notes

Virtualisation is the most transformative technology in IT operations since the internet. It decouples workloads from hardware, enabling the flexibility that makes cloud computing possible. Before virtualisation, a server was a physical machine that ran one OS; if the workload outgrew the server, you ordered a bigger one and migrated manually. With virtualisation, a server is a software construct that can be created, resized, migrated, and deleted in seconds.

KVM is the open-source hypervisor that powers most cloud infrastructure. It is not a standalone product but a Linux kernel module that transforms the kernel into a hypervisor. QEMU provides the userspace emulation (device models, BIOS, bootloader), and libvirt provides the management API. The beauty of KVM is its integration with the Linux ecosystem: the same tools that manage Linux systems (systemd, cgroups, namespaces, SELinux) manage KVM guests. A KVM VM is just another process from the host's perspective, schedulable, debuggable, and manageable with standard Linux tools.

Containers are not "lightweight VMs"; they are a different abstraction entirely. A VM virtualises hardware; a container virtualises the OS. Multiple containers share the host kernel but have isolated filesystems, process trees, and network stacks. This makes containers faster to start (seconds vs. minutes) and more efficient (hundreds or thousands per host vs. tens of VMs). But the shared kernel means weaker isolation: a container escape vulnerability (e.g., a bug in the kernel's namespace implementation) compromises the host, whereas a VM escape is far rarer and typically requires hypervisor-level bugs.

The container image format is one of Docker's enduring contributions. An image is a stack of layers, each a filesystem diff from the previous one. The base layer might be Alpine Linux (5MB); the next layer adds the application runtime; the next adds the application code. Layers are content-addressed and shared between images, reducing storage and transfer. The 2040 best practice is minimal images: start from `scratch` or `distroless` and add only what is needed, reducing attack surface. The "Golden Image" standard at Yggdrasil requires: no shell, no package manager, no compiler, no unnecessary libraries — just the application and its runtime dependencies.

Kubernetes runtime security in 2040 has evolved beyond simple container isolation. gVisor implements a user-space kernel ("Sentry") that intercepts syscalls from the container and implements them in Go, adding a second boundary between the container and the host kernel. Kata Containers run each pod in a lightweight VM (microVM using Firecracker or Cloud Hypervisor), providing VM-level isolation with container-level management. The choice depends on the threat model: a university research cluster might use containerd for trusted workloads and Kata for untrusted student code.

### Required Reading

- Vegt, M. van der. (2033). *KVM Virtualisation Handbook*. Apress. Chapters 1-3, 7.
- Mouat, A. (2034). *Using Docker: Developing and Deploying Software with Containers*, 3rd Edition. O'Reilly. Chapters 1-4, 10.
- Hightower, K., Burns, B., & Beda, J. (2035). *Kubernetes: Up and Running*, 4th Edition. O'Reilly. Chapters 1-3.

### Discussion Questions

1. A university needs to provide isolated development environments for 1,000 students. Compare VMs (KVM) and containers (Docker/Podman) for this use case. Consider: resource efficiency, isolation strength, startup time, and operational complexity.
2. A container escape vulnerability is discovered in the Linux kernel's user namespace implementation. What is the blast radius if this vulnerability is exploited on: (a) a shared Kubernetes node running trusted internal services, and (b) a shared Kubernetes node running untrusted third-party workloads? How would you mitigate in each case?
3. The Norse *landnám* (land-taking) established farms with defined boundaries but shared communal resources (pasture, woodland, water). How does this balance between private holding and common infrastructure inform the design of multi-tenant container platforms?

---

ᚾ **Lecture 10: Kernel Internals and Debugging**

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

When standard diagnostic tools fail, the IT professional must dig deeper. This lecture covers kernel debugging: reading kernel logs, tracing system calls, using dynamic instrumentation (eBPF), and understanding kernel panics. Students learn to interpret `dmesg`, use `strace` and `ltrace`, write simple eBPF programs for observability, and analyse kernel oops messages. The lecture demystifies the kernel: it is complex, but it is not magic.

### Key Topics

- **Kernel Logs and `dmesg`:** The kernel ring buffer as the first source of truth for hardware and driver issues. The lecture covers: boot messages (hardware detection, driver loading, filesystem mounting), runtime messages (device errors, network link state changes, thermal events), and severity levels (emerg, alert, crit, err, warning, notice, info, debug). The `dmesg` command, `journalctl -k` for systemd-integrated systems, and `cat /var/log/kern.log` for traditional syslog.
- **System Call Tracing:** `strace` (Linux) and Process Monitor (Windows) as tools for observing the boundary between user space and kernel space. The lecture covers: attaching to running processes (`strace -p PID`), filtering by syscall (`strace -e open,read,write`), and interpreting output (return values, error codes, elapsed time). The hands-on lab: trace a slow file copy and identify whether the bottleneck is in `open`, `read`, `write`, or `close`, and whether errors occur.
- **Dynamic Instrumentation with eBPF:** Extended Berkeley Packet Filter as the revolutionary technology for safe, efficient kernel tracing. The lecture covers: eBPF architecture (verified bytecode loaded into the kernel, JIT-compiled to native instructions, attached to kprobes/uprobes/tracepoints), the BCC toolkit (Python/C frontends for eBPF), and bpftrace (a high-level language for one-liners). Example programs: counting syscalls by process, tracing TCP connections, measuring filesystem latency, and detecting short-lived processes. The 2040 reality: eBPF has expanded beyond tracing to networking (Cilium, load balancing), security (Falco, Tetragon), and performance profiling (Parca, Pyroscope).
- **Kernel Panics and Oops Messages:** When the kernel detects an unrecoverable error, it prints an "oops" (non-fatal but serious) or panics (fatal, system halts). The lecture covers: reading the oops message (register dump, stack trace, offending function, module list), using `kdump` to capture a crash dump for post-mortem analysis, and common causes (buggy drivers, hardware failures, memory corruption). The Windows equivalent: bug check (BSOD) analysis with WinDbg and memory dumps.
- **Kernel Modules and Tainting:** The concept of a "tainted" kernel (a kernel that has loaded proprietary or untrusted modules, or experienced an error, making bug reports less useful to upstream developers). The lecture covers: reading `/proc/sys/kernel/tainted` and decoding the taint flags, and the practical implication that a tainted kernel may exhibit instability that is difficult to diagnose.

### Lecture Notes

Kernel debugging is the final frontier of systems troubleshooting. When `top` shows high CPU but you cannot identify the process, when `iostat` shows no I/O but the system is unresponsive, when a service crashes with no user-space error — the answer lies in the kernel. The professional who can read a kernel oops, trace a syscall sequence, or write an eBPF program has diagnostic capabilities that others lack.

`dmesg` is the first place to look when hardware misbehaves. A failing disk will generate ATA errors; a network driver bug will generate DMA errors; a thermal event will generate CPU throttling messages. The lecture includes a "dmesg bingo" exercise: students are given five scenarios (slow disk, intermittent network, USB device not recognised, memory errors, overheating) and must identify the relevant `dmesg` patterns for each.

`strace` is the sysadmin's microscope. It reveals every interaction between a process and the kernel: every file opened, every byte read, every socket connected, every memory page mapped. A process that "hangs" is often blocked in a single syscall: `strace` will show it stuck in `read()` waiting for data that never arrives, or in `futex()` waiting for a lock held by a dead thread. The lecture includes a famous case study: a PostgreSQL server that intermittently froze for 30 seconds. `strace` revealed that it was blocked in `fsync()` on a filesystem whose journal was on a failing disk; the disk retries caused the delay.

eBPF is the most significant advance in OS observability since `strace`. Unlike traditional tracing tools that impose high overhead (systemtap, LTTng), eBPF programs are verified to be safe (no infinite loops, no null dereferences) and JIT-compiled to native code, achieving near-zero overhead. A simple eBPF program can trace every TCP connection establishment on a server, aggregating by source IP and destination port, with overhead measured in microseconds. The lecture includes hands-on exercises with bpftrace: `bpftrace -e 'kprobe:do_nanosleep { @[comm] = count(); }'` counts how many times each process enters sleep, revealing CPU hogs and I/O waiters.

### Required Reading

- Gregg, B. (2035). *BPF Performance Tools*. Addison-Wesley. Chapters 1-3, 6-7.
- Kerrisk, M. (2034). *The Linux Programming Interface*, 2nd Edition. No Starch Press. Chapter 23 (Tracing and Debugging).
- Corbet, J., Rubini, A., & Kroah-Hartman, G. (2031). *Linux Device Drivers*, 4th Edition. O'Reilly. Chapter 4 (Debugging Techniques).

### Discussion Questions

1. A process intermittently hangs for exactly 30 seconds before resuming. Describe your diagnostic strategy using `strace`, `lsof`, and eBPF. What patterns would confirm a network timeout versus a filesystem lock versus a DNS resolution delay?
2. An eBPF program attached to a kprobe causes a kernel panic. Explain how the eBPF verifier is supposed to prevent this, and under what conditions it might fail. What safeguards should you implement when deploying eBPF in production?
3. The Norse *vǫlva* (seeress) could perceive hidden currents of fate that others could not see. How does the kernel debugger's ability to perceive hidden system behaviour parallel the *vǫlva's* insight?

---

ᛁ **Lecture 11: Performance Tuning and Observability**

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

Performance tuning is the art and science of making systems faster, more efficient, and more predictable. This lecture covers systematic performance methodology: establishing baselines, identifying bottlenecks, implementing changes, and verifying results. Students learn to use the Linux performance tools (`perf`, `mpstat`, `pidstat`, `sar`, `vmstat`, `iostat`, `ss`, `tcpdump`) and understand the USE method (Utilisation, Saturation, Errors) for resource analysis.

### Key Topics

- **The USE Method:** Brendan Gregg's methodology for analysing system resources: for each resource (CPU, memory, disk, network), check Utilisation (busy time), Saturation (queue length or waiting time), and Errors (error counts). A bottleneck exists when utilisation is high and saturation is increasing. The lecture provides a matrix mapping resources to USE metrics and the tools for measuring them.
- **CPU Performance Analysis:** `perf` (Linux Performance Events) for hardware counter profiling (cycles, instructions, cache misses, branch mispredictions), flame graphs for visualising hot code paths, and `mpstat` for per-CPU metrics. The lecture covers: CPU-bound vs. I/O-bound vs. memory-bound workloads, the difference between user time and system time (high system time suggests excessive syscalls or driver issues), and the impact of CPU frequency scaling and thermal throttling.
- **Memory Performance Analysis:** Beyond `free` and `top`: `vmstat` for page faults and swap activity, `slabtop` for kernel object cache usage, `numastat` for NUMA (Non-Uniform Memory Access) locality, and `perf mem` for memory access profiling. The lecture covers: memory bandwidth saturation (rare but devastating on HPC systems), NUMA remote access penalties (accessing memory attached to another socket is 2-3x slower), and transparent huge page effects.
- **Disk I/O Performance Analysis:** `iostat` for device-level metrics, `iotop` for per-process I/O, `blktrace` for block-level events, and `fio` for synthetic benchmarking. The lecture covers: understanding IOPS vs. throughput vs. latency, queue depth effects (SSD performance increases with queue depth up to a point), and the difference between synchronous and asynchronous I/O patterns.
- **Network Performance Analysis:** `ss` (socket statistics, replacing `netstat`), `tcpdump` and `Wireshark` for packet capture, `nicstat` for NIC-level metrics, and `iperf3` / `netperf` for throughput benchmarking. The lecture covers: TCP tuning (window scaling, congestion control algorithms: BBR, CUBIC, RENO), latency vs. bandwidth (the "long fat network" problem), and kernel bypass for ultra-low latency (DPDK, RDMA).
- **Observability Stacks in 2040:** The modern observability platform: Prometheus for metrics collection, Grafana for visualization, Loki for log aggregation, Jaeger/Tempo for distributed tracing, and eBPF-based continuous profiling (Parca, Pyroscope). The lecture covers: the shift from monitoring ("is it up?") to observability ("why is it slow?"), and the AI-assisted correlation of metrics, logs, and traces for automated root cause analysis.

### Lecture Notes

Performance tuning without a methodology is superstition. The administrator who changes random sysctl parameters because "someone on a forum said it helped" is not tuning; they are gambling. The USE method provides a systematic framework: for every resource, measure utilisation, saturation, and errors. If utilisation is low, the resource is not the bottleneck. If utilisation is high but saturation is low, the resource is busy but not overwhelmed. If both are high, you have found a bottleneck.

CPU analysis with `perf` reveals what the CPU is actually doing. The most important hardware counters are: CPU cycles (total work), instructions retired (useful work), and their ratio (CPI — cycles per instruction; lower is better). A high CPI suggests stalls: cache misses (L1, L2, L3), TLB misses, branch mispredictions, or memory bandwidth saturation. `perf record -g` captures call graphs, which can be visualised as flame graphs: horizontal bars represent functions, width represents sample count (time spent), and vertical stacking represents the call stack. A flame graph immediately reveals "hot" functions where optimisation efforts should focus.

Memory performance on modern servers is complicated by NUMA. A dual-socket server has memory controllers on each CPU; accessing "remote" memory (attached to the other socket) is significantly slower than "local" memory. The OS tries to allocate memory locally ("NUMA first-touch" policy), but if a thread migrates between sockets or if memory is shared between threads on different sockets, remote access occurs. The `numastat` tool shows per-node memory allocation; `numactl` can force local allocation or interleave across nodes. For latency-sensitive applications, NUMA awareness is essential: misconfigured applications can lose 30% performance to remote memory access.

Network performance is often limited by latency rather than bandwidth. A 10 Gbps link can transfer 1.25 GB/s — but if the round-trip time is 100ms (a transatlantic link), TCP's congestion control will limit the throughput to a fraction of the link capacity unless the window size is increased. The "bandwidth-delay product" (BDP) determines the required buffer size: for a 10 Gbps link with 100ms RTT, the BDP is 125MB, meaning the sender and receiver must each buffer 125MB to keep the pipe full. The lecture includes a calculation: given link speed and RTT, what is the minimum TCP window size required for full utilisation?

### Required Reading

- Gregg, B. (2032). *Systems Performance: Enterprise and the Cloud*, 2nd Edition. Addison-Wesley. Chapters 1-2, 6-10.
- Gregg, B. & Mauro, J. (2030). *DTrace: Dynamic Tracing in Oracle Solaris, macOS, and FreeBSD*, 2nd Edition. Prentice Hall. Chapters 1-3. (For conceptual comparison with eBPF.)
- Yggdrasil Observability Standards (2040). "Metrics, Logs, Traces, and Profiles: The Complete Stack."

### Discussion Questions

1. A web server's response time has degraded from 50ms to 500ms. Using the USE method, describe your systematic diagnostic process. What metrics would you check first? What tools would you use? How would you distinguish between CPU, memory, disk, and network bottlenecks?
2. A developer proposes disabling CPU frequency scaling (`cpufreq` governor set to "performance") to reduce latency jitter. What are the benefits and costs of this approach? Calculate the increased power consumption for a 64-core server under 30% average load.
3. The Norse *skipstjórn* (ship's navigation) required constant observation of wind, current, and stars, with adjustments made continuously rather than at intervals. How does this continuous, attentive navigation parallel the SRE practice of continuous observability and proactive tuning?

---

ᛃ **Lecture 12: The Server Hardening Challenge**

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

### Overview

The final lecture is a capstone practical: students must harden their assigned server against a simulated attack and performance degradation scenario. The challenge includes: applying security updates, configuring firewall rules, enabling MAC (SELinux or AppArmor), hardening SSH, setting resource limits with cgroups, tuning kernel parameters for the workload, and documenting all changes. The server is then subjected to a penetration test and load test; students must maintain availability and security while explaining their decisions.

### Key Topics

- **Security Hardening Checklist:** OS updates (automated patching with `unattended-upgrades` or Windows Update for Business), minimal software installation (remove unnecessary packages and services), firewall configuration (`iptables`/`nftables` or Windows Defender Firewall — default deny, explicit allow), SSH hardening (key-based auth, disable root login, disable password auth, change default port or rate-limit), and file permissions (audit SUID/SGID binaries, verify critical file permissions).
- **Mandatory Access Control:** Enabling SELinux in enforcing mode (or AppArmor) and resolving any denials. Creating custom policies if necessary. The lecture reviews: file context labelling, boolean settings, and audit2allow for policy generation.
- **Resource Governance:** Configuring cgroups v2 limits for CPU, memory, and I/O. Setting up systemd resource controls for critical services. The hands-on: apply a `CPUQuota=70%` and `MemoryMax=8G` to a web server and verify that it throttles under load rather than crashing the system.
- **Kernel Parameter Tuning:** Tuning `vm.swappiness`, `vm.dirty_ratio`, `net.core.somaxconn`, and `kernel.randomize_va_space` for the specific workload. The lecture emphasises: every parameter change must be justified with a measured performance improvement; speculative tuning is discouraged.
- **Documentation and Verification:** Every hardening step must be documented in a "System Security Plan" that includes: the change made, the rationale, the expected effect, and the verification test. The lecture covers: automated compliance checking (OpenSCAP for Linux, Security Compliance Toolkit for Windows), and continuous monitoring (Falco for runtime threats, AIDE for file integrity monitoring).
- **The Challenge Scenario:** Over a 24-hour period, the instructor's automated tools will: (1) attempt to brute-force SSH, (2) attempt a container escape if containers are present, (3) run a memory exhaustion script if resource limits are misconfigured, and (4) submit a workload that causes performance degradation if tuning is inadequate. Students must detect, block, or survive these events while maintaining service availability.

### Lecture Notes

Server hardening is where all the course concepts converge. The process knowledge from Lecture 2 helps you identify and limit runaway processes. The memory knowledge from Lecture 3 helps you set appropriate resource limits. The file system knowledge from Lecture 4 helps you verify permissions and detect unauthorised changes. The I/O knowledge from Lecture 5 helps you tune for the workload. The Linux and Windows deep dives from Lectures 6-7 provide the platform-specific skills. The security isolation from Lecture 8 provides the defence mechanisms. The virtualisation knowledge from Lecture 9 helps you isolate services. The debugging skills from Lecture 10 help you diagnose failures. And the performance methodology from Lecture 11 ensures you tune systematically, not superstitiously.

The System Security Plan is as important as the hardening itself. An opaque system — one where no one knows why a particular setting was chosen — is a liability. When the original administrator leaves, the new administrator must guess whether a sysctl parameter was set for a good reason or was cargo-culted from an outdated blog post. The Yggdrasil standard requires that every production server have a Security Plan stored in version control, reviewed annually, and updated with every change.

Automated compliance checking is essential at scale. A single server can be hardened manually; a thousand servers cannot. OpenSCAP (Security Content Automation Protocol) provides automated checks against security baselines (CIS benchmarks, DISA STIGs) and generates reports showing which rules pass and which fail. The 2040 Yggdrasil compliance pipeline runs OpenSCAP daily on every server, with failures automatically creating tickets in the ITSM system. Similarly, file integrity monitoring (AIDE, OSSEC, Tripwire) detects unauthorised changes to critical files, alerting within minutes of a compromise.

The challenge scenario is designed to be realistic, not a Capture The Flag exercise. Real attackers do not announce themselves; they brute-force slowly from distributed IPs, they exploit application vulnerabilities rather than obvious OS flaws, and they aim for persistence (backdoors, cron jobs, modified binaries) rather than immediate destruction. The automated challenge reflects this: the SSH brute-force is slow and distributed; the container escape uses a known but unpatched vulnerability; the memory exhaustion is gradual. Students must not only block the attacks but also detect them: a firewall rule that blocks SSH is not enough if you do not also check the logs to see that someone was trying.

### Required Reading

- CIS Benchmarks. (2040). *CIS Red Hat Enterprise Linux 10 Benchmark v3.0* and *CIS Windows Server 2040 Benchmark v2.0*.
- NIST SP 800-123. (2039). *Guide to General Server Security*.
- Yggdrasil Security Operations Center. (2040). *The Server Hardening Challenge: Rules, Scoring, and Evaluation Criteria*.

### Discussion Questions

1. Your server hardening plan includes disabling IPv6 because "we do not use it." A security researcher argues that disabling IPv6 reduces your attack surface. A network engineer argues that disabling IPv6 causes technical debt when IPv6 is eventually required. Evaluate both positions and propose a policy.
2. A compliance scan flags your web server for running as root. You change it to run as an unprivileged user, but the application then cannot bind to port 80. What are three solutions, and what are the security implications of each?
3. The Norse *víkingr* (pirate, raider, explorer) had to be simultaneously aggressive and cautious — bold in attack, meticulous in ship maintenance, and vigilant against surprise. How does this dual temperament inform the IT professional's approach to both proactive hardening and reactive incident response?

---

## Final Examination Preparation

The IT103 final examination assesses OS internals knowledge and practical troubleshooting skill. It consists of two components:

### Component A: Written Examination (70%)

A 2.5-hour written examination with six questions, of which students must answer four.

**Sample Questions:**

1. **Process Management:** Explain the fork-exec model with attention to copy-on-write semantics. A web server forks a child process for each connection; under heavy load, memory usage appears to double. Is this real? How would you verify?

2. **Memory Management:** A server is experiencing severe performance degradation. `vmstat 1` shows `si` and `so` (swap in/out) at 5,000 per second, `wa` (I/O wait) at 40%, and `r` (run queue) at 2. Diagnose the problem, explain the causal chain, and propose three remediation strategies with trade-offs.

3. **File Systems:** Compare journaling (ext4) and copy-on-write (Btrfs/ZFS) approaches to crash consistency. For a database server that calls `fsync()` after every transaction, which file system paradigm provides better performance and why?

4. **Security Isolation:** A container running a university student's untrusted code must be isolated from the host and other containers. Describe the complete isolation stack: namespaces, cgroups, seccomp, capabilities, and MAC (SELinux/AppArmor). What attack vector remains even with all these controls in place?

5. **Performance:** Using the USE method, analyse a scenario where `iostat` shows 100% disk utilisation but `await` is only 2ms, while CPU utilisation is 20% and memory is 90% used with no swapping. Where is the bottleneck? What additional data would you collect?

6. **Windows and Linux Integration:** A hybrid enterprise runs Active Directory for identity and Linux servers for applications. Design an authentication and authorisation architecture that allows Linux servers to authenticate users against AD, enforce group-based access control, and audit all access attempts. Specify the protocols, tools, and configuration files involved.

### Component B: Live Server Examination (30%)

A 60-minute practical examination on the student's assigned server:
- Diagnose a pre-planted performance issue (the examiner will introduce a bottleneck before the exam)
- Harden the server against a specific threat model (provided at exam time)
- Explain your diagnostic reasoning and hardening choices to the examiner

**Evaluation Criteria:**
- Diagnostic accuracy (correctly identifying the root cause)
- Methodology (systematic, evidence-based reasoning)
- Technical correctness (appropriate tools, correct commands, valid configurations)
- Security awareness (defence in depth, least privilege, verification)
- Communication (clear explanation of reasoning)

---

*The kernel is the heart of the machine. Know it, and you know the machine. Tend it, and the machine serves you well. Neglect it, and it will betray you at the worst possible moment.* ᛟ

— Prof. Björn Hrafnkelsson, University of Yggdrasil, 2040
