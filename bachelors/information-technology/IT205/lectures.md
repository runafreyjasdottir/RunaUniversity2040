# IT205: Cybersecurity Fundamentals
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4  
**Description:** Cybersecurity Fundamentals

---

## Lectures

ᚠ **Lecture 1: The Security Mindset and the 2040 Threat Landscape**

**Course:** IT205 — Cybersecurity Fundamentals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Cybersecurity is not merely a technical discipline but a mindset of adversarial thinking. This opening lecture establishes the mental framework for security professionals: the ability to think like an attacker, to question assumptions, and to recognize that security is a process rather than a product. By 2040, the threat landscape has evolved from lone hackers to state-sponsored advanced persistent threats (APTs), AI-powered attacks, and quantum-enabled cryptanalysis. Students will learn to navigate this landscape with both technical skill and strategic awareness.

### Key Topics

- The CIA triad: confidentiality, integrity, and availability
- Threat actors: script kiddies, criminals, hacktivists, insiders, and nation-states
- The attack lifecycle: reconnaissance, weaponization, delivery, exploitation, installation, command and control, and actions on objectives
- AI in cybersecurity: both weapon and shield
- The 2040 threat landscape: supply chain attacks, deepfake social engineering, and quantum threats

### Lecture Notes

**Confidentiality, integrity, and availability (CIA)** remain the foundational goals of cybersecurity. **Confidentiality** ensures that information is accessible only to authorized parties. **Integrity** ensures that information is accurate and unmodified. **Availability** ensures that systems and data are accessible when needed. By 2040, two additional principles have gained prominence: **authenticity** (verifying the identity of users and systems) and **non-repudiation** (preventing denial of actions). The lecture emphasizes that security is a trade-off: maximizing confidentiality may reduce availability (e.g., multi-factor authentication adds friction); maximizing integrity may reduce performance (e.g., cryptographic verification adds latency).

**Threat actors** vary in capability, motivation, and persistence. **Script kiddies** use automated tools without deep understanding. **Criminals** seek financial gain through ransomware, fraud, and data theft. **Hacktivists** pursue political or ideological goals. **Insiders**—employees, contractors, or partners—have legitimate access and misuse it. **Nation-states (APTs)** possess advanced capabilities, unlimited resources, and strategic patience. By 2040, **AI-augmented threat actors** use large language models to generate phishing emails, write exploit code, and automate reconnaissance. The lecture profiles major APT groups of the 2030s: **GhostFleet** (attributed to a Pacific Rim nation, responsible for the 2032 maritime infrastructure compromise), **Nightingale** (attributed to a Northern European state, focused on academic and research espionage), and **Silicon Serpent** (a criminal syndicate using AI-generated ransomware).

The **attack lifecycle** (based on the Lockheed Martin Cyber Kill Chain) provides a framework for understanding and disrupting attacks. **Reconnaissance**: gathering information about targets (OSINT, social media, network scanning). **Weaponization**: creating exploits and payloads. **Delivery**: transmitting the weapon (email, web, USB). **Exploitation**: triggering the vulnerability. **Installation**: establishing persistence (backdoors, rootkits). **Command and Control (C2)**: remote communication with the attacker. **Actions on Objectives**: achieving the attacker's goal (data exfiltration, encryption, sabotage). By 2040, **AI-driven reconnaissance** automates the first three stages, but human operators still control the later stages.

**AI in cybersecurity** is dual-use. Attackers use AI to: generate convincing phishing emails (personalized via scraped social media), mutate malware to evade signature detection, and automate vulnerability discovery. Defenders use AI to: detect anomalies in network traffic, correlate alerts across systems, and predict attacker behavior. The lecture covers the **asymmetric advantage**: defenders must protect all surfaces, while attackers need find only one vulnerability. AI can narrow this asymmetry by scaling defensive analysis, but it also scales offensive capabilities.

The **2040 threat landscape** features several dominant trends. **Supply chain attacks** (compromising software vendors, open-source libraries, or CI/CD pipelines to distribute malware) have become the primary vector for widespread compromise. **Deepfake social engineering** uses AI-generated audio and video to impersonate executives, enabling fraudulent wire transfers and credential theft. **Quantum threats** (harvest now, decrypt later) involve stealing encrypted data today to decrypt it once quantum computers break current cryptography. The 2035 *Yggdrasil Supply Chain Compromise*—in which a compromised npm package exfiltrated research data from 200 institutions—demonstrated that no organization is an island.

### Required Reading

- Stallings, W., & Brown, L. (2018). *Computer Security: Principles and Practice* (4th Edition). Pearson. Chapters 1–2.
- Hutchins, E. M., et al. (2011). "Intelligence-Driven Computer Network Defense Informed by Analysis of Adversary Campaigns and Intrusion Kill Chains." *Lockheed Martin*.
- Yggdrasil Security Team (2035). "The Yggdrasil Supply Chain Compromise: Anatomy of a Multi-Institutional Breach." *UoY Security Postmortem* 2035-03.
- Yggdrasil Threat Intelligence (2040). "The 2040 Threat Actor Landscape: APTs, AI, and Criminal Syndicates." *UoY Intelligence Brief*.

### Discussion Questions

1. The CIA triad is foundational but incomplete. Should privacy, accountability, or resilience be added as explicit security goals?
2. AI-augmented attackers can generate millions of phishing emails with unique content. Can AI-based email filters keep pace, or does this create an unwinnable arms race?
3. Supply chain attacks target trust relationships. What organizational changes can reduce supply chain risk without paralyzing development velocity?
4. Quantum threats require long-term cryptographic planning. For data that must remain secret for 20 years, what migration timeline is appropriate?

### Practice Problems

- Analyze a recent public security incident (provided by the instructor). Map the attack to the Cyber Kill Chain, identify the threat actor type, and propose defensive measures for each stage.
- Research the tactics, techniques, and procedures (TTPs) of a known APT group. Document their preferred tools, targets, and indicators of compromise (IOCs).

---

ᚢ **Lecture 2: Cryptography Fundamentals**

**Course:** IT205 — Cybersecurity Fundamentals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Cryptography is the mathematical foundation of security. This lecture covers the cryptographic primitives that protect data: symmetric encryption, asymmetric encryption, hash functions, digital signatures, and key exchange. By 2040, post-quantum cryptography is being deployed alongside classical algorithms. Students will learn how these mechanisms work, when to use them, and how they can fail.

### Key Topics

- Symmetric encryption: AES, ChaCha20, modes of operation, and IV/nonce management
- Asymmetric encryption: RSA, ECC, and post-quantum alternatives (CRYSTALS-Kyber)
- Hash functions: SHA-256, SHA-3, and collision resistance
- Digital signatures: RSA-PSS, ECDSA, Ed25519, and post-quantum Dilithium
- Key exchange: Diffie-Hellman, ECDH, and hybrid post-quantum key encapsulation

### Lecture Notes

Cryptography transforms data to protect its confidentiality, integrity, and authenticity. The lecture begins with **Kerckhoffs's Principle** (1883): a cryptosystem should be secure even if everything about the system is public knowledge, except the key. This principle guides modern cryptography: algorithms are public, peer-reviewed standards; security depends solely on key secrecy.

**Symmetric encryption** uses the same key for encryption and decryption. **AES (Advanced Encryption Standard)**, standardized in 2001, remains the dominant symmetric cipher in 2040. AES operates on 128-bit blocks with keys of 128, 192, or 256 bits. **Modes of operation** define how AES encrypts data larger than one block: **CBC (Cipher Block Chaining)** (requires unpredictable IV, vulnerable to padding oracle attacks), **CTR (Counter)** (turns block cipher into stream cipher, parallelizable), **GCM (Galois/Counter Mode)** (provides authenticated encryption, combining confidentiality and integrity). By 2040, **AES-GCM** is the default for most applications, though **ChaCha20-Poly1305** (a stream cipher with built-in MAC) is preferred on devices without AES hardware acceleration. The lecture warns against **IV/nonce reuse**: reusing a nonce in GCM or ChaCha20 destroys confidentiality.

