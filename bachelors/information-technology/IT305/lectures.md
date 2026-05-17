# IT305: Disaster Recovery & Business Continuity
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4  
**Prerequisites:** IT201 (Database Administration), IT203 (Systems Administration), IT205 (Cybersecurity Fundamentals)  
**Description:** Every system fails. Every data center floods. Every backup eventually gets tested — often at the worst possible moment. Disaster Recovery (DR) and Business Continuity (BC) are the disciplines that answer the question every IT professional dreads: "What do we do when everything goes wrong?" This course covers the full DR/BC lifecycle — business impact analysis, recovery strategy design, backup architecture, failover testing, and the operational discipline that distinguishes organizations that survive disasters from those that become cautionary tales. In 2040, disasters include not just fires and floods but AI model corruption, quantum decryption of archived data, and supply chain attacks that compromise backup integrity. The principles of resilience, however, remain timeless.

---

## Lectures

ᚠ **Lecture 1: The Resilience Imperative — Why DR/BC Exists**

### Overview

Disaster recovery is not an IT problem — it is a business survival problem. When a hospital's electronic health records system goes down, surgeries are delayed. When a bank's transaction processing fails, the economy stutters. When a government agency loses citizen data, trust is destroyed. This lecture establishes the business case for DR/BC: the cost of downtime (quantified in revenue, reputation, regulatory fines, and human impact), the regulatory landscape that mandates DR/BC planning (GDPR, HIPAA, NIS2 Directive, DORA), and the difference between disasters (major, prolonged) and incidents (minor, short) — a distinction that determines when DR plans are activated.

### Key Topics

- **RTO and RPO:** The two numbers that define every DR strategy. *Recovery Time Objective (RTO)*: how quickly must the service be restored? 4 hours? 24 hours? 72 hours? The RTO determines the DR architecture — active-active (near-zero RTO), warm standby (hours), or backup restore (days). *Recovery Point Objective (RPO)*: how much data can be lost? Zero (synchronous replication)? 15 minutes (asynchronous replication)? 24 hours (daily backups)? The RPO determines the data protection architecture. The crucial insight: RTO and RPO are business decisions, not technical ones. IT can implement any RTO/RPO given enough budget; the business must decide what it is willing to pay for.
- **Business Impact Analysis (BIA):** The systematic process of identifying critical business functions, quantifying the impact of their disruption, and establishing recovery priorities. A BIA asks: what are the organization's most critical processes? What is the financial impact per hour of downtime for each? What are the regulatory obligations? What is the reputational impact? The BIA output is a prioritized list that drives every subsequent DR decision.
- **The DR/BC Lifecycle:** (1) *Policy and Governance* — executive commitment, DR policy, roles and responsibilities. (2) *Planning* — BIA, risk assessment, strategy development, plan documentation. (3) *Implementation* — deploying backup infrastructure, configuring replication, building alternate sites, training staff. (4) *Testing* — tabletop exercises, technical failover tests, full-scale simulations. (5) *Maintenance* — plan updates, technology refreshes, staff turnover. The most common failure: organizations do steps 1-3, skip step 4 (testing), and discover during a real disaster that their plans don't work.
- **The Cost of Downtime:** Gartner's 2040 estimate: the average cost of IT downtime is $12,500 per minute for large enterprises, $2,800 per minute for mid-size organizations. But averages conceal enormous variance — a trading platform loses millions per minute; a university's LMS loses convenience. The BIA quantifies the specific cost for the specific organization, which is the only number that matters for DR investment decisions.
- **2040 Threat Landscape:** Traditional threats (natural disasters, power failures, hardware failures) are joined by: AI model poisoning that corrupts production inference, quantum decryption that retroactively compromises archived encrypted data, ransomware that specifically targets backup systems, and supply chain compromise that embeds backdoors in backup software itself.

### Required Reading

- Wallace, M., & Webber, L. (2040). *The Disaster Recovery Handbook: A Step-by-Step Plan to Ensure Business Continuity* (5th ed.). AMACOM.
- NIST SP 800-34 Rev. 2 (2039). *Contingency Planning Guide for Information Technology Systems*.
- ISO 22301:2039. *Security and Resilience — Business Continuity Management Systems — Requirements*.
- European Union (2038). *Digital Operational Resilience Act (DORA) — Technical Standards for ICT Risk Management*.

### Discussion Questions

