# IT303: Zero-Trust Security Architecture
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4
**Description:** Deep study of zero-trust architecture — design principles, implementation patterns, identity-centric security, microsegmentation, continuous verification, and the 2040 evolution toward AI-driven zero-trust enforcement across hybrid and multi-cloud environments.

**Prerequisites:** IT205

**Instructor:** Dr. Freyja Hrafnsdóttir, Department of Information Technology

**Course Philosophy:** "Never trust, always verify." Zero trust is not a product — it is a philosophy, an architecture, and a discipline. This course moves beyond the marketing slogans to the technical reality: how to design, implement, and operate systems where every access request is authenticated, authorized, and encrypted, regardless of network location. In a world of remote work, cloud services, and AI-driven attacks, the perimeter-based security model is dead. Zero trust is the only coherent alternative.

---

## Lectures

---

### Lecture 1: The Death of the Perimeter — Why Zero Trust Is Inevitable

**Course:** IT303 — Zero-Trust Security Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

For decades, network security was perimeter-based: a firewall separated the trusted inside from the untrusted outside. This model collapsed under the weight of cloud computing, remote work, mobile devices, and sophisticated attacks that easily bypassed perimeters. This lecture traces the historical failure of perimeter security and establishes the zero-trust alternative.

#### Key Topics

- **The Perimeter Model and Its Failure:** The castle-and-moat model assumed: (1) everything inside is trusted; (2) everything outside is untrusted; (3) a strong perimeter keeps attackers out. Why it failed: (1) insiders — employees, contractors, and compromised accounts — are inside the perimeter; (2) lateral movement — once an attacker breaches the perimeter, they have free movement inside; (3) perimeter dissolution — cloud, SaaS, remote work, and mobile mean there is no single perimeter. By 2040, the "inside" is a meaningless concept.
- **Zero Trust Principles (NIST SP 800-207):** (1) All data sources and computing services are considered resources; (2) All communication is secured regardless of network location; (3) Access to individual enterprise resources is granted on a per-session basis; (4) Access is determined by dynamic policy — including the observable state of client identity, application/service, and the requesting asset; (5) The enterprise monitors and measures the integrity and security posture of all assets; (6) Authentication and authorization are strictly enforced before access; (7) The enterprise collects as much information as possible about the current state of assets and network infrastructure.
- **Zero Trust as a Journey:** No organization "completes" zero trust. It is a continuous journey measured by maturity: (1) **Traditional** — perimeter-based, static credentials, manual processes; (2) **Advanced** — some automation, MFA, basic segmentation; (3) **Zero Trust** — continuous verification, microsegmentation, automated policy enforcement; (4) **Optimal** — fully automated, AI-driven, self-healing zero trust.

#### Required Reading

- NIST. (2038). SP 800-207 Rev. 1: Zero Trust Architecture.
- Kindervag, J. (2010, updated 2038). "No More Chewy Centers: The Zero Trust Model of Information Security." Forrester Research.
- UoY Zero Trust Lab. (2040). *The Zero Trust Maturity Model*.

---

### Lecture 2: Identity-Centric Security — The New Perimeter

**Course:** IT303 — Zero-Trust Security Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

In zero trust, identity is the perimeter. Every access decision starts with: who is requesting access, from what device, in what context, and with what risk profile? This lecture covers the identity pillar of zero trust: authentication standards (FIDO2, WebAuthn, passkeys), authorization frameworks (RBAC, ABAC, PBAC), continuous authentication, and identity governance.

#### Key Topics

