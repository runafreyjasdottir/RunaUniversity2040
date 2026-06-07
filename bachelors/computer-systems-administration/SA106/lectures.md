# SA106: Filesystems & Storage Architecture

## Overview

This course delves into the critical area of data storage, covering both traditional and modern filesystems, storage architectures, and the principles of reliable data management. Students will learn how data is stored, accessed, and protected across various media and systems, from local disks to distributed storage networks.

**Course Credits**: 4  
**Term**: Year 1, Semester 2  
**Prerequisites**: SA101 (Introduction to Systems Administration), SA103 (Computer Hardware & Peripherals)  

## Learning Objectives

By the end of this course, students will be able to:

1. Explain the principles of data storage and retrieval
2. Compare and contrast different filesystem types (ext4, XFS, Btrfs, ZFS, APFS, NTFS, etc.)
3. Understand storage hierarchies and caching mechanisms
4. Configure and manage storage devices and arrays (RAID, LVM, etc.)
5. Implement network-attached storage (NAS) and storage area networks (SAN)
6. Understand and work with object storage and distributed filesystems
7. Apply data protection strategies (backup, replication, snapshots)
8. Troubleshoot storage performance and reliability issues

## Week-by-Week Breakdown

### Week 1: Storage Fundamentals
- Bit, byte, block, sector: units of storage
- Magnetic vs solid-state storage (HDD vs SSD)
- NVMe and storage protocols (SATA, SAS, PCIe, Fibre Channel)
- Latency, throughput, and IOPS
- **Lab**: Identifying storage devices, benchmarking with fio

### Week 2: Filesystem Basics
- What is a filesystem? Metadata vs data
- Inodes, directories, and file allocation
- Journaling and copy-on-write
- Filesystem hierarchy standards (FHS)
- **Lab**: Creating and mounting filesystems, examining inodes

### Week 3: Linux Filesystems (ext4, XFS, Btrfs)
- ext4: features, limitations, tuning
- XFS: high-performance, scalability
- Btrfs: snapshots, subvolumes, checksums
- Choosing the right filesystem for the workload
- **Lab**: Creating ext4, XFS, Btrfs filesystems, comparing features

### Week 4: Advanced Filesystems (ZFS, APFS, ReFS)
- ZFS: pooled storage, copy-on-write, data integrity
- APFS: Apple's modern filesystem, space sharing
- ReFS: Microsoft's resilient filesystem
- Comparison of advanced features (deduplication, compression, encryption)
- **Lab**: Setting up ZFS pool, creating snapshots and clones

### Week 5: Storage Hierarchies and Caching
- CPU caches, disk caches, page cache
- Buffered vs direct I/O
- Read-ahead and write-back policies
- SSD caching for HDDs (write-back, write-through)
- **Lab**: Configuring bcache or dm-cache, measuring performance impact

### Week 6: Block Storage Management
- Partitioning (MBR vs GPT)
- Logical Volume Manager (LVM): PV, VG, LV
- Snapshots and thin provisioning
- Device Mapper (dm) and multipathing
- **Lab**: Creating LVM volumes, extending filesystems, using snapshots

### Week 7: Redundant Arrays (RAID)
- RAID levels: 0, 1, 5, 6, 10, 50, 60
- Hardware vs software RAID (mdadm)
- Rebuild processes and performance impact
- Nested RAID and hybrid approaches
- **Lab**: Configuring mdadm RAID arrays, simulating disk failure

### Week 8: Network Storage (NAS/SAN)
- NAS: NFS, SMB/CIFS, AFP
- SAN: Fibre Channel, iSCSI, FCoE
- Differences between file-level and block-level storage
- Performance and use case considerations
- **Lab**: Setting up an NFS server and client, iSCSI target and initiator

### Week 9: Distributed and Clustered Filesystems
- Lustre, GlusterFS, CephFS
- Hadoop HDFS
- Consistency models and CAP theorem
- Self-healing and self-managing storage
- **Lab**: Deploying a simple GlusterFS volume, testing failover

