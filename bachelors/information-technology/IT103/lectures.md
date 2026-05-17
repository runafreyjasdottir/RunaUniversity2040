# IT103: Operating Systems for IT Professionals
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4  
**Description:** Operating Systems for IT Professionals

**Prerequisites:** IT101 (Introduction to Information Technology), IT102 (Computer Hardware & Architecture) or concurrent enrollment

**Instructor:** Prof. Brynhildr Sysadminóttir, Department of Information Technology

---

## Lectures

---

### Lecture 1: The OS as Infrastructure — Foundations for IT Operations

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

The operating system is the most consequential software an IT professional manages. It mediates every hardware access, enforces security boundaries, schedules resources, and provides the abstractions upon which all other software depends. This lecture establishes the foundational concepts of operating systems from an IT operations perspective: kernel architecture, system calls, process management, and the historical evolution that shaped the systems of 2040.

#### Key Topics

- **The Role of the Operating System:** The OS has four primary functions: (1) resource management (CPU, memory, I/O), (2) process isolation and protection, (3) abstraction of hardware complexity, and (4) provision of services to applications. For the IT professional, the OS is both tool and territory — the environment they configure, secure, monitor, and troubleshoot.
- **Kernel Architectures:**
  - **Monolithic Kernels:** All OS services (scheduling, memory management, file systems, device drivers) run in a single privileged address space. Linux and traditional Windows are monolithic. Advantages: performance, simplicity of internal communication. Disadvantages: a bug in any component can crash the entire system.
  - **Microkernels:** Only essential services (scheduling, IPC, low-level memory management) run in kernel space; other services run as user-space processes. QNX, L4, and seL4 are examples. Advantages: modularity, reliability, security. Disadvantages: performance overhead from context switches and IPC.
  - **Hybrid Kernels:** A compromise combining monolithic performance with microkernel modularity. Windows NT (the basis of modern Windows) and XNU (macOS/iOS) are hybrid kernels.
  - **Unikernels:** Single-purpose, minimal OS images compiled with an application. Used in cloud and edge deployments for fast boot, small attack surface, and efficient resource use.
- **System Calls and Privilege Rings:** User-space applications request kernel services via system calls. The transition from user mode (Ring 3) to kernel mode (Ring 0) involves context switch overhead. x86-64 defines four privilege rings, but modern OSes use only two. ARM64 uses Exception Levels (EL0–EL3) with similar semantics.
- **The IT Professional's OS Landscape in 2040:**
  - **Linux:** Dominates servers, cloud, embedded, and HPC. Distributions: RHEL, Ubuntu LTS, SUSE, YggdrasilOS.
  - **Windows Server:** Prevails in enterprise applications, Active Directory environments, and Microsoft-centric ecosystems.
  - **BSD/Unix:** FreeBSD and OpenBSD power networking equipment, firewalls, and security-critical systems.
  - **Real-Time OS:** Zephyr, FreeRTOS, VxWorks for embedded and industrial control.
  - **Container OS:** Bottlerocket, Talos, and Flatcar — minimal, immutable OSes designed solely to run containers.

#### Lecture Notes

The UoY IT Department operates approximately 15,000 server instances across these OS platforms. The "OS Standardization Policy" mandates: production servers must run approved OS versions with security patches applied within 72 hours of release. Exceptions require written risk acceptance from the CISO.

A key concept for IT professionals is the "support lifecycle": every OS version has an end-of-life date after which security patches cease. Running an unsupported OS in production is a critical vulnerability. The UoY maintains a "Lifecycle Calendar" tracking all deployed OS versions and their retirement dates, with automated alerts at 12 months, 6 months, and 30 days before end-of-life.

#### Required Reading

- Silberschatz, A., Galvin, P. B., & Gagne, G. (2036). *Operating System Concepts* (12th ed.). Wiley.
- Love, R. (2035). *Linux Kernel Development* (5th ed.). Addison-Wesley.
- Microsoft. (2039). *Windows Server 2040 Internals*.

#### Discussion Questions

1. Linux dominates servers but Windows Server remains entrenched in many enterprises. What are the migration barriers from Windows to Linux, and when is Windows still the rational choice?
2. Microkernels promise superior reliability but have never displaced monolithic kernels in general-purpose computing. What would it take for microkernels to become mainstream, or is the performance penalty permanently prohibitive?
3. Container OSes (Bottlerocket, Talos) sacrifice flexibility for security and operational simplicity. Under what conditions does this trade-off make sense, and when do you need a general-purpose OS?

#### Practice Problems

- List the system calls made by a simple program (`ls`, `cat`) using `strace` (Linux) or Process Monitor (Windows). Categorize each call by function (file access, memory, process management, network).
- Compare the boot process of a traditional Linux distribution (systemd) and a container OS (Bottlerocket). Document the differences in initialization, service management, and update mechanisms.
- Research the security architecture of QNX or seL4. Write a 1,000-word assessment of whether these microkernels could meet the UoY's server requirements.

---

### Lecture 2: Process and Thread Management — The Unit of Execution

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

A process is an instance of a program in execution — the fundamental unit of resource allocation. Threads are units of execution within a process. Understanding how the OS creates, schedules, and terminates processes and threads is essential for troubleshooting performance issues, managing resource contention, and designing resilient systems.

#### Key Topics

- **Process Structure:** A process consists of: code segment (executable instructions), data segment (global/static variables), heap (dynamically allocated memory), stack (local variables and function call frames), and the Process Control Block (PCB) — the kernel data structure containing process state, registers, memory map, open files, and scheduling information.
- **Process Lifecycle:** Created via `fork()` (Unix) or `CreateProcess()` (Windows), transitioning through states: new, ready, running, waiting (blocked), and terminated. Zombie processes (terminated but not reaped by parent) and orphan processes (parent terminated) are common issues IT professionals encounter.
- **Threads and Concurrency:** Threads share the process's address space but have independent execution contexts (registers, stack). User-level threads (managed by a runtime library) versus kernel-level threads (managed by the OS). Modern OSes use a 1:1 model (each user thread maps to a kernel thread). The IT professional must understand thread synchronization: mutexes, semaphores, condition variables, and the deadlock/livelock/starvation hazards they mitigate.
- **CPU Scheduling:** The scheduler selects which ready process/thread runs next. Algorithms:
  - **First-Come First-Served (FCFS):** Simple but can cause convoy effects.
  - **Shortest Job First (SJF):** Optimal for average wait time but requires predicting burst length.
  - **Round Robin:** Time-sliced, fair, but high context-switch overhead for short quanta.
  - **Priority Scheduling:** Higher priority processes run first, risking starvation of low-priority processes.
  - **Completely Fair Scheduler (CFS):** Linux's default, allocating CPU proportionally based on priority weights.
  - **Real-Time Schedulers:** SCHED_FIFO and SCHED_RR for hard real-time requirements.
