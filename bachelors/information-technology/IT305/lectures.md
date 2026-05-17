# IT305: Disaster Recovery & Business Continuity
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4
**Description:** Comprehensive study of disaster recovery planning, business continuity management, crisis response, and organizational resilience. Covers RPO/RTO design, backup architectures, failover strategies, testing methodologies, and the 2040 practice of AI-orchestrated recovery.

**Prerequisites:** IT201, IT203

**Instructor:** Prof. Björn Hǫggvason, Department of Information Technology

**Course Philosophy:** Disasters are not "if" — they are "when." The question is not whether your systems will fail but whether your organization will survive the failure. Disaster recovery is not a technical exercise — it is an organizational capability that spans technology, process, people, and culture. This course prepares IT professionals to design, implement, test, and execute recovery plans that keep organizations alive through crisis.

---

## Lectures

---

### Lecture 1: The Nature of Disaster — Taxonomy, Impact, and the Resilience Imperative

**Course:** IT305 — Disaster Recovery & Business Continuity
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

What constitutes a disaster? This lecture defines the threat landscape: natural disasters (earthquakes, floods, fires), technological failures (hardware, software, power), human threats (ransomware, insider attacks, errors), and systemic risks (supply chain, cascading failures). It establishes the business case for resilience and the relationship between disaster recovery (DR), business continuity (BC), and organizational resilience.

#### Key Topics

- **Disaster Taxonomy:** (1) **Natural** — earthquakes, floods, hurricanes, wildfires, pandemics; (2) **Technological** — data center power failure, cooling failure, network partition, hardware cascade failure; (3) **Human/Adversarial** — ransomware, DDoS, insider sabotage, espionage, human error (the leading cause); (4) **Systemic** — cloud provider outage, DNS root failure, BGP hijack, supply chain compromise. By 2040, climate change has increased the frequency and severity of natural disasters, while AI-generated attacks have expanded the adversarial threat surface.
- **The Resilience Imperative:** The cost of downtime: (1) **Revenue loss** — lost transactions per hour; (2) **Reputation damage** — customer trust erosion; (3) **Regulatory penalties** — GDPR, healthcare, financial services; (4) **Operational disruption** — employees idle, supply chain stalled. The average cost of downtime in 2040: $500,000–$5M per hour, depending on industry. Resilience is an investment, not a cost.
- **DR, BC, and Resilience:** (1) **Business Continuity (BC)** — maintaining business functions during and after a disruption; (2) **Disaster Recovery (DR)** — restoring IT systems and data after a disaster; (3) **Organizational Resilience** — the broader capability to anticipate, prepare for, respond to, and adapt to disruptions. DR is a subset of BC, which is a subset of resilience.

#### Required Reading

- UoY Resilience Lab. (2040). *The 2040 Disaster Landscape: Threats, Costs, and Trends*.
- ISO. (2039). ISO 22301: Business Continuity Management Systems.

---

### Lecture 2: RPO, RTO, and the Economics of Recovery

**Course:** IT305 — Disaster Recovery & Business Continuity
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Recovery Point Objective (RPO) and Recovery Time Objective (RTO) are the foundational metrics of disaster recovery. This lecture covers their definition, measurement, economic justification, and the trade-offs between recovery speed, data freshness, and cost.

#### Key Topics