- **Passwordless and Phishing-Resistant MFA:** Passwords are the weakest link. The 2040 standard: FIDO2/WebAuthn passkeys — cryptographic credentials bound to the origin, resistant to phishing, and synced across user devices. MFA is mandatory for all access to sensitive resources. By 2040, continuous authentication extends beyond login — behavioral biometrics, device health, and location context continuously assess risk throughout a session.
- **Attribute-Based Access Control (ABAC):** ABAC makes access decisions based on attributes of the user (role, department, clearance), resource (classification, owner, type), action (read, write, delete), and environment (time, location, device posture). Policy example: "Allow doctors from the cardiology department to read patient records during their shift from hospital-managed devices." ABAC enables fine-grained, context-aware access control that scales better than RBAC alone.
- **Identity Governance:** Managing the identity lifecycle: (1) **Joiner-Mover-Leaver** — automated provisioning, role changes, and de-provisioning; (2) **Access reviews** — periodic certification that users still need their access; (3) **Segregation of duties** — prevent conflicting access combinations; (4) **Privileged access management (PAM)** — just-in-time access, session recording, and approval workflows for administrative access.

#### Required Reading

- W3C. (2040). *WebAuthn Level 3*.
- NIST. (2039). SP 800-207 Rev. 1 — Identity Pillar.
- UoY Identity Lab. (2040). *Continuous Authentication: From Login to Session*.

---

### Lecture 3: Device Security and Posture Assessment

**Course:** IT303 — Zero-Trust Security Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

A legitimate user on a compromised device is a threat. Zero trust extends verification to the device: Is it managed? Is it patched? Is it running expected security software? Does it show signs of compromise? This lecture covers device trust, endpoint compliance, and the integration of device posture into access decisions.

#### Key Topics

- **Device Trust Establishment:** (1) **Device identity** — each device has a cryptographic identity (TPM-backed certificate); (2) **Device health attestation** — the device reports its state: OS version, patch level, security software status, disk encryption status; (3) **Compliance policies** — define required posture (encryption enabled, firewall on, antivirus running, no jailbreak/root); (4) **Conditional Access** — access is granted, limited, or denied based on posture. By 2040, TPM 3.0 and hardware-backed attestation are standard, providing cryptographic proof of device integrity.
- **Endpoint Detection and Response (EDR/XDR):** Continuous monitoring of endpoints for signs of compromise. By 2040, XDR (Extended Detection and Response) correlates signals across endpoints, network, identity, and cloud to detect sophisticated attacks that single-source detection misses. AI-driven XDR provides real-time risk scoring that feeds into access decisions.
- **BYOD and Unmanaged Devices:** The reality: employees use personal devices. Zero trust accommodation: (1) limited access from unmanaged devices (web-only, no download, read-only); (2) virtual desktop infrastructure (VDI) or browser isolation for access from personal devices; (3) mobile application management (MAM) that secures corporate data within personal apps without managing the entire device.

#### Required Reading

- Microsoft. (2039). *Device Health Attestation: Architecture and Implementation*.
- NIST. (2039). SP 800-207 Rev. 1 — Device Pillar.
- UoY Endpoint Lab. (2040). *XDR and Zero Trust: Integration Patterns*.

---

### Lecture 4: Network Microsegmentation and Software-Defined Perimeters

**Course:** IT303 — Zero-Trust Security Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Zero trust rejects the flat, trusted internal network. Instead, the network is microsegmented — fine-grained isolation so that compromising one asset doesn't grant access to others. This lecture covers the network pillar: microsegmentation technologies, software-defined perimeters (SDP), and the convergence with identity-based networking.

#### Key Topics

- **Microsegmentation:** Dividing the network into small, isolated segments with explicit, policy-controlled communication between them. Benefits: (1) lateral movement containment — an attacker who compromises a web server cannot reach the database unless explicitly allowed; (2) blast radius reduction — a breach affects only the compromised segment; (3) compliance — sensitive data can be isolated to specific segments. Technologies: (1) host-based firewalls with centralized policy (Illumio, Guardicore), (2) network virtualization overlays (VMware NSX, Cisco ACI), (3) cloud-native security groups and network policies (Kubernetes NetworkPolicy, AWS Security Groups).
- **Software-Defined Perimeter (SDP):** SDP makes infrastructure invisible to unauthorized users. An SDP controller authenticates users and devices, then dynamically creates encrypted, per-session connections between the user and the specific resources they're authorized to access. The infrastructure is "dark" — it doesn't respond to connection attempts from unauthorized sources. This eliminates the network as an attack surface.
- **Identity-Aware Proxy:** By 2040, the convergence of identity and networking: every network connection is authenticated and authorized. The identity-aware proxy (BeyondCorp-style) sits between users and applications, verifying identity and device posture on every request. Legacy applications that don't support modern authentication can be placed behind identity-aware proxies, bringing them into the zero-trust architecture.

