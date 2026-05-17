# IT301: Information Security — The Shield-Wall of the Digital Age

**Program:** Bachelor of Information Technology, Year 3  
**Credits:** 4 ECTS  
**Prerequisites:** IT101, IT205  
**Instructor:** Prof. Eiríkr Stefánsson, CISSP, CISM  
**Office:** Heorot Hall, Room 304  
**Semester:** Fall 2040  

> *"The best shield-wall is not the one that never breaks, but the one that knows how to reform after a breach."* — Eiríkr Stefánsson, *Annals of Digital Defence*, 2038

---

## Course Description

Information Security stands as the shield-wall between operational integrity and the constant assault of threat actors in an interconnected 2040. This course equips IT professionals with the practical, hands-on skills to identify vulnerabilities, model threats, respond to incidents, and build compliance frameworks that satisfy regulatory demands without strangling operational agility. Students will deploy and configure real security tools — from Wireshark and Nmap to Splunk and Snort — in sandboxed environments. By term's end, each student will have conducted a full penetration test, written an incident response playbook, and mapped a compliance framework to a fictional enterprise.

---

## Lecture 1: The Information Security Landscape in 2040

### Attack Surface Expansion and the Death of the Perimeter

Information security in 2040 operates in a world where the traditional network perimeter dissolved long ago. The attack surface now encompasses not only corporate data centres and cloud instances, but also edge devices numbering in the hundreds per employee, quantum-accessible cryptographic systems under active threat, and AI-augmented adversaries capable of generating polymorphic attack chains faster than human analysts can triage them. The Verizon 2039 Data Breach Investigations Report documented a 340% increase in AI-assisted social engineering attacks since 2035, with average dwell time — the period between initial compromise and detection — dropping from 21 days in 2030 to 4.2 hours in 2039, not because defenders improved, but because attackers automated their lateral movement. The perimeter is dead. Security is now a property of every transaction, every identity assertion, and every data access pattern.

The concept of "defence in depth" has evolved from a layered network architecture into a continuous verification model. Zero Trust Architecture (ZTA), formally standardised in NIST SP 800-207 and updated through Revision 3 in 2038, mandates that no actor, device, or workload be trusted by default — regardless of whether it sits inside a corporate network. Every access request must be authenticated, authorised, and continuously validated against real-time risk signals: device posture, behavioural biometrics, geolocation anomalies, and threat intelligence feeds. The 2040 practitioner must understand not only the technical implementation of ZTA (microsegmentation, software-defined perimeters, identity-aware proxies) but also the organisational psychology of transitioning from a "trust but verify" to a "never trust, always verify" culture.

### The Triad and Its Modern Extensions

The CIA triad — Confidentiality, Integrity, Availability — remains the conceptual backbone of information security, but 2040 practice extends it with three additional pillars. **Authenticity** ensures that data provenance can be cryptographically verified, critical in an era of deepfake-augmented phishing and synthetic media. **Non-repudiation** guarantees that actions cannot be denied after the fact, essential for regulatory compliance under frameworks like the EU Digital Operational Resilience Act (DORA) and the US Cyber Incident Reporting for Critical Infrastructure Act (CIRCIA). **Privacy** has graduated from a compliance checkbox to a first-order security concern, with the Global Privacy Enforcement Network (GPEN) wielding substantial fining power and the ISO 27701:2039 Privacy Information Management System becoming a baseline expectation for any organisation handling personal data. These six pillars — CIA + Authenticity, Non-repudiation, Privacy — form the hexagon of modern infosec.

```
THE SECURITY HEXAGON OF 2040

         Confidentiality
              /\
             /  \
   Privacy  /    \  Integrity
           /      \
          /________\
   Non-repudiation  Authenticity
          \        /
           \      /
            \    /
             \  /
              \/
         Availability
```

### Required Reading

- NIST SP 800-207 Rev. 3 (2038), *Zero Trust Architecture*, §§1-3.
- Verizon, *2039 Data Breach Investigations Report*, Executive Summary.
- Stefánsson, E. (2038), *Annals of Digital Defence*, University of Yggdrasil Press, Ch. 1, "The Unwalled City."

### Discussion Questions

1. How does the dissolution of the network perimeter change the role of the IT security practitioner compared to 2020?
2. In what ways might Zero Trust Architecture introduce new operational friction, and how should organisations balance security against usability?
3. Why has privacy become a first-order security pillar rather than a subset of confidentiality?

---

## Lecture 2: Threat Modelling — Knowing Your Enemy

### The Art of Anticipating Attack

Threat modelling is the structured practice of identifying what you need to protect, who might want to compromise it, and how they might attempt to do so. In the 2040 landscape, threat modelling has moved from a periodic exercise (done once per project, then filed away) to a continuous, automated discipline integrated into CI/CD pipelines. The STRIDE framework (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege), first developed at Microsoft in the early 2000s, remains relevant but has been augmented by STRIDE-LM 2040, which adds **Lateral Movement** and **Model Extraction** — the latter reflecting the rise of adversarial machine learning attacks against AI/ML systems that now pervade enterprise infrastructure.

Modern threat modelling tools — Microsoft Threat Modelling Tool 2040 Edition, OWASP Threat Dragon with AI-assisted diagramming, and the open-source PyTM library for programmatic threat modelling in Python — allow security analysts to generate attack trees, data flow diagrams, and threat catalogues automatically from infrastructure-as-code definitions. A Terraform or Pulumi configuration can be parsed, its resources identified, and a threat model generated before a single cloud resource is provisioned. This "shift left" approach moves threat modelling into the design phase, where fixing a vulnerability costs a fraction of what it would in production.

### Practical Threat Modelling Workshop