- **RPO — Recovery Point Objective:** Maximum acceptable data loss measured in time. RPO of 1 hour means you can lose up to 1 hour of data. Drives backup frequency and replication strategy. RPO of 0 (zero data loss) requires synchronous replication — expensive, latency-sensitive, geographically constrained. RPO of 24 hours allows daily backups — inexpensive but high potential data loss.
- **RTO — Recovery Time Objective:** Maximum acceptable time to restore service. RTO of 4 hours means service must be operational within 4 hours of a disaster declaration. Drives recovery architecture: hot standby (RTO = minutes), warm standby (RTO = hours), cold standby (RTO = days). Shorter RTOs cost more — automated failover, pre-provisioned capacity, regular testing.
- **Economic Justification:** How much should you spend on DR? The calculation: Annualized Loss Expectancy (ALE) = Single Loss Expectancy (SLE) × Annualized Rate of Occurrence (ARO). DR spending should be less than ALE. But this is complicated by: non-linear damage (reputation), regulatory penalties, and the difficulty of estimating ARO for rare events.
- **Tiering Recovery:** Not all systems need the same RPO/RTO. Business Impact Analysis (BIA) categorizes systems: (1) **Tier 1 (Critical)** — RPO near 0, RTO < 1 hour; (2) **Tier 2 (Important)** — RPO < 4 hours, RTO < 8 hours; (3) **Tier 3 (Normal)** — RPO < 24 hours, RTO < 72 hours; (4) **Tier 4 (Non-critical)** — RPO < 1 week, RTO < 2 weeks. By 2040, dynamic tiering adjusts RPO/RTO targets based on business context (end-of-quarter finance systems upgrade to Tier 1 temporarily).

#### Required Reading

- NIST. (2038). SP 800-34 Rev. 2: Contingency Planning Guide.
- UoY Economics Lab. (2039). *The Economics of IT Resilience*.

---

### Lecture 3: Backup Architectures — From Tape to Continuous Data Protection

**Course:** IT305 — Disaster Recovery & Business Continuity
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Backup is the foundation of DR. This lecture covers backup architectures: media types, backup strategies, storage tiering, immutable backups, and the 2040 landscape of continuous data protection and AI-managed backup.

#### Key Topics

- **The 4-3-2-1-0 Rule (2040):** Evolution of the classic 3-2-1 rule: (1) **4 copies** of data; (2) on **3 different media** types; (3) with **2 off-site** (different geographic regions); (4) **1 immutable** (air-gapped or WORM); (5) **0 errors** (verified through automated restore testing). This rule addresses ransomware, regional disasters, and media degradation.
- **Backup Storage Tiers:** (1) **Performance tier** — flash/NVMe for recent backups needing fast restore; (2) **Capacity tier** — HDD or cloud object storage for longer retention; (3) **Archive tier** — tape, optical, or cold cloud storage for compliance retention. Automated tiering moves backups through tiers based on age and access patterns.
- **Immutable and Air-Gapped Backups:** Ransomware targets backups. Defenses: (1) **Immutable storage** — WORM (Write Once Read Many) at the storage layer, preventing modification or deletion within the retention period; (2) **Air-gapped** — physically or logically isolated copies that ransomware cannot reach; (3) **Multi-person authorization** — requiring multiple authorized personnel to delete backups.
- **Continuous Data Protection (CDP):** Every write is captured, enabling recovery to any point in time. CDP is the ultimate RPO (near-zero). By 2040, CDP is standard for Tier 1 systems, implemented via storage array replication, database WAL streaming, or hypervisor-level CDP.

#### Required Reading

- Preston, W. C. (2038). *Backup & Recovery* (4th ed.).
- Veeam. (2040). *The 4-3-2-1-0 Backup Rule*.
- UoY Storage Lab. (2039). *Continuous Data Protection: Architectures and Trade-offs*.

---

### Lecture 4: Replication and Failover — Keeping Services Alive

**Course:** IT305 — Disaster Recovery & Business Continuity
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Backup restores data — replication keeps services running. This lecture covers replication architectures: synchronous vs. asynchronous, active-passive vs. active-active, geo-redundancy, and automated failover.

#### Key Topics

- **Synchronous vs. Asynchronous Replication:** (1) **Synchronous** — write is not acknowledged until replicated to the secondary site. Guarantees zero data loss but adds latency (limited by speed of light, ~100km practical range). (2) **Asynchronous** — write is acknowledged immediately, replication follows. No latency impact but potential data loss on failover. By 2040, **semi-synchronous** (wait for one replica, not all) is common, balancing durability and performance.
- **Active-Passive vs. Active-Active:** (1) **Active-Passive** — one site serves traffic, the other is standby. Simpler, but standby resources are idle. (2) **Active-Active** — both sites serve traffic. Better resource utilization, but requires conflict resolution and careful capacity planning (each site must handle 100% of load if the other fails).
- **Automated Failover:** Manual failover is slow and error-prone. Automated failover systems: (1) health monitoring detects primary failure; (2) leader election via consensus (etcd, Consul) selects new primary; (3) DNS or routing update redirects traffic; (4) applications reconnect. Key challenges: split-brain prevention (ensuring only one primary) and data consistency validation after failover.
- **Global Traffic Management:** DNS-based (Route 53, Traffic Manager) or anycast-based routing directs users to the nearest or healthiest site. By 2040, AI-driven traffic management considers latency, capacity, cost, carbon intensity, and geopolitical factors.