#### Required Reading

- NIST. (2039). SP 800-207 Rev. 1 — Network Pillar.
- Google. (2038). *BeyondCorp: A New Approach to Enterprise Security* (Updated).
- UoY Network Security Lab. (2040). *Microsegmentation at Scale: Design Patterns*.

---

### Lecture 5: Zero Trust for Applications and APIs

**Course:** IT303 — Zero-Trust Security Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Applications must be designed for zero trust — not trusting input, authenticating every API call, authorizing every data access. This lecture covers the application pillar: secure development practices, API security, service-to-service authentication, and the integration of applications with the zero-trust control plane.

#### Key Topics

- **Secure by Design:** Applications in a zero-trust architecture: (1) authenticate every request — no implicit trust for internal services; (2) authorize at the data level — row-level security, attribute-based access in the application layer; (3) validate all input — treat every input as potentially malicious; (4) encrypt everywhere — TLS for all communication, including service-to-service; (5) log everything — comprehensive audit trails for access and actions.
- **Service-to-Service Authentication:** In a microservices world, services call services. Zero-trust service authentication: (1) **Mutual TLS (mTLS)** — services authenticate each other with certificates; (2) **SPIFFE/SPIRE** — the Cloud Native Computing Foundation's standard for service identity; (3) **Short-lived tokens** — service tokens that expire in minutes, reducing the window for token theft. By 2040, SPIFFE-based identity is the standard for service mesh authentication.
- **API Security Gateway:** The API gateway enforces zero-trust for APIs: (1) authentication — OAuth 2.1, API keys, mTLS; (2) authorization — per-endpoint, per-method, per-parameter access control; (3) rate limiting — per-user, per-token, per-IP; (4) schema validation — reject requests that don't match the API contract; (5) threat detection — AI-driven detection of API abuse patterns.

#### Required Reading

- OWASP. (2040). *API Security Top 10*.
- CNCF. (2040). *SPIFFE: Secure Production Identity Framework for Everyone*.
- UoY Application Security Lab. (2039). *Zero Trust for Cloud-Native Applications*.

---

### Lecture 6: Data-Centric Security — Protecting Information, Not Just Systems

**Course:** IT303 — Zero-Trust Security Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

The ultimate asset is data. Zero-trust extends to the data layer: classifying data by sensitivity, encrypting everywhere, controlling access at the data level, and monitoring data movement. This lecture covers the data pillar of zero trust.

#### Key Topics

- **Data Classification and Discovery:** You can't protect what you don't know you have. Automated data discovery tools scan structured and unstructured data to identify sensitive information (PII, PHI, PCI, IP). Classification labels drive protection policies. By 2040, AI-powered data classification achieves high accuracy with minimal manual labeling.
- **Encryption Everywhere:** (1) **At rest** — all data encrypted, with customer-managed keys; (2) **In transit** — TLS 1.4 with PQC for all communication; (3) **In use** — confidential computing for sensitive workloads; (4) **Application-layer encryption** — encrypt sensitive fields before storing in the database, so even database administrators can't read them.
- **Data Loss Prevention (DLP):** Monitoring and controlling data movement: (1) **Endpoint DLP** — prevent copying sensitive data to USB drives, personal email, or unauthorized cloud services; (2) **Network DLP** — detect sensitive data in network traffic; (3) **Cloud DLP** — scan cloud storage for misconfigured permissions and exposed data. By 2040, AI-driven DLP reduces false positives by understanding context — distinguishing between a doctor sharing patient data for treatment (authorized) vs. exfiltration (unauthorized).

