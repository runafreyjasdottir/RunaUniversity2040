# IT203: Database Administration
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4  
**Description:** Database Administration & Data Management

---

## Lectures

ᚠ **Lecture 1: The Database Administrator's Worldview**

**Course:** IT203 — Database Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Database administration is the discipline of ensuring that an organization's most valuable asset—its data—is available, consistent, secure, and performant. This opening lecture establishes the DBA as a guardian of institutional memory, a performance engineer, and a security officer. By 2040, the DBA's role has evolved from manual tuning to AI-assisted optimization, but the core responsibility remains: the data must survive hardware failures, human errors, and malicious attacks.

### Key Topics

- The DBA's triple mandate: availability, integrity, and performance
- Data as organizational asset: valuation, classification, and lifecycle
- The 2040 data landscape: polyglot persistence, AI-generated data, and quantum-encrypted archives
- Ethics and compliance: GDPR evolution, data sovereignty, and research ethics
- DBAs and developers: collaboration, conflict, and the boundary between operations and engineering

### Lecture Notes

Organizations often claim that "data is our most valuable asset," yet they treat database administration as a cost center. This lecture challenges that framing. The lecture opens with a quantitative argument: in 2040, the average enterprise's data is valued at 35% of its market capitalization (McKinsey, 2038). A database outage that destroys customer trust can erase more value than a physical factory fire. The DBA is not merely a technician but a steward of this value.

**Availability** is measured in nines: 99.9% (8.77 hours downtime/year), 99.99% (52.6 minutes), 99.999% (5.26 minutes). Each additional nine increases cost exponentially. The lecture covers availability architectures: single-instance (acceptable for dev/test), primary-replica (read scaling, failover), and distributed consensus (Paxos, Raft) for true high availability. By 2040, **autonomous databases** (Oracle Autonomous, Azure SQL Managed Instance, CockroachDB) self-heal from common failures, but the DBA remains accountable for architecture decisions and edge-case recovery.

**Integrity** means that data is accurate, consistent, and protected against corruption. Constraints (primary keys, foreign keys, check constraints), transactions (ACID properties), and checksums (page verification) are the technical foundations. But integrity also requires procedural controls: change management for schema modifications, data validation pipelines, and reconciliation processes that compare systems of record against operational copies. The 2034 *Yggdrasil Grade Corruption Incident*—in which a bug in a batch update set 12,000 student grades to NULL—demonstrated that technical constraints alone cannot prevent integrity failures; peer review of DML (Data Manipulation Language) scripts is mandatory.

**Performance** is the art of making queries fast without compromising correctness. The lecture introduces the **performance triad**: hardware (CPU, memory, I/O subsystem), configuration (buffer pool size, connection pooling, parallelism), and design (schema normalization, indexing, query optimization). By 2040, **AI query optimizers** (e.g., Oracle's AutoML for SQL, PostgreSQL's pg_plan_advsr) suggest index creation and query rewrites, but the DBA must evaluate these suggestions against workload characteristics and maintenance overhead.

**Data classification** organizes data by sensitivity and regulatory requirements. **Public** data (course catalogs, published research) has minimal restrictions. **Internal** data (employee schedules, budget projections) requires authentication. **Confidential** data (student records, patient health information) requires encryption, access logging, and need-to-know authorization. **Restricted** data (research involving human subjects, national security classifications) requires air-gapped storage, multi-party control, and audit trails. By 2040, **automated data classification** (AI scanning content to infer sensitivity) supplements manual classification but requires human validation.

**Ethics and compliance** have grown more complex. The **GDPR** (General Data Protection Regulation, EU 2018) and its 2030 amendments mandate data minimization, purpose limitation, and the right to explanation for automated decisions. The **Global Data Protection Accord** (2034) harmonized standards across 80 nations. **Research ethics** (the UoY Institutional Review Board) govern data collected from human subjects, requiring informed consent, anonymization, and secure storage. The DBA must implement technical controls that satisfy these requirements: encryption at rest and in transit, access logging, data retention policies, and secure deletion (cryptographic erasure).

### Required Reading

- Lightstone, S., et al. (2010). *Database Administration: The Complete Guide to Practices and Procedures*. Addison-Wesley. (Updated concepts for 2040.)
- McKinsey & Company (2038). "The Value of Data: Enterprise Asset Valuation in the 2030s." *McKinsey Digital Report*.
- Yggdrasil IT Operations (2034). "The Grade Corruption Incident: NULL Values and Peer Review." *UoY Operations Postmortem* 2034-09.
- European Commission (2030). *GDPR Amendment 2030: AI and Automated Decision-Making*. EU Official Journal.
- Yggdrasil Ethics Board (2035). "Data Stewardship Guidelines for Database Administrators." *UoY Ethics Policy* v5.2.

### Discussion Questions

1. Autonomous databases promise to eliminate manual tuning. Does this make the DBA obsolete, or does it elevate the DBA's role from mechanic to architect?
2. The 2034 Grade Corruption Incident was caused by a DML script without peer review. Should all production DML require two-party approval, or does this create excessive overhead for routine updates?
3. AI-automated data classification can misclassify sensitive data as public. What validation processes ensure classification accuracy?
4. The right to explanation (GDPR 2030) requires that automated decisions be interpretable. How should DBAs design logging and audit trails to satisfy this requirement?

### Practice Problems

- Conduct a data classification exercise for a fictional university database. Identify tables, columns, and rows that fall into each classification tier. Propose technical controls for Confidential and Restricted data.
- Analyze an AI-generated query optimization suggestion. Evaluate its impact on: query latency, index maintenance overhead, storage cost, and concurrent workload performance.

---

ᚢ **Lecture 2: Relational Database Architecture: Pages, Transactions, and the Storage Engine**

**Course:** IT203 — Database Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

To administer a database effectively, one must understand its internal architecture. This lecture covers the storage engine—the component that translates SQL into physical disk operations. Students will learn about page structures, transaction logs, buffer pools, and the algorithms that ensure ACID compliance. The lecture uses PostgreSQL and InnoDB (MySQL/MariaDB) as primary examples, with references to SQL Server and Oracle where architectures differ.

### Key Topics

- Storage engines: PostgreSQL heap, InnoDB, SQL Server Storage Engine, Oracle ASM
- Page and block structures: headers, row data, free space, and pointers
- Transaction architecture: WAL/transaction log, checkpoints, and recovery
- Buffer management: LRU, clock sweep, and double buffering
- Multi-version concurrency control (MVCC): snapshots, visibility rules, and vacuuming

### Lecture Notes

A relational database is not a black box that "just works." It is a sophisticated system with carefully designed data structures and algorithms. The DBA who understands these internals can diagnose performance problems, design appropriate maintenance schedules, and recover from failures that would baffle a surface-level operator.

**PostgreSQL's heap storage** organizes tables as files of 8KB pages (blocks). Each page contains: a header (checksum, free space pointers), an array of line pointers (offsets to row data), row data (actual tuples), and free space. When a row is updated, PostgreSQL writes a new version rather than modifying the old one—the foundation of its **MVCC** implementation. Old row versions remain visible to concurrent transactions that started before the update, ensuring consistency without read locks. However, old versions must eventually be reclaimed by **VACUUM**, a background process that marks dead tuples as reusable space. Without vacuum, tables bloat; with overly aggressive vacuum, I/O overhead increases. The DBA must balance these factors.

