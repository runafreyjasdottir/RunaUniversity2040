# SA106: Filesystems & Storage Architecture — The Vaults of Yggdrasil
## Bachelor of Science in Computer Systems Administration — University of Yggdrasil, 2040

**Credits:** 4
**Term:** Year 1, Semester 2
**Prerequisites:** SA101 (Introduction to Systems Administration), SA103 (Computer Hardware & Peripherals)
**Description:** Comprehensive study of data storage architecture, filesystem internals, and the principles of reliable data management. Students master block devices, partition tables, RAID configurations, LVM, filesystem types (ext4, XFS, Btrfs, ZFS), network storage (NFS, SMB, iSCSI), object storage (S3-compatible), and distributed filesystems (Ceph). The course emphasizes data integrity, performance tuning, backup strategies, and the operational practices that ensure data survives hardware failure, human error, and disaster.

**Instructor:** Dr. Thorhallur Einarsson, Associate Professor of Storage Engineering and Keeper of the Yggdrasil Data Vaults
**Lab:** Mimir Storage Lab, Sublevel 1, Hakon Computing Centre
**Office Hours:** Thursdays 14:00-16:00, or by appointment

---

## Lectures

ᚠ **Lecture 1: The Nature of Persistent Storage — Why Data Must Survive**

**Course:** SA106 — Filesystems and Storage Architecture
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

