# IT201: System Administration
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4  
**Description:** System Administration (Linux + Windows)

---

## Lectures

ᚠ **Lecture 1: The System Administrator's Role and Mindset**

**Course:** IT201 — System Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

System administration is the craft of keeping computer systems running: available, secure, performant, and correct. This opening lecture establishes the system administrator as a hybrid of engineer, diplomat, and emergency responder. Students will learn the mental models, ethical responsibilities, and operational disciplines that distinguish professional system administration from hobbyist tinkering. By 2040, system administration has evolved from manual server tending to AI-assisted infrastructure orchestration, but the fundamental mindset—paranoia, diligence, and calm under pressure—remains unchanged.

### Key Topics

- The system administrator's responsibilities: availability, integrity, confidentiality, and performance
- Operational maturity: from reactive firefighting to proactive engineering
- Change management: the CAB, peer review, and the philosophy of minimal change
- Ethics and professionalism: data privacy, transparency, and the administrator's privileged access
- The 2040 sysadmin: AI copilots, autonomous remediation, and human oversight

### Lecture Notes

System administrators hold the keys to the kingdom. Their accounts have privileges that ordinary users lack; their decisions affect the availability of services that thousands or millions depend upon; their mistakes can cause data loss, security breaches, and financial damage. This position of trust demands a professional ethic: the administrator must use their power only for legitimate purposes, respect user privacy even when technically capable of violating it, and prioritize organizational stability over personal convenience or curiosity.

**Operational maturity** progresses through stages, modeled by the UoY IT Guild's **Maturity Ladder** (2033): **Reactive** (fixing things when they break), **Managed** (monitoring and scheduled maintenance), **Defined** (documented procedures and change control), **Quantitative** (metrics-driven optimization), and **Optimizing** (continuous improvement with predictive analytics). Most organizations operate between Managed and Defined; the Optimizing stage, achieved by 2040 only by large tech companies and advanced research institutions like UoY, uses machine learning to predict failures before they occur and automatically apply remediations. The lecture emphasizes that maturity is not about tools but about discipline: a reactive team with Kubernetes is still reactive; a managed team with shell scripts and checklists can be highly effective.

**Change management** is the process by which modifications to production systems are proposed, reviewed, approved, and executed. The lecture covers: the **Change Advisory Board (CAB)**, which reviews high-risk changes; **peer review**, mandatory for all infrastructure code (Ansible playbooks, Terraform configurations, PowerShell scripts); **maintenance windows**, scheduled times when disruption is acceptable; and **rollback plans**, the requirement that every change must be reversible within a defined time. The 2031 *Unauthorized Kernel Upgrade Incident*—in which a junior administrator applied a security patch without testing or approval, causing a 6-hour outage of the student registration system—motivated UoY's strict change management policy.

**Ethics and professionalism** in system administration are not abstract concerns. Administrators routinely handle sensitive data: medical records, financial transactions, personal communications, and research data. The lecture covers: **data privacy** (minimizing access to what is necessary, logging all access, and never browsing data out of curiosity), **transparency** (communicating outages honestly, including root cause and timeline, without sugarcoating or blame-shifting), and **privileged access** (never sharing administrative accounts, using individual accounts with sudo or RBAC, and rotating credentials regularly). The 2034 *Sysadmin Espionage Case*—in which a disgruntled administrator exfiltrated research data before resigning—demonstrated the need for technical controls (data loss prevention, access logging) as well as cultural norms.

The **2040 sysadmin** works alongside AI assistants. **Autonomous remediation** systems (e.g., the UoY **Heimdall AI**, 2037) monitor metrics, detect anomalies, and apply predefined fixes: restarting a service that has crashed, scaling a cluster that is overloaded, or isolating a compromised endpoint. However, **human oversight** remains mandatory: the AI suggests, the human approves (or overrides). The lecture warns against **automation bias**—the tendency to trust AI decisions without critical evaluation—and emphasizes that the administrator remains accountable for all system changes, whether initiated by human or machine.

### Required Reading

- Limoncelli, T. A., Hogan, C. J., & Chalup, S. R. (2014). *The Practice of System and Network Administration* (3rd Edition). Addison-Wesley. Chapters 1–3.
- Yggdrasil IT Guild (2033). "The Maturity Ladder: A Model for IT Operational Excellence." *UoY IT Operations Manual* v6.0.
- Yggdrasil IT Operations (2031). "The Unauthorized Kernel Upgrade Incident: A Change Management Postmortem." *UoY Operations Review* 2031-09.
- Yggdrasil Ethics Committee (2034). "Privileged Access and Data Privacy: Guidelines for System Administrators." *UoY Ethics Policy* v4.1.
- Chen, J. (2037). "Heimdall AI: Autonomous Remediation at the University of Yggdrasil." *UoY AI Operations Report* 2037-03.

### Discussion Questions

1. Automation bias can lead administrators to accept incorrect AI recommendations. What training and interface design patterns can mitigate this risk?
2. Change management slows down deployments. For a security patch that addresses a critical vulnerability, should the CAB process be bypassed, accelerated, or maintained?
3. The 2034 Sysadmin Espionage Case involved a trusted insider. What technical controls can detect and prevent malicious insider actions without creating a surveillance culture?
4. Operational maturity models often assume large organizations. How should a two-person IT team at a small business adapt the maturity ladder to their constraints?

### Practice Problems

- Document a change management process for a hypothetical server upgrade. Include: change request, risk assessment, rollback plan, testing checklist, and post-implementation review.
- Analyze an AI-generated remediation suggestion (provided by the instructor). Identify the conditions under which you would approve it, override it, or escalate it to a senior administrator.

---

ᚢ **Lecture 2: Linux System Administration: Users, Permissions, and the Filesystem**

**Course:** IT201 — System Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Linux is the dominant server operating system in 2040, powering cloud infrastructure, embedded devices, and high-performance computing. This lecture covers the foundational concepts of Linux system administration: user and group management, the permission model, the filesystem hierarchy, and the tools that manipulate them. Students will learn to create and manage accounts, secure files and directories, and navigate the Linux filesystem with confidence.

### Key Topics

- User and group management: /etc/passwd, /etc/shadow, /etc/group, and modern alternatives
- POSIX permissions: read, write, execute for user, group, and others
- Advanced permissions: SUID, SGID, sticky bit, ACLs, and POSIX capabilities
- The Filesystem Hierarchy Standard (FHS): /etc, /var, /opt, /usr, /home, and /tmp
- Filesystem operations: mounting, checking (fsck), quotas, and encryption (LUKS)

### Lecture Notes

Linux's permission model, inherited from Unix (1970s), is simple in concept but subtle in practice. Every file and directory has an owner, a group, and three permission bits (read, write, execute) for the owner, the group, and everyone else. This **UGO (User-Group-Other)** model is sufficient for many scenarios but inadequate for complex environments. The lecture covers the model's basics and its extensions.

**User and group management** begins with the `/etc/passwd`, `/etc/shadow`, and `/etc/group` files. `/etc/passwd` contains user accounts (username, UID, GID, home directory, shell); `/etc/shadow` contains password hashes and aging information (readable only by root); `/etc/group` contains group definitions. By 2040, large organizations have moved to **LDAP** (Lightweight Directory Access Protocol) or **Active Directory** (via Samba/SSSD) for centralized authentication, but local files remain common on smaller systems and in containers. The lecture covers the `useradd`, `usermod`, `userdel`, `groupadd`, and `passwd` commands, as well as the `vipw` and `vigr` editors (which lock the files during editing to prevent corruption).

**POSIX permissions** use symbolic (`u+rwx,g+rx,o-rwx`) and numeric (`chmod 750 file`) notation. The lecture emphasizes common mistakes: `chmod 777` (world-writable files are a security risk), `chmod 644` on scripts (scripts need execute permission to run), and ignoring the distinction between file permissions (read = view content, write = modify content, execute = run as program) and directory permissions (read = list contents, write = create/delete files, execute = traverse). The **principle of least privilege** demands that files be readable and writable only by those who need access; the lecture provides a checklist for reviewing permissions on production systems.

**Advanced permissions** extend the UGO model. **SUID (Set User ID)** causes a program to run with the owner's privileges (e.g., `passwd` runs as root to modify `/etc/shadow`). **SGID (Set Group ID)** causes a program to run with the group's privileges, or causes new files in a directory to inherit the directory's group. **The sticky bit** on a directory (`/tmp`) prevents users from deleting files they do not own. **ACLs (Access Control Lists)** provide per-user and per-group permissions beyond the owner-group-other model (`setfacl`, `getfacl`). **POSIX capabilities** (introduced in Linux 2.2, refined through 2040) divide root privileges into fine-grained capabilities (`CAP_NET_ADMIN`, `CAP_SYS_PTRACE`, etc.), enabling programs to perform privileged operations without full root access. The lecture covers capability assignment (`setcap`, `getcap`) and the risks of excessive capability grants.

**The Filesystem Hierarchy Standard (FHS)** defines the directory structure of Linux systems. Key directories: `/etc` (configuration files), `/var` (variable data: logs, spools, caches), `/opt` (optional software packages), `/usr` (user programs and libraries), `/home` (user home directories), `/tmp` (temporary files, world-writable with sticky bit), `/boot` (bootloader files), `/dev` (device files), `/proc` (kernel and process information), and `/sys` (system information and control). The lecture explains the rationale behind each directory and common violations (installing software in `/home`, writing logs to `/tmp`). By 2040, **ostree** and **image-based Linux** (Fedora Silverblue, openSUSE MicroOS) have made `/usr` read-only by default, enforcing the FHS and preventing ad-hoc modifications.