#### Required Reading

- NIST. (2039). SP 800-207 Rev. 1 — Data Pillar.
- CSA. (2040). *Cloud Data Security: Encryption, DLP, and Governance*.
- UoY Data Security Lab. (2040). *Data-Centric Zero Trust: Architectures and Practices*.

---

### Lecture 7: Zero Trust for Cloud and Multi-Cloud Environments

**Course:** IT303 — Zero-Trust Security Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Cloud introduces unique zero-trust challenges: shared responsibility, dynamic infrastructure, and the blurring of network boundaries. This lecture covers cloud-native zero trust: IAM as the control plane, infrastructure as code security, cloud security posture management, and multi-cloud zero-trust architectures.

#### Key Topics

- **Cloud IAM as the Zero-Trust Control Plane:** Cloud IAM (AWS IAM, Azure RBAC, Google Cloud IAM) is the foundation of cloud zero trust. Best practices: (1) least privilege — start with no permissions; (2) resource-based policies in addition to identity-based policies; (3) conditional access — MFA, IP restrictions, device posture; (4) temporary credentials — no long-lived access keys.
- **Infrastructure as Code Security:** IaC (Terraform, CloudFormation, Pulumi) defines cloud infrastructure. Security must be embedded: (1) policy-as-code (Open Policy Agent, Checkov) scans IaC for security violations before deployment; (2) drift detection identifies manual changes that bypass IaC; (3) immutable infrastructure prevents in-place modifications.
- **Cloud Security Posture Management (CSPM):** Continuous monitoring for misconfigurations across cloud environments. By 2040, CSPM has merged with CIEM (Cloud Infrastructure Entitlement Management) and CWPP (Cloud Workload Protection Platform) into unified CNAPP solutions that provide holistic cloud security from development to runtime.

#### Required Reading

- AWS. (2040). *Zero Trust on AWS: Architecture Guide*.
- HashiCorp. (2039). *Policy as Code for Zero Trust Infrastructure*.
- UoY Cloud Security Lab. (2040). *Multi-Cloud Zero Trust: Architecture Patterns*.

---

### Lecture 8: Zero Trust for AI and ML Systems

**Course:** IT303 — Zero-Trust Security Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

AI/ML systems introduce new zero-trust challenges: models are assets that must be protected, training data is sensitive, and model inference is an access point that can be attacked. This lecture covers AI-specific zero-trust: model access control, data pipeline security, adversarial defense, and model governance.

#### Key Topics

- **Model Access Control:** AI models are valuable IP. Zero-trust access to models: (1) authenticate every inference request; (2) authorize based on user identity, model tier, and usage limits; (3) rate limit to prevent model extraction; (4) log all inference requests for audit; (5) detect adversarial inputs designed to manipulate the model.
- **Training Data Protection:** Training data often contains sensitive information. Protections: (1) differential privacy — add noise during training to protect individual data points; (2) federated learning — train models without centralizing data; (3) data provenance — track where training data came from and who has accessed it.
- **ML Pipeline Security:** The CI/CD pipeline for ML models must be secured: (1) signed model artifacts — verify model integrity before deployment; (2) provenance tracking — know the training data, code, and parameters for every deployed model; (3) vulnerability scanning — scan ML libraries and dependencies; (4) model registry access control — who can register, promote, and deploy models.

#### Required Reading

- NIST. (2040). *AI 600-1: Zero Trust for Artificial Intelligence Systems*.
- UoY AI Security Lab. (2039). *Securing the ML Pipeline: A Zero-Trust Approach*.

---

### Lecture 9: Designing and Deploying a Zero-Trust Architecture

