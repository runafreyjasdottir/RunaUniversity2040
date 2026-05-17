# IT201: System Administration (Linux + Windows)
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4
**Prerequisites:** IT101 Introduction to Information Technology, IT103 Operating Systems for IT Professionals
**Description:** System administration is the art and science of keeping computing infrastructure alive, secure, and performant. This course covers both major server platforms — Linux (the dominant cloud and HPC operating system) and Windows Server (the backbone of enterprise IT) — with an emphasis on the principles that transcend any single platform. Students will learn user and permission management, filesystem architecture, service orchestration (systemd and Windows Service Control Manager), configuration automation (Ansible, Puppet, DSC), monitoring and observability, backup and disaster recovery, and security hardening. By 2040, the sysadmin's role has evolved: AI-assisted operations handle routine tasks, but human judgment remains essential for architecture decisions, incident response, and the ethical governance of autonomous infrastructure.

---

## Lectures

ᚠ **Lecture 1: The Sysadmin's Domain — Philosophy, Responsibility, and Craft**

### Overview

System administration is not merely a technical role; it is a stewardship. This lecture establishes the philosophical foundations of the craft: the sysadmin as caretaker of shared computational resources, the tension between stability and change, the principle of least privilege, and the operational mindset that distinguishes great administrators from adequate ones. We trace the profession's evolution from the "root" accounts of 1970s UNIX through the DevOps revolution to the AI-augmented operations of 2040.

### Lecture Notes

The word "administration" derives from the Latin *administrare* — to serve, to manage, to attend to. This etymology captures something essential about the craft that is lost in purely technical descriptions. A system administrator serves the users who depend on the systems; manages resources that are always finite; and attends to infrastructure that will, without constant care, decay. The sysadmin's first duty is not to the technology but to the people and purposes that the technology serves.

The operational mindset is a distinct cognitive stance. Where developers optimise for building — adding features, writing new code — sysadmins optimise for running — ensuring existing systems continue to function correctly under real-world conditions. This manifests in specific habits: monitoring before alerting, testing backups by restoring them, documenting procedures before they're needed at 3 AM, and treating every incident as a learning opportunity through blameless postmortems. The Site Reliability Engineering (SRE) movement, originating at Google in the early 2000s and codified in the 2016 *Site Reliability Engineering* book, formalised many of these instincts: Service Level Objectives (SLOs) define acceptable performance; error budgets govern the acceptable rate of failure; and toil — repetitive, automatable operational work — is treated as a bug to be engineered away.

The principle of least privilege, formalised by Saltzer and Schroeder in 1975, is the sysadmin's ethical north star. Every user, process, and service should operate with the minimum permissions necessary to perform its function — and no more. In practice, this means: never log in as root; use `sudo` with specific command restrictions; run services under dedicated, unprivileged accounts; and design permission models so that compromise of any single component limits the blast radius. On Windows, this translates to avoiding Domain Admin accounts for daily tasks, using Just Enough Administration (JEA) endpoints, and implementing tiered administrative models where Tier 0 (domain controllers) is strictly separated from Tier 1 (member servers) and Tier 2 (workstations).

By 2040, the sysadmin's role has been transformed by AI but not eliminated. Routine tasks — patch assessment, log triage, capacity forecasting — are handled by ML models with unprecedented accuracy. But system administration requires judgment that AI cannot yet replicate: understanding the business context that determines whether a 0.1% error rate is acceptable or catastrophic; navigating the organisational politics of a maintenance window that affects revenue-generating services; and making ethical decisions about data access, surveillance, and user privacy that algorithms can inform but not resolve. The 2040 sysadmin is less a mechanic and more a physician — diagnosing systemic health, prescribing interventions, and knowing when to operate and when to observe.

### Required Reading

- Limoncelli, T.A., Hogan, C.J., & Chalup, S.R. (2016). *The Practice of System and Network Administration*, 3rd Edition. Addison-Wesley. Chapters 1-3.
- Beyer, B., Jones, C., Petoff, J., & Murphy, N.R. (2016). *Site Reliability Engineering*. O'Reilly. Chapters 1-4.
- Saltzer, J.H. & Schroeder, M.D. (1975). "The Protection of Information in Computer Systems." *Proceedings of the IEEE*, 63(9).
- UoY Operational Philosophy Lab (2039). *Stewardship in the Age of Autonomous Systems: An Ethical Framework for 2040 Operations*.

### Discussion Questions

1. The SRE model treats reliability as a feature with an error budget. What are the risks of this framing? When might 99.9% reliability be insufficient, and when might 99% be perfectly adequate?
2. How does the principle of least privilege apply to AI agents that manage infrastructure autonomously? What permissions should an AI ops agent have, and what should be reserved for human approval?
3. System administration has been described as "the profession that disappears when it's done well." Is this a feature or a bug? How should sysadmins communicate their value?

---

ᚢ **Lecture 2: Linux System Architecture — The Kernel, systemd, and the Userspace Contract**

### Overview

This lecture establishes the technical foundation of Linux system administration. We examine the kernel's role as resource manager and security boundary, the systemd init system (which replaced SysV init and now manages services, sockets, timers, and mounts), the filesystem hierarchy standard, and the userspace contract — the stable kernel APIs that enable decades of binary compatibility. Students will understand boot process (UEFI → bootloader → kernel → initramfs → systemd → target), service unit files, and the cgroups/namespaces infrastructure that underpins containerisation.

### Lecture Notes

The Linux kernel is the absolute monarch of the system — a constitutional monarch, bound by stable API contracts, but a monarch nonetheless. It manages CPU scheduling (Completely Fair Scheduler, replaced in the 2030s by EEVDF — Earliest Eligible Virtual Deadline First), memory allocation (buddy allocator, slab allocator, transparent huge pages), device I/O (block layer with multi-queue scheduling), and network stack (with eBPF extensions that enable programmable packet processing without kernel modules). The kernel exposes its functionality through system calls — approximately 450 of them, stable since the 2.6 era — that userspace programs invoke through the C library (glibc, musl, or by 2040, the increasingly popular Cosmopolitan libc for truly portable binaries).

systemd, designed by Lennart Poettering and Kay Sievers and adopted as the default init system by most distributions between 2011-2015, represents a philosophical shift in system management. Where traditional init systems (SysV init, Upstart) managed only processes, systemd manages *units* — a unified abstraction that encompasses services (.service), sockets (.socket), devices (.device), mounts (.mount), timers (.timer), and more. A systemd service unit file declares not just what to run but under what conditions: which dependencies must be satisfied, what environment variables to set, what resource limits to apply, and how to handle failure (restart policies). systemd's socket activation allows services to be started on-demand when a connection arrives, reducing resource consumption for infrequently used services.