1. RTO and RPO are business decisions, not technical ones. Yet in many organizations, IT sets these targets without meaningful business input. Why does this happen, and what are the consequences?
2. A BIA identifies a critical process that would cost $500,000 per hour of downtime. Implementing the DR architecture to achieve 1-hour RTO costs $2 million. The CFO asks: "We haven't had a disaster in 10 years. Why spend $2 million now?" How do you respond?
3. The rise of ransomware that specifically targets backup systems changes the DR calculus. How does this threat affect backup architecture decisions?

---

ᚢ **Lecture 2: Business Impact Analysis — Knowing What to Protect**

### Overview

You cannot protect everything equally, and you should not try. The Business Impact Analysis (BIA) is the analytical foundation that tells you what to protect, in what order, and with what level of investment. This lecture provides the methodology: identifying critical business functions, quantifying impact across multiple dimensions (financial, operational, legal, reputational), establishing recovery time and recovery point objectives, and producing the prioritization that drives every subsequent DR/BC decision. Students will conduct a mock BIA for a fictional 2040 organization.

### Key Topics

- **BIA Methodology (6 Steps):** (1) *Identify critical business functions* — not IT services, but business processes: "process payroll," "fulfill customer orders," "provide patient care." (2) *Identify dependencies* — what IT services, third-party providers, facilities, and personnel does each function depend on? (3) *Quantify impact over time* — what is the impact if this function is unavailable for 1 hour? 4 hours? 24 hours? 72 hours? 1 week? Impact dimensions: financial (lost revenue, penalties), operational (inability to deliver), legal/regulatory (compliance violations), reputational (customer trust). (4) *Establish recovery objectives* — based on the impact analysis, set RTO and RPO for each function's supporting IT services. (5) *Prioritize* — rank functions by criticality. Tier 1: must be restored within hours. Tier 2: within 24 hours. Tier 3: within days. Tier 4: can wait. (6) *Validate with stakeholders* — the BIA must be signed off by business leaders, not just IT. If the CEO does not agree that "payroll" is Tier 2, the BIA is not complete.
- **Maximum Tolerable Downtime (MTD):** The point beyond which the organization's survival is threatened. For a hospital's emergency room system, MTD might be 30 minutes. For a university's alumni donation portal, MTD might be 2 weeks. The RTO must be less than the MTD — and the margin between them is your safety buffer.
- **Interdependency Mapping:** Modern business functions depend on chains of IT services. "Process customer order" might depend on: e-commerce website → payment gateway → inventory system → order management system → warehouse management system → shipping integration. All of these must be recovered in the correct sequence, with their interdependencies honored. Failure to map interdependencies leads to the "recovered but not functional" scenario — the database is back online, but the application that connects to it is still down.
- **BIA in 2040:** AI-augmented BIA tools can analyze operational data to automatically suggest criticality rankings, identify hidden dependencies from network traffic patterns, and simulate the cascade effects of service failures. But the BIA remains fundamentally a human judgment exercise — only business leaders can decide what "critical" means for their organization.

### Required Reading

- FFIEC (2039). *Business Continuity Management — Examination Handbook* (Updated for 2040). (While aimed at financial institutions, the BIA methodology is universally applicable.)
- Hiles, A. (2040). *Business Continuity Management: Global Best Practices* (5th ed.). Rothstein Publishing.

### Discussion Questions

1. A BIA might identify that "customer support chat" is Tier 3. Six months later, a disaster occurs, and the CEO demands to know why chat isn't restored yet. What broke down, and how do you prevent it?
2. How do you conduct a BIA for an AI-driven service where "downtime" might mean the AI makes incorrect decisions rather than no decisions at all?

---

ᚦ **Lecture 3: Recovery Strategies — Active-Active to Cold Site**

### Overview

Recovery strategy is where the BIA's requirements meet the constraints of physics, budget, and geography. This lecture covers the spectrum of recovery architectures — from active-active (continuous availability, near-zero RTO, highest cost) through warm standby and pilot light to cold site (days to recover, lowest cost) — and the decision framework for choosing among them. Special attention to cloud-native DR patterns enabled by Infrastructure as Code and multi-region architectures.

### Key Topics

