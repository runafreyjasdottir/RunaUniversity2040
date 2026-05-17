# IT201: System Administration (Linux + Windows)
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4
**Prerequisites:** IT105 (Programming for IT), IT107 (Web Technologies & Internet Architecture)
**Description:** The practice of system administration is the art and science of keeping computers, networks, and services running reliably, securely, and efficiently. This course provides intensive, hands-on training in administering both Linux and Windows systems in enterprise environments. Students learn user management, package management, service configuration, networking, storage, security hardening, monitoring, backup and recovery, and automation. By 2040, system administration has evolved from manual server tending to platform engineering — the design and operation of self-healing, scalable, observable infrastructure. Yet the fundamentals remain unchanged: understanding the systems you operate, anticipating failure, responding calmly to crisis, and documenting everything. The course is taught in the Yggdrasil IT Sandbox, where students administer live systems that serve real (if simulated) organisational workloads.

---

## Lecture 1: The System Administrator as Craftsman — Philosophy, Ethics, and Practice

System administration is not merely a technical role; it is a craft that demands judgment, responsibility, and continuous learning. This lecture examines the philosophy of system administration, the ethical dimensions of operational power, and the practices that distinguish professional administrators from amateurs.

**The system administrator's role** has evolved significantly. In the 1990s, the SA was a "computer janitor" who installed software, replaced hardware, and answered helpdesk tickets. In the 2010s, the SA became a "DevOps engineer" who wrote automation, managed cloud resources, and participated in agile teams. In 2040, the SA is a **platform engineer** who designs internal developer platforms, manages Kubernetes clusters, optimises cloud costs, and ensures security and compliance at scale. Yet through all these changes, the core competencies remain: **troubleshooting** (systematic diagnosis of complex problems), **communication** (explaining technical issues to non-technical stakeholders), **documentation** (recording configurations, procedures, and decisions), and **calm under pressure** (maintaining composure during outages).

**The principle of least privilege** is the cornerstone of operational security: administrators should have only the permissions necessary for their current task, and no more. **sudo** (Linux) and **User Account Control** (Windows) enforce this principle by requiring explicit elevation for privileged operations. **Privileged Access Management (PAM)** systems (CyberArk, BeyondTrust, HashiCorp Vault) provide just-in-time access: administrators request elevated permissions for a specific time window, and the system audits every action. In 2040, **zero-trust administration** is the standard: no administrator is trusted by default, and every privileged action requires multi-factor authentication, approval workflows, and session recording.

**The ethical responsibilities** of system administrators are profound. An SA with root access can read any user's email, modify any database record, and conceal any action. **Professional ethics** demand: respect for user privacy (do not read personal data without authorisation); honesty about mistakes (disclose errors promptly so they can be remediated); responsibility for security (protect the systems under your care from attack); and transparency about capabilities (do not claim expertise you do not possess). The **Yggdrasil IT Covenant** (discussed in IT101) includes specific obligations for administrators: "I will not use my access for personal gain, for pranks, or for curiosity about others' private affairs. I will report security vulnerabilities rather than exploit them. I will share my knowledge with colleagues and mentees."

**The craft of system administration** includes habits and practices that are rarely taught in textbooks. **Checklists** (pre-flight checks before changes, post-incident verification) prevent simple errors. **Staging environments** (test changes before production) catch problems before they impact users. **Change management** (documenting, reviewing, and scheduling changes) reduces unexpected downtime. **Observability** (logging, metrics, tracing) enables rapid diagnosis. **Postmortems** (blameless analysis of incidents) drive continuous improvement. In 2040, **AI-assisted administration** (e.g., the *Mimir Admin* assistant) provides recommendations, but the human administrator remains responsible for decisions.

**Required Reading:**
- Thomas A. Limoncelli, Christina J. Hogan & Strata R. Chalup, *The Practice of System and Network Administration* (3rd ed., Addison-Wesley, 2016/2035), ch. 1–3
- Mark Burgess, *In Search of Certainty: The Science of Our Information Infrastructure* (2nd ed., xt Axis Press, 2035), ch. 3 ("The Human Element")
- K. J. S. Anand, "The System Administrator as Craftsman" *;login:* 41, no. 4 (2016/2035): 12–17
- ACM/IEEE-CS, *Software Engineering Code of Ethics and Professional Practice* (1999/2035)
- University of Yggdrasil, "The Yggdrasil IT Covenant: Administrator Responsibilities" (2040)

**Discussion Questions:**
1. System administrators have extraordinary power over the systems they manage. Is this concentration of power inevitable, or can organisational structures (e.g., separation of duties, peer review of changes) mitigate the risk?
2. AI-assisted administration promises to reduce human error, but it also raises questions of accountability. If an AI-recommended change causes an outage, who is responsible — the AI, the administrator who approved it, or the vendor who trained the AI?
3. The "platform engineer" role of 2040 is more strategic than the "system administrator" of 1990. Is this evolution a genuine professionalisation, or has it merely added layers of abstraction that distance engineers from the systems they operate?

---

## Lecture 2: Linux Administration — Installation, Package Management, and Boot Process

Linux is the dominant server operating system in 2040, powering cloud infrastructure, embedded systems, and supercomputers. This lecture covers Linux installation, package management, and the boot process — the foundations of Linux system administration.

**Linux distributions** are varied, each optimised for different use cases. **Enterprise distributions** (Red Hat Enterprise Linux / RHEL, SUSE Linux Enterprise Server / SLES, Ubuntu Pro) provide long-term support, security updates, and vendor certifications. **Community distributions** (Fedora, openSUSE, Debian, Arch) offer cutting-edge features and flexibility. **Container-optimised distributions** (CoreOS, Flatcar, Talos, Bottlerocket) are minimal systems designed solely for running containers. The University of Yggdrasil's **Nordux** distribution is a customised Ubuntu variant optimised for academic and research environments, with pre-installed scientific libraries, HPC tools, and Yggdrasil-specific configuration management. In 2040, **immutable distributions** (where the root filesystem is read-only and updates are atomic image replacements) are gaining traction for servers and edge devices.

**Installation** methods include: **physical media** (USB drives, DVDs — rare in 2040); **network boot** (PXE — Preboot Execution Environment); **virtual machine images** (cloud-init configured images for AWS, Azure, Google Cloud); **container images** (Docker, Podman, LXD); and **bare-metal provisioning** (MAAS — Metal as a Service, Foreman, Cobbler). The installation process involves: partitioning (ext4, XFS, Btrfs, ZFS); filesystem selection; bootloader installation (GRUB2, systemd-boot); initial user creation; and network configuration. In 2040, **automated installation** (Kickstart for RHEL, Preseed for Debian, cloud-init for cloud images) eliminates manual steps, enabling hundreds of machines to be provisioned identically.