The cgroups (control groups) and namespaces infrastructure, which systemd leverages heavily, is the foundation of modern containerisation. Cgroups limit, account for, and isolate resource usage (CPU, memory, I/O) of process groups. Namespaces provide isolation of system resources: the PID namespace gives a process its own process tree; the network namespace gives it its own network stack; the mount namespace gives it its own filesystem view; the user namespace allows unprivileged users to create namespaces where they appear as root (with important security caveats). When Docker or Podman "starts a container," what actually happens is the orchestration of these kernel features — cgroups and namespaces — plus a filesystem image and some networking configuration. There is no kernel-level "container" object; containers are a userspace pattern built on kernel primitives.

The Filesystem Hierarchy Standard (FHS) defines where things go: `/bin` for essential user binaries, `/etc` for host-specific configuration, `/var` for variable data (logs, spools, databases), `/home` for user directories, `/tmp` for temporary files (cleared on boot on many 2040 distributions). Understanding the FHS is not pedantry — it is the difference between a system that can be administered by any experienced sysadmin and one that requires institutional knowledge to navigate. When you encounter a server where "the application is installed in /opt/custom-app-v3-final-FINAL," you are looking at technical debt in directory form.

### Required Reading

- Kerrisk, M. (2010). *The Linux Programming Interface*. No Starch Press. Chapters 1-3 (kernel overview), 7-9 (users and groups), 12 (system concepts).
- Poettering, L., Sievers, K., & Leemhuis, T. (2013). "systemd for Administrators." Series of blog posts, 0pointer.de.
- Linux Foundation. *Filesystem Hierarchy Standard*, Version 3.1.
- UoY Linux Systems Lab (2040). *systemd at 30: Evolution, Criticism, and the Future of Service Management*.

### Discussion Questions

1. systemd's critics argue it violates the Unix philosophy of "do one thing well" by absorbing udev, journald, resolved, and timedated into a single project. Its defenders argue these are separate binaries with well-defined interfaces. Which perspective is more persuasive, and what does this debate reveal about the Unix philosophy itself?
2. Containers are "just" cgroups + namespaces + filesystem image. What security properties does this combination provide, and what security properties does it NOT provide?
3. The stable kernel ABI allows binaries compiled decades ago to run on modern kernels. What are the costs of this stability? When, if ever, should stability be sacrificed?

---

ᚦ **Lecture 3: Windows Server Architecture — Active Directory, Group Policy, and the Enterprise Fabric**

### Overview

Windows Server is the foundation of enterprise IT infrastructure, and Active Directory is its central organising principle. This lecture covers the Windows Server architecture: the NT kernel, the registry as configuration database, the Service Control Manager, and the security model (access tokens, security descriptors, Kerberos authentication). We focus on Active Directory Domain Services — the LDAP-compatible directory that provides authentication, authorisation, and policy enforcement for Windows domains — and Group Policy, the mechanism for declaratively configuring thousands of machines from a central console.

### Lecture Notes

Windows Server's architecture differs fundamentally from Linux's, and understanding these differences is essential for cross-platform administration. The NT kernel (the same kernel that powers desktop Windows, with server-specific tuning) is a hybrid kernel — neither purely monolithic like Linux nor purely microkernel like MINIX. It provides the same core abstractions — processes, threads, virtual memory, I/O — but organises them differently. The Windows API (Win32) is the stable interface, preserved across decades for backward compatibility; the Native API (NT API), used internally and by certain low-level tools, is less stable but more powerful. Understanding the distinction is important: sysadmins interact with Win32; kernel-mode drivers interact with the NT API.

The registry is simultaneously Windows's greatest administrative innovation and its most persistent headache. It is a hierarchical database that stores configuration for the kernel, device drivers, services, and applications — a single, structured, machine-parseable configuration store that is a genuine improvement over the scattered text files of traditional UNIX (a gap Linux partially closed with systemd's configuration model and `/etc` conventions). The registry's problems are operational: it is a single point of corruption; its binary format makes disaster recovery difficult; and applications abuse it by storing runtime state alongside configuration. By 2040, the trend is toward "registry light" — storing application configuration in JSON/YAML files under `%ProgramData%` and using the registry only for OS-level and COM component settings — but legacy systems keep the registry administrator-relevant.

Active Directory Domain Services (AD DS) is the crown jewel of Windows Server. At its core, AD is an LDAP v3-compliant directory service with a multi-master replication model, Kerberos-based authentication, and a flexible schema. The domain is the security boundary: all domain controllers in a domain replicate with each other, and trust relationships between domains (or forests of domains) enable cross-domain resource access. AD's organisational unit (OU) hierarchy enables delegated administration — the Help Desk group can reset passwords for users in the "Branch Offices" OU but not in the "Executive" OU — without granting broader domain privileges. Group Policy Objects (GPOs), linked to sites, domains, or OUs, apply registry-based policies, security settings, software installation rules, and (by 2040) configuration-as-code declarations to machines and users.

The operational reality of AD is that it accumulates complexity over time. Organisations that have been on Active Directory for 20+ years often have GPOs whose purpose no living administrator remembers, OUs that reflect reorganisations from a decade ago, and schema extensions from applications that were decommissioned years ago. The AD administrator's most important skill is not creating new objects but understanding the existing ones well enough to clean up without breaking anything. Microsoft's AD Recycle Bin (introduced in Windows Server 2008 R2), AD Administrative Center, and by 2040, AI-assisted GPO analysis tools that identify redundant and conflicting policies — all exist to help manage this accumulated complexity.

### Required Reading

- Russinovich, M., Solomon, D., Ionescu, A., & Yosifovich, P. (2017). *Windows Internals*, 7th Edition. Microsoft Press. Chapters 1-4 (system architecture), 7 (security).
- Microsoft Docs. "Active Directory Domain Services Overview." Windows Server 2040 documentation.
- Desmond, B., et al. (2013). *Active Directory*, 5th Edition. O'Reilly.
- UoY Enterprise Infrastructure Lab (2040). *Legacy AD: Managing 30 Years of Accumulated Configuration*.

### Discussion Questions

1. The registry centralises configuration but creates a single point of corruption. Text-file configuration is distributed but harder to manage at scale. Which model is better for server infrastructure, and why?
2. Active Directory Group Policy enables centralised administration of thousands of machines. What are the risks of this power? What safeguards should prevent a single GPO mistake from affecting the entire organisation?
3. AD's multi-master replication model means changes can be made on any domain controller. Under what conditions could this lead to conflicts, and how does AD resolve them?

---

ᚨ **Lecture 4: Users, Groups, and Permissions — The Authorisation Architecture**

### Overview