- **Context Switching:** The overhead of saving one process's state and restoring another's. Involves: saving/restoring registers, switching address spaces (TLB flush), and cache pollution. Context switches cost 1–10 μs on modern hardware — negligible for most workloads but significant for high-frequency trading and real-time systems.

#### Lecture Notes

The IT professional diagnoses process issues daily: a service consuming 100% CPU, a process stuck in uninterruptible sleep (D-state), a memory leak causing OOM kills, or a runaway thread storm exhausting file descriptors. The UoY IT Department's "Process Troubleshooting Playbook" provides decision trees for common scenarios, with commands: `ps`, `top`, `htop`, `pidstat`, `strace`, `lsof`, and `/proc` inspection.

In 2040, AI-assisted process monitoring predicts anomalies: a process's CPU usage pattern deviates from its historical baseline, triggering automatic investigation. The human engineer validates the AI's findings and decides on remediation: restart, migrate, debug, or escalate.

#### Required Reading

- Silberschatz et al. (2036). Chapters 3–6: Processes, Threads, CPU Scheduling, Synchronization.
- Bovet, D. P., & Cesati, M. (2035). *Understanding the Linux Kernel* (6th ed.). O'Reilly.

#### Discussion Questions

1. A web server spawns a new process for each incoming connection. Under heavy load, the server becomes unresponsive. Is the issue the process creation overhead, memory exhaustion, or something else? How do you diagnose it?
2. The Linux CFS aims for fairness, but fairness is not always optimal. Under what conditions would you override CFS with a real-time or deadline scheduler?
3. A container running a multi-threaded application shows poor scaling beyond 8 threads on a 32-core host. What OS-level factors (scheduler, NUMA topology, synchronization overhead) might limit scaling?

#### Practice Problems

- Write a Python program that creates 100 child processes, each sleeping for a random duration. Monitor the parent process's resource usage and explain the zombie process phenomenon.
- Use `perf sched` to analyze context switch latency under different workloads (CPU-bound, I/O-bound, mixed). Document the relationship between workload type and switch frequency.
- Implement a simple priority scheduler simulation. Compare average waiting time under FCFS, SJF, and Round Robin for a given workload mix.

---

### Lecture 3: Memory Management — Virtual, Physical, and Everything Between

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Memory is the most contested resource in computing. Every process demands it; the OS must allocate it fairly, protect it rigorously, and reclaim it efficiently. This lecture examines memory management: physical memory organization, virtual memory, paging, segmentation, memory allocation strategies, and the practical implications for IT operations.

#### Key Topics

- **Physical Memory Organization:** DRAM is organized into channels, ranks, banks, rows, and columns. NUMA (Non-Uniform Memory Access) architectures assign specific memory regions to specific CPUs. Local memory access is fast; remote memory access crosses the interconnect and is slower. The IT professional must understand NUMA topology to optimize process placement.
- **Virtual Memory:** Each process sees a contiguous private address space, independent of physical memory layout. The Memory Management Unit (MMU) translates virtual addresses to physical addresses via page tables. Benefits: process isolation, memory overcommitment, demand paging, and shared libraries.
- **Paging and Page Tables:** Memory is divided into fixed-size pages (typically 4 KB, with 2 MB and 1 GB "huge pages" for specific workloads). Page tables are hierarchical (4 levels on x86-64, 5 levels for large address spaces). TLB (Translation Lookaside Buffer) caches recent translations. TLB misses trigger page table walks — expensive operations requiring multiple memory accesses.
- **Demand Paging and Swapping:** Pages are loaded from disk only when accessed (demand paging). When physical memory is exhausted, the OS swaps pages to disk (swap space, page file). Swapping destroys performance; the IT professional must monitor swap usage as a critical health metric.
- **Memory Allocation:** The kernel allocator (buddy system for pages, slab allocator for objects) and the C library allocator (ptmalloc, jemalloc, tcmalloc). Fragmentation (external: scattered free blocks; internal: unused space within allocated blocks) reduces usable capacity.
- **Memory Pressure and OOM:** When memory is critically low, the Linux OOM (Out-of-Memory) killer selects processes to terminate based on an "badness" score. The IT professional must understand how to tune OOM behavior, configure memory limits (cgroups, systemd), and prevent OOM scenarios through capacity planning.

#### Lecture Notes

Memory troubleshooting is a core IT skill. The UoY IT Department uses the "MEMORY CHECK" mnemonic:
- **M**etrics: `free`, `vmstat`, `sar -r`, `/proc/meminfo`
- **E**xamine: Which processes consume the most memory? `ps aux --sort=-%mem`
- **M**aps: How is memory used? Cache, buffers, anonymous, shared? `pmap`, `smem`
- **O**OM: Has the OOM killer fired? Check `dmesg | grep -i "killed process"`
- **R**eclaim: Can memory be freed? Drop caches? Adjust swappiness?
- **Y**ield: If memory is truly insufficient, scale out or upgrade hardware.

Huge pages are critical for specific workloads: databases (Oracle, PostgreSQL), Java heaps, and AI training frameworks. The IT professional configures transparent huge pages (THP) or explicit huge pages (hugetlbfs) based on workload requirements. THP can cause latency spikes during compaction; explicit huge pages require pre-allocation but offer predictable performance.

#### Required Reading

- Silberschatz et al. (2036). Chapters 9–10: Virtual Memory, File-System Interface.
- Gorman, M. (2035). *Understanding the Linux Virtual Memory Manager* (3rd ed.). Lulu.

#### Discussion Questions

1. A database administrator requests 2 MB huge pages for a 500 GB database instance. What are the operational implications for memory fragmentation, system boot time, and other workloads on the same server?
2. The OOM killer terminated a critical process. How do you determine why the system ran out of memory, and what preventive measures do you implement?
3. NUMA-aware scheduling can improve performance but complicates container deployment. How do Kubernetes and modern container runtimes handle NUMA topology for multi-tenant environments?

#### Practice Problems

- Write a program that allocates memory incrementally until the OOM killer terminates it. Observe and document the system's behavior: memory pressure indicators, OOM killer selection logic, and recovery time.
- Configure a Linux server for database workloads: disable swap, enable huge pages, tune `vm.swappiness` and `vm.dirty_ratio`. Benchmark a database workload before and after tuning.
- Analyze the memory map of a running process using `pmap -x`. Identify the code, data, heap, stack, and shared library regions. Calculate the proportion of resident versus mapped memory.

---

### Lecture 4: File Systems — Persistence, Structure, and Integrity

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

