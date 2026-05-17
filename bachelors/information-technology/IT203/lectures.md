# IT203: Database Administration & Data Management
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4
**Prerequisites:** IT201 (System Administration)
**Description:** Databases are the critical infrastructure of the information age — the silent engines that power every transaction, query, and analytics pipeline. This course provides comprehensive training in database administration, data modelling, performance tuning, backup and recovery, and the emerging data architectures of 2040. Students work with PostgreSQL (the primary teaching database), MySQL, Redis, MongoDB, and cloud-native databases in the Yggdrasil Sandbox. By the end of the course, students can design schemas that scale, diagnose performance bottlenecks, implement high-availability replication, and reason about the trade-offs between relational, NoSQL, and NewSQL systems. The course culminates in a capstone where students design and operate a database infrastructure for a simulated high-traffic web application.

---

## Lecture 1: The Database Administrator as Steward — Roles, Responsibilities, and Ethics

The database administrator (DBA) is the custodian of an organisation's most valuable asset: its data. This lecture examines the DBA's role, the ethical obligations that accompany access to sensitive information, and the evolution of database administration in the platform engineering era.

**The DBA's responsibilities** span the entire data lifecycle. **Design:** creating logical and physical schemas that accurately model business entities and relationships. **Implementation:** installing, configuring, and patching database software. **Performance:** tuning queries, indexes, and parameters to meet latency and throughput requirements. **Availability:** ensuring databases are accessible when needed through replication, clustering, and failover. **Integrity:** preventing and correcting data corruption through constraints, backups, and validation. **Security:** controlling access, encrypting data, auditing activity, and complying with regulations. **Growth:** planning capacity and archiving historical data. In 2040, the DBA role has split into **specialist tracks**: operational DBAs manage production instances; development DBAs optimise application schemas; data platform engineers build self-service database platforms; and data governance officers ensure compliance and quality.

**The ethics of data stewardship** are profound. A DBA with superuser access can read, modify, or delete any record. **Privacy obligations** require that personal data be accessed only for legitimate purposes, minimised to what is necessary, and protected from unauthorised disclosure. **Regulatory compliance** (GDPR, CCPA, the Nordic Data Compact) imposes legal obligations with severe penalties for violations. **Insider threats** — malicious or negligent actions by authorised users — are a leading cause of data breaches. The **Yggdrasil Data Stewardship Oath**, administered to all database administrators, includes: "I will treat data as a sacred trust, not as a resource to be exploited. I will not access data beyond what my role requires. I will report vulnerabilities and breaches promptly. I will ensure that data outlives the systems that store it."

