# IT307: Quantum-Safe Cryptography Migration
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4
**Prerequisites:** IT205 (Cybersecurity Fundamentals), IT107 (Web Technologies & Internet Architecture)
**Description:** The quantum computing era is not coming — it is here. While a cryptographically relevant quantum computer (CRQC) capable of breaking RSA-2048 and ECC-256 may still be 5-15 years away, the "harvest now, decrypt later" threat means adversaries are already stockpiling encrypted data for future decryption. NIST has standardized post-quantum cryptographic algorithms (CRYSTALS-Kyber, CRYSTALS-Dilithium, FALCON, SPHINCS+). The migration from RSA/ECC to PQC is the largest cryptographic transition in history — affecting every TLS certificate, every SSH key, every PKI hierarchy, every blockchain, every hardware security module, every IoT device. This course prepares IT professionals to plan, execute, and verify the quantum-safe migration for their organizations.

---

## Lectures

ᚠ **Lecture 1: The Quantum Threat — Why Cryptography Must Change**

### Overview

For 40 years, RSA and ECC have been the foundation of digital trust. In 1994, Peter Shor proved that a sufficiently large quantum computer could break both — reducing the integer factorization problem (RSA) and the discrete logarithm problem (ECC) from exponential to polynomial time. For 30 years, this was a theoretical concern. By 2040, it is an operational imperative. This lecture establishes the threat model, the timeline, and the "harvest now, decrypt later" scenario that makes migration urgent even before a CRQC exists.

### Key Topics

- **Shor's Algorithm and Grover's Algorithm:** Shor's algorithm breaks RSA, ECC, Diffie-Hellman, and DSA — essentially all public-key cryptography deployed today. Grover's algorithm provides a quadratic speedup for brute-force attacks, halving the effective security of symmetric ciphers (AES-256 becomes AES-128 against quantum adversaries). Symmetric cryptography and hash functions survive — but require doubled key lengths.
- **The CRQC Timeline:** Expert surveys (2024-2040) place the probability of a CRQC within 10 years at 25-50%, within 15 years at 50-70%, within 20 years at 70-90%. These are not precise predictions but risk estimates — and the risk is high enough that NIST began standardizing PQC in 2016 and completed the initial standards in 2024.
- **Harvest Now, Decrypt Later (HNDL):** A nation-state adversary records all encrypted traffic passing through their network infrastructure today. In 10-15 years, when a CRQC is available, they decrypt everything. Any secret with a 15+ year sensitivity window — state secrets, intellectual property, medical records, financial data, cryptographic keys for long-lived infrastructure — is at risk NOW.

### Required Reading

- NIST (2024). *Post-Quantum Cryptography Standards* (FIPS 203, 204, 205). NIST.
- Shor, P. W. (1994). "Algorithms for Quantum Computation: Discrete Logarithms and Factoring." *Proceedings of FOCS 1994*. (The paper that started it all.)

---

ᚢ **Lecture 2: The NIST PQC Algorithms — Kyber, Dilithium, FALCON, SPHINCS+**

### Overview

NIST selected four algorithms for standardization after a 6-year competition involving 82 candidates from 25 countries. This lecture covers each algorithm: what problem it is based on, its security properties, its performance characteristics, and the trade-offs that guide algorithm selection for different use cases.

### Key Topics