**Course:** IT303 — Zero-Trust Security Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Zero trust is not one product — it is an architecture composed of multiple technologies integrated through a policy engine. This lecture provides a practical framework for designing, deploying, and evolving a zero-trust architecture.

#### Key Topics

- **The Zero Trust Logical Architecture:** NIST's reference architecture: (1) **Policy Engine (PE)** — makes access decisions based on policy, identity, device posture, and context; (2) **Policy Administrator (PA)** — executes the PE's decisions (establish, block, or terminate connections); (3) **Policy Enforcement Point (PEP)** — the gatekeeper that intercepts access requests and enforces PA decisions; (4) **Supporting data sources** — identity management, device inventory, threat intelligence, SIEM, data classification.
- **Implementation Patterns:** (1) **Identity-centric** — all access routed through identity-aware proxies; (2) **Network-centric** — microsegmentation and SDP as the foundation; (3) **Application-centric** — zero trust embedded in application architecture. Most organizations combine patterns. The key: choose the pattern that best addresses your most critical assets.
- **Migration Strategy:** Zero trust is implemented incrementally: (1) **Identify** — discover assets, users, and data flows; (2) **Classify** — categorize by sensitivity and criticality; (3) **Protect the crown jewels first** — start with your most critical assets; (4) **Expand** — incrementally bring more assets into zero trust; (5) **Optimize** — continuously tune policies and automate. The migration typically takes 3-5 years for a large enterprise.

#### Required Reading

- NIST. (2038). SP 800-207 Rev. 1 — Appendix: Implementation Scenarios.
- CISA. (2039). *Zero Trust Maturity Model v2.0*.
- UoY Zero Trust Lab. (2039). *Deployment Patterns and Migration Strategies*.

---

### Lecture 10: Continuous Monitoring, Analytics, and Automated Response

**Course:** IT303 — Zero-Trust Security Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Zero trust is not a one-time check — it's continuous. The architecture must continuously monitor, analyze, and respond to changes in identity, device posture, network behavior, and threat landscape. This lecture covers the visibility and analytics pillar: SIEM/SOAR integration, UEBA, and the feedback loop that makes zero trust adaptive.

#### Key Topics

- **Continuous Diagnostics and Monitoring:** Zero trust requires comprehensive visibility: (1) **Asset inventory** — every device, user, and service is tracked; (2) **Configuration monitoring** — detect deviations from secure baselines; (3) **Behavior monitoring** — detect anomalous user and entity behavior; (4) **Threat intelligence integration** — contextualize events with external threat data. The goal: detect and respond to threats in real time, not after the fact.
- **Policy Feedback Loop:** Zero trust policies must evolve. The feedback loop: (1) monitor access patterns and threats; (2) analyze for policy gaps and optimization opportunities; (3) update policies; (4) deploy updated policies; (5) monitor the effect. By 2040, AI-driven policy optimization suggests policy changes based on observed traffic patterns and threat intelligence.
- **Incident Response in Zero Trust:** Zero trust changes incident response: (1) microsegmentation limits blast radius — incidents are easier to contain; (2) comprehensive logging speeds investigation — every access event is recorded; (3) dynamic policy enables rapid response — revoke access, isolate segments, or increase authentication requirements instantly.

#### Required Reading

- NIST. (2039). SP 800-207 Rev. 1 — Visibility and Analytics Pillar.
- UoY SOC Lab. (2039). *Incident Response in Zero-Trust Environments*.

---

### Lecture 11: Zero Trust Governance, Compliance, and Metrics

**Course:** IT303 — Zero-Trust Security Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Zero trust must be governed — policies must be managed, compliance must be demonstrated, and effectiveness must be measured. This lecture covers the governance framework for zero trust: policy management lifecycle, compliance mapping, metrics and KPIs, and executive reporting.

#### Key Topics