**Asymmetric encryption** uses key pairs: a public key for encryption and a private key for decryption. **RSA** (Rivest-Shamir-Adleman), based on integer factorization, has been the standard since the 1970s. **ECC (Elliptic Curve Cryptography)** provides equivalent security with smaller keys (e.g., a 256-bit ECC key is comparable to a 3072-bit RSA key). By 2040, **post-quantum asymmetric encryption** is being deployed: **CRYSTALS-Kyber** (lattice-based key encapsulation mechanism) is the NIST-selected standard for quantum-resistant encryption. The lecture covers hybrid schemes: combining classical ECC with post-quantum Kyber to ensure security even if one algorithm is broken.

**Hash functions** map arbitrary-length input to fixed-length output, with three critical properties: **preimage resistance** (given a hash, finding the input is hard), **second preimage resistance** (given an input, finding another input with the same hash is hard), and **collision resistance** (finding any two inputs with the same hash is hard). **SHA-256** and **SHA-3** are the standard secure hash functions in 2040. **MD5** and **SHA-1** are broken (collisions can be found) and must not be used for security purposes. The lecture demonstrates length extension attacks against Merkle-Damgård constructions (SHA-256) and explains why HMAC (Hash-based Message Authentication Code) is preferred over raw hashing for message authentication.

**Digital signatures** provide authentication, integrity, and non-repudiation. **RSA-PSS** (Probabilistic Signature Scheme), **ECDSA** (Elliptic Curve Digital Signature Algorithm), and **Ed25519** (a modern, fast, secure elliptic curve signature) are the dominant classical schemes. By 2040, **CRYSTALS-Dilithium** (lattice-based) is the NIST-selected post-quantum signature standard. The lecture covers signature verification: anyone with the public key can verify a signature, but only the private key holder can create one. **Certificate chains** bind public keys to identities via a chain of trust (covered in depth in IT107).

**Key exchange** establishes shared secrets over untrusted channels. **Diffie-Hellman** (classical, based on discrete logarithm) and **ECDH** (Elliptic Curve Diffie-Hellman) enable two parties to derive a shared key without transmitting it. By 2040, **hybrid post-quantum key exchange** (X25519 + Kyber) is standard in TLS 1.4. The lecture covers **forward secrecy**: ephemeral key exchange ensures that compromising a long-term key does not decrypt past sessions.

### Required Reading

- Ferguson, N., Schneier, B., & Kohno, T. (2015). *Cryptography Engineering: Design Principles and Practical Applications*. Wiley. Chapters 1–5.
- NIST (2024). *Post-Quantum Cryptography Standardization: Selected Algorithms*. NISTIR 8547.
- Bernstein, D. J., & Lange, T. (2017). "Post-Quantum Cryptography." *Nature*, 549(7671), 188–194.
- Yggdrasil Cryptography Lab (2036). "Hybrid Post-Quantum TLS: Deployment Experience at UoY." *UoY Security Research Report*.

### Discussion Questions

1. Kerckhoffs's Principle assumes algorithms are public. Does this hold for proprietary cryptography (e.g., closed-source encryption products), and what are the risks?
2. AES-GCM is fast but vulnerable to nonce reuse. For systems that cannot guarantee unique nonces (e.g., virtual machines restored from snapshots), what alternatives are safe?
3. Post-quantum algorithms have larger key and ciphertext sizes than ECC. For IoT devices with limited bandwidth, is the post-quantum overhead prohibitive?
4. Digital signatures provide non-repudiation, but private keys can be stolen. How should systems balance non-repudiation with the reality of key compromise?

### Practice Problems

- Implement AES-GCM encryption and decryption in Python using the `cryptography` library. Generate a random key and nonce, encrypt a message, and verify that tampering with the ciphertext is detected.
- Generate an Ed25519 key pair, sign a message, and verify the signature. Then demonstrate that modifying a single bit of the message invalidates the signature.

---

ᚦ **Lecture 3: Network Security**

**Course:** IT205 — Cybersecurity Fundamentals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Networks are the primary attack vector for most intrusions. This lecture covers the security mechanisms that protect network communications: firewalls, intrusion detection and prevention, VPNs, network segmentation, and zero-trust architecture. Students will learn to design secure networks that resist both external attacks and lateral movement.

### Key Topics

- Firewalls: packet filtering, stateful inspection, application-layer, and next-generation
- IDS/IPS: signature-based, anomaly-based, and behavioral detection
- VPNs: IPsec, SSL/TLS VPN, WireGuard, and zero-trust network access
- Network segmentation: VLANs, microsegmentation, and software-defined perimeters
- Zero-trust architecture: never trust, always verify

### Lecture Notes

**Firewalls** are the first line of network defense. **Packet-filtering firewalls** (iptables, nftables) inspect headers and apply rules based on source/destination IP, port, and protocol. **Stateful inspection** tracks connection state, allowing return traffic for established connections while blocking unsolicited inbound traffic. **Application-layer firewalls** (WAFs) inspect HTTP/HTTPS content for SQL injection, XSS, and other application attacks. **Next-generation firewalls (NGFWs)** combine traditional firewalling with intrusion prevention, application identification, and threat intelligence feeds. By 2040, **AI-powered firewalls** dynamically adjust rules based on observed threat patterns, though human oversight remains for critical changes.

**IDS (Intrusion Detection Systems)** monitor traffic for malicious activity, generating alerts without blocking. **IPS (Intrusion Prevention Systems)** actively block detected threats. **Signature-based detection** matches traffic against known attack patterns (Snort rules, Suricata rules). **Anomaly-based detection** establishes baselines of normal behavior and flags deviations. **Behavioral detection** correlates events across time and systems to identify multi-stage attacks. By 2040, **AI-enhanced IDS/IPS** (e.g., Darktrace, Vectra AI) use machine learning to detect novel threats without signatures, but they produce false positives that require analyst tuning.

**VPNs (Virtual Private Networks)** encrypt traffic over untrusted networks. **IPsec VPNs** operate at the network layer, encrypting all traffic between sites (site-to-site) or between a client and gateway (remote access). **SSL/TLS VPNs** operate at the application layer, providing browser-based access to internal resources. **WireGuard** (introduced 2016, widely adopted by 2025) provides a modern, fast, simple VPN protocol using Curve25519 for key exchange and ChaCha20 for encryption. By 2040, **Zero-Trust Network Access (ZTNA)** replaces traditional VPNs: rather than connecting to a network and gaining broad access, users connect to specific applications with per-session authentication and authorization.

**Network segmentation** limits the blast radius of breaches by dividing networks into isolated zones. **VLANs** provide Layer 2 segmentation. **Microsegmentation** (using host-based firewalls or SDN controllers) enforces policies between individual workloads, even within the same subnet. **Software-Defined Perimeters (SDP)** hide infrastructure from unauthorized users, requiring authentication before any network access is granted. By 2040, **software-defined networking (SDN)** enables dynamic, automated segmentation that adapts to workload changes.

**Zero-trust architecture** is the dominant security paradigm by 2040. Coined by Forrester (2010) and popularized by NIST (SP 800-207, 2020), zero-trust assumes that no user, device, or network should be implicitly trusted. Every access request is authenticated, authorized, and encrypted. Key principles: **never trust, always verify**; **assume breach** (design for containment, not just prevention); **verify explicitly** (strong authentication, least privilege); and **use least privilege access** (grant only the minimum necessary permissions). The lecture covers zero-trust implementation: identity verification (MFA, device health), microsegmentation, encryption everywhere, and continuous monitoring.

### Required Reading

- Scarfone, K., & Hoffman, P. (2009). *Guidelines on Firewalls and Firewall Policy*. NIST SP 800-41 Rev. 1.
- NIST (2020). *Zero Trust Architecture*. NIST SP 800-207.
- Donenfeld, J. A. (2017). "WireGuard: Next Generation Kernel Network Tunnel." *NDSS*.
- Yggdrasil Network Security Team (2038). "Microsegmentation in the 2030s: SDN and Host-Based Enforcement." *UoY Security Report*.