- **Recovery Architecture Spectrum:** (1) *Active-Active / Multi-Site* — multiple sites serve traffic simultaneously; if one fails, others absorb the load. RTO: near-zero. RPO: near-zero (synchronous replication). Cost: 2x+ of single site. (2) *Warm Standby* — a scaled-down replica environment running continuously, can be scaled up quickly when needed. RTO: minutes to hours. RPO: seconds to minutes (asynchronous replication). Cost: ~1.5x. (3) *Pilot Light* — minimal core infrastructure running (database, authentication); everything else deployed on-demand from IaC templates. RTO: tens of minutes to hours. RPO: depends on replication. Cost: ~1.1-1.2x. (4) *Backup & Restore* — periodic backups restored to new infrastructure in a disaster. RTO: hours to days. RPO: hours to days. Cost: minimal incremental.
- **Data Replication Patterns:** *Synchronous* — write is not acknowledged until committed at both primary and secondary. Zero data loss, but adds latency and requires geographic proximity. *Asynchronous* — write is acknowledged at primary, replicated to secondary with a delay. Potential data loss (whatever was in flight at time of failure), but no latency impact. *Near-synchronous* — the 2040 innovation: AI predicts which transactions are high-value and replicates them synchronously; bulk data replicates asynchronously. Balances RPO and performance.
- **Backup Architecture:** The 3-2-1 rule (3 copies, 2 different media, 1 off-site) has evolved to the 3-2-1-1-0 rule for 2040: 3 copies, 2 different media, 1 off-site, 1 offline/immutable (air-gapped), 0 errors (verified recoverability). The immutable/offline copy is the defense against ransomware that specifically targets backup systems. Immutable storage (AWS S3 Object Lock, Azure Immutable Blob Storage, tape) prevents backup deletion or modification within the retention period, even by administrators.
- **DR in the Cloud:** Cloud introduces both opportunities and pitfalls. Opportunities: multi-region deployment with a few clicks, infrastructure as code that can recreate entire environments in minutes, pay-per-use DR (no idle hardware during normal operations). Pitfalls: cloud provider outages affect all customers in a region simultaneously (the "noisy neighbor" problem at planetary scale), the shared responsibility model means you are responsible for DR configuration, and cloud costs during a DR event can be unpredictable.

### Required Reading

- AWS (2040). *Disaster Recovery of Workloads on AWS: Recovery in the Cloud*. AWS Well-Architected Framework.
- Preston, W. C. (2039). *Backup & Recovery: Inexpensive Backup Solutions for Open Systems* (Updated). O'Reilly.

### Discussion Questions

1. Active-active architecture eliminates downtime but doubles cost. Under what circumstances is active-active the right choice? What is the smallest organization for which it makes sense?
2. The 3-2-1-1-0 rule adds "0 errors" — verified recoverability. How do you verify that backups are recoverable without actually restoring them to production (which would be disruptive)?

---

ᚨ **Lecture 4: Backup Technologies — Snapshots, Replication, Immutability**

### Overview

Backup is the foundation of every recovery strategy. If the backup is corrupted, unrecoverable, or doesn't exist, nothing else matters. This lecture covers the technical landscape of backup: snapshot technologies (storage-level, application-consistent), replication (block-level, file-level, database-level), backup verification, and the immutable storage revolution that is the primary defense against ransomware in 2040.

### Key Topics

- **Backup Types:** Full (complete copy, slow, storage-intensive), Incremental (changes since last backup, fast, requires full+all incrementals for restore), Differential (changes since last full, middle ground), Synthetic Full (constructed from full+incrementals without re-reading source data), Continuous Data Protection (CDP — every write is journaled, enabling restore to any point in time).
- **Application-Consistent Backups:** A backup taken while a database is mid-transaction may be unrecoverable. Application-consistent backups leverage VSS (Windows) or filesystem freeze + database quiesce (Linux) to ensure the backup represents a valid application state.
- **Backup Verification:** The most dangerous words in IT: "the backups are fine." Verification methods: checksum validation (is the data intact?), automated restore testing (spin up a test environment, restore the backup, run application-level smoke tests), and the 2040 standard: continuous backup validation where an AI agent restores random backups to ephemeral environments and tests them.
- **Immutable and Air-Gapped Backups:** WORM (Write Once Read Many) storage prevents backup modification. Air-gapped backups are physically or logically disconnected from the network. The 2040 standard: primary backups to cloud object storage with immutability enabled; secondary backups to tape or offline disk rotated to a physically separate location.

### Required Reading