**Package management** is the system for installing, updating, and removing software. **RPM-based systems** (RHEL, Fedora, SUSE) use **rpm** (low-level) and **yum/dnf** (high-level) package managers. **DEB-based systems** (Debian, Ubuntu) use **dpkg** (low-level) and **apt** (high-level). **Arch-based systems** use **pacman**. **Universal package formats** (Flatpak, Snap, AppImage) provide distribution-agnostic packages with sandboxed execution. In 2040, **container-based deployment** (Docker, Kubernetes) has largely replaced traditional package management for server applications, but packages remain essential for system tools, libraries, and desktop software. **Package security** is critical: repositories must be signed (GPG), and **SBOMs** (Software Bill of Materials) track all dependencies for vulnerability scanning.

**The Linux boot process** is a sequence of stages: **BIOS/UEFI** (firmware initialisation, hardware detection); **bootloader** (GRUB2 loads the kernel and initramfs); **kernel** (initialises hardware, mounts the root filesystem); **initramfs** (initial RAM filesystem, contains drivers and scripts needed to mount the real root filesystem); **init system** (systemd in 2040 — manages services, mounts, sockets, timers); and **user space** (login managers, graphical sessions, or server daemons). Understanding the boot process is essential for troubleshooting: a system that won't boot may have a corrupted bootloader, missing kernel modules, or a failed filesystem check. The **systemd** init system (adopted by virtually all major distributions by 2020) uses **units** (service, socket, device, mount, automount, swap, target, path, timer, slice, scope) to define system resources and their dependencies. **systemctl** is the primary management tool: `systemctl start nginx`, `systemctl enable sshd`, `systemctl status mariadb`.

**Required Reading:**
- Evi Nemeth et al., *UNIX and Linux System Administration Handbook* (5th ed., Addison-Wesley, 2017/2035), ch. 2–4, 6
- Lennart Poettering, "Rethinking PID 1" (2010/2035) — the original systemd announcement
- Red Hat, *System Administration Guide* (RHEL 10, 2035)
- Ubuntu Server Documentation, "Installation and Configuration" (2040)
- University of Yggdrasil, "Nordux: The Yggdrasil Linux Distribution — Architecture and Administration" (2039)

**Discussion Questions:**
1. systemd is powerful and comprehensive but also controversial, with critics arguing it violates the Unix philosophy. Is systemd a genuine improvement over SysV init, or has it created an overly complex, monolithic system?
2. Container-based deployment has reduced the importance of traditional package management for servers. Will package managers eventually become obsolete, or will they remain essential for system-level software?
3. Immutable distributions promise atomic updates and rollback capability, but they also limit customisation. Is immutability the future of Linux server administration, or will mutable systems remain necessary for development and specialisation?

---

## Lecture 3: Linux Administration — Users, Groups, Permissions, and ACLs

User management is the foundation of multi-user system security. This lecture covers Linux user and group administration, file permissions, and Access Control Lists (ACLs).

**User accounts** in Linux are defined in `/etc/passwd` (username, UID, GID, home directory, shell) and `/etc/shadow` (encrypted password, password aging, account expiration). **UID 0** is root, the superuser. **System accounts** (UID 1–999) run daemons and services. **Regular users** (UID 1000+) are human users. **User administration commands**: `useradd` (create), `usermod` (modify), `userdel` (delete), `passwd` (set password), `chage` (manage password aging). In 2040, **centralised identity management** (LDAP, Active Directory, FreeIPA, or cloud identity providers) has largely replaced local user management in enterprise environments, but local accounts remain important for standalone systems, service accounts, and emergency access.

**Groups** organise users for permission management. **Primary group** (defined in /etc/passwd) is the default group for a user's files. **Supplementary groups** (defined in /etc/group) provide additional permissions. **Group administration**: `groupadd`, `groupmod`, `groupdel`, `gpasswd`, `usermod -aG group user`. In 2040, **dynamic group membership** (e.g., based on attributes in LDAP or policies in cloud identity systems) has largely replaced static group assignments, but the underlying Unix group mechanism remains unchanged.

**File permissions** use the traditional Unix model: **owner**, **group**, and **others**, each with **read (r)**, **write (w)**, and **execute (x)** permissions. Numeric notation (octal): 4=read, 2=write, 1=execute; 7=rwx, 6=rw-, 5=r-x, 4=r--, etc. `chmod 755 file` sets rwxr-xr-x. `chown user:group file` changes ownership. **Special permissions**: **SUID** (4) — execute as file owner; **SGID** (2) — execute as file group, or new files inherit group; **sticky bit** (1) — only owner can delete files in directory (used on /tmp). In 2040, **SUID binaries** are increasingly restricted (via capabilities and namespaces) because they are a common attack vector.

**ACLs (Access Control Lists)** extend the traditional permission model to allow multiple users and groups with different permissions on the same file. **setfacl** sets ACLs; `setfacl -m u:alice:rwx file` grants user alice read, write, and execute. **getfacl** displays ACLs. **Default ACLs** on directories automatically apply to newly created files. In 2040, **ACLs are standard** on enterprise file servers (NFSv4, Samba, CephFS) but are often avoided on local systems due to complexity. **Capabilities** (Linux capabilities, introduced in kernel 2.2) provide a finer-grained alternative to SUID: a binary can be granted specific privileges (e.g., `CAP_NET_BIND_SERVICE` to bind to ports <1024) without full root access. **setcap** and **getcap** manage capabilities.

**Lab Exercise:** Students configure a multi-user Linux environment in the Yggdrasil Sandbox. They must: create 10 users with different primary and supplementary groups; set up a shared project directory with SGID so all group members can collaborate; configure ACLs so a specific user has read-only access to a sensitive file; remove SUID from all unnecessary binaries using `find / -perm -4000`; and document all changes in a runbook.

**Required Reading:**
- Evi Nemeth et al., *UNIX and Linux System Administration Handbook*, ch. 5
- Michael Kerrisk, *The Linux Programming Interface* (No Starch Press, 2010/2035), ch. 35 ("Process Credentials")
- Robert Love, *Linux Kernel Development* (3rd ed., Addison-Wesley, 2010/2035), ch. 9 ("Kernel Synchronization Methods") — for understanding capabilities
- University of Yggdrasil, "User and Permission Management in the Nordux Environment" (2039)

**Discussion Questions:**
1. The Unix permission model (owner/group/others) is simple but coarse. ACLs provide finer control but are complex and often misconfigured. Is the simplicity of Unix permissions a feature or a bug?
2. SUID binaries are a major security risk but are still necessary for some system functions (e.g., `ping` with CAP_NET_RAW). Should SUID be completely replaced by capabilities, or are there cases where SUID is still the right solution?
3. Centralised identity management (LDAP/AD) has replaced local user management in enterprises, but it also creates a single point of failure. What are the resilience and security implications of centralised identity, and how should organisations mitigate them?

---

## Lecture 4: Linux Administration — Storage, Filesystems, and LVM

Storage management is a critical system administration skill. This lecture covers Linux storage devices, filesystems, partitioning, Logical Volume Management (LVM), and RAID.