### Discussion Questions

1. AI-powered firewalls adapt rules dynamically. Could an attacker poison the AI model to create permissive rules, and how would such an attack be detected?
2. Zero-trust requires continuous authentication, which adds latency. For a high-frequency trading application, is zero-trust compatible with sub-millisecond response requirements?
3. VPNs provide network-layer access, while ZTNA provides application-layer access. For remote workers needing access to multiple systems, is ZTNA always superior?
4. Anomaly-based IDS produces false positives that waste analyst time. What tuning strategies balance detection sensitivity with operational feasibility?

### Practice Problems

- Configure a pfSense firewall with rules for a three-zone network: DMZ, internal, and management. Allow HTTP/HTTPS from DMZ to internal, SSH only from management, and deny all other traffic. Test with `nmap` and document the results.
- Implement a WireGuard VPN between two Linux servers. Verify encryption with `tcpdump`, test failover by disconnecting one endpoint, and measure throughput compared to unencrypted traffic.

---

ᚨ **Lecture 4: Host and Endpoint Security**

**Course:** IT205 — Cybersecurity Fundamentals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Networks can be secured, but endpoints remain vulnerable. This lecture covers the protection of individual systems: servers, workstations, mobile devices, and IoT endpoints. Students will learn to harden operating systems, deploy endpoint protection, manage vulnerabilities, and respond to endpoint compromises.

### Key Topics

- OS hardening: patching, configuration baselines, and minimal installation
- Endpoint protection: antivirus, EDR, XDR, and application control
- Vulnerability management: scanning, prioritization, and patching workflows
- Mobile and IoT security: MDM, firmware updates, and device authentication
- Endpoint detection: behavioral analysis, threat hunting, and forensic preservation

### Lecture Notes

**OS hardening** reduces attack surface by eliminating unnecessary features and enforcing secure configurations. **Patching** applies security updates promptly: critical patches within 24 hours, high-priority within 7 days. **Configuration baselines** (CIS Benchmarks, DISA STIGs) define hardened states for operating systems and applications. **Minimal installation** removes unused software, services, and features that could harbor vulnerabilities. By 2040, **immutable infrastructure** (read-only OS images, containers, and micro-VMs) eliminates runtime modification, preventing persistent malware.

**Endpoint protection** has evolved beyond traditional antivirus. **Antivirus (AV)** detects known malware via signatures. **EDR (Endpoint Detection and Response)** monitors endpoint behavior in real time, detecting anomalous processes, network connections, and file modifications. **XDR (Extended Detection and Response)** correlates endpoint data with network and cloud telemetry for holistic threat detection. **Application control** (AppLocker, Windows Defender Application Control) allows only approved executables to run, preventing malware execution. By 2040, **AI-driven EDR** (CrowdStrike Falcon, Microsoft Defender for Endpoint) provides autonomous threat detection and response, isolating compromised endpoints without human intervention.

**Vulnerability management** is a continuous cycle of discovery, assessment, remediation, and verification. **Scanning** (Nessus, Qualys, OpenVAS) identifies missing patches, misconfigurations, and known vulnerabilities. **Prioritization** uses risk scoring (CVSS, EPSS, and threat intelligence) to focus on vulnerabilities actively exploited in the wild. **Patching workflows** define SLAs, testing procedures, and rollback plans. By 2040, **risk-based vulnerability management** (RBVM) uses AI to predict which vulnerabilities are most likely to be exploited in a specific environment, prioritizing remediation accordingly.

**Mobile and IoT security** addresses the proliferation of non-traditional endpoints. **MDM (Mobile Device Management)** enforces policies on smartphones and tablets: encryption, PIN requirements, remote wipe, and app whitelisting. **IoT security** is challenging due to diverse devices, limited compute resources, and long lifecycles. Best practices: network segmentation (isolating IoT devices from critical systems), firmware update automation, strong device authentication (certificates, not passwords), and device inventory (knowing what is connected). By 2040, **IoT security frameworks** (Matter, ioXT) provide standardized security requirements, but legacy devices remain vulnerable.

**Endpoint detection and response** requires proactive hunting, not just reactive alerts. **Threat hunting** assumes compromise and searches for indicators of attack (IoAs) that evade automated detection. **Forensic preservation** captures memory dumps, disk images, and log files before evidence is lost. The lecture covers the **order of volatility**: capture RAM first (lost on reboot), then disk (may be encrypted or wiped), then logs. By 2040, **automated forensic pipelines** (Velociraptor, KAPE) collect and analyze endpoint artifacts at scale.

### Required Reading

- NIST (2035). *Guide to Malware Incident Prevention and Handling*. NIST SP 800-83 Rev. 2.
- Microsoft (2040). *Microsoft Defender for Endpoint Documentation*. Microsoft Learn.
- FIRST (2040). *EPSS: Exploit Prediction Scoring System*. first.org/epss.
- Yggdrasil Endpoint Security Team (2037). "The IoT Botnet of 2037: 100,000 Compromised Smart Devices." *UoY Security Postmortem*.

### Discussion Questions

1. Immutable infrastructure prevents malware persistence but complicates troubleshooting. How should organizations balance immutability against the need for rapid incident response?
2. AI-driven EDR can autonomously isolate endpoints. Should this autonomy be absolute, or should critical isolations require human approval?
3. IoT devices often lack update mechanisms and have lifespans of 10+ years. For a smart building with 5,000 IoT sensors, what security architecture protects against unpatchable vulnerabilities?
4. Threat hunting assumes compromise, but most hunts find nothing. How should organizations justify the cost of threat hunting programs?

### Practice Problems

- Harden a Windows 11 workstation using the CIS benchmark. Apply at least 20 recommendations, document each change, and verify compliance with Microsoft Security Compliance Toolkit.
- Conduct a threat hunt on a provided endpoint image. Use Velociraptor or a similar tool to identify suspicious processes, network connections, and persistence mechanisms. Document your hunting hypothesis and findings.

---

ᚱ **Lecture 5: Application Security**

**Course:** IT205 — Cybersecurity Fundamentals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Applications are the ultimate target of most attacks. This lecture covers the secure development lifecycle and the vulnerabilities that plague software: injection, authentication flaws, insecure design, and vulnerable dependencies. Students will learn to identify, exploit (in controlled environments), and remediate common application vulnerabilities.

### Key Topics

- The OWASP Top 10: injection, broken authentication, sensitive data exposure, and more
- Secure development: SAST, DAST, SCA, and IaC scanning
- Authentication and session management: MFA, OAuth, JWT, and session fixation
- Input validation and output encoding: preventing injection attacks
- Software supply chain security: SBOMs, dependency scanning, and signed builds

### Lecture Notes

**The OWASP Top 10** (updated every 3–4 years) lists the most critical web application security risks. By 2040, the list has stabilized around persistent issues: **Injection** (SQL, NoSQL, OS command, LDAP), **Broken Authentication** (weak passwords, session hijacking, credential stuffing), **Sensitive Data Exposure** (unencrypted storage, weak cryptography), **Insecure Design** (flawed architecture, missing security controls), **Security Misconfiguration** (default credentials, unnecessary features, verbose error messages), **Vulnerable and Outdated Components** (known CVEs in dependencies), **Identification and Authentication Failures** (MFA bypass, brute force), **Software and Data Integrity Failures** (CI/CD compromises, unsigned updates), **Security Logging and Monitoring Failures** (insufficient logging, missed detection), and **Server-Side Request Forgery (SSRF)**. The lecture provides a detailed analysis of each risk with exploitation examples and mitigation strategies.

**Secure development** integrates security into the software lifecycle. **SAST (Static Application Security Testing)** analyzes source code for vulnerabilities without execution. **DAST (Dynamic Application Security Testing)** tests running applications by sending malicious inputs. **SCA (Software Composition Analysis)** scans dependencies for known vulnerabilities. **IaC scanning** (Checkov, tfsec) identifies security issues in infrastructure code. By 2040, **AI-powered code review** (GitHub Copilot Security, Amazon CodeWhisperer) suggests secure code patterns and flags potential vulnerabilities during development.