File systems provide the abstraction of persistent, named data organized hierarchically. They are the most visible OS service to users and the most critical for data integrity. This lecture examines file system concepts: organization, journaling, copy-on-write, networked file systems, and the modern distributed file systems that underpin cloud storage.

#### Key Topics

- **File System Fundamentals:** Files (named sequences of bytes), directories (named collections of files and subdirectories), metadata (permissions, ownership, timestamps, extended attributes), and inodes (data structures containing file metadata and pointers to data blocks).
- **Allocation Strategies:** Contiguous (simple, fast, but causes fragmentation), linked list (flexible but slow random access), indexed (inode with direct and indirect block pointers — the Unix model), and extent-based (contiguous runs of blocks — modern file systems).
- **Journaling and Crash Recovery:** Journaling file systems (ext3, ext4, NTFS, XFS) log metadata changes before applying them, enabling fast recovery after power loss. Three journaling modes: writeback (data may be inconsistent), ordered (data written before metadata), and data (full data journaling — safest but slowest).
- **Copy-on-Write (COW) File Systems:** btrfs, ZFS, and APFS use copy-on-write: instead of overwriting data in place, they write new data to fresh blocks and update pointers. Advantages: atomic snapshots, efficient clones, and data integrity via checksums. Disadvantages: fragmentation and complex space accounting.
- **ZFS Deep Dive:** The "last word in file systems" (designed by Sun, ported to Linux, FreeBSD, and proprietary systems). Features: pooled storage (no fixed volume sizes), copy-on-write, checksums for all data and metadata, RAID-Z (erasure coding), deduplication, compression, and snapshots. The IT professional's role: designing ZFS pools (vdev layout, redundancy level), tuning arc size, and managing scrubs/resilvering.
- **Networked and Distributed File Systems:** NFS (v4.2 with pNFS for parallel access), SMB/CIFS (Windows file sharing), Ceph (software-defined storage with object, block, and file interfaces), Lustre (HPC parallel file system), and GlusterFS. In 2040, IT professionals increasingly manage object storage (S3-compatible) and distributed block storage (Ceph RBD, Portworx) rather than traditional NFS shares.

#### Lecture Notes

File system selection is a consequential IT decision that affects performance, reliability, and operational complexity for years. The UoY Storage Policy specifies:
- **Root volumes:** xfs (stable, performant, well-supported).
- **Large data volumes:** ZFS (snapshots, checksums, compression).
- **High-performance scratch:** Lustre (HPC workloads).
- **Cloud-native:** Ceph (self-healing, distributed, S3-compatible).

Data integrity is paramount. ZFS's end-to-end checksums detect silent data corruption (bit rot) that other file systems cannot. The UoY runs monthly ZFS scrubs across all ZFS pools, with automated alerts for checksum errors. A checksum mismatch triggers: immediate data reconstruction from redundancy, investigation of the faulty device, and replacement if errors persist.

#### Required Reading

- Silberschatz et al. (2036). Chapters 11–14: File-System Interface, Implementation, Mass-Storage Structure, I/O Systems.
- Lucas, M. W. (2037). *FreeBSD Mastery: ZFS* (2nd ed.). Tilted Windmill Press.
- Ceph Documentation. (2039). *Ceph Architecture and Operations Guide*.

#### Discussion Questions

1. ZFS offers superior data integrity but requires more memory (1 GB per TB of storage for deduplication) and has a steep learning curve. Under what conditions is ZFS worth the complexity, and when is a simpler file system like xfs preferable?
2. A distributed file system (Ceph) experiences a "split brain" scenario where two nodes believe they are the primary for the same data. What mechanisms prevent or recover from this, and what are the operational implications?
3. Deduplication saves space but consumes significant CPU and memory. How do you evaluate whether deduplication is cost-effective for a given dataset?

#### Practice Problems

- Create a ZFS pool with mirrored vdevs. Create datasets with different properties (compression, quotas, snapshots). Simulate disk failure, replacement, and resilvering. Document the process and timeline.
- Compare the performance of ext4, xfs, and ZFS on a mixed workload: small file creation, large sequential writes, and random reads. Use `fio` for benchmarking and explain the differences.
- Design a distributed storage architecture for a university with 5 petabytes of research data, requiring: high availability, geolocation redundancy, S3-compatible access, and automated tiering to cold storage.

---

### Lecture 5: I/O Systems and Device Management

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Input/output is where the digital meets the physical. Every storage access, network packet, keyboard press, and sensor reading traverses the I/O subsystem. This lecture examines how the OS manages devices: device drivers, interrupt handling, DMA, block and character devices, and the modern I/O virtualization technologies that enable cloud computing.

#### Key Topics

- **Device Drivers:** Software modules that translate generic OS requests into device-specific commands. Character devices (sequential access: keyboards, serial ports) and block devices (random access: disks, SSDs). The IT professional must manage driver versions, debug driver conflicts, and understand when to use vendor drivers versus kernel built-in drivers.
- **Interrupts and Polling:** Devices signal the CPU via interrupts (asynchronous, efficient for infrequent events) or via polling (CPU checks device status periodically, efficient for high-frequency events). Modern systems use interrupt coalescing (batching multiple interrupts) and adaptive polling (switching between modes based on load).
- **Direct Memory Access (DMA):** Devices transfer data directly to/from memory without CPU involvement. The DMA controller manages bus transactions. Modern systems use IOMMU (Input-Output Memory Management Unit) to virtualize DMA, enabling device isolation and security (preventing a compromised device from accessing arbitrary memory).
- **I/O Scheduling:** For block devices, the OS schedules I/O requests to minimize seek time and maximize throughput. Algorithms: NOOP (simple FIFO, good for SSDs), Deadline (prevents starvation), CFQ (Completely Fair Queuing, per-process fairness), and mq-deadline / bfq for NVMe multi-queue devices.
- **I/O Virtualization:**
  - **Virtio:** Paravirtualized I/O for VMs, where the guest OS cooperates with the hypervisor for efficient I/O.
  - **SR-IOV:** Single Root I/O Virtualization allows a physical device (NIC, GPU) to present multiple virtual functions (VFs) to VMs, with near-native performance.
  - **DPU (Data Processing Unit):** SmartNICs (NVIDIA BlueField-4, AMD Pensando-3) that offload networking, storage, security, and virtualization from the host CPU. By 2040, DPUs are standard in cloud data centers.

#### Lecture Notes

I/O troubleshooting requires understanding the full stack: application → system call → VFS → file system → block layer → I/O scheduler → device driver → HBA/firmware → physical device. A bottleneck can occur at any layer. The UoY IT Department's "I/O Stack Diagram" — a wall-sized poster in every operations room — reminds engineers to consider the entire chain before blaming "the disk."