**The platform engineering perspective** on databases treats database provisioning as a self-service platform capability rather than a ticket-driven request. **Database as a Service (DBaaS)** platforms (Amazon RDS, Azure SQL, Google Cloud SQL, the University's *MímirDB*) provide automated provisioning, patching, backup, and monitoring. **Internal DBaaS** platforms (built on Kubernetes operators like **CloudNativePG**, **KubeDB**, or **Zalando Postgres Operator**) enable developers to provision databases on demand while platform teams enforce standards for security, backup, and compliance. The DBA of 2040 is less a "database babysitter" and more a "database platform engineer" who designs and operates these self-service platforms.

**Required Reading:**
- Craig S. Mullins, *Database Administration: The Complete Guide to DBA Practices and Procedures* (2nd ed., Addison-Wesley, 2012/2035), ch. 1–3
- Thomas M. Connolly & Carolyn E. Begg, *Database Systems: A Practical Approach to Design, Implementation, and Management* (6th ed., Pearson, 2014/2035), ch. 20 ("Database Administration and Security")
- Don Burleson, *Oracle DBA Ethics" (Rampant TechPress, 2003/2035)
- University of Yggdrasil, "The Yggdrasil Data Stewardship Oath and Policy Framework" (2040)

**Discussion Questions:**
1. The DBA role has fragmented into multiple specialisations. Is this fragmentation a sign of professional maturation, or does it create coordination problems when no single person understands the entire data landscape?
2. Data stewardship ethics are often in tension with operational convenience (e.g., encrypting backups makes recovery slower). How should organisations balance ethical obligations against practical constraints?
3. Self-service database platforms democratise access but can lead to "database sprawl" (hundreds of unmanaged instances). Is the solution stricter governance, better automation, or a cultural shift toward shared responsibility?

---

## Lecture 2: Relational Database Architecture — PostgreSQL Internals

Understanding how a database works internally is essential for effective administration. This lecture examines the architecture of PostgreSQL, the most feature-rich open-source relational database, and the principles that underlie its design.

**PostgreSQL architecture** uses a **client-server model** with a **postmaster** process that listens for connections and spawns **backend processes** for each client. **Shared memory** contains buffers, locks, and process information accessible to all backends. **Background writer** flushes dirty buffers to disk. **WAL writer** writes Write-Ahead Log records. **Autovacuum** reclaims storage and updates statistics. **Checkpointer** performs periodic checkpoints. **Stats collector** gathers activity statistics. **WAL archiver** and **WAL receiver/sender** handle replication. This multi-process architecture (as opposed to MySQL's thread-based model) provides process isolation and crash resilience at the cost of higher memory overhead.

**Storage internals** include: **table files** (one file per table, in 1GB segments); **TOAST** (The Oversized-Attribute Storage Technique, for large values); **indexes** (B-tree, hash, GiST, SP-GiST, GIN, BRIN); **WAL** (Write-Ahead Log, for crash recovery and replication); **clog** (commit log, tracking transaction status); and **multixact** (multi-transaction status for row-level locking). **MVCC (Multi-Version Concurrency Control)** is PostgreSQL's approach to concurrency: readers do not block writers, and writers do not block readers. Each transaction sees a **snapshot** of the database at its start time. Old row versions are eventually removed by **VACUUM**. Understanding MVCC is essential for troubleshooting bloat, tuning vacuum, and interpreting query plans.

**Configuration management** in PostgreSQL is controlled by **postgresql.conf** (main configuration), **pg_hba.conf** (client authentication), and **pg_ident.conf** (user name mapping). Key parameters: **shared_buffers** (memory for caching table data, typically 25% of RAM); **effective_cache_size** (estimate of total available cache, used by the query planner); **work_mem** (memory per sort/hash operation); **maintenance_work_mem** (memory for VACUUM, CREATE INDEX, etc.); **max_connections** (concurrent client connections); **wal_level** (WAL detail level: minimal, replica, logical); **max_wal_size** and **checkpoint_completion_target** (tuning checkpoint frequency); and **random_page_cost** (planner's estimate of random read cost, should be tuned to storage type). In 2040, **AI-assisted tuning** (e.g., the *Mímir Tuner* developed at Yggdrasil) analyses workload patterns and recommends configuration changes.

**Required Reading:**
- Bruce Momjian, *PostgreSQL: Introduction and Concepts* (Addison-Wesley, 2001/2035) — foundational, though some details have evolved
- Emanuel Calvo & Angélique J. Smith, *PostgreSQL High Performance* (Packt, 2035), ch. 1–4
- Gregory Smith, *PostgreSQL 9.0 High Performance* (Packt, 2010/2035), ch. 2–4 (still relevant for core concepts)
- University of Yggdrasil, "Mímir Tuner: AI-Assisted PostgreSQL Configuration Optimisation" (2039)

**Discussion Questions:**
1. PostgreSQL's multi-process architecture provides isolation but uses more memory than thread-based designs. Is the isolation benefit worth the memory cost in an era of abundant RAM?
2. MVCC eliminates read locks but creates table bloat that must be managed by VACUUM. Is MVCC a genuine advance over lock-based concurrency, or does it merely trade one problem (locking) for another (bloat and vacuum tuning)?
3. AI-assisted tuning promises to optimise database configuration automatically, but it requires detailed workload data that may be sensitive. Is the performance gain worth the privacy implications of sharing workload patterns with an AI system?

---

## Lecture 3: SQL Mastery for Administrators — Query Optimisation and Performance Tuning

SQL is the language of relational databases, and mastering it is the foundation of database administration. This lecture covers advanced SQL, query planning, index design, and performance tuning.

**Advanced SQL** includes: **window functions** (`ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `LEAD()`, `LAG()`, `FIRST_VALUE()`, `LAST_VALUE()`, `NTH_VALUE()`, `SUM() OVER (...)`, `AVG() OVER (...)`) for analytical queries without self-joins; **common table expressions (CTEs)** (`WITH recursive_cte AS (...)`) for readable, composable queries; **recursive queries** for hierarchical data (org charts, bill of materials, graph traversal); **lateral joins** (`LATERAL`) for correlated subqueries in the FROM clause; **JSON/JSONB operators** (`->`, `->>`, `#>`, `@>`, `?`, `jsonb_agg`, `jsonb_object_agg`) for semi-structured data; **full-text search** (`to_tsvector`, `to_tsquery`, `ts_rank`, `ts_headline`); **geospatial queries** (PostGIS extension: `ST_Distance`, `ST_Within`, `ST_Intersects`); and **custom aggregates** and **procedural code** (PL/pgSQL functions, triggers). In 2040, **AI-assisted SQL generation** (natural language to SQL, query explanation, and optimisation suggestions) is standard in database IDEs.

**Query planning** is the process by which the database translates SQL into an execution plan. **EXPLAIN** shows the plan; **EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)** shows the plan with actual execution statistics. Key plan nodes: **Seq Scan** (read entire table — slow for large tables); **Index Scan** (read index, then fetch rows from table); **Index Only Scan** (read index without table access — fastest); **Bitmap Heap Scan** (bitmap index scan followed by heap access); **Nested Loop** (join small outer table with inner table using index); **Hash Join** (hash the smaller table, probe with larger); **Merge Join** (sort both tables, merge — efficient for large sorted inputs); **Sort** (ORDER BY); **Aggregate** (GROUP BY); and **Limit** (TOP N). Understanding these nodes enables diagnosis of slow queries.

**Index design** is the most impactful performance optimisation. **B-tree indexes** (the default) support equality and range queries on scalar data. **Partial indexes** (`CREATE INDEX ... WHERE condition`) index only a subset of rows, reducing size and maintenance cost. **Expression indexes** (`CREATE INDEX ON table (lower(column))`) index computed values. **Covering indexes** (include additional columns) enable Index Only Scans. **Composite indexes** (multiple columns) support multi-column queries but require careful column ordering (most selective first, equality before range). **GIN indexes** support full-text search and JSONB containment. **GiST indexes** support geospatial and range queries. **BRIN indexes** (Block Range INdexes) are tiny indexes for naturally ordered data (timestamps, sequences). In 2040, **AI-assisted index advisors** (e.g., PostgreSQL's *hypopg* with ML-based recommendation) suggest indexes based on query workload.

**Lab Exercise:** Students optimise a poorly performing database for a simulated e-commerce application. They must: analyse slow queries using EXPLAIN ANALYZE; design appropriate indexes; rewrite inefficient queries using CTEs and window functions; partition large tables; and tune PostgreSQL configuration parameters. Performance improvement targets: reduce p95 query latency by 80% and eliminate table scans on the top 10 queries.

**Required Reading:**
- Joe Celko, *SQL for Smarties: Advanced SQL Programming* (5th ed., Morgan Kaufmann, 2015/2035), ch. 1–5, 8, 10
- Markus Winand, *SQL Performance Explained* (3rd ed., 2015/2035), ch. 1–5
- Laurenz Albe & Hans-Jürgen Schönig, *PostgreSQL Query Optimization" (Packt, 2035), ch. 1–4
- University of Yggdrasil, "Query Optimisation Case Study: Reducing E-Commerce Latency from 2s to 50ms" (2039)

**Discussion Questions:**
1. Window functions are powerful but can be difficult to understand and debug. Are they an essential SQL feature, or do they encourage overly complex queries that should be broken into simpler steps?
2. Index design is often described as an art rather than a science. Is there a systematic methodology for index design, or does it inevitably require intuition and experimentation?
3. AI-assisted index advisors recommend indexes based on workload analysis, but workload patterns change. How should administrators balance the cost of creating and maintaining indexes against the benefits of AI recommendations?

---

## Lecture 4: High Availability and Replication — Keeping Data Accessible

Downtime is expensive. This lecture covers the technologies and architectures that ensure databases remain available despite hardware failures, software bugs, and human error.

**PostgreSQL replication** keeps standby servers synchronised with the primary. **Streaming replication** (physical replication, since PostgreSQL 9.0) streams WAL records from primary to standby in near-real-time. **Synchronous replication** waits for confirmation from one or more standbys before committing, ensuring zero data loss at the cost of latency. **Asynchronous replication** commits on the primary without waiting, minimising latency but with a small risk of data loss on failover. **Cascading replication** allows standbys to replicate from other standbys, reducing load on the primary. **Logical replication** (since PostgreSQL 10) replicates at the table level, enabling selective replication, cross-version replication, and replication to non-PostgreSQL systems. In 2040, **logical replication** is the standard for active-active architectures and data migration.

**Failover and promotion** transfer primary responsibility to a standby. **Manual failover** requires an administrator to stop the old primary, promote a standby (`pg_ctl promote`), and redirect clients. **Automatic failover** uses tools like **Patroni** (Python-based, uses DCS like etcd or ZooKeeper for leader election), **repmgr** (command-line management), or **pg_auto_failover** (Citus extension). **Connection pooling** (PgBouncer, Odyssey) reduces connection overhead and enables transparent failover. **In 2040, Kubernetes operators** (CloudNativePG, Zalando Postgres Operator, StackGres) automate failover, backup, and scaling within container orchestration platforms.

**High availability architectures** vary by tolerance for downtime and data loss. **Single primary with hot standby:** one primary, one or more standbys; failover to standby on primary failure. **Single primary with warm standby:** standby is not streaming but restored from backups; longer RTO. **Dual primary (multi-master):** both nodes accept writes; requires conflict resolution (rarely used with PostgreSQL, more common with MySQL Group Replication or Galera Cluster). **Active-active with logical replication:** multiple primaries, each replicating specific tables or databases to others; used for geographic distribution and workload segregation. **Shared storage:** multiple nodes access the same storage (SAN, NAS, or distributed filesystem); only one is primary at a time. In 2040, **distributed SQL databases** (CockroachDB, YugabyteDB, Google Spanner) provide built-in high availability and horizontal scalability, challenging traditional primary-standby architectures.

**The Yggdrasil Database Platform** operates a **Patroni-managed PostgreSQL cluster** with: one primary (writes), three synchronous standbys (zero RPO), two asynchronous standbys (disaster recovery), automatic failover (<30 seconds), PgBouncer connection pooling, and continuous backup to the Mímir Archive (WAL archiving + weekly base backups). Students configure a miniature version of this architecture in the Sandbox.

**Required Reading:**
- Zoltan Böszörményi & Hans-Jürgen Schönig, *PostgreSQL Replication* (2nd ed., Packt, 2015/2035), ch. 1–4
- Alexander Kukushkin, "Patroni: A Template for PostgreSQL High Availability" (GitHub, 2035)
- Gabriele Bartolini et al., "CloudNativePG: The Kubernetes Operator for PostgreSQL" (EDB, 2035)
- Martin Kleppmann, *Designing Data-Intensive Applications*, ch. 5 ("Replication")
- University of Yggdrasil, "The Yggdrasil Database Platform: Patroni, PgBouncer, and Kubernetes" (2039)

**Discussion Questions:**
1. Synchronous replication guarantees zero data loss but increases write latency. For a financial trading application, is synchronous replication mandatory, or can asynchronous replication with careful monitoring suffice?
2. Automatic failover reduces RTO but can cause split-brain if network partitions occur. Is the risk of automatic failover (false positives, data inconsistency) worth the benefit of reduced downtime?
3. Distributed SQL databases (CockroachDB, Spanner) promise high availability and scalability without the complexity of manual replication management. Will they eventually replace traditional PostgreSQL/MySQL replication, or will the familiarity and maturity of traditional databases preserve their dominance?

---

## Lecture 5: Backup, Recovery, and Point-in-Time Restoration

Backups are the insurance policy of database administration. This lecture covers backup strategies, tools, and the procedures for recovering from data loss.

**PostgreSQL backup methods** include: **SQL dumps** (`pg_dump` for single databases, `pg_dumpall` for all databases); **file-system-level backups** (copying the data directory with `tar` or `rsync`, requiring the server to be stopped or using `pg_start_backup` / `pg_stop_backup` for online backup); **continuous archiving** (WAL archiving to a secondary location, enabling point-in-time recovery); and **logical replication** (replicating to a standby that serves as a warm backup). In 2040, **incremental backups** (using `pg_basebackup` with `--wal-method=fetch` and incremental options) reduce backup time and storage. **Cloud-native backups** (RDS automated backups, Azure Database backup, CloudNativePG scheduled backups) abstract the details.

**Point-in-time recovery (PITR)** restores a database to any moment in time using a base backup and archived WAL files. The procedure: restore the base backup; create a `recovery.signal` file; configure `recovery_target_time` in `postgresql.conf`; start PostgreSQL; and the server replays WAL until the target time is reached. **PITR is essential** for recovering from logical errors (accidental `DELETE`, `DROP TABLE`, application bugs) that are not caught by failover. In 2040, **AI-assisted recovery** (analysing WAL to identify the exact moment before a destructive operation) reduces recovery time by 50–70%.

**Backup tools** include: **pgBackRest** (modern, feature-rich: full/incremental/differential backups, compression, encryption, retention policies, S3/Azure/GCS support); **Barman** (2ndQuadrant's backup tool, similar to pgBackRest); **pg_probackup** (Postgres Professional's tool); **WAL-G** (modern, cloud-native, used by Yandex and CitusData); and **pg_dump** / **pg_dumpall** (logical dumps, always required for migrations and schema-only backups). In 2040, **pgBackRest** and **WAL-G** are the dominant open-source tools; **pg_dump** remains essential for logical backups and cross-version migration.

**Recovery procedures** vary by failure type. **Hardware failure:** promote standby (if available) or restore from backup to new hardware. **Corruption:** identify extent of corruption with `pg_dump` or `amcheck`; restore from backup if corruption is widespread; use `zero_damaged_pages` for minor corruption (with data loss). **Logical error (human mistake):** use PITR to restore to before the error; extract the affected data; reload into production. **Ransomware:** restore from offline, immutable backups (WORM tape, air-gapped storage). **Disaster (data centre loss):** failover to geographically distant standby; or restore from offsite backup. In all cases, **testing recovery procedures** is essential: untested backups are Schrödinger's backups — they are both valid and invalid until you try to restore.

**Required Reading:**
- PostgreSQL Documentation, "Backup and Restore" (Chapter 26, 2040)
- David Steele, "pgBackRest Documentation" (2035)
- Martin Kleppmann, *Designing Data-Intensive Applications*, ch. 7 ("Batch Processing")
- NIST, *Guide to Storage Encryption Technologies for End User Devices* (SP 800-111 Rev. 2, 2035)
- University of Yggdrasil, "Database Recovery Procedures: Runbooks and Drill Schedules" (2039)

**Discussion Questions:**
1. PITR requires continuous WAL archiving, which consumes significant storage and bandwidth. For databases with high write volume, is the storage cost of PITR justified by the ability to recover from logical errors?
2. Immutable backups (WORM, air-gapped) are the only reliable defence against ransomware, but they are expensive and slow to restore. Is the ransomware threat severe enough to mandate immutable backups for all databases, or only for critical systems?
3. Testing recovery procedures is essential but disruptive. How often should organisations perform full recovery drills, and what are the risks of testing too infrequently versus too frequently?

---

## Lecture 6: NoSQL and NewSQL — Beyond the Relational Model

Relational databases are not always the best choice. This lecture examines the alternatives: document stores, key-value stores, wide-column stores, graph databases, search engines, and the NewSQL systems that attempt to combine the best of both worlds.

**Document stores** (MongoDB, Couchbase, Firestore) store semi-structured data as JSON-like documents. They are ideal for: rapidly evolving schemas (product catalogues, content management); hierarchical data (nested documents without joins); and mobile/sync applications (offline-first with conflict resolution). **MongoDB** features: flexible schema; rich query language (aggregation pipelines, text search, geospatial queries); sharding for horizontal scaling; and ACID transactions (since v4.0). **Trade-offs**: no JOINs (denormalisation required); eventual consistency in sharded clusters; and index bloat if schemas change frequently. In 2040, **MongoDB Atlas** (managed cloud service) is the dominant MongoDB deployment model.

**Key-value stores** (Redis, DynamoDB, etcd, Riak) provide O(1) lookup by key. **Redis** is the dominant in-memory store: strings, hashes, lists, sets, sorted sets, bitmaps, hyperloglogs, streams, and geospatial indexes. It supports persistence (RDB snapshots, AOF logs), replication, clustering, and Lua scripting. **Use cases**: caching, session storage, rate limiting, real-time leaderboards, message queues (Redis Streams), and pub/sub. **DynamoDB** (AWS) is the dominant managed key-value store: single-digit millisecond latency, automatic scaling, global tables, and on-demand capacity. In 2040, **Redis** and **DynamoDB** are the standard choices for key-value workloads.

**Wide-column stores** (Cassandra, ScyllaDB, HBase, Bigtable) optimise for massive write throughput and wide tables with many columns. **Cassandra** features: peer-to-peer architecture (no single point of failure); tunable consistency (ONE, QUORUM, ALL); partition keys and clustering columns for data distribution and sorting; and CQL (Cassandra Query Language, SQL-like). **Use cases**: time-series data, sensor data, messaging, and write-heavy applications. **Trade-offs**: no JOINs, no ACID transactions (lightweight transactions since v2.0), and complex data modelling requirements.

**Graph databases** (Neo4j, Amazon Neptune, TigerGraph, ArangoDB) model data as nodes and edges with properties. **Neo4j** uses **Cypher** query language: `MATCH (p:Person)-[:KNOWS]->(friend) WHERE p.name = 'Alice' RETURN friend.name`. **Use cases**: social networks, recommendation engines, fraud detection, knowledge graphs, and network management. **Trade-offs**: specialised for relationship-heavy data; poor performance for non-graph workloads; and proprietary query languages (though GQL — Graph Query Language — is standardising in ISO/IEC).

**NewSQL databases** (CockroachDB, Google Spanner, YugabyteDB, VoltDB) provide ACID transactions and SQL queries with horizontal scalability. **CockroachDB** is PostgreSQL-compatible, distributed, and strongly consistent (using the Raft consensus algorithm). **Google Spanner** provides global distribution, external consistency (TrueTime API), and SQL semantics. **Trade-offs**: write latency (consensus requires network round-trips); complexity; and cost. In 2040, **NewSQL** is the choice for applications that outgrow single-node PostgreSQL/MySQL but require transactional consistency.

**Required Reading:**
- Martin Kleppmann, *Designing Data-Intensive Applications*, ch. 2 ("Data Models and Query Languages")
- Kristina Chodorow, *MongoDB: The Definitive Guide* (3rd ed., O'Reilly, 2019/2035), ch. 1–4
- Josiah L. Carlson, *Redis in Action* (Manning, 2013/2035), ch. 1–3
- Ian Robinson, Jim Webber & Emil Eifrem, *Graph Databases* (2nd ed., O'Reilly, 2015/2035), ch. 1–3
- Spencer Kimball et al., "CockroachDB: The Resilient Geo-Distributed SQL Database" (Cockroach Labs, 2035)

**Discussion Questions:**
1. MongoDB's flexible schema is praised for agility but criticised for enabling poor data modelling. Is schema flexibility a feature that empowers developers or a trap that leads to inconsistent data?
2. Redis is often used as a cache, but it is also a database. Using Redis as a primary database risks data loss on restart (if persistence is misconfigured). Should Redis be restricted to caching, or is it suitable for primary storage when properly configured?
3. NewSQL databases promise the best of both worlds (SQL + scalability), but they add latency and complexity. For what classes of applications is NewSQL genuinely necessary, and for what classes is traditional PostgreSQL with read replicas sufficient?

---

## Lecture 7: Data Modelling — From Conceptual to Physical Design

Data modelling is the process of defining the structure of data to support business requirements. This lecture covers the three levels of data modelling — conceptual, logical, and physical — and the techniques for each.

**Conceptual modelling** captures business entities and relationships without regard to implementation. **Entity-Relationship (ER) diagrams** use rectangles (entities), diamonds (relationships), and lines (connections) to visualise data. ** cardinality** (1:1, 1:N, M:N) defines how many instances participate in a relationship. **Supertype/subtype** (generalisation/specialisation) models hierarchies (e.g., Person -> Employee, Customer). In 2040, **domain-driven design (DDD)** has influenced conceptual modelling: **aggregates** (clusters of entities and value objects with a single root), **bounded contexts** (explicit boundaries within which a domain model applies), and **ubiquitous language** (shared terminology between domain experts and technologists). The University's *Mímir Modelling Framework* integrates DDD with traditional ER modelling.

**Logical modelling** defines entities, attributes, keys, and relationships in detail. **Normalisation** eliminates redundancy and anomalies. **First Normal Form (1NF):** atomic values, no repeating groups. **Second Normal Form (2NF):** no partial dependencies (non-key attributes depend on the whole key). **Third Normal Form (3NF):** no transitive dependencies (non-key attributes depend only on the key). **Boyce-Codd Normal Form (BCNF):** every determinant is a candidate key. **Higher normal forms** (4NF, 5NF, DKNF) address multi-valued dependencies and join dependencies but are rarely required in practice. **Denormalisation** (intentionally adding redundancy) improves read performance at the cost of write complexity and data consistency. In 2040, **automated normalisation checkers** analyse schemas and suggest improvements or intentional denormalisations.

**Physical modelling** translates the logical model into database-specific structures. **Table design:** column data types, constraints (NOT NULL, UNIQUE, CHECK, FOREIGN KEY), and defaults. **Index design:** primary keys, foreign key indexes, search indexes, and covering indexes. **Partitioning:** range (by date), list (by category), hash (by hash of key), and composite partitioning. **Tablespaces:** placing tables and indexes on different storage tiers (SSD for hot data, HDD for cold). **Compression:** reducing storage size at the cost of CPU. **Encryption:** transparent data encryption (TDE) or column-level encryption. In 2040, **AI-assisted physical design** (the *Mímir Designer* tool) generates physical schemas from logical models, suggesting types, indexes, partitions, and compression based on workload predictions.

**Lab Exercise:** Students model a database for a simulated University library system. They must: create a conceptual ER diagram; develop a 3NF logical model; design the physical schema for PostgreSQL (with appropriate types, indexes, constraints, and partitioning); write DDL scripts; and load sample data. The schema must support: book cataloguing, patron management, circulation (check-out/check-in), holds and reservations, fines, and analytics (most popular books, overdue trends, patron demographics).

**Required Reading:**
- Thomas M. Connolly & Carolyn E. Begg, *Database Systems*, ch. 14–17
- Elmasri & Navathe, *Fundamentals of Database Systems* (7th ed., Pearson, 2017/2035), ch. 9–10
- Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software* (Addison-Wesley, 2003/2035), ch. 5–6
- University of Yggdrasil, "The Mímir Modelling Framework: Integrating DDD and ER Modelling" (2039)

**Discussion Questions:**
1. Normalisation eliminates redundancy but can fragment data across many tables, requiring complex joins. Is 3NF always the right target, or are there cases where 2NF or even denormalised schemas are preferable?
2. Domain-driven design introduces concepts (aggregates, bounded contexts) that do not map directly to relational databases. Is DDD compatible with relational modelling, or does it push toward document stores and event sourcing?
3. AI-assisted physical design promises to automate schema optimisation, but it requires workload predictions that may be inaccurate. Can AI genuinely design better physical schemas than experienced DBAs, or does it merely automate the obvious choices?

---

## Lecture 8: Security, Encryption, and Compliance in Database Systems

Databases store the most sensitive data in any organisation. This lecture covers database security: authentication, authorisation, encryption, auditing, and compliance.

**Authentication** verifies identity. **PostgreSQL methods:** trust (no auth, for local testing), password (md5, scram-sha-256), GSSAPI (Kerberos), SSPI (Windows), LDAP, RADIUS, certificate (SSL client certs), and PAM. **pg_hba.conf** controls which authentication method is used for which connection. In 2040, **centralised identity** (LDAP, Active Directory, cloud IAM) is standard for enterprise databases. **Multi-factor authentication (MFA)** is mandatory for privileged accounts. **Password policies** enforce complexity, rotation, and history. **Certificate-based authentication** eliminates passwords entirely, using TLS client certificates.

**Authorisation** controls access. **PostgreSQL roles** (users and groups) are granted **privileges** on database objects. **Object privileges:** SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER on tables; USAGE on schemas, sequences, functions; CONNECT on databases; TEMPORARY on temp table space. **Row-level security (RLS)** restricts rows based on user attributes: `CREATE POLICY user_policy ON accounts FOR ALL TO PUBLIC USING (user_id = current_user_id())`. **Column-level security** restricts columns (via views or RLS with expressions). **Default privileges** control permissions on newly created objects. In 2040, **attribute-based access control (ABAC)** — where permissions depend on user attributes, resource attributes, and environmental context — is the emerging standard for fine-grained access control.

**Encryption** protects data from unauthorised disclosure. **Encryption at rest:** OS-level (LUKS, BitLocker), filesystem-level (eCryptfs, ZFS encryption), or database-level (TDE — Transparent Data Encryption). **Encryption in transit:** TLS 1.3 for all client connections. **Encryption in use:** **homomorphic encryption** (computing on encrypted data without decryption — still experimental in 2040); **secure enclaves** (Intel SGX, AMD SEV) that process sensitive data in hardware-isolated memory. **Key management** is critical: keys must be stored in HSMs (Hardware Security Modules) or cloud KMS (Key Management Services), rotated regularly, and accessible only to authorised processes. In 2040, **quantum-resistant encryption** (post-quantum algorithms) is being deployed for long-term data protection.

**Auditing** records who did what and when. **PostgreSQL audit extensions:** **pgaudit** (session and object auditing); **pgAudit Analyse** (user-friendly reporting); and **pgAudit Log** (structured logging). **Audit requirements:** the EU's Digital Operational Resilience Act (DORA, 2035) mandates 7-year retention of financial system audit logs; HIPAA requires 6 years of access logs; the Nordic Data Compact requires comprehensive data access auditing for all personal data. In 2040, **immutable audit trails** (blockchain-based or WORM storage) ensure that audit logs cannot be tampered with.

**Required Reading:**
- PostgreSQL Documentation, "Client Authentication" (Chapter 20, 2040) and "Role Membership" (Chapter 21)
- NIST, *Guide to Storage Encryption Technologies* (SP 800-111 Rev. 2, 2035)
- European Union, *Digital Operational Resilience Act (DORA)* (2035)
- Bruce Schneier, *Applied Cryptography* (20th Anniversary ed., Wiley, 2035), ch. 1–3, 10
- University of Yggdrasil, "Database Security at Yggdrasil: Authentication, Encryption, and Audit" (2039)

**Discussion Questions:**
1. Row-level security (RLS) provides fine-grained access control but can impact query performance. Is RLS a practical security mechanism for high-throughput systems, or should access control be enforced in the application layer?
2. Homomorphic encryption promises to enable computation on encrypted data, but it is orders of magnitude slower than plaintext computation. Is homomorphic encryption a realistic technology for production databases, or will it remain a research curiosity?
3. Audit log retention requirements (7 years under DORA) create massive storage and management burdens. Are these requirements proportionate to the security benefit, or do they impose compliance costs that outweigh the risk reduction?

---

## Lecture 9: Cloud and Managed Database Services

Cloud databases have transformed how organisations provision, operate, and scale database infrastructure. This lecture covers cloud database services, their trade-offs, and the operational considerations for managed databases.

**Amazon RDS** (Relational Database Service) was the first major managed database service (2009). It automates: provisioning, patching, backup, recovery, scaling (read replicas), failover (Multi-AZ), and monitoring. **RDS engines:** PostgreSQL, MySQL, MariaDB, Oracle, SQL Server, and **Amazon Aurora** (a MySQL/PostgreSQL-compatible engine with up to 5x performance improvement). **RDS limitations:** limited root access, no custom plugins (for most engines), and vendor lock-in. **Amazon DynamoDB** is the managed NoSQL service: single-digit millisecond latency, automatic scaling, global tables, and on-demand capacity.

**Azure SQL Database** is Microsoft's managed SQL Server service. **Service tiers:** Basic, Standard, Premium, Hyperscale (up to 100 TB), and Serverless (auto-scales based on workload). **Features:** automatic tuning (AI-driven index and query recommendations), geo-replication, transparent data encryption, and Advanced Threat Protection. **Azure Cosmos DB** is the managed multi-model database: SQL, MongoDB, Cassandra, Gremlin (graph), and Table APIs on a globally distributed backend. **Google Cloud SQL** manages PostgreSQL, MySQL, and SQL Server. **Google Cloud Spanner** is the globally distributed, strongly consistent NewSQL database. **Cloud Bigtable** is the wide-column store for massive workloads.

**Operational considerations** for managed databases include: **vendor lock-in** (proprietary features make migration difficult); **cost management** (managed databases are more expensive than self-managed; reserved instances and committed use discounts reduce costs); **compliance** (cloud providers offer certifications: SOC 2, ISO 27001, HIPAA BAA, GDPR DPA); **performance** (shared resources in multi-tenant services can have noisy neighbours); **customisation** (limited ability to install extensions, modify kernel parameters, or access the OS); and **disaster recovery** (cross-region replication, but RTO/RPO depends on service tier). In 2040, **multi-cloud database strategies** (using different cloud providers for different workloads) are common, increasing complexity but reducing lock-in.

**The University's cloud database strategy** uses: **on-premises PostgreSQL** (Patroni clusters) for regulated student data and research datasets; **Azure SQL Database** (Hyperscale tier) for administrative systems; **Amazon Aurora** (PostgreSQL-compatible) for web applications with global users; **Redis Enterprise Cloud** for caching and session storage; and **Elasticsearch** (Elastic Cloud) for search and log analytics. This **polyglot, multi-cloud** approach maximises flexibility but requires a data platform team to manage cross-cloud operations, security, and compliance.

**Required Reading:**
- AWS, *Amazon RDS User Guide* (2040)
- Microsoft, *Azure SQL Database Documentation* (2040)
- Google Cloud, *Cloud SQL and Cloud Spanner Documentation* (2040)
- Gojko Adzic & Robert Chatley, *Serverless Computing: Concepts, Tools, and Architecture* (Manning, 2035), ch. 5 ("Data in Serverless Architectures")
- University of Yggdrasil, "The Yggdrasil Multi-Cloud Database Strategy: Polyglot Persistence at Scale" (2039)

**Discussion Questions:**
1. Managed databases reduce operational burden but increase vendor lock-in. For a small organisation with limited DBA expertise, is the convenience of managed databases worth the long-term dependency?
2. Multi-cloud strategies reduce lock-in but add complexity (different APIs, monitoring tools, security models). Is the flexibility worth the operational overhead, or should organisations standardise on a single cloud provider?
3. Cloud database costs can spiral unexpectedly (auto-scaling, data transfer, storage growth). What governance mechanisms should organisations implement to control cloud database spending?

---

## Lecture 10: Data Warehousing and Analytics — OLAP, ETL, and Modern Data Stacks

Transactional databases (OLTP) are optimised for fast writes and single-row lookups. Analytics workloads (OLAP) require scanning millions of rows and aggregating across dimensions. This lecture covers data warehousing, ETL/ELT pipelines, and the modern data stack.

**OLAP vs. OLTP.** OLTP systems handle high volumes of short transactions (INSERT, UPDATE, DELETE) with millisecond latency. OLAP systems handle low volumes of complex analytical queries (aggregation, grouping, window functions) over large datasets. **OLAP databases** use **columnar storage** (storing data by column rather than by row, enabling efficient compression and vectorised processing): **Amazon Redshift**, **Google BigQuery**, **Snowflake**, **Databricks Delta Lake**, **Apache Druid**, **ClickHouse**. **Star schema** is the classic dimensional model: a central **fact table** (measurements) surrounded by **dimension tables** (context: time, product, customer, location).

**ETL (Extract, Transform, Load)** and **ELT (Extract, Load, Transform)** are the pipelines that move data from sources to the warehouse. **ETL** transforms data before loading (traditional, used when source data is dirty or unstructured). **ELT** loads raw data first and transforms it in the warehouse (modern, enabled by the power of cloud data warehouses). **Tools:** **Apache Airflow** (orchestration), **dbt** (data build tool, SQL-based transformations), **Fivetran** / **Stitch** (managed data connectors), **Apache Kafka** (streaming data pipeline), **Apache Flink** (stream processing), and **AWS Glue** / **Azure Data Factory** / **Google Cloud Dataflow** (cloud-native ETL). In 2040, **reverse ETL** (syncing warehouse data back to operational systems) is standard for operational analytics.

**The modern data stack** (2020s–2040) consists of: **ingestion** (Fivetran, Airbyte); **storage** (cloud data warehouse: Snowflake, BigQuery, Redshift); **transformation** (dbt); **orchestration** (Airflow, Prefect, Dagster); **observability** (Monte Carlo, Bigeye); **BI** (Tableau, Looker, Metabase, Superset); **reverse ETL** (Census, Hightouch); and **AI/ML** (feature stores, model training on warehouse data). **Data contracts** (agreements between data producers and consumers about schema, quality, and SLAs) ensure reliability in complex pipelines. **Data mesh** (decentralised domain-oriented data ownership) challenges the centralised data warehouse model, distributing responsibility to domain teams.

**Required Reading:**
- Ralph Kimball & Margy Ross, *The Data Warehouse Toolkit* (3rd ed., Wiley, 2013/2035), ch. 1–4
- Claire Carroll & Anna Filippova, *dbt Labs Documentation* (2040)
- James Densmore, *Data Pipelines with Apache Airflow* (Packt, 2021/2035), ch. 1–3
- Zhamak Dehghani, "Data Mesh: Delivering Data-Driven Value at Scale" (O'Reilly, 2022/2035), ch. 1–3
- University of Yggdrasil, "The Yggdrasil Data Platform: Modern Data Stack for Academic Analytics" (2039)

**Discussion Questions:**
1. Columnar storage is optimal for analytics but poor for transactional workloads. Will hybrid databases (supporting both row and column storage) eventually dominate, or will the two remain separate?
2. dbt has popularised SQL-based transformations, but it shifts complexity from ETL tools to SQL. Is dbt a genuine simplification, or does it merely move the problem without solving it?
3. Data mesh decentralises data ownership but requires significant cultural and organisational change. Is data mesh a realistic model for most organisations, or is it applicable only to large tech companies with mature engineering cultures?

---

## Lecture 11: Emerging Database Technologies — Time-Series, Vector, and Quantum Databases

Database technology continues to evolve. This lecture examines three emerging categories: time-series databases, vector databases, and the speculative frontier of quantum databases.

**Time-series databases** (TSDBs) specialise in data indexed by time: metrics, sensor readings, financial ticks, application events. **Characteristics:** high write throughput (millions of points per second); efficient time-range queries; downsampling and aggregation; retention policies (automatic deletion of old data); and anomaly detection. **Leading TSDBs:** **InfluxDB** (open-source and commercial); **TimescaleDB** (PostgreSQL extension); **Prometheus** (monitoring-focused); **QuestDB** (fast SQL-based); and **Apache IoTDB** (IoT-focused). In 2040, **TimescaleDB** is the dominant choice for organisations that want time-series capabilities within a familiar PostgreSQL environment. The University's *Muninn Metrics* platform uses TimescaleDB to store 50 billion data points from campus sensors and systems.

**Vector databases** store and query high-dimensional vectors (embeddings from machine learning models). **Use cases:** semantic search (find documents similar to a query vector); recommendation systems (find items similar to user preferences); image search (find visually similar images); and anomaly detection (find vectors that deviate from normal patterns). **Vector search** uses **approximate nearest neighbour (ANN)** algorithms: **HNSW** (Hierarchical Navigable Small World), **IVF** (Inverted File Index), **PQ** (Product Quantisation). **Leading vector databases:** **Pinecone** (managed); **Weaviate** (open-source, GraphQL interface); **Milvus** (open-source, cloud-native); **pgvector** (PostgreSQL extension); and **Redis** (with vector search module). In 2040, **pgvector** is the standard for organisations that want vector search within PostgreSQL, while **Pinecone** and **Weaviate** dominate standalone deployments.

**Quantum databases** are speculative. A **quantum database** would use quantum mechanics to store and query data, potentially offering exponential speedups for certain queries (e.g., Grover's algorithm for unstructured search). However, as of 2040, no practical quantum database exists. Research focuses on: **quantum random access memory (qRAM)**; **quantum graph databases** (using quantum walks); and **quantum machine learning for database optimisation** (using quantum annealers to optimise query plans). The University of Yggdrasil's **Quantum Information Lab** maintains a research programme on quantum databases, but commercial viability is not expected before 2060.

**Required Reading:**
- TimescaleDB Documentation, "Time-Series Concepts" (2040)
- Pinecone Documentation, "Vector Database Fundamentals" (2040)
- Weaviate Documentation, "What Is a Vector Database?" (2040)
- Scott Aaronson, "Quantum Computing Since Democritus" (Cambridge, 2013/2035), ch. 14 ("Quantum Computing and the Future")
- University of Yggdrasil, "Muninn Metrics: TimescaleDB at 50 Billion Data Points" (2039)

**Discussion Questions:**
1. Time-series databases are highly optimised for their niche, but general-purpose databases (PostgreSQL with TimescaleDB, ClickHouse) are increasingly capable. Will specialised TSDBs be displaced by general-purpose databases, or will their optimisation retain a niche?
2. Vector databases are essential for AI-powered search, but they are yet another database to manage. Will vector search be absorbed into general-purpose databases (like pgvector), or will standalone vector databases remain dominant?
3. Quantum databases are purely speculative. Is research into quantum databases a worthwhile investment, or should resources be directed toward more immediate problems?

---

## Lecture 12: The Future of Data — Governance, Ethics, and the Data-Centric Organisation

The final lecture examines the strategic and ethical dimensions of data management: data governance, data ethics, and the emergence of the data-centric organisation.

**Data governance** is the framework for managing data availability, usability, integrity, and security. **Components:** data quality (accuracy, completeness, consistency, timeliness); data lineage (tracking data from origin to consumption); data catalogues (inventories of datasets with metadata); master data management (single source of truth for critical entities); and data policies (retention, access, privacy, security). **Tools:** **Apache Atlas**, **Collibra**, **Alation**, **DataHub** (LinkedIn's open-source catalogue). In 2040, **AI-assisted governance** automatically classifies data, detects quality issues, suggests policies, and enforces compliance.

**Data ethics** encompasses: **privacy** (respecting individual autonomy over personal data); **fairness** (preventing algorithmic bias in data-driven decisions); **transparency** (explaining how data is used and how decisions are made); **accountability** (holding organisations responsible for data misuse); and **consent** (ensuring that data collection and use are genuinely voluntary and informed). The **EU AI Act (2024/2035)** classifies AI systems by risk and imposes strict requirements on high-risk systems (biometric identification, critical infrastructure, education, employment, law enforcement). The **Nordic Data Compact (2035)** goes further, requiring algorithmic transparency for all automated decisions affecting individuals and mandating data localisation for sensitive categories.

**The data-centric organisation** treats data as a strategic asset rather than a byproduct of operations. **Characteristics:** data is shared across silos (not hoarded in departments); data quality is everyone's responsibility (not just the DBA's); decisions are evidence-based (not hierarchical); and data products are developed with the same rigour as software products. **Data mesh** (discussed in Lecture 10) is the architectural manifestation of the data-centric organisation: decentralised domain ownership, federated governance, and self-serve data infrastructure.

**The Yggdrasil Data Strategy** (2040) states: "Data is the memory of the University. It must be accurate, accessible, secure, and preserved for future generations." The strategy mandates: open data by default for research outputs (with appropriate privacy safeguards); FAIR principles (Findable, Accessible, Interoperable, Reusable) for all research data; data literacy training for all staff; and a University-wide data catalogue (powered by DataHub) that indexes all datasets, their lineage, and their quality scores.

**Required Reading:**
- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge* (2nd ed., Technics Publications, 2017/2035), ch. 1–3, 7, 12
- Luciano Floridi, *The Ethics of Information* (Oxford, 2013/2035), ch. 14–16
- European Commission, *Ethics Guidelines for Trustworthy AI* (2019/2035)
- Zhamak Dehghani, *Data Mesh* (O'Reilly, 2022/2035), ch. 4–5
- University of Yggdrasil, "The Yggdrasil Data Strategy: Principles, Policies, and Practices" (2040)

**Discussion Questions:**
1. Data governance frameworks are often seen as bureaucratic obstacles to agility. Is governance a genuine enabler of data value, or does it merely slow down innovation?
2. The Nordic Data Compact requires algorithmic transparency for all automated decisions. Is this requirement technically feasible for complex machine learning models, or does it create an impossible standard?
3. Data mesh decentralises ownership but requires federated governance. Is federated governance realistic, or will domains inevitably diverge from shared standards without strong central enforcement?

---

## Final Examination Preparation

The final examination for IT203 is a **practical capstone** (60% of grade) combined with a **written theory exam** (40% of grade).

**Practical Capstone (60%):**
Students design and operate a database infrastructure for a simulated high-traffic web application (a ride-sharing platform with 1 million daily transactions). Requirements:
- Design a PostgreSQL schema for users, drivers, rides, payments, and ratings (3NF, with appropriate indexes).
- Implement streaming replication with one synchronous standby and two asynchronous standbys.
- Configure PgBouncer for connection pooling.
- Implement automated backups (pgBackRest, hourly incremental, daily full, 7-day retention) with PITR capability.
- Load test the database with pgbench and optimise until p95 latency < 10ms for read queries.
- Document all configurations, procedures, and disaster recovery runbooks.

**Written Theory Exam (40%):**
Choose 4 of 8 essay questions:

1. MVCC enables high concurrency but creates table bloat that must be managed by VACUUM. Analyse the trade-offs of MVCC and propose a systematic approach to vacuum tuning.

2. Compare synchronous and asynchronous replication. For a financial application requiring RPO = 0, what architecture would you design, and what are the operational implications?

3. NewSQL databases promise ACID transactions at scale, but they add latency and complexity. For what classes of applications is NewSQL genuinely necessary, and when is PostgreSQL with read replicas sufficient?

4. Describe the modern data stack and its components. What are the advantages of ELT over ETL, and what are the risks?

5. Vector databases are essential for AI-powered search. Will vector search be absorbed into general-purpose databases, or will standalone vector databases remain dominant?

6. Data mesh decentralises data ownership. Is this a realistic model for most organisations, or is it applicable only to large tech companies with mature engineering cultures?

7. Immutable backups protect against ransomware but are expensive. Is the ransomware threat severe enough to mandate immutable backups for all databases?

8. AI-assisted database tuning promises to automate configuration and index design. Can AI genuinely design better databases than experienced DBAs, or does it merely automate the obvious choices?

**Grading:**
- A (Excellent): A fully functional, optimised, and well-documented database infrastructure. Written exam demonstrates deep understanding of database internals, performance tuning, and architectural trade-offs.
- B (Good): A competent infrastructure with minor gaps in performance, replication, or documentation. Written exam is solid but lacks critical depth.
- C (Satisfactory): An infrastructure that meets minimum requirements but has significant gaps. Written exam shows basic understanding but limited analysis.
- D (Poor): A partially functional infrastructure or one with serious security or performance flaws. Written exam is superficial or contains errors.
- F (Fail): No functional infrastructure or missing capstone. Written exam fails to demonstrate understanding of database administration.