**Authentication and session management** verify user identity and maintain state. **MFA (Multi-Factor Authentication)** requires two or more factors: something you know (password), something you have (token, phone), or something you are (biometric). **OAuth 2.1** (standardized 2024, refined through 2040) enables delegated authorization without password sharing. **JWT (JSON Web Tokens)** carry authentication state but must be protected against theft and replay. **Session fixation** occurs when an attacker sets a user's session ID, then uses it after authentication. Mitigations: rotate session IDs on login, enforce secure and HttpOnly cookies, and implement short session timeouts.

**Input validation and output encoding** prevent injection attacks. **Input validation** rejects or sanitizes untrusted data before processing (whitelist validation: accept only known-good patterns). **Output encoding** escapes special characters when rendering data in different contexts (HTML encoding for web pages, SQL parameterization for queries, command array invocation for shell commands). The lecture demonstrates: a SQL injection attack (`' OR '1'='1`), its prevention via parameterized queries, and a reflected XSS attack (`<script>alert(1)</script>`), its prevention via HTML encoding.

**Software supply chain security** addresses the risk of compromised dependencies. **SBOMs (Software Bills of Materials)** list all components in a software product, enabling vulnerability tracking. **Dependency scanning** (Snyk, Dependabot, OWASP Dependency-Check) identifies known vulnerabilities in open-source libraries. **Signed builds** cryptographically verify that software artifacts were produced by trusted build systems. By 2040, **reproducible builds** (producing bit-for-bit identical outputs from source) and **attestation frameworks** (SLSA, Sigstore) provide end-to-end supply chain integrity.

### Required Reading

- OWASP (2040). *OWASP Top 10: Web Application Security Risks*. OWASP Foundation.
- OWASP (2040). *OWASP Cheat Sheet Series: Input Validation, Authentication, Session Management*. OWASP.
- NIST (2033). *Software Supply Chain Security Guidance*. NIST SP 800-204D.
- Yggdrasil Application Security Team (2036). "The CI/CD Compromise: When Build Pipelines Become Attack Vectors." *UoY Security Postmortem*.

### Discussion Questions

1. AI code review tools suggest secure patterns but can also generate vulnerable code. How should teams integrate AI assistance without creating false confidence?
2. MFA significantly improves security but adds friction. For consumer-facing applications, what MFA methods (SMS, TOTP, WebAuthn, passkeys) balance security and usability?
3. Reproducible builds ensure integrity but require strict control over build environments. For a team using cloud CI/CD, is reproducibility achievable?
4. The OWASP Top 10 has remained relatively stable for decades. Does this indicate that application security is a solved problem, or that attackers and defenders are stuck in an equilibrium?

### Practice Problems

- Perform a security audit of a provided web application. Identify vulnerabilities from the OWASP Top 10, exploit them in a controlled environment, and propose mitigations. Document each finding with CVSS scoring.
- Generate an SBOM for an open-source project using Syft or a similar tool. Identify vulnerable dependencies, research available patches, and propose an update strategy.

---

ᚲ **Lecture 6: Identity and Access Management**

**Course:** IT205 — Cybersecurity Fundamentals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Identity is the perimeter of modern security. This lecture covers the technologies and practices that manage digital identities: authentication, authorization, federation, and privileged access management. Students will learn to design identity architectures that are both secure and usable.

### Key Topics

- Authentication: passwords, MFA, biometrics, and passwordless authentication
- Authorization: RBAC, ABAC, PBAC, and policy engines
- Identity federation: SAML, OAuth, OIDC, and decentralized identity
- Privileged Access Management (PAM): vaulting, session recording, and just-in-time access
- Identity governance: lifecycle management, access reviews, and compliance

### Lecture Notes

**Authentication** verifies who you are. **Passwords**, despite decades of criticism, persist in 2040 but are increasingly supplemented or replaced. **MFA** (covered in Lecture 5) adds layers. **Biometrics** (fingerprint, facial recognition, iris scan) provide convenience but raise privacy concerns and can be spoofed. **Passwordless authentication** (WebAuthn, FIDO2, passkeys) uses public-key cryptography: the device stores a private key and presents a signed challenge to authenticate. By 2040, **passkeys** (synchronized across devices via cloud keychains) are the default for consumer services, while **hardware security keys** (YubiKey, Titan) protect high-value accounts.

**Authorization** determines what you can do. **RBAC (Role-Based Access Control)** assigns permissions to roles, which are granted to users. **ABAC (Attribute-Based Access Control)** evaluates policies based on user attributes, resource attributes, and environmental conditions. **PBAC (Policy-Based Access Control)** uses a centralized policy engine (Open Policy Agent, AWS IAM Policies) to evaluate decisions. By 2040, **ReBAC (Relationship-Based Access Control)** models permissions as graph relationships (Google Zanzibar), enabling fine-grained access control for complex hierarchies.

**Identity federation** enables single sign-on (SSO) across organizational boundaries. **SAML (Security Assertion Markup Language)** is the legacy enterprise standard for web SSO. **OAuth 2.1** and **OpenID Connect (OIDC)** are the modern standards, enabling delegated authorization and authentication across platforms. By 2040, **decentralized identity** (DIDs, Verifiable Credentials) allows users to control their own identity without relying on centralized providers. The UoY **Yggdrasil ID** (2038) issues Verifiable Credentials for students and staff, enabling passwordless access to partner institutions.

**Privileged Access Management (PAM)** protects administrative accounts. **Vaulting** stores privileged credentials in a secure vault (HashiCorp Vault, CyberArk), releasing them only upon approval. **Session recording** captures all actions performed with privileged accounts, creating an audit trail. **Just-in-time (JIT) access** grants elevated privileges only for a specific task and time period, reducing standing administrative access. By 2040, **JIT access is mandatory** for all UoY administrative accounts, with automatic revocation after the approved window.

**Identity governance** ensures that access rights are appropriate and compliant. **Lifecycle management** automates provisioning (new employee gets standard access), changes (role transfer updates permissions), and deprovisioning (termination removes all access). **Access reviews** require managers to periodically certify that their team members' access is still necessary. **Compliance reporting** demonstrates adherence to regulations (SOX, HIPAA, GDPR) with audit trails of who had access to what and when. By 2040, **AI-driven identity analytics** detect anomalous access patterns (e.g., an employee accessing systems outside their role) and trigger automatic reviews.

### Required Reading

- Windley, P. J. (2005). *Digital Identity*. O'Reilly. (Updated concepts for 2040.)
- Hardt, D. (2012). *The OAuth 2.0 Authorization Framework*. RFC 6749. IETF.
- W3C (2030). *Decentralized Identifiers (DIDs) v2.0*. W3C Recommendation.
- Yggdrasil Identity Team (2038). "Yggdrasil ID: Decentralized Identity for Higher Education." *UoY Identity Research Report*.

### Discussion Questions

1. Passkeys eliminate passwords but create dependency on device manufacturers (Apple, Google). Is this centralization a privacy risk, or do the security benefits outweigh concerns?
2. ReBAC provides fine-grained control but requires modeling all relationships. For a university with 50,000 users and complex organizational hierarchies, is ReBAC scalable?
3. JIT access reduces standing privilege but can slow down emergency response. What break-glass procedures enable rapid access during critical incidents?
4. AI-driven identity analytics can flag anomalous access, but anomalies are not always malicious. How should organizations balance automated enforcement with human review?

### Practice Problems

- Design an RBAC model for a university IT department. Define roles, permissions, and inheritance hierarchies. Implement it in a directory service (Active Directory or OpenLDAP) and test access scenarios.
- Configure HashiCorp Vault for dynamic secret generation. Create a policy that allows an application to request database credentials with a 1-hour TTL. Verify that credentials are automatically revoked after expiration.

---

ᚷ **Lecture 7: Security Operations and Monitoring**