In Norse mythology, Mimisbrunnr (Mimir's Well) is the source of all wisdom — the well from which Odin sacrificed an eye to drink the waters of knowledge. The well must never run dry, and its contents must never be corrupted. A filesystem is precisely this: a repository of knowledge that must persist across power failures, disk crashes, software bugs, and human mistakes. This introductory lecture examines why persistent storage matters, the fundamental properties that storage systems must guarantee, and the evolving landscape of storage technologies. The SA's highest obligation is to the data; systems can be rebuilt, but data, once lost, cannot be recreated.

### Key Topics

- **The Five Properties of Storage:** Durability (data persists after power loss), Consistency (data read matches data written), Availability (data accessible when needed), Integrity (data uncorrupted by media degradation or bit rot), Confidentiality (data protected from unauthorized access). These properties are interdependent and sometimes in tension — maximizing durability often reduces availability (synchronous replication adds latency).
- **The Storage Hierarchy:** CPU registers (nanoseconds, bytes) to CPU caches (nanoseconds, kilobytes) to DRAM (nanoseconds-microseconds, gigabytes) to NVMe SSD (microseconds, terabytes) to SATA SSD (tens of microseconds, terabytes) to HDD (milliseconds, terabytes) to network storage (hundreds of microseconds to milliseconds, petabytes) to object/tape storage (seconds, exabytes). Each level is 10-100x larger, slower, and cheaper.
- **Block Devices and Sectors:** The fundamental unit of storage is the block device — a sequence of addressable blocks (typically 512 bytes or 4096 bytes). Advanced Format drives use 4096-byte physical sectors (4Kn). The NVMe protocol eliminates SCSI/ATA command overhead, allowing millions of IOPS through multiple submission queues.
- **The Cost of Data Loss:** The 2023 Uptime Institute survey: 60% of outages cost over $100,000; 25% cost over $1 million. The SA's job is to ensure these costs are never paid because data is never lost.

### Lecture Notes

Data is the only irreplaceable asset in a computing system. Hardware can be replaced, software can be reinstalled, configurations can be reconstructed — but the customer database, the research dataset, or the ten-year audit log: once gone, it is gone forever. This is the Mimir principle: the well of knowledge must be kept full and pure. Every design decision in this course will be evaluated against this principle.

The storage hierarchy is the most important mental model for understanding storage performance. Each level is 10-100x larger than the level above it and 10-100x slower. DRAM is measured in nanoseconds and gigabytes; NVMe SSD in microseconds and terabytes; HDD in milliseconds and terabytes; network storage adds network latency on top. The SA places data at the right level: frequently accessed data on fast storage, archival data on cheap storage, and everything replicated for durability.

The mathematics of data loss are sobering. A drive with an Annualized Failure Rate (AFR) of 2% means that in a 50-drive array, approximately one drive fails per year. If using RAID 5 (single parity), the probability of an unrecoverable read error during rebuild after a drive failure is significant: with 12TB drives and a 10^-14 bit error rate, the probability of encountering an error during a RAID 5 rebuild with 10 remaining drives is approximately 35%. This is why RAID 6 (dual parity) and erasure coding are the standard in 2040.

### Required Reading

- Love, R. (2035). *Linux Kernel Development*, 4th Edition. Addison-Wesley. Chapter 12 (The Block I/O Layer).
- Gregg, B. (2034). *Systems Performance*, 2nd Edition. Addison-Wesley. Chapter 8 (Disk I/O).
- Patterson, D.A., Gibson, G., and Katz, R.H. (1988). *A Case for Redundant Arrays of Inexpensive Disks (RAID)*. ACM SIGMOD.

### Discussion Questions

1. A colleague argues that RAID is obsolete because cloud storage provides replication and durability. Under what circumstances is RAID still necessary? When can you rely on cloud replication alone?
2. Calculate the expected annual data loss probability for: a single drive with 2% AFR, a RAID 5 array of 5 drives with 2% AFR each, and a RAID 6 array of 6 drives.
3. DRAM is 1000x faster than NVMe. Why not store everything in DRAM? What are the cost, power, volatility, and capacity tradeoffs?

---

ᚢ **Lecture 2: Block Devices, Partition Tables, and LVM**

**Course:** SA106 — Filesystems and Storage Architecture
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Before a filesystem can exist, there must be a block device to store it on, and before data can be organized, the block device must be partitioned. This lecture covers the device hierarchy in Linux, partition tables (MBR and GPT), the Logical Volume Manager (LVM) that abstracts physical storage into flexible logical volumes, and the Device Mapper that underpins LVM and many other storage technologies.

### Key Topics

- **Block Device Hierarchy:** Physical devices (/dev/nvme0n1, /dev/sda), partitions (/dev/nvme0n1p1, /dev/sda1), MD RAID devices (/dev/md0), LVM logical volumes (/dev/mapper/vg0-root), and Device Mapper targets. Each layer adds abstraction.
- **Partition Tables:** MBR (Master Boot Record): 4 primary partitions, 2TB maximum, 32-bit sector addresses. GPT (GUID Partition Table): 128 partitions, 9.4 ZB maximum, 64-bit sector addresses, protective MBR for backward compatibility, CRC32 checksum for integrity. GPT is the 2040 mandatory standard.
- **Logical Volume Manager (LVM):** Physical Volumes (PVs), Volume Groups (VGs), Logical Volumes (LVs). LVM enables dynamic resizing (extend a filesystem without unmounting), snapshots (point-in-time copies for backup), and thin provisioning (allocate storage on demand).
- **Device Mapper:** The kernel framework underlying LVM, dm-crypt (disk encryption), dm-snapshot, dm-thin (thin provisioning), dm-multipath (multipath I/O), and dm-verity (integrity verification). The `dmsetup` command inspects and manages Device Mapper devices.

### Lecture Notes

The partition table is the first structure written to a new disk. GPT is the correct choice in 2040: it supports disks larger than 2TB, allows up to 128 partitions, stores a backup partition table at the end of the disk, and includes CRC32 checksums. The `gdisk` utility creates and manages GPT partitions; `parted` provides a more general interface.

LVM is the SA's best friend for storage management. Without LVM, resizing a filesystem requires either unmounting it (causing downtime) or having free space immediately after the partition. With LVM: `lvextend -L +10G /dev/mapper/vg0-root && resize2fs /dev/mapper/vg0-root` extends a live, mounted filesystem. LVM snapshots create point-in-time copies that require minimal additional storage (only changed blocks), making them ideal for consistent backups.

The Device Mapper is the unsung hero of the Linux storage stack. Every LVM logical volume, every encrypted partition (dm-crypt with LUKS), every thin-provisioned volume, and every multipath device is a Device Mapper target. When LVM commands fail, `dmsetup` provides the next level of detail.

### Required Reading

- LVM2 Resource Page (2040). https://sourceware.org/lvm2/.
- Yggdrasil Storage Provisioning Guide (2040). UoY Infrastructure Documentation.

### Discussion Questions

1. A production server has a 2TB root filesystem on LVM that is 95% full. Describe the step-by-step process to add a new physical disk, extend the volume group, extend the logical volume, and resize the filesystem, all without downtime.
2. LVM snapshots copy modified blocks to the snapshot volume. What happens when the snapshot volume fills up? How does this differ from ZFS snapshots?
3. GPT stores a backup partition table at the end of the disk. How does the system recover the primary table if it is corrupted?

---

ᚦ **Lecture 3: Linux Filesystems — ext4, XFS, and Data Organization**

**Course:** SA106 — Filesystems and Storage Architecture
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

The filesystem is the data structure that transforms a block device into an organized hierarchy of files and directories. This lecture covers ext4 (the reliable workhorse) and XFS (the high-performance choice for large files), their internal mechanisms (inode tables, extent maps, journaling modes), and the practical knowledge the SA needs to select, configure, and tune filesystems for production workloads.

### Key Topics

- **Inode Architecture:** The inode stores file metadata: type, permissions, owner/group, timestamps (mtime, atime, ctime), size, link count, and pointers to data blocks. Direct blocks, indirect blocks, double-indirect blocks. In ext4, extent trees replace the indirect block scheme.
- **ext4:** The default Linux filesystem. Journaling (ordered mode by default), extents, dir_index (HTree), bigalloc, metadata checksums. Maximum filesystem size: 16-60TB (depending on block size). ext4 is the safe, reliable choice.
- **XFS:** Silicon Graphics' filesystem ported to Linux. Extent-based allocation, delayed allocation, allocation groups (parallel allocation), online defragmentation. Excels at large file workloads. Maximum filesystem size: 8 exabytes. XFS cannot be shrunk (only grown).
- **Journaling Modes:** Ordered (default): data written before journal entry committed. Journal: both data and metadata written to journal (safest, slowest). Writeback: metadata journaled, data written directly (fastest, risk of corruption after crash).
- **Mount Options for Performance:** `noatime` (mandatory for performance), `discard` (TRIM for SSDs), `data=ordered` (default journaling mode).

### Lecture Notes

The inode is the heart of the Unix filesystem. When you create a file, the kernel allocates an inode from the inode table, populates it with metadata, and creates a directory entry linking the filename to the inode number. When you access a file by name, the kernel traverses the directory tree, finds the inode number, reads the inode, and follows the block pointers to the data. The filename is stored in the directory, not in the inode — which is why hard links work (multiple names can point to the same inode).

ext4 is the default for good reason: it is the most thoroughly tested and widely understood filesystem in the Linux ecosystem. Journaling in ordered mode ensures that after a crash, the filesystem is consistent: metadata changes are journaled, and data is written before the metadata that references it. The tradeoff is a small performance cost, negligible on modern hardware.

XFS excels at large, contiguous files. Its extent-based allocation represents a 10GB file as a few large extents rather than thousands of block pointers, reducing metadata overhead and improving sequential I/O. The practical recommendation: ext4 for root and OS filesystems, XFS for data and archive filesystems.

### Required Reading

- ext4 Documentation (2040). https://ext4.wiki.kernel.org/.
- XFS Documentation (2040). https://xfs.wiki.kernel.org/.

### Discussion Questions

1. An ext4 filesystem mounted with `data=writeback` has garbage data after a power failure. Explain why and what mount option would prevent it.
2. XFS cannot be shrunk. When is XFS the wrong filesystem choice? What alternatives exist?
3. The `noatime` mount option significantly reduces disk I/O. Why don't all distributions mount all filesystems with `noatime` by default?

---

ᚨ **Lecture 4: ZFS and Btrfs — Next-Generation Filesystems with Built-In Integrity**

**Course:** SA106 — Filesystems and Storage Architecture
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Traditional filesystems delegate data protection to external layers (RAID controllers, LVM, backup software). ZFS and Btrfs integrate RAID, volume management, checksumming, and snapshots into the filesystem itself. ZFS is the gold standard for data integrity; Btrfs is the Linux-native challenger. This lecture covers their architectures, advantages, and operational implications.

### Key Topics

- **ZFS Architecture:** Pools (vdevs organized into storage pools), datasets (filesystems and volumes within pools), snapshots (point-in-time copies). ZFS eliminates the separate volume manager: physical devices become vdevs (mirror, raidz1, raidz2, raidz3), vdevs become pools, datasets are carved from pools.
- **ZFS Data Integrity:** End-to-end checksumming: every block has a checksum stored in its parent pointer. On read, ZFS verifies checksums; if corrupted, ZFS reads from the redundant copy (mirror or parity) and returns correct data. This catches silent data corruption (bit rot).
- **ZFS Snapshots and Replication:** Space-efficient (only changed blocks), instantaneous (no I/O), replicated with `zfs send`/`zfs receive`. Incremental replication sends only changed blocks. Most efficient backup method available.
- **Btrfs Architecture:** Similar to ZFS (integrated volume management, checksumming, snapshots) but native to the Linux kernel. B-trees for all metadata and data. Subvolumes organize data. RAID 0, 1, 5, 6, 10 within the filesystem. More flexible device management than ZFS.
- **Btrfs vs. ZFS:** ZFS: mature, battle-tested, excellent integrity, CDDL license (not in mainline kernel). Btrfs: native kernel, flexible, RAID 5/6 unstable as of 2040, GPL. Use ZFS for production data integrity; Btrfs for workstations and root filesystems.

### Lecture Notes

ZFS represents a philosophical shift. In the traditional stack, the RAID controller provides redundancy, the volume manager provides flexibility, and the filesystem provides organization. If a block is corrupted on disk, none of these layers detect it. ZFS makes the filesystem the integrity authority: it checksums every block, verifies on every read, and automatically repairs using redundancy. This is the Mimir principle made concrete.

ZFS snapshots are the SA's most powerful tool for backup. Creating a snapshot takes milliseconds and requires no additional space initially. Only changed blocks consume space. The SA can create snapshots every 15 minutes with negligible overhead. Replication: `zfs send -i @snap1 pool0/data@snap2 | ssh backup-server zfs receive backup-pool/data`. Incremental replication sends only the changed blocks.

The choice between ZFS and Btrfs is practical. Use ZFS for data integrity-critical production storage (databases, archives, backups). Use Btrfs for root filesystems and workstations (where flexibility and native kernel support matter, and RAID 1/10 provides sufficient redundancy).

### Required Reading

- Bonwick, J. and Moore, B. (2033). *OpenZFS Administration Guide*, 5th Edition. Oracle Press.
- Btrfs Wiki (2040). https://btrfs.readthedocs.io/.

### Discussion Questions

1. A ZFS pool consists of two raidz2 vdevs of 8 drives each. One drive fails in each vdev simultaneously. Is data still accessible? How many more drives can fail?
2. Why is RAID 5/6 harder to implement in a CoW filesystem than in a traditional RAID controller? What specific failure scenario causes data loss?
3. Propose a vdev layout for a ZFS pool that must survive any two drive failures with maximum storage efficiency.

---

ᚱ **Lecture 5: RAID — Redundant Arrays and the Mathematics of Reliability**

**Course:** SA106 — Filesystems and Storage Architecture
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

RAID provides data redundancy and performance through aggregation. This lecture covers RAID levels 0-6, nested RAID (10, 50, 60), reliability mathematics (MTBF, AFR, probability of data loss during rebuild), software RAID (mdadm), and erasure coding for distributed storage.

### Key Topics

- **RAID Levels:** RAID 0 (striping, no redundancy, max performance), RAID 1 (mirroring, 50% capacity), RAID 5 (single parity, 1-disk redundancy, (n-1)/n capacity), RAID 6 (double parity, 2-disk redundancy), RAID 10 (mirrored stripes, best for databases).
- **Nested RAID:** RAID 10 (1+0): stripes across mirrored pairs. RAID 50 (5+0): stripes across RAID 5 groups. RAID 60 (6+0): stripes across RAID 6 groups.
- **Reliability Mathematics:** URE (Unrecoverable Read Error) rate of approximately 10^-14 per bit for enterprise drives. RAID 5 rebuild probability of data loss: P(loss) = 1 - (1 - URE)^N. For 12TB drives with 10 remaining drives, P is approximately 35%. RAID 6 reduces this to negligible levels.
- **Software RAID (mdadm):** Linux md driver creates, manages, and monitors RAID arrays. Advantages over hardware RAID: no vendor lock-in, transparent operation, works with any block device.
- **Erasure Coding:** (k, m) codes split data into k data chunks and m parity chunks; any k of k+m chunks can reconstruct. 8+4 = 66.7% efficiency vs. 3x replication = 33.3%. Used in Ceph, MinIO, and cloud object storage.

### Lecture Notes

RAID was proposed in the 1988 Patterson-Gibson-Katz paper to use inexpensive disks to match the performance and reliability of expensive mainframe disks at a fraction of the cost. The "I" originally stood for "Inexpensive."

RAID 5 is "the most dangerous RAID level" because during rebuild after a drive failure, the probability of encountering an URE on the remaining drives is significant. With modern 12TB+ drives and a bit error rate of 10^-14, the probability of data loss during RAID 5 rebuild exceeds 35%. RAID 6 (dual parity) reduces this to negligible levels.

RAID 10 is preferred for high-IOPS workloads. It stripes across mirrored pairs, so read performance scales with drive count and write performance with pair count. RAID 10 can survive up to half the drives failing (if no mirror pair loses both drives).

Practical RAID selection: RAID 0 for scratch data, RAID 1 for boot volumes, RAID 10 for databases, RAID 6 for archival storage, erasure coding for distributed/object storage. Never use RAID 5 for drives larger than 4TB.

### Required Reading

- Patterson, D.A., Gibson, G., and Katz, R.H. (1988). *A Case for Redundant Arrays of Inexpensive Disks (RAID)*. ACM SIGMOD.
- mdadm Documentation (2040). https://raid.wiki.kernel.org/.

### Discussion Questions

1. Design a storage array for a database workload: 10TB usable storage, 5000+ IOPS, survive 2 drive failures. Compare RAID 10 vs. RAID 6.
2. An mdadm RAID 1 array has one drive showing SMART errors. Describe the replacement procedure with minimal downtime.
3. Erasure coding provides 8+4 (66.7% efficiency) vs. triple replication (33.3%). Compare storage cost, repair bandwidth, CPU cost, and read latency.

---

ᚲ **Lecture 6: Network Storage — NFS, SMB, iSCSI, and FCoE**

**Course:** SA106 — Filesystems and Storage Architecture
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Modern infrastructure requires shared storage: multiple servers accessing the same data. This lecture covers network file storage (NFS, SMB/CIFS) and network block storage (iSCSI, NVMe-oF), the protocols, architectures, and operational practices the SA must master.

### Key Topics

- **NFS (Network File System):** NFSv4.2: stateful protocol, Kerberos security, delegation, compound operations, server-side copy. Mount options: hard vs. soft, rsize/wsize, noatime, sync vs. async. The 2040 standard: hard mounts with `intr` for all data-critical filesystems.
- **SMB/CIFS:** SMB3: multi-channel, encryption, continuous availability (transparent failover). Samba provides SMB/CIFS on Linux. Key features: oplock, share modes, NT ACLs.
- **iSCSI:** Block-level storage over IP. Initiator (client), target (server), IQN identifiers, LUNs (Logical Unit Numbers). Multipath I/O (dm-multipath) for redundancy. `targetcli` for target configuration; `iscsiadm` for initiator configuration.
- **NVMe over Fabrics (NVMe-oF):** NVMe commands encapsulated in RDMA (RoCEv2) or TCP. Microsecond-level latency for remote NVMe devices. The 2040 standard for high-performance network storage.

### Lecture Notes

NFS is the workhorse of Unix network storage. The Yggdrasil campus uses NFSv4.2 for all home directories and shared project spaces. NFSv4's statefulness enables proper locking, caching, and delegation. When the server grants a delegation, the client can cache and modify files locally, dramatically reducing server load.

The hard vs. soft mount decision is critical. Hard mounts (default) retry indefinitely if the server is unavailable; processes hang until the server returns. Soft mounts fail after a timeout, returning I/O errors. For data integrity, hard mounts are essential: soft mounts can cause data corruption. The 2040 standard: hard mounts with `intr` (allows signals to interrupt hung processes).

iSCSI provides block-level storage over IP. The initiator sees iSCSI LUNs as local block devices. This makes iSCSI ideal for database clusters requiring shared block storage. The SA configures multipath I/O for redundancy: if one network path fails, traffic shifts to the alternate path.

NVMe-oF provides near-local NVMe performance to remote devices with 10-20 microsecond latency overhead. Use NVMe-oF for workloads requiring absolute lowest latency: database logs, high-frequency trading, hyperconverged VMs.

### Required Reading

- NFSv4.2 Specification (RFC 7862, 7863). IETF.
- Samba Documentation (2040). https://www.samba.org/.
- Open-iSCSI Documentation (2040). https://www.open-iscsi.com/.

### Discussion Questions

1. Why are NFS soft mounts dangerous for data integrity? Describe the correct approach.
2. Design an iSCSI architecture for a 3-node database cluster needing 500GB data LUN and 10GB quorum LUN per node.
3. NVMe-oF over RDMA provides 10-20 microseconds latency overhead. For which workloads does this matter?

---

ᚷ **Lecture 7: Object Storage and Distributed Filesystems — Ceph and MinIO**

**Course:** SA106 — Filesystems and Storage Architecture
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Object storage and distributed filesystems shatter the single-server model. Data is spread across many servers, accessed via APIs rather than POSIX, and designed for scale beyond any single machine. This lecture covers S3-compatible object storage (MinIO), Ceph (unified distributed storage), the CRUSH algorithm, and the CAP theorem.

### Key Topics

- **Object Storage:** Data stored as objects in flat namespaces (buckets), accessed via HTTP (GET, PUT, DELETE). S3 API is the de facto standard. MinIO provides on-premise S3-compatible storage. Use cases: backup archives, media, data lakes, static hosting.
- **Ceph:** Unified distributed storage providing object (RADOS Gateway), block (RBD), and file (CephFS) from a single cluster. RADOS: self-healing, self-balancing object store. OSDs (Object Storage Daemons) on every storage node. MONs (monitors) maintain cluster state with Paxos consensus. MGRs (managers) provide dashboards.
- **CRUSH Algorithm:** Controlled Replication Under Scalable Hashing. Determines data placement across OSDs considering failure domains (host, rack), device types, and weights. Deterministic (same input, same output) but adjustable (topology changes relocate only affected objects).
- **CAP Theorem:** Consistency, Availability, Partition tolerance — choose at most two. Ceph chooses CP (consistency and partition tolerance). MinIO in erasure-coded mode provides AP for reads with eventual consistency for writes.

### Lecture Notes

Object storage abandons POSIX compatibility: no directories, no inodes, no file locks. Just buckets of objects accessed by unique keys. This simplicity enables horizontal scalability that POSIX filesystems cannot achieve. An S3-compatible store can serve billions of objects across thousands of servers.

Ceph's CRUSH algorithm eliminates the central mapping service. Each client and OSD calculates object placement independently using the CRUSH map. CRUSH is deterministic but adjustable, making Ceph self-managing at scale. Adding a new OSD automatically triggers data rebalancing without central coordination.

MinIO is simpler than Ceph: no MONs, OSDs, or CRUSH. It supports erasure coding and encryption, and provides a high-performance S3 API. Deploy: `minio server http://node{1...4}/data{1...4}` for distributed erasure-coded mode.

### Required Reading

- Weil, S.A., et al. (2006). *CRUSH: Controlled, Scalable, Decentralized Placement of Replicated Data*. OSDI.
- Ceph Documentation (2040). https://docs.ceph.com/.
- MinIO Documentation (2040). https://min.io/docs/.

### Discussion Questions

1. A startup needs 10PB of video storage with 99.999% durability. Compare Ceph 3x replication, Ceph 8+4 erasure coding, and cloud S3 in terms of cost, complexity, and durability.
2. CRUSH is deterministic. What propagation delay exists between a node failure and clients learning about it? How does Ceph handle this?
3. An application requires POSIX file locking. Explain why object storage cannot provide this, and describe what to use instead.

---

ᚻ **Lecture 8: Backup and Recovery — The Norns' Red Thread of Data Preservation**

**Course:** SA106 — Filesystems and Storage Architecture
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

In Norse mythology, the Norns — Urthr (Past), Verthandi (Present), and Skuld (Future) — weave the threads of fate. The SA plays a similar role with data: the backup strategy determines which threads can be rewoven after catastrophe. This lecture covers backup strategies, tools, and operational practices: the 3-2-1 rule, full/incremental/differential backups, deduplication, encryption, off-site replication, disaster recovery, and the testing regimen that ensures backups work when needed. A backup that hasn't been tested is not a backup — it is a wish.

### Key Topics

- **The 3-2-1 Rule:** 3 copies of data, on 2 different media types, with 1 copy off-site. Extended: 3-2-1-1 (add one immutable copy). Immutable backups cannot be deleted even by administrators, protecting against ransomware.
- **Backup Types:** Full (complete copy), Incremental (changed since last backup), Differential (changed since last full). Tradeoffs: full is largest but simplest to restore; incremental is smallest but requires all incrementals in chain; differential is intermediate.
- **Deduplication and Compression:** Deduplication eliminates duplicate blocks across backups. Source deduplication (before transmission) vs. target deduplication (at backup server). Compression: lz4 for fast backup, zstd for archive.
- **Backup Tools:** restic (modern, encrypted, deduplicated, S3/SFTP backends), Borg Backup (efficient, deduplicated), Amanda/Bacula/Bareos (enterprise frameworks), Velero (Kubernetes-native).
- **Disaster Recovery (DR):** RTO (Recovery Time Objective): maximum acceptable time to restore. RPO (Recovery Point Objective): maximum acceptable data loss. Hot standby (near-zero RTO), warm standby (minutes), cold standby (hours). The Bifrost Mesh targets: RTO under 1 hour, RPO under 15 minutes.

### Lecture Notes

The most important fact about backups: untested backups are not backups. Backup failures are common: full tapes, changed network paths, lost encryption keys, corrupted deduplication databases, backups that ran but missed critical directories. The only way to know a backup works is to restore from it. The 2040 standard: monthly full restore tests for critical systems, quarterly for non-critical.

The 3-2-1-1-0 rule (3 copies, 2 media, 1 off-site, 1 immutable, 0 errors) is the gold standard. Immutable backups protect against ransomware that encrypts production data and then deletes backups before the encryption is detected. ZFS snapshots sent to a read-only target, S3 Object Lock in WORM mode, and offline tape cartridges provide immutability.

restic is the Yggdrasil standard for server backups. It encrypts (AES-256) before uploading, deduplicates at the block level, and supports S3, SFTP, and REST backends. Typical usage: `restic backup /data --tag hourly -r sftp:backup-server:/backups/server1`. Retention: `restic forget --keep-daily 7 --keep-weekly 4 --keep-monthly 12 --prune`. Restore: `restic restore latest --target /tmp/restore -r sftp:backup-server:/backups/server1`.

For Kubernetes clusters, Velero provides native backup of cluster resources and persistent volumes. Velero schedules backups as Custom Resources, integrates with S3-compatible storage, and supports namespace-level granularity. The SA defines a backup schedule: daily for development namespaces, hourly for production namespaces, weekly full cluster backup.

### Required Reading

- restic Documentation (2040). https://restic.readthedocs.io/.
- Velero Documentation (2040). https://velero.io/docs/.
- Yggdrasil Backup and Recovery Guide (2040). UoY Infrastructure Documentation.

### Discussion Questions

1. Design a backup strategy for a 50-server campus infrastructure with 100TB of data. Specify: backup type schedule, retention policy, storage backend, encryption, off-site replication, and testing frequency.
2. A ransomware attack encrypts all production data and then deletes all accessible backups. Describe how immutable backups (S3 Object Lock, ZFS read-only snapshots, offline tape) would have prevented total data loss.
3. Restic and Borg both use deduplication. Compare their approaches: how does each detect duplicate blocks? What are the tradeoffs in terms of memory usage, backup speed, and restore speed?

---

ᚹ **Lecture 9: Storage Performance Tuning — From IOPS to Latency**

**Course:** SA106 — Filesystems and Storage Architecture
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Storage performance is often the bottleneck in server workloads. This lecture covers the metrics (IOPS, throughput, latency, queue depth), the tools (fio, iostat, perf, eBPF), the tuning parameters (scheduler, read-ahead, write-back), and the systematic methodology the SA uses to identify and resolve storage performance problems.

### Key Topics

- **Performance Metrics:** IOPS (Input/Output Operations Per Second): the number of discrete I/O operations per second. Throughput (MB/s): data transferred per second. Latency (microseconds/milliseconds): time from I/O submission to completion. Queue depth: number of outstanding I/O requests. The relationship: throughput = IOPS x block size; latency increases as queue depth increases beyond the device's optimal parallelism.
- **Storage Benchmarks:** fio (Flexible I/O Tester): the gold standard for storage benchmarking. fio can simulate any workload: sequential read/write, random read/write, mixed read/write, with configurable block sizes, queue depths, and I/O engines. The SA uses fio to characterize a device's performance envelope before deploying it in production.
- **I/O Schedulers:** The Linux kernel I/O scheduler controls the order in which I/O requests are submitted to the device. mq-deadline: guarantees a maximum latency for each request, good for general-purpose use. bfq (Budget Fair Queueing): provides fair bandwidth allocation among processes, good for desktop and interactive use. none (no scheduling): optimal for NVMe devices with their own hardware queues. In 2040, NVMe devices use none; SATA/SAS devices use mq-deadline.
- **Performance Tuning Parameters:** Read-ahead (blockdev --setra): prefetch data into page cache. Write-back caching: allow the device to acknowledge writes before they hit stable storage (increases performance but risks data loss on power failure). Elevator merging: coalesce adjacent I/O requests into larger ones.
- **eBPF for Storage Observability:** bpftrace and bcc tools provide kernel-level visibility into I/O: which process is issuing I/O, what latency each request experiences, whether the I/O scheduler is working effectively. The `biosnoop` tool traces every block I/O request with its latency; `biolatency` shows latency histograms.

### Lecture Notes

The fundamental insight of storage performance is that IOPS and throughput are not independent metrics — they are related by block size. A device that delivers 100,000 IOPS at 4KB block size delivers 400 MB/s of throughput (100,000 x 4KB). The same device at 128KB block size delivers only 3,125 IOPS to achieve the same throughput (400 MB/s / 128KB). The SA must understand the workload's I/O pattern (sequential vs. random, read vs. write, small vs. large blocks) to select the right storage technology and tune it appropriately.

fio is the essential storage benchmark tool. A typical fio command: `fio --name=rand-read --ioengine=libaio --iodepth=32 --rw=randread --bs=4k --direct=1 --size=10G --numjobs=4 --runtime=60 --group_reporting`. This runs a 4-job random read workload at 4KB block size, 32 queue depth, on a 10GB file, for 60 seconds. The `--direct=1` flag bypasses the page cache to measure device performance, not cache performance. The SA should benchmark every new storage device before deploying it.

NVMe devices have caused a paradigm shift in I/O scheduling. Traditional HDD schedulers (CFQ, deadline) were designed to minimize seek time by reordering I/O requests to reduce head movement. NVMe devices have no seek time — they service requests from multiple hardware queues with no mechanical constraints. The kernel's none scheduler simply passes requests to the device in the order they arrive, letting the device's internal scheduler optimize for its own hardware. For NVMe, the kernel scheduler is overhead; removing it improves performance.

The iostat tool provides real-time I/O statistics: `iostat -xz 1` shows extended statistics every second. Key columns: r/s and w/s (reads and writes per second), rMB/s and wMB/s (throughput), await (average I/O latency in milliseconds), %util (device busy percentage). A device at 100% util with low await is performing well; a device at 100% util with high await is saturated and needs more spindles or faster devices.

### Required Reading

- Gregg, B. (2034). *Systems Performance*, 2nd Edition. Addison-Wesley. Chapter 8 (Disk I/O).
- fio Documentation (2040). https://fio.readthedocs.io/.
- Axboe, J. (2036). *Linux Block I/O: From Scheduler to NVMe*. LWN.net. (Deep dive into I/O scheduling.)

### Discussion Questions

1. An NVMe SSD delivers 500,000 IOPS at 4KB random reads. Calculate the throughput in MB/s. If the workload changes to 128KB sequential reads, how many IOPS does the device deliver at the same throughput?
2. A database server shows average I/O latency of 50ms during peak hours but 2ms during off-peak. Describe the systematic methodology to identify whether the bottleneck is storage device saturation, I/O scheduler misconfiguration, or application query patterns.
3. The none I/O scheduler is recommended for NVMe devices. Why is reordering I/O requests counterproductive for NVMe but beneficial for HDDs? What hardware feature of NVMe makes kernel scheduling unnecessary?

---

ᚬ **Lecture 10: Storage Security — Encryption, Access Control, and Data Destruction**

**Course:** SA106 — Filesystems and Storage Architecture
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Storage security encompasses three concerns: protecting data at rest (encryption), controlling who can access data (access control), and ensuring data is truly destroyed when no longer needed (data destruction). This lecture covers LUKS disk encryption, filesystem-level access controls (POSIX ACLs, SELinux contexts), secure erase, and the operational practices that ensure data confidentiality from cradle to grave.

### Key Topics

- **LUKS (Linux Unified Key Setup):** The standard for Linux disk encryption. LUKS creates an encrypted container on a block device with a header containing key slots (up to 8). The master key is encrypted with each key slot's passphrase. Advantages: key management (add/remove passphrases without re-encrypting), header backup (recover from damaged headers), and multiple key slots (emergency access passphrase plus daily passphrase). The SA uses `cryptsetup luksFormat`, `cryptsetup luksOpen`, and `cryptsetup luksAddKey`.
- **Full Disk Encryption vs. File Encryption:** Full disk encryption (LUKS) encrypts the entire block device — all data, all metadata, all free space. File encryption (eCryptfs, fscrypt) encrypts individual files, leaving metadata visible. Full disk encryption is simpler and more secure (no metadata leakage) but requires a passphrase at boot. File encryption allows per-user encryption and selective encryption.
- **POSIX ACLs:** Extended access control lists that supplement the traditional Unix rwx permission model. ACLs allow fine-grained permissions: user A can read, user B can read and write, group C has no access. Set with `setfacl`, viewed with `getfacl`. NFSv4 ACLs provide even richer semantics (deny entries, inheritance).
- **SELinux Contexts on Files:** SELinux enforces mandatory access control on files. Every file has a security context (type, role, user). Processes can only access files with contexts allowed by the SELinux policy. The SA must manage SELinux contexts on sensitive data: `chcon` to change, `restorecon` to reset to policy defaults, `semanage fcontext` for persistent changes.
- **Secure Erase:** ATA Secure Erase (firmware-level erase that overwrites all sectors), NVMe Format NVM (cryptographic erase for encrypted NVMe devices), and physical destruction (shredding, degaussing). The NIST 800-88 guidelines: Clear (overwrite), Purge (firmware erase or cryptographic erase), Destroy (physical destruction). The SA must follow the organization's data classification to determine the appropriate method.

### Lecture Notes

LUKS encryption is the foundation of storage security on Linux. When the SA sets up a new server, the root filesystem is encrypted with LUKS. At boot, the initramfs prompts for the passphrase, LUKS decrypts the master key, the device mapper creates a decrypted mapping (`/dev/mapper/root`), and the root filesystem is mounted. For headless servers, the SA uses a key file stored on a USB device or a network key server (Clevis/Tang) for automated decryption. The key management advantage of LUKS: multiple key slots allow adding an emergency passphrase without re-encrypting the entire disk, and removing a compromised passphrase by re-encrypting the master key with new keys.

Full disk encryption protects against physical theft: if an encrypted laptop is stolen, the thief cannot access the data without the passphrase. It does not protect against runtime attacks: when the system is running, the data is decrypted and accessible. For protection against runtime attacks (malware, compromised processes), the SA uses file encryption (eCryptfs for home directories, fscrypt for ext4 and F2FS) or application-level encryption (TLS for data in transit, application-level encryption for data at rest).

POSIX ACLs extend the Unix permission model from the simple owner/group/other rwx to arbitrary lists of users and groups with specific permissions. On the Yggdrasil campus, ACLs enable fine-grained access to shared project directories: the project group has rw access, the PI has rwx access, the audit team has read-only access, and all other users have no access. `setfacl -m u:pi:rwx,u:audit:r,d:u:pi:rwx,d:u:audit:r /projects/research-x` sets these permissions plus default ACLs for new files.

Secure erase is the SA's responsibility when decommissioning storage. For HDDs: ATA Secure Erase (the firmware overwrites every sector). For SSDs: NVMe Format NVM with cryptographic erase (the encryption key is deleted, making all data unreadable in microseconds). For classified data: physical destruction (shredding). The SA must document the erase method, verify completion, and maintain a chain of custody record.

### Required Reading

- cryptsetup Documentation (2040). https://gitlab.com/cryptsetup/cryptsetup/.
- NIST Special Publication 800-88 Rev. 1 (2014). *Guidelines for Media Sanitization*.
- Yggdrasil Disk Encryption and Erasure Policy (2040). UoY Security Office.

### Discussion Questions

1. A server with LUKS-encrypted root filesystem needs to boot unattended after a power failure. Describe two methods for automated key management (key file on USB, Clevis/Tang network key server) and their security tradeoffs.
2. Compare full disk encryption (LUKS) with file-level encryption (fscrypt) for a multi-user file server. When is each appropriate? What metadata does each leak?
3. A decommissioned SSD controller reports "Secure Erase Complete" but you need to verify the data is actually gone. Describe the verification process. What are the limitations of verification?

---

ᛁ **Lecture 11: Cloud and Hybrid Storage — S3, EBS, and the Multi-Cloud Data Fabric**

**Course:** SA106 — Filesystems and Storage Architecture
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Cloud storage is no longer an exotic alternative — it is a standard component of every storage architecture. This lecture covers the major cloud storage services (S3, EBS, EFS, Azure Blob, GCP Persistent Disk), the operational patterns for hybrid cloud storage, and the cost and performance models that determine when to store data on-premise versus in the cloud.

### Key Topics

- **S3 and Object Storage in the Cloud:** AWS S3 storage classes: Standard (frequently accessed), Standard-IA (infrequently accessed), Glacier (archive), Glacier Deep Archive (long-term archive). Lifecycle policies: automatically transition objects between classes based on age. S3 features: versioning, replication (cross-region and same-region), Object Lock (WORM), event notifications, and request metrics.
- **EBS (Elastic Block Store):** Network-attached block storage for EC2 instances. Volume types: gp3 (general-purpose SSD, up to 16,000 IOPS), io2 Block Express (provisioned IOPS SSD, up to 256,000 IOPS), st1 (throughput-optimized HDD), sc1 (cold HDD). EBS snapshots: point-in-time backups stored in S3, incremental, cross-region copy. Multi-attach: attach a volume to multiple instances for shared block storage.
- **EFS (Elastic File System):** Managed NFS filesystem that scales automatically. Performance modes: General Purpose (low latency, default), Max I/O (higher throughput, higher latency). Throughput modes: Bursting (default, based on storage size), Provisioned (fixed throughput). EFS is the simplest way to provide shared filesystem access to EC2 instances.
- **Hybrid Cloud Storage Patterns:** Cloud tiering (hot data on-premise, cold data in cloud S3), cloud burst (on-premise for normal load, cloud for peak), backup to cloud (on-premise primary, cloud secondary), and cloud-native (all data in cloud). The SA selects the pattern based on latency requirements, data sovereignty regulations, and cost.
- **Cost Models:** S3 pricing: $0.023/GB/month (Standard), $0.004/GB/month (Glacier Deep Archive). EBS: $0.08/GB/month (gp3). Data transfer: $0.01/GB (same region), $0.02-0.12/GB (cross-region). The SA must calculate total cost of ownership including egress fees, which often dominate the cost model.

### Lecture Notes

AWS S3 is the de facto standard for cloud object storage, and its API has become the universal language of object storage. MinIO, Ceph RADOS Gateway, and every major cloud provider implements the S3 API, making it the lingua franca for object storage. The SA must understand S3 storage classes and lifecycle policies to optimize costs: frequently accessed data stays in Standard, aging data transitions to Standard-IA after 30 days, and archival data transitions to Glacier after 90 days. A well-designed lifecycle policy can reduce storage costs by 70% without data loss.

EBS volumes are the cloud equivalent of local disks, with critical differences: they are network-attached (not directly attached), they can be detached from one instance and attached to another, and they can be snapshot independently. The gp3 volume type provides up to 16,000 IOPS and 1,000 MB/s throughput at baseline, with the option to provision additional IOPS. EBS snapshots are stored in S3 and are incremental: each snapshot contains only the changed blocks since the previous snapshot. The SA creates regular snapshots for backup and cross-region disaster recovery.

EFS is the simplest way to provide shared filesystem access in AWS. It auto-scales from gigabytes to petabytes without provisioning. Performance scales with storage size (bursting mode) or can be provisioned at a fixed throughput level. The SA mounts EFS on EC2 instances using NFSv4.1: `mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,intr fs-12345678.efs.region.amazonaws.com:/ /mnt/efs`. The key advantage: no capacity planning or provisioning required.

The hybrid cloud pattern of Bifrost Mesh uses on-premise MinIO as a hot tier and AWS S3 as a cold tier. Data is tiered automatically based on access patterns: objects not accessed in 30 days are transitioned to S3 Standard-IA, and objects not accessed in 90 days are transitioned to S3 Glacier. The SA configures the tiering policy in MinIO's ILM (Information Lifecycle Management) rules. This pattern provides the performance of on-premise storage for active data and the cost efficiency of cloud storage for archival data.

### Required Reading

- AWS S3 Documentation (2040). https://docs.aws.amazon.com/s3/.
- AWS EBS Documentation (2040). https://docs.aws.amazon.com/ebs/.
- MinIO ILM Documentation (2040). https://min.io/docs/minio/linux/administration/object-management/object-lifecycle-management.html.

### Discussion Questions

1. A research group generates 50TB of data per year, accessed frequently in the first month and rarely after that. Design an S3 lifecycle policy that minimizes cost while ensuring data is accessible within 12 hours when needed.
2. EFS and EBS serve different use cases. Under what circumstances is EFS preferable to EBS? When is EBS preferable? What are the performance tradeoffs?
3. A colleague proposes storing all data in S3 Standard to simplify operations. Calculate the monthly cost for 100TB of data in S3 Standard versus a tiered approach (20TB Standard, 30TB Standard-IA, 50TB Glacier). Include egress costs for 1TB/month of data access.

---

ᛃ **Lecture 12: The Future of Storage — Persistent Memory, Computational Storage, and the DNA Archive**

**Course:** SA106 — Filesystems and Storage Architecture
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

The storage landscape is evolving faster than at any point since the introduction of the HDD. Persistent memory (PMEM) blurs the line between RAM and storage, computational storage moves processing into the storage device, and DNA storage promises densities beyond any magnetic or electronic medium. This final lecture surveys these emerging technologies and their implications for the SA's role in the next decade. The Mimir principle endures: whatever the technology, the SA's obligation is to preserve and protect data.

### Key Topics

- **Persistent Memory (PMEM):** Byte-addressable, non-volatile memory that sits on the memory bus alongside DRAM. Intel Optane DC Persistent Memory (the first widely available PMEM) provides latency of ~300ns for reads (10x slower than DRAM, 1000x faster than NVMe). PMEM is accessed through the memory controller using the `memmap` kernel parameter or the `ndctl` utility. DAX (Direct Access) mode maps PMEM directly into the application address space, bypassing the page cache entirely. The `libpmem` and `libpmemobj` libraries provide persistent memory programming models.
- **Computational Storage:** Storage devices with embedded processors (ARM SoCs, FPGAs) that execute computation near the data. Computational storage drives (CSDs) run filtering, compression, encryption, and machine learning inference directly on the drive, reducing data movement between storage and CPU. The NVMe Computational Programs command set standardizes the interface for submitting compute tasks to CSDs.
- **Computational Storage Use Cases:** Database scan acceleration (filter rows on the drive, return only matching rows), video transcoding (transcode on the drive, eliminate data transfer), encryption at-rest (encrypt/decrypt on the drive, keys never leave the device), and AI inference (run models on the drive for edge computing). Each use case eliminates the need to move data to the CPU for processing.
- **DNA Storage:** Encoding digital data in synthetic DNA molecules. Theoretical density: 215 petabytes per gram of DNA. DNA storage is write-once, read-many (WORM) with current technology. Reading requires sequencing (currently hours for small datasets, projected minutes by 2045). Writing requires synthesis (currently expensive, projected 100x cost reduction by 2045). DNA storage is not yet practical for general use, but research prototypes have stored and retrieved data successfully.
- **The Yggdrasil DNA Archive Project:** The University of Yggdrasil's Yggsdrasil research group is developing a DNA-based archival system for long-term data preservation. DNA has a half-life of 500 years at room temperature (over 10,000 years at -20°C), making it the most durable storage medium known. The project aims to create a 1 PB DNA archive by 2045 for the university's irreplaceable research data.

### Lecture Notes

Persistent Memory (PMEM) changes the storage hierarchy fundamentally. Before PMEM, the gap between DRAM (nanoseconds) and NVMe SSD (microseconds) was a factor of 1000. PMEM operates at ~300 nanoseconds, bridging this gap. Applications can access PMEM as memory (via mmap and DAX) without going through the block I/O stack, eliminating the kernel overhead of syscalls, page cache, and I/O scheduling. For workloads that need persistence (databases, key-value stores), PMEM reduces write latency from microseconds to hundreds of nanoseconds, enabling new architectures like PMDK's libpmemobj for persistent data structures.

Computational Storage is the natural evolution of the NVMe offload model. Just as NVMe moved the I/O queue from the kernel to the device, computational storage moves computation to the device. A computational storage drive with an ARM SoC can filter a 10TB dataset and return only the matching 100MB — a 100x reduction in data transfer. The SA's role shifts from managing block devices to managing computational endpoints that return processed data rather than raw blocks. This is a profound change: the storage device is no longer a passive data repository but an active participant in computation.

DNA Storage represents the extreme end of data density and durability. DNA has a theoretical storage density of 215 PB per gram — enough to store the entire internet in a volume smaller than a coffee cup. The tradeoff is access latency: synthesizing DNA (writing) takes hours to days, and sequencing (reading) takes minutes to hours per access. DNA is ideal for archival data that must survive centuries: the Magna Carta, the collected works of humanity, the Yggdrasil University's irreplaceable research archives. The Yggdrasil DNA Archive Project is developing encoding schemes that achieve 80% of theoretical density with nested error-correcting codes (Reed-Solomon within DNA base sequences).

Looking ahead, the SA's role continues to evolve but the core principle remains: data must be preserved, protected, and accessible. Whether the medium is HDD, SSD, PMEM, computational storage, or DNA, the Mimir principle applies — the well of knowledge must never run dry, its contents must never be corrupted, and access must be available to those who need it.

### Required Reading

- Snir, M., et al. (2038). *Persistent Memory Programming: The PMDK Guide*, 3rd Edition. Intel Press.
-演变Cooper, A., et al. (2039). "Computational Storage: Moving Compute to Data." *ACM Computing Surveys*, 51(3).
- Organick, L., et al. (2020). "Random Access in Large-Scale DNA Data Storage." *Nature Biotechnology*, 38, 692-694.
- Yggdrasil DNA Archive Project Technical Report (2040). UoY Research Publication #YDA-2040-001.

### Discussion Questions

1. PMEM provides ~300ns latency but is 10x slower than DRAM and currently 4x more expensive. For which workloads does PMEM provide a clear advantage over DRAM + NVMe? When is DRAM + NVMe still the better choice?
2. A computational storage drive can filter rows at the drive and return only matching results. Describe how this changes the architecture of a data warehouse. What new security concerns arise when computation moves to the storage device?
3. DNA storage can preserve data for thousands of years but requires hours to read and days to write. Propose a storage architecture that uses DNA as the ultimate archive tier, PMEM as the fast tier, and NVMe SSD as the working tier. What are the tiering policies?

---

## Final Examination Preparation

### Format

The final examination consists of **8 essay questions**, from which you must choose **4** to answer. Each answer should be 800-1200 words and demonstrate both technical depth and practical application. Credit is given for specific commands, configurations, and architectures — vague generalizations receive minimal credit.

### Sample Essay Questions

1. **RAID and Reliability Debate:** A startup proposes using RAID 5 with 12TB drives for their database cluster, claiming "parity is enough." Calculate the probability of data loss during a RAID 5 rebuild with 12TB drives and a 10^-14 bit error rate. Explain why RAID 6 is the minimum acceptable choice for drives over 4TB. Present the mathematical analysis and discuss the operational implications for a 50-server campus deployment.

2. **ZFS vs. Btrfs for Production Storage:** The University of Yggdrasil needs to choose between ZFS and Btrfs for its student project storage cluster (200TB, 50 concurrent users). Compare the two filesystems across: data integrity mechanisms, snapshot and replication capabilities, RAID implementations and maturity, device management flexibility, licensing implications, and community support. Make a specific recommendation with justification.

3. **Backup Architecture Design:** Design a comprehensive backup strategy for the Yggdrasil campus infrastructure (50 servers, 100TB data, 24/7 availability requirement). Specify: backup schedule (full/incremental/differential), retention policy (daily/weekly/monthly/yearly), storage backends (on-site and off-site), encryption (at rest and in transit), immutable backup strategy (protection against ransomware), disaster recovery targets (RTO and RPO for each tier), and testing frequency and methodology. Justify each choice.

4. **Storage Performance Investigation:** A production database server experiences average I/O latency of 50ms during peak hours but 2ms during off-peak hours. Describe a systematic investigation methodology using iostat, fio, eBPF biosnoop, and application-level profiling to determine whether the bottleneck is: storage device saturation, I/O scheduler misconfiguration, filesystem mount option issues, or application query patterns. Present the commands, metrics, and decision criteria for each step of the investigation.

5. **Hybrid Cloud Storage Architecture:** Design a hybrid cloud storage architecture for a university with 500TB of research data. Active data (accessed within 30 days) must be accessible within 1 second. Archival data (not accessed in 90+ days) must be accessible within 12 hours and cost less than $0.01/GB/month. Specify: on-premise storage technology, cloud storage service, tiering policy, data sovereignty considerations (GDPR), encryption standards, and a cost comparison of your architecture versus all-cloud or all-on-premise.

6. **LUKS and Storage Security:** A university processes research data classified as "sensitive" under data protection regulations. Design a storage encryption architecture that provides: full disk encryption for all servers, per-project encryption keys (project data encrypted with project-specific keys, not recoverable by other projects' members), automated key rotation (keys rotated every 90 days without re-encrypting data), and secure decommissioning with verified data destruction. Describe the LUKS configuration, key management, eCryptfs/fscrypt layering, and the decommissioning procedure.

7. **Ceph Cluster Architecture:** Design a Ceph storage cluster for the Yggdrasil campus: 500TB usable storage, 10,000 IOPS, 99.99% availability. Specify: number and layout of OSDs, MONs, MGRs, MDSs, and RGWs; the CRUSH map topology (failure domains: host, rack, row); the pool configuration (replicated vs. erasure-coded, size, min_size, pg_num); and the network architecture (separate public and cluster networks). Explain how the cluster handles: one OSD failure, one rack failure, and one MON failure.

8. **The Future SA Role:** In 2010, the SA managed spinning disks, RAID controllers, and NFS servers. In 2040, the SA manages NVMe-oF, ZFS, Ceph, and cloud storage tiers. In 2050, PMEM, computational storage, and DNA archives may be standard. Discuss: How does the SA's role change as storage becomes more abstracted (from block devices to object APIs to computational endpoints)? What skills remain constant? What skills must the SA acquire? Argue for or against the proposition that "the SA's core skill is not knowledge of any particular storage technology, but the discipline of protecting data."

---

*May the Norns' threads guide your data safely through all the realms of storage. Frᛏr, Keeper of the Vaults, watches over every block that traverses the Bifrǫst between disk and memory. ᛏ*