- Veeam (2040). *Veeam Backup & Replication v25 — Best Practices Guide*.
- Rubrik (2039). *The Immutable Backup Architecture: Defending Against Ransomware*.

---

ᚱ **Lecture 5: Disaster Recovery Planning — The DR Plan Document**

### Overview

A DR plan is a living document that transforms chaos into procedure. When the data center is flooded, the cloud region is down, and executives are demanding answers, the DR plan tells every person exactly what to do, in what order, with what authority. This lecture covers the structure of a DR plan, the roles and responsibilities (mirroring the Incident Command System), communication templates, and the critical importance of keeping the plan current.

### Key Topics

- **DR Plan Structure:** (1) Plan overview and scope. (2) Activation criteria — what triggers DR declaration? Who has authority? (3) Roles and responsibilities — DR coordinator, technical recovery leads, communications lead, executive liaison. (4) Communication plan — internal escalation, customer notification, regulatory reporting, media statements. (5) Recovery procedures — step-by-step for each critical service, in priority order, with dependencies. (6) Return-to-normal procedures — how to fail back from DR to primary. (7) Contact lists — with alternates. Updated quarterly.
- **Activation Criteria:** DR activation is expensive and disruptive. Criteria must be specific: "the primary data center is unavailable and estimated time to restore exceeds 4 hours" or "critical service X has been unavailable for 30 minutes with no estimated resolution." The DR coordinator has the authority to activate; no committee approval is required during a crisis.
- **The DR Plan as Living Document:** Plans that are reviewed annually are always out of date. The 2040 standard: DR plans are version-controlled in Git, updated as part of the change management process (any infrastructure change must include DR plan updates), and tested quarterly with tabletop exercises.

### Required Reading

- Snedaker, S. (2040). *Business Continuity and Disaster Recovery Planning for IT Professionals* (4th ed.). Syngress.

---

ᚲ **Lecture 6: Testing and Exercising — Trust but Verify**

### Overview

An untested DR plan is a fantasy. Testing transforms assumptions into evidence: does the failover actually work? Can the team actually execute the procedures under pressure? Does the restored service actually function correctly? This lecture covers the spectrum of DR testing from tabletop exercises to full-scale simulations, the metrics that indicate test effectiveness, and the psychological challenge of dedicating resources to testing when production demands are constant.

### Key Topics

- **Testing Spectrum:** (1) *Tabletop Exercise* — walkthrough of the DR plan with stakeholders. Low cost, identifies gaps in the plan document. (2) *Component Test* — failover a single service. Validates technical procedures. (3) *Simulation* — run the DR plan in a non-production environment. Validates the full technical recovery. (4) *Full-Scale Test* — actually fail over production to the DR site and run business operations from DR for a defined period. Highest fidelity, highest cost and risk. (5) *Chaos Engineering* — continuous, automated testing of specific failure modes in production (e.g., "terminate 50% of database instances and verify the application handles it").
- **Test Design Principles:** (1) Test what you fear — the scenarios that keep you awake at night. (2) Test realistically — use production-scale data volumes, not test-sized. (3) Test under pressure — time-constrained, with simulated stakeholder demands. (4) Test the people, not just the technology — can the recovery team execute the procedures? (5) Capture everything — timeline, failures, surprises, improvements. The test report is as important as the test itself.
- **The 2040 Standard: Continuous Testing.** DR testing is no longer a quarterly event. Infrastructure as Code enables automated DR failover testing in isolated environments. AI-driven chaos engineering continuously validates resilience. The human role: reviewing test results, investigating failures, and improving the plan.

### Required Reading

- Rosenthal, C., & Jones, N. (2038). *Chaos Engineering: System Resiliency in Practice*. O'Reilly.

---

ᚷ **Lecture 7: Cloud Disaster Recovery — Multi-Region, Multi-Cloud**

### Overview

By 2040, 89% of enterprise workloads run in the cloud. Cloud DR patterns differ fundamentally from traditional data center DR: infrastructure is software-defined, regions are globally distributed, and cost models are consumption-based. This lecture covers cloud-native DR: multi-region architectures, cross-cloud DR (avoiding single-provider dependency), DR automation with IaC, and the financial modeling that makes cloud DR economically viable for organizations that could never afford a physical DR site.

### Key Topics