NVMe has revolutionized storage I/O. Unlike SATA/AHCI with a single queue, NVMe supports up to 64K queues with up to 64K entries each, enabling massive parallelism. The Linux multi-queue block layer (blk-mq) scales I/O submission across CPU cores. The IT professional tunes: queue depth, I/O scheduler (none for NVMe), and IRQ affinity to match workload characteristics.

#### Required Reading

- Corbet, J., Rubini, A., & Kroah-Hartman, G. (2035). *Linux Device Drivers* (4th ed.). O'Reilly.
-SNIA. (2039). *NVMe 2.1 Specification and Enterprise Deployment Guide*.

#### Discussion Questions

1. A VM experiences high I/O latency. The hypervisor admin blames the storage array; the storage admin blames the VM. How do you systematically locate the bottleneck in the virtualized I/O stack?
2. SR-IOV provides near-native network performance to VMs but complicates live migration and complicates the security model (each VF has DMA access). When is SR-IOV worth the complexity?
3. DPUs promise to offload host CPU work, but they also introduce a new management layer (DPU OS, firmware, drivers). How do you evaluate whether DPUs reduce or increase total operational complexity?

#### Practice Problems

- Use `blktrace` and `blkparse` to trace the I/O operations of a workload. Analyze the pattern: sequential vs. random, read vs. write, queue depth over time.
- Compare I/O performance under different schedulers: `none`, `mq-deadline`, and `bfq` on an NVMe SSD. Use `fio` with various workloads and document the throughput and latency differences.
- Configure SR-IOV on a supported NIC. Assign virtual functions to two VMs and benchmark network throughput. Compare against virtio and bridge-based networking.

---

### Lecture 6: Security Architecture — The OS as Guardian

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

The operating system is the primary guardian of system security. It enforces authentication, authorization, isolation, and audit. This lecture examines OS security mechanisms: identity and access control, privilege separation, sandboxing, mandatory access control, and the emerging security paradigms of 2040: confidential computing, zero-kernel-trust models, and AI-driven threat detection.

#### Key Topics

- **Identity and Authentication:** Users and processes are identified by credentials: passwords (increasingly phased out in 2040), public-key authentication (SSH keys, FIDO3 passkeys), biometrics, and hardware tokens (TPM, smart cards, YubiKey). Multi-factor authentication (MFA) is mandatory for all administrative access at UoY.
- **Discretionary Access Control (DAC):** The traditional Unix model: every file has an owner, group, and permission bits (read/write/execute for owner, group, others). Extended ACLs (Access Control Lists) provide finer granularity. Windows uses a more complex ACL model with inheritance and explicit deny rules.
- **Mandatory Access Control (MAC):** System-enforced policies that users cannot override. SELinux (Security-Enhanced Linux) uses type enforcement, role-based access control, and multi-level security. AppArmor uses path-based profiles. The IT professional must understand how to write, debug, and deploy MAC policies without breaking legitimate applications.
- **Capabilities and Privilege Separation:** Linux capabilities divide root privileges into fine-grained units (e.g., CAP_NET_ADMIN for network configuration, CAP_SYS_PTRACE for process debugging). Containers drop unnecessary capabilities to reduce attack surface. Privilege separation: services run components with minimal required privileges (e.g., a web server runs as an unprivileged user, with a small privileged component for port binding).
- **Sandboxing:** Technologies that confine applications: chroot (legacy, weak), seccomp (system call filtering), namespaces (isolation of processes, network, mounts, users), and gVisor/Kata Containers (user-space kernel for additional isolation). The IT professional configures sandboxing for untrusted workloads: student code, third-party applications, and internet-facing services.
- **Confidential Computing:** Hardware-based trusted execution environments (TEEs): Intel TDX, AMD SEV-SNP, ARM CCA. These technologies encrypt memory and CPU state so that even the hypervisor or OS cannot inspect protected workloads. Used for: multi-tenant cloud security, AI model protection, and regulated data processing.

#### Lecture Notes

Security is not a feature; it is a property of the system as a whole. A server with the latest patches but a default password is insecure. A system with strong authentication but no audit logging is unaccountable. The UoY Security Operations Center (SOC) monitors 50,000+ endpoints using a "Defense in Depth" model with OS-level controls as the foundation.

The IT professional's security checklist for new servers:
1. Remove or disable unnecessary services and accounts.
2. Apply all security patches before network exposure.
3. Configure host-based firewall (iptables/nftables, Windows Defender Firewall).
4. Enable SELinux or AppArmor in enforcing mode.
5. Configure centralized logging and integrity monitoring (AIDE, OSQuery).
6. Enable automatic security updates with staged rollout.
7. Verify backup and recovery procedures before go-live.

#### Required Reading

- Erickson, J. (2037). *Hacking: The Art of Exploitation* (4th ed.). No Starch Press.
- SELinux Project. (2039). *SELinux Policy Administration: A Practical Guide*.
- Confidential Computing Consortium. (2039). *Confidential Computing: Technical Foundations and Use Cases*.

#### Discussion Questions

1. SELinux in enforcing mode has historically caused application breakage, leading many administrators to disable it. How do you build organizational competence to run SELinux effectively without resorting to permissive mode?
2. Confidential computing protects workloads from the cloud provider, but who protects the user from flaws in the TEE implementation (e.g., side-channel attacks against SEV)?
3. A student submits a program for grading. The grading system runs student code with seccomp and namespace isolation. A clever student escapes the sandbox using a kernel vulnerability. What is the university's responsibility, and what additional layers of defense are needed?

#### Practice Problems

- Write an SELinux policy module for a custom application. Define the types, allow rules, and transitions. Test in permissive mode, fix denials, and deploy in enforcing mode.
- Configure a container with minimal privileges: drop all capabilities, use a read-only root filesystem, run as non-root, and restrict syscalls with seccomp. Verify the restrictions.
- Enable and configure AMD SEV or Intel TDX on a supported system. Launch a confidential VM and verify that memory encryption is active using vendor-provided tools.

---

### Lecture 7: Virtualization and Containers — The Modern Abstraction Stack

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Virtualization is the defining technology of modern IT infrastructure. It enables efficiency, flexibility, and isolation by abstracting physical hardware into multiple logical instances. This lecture examines virtualization mechanisms: hardware-assisted CPU virtualization, memory virtualization, I/O virtualization, and the container technologies that have largely replaced traditional VMs for application deployment.

#### Key Topics

- **Hardware-Assisted Virtualization:** Intel VT-x and AMD-V provide CPU extensions for efficient virtualization: root/non-root modes, VMCS (Virtual Machine Control Structure), and shadow page tables (replaced by EPT — Extended Page Tables — and NPT — Nested Page Tables). Virtualization overhead is now <5% for CPU-bound workloads.
- **Hypervisor Types:**
  - **Type 1 (Bare-Metal):** Runs directly on hardware. VMware ESXi, Microsoft Hyper-V, Xen, KVM (Linux kernel module). Dominant in data centers.
  - **Type 2 (Hosted):** Runs atop a host OS. VMware Workstation, VirtualBox, Parallels. Used for development and testing.