Consider a fictional 2040 enterprise: **Yggdrasil Health**, a telemedicine platform handling Protected Health Information (PHI) under HIPAA and GDPR. Its architecture includes patient-facing mobile apps, a Kubernetes-hosted API gateway, a FHIR-compliant health data store, and an AI diagnostic module that analyses medical imaging. Students will model this system using STRIDE-LM:

| Threat Category | Example for Yggdrasil Health |
|----------------|------------------------------|
| **Spoofing** | Attacker impersonates a physician via compromised credentials |
| **Tampering** | Malicious modification of medical images to induce misdiagnosis |
| **Repudiation** | Physician denies ordering a specific test; audit log integrity questioned |
| **Information Disclosure** | PHI exfiltrated via misconfigured S3 bucket |
| **Denial of Service** | DDoS against telemedicine gateway during pandemic surge |
| **Elevation of Privilege** | Horizontal privilege escalation from patient to physician role |
| **Lateral Movement** | Compromised IoT nurse-call device used to pivot to EHR database |
| **Model Extraction** | Attacker queries AI diagnostic module to reconstruct proprietary model |

### Required Reading

- Shostack, A. (2035), *Threat Modelling: Designing for Security*, 3rd ed., Wiley, Chs. 2-4.
- OWASP, *Threat Modelling Cheat Sheet*, 2040 Edition.
- PyTM Documentation, https://github.com/izar/pytm, §§1-3.

### Discussion Questions

1. STRIDE-LM adds "Lateral Movement" and "Model Extraction." What other threat categories might emerge by 2050?
2. How does automated threat modelling from Infrastructure-as-Code change the role of the human security analyst?
3. For Yggdrasil Health, which threat category do you consider the highest risk, and why?

---

## Lecture 3: Cryptography for the IT Practitioner

### From Caesar to Quantum-Resistant

Cryptography is the runecraft of information security — the art of transforming plaintext into ciphertext and back again, such that only those who hold the correct keys can read the message. The IT practitioner need not be a cryptographer, but must understand the operational properties of the primitives they deploy: symmetric vs. asymmetric encryption, hashing, digital signatures, key exchange protocols, and Public Key Infrastructure (PKI). The 2040 landscape introduces an urgent new dimension: the impending arrival of cryptographically relevant quantum computers (CRQCs), which threaten to break RSA, ECDSA, and Diffie-Hellman through Shor's algorithm.

NIST's Post-Quantum Cryptography (PQC) standardisation process, completed in 2024 and updated through 2038, selected three primary algorithms: **CRYSTALS-Kyber** for key encapsulation (FIPS 203), **CRYSTALS-Dilithium** for digital signatures (FIPS 204), and **SPHINCS+** for stateless hash-based signatures (FIPS 205). The 2040 IT professional must plan migrations from RSA-2048 and ECDSA to these PQC algorithms, a process complicated by the "harvest now, decrypt later" threat: adversaries with sufficient storage capacity may be capturing encrypted traffic today, intending to decrypt it once CRQCs become available. All long-lived secrets — medical records, national security communications, financial transaction histories — must be protected with PQC or hybrid classical-PQC schemes immediately.

### Practical Cryptography Operations

```bash
# Generate an Ed25519 key pair (modern, fast, considered quantum-resistant against known attacks)
ssh-keygen -t ed25519 -C "yggdrasil-health-admin" -f ~/.ssh/id_ed25519

# Generate a self-signed certificate with ECDSA and SHA-384
openssl req -x509 -newkey ec -pkeyopt ec_paramgen_curve:P-384 -sha384 \
    -days 365 -nodes -keyout server.key -out server.crt \
    -subj "/CN=yggdrasil-health.no/O=Yggdrasil Health"

# Verify a certificate chain
openssl verify -CAfile root-ca.crt -untrusted intermediate.crt server.crt

# Hash a file with SHA-3-512 (FIPS 202)
openssl dgst -sha3-512 patient_records.fhir

# Encrypt a file with AES-256-GCM (authenticated encryption)
openssl enc -aes-256-gcm -in sensitive_data.txt -out sensitive_data.enc -pass pass:...
```

### Key Management — The Hardest Problem

The operational Achilles' heel of cryptography is not algorithm selection but key management. Hardware Security Modules (HSMs), cloud key management services (AWS KMS, Azure Key Vault, Google Cloud KMS), and the emerging decentralised key management protocols (DKMS) each have distinct operational profiles. The IT practitioner must understand: key generation ceremonies, key rotation schedules, key destruction procedures (cryptographic erasure), and the difference between envelope encryption (where a data encryption key is wrapped by a key encryption key stored in an HSM) and direct HSM encryption. The 2039 Thales Cloud Security Study found that 67% of organisations store cryptographic keys in the same environment as the data they protect — a finding that prompts the wry observation that "locking the door and leaving the key under the mat" remains the most popular security architecture in history.

### Required Reading

- NIST SP 800-175B Rev. 2 (2039), *Guideline for Using Cryptographic Standards in the Federal Government: Post-Quantum Cryptography Transition*.
- Ferguson, N., Schneier, B., & Kohno, T. (2035), *Cryptography Engineering*, 2nd ed., Wiley, Chs. 3-5, 14.
- Thales, *2039 Cloud Security Study*, "Key Management Practices" section.

### Discussion Questions

1. If an organisation has been using RSA-2048 for all TLS connections since 2030, what is their exposure under "harvest now, decrypt later"?
2. Why is key rotation more operationally complex than it appears on paper, and what automation strategies mitigate this?
3. What are the trade-offs between cloud KMS, on-premises HSM, and DKMS for a mid-size enterprise?

---