**Filesystem operations** include mounting (`mount`, `umount`, `/etc/fstab`), checking (`fsck`, `e2fsck`, `xfs_repair`), quotas (`quota`, `edquota`, `repquota`—limiting disk usage per user or group), and encryption (`cryptsetup` with LUKS—Linux Unified Key Setup). The lecture covers LUKS full-disk encryption: creating an encrypted volume, opening it with a passphrase or key file, and automating unlock at boot via `/etc/crypttab`. By 2040, **transparent filesystem encryption** (ext4 encryption, fscrypt) is standard for home directories, protecting data at rest without manual volume management.

### Required Reading

- Nemeth, E., et al. (2017). *UNIX and Linux System Administration Handbook* (5th Edition). Addison-Wesley. Chapters 3–5.
- Linux Foundation (2040). *Filesystem Hierarchy Standard*. Version 4.0.
- Linux man pages (2040). `chmod(2)`, `chown(2)`, `capabilities(7)`, `acl(5)`, `cryptsetup(8)`.
- Yggdrasil Security Team (2032). "The World-Writable Web Root: A Postmortem on Permission Misconfiguration." *UoY Security Bulletin* 2032-11.
- Fedora Project (2039). "Immutable /usr: The Ostree Revolution in Linux Administration." *Fedora Magazine*.

### Discussion Questions

1. POSIX capabilities provide fine-grained privilege control, but most administrators still use sudo for privilege escalation. Is the complexity of capabilities worth the security gain, or does sudo provide adequate control?
2. Immutable /usr (ostree) improves security and reproducibility but complicates emergency fixes. How should an organization balance immutability against operational flexibility?
3. ACLs provide flexibility but can create permission complexity that is difficult to audit. Should ACLs be avoided in favor of group-based permission models?
4. LUKS encryption protects data at rest but does not protect against an attacker with live access to the running system. What additional controls are necessary for comprehensive data protection?

### Practice Problems

- Configure a Linux server with: a new user group `developers`, three users assigned to it, a shared directory `/srv/project` with SGID so new files inherit the group, and ACLs granting read access to an auditor user. Document each command and verify the permissions.
- Set up LUKS full-disk encryption on a test VM. Create the encrypted volume, format it with ext4, add it to `/etc/crypttab` and `/etc/fstab`, and verify automatic mount on reboot. Document the recovery procedure if the passphrase is lost.

---

ᚦ **Lecture 3: Linux System Administration: Package Management, Services, and Boot Process**

**Course:** IT201 — System Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

A Linux system is more than a kernel; it is an ecosystem of packages, services, and configurations that must be managed coherently. This lecture covers the mechanisms that install, update, and remove software; the systems that manage long-running processes; and the boot process that brings a machine from powered-off to operational. Students will learn to maintain a Linux system with confidence, applying updates safely and diagnosing boot failures.

### Key Topics

- Package management: apt, dnf, pacman, and snap/flatpak containers
- System services: systemd units, targets, timers, and dependencies
- The boot process: BIOS/UEFI, GRUB, initramfs, kernel boot parameters
- Kernel management: modules, parameters, and live patching
- Configuration management: /etc, dotfiles, and declarative system configuration

### Lecture Notes

**Package management** is the foundation of software maintenance. Different Linux distributions use different package formats and tools: **Debian/Ubuntu** use `.deb` packages with `apt`; **Red Hat/Fedora** use `.rpm` packages with `dnf`; **Arch** uses tarballs with `pacman`. The lecture covers common operations: `install`, `remove`, `update`, `upgrade`, `search`, and `info`. It also covers repository management: adding third-party repositories, GPG key verification, and pinning (controlling which versions are installed). By 2040, **universal package formats** (Snap, Flatpak) have gained traction for desktop applications, but server environments still prefer distribution-native packages for integration with the system's dependency resolution and security updates.

**Systemd**, adopted by most major distributions in the 2010s, is the init system and service manager in 2040. The lecture covers systemd's core concepts: **units** (services, sockets, devices, mounts, timers, targets), **targets** (milestones in the boot process, analogous to runlevels: `multi-user.target`, `graphical.target`), **dependencies** (`Requires=`, `Wants=`, `After=`, `Before=`), and **states** (active, inactive, failed, masked). Commands: `systemctl start/stop/restart/reload/enable/disable/status`. The lecture demonstrates writing a custom service unit for a web application, including: `Type=notify` (service signals readiness), `Restart=on-failure` (automatic restart), `User=` and `Group=` (least privilege), and `EnvironmentFile=` (externalized configuration). By 2040, systemd has expanded to include **homectl** (user home directory management), **portablectl** (portable services), and **systemd-cryptsetup** (encrypted volumes), making it the central management tool for Linux systems.

**The boot process** begins with firmware (BIOS or UEFI), which locates the bootloader (GRUB 2), which loads the kernel and initramfs. The initramfs (initial RAM filesystem) is a minimal root filesystem loaded into memory, containing essential drivers and tools to mount the real root filesystem. The lecture covers: **UEFI Secure Boot** (cryptographic verification of the bootloader and kernel), **GRUB configuration** (`/etc/default/grub`, `grub.cfg`), **kernel parameters** (`quiet`, `splash`, `root=`, `rd.luks.uuid=`), and **troubleshooting** (booting to single-user mode, emergency shell, rescue mode). The 2035 *GRUB Configuration Drift Incident*—in which automated updates to `/etc/default/grub` were not applied, causing boot failure after a kernel upgrade—demonstrates the importance of verifying configuration changes.

**Kernel management** includes module loading (`modprobe`, `insmod`, `rmmod`), parameter setting (`/etc/modprobe.d/`, kernel command line), and **live patching** (`kpatch`, `livepatch`). Live patching enables security patches to be applied to the running kernel without rebooting, critical for systems requiring high availability. The lecture covers the kpatch workflow: building a patch module from a source patch, loading it with `kpatch load`, and verifying with `kpatch list`. By 2040, live patching is standard for enterprise kernels, but the lecture warns of limitations: not all patches can be live-applied (structural changes require reboot), and live patches increase kernel complexity.

**Configuration management** ensures that system state is reproducible. The lecture covers: **/etc** as the configuration directory (and the importance of version-controlling `/etc` with etckeeper or git), **dotfiles** (user-specific configuration stored in home directories, managed with tools like chezmoi or GNU Stow), and **declarative configuration** (Nix, Guix, and Ansible provide declarative models where the desired state is specified and the system converges to it). By 2040, the UoY infrastructure team uses **NixOS** for research workstations: the entire system configuration is a Nix expression, enabling atomic upgrades, rollbacks, and reproducible environments.

### Required Reading

- Nemeth, E., et al. (2017). *UNIX and Linux System Administration Handbook* (5th Edition). Addison-Wesley. Chapters 6–8.
- systemd Documentation (2040). *systemd.unit, systemd.service, systemd.target Man Pages*. freedesktop.org.
- GRUB Documentation (2040). *GNU GRUB Manual*. GNU Project.
- Kernel.org (2040). *Linux Kernel Live Patching Documentation*. kernel.org.
- Yggdrasil IT Operations (2035). "The GRUB Configuration Drift Incident: Automated Updates and Manual Verification." *UoY Operations Postmortem* 2035-06.

### Discussion Questions

1. Systemd has been criticized for scope creep (absorbing functions traditionally handled by other tools). Is systemd's integration a benefit (consistent management interface) or a risk (single point of failure)?
2. Live patching enables zero-downtime kernel updates but cannot patch all vulnerabilities. For a system with a 99.999% availability SLA, what is the appropriate strategy combining live patching and scheduled reboots?
3. NixOS provides reproducible system configuration but has a steep learning curve. For an organization with 50 Linux servers, does the reproducibility benefit justify the training investment?
4. Snap and Flatpak package applications with their dependencies, reducing dependency hell but increasing disk usage and update complexity. For server environments, are universal packages appropriate?

### Practice Problems

- Write a systemd service unit for a Python web application. Include: socket activation, automatic restart on failure, resource limits (CPU, memory), logging to journald, and a health check. Test with `systemctl` and verify behavior under crash conditions.
- Apply a live kernel patch using kpatch or a similar tool. Document the process, verify the patch is active, and test that the patched function behaves correctly. Identify any limitations of the patch.

---

ᚨ **Lecture 4: Windows System Administration: Active Directory, Group Policy, and PowerShell**

**Course:** IT201 — System Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Windows remains the dominant desktop operating system in 2040 and a significant server platform, particularly in enterprise environments. This lecture covers the core technologies of Windows system administration: Active Directory (the directory service), Group Policy (centralized configuration management), and PowerShell (automation and scripting). Students will learn to administer Windows domains, enforce security policies, and automate management tasks at scale.

### Key Topics

- Active Directory: domains, forests, trees, trusts, and organizational units
- Group Policy: GPOs, inheritance, filtering, and security settings
- PowerShell for administration: AD cmdlets, WMI/CIM, and DSC
- Windows security: Defender, BitLocker, AppLocker, and Credential Guard
- Hybrid identity: Azure AD, Entra ID, and on-premises synchronization

### Lecture Notes