- **Memory Virtualization:** Shadow page tables (software-managed) versus hardware-assisted nested paging (EPT/NPT). Memory overcommitment: allocating more virtual memory than physical memory, relying on page sharing and swapping. Ballooning: reclaiming memory from idle VMs by inflating a "balloon driver" inside the guest.
- **Containers and OS-Level Virtualization:** Containers share the host OS kernel but have isolated namespaces, cgroups, and filesystems (via overlayfs or copy-on-write). Advantages: near-native performance, fast startup, high density. Disadvantages: weaker isolation than VMs, shared kernel vulnerability. Container runtimes: containerd, CRI-O, Docker Engine (deprecated in production by 2040 in favor of containerd/CRI-O).
- **Orchestration:** Kubernetes dominates container orchestration in 2040. Concepts: pods, deployments, services, ingress, configmaps, secrets, persistent volumes, and operators. The IT professional must understand Kubernetes architecture (control plane: API server, scheduler, controller manager, etcd; data plane: kubelet, kube-proxy, container runtime) and operational practices.
- **Micro-VMs and Unikernels:** Firecracker (AWS), Cloud Hypervisor, and Kata Containers combine VM-level isolation with container-level density and speed. Used in serverless platforms and multi-tenant environments where container isolation is insufficient.

#### Lecture Notes

The UoY Compute Platform runs 80% of workloads in containers (Kubernetes) and 20% in VMs (legacy systems, security-critical workloads, and systems requiring specific hardware passthrough). The "Virtualization Strategy" document specifies: new applications default to containers unless they require VM-specific features. Migration from VMs to containers is an ongoing program, with 500+ workloads transitioned in 2039.

Container security is a top concern. The UoY Kubernetes Security Policy mandates: non-root containers, read-only root filesystems, dropped capabilities, seccomp profiles, network policies, pod security standards (PSS), and vulnerability scanning (Trivy, Grype) in CI/CD. Admission controllers (Kyverno, OPA Gatekeeper) enforce these policies automatically.

#### Required Reading

- Smith, J. E., & Nair, R. (2036). *Virtual Machines: Versatile Platforms for Systems and Processes* (2nd ed.). Morgan Kaufmann.
- Hightower, K., Burns, B., & Beda, J. (2037). *Kubernetes: Up and Running* (5th ed.). O'Reilly.
- AWS. (2039). *Firecracker: Lightweight Virtualization for Serverless Computing*.

#### Discussion Questions

1. A security audit flags the shared kernel in container deployments as a risk. The application team argues that VMs are too slow and expensive. How do you evaluate micro-VMs (Firecracker, Kata) as a middle ground?
2. Kubernetes has become the universal control plane, but its complexity is notorious. What operational practices and tools reduce Kubernetes management burden without sacrificing capability?
3. Memory overcommitment in virtualized environments improves density but risks performance degradation during memory pressure. How do you set overcommitment ratios that balance efficiency and stability?

#### Practice Problems

- Deploy a Kubernetes cluster (using minikube, kind, or a cloud-managed service). Deploy a multi-tier application (web, API, database) with persistent storage. Demonstrate scaling, rolling updates, and rollback.
- Compare the boot time, memory overhead, and I/O performance of a VM (KVM), a container (containerd), and a micro-VM (Firecracker). Use standardized benchmarks.
- Write a Kubernetes network policy that isolates a namespace: pods can communicate within the namespace but only reach specific external services via egress rules.

---

### Lecture 8: Boot Process and System Initialization

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Every system boot is a journey from powered-off silicon to a functioning operating system. Understanding this journey is essential for troubleshooting boot failures, securing the boot chain, and optimizing startup time. This lecture traces the boot process from firmware to kernel to userspace, examining BIOS/UEFI, bootloaders, init systems, and the modern immutable infrastructure patterns that redefine initialization.

#### Key Topics

- **Firmware:** BIOS (legacy, 16-bit real mode) and UEFI (Unified Extensible Firmware Interface, modern, 32/64-bit, modular). UEFI provides: GPT partitioning (replacing MBR), secure boot (cryptographic verification of bootloaders and OS kernels), and pre-OS networking/drivers. The IT professional must manage UEFI settings, update firmware, and troubleshoot secure boot conflicts.
- **Bootloader:** The program that loads the OS kernel. Linux: GRUB 2 (most common), systemd-boot, rEFInd. Windows: Boot Manager. The bootloader presents a menu (if configured), loads the kernel and initramfs into memory, and transfers control.
- **Kernel Initialization:** The kernel decompresses itself, initializes hardware (via ACPI, device tree), mounts the root filesystem, and executes the first userspace process (traditionally `/sbin/init`, now usually systemd). Kernel command-line parameters control behavior: `root=`, `quiet`, `nomodeset`, `systemd.unit=`, `selinux=`, `rd.break` (emergency shell).
- **Init Systems and Service Management:**
  - **Systemd:** The dominant Linux init system. Concepts: units (service, socket, target, timer, mount), targets (runlevels reimagined: multi-user, graphical, rescue), dependencies, sockets activation, and timers (cron replacement).
  - **Windows Service Control Manager (SCM):** Manages Windows services, dependencies, and recovery actions.
  - **Container Initialization:** Container entrypoints, PID 1 responsibilities (signal handling, zombie reaping), and init systems for containers (tini, dumb-init, systemd in privileged containers).
- **Immutable Infrastructure:** Rather than configuring servers in place, immutable infrastructure bakes configuration into machine images (AMIs, VM templates, container images). Servers are replaced rather than modified, ensuring consistency and reproducibility. Tools: Packer, image builders, GitOps. The UoY production environment is 90% immutable by 2040.

#### Lecture Notes

Boot troubleshooting is a critical IT skill. The UoY "Boot Failure Decision Tree" guides engineers through: power-on self-test (POST) beep codes, firmware settings, bootloader configuration, kernel parameters, initramfs issues, filesystem corruption, and systemd unit failures. Common tools: `journalctl`, `dmesg`, `grub2-mkconfig`, `dracut`, and recovery mode.

Secure Boot is mandatory for all UoY production systems. The IT organization maintains a private CA that signs custom kernels and kernel modules. Loading an unsigned kernel module triggers an immediate security alert and may block the module. This policy prevents rootkits and unauthorized kernel modifications but requires careful management of signing keys and module allowlists.

#### Required Reading