**Storage devices** are identified in Linux by device files: **SCSI/SATA disks** (`/dev/sda`, `/dev/sdb`); **NVMe SSDs** (`/dev/nvme0n1`, `/dev/nvme1n1`); **virtual disks** (`/dev/vda`, `/dev/xvda` in cloud VMs); and **loop devices** (`/dev/loop0` for mounting ISO images). **Device identification**: `lsblk` lists block devices; `fdisk -l` or `parted -l` shows partition tables; `smartctl` displays SMART health data for physical disks. In 2040, **persistent naming** (by UUID, label, or path in `/dev/disk/by-uuid/`, `/dev/disk/by-label/`) is standard to ensure consistent device naming across reboots.

**Partitioning** divides a disk into independent sections. **MBR** (Master Boot Record, legacy) supports up to 4 primary partitions (or 3 primary + 1 extended with logical partitions) and disks up to 2 TB. **GPT** (GUID Partition Table, modern) supports up to 128 partitions and disks up to 18 exabytes. **Partitioning tools**: `fdisk` (MBR and GPT), `gdisk` (GPT-only), `parted` (scriptable, supports resizing). In 2040, **GPT is universal** for new systems, but MBR persists in legacy embedded devices. **Partition types**: standard data partitions (Linux filesystem, Linux swap); EFI System Partition (ESP, required for UEFI boot); and special-purpose partitions (LUKS encryption, LVM physical volume).

**Filesystems** organise data on partitions. **ext4** is the default for most Linux distributions: journaling, extents, delayed allocation, online defragmentation. **XFS** is preferred for large files and high-performance workloads: excellent scalability, parallel I/O, online growth (but not shrinkage). **Btrfs** (B-tree filesystem) provides advanced features: copy-on-write, snapshots, subvolumes, RAID-like redundancy, compression, and deduplication. **ZFS** (from Sun/Oracle, now OpenZFS) provides similar features with a mature codebase and strong data integrity guarantees (checksums for all data and metadata). In 2040, **Btrfs is the default** on Fedora and SUSE; **ZFS** is popular on Ubuntu and FreeBSD; **ext4** remains the conservative choice for stability. **stratis** (Red Hat) and **bcachefs** (new in the 2030s) are emerging alternatives.

**LVM (Logical Volume Management)** provides flexible storage abstraction above physical disks. **Physical Volumes (PVs)** are raw disks or partitions. **Volume Groups (VGs)** aggregate PVs into pools. **Logical Volumes (LVs)** are allocated from VGs and formatted with filesystems. LVM enables: **dynamic resizing** (grow or shrink filesystems without downtime); **snapshotting** (read-only or read-write copies of a volume at a point in time); **striping** (RAID-0 across multiple PVs); **mirroring** (RAID-1); and **thin provisioning** (allocate storage on demand rather than upfront). **Commands**: `pvcreate`, `vgcreate`, `lvcreate`, `lvextend`, `lvreduce`, `lvremove`, `lvdisplay`. In 2040, **LVM is standard** in enterprise Linux environments, though **Btrfs subvolumes** and **ZFS datasets** provide similar functionality with integrated filesystem features.

**RAID (Redundant Array of Independent Disks)** provides redundancy and performance. **RAID 0** (striping) improves performance but provides no redundancy. **RAID 1** (mirroring) duplicates data across disks. **RAID 5** (striping with distributed parity) tolerates one disk failure but has poor write performance. **RAID 6** (striping with double parity) tolerates two disk failures. **RAID 10** (mirrored stripes) combines RAID 0 and RAID 1 for performance and redundancy. In 2040, **hardware RAID** is rare (CPU overhead of software RAID is negligible on modern processors); **mdadm** (Linux software RAID) and **LVM RAID** are standard. **Erasure coding** (Reed-Solomon, used in Ceph, HDFS, and cloud storage) is the modern replacement for RAID in large-scale distributed storage.

**Required Reading:**
- Evi Nemeth et al., *UNIX and Linux System Administration Handbook*, ch. 8–9
- Robert Love, *Linux Kernel Development*, ch. 13 ("The Block I/O Layer")
- Val Henson et al., "Chunkfs: Using Divide-and-Conquer to Improve File System Reliability and Repair," *HotDep 2006*
- OpenZFS Documentation, "ZFS Administration Guide" (2040)
- University of Yggdrasil, "Storage Management in the Muninn Cluster: LVM, Btrfs, and ZFS" (2039)

**Discussion Questions:**
1. Btrfs and ZFS offer similar features (snapshots, compression, RAID-like redundancy), but Btrfs is in the Linux kernel while ZFS is a separate module due to licensing incompatibility. Is the licensing issue a genuine barrier, or is it a political obstacle that should be resolved?
2. LVM adds a layer of abstraction that can complicate recovery if the LVM metadata is corrupted. Is the flexibility of LVM worth the added complexity and risk, or should administrators use simple partitions for critical systems?
3. RAID is increasingly replaced by erasure coding in large-scale storage. Is RAID obsolete for data centres, or does it still have a role in small-scale deployments (e.g., a single server with 4–8 drives)?

---

## Lecture 5: Linux Administration — Networking, Firewalls, and Services

A server without network connectivity is an island; a server with misconfigured networking is a liability. This lecture covers Linux network configuration, firewalls, and service management.

**Network configuration** in 2040 Linux uses **systemd-networkd** (low-level network management), **NetworkManager** (desktop and laptop-oriented), or **cloud-init** (cloud VM initialisation). **Interface configuration**: `ip` (modern replacement for `ifconfig`) — `ip addr`, `ip link`, `ip route`, `ip neigh`; `ss` (modern replacement for `netstat`) — `ss -tlnp` shows listening TCP sockets with process names. **Configuration files**: `/etc/systemd/network/*.network` for systemd-networkd; `/etc/NetworkManager/system-connections/` for NetworkManager; `/etc/netplan/*.yaml` on Ubuntu. **DNS resolution** is handled by **systemd-resolved** in 2040, with configuration in `/etc/systemd/resolved.conf` and `/etc/resolv.conf` as a symlink. **Hostname management**: `hostnamectl` sets static, transient, and pretty hostnames.

**Routing** directs traffic between networks. **Static routes** (`ip route add 192.168.10.0/24 via 10.0.0.1`) are simple but do not adapt to network changes. **Dynamic routing protocols** (BGP, OSPF, IS-IS) enable routers to share routing information automatically. On Linux, **BIRD** and **FRRouting** implement these protocols. In 2040, **segment routing** (SRv6) and **software-defined networking (SDN)** have transformed routing in data centres, with controllers (e.g., Open vSwitch, Cilium) programming switch forwarding tables dynamically. The University of Yggdrasil's campus network uses **Cilium** for eBPF-based networking and security in its Kubernetes clusters.