### Week 10: Object Storage
- S3 API and compatible implementations (MinIO, Ceph RADOSGW)
- Metadata and object versioning
- Lifecycle policies and tiering
- Use cases: backups, media archives, big data
- **Lab**: Setting up MinIO, creating buckets, configuring lifecycle rules

### Week 11: Data Protection and Backup Strategies
- Backup types: full, incremental, differential
- Backup targets: disk, tape, cloud
- Backup software: rsync, Borg, Restic, Veeam
- Snapshot-based backup and replication
- **Lab**: Creating a backup strategy with rsync and snapshots, testing restore

### Week 12: Storage Performance and Troubleshooting
- Measuring storage performance (latency, IOPS, bandwidth)
- Identifying bottlenecks (disk, controller, cable, protocol)
- Queue depth and scheduling algorithms
- Tools: iostat, iotop, blktrace, perf
- **Lab**: Performance tuning experiments, diagnosing slow storage

## Detailed Topics

### Storage Media Evolution
- From punch cards to magnetic tape to HDD to SSD to NVMe
- Emerging technologies: Storage Class Memory (SCM), Optane
- Shingled magnetic recording (SMR) and its implications
- NVMe over Fabrics (NVMe-oF)

### Filesystem Internals
- Superblock and mount options
- Journaling mechanisms (write-ahead logging)
- Copy-on-write (CoW) and implications for snapshots
- Extent-based vs block-based allocation
- Filesystem checking (fsck) and consistency

### Linux Storage Stack
- Virtual Filesystem Switch (VFS)
- Block layer and I/O schedulers (CFQ, deadline, BFQ, none)
- Device mapper and multipath I/O
- Loop devices and encrypted volumes (LUKS)

### Logical Volume Management (LVM)
- Physical Extents (PE) and Logical Extents (LE)
- Volume Group (VG) and Logical Volume (LV) commands
- Thin provisioning and thin snapshots
- LVM metadata and recovery

### RAID Deep Dive
- Parity calculation in RAID 5/6
- Rebuild impact and background initialization
- RAID 10 vs RAID 01
- Hot spares and automatic failover
- Monitoring RAID health with mdadm

### Network File System Protocols
- NFSv3 vs NFSv4: statefulness, security, performance
- SMB evolution: SMB1, SMB2, SMB3
- Authentication and encryption in network storage
- pNFS (parallel NFS) for scalability

### Object Storage Principles
- Flat namespace vs hierarchical
- Consistency models: eventual, strong, bounded
- Multi-region replication and conflict resolution
- Metadata indexing and search capabilities

### Data Integrity and Protection
- Checksums and scrubbing (ZFS, Btrfs)
- Erasure coding vs replication
- Write hole and battery-backed cache
- End-to-end data protection in storage stacks

### Storage for Virtualization and Containers
- Virtual disk formats (VMDK, VHD, QCOW2)
- Thin provisioning in hypervisors
- Container storage interfaces (CSI)
- Persistent volumes in Kubernetes

### Emerging Storage Technologies
- Computational storage: processing data where it resides
- Zoned namespaces (ZNS) SSDs
- Persistent memory (PMem) and DAX
- Storage offload to smart NICs (DPUs)

## Hands-On Labs

### Lab 1: Storage Device Identification and Benchmarking
- Use lsblk, hdparm, smartctl to identify devices
- Run fio to measure sequential and random I/O
- Compare HDD, SSD, and NVMe performance

### Lab 2: Filesystem Creation and Tuning
- Create ext4, XFS, Btrfs filesystems with various options
- Tune parameters (journal size, block size, inode ratio)
- Measure performance differences with fio

### Lab 3: LVM Management
- Create physical volumes, volume group, and logical volumes
- Extend and reduce logical volumes
- Create and merge snapshots
- Practice LVM recovery scenarios