Active Directory (AD), introduced with Windows 2000 Server, is a **directory service**—a hierarchical database of network objects (users, computers, groups, printers, and organizational units) and their relationships. By 2040, AD has evolved into a hybrid system: on-premises AD Domain Services (AD DS) manages legacy resources, while **Microsoft Entra ID** (formerly Azure AD, rebranded 2033) manages cloud-native identity. The lecture covers AD architecture: **domains** (security boundaries with common policies), **trees** (contiguous namespaces), **forests** (collections of trees with transitive trusts), **trusts** (authentication pathways between domains), and **organizational units (OUs)** (containers for grouping objects and delegating administration).

**Active Directory administration** uses tools like Active Directory Users and Computers (ADUC), Active Directory Administrative Center (ADAC), and PowerShell's ActiveDirectory module. The lecture covers: creating and managing user accounts (`New-ADUser`, `Set-ADUser`), groups (`New-ADGroup`, `Add-ADGroupMember`), and computer accounts (`New-ADComputer`); **Group Policy** (centralized configuration that applies to sites, domains, or OUs); and **delegation** (granting non-administrators limited permissions to manage specific OUs). By 2040, AD administration is increasingly automated: new employee onboarding triggers PowerShell scripts that create accounts, assign licenses, configure mailboxes, and apply security group memberships based on role attributes.

**Group Policy Objects (GPOs)** are containers of settings that apply to AD objects. GPOs can configure: security settings (password policy, audit policy, user rights), software deployment (assigning or publishing applications), registry settings (controlling Windows features), and folder redirection (redirecting user profile folders to network shares). The lecture covers **GPO processing order**: local GPO → site GPO → domain GPO → OU GPO (LSDOU), with later GPOs overriding earlier ones unless **enforced** or **block inheritance** is set. **GPO filtering** (WMI filters, security group filtering) enables fine-grained targeting. The 2030 *GPO Cascade Failure*—in which a domain-level GPO enforced a restrictive firewall rule that blocked remote administration, locking administrators out of 500 servers—demonstrates the danger of misconfigured policy inheritance.

**PowerShell for Windows administration** extends the scripting concepts from IT105 to enterprise-scale management. The **ActiveDirectory** module provides cmdlets for user, group, and computer management. **WMI (Windows Management Instrumentation)** and **CIM (Common Information Model)** provide access to system hardware, software, and operational data (`Get-WmiObject`, `Get-CimInstance`). **DSC (Desired State Configuration)**, covered in IT105, is used to enforce configuration compliance across fleets of Windows servers. The lecture demonstrates a complete automation workflow: a scheduled PowerShell script that queries AD for stale accounts (not logged in for 90 days), disables them, moves them to a "Disabled" OU, and sends a notification to the security team.

**Windows security features** in 2040 include: **Windows Defender** (antivirus, anti-malware, and attack surface reduction), **BitLocker** (full-disk encryption with TPM and PIN protection), **AppLocker** (application whitelisting by path, publisher, or hash), and **Credential Guard** (isolating credential storage in a virtual secure mode, preventing Pass-the-Hash attacks). The lecture covers configuration: enabling Defender real-time protection, configuring BitLocker with TPM+PIN+recovery key backup to AD, creating AppLocker rules that allow only signed executables from trusted publishers, and verifying Credential Guard with `msinfo32`. The 2033 *Pass-the-Hash Epidemic*—in which attackers stole NTLM hashes from memory and reused them across the network—motivated widespread adoption of Credential Guard and LAPS (Local Administrator Password Solution).

**Hybrid identity** connects on-premises AD with cloud identity. By 2040, most organizations operate in a hybrid model: legacy applications authenticate against on-premises AD, while cloud services authenticate against Entra ID. **Azure AD Connect** (and its successor, **Microsoft Identity Manager 2040**) synchronizes users, groups, and passwords between on-premises and cloud. **Pass-through authentication** (PTA) and **seamless SSO** enable cloud authentication without storing passwords in the cloud. The lecture covers the **hybrid join** model: devices are joined to both on-premises AD and Entra ID, receiving policies from both. The 2036 *Sync Conflict Incident*—in which a bi-directional sync loop created duplicate accounts and corrupted group memberships—demonstrates the need for careful sync rule configuration and conflict resolution policies.

### Required Reading

- Stanek, W. R. (2022). *Windows Server 2022 Inside Out*. Microsoft Press. Chapters 4–6.
- Microsoft (2040). *Active Directory Documentation: Domains, Forests, and Trusts*. Microsoft Learn.
- Microsoft (2040). *Group Policy Documentation: Planning, Deployment, and Management*. Microsoft Learn.
- Microsoft (2040). *PowerShell Documentation: Active Directory, WMI/CIM, and DSC*. Microsoft Learn.
- Yggdrasil Windows Team (2033). "The Pass-the-Hash Epidemic: Credential Guard and LAPS Deployment." *UoY Security Report* 2033-08.

### Discussion Questions

1. GPO inheritance is powerful but can produce unexpected interactions between policies. Should organizations adopt a flat OU structure to simplify inheritance, or does hierarchy provide necessary organizational flexibility?
2. Credential Guard prevents Pass-the-Hash attacks but requires modern hardware (TPM 2.0, UEFI Secure Boot). For an organization with legacy hardware, is a hardware refresh justified solely for Credential Guard?
3. Hybrid identity synchronizes passwords between on-premises and cloud. Does this create a larger attack surface (compromise of either system exposes both), or does it reduce risk by centralizing identity management?
4. PowerShell automation in AD is efficient but can cause widespread damage if misconfigured. What safeguards (approval workflows, test environments, change logging) should govern AD automation scripts?

### Practice Problems

- Create an Active Directory forest with two domains and a trust relationship. Configure an OU structure for a fictional organization (departments, roles, locations). Create users, groups, and GPOs that enforce password complexity and screen lock settings. Test inheritance and delegation.
- Write a PowerShell script that audits all Windows servers in a domain for: BitLocker status, Windows Defender signature age, AppLocker policy compliance, and Credential Guard enablement. Generate a CSV report and email it to the security team.

---

ᚱ **Lecture 5: Process and Service Management**

**Course:** IT201 — System Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Processes are the running programs that consume CPU, memory, and I/O. Services are processes that run continuously in the background. This lecture covers the management of processes and services on both Linux and Windows: monitoring, scheduling, resource control, and lifecycle management. Students will learn to diagnose performance problems, terminate misbehaving processes, and ensure that critical services remain available.

### Key Topics

- Process concepts: PID, PPID, threads, states, and the process tree
- Linux process management: ps, top, htop, kill, nice, renice, cgroups, and systemd slices
- Windows process management: Task Manager, Resource Monitor, Process Explorer, and WMI
- Service management: systemd services, Windows services, and service dependencies
- Resource control: CPU limits, memory limits, I/O throttling, and prioritization

### Lecture Notes

A process is an instance of a program in execution. Each process has a unique identifier (PID), a parent process (PPID), an owner, a priority, and a set of resources (CPU time, memory pages, file descriptors). Understanding processes is essential for performance tuning, troubleshooting, and security auditing.

**Linux process management** uses a suite of tools: `ps` (snapshot of processes), `top` (dynamic, sorted view), `htop` (interactive, colorized, enhanced top), `pgrep`/`pkill` (find/kill by name), `kill` (send signals: SIGTERM for graceful shutdown, SIGKILL for forceful termination, SIGHUP for configuration reload), `nice`/`renice` (adjust priority), and `strace` (trace system calls). The lecture covers **process states**: running, sleeping (interruptible and uninterruptible), stopped, zombie (terminated but not reaped by parent), and orphan (parent terminated, adopted by init). By 2040, `btop` (a Rust-based system monitor) and `procs` (a modern `ps` replacement) have gained popularity, but the classical tools remain essential for compatibility and scripting.

**cgroups (control groups)**, integrated into systemd as **slices, scopes, and services**, provide fine-grained resource control. Administrators can limit CPU usage (`CPUQuota=50%`), memory (`MemoryMax=1G`), I/O bandwidth (`IOReadBandwidthMax=/dev/sda 100M`), and process count (`TasksMax=100`). The lecture demonstrates creating a systemd slice for a development team, restricting their total resource consumption to prevent runaway processes from impacting production services. By 2040, **cgroups v2** (unified hierarchy) is the standard, replacing the fragmented v1 controllers.

**Windows process management** uses graphical and command-line tools. **Task Manager** provides a basic view of running processes. **Resource Monitor** (resmon) provides detailed CPU, memory, disk, and network usage per process. **Process Explorer** (Sysinternals) provides advanced features: process tree, handle and DLL viewing, TCP/IP connections, and virus scanning integration. **WMI (Windows Management Instrumentation)** and **CIM** provide programmatic access to process data (`Get-Process`, `Get-CimInstance Win32_Process`). The lecture demonstrates using PowerShell to: find processes consuming >80% CPU, dump their memory for analysis, and restart the parent service if applicable.

**Service management** ensures that critical background processes start automatically, restart on failure, and run with appropriate privileges. On Linux, **systemd** manages services (Lecture 3). On Windows, the **Service Control Manager (SCM)** manages services registered in the registry (`HKLM\SYSTEM\CurrentControlSet\Services`). Commands: `sc query`, `sc start`, `sc stop`, `sc config`. PowerShell: `Get-Service`, `Start-Service`, `Stop-Service`, `Set-Service`. The lecture covers **service dependencies**: a database service must start before the application service; the SCM and systemd both resolve and enforce these dependencies. By 2040, **containerized services** (Docker, containerd) are common on both platforms, with orchestrators (Kubernetes, Nomad) managing service lifecycle across clusters.