**Firewalls** control network traffic based on rules. **iptables** (legacy) and **nftables** (modern) are the Linux kernel packet filtering frameworks. **nftables** provides a unified, more readable syntax for filtering, NAT, and logging. **firewalld** (RHEL/Fedora) and **ufw** (Ubuntu) provide higher-level abstractions over nftables. **Rules** specify: source/destination IP and port; protocol (TCP, UDP, ICMP); chain (INPUT, OUTPUT, FORWARD); and action (ACCEPT, DROP, REJECT, LOG). **Best practices**: default deny (drop all traffic not explicitly allowed); allow only necessary ports; log dropped packets for analysis; and use connection tracking (stateful inspection) to allow return traffic. In 2040, **eBPF-based firewalls** (Cilium, Falco, bpfilter) provide programmable, high-performance filtering with deep packet inspection and application-aware rules.

**Service management** with systemd. **Service units** (`*.service`) define how daemons are started, stopped, and restarted. **Socket units** (`*.socket`) enable socket activation (systemd creates the socket and starts the service only when a connection arrives). **Timer units** (`*.timer`) replace cron for scheduled tasks. **Target units** (`*.target`) group units for boot milestones (multi-user, graphical). **systemctl commands**: `start`, `stop`, `restart`, `reload`, `enable`, `disable`, `status`, `mask`, `unmask`. **journalctl** queries systemd logs: `journalctl -u nginx`, `journalctl --since "1 hour ago"`, `journalctl -f` (follow). In 2040, **structured logging** (JSON-formatted logs stored in the journal) enables rich querying and analysis.

**Required Reading:**
- Evi Nemeth et al., *UNIX and Linux System Administration Handbook*, ch. 14–15
- Jan "ya" Engelhardt, "The nftables Handbook" (Netfilter Project, 2035)
- Thomas Graf, "Cilium: BPF and XDP Guide" (Isovalent, 2035)
- systemd documentation, "systemd-networkd.service" and "systemd-resolved.service" (2040)
- University of Yggdrasil, "eBPF-Based Networking and Security with Cilium in the Muninn Cluster" (2039)

**Discussion Questions:**
1. systemd has absorbed many functions that were previously handled by separate tools (network configuration, DNS resolution, logging, time synchronisation). Is this consolidation beneficial, or does it violate the Unix philosophy and create excessive dependency on a single project?
2. nftables is the modern replacement for iptables, but many administrators still use iptables due to familiarity. Is the transition to nftables worth the learning curve, or should the Linux kernel maintain iptables indefinitely?
3. eBPF enables powerful, programmable networking and security, but it also introduces new risks (eBPF programs can crash the kernel if buggy). Is eBPF a genuine advance, or does its power outweigh its safety for production systems?

---

## Lecture 6: Windows Administration — Installation, Active Directory, and Group Policy

Windows Server remains a dominant enterprise platform in 2040. This lecture covers Windows installation, Active Directory, Group Policy, and the tools that Windows administrators use daily.

**Windows Server editions** in 2040 include: **Standard** (for physical or minimally virtualised environments); **Datacenter** (unlimited virtualisation rights); **Azure Edition** (optimised for Azure, with hotpatching and SMB over QUIC); and **Container** (minimal image for containers). **Installation** methods: physical media, network boot (PXE with WDS — Windows Deployment Services), virtual machine templates (VHDX images with Sysprep), and cloud images (Azure, AWS, GCP). **Automated deployment** uses **Answer Files** (unattend.xml) and **Windows Imaging Format (WIM)** for custom images. In 2040, **Autopilot** (for client devices) and **Windows Admin Center** (web-based server management) have replaced many traditional deployment tools.

**Active Directory (AD)** is Microsoft's directory service, the cornerstone of Windows enterprise administration. **AD DS (Domain Services)** stores objects: users, groups, computers, organisational units (OUs), and Group Policy Objects (GPOs). **Forests** are the top-level security boundary; **domains** are administrative boundaries within forests; **trees** are contiguous domain namespaces. **Trusts** enable authentication across domains and forests. **Global Catalog** (GC) provides a partial replica of all objects in the forest for fast searches. **FSMO roles** (Flexible Single Master Operations) are special roles (Schema Master, Domain Naming Master, RID Master, PDC Emulator, Infrastructure Master) that must be carefully managed during DC promotion/demotion. In 2040, **Azure AD** (now **Microsoft Entra ID**) is the cloud-based identity platform that extends or replaces on-premises AD for many organisations, but on-premises AD persists in regulated environments and legacy systems.

**Group Policy** is the centralised management system for Windows configuration. **GPOs** are linked to sites, domains, or OUs and contain ** policies** (registry-based settings) and ** preferences** (flexible, non-enforced settings). **Group Policy processing order**: local → site → domain → OU (LSDOU), with later policies overriding earlier ones (unless enforced or blocked). **Common GPO settings**: password policies, account lockout, software installation, folder redirection, drive mappings, registry settings, security options, and Windows Update configuration. In 2040, **Microsoft Endpoint Manager (Intune)** provides cloud-based policy management that complements or replaces Group Policy for hybrid and cloud-native environments.

**Windows administration tools** include: **Server Manager** (dashboard for local and remote server management); **Windows Admin Center** (modern, web-based replacement for Server Manager and MMC); **PowerShell** (the primary automation tool); **RSAT (Remote Server Administration Tools)** (MMC snap-ins for AD, DNS, DHCP, Group Policy); **Sysinternals Suite** (advanced troubleshooting tools: Process Explorer, Autoruns, TCPView, DebugView); and **Event Viewer** (system, security, application, and forwarded event logs). In 2040, **AI-assisted troubleshooting** (built into Windows Admin Center) analyses event logs and performance data to suggest remediation steps.