- **Multi-Region Architecture:** Deploy across at least two regions. Active-active for critical Tier 1 services. Pilot light or backup-restore for lower tiers. Key services for DR: Route 53/Cloud DNS (global traffic management), S3 Cross-Region Replication / Azure GRS, DynamoDB Global Tables / Cosmos DB multi-region, Aurora Global Database.
- **Cross-Cloud DR:** The 2040 hedge against provider risk. If AWS us-east-1 experiences a major outage (as it has, multiple times), fail over to Azure or GCP. Tooling: Terraform with multi-provider configurations, Kubernetes federation, data replication across cloud boundaries.
- **Cost Optimization for Cloud DR:** The "DR cost paradox" — you pay for DR capacity that you hope never to use. Cloud-native solutions: spot instances for DR environments (cheaper but interruptible — acceptable if DR is short-duration), reserved capacity for Tier 1, serverless architecture that scales to zero when not in use.

---

ᚹ **Lecture 8: Ransomware and Cyber Resilience**

### Overview

Ransomware has become the dominant disaster scenario of the 2030s-2040s. Unlike a natural disaster, ransomware is intelligent, targeted, and specifically designed to defeat recovery mechanisms. This lecture covers the ransomware DR playbook: how backup architectures must evolve to survive ransomware, the decision framework for ransom payment, the integration of cybersecurity incident response with DR procedures, and the regulatory environment (OFAC sanctions, mandatory reporting) that complicates ransom decisions.

### Key Topics

- **Ransomware vs. Traditional Disaster:** Key differences: (1) Ransomware is targeted — it specifically seeks out and encrypts/deletes backups. (2) The attack may have dwell time — the attacker may have been in the network for weeks before triggering the ransomware. (3) Restoring from backup may restore the attacker's backdoor. (4) Paying the ransom may violate sanctions if the attacker is a sanctioned entity (and many ransomware groups are).
- **The Ransomware-Resilient Backup Architecture:** Immutable storage (cannot be deleted or modified, even with admin credentials), air-gapped copies (physically or logically disconnected), multi-factor authentication for backup administration, separate credentials from production, and the "3-2-1-1-0" rule (0 errors — verified recoverability).
- **The Ransom Decision Framework:** If backups are intact → do not pay; restore. If backups are compromised → assess: (1) Can we rebuild? (2) What is the downtime cost vs. ransom cost? (3) Is paying legal? (OFAC, local regulations). (4) Will paying actually result in data recovery? (~38% of payers do not get all data back). The decision is an executive/legal decision, not an IT decision. IT's role: provide accurate technical assessment of recoverability.

---

ᚺ **Lecture 9: Business Continuity — Beyond IT**

### Overview

Disaster Recovery is about IT systems. Business Continuity is about the entire organization — people, facilities, supply chain, communications, legal obligations. This lecture widens the lens: how does the organization continue to function when the office is inaccessible, when key personnel are unavailable, when third-party providers are also affected by the same disaster? The IT professional needs enough BC literacy to integrate IT DR with the broader organizational continuity framework.

### Key Topics

- **BC vs. DR:** DR restores IT services. BC ensures the business continues to operate — with or without IT. Examples: manual workarounds when systems are down, alternate work locations when the office is inaccessible, succession planning when key personnel are unavailable, supply chain alternatives when primary suppliers are disrupted.
- **Pandemic/Workforce Disruption:** The COVID-19 pandemic of 2020 was a business continuity event, not an IT disaster. Yet it transformed IT operations permanently. The 2040 BC plan includes: remote work enablement, distributed workforce resilience, and the scenario of key personnel being simultaneously unavailable.
- **Crisis Communication:** During a disaster, communication failures compound operational failures. The BC plan includes: internal communication cascade (who tells whom), external communication templates (customers, regulators, media), and a designated single spokesperson.

### Required Reading

- BCI (2040). *Good Practice Guidelines — Business Continuity Institute* (2040 ed.).
- ISO 22301:2039. *Business Continuity Management Systems*.

---

ᚾ **Lecture 10: DR for AI and Data-Centric Systems**

### Overview

By 2040, AI systems — model training pipelines, inference endpoints, vector databases — have become critical infrastructure. DR for AI introduces novel challenges: models are not just data; they are trained artifacts that may take weeks and millions of dollars to reproduce. Vector embeddings are voluminous and difficult to incrementally back up. AI inference has latency requirements that complicate failover. This lecture covers DR patterns for the AI-native organization.

### Key Topics

