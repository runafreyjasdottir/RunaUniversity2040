# IT307: Quantum-Safe Cryptography Migration
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4
**Description:** Comprehensive study of the post-quantum cryptography transition — the largest cryptographic migration in Internet history. Covers quantum threats, PQC algorithms (Kyber, Dilithium, SPHINCS+), hybrid migration strategies, crypto-agility, and practical deployment across web, email, VPN, database, and blockchain systems.

**Prerequisites:** IT205, IT303

**Instructor:** Dr. Freyja Hrafnsdóttir, Department of Information Technology

**Course Philosophy:** Quantum computers will break the cryptography that secures the Internet. This is not science fiction — it is an engineering timeline. The migration to post-quantum cryptography (PQC) is the defining cryptographic challenge of our era. This course prepares IT professionals to understand, plan, and execute this migration — not as cryptographers, but as the practitioners who will deploy and operate quantum-safe systems for decades to come.

---

## Lectures

---

### Lecture 1: The Quantum Threat — Why Cryptography Must Change

**Course:** IT307 — Quantum-Safe Cryptography Migration
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Quantum computers exploit quantum mechanical phenomena — superposition, entanglement, interference — to solve certain problems exponentially faster than classical computers. Unfortunately, those problems include the mathematical foundations of modern cryptography. This lecture explains the quantum threat: Shor's algorithm (breaks RSA, ECC, Diffie-Hellman), Grover's algorithm (weakens symmetric crypto), and the "harvest now, decrypt later" threat that makes migration urgent even before large quantum computers exist.

#### Key Topics

- **Quantum Computing Fundamentals (for IT professionals):** Quantum bits (qubits) can exist in superposition — representing 0 and 1 simultaneously. Quantum algorithms exploit this to explore many possibilities at once. Two key algorithms threaten cryptography: (1) **Shor's algorithm (1994)** — factors large integers in polynomial time, breaking RSA and computing discrete logarithms (breaking ECC, DH); (2) **Grover's algorithm (1996)** — searches an unsorted database quadratically faster, effectively halving the security of symmetric ciphers (AES-256 becomes effectively AES-128).
- **The Timeline:** When will cryptographically relevant quantum computers exist? Estimates range from 5 to 20 years. By 2040, quantum computers with ~1000 logical qubits exist in research labs — not yet enough to break RSA-2048 (which requires ~4000 logical qubits), but approaching. The key insight: cryptographic migration takes 10-15 years for large organizations. We must migrate before the threat materializes.
- **Harvest Now, Decrypt Later:** An attacker can record encrypted traffic today and decrypt it once quantum computers are available. For data with long-term sensitivity (government secrets, financial records, healthcare data, intellectual property), this means the quantum threat is *already active* — data intercepted today may be decrypted in 10 years. By 2040, this threat drives regulatory mandates for quantum-safe encryption of long-lived data.

#### Required Reading

- Shor, P. (1994). "Algorithms for Quantum Computation: Discrete Logarithms and Factoring." *FOCS*.
- NIST. (2039). *Quantum Computing and Cryptography: Status Report*.
- UoY Quantum Security Lab. (2040). *The Harvest Now, Decrypt Later Threat: Analysis and Mitigation*.

---

### Lecture 2: The NIST PQC Standards — Kyber, Dilithium, and SPHINCS+

**Course:** IT307 — Quantum-Safe Cryptography Migration
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

NIST's Post-Quantum Cryptography standardization process (2016–2024) selected the algorithms that will secure the post-quantum Internet. This lecture introduces the selected algorithms at a conceptual level: CRYSTALS-Kyber (key encapsulation), CRYSTALS-Dilithium (digital signatures), FALCON (signatures), and SPHINCS+ (stateless hash-based signatures as backup).

#### Key Topics