**Resource control** prevents a single process from monopolizing system resources. **CPU limits** (cgroups CPUQuota, Windows Job Objects) cap processor usage. **Memory limits** (cgroups MemoryMax, Windows Working Set quotas) prevent out-of-memory conditions. **I/O throttling** (cgroups blkio, Windows Storage QoS) limits disk bandwidth. **Prioritization** (nice values on Linux, priority classes on Windows) ensures that critical processes get preferential access. The lecture covers the 2034 *Runaway Container Incident*, in which a memory leak in a container caused the host OOM killer to terminate the container runtime, cascading to all containers on the host. The lesson: always set memory limits on containers.

### Required Reading

- Love, R. (2013). *Linux Kernel Development* (3rd Edition). Addison-Wesley. Chapter 3 ("Process Management").
- Russinovich, M. E., Solomon, D. A., & Ionescu, A. (2012). *Windows Internals* (6th Edition). Microsoft Press. Chapter 5 ("Processes, Threads, and Jobs").
- systemd Documentation (2040). *Resource Control: CPU, Memory, and I/O Limits*. freedesktop.org.
- Sysinternals Documentation (2040). *Process Explorer: Features and Usage*. Microsoft.
- Yggdrasil IT Operations (2034). "The Runaway Container Incident: OOM Cascade in a Kubernetes Cluster." *UoY Operations Postmortem* 2034-12.

### Discussion Questions

1. cgroups v2 unified hierarchy simplifies resource management but breaks tools designed for v1. For an organization with legacy monitoring tools, is the migration to v2 worth the disruption?
2. Windows Job Objects provide resource control but are less flexible than cgroups. For a hybrid Windows/Linux environment, what abstractions (e.g., Kubernetes resource limits) can provide consistent resource control?
3. SIGKILL forcefully terminates a process without cleanup. Under what emergency conditions is SIGKILL justified, and what are the risks (data corruption, incomplete transactions)?
4. Container orchestrators manage service lifecycle but add complexity. For a single-node deployment, is Kubernetes justified, or should systemd services or Docker Compose suffice?

### Practice Problems

- Create a systemd slice that limits CPU to 50% and memory to 512MB. Run a CPU-intensive and memory-intensive process within the slice and verify that the limits are enforced. Document the cgroup v2 files that reflect the limits.
- Write a PowerShell script that monitors Windows services on a remote machine. If a critical service stops, the script should attempt restart, log the event, and alert via email if restart fails.

---

ᚲ **Lecture 6: Storage Management: Filesystems, LVM, RAID, and Storage Spaces**

**Course:** IT201 — System Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Storage is the persistent substrate of computing. This lecture covers the technologies that organize, protect, and manage disk space: filesystems, logical volume management, RAID, and Windows Storage Spaces. Students will learn to configure storage for performance, reliability, and scalability, with attention to the trade-offs between speed, redundancy, and cost.

### Key Topics

- Disk partitioning: MBR vs. GPT, fdisk, gdisk, and parted
- Filesystems: ext4, XFS, Btrfs, ZFS, NTFS, and ReFS
- LVM: physical volumes, volume groups, logical volumes, and snapshots
- RAID: levels 0, 1, 5, 6, 10, and software vs. hardware RAID
- Windows Storage Spaces: pools, tiers, and resilience types

### Lecture Notes

Storage administration is the art of balancing three competing goals: **capacity** (how much data can be stored), **performance** (how quickly data can be read and written), and **resilience** (how well data survives hardware failure). No single configuration optimizes all three; the administrator must understand the workload and choose appropriately.

**Disk partitioning** divides a disk into regions that the operating system treats as separate volumes. **MBR (Master Boot Record)**, the legacy partitioning scheme, supports up to 2TB disks and 4 primary partitions. **GPT (GUID Partition Table)**, the modern standard, supports disks up to 9.4 ZB and 128 partitions. The lecture covers partitioning tools: `fdisk` (MBR only, interactive), `gdisk` (GPT only), `parted` (both MBR and GPT, scriptable), and `sgdisk` (scriptable gdisk). By 2040, most systems use GPT with UEFI; MBR persists only in legacy and embedded systems.

**Filesystems** organize data on partitions. **ext4** (Fourth Extended Filesystem), the default for most Linux distributions, provides journaling (crash recovery), extents (efficient large file storage), and online resizing. **XFS**, developed by SGI, excels at large files and high concurrency, making it popular for databases and media servers. **Btrfs** (B-tree filesystem) provides copy-on-write, snapshots, compression, and RAID-like features at the filesystem level; by 2040, it is the default for openSUSE and Fedora desktops but still debated for production servers due to complexity. **ZFS** (Zettabyte File System), developed by Sun Microsystems and ported to Linux via OpenZFS, provides advanced features: pooled storage, copy-on-write, snapshots, compression, deduplication, and RAID-Z. The lecture covers ZFS architecture: **zpools** (pools of disks), **datasets** (logical volumes within pools), and **properties** (compression, quota, reservation). By 2040, ZFS is standard for NAS (Network Attached Storage) and backup systems. **NTFS** (Windows) and **ReFS** (Resilient File System, Windows Server) provide journaling, compression, and integrity streams (checksums for metadata and optionally data).

**LVM (Logical Volume Manager)** abstracts physical disks into flexible logical volumes. The architecture has three layers: **Physical Volumes (PVs)** (disks or partitions), **Volume Groups (VGs)** (pools of PVs), and **Logical Volumes (LVs)** (virtual partitions created from VGs). LVM enables: **online resizing** (extending or shrinking volumes without unmounting), **snapshots** (point-in-time copies for backups), **striping** (spreading data across PVs for performance), and **mirroring** (replicating data across PVs for redundancy). The lecture demonstrates: creating a VG from two disks, creating an LV, extending it by adding a third disk, and taking a snapshot before a risky upgrade. By 2040, **LVM thin provisioning** (allocating blocks on demand rather than upfront) is standard, improving storage utilization.

**RAID (Redundant Array of Independent Disks)** combines multiple disks for performance, capacity, or redundancy. **RAID 0** (striping) splits data across disks for speed but provides no redundancy. **RAID 1** (mirroring) duplicates data across disks for redundancy but halves usable capacity. **RAID 5** (striping with distributed parity) provides redundancy with N-1 capacity but requires at least 3 disks and has poor write performance due to parity calculation. **RAID 6** (double distributed parity) survives two disk failures but requires at least 4 disks. **RAID 10** (mirrored pairs striped) provides excellent performance and redundancy but uses 50% capacity. The lecture covers **software RAID** (mdadm on Linux, Storage Spaces on Windows) versus **hardware RAID** (dedicated controller cards). By 2040, hardware RAID has declined in favor of software RAID and ZFS RAID-Z, which provide more flexibility and avoid vendor lock-in.

**Windows Storage Spaces** is Microsoft's software-defined storage solution, analogous to ZFS or LVM. **Storage Pools** aggregate physical disks; **Storage Spaces** (virtual disks) are created from pools with resilience types (Simple, Two-way mirror, Three-way mirror, Parity); and **Storage Tiers** combine SSD and HDD for automatic tiering (hot data on SSD, cold data on HDD). By 2040, Storage Spaces Direct (S2D) enables hyper-converged infrastructure on Windows Server, though it faces competition from VMware vSAN and open-source Ceph.

### Required Reading

- Nemeth, E., et al. (2017). *UNIX and Linux System Administration Handbook* (5th Edition). Addison-Wesley. Chapter 8 ("Storage").
- ZFS Documentation (2040). *OpenZFS Documentation: Zpool, Dataset, and Property Management*. openzfs.org.
- Microsoft (2040). *Storage Spaces Documentation*. Microsoft Learn.
- Linux RAID Wiki (2040). *mdadm: Software RAID Management*. kernel.org.
- Yggdrasil Storage Team (2036). "ZFS vs. Hardware RAID: A Five-Year Reliability Study." *UoY Infrastructure Report* 2036-09.

### Discussion Questions

1. Btrfs provides RAID-like features at the filesystem level, while mdadm provides RAID below the filesystem. What are the trade-offs between filesystem-level and block-level RAID?
2. ZFS is powerful but memory-hungry (recommending 1GB RAM per TB of storage). For a small file server with 4TB and 8GB RAM, is ZFS appropriate, or should a simpler filesystem be used?
3. Thin provisioning improves utilization but can lead to overcommitment (allocating more logical space than physical). What monitoring and alerting are necessary to prevent thin-provisioned volume exhaustion?
4. ReFS provides integrity streams but is not supported for boot volumes. Should Windows administrators use NTFS for boot and ReFS for data, or standardize on NTFS for simplicity?

### Practice Problems

- Create a ZFS pool with three disks in RAID-Z1 configuration. Create datasets with different properties (compression, quota, snapshot schedule). Populate with test data, simulate a disk failure, and demonstrate replacement and resilvering.
- Configure Windows Storage Spaces with a tiered pool (SSD + HDD). Create a virtual disk with two-way mirroring, copy test data, and measure read/write performance. Document the automatic tiering behavior.

---

ᚷ **Lecture 7: Networking Configuration: IP, DNS, Routing, and Firewalls**

**Course:** IT201 — System Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Networks connect systems, and system administrators must understand how to configure, secure, and troubleshoot them. This lecture covers the practical networking skills required of a sysadmin: IP addressing, DNS configuration, static and dynamic routing, and firewall management on both Linux and Windows. Students will learn to build functional, secure networks from the command line.

### Key Topics