**Course:** IT205 — Cybersecurity Fundamentals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Security operations (SecOps) is the continuous practice of monitoring, detecting, and responding to security events. This lecture covers the Security Operations Center (SOC), SIEM platforms, threat intelligence, and the workflows that transform raw alerts into actionable intelligence. By 2040, AI augments but does not replace human analysts.

### Key Topics

- SOC structure: tiers, roles, and the incident response lifecycle
- SIEM: Splunk, Sentinel, QRadar, and open-source alternatives (Wazuh, Elastic SIEM)
- Threat intelligence: feeds, sharing platforms (MISP), and indicator lifecycle
- Log management: collection, parsing, retention, and correlation
- Automation: SOAR platforms, playbooks, and alert enrichment

### Lecture Notes

The **Security Operations Center (SOC)** is the organizational unit responsible for continuous security monitoring. **Tier 1 analysts** triage alerts, performing initial validation and escalation. **Tier 2 analysts** investigate confirmed incidents, performing deeper analysis and containment. **Tier 3 analysts** (threat hunters, incident responders) handle complex threats and proactive hunting. **SOC managers** oversee operations, metrics, and strategy. By 2040, **AI analysts** (covered in Lecture 1) handle routine triage, escalating only novel or high-confidence threats to humans.

**SIEM (Security Information and Event Management)** platforms aggregate, correlate, and analyze security data from across the organization. **Splunk** (dominant enterprise SIEM) provides powerful search and visualization. **Microsoft Sentinel** (cloud-native) provides AI-driven analytics and SOAR integration. **IBM QRadar** provides network flow analysis and behavioral analytics. **Open-source alternatives**: **Wazuh** (fork of OSSEC, providing HIDS and SIEM), **Elastic SIEM** (built on the ELK stack), and **Apache Metron**. The lecture covers SIEM architecture: log collection (agents, syslog, API), parsing (normalization into a common schema), storage (hot/warm/cold tiers), correlation rules (detecting multi-event patterns), and alerting.

**Threat intelligence** provides context about threats. **Feeds** (commercial and open-source) deliver IOCs (Indicators of Compromise): IP addresses, domain names, file hashes, and behavioral patterns. **MISP (Malware Information Sharing Platform)** enables structured threat sharing between organizations. **STIX/TAXII** (Structured Threat Information Expression / Trusted Automated Exchange of Intelligence Information) standardizes threat data format and transport. By 2040, **AI-generated threat intelligence** predicts emerging threats by analyzing dark web chatter, vulnerability disclosures, and attack patterns. The lecture emphasizes **indicator lifecycle**: IOCs have limited shelf life; attackers change infrastructure frequently. Stale IOCs produce false positives and wasted analyst time.

**Log management** is the foundation of security monitoring. **Collection**: forwarding logs from endpoints, network devices, cloud services, and applications to a central platform. **Parsing**: extracting structured fields from unstructured log formats. **Retention**: storing logs for compliance (often 1–7 years) and investigation (hot storage for 30–90 days, cold storage for long-term). **Correlation**: linking events across systems to identify multi-stage attacks. By 2040, **AI log summarization** compresses millions of events into narrative incident descriptions, reducing analyst cognitive load.

**SOAR (Security Orchestration, Automation, and Response)** platforms automate repetitive tasks. **Playbooks** define automated workflows: when an alert fires, enrich it with threat intelligence, query related systems, create a ticket, and if confidence is high, block the IP. **Alert enrichment** adds context (user identity, asset criticality, threat intelligence) to raw alerts, enabling faster triage. By 2040, **autonomous response** (blocking threats without human approval) is common for low-risk actions, but high-impact actions (isolating a production server) require human confirmation.

### Required Reading

- Jared, R. (2019). *Security Operations Center: Building, Operating, and Maintaining Your SOC*. Cisco Press. (Updated for 2040 context.)
- Splunk (2040). *Splunk Enterprise Security: Implementation and Best Practices*. Splunk Docs.
- MISP Project (2040). *MISP Documentation: Threat Sharing Platform*. MISP Project.
- Yggdrasil SOC (2039). "AI-Augmented Security Operations: One Year of Ratatoskr in the SOC." *UoY Security Operations Report*.

### Discussion Questions

1. AI analysts handle routine triage, but who is accountable when an AI misses a critical alert? Is the vendor, the SOC manager, or the organization responsible?
2. Threat intelligence feeds can contain false positives or even poisoned data from adversaries. What validation processes ensure feed trustworthiness?
3. SIEM storage costs scale with data volume. For an organization generating 5TB of logs daily, what retention and sampling strategies balance cost with investigative capability?
4. Autonomous response improves speed but can disrupt legitimate activity. What safeguards prevent SOAR playbooks from causing business outages?

### Practice Problems

- Deploy Wazuh or Elastic SIEM in a lab environment. Configure agents on Linux and Windows endpoints, create detection rules for common attacks (brute force, malware execution), and build a dashboard showing alert trends and top threats.
- Write a SOAR playbook (using a platform like Shuffle or Splunk Phantom) that: enriches a phishing alert with email headers and URL reputation, quarantines the email, blocks the URL at the firewall, and notifies the user. Test with a simulated phishing email.

---

ᚹ **Lecture 8: Incident Response**

**Course:** IT205 — Cybersecurity Fundamentals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Despite all preventive measures, incidents occur. This lecture covers the structured approach to detecting, containing, eradicating, and recovering from security incidents. Students will learn to lead incident response, preserve evidence, communicate with stakeholders, and conduct post-incident reviews that prevent recurrence.

### Key Topics

- The incident response lifecycle: preparation, detection, analysis, containment, eradication, recovery, and post-incident activity
- Incident classification: severity, scope, and impact assessment
- Forensics: evidence collection, chain of custody, and analysis
- Communication: internal notification, external disclosure, and regulatory reporting
- Post-incident review: blameless postmortems, improvement tracking, and metrics

### Lecture Notes

**Preparation** is the foundation of effective incident response. **Incident response plan**: a documented procedure defining roles, responsibilities, communication channels, and escalation paths. **Playbooks**: step-by-step guides for common incident types (ransomware, data breach, insider threat, DDoS). **Tools**: forensic workstations, network taps, memory capture tools, and isolated analysis environments. **Training**: tabletop exercises, red team engagements, and simulated incidents. By 2040, **AI-generated scenarios** create realistic training simulations based on current threat intelligence.

**Detection** identifies that an incident is occurring. **Automated detection**: SIEM alerts, EDR notifications, IDS signatures, and anomaly detection. **Manual detection**: user reports, third-party notifications, and threat hunting discoveries. **Triage**: classifying incidents by severity (Critical: active data exfiltration; High: confirmed compromise; Medium: suspicious activity; Low: policy violation). The lecture covers the **incident ticket**: documenting initial observations, affected systems, timeline, and assigned responder.

**Analysis** determines what happened, how, and why. **Timeline reconstruction**: correlating events across logs to establish the attack sequence. **Scope assessment**: identifying all affected systems, accounts, and data. **Root cause analysis**: determining the initial vector (phishing, unpatched vulnerability, stolen credentials). By 2040, **AI timeline reconstruction** automatically correlates events and suggests attack paths, validated by human analysts.

**Containment** prevents further damage. **Short-term containment**: isolating affected systems (network disconnection, account disablement, IP blocking) without destroying evidence. **Long-term containment**: applying patches, changing credentials, and implementing monitoring while preparing for eradication. The lecture warns against **over-containment**: disconnecting an entire datacenter for a single compromised workstation disrupts business unnecessarily.

**Eradication** removes the attacker's presence. **Malware removal**: antivirus scans, reimaging affected systems, and validating clean state. **Backdoor elimination**: reviewing startup items, scheduled tasks, and authorized keys for persistence mechanisms. **Vulnerability remediation**: patching the root cause. By 2040, **automated eradication** (reimaging compromised endpoints from golden images, rotating credentials via vaults) reduces response time.

**Recovery** restores normal operations. **System restoration**: rebuilding from clean backups, verifying integrity, and monitoring for recurrence. **Service restoration**: bringing systems online in priority order (critical services first). **Validation**: confirming that restored systems are clean and functional. The lecture covers **prolonged recovery**: some incidents (e.g., ransomware with data destruction) require weeks or months of rebuilding.