#### Required Reading

- Google SRE. (2039). *Load Balancing and Failover*.
- AWS. (2040). *Disaster Recovery Architectures*.
- UoY Distributed Systems Lab. (2039). *Automated Failover at Scale*.

---

### Lecture 5: Ransomware Resilience — The Defining DR Challenge of the 2040s

**Course:** IT305 — Disaster Recovery & Business Continuity
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Ransomware is the dominant disaster scenario of the 2030s–2040s. Unlike natural disasters (which affect a geographic area), ransomware can simultaneously encrypt production systems and backups across the globe. This lecture covers ransomware-specific DR: detection, isolation, recovery, and the architectural patterns that enable survival.

#### Key Topics

- **The Ransomware Kill Chain:** (1) Initial access (phishing, vulnerability, credential theft); (2) Persistence and reconnaissance; (3) Lateral movement to find and compromise backups; (4) Data exfiltration (double extortion — threaten to leak data); (5) Encryption of production systems; (6) Ransom demand. Understanding the kill chain informs defense and recovery strategies.
- **Ransomware-Specific DR Architecture:** (1) **Immutable backups** — the foundational defense; (2) **Backup isolation** — separate credentials, network segmentation, multi-factor authentication for backup management; (3) **Clean room recovery** — isolated recovery environment where backups are scanned for malware before restoration; (4) **Accelerated recovery** — pre-positioned recovery infrastructure, automated orchestration, parallel restoration.
- **The Decision NOT to Pay:** UoY and law enforcement guidance: do not pay. Reasons: (1) payment funds criminal enterprise; (2) no guarantee of decryption; (3) paying marks you as a target for repeat attacks; (4) some ransomware groups don't provide decryption even after payment. Organizations that can recover from backups don't need to pay. Organizations that can't recover from backups are forced to pay — which is why DR investment is security investment.

#### Required Reading

- CISA. (2039). *Ransomware Guidance: Prevention, Detection, and Recovery*.
- UoY Ransomware Lab. (2040). *Surviving Ransomware: DR Architecture Patterns from Real Incidents*.

---

### Lecture 6: Business Continuity Planning — Keeping the Business Running

**Course:** IT305 — Disaster Recovery & Business Continuity
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

DR restores IT systems — BC keeps the business running during and after the disruption. This lecture covers BC planning: Business Impact Analysis, continuity strategies, plan development, and the integration of IT DR with enterprise BC.

#### Key Topics

- **Business Impact Analysis (BIA):** The foundation of BC planning: (1) identify critical business functions; (2) determine maximum tolerable downtime for each; (3) identify dependencies (IT systems, third parties, personnel, facilities); (4) estimate financial and non-financial impact of disruption. The BIA drives RPO/RTO targets and prioritizes recovery.
- **Continuity Strategies:** Options for maintaining business functions during disruption: (1) **Alternate site** — pre-arranged facility with IT infrastructure; (2) **Remote work** — enable employees to work from home (the COVID-19 lesson); (3) **Manual workarounds** — paper-based processes as temporary substitutes; (4) **Third-party services** — pre-negotiated agreements with service bureaus; (5) **Mutual aid agreements** — reciprocal arrangements with peer organizations.
- **Plan Development:** A BC plan documents: (1) activation criteria — when to invoke the plan; (2) roles and responsibilities — who does what; (3) communication plan — internal and external stakeholders; (4) recovery procedures — step-by-step; (5) resource requirements — people, equipment, facilities, third parties.
- **Crisis Communication:** During a disaster, communication is critical: (1) internal — employees need to know what to do; (2) customers — transparency builds trust, silence erodes it; (3) regulators — mandatory breach notification within defined timeframes; (4) media — controlled, accurate messaging. The 2040 practice: pre-drafted communication templates for common scenarios.