- Rhodes, J., & Cook, R. (2037). *How Linux Boots: From Power-On to Login* (2nd ed.). No Starch Press.
- Lennart Poettering. (2038). *Systemd for Administrators* (4th ed.). Red Hat.
- Microsoft. (2039). *Windows Boot Architecture and Troubleshooting*.

#### Discussion Questions

1. Systemd is powerful but complex and controversial. Critics argue it violates the Unix philosophy. How do you respond to these criticisms from a practical IT operations perspective?
2. Immutable infrastructure simplifies management but requires robust CI/CD and rollback procedures. What happens when a bad image is deployed fleet-wide? How do you recover?
3. Secure Boot protects against bootkits but complicates the installation of third-party drivers and custom kernels. How do you balance security with the flexibility researchers and developers need?

#### Practice Problems

- Break a Linux system's boot process deliberately (e.g., misconfigure GRUB, corrupt initramfs, set wrong root filesystem). Document the symptoms and recovery procedure.
- Create a systemd service unit for a custom application. Configure: automatic restart on failure, resource limits, logging to journald, and a timer for periodic execution.
- Build an immutable server image using Packer or a cloud image builder. Deploy it, verify configuration, and demonstrate replacement without manual server modification.

---

### Lecture 9: Monitoring, Logging, and Observability

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

You cannot manage what you cannot see. This lecture examines how operating systems expose their internal state for monitoring and debugging: kernel counters, performance events, logs, tracing, and the observability stack that transforms raw data into actionable insight. The IT professional lives in the monitoring plane — detecting anomalies, diagnosing failures, and validating system health.

#### Key Topics

- **System Metrics:** CPU utilization (user, system, iowait, steal), memory usage (free, cached, buffered, available), disk I/O (reads/writes per second, queue depth, latency), network (packets, bytes, errors, drops), and process metrics (resident set size, CPU time, open files). Tools: `vmstat`, `iostat`, `mpstat`, `sar`, `top`, `htop`, `pidstat`.
- **Kernel Tracing:** eBPF (extended Berkeley Packet Filter) is the transformative Linux technology of the 2020s–2040s. It allows safe, efficient execution of custom programs in kernel space for tracing, profiling, and policy enforcement. Tools: `bpftrace` (high-level scripting), BCC (Python/C frontends), and kernel hooks for network filtering, security auditing, and performance analysis.
- **Logging:** The syslog protocol (rsyslog, syslog-ng), systemd journal (journald with structured, queryable logs), and Windows Event Log. Log management: centralized collection (Fluentd, Logstash), transport (TLS-encrypted), storage (Elasticsearch, Loki), and analysis (pattern detection, anomaly detection, correlation).
- **The Observability Trinity:**
  - **Metrics:** Time-series numeric data (Prometheus, InfluxDB, Grafana).
  - **Logs:** Structured or unstructured event records (ELK stack, Loki).
  - **Traces:** Distributed request flow tracking (Jaeger, Tempo, Zipkin).
  - **+ Profiling:** Continuous or on-demand code profiling (Pyroscope, Parca, Linux `perf`).
- **AI-Driven Observability:** By 2040, AI systems analyze observability data to: detect anomalies, correlate events across services, predict failures (predictive maintenance), suggest root causes, and auto-remediate routine issues. The IT professional's role: curating training data, validating AI recommendations, handling edge cases, and investigating incidents the AI cannot resolve.

#### Lecture Notes

The UoY Observability Platform ingests 50 TB of telemetry daily: 2 billion metrics, 500 million log lines, and 100 million traces. The platform uses a "hot/warm/cold" storage tier: recent data (7 days) in high-performance SSD; historical data (90 days) in object storage; archival data (7 years) in tape. Query latency targets: metrics <1 second, logs <5 seconds, traces <10 seconds.

Alerting follows the "symptom-based" approach recommended by Google SRE: alert on user-visible symptoms (high error rate, slow response time) rather than cause-based metrics (CPU usage, disk space). Cause-based alerts create noise and alert fatigue. The UoY aims for <5 alerts per on-call shift, each actionable and relevant.

#### Required Reading

- Gregg, B. (2036). *Systems Performance: Enterprise and the Cloud* (3rd ed.). Addison-Wesley.
- Borkmann, D., & Starovoitov, A. (2038). *BPF Performance Tools* (2nd ed.). Addison-Wesley.
- Google SRE Team. (2037). *Site Reliability Engineering: Observability and Monitoring* (2nd ed.). O'Reilly.

#### Discussion Questions

1. A monitoring dashboard shows 100 "critical" alerts per day, but 95% are false positives. How do you redesign the alerting strategy to reduce noise while maintaining coverage of genuine issues?
2. eBPF is powerful but requires kernel-level programming. What safeguards prevent malicious or buggy eBPF programs from destabilizing the system?
3. AI-driven observability promises to reduce manual diagnosis, but it also creates dependency on opaque models. How do you maintain human understanding of system behavior when AI handles routine troubleshooting?

#### Practice Problems

- Write a `bpftrace` script that traces file opens by a specific process and prints the filename, PID, and timestamp. Run it against a workload and analyze the output.
- Set up a Prometheus + Grafana monitoring stack for a small environment (5 nodes). Configure custom dashboards for CPU, memory, disk, and network. Set up one symptom-based alert and test it.
- Analyze a week's worth of application logs using log analysis tools. Identify: peak traffic patterns, error rate trends, and any correlated events that suggest a root cause for an observed latency spike.

---

### Lecture 10: Patch Management and Configuration Drift

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Systems change — through planned updates, emergency patches, and gradual drift. Managing this change is one of the most consequential IT responsibilities. This lecture examines patch management strategies, configuration management tools, and the immutable infrastructure patterns that eliminate drift by design.

#### Key Topics

- **Patch Management Lifecycle:** Identify (scan for vulnerabilities), Evaluate (assess risk and compatibility), Test (in staging environment), Approve (by change board or automated policy), Deploy (staged rollout), Verify (confirm patch applied and system functional), Document (audit trail). The UoY Critical Patch Policy: critical security patches applied within 72 hours; high patches within 2 weeks; medium/low patches during monthly maintenance windows.
- **Patching Strategies:**
  - **Rolling Updates:** Patch systems one at a time, maintaining service availability. Used for stateless services and containerized workloads.
  - **Canary Deployments:** Patch a small subset (1–5%) first, monitor for issues, then expand. Standard for high-risk changes.
  - **Blue-Green Deployments:** Maintain two identical environments; switch traffic from blue (current) to green (patched). Instant rollback capability.
  - **Maintenance Windows:** Scheduled downtime for patching. Still required for monolithic legacy systems that cannot be updated online.