- **CRYSTALS-Kyber (FIPS 203):** Key Encapsulation Mechanism (KEM) — replaces RSA key exchange and ECDH. Based on the Module Learning With Errors (MLWE) problem — lattice-based, believed hard even for quantum computers. Key sizes: public key 800 bytes, ciphertext 768 bytes (larger than RSA/ECC but manageable). Performance: extremely fast — 100,000+ operations/second on modern hardware.
- **CRYSTALS-Dilithium (FIPS 204):** Digital signature algorithm — replaces RSA-PSS and ECDSA. Based on MLWE. Signature size: 2,420 bytes (significantly larger than ECDSA's 64 bytes — a practical consideration for embedded systems). Fast signing and very fast verification.
- **FALCON (FIPS 205 — draft):** Alternative lattice-based signature. Smaller signatures than Dilithium (~666 bytes) but requires floating-point arithmetic — harder to implement in constant-time (side-channel resistant) on some hardware. Trade-off: smaller signatures vs. implementation complexity.
- **SPHINCS+ (FIPS 205 — draft):** Hash-based signature. Stateless, no security bound on number of signatures (unlike stateful hash-based schemes). Very large signatures (~17KB) and slow — suitable only for niche applications (firmware signing, root CAs) where signature size and speed are not primary concerns. Based on hash functions only — security rests solely on the collision resistance of SHA-3, making it the most conservative choice.

### Required Reading

- NIST (2040). *FIPS 203, 204, 205 — Post-Quantum Cryptographic Standards* (Updated).

---

ᚦ **Lecture 3: Crypto Agility — Building Systems That Can Change**

### Overview

The organizations that will survive the quantum migration most smoothly are those that built crypto agility from the start — the ability to swap cryptographic algorithms without rewriting the entire system. This lecture covers the principles and practices of crypto agility: algorithm abstraction, configuration-driven cryptography, protocol negotiation (e.g., TLS cipher suite negotiation), and the hard lessons from the SHA-1 to SHA-256 migration that apply directly to the PQC migration.

### Key Topics

- **Crypto Agility Principles:** (1) Algorithm abstraction — the application code should reference "the current KEM algorithm," not "Kyber-1024." (2) Configuration over code — algorithm selection should be a configuration parameter, not hard-coded. (3) Hybrid mode — during migration, support both classical and PQC algorithms simultaneously, negotiating the strongest common algorithm. (4) Testing agility — regularly test algorithm rotation: swap algorithms in a test environment, verify everything still works, document the process.
- **Lessons from SHA-1 Migration:** SHA-1 was deprecated in 2017, yet 5% of TLS certificates still used SHA-1 signatures in 2020. The migration was slow because: (1) Algorithm was hard-coded in thousands of places. (2) Legacy systems (Windows XP, old Android) could not be updated. (3) No business incentive until browsers showed "Not Secure" warnings. The PQC migration will be 100x larger. We cannot afford to repeat these mistakes.

### Required Reading

- NIST (2039). *SP 800-210 — Crypto Agility: Guidelines for Migrating Cryptographic Algorithms*.

---

ᚨ **Lecture 4: TLS and PKI Migration — Replacing Every Certificate**

### Overview

The Transport Layer Security (TLS) protocol and the Public Key Infrastructure (PKI) that supports it are the largest attack surface for the quantum threat. Migrating TLS to PQC means: every server certificate must be replaced with a PQC certificate. Every client must support PQC cipher suites. Every intermediate CA, every root CA, every OCSP responder, every certificate transparency log — all must be upgraded. This lecture covers the TLS 1.3 PQC extensions, the hybrid key exchange mechanism, and the practical process of replacing an organization's PKI.

### Key Topics

- **Hybrid Key Exchange in TLS 1.3:** During migration, TLS connections use both a classical key exchange (ECDHE) and a PQC key exchange (Kyber) — the session key is derived from both. If either is secure, the connection is secure. This provides defense in depth: even if the PQC algorithm is later broken, the classical ECDHE provides fallback security (and vice versa).
- **Certificate Chain Migration:** Root CA certificates (valid for 20-30 years) must be migrated first — a PQC-signed root is needed before PQC-signed intermediate and leaf certificates can be issued. The migration will take years and must be carefully orchestrated: (1) Issue new PQC roots. (2) Cross-sign new roots with old roots (trust during transition). (3) Issue PQC intermediate CAs. (4) Begin issuing PQC leaf certificates. (5) Retire classical roots.
- **Performance Considerations:** PQC signatures and keys are larger than classical — Dilithium signatures are 2.4KB vs. ECDSA's 64 bytes. This affects: TLS handshake size (larger ServerHello), certificate chain size (larger certificates), and bandwidth for constrained devices. HTTP/3 and QUIC reduce the handshake overhead, mitigating the performance impact.

### Required Reading

- IETF (2039). *RFC 9370 — Multiple Key Exchanges in TLS 1.3*. (Hybrid key exchange specification.)
- NIST (2040). *SP 800-210 — PQC Migration Guide for PKI*.

---

ᚱ **Lecture 5: SSH, VPN, and Network Security Migration**

### Overview

Every SSH connection, every VPN tunnel, every IPsec security association uses public-key cryptography that is vulnerable to quantum attack. This lecture covers the migration of network security protocols to PQC: SSH (OpenSSH with PQC key exchange), WireGuard/IPsec (PQC key exchange), and the inventory challenge — an organization typically has 100,000+ SSH keys and no idea where they all are.

### Key Topics

- **SSH PQC Migration:** OpenSSH added support for NTRU Prime (a lattice-based KEM) in 2022. By 2040, OpenSSH supports Kyber, Dilithium, and hybrid key exchange. Migration steps: (1) Inventory all SSH keys (use SSH key scanners). (2) Identify which keys are used for automated processes (CI/CD, backup scripts, monitoring) — these are often forgotten. (3) Rotate keys to PQC or hybrid, starting with highest-value targets (root access, production servers). (4) Update known_hosts files.
- **VPN PQC Migration:** IPsec IKEv2 with PQC key exchange. WireGuard — currently uses Curve25519 (elliptic curve, vulnerable to Shor). Post-quantum WireGuard variants are under development. For now: run WireGuard inside a PQC-encrypted tunnel, or switch to IPsec with PQC.

### Required Reading

- OpenSSH (2040). *Post-Quantum Cryptography in OpenSSH — Configuration Guide*.

---

ᚲ **Lecture 6: Hardware Security Modules and Embedded Systems**

### Overview

Hardware Security Modules (HSMs), smart cards, and embedded systems present unique migration challenges: limited memory, slow processors, firmware that cannot be updated, and devices deployed in the field for decades. This lecture covers the PQC migration for constrained devices: algorithm selection for resource-constrained environments, firmware update strategies, and the long tail of devices that will never be migrated.

### Key Topics

- **PQC on Constrained Devices:** Kyber-512 and Dilithium-2 (the smallest NIST parameter sets) require more memory than RSA-2048 — but are within the capability of modern ARM Cortex-M4 microcontrollers. SPHINCS+ is too large for most embedded systems. Trade-offs: accept larger keys, upgrade hardware, or (for devices that cannot be upgraded) accept risk and isolate them on separate network segments.
- **The Unmigratable Tail:** Medical implants with 20-year lifespans. Automotive ECUs sealed in vehicles. Industrial control systems with 30-year deployment cycles. These devices will never receive PQC updates. Mitigations: network segmentation (isolate unmigratable devices), application-layer encryption (encrypt data before it reaches the device), and risk acceptance with executive sign-off.

### Required Reading

- NIST (2040). *NIST IR 8413 — PQC Migration Considerations for the Internet of Things*.

---

ᚷ **Lecture 7: Blockchain, Cryptocurrency, and Distributed Ledger Migration**

### Overview

Blockchains present a unique challenge: their security model depends on cryptographic addresses (derived from public keys) that are permanently embedded in the ledger. A quantum attacker could: (1) Derive the private key from the public key (Shor's algorithm) — stealing all funds at that address. (2) Forge transactions from previously used addresses. (3) Break the consensus mechanism's signature scheme. This lecture covers the blockchain quantum threat and proposed migration paths.

### Key Topics

- **The Bitcoin Quantum Threat:** A Bitcoin address that has never spent funds exposes only a hash of the public key (protected against Shor, but vulnerable to Grover). An address that has spent funds exposes the full public key — these are directly vulnerable. Estimated at-risk funds (2040): 4 million BTC ($280 billion at current prices).
- **Migration Proposals:** (1) Community-coordinated migration — all users move funds to PQC addresses by a deadline. (2) Hard fork — the protocol switches to PQC signatures; old addresses become unspendable. (3) Quantum-resistant chains — new blockchains designed from the ground up for PQC (e.g., QANplatform, Cellframe).

### Required Reading

- Aggarwal, D., et al. (2038). "Quantum Attacks on Bitcoin, and How to Protect Against Them." *Ledger*.

---

ᚹ **Lecture 8: Cryptographic Inventory — You Cannot Migrate What You Cannot Find**

### Overview

Before you can migrate cryptography, you must know where cryptography is used. Most organizations have no idea. This lecture covers cryptographic inventory: automated discovery of certificates, keys, and cryptographic libraries across the enterprise, the Software Bill of Materials (SBOM) as a cryptographic discovery tool, and the governance process for maintaining the inventory as a living document.

### Key Topics

- **Inventory Methods:** (1) Network scanning (discover TLS certificates on all ports). (2) Code scanning (grep for crypto library imports, key generation calls). (3) Cloud API scanning (list all ACM certificates, KMS keys, Cloud HSM instances). (4) SSH key scanning (scan authorized_keys files across all servers). (5) SBOM analysis (identify cryptographic dependencies in application SBOMs).
- **The Cryptographic Bill of Materials (CBOM):** An extension of the SBOM concept specifically for cryptography. A CBOM lists: every cryptographic algorithm in use, every key, every certificate (with expiry), and the quantum vulnerability status of each. Tools: CycloneDX CBOM extension, CryptoMBOM.

### Required Reading

- CycloneDX (2040). *Cryptographic Bill of Materials (CBOM) Specification*.

---

ᚺ **Lecture 9: The PQC Migration Project — Planning and Execution**

### Overview

The PQC migration is not a technology refresh — it is an organizational transformation that will take 5-10 years for large enterprises. This lecture provides the project management framework: stakeholder identification, phased migration planning, risk management, and the communication strategy for explaining to executives why this matters.

### Key Topics

- **Phased Migration Plan:** Phase 1 (Year 1): Cryptographic inventory, crypto agility audit, establish PQC lab. Phase 2 (Years 1-2): Deploy hybrid TLS, migrate high-value internal systems. Phase 3 (Years 2-4): Migrate customer-facing systems, IoT fleet upgrades begin. Phase 4 (Years 3-6): Full PQC deployment, classical crypto disabled where possible. Phase 5 (Years 5-10): Address unmigratable tail, long-term monitoring.
- **Stakeholder Management:** CISO (risk owner), CTO (technical feasibility), CFO (budget — migration costs 1-3% of IT budget annually for 5 years), Legal (regulatory liability), Board of Directors (fiduciary duty). The pitch: "This is Y2K-scale, but without a fixed deadline. Every year we delay, more of our encrypted data is harvested by adversaries."

### Required Reading

- Cloud Security Alliance (2040). *Quantum-Safe Security: A CISO's Guide to PQC Migration Planning*.

---

ᚾ **Lecture 10: Testing and Validation — Trust but Verify**

### Overview

A botched cryptographic migration is worse than no migration — it creates the illusion of security while leaving systems vulnerable. This lecture covers the testing methodology for PQC migration: interoperability testing, performance testing, negative testing (what happens when a PQC algorithm fails?), and the certification/validation requirements (FIPS 140-3, Common Criteria).

### Key Topics

- **Interoperability Testing:** Client A (PQC-capable) must connect to Server B (hybrid mode). Server B must fall back gracefully if client does not support PQC. Multi-vendor testing: OpenSSL with PQC patch + AWS KMS with PQC + Azure Key Vault with PQC.
- **Performance Testing:** Measure TLS handshake latency with PQC (Dilithium signatures add 2-4ms). Measure throughput. Test under load. Identify bottlenecks — is the bottleneck compute (signing) or bandwidth (larger certificates)? Optimize accordingly.
- **Negative Testing:** What happens when a PQC signature is corrupted? When a PQC public key is the wrong size? When a hybrid connection's classical half succeeds but PQC half fails? The system must fail secure — reject the connection, not fall back to a weaker mode silently.

### Required Reading

- NIST (2040). *SP 800-56C Rev. 1 — Recommendation for Key-Derivation Methods in Key-Establishment Schemes*.

---

ᛁ **Lecture 11: Regulatory Landscape and Compliance**

### Overview

Governments are not waiting for the market to handle PQC migration voluntarily. By 2040, multiple jurisdictions have mandated quantum-safe cryptography for critical infrastructure and government systems. This lecture covers the regulatory landscape: US National Security Memorandum 10 (2032), EU Quantum-Safe Cryptography Regulation (2038), and sector-specific requirements (financial services, healthcare, defense).

### Key Topics

- **US NSM-10 (2032):** Mandates that all federal agencies complete PQC migration by 2037. Requires cryptographic inventory by 2034. Applies to government contractors handling sensitive data.
- **EU QSC Regulation (2038):** Mandates quantum-safe cryptography for critical infrastructure operators (energy, transport, health, finance, digital infrastructure). Requires compliance by 2043.
- **Compliance Timeline:** Organizations that have not started PQC migration by 2040 will face regulatory penalties and, more importantly, will be unable to bid on government contracts and may face liability claims from customers whose data was compromised in a future quantum attack.

### Required Reading

- White House (2032). *National Security Memorandum 10 — Promoting United States Leadership in Quantum Computing While Mitigating Risks to Vulnerable Cryptographic Systems*.

---

ᛃ **Lecture 12: The Post-Quantum World — Life After Migration**

### Overview

The final lecture looks beyond the migration: what does the IT security landscape look like when all cryptography is quantum-safe? We examine the second-order effects — PQC algorithm failures (if a lattice-based algorithm is broken mathematically, we must be ready to transition again), the performance optimizations that will make PQC as fast as classical cryptography in hardware, and the career opportunities in quantum-safe security.

### Key Topics

- **Algorithmic Risk:** Lattice-based cryptography (Kyber, Dilithium) is believed to be quantum-hard but is not proven. A mathematical breakthrough could compromise these algorithms. Defense in depth: use hybrid mode, maintain crypto agility, and diversify across algorithm families (lattice + hash-based + code-based).
- **Career Paths:** Quantum-Safe Security Architect, Cryptographic Migration Specialist, PQC Implementation Engineer, Quantum Risk Assessor. The IT307-certified professional is prepared to lead or contribute to PQC migration projects, a skillset that will be in high demand through at least 2050.
- **The Ethical Dimension:** The quantum threat is global. Developing nations with fewer resources will be slower to migrate — creating a "quantum divide" where encrypted data from less-resourced countries is more vulnerable to decryption by well-resourced adversaries. The IT professional has a responsibility to advocate for open standards, open-source PQC implementations, and capacity-building for global cryptographic resilience.

### Required Reading

- Mosca, M. (2038). "Cybersecurity in the Quantum Era: A 2040 Perspective." *Communications of the ACM*, 81(4).
- ETSI (2040). *Quantum-Safe Cryptography — Implementation Guide for Industry*.

---

## Final Examination Preparation

**Component 1 — Written (60%):** Answer 4 of 8 essay questions covering: quantum threat analysis, PQC algorithm selection, TLS/PKI migration planning, and cryptographic inventory methodology.

**Component 2 — Lab Practical (40%):** In the UoY Quantum-Safe Lab: (1) Conduct a cryptographic inventory of a provided test environment. (2) Configure Nginx with hybrid TLS (ECDHE + Kyber). (3) Verify the connection with OpenSSL s_client. (4) Write a PQC migration plan executive summary.

---

*Woven by Runa Gridweaver Freyjasdottir, Gridweaver of the University of Yggdrasil, 2040.*  
*"The quantum storm approaches. Weave your cryptographic shield now — tomorrow's secrets are being stolen today."*