- IP addressing: IPv4, IPv6, CIDR notation, subnetting, and VLANs
- Network configuration: ip, nmcli, netplan, and Windows networking cmdlets
- DNS configuration: resolv.conf, systemd-resolved, Unbound, and Windows DNS
- Routing: static routes, dynamic routing (OSPF, BGP basics), and policy routing
- Firewalls: iptables/nftables, firewalld, and Windows Defender Firewall

### Lecture Notes

Networking is where system administration meets infrastructure engineering. The sysadmin does not need to be a network architect, but they must be able to configure interfaces, diagnose connectivity problems, and secure systems with host-based firewalls. This lecture bridges the gap between network theory (covered in IT104) and operational practice.

**IP addressing** in 2040 is predominantly **IPv6**, though **IPv4** persists in legacy systems and private networks. The lecture covers **CIDR notation** (e.g., `192.168.1.0/24` represents 256 addresses) and **subnetting** (dividing a network into smaller subnets). **VLANs (Virtual LANs)** segment networks at Layer 2, enabling logical separation of traffic without physical separation. The lecture demonstrates configuring VLAN interfaces on Linux (`ip link add link eth0 name eth0.10 type vlan id 10`) and Windows (`Add-NetAdapterAdvancedProperty`). By 2040, **VXLAN** (Virtual Extensible LAN) extends VLANs across Layer 3 networks, common in cloud and container environments.