## Lecture 4: Network Security — The Moat and the Drawbridge

### Network Segmentation and Microsegmentation

Network security in 2040 rests on the principle that flat networks are indefensible. Segmentation carves a network into trust zones with controlled traffic flows between them. Traditional segmentation used VLANs and subnets with firewall rules at zone boundaries; modern microsegmentation extends this to the workload level, where every container, virtual machine, and serverless function has its own software-defined perimeter with identity-based access policies. The Kubernetes NetworkPolicy API, Istio service mesh with mTLS, and cloud-native constructs like AWS Security Groups and Azure Network Security Groups (NSGs) are the tools of the trade.

The IT practitioner configures segmentation using a policy-as-code approach: rules are defined declaratively (in YAML, HCL, or Rego), stored in version control, and applied automatically via CI/CD pipelines. This eliminates the "snowflake firewall" problem where years of manual rule additions create a configuration so complex that no single person understands the full security posture. Tools like CloudQuery, Steampipe, and OPA (Open Policy Agent) enable continuous compliance scanning of network configurations against security benchmarks such as CIS Controls v9 and the AWS Well-Architected Framework, Security Pillar.

### Firewall Architectures and IDS/IPS

Next-generation firewalls (NGFWs) have evolved beyond Layer 4 filtering to application-aware, identity-aware, and threat-intelligence-integrated enforcement points. In 2040, the dominant architectures are:

- **Distributed NGFW**: Firewall enforcement at every workload (e.g., Calico, Cilium for Kubernetes; AWS Network Firewall for cloud VPCs).
- **Firewall-as-a-Service (FWaaS)**: Cloud-delivered firewalls (Cloudflare Magic Firewall, Zscaler) that route traffic through a global enforcement mesh.
- **AI-augmented IDS/IPS**: Intrusion detection and prevention systems (Snort 4, Suricata 8) that use transformer-based models to detect zero-day exploits from packet patterns, reducing false positive rates below 0.1%.

```python
# Example: OPA/Rego policy for Kubernetes network policy
import yaml

network_policy = {
    "apiVersion": "networking.k8s.io/v1",
    "kind": "NetworkPolicy",
    "metadata": {"name": "deny-all-ingress", "namespace": "hipaa-workloads"},
    "spec": {
        "podSelector": {},
        "policyTypes": ["Ingress"],
        "ingress": [
            {
                "from": [
                    {"namespaceSelector": {"matchLabels": {"trust-zone": "api-gateway"}}}
                ],
                "ports": [{"protocol": "TCP", "port": 443}]
            }
        ]
    }
}
print(yaml.dump(network_policy, default_flow_style=False))
```

### Required Reading

- CIS, *CIS Controls v9*, Control 4: Secure Configuration of Enterprise Assets and Software.
- Cilium Documentation, "Network Policy Editor," https://docs.cilium.io, §§1-4.
- Lyon, G. (2037), *Nmap Network Scanning: The Official Nmap Project Guide*, 2nd ed., Chs. 3, 7, 10.

### Discussion Questions

1. How does microsegmentation change incident response compared to traditional VLAN-based segmentation?
2. What are the operational risks of AI-augmented IDS/IPS that autonomously blocks traffic — and how should an IT team configure guardrails?
3. Design a network segmentation strategy for Yggdrasil Health that separates patient data, AI inference, and public-facing APIs.

---

## Lecture 5: Identity and Access Management (IAM) — The Gatekeeper's Ledger

### Authentication, Authorisation, and Accounting

Identity and Access Management (IAM) forms the gatekeeper's ledger of the digital realm. Every access decision rests on three pillars: **Authentication** (who are you?), **Authorisation** (what are you allowed to do?), and **Accounting** (what did you do?). In 2040, authentication has moved well beyond passwords. The FIDO2 standard, with its WebAuthn and CTAP components, has achieved near-universal adoption for consumer and enterprise use. Passkeys — cryptographic key pairs tied to a user's device and synchronised across their ecosystem — have replaced passwords for the majority of authentication events. For high-security environments, continuous behavioural biometrics (keystroke dynamics, mouse movement patterns, voiceprint analysis) provide a passive authentication layer that augments the initial authentication event.