Every system administration decision ultimately comes down to who can do what. This lecture covers the permission architectures of Linux (POSIX discretionary access control, ACLs, capabilities) and Windows (access tokens, security descriptors, ACLs, mandatory integrity control). We examine best practices for user and group management, the role of centralised authentication (LDAP, Kerberos, and by 2040, passkey-based enterprise identity), and the principle of separating identity (who you are) from authorisation (what you're allowed to do).

### Lecture Notes

POSIX permissions — the `rwx` triple for owner, group, and others — are the simplest permission model that works. A file or directory has nine permission bits plus three special bits (setuid, setgid, sticky), and the kernel enforces them on every access. The model's elegance is its limitation: it supports exactly one owner and one group, and the "others" category provides no granularity. When a system needs more complex access control — allowing two different groups different levels of access to the same file — POSIX ACLs (Access Control Lists, implemented via the `setfacl` and `getfacl` commands on Linux) extend the model with named users and groups. By 2040, rich ACL support is standard on all Linux filesystems, though the mental model remains more complex than the simple `rwx` triad.

Linux capabilities, introduced in kernel 2.2 (1999), address a fundamental problem of the POSIX model: the all-or-nothing nature of root. Traditionally, a process either runs as root (UID 0, full power) or as an unprivileged user. Capabilities decompose root's power into approximately 40 distinct privileges: `CAP_NET_BIND_SERVICE` to bind to ports below 1024, `CAP_SYS_TIME` to set the system clock, `CAP_SYS_ADMIN` for a broad set of administrative operations. A web server can be granted `CAP_NET_BIND_SERVICE` without being root, dramatically reducing the damage from a compromise. By 2040, capability-aware service design is standard practice — systemd unit files routinely specify `CapabilityBoundingSet=` and `AmbientCapabilities=` to restrict what services can do even if compromised.

Windows permissions are conceptually richer but operationally more complex than POSIX permissions. A Windows access token — created at login and attached to every process — contains the user's SID (Security Identifier), group SIDs, privileges (analogous to Linux capabilities), and integrity level. When a process attempts to access a securable object (file, registry key, service, etc.), the Security Reference Monitor compares the access token against the object's security descriptor, which contains a Discretionary Access Control List (DACL — who is allowed/denied what) and a System Access Control List (SACL — what access attempts should be audited). Windows ACLs support allow and deny entries (deny takes precedence), and inheritance flags control how permissions propagate to child objects.

Both platforms support centralised authentication. On Linux, SSSD (System Security Services Daemon) connects to LDAP directories and Kerberos realms, enabling users to authenticate against a central directory rather than local `/etc/passwd`. On Windows, domain-joined machines authenticate against domain controllers via Kerberos, with NTLM as a fallback (deprecated but still present in 2040 for legacy compatibility). The trend in both ecosystems is toward passwordless authentication: passkeys (FIDO2/WebAuthn) for interactive login, certificate-based authentication for services, and just-in-time access (temporary, audited privilege elevation) replacing standing administrator accounts. The 2040 sysadmin rarely has permanent root or Domain Admin access; they request it for specific tasks and it is automatically revoked when the task completes.

### Required Reading

- Nemeth, E., Snyder, G., Hein, T.R., Whaley, B., & Mackin, D. (2017). *UNIX and Linux System Administration Handbook*, 5th Edition. Chapter 3 (access control).
- Kerrisk, M. (2010). *The Linux Programming Interface*. Chapter 39 (capabilities).
- Microsoft Docs. "Access Control Overview." Windows App Development documentation.
- UoY Identity Lab (2040). *Passwordless Enterprise: Five Years of FIDO2 in Production Infrastructure*.

### Discussion Questions

1. Linux capabilities fragment root's power into ~40 distinct privileges. In practice, `CAP_SYS_ADMIN` is described as "the new root" because it grants so much. Is the capability model a genuine security improvement, or does it just move the problem?
2. Windows ACLs support deny entries that override allow entries. This is powerful but creates confusing configurations. Under what circumstances is a deny ACE genuinely necessary rather than a sign of poor group design?
3. Just-in-time access eliminates standing administrator accounts. What happens when the JIT access system itself goes down? How do you design a break-glass procedure that is secure enough to exist but accessible when needed?

---

ᚱ **Lecture 5: Filesystems and Storage — ZFS, NTFS, and the Data Layer**

### Overview

Data persistence is the sysadmin's ultimate responsibility. This lecture covers modern filesystem architecture: the design trade-offs of ZFS (copy-on-write, checksumming, snapshots, RAID-Z), NTFS (journaling, ACLs, compression, deduplication in Windows Server), and the Linux ecosystem (ext4, XFS, Btrfs). We examine RAID levels, LVM (Logical Volume Manager), Storage Spaces on Windows, and the 2040 storage landscape: NVMe-oF (NVMe over Fabrics), computational storage, and AI-driven tiering that moves data between performance and capacity layers without human intervention.

### Lecture Notes

ZFS, created at Sun Microsystems and released as open source in 2005, represents a philosophical maximalism in filesystem design: the filesystem should handle everything. ZFS combines the roles traditionally split between filesystem, volume manager, and RAID controller into a single integrated system. Its copy-on-write (COW) design means data is never overwritten; writes go to new blocks, and the old blocks remain until the transaction completes. This enables atomic updates (the filesystem is always consistent, eliminating fsck), snapshots (nearly instant, consuming only the space of changed blocks), and checksumming (every block is verified on read, detecting and — with redundancy — correcting silent data corruption). ZFS's send/receive enables efficient replication: send a snapshot's data stream to another system and receive it into a filesystem there, transferring only changed blocks.

The Linux filesystem ecosystem offers multiple mature options. ext4, the direct descendant of ext2 (1993), is the most widely deployed Linux filesystem — stable, well-tested, and performant for most workloads. Its limitations (no built-in checksumming, limited snapshots) have driven adoption of XFS (excellent for large files, online resizing, and by 2040, reflink support for COW-style snapshots) and Btrfs (Linux's answer to ZFS, with COW, snapshots, and built-in RAID, though its RAID5/6 implementation was unstable for many years and remains approached cautiously in 2040). The LVM (Logical Volume Manager) provides storage abstraction above the filesystem layer — physical volumes are combined into volume groups, from which logical volumes are carved — enabling online resizing, snapshots (via thin provisioning), and storage migration without unmounting.

NTFS, Windows' primary filesystem since Windows NT 3.1 (1993), is a journaling filesystem with rich metadata support. Its Master File Table (MFT) stores metadata about every file, including multiple data streams per file (the primary data stream plus alternate data streams, a feature that is both powerful and a persistent malware hiding technique). The NTFS ACL model integrates with the Windows security architecture described in Lecture 4. ReFS (Resilient File System), introduced in Windows Server 2012, is Microsoft's next-generation filesystem that incorporates checksumming, storage spaces integration, and (by 2040) block cloning for VM and database workloads — but NTFS remains the default for most deployments due to its maturity and tooling ecosystem.

The 2040 storage landscape is defined by speed and intelligence. NVMe drives, connected directly to the PCIe bus, achieve latencies measured in microseconds. NVMe-oF (NVMe over Fabrics) extends this performance across the network using RDMA (Remote Direct Memory Access), enabling storage arrays that feel like local disks to servers connected via high-speed fabric. Computational storage — SSDs with onboard processors — offloads compression, encryption, and even database query execution to the storage device itself. AI-driven tiering, now standard in enterprise storage arrays, continuously analyses access patterns and can be configured with policy-based objectives rather than manual LUN (Logical Unit Number) configuration. The sysadmin's relationship with storage has shifted from manual provisioning to policy declaration.

### Required Reading

- Bonwick, J., et al. (2003). "The Zettabyte File System." *Proceedings of the 2nd USENIX Conference on File and Storage Technologies*.
- Oracle. *ZFS Administration Guide*. Oracle Solaris documentation.
- Microsoft Docs. "NTFS Overview" and "ReFS Overview." Windows Server 2040 documentation.
- UoY Storage Architecture Lab (2040). *Computational Storage at Scale: A Two-Year Production Study*.

### Discussion Questions

1. ZFS combines filesystem, volume management, and RAID into a single system. What are the benefits of this integration, and what are the risks of the resulting complexity?
2. Silent data corruption — bit flips in stored data that go undetected — has been observed at scale. ZFS and ReFS detect and correct this; ext4 does not. Should checksumming be mandatory for all production filesystems?
3. AI-driven storage tiering promises optimal data placement without human intervention. What performance anomalies might machine learning introduce that a human administrator would have caught?

---

ᚲ **Lecture 6: Service Management and Process Supervision**

### Overview

Services are the reason servers exist. This lecture covers service lifecycle management on both platforms: systemd service units (Type=simple/forking/oneshot/notify, restart policies, dependencies, resource controls) and Windows Service Control Manager (service accounts, recovery actions, delayed start). We examine process supervision patterns — health checking, graceful shutdown, crash loops — and the operational practices that keep services running: log management (journald, Windows Event Log), resource monitoring (cgroups resource accounting, Windows Performance Counters), and the "cattle, not pets" philosophy of service management.

### Lecture Notes

A service is a long-running process that provides a function to other processes or users. The sysadmin's job, at its most concrete, is ensuring that the right services are running with the right configuration and the right resource allocations. On Linux, systemd service units are the standard mechanism. A service unit file declares *what* to run (`ExecStart=`), *how* to run it (`User=`, `Group=`, environment variables, working directory), *when* to run it (dependency ordering via `After=`/`Before=` and requirement declarations via `Requires=`/`Wants=`), and *what to do when it fails* (`Restart=on-failure`, `RestartSec=`, `StartLimitBurst=`). The `Type=` setting is particularly important: `simple` (default) assumes the process is ready immediately; `forking` expects the process to fork and the parent to exit; `notify` (preferred for modern services) expects the service to send a readiness notification via `sd_notify()`; `oneshot` is for services that run once and exit.

Windows Service Control Manager (SCM) provides analogous functionality with a different architecture. Windows services are executables that conform to the Service Main / Service Control Handler interface, enabling the SCM to start, stop, pause, and query them. Service accounts — the identities under which services run — are a critical security consideration: the LocalSystem account has full local privileges; NetworkService has reduced privileges but can authenticate to network resources as the machine account; dedicated Managed Service Accounts (MSAs) and Group Managed Service Accounts (gMSAs), introduced in Windows Server 2008 R2 and Windows Server 2012 respectively, provide automatic password management and are the recommended approach for 2040 deployments.

The "cattle, not pets" philosophy, popularised by the cloud computing era, captures a profound operational shift. In the pet model, servers are individual, named, cared-for machines — if one gets sick, you nurse it back to health. In the cattle model, servers are numbered, interchangeable, and replaced rather than repaired. This philosophy, enabled by configuration management and immutable infrastructure, reduces operational toil and eliminates configuration drift. However, the metaphor is incomplete: a herd of cattle still requires a rancher. The sysadmin's role shifts from nursing individual servers to designing the systems that automatically provision, configure, and replace them. By 2040, most production infrastructure follows the cattle model — servers that run for more than a few days without being replaced are the exception — but databases, legacy applications, and specialised hardware still require pet-level care.

Process supervision patterns transcend any specific init system. A well-designed service: (1) logs to stdout/stderr (leaving log collection to the infrastructure), (2) handles SIGTERM gracefully (finishing in-flight work before exiting), (3) implements health checks (HTTP `/health` endpoint or equivalent), (4) exports metrics in a standard format (Prometheus exposition format has become the de facto standard by 2040), and (5) is configured via environment variables or a single config file, not command-line flags scattered across init scripts. When a service crashes, the sysadmin's questions are: did it leave a core dump? What do the logs show? Is this part of a pattern (crash loop)? And, most importantly, what was the *first* thing that went wrong — because subsequent errors are often cascading symptoms, not root causes.

### Required Reading

- Freedesktop.org. "systemd.service — Service unit configuration." systemd documentation.
- Microsoft Docs. "Service User Accounts." Windows Server documentation.
- Beyer, B., et al. (2016). *Site Reliability Engineering*. Chapter 5: "Toil" and Chapter 6: "Monitoring Distributed Systems."
- UoY Service Reliability Lab (2039). *Crash Loop Diagnosis: Pattern Recognition for Automated Incident Response*.

### Discussion Questions

1. The "cattle, not pets" philosophy promises operational efficiency but introduces new failure modes (e.g., a bad image causing all cattle to be born sick). What guardrails prevent a single configuration change from destroying an entire herd?
2. systemd's `Type=notify` provides precise readiness signalling, but requires services to implement `sd_notify()`. Many applications don't. What are the alternatives, and what are their limitations?
3. When a service crashes and automatically restarts, the underlying problem may persist, creating a crash loop. How should monitoring systems distinguish between a transient crash and a crash loop requiring human intervention?

---

ᚷ **Lecture 7: Configuration Management and Infrastructure as Code**

### Overview

Manual configuration is the enemy of reliability. This lecture covers the tools and philosophies of declarative configuration management: Ansible (agentless, SSH-based, YAML playbooks), Puppet (agent-based, declarative language, resource abstraction layer), and the infrastructure-as-code paradigm (Terraform, Pulumi, Bicep). We examine the principles that underpin all of these tools — idempotency, convergence, desired state management — and the testing and validation practices that prevent configuration errors from reaching production.

### Lecture Notes

Infrastructure as Code (IaC) is the practice of managing infrastructure — servers, networks, load balancers, firewall rules — through machine-readable definition files rather than manual processes. The insight is that the same practices that improved software quality — version control, code review, automated testing, continuous integration — can improve infrastructure quality. A Terraform configuration in a git repository is auditable (who changed the firewall rule, when, and why?), reproducible (the same configuration applied to a different environment produces the same infrastructure), and testable (policy-as-code tools like Open Policy Agent validate configurations before they're applied). By 2040, IaC is not a best practice; it is the only practice — infrastructure not defined in code is considered legacy technical debt.

Ansible represents the agentless, push-based approach to configuration management. An Ansible playbook is a YAML file that declares the desired state of a system: packages to install, files to create, services to run, users to manage. Ansible connects to target systems via SSH (Linux) or WinRM (Windows), executes modules (Python scripts for Linux, PowerShell scripts for Windows) that converge the system toward the desired state, and reports results. The agentless design means no infrastructure beyond SSH/WinRM access is required — a significant operational advantage. However, Ansible's push model means it only runs when invoked; it cannot detect and correct configuration drift between runs (though by 2040, Ansible Semaphore and AWX provide scheduled and event-driven execution).

Puppet represents the agent-based, pull-based approach. A Puppet agent runs on each managed node, periodically (typically every 30 minutes) connecting to the Puppet server, retrieving its catalog (the compiled declaration of the node's desired state), and converging the local system to match. This model detects and corrects drift automatically — if someone manually changes a file that Puppet manages, the next agent run will restore it. Puppet's declarative language (originally a Ruby DSL, now with a YAML-based alternative) enables expressing complex dependencies and resource ordering. By 2040, Puppet and Ansible have largely converged in capability; the choice between them is primarily about operational philosophy (push vs. pull) and organisational familiarity.

The testing of infrastructure code is the frontier that separates mature operations from immature ones. Static analysis (linting playbooks, validating Terraform plans) catches syntax errors and known anti-patterns. Unit testing (using test frameworks like Molecule for Ansible roles) validates individual components in isolation. Integration testing provisions real (though ephemeral) infrastructure, applies the configuration, and runs validation tests — a practice enabled by cloud APIs that make provisioning a test environment as fast as writing the configuration. Policy-as-code (Open Policy Agent's Rego language, HashiCorp Sentinel) enforces organisational rules: "no S3 bucket may be publicly readable," "all VMs must have a specific monitoring agent installed." These tests run in CI/CD pipelines before any configuration reaches production.

### Required Reading

- Morris, K. (2016). *Infrastructure as Code: Managing Servers in the Cloud*. O'Reilly.
- Geerling, J. (2020). *Ansible for DevOps*. LeanPub.
- Loope, J. (2019). *Puppet 5 Essentials*. Packt Publishing.
- Brikman, Y. (2019). *Terraform: Up & Running*, 2nd Edition. O'Reilly.
- UoY Infrastructure Reliability Lab (2040). *Testing Infrastructure Code: A Survey of Practices Across 500 Organisations*.

### Discussion Questions

1. Ansible's agentless model means it can't detect drift between runs. Puppet's agent model corrects drift but requires agent infrastructure. Which approach results in more reliable systems in practice?
2. Infrastructure code can be version-controlled, but the *state* of running infrastructure (the actual state vs. the declared state) may diverge. How should operations teams detect and resolve state drift?
3. Policy-as-code tools enforce rules programmatically. But who writes the policies, and who enforces the policy writers? What governance model prevents policy-as-code from becoming "security theatre"?

---

ᚹ **Lecture 8: Monitoring, Observability, and the Art of Knowing**

### Overview

You cannot administer what you cannot see. This lecture covers the monitoring and observability stack: metrics (Prometheus, Grafana, Windows Performance Counters), logs (Elasticsearch/OpenSearch, Loki, Windows Event Log), traces (OpenTelemetry, distributed tracing), and the 2040 evolution toward AI-assisted observability. We distinguish between monitoring (known unknowns — "is the CPU above 90%?") and observability (unknown unknowns — "why are users experiencing latency?"), and examine the operational practices: alert design (avoiding alert fatigue), runbooks (making incident response repeatable), and the dashboard as a tool for understanding, not decoration.

### Lecture Notes

Monitoring is the systematic collection and analysis of metrics to answer the question "is the system working correctly?" The traditional approach — check-based monitoring (Nagios, Icinga, Zabbix) — defines explicit checks (is port 443 responding? is disk usage below 90%?) and alerts when they fail. This approach works well for known failure modes but fails for complex systems where failures emerge from interactions between components, not from individual component failures. The 2040 consensus is that check-based monitoring is necessary but insufficient; it must be complemented by the observability paradigm.

Observability, a term borrowed from control theory by the software engineering community in the late 2010s, is the ability to understand a system's internal state from its external outputs. In practice, this means instrumenting systems to emit three signal types: metrics (numerical time-series data — request rates, error rates, latency distributions), logs (immutable, timestamped records of discrete events), and traces (records of the path of a single request through a distributed system, showing each service it touched and how long each step took). The OpenTelemetry project, formed by the merger of OpenTracing and OpenCensus in 2019 and now a CNCF graduated project, provides a vendor-neutral standard for emitting and collecting all three signal types.

The alerting problem is the hardest part of monitoring. Too many alerts lead to alert fatigue — the sysadmin learns to ignore them, including the critical one buried in the noise. Too few alerts mean problems go undetected. The SRE approach is to alert on symptoms (user-visible problems — "error rate above SLO") rather than causes (system-level metrics — "CPU above 90%"), and to page only for conditions that require immediate human action. Everything else goes to a ticket queue or a dashboard. Alert design is a social and cognitive problem, not a technical one. By 2040, AI-assisted alert correlation — grouping related alerts, suppressing cascading noise, and suggesting root causes based on historical incident patterns — has reduced but not eliminated the alert fatigue problem.

Dashboards deserve special attention because they are both the most visible and the most abused tool in the monitoring toolbox. A well-designed dashboard tells a story: "here is the system's current health, here is how it relates to the SLOs, here is what changed recently." A poorly designed dashboard is a wall of numbers — every metric the team could think of, displayed without context or prioritisation. The dashboard design principle: every element on a dashboard should enable a decision. If a graph doesn't help the viewer decide whether to investigate, escalate, or ignore, it doesn't belong on the dashboard. By 2040, AI-generated dashboards that adapt to the viewer's role and current context are standard, but the principle remains: the purpose of visibility is action.

### Required Reading

- Beyer, B., et al. (2016). *Site Reliability Engineering*. Chapters 6 (Monitoring), 10 (Practical Alerting), 11 (Being On-Call).
- Turnbull, J. (2014). *The Art of Monitoring*. Self-published.
- OpenTelemetry Documentation. "Concepts" and "Specification." opentelemetry.io.
- UoY Observability Research Group (2040). *Alert Fatigue in the Age of AI Assistance: A Controlled Study*.

### Discussion Questions

1. The distinction between "monitoring" (known unknowns) and "observability" (unknown unknowns) is now mainstream. But is observability truly achievable, or is it an asymptote — we can get arbitrarily close but never fully understand a complex system?
2. Alerting on symptoms rather than causes sounds ideal, but what if the only symptom is subtle and slow — a gradual latency increase over weeks? At what point does a metric become an alert?
3. Dashboards that "tell a story" require the dashboard designer to understand the system deeply. What happens when the person who designed the dashboard leaves the organisation? How do you make dashboards maintainable?

---

ᚺ **Lecture 9: Backup, Recovery, and the Certainty of Failure**

### Overview

Backups are not about preventing failure — they are about surviving it. This lecture covers backup strategy: the 3-2-1 rule (three copies, two different media, one offsite), incremental vs. differential vs. full backups, Recovery Point Objective (RPO — how much data can you afford to lose?) and Recovery Time Objective (RTO — how long can you afford to be down?). We examine backup technologies (rsync, Veeam, Windows Server Backup, cloud-native snapshots), the critical importance of *testing* backups (a backup you haven't restored is a hope, not a strategy), and the 2040 evolution toward continuous data protection and ransomware-resilient architectures.

### Lecture Notes

The sysadmin's relationship with backups is defined by a paradox: backups are the most boring, most important thing you will ever do. No one gets promoted for running good backups. But when a database server's storage array suffers a double-disk failure, or a ransomware attack encrypts the entire filesystem, or a fat-fingered `rm -rf /` command meets an unprotected root shell — the backup is the difference between a bad day and a career-ending disaster. The 3-2-1 rule, formulated by photographer Peter Krogh for digital photo workflows and adopted by the IT community, provides the minimum standard: three copies of data (production + two backups), on two different media types (e.g., disk and tape, or two different storage systems), with one copy offsite (geographically separated from the primary site).

RPO and RTO translate business requirements into technical specifications. Recovery Point Objective answers: "up to how much data loss is acceptable?" An RPO of one hour means backups must be taken at least hourly. An RPO of zero means synchronous replication — every write must be committed to the backup site before it is acknowledged to the application, which imposes latency and availability constraints. Recovery Time Objective answers: "how long can the service be unavailable?" An RTO of four hours means the restoration process must complete within four hours — which constrains backup format choices (full restores are faster than replaying days of transaction logs), network bandwidth, and the availability of replacement hardware.

Backup technologies have evolved dramatically. Traditional tape backup — LTO (Linear Tape-Open), now at generation 12+ with native capacity exceeding 100TB per cartridge — remains relevant for archival data and air-gapped ransomware protection (a tape in a vault has no network interface to attack). Disk-based backup (snapshots, replication, purpose-built backup appliances) provides faster restores and random access. Cloud-native backup leverages the cloud provider's snapshot and replication capabilities. By 2040, continuous data protection (CDP) — journaling every write so that any point-in-time can be restored — is standard for critical databases, effectively reducing RPO to seconds.

Testing backups is where most organisations fail. A backup that hasn't been restored is not a backup; it is a belief. Restore testing must be regular (monthly at minimum), automated (scripted restores to ephemeral test environments with integrity verification), and comprehensive (testing individual file restores, full system restores, and application-level consistency). The 2040 state of the art is "chaos restore" — the backup system periodically, without warning, restores a random subset of data to a test environment and verifies its integrity, reporting only failures. This turns the backup system from a passive insurance policy into an active, continuously validated safety net.

### Required Reading

- Limoncelli, T.A., et al. (2016). *The Practice of System and Network Administration*. Chapter 26 (Backups).
- Preston, W.C. (2007). *Backup & Recovery*. O'Reilly.
- NIST SP 800-209: "Security Guidelines for Storage Infrastructure." NIST, 2020.
- UoY Resilience Lab (2040). *Chaos Restore: Continuous Validation of Backup Integrity at Scale*.

### Discussion Questions

1. The 3-2-1 rule was formulated in the era of physical media. Does it remain adequate in the cloud era, where "offsite" may mean a different availability zone of the same cloud provider? What would a 2040-era backup rule look like?
2. Ransomware attacks specifically target backups — deleting them, encrypting them, or compromising the backup infrastructure. How should backup architecture change to be ransomware-resilient?
3. Continuous data protection reduces RPO to nearly zero but dramatically increases storage costs. For what classes of data is CDP justifiable, and for what classes is hourly or daily backup sufficient?

---

ᚾ **Lecture 10: Security Hardening and the Defensive Posture**

### Overview

System administration and security administration were once separate roles; by 2040, they are inseparable. This lecture covers the hardening practices that every sysadmin must internalise: the principle of least functionality (disable everything not needed), patch management (balancing speed against stability), network segmentation and firewall configuration, host-based intrusion detection, and the secure defaults that should be established before a server ever connects to a network. We examine security benchmarks (CIS Benchmarks, DISA STIGs) as operational standards and discuss the tension between security and usability.

### Lecture Notes

Security hardening begins with a simple principle that is difficult to execute: the system should do only what it is supposed to do, and nothing else. Every installed package, every running service, every open port, every user account is a potential attack surface. The hardening process is therefore a process of subtraction: remove unnecessary packages, disable unnecessary services, close unnecessary ports, delete unnecessary accounts. On Linux, this means starting with a minimal installation (no graphical environment, no development tools, no compilers on production servers) and adding only what the application requires. On Windows, this means using Server Core (the headless, GUI-free installation option) whenever possible and removing roles and features that aren't needed.

Patch management is the sysadmin's most thankless task and most critical security function. The rhythm is relentless: vendors release patches, researchers publish vulnerabilities, and attackers reverse-engineer patches to develop exploits — often within hours. The sysadmin must balance the security risk of delaying a patch (exposure window) against the operational risk of deploying it (potential for regressions). The 2040 consensus is a tiered approach: critical security patches are deployed within 24 hours to all systems; important patches within a week; moderate patches within a month. Testing happens in parallel, not before deployment — the risk of unpatched vulnerabilities outweighs the risk of patch-induced regressions for all but the most safety-critical systems. Automated rollback (via filesystem snapshots or VM snapshots taken before patching) provides a safety net.

Network segmentation is defence in depth applied to infrastructure architecture. The flat network — where every server can reach every other server — is a ransomware operator's dream. Segmentation divides the network into zones with controlled boundaries: a DMZ for internet-facing services, an application zone for backend services, a data zone for databases, a management zone for administrative access. Firewall rules between zones enforce the principle of least privilege at the network level: the web server can reach the database on port 5432, but the database cannot initiate connections to the web server; administrative access is restricted to a jump host in the management zone. By 2040, microsegmentation — applying firewall policy at the individual workload level rather than the subnet level — is standard in virtualised and containerised environments, enabled by software-defined networking.

Security benchmarks provide operational standards that replace ad hoc judgment. The Center for Internet Security (CIS) publishes consensus-developed benchmarks for most operating systems and applications, with specific, auditable recommendations: "Ensure permissions on /etc/passwd are configured" → `chmod 644 /etc/passwd`. The Defense Information Systems Agency (DISA) publishes Security Technical Implementation Guides (STIGs) for U.S. Department of Defense systems, with more stringent requirements. By 2040, compliance-as-code tools (InSpec, OpenSCAP) can automatically audit systems against these benchmarks and report compliance status, making security posture a measurable, trackable metric rather than a subjective assessment.

### Required Reading

- Center for Internet Security. "CIS Benchmarks." cisecurity.org. [Relevant OS and application benchmarks]
- Limoncelli, T.A., et al. (2016). *The Practice of System and Network Administration*. Chapter 24 (Security).
- NIST SP 800-53: "Security and Privacy Controls for Information Systems and Organizations." Revision 6.
- UoY Security Operations Lab (2040). *Patch Velocity vs. Stability: A Longitudinal Analysis of 10,000 Production Systems*.

### Discussion Questions

1. Patch management requires balancing security risk (delay) against operational risk (regression). Is "patch immediately and rely on automated rollback" a valid strategy, or does it create unacceptable availability risk?
2. CIS benchmarks provide specific, auditable controls (e.g., "ensure password minimum length is 14 characters"). But compliance with a benchmark does not guarantee security. What does a benchmark miss?
3. Microsegmentation promises fine-grained network security, but its complexity grows with the number of workloads. At what point does the operational burden of managing microsegmentation outweigh its security benefits?

---

ᛁ **Lecture 11: Automation and Scripting — The Sysadmin's Leverage**

### Overview

A sysadmin who does something twice without scripting it is doing it wrong — the third time, at least. This lecture covers the scripting languages and automation patterns that multiply the sysadmin's effectiveness: Bash (the universal Linux glue language), PowerShell (the Windows administrative interface that became cross-platform), Python (for complex logic beyond what shell scripts handle cleanly), and the automation frameworks (Ansible playbooks, PowerShell DSC, cron/systemd timers/task scheduler) that turn scripts into reliable, scheduled, monitored operations.

### Lecture Notes

Bash is the lingua franca of Linux system administration — not because it is the best programming language (it emphatically is not), but because it is everywhere. Every Linux system has Bash (or a compatible shell). Every sysadmin knows at least enough Bash to read and modify scripts. The Bash philosophy is composition through pipes: small, focused commands (grep, awk, sed, sort, uniq) connected by pipes (`|`) into pipelines that answer questions. A classic example: `awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head -10` — a one-liner that answers "which IP addresses are hitting my server the most?" without any database, any programming framework, or any latency beyond disk read speed.

Bash's weaknesses are significant and well-known. Error handling is manual and error-prone (the `set -euo pipefail` idiom, while recommended, has subtle behaviours). String handling is awkward. Data structures beyond arrays are non-existent. For any script exceeding roughly 100 lines, or requiring complex data manipulation, API interaction, or structured error handling, Python is the preferred alternative. By 2040, the division of labour is well-established: Bash for glue — orchestrating other commands, simple text processing, one-off tasks. Python for logic — anything that involves data structures, API calls, JSON/XML processing, or complex control flow. Shell scripts that grow organically into 500-line monstrosities are technical debt, not assets.

PowerShell, developed by Microsoft and released in 2006, was designed from the ground up as an administrative automation language. Where Bash pipes text between commands, PowerShell pipes objects — structured data with typed properties. `Get-Process | Where-Object { $_.CPU -gt 100 } | Stop-Process` is not parsing text output; it is filtering a collection of process objects by their CPU property and passing them to a command that operates on process objects. This object pipeline eliminates an entire class of text-parsing bugs that plague Bash scripts. PowerShell's verb-noun cmdlet naming convention (`Get-Service`, `Start-Service`, `Stop-Service`) makes commands discoverable and predictable. By 2040, PowerShell 7+ (the cross-platform, .NET-based successor to Windows PowerShell 5.1) runs on Linux and macOS as well as Windows, making it a viable cross-platform automation language — though Bash remains the default on Linux for historical and cultural reasons.

Automation frameworks build on scripting languages to provide reliability, scheduling, and auditability. A cron job that runs a Bash script at 3 AM is automation, but it lacks visibility (did it succeed? what was the output? who will notice if it starts failing?). Modern automation wraps scripts in frameworks: systemd timers (which provide logging, dependency management, and randomised delay windows to avoid thundering herd problems), Ansible playbooks (which are idempotent and report changes), or workflow engines (Apache Airflow for data pipelines, GitHub Actions for CI/CD). By 2040, AI-assisted script generation — describe the desired outcome in natural language and receive a validated, tested script — is increasingly common, but the sysadmin must still understand the generated code well enough to debug it when it inevitably encounters an edge case.

### Required Reading

- Robbins, A. & Beebe, N.H.F. (2005). *Classic Shell Scripting*. O'Reilly.
- Jones, D., Hicks, J., & Wilson, E. (2017). *Learn Windows PowerShell in a Month of Lunches*, 3rd Edition. Manning.
- Holmes, L. (2017). *PowerShell Cookbook*, 4th Edition. O'Reilly.
- UoY Automation Research Lab (2040). *AI-Generated Scripts in Production: A Risk Assessment*.

### Discussion Questions

1. Bash's text-based pipeline model has been called "the worst scripting model except for all the others." What advantages does text pipelining have over PowerShell's object pipeline, and in what scenarios?
2. AI-generated scripts reduce the barrier to automation but introduce the risk of running code the sysadmin doesn't fully understand. How should organisations govern AI-generated administrative scripts?
3. At what point does a cron job become technical debt? What are the signs that a scheduled script should be replaced with a proper automation framework?

---

ᛃ **Lecture 12: The 2040 Sysadmin — AI Co-Pilot, Human Steward**

### Overview

This concluding lecture synthesises the course material into a vision of the system administrator's evolving role. By 2040, AI handles routine operations — patch assessment, capacity planning, log triage, initial incident diagnosis — with competence that exceeds the average human. But the sysadmin is not obsolete; the role has shifted from operator to steward. The 2040 sysadmin designs the policies that autonomous systems execute, makes the judgment calls that AI cannot, manages the ethical dimensions of infrastructure that affects millions of users, and maintains the institutional knowledge that machines, for all their pattern-matching prowess, cannot replicate.

### Lecture Notes

The automation of routine administration has been underway for decades. What changed in the 2020s-2030s was the scope of what counts as "routine." Machine learning models trained on billions of system logs, incident tickets, and performance traces can now perform triage that once required a senior sysadmin with ten years of experience: "This alert pattern matches a disk controller firmware bug we saw in 2041; the recommended action is to apply firmware update KX-4.2.3 and reboot during the next maintenance window." The 2040 sysadmin does not discover this correlation; they review the AI's recommendation, consider the operational context (this server is part of a clustered pair; the partner will take over during the reboot), and approve or modify the action.

Yet the limits of AI in system administration are structural, not temporary. AI models optimise for patterns they have seen; they cannot reason about novel failure modes that combine components in unprecedented ways. AI can suggest that a configuration change satisfies security policy, but it cannot understand that applying that change to a legacy system that predates the policy might break an undocumented dependency that keeps the payroll system running. AI can optimise for cost efficiency, but it cannot weigh the human impact of consolidating data centres in ways that eliminate jobs in vulnerable communities. These are not temporary limitations awaiting better models; they are fundamental boundaries between optimisation and wisdom, between pattern-matching and understanding, between computation and judgment.

The 2040 sysadmin's core competencies have therefore shifted. Technical knowledge — knowing the exact syntax of an iptables rule or a Group Policy setting — is less valuable than it was, because the AI knows it better. What remains valuable: (1) **Systems thinking** — the ability to reason about complex, interacting systems and anticipate second-order effects of changes. (2) **Incident command** — the ability to lead a response under pressure, coordinating multiple specialists, communicating with stakeholders, and maintaining calm when the system is on fire. (3) **Ethical reasoning** — the ability to identify and navigate the ethical dimensions of infrastructure decisions: surveillance, access, environmental impact, labour displacement. (4) **Institutional memory** — the knowledge of *why* things are the way they are, which lives in human minds and team culture, not in configuration files. The AI can tell you what the configuration is; only the experienced colleague can tell you why it became that way.

The word "stewardship" captures this evolved role better than "administration." A steward manages resources on behalf of others, with obligations to the present and the future. The 2040 sysadmin stewards computational resources that society depends on — healthcare systems, financial infrastructure, communication networks, energy grids. This is a position of trust, not merely a technical function. The skills taught in IT201 — from filesystem architecture to security hardening to automation — are the tools of the trade. But the purpose they serve is larger than any tool: to build and maintain infrastructure that is reliable, secure, equitable, and worthy of the trust placed in it.

### Required Reading

- Russell, S. (2019). *Human Compatible: Artificial Intelligence and the Problem of Control*. Viking. Chapters 7-8.
- Beyer, B., et al. (2016). *Site Reliability Engineering*. Chapter 33: "Lessons Learned from Other Industries."
- UoY Philosophy of Technology Department (2040). *Stewardship in the Age of Autonomous Systems*. Yggdrasil Press.
- Course lecture notes, Lectures 1-11. [Cumulative synthesis]

### Discussion Questions

1. The 2040 sysadmin's role has shifted from "operator" to "steward." What concrete skills should a sysadmin develop to prepare for this shift, and which traditional skills are becoming obsolete?
2. AI can optimise for declared objectives but cannot set those objectives. Who should define the objectives that autonomous infrastructure optimises toward, and how do we ensure those objectives reflect diverse stakeholder interests?
3. Institutional memory — "why things are the way they are" — is notoriously fragile in IT organisations. What practices preserve this knowledge when the people who hold it leave?

---

## Final Examination Preparation

### Examination Format

The final examination for IT201 consists of two parts:

**Part A: Written Examination (50%)** — Choose 4 of the following 8 essay questions. Each essay should demonstrate command of technical material, cross-platform perspective, and operational judgment. Each essay: 500-750 words.

**Part B: Practical Scenario (50%)** — You will be given a scenario describing an organisation and its infrastructure requirements. Design and justify: (1) the server platform(s) to use (Linux, Windows, or both, with rationale), (2) the authentication and authorisation architecture, (3) the backup strategy with RPO/RTO specifications, (4) the monitoring and alerting strategy, and (5) the security hardening priorities. Maximum 2000 words.

### Essay Questions (Choose 4 of 8)

1. **The Cross-Platform Reality:** Most enterprises run both Linux and Windows servers. Compare the two platforms' approaches to: (a) service management, (b) user and permission management, and (c) configuration automation. Which platform is easier to administer at scale, and why?

2. **Infrastructure as Code at Scale:** An organisation with 10,000 servers runs Ansible playbooks from a central control node. The playbook that configures SSH settings accidentally sets `PermitRootLogin yes` and is applied to all servers before the error is detected. Analyse the failure: how could it have been prevented, how should it be detected, and how should recovery proceed?

3. **The Backup Testing Imperative:** Most organisations back up their data; far fewer test their restores. Design a restore testing programme that: (a) can be automated, (b) covers full system restores, individual file restores, and application-level consistency, and (c) is resilient to the restore testing system itself failing.

4. **Alert Fatigue and Signal-to-Noise:** An operations team receives 500 alerts per day, of which approximately 10 require action. Analyse the causes of this signal-to-noise ratio and propose concrete changes — to monitoring configuration, alert routing, team process, and organisational culture — that would reduce alert noise without missing critical signals.

5. **The Ethical Steward:** A hospital's ICU monitoring system runs on infrastructure you administer. An AI-assisted patch management system recommends applying a kernel security patch that has a 0.1% chance of causing a system crash on your specific hardware configuration. Analyse the ethical dimensions of this decision: what principles should guide it, who should make it, and how should it be documented?

6. **Active Directory at Mid-Life:** An organisation's Active Directory was designed in 2015 and has accumulated 10 years of OUs, GPOs, security groups, and schema extensions — many from applications that no longer exist. Design an approach to cleaning up this AD without breaking dependencies. What tools and testing strategies would you use?

7. **Linux Capabilities and the Root Problem:** The Linux capabilities system was designed to decompose root's power, but `CAP_SYS_ADMIN` has been called "the new root" because it grants so much. Analyse: is the capabilities model a meaningful security improvement, and what would a better decomposition of administrative privilege look like?

8. **The Human-AI Partnership:** AI now handles routine system administration tasks — patch assessment, log triage, capacity forecasting — with high competence. What tasks should remain reserved for human administrators, and what principles should determine this boundary? Defend your boundary with specific examples.

### Recommended Study Approach

1. **Build a lab environment:** Two VMs (one Linux, one Windows Server), configured to communicate. Practice all the administrative operations covered in lectures.
2. **Write and test Ansible playbooks** that configure both the Linux and Windows VMs. Verify idempotency.
3. **Simulate failures:** Delete a critical file, corrupt a configuration, fill a disk — and practice recovery.
4. **Review all Discussion Questions** from the lectures; the examination essays build on these themes.
5. **Form a study group** to debate the human-AI partnership question, which will appear on every examination in some form.

---

*IT201 System Administration (Linux + Windows) — woven by Runa Gridweaver Freyjasdottir for the University of Yggdrasil, 2040. May the systems you administer serve with the reliability of the World Tree and the wisdom of the Norns.*