**Post-incident review** transforms incidents into learning opportunities. **Blameless postmortems** focus on systemic failures, not individual blame. **Five Whys** (iteratively asking "why" to find root causes) and **fishbone diagrams** (Ishikawa) structure the analysis. **Improvement tracking**: assigning action items with owners and deadlines. **Metrics**: Mean Time to Detect (MTTD), Mean Time to Respond (MTTR), and recurrence rate. By 2040, **automated postmortem generation** drafts incident summaries from timeline data, which human reviewers refine.

### Required Reading

- Cichonski, P., et al. (2012). *Computer Security Incident Handling Guide*. NIST SP 800-61 Rev. 2.
- SANS Institute (2040). *Incident Handler's Handbook*. SANS Reading Room.
- Allspaw, J. (2012). "Blameless Postmortems and a Just Culture." *Etsy Code as Craft*.
- Yggdrasil Incident Response Team (2037). "The Ransomware Recovery of 2037: 45 Days from Encryption to Full Restoration." *UoY IR Postmortem*.

### Discussion Questions

1. Blameless postmortems aim to create psychological safety, but some incidents involve clear negligence. How should organizations balance blamelessness with accountability?
2. Automated eradication is fast but can destroy forensic evidence. For incidents requiring law enforcement involvement, should eradication be delayed for evidence preservation?
3. MTTR (Mean Time to Respond) is a common metric, but it can be gamed by classifying incidents as low severity. What complementary metrics ensure meaningful measurement?
4. AI-generated training simulations are realistic but may desensitize responders. How should organizations maintain the urgency and emotional engagement of live incidents?

### Practice Problems

- Conduct a tabletop exercise for a ransomware incident. Assign roles (incident commander, technical lead, communications lead, legal counsel) and walk through each phase of the response. Document decisions, timelines, and gaps.
- Analyze a provided incident timeline (logs from a compromised system). Reconstruct the attack sequence, identify the initial vector, assess scope, and propose containment and eradication steps.

---

ᚺ **Lecture 9: Risk Management and Compliance**

**Course:** IT205 — Cybersecurity Fundamentals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Security is a risk management discipline. This lecture covers the frameworks and practices that identify, assess, and mitigate security risks while satisfying regulatory requirements. Students will learn to speak the language of risk: threats, vulnerabilities, likelihood, impact, and control effectiveness.

### Key Topics

- Risk management frameworks: NIST RMF, ISO 27005, FAIR, and OCTAVE
- Risk assessment: asset inventory, threat modeling, and vulnerability analysis
- Risk treatment: acceptance, mitigation, transfer, and avoidance
- Compliance: GDPR, HIPAA, PCI-DSS, SOC 2, and industry-specific regulations
- Audit and assurance: internal audits, third-party assessments, and continuous compliance

### Lecture Notes

**Risk** is the potential for loss or harm. In cybersecurity, risk arises from the intersection of **threats** (adversaries, accidents, natural events), **vulnerabilities** (weaknesses in systems or processes), and **impact** (financial, reputational, operational, legal). **Risk = Threat × Vulnerability × Impact** (qualitatively) or quantitatively via models like FAIR (Factor Analysis of Information Risk).

**Risk management frameworks** provide structured approaches. **NIST RMF (Risk Management Framework)** provides a seven-step process: Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor. **ISO 27005** provides guidelines for information security risk management. **FAIR** provides quantitative risk analysis using probability and financial impact. **OCTAVE** (Operationally Critical Threat, Asset, and Vulnerability Evaluation) is a self-directed risk assessment for organizations. By 2040, **AI-assisted risk assessment** automatically identifies assets, discovers vulnerabilities, and calculates risk scores, but human judgment remains essential for contextual factors.

**Risk assessment** identifies and evaluates risks. **Asset inventory**: cataloging hardware, software, data, and personnel. **Threat modeling** (STRIDE, PASTA, attack trees) identifies how adversaries could attack systems. **Vulnerability analysis** (scanning, penetration testing, code review) identifies weaknesses. **Risk scoring**: combining likelihood and impact into a priority matrix (Critical, High, Medium, Low). The lecture demonstrates a risk register: a spreadsheet or database tracking each risk, its owner, mitigation status, and residual risk.

**Risk treatment** addresses identified risks. **Acceptance**: acknowledging the risk and its potential impact (appropriate for low risks or when mitigation cost exceeds impact). **Mitigation**: implementing controls to reduce likelihood or impact (firewalls, encryption, training). **Transfer**: shifting risk to another party (cyber insurance, outsourcing). **Avoidance**: eliminating the risk by discontinuing the activity (shutting down a vulnerable legacy system). By 2040, **cyber insurance** is standard for enterprises, with premiums tied to risk posture (verified by third-party assessments).

**Compliance** satisfies legal and regulatory requirements. **GDPR** (EU, 2018, amended 2030) governs personal data protection. **HIPAA** (U.S.) governs health information. **PCI-DSS** governs payment card data. **SOC 2** (Service Organization Control) attests to security controls for service providers. By 2040, **the Global Data Protection Accord** (2034) harmonizes privacy standards across 80 nations, and **AI regulations** (EU AI Act 2030, U.S. AI Bill of Rights 2032) add algorithmic accountability requirements. The lecture maps common controls (encryption, access logging, data retention) to regulatory requirements.