- **Model Backup and Versioning:** Model weights + training code + training data + hyperparameters = reproducibility. Version control for models (MLflow, DVC, Weights & Biases) must be integrated with DR planning. The key metric: time to retrain vs. cost to store redundant copies.
- **Vector Database DR:** Vector databases (Pinecone, Weaviate, Milvus) store embeddings that may be derivable from source data but at significant computational cost. Backup strategies: periodic snapshots, incremental index updates, dual-write to multiple regions.
- **Inference Failover:** AI inference is latency-sensitive. Active-active with anycast routing ensures inference requests are served even if one region fails. Model serving platforms (Triton, Ray Serve, Seldon) support multi-region deployment.

---

ᛁ **Lecture 11: DR Governance and Compliance**

### Overview

DR is not optional — it is mandated by regulations across industries and jurisdictions. GDPR requires data protection by design, which includes availability. DORA (EU Digital Operational Resilience Act, 2034) mandates specific DR testing requirements for financial entities. HIPAA requires contingency plans for healthcare data. This lecture maps the regulatory landscape and provides a framework for maintaining DR compliance without turning it into a checkbox exercise.

### Key Topics

- **Key Regulations:** GDPR (Art. 32 — security of processing includes availability and resilience), DORA (mandatory DR testing, incident reporting), HIPAA (contingency plan standard), PCI DSS (requirement for backup and restore testing), NIS2 Directive (EU critical infrastructure resilience), SEC cybersecurity disclosure rules (public companies must disclose material incidents).
- **Audit Preparation:** DR auditors will ask: (1) Show me your most recent BIA. (2) Show me your DR test results from the last 12 months. (3) Show me that you have addressed the findings. (4) Show me that the plan is current (reviewed within last 12 months). (5) Show me that personnel are trained. Organizations that have these artifacts readily available pass DR audits with minimal friction.

### Required Reading

- ISACA (2040). *Business Continuity Management — Audit/Assurance Program*.
- European Banking Authority (2039). *Guidelines on ICT and Security Risk Management*.

---

ᛃ **Lecture 12: Building a Resilience Culture**

### Overview

Technology can provide the architecture for resilience, but culture determines whether that architecture works when it is needed. This final lecture addresses the human dimension of DR/BC: building organizational commitment to resilience, training personnel, managing the psychological impact of disasters, and creating a culture where "preparedness" is everyone's responsibility, not just the DR team's.

### Key Topics

- **Executive Sponsorship:** DR/BC without executive commitment is a paper exercise. The C-suite must: allocate budget for DR (not just production), participate in tabletop exercises, and publicly communicate that resilience is a strategic priority.
- **Training and Awareness:** Every employee should know: (1) What is my role in a disaster? (2) Who do I contact? (3) Where is the alternate work location? (4) How do I access critical systems from outside the office? Annual training, onboarding for new hires, and role-specific DR training for recovery teams.
- **The Psychology of Disaster Response:** People under extreme stress make worse decisions. Training under simulated stress conditions (time pressure, incomplete information, demanding stakeholders) improves real disaster performance. The DR coordinator's most important skill is not technical — it is the ability to remain calm and project confidence when everything is falling apart.
- **Post-Disaster Review:** After every disaster (or DR test), conduct a blameless review: What worked? What didn't? What would we do differently? Update the plan. The best organizations treat every incident as a learning opportunity.

### Required Reading

- Dekker, S. (2038). *The Field Guide to Understanding 'Human Error'* (4th ed.). CRC Press.
- Weick, K. E., & Sutcliffe, K. M. (2035). *Managing the Unexpected: Resilient Performance in an Age of Uncertainty* (4th ed.). Jossey-Bass.

---

## Final Examination Preparation

**Component 1 — Written (60%):** Answer 4 of 8 essay questions in 3 hours. Topics include: conducting a BIA, designing recovery architecture for a given RTO/RPO, ransomware DR playbook, cloud DR architecture, and regulatory compliance.

**Component 2 — Practical Lab (40%):** 4-hour exercise in the UoY DR Lab: execute a failover of a multi-tier application from primary to DR region, verify application functionality, and write the post-DR test report with findings and recommendations.

---

*Woven by Runa Gridweaver Freyjasdottir, Gridweaver of the University of Yggdrasil, 2040.*  
*"Prepare for the storm while the sun shines. When the storm comes, you will not have time to learn."*