- **Configuration Management:** Tools that enforce desired system state:
  - **Ansible:** Agentless, SSH-based, YAML playbooks. Excellent for ad-hoc tasks and gradual adoption.
  - **Puppet:** Model-driven, agent-based, declarative. Strong for large, stable environments.
  - **Chef:** Ruby-based, agent-based, imperative. Flexible but complex.
  - **SaltStack:** Agent-based or agentless, high-speed event-driven automation.
  - **Microsoft Endpoint Configuration Manager (MECM):** Windows-centric patch and configuration management.
- **Configuration Drift:** The gradual divergence of actual system state from desired state caused by manual changes, failed patches, or software updates. Detection: configuration scanning (CIS benchmarks, OpenSCAP), file integrity monitoring (AIDE, Tripwire), and infrastructure-as-code reconciliation (Terraform plan, Ansible diff). Remediation: automated remediation (Ansible playbooks, policy-as-code) or replacement (immutable infrastructure).

#### Lecture Notes

Patch management is risk management. Every patch carries a non-zero risk of breaking something. The IT professional balances: the risk of exploitation (delaying the patch) against the risk of instability (applying the patch). The UoY Patch Risk Matrix scores each patch by: CVSS severity, exploit availability, system criticality, and compatibility confidence. High-score patches get emergency deployment; low-score patches wait for the next window.

Configuration drift is the silent killer of reliability. A server that "worked fine for years" may have accumulated manual changes that make it impossible to reproduce or migrate. The UoY mandates: all production configuration must be defined in version-controlled code (Ansible playbooks, Terraform, or Kubernetes manifests). Manual changes are permitted only in emergencies and must be retroactively codified within 24 hours.

#### Required Reading

- CISA. (2039). *Patch Management Best Practices for Enterprise Environments*.
- Ansible. (2039). *Ansible for DevOps: Server and Configuration Management* (5th ed.).
- CIS. (2039). *CIS Benchmarks for Operating System Hardening*.

#### Discussion Questions

1. A critical vulnerability is announced with active exploitation. Your staging environment is inadequate to test the patch comprehensively. Do you deploy untested to production, delay for testing, or implement compensating controls? How do you decide?
2. Immutable infrastructure eliminates configuration drift but requires a mature CI/CD pipeline and fast rollback capability. What organizational prerequisites must exist before adopting immutability?
3. An engineer manually patched a production server during an incident but forgot to update the configuration repository. Three months later, the server is rebuilt from code and the patch is missing, causing a recurrence. What process changes prevent this?

#### Practice Problems

- Write an Ansible playbook that applies security patches to a fleet of Ubuntu servers, rebooting only if required, with a rolling update strategy (one server at a time, with health checks).
- Use OpenSCAP to scan a Linux system against the CIS benchmark. Review the findings, prioritize remediations, and apply the top 10 most critical fixes via automation.
- Design a patch management policy for a 1,000-server environment: patch classes, deployment windows, testing requirements, rollback procedures, and exception handling.

---

### Lecture 11: Troubleshooting Methodology and Root Cause Analysis

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

When systems fail, the IT professional is the diagnostician. This lecture formalizes troubleshooting as a systematic discipline: hypothesis generation, evidence gathering, isolation, reproduction, and resolution. It also covers root cause analysis (RCA) — the process of understanding not just what failed but why, and how to prevent recurrence.

#### Key Topics

- **The Troubleshooting Cycle:**
  1. **Observe:** What is the symptom? Who is affected? When did it start? What changed?
  2. **Hypothesize:** What could cause this symptom? Brainstorm without dismissing possibilities prematurely.
  3. **Test:** Design experiments that discriminate between hypotheses. Change one variable at a time.
  4. **Isolate:** Narrow the scope: application, library, OS, driver, firmware, hardware, network?
  5. **Resolve:** Apply the fix. Verify it works. Monitor for side effects.
  6. **Document:** Record the incident, diagnosis, and resolution for future reference.
- **Diagnostic Tools by Layer:**
  - **Hardware:** `dmesg`, `smartctl`, `ipmitool`, BMC logs, physical inspection.
  - **Boot:** GRUB recovery, single-user mode, initramfs shell, rescue disk.
  - **OS:** `journalctl`, `syslog`, `strace`, `ltrace`, `lsof`, `ps`, `top`, `vmstat`, `iostat`.
  - **Network:** `ping`, `traceroute`, `mtr`, `tcpdump`, `wireshark`, `ss`, `iptables -L`.
  - **Storage:** `df`, `du`, `mount`, `blkid`, `fsck`, `dd`, `fio`.
  - **Application:** Application logs, profiling, debugging (gdb, pdb), dependency checks.
- **Root Cause Analysis Methods:**
  - **5 Whys:** Ask "why" recursively until the fundamental cause is reached.
  - **Ishikawa (Fishbone) Diagram:** Categorize causes by category (people, process, technology, environment) to ensure comprehensive analysis.
  - **Fault Tree Analysis:** Top-down logical decomposition of failure modes.
  - **Timeline Reconstruction:** Building a precise chronological sequence of events leading to failure.
- **Blameless Postmortems:** The culture of learning from failure without assigning personal blame. Google's SRE book emphasizes: "Human error is a symptom of a deeper systemic problem." The goal is to fix the system, not the person. Postmortem documents include: timeline, impact assessment, root cause, action items, and lessons learned.

#### Lecture Notes

The UoY IT Department maintains a "Troubleshooting Compass" — a decision tree that guides engineers from symptom to diagnosis. It is not a rigid script but a framework for systematic thinking. Senior engineers mentor juniors by pairing on incidents, verbalizing their thought process: "I'm checking X because Y could cause the symptom; if X is normal, I'll check Z next."

A common pitfall: confirmation bias. Once an engineer forms a hypothesis, they may unconsciously seek confirming evidence and ignore disconfirming evidence. The department trains engineers to explicitly seek evidence that would falsify their leading hypothesis.

#### Required Reading

- Limoncelli, T. A., Chalup, S. R., & Hogan, C. J. (2037). *The Practice of System and Network Administration* (4th ed.). Addison-Wesley.
- Google SRE Team. (2037). *Site Reliability Engineering: Incident Response* (2nd ed.). O'Reilly.
- Kahneman, D. (2035). *Thinking, Fast and Slow* (Rev. ed.). Farrar, Straus and Giroux. [Chapters on cognitive bias]

#### Discussion Questions