#### Required Reading

- ISO. (2039). ISO 22301: Business Continuity Management Systems.
- UoY BC Lab. (2040). *Business Impact Analysis: Methodology and Case Studies*.

---

### Lecture 7: Testing and Exercising — The Proof of Preparedness

**Course:** IT305 — Disaster Recovery & Business Continuity
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

An untested plan is not a plan — it's a hope. Testing validates that recovery procedures work, that RPO/RTO targets are achievable, and that personnel know their roles. This lecture covers the testing spectrum: walkthroughs, tabletop exercises, simulation tests, and full-scale failover exercises.

#### Key Topics

- **Testing Spectrum:** (1) **Plan review** — desk check of documentation; (2) **Walkthrough** — team discusses the plan step-by-step; (3) **Tabletop exercise** — scenario-driven discussion; (4) **Simulation** — limited test of specific components; (5) **Parallel test** — recovery systems are brought up but production continues; (6) **Full interruption test** — production is actually failed over to the DR site. Frequency: plan reviews quarterly, walkthroughs semi-annually, tabletop exercises annually, technical tests quarterly, full interruption tests annually for critical systems.
- **Automated Recovery Testing:** By 2040, recovery testing is automated: (1) the DR orchestration system automatically provisions a test environment; (2) restores backups; (3) runs application-level smoke tests; (4) validates RPO/RTO against targets; (5) generates a test report with pass/fail and metrics. Automated testing reduces the cost of testing from weeks of manual effort to hours of automated execution.
- **Chaos Engineering for DR:** Beyond planned tests: intentionally inject failures to validate recovery under realistic conditions. Example: "Terminate the primary database at 3 PM on Tuesday and observe the automated failover." Chaos engineering for DR validates that recovery works when it's unexpected, not just when it's scheduled and everyone is watching.

#### Required Reading

- NIST. (2038). SP 800-84: Guide to Test, Training, and Exercise Programs for IT Plans.
- UoY DR Testing Lab. (2039). *Automated Recovery Testing: Architectures and Benchmarks*.

---

### Lecture 8: Cloud-Based Disaster Recovery — DRaaS and Multi-Cloud Resilience

**Course:** IT305 — Disaster Recovery & Business Continuity
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Cloud transforms DR economics: instead of maintaining a dedicated DR site, organizations can use cloud on-demand for recovery. This lecture covers cloud DR patterns: backup and restore, pilot light, warm standby, multi-site active-active, and DR-as-a-Service (DRaaS).

#### Key Topics