**Required Reading:**
- Brian Desmond et al., *Active Directory: Designing, Deploying, and Running Active Directory* (5th ed., O'Reilly, 2021/2035), ch. 1–5
- Jeremy Moskowitz, *Group Policy: Fundamentals, Security, and the Managed Desktop* (3rd ed., Sybex, 2018/2035), ch. 1–4
- Mark Russinovich, Aaron Margosis & David Solomon, *Troubleshooting with the Windows Sysinternals Tools* (2nd ed., Microsoft Press, 2016/2035), ch. 1–3
- Microsoft, *Windows Server 2040 Documentation* (2040)
- University of Yggdrasil, "Active Directory and Entra ID: Hybrid Identity Management at the University" (2039)

**Discussion Questions:**
1. Active Directory is a monolithic, proprietary directory service that has dominated enterprise Windows environments for 25 years. Is AD's longevity a sign of fundamental design strength, or is it merely the result of vendor lock-in and the high cost of migration?
2. Group Policy is powerful but complex, with thousands of settings and unpredictable interaction effects. Is Group Policy a well-designed management tool, or has its complexity grown beyond the capacity of most administrators to use effectively?
3. Microsoft is pushing organisations toward cloud-based management (Intune, Entra ID). For organisations with strict data sovereignty requirements (e.g., the University of Yggdrasil under the Nordic Data Compact), is cloud-based identity management acceptable, or must critical identity infrastructure remain on-premises?

---

## Lecture 7: Windows Administration — PowerShell, DSC, and Azure Management

Modern Windows administration is increasingly automated through PowerShell and cloud management tools. This lecture covers PowerShell for Windows administration, Desired State Configuration (DSC), and Azure/Entra management.

**PowerShell for Windows administration** (introduced in IT105) is the primary tool for managing Windows servers. **WMI/CIM** (Windows Management Instrumentation / Common Information Model) provides access to hardware, software, and system state: `Get-CimInstance Win32_Process`, `Get-CimInstance Win32_LogicalDisk`. **AD cmdlets** (ActiveDirectory module): `Get-ADUser`, `New-ADUser`, `Set-ADUser`, `Get-ADGroupMember`. **Group Policy cmdlets**: `Get-GPO`, `New-GPO`, `Set-GPLink`. **DNS cmdlets**: `Get-DnsServerZone`, `Add-DnsServerResourceRecord`. **DHCP cmdlets**: `Get-DhcpServerv4Scope`, `Add-DhcpServerv4Reservation`. **Remote management**: `Invoke-Command` (run commands on remote machines), `Enter-PSSession` (interactive remote session), `New-PSSession` (persistent session). In 2040, **PowerShell 7** is the cross-platform standard, and **Windows PowerShell 5.1** is maintained only for legacy compatibility.

**Desired State Configuration (DSC)** is PowerShell's declarative configuration management framework (introduced in IT105, expanded here for Windows). **DSC resources** manage: files, registry keys, services, users, groups, Windows features, IIS, SQL Server, and custom resources. **DSC Local Configuration Manager (LCM)** enforces the desired state on target nodes. **DSC Pull Server** (or Azure Automation State Configuration) distributes configurations to nodes. **DSC compliance** reporting shows which nodes are compliant and which have drifted. In 2040, **DSC v3** is cross-platform and integrates with Azure Policy, AWS Config, and Kubernetes operators. The University of Yggdrasil uses DSC to manage the configuration of 500+ Windows servers, ensuring consistency and enabling rapid remediation of configuration drift.

**Azure and Entra management** with PowerShell. **Az module** manages Azure resources: `New-AzVM`, `Get-AzStorageAccount`, `Set-AzKeyVaultSecret`. **Microsoft.Graph module** manages Entra ID (formerly Azure AD): `Get-MgUser`, `New-MgGroup`, `Update-MgUser`. **ExchangeOnlineManagement** manages Exchange Online. **MicrosoftTeams** manages Teams. In 2040, **cloud administration** is as important as on-premises administration: most organisations operate hybrid environments with workloads split between on-premises data centres and multiple cloud providers. **Multi-cloud management** tools (Terraform, Pulumi, Crossplane) provide cloud-agnostic abstractions, but cloud-native PowerShell modules remain essential for detailed management.

**Lab Exercise:** Students automate the deployment of a Windows Server environment in the Yggdrasil Sandbox. They must: write a PowerShell script that creates 20 AD users, 5 groups, and assigns memberships; write a DSC configuration that ensures IIS is installed, a website is configured, and SSL is bound; write a script that deploys an Azure VM, configures networking, and installs the Azure Monitor agent; and write a Pester test suite that verifies all configurations.

**Required Reading:**
- Bruce Payette & Richard Siddaway, *Windows PowerShell in Action* (4th ed.), ch. 6–10, 19–20
- Ritesh Modi, *Windows PowerShell Desired State Configuration Revealed* (Apress, 2014/2035), ch. 6–10
- Thomas Lee, "Managing Azure with PowerShell 7" (Packt, 2035), ch. 1–5
- University of Yggdrasil, "DSC at Scale: Managing 500 Windows Servers with PowerShell Desired State Configuration" (2039)

**Discussion Questions:**
1. PowerShell's deep integration with Windows is its greatest strength but also limits its usefulness on Linux. As organisations adopt multi-cloud and hybrid environments, should administrators prioritise cross-platform tools (Terraform, Python) over platform-specific tools (PowerShell, DSC)?
2. DSC promises self-healing infrastructure, but in practice, many organisations use DSC only for initial configuration and not for ongoing enforcement. Is this a failure of DSC's design, a lack of organisational discipline, or a rational response to the complexity of continuous enforcement?
3. Azure and Entra PowerShell modules are powerful but require significant setup (authentication, module installation, understanding the object model). Is the complexity inherent to cloud management, or could Microsoft design simpler abstractions for common tasks?

---

## Lecture 8: Monitoring, Logging, and Observability

You cannot manage what you cannot see. This lecture covers the tools and practices for monitoring system health, collecting logs, and building observable systems.

**Monitoring** tracks the health and performance of systems over time. **Metrics** are quantitative measurements: CPU utilisation, memory usage, disk I/O, network throughput, application response time, error rates. **Monitoring tools**: **Prometheus** (open-source metrics collection and alerting, the de facto standard in 2040); **Grafana** (visualisation and dashboards); **Nagios** (legacy but still used); **Zabbix** (enterprise monitoring); **Datadog** (SaaS monitoring); and **New Relic** (application performance monitoring). **Alerting rules** define thresholds that trigger notifications: "CPU > 90% for 5 minutes" or "disk usage > 85%". **Alert fatigue** occurs when too many alerts desensitise operators; the solution is to tune thresholds, suppress duplicates, and prioritise actionable alerts. In 2040, **AI-assisted anomaly detection** (e.g., Prometheus with ML-based forecasting) reduces false positives by 30–50%.

**Logging** records events for later analysis. **System logs** (syslog, systemd journal, Windows Event Log) record kernel messages, service status, authentication events, and errors. **Application logs** record user actions, errors, and business events. **Log levels**: DEBUG (detailed information for debugging), INFO (normal operation), WARNING (unexpected but not erroneous), ERROR (failed operations), CRITICAL (system failure). **Structured logging** (JSON-formatted logs with consistent fields) enables automated parsing and analysis. **Log aggregation tools**: **ELK Stack** (Elasticsearch, Logstash, Kibana); **Grafana Loki** (lightweight, Prometheus-inspired); **Splunk** (enterprise); **Fluentd/Fluent Bit** (log collectors). In 2040, **centralised logging** is standard: every system streams logs to a central aggregator where they are indexed, searched, and analysed.

**Observability** extends beyond monitoring and logging to provide a holistic understanding of system behaviour. The **three pillars of observability**: **metrics** (what is happening?), **logs** (why is it happening?), and **traces** (where is the problem in a distributed system?). **Distributed tracing** (OpenTelemetry, Jaeger, Zipkin) follows requests as they traverse multiple services, revealing latency bottlenecks and failure points. **Service mesh** (Istio, Linkerd, Cilium Service Mesh) automatically generates traces and metrics for all service-to-service communication. In 2040, **correlation** between metrics, logs, and traces is automated: when an alert fires, the system presents related log entries and trace spans, reducing mean time to resolution (MTTR) by 40–60%.

**The Yggdrasil Observability Platform** (built on Prometheus, Grafana, Loki, Tempo, and OpenTelemetry) monitors all University IT systems. **Custom dashboards** display: real-time campus network traffic; data centre PUE and carbon footprint; application error rates and latencies; user experience metrics (Core Web Vitals for University web properties); and security events (failed logins, firewall blocks, malware detections). Students in IT201 configure monitoring for their Sandbox environments, gaining hands-on experience with the same tools used in production.

**Required Reading:**
- James Turnbull, *The Art of Monitoring* (James Turnbull, 2016/2035), ch. 1–5
- Jamie Wilkinson et al., *Site Reliability Engineering*, ch. 10 ("Practical Alerting")
- Cindy Sridharan, *Distributed Systems Observability* (O'Reilly, 2018/2035), ch. 1–3
- OpenTelemetry Documentation, "Getting Started" (2040)
- University of Yggdrasil, "The Yggdrasil Observability Platform: Architecture and Practice" (2039)

**Discussion Questions:**
1. Monitoring generates vast quantities of data, but most of it is never analysed. Is the solution better dashboards, AI-assisted analysis, or simply collecting less data?
2. Observability promises to make systems understandable, but it requires significant instrumentation effort. For legacy systems that were not designed for observability, is the retrofitting effort worth the benefit?
3. AI-assisted anomaly detection reduces false positives but can also miss novel failure modes that do not match historical patterns. Is AI a genuine improvement over rule-based alerting, or does it merely trade one set of problems for another?

---

## Lecture 9: Backup and Disaster Recovery

Data loss is not a question of if but when. This lecture covers backup strategies, disaster recovery planning, and the tools that protect organisations from catastrophic data loss.

**Backup strategies** balance recovery objectives against cost and complexity. **RTO (Recovery Time Objective)** is the maximum acceptable downtime after a disaster. **RPO (Recovery Point Objective)** is the maximum acceptable data loss (time between the last backup and the disaster). **Full backup** copies all data; it is comprehensive but slow and storage-intensive. **Incremental backup** copies only data changed since the last backup; it is fast and efficient but requires the last full backup and all subsequent incrementals for recovery. **Differential backup** copies all data changed since the last full backup; it requires only the last full and the last differential for recovery. **Snapshot** ( filesystem-level point-in-time copy) enables instant backup with minimal overhead (Btrfs, ZFS, LVM, and storage arrays all support snapshots). In 2040, **synthetic full backups** (combining a full backup with incrementals to create a new full backup without reading the source) are standard.

**Backup tools** include: **rsync** (file-level synchronisation, ideal for incremental backups); **tar** (archiving, often with gzip/bzip2/xz compression); **dd** (block-level copying, for disk images); **Bacula** (enterprise backup suite); **Bareos** (Bacula fork, open-source); **Veeam** (virtual machine and cloud backup); **Restic** (modern, encrypted, deduplicated backup); **BorgBackup** (encrypted, deduplicated, compressed); **Duplicati** (encrypted cloud backups); and **cloud-native backup** (AWS Backup, Azure Backup, Google Cloud Backup). In 2040, **immutable backups** (write-once, read-many storage that cannot be deleted or modified by ransomware) are mandatory for compliance. The **3-2-1-1-0 rule** (3 copies of data, 2 different media, 1 offsite, 1 immutable, 0 errors after verification) is the standard for critical data.

**Disaster Recovery (DR)** is the process of restoring systems after a catastrophic failure. **DR planning** includes: risk assessment (identifying threats and their likelihood); business impact analysis (determining the cost of downtime for each system); DR strategy selection (cold site, warm site, hot site, active-active); recovery procedures (documented, tested, and regularly updated); and testing (annual DR drills). **Cold site**: a facility with power and cooling but no equipment (slowest recovery). **Warm site**: pre-configured equipment that requires data restoration. **Hot site**: fully operational mirror of production (fastest recovery, highest cost). **Active-active**: multiple sites serving traffic simultaneously (no single point of failure). In 2040, **cloud DR** (replicating VMs and data to a secondary cloud region) has made hot-site DR affordable for small and medium organisations.

**The Yggdrasil Backup Strategy** is a tiered approach: **Tier 1** (critical systems — ERP, student records, research data): continuous replication with 1-hour RPO, 4-hour RTO, stored in three locations (on-premises, Nordic Cloud Collective, Mímir Archive). **Tier 2** (important systems — email, file shares): daily backups, 24-hour RPO, 8-hour RTO. **Tier 3** (non-critical systems — development environments, logs): weekly backups, 7-day RPO, 48-hour RTO. **Immutable snapshots** are stored on WORM (Write Once Read Many) tape and optical media, protected against ransomware and insider threats. Students design a backup strategy for a simulated small business as part of the IT201 capstone.

**Required Reading:**
- W. Curtis Preston, *Backup & Recovery: Inexpensive Backup Solutions for Open Systems* (O'Reilly, 2007/2035), ch. 1–4
- Veeam, *The 3-2-1-1-0 Backup Rule* (2035 white paper)
- NIST, *Contingency Planning Guide for Federal Information Systems* (SP 800-34 Rev. 2, 2035)
- University of Yggdrasil, "The Yggdrasil Backup and Disaster Recovery Plan: A Tiered Approach" (2039)

**Discussion Questions:**
1. The 3-2-1-1-0 rule is comprehensive but expensive. For small organisations with limited budgets, which elements of the rule are most essential, and which can be deferred?
2. Immutable backups protect against ransomware but require specialised storage (WORM tape, optical media). Is the cost of immutable storage justified by the ransomware threat, or is it an overreaction to a rare event?
3. Cloud DR has made hot-site recovery affordable, but it also creates dependency on cloud providers. If a cloud provider experiences a regional outage, what is the fallback plan for organisations that rely on cloud DR?

---

## Lecture 10: Security Hardening and Compliance

A system is only as secure as its weakest configuration. This lecture covers security hardening practices for Linux and Windows, compliance frameworks, and the tools that enforce security posture.

**Linux security hardening** includes: **minimising the attack surface** (removing unnecessary packages, services, and users); **keeping systems patched** (automated security updates via `unattended-upgrades` or `dnf-automatic`); **configuring firewalls** (nftables/firewalld with default-deny rules); **hardening SSH** (disable root login, use key-based auth, change default port, enable fail2ban); **using SELinux or AppArmor** (mandatory access control frameworks that restrict what processes can do); **enabling auditing** (auditd for system call auditing); **encrypting data at rest** (LUKS for disk encryption, dm-crypt for containers); and **encrypting data in transit** (TLS 1.3 for all services). **Security benchmarks**: **CIS Benchmarks** (Center for Internet Security) provide detailed hardening guides for all major operating systems and applications. **OpenSCAP** automates benchmark assessment and remediation.

**Windows security hardening** includes: **enabling Windows Defender** (antivirus, firewall, exploit guard, application control); **configuring User Account Control** (UAC) at the highest setting; **enabling BitLocker** (full-disk encryption); **hardening PowerShell** (constrained language mode, logging, transcription); **using Windows Defender Application Control (WDAC)** or **AppLocker** (application whitelisting); **enabling Credential Guard** ( isolating credential storage from the OS); **configuring Attack Surface Reduction (ASR) rules** (blocking risky behaviours like executable content in email); and **enabling Windows Hello** (biometric authentication). **Microsoft Security Compliance Toolkit** provides GPO-based hardening templates. In 2040, **Microsoft Defender for Endpoint** is the unified security platform that replaces standalone tools.

**Compliance frameworks** define security standards that organisations must meet. **ISO/IEC 27001** is the international standard for information security management systems (ISMS). **NIST Cybersecurity Framework** (CSF) provides a risk-based approach: Identify, Protect, Detect, Respond, Recover. **PCI DSS** (Payment Card Industry Data Security Standard) applies to organisations that handle credit card data. **HIPAA** (Health Insurance Portability and Accountability Act) applies to healthcare organisations in the US. **GDPR** (General Data Protection Regulation) applies to organisations handling EU personal data. **SOC 2** (Service Organization Control) assesses security, availability, processing integrity, confidentiality, and privacy. In 2040, **continuous compliance** is the standard: automated tools (Qualys, Tenable, Rapid7, the University's *Vörðr Scanner*) continuously assess systems against benchmarks and frameworks, generating real-time compliance dashboards.

**The Yggdrasil Security Posture** is assessed quarterly against CIS benchmarks, NIST CSF, and the Nordic Data Compact. **Automated hardening**: Nordux ships with a hardening script (`/usr/local/bin/nordux-harden`) that applies CIS Level 2 settings. **Compliance dashboards** in the Yggdrasil SOC display: patch status (percentage of systems fully patched); benchmark scores (percentage of CIS controls passed); vulnerability counts (critical, high, medium, low); and incident metrics (mean time to detect, mean time to respond). Students run OpenSCAP scans and review compliance reports as part of IT201 labs.

**Required Reading:**
- CIS, *CIS Benchmarks for RHEL 10 and Windows Server 2040* (2040)
- NIST, *Cybersecurity Framework 2.0* (2035)
- Lee Brotherston & Amanda Berlin, *Defensive Security Handbook* (O'Reilly, 2018/2035), ch. 1–4
- Microsoft, *Windows Server 2040 Security Baseline* (2040)
- University of Yggdrasil, "Continuous Compliance: Automated Security Assessment with OpenSCAP and Vörðr" (2039)

**Discussion Questions:**
1. CIS benchmarks are comprehensive but can break functionality if applied blindly. Is benchmark compliance a genuine security improvement, or does it encourage checkbox security that prioritises passing audits over actual risk reduction?
2. Continuous compliance tools generate vast amounts of data, but remediation often requires manual effort. Is the bottleneck in compliance the detection of issues or the capacity to fix them?
3. The Nordic Data Compact imposes stricter requirements than GDPR in some areas (e.g., data localisation, algorithmic transparency). Is regional divergence in compliance frameworks beneficial (tailored to local values) or harmful (increases complexity for multinational organisations)?

---

## Lecture 11: Automation and Configuration Management at Scale

Managing one server manually is feasible; managing a thousand is not. This lecture covers the automation and configuration management tools that enable administration at scale.

**Configuration management** ensures that systems maintain a desired state. **Ansible** (agentless, Python-based, YAML playbooks) is the most popular open-source tool: it uses SSH to connect to managed nodes and executes tasks defined in playbooks. **SaltStack** (Python-based, event-driven, uses a message bus for real-time orchestration) is favoured for speed and scale. **Puppet** (Ruby-based, declarative, client-server model) has a long history in enterprise environments. **Chef** (Ruby-based, imperative recipes) is used by large SaaS companies. In 2040, **Ansible and SaltStack** dominate new deployments, while Puppet and Chef maintain large installed bases.

**Ansible in depth**. **Playbooks** are YAML files defining tasks to execute on hosts. **Inventory** defines managed hosts (static files or dynamic scripts). **Modules** perform specific tasks (apt, yum, copy, template, service, user, mount, etc.). **Roles** organise playbooks into reusable components. **Variables** parameterise roles and playbooks. **Handlers** trigger actions (e.g., restart nginx) only when notified by a task change. **Conditionals** (`when`) and **loops** (`with_items`) add logic. **Vault** encrypts sensitive data (passwords, keys) in playbooks. **Ansible Tower / AWX** provides a web UI, scheduling, and RBAC for Ansible. In 2040, **ansible-lint** and **molecule** (testing framework) are standard for ensuring playbook quality.

**Container orchestration** at scale uses **Kubernetes**. **Kubernetes administration** includes: cluster installation (kubeadm, kops, EKS, AKS, GKE); node management (joining, cordoning, draining); resource management (CPU/memory limits, quotas, LimitRanges); networking (CNI plugins, Services, Ingress, NetworkPolicies); storage (PVs, PVCs, StorageClasses); security (RBAC, PodSecurityPolicies / Pod Security Standards, secrets management); and workload management (Deployments, StatefulSets, DaemonSets, Jobs, CronJobs). **Helm** packages applications for Kubernetes. **Operators** (custom controllers) automate complex application lifecycle management. In 2040, **platform engineers** (the evolution of system administrators) design and manage internal Kubernetes platforms that developers use to deploy applications.

**Infrastructure as Code (IaC)** defines infrastructure in version-controlled code. **Terraform** (HashiCorp, HCL language) is the dominant multi-cloud IaC tool: it supports AWS, Azure, Google Cloud, Kubernetes, and hundreds of other providers. **Pulumi** (Python/TypeScript/Go/C#) provides general-purpose programming languages for IaC. **AWS CloudFormation** and **Azure Resource Manager** are cloud-native IaC tools. **Crossplane** (Kubernetes-based) enables platform teams to build custom cloud APIs. In 2040, **Terraform with Atlantis** (pull request-based Terraform workflows) is the standard for collaborative infrastructure management. The University's *Völundr* framework (built on Terraform and Ansible) manages all cloud and on-premises infrastructure.

**Required Reading:**
- Lorin Hochstein & René Moser, *Ansible: Up and Running* (3rd ed., O'Reilly, 2017/2035), ch. 1–6
- Kelsey Hightower, Brendan Burns & Joe Beda, *Kubernetes: Up and Running* (3rd ed.), ch. 1–5, 9–10
- Yevgeniy Brikman, *Terraform: Up and Running* (3rd ed., O'Reilly, 2022/2035), ch. 1–5
- Crossplane Documentation, "Getting Started" (2040)
- University of Yggdrasil, "Völundr: The Yggdrasil Infrastructure as Code Framework" (2039)

**Discussion Questions:**
1. Ansible is agentless (uses SSH), while Puppet and Chef require agents. Is the agentless model genuinely superior, or does it create problems with SSH key management, connection reliability, and performance at scale?
2. Kubernetes has become the standard for container orchestration, but its complexity is notorious. Is Kubernetes a necessary abstraction for modern infrastructure, or has the industry standardised on a tool that is more complex than most organisations need?
3. Terraform's HCL is a domain-specific language, while Pulumi uses general-purpose languages. Is the restriction of HCL a benefit (prevents abstraction abuse) or a limitation (prevents reusable patterns)?

---

## Lecture 12: The Platform Engineer — The Future of System Administration

The final lecture examines the evolution of system administration into platform engineering, the skills required for the role, and the future of IT operations in an AI-augmented world.

**Platform engineering** is the discipline of building internal platforms that enable developers to deploy, operate, and debug applications with minimal operational overhead. **Internal Developer Platforms (IDPs)** provide: self-service provisioning of environments; automated CI/CD pipelines; observability and alerting; security and compliance guardrails; and cost management. **Platform engineers** design and operate these platforms, acting as a bridge between infrastructure and application development. They are not "devs who do ops" or "ops who do dev" but a distinct role with its own skills and culture.

**Platform engineering skills** include: **Kubernetes expertise** (deep knowledge of cluster architecture, networking, storage, security, and troubleshooting); **cloud architecture** (multi-cloud design, cost optimisation, resilience patterns); **software engineering** (writing maintainable tools and automation in Go, Python, or Rust); **SRE practices** (SLOs, error budgets, incident management, postmortems); **product management** (treating the platform as a product with users — developers — who have needs and feedback); and **communication** (evangelising the platform, writing documentation, and gathering requirements). In 2040, **platform engineering** is one of the highest-demand IT specialisations, with salaries exceeding those of traditional system administrators by 30–50%.

**AI in operations** is transforming how platforms are managed. **AIOps** (AI for IT Operations) uses machine learning to: detect anomalies in metrics and logs; correlate alerts and reduce noise; predict failures before they occur; suggest remediation steps; and automate routine tasks (scaling, patching, backup verification). **AI-generated runbooks** (based on historical incident data) guide operators through novel problems. **AI-assisted coding** (Copilot, CodeWhisperer, Skald) accelerates the development of platform tools. However, AI also introduces risks: **hallucinated recommendations** (AI suggesting incorrect fixes); **over-reliance** (operators losing manual troubleshooting skills); and **adversarial AI** (attackers using AI to evade detection). The platform engineer of 2040 must be an **AI collaborator**: using AI to augment human judgment, not replace it.

**The Yggdrasil Platform** is the internal developer platform used by all University software projects. It provides: **Völundr IaC** (Terraform + Ansible for infrastructure); **Bifröst CI/CD** (GitLab-based pipelines with automated testing, security scanning, and deployment); **Muninn Observability** (Prometheus, Grafana, Loki, Tempo); **Heimdall Security** (SAST, DAST, dependency scanning, secret detection); **Freyja Cost Management** (cloud cost allocation, optimisation recommendations, carbon tracking); and **YVA Self-Service** (a natural-language interface for developers to request resources, check status, and troubleshoot). Students in IT201 deploy a microservice to the Yggdrasil Platform as their capstone, experiencing the full platform engineering lifecycle.

**Required Reading:**
- Matthew Skelton, Manuel Pais & Ruth Malan, *Team Topologies: Organizing Business and Technology Teams for Fast Flow* (IT Revolution, 2019/2035), ch. 4 ("Platform Teams")
- Evan Bottcher, "What Is Platform Engineering?" (Thoughtworks, 2022/2035)
- Charity Majors, "Platform Engineering: The Next Evolution of DevOps" (Honeycomb, 2033)
- Niall Murphy et al., *Site Reliability Engineering*, ch. 32 ("SRE Engagement Model")
- University of Yggdrasil, "The Yggdrasil Platform: A Case Study in Internal Developer Platforms" (2039)

**Discussion Questions:**
1. Platform engineering treats infrastructure as a product for developers. Is this product mindset a genuine improvement, or does it risk prioritising developer convenience over operational stability?
2. AIOps promises to reduce operational toil, but it also raises concerns about deskilling. Will platform engineers of 2050 still need deep troubleshooting skills, or will AI handle most operational problems?
3. The Yggdrasil Platform is comprehensive but requires significant maintenance. For smaller organisations that cannot afford a dedicated platform team, is it better to use a managed platform (e.g., GitHub Codespaces, Gitpod, Railway) or to accept less sophisticated tooling?

---

## Final Examination Preparation

The final examination for IT201 is a **practical capstone** (60% of grade) combined with a **written theory exam** (40% of grade).

**Practical Capstone (60%):**
Students are given a scenario: "You are the system administrator for a 50-person research group at the University of Yggdrasil. Design, implement, and document a complete IT infrastructure." Requirements:
- Deploy 5 Linux servers (web, database, file, monitoring, backup) and 2 Windows servers (domain controller, application server).
- Configure Active Directory with users, groups, and GPOs.
- Implement network segmentation with firewalls.
- Set up monitoring and alerting for all systems.
- Configure automated backups with a 4-hour RPO and 24-hour RTO.
- Harden all systems against CIS benchmarks and document deviations.
- Write Ansible playbooks and PowerShell DSC configurations for automated deployment.
- Produce a runbook documenting all procedures.

The capstone is evaluated on: technical correctness (does it work?); security posture (is it hardened?); documentation quality (is it clear and complete?); automation professionalism (are playbooks idempotent and tested?); and disaster recovery readiness (can the system be rebuilt from documentation and backups?).

**Written Theory Exam (40%):**
Choose 4 of 8 essay questions:

1. The system administrator's role has evolved from "computer janitor" to "platform engineer." Is this evolution a genuine professionalisation, or has it merely added layers of abstraction that distance engineers from the systems they operate?

2. systemd is both praised for its integration and criticised for its complexity. Analyse the arguments for and against systemd as an init system. Is systemd a net benefit for Linux administration?

3. Immutable distributions promise atomic updates and rollback, but they also limit customisation. Are immutable systems the future of Linux server administration, or will mutable systems always be necessary?

4. Compare Ansible (agentless) and Puppet (agent-based) as configuration management tools. For what scale and environment is each best suited? Is one fundamentally better, or do they serve different niches?

5. The 3-2-1-1-0 backup rule is comprehensive but expensive. For a small research group with limited budget, which elements are essential and which can be deferred?

6. Kubernetes has become the standard for container orchestration, but its complexity is notorious. Is Kubernetes genuinely necessary for most organisations, or has the industry adopted a tool that exceeds their needs?

7. AIOps promises to reduce operational toil through AI-driven anomaly detection and remediation. Is AIOps a liberating technology or a deskilling threat?

8. Platform engineering treats internal infrastructure as a product. What are the risks of this product mindset, and how can organisations ensure that platform teams do not prioritise developer convenience over operational stability?

**Grading:**
- A (Excellent): A fully functional, secure, automated, and well-documented infrastructure. Written exam demonstrates deep understanding of administration principles and their practical application.
- B (Good): A competent infrastructure with minor gaps in security, automation, or documentation. Written exam is solid but lacks critical depth.
- C (Satisfactory): An infrastructure that meets minimum requirements but has significant gaps. Written exam shows basic understanding but limited analysis.
- D (Poor): A partially functional infrastructure or one with serious security flaws. Written exam is superficial or contains errors.
- F (Fail): No functional infrastructure or missing capstone. Written exam fails to demonstrate understanding of system administration.