- **Policy Management Lifecycle:** (1) Draft — security architects write policies; (2) Review — stakeholders validate; (3) Test — simulate policy impact before deployment; (4) Deploy — roll out progressively; (5) Monitor — track policy effectiveness; (6) Refine — improve based on data. By 2040, policy-as-code with GitOps workflows manages this lifecycle.
- **Compliance Mapping:** Map zero trust controls to regulatory frameworks (GDPR, CCPA, PCI DSS, HIPAA, NIST CSF). Automated compliance reporting demonstrates that zero trust controls satisfy regulatory requirements. The 2040 practice: continuous compliance — real-time monitoring of control effectiveness, not point-in-time audits.
- **Zero Trust KPIs:** (1) **Coverage** — percentage of assets, users, and applications under zero trust; (2) **Authentication strength** — percentage of access using phishing-resistant MFA; (3) **Least privilege** — percentage of over-privileged accounts identified and remediated; (4) **Microsegmentation** — percentage of network traffic subject to microsegmentation policy; (5) **Mean time to detect/respond** — speed of threat detection and response; (6) **Policy violation rate** — frequency of access denied by policy.

#### Required Reading

- CISA. (2040). *Zero Trust Performance Metrics*.
- UoY Governance Lab. (2039). *Governing Zero Trust: Policy, Compliance, and Metrics*.

---

### Lecture 12: The Future of Zero Trust — Autonomous, Predictive, and Ubiquitous

**Course:** IT303 — Zero-Trust Security Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Where does zero trust go from here? This lecture projects trends: autonomous policy generation, predictive access (grant access before it's needed based on context prediction), ubiquitous zero trust extending to IoT, OT, and personal devices, and the convergence of zero trust with decentralized identity and verifiable credentials.

#### Key Topics

- **Autonomous Policy:** AI that generates and tunes zero trust policies: (1) observe normal access patterns; (2) propose policies that permit legitimate patterns and deny everything else; (3) human review and approval; (4) continuous tuning. This addresses the biggest zero trust bottleneck: policy creation and maintenance.
- **Predictive Access:** Instead of evaluating access at request time, predict and pre-authorize access based on context: calendar (meeting with a client suggests access to client files), location (entering the office suggests access to office resources), behavior patterns. This reduces latency while maintaining security.
- **Ubiquitous Zero Trust:** Extending zero trust beyond traditional IT: (1) IoT — every device authenticated and authorized; (2) OT — industrial control systems with zero-trust access; (3) 6G — zero trust built into the network layer; (4) Personal — individuals controlling access to their personal data through zero-trust principles and verifiable credentials.

#### Required Reading

- UoY Future Security Lab. (2040). *Zero Trust 2050: Autonomous, Predictive, Ubiquitous*.
- W3C. (2040). *Verifiable Credentials and Zero Trust: Convergence Patterns*.

---

## Final Examination Preparation

### Sample Essay Questions (Choose 4 of 8)

1. **Architecture Design:** Design a zero-trust architecture for a healthcare organization. Address all pillars: identity, device, network, application, and data.

2. **Migration Strategy:** Your organization operates a traditional perimeter-based network. Design a 4-year zero trust migration roadmap.

3. **Microsegmentation Deep Dive:** Compare three microsegmentation approaches (host-based, network overlay, cloud-native). When is each appropriate?

4. **AI and Zero Trust:** AI systems both enable zero trust (automated policy, anomaly detection) and require zero trust (model protection, pipeline security). Analyze this duality.

5. **Zero Trust for Legacy:** Your organization has mainframe applications that can't be modified. How do you bring them into a zero-trust architecture?

6. **Compliance Case Study:** Map zero trust controls to GDPR requirements. What gaps remain?

7. **Incident Response:** A zero-trust environment detects anomalous access. Walk through the incident response — how does zero trust change detection, containment, investigation, and recovery?

8. **The Limits of Zero Trust:** Zero trust reduces but doesn't eliminate risk. What are the residual risks? What attacks does zero trust NOT protect against?

---

**Þǫkk — May your trust be earned, never assumed.**