### Lab 4: RAID Configuration and Fault Tolerance
- Build RAID 1, 5, 6, and 10 arrays with mdadm
- Simulate disk failure and monitor rebuild
- Test array performance under degraded mode
- Replace failed disk and verify array health

### Lab 5: Network File System Setup
- Configure NFS server with exports
- Mount NFS share on client and test performance
- Set up Samba server for Windows/Linux cross-platform sharing
- Test SMB multichannel and encryption

### Lab 6: Distributed Filesystem Experiment
- Deploy a 3-node GlusterFS trusted pool
- Create a replicated volume and test client access
- Simulate node failure and observe self-healing
- Benchmark read/write performance

### Lab 7: Object Storage with MinIO
- Install and configure MinIO server
- Create buckets and set policies
- Test S3 API compatibility with awscli
- Implement lifecycle rules for object expiration

### Lab 8: Backup and Restore Strategies
- Implement a backup plan using rsync and snapshots
- Test full and incremental backups
- Practice bare-metal recovery from backups
- Verify backup integrity with checksums

### Lab 9: Storage Performance Analysis
- Use iostat to identify device utilization and wait times
- Measure impact of queue depth on performance
- Test different I/O schedulers for various workloads
- Use blktrace to analyze I/O patterns

### Lab 10: Advanced Filesystem Features
- Test Btrfs send/receive for incremental backups
- Use ZFS send/receive for remote replication
- Enable compression and deduplication where applicable
- Create and manage filesystem snapshots for rollback

## Assessment and Grading

### Evaluation Components
- **Lab Exercises** (40%): Weekly hands-on storage labs
- **Quizzes** (20%): Bi-weekly knowledge checks
- **Midterm Exam** (15%): Written and practical components
- **Final Project** (15%): Design and implement a storage solution for a given scenario
- **Participation and Attendance** (10%): Engagement in discussions and lab work

### Lab Requirements
- Complete all assigned lab exercises
- Maintain a storage engineering lab journal
- Submit lab reports with configurations, performance data, and analysis
- Demonstrate ability to troubleshoot storage issues

### Exam Structure
- Multiple choice and short answer questions
- Filesystem and RAID calculations
- Storage architecture diagram interpretation
- Troubleshooting scenario analysis

## Recommended Resources

### Textbooks
- "Designing Data-Intensive Applications" - Martin Kleppmann
- "Linux File Systems" - various authors (Linux Documentation Project)
- "Storage Networks Explained" - Ulf Troppens et al.
- "File System Forensic Analysis" - Brian Carrier

### Online Resources
- The Linux Kernel Documentation (filesystems section)
- ZFS on Linux Documentation
- Btrfs Wiki
- Storage Networking Industry Association (SNIA) resources
- Vendor-specific documentation (e.g., Ceph, GlusterFS, MinIO)

### Tools and Software
- fio for flexible I/O testing
- iostat, iotop, blktrace for performance analysis
- mdadm for Linux RAID management
- lvm2 for LVM management
- parted/gparted for partitioning
- Ceph, GlusterFS, MinIO for distributed storage labs
- rsync, Borg, Restic for backup practice

## Professional Applications

### Systems Administration Relevance
- Storage knowledge is essential for:
  - Capacity planning and storage procurement
  - Performance tuning of database and application servers
  - Implementing backup and disaster recovery plans
  - Managing virtualization and container storage
  - Ensuring data integrity and compliance

### Career Pathways
- Storage Administrator
- Database Administrator (storage aspects)
- Backup and Recovery Engineer
- Cloud Storage Engineer
- Data Center Operations Technician
- Systems Engineer (infrastructure focus)

## Conclusion

SA106 provides a comprehensive foundation in filesystems and storage architecture, which is critical for any systems administrator. In an era where data is the most valuable asset, the ability to store, protect, and retrieve data efficiently and reliably is paramount. By combining theoretical concepts with extensive hands-on practice, students will gain the skills needed to make informed storage decisions and manage complex storage environments confidently.

*Remember: In systems administration, if the data isn't stored correctly, nothing else matters.*