**InnoDB** (MySQL/MariaDB's default storage engine) uses a different approach: **clustered indexes** where table data is stored in the leaf pages of the primary key index. Secondary indexes contain primary key values, not row pointers, requiring a lookup ("index dive") to fetch full rows. InnoDB's **buffer pool** caches data and index pages in memory, with an LRU (Least Recently Used) replacement policy modified to avoid sequential scan pollution. The **redo log** (ib_logfile) records changes for crash recovery; the **undo log** stores previous versions for rollback and MVCC. **Checkpoints** flush dirty pages from the buffer pool to disk, bounding recovery time. By 2040, **InnoDB's adaptive hash index** and **change buffer** automatically optimize for workload patterns, but the DBA must monitor their memory consumption.

**Transaction architecture** ensures durability through **Write-Ahead Logging (WAL)**. Before a transaction commits, its changes are written to the WAL (PostgreSQL) or redo log (InnoDB). On crash, the database replays the log to reconstruct committed transactions and undo uncommitted ones. **Checkpoints** establish a point before which all data is safely on disk, allowing old log segments to be recycled. The lecture covers checkpoint tuning: too frequent checkpoints waste I/O; too infrequent checkpoints extend recovery time. By 2040, **fuzzy checkpoints** (writing dirty pages gradually rather than all at once) and **checkpoint spikes** (periodic I/O bursts) remain active research areas.

**Buffer management** determines which pages remain in memory. The **LRU** algorithm evicts the least recently accessed page, but sequential scans can pollute the cache by loading many pages that are not reused. PostgreSQL's **clock sweep** (a variant of second-chance algorithm) gives pages a "usage count" before eviction. **Double buffering** (maintaining separate buffers for clean and dirty pages) improves write efficiency. The DBA tunes buffer pool size: too small causes excessive disk I/O; too large risks swapping or depriving the OS cache. By 2040, **AI buffer predictors** (prefetching pages based on query patterns) supplement traditional algorithms.

**Multi-version concurrency control (MVCC)** enables readers and writers to coexist without blocking. PostgreSQL implements MVCC by storing multiple row versions with transaction IDs (xmin, xmax) and using **visibility rules** to determine which version each transaction sees. InnoDB implements MVCC via **undo logs** and **system version numbers**. The lecture covers the trade-offs: MVCC eliminates read locks but requires garbage collection (VACUUM in PostgreSQL, purge in InnoDB) and can cause index bloat or fragmentation. By 2040, **zheap** (PostgreSQL's experimental undo-log-based storage) aims to reduce bloat by storing old versions in undo logs rather than the heap.

### Required Reading

- PostgreSQL Global Development Group (2040). *PostgreSQL Documentation: Chapter 68 (Database Page Layout), Chapter 29 (WAL)*. postgresql.org.
- MySQL Documentation (2040). *InnoDB Internals: Buffer Pool, Transaction Log, and MVCC*. mysql.com.
- Mohan, C., et al. (1992). "ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging." *ACM TODS*, 17(1), 94–162.
- Elmasri, R., & Navathe, S. B. (2015). *Fundamentals of Database Systems* (7th Edition). Pearson. Chapter 21 ("Database Recovery Techniques").
- Yggdrasil Database Lab (2037). "Zheap: Reducing PostgreSQL Bloat with Undo-Log Storage." *UoY Database Research Report* 2037-02.

### Discussion Questions

1. PostgreSQL's MVCC causes table bloat that requires VACUUM. Is this an acceptable trade-off for lock-free reads, or should PostgreSQL adopt InnoDB's undo-log approach?
2. InnoDB's clustered index architecture provides fast primary key lookups but slows secondary index access. For a workload with many secondary index queries, what schema or indexing strategies can mitigate this?
3. AI buffer predictors promise to improve cache hit ratios but add complexity. For a database with a stable, well-understood workload, is AI prediction worth the overhead?
4. Checkpoints balance recovery time against I/O overhead. For a system with a 1-hour RTO, what checkpoint frequency bounds recovery time while minimizing performance impact?

### Practice Problems

- Examine the page structure of a PostgreSQL table using the `pageinspect` extension. Interpret the header, line pointers, and tuple data for a sample table. Calculate the fill factor and identify fragmentation.
- Configure InnoDB buffer pool and redo log sizes for a given workload specification (database size, read/write ratio, concurrent connections). Justify each parameter choice and predict the impact of doubling the buffer pool.

---

ᚦ **Lecture 3: SQL for the DBA: DDL, DML, and Administrative Commands**

**Course:** IT203 — Database Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

SQL is the DBA's primary language—not just for querying data but for creating, modifying, securing, and optimizing the database itself. This lecture covers the SQL commands that DBAs use daily: Data Definition Language (DDL) for schema management, Data Manipulation Language (DML) for data operations, and administrative commands for monitoring and control.

### Key Topics

- DDL: CREATE, ALTER, DROP for tables, indexes, constraints, and schemas
- DML: INSERT, UPDATE, DELETE, MERGE, and bulk loading
- Administrative SQL: system catalogs, dynamic management views, and performance schemas
- Privilege management: GRANT, REVOKE, roles, and row-level security
- Scripting and automation: stored procedures, functions, and triggers for administration

### Lecture Notes

The DBA's SQL is different from the developer's SQL. Developers write queries for applications; DBAs write scripts for infrastructure. The DBA must master DDL to evolve schemas without breaking applications, DML to migrate and correct data safely, and administrative SQL to interrogate the database's internal state.

**DDL** defines and modifies database objects. `CREATE TABLE` specifies columns, data types, constraints, and storage parameters. `ALTER TABLE` adds, modifies, or drops columns and constraints. `CREATE INDEX` builds access paths for query optimization. `DROP` removes objects permanently (with no undo in most systems). The lecture covers DDL safety: **transactional DDL** (PostgreSQL, SQL Server—DDL can be rolled back if in a transaction), **online DDL** (MySQL, Oracle—schema changes do not lock tables for the duration), and **DDL triggers** (fire on schema changes for audit logging). By 2040, **schema migration tools** (Flyway, Liquibase, Sqitch, and pgroll for zero-downtime migrations) automate DDL deployment with version control and rollback.

**DML** manipulates data. `INSERT` adds rows; `UPDATE` modifies existing rows; `DELETE` removes rows; `MERGE` (or `UPSERT` in PostgreSQL via `INSERT ... ON CONFLICT`) performs insert-or-update atomically. The lecture emphasizes **safe DML**: always use `WHERE` clauses (preventing accidental full-table updates), test DML in a transaction with `SELECT` first (verifying affected rows), and use `LIMIT` or `TOP` for large updates (batching to avoid long transactions). Bulk loading (`COPY` in PostgreSQL, `LOAD DATA` in MySQL, `bcp` in SQL Server) is faster than row-by-row inserts for large datasets. By 2040, **parallel bulk loaders** distribute loading across CPU cores, and **foreign data wrappers** stream data directly from external sources.

**Administrative SQL** queries system catalogs to inspect database state. PostgreSQL's **system catalogs** (`pg_class`, `pg_attribute`, `pg_index`, `pg_stat_user_tables`) expose metadata and statistics. **Dynamic Management Views (DMVs)** in SQL Server (`sys.dm_exec_requests`, `sys.dm_os_wait_stats`) expose runtime state. **Performance Schema** in MySQL (`events_waits_summary_global_by_event_name`, `table_io_waits_summary_by_table`) exposes performance metrics. The lecture provides a reference of essential administrative queries: finding the largest tables, identifying missing indexes, monitoring replication lag, detecting lock contention, and analyzing wait events.

**Privilege management** controls who can access what. `GRANT` and `REVOKE` assign permissions (SELECT, INSERT, UPDATE, DELETE, CREATE, EXECUTE) to users or roles. **Roles** (introduced in PostgreSQL 8.1, standard by 2040) group permissions for easier management. **Row-level security (RLS)** filters rows based on user attributes (e.g., a tenant can see only their own rows). The lecture covers the **principle of least privilege** for DBAs: application accounts get only necessary permissions; DBA accounts are individualized (not shared `postgres` or `root`); and **break-glass** procedures document emergency privilege escalation. By 2040, **attribute-based access control (ABAC)** extends RLS with complex policies involving user roles, time of day, and client IP.

**Scripting and automation** reduce manual error and ensure consistency. **Stored procedures** encapsulate complex operations; **functions** return values for computation; **triggers** execute automatically on data changes. The lecture covers administrative use cases: audit triggers (logging all changes to sensitive tables), maintenance procedures (automated index rebuilds), and data validation functions (ensuring referential integrity across databases). By 2040, **pgTAP** (PostgreSQL testing framework) and similar tools enable unit testing of database code.

### Required Reading

- PostgreSQL Global Development Group (2040). *PostgreSQL Documentation: Chapter 5 (Data Definition), Chapter 6 (Data Manipulation)*. postgresql.org.
- MySQL Documentation (2040). *MySQL Reference Manual: SQL Statements*. mysql.com.
- Microsoft (2040). *Transact-SQL Reference: DDL, DML, and System Views*. Microsoft Learn.
- Yggdrasil Database Team (2035). "Safe DML: Procedures for Production Data Modification." *UoY Database Operations Manual* v4.1.

### Discussion Questions

1. Transactional DDL (PostgreSQL) vs. non-transactional DDL (MySQL historically). Should all DDL be transactional, or are there cases where immediate commit is preferable?
2. Row-level security adds query overhead. For a table with 10 million rows and complex RLS policies, what performance optimization strategies (indexing, predicate pushdown, materialized views) can maintain query speed?
3. Bulk loading bypasses transaction logging in some systems for speed. What are the recovery implications, and how should bulk-loaded data be protected?
4. Triggers are powerful but can create hidden dependencies and performance bottlenecks. What governance should limit trigger usage in production databases?

### Practice Problems

- Write a schema migration script that: adds a nullable column, backfills it from a related table, adds a NOT NULL constraint, and creates an index. Ensure the migration can run without locking the table for more than 5 seconds (use online DDL or batching).
- Query the PostgreSQL system catalogs to generate a report of: all tables over 1GB, all indexes not used in the last 30 days, all tables with more than 20% dead tuples, and all connections idle for more than 10 minutes. Automate this as a weekly report.

---

ᚨ **Lecture 4: Indexing and Query Optimization**

**Course:** IT203 — Database Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Indexes are the most powerful tool for query performance—and the most frequently misused. This lecture covers index structures, query plan analysis, and optimization strategies. Students will learn to design indexes that accelerate queries without excessive overhead, read execution plans, and apply optimizer hints judiciously.

### Key Topics

- Index structures: B-trees, hash indexes, GiST, GIN, BRIN, and inverted indexes
- Query execution plans: sequential scans, index scans, joins, and sorting
- The query optimizer: cost model, statistics, and plan selection
- Index design: covering indexes, partial indexes, composite indexes, and functional indexes
- Query tuning: rewrite strategies, parameter sniffing, and hinting

### Lecture Notes

An index is a data structure that enables the database to find rows without scanning every page. The most common structure is the **B-tree** (balanced tree), which maintains sorted order and supports equality and range lookups with O(log n) complexity. But B-trees are not universal; different workloads require different structures.

**Index structures**: **B-tree** (default for most indexes, supports equality and range queries). **Hash indexes** (constant-time equality lookups, no range support; improved in PostgreSQL 10+). **GiST (Generalized Search Tree)** (supports user-defined types and operators: nearest-neighbor, overlap, containment). **GIN (Generalized Inverted Index)** (efficient for multi-value elements: arrays, full-text search, JSONB). **BRIN (Block Range INdex)** (tiny indexes for naturally ordered data like timestamps, storing min/max per block). **Inverted indexes** (full-text search: mapping words to documents). By 2040, **learned indexes** (machine-learned models that predict record locations, replacing B-trees for some workloads) are an active research area, though not yet mainstream in production DBMS.

**Query execution plans** reveal how the database will execute a query. The lecture teaches plan reading: **sequential scan** (reading all pages), **index scan** (using an index to find rows, then fetching heap pages), **index-only scan** (using a covering index without heap access), **bitmap index scan** (combining multiple index results to reduce random I/O), **nested loop join** (for each outer row, scan inner table), **hash join** (build hash table on inner, probe with outer), **merge join** (sort both inputs, merge), and **sort/aggregate** operations. Plans are read from root to leaves, with cost estimates (arbitrary units representing I/O + CPU) and actual timings (from `EXPLAIN ANALYZE`).

**The query optimizer** generates plans based on **statistics**: table row counts, column distinct values, most common values, histograms, and correlation. Stale statistics cause poor plans; the DBA schedules `ANALYZE` (PostgreSQL) or updates statistics (SQL Server) to keep them current. The **cost model** assigns weights to sequential page reads, random page reads, CPU operations, and parallel worker startup. By 2040, **adaptive query optimization** (feedback loops that adjust plans based on runtime cardinality) improves estimates for complex queries.

**Index design** balances query acceleration against maintenance cost. **Covering indexes** include all columns needed by a query, enabling index-only scans. **Partial indexes** index only rows matching a predicate (`WHERE status = 'active'`), reducing size and maintenance for skewed data. **Composite indexes** (multiple columns) support multi-column predicates but require careful column ordering (leading columns must match query predicates). **Functional indexes** index expressions (`LOWER(email)`) for case-insensitive lookups. The lecture provides a decision tree: when to create an index, when to use a composite vs. partial index, and when an index is not worth the cost (small tables, write-heavy tables, low-selectivity columns).

**Query tuning** goes beyond indexing. **Rewrite strategies**: replacing `OR` with `UNION`, using `EXISTS` instead of `IN` for subqueries, avoiding `SELECT *`, and pushing predicates into CTEs. **Parameter sniffing** (SQL Server) occurs when a stored plan optimized for one parameter value performs poorly for others; solutions include `OPTION (RECOMPILE)`, optimizer hints, or plan guides. **Hinting** (`/*+ INDEX(...) */`) forces the optimizer to use a specific index or join order, but the lecture warns that hints override the optimizer's adaptability and should be used sparingly. By 2040, **query store** features (SQL Server Query Store, PostgreSQL pg_stat_statements) capture historical plans and performance, enabling regression analysis.

### Required Reading

- PostgreSQL Global Development Group (2040). *PostgreSQL Documentation: Chapter 11 (Indexes), Chapter 14 (Performance Tips)*. postgresql.org.
- MySQL Documentation (2040). *MySQL Optimization: Indexes and Query Execution Plans*. mysql.com.
- Microsoft (2040). *SQL Server Query Processing Architecture Guide*. Microsoft Learn.
- Krishnamurthy, R., et al. (2020). "The Case for Learned Index Structures." *SIGMOD*, 489–504.
- Yggdrasil Database Team (2036). "Index Design Patterns for the 2040s: A UoY Case Study." *UoY Database Operations Report*.

### Discussion Questions

1. Learned indexes promise better performance than B-trees but require training and are sensitive to data distribution. For a general-purpose database, are learned indexes ready to replace B-trees?
2. Covering indexes improve read performance but increase write overhead and storage. What is the appropriate maximum number of covering indexes per table?
3. Parameter sniffing causes performance regression when data distributions change. Is `OPTION (RECOMPILE)` (recompiling on every execution) a viable solution, or does the compilation overhead negate the benefit?
4. Partial indexes are powerful but require manual analysis of query patterns. Can automated index advisors reliably suggest partial indexes, or do they lack the semantic understanding?

### Practice Problems

- Given a set of slow queries from a production application, analyze each with `EXPLAIN (ANALYZE, BUFFERS)`. Identify missing indexes, inefficient joins, and unnecessary sorts. Propose and test optimizations, measuring improvement.
- Create a workload with mixed read/write patterns. Add indexes to improve read performance and measure the impact on write throughput and storage. Determine the optimal index set that maximizes overall throughput.

---

ᚱ **Lecture 5: Replication, High Availability, and Disaster Recovery**

**Course:** IT203 — Database Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

A single database server is a single point of failure. This lecture covers the technologies that distribute data across multiple servers: replication for scale and redundancy, failover for availability, and backup strategies for recovery. Students will learn to architect database clusters that survive hardware failures, network partitions, and datacenter outages.

### Key Topics

- Replication models: logical vs. physical, synchronous vs. asynchronous
- PostgreSQL replication: streaming replication, logical replication, and patroni
- MySQL replication: binary log replication, Group Replication, and Galera
- Failover: automatic promotion, split-brain prevention, and connection routing
- Backup strategies: physical, logical, point-in-time recovery, and object storage

### Lecture Notes

**Replication** creates copies of data on multiple servers. **Physical replication** copies byte-for-byte changes (WAL segments in PostgreSQL, InnoDB redo log in MySQL); it is fast and preserves exact state but is limited to identical versions and platforms. **Logical replication** copies row changes decoded from WAL; it supports cross-version and cross-platform replication, selective table replication, and conflict resolution. By 2040, **logical replication** is the default for new deployments due to its flexibility.

**Synchronous replication** waits for the standby to confirm writes before acknowledging the client, ensuring zero data loss but adding latency. **Asynchronous replication** acknowledges immediately and replicates in the background, minimizing latency but risking data loss on failover. **Quorum-based replication** (e.g., PostgreSQL synchronous_commit = remote_apply with multiple standbys) requires confirmation from a majority, balancing consistency and availability. The lecture covers the **CAP theorem** implications: synchronous replication favors consistency (CP); asynchronous favors availability (AP).

**PostgreSQL replication** evolved significantly by 2040. **Streaming replication** (since 9.0) sends WAL records to standbys in real time. **Cascading replication** allows standbys to replicate from other standbys, reducing primary load. **Synchronous replication** (since 9.1) with `synchronous_commit` levels (`off`, `local`, `remote_write`, `remote_flush`, `remote_apply`) provides tunable durability. **Logical replication** (since 10) enables selective table replication and cross-version replication. **Patroni** (a template for HA PostgreSQL using etcd, ZooKeeper, or Consul) provides automatic failover, leader election, and health checks. By 2040, **pg_auto_failover** and **repmgr** provide simpler HA alternatives.

**MySQL replication** uses the **binary log** (binlog) to record changes. Traditional replication is asynchronous, with a primary writing binlog and replicas reading it. **GTID (Global Transaction Identifier)** ensures transaction consistency across failover. **Group Replication** (MySQL 5.7+) provides multi-primary, synchronous replication using Paxos. **Galera Cluster** (MariaDB) provides synchronous multi-master replication with certification-based conflict detection. By 2040, **MySQL InnoDB Cluster** (Group Replication + MySQL Router + MySQL Shell) is Oracle's recommended HA solution.

**Failover** promotes a replica to primary when the primary fails. **Automatic failover** (Patroni, Orchestrator, repmgr) detects failure via health checks and promotes the most advanced replica. **Split-brain prevention** ensures only one primary exists at a time: Patroni uses distributed consensus (etcd) to elect a single leader; manual failover risks two primaries if the old primary is not properly demoted. **Connection routing** (PgBouncer, HAProxy, MySQL Router) directs applications to the current primary without reconfiguration. By 2040, **service discovery** (Consul, etcd) automates connection routing.

**Backup strategies** for databases include: **physical backups** (copying data files: `pg_basebackup`, Percona XtraBackup, SQL Server BACKUP DATABASE) for fast restore; **logical backups** (SQL dumps: `pg_dump`, `mysqldump`) for portability and selective restore; and **incremental backups** (WAL archiving, binlog archiving) for point-in-time recovery. The lecture covers **PITR (Point-In-Time Recovery)**: restoring a base backup and replaying WAL/binlog up to a specific timestamp. By 2040, **object storage backups** (S3, Azure Blob, GCS) are standard, with automated lifecycle policies transitioning old backups to cheaper tiers.

### Required Reading

- PostgreSQL Global Development Group (2040). *High Availability, Load Balancing, and Replication*. postgresql.org.
- MySQL Documentation (2040). *MySQL Replication and Group Replication*. mysql.com.
- Zaloni (Patroni Authors) (2040). *Patroni Documentation: HA PostgreSQL*. patroni.readthedocs.io.
- Versteeg, S. (2020). *Orchestrator: MySQL High Availability and Topology Management*. GitHub.
- Yggdrasil Database Team (2035). "Split-Brain in the Student Records Cluster: A Failover Postmortem." *UoY Operations Postmortem* 2035-11.

### Discussion Questions

1. Synchronous replication ensures consistency but increases write latency. For a global application with users on three continents, what replication topology minimizes latency while maintaining acceptable durability?
2. Automatic failover reduces downtime but can promote a replica with slightly stale data. What are the business implications of seconds or minutes of data loss, and how should RPO be negotiated?
3. MySQL Group Replication and Galera provide multi-master writes but have conflict resolution limitations. For a write-heavy workload, is multi-master appropriate, or should read replicas with single-master writes be preferred?
4. Object storage backups are cheap and durable but have egress fees and retrieval latency. For a 10TB database, what backup architecture (local + cloud, cloud-only, tape + cloud) balances cost, RTO, and ransomware resilience?

### Practice Problems

- Set up PostgreSQL streaming replication with one standby. Test failover manually (promote standby) and with Patroni (simulate primary failure). Measure failover time and verify data consistency.
- Design a backup and recovery strategy for a 2TB PostgreSQL database with a 4-hour RTO and 15-minute RPO. Specify: backup types, schedule, retention, storage targets, and recovery procedures. Include a cost estimate.

---

ᚲ **Lecture 6: Performance Tuning and Capacity Planning**

**Course:** IT203 — Database Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Performance tuning is the DBA's art and science. This lecture covers the methodologies and tools for diagnosing performance problems, optimizing resource utilization, and planning for growth. Students will learn to measure, model, and predict database performance, ensuring that systems scale smoothly from startup to enterprise.

### Key Topics

- Performance metrics: throughput, latency, concurrency, and resource utilization
- Wait event analysis: identifying bottlenecks by what the database is waiting for
- Configuration tuning: memory, I/O, parallelism, and connection pooling
- Workload analysis: query patterns, access paths, and contention points
- Capacity planning: trend analysis, modeling, and predictive scaling

### Lecture Notes

Performance tuning begins with measurement. Without accurate metrics, tuning is guesswork. The lecture introduces the **USE method** (Utilization, Saturation, Errors) for resource analysis and the **RED method** (Rate, Errors, Duration) for service analysis, adapted from Brendan Gregg's systems performance methodology.

**Performance metrics** for databases include: **throughput** (transactions per second, queries per second), **latency** (response time percentiles: p50, p95, p99), **concurrency** (active connections, waiting transactions), and **resource utilization** (CPU %, memory %, disk IOPS, disk throughput, network bandwidth). The lecture emphasizes **percentiles over averages**: a query with 10ms average may have 1% of executions taking 5 seconds, which impacts user experience disproportionately. By 2040, **distributed tracing** (OpenTelemetry) links database queries to application requests, enabling end-to-end latency analysis.

**Wait event analysis** identifies bottlenecks by what the database is waiting for rather than what it is doing. PostgreSQL's `pg_stat_activity` and `pg_wait_sampling` expose wait events: `IO:DataFileRead` (reading data from disk), `Lock:tuple` (waiting for a row lock), `Client:ClientRead` (waiting for the client to send data). SQL Server's `sys.dm_os_wait_stats` provides similar visibility. The lecture covers: filtering noise (excluding idle waits), identifying top waits, and correlating waits with resource metrics. For example, high `IO:DataFileRead` with low disk IOPS suggests that queries are reading too much data (missing indexes, excessive sorting); high `Lock:tuple` with moderate throughput suggests contention (hot rows, long transactions).

**Configuration tuning** adjusts database parameters to match hardware and workload. **Memory**: buffer pool size (typically 70-80% of RAM for dedicated database servers), work memory (per-query sort/hash memory), and maintenance work memory (VACUUM, index creation). **I/O**: random vs. sequential page cost (influencing optimizer plan selection), effective I/O concurrency (number of concurrent disk operations), and WAL sync method. **Parallelism**: max parallel workers, cost thresholds for parallel plans. **Connection pooling**: max connections (excessive connections waste memory and cause contention; connection pooling via PgBouncer or pgpool reduces overhead). By 2040, **autotuning advisors** (e.g., Azure SQL Database Intelligent Insights, PostgreSQL's auto_explain with plan analysis) suggest parameter changes, but the DBA validates them.

**Workload analysis** characterizes the application's interaction with the database. Read-heavy vs. write-heavy? OLTP (many small transactions) vs. OLAP (few large analytical queries)? Random access vs. sequential scans? The lecture covers **workload classification** and its implications: an OLTP workload needs fast indexes, low-latency commits, and connection pooling; an OLAP workload needs parallel scans, columnar storage, and batch loading. By 2040, **HTAP (Hybrid Transactional/Analytical Processing)** databases (TiDB, CockroachDB, SingleStore) serve both workloads, but the DBA must still understand the mix to configure resources.

**Capacity planning** ensures the database can handle future growth. **Trend analysis**: extrapolating from historical metrics (data growth rate, query volume growth, peak load patterns). **Modeling**: queueing theory models (M/M/c queues) predicting response time under increased load. **Predictive scaling**: cloud auto-scaling policies (adding read replicas when CPU > 70% for 5 minutes) and pre-provisioning for known events (student enrollment periods, registration days). By 2040, **AI capacity forecasting** (predicting peak load 72 hours ahead based on academic calendar, weather, and social media trends) enables proactive scaling at UoY.

### Required Reading

- Gregg, B. (2013). *Systems Performance: Enterprise and the Cloud*. Prentice Hall. Chapters 1–2.
- PostgreSQL Global Development Group (2040). *PostgreSQL Documentation: Chapter 19 (Server Configuration)*. postgresql.org.
- MySQL Documentation (2040). *MySQL Server Administration: Tuning and Performance*. mysql.com.
- Menasce, D. A., & Almeida, V. A. F. (2001). *Capacity Planning for Web Services: Metrics, Models, and Methods*. Prentice Hall.
- Yggdrasil Database Team (2039). "AI Capacity Forecasting for Academic Workloads." *UoY Database Operations Report*.

### Discussion Questions

1. AI autotuning advisors suggest configuration changes but may not understand workload seasonality. Should DBAs accept AI recommendations automatically, or is human validation always necessary?
2. HTAP databases promise to eliminate the OLTP/OLAP split, but single systems serving both workloads risk resource contention. Is HTAP a genuine simplification, or does it create new tuning complexity?
3. Connection pooling reduces overhead but adds a hop (application → pooler → database). For a latency-sensitive application, is pooling justified?
4. Queueing theory models assume steady-state workloads, but real workloads are bursty. How should capacity planning account for burstiness and tail latency?

### Practice Problems

- Profile a running PostgreSQL database using `pg_stat_statements`, `pg_stat_activity`, and `pg_wait_sampling`. Identify the top 5 queries by total time, the top 3 wait events, and the queries with the worst latency outliers. Propose and implement optimizations.
- Build a capacity plan for a database expected to grow from 500GB to 2TB over 2 years, with query volume doubling. Predict IOPS, storage, and memory requirements. Model the impact of adding 2 read replicas vs. upgrading the primary server.

---

ᚷ **Lecture 7: Security: Encryption, Auditing, and Access Control**

**Course:** IT203 — Database Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Databases store the most sensitive information an organization possesses. This lecture covers the security controls that protect data at rest, in transit, and in use: encryption, access control, auditing, and vulnerability management. Students will learn to implement defense in depth for database systems, satisfying regulatory requirements and resisting sophisticated attacks.

### Key Topics

- Encryption at rest: TDE, filesystem encryption, and column-level encryption
- Encryption in transit: TLS for database connections, certificate management
- Access control: RBAC, ABAC, row-level security, and database firewalls
- Auditing: query logging, object access logging, and SIEM integration
- Vulnerability management: patching, configuration hardening, and penetration testing

### Lecture Notes

Database security operates at multiple layers: the network (firewalls, TLS), the operating system (permissions, SELinux), the database server (authentication, authorization), and the application (parameterized queries, input validation). No single layer is sufficient; defense in depth requires all layers to function.

**Encryption at rest** protects data stored on disk. **TDE (Transparent Data Encryption)** encrypts database files automatically, with decryption occurring in memory when data is accessed. SQL Server TDE, Oracle TDE, and MySQL InnoDB tablespace encryption provide this capability. **Filesystem encryption** (LUKS, BitLocker) encrypts the entire volume, protecting all files including backups and logs. **Column-level encryption** encrypts specific sensitive columns (credit card numbers, health records) with application-managed keys, providing finer control but requiring application changes. By 2040, **post-quantum encryption** (CRYSTALS-Kyber for key encapsulation, AES-256 for bulk encryption) is standard for long-term archival.

**Encryption in transit** protects data moving between application and database. **TLS** (covered in IT107) is mandatory for all database connections by 2040. The lecture covers: certificate configuration (server certificates, client certificates for mTLS), cipher suite selection (forward secrecy, strong ciphers), and certificate rotation (automated via ACME or internal PKI). **Connection encryption** should be enforced (rejecting unencrypted connections) to prevent downgrade attacks. The 2032 *Unencrypted Replication Channel*—in which an attacker intercepted and modified WAL records between primary and standby—demonstrated that replication traffic must also be encrypted.

**Access control** restricts who can do what. **RBAC (Role-Based Access Control)** assigns permissions to roles, which are granted to users. **ABAC (Attribute-Based Access Control)** evaluates policies based on user attributes, resource attributes, and environmental conditions (time, location, device posture). **Row-level security (RLS)** filters rows based on user identity. **Database firewalls** (e.g., GreenSQL, Imperva) inspect SQL traffic in real time, blocking injection attempts and unauthorized access patterns. By 2040, **zero-trust database access** (each query authenticated and authorized, with session tokens rather than persistent connections) is emerging.

**Auditing** provides accountability. **Query logging** (PostgreSQL `log_statement = 'all'`, MySQL general query log, SQL Server Extended Events) records all SQL statements. **Object access logging** records who accessed which tables, columns, and rows. **Audit policies** define what to log, where to store logs, and how long to retain them. By 2040, **SIEM integration** (Splunk, QRadar, Sentinel) correlates database audit logs with network, application, and identity logs to detect anomalies. The UoY **Bifröst Audit Pipeline** (2036) streams database audit events to a tamper-proof blockchain ledger, providing non-repudiable evidence.

**Vulnerability management** keeps database software secure. **Patching**: applying security updates within defined SLAs (critical patches within 24 hours, high within 7 days). **Configuration hardening**: disabling unused features, removing default accounts, enforcing strong authentication. **Penetration testing**: authorized simulated attacks that identify weaknesses. The lecture covers **database-specific vulnerabilities**: SQL injection (mitigated by parameterized queries and stored procedures), privilege escalation (mitigated by least privilege and patch management), and side-channel attacks (mitigated by constant-time operations and memory isolation). By 2040, **automated vulnerability scanning** (Qualys, Nessus, OpenVAS) includes database-specific checks.

### Required Reading

- NIST (2035). *Database Security Guidelines*. NIST SP 800-171 Rev. 3.
- PostgreSQL Global Development Group (2040). *PostgreSQL Encryption and Authentication*. postgresql.org.
- Microsoft (2040). *SQL Server Security Best Practices*. Microsoft Learn.
- Oracle (2040). *Oracle Database Security Guide*. Oracle Documentation.
- Yggdrasil Security Team (2032). "The Unencrypted Replication Channel: Man-in-the-Middle Against Database Clusters." *UoY Security Bulletin* 2032-05.

### Discussion Questions

1. TDE encrypts data at rest but decrypts it in memory for access. Does TDE provide meaningful protection against an attacker with OS-level access, or is it primarily a compliance checkbox?
2. Column-level encryption provides strong security but complicates query processing (encrypted columns cannot be indexed or filtered efficiently). What data is worth this overhead?
3. Zero-trust database access requires authentication per query, adding latency. For a high-throughput OLTP system, is the security gain worth the performance cost?
4. The Bifröst Audit Pipeline stores audit logs on a blockchain. Does blockchain immutability justify the storage and performance overhead compared to append-only traditional logs?

### Practice Problems

- Configure TDE for a PostgreSQL database using pgcrypto for column-level encryption and LUKS for filesystem encryption. Verify that data is encrypted on disk but queryable in memory. Measure the performance impact.
- Implement row-level security on a multi-tenant database. Ensure that each tenant sees only their own rows, even when querying through shared application accounts. Test with SQL injection attempts to verify isolation.

---

ᚹ **Lecture 8: Schema Design, Normalization, and Data Modeling**

**Course:** IT203 — Database Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

While schema design is often considered a developer responsibility, the DBA must ensure that designs are performant, maintainable, and scalable. This lecture covers relational modeling, normalization, denormalization, and the practical compromises that production systems require. Students will learn to evaluate schemas, suggest improvements, and balance theoretical purity with operational reality.

### Key Topics

- Entity-Relationship modeling: entities, attributes, relationships, and cardinality
- Normal forms: 1NF, 2NF, 3NF, BCNF, and their practical implications
- Denormalization: when and why to violate normal forms
- Temporal data: slowly changing dimensions, valid time, and transaction time
- Schema evolution: backward-compatible changes, expand-contract, and versioning

### Lecture Notes

**Entity-Relationship (ER) modeling** is the conceptual foundation of relational design. Entities represent real-world objects (Student, Course, Instructor); attributes describe their properties (name, enrollment_date); relationships connect entities (Student enrolls in Course). Cardinality defines how many instances participate: one-to-one, one-to-many, many-to-many. The lecture demonstrates creating an ER diagram for a university registrar system and translating it to relational tables.

**Normalization** eliminates redundancy and prevents anomalies. **1NF (First Normal Form)** requires atomic values (no repeating groups or arrays in columns). **2NF** requires 1NF plus no partial dependencies (non-key attributes must depend on the whole primary key). **3NF** requires 2NF plus no transitive dependencies (non-key attributes must depend only on the primary key). **BCNF (Boyce-Codd Normal Form)** requires that every determinant be a candidate key. The lecture works through examples: a table with student_id, course_id, student_name, course_name, and grade violates 2NF (student_name depends only on student_id) and 3NF (course_name depends only on course_id). Decomposition into Student, Course, and Enrollment tables achieves BCNF.

**Denormalization** intentionally introduces redundancy for performance. Read-heavy analytical workloads often benefit from denormalized tables that avoid joins. Common patterns: **materialized views** (precomputed join results), **summary tables** (pre-aggregated metrics), **embedded documents** (storing related data in JSONB columns), and **star schemas** (fact tables surrounded by dimension tables in data warehouses). The lecture emphasizes that denormalization is a **performance optimization**, not a design default: it should be applied after profiling demonstrates that normalization causes unacceptable latency, and it must be maintained (updated when source data changes).

**Temporal data** tracks how information changes over time. **Slowly Changing Dimensions (SCD)** manage historical versions of dimensional data: Type 1 (overwrite, losing history), Type 2 (add new row with effective dates), Type 3 (add columns for previous values). **Valid time** tracks when a fact was true in the real world; **transaction time** tracks when it was recorded in the database. By 2040, **temporal tables** (SQL:2011 standard, supported by SQL Server, Oracle, and PostgreSQL via extensions) provide built-in valid-time and transaction-time support, automatically maintaining history without application changes.

**Schema evolution** changes the database structure without breaking applications. The **expand-contract pattern** (Lecture 3) adds new structures before removing old ones, maintaining backward compatibility. The lecture covers safe changes: adding nullable columns, adding tables, creating indexes (online). Unsafe changes: dropping columns, changing data types, renaming objects. By 2040, **schema registries** (Confluent Schema Registry for Kafka, database-specific registries for PostgreSQL) track schema versions and enforce compatibility rules.

### Required Reading

- Elmasri, R., & Navathe, S. B. (2015). *Fundamentals of Database Systems* (7th Edition). Pearson. Chapters 3–4, 14–15.
- Kimball, R., & Ross, M. (2013). *The Data Warehouse Toolkit* (3rd Edition). Wiley. Chapters 1–2.
- Date, C. J. (2012). *Database Design and Relational Theory*. O'Reilly. Chapters 1–3.
- Snodgrass, R. T. (2000). *Developing Time-Oriented Database Applications in SQL*. Morgan Kaufmann.
- Yggdrasil Database Team (2034). "Schema Evolution at Scale: The UoY Expand-Contract Playbook." *UoY Database Operations Manual*.

### Discussion Questions

1. Normalization to BCNF can produce many small tables, increasing join complexity. For an OLTP system with simple queries, is 3NF sufficient, or should designers aim for BCNF regardless?
2. Materialized views improve query performance but require maintenance (refresh strategies). What refresh strategy (on-demand, scheduled, incremental, real-time) is appropriate for a rapidly changing dataset?
3. Temporal tables simplify history tracking but double storage requirements. For a table with 100 million rows and 10% monthly change rate, is the storage overhead justified?
4. Schema registries enforce compatibility but can block necessary breaking changes. How should teams manage major schema revisions that cannot be backward-compatible?

### Practice Problems

- Design a normalized schema for a university course registration system. Include entities for students, courses, instructors, enrollments, and prerequisites. Normalize to 3NF and verify that no insertion, update, or deletion anomalies remain.
- Take a denormalized reporting table and redesign it using materialized views. Measure query performance before and after, and implement an incremental refresh strategy that maintains consistency.

---

ᚺ **Lecture 9: NoSQL, NewSQL, and Polyglot Persistence**

**Course:** IT203 — Database Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Relational databases are not the only option. This lecture covers the alternative data management systems that have emerged to handle workloads poorly served by SQL: document stores, key-value stores, wide-column stores, graph databases, and time-series databases. Students will learn when to use each type, how to administer them, and how to integrate them in polyglot architectures.

### Key Topics

- Document stores: MongoDB, Couchbase, and PostgreSQL JSONB
- Key-value stores: Redis, etcd, and DynamoDB
- Wide-column stores: Cassandra, ScyllaDB, and HBase
- Graph databases: Neo4j, Amazon Neptune, and RDF stores
- Time-series databases: InfluxDB, TimescaleDB, and Prometheus

### Lecture Notes

The **NoSQL** movement (late 2000s) rejected the rigid schemas and ACID constraints of relational databases in favor of scalability and flexibility. By 2040, the distinction between SQL and NoSQL has blurred: PostgreSQL supports JSONB documents; MongoDB supports multi-document ACID transactions; CockroachDB provides scalable SQL. The lecture treats NoSQL not as a rejection of relational theory but as an expansion of the database administrator's toolkit.

**Document stores** store data as JSON-like documents with flexible schemas. **MongoDB** (the most popular document database) provides rich querying, indexing, and aggregation. **Couchbase** combines document storage with key-value caching and SQL-like querying (N1QL). **PostgreSQL JSONB** provides document storage within a relational database, with indexing (GIN), querying (JSON path), and ACID transactions. By 2040, document stores are the default for content management, catalogs, and user profiles—data with evolving schemas and nested structures.

**Key-value stores** provide the simplest data model: a key maps to a value. **Redis** (in-memory with optional persistence) serves as a cache, message broker, and session store. **etcd** (distributed, consistent) stores configuration and coordination data for Kubernetes and other distributed systems. **DynamoDB** (AWS managed) provides single-digit millisecond latency at any scale. The lecture covers Redis administration: persistence (RDB snapshots, AOF logs), replication, clustering (Redis Cluster for sharding), and memory management (eviction policies: LRU, LFU, TTL). By 2040, **Redis-compatible stores** (KeyDB, Dragonfly) provide multi-threading and improved performance.

**Wide-column stores** organize data in columns rather than rows, optimizing for analytical queries over large datasets. **Apache Cassandra** (distributed, masterless, peer-to-peer) provides linear scalability and tunable consistency. **ScyllaDB** (Cassandra-compatible, C++ implementation) offers 10× throughput. The lecture covers Cassandra administration: ring topology, replication factor, consistency levels (ONE, QUORUM, ALL), compaction strategies (SizeTieredCompaction, LeveledCompaction), and repair operations. By 2040, Cassandra remains dominant for IoT, messaging, and time-series workloads that exceed single-node capacity.

**Graph databases** model relationships as first-class citizens. **Neo4j** (property graph model) uses nodes, relationships, and properties, queried with Cypher. **Amazon Neptune** provides property graph and RDF graph support. The lecture covers graph administration: index-free adjacency (traversing relationships without index lookups), query optimization (pattern matching, shortest path), and sharding (graphs are hard to partition). By 2040, **knowledge graphs** (enterprise-scale RDF/OWL databases) integrate with AI systems for reasoning and recommendation.

**Time-series databases** optimize for timestamped data: metrics, events, sensor readings. **InfluxDB** (popular open-source TSDB) provides high ingestion rates, retention policies, and continuous queries. **TimescaleDB** (PostgreSQL extension) brings time-series capabilities to SQL, enabling JOINs with relational data. **Prometheus** (monitoring-focused) stores metrics in its own TSDB. The lecture covers TSDB administration: retention policies (automatically expiring old data), downsampling (aggregating high-resolution to low-resolution), and high-cardinality handling (managing millions of unique time series). By 2040, **AI-native TSDBs** (e.g., UoY's **Völuspá**) use learned compression and anomaly detection for scientific instruments.

### Required Reading

- Sadalage, P. J., & Fowler, M. (2012). *NoSQL Distilled: A Brief Guide to the Emerging World of Polyglot Persistence*. Addison-Wesley.
- MongoDB Documentation (2040). *MongoDB Administration*. mongodb.com.
- Redis Documentation (2040). *Redis: Persistence, Replication, Clustering*. redis.io.
- Neo4j Documentation (2040). *Neo4j Operations Manual*. neo4j.com.
- Yggdrasil Database Team (2038). "Völuspá: AI-Native Time-Series Storage for Scientific Instruments." *UoY Database Research Report*.

### Discussion Questions

1. PostgreSQL JSONB provides document storage with ACID transactions. For a new project, should the team choose PostgreSQL JSONB or MongoDB, and what factors determine the choice?
2. Redis is single-threaded (per node), which limits throughput on a single instance. Does Redis Cluster's sharding adequately address this, or should Redis-compatible multi-threaded alternatives be considered?
3. Graph databases excel at relationship queries but struggle with horizontal scaling. For a social network with 1 billion users, is a graph database feasible, or should relationships be modeled in a relational or wide-column store?
4. Time-series databases optimize for ingestion and retention but sacrifice general query flexibility. For a workload that is 80% time-series and 20% relational, should the team use a TSDB with relational extensions or maintain separate systems?

### Practice Problems

- Migrate a relational schema to MongoDB for a product catalog with variable attributes (different products have different specifications). Design documents, indexes, and aggregation pipelines. Compare query performance and schema flexibility.
- Configure a Redis cluster with 3 masters and 3 replicas. Test failover by stopping a master, verify automatic promotion of replica, and measure downtime. Benchmark throughput and latency under load.

---

ᚾ **Lecture 10: Data Migration, ETL, and Integration**

**Course:** IT203 — Database Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Data rarely stays in one place. Organizations migrate data between systems, integrate disparate sources, and transform formats for analytics. This lecture covers the tools and techniques for moving data safely and efficiently: ETL (Extract, Transform, Load), change data capture, replication-based integration, and API-based synchronization.

### Key Topics

- ETL architecture: extraction strategies, transformation types, and loading patterns
- Change Data Capture (CDC): log-based, trigger-based, and polling
- Data quality: profiling, cleansing, validation, and reconciliation
- Integration patterns: ETL vs. ELT, streaming vs. batch, and data virtualization
- Migration tools: pg_dump, mysqldump, AWS DMS, Talend, and Apache NiFi

### Lecture Notes

**ETL** is the classical pattern for data integration: extract data from source systems, transform it (clean, validate, enrich, restructure), and load it into a target system (typically a data warehouse). **ELT** (Extract, Load, Transform) loads raw data into the target first, then transforms it using the target's compute power (common in cloud data warehouses like Snowflake, BigQuery, and Redshift). By 2040, **streaming ETL** (Kafka Connect, Apache Flink, Spark Streaming) processes data in real time rather than batches, enabling near-real-time analytics.

**Extraction strategies** depend on source system capabilities. **Full extract**: copying all data (simple but slow, suitable for small sources). **Incremental extract**: copying only changed data (requires a change tracking mechanism: timestamp columns, CDC, or triggers). **Delta extract**: copying changed and deleted rows (requires soft deletes or tombstones). The lecture covers source system impact: extraction queries should not lock tables or consume excessive I/O; **read replicas** are often used as extraction sources to isolate the primary.

**Change Data Capture (CDC)** captures changes as they occur. **Log-based CDC** reads the database transaction log (WAL in PostgreSQL, binlog in MySQL) and replays changes to the target. It is low-impact (no queries on source) and captures all changes (including deletes), but requires access to logs and parsing logic. **Trigger-based CDC** uses database triggers to write changes to a staging table. It is database-agnostic but adds overhead to every write. **Polling CDC** queries the source periodically for changes. It is simple but misses intermediate changes and can cause delays. By 2040, **debezium** (open-source log-based CDC) is the standard for streaming data pipelines.

**Data quality** ensures that integrated data is fit for purpose. **Profiling** analyzes data distributions, patterns, and anomalies (null rates, cardinality, value ranges). **Cleansing** corrects errors (standardizing formats, removing duplicates, imputing missing values). **Validation** checks data against rules (referential integrity, business constraints, format compliance). **Reconciliation** compares source and target totals to verify completeness. By 2040, **AI data quality tools** (Great Expectations, Soda, dbt tests) automatically generate and monitor data quality rules.

**Integration patterns** vary by latency and complexity requirements. **Batch ETL** runs on schedules (hourly, nightly), suitable for reporting and analytics. **Streaming ETL** processes events as they occur, suitable for operational dashboards and real-time decisions. **Data virtualization** (Denodo, Starburst Galaxy) provides a unified query interface over disparate sources without moving data, suitable for exploratory analysis and temporary integration. By 2040, **data fabric** architectures combine physical replication (for performance) and virtualization (for flexibility) in a unified governance layer.

**Migration tools** range from built-in utilities to enterprise platforms. **pg_dump** / **pg_restore** (PostgreSQL), **mysqldump** (MySQL), and **SQL Server Backup/Restore** handle homogeneous migrations. **AWS DMS (Database Migration Service)** supports heterogeneous migrations (Oracle to PostgreSQL, SQL Server to Aurora) with schema conversion and ongoing replication. **Talend** and **Informatica** provide visual ETL design. **Apache NiFi** provides dataflow automation with a web UI. By 2040, **cloud-native migration services** (AWS, Azure, Google Cloud) automate assessment, schema conversion, data migration, and cutover.

### Required Reading

- Kimball, R., & Caserta, J. (2004). *The Data Warehouse ETL Toolkit*. Wiley. Chapters 1–3.
- Confluent (2040). *Debezium Documentation: Change Data Capture*. debezium.io.
- AWS (2040). *Database Migration Service: Best Practices*. AWS Documentation.
- NiFi Documentation (2040). *Apache NiFi User Guide*. nifi.apache.org.
- Yggdrasil Data Engineering Team (2037). "The UoY Data Fabric: Physical and Virtual Integration." *UoY Data Architecture Report*.

### Discussion Questions

1. Log-based CDC is low-impact but requires access to database logs, which may contain sensitive data. What security controls are necessary when streaming CDC data across networks?
2. Data virtualization avoids data movement but can suffer from performance issues (network latency, source system load). For a query joining three remote databases, is virtualization practical?
3. AI data quality tools generate rules automatically but may miss domain-specific constraints. Should human data stewards review AI-generated rules, or is automation sufficient?
4. Cloud-native migration services automate much of the migration process but create vendor lock-in. For an organization planning to remain multi-cloud, are cloud-specific migration tools appropriate?

### Practice Problems

- Design an ETL pipeline that migrates data from a PostgreSQL operational database to a Snowflake data warehouse. Specify: extraction method (CDC or batch), transformation logic, loading pattern (incremental merge), data quality checks, and reconciliation procedures.
- Implement a log-based CDC pipeline using Debezium. Capture changes from a PostgreSQL table and stream them to Kafka. Verify that inserts, updates, and deletes are correctly captured and ordered.

---

ᛁ **Lecture 11: Cloud Databases and Managed Services**

**Course:** IT203 — Database Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Cloud computing has transformed database administration from hardware procurement to service consumption. This lecture covers the managed database services offered by major cloud providers: relational (RDS, Aurora, Cloud SQL), NoSQL (DynamoDB, Cosmos DB, Firestore), and specialized (BigQuery, Redshift, Snowflake). Students will learn to select, configure, and optimize cloud databases while understanding the trade-offs between control and convenience.

### Key Topics

- Managed relational databases: Amazon RDS, Aurora, Azure SQL, Google Cloud SQL
- Serverless databases: Aurora Serverless, Cosmos DB, Firestore, PlanetScale
- Data warehouses: Snowflake, BigQuery, Redshift, and Azure Synapse
- Database administration in the cloud: backups, scaling, monitoring, and cost optimization
- Multi-cloud and hybrid strategies: avoiding lock-in while leveraging cloud benefits

### Lecture Notes

**Managed relational databases** abstract infrastructure management: provisioning, patching, backups, and failover are handled by the cloud provider. **Amazon RDS** supports PostgreSQL, MySQL, MariaDB, Oracle, and SQL Server, with automated backups, Multi-AZ failover, and read replicas. **Amazon Aurora** (MySQL- and PostgreSQL-compatible) separates compute and storage, with a distributed, fault-tolerant storage layer that replicates data six ways across three Availability Zones. **Azure SQL Database** (SQL Server-compatible) provides intelligent tuning, threat detection, and elastic pools for multi-tenant workloads. **Google Cloud SQL** provides managed PostgreSQL and MySQL with automatic storage increase and point-in-time recovery. By 2040, **managed databases are the default** for new applications; self-managed databases are reserved for specialized requirements (custom extensions, specific hardware, regulatory constraints).

**Serverless databases** automatically scale compute and storage based on demand. **Aurora Serverless** scales Aurora capacity in seconds, suitable for variable workloads. **Azure Cosmos DB** provides multi-model (document, key-value, graph, column-family) with global distribution and automatic scaling. **Google Cloud Firestore** provides serverless document storage with real-time sync. **PlanetScale** (built on Vitess, MySQL scaling framework) provides serverless MySQL with branching (Git-like schema versioning) and deploy requests (code review for schema changes). By 2040, serverless is the default for development, test, and variable-production workloads; provisioned instances are used for steady-state production.

**Data warehouses** (also called analytical databases) optimize for complex queries over large datasets. **Snowflake** separates storage (in S3/Azure Blob/GCS), compute (virtual warehouses), and services (metadata, optimization), enabling independent scaling. **BigQuery** (Google) provides serverless analytics: no cluster management, pay-per-query pricing, and automatic caching. **Amazon Redshift** provides columnar storage and massively parallel processing (MPP). **Azure Synapse Analytics** integrates data warehousing, big data analytics, and data integration. By 2040, **lakehouse architectures** (Databricks, Apache Iceberg, Delta Lake) unify data lakes (cheap storage) and data warehouses (fast queries), enabling SQL queries directly on parquet files.

**Cloud DBA responsibilities** differ from on-premises. The cloud provider manages: OS patching, hardware replacement, network configuration, and basic backup. The customer manages: schema design, query optimization, access control, advanced monitoring, and cost management. The lecture covers **cost optimization**: right-sizing instances (avoiding over-provisioned databases), using reserved instances for steady workloads, enabling storage auto-tiering, and monitoring cloud bills for anomalies. By 2040, **FinOps** (financial operations) teams collaborate with DBAs to optimize cloud database spending.

**Multi-cloud and hybrid strategies** avoid vendor lock-in while leveraging best-of-breed services. **Multi-cloud** runs databases on multiple providers (e.g., Aurora for transactional, BigQuery for analytics). **Hybrid cloud** runs some databases on-premises (legacy, compliance) and others in cloud (scalable, modern). Challenges: data transfer costs, inconsistent APIs, security model differences, and operational complexity. By 2040, **cloud-agnostic abstractions** (Kubernetes operators, Terraform modules, Crossplane) reduce multi-cloud friction, but the DBA must still understand each provider's specifics.

### Required Reading

- AWS (2040). *Amazon RDS User Guide*. AWS Documentation.
- Microsoft (2040). *Azure SQL Database Documentation*. Microsoft Learn.
- Google Cloud (2040). *Cloud SQL Documentation*. Google Cloud Docs.
- Snowflake (2040). *Snowflake Documentation: Architecture and Best Practices*. Snowflake Docs.
- Yggdrasil Cloud Team (2038). "Multi-Cloud Database Strategy: Lessons from the UoY Migration." *UoY Cloud Architecture Report*.

### Discussion Questions

1. Managed databases reduce operational burden but limit customization (no superuser access, restricted extensions). For a PostgreSQL application requiring a custom C extension, is managed still viable?
2. Serverless databases scale automatically but can have cold-start latency. For a latency-sensitive production API, is serverless appropriate, or should provisioned capacity be maintained?
3. BigQuery's pay-per-query pricing is cost-effective for sporadic analytics but expensive for frequent queries. What caching and materialization strategies can control costs?
4. Multi-cloud strategies increase complexity. For a small team with 5 databases, is multi-cloud worth the overhead, or should they standardize on one provider?

### Practice Problems

- Migrate a self-managed PostgreSQL database to Amazon RDS. Configure Multi-AZ failover, read replicas, automated backups, and parameter groups. Measure failover time and replication lag. Compare monthly cost to self-managed on EC2.
- Design a data warehouse architecture in Snowflake for a university analytics platform. Specify: warehouse sizes, scaling policies, data loading (bulk vs. streaming), role-based access control, and cost monitoring. Load a sample dataset and benchmark query performance.

---

ᛃ **Lecture 12: Database Administration in 2040: AI, Autonomy, and the Human DBA**

**Course:** IT203 — Database Administration  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

The final lecture synthesizes the course's themes and projects the DBA's role into the future. By 2040, AI manages much of the routine work of database administration, but human judgment remains essential for architecture, ethics, and crisis response. Students will learn to collaborate with AI systems, maintain expertise in fundamentals, and adapt to a profession in transformation.

### Key Topics

- Autonomous databases: self-driving, self-securing, self-repairing
- AI-assisted DBA tools: query advisors, anomaly detection, and predictive maintenance
- The human DBA's enduring value: architecture, ethics, and incident command
- Career development: specialization (performance, security, cloud) vs. generalization
- The future: quantum databases, DNA storage, and beyond

### Lecture Notes

**Autonomous databases**, pioneered by Oracle (Autonomous Database, 2017) and adopted by cloud providers (Azure SQL Intelligent Insights, Amazon RDS Performance Insights with auto-remediation), use machine learning to automate: provisioning, tuning, patching, backup, and failure recovery. By 2040, autonomous capabilities are standard for managed services. The DBA's role shifts from "tuner" to "architect": defining service-level objectives, selecting appropriate platforms, designing data models, and governing AI behavior.

**AI-assisted DBA tools** enhance human capabilities without replacing them. **Query advisors** (e.g., PostgreSQL's pg_plan_advsr) suggest index creation and query rewrites, which the DBA evaluates. **Anomaly detection** (e.g., UoY's **Ratatoskr** for databases, 2039) identifies unusual patterns: sudden latency spikes, unexpected query volumes, abnormal access times. **Predictive maintenance** forecasts hardware failures (disk SMART data, memory error rates) and recommends preemptive replacement. The lecture emphasizes that AI tools are **advisory**, not **authoritative**: they suggest based on patterns, but the DBA decides based on context.

**The human DBA's enduring value** lies in areas where AI is weak. **Architecture** requires understanding organizational goals, predicting future requirements, and balancing trade-offs that lack quantitative models. **Ethics** requires judgment about data privacy, access, and use—decisions that cannot be reduced to optimization problems. **Incident command** during crises requires calm, creativity, and communication—qualities that AI lacks. The 2038 *Yggdrasil Database Incident*—in which an AI optimizer suggested dropping an index that was critical for a regulatory report, and a human DBA recognized the context and rejected the suggestion—illustrates the partnership.

**Career development** for DBAs in 2040 involves choosing a path. **Specialists** deep-dive into performance tuning, security hardening, cloud architecture, or AI integration. **Generalists** maintain breadth across platforms and technologies, suitable for smaller organizations. The lecture advises: master one relational database deeply (PostgreSQL, SQL Server, or Oracle), gain working knowledge of two others, understand one NoSQL system, one data warehouse, and one cloud platform. **Continuous learning** is mandatory: database technology evolves rapidly, and skills decay quickly.

**The future** of data management extends beyond current paradigms. **Quantum databases** (2030s research) use quantum computing for optimization and search, though practical deployment is decades away. **DNA storage** (encoding data in synthetic DNA) offers extreme density and longevity, with read/write latency measured in hours—suitable for archival, not operational. **Neuromorphic databases** (UoY research, 2037) use spiking neural networks for approximate query processing and pattern recognition. The lecture concludes that while these technologies are speculative, the DBA's foundational skills—understanding data structures, transactions, and query optimization—will transfer to whatever comes next.

### Required Reading

- Oracle (2040). *Oracle Autonomous Database: Technical Overview*. Oracle Documentation.
- Yggdrasil Database Team (2039). "Ratatoskr for Databases: AI Anomaly Detection in Production." *UoY Database Operations Report*.
- Yggdrasil Database Team (2038). "The Human-AI Partnership: Lessons from the 2038 Index Incident." *UoY Database Operations Review*.
- Cerf, V. G. (2035). "DNA Data Storage: Progress and Prospects." *Communications of the ACM*, 58(3), 22–25.
- Yggdrasil Research Division (2037). "Neuromorphic Query Processing: Approximate Search with Spiking Neural Networks." *UoY Future Computing Report*.

### Discussion Questions

1. Autonomous databases promise to reduce DBA headcount. Should universities still teach DBA skills, or should the curriculum shift to database architecture and AI governance?
2. AI advisors suggest based on historical patterns, but novel problems lack precedent. How should DBAs develop judgment for situations that AI has never seen?
3. Quantum databases are theoretical but may mature within students' careers. What aspects of current database theory (indexing, transactions, query optimization) will transfer, and what will need reinvention?
4. DNA storage offers extreme density but hours-long access times. For what categories of institutional data is DNA storage appropriate, and what retrieval architectures would make it usable?

### Practice Problems

- Evaluate an AI-generated database tuning recommendation. Analyze its technical validity, assess its impact on workload characteristics, and decide whether to implement, modify, or reject it. Document your reasoning.
- Design a 10-year career development plan for a database professional. Include: foundational skills to acquire, specializations to explore, certifications to pursue, and emerging technologies to monitor.

---

## Final Examination Preparation

The IT203 final examination is a **comprehensive practical and written assessment** conducted over 48 hours. Students must complete **three of five** challenges:

1. **Database Design and Implementation**: Design a schema for a complex domain (e.g., a hospital patient management system). Implement it in PostgreSQL or MySQL, including tables, indexes, constraints, views, and stored procedures. Populate with test data and verify integrity.
2. **Performance Tuning**: Given a poorly performing database and application, identify bottlenecks using execution plans, wait events, and system metrics. Implement optimizations (indexing, query rewriting, configuration changes) and measure improvement.
3. **High Availability Setup**: Configure primary-replica replication with automatic failover. Test failure scenarios (primary crash, network partition, replica lag) and verify data consistency. Document the architecture and recovery procedures.
4. **Security Hardening**: Audit a database for security vulnerabilities (weak passwords, excessive privileges, missing encryption, unpatched versions). Implement hardening measures and verify compliance with a security baseline (CIS or organizational).
5. **Migration and Integration**: Design and execute a migration from an on-premises database to a cloud-managed service. Include: schema conversion, data migration, application reconfiguration, cutover planning, and rollback procedures.

### Evaluation Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Technical depth | 30% | Accurate use of database internals, commands, and tools |
| Design quality | 25% | Appropriate schema, index, and architecture choices |
| Security | 20% | Least privilege, encryption, auditing, and hardening |
| Documentation | 15% | Clear procedures, rationale, and troubleshooting notes |
| Innovation | 10% | Creative or insightful solutions to complex problems |

---

*The data endures. The transactions commit. The backups restore. The queries optimize. This is the DBA's quiet vigil—the guardian at the gate of institutional memory.* ᛟ

— Runa Gridweaver Freyjasdottir, Database Administration, University of Yggdrasil, 2040