- **Kyber — Module-Lattice-Based KEM:** A Key Encapsulation Mechanism (KEM) securely exchanges symmetric keys. Kyber is based on the hardness of the Module Learning With Errors (MLWE) problem. Properties: small public keys (~800 bytes), small ciphertexts (~768 bytes), fast operations. Kyber-1024 provides security roughly equivalent to AES-256. By 2040, Kyber is the dominant PQC KEM, integrated into TLS 1.4, SSH, and most key exchange protocols.
- **Dilithium — Module-Lattice-Based Signatures:** Digital signatures for authentication. Dilithium is also lattice-based, sharing mathematical foundations with Kyber. Properties: moderate public key size (~1.3KB), large signatures (~2.4KB), fast signing and verification. Dilithium5 provides the highest security level. The large signature size (compared to ECDSA's ~64 bytes) has operational implications — more bandwidth, more storage, potential protocol compatibility issues.
- **SPHINCS+ — Stateless Hash-Based Signatures:** A backup signature scheme based only on hash functions, not lattice assumptions. Much larger signatures (~8KB–50KB) and slower than Dilithium, but its security rests on the well-understood hardness of hash function collision — a more conservative assumption. Used as a backup or for very high-security applications where lattice assumptions are considered insufficiently mature.
- **FALCON — Lattice-Based Signatures with Compact Output:** A lattice-based signature scheme with smaller signatures (~666 bytes) than Dilithium, but more complex implementation (floating-point FFT). Preferred for bandwidth-constrained applications.

#### Required Reading

- NIST. (2024). FIPS 203 (Kyber), FIPS 204 (Dilithium), FIPS 205 (SPHINCS+).
- UoY Crypto Lab. (2039). *PQC Algorithm Performance: Benchmarks for Deployers*.

---

### Lecture 3: Hybrid Cryptography — Bridging Classical and Post-Quantum

**Course:** IT307 — Quantum-Safe Cryptography Migration
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

The migration to PQC is not a flag day — it's a transition. Hybrid cryptography combines classical and post-quantum algorithms so that security holds as long as *either* is secure. This lecture covers hybrid design patterns, protocol integration (TLS, SSH, IPsec), and the transition from hybrid to PQC-only.

#### Key Topics

- **Why Hybrid?** (1) PQC algorithms are newer and less battle-tested — combining with classical crypto provides defense in depth; (2) if a weakness is found in a PQC algorithm, classical crypto still protects; (3) compliance — many standards require approved classical algorithms. The hybrid approach: perform both a classical key exchange (ECDH) and a PQC key exchange (Kyber), then combine the shared secrets. If either is secure, the combined key is secure.
- **Hybrid TLS 1.4:** TLS 1.4 (2038) supports hybrid key exchange: the ClientHello advertises both classical and PQC key share extensions; the server selects and responds with both; the handshake proceeds with both, and the master secret is derived from both. Hybrid TLS adds ~2KB to the handshake (Kyber key share) and ~5% latency overhead — acceptable for the security gain.
- **Hybrid to PQC-Only Transition:** The migration timeline: (1) **2025–2030:** hybrid PQC optional; (2) **2030–2035:** hybrid PQC preferred, classical accepted; (3) **2035–2040:** PQC-only preferred, hybrid accepted; (4) **2040+:** PQC-only required for sensitive applications. The transition is gradual — clients and servers negotiate the strongest mutually supported option.

#### Required Reading

- IETF. (2038). RFC 9370: Hybrid Key Exchange in TLS 1.3 (Updated for TLS 1.4).
- UoY Transition Lab. (2039). *The Hybrid-to-PQC Migration: Operational Lessons*.

---

### Lecture 4: Crypto-Agility — Designing Systems That Survive Algorithm Transitions

**Course:** IT307 — Quantum-Safe Cryptography Migration
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

The PQC migration is not the last cryptographic transition. Crypto-agility is the architectural property that enables systems to swap cryptographic algorithms without rewriting applications. This lecture covers crypto-agility principles: algorithm abstraction, protocol negotiation, key lifecycle management, and the operational practices that make migration feasible.

#### Key Topics

- **Principles of Crypto-Agility:** (1) **Algorithm abstraction** — applications reference "the current key exchange algorithm" not "RSA-2048"; (2) **Protocol negotiation** — endpoints negotiate the algorithm during connection; (3) **Modular cryptography** — replace cryptographic modules without changing application logic; (4) **Key and certificate management** — automate issuance, rotation, and revocation across algorithms; (5) **Inventory** — know what cryptography is used where.
- **Crypto-Agility Patterns:** (1) **Crypto service abstraction layer** — applications call a crypto service API that handles algorithm selection; (2) **Certificate transparency for PQC** — monitor CT logs for PQC certificates; (3) **Versioned cryptographic policies** — define allowed algorithms as version-controlled policy; (4) **Algorithm sunset** — plan the deprecation of old algorithms (RSA-1024 was deprecated long ago but still appears in legacy systems).
- **The Cost of Non-Agility:** Organizations that hard-coded RSA found the PQC migration difficult — requiring application rewrites, protocol upgrades, and painful coordination. The lesson: crypto-agility is not a luxury. It is the cost of doing business in a world of evolving cryptographic threats.

#### Required Reading

- IETF. (2038). RFC 7696: Guidelines for Cryptographic Algorithm Agility.
- UoY Crypto Agility Lab. (2039). *Crypto-Agility: Design Patterns and Antipatterns*.

---

### Lecture 5: Deploying PQC in TLS, SSH, and VPNs

**Course:** IT307 — Quantum-Safe Cryptography Migration
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

The first protocols to be migrated are the ones that secure network communication: TLS (web, API), SSH (server administration), and VPNs/IKEv2 (network tunnels). This lecture covers practical deployment: configuration, certificate management, performance tuning, and troubleshooting.

#### Key Topics

- **TLS Deployment:** Steps: (1) upgrade TLS libraries (OpenSSL 4.x, BoringSSL, LibreSSL with PQC support); (2) obtain PQC certificates (hybrid or PQC-only from CAs supporting PQC); (3) configure web servers to prefer PQC cipher suites; (4) test with PQC-capable clients; (5) monitor performance and errors; (6) gradually increase PQC preference. Pitfalls: PQC certificates are larger (Dilithium signatures), potentially exceeding size limits in legacy middleware.
- **SSH Deployment:** OpenSSH 10.x supports PQC key exchange (sntrup761x25519-sha512) and PQC host keys. Deployment: upgrade OpenSSH, configure `KexAlgorithms` and `HostKeyAlgorithms`, distribute PQC host keys, test connections. SSH is often overlooked in PQC migration plans because it's "just admin access" — but SSH keys protect access to every server.
- **VPN/IKEv2 Deployment:** IPsec IKEv2 with PQC key exchange. Deploy by upgrading VPN concentrators and client software. Challenge: hardware VPN appliances may not support PQC — requiring replacement or software-based termination.

#### Required Reading

- OpenSSL. (2040). *PQC Configuration Guide*.
- OpenSSH. (2040). *Post-Quantum Cryptography in SSH*.

---

### Lecture 6: PQC for Data at Rest — Databases, File Systems, and Backup

**Course:** IT307 — Quantum-Safe Cryptography Migration
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Encrypted data at rest is vulnerable to harvest-now-decrypt-later. Data with multi-decade sensitivity must be re-encrypted with PQC. This lecture covers migrating encryption at rest: database TDE, filesystem encryption, backup encryption, and object storage encryption.

#### Key Topics

- **The "Harvest Now" Threat to Data at Rest:** An attacker who steals encrypted data today (via breach, insider, or physical theft) can decrypt it when quantum computers mature. For long-lived sensitive data — medical records (lifetime retention), government classified (50+ years), financial records, intellectual property — this means data encrypted today with RSA/ECC is at risk.
- **Migration Strategies:** (1) **Re-encrypt in place** — decrypt with old key, encrypt with PQC key. Requires downtime or careful orchestration; (2) **Dual encryption** — maintain both classical and PQC encryption during transition; (3) **Key rotation** — rotate encryption keys to PQC during normal key rotation cycles; (4) **Greenfield PQC** — encrypt all new data with PQC, leave old data until key rotation. The approach depends on data sensitivity and operational constraints.
- **Performance Considerations:** PQC key encapsulation (Kyber) is fast — comparable to ECDH for key exchange. PQC signatures (Dilithium) are slower to generate than ECDSA but verification is fast. For data at rest (which uses symmetric encryption with keys exchanged via KEM), the performance impact is minimal — once the key is established, AES-256 encrypts the data, unchanged.

#### Required Reading

- NIST. (2039). SP 800-57 Pt. 1 Rev. 6: Recommendation for Key Management — PQC Transition.
- UoY Storage Security Lab. (2039). *PQC for Data at Rest: Migration Guide*.

---

### Lecture 7: PQC in Blockchain, DLT, and Decentralized Systems

**Course:** IT307 — Quantum-Safe Cryptography Migration
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Blockchains and decentralized systems present unique PQC migration challenges: immutable ledgers with long-lived addresses, consensus algorithms that depend on specific signature schemes, and decentralized governance that makes coordinated upgrades difficult. This lecture covers PQC in Web3, Ethereum 3.0's post-quantum roadmap, and the migration of decentralized identity systems.

#### Key Topics

- **The Blockchain PQC Challenge:** Blockchains use cryptography fundamentally: (1) addresses derived from public keys — if ECDSA is broken, all funds in addresses with exposed public keys are vulnerable; (2) transaction signing — signature forgery enables theft; (3) consensus — some chains use signature-based consensus (e.g., BFT). Migration requires: new address formats supporting PQC, wallet upgrades, and possibly a hard fork for consensus algorithms.
- **Ethereum 3.0 PQC Roadmap:** Ethereum's multi-phase upgrade includes: Phase 1 — PQC signature support in wallets (users can create PQC-secured addresses); Phase 2 — PQC-preferred for new transactions, classical accepted; Phase 3 — classical signature deprecation, with a migration window for users to move funds from vulnerable addresses. The challenge: decentralized governance means no one can force migration — adoption is voluntary.
- **PQC for Verifiable Credentials:** Decentralized identity systems (DIDs, VCs) rely on digital signatures. The DID method specification must be updated to support PQC signature suites. VC issuers must re-issue credentials with PQC signatures. Verifiers must update to accept PQC signatures. The W3C Verifiable Credentials Working Group published PQC signature suite specifications in 2038.

#### Required Reading

- Ethereum Foundation. (2039). *Ethereum 3.0 Post-Quantum Roadmap*.
- W3C. (2038). *PQC Signature Suites for Verifiable Credentials*.

---

### Lecture 8: PQC Migration Planning — Inventory, Prioritization, and Execution

**Course:** IT307 — Quantum-Safe Cryptography Migration
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

PQC migration is a multi-year program touching every system. This lecture provides a practical framework: cryptographic inventory, risk-based prioritization, migration sequencing, and the organizational capabilities needed for successful execution.

#### Key Topics

- **Cryptographic Inventory:** You can't migrate what you don't know exists. Build a complete inventory: (1) what cryptographic algorithms are used, where, and for what purpose; (2) what data is protected, with what sensitivity and retention period; (3) what third parties are involved (their PQC readiness affects yours); (4) what hardware/software constraints exist (embedded systems, legacy platforms). Automated discovery tools scan code repositories, network traffic, and configuration files to build the inventory.
- **Risk-Based Prioritization:** Not everything needs to be migrated immediately. Prioritize: (1) data with the longest sensitivity lifetime; (2) externally-facing systems (harvest now, decrypt later); (3) cryptographic components that protect many other systems (PKI, key management); (4) systems with the longest upgrade lead time. Deprioritize: short-lived data, isolated systems, systems scheduled for replacement.
- **Phased Migration:** (1) **Preparation** — build inventory, develop migration plan, establish crypto-agility; (2) **Infrastructure** — upgrade crypto libraries, PKI, key management; (3) **Network security** — TLS, SSH, VPN; (4) **Applications** — application-level encryption and signatures; (5) **Data at rest** — re-encrypt sensitive stored data; (6) **Legacy** — address systems that can't be upgraded.
- **Organizational Requirements:** Successful migration requires: executive sponsorship, dedicated program management, cross-functional team (security, infrastructure, application, compliance), clear metrics and milestones, and ongoing communication.

#### Required Reading

- NIST. (2039). *PQC Migration Planning Guide*.
- UoY Migration Lab. (2039). *PQC Migration: Lessons from Early Adopters*.

---

### Lecture 9: Certificates, PKI, and Identity in the Post-Quantum Era

**Course:** IT307 — Quantum-Safe Cryptography Migration
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Public Key Infrastructure (PKI) is the backbone of Internet trust. Migrating PKI to PQC requires: CAs that issue PQC certificates, certificate profiles that support PQC algorithms, root program updates, and the complex dance of cross-signing and transitional trust. This lecture covers the PQC PKI ecosystem.

#### Key Topics

- **PQC Certificates:** X.509 certificates now support PQC signature algorithms (Dilithium, FALCON, SPHINCS+). PQC certificates are larger: a Dilithium-signed certificate is ~3KB vs. ~1KB for RSA. This impacts TLS handshake size, CT log storage, and bandwidth. Hybrid certificates (signed by both classical and PQC) provide transitional trust — verifiers that understand PQC check the PQC signature; verifiers that don't check the classical signature.
- **Root Program Migration:** Browser/OS root programs must update trust stores to include PQC root CAs, define PQC certificate profiles, and establish transition timelines. By 2040, all major root programs (Microsoft, Mozilla, Apple, Google) accept PQC end-entity certificates.
- **Certificate Transparency for PQC:** CT logs must accept PQC certificates, verify PQC signatures, and produce PQC-signed SCTs (Signed Certificate Timestamps). The added size of PQC signatures increases CT log storage requirements by 2-4x.

#### Required Reading

- CA/Browser Forum. (2039). *Baseline Requirements for PQC Certificates*.
- Google. (2038). *Certificate Transparency and PQC*.

---

### Lecture 10: Hardware, IoT, and Embedded PQC

**Course:** IT307 — Quantum-Safe Cryptography Migration
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

PQC on constrained devices — IoT sensors, smart cards, automotive ECUs, industrial controllers — presents unique challenges: limited CPU, memory, and power. This lecture covers PQC for embedded systems, hardware acceleration, and the lifecycle challenge of devices that can't be upgraded.

#### Key Topics

- **PQC Performance on Constrained Devices:** Lattice-based algorithms (Kyber, Dilithium) perform well on modern microcontrollers — Kyber-768 key generation takes ~1ms, encapsulation ~0.5ms on a Cortex-M4. But memory footprint (Kyber needs ~3KB RAM) and code size may challenge the smallest devices. Hash-based signatures (SPHINCS+) are too slow for most constrained devices.
- **Hardware Acceleration:** By 2040, many CPUs include PQC hardware acceleration — dedicated instructions for polynomial multiplication, NTT (Number Theoretic Transform), and SHA-3. Hardware security modules (HSMs) and TPMs support PQC key generation and storage. The transition: hardware that can't be upgraded (automotive, industrial IoT with 15+ year lifespans) must rely on pre-shared keys, symmetric-only security, or physical replacement.
- **The "Too Late to Migrate" Problem:** Devices deployed today with classical crypto may be in service when quantum computers mature. For long-lifetime devices, PQC must be designed in now. By 2040, all new IoT and embedded designs mandate PQC, but the legacy fleet remains — secured by network-level PQC gateways that terminate classical connections and forward via PQC.

#### Required Reading

- NIST. (2040). *PQC for Constrained Devices: Implementation Guidance*.
- UoY Embedded Security Lab. (2039). *PQC on ARM Cortex-M: Performance Analysis*.

---

### Lecture 11: Operational PQC — Key Management, Rotation, and Incident Response

**Course:** IT307 — Quantum-Safe Cryptography Migration
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

PQC changes key management operations: new key types, new rotation requirements, new incident response scenarios. This lecture covers the operational dimension: PQC key lifecycle management, automated rotation, and what happens when a PQC algorithm is compromised.

#### Key Topics

- **PQC Key Lifecycle:** PQC keys are larger and have different lifecycle properties than classical keys. Kyber key pairs are ~3KB; Dilithium key pairs are ~5KB. Key management systems must be updated to store, distribute, and rotate these larger keys. HSMs must support PQC key generation and storage. By 2040, key management standards (KMIP, PKCS#11) include PQC algorithm support.
- **Automated Key Rotation:** The higher risk of algorithmic breakthroughs in newer PQC algorithms means more frequent key rotation is prudent. Automated rotation: certificates issued with shorter validity, keys rotated via automated pipelines. Crypto-agility enables rotation without application changes.
- **Algorithm Compromise Response:** If a PQC algorithm is broken: (1) revoke all certificates using that algorithm; (2) rotate all keys generated with that algorithm; (3) switch to backup algorithms (the hybrid approach pays off here — classical crypto still protects); (4) re-encrypt affected data. The incident response plan for cryptographic compromise must be tested — it's not hypothetical.

#### Required Reading

- NIST. (2039). SP 800-57: Key Management — PQC Addendum.
- UoY Crypto Ops Lab. (2040). *Algorithm Compromise: Incident Response Playbook*.

---

### Lecture 12: The Cryptographic Horizon — Beyond PQC

**Course:** IT307 — Quantum-Safe Cryptography Migration
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Post-quantum cryptography is the solution for today's quantum threat. But what comes next? This lecture surveys the cryptographic horizon: quantum cryptography (QKD and beyond), fully homomorphic encryption, indistinguishability obfuscation, and the ongoing dance between cryptographers and adversaries that defines the field.

#### Key Topics

- **Quantum Cryptography (QKD):** Quantum Key Distribution uses quantum physics to establish keys with information-theoretic security. Limitations: requires specialized hardware, limited to ~100km without quantum repeaters, point-to-point only. QKD is a niche technology — valuable for specific high-security links but not a replacement for PQC algorithms that work on existing infrastructure.
- **Fully Homomorphic Encryption (FHE):** Compute on encrypted data without decrypting it. By 2040, FHE is practical for certain applications (private database queries, secure multi-party computation) but still 1,000-1,000,000x slower than unencrypted computation. Ongoing research aims to close this gap. FHE does not directly relate to PQC but represents the broader trend toward ubiquitous encryption.
- **The Eternal Dance:** Cryptographic history is: mathematicians develop hard problems → cryptographers build systems on them → attackers (classical and quantum) develop attacks → cryptographers develop new hard problems. PQC is this round's response. The next round is unknown — but the lesson is clear: design for crypto-agility, assume algorithms will be broken, and never tie your security to any single mathematical assumption.

#### Required Reading

- UoY Future Crypto Lab. (2040). *Beyond PQC: The Cryptographic Horizon*.

---

## Final Examination Preparation

### Sample Essay Questions (Choose 4 of 8)

1. **Quantum Threat Analysis:** Explain Shor's and Grover's algorithms, their impact on current cryptography, and why "harvest now, decrypt later" makes migration urgent.

2. **Hybrid Migration Design:** Design a hybrid PQC deployment for a web application. Cover TLS, certificate management, and the transition timeline to PQC-only.

3. **Crypto-Agility Architecture:** Design a crypto-agile architecture that enables algorithm transitions without application changes. Provide specific patterns and antipatterns.

4. **PQC for Data at Rest:** A healthcare organization retains patient records for life. Design a PQC migration strategy for their encrypted databases and backups.

5. **Blockchain PQC:** Design a PQC migration plan for a public blockchain. Address wallet migration, consensus algorithm changes, and governance.

6. **PKI Migration:** Plan the PKI migration for an enterprise with 10,000 internal certificates. Address root CA, issuing CAs, end-entity certificates, and revocation.

7. **Constrained Device PQC:** A smart grid operator has 100,000 field devices with 15-year lifespans running RSA. Design a PQC strategy.

8. **Algorithm Compromise Response:** A lattice-based PQC algorithm is broken. Design the incident response — detection, containment, migration, and lessons.

---

**Þǫkk — May your keys remain secure against all adversaries, classical and quantum alike.**