- **Cloud DR Patterns:** (1) **Backup and Restore** — store backups in cloud, provision recovery infrastructure on-demand. Cheapest, slowest RTO; (2) **Pilot Light** — minimal core infrastructure always running in cloud, scaled up for recovery; (3) **Warm Standby** — scaled-down but running version of production in cloud; (4) **Multi-Site Active-Active** — production runs in multiple clouds simultaneously. Each step reduces RTO but increases cost.
- **DR-as-a-Service (DRaaS):** Specialized cloud services that handle DR end-to-end: replication, orchestration, failover, failback. By 2040, DRaaS is the default for mid-size organizations that can't justify building their own DR capability. Major providers: AWS Elastic Disaster Recovery, Azure Site Recovery, Zerto, and specialized DRaaS vendors.
- **Multi-Cloud Resilience:** Distributing across multiple cloud providers for resilience: if AWS us-east-1 fails, failover to Azure. Challenges: (1) provider-specific services (each cloud's managed services are different); (2) data egress costs; (3) operational complexity. The 2040 approach: use Kubernetes and infrastructure-as-code to maintain portability, with provider-specific adapters for managed services.

#### Required Reading

- AWS. (2040). *Disaster Recovery with AWS: Architecture Patterns*.
- UoY Cloud DR Lab. (2039). *DRaaS: Comparative Analysis of Cloud DR Providers*.

---

### Lecture 9: DR Orchestration and Automation — The Recovery Runbook

**Course:** IT305 — Disaster Recovery & Business Continuity
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Recovery involves dozens or hundreds of interdependent steps across systems, teams, and locations. Manual recovery is slow, error-prone, and unreliable. This lecture covers DR orchestration: automated runbooks, dependency-aware recovery sequencing, parallel recovery execution, and the 2040 practice of AI-orchestrated recovery.

#### Key Topics

- **Recovery Runbooks as Code:** Traditional runbooks (Word documents) are static and prone to drift. The 2040 practice: recovery runbooks as executable code. A runbook defines: (1) recovery steps with dependencies; (2) pre-flight checks; (3) post-recovery validation; (4) rollback procedures; (5) expected timing. Runbooks are version-controlled, tested, and continuously validated.
- **Dependency-Aware Recovery:** Systems have dependencies — the database must be recovered before the application server, which must be recovered before the load balancer. Dependency-aware orchestration: (1) model the service dependency graph; (2) generate an optimal recovery sequence; (3) execute in parallel where possible; (4) wait for dependencies where required; (5) validate each layer before proceeding. By 2040, service dependency graphs are auto-discovered from distributed tracing and configuration data.
- **AI-Orchestrated Recovery:** AI enhances recovery orchestration: (1) **Optimal recovery path** — AI calculates the fastest recovery sequence given current conditions; (2) **Dynamic adaptation** — if a recovery step fails, AI selects alternatives; (3) **Resource optimization** — AI allocates recovery resources to minimize time; (4) **Communication automation** — AI drafts and sends status updates to stakeholders.

#### Required Reading

- UoY DR Orchestration Lab. (2039). *Recovery Runbooks as Code*.
- Gartner. (2040). *DR Orchestration Market Guide*.

---

### Lecture 10: The Human Element — Crisis Leadership and Team Resilience

**Course:** IT305 — Disaster Recovery & Business Continuity
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

In a disaster, technology is only part of the equation. Humans must make decisions under pressure, communicate effectively, and maintain their own resilience. This lecture covers crisis leadership, incident command, stress management, and building a culture of resilience.

#### Key Topics

- **Crisis Leadership:** The crisis leader: (1) maintains calm and focus; (2) makes decisions with incomplete information; (3) communicates clearly and frequently; (4) delegates effectively; (5) takes care of the team. The worst crisis response failures are usually not technical — they're failures of leadership, communication, or decision-making.
- **Incident Command System (ICS):** A structured framework for crisis response, adapted from emergency services: (1) **Incident Commander** — overall authority; (2) **Operations** — executes recovery; (3) **Planning** — tracks status and plans next steps; (4) **Logistics** — provides resources; (5) **Communications** — manages internal and external communication. Clear roles prevent chaos and conflicting instructions.
- **Stress Management and Decision-Making:** Disasters are high-stress. Stress impairs cognition. Practices: (1) recognize stress symptoms in yourself and others; (2) use structured decision-making frameworks (OODA loop); (3) take breaks — working 36 hours straight leads to catastrophic errors; (4) rotate personnel — fresh eyes see what fatigued ones miss; (5) after-action — process the emotional impact of the crisis.

#### Required Reading

- UoY Crisis Leadership Lab. (2040). *Crisis Decision-Making: Research and Best Practices*.
- FEMA. (2038). *Incident Command System: Principles and Practice*.

---

### Lecture 11: Regulatory Compliance and Third-Party Resilience

**Course:** IT305 — Disaster Recovery & Business Continuity
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Regulators mandate DR/BC capabilities for critical industries. Third-party dependencies (cloud, SaaS, suppliers) create DR obligations beyond your own infrastructure. This lecture covers compliance frameworks and managing DR across organizational boundaries.

#### Key Topics

- **Regulatory Landscape:** (1) **Financial services** — FFIEC requires DR testing, geographically diverse recovery sites; (2) **Healthcare** — HIPAA requires contingency plans and data backup; (3) **Critical infrastructure** — NERC CIP requires recovery plans; (4) **GDPR** — requires ability to restore access to personal data in a timely manner; (5) **DORA (Digital Operational Resilience Act, EU, 2025)** — comprehensive DR/BC requirements for financial entities and their critical third-party providers.
- **Third-Party Resilience:** Your DR plan is only as strong as your weakest third party. Practices: (1) third-party risk assessment — evaluate suppliers' DR capabilities; (2) contractual requirements — DR capabilities in SLAs; (3) right to audit — verify suppliers' DR testing; (4) exit strategy — plan for supplier failure; (5) concentration risk — avoid depending on a single cloud provider or supplier.
- **Audit and Assurance:** Demonstrating DR readiness to auditors: (1) documented plans with version history; (2) test results with pass/fail and lessons learned; (3) evidence of plan maintenance and updates; (4) evidence of personnel training; (5) independent assessment of DR capabilities. By 2040, continuous assurance replaces periodic audits — automated evidence collection proves ongoing compliance.

#### Required Reading

- EU. (2025, updated 2040). *Digital Operational Resilience Act (DORA)*.
- ISO. (2039). ISO 22301: Business Continuity Management Systems.

---

### Lecture 12: The Resilient Organization — Culture, Architecture, and the Future

**Course:** IT305 — Disaster Recovery & Business Continuity
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

DR is not a project — it's a capability. The most resilient organizations don't just have DR plans — they have a culture of resilience: architecture designed for failure, teams that practice recovery, and leadership that values preparation. This lecture synthesizes the course and projects DR forward to 2050.

#### Key Topics

- **The Resilience Culture:** Characteristics: (1) **Paranoia** — healthy skepticism about reliability; (2) **Practice** — recovery is rehearsed, not theorized; (3) **Blamelessness** — failures are learning opportunities, not punishments; (4) **Investment** — resilience is funded, not begged for after a disaster; (5) **Transparency** — honest communication about risk and capability.
- **Architecting for Failure:** Resilient architecture principles: (1) **No single points of failure** — redundancy for everything; (2) **Failure domains** — isolate failures so they don't cascade; (3) **Graceful degradation** — partial functionality is better than no functionality; (4) **Automated recovery** — faster than humans, more reliable than runbooks; (5) **Immutable infrastructure** — rebuild rather than repair.
- **The Future of DR — 2050:** Trends: (1) **AI-native DR** — recovery orchestrated, optimized, and verified by AI; (2) **Recovery as code** — fully executable, continuously tested recovery plans; (3) **Global resilience mesh** — multi-cloud, multi-region architectures that survive any single failure; (4) **Predictive DR** — AI predicts failures before they occur and preemptively shifts workloads; (5) **Resilience as a service** — fully managed DR that organizations consume rather than build. The DR professional of 2050 will be a resilience architect and AI governor, not a runbook executor.

#### Required Reading

- UoY Future Resilience Lab. (2040). *DR 2050: The Resilient Organization*.

---

## Final Examination Preparation

### Sample Essay Questions (Choose 4 of 8)

1. **RPO/RTO Design:** Design RPO/RTO tiers for a multi-business-unit enterprise. Justify your targets with business impact analysis and cost-benefit reasoning.

2. **Ransomware DR Architecture:** Design a DR architecture specifically for ransomware resilience. Address backup immutability, isolation, detection, and accelerated recovery.

3. **Cloud DR Strategy:** Compare cloud DR patterns (backup/restore, pilot light, warm standby, multi-site). When is each appropriate? Provide cost-benefit analysis.

4. **Testing Program:** Design an annual DR testing program for a financial services firm. Include test types, frequency, participants, and success criteria.

5. **Crisis Leadership:** You are the incident commander during a major outage. Walk through your first 4 hours — decisions, communications, team management.

6. **Third-Party Resilience:** Your organization depends on 15 SaaS providers and 2 cloud platforms. Design a third-party resilience program.

7. **DR Automation:** Design an automated recovery orchestration system. Address dependency modeling, parallel execution, validation, and fallback to human control.

8. **The Future of DR:** Project DR practice to 2060. What is automated? What human skills remain? How does the profession evolve?

---

**Þǫkk — May your backups restore and your people prevail.**