Authorisation models have evolved from Role-Based Access Control (RBAC) to Attribute-Based Access Control (ABAC) and Relationship-Based Access Control (ReBAC), implemented via policy languages like Cedar (AWS Verified Permissions), OpenFGA (based on Google's Zanzibar), and OPA/Rego. The 2040 practitioner must understand how to model access policies declaratively and test them exhaustively before deployment. The "principal of least privilege" — granting only the permissions necessary to perform a task — must be enforced automatically through tools like IAM Access Analyzer, Cloudsplaining, and Policy Sentry.

### Practical IAM: AWS IAM and Beyond

```bash
# Audit IAM users with console access but no MFA (AWS CLI)
aws iam list-users --query "Users[?PasswordEnabled=='true'].[UserName]" --output text | \
while read user; do
    mfa=$(aws iam list-mfa-devices --user-name "$user" --query "MFADevices" --output text)
    if [ -z "$mfa" ]; then echo "NO MFA: $user"; fi
done

# Create an IAM policy with least privilege (JSON)
cat > allow_s3_read_patient_images.json << 'EOF'
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:ListBucket"],
            "Resource": [
                "arn:aws:s3:::yggdrasil-health-patient-images",
                "arn:aws:s3:::yggdrasil-health-patient-images/*"
            ],
            "Condition": {
                "StringEquals": {"aws:PrincipalTag/Department": "Radiology"},
                "Bool": {"aws:MultiFactorAuthPresent": "true"}
            }
        }
    ]
}
EOF
```

### Single Sign-On and Federation

Federation protocols — SAML 2.0, OpenID Connect (OIDC), and the emerging OIDC4IA (OIDC for Identity Assurance, standardised in 2037) — enable users to authenticate once and access multiple systems. The 2040 IT professional configures identity providers (Okta, Azure AD/Entra ID, Keycloak) and implements service provider integrations. The critical security consideration is token hygiene: access tokens should be short-lived (5-15 minutes), refresh tokens should be rotated on each use, and JSON Web Tokens (JWTs) should be validated rigorously — checking the signature algorithm, issuer, audience, and expiration claims on every request.

### Required Reading

- NIST SP 800-63-4 (2039), *Digital Identity Guidelines*, §§1-5.
- W3C, *Web Authentication: An API for Accessing Public Key Credentials*, Level 3 (2038).
- FIDO Alliance, *FIDO2 Technical Specification*, Version 2.1.

### Discussion Questions

1. What are the security implications of synchronised passkeys across a user's device ecosystem?
2. How does ABAC differ from RBAC in operational practice, and when would you choose one over the other?
3. If an organisation moves all authentication to FIDO2 passkeys, what residual identity risks remain?

---

## Lecture 6: Vulnerability Management and Penetration Testing

### The Vulnerability Lifecycle

Vulnerability management is the disciplined practice of identifying, classifying, prioritising, remediating, and verifying security weaknesses across an organisation's entire technology estate. The Common Vulnerabilities and Exposures (CVE) system, maintained by MITRE, catalogued over 250,000 vulnerabilities by 2040, with new entries averaging 75 per day. The Common Vulnerability Scoring System (CVSS v4.0, 2038) provides a standardised severity rating (0.0-10.0), but the 2040 practitioner learns quickly that CVSS scores alone are insufficient: the Exploit Prediction Scoring System (EPSS) estimates the probability that a vulnerability will be exploited in the wild within 30 days, adding a risk-prioritisation layer that prevents "alert fatigue" from high-CVSS, low-exploit-probability findings.

The vulnerability management lifecycle follows five phases: **Asset Discovery** (you cannot protect what you do not know you have), **Scanning** (automated vulnerability scanners — Nessus, Qualys, OpenVAS, cloud-native tools like AWS Inspector and Azure Defender), **Prioritisation** (CVSS + EPSS + asset criticality + exposure context), **Remediation** (patch, configuration change, compensating control, or risk acceptance), and **Verification** (rescan to confirm the fix). In 2040, this lifecycle runs continuously, with scanning pipelines integrated into CI/CD and asset discovery updated in near-real-time through cloud asset inventory APIs and agent-based endpoint telemetry.

### Penetration Testing Methodology

Penetration testing (pentesting) is the authorised simulated attack against a system to identify exploitable vulnerabilities. The 2040 methodology follows the Penetration Testing Execution Standard (PTES) with seven phases:

1. **Pre-engagement Interactions** — Rules of engagement, scope definition, legal authorisation
2. **Intelligence Gathering** — OSINT (recon-ng, theHarvester, Shodan, Censys), DNS enumeration, social media profiling
3. **Threat Modelling** — Mapping the gathered intelligence into attack vectors
4. **Vulnerability Analysis** — Active scanning (Nmap, Nessus, Nikto) combined with manual analysis
5. **Exploitation** — Metasploit Framework, custom Python/Rust exploits, password cracking (Hashcat, John the Ripper)
6. **Post-Exploitation** — Privilege escalation, lateral movement, data exfiltration simulation, persistence mechanisms
7. **Reporting** — Executive summary, technical findings with CVSS scores and remediation guidance, retesting schedule

```bash
# Basic pentesting toolchain example
# 1. Network discovery
nmap -sS -sV -O -p- --script vuln 10.0.0.0/24 -oA it301_lab_scan

# 2. Web application scanning
nikto -h https://yggdrasil-health-staging.no -output nikto_scan.txt

# 3. Directory enumeration
gobuster dir -u https://yggdrasil-health-staging.no -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o gobuster.txt

# 4. SQL injection testing
sqlmap -u "https://yggdrasil-health-staging.no/api/patient?id=1" --level=3 --risk=2
```

### Required Reading

- PTES Technical Guidelines, http://www.pentest-standard.org, all sections.
- MITRE, *CVE and CVSS v4.0 Documentation*, 2038.
- Kim, P. (2039), *The Hacker Playbook 2040: Practical Guide to Penetration Testing*, 4th ed., Secure Planet Press.

### Discussion Questions

1. Why is EPSS a necessary complement to CVSS for vulnerability prioritisation?
2. What ethical and legal considerations govern the difference between penetration testing and unauthorised hacking?
3. If a critical vulnerability in a medical device cannot be patched for six months due to regulatory re-certification requirements, what compensating controls would you implement?

---

## Lecture 7: Incident Response — When the Shield-Wall Breaks

### The Incident Response Lifecycle

Incident response is the organised approach to addressing and managing the aftermath of a security breach or cyberattack. The NIST Computer Security Incident Handling Guide (SP 800-61 Rev. 3, 2039) defines a four-phase lifecycle: **Preparation**, **Detection & Analysis**, **Containment, Eradication & Recovery**, and **Post-Incident Activity**. The 2040 IT professional must transition from reactive incident response to a **continuous incident response** posture, where detection pipelines feed SIEM/SOAR platforms and playbooks are automated to the maximum extent feasible.

The **Preparation** phase requires more than documentation. It demands: an incident response team (IRT) with clearly defined roles (Incident Commander, Technical Lead, Communications Lead, Legal Liaison), a communication plan that accounts for regulatory notification timelines (72 hours under GDPR, 24 hours under CIRCIA for critical infrastructure), pre-staged forensic toolkits (volatility for memory forensics, GRR Rapid Response for remote evidence collection, Velociraptor for endpoint interrogation), and tabletop exercises conducted quarterly. The 2040 IRT also includes an **AI Incident Liaison** role, responsible for determining whether AI/ML systems were involved in the incident — either as attack vector or defender — which triggers additional reporting requirements under the EU AI Act of 2036.

### The First Hour: Triage and Containment

When a security incident is declared, the first hour is critical. The Incident Commander follows the **DECIDE framework**:

1. **Declare** the incident and activate the IRT
2. **Evaluate** the scope — what systems, data, and users are affected?
3. **Contain** the threat — isolate affected systems (network segmentation, credential rotation, token revocation)
4. **Investigate** — begin forensic evidence collection before containment actions destroy volatile data
5. **Document** — every action, timestamp, and decision in the incident log
6. **Escalate** — notify leadership, legal, and regulatory bodies as required

Containment strategy depends on the threat type. For ransomware, containment means immediately disconnecting affected systems and disabling domain accounts. For data exfiltration, containment means revoking the exfiltrating entity's credentials and blocking egress at the firewall. For an insider threat, containment may involve legal hold procedures and HR coordination before technical action. Short-term containment buys time for forensic analysis; long-term containment implements temporary fixes that allow business operations to resume while permanent remediation is engineered.

### Required Reading

- NIST SP 800-61 Rev. 3 (2039), *Computer Security Incident Handling Guide*, all sections.
- Cichonski, P., Millar, T., Grance, T., & Scarfone, K. (2039), "DECIDE: A Decision Framework for Cyber Incident Response," *SANS Digital Forensics and Incident Response Summit 2039*.
- SANS, *Incident Handler's Handbook*, 2040 Edition.

### Discussion Questions

1. What are the trade-offs between immediate containment and forensic evidence preservation?
2. How should incident response procedures differ for ransomware vs. data exfiltration vs. insider threat?
3. Design a 60-minute incident response timeline for Yggdrasil Health if a patient data exfiltration is detected at 09:00 UTC.

---

## Lecture 8: Security Information and Event Management (SIEM) and SOAR

### The Central Nervous System of Security Operations

Security Information and Event Management (SIEM) platforms aggregate, correlate, and analyse log data from across the enterprise to detect security incidents. In 2040, the SIEM has evolved from a log search engine into a real-time analytics platform with integrated User and Entity Behaviour Analytics (UEBA), network traffic analysis, and threat intelligence feeds. Dominant platforms include Splunk Enterprise Security, Microsoft Sentinel, Elastic Security, and the open-source Wazuh and Matano stacks. The IT practitioner configures data connectors, normalises log formats (ECS — Elastic Common Schema, OCSF — Open Cybersecurity Schema Framework), writes detection rules in Sigma or KQL, and tunes alert thresholds to balance false positive reduction with detection sensitivity.

The companion technology to SIEM is SOAR — Security Orchestration, Automation, and Response. SOAR platforms (Splunk Phantom, Palo Alto Cortex XSOAR, Tines, Shuffle) enable security teams to codify incident response procedures into automated playbooks. When a SIEM alert fires, a SOAR playbook can: enrich the alert with threat intelligence, query the asset management system for ownership information, isolate the affected endpoint via EDR API, create a ticket in ServiceNow, and notify the on-call engineer via Slack — all without human intervention. The 2040 practitioner writes these playbooks in Python or low-code visual editors and tests them against simulated incidents in a digital twin environment.

### Building a Detection Pipeline

```python
# Example: Sigma rule converted to Elasticsearch query (KQL)
# Detects: Multiple failed login attempts followed by success (password spraying)
sigma_rule = """
title: Password Spraying Detection
description: Detects multiple failed logins across different accounts from same IP
logsource:
    category: authentication
detection:
    selection:
        event.outcome: failure
    timeframe: 5m
    condition: selection | count() by source.ip > 20
"""

# Practical KQL for Microsoft Sentinel / Azure Data Explorer
kql_query = """
let timeframe = 5m;
SigninLogs
| where TimeGenerated > ago(timeframe)
| where ResultType != "0"  // Failed sign-in
| summarize FailedAttempts = count(), DistinctUsers = dcount(UserPrincipalName) 
    by IPAddress, bin(TimeGenerated, 1m)
| where FailedAttempts > 20
| project TimeGenerated, IPAddress, FailedAttempts, DistinctUsers
"""
print("# Detection Query (Microsoft Sentinel KQL):")
print(kql_query)
```

### Required Reading

- Splunk, *Splunk Enterprise Security 2040: Detection and Response Playbook*.
- OCSF, *Open Cybersecurity Schema Framework Specification*, v1.3 (2039).
- Sadowski, G. (2039), *Practical Detection Engineering: From Sigma Rules to SOAR Playbooks*, O'Reilly Media.

### Discussion Questions

1. What are the limits of SIEM detection if log sources are incomplete or improperly normalised?
2. How can SOAR automation create new risks (e.g., automated containment of a false positive) and how should these be mitigated?
3. Compare Sigma rules to KQL-based detection: when would you use each?

---

## Lecture 9: Cloud Security — Defending the Ethereal Realm

### Shared Responsibility and Cloud-Native Security

Cloud security in 2040 operates under the Shared Responsibility Model: the cloud provider secures the infrastructure *of* the cloud (physical hardware, hypervisor, network fabric), while the customer secures their resources *in* the cloud (data, applications, identity, configurations). For Infrastructure-as-a-Service (IaaS), the customer's responsibility is largest. For Software-as-a-Service (SaaS), it is smallest. The IT practitioner must understand exactly where this line falls for each service model — and the 2038 Cloud Security Alliance (CSA) report found that 82% of cloud security incidents originated from customer-side misconfigurations, not provider failures.

The Cloud Security Posture Management (CSPM) tool category — Wiz, Orca Security, Prisma Cloud, Prowler (open-source) — continuously scans cloud environments for misconfigurations against benchmarks like the CIS AWS Foundations Benchmark v2.0, the CIS Azure Foundations Benchmark v3.0, and the CIS Google Cloud Platform Foundation Benchmark v2.0. In parallel, Cloud Workload Protection Platforms (CWPP) secure the workloads themselves: runtime protection for containers (Falco, Tracee), vulnerability scanning of container images (Trivy, Grype), and serverless function security (PureSec, Aqua).

### Terraform Security Scanning

```bash
# Infrastructure-as-Code security scanning pipeline example
# 1. Static analysis of Terraform code
checkov --directory terraform/ --framework terraform --output cli --soft-fail

# 2. Secret scanning to prevent credential leaks
trufflehog filesystem terraform/ --json > secret_scan.json

# 3. Policy-as-code validation with OPA/Rego
conftest test terraform/*.tf --policy policies/ --all-namespaces

# 4. Drift detection between IaC and live state
terraform plan -detailed-exitcode
```

### Identity in the Cloud

Cloud IAM deserves its own focus. The principle of least privilege is enforced through service-specific IAM systems (AWS IAM, Azure RBAC, Google Cloud IAM) where permissions are granted through policies attached to roles, groups, or service accounts. The 2040 best practice is to use **temporary credentials everywhere**: AWS STS tokens, Azure Managed Identities, GCP Service Account impersonation — never long-lived access keys. Infrastructure deployments use OIDC federation between the CI/CD pipeline and the cloud provider, eliminating the need to store cloud credentials in CI/CD secrets managers.

### Required Reading

- CSA, *Security Guidance for Critical Areas of Focus in Cloud Computing*, v5 (2039).
- CIS Benchmarks for AWS, Azure, and GCP — latest versions.
- HashiCorp, *Terraform Security Best Practices*, 2040 Edition.

### Discussion Questions

1. A developer accidentally commits an AWS access key to a public GitHub repository. What is your incident response, and what preventive measures should have been in place?
2. Compare CSPM and CWPP: what security gaps does each address, and where do they overlap?
3. How does the shift to temporary, federated credentials change the IAM threat model?

---

## Lecture 10: Governance, Risk, and Compliance (GRC)

### The Framework Landscape

Governance, Risk, and Compliance (GRC) forms the institutional memory and legal anchor of information security. Governance defines who makes security decisions and how those decisions are enforced. Risk management quantifies the likelihood and impact of security threats and guides resource allocation. Compliance demonstrates to regulators, customers, and partners that security controls meet specified standards. The 2040 GRC professional navigates a complex matrix of frameworks:

| Domain | Framework | Scope |
|--------|-----------|-------|
| General Security | ISO/IEC 27001:2039, NIST CSF 2.0 | Organisation-wide ISMS |
| Healthcare | HIPAA Security Rule, HITRUST CSF v11 | PHI protection |
| Finance | PCI DSS 5.0, SOX §404 | Payment data, financial reporting |
| Privacy | GDPR, CCPA/CPRA, LGPD, ISO 27701 | Personal data |
| Critical Infrastructure | NERC CIP, CIRCIA, DORA | Energy, finance, transport |
| AI Systems | EU AI Act (2036), ISO/IEC 42001 (2037) | AI governance |
| Cloud | CSA STAR, FedRAMP Rev. 6 | Cloud service providers |

### Risk Assessment Methodology

Quantitative risk assessment has gained ground over purely qualitative methods in the 2040 practice. The Factor Analysis of Information Risk (FAIR) model decomposes risk into measurable components:

```
Risk = f(Loss Event Frequency, Loss Magnitude)

Loss Event Frequency = Threat Event Frequency × Vulnerability
Loss Magnitude = Primary Loss + Secondary Loss
```

The IT practitioner conducts an annual risk assessment: identifying assets, enumerating threats, estimating likelihood and impact, calculating inherent risk (before controls), evaluating control effectiveness, and deriving residual risk (after controls). Residual risks above the organisation's risk appetite require treatment — either mitigation (additional controls), transfer (cyber insurance), avoidance (ceasing the activity), or acceptance (executive sign-off). The risk register becomes a living document tracked in a GRC platform (ServiceNow GRC, Archer, LogicGate, or the open-source Eramba).

### Required Reading

- ISACA, *COBIT 2040: Governance and Management Objectives for Information and Technology*.
- FAIR Institute, *FAIR Model Quantitative Risk Analysis*, v3.0.
- ISO/IEC 27001:2039, Annex A — Control Objectives and Controls.

### Discussion Questions

1. How does quantitative risk assessment (FAIR) improve security budget justification compared to qualitative "high/medium/low" ratings?
2. If residual risk exceeds risk appetite and mitigation is too expensive, what are your options as a CISO?
3. Map Yggdrasil Health's compliance obligations: which frameworks apply, and which controls overlap across them?

---

## Lecture 11: Application Security — Weaving Security into the Code

### Secure Development Lifecycle

Application security shifts security left — into the design and development phases where prevention is orders of magnitude cheaper than remediation. The Microsoft Security Development Lifecycle (SDL), the OWASP Software Assurance Maturity Model (SAMM v3.0), and NIST SSDF (Secure Software Development Framework, SP 800-218) provide structured approaches for integrating security into every phase of the SDLC: requirements, design, implementation, verification, and release. In 2040, the "shift left" philosophy has been augmented by "shift everywhere" — security testing occurs at every stage: SAST (Static Application Security Testing) at commit time, DAST (Dynamic Application Security Testing) at staging deployment, IAST (Interactive Application Security Testing) during QA testing, and RASP (Runtime Application Self-Protection) in production.

The OWASP Top 10, updated quadrennially, remains the essential taxonomy of web application risks. The 2040 edition introduced new categories: **AI Prompt Injection**, **Supply Chain Dependencies** (following the 2037 Log4Shell-scale event in the ML framework ecosystem), and **Server-Side Request Forgery in Cloud Metadata Services**. The IT practitioner must be fluent in all ten categories and know the primary prevention technique for each:

| OWASP Top 10 (2040) | Primary Prevention |
|---------------------|-------------------|
| Broken Access Control | ABAC/ReBAC with centralised policy decision point |
| Cryptographic Failures | PQC migration, key rotation automation |
| Injection (SQL, NoSQL, OS, Prompt) | Parameterised queries, input validation, prompt sanitisation |
| Insecure Design | Threat modelling, secure design patterns |
| Security Misconfiguration | IaC security scanning, immutable infrastructure |
| Vulnerable Components | SBOM management, automated dependency updates |
| Auth Failures | Passkeys, MFA, token hygiene |
| Software & Data Integrity Failures | Code signing, artifact integrity verification |
| Logging & Monitoring Failures | SIEM integration, structured logging |
| SSRF in Cloud Metadata | IMDSv2 enforcement, metadata endpoint hardening |

### SAST and Dependency Scanning in CI/CD

```yaml
# Example GitHub Actions workflow for AppSec pipeline
name: Security Scan
on: [push, pull_request]
jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: SAST — Semgrep
        run: |
          pip install semgrep
          semgrep --config=auto --error --json -o semgrep.json .
      - name: Secret Scanning — Gitleaks
        run: |
          brew install gitleaks
          gitleaks detect --source . --verbose --redact
      - name: Dependency Scan — OWASP Dependency-Check
        run: |
          mvn dependency-check:check -DfailBuildOnCVSS=7
      - name: Container Scan — Trivy
        run: |
          docker build -t yggdrasil-health:latest .
          trivy image --severity CRITICAL,HIGH --exit-code 1 yggdrasil-health:latest
```

### Required Reading

- OWASP, *Top 10 Web Application Security Risks*, 2040 Edition.
- NIST SP 800-218 (2037), *Secure Software Development Framework (SSDF)*, all sections.
- Zalewski, M. (2037), *The Tangled Web: A Guide to Securing Modern Web Applications*, 3rd ed., No Starch Press.

### Discussion Questions

1. How does "shift everywhere" differ from "shift left" in practice, and what new challenges does it introduce?
2. AI Prompt Injection is a novel threat category. How should developers of LLM-integrated applications defend against it?
3. What is the role of an SBOM (Software Bill of Materials) in supply chain security, and what are its limitations?

---

## Lecture 12: The Security Architect — Synthesis and the Path Forward

### From Practitioner to Architect

This final lecture synthesises the twelve-week journey from practitioner to security architect — a professional who does not merely operate security controls but designs the security posture of entire systems. The security architect sits at the intersection of threat modelling, cryptography, network design, IAM, vulnerability management, incident response, SIEM architecture, cloud security, GRC, and application security. Their role is to ensure that security is not bolted on but woven into every fibre of the technology stack — a spirit that the Norse tradition would recognise as the principle that "what is woven cannot be unwoven without leaving its mark."

The security architect produces **security architecture documentation**: system context diagrams, security control matrices, data flow mappings with trust boundaries, threat models with risk ratings, and control traceability matrices that map implemented controls to regulatory requirements. These artifacts are living documents, maintained in version control alongside the infrastructure code they govern. In 2040, security architecture is increasingly expressed as machine-readable policy (OPA/Rego, Cedar, Kyverno) that enforces controls automatically — architecture as code.

### The Wyrd of Security — A Heathen Reflection

In computing the final grade, the student should reflect on a deeper truth: security is not a state but a process — an ongoing weaving of the Wyrd, the Norse conception of fate as an interleaved fabric of actions and consequences. The shield-wall that held today may break tomorrow. The encryption that sufficed this year may be broken by next year's mathematics. The compliance certification obtained this quarter must be renewed next quarter. The only enduring security principle is **vigilance woven into practice** — continuous monitoring, continuous testing, continuous improvement, continuous learning.

The Norns — Urðr (what has become), Verðandi (what is becoming), and Skuld (what shall become) — offer a tripartite framework for the security mindset: learn from past incidents (Urðr), monitor the present threat landscape (Verðandi), and prepare for future threats (Skuld). The 2040 security professional who internalises this rhythmic awareness will not be paralysed by the impossibility of perfect security; instead, they will find purpose in the craft of perpetual, resilient improvement.

### Required Reading

- Stefánsson, E. (2038), *Annals of Digital Defence*, University of Yggdrasil Press, Ch. 12, "The Norns' Protocol."
- Shostack, A. (2037), *Security Architecture: Design, Deploy, and Defend*, Microsoft Press.
- Schneier, B. (2040), *Click Here to Kill Everybody: Security and Survival in a Hyperconnected World*, 2nd ed., Norton.

### Discussion Questions

1. How does the shift from "practitioner" to "architect" change the daily workflow of a security professional?
2. The Heathen framework of Urðr-Verðandi-Skuld maps to past-present-future in security. Is this a useful mental model? Why or why not?
3. What is the single most important skill a security architect needs that is NOT captured by any of the ten OWASP categories?

---

## Final Examination Preparation

The final examination for IT301 consists of two components:

### Component A: Written Examination (60%)

Choose **four** of the following eight essay questions. Each essay should be 500-750 words, demonstrate mastery of the course material, and integrate concepts from multiple lectures.

1. Critically evaluate the claim that "Zero Trust Architecture solves the security problems created by the dissolution of the network perimeter." What problems does ZTA solve, which does it leave unaddressed, and what new challenges does it create?

2. Using the Yggdrasil Health case study from Lecture 2, produce a complete threat model using STRIDE-LM. For each threat category, identify at least one concrete vulnerability, estimate its risk using CVSS v4.0, and propose a specific mitigation.

3. Explain the "harvest now, decrypt later" threat. What data categories are most exposed to this risk, and what migration strategies should organisations adopt to transition to Post-Quantum Cryptography? Evaluate at least two NIST PQC algorithms for operational suitability.

4. Design an incident response playbook for a ransomware attack against Yggdrasil Health's telemedicine platform. Address all four phases (Preparation, Detection & Analysis, Containment/Eradication/Recovery, Post-Incident Activity) and specify decision criteria for each containment action.

5. Compare and contrast SIEM and SOAR technologies. How do they complement each other in a 2040 Security Operations Centre? Provide a concrete example of a SOAR playbook triggered by a SIEM alert, including the decision logic and API integrations involved.

6. Yggdrasil Health is migrating its on-premises EHR system to a multi-cloud architecture (AWS and Azure). Design its cloud security architecture, addressing: shared responsibility mapping, CSPM tool selection, IAM design, network segmentation, and encryption strategy. Justify each design choice.

7. Using the FAIR model, conduct a quantitative risk assessment for a data breach scenario at Yggdrasil Health. Estimate loss event frequency, loss magnitude, and residual risk after controls. Discuss how this analysis would inform a cyber insurance purchasing decision.

8. The OWASP Top 10 (2040) includes "AI Prompt Injection" as a new category. Analyse this threat for Yggdrasil Health's AI diagnostic module. What specific attack vectors exist? What defensive controls — at the prompt, model, and infrastructure layers — would you implement?

### Component B: Practical Lab Examination (40%)

Students will be given a deliberately vulnerable cloud environment (simulated in a sandbox) and must:

1. Conduct reconnaissance and identify at least five distinct vulnerabilities
2. Exploit at least three of those vulnerabilities with documented steps
3. Produce a penetration test report with findings, CVSS scores, and remediation recommendations
4. Design and present a remediation plan addressing all findings
5. Write a SOAR playbook (Python or visual) that would detect and automatically contain one of the exploited vulnerabilities

### Grading Rubric

| Criterion | Weight | Excellent (A) | Good (B) | Adequate (C) | Insufficient (D/F) |
|-----------|--------|---------------|----------|--------------|-------------------|
| Technical accuracy | 30% | Flawless; correct terminology and concepts throughout | Minor errors; mostly accurate | Several errors; basic understanding | Fundamental misunderstandings |
| Analytical depth | 25% | Original synthesis; connects multiple lectures | Good analysis; some synthesis | Surface-level analysis | Descriptive only; no analysis |
| Practical applicability | 25% | Real-world operational detail; specific tools/configs | Mostly practical; some abstraction | Generic; lacks operational specifics | Purely theoretical; no practical content |
| Clarity and structure | 20% | Well-organised; clear argumentation; professional tone | Clear but some structural issues | Disorganised but readable | Incoherent or unreadable |

---

## Course Resources

### Primary Textbooks
- Stefánsson, E. (2038), *Annals of Digital Defence: Information Security in the Age of AI*, University of Yggdrasil Press.
- Schneier, B. (2040), *Click Here to Kill Everybody*, 2nd ed., Norton.
- Kim, P. (2039), *The Hacker Playbook 2040*, 4th ed., Secure Planet Press.

### Supplemental Texts
- Shostack, A. (2035), *Threat Modelling: Designing for Security*, 3rd ed., Wiley.
- Ferguson, N., Schneier, B., & Kohno, T. (2035), *Cryptography Engineering*, 2nd ed., Wiley.
- Zalewski, M. (2037), *The Tangled Web*, 3rd ed., No Starch Press.
- Sadowski, G. (2039), *Practical Detection Engineering*, O'Reilly Media.

### Standards and Frameworks (All 2038-2040 editions)
- NIST Cybersecurity Framework (CSF) 2.0
- NIST SP 800-207 Rev. 3 (Zero Trust)
- NIST SP 800-61 Rev. 3 (Incident Response)
- NIST SP 800-218 (SSDF)
- ISO/IEC 27001:2039, ISO/IEC 27701:2039, ISO/IEC 42001:2037
- CIS Controls v9
- OWASP Top 10 (2040)

### Tools
- **Network**: Nmap, Wireshark, Zeek, tcpdump
- **Vulnerability**: Nessus, OpenVAS, Nikto, Trivy, Checkov
- **Exploitation**: Metasploit, Hashcat, John the Ripper, sqlmap
- **SIEM/SOAR**: Splunk, Elastic Security, Tines, Shuffle
- **Cloud Security**: Prowler, ScoutSuite, Cloudsplaining, Falco
- **Forensics**: Volatility 4, Velociraptor, Autopsy
- **IAM**: AWS IAM Access Analyzer, Policy Sentry, Cloudsplaining
- **AppSec**: Semgrep, Gitleaks, OWASP ZAP, Burp Suite

---

*Þegar skjöldurinn brotnar, þá fléttum við nýjan.* — When the shield breaks, we weave a new one.

*Course designed and maintained by the Faculty of Information Technology, University of Yggdrasil, 2040.*