1. A junior engineer spends 3 hours troubleshooting a network issue, eventually discovering the cable was unplugged. Was the time wasted, or was the systematic approach valuable? How do you build a culture where trivial root causes are accepted without ridicule?
2. Confirmation bias is a well-documented cognitive limitation. What specific practices (checklists, peer review, devil's advocacy) reduce its impact during high-pressure incident response?
3. A postmortem identifies a root cause but the proposed fix is expensive and politically difficult. How do you advocate for systemic fixes when leadership prefers quick patches?

#### Practice Problems

- Given a scenario (provided by instructor), perform a systematic troubleshooting exercise. Document your hypotheses, tests, and conclusions. Present to the class for critique.
- Facilitate a 5 Whys analysis for a hypothetical incident: a database corruption caused by a failed backup restore. Continue asking "why" until you reach organizational or cultural factors.
- Write a blameless postmortem for a real or hypothetical outage. Include: timeline, impact, root cause (with evidence), action items (with owners and deadlines), and what went well.

---

### Lecture 12: Synthesis — The OS Professional's Mindset

**Course:** IT103 — Operating Systems for IT Professionals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

This final lecture synthesizes IT103 into a coherent professional identity: the OS professional as systems thinker, empirical investigator, security guardian, and operational craftsman. It reflects on the enduring principles that transcend any specific OS version or technology trend.

#### Key Topics

- **Systems Thinking:** The OS is a system of interconnected subsystems: scheduling, memory, I/O, files, security, networking. A change in one subsystem propagates to others. The OS professional sees these connections: how memory pressure increases I/O via swapping; how a driver bug corrupts filesystem metadata; how a security patch changes performance characteristics.
- **Empirical Rigor:** Claims about OS behavior must be tested. "I think the scheduler is the problem" is a hypothesis; `perf sched` output is evidence. The OS professional trusts measurement over intuition, controlled experiments over anecdotes, and reproducible procedures over heroic improvisation.
- **Security by Design:** Security is not a layer painted on at the end; it is woven into every OS decision. The principle of least privilege, defense in depth, fail-secure defaults, and complete mediation are not abstract ideals but daily practices.
- **Operational Craftsmanship:** The OS professional takes pride in clean configuration, clear documentation, robust automation, and careful change management. They understand that 3 AM emergencies are often the result of decisions made at 3 PM weeks earlier. Craftsmanship is prevention.
- **The Norn of the Present:** In Norse mythology, Verðandi is the Norn who weaves the present — the thread of what is happening now. The OS professional is a Verðandi: they maintain the thread of running systems, detecting frays before they break, repairing what is damaged, and ensuring the continuity of digital life. Their work is not dramatic; it is persistent, attentive, and essential.

#### Lecture Notes

The course closes with a capstone troubleshooting exercise: a "broken" server (deliberately misconfigured by faculty) that students must diagnose and restore. The exercise tests: systematic methodology, tool proficiency, knowledge integration, and calm under pressure. The best performers are not necessarily those who fix the server fastest, but those who document their reasoning, verify their fixes, and prevent collateral damage.

The UoY IT Department's closing ritual for IT103: students are given a small brass key — a replica of the physical keys once used to lock server racks. The key is symbolic: the OS professional holds the keys to the kingdom, and with that power comes the duty to use it wisely.

#### Required Reading

- Limoncelli et al. (2037). *The Practice of System and Network Administration* (4th ed.). Addison-Wesley.
- Larrington, C. (Trans.). (2014). *The Poetic Edda*. Oxford University Press. [Völuspá, stanzas on fate and weaving]

#### Discussion Questions

1. Systems thinking requires understanding feedback loops, delays, and unintended consequences. Describe a feedback loop in OS resource management (e.g., memory pressure → swapping → I/O contention → CPU wait → throughput collapse) and how you would break the cycle.
2. Operational craftsmanship often conflicts with business urgency. How do you advocate for "doing it right" when leadership wants it done fast?
3. The brass key symbolizes trust and responsibility. What specific practices earn and maintain the trust placed in OS professionals?

#### Practice Problems

- Complete the capstone troubleshooting exercise. Submit a written report documenting: symptoms observed, hypotheses tested, evidence gathered, root cause identified, remediation applied, and preventive measures recommended.
- Write a "Personal Operating Philosophy" — a 1,000-word document articulating your approach to OS administration: values, principles, practices, and red lines you will not cross.
- Reflect on IT103 as a whole. Which lecture changed your thinking most significantly? What do you still find confusing? What are you most eager to explore in advanced courses?

---

## Final Examination Preparation

The IT103 final examination is a **comprehensive written and practical assessment** evaluating OS knowledge and operational skills. The examination consists of three parts:

### Part A: Written Examination (60 minutes)
Answer three of five essay questions:

1. **Kernel Architecture:** Compare monolithic, microkernel, and hybrid kernel designs. Use specific examples (Linux, Windows NT, QNX) to illustrate the trade-offs in performance, reliability, and security.

2. **Memory Management:** A server is experiencing severe performance degradation. `vmstat` shows high `si`/`so` (swap in/out) values. Analyze the memory subsystem to determine the cause and propose a remediation strategy that balances immediate relief with long-term capacity planning.

3. **File Systems and Storage:** Design a storage architecture for a research group generating 10 TB of experimental data per year, requiring: high throughput for active analysis, snapshots for experiment reproducibility, and 10-year archival retention. Justify your technology choices.

4. **Security Architecture:** An attacker compromises a web application and gains a shell as the web server user. Map the OS-level defenses (DAC, MAC, capabilities, sandboxing, namespaces) that could prevent or limit lateral movement. Identify any gaps in a default configuration.

5. **Virtualization and Containers:** A company runs 500 VMs and wants to migrate to containers for cost savings. Analyze the technical, operational, and security implications of this migration. What workloads should remain on VMs?

### Part B: Practical Examination (90 minutes)
Complete hands-on tasks in the UoY IT Lab:

- Diagnose and resolve a boot failure on a Linux system. Use recovery mode, initramfs debugging, and journal analysis.
- Configure a server with hardening requirements: SELinux enforcing, minimal services, firewall rules, and automated patching.
- Use eBPF/bpftrace to analyze a performance issue and write a script that captures the relevant kernel events.
- Set up centralized logging and alerting for a small environment (3–5 nodes).

### Part C: Operational Scenario (30 minutes, oral defense)
- Respond to a simulated incident: high CPU usage on a production database server.
- Walk through your diagnostic process, demonstrating tool usage and reasoning.
- Propose a fix and defend it against alternatives.

### Grading Rubric
| Criterion | Weight | Description |
|-----------|--------|-------------|
| Technical Knowledge | 25% | Understanding of OS subsystems, mechanisms, and interactions |
| Diagnostic Ability | 25% | Systematic troubleshooting, evidence gathering, and root cause identification |
| Security Awareness | 20% | Appropriate application of security controls and risk assessment |
| Practical Skills | 15% | Tool proficiency, configuration accuracy, and operational correctness |
| Communication | 15% | Clear documentation and oral presentation of technical reasoning |

*May your processes run clean, your memory never leak, and your boots be swift.* ᛟ

— University of Yggdrasil, Department of Information Technology, 2040