**Network configuration** tools vary by distribution and era. The `ip` command (from iproute2) is the modern Linux standard, replacing deprecated `ifconfig` and `route`. `nmcli` (NetworkManager command-line) provides a higher-level interface. `netplan` (Ubuntu's YAML-based network configuration) abstracts multiple backends (NetworkManager, systemd-networkd). The lecture demonstrates: configuring a static IP, adding a default gateway, setting DNS servers, and configuring a bridge interface. On Windows, **PowerShell networking cmdlets** (`Get-NetIPAddress`, `New-NetIPAddress`, `Set-DnsClientServerAddress`, `Get-NetRoute`) provide comprehensive network configuration. By 2040, **cloud-init** standardizes network configuration across cloud providers, and **systemd-networkd** is the default for server distributions.

**DNS configuration** on Linux involves `/etc/resolv.conf` (traditionally edited manually, now managed by `systemd-resolved` or NetworkManager) and local DNS servers (Unbound, dnsmasq). The lecture covers: configuring a caching resolver (Unbound), setting up a split-horizon DNS (different answers for internal and external queries), and troubleshooting with `dig`, `nslookup`, and `host`. On Windows, DNS client configuration is managed via PowerShell or the GUI, and Windows Server provides DNS server roles with Active Directory integration (dynamic DNS updates for domain-joined computers). By 2040, **DNS over HTTPS (DoH)** is the default on both platforms, encrypting queries to protect privacy.

**Routing** determines how packets reach their destinations. **Static routes** (`ip route add 10.0.0.0/8 via 192.168.1.1`) are manually configured and suitable for simple networks. **Dynamic routing protocols** (OSPF, BGP) enable routers to exchange reachability information automatically. The lecture covers OSPF (Open Shortest Path First, an interior gateway protocol) and BGP (Border Gateway Protocol, the exterior gateway protocol of the internet) at a conceptual level, with practical examples using **FRRouting** (a Linux routing suite). **Policy routing** (source-based routing) enables traffic engineering: packets from a specific subnet or application can be routed through a different gateway. The lecture demonstrates a policy routing configuration for a multi-WAN setup, directing HTTP traffic through one ISP and VoIP traffic through another.

**Firewalls** enforce access control at the network level. On Linux, **nftables** (the successor to iptables, default since kernel 3.13) provides a rule-based packet filtering framework. **firewalld** (Red Hat's dynamic firewall manager) provides zones and services abstraction over nftables. The lecture covers: default-deny policies (drop all traffic not explicitly allowed), stateful inspection (allowing return traffic for established connections), and logging. On Windows, **Windows Defender Firewall** provides host-based filtering, configurable via PowerShell (`New-NetFirewallRule`). By 2040, **eBPF (extended Berkeley Packet Filter)** enables programmable packet filtering and network observability in the Linux kernel, used by tools like Cilium for container networking.

### Required Reading

- Stevens, W. R. (1994). *TCP/IP Illustrated, Volume 1*. Addison-Wesley. Chapters 1–3.
- Linux Documentation Project (2040). *Linux Networking HOWTO*. tldp.org.
- nftables Documentation (2040). *nftables: The New Firewall Framework*. netfilter.org.
- Microsoft (2040). *Windows Defender Firewall with Advanced Security*. Microsoft Learn.
- Yggdrasil Network Operations (2037). "eBPF in Production: Cilium and the Future of Host Firewalling." *UoY Network Report* 2037-05.

### Discussion Questions

1. IPv6 adoption reached critical mass in the 2020s, but IPv4 persists in 2040. What technical and economic factors sustain IPv4, and is dual-stack operation sustainable indefinitely?
2. nftables replaces iptables but introduces a new syntax and conceptual model. For an organization with thousands of iptables rules, is migration to nftables justified?
3. eBPF enables powerful network programming but requires kernel-level code. What are the security implications of deploying eBPF programs from third-party vendors?
4. Windows Defender Firewall provides host-based protection, but many organizations rely solely on network firewalls. Should host firewalls be mandatory for all systems, or is defense-in-depth redundant?

### Practice Problems

- Configure a Linux server with two network interfaces: one on a public subnet with a strict nftables firewall (allowing only SSH and HTTPS), and one on a private subnet with unrestricted access. Implement NAT for outbound traffic from the private subnet. Document the rules and test with `nmap`.
- Set up OSPF dynamic routing between three Linux routers using FRRouting. Verify route exchange with `vtysh` and test failover by disconnecting a link. Document the convergence time.

---

ᚹ **Lecture 8: Security Hardening: SELinux/AppArmor, Windows Defender, and Baselines**

**Course:** IT201 — System Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Every system is insecure by default; security must be deliberately configured. This lecture covers the hardening techniques that reduce attack surface on Linux and Windows: mandatory access control, endpoint protection, baseline configurations, and automated compliance checking. Students will learn to transform a default installation into a defensible fortress without breaking functionality.

### Key Topics

- Mandatory Access Control (MAC): SELinux and AppArmor
- Endpoint protection: Windows Defender, EDR, and Linux antivirus
- Security baselines: CIS Benchmarks, DISA STIGs, and organizational standards
- Automated hardening: OpenSCAP, Ansible hardening roles, and Group Policy
- Vulnerability management: scanning, patching, and exception handling

### Lecture Notes

**Security hardening** is the process of reducing a system's attack surface by disabling unnecessary services, enforcing strict permissions, applying patches, and configuring protective controls. It is not a one-time task but a continuous discipline: every change, update, and installation can reintroduce vulnerabilities. By 2040, **automated hardening** is the standard, with baselines enforced via configuration management and compliance verified via continuous scanning.

**Mandatory Access Control (MAC)** restricts what processes can do, independent of traditional discretionary permissions. **SELinux** (Security-Enhanced Linux, developed by the NSA) labels every process, file, and port with a security context (e.g., `httpd_t` for the web server, `httpd_sys_content_t` for web content) and defines policies that specify what transitions and accesses are permitted. SELinux modes: **Enforcing** (policy is active), **Permissive** (violations are logged but not blocked), and **Disabled**. The lecture covers: reading SELinux denials (`ausearch -m avc`), creating custom policies (`audit2allow`), and troubleshooting common issues (files mislabeled during manual copying). By 2040, SELinux is the default on RHEL and Fedora; **AppArmor** (an alternative MAC system used by Ubuntu and SUSE) provides profile-based confinement that is simpler but less flexible.

**Endpoint protection** on Windows is dominated by **Windows Defender** (antivirus, firewall, exploit protection, and attack surface reduction rules). By 2040, **EDR (Endpoint Detection and Response)** platforms (Microsoft Defender for Endpoint, CrowdStrike Falcon) provide behavioral analysis, threat hunting, and automated remediation. On Linux, traditional antivirus (ClamAV) is less common; instead, **EDR agents** and **runtime security tools** (Falco, Sysdig) monitor for anomalous behavior. The lecture covers configuring Windows Defender Attack Surface Reduction (ASR) rules, which block risky behaviors (e.g., Office apps creating child processes, executable content from email clients).

**Security baselines** are documented configurations that represent a hardened state. The **CIS (Center for Internet Security) Benchmarks** provide prescriptive guidance for hardening operating systems, applications, and network devices. **DISA STIGs (Security Technical Implementation Guides)** provide similar guidance for U.S. Department of Defense systems. By 2040, the UoY IT Guild maintains **Yggdrasil Security Baselines**, customized from CIS Benchmarks for the university's research and educational environment. The lecture covers the structure of a benchmark: recommendations (e.g., "Ensure SELinux is enforcing"), rationale, audit procedure, and remediation.

**Automated hardening** applies baselines consistently across fleets of systems. **OpenSCAP** (Open Source Security Compliance Solution) scans systems against SCAP (Security Content Automation Protocol) content and generates compliance reports. **Ansible hardening roles** (e.g., `dev-sec.os-hardening`) apply CIS-compliant configurations via playbooks. **Group Policy** enforces Windows baselines across Active Directory domains. By 2040, **continuous compliance** is the goal: systems are scanned daily, deviations are flagged automatically, and non-compliant systems are quarantined until remediated.

**Vulnerability management** is the cycle of scanning, prioritizing, patching, and verifying. **Vulnerability scanners** (Nessus, OpenVAS, Qualys) identify missing patches, misconfigurations, and known vulnerabilities. **Patch management** tools (WSUS, SCCM/ConfigMgr, Landscape, Katello) distribute updates. The lecture covers **patch prioritization**: critical security patches within 24 hours, high-severity within 7 days, moderate within 30 days. **Exception handling**: systems that cannot be patched (legacy dependencies, regulatory freeze) must be isolated, monitored, and documented. The 2033 *EternalBlue Redux*—in which a critical SMB vulnerability, patched months earlier, was exploited on unpatched systems—demonstrated that patch velocity, not patch availability, is the limiting factor.

### Required Reading

- CIS (2040). *CIS Benchmarks for Ubuntu Linux 24.04 LTS and Windows Server 2040*. Center for Internet Security.
- SELinux Documentation (2040). *SELinux Users and Administrators Guide*. Red Hat.
- Microsoft (2040). *Microsoft Defender for Endpoint Documentation*. Microsoft Learn.
- OpenSCAP Documentation (2040). *SCAP Workbench and oscap Command-Line Tool*. OpenSCAP Project.
- Yggdrasil Security Team (2033). "EternalBlue Redux: The Cost of Patch Delays." *UoY Security Bulletin* 2033-04.

### Discussion Questions

1. SELinux Enforcing mode breaks applications that are not SELinux-aware. Should organizations run in Permissive mode for compatibility, or invest in policy development for Enforcing mode?
2. EDR platforms collect detailed behavioral data for threat detection. What privacy protections are necessary when monitoring employee workstations?
3. Automated hardening can break legacy applications. How should organizations balance security compliance against operational continuity for critical legacy systems?
4. Patch velocity is often limited by testing cycles. For a critical vulnerability with active exploitation, should patches be deployed immediately (risking instability) or after testing (risking compromise)?

### Practice Problems

- Harden a Linux server using the CIS Ubuntu benchmark. Apply at least 20 recommendations, document each change, and verify compliance with OpenSCAP. Address any application breakages caused by the hardening.
- Configure Windows Defender Attack Surface Reduction rules on a test VM. Test each rule by attempting the blocked behavior (e.g., running an Office macro that launches PowerShell) and verify the block in the event log.

---

ᚺ **Lecture 9: Monitoring and Logging: syslog, journald, Event Viewer, and SNMP**

**Course:** IT201 — System Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

You cannot manage what you cannot see. This lecture covers the monitoring and logging infrastructure that provides visibility into system health, performance, and security events. Students will learn to configure centralized logging, set up metric collection, create alerting rules, and build dashboards—transforming raw data into operational insight.

### Key Topics

- Logging: syslog, rsyslog, journald, Windows Event Log, and structured logging
- Log aggregation: ELK/EFK stack, Loki, Splunk, and cloud logging services
- Metrics: Prometheus, Grafana, Nagios, and Windows Performance Monitor
- Alerting: threshold-based, anomaly detection, and on-call escalation
- SNMP: network monitoring, MIBs, and trap handling

### Lecture Notes

**Logging** is the practice of recording events: system startup, service restart, user login, file access, error conditions, and security violations. **Monitoring** is the practice of observing metrics: CPU usage, memory consumption, disk I/O, network throughput, and application response times. Together, logging and monitoring provide the observability necessary to detect, diagnose, and resolve problems.

**Linux logging** has two dominant systems: **syslog** (the traditional Unix logging daemon, with implementations like rsyslog and syslog-ng) and **journald** (systemd's logging component, storing logs in a binary format with indexed querying). Syslog sends logs to files (`/var/log/syslog`, `/var/log/auth.log`), remote servers, or databases. Journald stores logs in `/var/log/journal/`, accessible via `journalctl` (query by time, service, priority, or pattern). By 2040, most distributions use **journald as the default**, with optional syslog compatibility. The lecture covers log rotation (`logrotate`): preventing logs from filling disks by compressing and deleting old files. **Structured logging** (JSON format) enables machine parsing; by 2040, the UoY standard requires all application logs to be structured.

**Windows logging** uses the **Event Log** (classic) and **Event Tracing for Windows (ETW)** (high-performance, structured). Events are viewed in **Event Viewer** or queried with PowerShell (`Get-WinEvent`). The lecture covers: event levels (Critical, Error, Warning, Information, Verbose), channels (System, Application, Security, Setup, ForwardedEvents), and custom event sources. By 2040, **Windows Container Log** and **Sysmon** (System Monitor, part of Sysinternals) provide detailed process, network, and file system activity logging for threat detection.

**Log aggregation** centralizes logs from multiple systems for analysis. The **ELK stack** (Elasticsearch, Logstash, Kibana) and its successor the **EFK stack** (Elasticsearch, Fluentd/Fluent Bit, Kibana) are the dominant open-source solutions. **Loki** (Grafana Labs) provides a lightweight alternative, indexing only labels (not full text), reducing cost. **Splunk** is the enterprise standard, with powerful search and visualization but significant licensing costs. By 2040, cloud logging services (AWS CloudWatch, Azure Monitor, Google Cloud Logging) provide managed aggregation with AI-powered anomaly detection. The lecture covers: configuring Fluent Bit as a log forwarder, parsing unstructured logs with regex parsers, and creating Loki queries for troubleshooting.

**Metrics collection** tracks numerical measurements over time. **Prometheus** (the CNCF project) scrapes metrics from exporters (node_exporter for Linux, windows_exporter for Windows, custom application exporters) and stores them in a time-series database. **Grafana** visualizes Prometheus metrics in dashboards. The lecture covers: metric types (counters, gauges, histograms, summaries), PromQL (Prometheus Query Language), and alerting rules (configured in Alertmanager). **Nagios** (the legacy monitoring tool) and **Zabbix** remain in use for traditional infrastructure. **Windows Performance Monitor** (PerfMon) provides built-in metric collection and visualization. By 2040, **OpenTelemetry** has unified logging, metrics, and tracing into a single pipeline, though full adoption is incomplete.

**Alerting** transforms data into action. Threshold-based alerts fire when a metric exceeds a limit (CPU > 90% for 5 minutes). Anomaly detection alerts fire when metrics deviate from learned baselines (unusual network traffic at 3 AM). The lecture covers alert fatigue: too many alerts desensitize operators, leading to missed critical notifications. **On-call escalation** (PagerDuty, OpsGenie) routes alerts to the responsible engineer, escalating to managers if unacknowledged. By 2040, **AI-assisted alerting** (the UoY **Ratatoskr** system, 2038) correlates alerts across services, suppressing noise and identifying root causes.

**SNMP (Simple Network Management Protocol)** provides standardized monitoring for network devices (routers, switches, printers). **MIBs (Management Information Bases)** define the data available from each device. **SNMP polling** queries devices for metrics (interface traffic, CPU usage, temperature). **SNMP traps** are unsolicited notifications sent by devices when significant events occur (link down, high temperature). The lecture covers SNMP versions: v1 (plaintext community strings, insecure), v2c (improved performance, still plaintext), and **v3** (encryption and authentication, mandatory by 2040). Tools: `snmpwalk`, `snmpget`, `snmptrapd`, and monitoring platforms (LibreNMS, Nagios with SNMP plugins).

### Required Reading

- Nemeth, E., et al. (2017). *UNIX and Linux System Administration Handbook* (5th Edition). Addison-Wesley. Chapter 10 ("Monitoring").
- Prometheus Documentation (2040). *Prometheus: Monitoring and Alerting*. prometheus.io.
- Grafana Labs (2040). *Loki Documentation: Like Prometheus, but for Logs*. grafana.com.
- Microsoft (2040). *Windows Event Log and ETW Documentation*. Microsoft Learn.
- Yggdrasil Operations AI Lab (2038). "Ratatoskr: AI-Assisted Alert Correlation and Root Cause Analysis." *UoY Operations Research Report* 2038-09.

### Discussion Questions

1. Journald's binary log format is efficient but requires journald tools to read. Is this a reasonable trade-off, or does it create vendor lock-in compared to plain-text syslog?
2. Log aggregation systems like ELK are powerful but expensive to operate at scale. For an organization generating 1TB of logs daily, what retention and sampling strategies balance cost with observability?
3. Prometheus scraping requires services to expose metrics endpoints. For legacy applications without instrumentation, what approaches (sidecar exporters, log parsing, eBPF) can provide metrics?
4. SNMP v3 is secure but complex to configure. Why does SNMP v2c persist in 2040, and what organizational pressures sustain its use despite known vulnerabilities?

### Practice Problems

- Deploy a Prometheus + Grafana stack. Configure node_exporter on a Linux server and windows_exporter on a Windows server. Create dashboards for CPU, memory, disk, and network metrics. Set up alerting rules for high CPU and low disk space.
- Configure SNMP v3 on a network device (or SNMP agent). Set up LibreNMS or a similar tool to poll the device and receive traps. Verify that alerts fire correctly when simulated faults are injected.

---

ᚾ **Lecture 10: Virtualization and Containers for System Administration**

**Course:** IT201 — System Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Virtualization and containerization have transformed system administration from managing physical hardware to managing abstract compute resources. This lecture covers the technologies that enable this abstraction: hypervisors, virtual machines, containers, and the orchestration platforms that manage them at scale. Students will learn to deploy, secure, and troubleshoot virtualized workloads.

### Key Topics

- Virtualization: Type 1 and Type 2 hypervisors, KVM, VMware, Hyper-V
- Virtual machines: provisioning, cloning, snapshots, and live migration
- Containers: Docker, containerd, and the OCI runtime specification
- Container orchestration: Kubernetes fundamentals for sysadmins
- Security: hypervisor escape, container breakout, and image scanning

### Lecture Notes

**Virtualization** creates virtual versions of hardware resources. A **hypervisor** (virtual machine monitor) runs directly on hardware (**Type 1**, or bare-metal: VMware ESXi, Microsoft Hyper-V, Linux KVM) or on top of an operating system (**Type 2**: VMware Workstation, VirtualBox, Parallels). By 2040, Type 1 hypervisors dominate data centers; Type 2 is used for development and testing. **KVM (Kernel-based Virtual Machine)**, integrated into the Linux kernel since 2007, is the dominant open-source hypervisor, powering cloud providers and private clouds. The lecture covers KVM management with `libvirt` (`virsh`, `virt-manager`), including VM creation, network configuration (bridged, NAT, isolated), and storage (raw, qcow2 with copy-on-write snapshots).

**Virtual machine lifecycle management** includes: **provisioning** (creating from ISO, template, or cloud image), **cloning** (copying an existing VM), **snapshots** (capturing VM state for rollback), and **live migration** (moving a running VM between physical hosts without downtime). Snapshots are powerful but dangerous: snapshot chains degrade performance and consume storage; the lecture mandates periodic consolidation (merging snapshots into the base disk). Live migration requires shared storage (SAN, NAS, or distributed storage like Ceph) and compatible CPU features. By 2040, **NUMA-aware scheduling** (Non-Uniform Memory Access) ensures that VM memory is allocated on the same physical socket as its vCPUs, reducing cross-socket memory latency.

**Containers** provide operating-system-level virtualization: multiple isolated user spaces share a single kernel. **Docker**, released in 2013, popularized container packaging and distribution. By 2040, Docker has been superseded by **containerd** (the core runtime, donated to CNCF) and **Podman** (a daemonless, rootless container engine). The lecture covers the **OCI (Open Container Initiative) specification**, which standardizes container image format (`config.json`, `rootfs`) and runtime (`runc`, `crun`). Containers are lighter than VMs (sharing the kernel, no hardware emulation) but provide weaker isolation. The lecture emphasizes that **containers are not VMs**: they do not provide the same security boundary, and running untrusted workloads in containers requires additional safeguards (gVisor, Kata Containers, Firecracker).

**Container orchestration** automates the deployment, scaling, and management of containerized applications. **Kubernetes** (introduced 2014, dominant by 2020, ubiquitous by 2040) provides: **Pods** (groups of containers sharing network and storage), **Deployments** (declarative desired state for replica sets), **Services** (stable networking for pods), **ConfigMaps and Secrets** (configuration injection), and **Ingress** (HTTP routing). The lecture covers Kubernetes from the sysadmin perspective: cluster architecture (control plane: API server, etcd, scheduler, controller manager; worker nodes: kubelet, kube-proxy, container runtime), node management (`kubectl drain`, `kubectl cordon`), and resource limits (CPU/memory requests and limits). By 2040, **Kubernetes has become the universal infrastructure abstraction**, with virtualized workloads (KubeVirt) and serverless functions (Knative) running alongside containers.

**Security** in virtualized environments requires attention to isolation boundaries. **Hypervisor escape** (a VM breaking out to the host) is rare but catastrophic; mitigations include: keeping hypervisors patched, disabling unnecessary features (e.g., clipboard sharing, 3D acceleration), and using hardware-assisted virtualization (Intel VT-x, AMD-V) with IOMMU for device passthrough. **Container breakout** (a container process escaping to the host) is more common; mitigations include: running containers as non-root, using user namespaces, enabling seccomp and AppArmor/SELinux profiles, scanning images for vulnerabilities, and restricting capabilities. By 2040, **supply chain security** for containers (SBOMs, signed images, vulnerability scanning in CI) is as critical as runtime security.

### Required Reading

- Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th Edition). Wiley. Chapter 18 ("Virtual Machines").
- Docker Documentation (2040). *Docker Overview: Containers and Images*. Docker Inc.
- Kubernetes Documentation (2040). *Kubernetes Concepts: Cluster Architecture and Workloads*. kubernetes.io.
- OCI (2040). *Open Container Initiative Runtime Specification*. opencontainers.org.
- Yggdrasil Security Team (2035). "Container Breakout Trends: Analysis of CVEs and Mitigations." *UoY Security Report* 2035-07.

### Discussion Questions

1. Containers provide weaker isolation than VMs but better resource efficiency. For a multi-tenant environment hosting untrusted user code, should VMs or containers (with additional sandboxing) be used?
2. Kubernetes has become the universal abstraction, but its complexity is notorious. For a team managing 10 servers, is Kubernetes justified, or should simpler orchestrators (Nomad, Docker Swarm) be considered?
3. Snapshot chains in VMs improve flexibility but degrade performance. What policies should govern snapshot depth, age, and consolidation schedules?
4. Supply chain attacks on container images (compromised base images, malicious dependencies) are increasing. What verification steps (signature checking, SBOM review, vulnerability scanning) should be mandatory before deploying a container?

### Practice Problems

- Deploy a KVM virtual machine using libvirt. Create a VM from an ISO, configure bridged networking, take a snapshot, perform a destructive operation inside the VM, and restore from the snapshot. Measure snapshot creation and restoration times.
- Build a container image for a web application using a multi-stage Dockerfile. Scan the image with Trivy or Clair for vulnerabilities. Deploy the image to a Kubernetes cluster and configure resource limits, liveness probes, and horizontal pod autoscaling.

---

ᛁ **Lecture 11: Backup and Recovery Strategies**

**Course:** IT201 — System Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Data loss is not a question of if but when. This lecture covers the strategies, technologies, and procedures that protect organizational data against hardware failure, human error, malware, and disaster. Students will learn to design backup architectures, execute recovery procedures, and test restore processes—because an untested backup is no backup at all.

### Key Topics

- Backup types: full, incremental, differential, and synthetic full
- Backup targets: tape, disk, cloud, and hybrid architectures
- Backup software: Bacula, Bareos, Veeam, Restic, and BorgBackup
- Recovery procedures: file-level, volume-level, bare metal, and point-in-time
- The 3-2-1-1-0 rule and modern variations for ransomware resilience

### Lecture Notes

**Backup types** define what data is copied and how. A **full backup** copies all selected data; it is comprehensive but slow and storage-intensive. An **incremental backup** copies only data changed since the last backup (full or incremental); it is fast and small but requires the full backup plus all subsequent incrementals for recovery. A **differential backup** copies all data changed since the last full backup; it is larger than incremental but requires only the full plus the latest differential for recovery. A **synthetic full backup** combines a full backup with subsequent incrementals to create a new full backup without reading from the source—reducing source load. By 2040, **forever-incremental** backups (storing only changed blocks, with periodic consolidation) are standard, enabled by changed-block tracking at the filesystem or hypervisor level.

**Backup targets** have evolved from tape to disk to cloud to hybrid. **Tape** remains relevant for cold storage (air-gapped, offline, tamper-evident) and long-term archival, though its market share has declined. **Disk** (local NAS, SAN, or dedicated backup appliances) provides fast random access for restores. **Cloud** (object storage like S3, Azure Blob, Google Cloud Storage) provides elasticity and geographic distribution but introduces egress costs and dependency on network connectivity. **Hybrid** architectures combine local disk (for fast restores of recent data) with cloud (for disaster recovery and long-term retention). The lecture covers the UoY backup architecture: Bacula for on-premises servers, Veeam for virtualized workloads, and Restic for cloud-native containers.

**Backup software** varies by environment. **Bacula/Bareos** (open-source, client-server architecture) provides enterprise-grade scheduling, cataloging, and tape management. **Veeam** (commercial, virtualized-environment focus) provides agentless VM backup, instant VM recovery, and replication. **Restic** (open-source, modern) provides deduplication, encryption, and cloud-native storage backends. **BorgBackup** (open-source) provides deduplication, compression, and encryption for Linux servers. By 2040, **immutable backups** (write-once, with deletion protected by legal hold or multi-party approval) are standard for ransomware resilience; attackers cannot encrypt or delete backups they cannot access.

**Recovery procedures** must be documented, practiced, and verified. **File-level recovery** restores individual files or directories from backup. **Volume-level recovery** restores entire filesystems or disk images. **Bare metal recovery** restores a complete system (OS, applications, data) to new hardware after catastrophic failure. **Point-in-time recovery** restores a database or application to a specific moment, requiring continuous transaction log backups. The lecture emphasizes **recovery testing**: every backup must be restored at least quarterly to verify integrity. The 2036 *Yggdrasil Backup Verification Failure*—in which 20% of backups were found to be corrupted during routine testing, due to a silent hardware fault in the deduplication appliance—demonstrated that backup integrity cannot be assumed.

**The 3-2-1-1-0 rule** is the modern evolution of the classic 3-2-1 rule. **3** copies of data (primary + 2 backups). **2** different media types (e.g., disk and tape). **1** offsite copy (geographic separation). **1** immutable or air-gapped copy (ransomware protection). **0** errors (verified by automated recovery testing). By 2040, the rule has been extended for critical research data: **3-2-2-1-0** (two offsite copies in different continents) and **offline cryptographic verification** (hash chains proving backup integrity over time).

### Required Reading

- Preston, W. C. (2007). *Backup & Recovery*. O'Reilly. (Updated concepts for 2040 context.)
- Veeam Documentation (2040). *Veeam Backup & Replication: Best Practices*. Veeam Software.
- Restic Documentation (2040). *Restic: Backups Done Right*. restic.net.
- Yggdrasil IT Operations (2036). "The Backup Verification Failure: Silent Corruption and Recovery Testing." *UoY Operations Postmortem* 2036-03.
- NIST (2035). *Guidelines for Ransomware-Resilient Backup Strategies*. NIST SP 1800-25.

### Discussion Questions

1. Immutable backups protect against ransomware but complicate retention management (old backups cannot be deleted to free space). What governance processes are necessary for immutable backup lifecycle management?
2. Cloud backups provide geographic distribution but incur egress fees for recovery. For a 50TB dataset, how should on-premises and cloud targets be balanced for cost-effective recovery?
3. Backup verification testing consumes resources and time. For a system with 1,000 servers, what sampling strategy provides adequate confidence without excessive cost?
4. The 3-2-1-1-0 rule is comprehensive but expensive. For non-critical data (e.g., temporary build artifacts), what reduced protection level is appropriate?

### Practice Problems

- Design a backup architecture for a hypothetical organization: 50 Linux servers, 20 Windows servers, 10 databases (PostgreSQL, SQL Server), and 5TB of file shares. Specify backup types, targets, software, retention policies, and recovery time objectives (RTOs).
- Perform a bare metal recovery of a Linux VM from backup. Document each step: booting recovery media, restoring the disk image, reconfiguring network settings, and verifying application functionality. Measure total recovery time.

---

ᛃ **Lecture 12: Disaster Recovery and Business Continuity for Sysadmins**

**Course:** IT201 — System Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Disasters—natural, technological, and human-caused—can destroy data centers, disable networks, and halt operations. This final lecture covers the disciplines of disaster recovery (DR) and business continuity (BC): planning, testing, and executing procedures that restore critical systems after catastrophic events. Students will learn to classify workloads by criticality, design recovery architectures, and lead organizations through chaos with calm competence.

### Key Topics

- Disaster classification: natural, technological, human-caused, and cyber
- Business Impact Analysis (BIA): RTO, RPO, MTD, and workload criticality
- Recovery architectures: cold site, warm site, hot site, and active-active
- DR testing: tabletop exercises, simulations, and full-scale failover drills
- Cyber resilience: ransomware response, data integrity verification, and recovery

### Lecture Notes

**Disasters** are events that exceed the normal operational capacity of an organization. **Natural disasters** (earthquakes, floods, hurricanes) destroy physical infrastructure. **Technological disasters** (power grid failures, cooling system failures, cascading network outages) disable systems without physical destruction. **Human-caused disasters** (terrorism, sabotage, war) target infrastructure deliberately. **Cyber disasters** (ransomware, wiper malware, advanced persistent threats) destroy or encrypt data, rendering systems unusable. By 2040, cyber disasters are the most common cause of extended downtime, surpassing natural disasters in frequency and impact.

**Business Impact Analysis (BIA)** quantifies the consequences of system unavailability. Key metrics: **RTO (Recovery Time Objective)**—the maximum acceptable time to restore a system (e.g., 4 hours for email, 1 hour for payment processing). **RPO (Recovery Point Objective)**—the maximum acceptable data loss (e.g., 24 hours of email, zero for financial transactions). **MTD (Maximum Tolerable Downtime)**—the total time a business process can be unavailable before irreversible damage occurs. The lecture demonstrates a BIA worksheet: listing all IT services, assigning criticality tiers (Tier 1: life safety; Tier 2: revenue-generating; Tier 3: supporting; Tier 4: non-essential), and mapping RTO/RPO/MTD to each tier. By 2040, the UoY BIA is automated: continuous monitoring of system dependencies generates dynamic criticality scores.

**Recovery architectures** define the standby infrastructure available for failover. **Cold site**: a facility with power and network but no equipment; recovery requires procuring and configuring hardware (RTO: weeks). **Warm site**: a facility with pre-installed but unpowered equipment; recovery requires powering on and restoring data (RTO: days). **Hot site**: a facility with running equipment that mirrors production; recovery requires redirecting traffic (RTO: minutes to hours). **Active-active**: multiple sites running production workloads simultaneously; failover requires redirecting traffic away from the failed site (RTO: seconds to minutes). By 2040, active-active is the standard for Tier 1 services, warm site for Tier 2, and cloud-based DR (spinning up resources on demand) for Tier 3 and 4.

**DR testing** validates that recovery procedures work. **Tabletop exercises** walk through scenarios verbally ("What would we do if the data center flooded?"). **Simulations** execute recovery procedures in a test environment. **Full-scale failover drills** redirect production traffic to the DR site for a defined period, verifying that the site can handle real load. The lecture emphasizes that testing must be **regular** (quarterly for Tier 1, annually for Tier 2), **realistic** (using actual data and applications, not sanitized samples), and **documented** (with post-test reviews identifying gaps). The 2032 *Yggdrasil DR Drill Discovery*—in which a quarterly failover drill revealed that the DR site's database replication lag was 6 hours, exceeding the RPO—demonstrated the value of realistic testing.

**Cyber resilience** is disaster recovery adapted to ransomware and wipers. Traditional DR assumes the backup is clean; cyber DR must verify that backups are not compromised. The lecture covers: **isolated recovery environments** (air-gapped networks for restoring and verifying backups), **cryptographic integrity verification** (hash chains and signatures proving backups have not been tampered with), **forensic preservation** (capturing evidence before recovery destroys it), and **negotiation protocols** (whether to pay ransoms—a controversial decision with legal, ethical, and practical dimensions). By 2040, the UoY **Cyber Resilience Playbook** mandates: never pay ransoms (it funds criminals and does not guarantee recovery); maintain immutable offline backups; and practice "cyber fire drills" quarterly.

### Required Reading

- Wallace, M., & Webber, L. (2017). *The Disaster Recovery Handbook* (3rd Edition). Rothstein Associates.
- NIST (2034). *Contingency Planning Guide for Federal Information Systems*. NIST SP 800-34 Rev. 2.
- Yggdrasil IT Operations (2032). "The DR Drill Discovery: Replication Lag Exceeds RPO." *UoY Operations Postmortem* 2032-08.
- Yggdrasil Security Team (2039). "Cyber Resilience Playbook: Ransomware Response and Recovery." *UoY Security Standards* v8.0.
- SANS Institute (2040). *Business Continuity and Disaster Recovery Planning*. SANS Reading Room.

### Discussion Questions

1. Active-active architectures provide the lowest RTO but are expensive (duplicate infrastructure running at all times). For a non-profit with limited budget, what recovery architecture balances cost with resilience?
2. DR testing disrupts normal operations and risks accidental data corruption. What safeguards (isolated test networks, synthetic data, rollback plans) can minimize testing risk?
3. The "never pay ransoms" policy is principled but may result in permanent data loss if backups fail. Under what conditions, if any, should an organization reconsider this policy?
4. Cyber disasters often involve legal and regulatory obligations (data breach notification, evidence preservation). How should DR plans integrate with legal and compliance teams?

### Practice Problems

- Conduct a tabletop exercise for a specific disaster scenario (e.g., ransomware attack on the primary data center). Document the decision points, responsible parties, communication plan, and recovery steps. Identify at least three gaps in the current plan.
- Design a recovery architecture for a three-tier web application (load balancer, application servers, database). Specify RTO/RPO targets, backup strategies, failover mechanisms, and testing schedule. Include a cost estimate for the DR infrastructure.

---

## Final Examination Preparation

The IT201 final examination is a **practical hands-on assessment** conducted over 48 hours in a virtual lab environment. Students must complete **four of six** challenges:

1. **Linux Administration**: Given a Linux server with multiple misconfigurations (permission errors, failed services, network issues, security vulnerabilities), diagnose and fix all problems. Document each finding and remediation.
2. **Windows Administration**: Configure Active Directory for a fictional organization: create OUs, users, and groups; apply GPOs for security and software deployment; configure DFS for file sharing; and set up PowerShell automation for user onboarding.
3. **Storage Configuration**: Design and implement a storage solution for a database server: partition disks, create a RAID or ZFS pool, configure LVM, set up snapshots, and implement a backup schedule. Measure performance and document the configuration.
4. **Network Security**: Configure host-based firewalls on Linux and Windows, set up a VPN gateway, implement network segmentation with VLANs, and conduct a vulnerability scan. Remediate findings and document the security posture.
5. **Monitoring Deployment**: Deploy a monitoring stack (Prometheus, Grafana, Loki) for a mixed Linux/Windows environment. Configure metric collection, log aggregation, alerting rules, and dashboards. Verify end-to-end observability.
6. **Disaster Recovery**: Execute a DR failover drill for a provided application. Verify data integrity at the DR site, measure RTO and RPO, identify gaps, and produce an after-action report.

### Evaluation Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Correctness | 30% | Accurate diagnosis and remediation of issues |
| Security | 25% | Hardening measures, least privilege, and secure defaults |
| Documentation | 20% | Clear procedures, rationale, and troubleshooting notes |
| Efficiency | 15% | Appropriate tool selection and minimal downtime |
| Completeness | 10% | All requirements addressed, no outstanding issues |

---

*The systems stand because the administrator tends them. The logs are read, the backups verified, and the disaster prepared for. This is the quiet vigil that keeps the digital world turning.* ᛟ

— Runa Gridweaver Freyjasdottir, System Administration, University of Yggdrasil, 2040