**Audit and assurance** verify that controls are effective. **Internal audits** (conducted by the organization) assess compliance and control effectiveness. **Third-party assessments** (penetration tests, SOC 2 audits, ISO 27001 certifications) provide independent validation. **Continuous compliance** monitoring (automated scanning, policy-as-code, real-time dashboards) replaces periodic audits with ongoing verification. By 2040, **blockchain-based audit trails** (UoY's Bifröst system) provide tamper-evident compliance records.

### Required Reading

- NIST (2018). *Risk Management Framework for Information Systems and Organizations*. NIST SP 800-37 Rev. 2.
- Freund, J., & Jones, J. (2014). *Measuring and Managing Information Risk: Using FAIR*. Butterworth-Heinemann.
- ISO/IEC (2018). *ISO/IEC 27005:2018 Information Security Risk Management*. ISO.
- Yggdrasil Compliance Team (2034). "The Global Data Protection Accord: Implementation at UoY." *UoY Compliance Report*.

### Discussion Questions

1. Quantitative risk analysis (FAIR) produces financial estimates, but security incidents often cause intangible harm (reputation, trust). How should risk assessments account for non-financial impacts?
2. Cyber insurance transfers risk but can create moral hazard (organizations may under-invest in security knowing insurance covers losses). How should insurers incentivize security investment?
3. Continuous compliance monitoring reduces audit burden but increases operational overhead. For a small organization, is continuous monitoring feasible, or should periodic audits suffice?
4. Blockchain-based audit trails are tamper-evident but not tamper-proof (a 51% attack could alter records). For what compliance use cases is blockchain appropriate?

### Practice Problems

- Conduct a risk assessment for a fictional e-commerce company. Identify assets, threats, and vulnerabilities. Score risks using a qualitative matrix and a FAIR-like quantitative approach. Propose mitigations and calculate residual risk.
- Map the controls of a provided security policy to GDPR, HIPAA, and PCI-DSS requirements. Identify gaps and propose remediation.

---

ᚾ **Lecture 10: Malware and Threat Actors**

**Course:** IT205 — Cybersecurity Fundamentals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Malware is the weapon of the digital age. This lecture covers the taxonomy of malicious software, the techniques used by threat actors, and the defenses that protect against them. By 2040, malware has evolved to include AI-generated payloads, fileless attacks, and living-off-the-land techniques that evade traditional detection.

### Key Topics

- Malware taxonomy: viruses, worms, trojans, ransomware, spyware, rootkits, and bootkits
- Attack techniques: phishing, spear phishing, watering holes, and supply chain compromise
- Fileless malware: PowerShell-based attacks, reflective DLL injection, and LOLBAS
- Ransomware evolution: encryption, double extortion, triple extortion, and RaaS
- Defense strategies: endpoint protection, network segmentation, and backup resilience

### Lecture Notes

**Malware taxonomy** classifies malicious software by behavior. **Viruses** attach to legitimate programs and spread when executed. **Worms** self-replicate across networks without user action. **Trojans** masquerade as legitimate software. **Ransomware** encrypts data and demands payment for decryption. **Spyware** steals information (keyloggers, screen capture). **Rootkits** hide deep in the OS, concealing malware presence. **Bootkits** infect the boot process, loading before the OS. By 2040, **AI-generated malware** mutates its code to evade signature detection, and **polymorphic malware** changes its appearance on every infection.

**Attack techniques** deliver malware to targets. **Phishing** (mass email with malicious links/attachments) remains the most common vector. **Spear phishing** targets specific individuals with personalized content (often using OSINT and AI-generated text). **Watering hole attacks** compromise websites frequented by the target audience. **Supply chain compromise** (covered in Lecture 1) injects malware into trusted software. By 2040, **deepfake phishing** uses AI-generated voice and video to impersonate executives, with a 400% increase in business email compromise (BEC) losses between 2030 and 2040.

**Fileless malware** avoids writing files to disk, evading signature-based detection. **PowerShell-based attacks** execute malicious scripts in memory. **Reflective DLL injection** loads malicious libraries directly into process memory. **LOLBAS (Living Off The Land Binaries And Scripts)** uses legitimate system tools (PowerShell, WMI, certutil) for malicious purposes. By 2040, **memory-only implants** (malware that exists solely in RAM, never touching disk) require behavioral detection and memory forensics.

**Ransomware** has evolved through stages. **First generation** (2010s): encrypts files, demands Bitcoin payment. **Double extortion** (2020s): encrypts files and threatens to leak stolen data. **Triple extortion** (2030s): encrypts, leaks data, and threatens DDoS against victims who refuse to pay. **RaaS (Ransomware as a Service)** enables non-technical criminals to launch attacks using pre-built ransomware platforms (affiliate model). By 2040, **AI-optimized ransomware** automatically identifies the most valuable data to encrypt and negotiates payment amounts based on victim financial analysis.

**Defense strategies** against malware are layered. **Prevention**: email filtering, web filtering, application control, and user training. **Detection**: EDR, behavioral analysis, and threat hunting. **Containment**: network segmentation, endpoint isolation, and account lockout. **Recovery**: immutable backups, disaster recovery plans, and incident response. The lecture emphasizes that **no single control is sufficient**: defense in depth requires multiple overlapping protections. The 2037 *Yggdrasil Ransomware Defense*—in which layered controls (application control blocked initial execution, EDR detected lateral movement, network segmentation limited spread, and immutable backups enabled recovery without payment)—demonstrates effective defense.

### Required Reading

- Sikorski, M., & Honig, A. (2012). *Practical Malware Analysis: The Hands-On Guide to Dissecting Malicious Software*. No Starch Press.
- MITRE ATT&CK Framework (2040). *ATT&CK for Enterprise: Techniques and Sub-techniques*. MITRE.
- Yggdrasil Malware Analysis Lab (2040). "AI-Generated Malware: A Technical Analysis of 2039 Campaigns." *UoY Security Research Report*.
- Yggdrasil Incident Response (2037). "The Yggdrasil Ransomware Defense: Layered Controls in Action." *UoY IR Case Study*.

### Discussion Questions

1. AI-generated malware evades signature detection but may still exhibit behavioral patterns. Can behavioral detection keep pace with AI-generated threats, or does this create another arms race?
2. Ransomware payments fund criminal organizations, yet some victims have no recovery alternative. Should governments ban ransom payments, and what support would victims need?
3. Fileless malware uses legitimate tools, making detection difficult. Does this mean application whitelisting (blocking all unauthorized executables) should be mandatory?
4. Deepfake phishing undermines voice and video as authentication factors. What replacement authentication methods are viable for high-value transactions?

### Practice Problems

- Analyze a provided malware sample (in a sandboxed environment). Identify its type, infection vector, persistence mechanisms, network communication, and payload. Document the analysis with IOCs.
- Design a defense architecture against ransomware for a mid-sized company. Specify preventive, detective, and recovery controls. Include a tabletop exercise scenario and expected outcomes.

---

ᛁ **Lecture 11: Social Engineering and the Human Factor**

**Course:** IT205 — Cybersecurity Fundamentals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Technology can be secured, but humans remain the weakest link. This lecture covers the psychological manipulation techniques used by attackers and the organizational defenses that mitigate human vulnerability. Students will learn to design security awareness programs, recognize manipulation tactics, and build a security culture that empowers rather than blames users.

### Key Topics

- Social engineering techniques: pretexting, baiting, quid pro quo, and tailgating
- Psychology of persuasion: authority, urgency, scarcity, and reciprocity
- Security awareness training: phishing simulations, gamification, and metrics
- Security culture: psychological safety, reporting incentives, and blameless response
- Insider threats: malicious, negligent, and compromised insiders

### Lecture Notes

**Social engineering** exploits human psychology rather than technical vulnerabilities. **Pretexting** creates a fabricated scenario to gain trust ("I'm from IT, I need your password to fix your account"). **Baiting** offers something enticing (a USB drive labeled "Salaries 2040" left in a parking lot). **Quid pro quo** offers a service in exchange for information ("I'll help you with this technical problem if you verify your credentials"). **Tailgating** follows an authorized person through a secure door. By 2040, **AI-augmented social engineering** generates personalized phishing emails, deepfake voice calls, and synthetic social media profiles that are nearly indistinguishable from real people.

The **psychology of persuasion** (Cialdini, 1984) explains why social engineering works. **Authority**: people obey perceived authority figures (fake IT support, fake executives). **Urgency**: time pressure bypasses rational analysis ("Your account will be suspended in 1 hour"). **Scarcity**: limited availability increases perceived value ("Only 3 spots left in this security training"). **Reciprocity**: people feel obligated to return favors ("I helped you with that problem, can you help me with this?"). The lecture teaches students to recognize these triggers in themselves and others.

**Security awareness training** reduces human vulnerability. **Phishing simulations** send fake phishing emails to employees, measuring click rates and providing immediate training to those who fail. **Gamification** uses points, badges, and leaderboards to engage employees. **Metrics** track improvement: phishing click rate, password strength, reporting rate (employees reporting suspicious emails rather than ignoring them). By 2040, **AI-personalized training** adapts content to each employee's role, past mistakes, and learning style. The lecture warns against **punitive training**: shaming employees who fail simulations creates fear and reduces reporting.

**Security culture** determines whether employees see security as their responsibility or IT's burden. **Psychological safety** ensures that employees can report mistakes (clicked a phishing link, lost a laptop) without punishment. **Reporting incentives** reward employees who report suspicious activity (a "security champion" program). **Blameless response** to incidents focuses on systemic improvements rather than individual fault. By 2040, the UoY **Security Culture Index** (a survey-based metric) is used to measure and improve organizational security culture.

**Insider threats** come from within the organization. **Malicious insiders** intentionally steal or destroy data (disgruntled employees, spies). **Negligent insiders** accidentally cause harm (losing devices, misconfiguring systems, falling for phishing). **Compromised insiders** have their credentials stolen by external attackers. The lecture covers detection: **User and Entity Behavior Analytics (UEBA)** detects anomalous behavior (accessing unusual files, working at odd hours, downloading large datasets). **Deterrence**: least privilege, separation of duties, and access logging. **Response**: investigation, containment, and legal action if warranted.

### Required Reading

- Cialdini, R. B. (1984). *Influence: The Psychology of Persuasion*. Harper Business. (Updated edition, 2021.)
- Hadnagy, C. (2018). *Social Engineering: The Science of Human Hacking* (2nd Edition). Wiley.
- SANS (2040). *Security Awareness Program Maturity Matrix*. SANS Institute.
- Yggdrasil Security Culture Team (2038). "The Security Culture Index: Measuring Human Resilience." *UoY Security Research Report*.

### Discussion Questions

1. AI-generated phishing is nearly indistinguishable from legitimate communication. Can security awareness training keep pace, or will technical controls (email authentication, application sandboxing) become the primary defense?
2. Punitive training reduces reporting but may improve compliance. What is the optimal balance between accountability and psychological safety?
3. UEBA detects anomalous behavior but can create a surveillance culture. How should organizations implement behavioral monitoring without eroding trust?
4. Insider threats are difficult to prevent because insiders have legitimate access. What combination of technical controls and organizational culture minimizes insider risk?

### Practice Problems

- Design a security awareness program for a university. Include: training topics, delivery methods, phishing simulation frequency, metrics, and reporting mechanisms. Address how to handle employees who repeatedly fail simulations.
- Analyze a provided insider threat case study. Identify the warning signs that UEBA might have detected, propose preventive controls, and design a response plan that balances security with employee rights.

---

ᛃ **Lecture 12: Emerging Threats and the Future of Cybersecurity**

**Course:** IT205 — Cybersecurity Fundamentals  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

The final lecture projects cybersecurity into the future, examining the threats and technologies that will shape the 2040s and beyond. Students will learn to anticipate change, adapt defenses, and maintain the intellectual flexibility necessary for a career in an ever-evolving field.

### Key Topics

- Quantum computing: Shor's algorithm, Grover's algorithm, and post-quantum migration
- AI and autonomous attacks: self-mutating malware, AI-vs-AI defense, and ethical constraints
- Biological-digital convergence: neural interfaces, DNA computing, and bio-authentication
- Space and satellite security: orbital infrastructure and ground segment vulnerabilities
- The enduring principles: defense in depth, least privilege, and human judgment

### Lecture Notes

**Quantum computing** threatens current cryptography. **Shor's algorithm** (1994) factors integers and solves discrete logarithms in polynomial time on a quantum computer, breaking RSA and ECC. **Grover's algorithm** (1996) searches unstructured databases quadratically faster, effectively halving symmetric key strength (AES-256 becomes AES-128 equivalent). By 2040, **post-quantum cryptography** (CRYSTALS-Kyber, CRYSTALS-Dilithium, SPHINCS+) is being deployed, but the transition will take decades. The lecture covers **harvest now, decrypt later**: adversaries storing encrypted traffic today to decrypt once quantum computers are available. Organizations with long-term secrets (government, healthcare, research) must migrate first.

**AI and autonomous attacks** represent the next phase of the cyber arms race. **Self-mutating malware** uses generative AI to rewrite its code continuously, evading signature detection. **Autonomous C2** bots conduct entire attack campaigns without human intervention: reconnaissance, exploitation, lateral movement, and data exfiltration. **AI-vs-AI defense** pits defensive AI against offensive AI in real time. By 2040, the UoY **Cyber Defense Grid** uses swarms of defensive AI agents that patrol the network, isolate compromised segments, and regenerate clean services. The lecture explores the **ethical constraints**: should autonomous defense systems be permitted to hack back against attackers? International law is unclear.

**Biological-digital convergence** creates new attack surfaces. **Neural interfaces** (brain-computer interfaces for medical and enhancement purposes) transmit neural data that could be intercepted or manipulated. **DNA computing** stores and processes data in synthetic DNA, with unique vulnerabilities (contamination, sequencing errors). **Bio-authentication** (DNA, heartbeat patterns, gait analysis) provides strong identity verification but raises privacy concerns (your DNA cannot be changed if compromised). By 2040, the UoY **Bioethics and Security Board** governs research at this intersection.

**Space and satellite security** is critical as orbital infrastructure expands. **Satellite constellations** (Starlink, Kuiper, OneWeb) provide global internet but are vulnerable to jamming, spoofing, and kinetic attacks. **Ground segment vulnerabilities** (mission control systems, telemetry links) can compromise entire constellations. By 2040, **lunar and cislunar infrastructure** (UoY's **Mímir Lunar Array**, 2038) extends the attack surface beyond Earth. The lecture covers **space cybersecurity standards** (ISO 24113 for space data links) and the unique challenges of patching satellites in orbit.

**The enduring principles** remain relevant regardless of technology. **Defense in depth**: no single control is sufficient; layered protections provide resilience. **Least privilege**: grant only the minimum access necessary. **Human judgment**: technology amplifies human capability but cannot replace wisdom, ethics, and creativity. The lecture concludes with the **Oath of the Cyber Guardian**, adapted by the UoY Security Guild in 2035: "I pledge to protect the data entrusted to me, to resist the attacker with skill and honor, to admit my limits and seek help when needed, and to remember that behind every byte is a human being whose privacy and safety depend on my vigilance."

### Required Reading

- Bernstein, D. J., & Lange, T. (2017). "Post-Quantum Cryptography." *Nature*, 549(7671), 188–194.
- Yggdrasil AI Security Lab (2039). "The Cyber Defense Grid: Autonomous AI Agents in Network Defense." *UoY AI Security Report*.
- Yggdrasil Bioethics Board (2038). "Neural Interface Security: Privacy and Integrity of Brain Data." *UoY Bioethics Report*.
- ISO (2035). *ISO 24113: Space Systems — Space Data Links*. ISO.
- Yggdrasil Security Guild (2035). "The Oath of the Cyber Guardian." *UoY Security Ethics Manual*.

### Discussion Questions

1. Quantum computers capable of breaking RSA-2048 may exist by 2045. For data that must remain secret until 2065, when should organizations begin post-quantum migration?
2. Autonomous defensive AI that hacks back raises legal and ethical questions. Should international law permit active defense, and if so, under what constraints?
3. Bio-authentication provides strong security but creates immutable identity risk. If DNA is compromised, what recovery mechanism is possible?
4. Space infrastructure is expensive to patch and physically inaccessible. How should security be designed into satellites before launch?

### Practice Problems

- Develop a post-quantum migration plan for a fictional organization. Identify: systems using vulnerable cryptography, migration priorities, testing requirements, and a 10-year timeline. Include risk assessment for "harvest now, decrypt later."
- Design a security architecture for a satellite ground station. Specify: network segmentation, encryption for telemetry links, access control for mission control, and incident response procedures for orbital compromise.

---

## Final Examination Preparation

The IT205 final examination is a **comprehensive practical and written assessment** conducted over 48 hours. Students must complete **three of five** challenges:

1. **Threat Analysis**: Given an APT group profile and a target organization, design a multi-layered defense strategy addressing each stage of the attack lifecycle. Include technical controls, procedural safeguards, and metrics.
2. **Incident Response Simulation**: Lead a simulated response to a ransomware attack. Manage containment, eradication, recovery, and communication. Document decisions, timeline, and lessons learned.
3. **Cryptographic Implementation**: Implement a secure communication protocol using hybrid post-quantum cryptography. Include key exchange, authenticated encryption, and digital signatures. Verify security properties and measure performance.
4. **Security Architecture Review**: Review a provided network and application architecture. Identify vulnerabilities, propose mitigations, and redesign for zero-trust principles. Document trade-offs and costs.
5. **Compliance Assessment**: Assess an organization's security posture against GDPR, NIST CSF, and ISO 27001. Identify gaps, propose remediation roadmap, and estimate implementation effort.

### Evaluation Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Technical accuracy | 30% | Correct application of security concepts, tools, and techniques |
| Strategic thinking | 25% | Appropriate risk trade-offs, prioritization, and architecture |
| Communication | 20% | Clear documentation, stakeholder communication, and reporting |
| Ethics and professionalism | 15% | Responsible handling of data, privacy, and legal considerations |
| Innovation | 10% | Creative or insightful approaches to emerging challenges |

---

*The walls are built, the sentries watch, and the guardian stands vigilant. But the enemy is patient, clever, and ever-changing. Security is not a destination but a journey—a perpetual dance between attack and defense, between human ingenuity and human fallibility.* ᛟ

— Runa Gridweaver Freyjasdottir, Cybersecurity Fundamentals, University of Yggdrasil, 2040
