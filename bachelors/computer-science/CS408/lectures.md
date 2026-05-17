# CS408: Post-Quantum Cryptographic Engineering & Secure Distributed Systems
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4  
**Prerequisites:** CS301 — Distributed Systems; CS305 — Artificial Intelligence; MATH204 — Abstract Algebra or instructor consent  
**Description:** An advanced elective covering the cryptographic transition of the 2030s-2040s: the design, analysis, and implementation of post-quantum cryptographic systems resilient to attacks by quantum computers. Covers lattice-based cryptography (ML-KEM, ML-DSA), hash-based signatures, zero-knowledge proofs, secure multi-party computation, side-channel-resistant implementation, formal verification, and the engineering challenges of migrating billion-user protocols from RSA/ECC to post-quantum primitives. Students implement and formally verify components of a post-quantum secure messaging system. By 2040, the NIST post-quantum standards are fully deployed; this course prepares engineers to build and audit systems in the post-quantum era.

**Instructor:** Dr. Hákon Erlendsson, Professor of Cryptography & Director, Yggdrasil Centre for Quantum-Safe Systems  
**Lab:** Muninn Computing Centre, Secure Systems Lab (Shielded Room 3 — required for side-channel analysis exercises)  
**Office Hours:** Tuesdays 14:00-16:00, and by encrypted appointment via Signal/MLS

---

## Lectures

ᚠ **Lecture 1: The Quantum Threat — Why RSA and ECC Are Dying**

**Course:** CS408 — Post-Quantum Cryptographic Engineering  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

The cryptographic foundations of the digital world — RSA, Diffie-Hellman, Elliptic Curve Cryptography — rest on a single assumption: that certain mathematical problems are computationally infeasible to solve. RSA depends on the difficulty of integer factorization; ECC depends on the discrete logarithm problem. These assumptions held for fifty years against classical computers. They do not hold against quantum computers. This lecture introduces **Shor's algorithm** (1994), which solves factorization and discrete logarithms in polynomial time on a sufficiently large quantum computer, and explains why the transition to post-quantum cryptography is not a theoretical concern but an immediate engineering imperative. By 2040, the transition is largely complete for critical infrastructure, but the engineering lessons — and the residual risks from "harvest now, decrypt later" attacks — remain vital.

### Key Topics

- **Shor's Algorithm and the Quantum Threat:** A quantum computer with ~4,000 logical qubits can break RSA-2048. Current quantum computers (2040) have hundreds of physical qubits, but error correction and scaling are advancing rapidly. The threat is not today but "cryptographically relevant" — within the lifetime of secrets being encrypted now. A diplomatic cable encrypted today with RSA may be stored and decrypted in 2045 by a quantum adversary.
- **The "Harvest Now, Decrypt Later" (HNDL) Threat:** Adversaries are already collecting encrypted traffic, waiting for quantum computers to decrypt it. This means the transition to post-quantum cryptography cannot wait until quantum computers exist; it must happen now for data with long secrecy requirements (government communications, medical records, infrastructure designs, personal data).
- **NIST Post-Quantum Standardization (2016-2040):** The 20-year journey from NIST's first call for proposals to full deployment. The selected algorithms: **ML-KEM** (Module Lattice-based Key Encapsulation Mechanism, formerly Kyber) for key establishment; **ML-DSA** (Module Lattice-based Digital Signature Algorithm, formerly Dilithium) for signatures; **SLH-DSA** (Stateless Hash-Based Digital Signature Algorithm, formerly SPHINCS+) for high-assurance signatures; and **FN-DSA** (Fast NTRU-based Digital Signature Algorithm, formerly Falcon) for resource-constrained devices.
- **The Post-Quantum Transition Timeline:** 2024 (NIST standards published), 2028 (major browsers and operating systems support hybrid post-quantum TLS), 2032 (government mandates for post-quantum in critical infrastructure), 2035 (financial systems fully migrated), 2040 (the transition is considered complete for new systems, but legacy systems remain a persistent vulnerability).

### Lecture Notes

The cryptographic community spent decades treating quantum computing as a distant theoretical threat. This was a mistake. The correct threat model is not "when will quantum computers exist?" but "when will my encrypted data cease to be secret?" If you encrypt a document today that must remain secret for thirty years, and quantum computers become viable in twenty years, your encryption is already broken — you just don't know it yet.

**Shor's algorithm** is not merely faster than classical factorization; it is fundamentally different. Classical algorithms for factorization (the General Number Field Sieve) have sub-exponential complexity — roughly exp((64/9)^(1/3) * (ln n)^(1/3) * (ln ln n)^(2/3)). For RSA-2048, this requires ~10^29 operations, infeasible for any classical computer. Shor's algorithm requires O((log n)^3) operations — for RSA-2048, roughly 10^9 operations. A quantum computer running at 10 MHz could complete this in minutes. The difference is not incremental; it is categorical.

The **HNDL threat** transforms the quantum computing timeline from a technical question into an immediate policy question. Intelligence agencies have been storing encrypted traffic since the 2010s. The Snowden revelations (2013) confirmed bulk collection; subsequent revelations (2020s) confirmed that adversaries specifically target encrypted data for future decryption. Every RSA-encrypted message sent before the post-quantum transition is potentially readable by future adversaries. This is why the transition cannot wait.

The NIST standardization process was the largest cryptographic competition in history. Eighty-two initial submissions from researchers across six continents were winnowed through three rounds of analysis, cryptanalysis, and implementation testing. The final selections (2024) balanced security, performance, and implementability. **ML-KEM** (Kyber) was selected for its excellent balance of key size, ciphertext size, and computational efficiency. **ML-DSA** (Dilithium) was selected for its conservative security margins and relatively small signatures. **SLH-DSA** (SPHINCS+) provides security based purely on hash function assumptions — no lattice assumptions at all — at the cost of larger signatures. **FN-DSA** (Falcon) offers the smallest signatures but requires floating-point arithmetic and careful Gaussian sampling, making implementation more complex.

By 2040, the transition is substantially complete for new systems. Major browsers negotiate hybrid post-quantum TLS by default. The Yggdrasil computing infrastructure uses ML-KEM for all internal key establishment. But legacy systems — embedded devices with firmware that cannot be updated, old VPN configurations, hardcoded RSA certificates in industrial control systems — remain vulnerable. The post-quantum era is not a destination but a continuous process of migration, monitoring, and vigilance.

### Required Reading

- Bernstein, D.J. & Lange, T. (2037). *Post-Quantum Cryptography*, 3rd Edition. Springer. Chapters 1-3.
- NIST. (2024). *Module-Lattice-Based Key-Encapsulation Mechanism Standard* (FIPS 203). (The foundational specification; read the security considerations section carefully.)
- Mosca, M. (2035). "Cybersecurity in an Era with Quantum Computers: Will We Be Ready?" *IEEE Security & Privacy*. (An update to Mosca's influential 2015 paper, tracking the transition progress.)

### Discussion Questions

1. A government agency argues that post-quantum migration can wait until "cryptographically relevant quantum computers" are demonstrated. Using the HNDL threat model, explain why this argument is dangerous. What is the correct policy response?
2. ML-KEM is based on the hardness of the Module Learning With Errors (MLWE) problem. What would it mean for cryptography if a polynomial-time algorithm for MLWE were discovered tomorrow? Would all post-quantum systems collapse, or are there alternative foundations?
3. Your employer has a legacy embedded system (deployed 2028) that uses RSA-2048 and cannot be firmware-updated in the field. The system controls water treatment infrastructure and must operate until 2055. What are your options? What is the risk, and how do you mitigate it?

---

ᚢ **Lecture 2: Lattice-Based Cryptography — The Mathematics of Hard Problems**

**Course:** CS408 — Post-Quantum Cryptographic Engineering  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

Lattice-based cryptography is the foundation of the NIST post-quantum standards, and understanding it requires comfort with linear algebra, modular arithmetic, and the geometry of numbers. This lecture builds the mathematical scaffolding: **lattices** (discrete additive subgroups of R^n), **shortest vector problems** (SVP, finding the shortest non-zero vector in a lattice), **closest vector problems** (CVP, finding the lattice vector nearest to an arbitrary point), and the **Learning With Errors (LWE)** problem — the computational hardness assumption that underpins ML-KEM and ML-DSA. We develop these concepts from first principles, with concrete examples in small dimensions, and explain why these problems resist both classical and quantum attacks.

### Key Topics

- **Lattices and Bases:** A lattice L in R^n is the set of all integer linear combinations of n linearly independent basis vectors {b_1, ..., b_n}. The same lattice has infinitely many bases; some bases are "good" (short, nearly orthogonal vectors) and some are "bad" (long, highly skewed). The **Hermite normal form** provides a canonical representation. The **Lattice Reduction** problem: given a bad basis, find a good basis. This is believed to be hard for high dimensions.
- **SVP and CVP:** The **Shortest Vector Problem (SVP)**: given a basis, find the shortest non-zero vector in the lattice. The **Closest Vector Problem (CVP)**: given a basis and a target vector t in R^n, find the lattice vector closest to t. Both problems are NP-hard in their exact forms and believed to be hard to approximate within polynomial factors. The **GapSVP** and **GapCVP** variants (distinguishing between "very short/close" and "not very short/close") are the problems used in cryptographic reductions.
- **Learning With Errors (LWE):** Introduced by Regev (2005), LWE is a computational problem that generalizes linear systems with noise. Given a secret vector s in Z_q^n and many pairs (a_i, b_i = <a_i, s> + e_i mod q), where a_i are random and e_i are small random errors, recover s. The hardness of LWE is proven: solving average-case LWE is as hard as solving worst-case GapSVP for certain lattice parameters. This is a **worst-case to average-case reduction** — a rare and powerful property in cryptography.
- **Ring-LWE and Module-LWE:** LWE requires large keys (O(n^2) elements). **Ring-LWE** (Lyuashevsky, Peikert, Regev, 2010) works over polynomial rings R = Z_q[x]/(x^n + 1), reducing key sizes to O(n). **Module-LWE** generalizes Ring-LWE to modules over polynomial rings, offering a flexible security/efficiency trade-off. ML-KEM uses Module-LWE over R = Z_3329[x]/(x^256 + 1) with module rank k = 3 or 4.
- **Concrete Parameter Selection:** How do we choose n, q, and the error distribution? The **Core-SVP hardness model** estimates the cost of the best known attacks (primal and dual lattice attacks) and selects parameters such that the attack requires >2^128 operations. ML-KEM-768 (the recommended parameter set) targets Core-SVP hardness of ~2^182, providing substantial security margin.

### Lecture Notes

Lattice-based cryptography is beautiful because it connects abstract mathematics to practical security through a single elegant assumption: finding short vectors in high-dimensional lattices is hard. This assumption has withstood twenty years of cryptanalysis, including targeted attacks by quantum computers (which provide only a quadratic speedup for lattice problems via Grover's algorithm, unlike the exponential speedup for factorization via Shor's algorithm).

The **geometry of lattices** is intuitive in low dimensions. In 2D, a lattice is a grid of points generated by two basis vectors. The shortest vector problem is easy to visualize: given a skewed grid, find the grid point closest to the origin (excluding the origin itself). In 2D, this is easy — you can enumerate. In 100D, it is believed to be exponentially hard. The intuition: the number of lattice points inside a sphere grows exponentially with dimension, and the ratio of the shortest vector length to the basis vector lengths can be enormous.

**Lattice reduction algorithms** are the practical attacks on SVP. The **LLL algorithm** (Lenstra-Lenstra-Lovász, 1982) finds a "reasonably good" basis in polynomial time, but the approximation factor is exponential in dimension. The **BKZ algorithm** (Block Korkine-Zolotarev) achieves better approximations by solving SVP exactly on smaller blocks, but requires exponential time in the block size. Modern lattice attacks use BKZ with extreme pruning, sieving, and enumeration techniques. The security analysis of ML-KEM assumes the attacker uses the best known combination of these techniques and still requires >2^128 operations.

**The LWE problem** is the computational heart of post-quantum key exchange. Imagine you are trying to learn a secret linear function f(a) = <a, s>, but every evaluation returns a noisy result: f(a) + e. If the noise e is small relative to the modulus q, you can still recover s given enough samples. But if the noise is appropriately scaled, recovery becomes as hard as solving SVP in the worst case. The beauty of Regev's reduction is that it connects the average-case problem (random LWE instances) to the worst-case problem (hardest lattice instances), giving us confidence that random LWE instances are genuinely hard.

**Module-LWE** is the practical refinement that makes ML-KEM efficient. Instead of working with matrices over Z_q (LWE), we work with modules over polynomial rings. The polynomial ring Z_q[x]/(x^n + 1) has a fast multiplication algorithm (Number Theoretic Transform, NTT) that reduces polynomial multiplication from O(n^2) to O(n log n). This makes ML-KEM operations fast enough for real-time protocols: key generation in ~50,000 cycles, encapsulation in ~60,000 cycles, decapsulation in ~70,000 cycles on a standard CPU.

### Required Reading

- Regev, O. (2005/2035). "On Lattices, Learning with Errors, Random Linear Codes, and Cryptography." *JACM*. (The foundational paper; read the proof sketch of the worst-case to average-case reduction.)
- Lyubashevsky, V., Peikert, C., & Regev, O. (2010/2035). "On Ideal Lattices and Learning with Errors Over Rings." *Eurocrypt*. (Ring-LWE and its properties.)
- NIST. (2024). *FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard*. Section 4: "Security."

### Discussion Questions

1. LWE has a worst-case to average-case reduction, but Ring-LWE does not (its reduction is from ideal lattice problems). Does this weaken confidence in Ring-LWE/Module-LWE? What practical evidence supports or undermines their hardness?
2. Why is the NTT (Number Theoretic Transform) critical for ML-KEM's performance? What properties must the polynomial ring have to support NTT? What happens if we choose parameters that do not support NTT?
3. Grover's algorithm provides a quadratic speedup for unstructured search. Why does this not break lattice-based cryptography the way Shor's algorithm breaks RSA? What is the best known quantum attack on SVP, and what is its complexity?

---

ᚦ **Lecture 3: ML-KEM and ML-DSA — The NIST Standards in Depth**

**Course:** CS408 — Post-Quantum Cryptographic Engineering  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

This lecture is a deep technical dive into the two most important NIST post-quantum standards: **ML-KEM** (key encapsulation) and **ML-DSA** (digital signatures). We walk through the algorithms line by line, understand the data formats, analyze the security proofs, and examine the reference implementations. The goal is not merely to use these algorithms (libraries do that) but to understand them well enough to implement, audit, and optimize them. We cover the **IND-CCA2 security** of ML-KEM (indistinguishability under adaptive chosen-ciphertext attack) and the **EUF-CMA security** of ML-DSA (existential unforgeability under chosen-message attack), and explain the engineering decisions that make these standards practical.

### Key Topics

- **ML-KEM Architecture:** A Key Encapsulation Mechanism (KEM) provides three algorithms: **KeyGen** (generate a public/secret key pair), **Encaps** (generate a shared secret and a ciphertext, using the public key), and **Decaps** (recover the shared secret from the ciphertext, using the secret key). ML-KEM-512, -768, and -1024 offer increasing security levels. ML-KEM-768 is the default recommendation (equivalent to AES-192 in classical security). Key sizes: public key ~1,184 bytes, secret key ~2,400 bytes, ciphertext ~1,088 bytes.
- **The Fujisaki-Okamoto Transform:** Raw LWE-based encryption is vulnerable to chosen-ciphertext attacks. The Fujisaki-Okamoto (FO) transform converts a weakly secure public-key encryption scheme into a strongly secure KEM. The idea: the shared secret is derived from the randomness used during encryption, not from the plaintext. During decapsulation, the recipient re-encrypts the recovered plaintext and verifies that the ciphertext matches; if not, the ciphertext is rejected. This implicit rejection provides CCA security without the complexity of explicit rejection codes.
- **ML-DSA Architecture:** A signature scheme providing **KeyGen**, **Sign**, and **Verify**. ML-DSA is a **Fiat-Shamir-with-Aborts** signature scheme: the signer generates a commitment, computes a challenge from the message and commitment, computes a response, and repeats the process until the response satisfies a size bound. The "aborts" mechanism ensures that the signature does not leak information about the secret key. Signature sizes: ~2,420 bytes for ML-DSA-65. Public key sizes: ~1,952 bytes.
- **Implementation Considerations:** Constant-time operations (to prevent timing attacks), rejection sampling (for the FO transform and signature aborts), and the NTT (for fast polynomial arithmetic). The reference implementation uses Montgomery reduction for modular arithmetic and Barrett reduction for coefficient compression. Understanding these optimizations is essential for secure implementation — naive implementations leak information through timing.
- **Hybrid Post-Quantum TLS:** By 2040, TLS 1.4 (finalized 2032) supports **hybrid key exchange**: a classical ECDH share is combined with a post-quantum ML-KEM share, producing a session key that is secure if either mechanism is secure. This provides "cryptographic agility" — if a flaw is found in ML-KEM, the classical component still protects traffic until ML-KEM is replaced.

### Lecture Notes

ML-KEM and ML-DSA are the workhorses of the post-quantum transition. They will be used in billions of connections, signatures, and encrypted messages. Understanding their internals is not academic pedantry — it is necessary for secure implementation. A developer who treats ML-KEM as a black box will make mistakes: using the public key as a secret, reusing ephemeral keys, failing to validate ciphertexts, or implementing the FO transform incorrectly.

**The Fujisaki-Okamoto transform** is the security-critical component of ML-KEM. Without it, an attacker could submit modified ciphertexts and learn information about the secret key from the decapsulation oracle's behavior (error messages, timing). The FO transform prevents this by making the decapsulation process deterministic: given a ciphertext, the decapsulator extracts the candidate plaintext, re-encrypts it with the same randomness, and compares. If the re-encrypted ciphertext matches the received ciphertext, the plaintext is valid; otherwise, the ciphertext is rejected and a pseudorandom shared secret is returned (so the attacker cannot distinguish a valid ciphertext from an invalid one). This implicit rejection is elegant but subtle — implementation errors here have led to real vulnerabilities in deployed systems.

**ML-DSA's Fiat-Shamir-with-Aborts** is equally subtle. The signer generates a random vector y, computes a commitment w = Ay (where A is a public matrix), derives a challenge c from H(message || w), computes z = y + cs, and checks whether z is "small enough." If not, the signer aborts and tries again. The abort mechanism is essential: if the signer always published z, an attacker could solve for the secret key s using linear algebra over many signatures. The aborts introduce non-linearity that prevents this attack. But the aborts also mean that signing time is variable — a potential timing side channel that must be masked.

**Constant-time implementation** is non-negotiable for both ML-KEM and ML-DSA. The FO transform's comparison must be done in constant time (comparing all bytes regardless of where a mismatch occurs). The ML-DSA abort loop must not leak the number of iterations through timing. Polynomial multiplication must not use data-dependent memory accesses. These requirements make post-quantum implementations significantly more complex than classical cryptography, where constant-time arithmetic is well-understood. The Yggdrasil Secure Systems Lab maintains a formally verified ML-KEM implementation in Rust, which serves as the reference for all university systems.

**Hybrid TLS** is the pragmatic bridge between classical and post-quantum security. By combining an X25519 share with an ML-KEM-768 share, TLS 1.4 ensures that an attacker must break both mechanisms to recover the session key. This protects against two failure modes: a cryptanalytic breakthrough in ML-KEM (unlikely but not impossible) and a quantum computer that breaks X25519 (inevitable in the long term). The hybrid approach increases handshake size by ~1,200 bytes — acceptable for most applications, but a concern for constrained environments.

### Required Reading

- NIST. (2024). *FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard*. (Read algorithms 12-14: KeyGen, Encaps, Decaps.)
- NIST. (2024). *FIPS 204: Module-Lattice-Based Digital Signature Standard*. (Read algorithms 1-3: KeyGen, Sign, Verify.)
- Schanck, J.M. (2035). "A Survey of Attacks on the NIST Post-Quantum Standards." *Crypto ePrint Archive*. (A comprehensive analysis of known attack vectors and implementation pitfalls.)

### Discussion Questions

1. The FO transform's implicit rejection returns a pseudorandom shared secret for invalid ciphertexts. Why is this safer than explicit rejection (returning an error)? What implementation mistakes have occurred with explicit rejection in real-world deployments?
2. ML-DSA signing involves an abort loop with variable iteration count. How do you implement this in constant time? What is the performance cost, and how do modern implementations mitigate it?
3. Hybrid TLS increases handshake size by ~1,200 bytes. For a mobile application with millions of users on metered connections, is this acceptable? What optimizations exist, and when might you choose pure post-quantum over hybrid?

---

ᚨ **Lecture 4: Hash-Based and Alternative Post-Quantum Signatures**

**Course:** CS408 — Post-Quantum Cryptographic Engineering  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

Lattice-based signatures are efficient but rely on relatively new hardness assumptions. **Hash-based signatures** offer a conservative alternative: their security depends only on the hardness of collision-resistant hash functions (a well-studied assumption with no known quantum speedup beyond Grover's algorithm). This lecture covers the two NIST-standardized hash-based schemes — **SLH-DSA** (SPHINCS+) and **XMSS** (eXtended Merkle Signature Scheme) — as well as code-based signatures (FN-DSA/Falcon, based on NTRU lattices) and isogeny-based key exchange (SIKE, now broken, and its lessons). We analyze the trade-offs: hash-based signatures have small keys but large signatures; code-based signatures have small signatures but complex implementation; isogeny-based schemes were elegant but fell to classical attacks.

### Key Topics

- **Lamport and Winternitz One-Time Signatures (OTS):** The foundation of hash-based cryptography. A Lamport signature uses a secret key of 2n hash values (for n-bit messages) and a public key of their hashes. It signs one message securely; reusing the key breaks security. Winternitz signatures compress the secret key by signing multiple bits per hash chain, at the cost of increased signature size. These are **one-time signatures** — the key can be used once only.
- **Merkle Trees and Many-Time Signatures:** To sign multiple messages, combine many OTS keys in a Merkle tree. The public key is the root hash; each leaf is an OTS key. To sign message i, use OTS key i and include the authentication path (sibling hashes) from leaf i to the root. **XMSS** and **XMSS^MT** (multi-tree XMSS) are stateful Merkle schemes: the signer must track which OTS keys have been used. **SLH-DSA** (SPHINCS+) is stateless: it uses a hypertree of Merkle trees and a few-time signature scheme (FORC) at the leaves, allowing unlimited signatures without state.
- **SLH-DSA (SPHINCS+) in Detail:** A hyper-tree of height h, divided into d layers of subtrees. Each leaf of the bottom-level subtree is a FORS (Forest of Random Subsets) few-time signature key. A message is hashed to select FORS indices; the FORS signature and authentication paths through all d layers constitute the final signature. Signature sizes: ~7,800 bytes (SLH-DSA-128s) to ~49,000 bytes (SLH-DSA-256f). Public key: 32 or 64 bytes. Private key: 64 bytes.
- **FN-DSA (Falcon):** Based on the NTRU lattice problem, which predates LWE. Falcon uses the **Fast Fourier Sampling** technique to generate short lattice vectors from a public basis, producing signatures as small as ~666 bytes (FN-DSA-512). The implementation requires floating-point arithmetic, discrete Gaussian sampling, and careful handling of numerical stability — making it the most complex NIST standard to implement securely.
- **The SIKE Story:** Supersingular Isogeny Diffie-Hellman (SIDH/SIKE) was a promising candidate based on isogeny walks between elliptic curves. It had extremely small key sizes (~300 bytes) and elegant mathematics. In 2022, Castryck and Decru found a devastating classical attack using auxiliary isogenies. The attack was extended and refined; SIKE was withdrawn from the NIST process. The lesson: new mathematical structures may hide unexpected algebraic structures. Cryptographic conservatism is warranted.

### Lecture Notes

Hash-based signatures are the **conservative choice** in post-quantum cryptography. If SHA-3-256 is secure, then SLH-DSA-128s is secure. This is a remarkably small assumption compared to the lattice assumptions underlying ML-KEM and ML-DSA. For high-assurance applications — signing firmware updates, root certificates, long-term archival signatures — this conservatism is worth the cost of larger signatures.

The **one-time signature limitation** is the defining constraint of hash-based cryptography. A Lamport key can sign exactly one message securely; if you sign two messages with overlapping bit patterns, an attacker can combine the revealed hash preimages to forge signatures on other messages. Merkle trees solve this by binding each OTS key to a leaf and authenticating the leaf path. But the signer must know which leaf to use next — this is **state**. XMSS requires the signer to maintain state (a counter of used leaves) and never reuse a leaf. For embedded devices with unreliable storage, this is a serious operational hazard.

**SLH-DSA's statelessness** is its defining innovation. Instead of pre-generating all OTS keys in a Merkle tree, SLH-DSA generates them on the fly using a pseudo-random function (PRF) keyed by the master secret. The message hash deterministically selects which FORS key to use, and the hypertree structure ensures that the same leaf is unlikely to be reused. This eliminates the state management problem but increases signature size: the signature must include the full authentication path through d layers of Merkle trees plus the FORS signature.

The **signature size trade-off** is the central engineering decision. ML-DSA signatures are ~2.4KB; SLH-DSA signatures are ~8-50KB; FN-DSA signatures are ~0.7KB. For TLS certificates (transmitted once per connection), ML-DSA is ideal. For firmware update signatures (where every device must download and verify), SLH-DSA's larger signatures may be problematic for bandwidth-constrained devices. FN-DSA offers the best size but the most complex implementation.

The **SIKE collapse** is a cautionary tale. SIDH was mathematically elegant, had small parameters, and seemed to resist both classical and quantum attacks for years. Then a single paper introduced an attack that recovered the secret key in polynomial time. The attack exploited the auxiliary isogeny structure that had been overlooked in security proofs. Within months, SIKE was withdrawn. The lesson is not that post-quantum cryptography is fragile — it is that **new assumptions require more scrutiny than old ones**. ML-KEM and ML-DSA are based on problems that have been studied for over a decade; SIKE was based on a problem that had been studied for less time and had a more complex algebraic structure.

### Required Reading

- Hülsing, A. et al. (2036). *SPHINCS+ (SLH-DSA) — Stateless Hash-Based Signatures*, 2nd Edition. Springer. (The authoritative reference; read the security analysis carefully.)
- Fouque, P.A. & Hoffstein, J. (2035). "NTRU and Lattice-Based Cryptography: A Historical Perspective." *Journal of Cryptology*. (The story of NTRU, from 1996 to FN-DSA.)
- Castryck, W. & Decru, T. (2022). "An Efficient Key Recovery Attack on SIDH." *Eurocrypt*. (The paper that broke SIKE; read it to understand how hidden algebraic structure can undermine apparently secure systems.)

### Discussion Questions

1. For a certificate authority that issues ~1 million certificates per day, would you recommend ML-DSA, SLH-DSA, or FN-DSA? Consider key generation time, signing time, signature size, verification time, and security assumptions. What is your recommendation and why?
2. SLH-DSA's statelessness relies on the assumption that the PRF does not produce collisions in leaf selection. What is the concrete security bound for this assumption? Under what circumstances might stateful XMSS be preferable despite the operational complexity?
3. The SIKE attack exploited "auxiliary isogenies" that were not considered in the original security proof. What does this tell us about the role of cryptanalytic community scrutiny? Should NIST have required a longer evaluation period for isogeny-based schemes?

---

ᚱ **Lecture 5: Zero-Knowledge Proofs — Proving Without Revealing**

**Course:** CS408 — Post-Quantum Cryptographic Engineering  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

A **zero-knowledge proof (ZKP)** allows one party (the prover) to convince another party (the verifier) that a statement is true, without revealing any information beyond the truth of the statement. This seemingly magical property has become one of the most important tools in modern cryptography, with applications in authentication, blockchain privacy, verifiable computation, and identity systems. This lecture covers the foundations: interactive proofs, the **Fiat-Shamir heuristic** (making interactive proofs non-interactive), **zk-SNARKs** (zero-knowledge Succinct Non-interactive ARguments of Knowledge), and **zk-STARKs** (Scalable Transparent ARguments of Knowledge). We examine the trade-offs between proof size, verification time, prover time, and trusted setup requirements, and implement a simple ZK proof for set membership using the Bulletproofs framework.

### Key Topics

- **The Definition of Zero-Knowledge:** Formally, a proof system is zero-knowledge if there exists a simulator that can produce a transcript indistinguishable from a real interaction, without access to the witness. The three properties: **completeness** (an honest prover convinces an honest verifier), **soundness** (a dishonest prover cannot convince the verifier of a false statement), and **zero-knowledge** (the verifier learns nothing beyond the statement's truth). The **knowledge extraction** property: if a prover convinces the verifier, there exists an extractor that can recover the witness — proving that the prover actually "knows" the secret, not merely that the statement is true.
- **zk-SNARKs:** The most widely deployed ZK construction. A zk-SNARK for a computation C(x, w) allows the prover to demonstrate knowledge of a witness w such that C(x, w) = 0, with a proof that is O(1) in size and verifiable in O(1) time (relative to the computation size). The cost: a **trusted setup** ceremony that generates public parameters. If the setup is compromised, fake proofs can be generated. Applications: Zcash (private cryptocurrency transactions), Tornado Cash (private Ethereum transfers), and identity systems (proving age without revealing birthdate).
- **zk-STARKs:** An alternative that eliminates the trusted setup, using hash functions and Reed-Solomon codes instead of elliptic curve pairings. The trade-off: larger proof sizes (~50-100KB vs. ~200 bytes for SNARKs) but faster prover time, post-quantum security (no elliptic curves), and no trusted setup. By 2040, zk-STARKs have largely supplanted zk-SNARKs in new deployments due to the trusted setup risk.
- **Bulletproofs:** A ZK proof system with no trusted setup, logarithmic proof size, and linear verification time. Bulletproofs are particularly efficient for **range proofs** (proving that a committed value is in a range [0, 2^n]) and have been adopted by Monero (private transaction amounts) and other systems. The proof size is 2 log_2(n) + 13 group elements — for a 64-bit range, roughly 672 bytes.
- **Applications in 2040:** Privacy-preserving identity (proving vaccination status without revealing medical history), verifiable machine learning (proving that a model was trained on specific data without revealing the data), anonymous credentials (proving membership in a group without revealing identity), and regulatory compliance (proving that a transaction meets legal requirements without revealing the transaction details).

### Lecture Notes

Zero-knowledge proofs are the closest thing cryptography has to magic. The prover convinces the verifier of a profound truth — "I know the solution to this Sudoku puzzle" or "I am over 18 years old" or "this encrypted transaction is valid" — without revealing the Sudoku solution, the birthdate, or the transaction amount. This capability transforms what is possible in digital systems: privacy and verifiability, which were previously in tension, become simultaneously achievable.

The **Fiat-Shamir heuristic** is the bridge from theory to practice. Interactive ZK proofs require back-and-forth communication between prover and verifier, which is impractical for many applications. Fiat-Shamir replaces the verifier's random challenges with hash function outputs: the prover hashes the protocol transcript so far to generate the challenge locally. This makes the proof non-interactive and publicly verifiable — anyone can verify it without talking to the prover. But Fiat-Shamir must be applied carefully: if the hash input does not include all prior protocol messages, the proof can be forged. Multiple real-world vulnerabilities (including a critical flaw in the SwissPost e-voting system, 2019) resulted from incorrect Fiat-Shamir application.

**zk-SNARKs** achieve the remarkable property of constant proof size and constant verification time, regardless of how complex the underlying computation is. A SNARK proof that "I correctly executed a program with 10^9 steps" is ~200 bytes and verifies in milliseconds. The program could be a neural network inference, a cryptographic protocol, or a database query. The verification cost does not scale with the computation size — this is what makes SNARKs suitable for blockchain verification, where every node must check every proof. The trusted setup is the Achilles heel: the 2016 Zcash ceremony required six participants, with the security guarantee that the proof is sound if *any one* participant was honest and destroyed their secret. By 2040, multi-party computation ceremonies have become routine, but the fundamental risk remains.

**zk-STARKs** eliminate the trusted setup at the cost of larger proofs. A STARK proof for the same 10^9-step computation might be ~100KB — still small enough for most applications, but 500× larger than a SNARK. The trade-off is often worth it: the Yggdrasil identity system uses STARKs for age verification because the trusted setup risk of SNARKs was deemed unacceptable for government-adjacent infrastructure. The post-quantum security of STARKs (relying only on hash functions) is an additional advantage as the quantum transition proceeds.

The **Yggdrasil Anonymous Credential System** (YACS) is a university research project that applies ZK proofs to student services. A YACS credential allows a student to prove: "I am enrolled in a CS course" without revealing which course; "I have a GPA above 3.5" without revealing the exact GPA; "I am over 21" without revealing their birthdate. The credential issuer (the university registrar) signs a commitment to the student's attributes; the student generates ZK proofs about those attributes without revealing the underlying values. This system is deployed for library access, event admission, and alcohol purchases on campus.

### Required Reading

- Goldreich, O., Micali, S., & Wigderson, A. (2035). "Proofs that Yield Nothing but Their Validity." *JACM* (Reprint of the 1991 foundational paper with 2040 commentary.)
- Ben-Sasson, E., Bentov, I., Horesh, Y., & Riabzev, M. (2038). "Scalable, Transparent, and Post-Quantum Secure Computational Integrity." *IACR ePrint*. (The STARK construction; read the security analysis.)
- Bünz, B., Bootle, J., Boneh, D., Poelstra, A., Wuille, P., & Maxwell, G. (2035). "Bulletproofs: Short Proofs for Confidential Transactions and More." *IEEE S&P*. (The Bulletproofs construction and applications.)

### Discussion Questions

1. The Fiat-Shamir heuristic is widely used but has been incorrectly applied in multiple deployed systems, leading to vulnerabilities. What is the correct way to apply Fiat-Shamir? Why do implementers keep making the same mistake, and what tooling or verification approaches could prevent it?
2. Your organization must choose between zk-SNARKs (small proofs, trusted setup) and zk-STARKs (larger proofs, no trusted setup) for a privacy-preserving identity system. The system will be used by 500 million citizens and must last 30 years. What do you choose, and what is your reasoning?
3. Zero-knowledge proofs are sometimes criticized as "cryptographic overkill" for simple applications. When is a ZK proof necessary, and when is a simpler mechanism (hash commitment, Merkle proof) sufficient? Give specific criteria.

---

ᚲ **Lecture 6: Secure Multi-Party Computation — Computing on Encrypted Data**

**Course:** CS408 — Post-Quantum Cryptographic Engineering  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

**Secure Multi-Party Computation (MPC)** allows multiple parties to jointly compute a function over their inputs while keeping those inputs private. The classic scenario: two millionaires want to know who is richer, without revealing their actual wealth. The general result: any function can be computed securely by n parties, as long as a majority is honest (or, in different models, as long as fewer than n/2 parties are corrupted). This lecture covers the foundational results: **Yao's garbled circuits**, the **GMW protocol**, **secret sharing** (Shamir's scheme), and the practical optimizations that have made MPC feasible for real applications by 2040. We examine case studies: private set intersection (determining shared contacts without revealing all contacts), secure machine learning (training models on private datasets from multiple hospitals), and threshold cryptography (distributing a signing key across multiple devices so that no single device can sign alone).

### Key Topics

- **Yao's Garbled Circuits:** The first general solution for two-party computation (2PC). One party (the garbler) encrypts a boolean circuit gate-by-gate, such that evaluating the garbled circuit reveals only the output, not the inputs. The other party (the evaluator) uses oblivious transfer to obtain the garbled input labels corresponding to their private input, then evaluates the circuit. Modern optimizations: free XOR gates (no encryption needed for XOR), row reduction (reducing garbled table size by 25%), and half-gates (reducing size by another 50%).
- **Secret Sharing and GMW:** Shamir's **(t, n)-threshold secret sharing** splits a secret s into n shares, such that any t shares can reconstruct s, but any t-1 shares reveal nothing. The **GMW protocol** (Goldreich-Micali-Wigderson) extends secret sharing to arbitrary computations: parties secret-share their inputs, then jointly evaluate the circuit using local operations and communication for non-linear gates. GMW generalizes to n parties and provides security against semi-honest adversaries (parties that follow the protocol but try to learn extra information).
- **MPC in Practice — The 2040 Landscape:** Protocols like **SPDZ** (for dishonest majority with preprocessing), **MP-SPDZ** (a unified implementation framework), and **MOTION** (for malicious security with low communication) have made MPC practical for applications with tens of parties and billions of gates. The **Yggdrasil Medical Privacy Network** uses MPC to train diagnostic AI models on patient data from twelve Nordic hospitals without any hospital revealing its data. The **Nordic Tax Authority Consortium** uses MPC to detect cross-border tax fraud by jointly computing risk scores without sharing raw financial data.
- **Threshold Cryptography:** A special case of MPC where the secret is a cryptographic key. A **(t, n)-threshold signature scheme** distributes a signing key such that any t parties can sign, but t-1 cannot. This eliminates single points of failure: a compromised device cannot forge signatures, and lost devices do not prevent signing (as long as t devices are available). Threshold ECDSA and threshold BLS signatures are deployed in cryptocurrency custody; threshold ML-DSA is an active research area.
- **Performance and Communication Costs:** MPC is fundamentally communication-intensive. Yao's protocol requires O(|C|) symmetric key operations and O(|C|) bits of communication for 2PC. GMW requires O(|C| * n^2) communication for n parties. The preprocessing model (generating correlated randomness in advance) reduces online latency but increases total computation. For large computations, **MPC-friendly primitives** (arithmetic circuits over finite fields, rather than boolean circuits) reduce cost by orders of magnitude.

### Lecture Notes

Secure multi-party computation is one of the most profound achievements in theoretical computer science: the proof that distrusting parties can collaborate without trusting each other. The **Feasibility Theorem** (Yao 1982, Goldreich-Micali-Wigderson 1987): for any probabilistic polynomial-time function f and any number of parties n, there exists a protocol that securely computes f in the presence of semi-honest adversaries. For malicious adversaries (who may deviate arbitrarily from the protocol), the result holds against minority corruptions.

**Yao's garbled circuits** are the practical foundation of 2PC. The intuition: instead of computing a circuit directly, we compute an encrypted version where each wire value is represented by a random label, and each gate output is determined by a garbled truth table. The evaluator learns only the output labels, not the input labels or intermediate values. The security relies on the encryption scheme: the evaluator cannot decrypt entries in the garbled table that do not correspond to the actual wire values.

The **free XOR optimization** is a beautiful example of cryptographic engineering. In standard garbling, every gate requires encrypting and transmitting a garbled truth table. But XOR gates have a special property: if wire labels are chosen such that the XOR of the two possible labels for each wire is a global constant Δ, then the output label of an XOR gate is simply the XOR of the input labels — no encryption, no communication. This optimization, discovered independently by Kolesnikov and Schneider (2008), reduces garbled circuit size by ~30% for typical circuits.

**SPDZ** (pronounced "Speedz") is the protocol that made MPC practical for machine learning. The insight: separate the protocol into an expensive **offline phase** (generating multiplication triples via somewhat homomorphic encryption or oblivious transfer) and a fast **online phase** (local computation plus one round of communication per multiplication gate). For neural network training, the offline phase may take hours, but the online phase processes each training iteration in milliseconds. The Yggdrasil Medical Privacy Network uses this model: hospitals run the offline phase nightly (generating triples for the next day's training), then participate in the online phase during working hours.

**Threshold cryptography** is MPC's most commercially successful application. Cryptocurrency custody is the driving use case: no exchange wants to store its signing key on a single server (theft risk) or in a single hardware security module (failure risk). Instead, the key is split across three or more devices, with a threshold of two required to sign. Even if one device is compromised, the attacker cannot sign. Even if one device fails, the exchange can still sign. The **Yggdrasil Threshold Wallet** (a research project in collaboration with the Nordic Central Bank's CBDC team) extends this to ML-DSA, providing post-quantum threshold signatures for national digital currency infrastructure.

### Required Reading

- Lindell, Y. & Pinkas, B. (2037). *Secure Multiparty Computation and Secret Sharing*, 2nd Edition. Cambridge University Press. Chapters 1-4, 7-8.
- Damgård, I. et al. (2036). "MP-SPDZ: A Versatile Framework for Multi-Party Computation." *ACM CCS*. (The implementation reference for modern MPC.)
- Gennaro, R. & Goldfeder, S. (2035). "Fast Multiparty Threshold ECDSA with Fast Trustless Setup." *Crypto*. (Threshold signatures and their practical deployment.)

### Discussion Questions

1. Yao's garbled circuits are secure against semi-honest adversaries but not malicious adversaries without additional mechanisms. What is the difference, and what techniques (cut-and-choose, authenticated garbling) provide malicious security? What is the performance cost?
2. The Yggdrasil Medical Privacy Network trains AI models on patient data from twelve hospitals using MPC. A hospital suspects the model may be memorizing patient data. How can they verify that the MPC protocol does not leak information? What are the limits of MPC privacy guarantees?
3. Threshold signatures eliminate single points of failure but introduce new risks: what if t parties collude? What if the key generation ceremony is subverted? How do you balance redundancy against collusion resistance?

---

ᚷ **Lecture 7: Side-Channel Resistance — The Implementation Is the Attack Surface**

**Course:** CS408 — Post-Quantum Cryptographic Engineering  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

A cryptographic algorithm may be mathematically secure, but its implementation can leak secrets through **side channels**: timing (operations that take longer for certain inputs), power consumption (variations in electrical draw that correlate with secret data), electromagnetic radiation (RF emissions from the CPU), cache behavior (memory access patterns that reveal secret-dependent branches), and acoustic emissions (sounds produced by capacitors and voltage regulators). This lecture covers the taxonomy of side-channel attacks, **constant-time programming** (writing code whose execution path does not depend on secrets), **masking** (splitting secrets into random shares such that any single observation reveals nothing), and **hardened implementations** of ML-KEM and ML-DSA. The lab session includes a power analysis attack on an unprotected AES implementation and the corresponding countermeasures.

### Key Topics

- **Timing Attacks:** Introduced by Kocher (1996). The execution time of cryptographic operations often depends on secret values: conditional branches (if (secret) { heavy_op(); }), cache misses (array lookups indexed by secret), and variable-time arithmetic (division, modular reduction). Attack model: the adversary measures thousands of execution times, correlates them with hypothesized secret values, and recovers the key. Defense: constant-time programming — no secret-dependent branches, no secret-dependent memory accesses, no variable-time operations on secret data.
- **Power Analysis:** **Simple Power Analysis (SPA)** directly observes power traces to identify operations ("this spike is a multiplication, so the secret bit is 1"). **Differential Power Analysis (DPA)** statistically correlates power traces with hypothetical intermediate values, recovering secrets even when individual traces are noisy. **Correlation Power Analysis (CPA)** is the most powerful variant: the attacker computes the Pearson correlation between measured power consumption and predicted power consumption (based on a power model like the Hamming weight of intermediate values). Defenses: masking (splitting every secret variable into two or more shares), shuffling (randomizing the order of operations), and power-balancing circuits.
- **Cache Attacks:** **Flush+Reload** and **Prime+Probe** exploit the CPU cache as a side channel. In Flush+Reload, the attacker flushes a cache line, waits for the victim to run, then measures the reload time — fast means the victim accessed the line, slow means they didn't. This reveals secret-dependent memory accesses. Defenses: cache-aware algorithm design (avoiding table lookups indexed by secrets), software-based cache partitioning, and hardware cache randomization (implemented in the Yggdrasil-9 processor).
- **Spectre and Meltdown:** The 2018 revelations that speculative execution leaks secrets across security boundaries. Spectre exploits branch prediction: the CPU speculatively executes code past a bounds check, leaving traces in the cache that reveal out-of-bounds data. Meltdown exploits out-of-order execution: the CPU executes instructions before privilege checks complete, allowing user-mode code to read kernel memory. By 2040, new variants continue to emerge; mitigation requires a combination of hardware changes (speculation barriers), software changes (retpolines, site isolation), and architectural changes (privileged access isolation).
- **Constant-Time Implementation of ML-KEM:** The NTT must not have data-dependent memory accesses. The FO transform's comparison must compare all bytes regardless of mismatch position. The rejection sampling loop must have constant iteration count or be padded. The reference implementation uses bitwise operations for conditional selection (cmov) rather than branches. The Yggdrasil formally verified ML-KEM implementation proves these properties using the **dudect** (distinguishing attacks using differential testing) tool for statistical testing and the **ct-verif** tool for formal verification.

### Lecture Notes

Side-channel attacks are the most insidious threat in cryptography because they exploit the gap between mathematical abstraction and physical reality. The RSA algorithm says "computing d from (n, e) is hard" — but it says nothing about whether the time to compute x^d mod n leaks information about d. The AES algorithm says "without the key, ciphertext is indistinguishable from random" — but it says nothing about whether the power consumption during the SubBytes operation reveals the key byte.

**Constant-time programming** is the first line of defense. The rules are simple in principle: never branch on secrets, never index memory by secrets, never perform variable-time operations on secrets. In practice, this is surprisingly difficult. Compilers optimize away "unnecessary" operations, potentially reintroducing branches. Hardware speculates past barriers, potentially leaking information. Operating systems interrupt execution, introducing timing variations. Achieving true constant time requires cooperation across the entire stack: algorithm design, implementation language, compiler flags, and hardware features.

The **dudect** tool illustrates the statistical approach to verification. Instead of proving constant time (which is difficult and may require formal methods), dudect tests for constant time by executing the target function on two classes of inputs (differing in a secret bit) thousands of times and applying statistical tests (t-test, Welch's test) to the timing distributions. If the distributions are statistically distinguishable, the implementation is not constant time. Dudect has found timing leaks in widely used libraries, including OpenSSL and libsodium.

**Masking** is the defense of last resort when constant time is impossible or insufficient. The idea: split a secret x into two shares (x = a ⊕ b, where a is random), perform all computations on the shares separately, and recombine only at the end. A single observation of the computation reveals only one share, which is uniformly random and independent of x. **Higher-order masking** uses more shares (x = a ⊕ b ⊕ c) to resist attacks that combine multiple observations. The cost: computation and memory increase linearly with the number of shares. First-order masking (2 shares) is standard; second-order masking (3 shares) is used for high-assurance applications.

The **Yggdrasil-9 processor** includes hardware features for side-channel resistance: cache randomization (the cache set index is XORed with a process-specific key, preventing Prime+Probe), speculation barriers (instructions that prevent speculative execution past a boundary), and a constant-time multiplier (integer multiplication takes the same number of cycles regardless of operand values). These features reduce but do not eliminate the need for careful software implementation.

### Required Reading

- Kocher, P. et al. (1996/2035). "Introduction to Differential Power Analysis and Related Attacks." (The foundational paper; read with the 2035 commentary on modern variants.)
- Reparaz, O. (2036). "Detecting Flawed Masking Implementations with leakage Detection." *IEEE S&P*. (On verifying that masking actually works in practice.)
- Almeida, J.B. et al. (2036). "Verifying Constant-Time Implementations." *USENIX Security*. (The ct-verif formal verification approach.)

### Discussion Questions

1. Your compiler optimizes away your carefully written constant-time code, reintroducing a branch. How do you prevent this? What compiler flags, language features, and verification tools do you use?
2. First-order masking protects against attacks that observe a single point in time. Second-order masking protects against attacks that correlate two observations. Why is second-order masking rarely used in practice despite its stronger security?
3. The Yggdrasil-9 processor has hardware cache randomization. Does this mean software developers no longer need to worry about cache attacks? What attacks does hardware randomization not prevent?

---

ᚹ **Lecture 8: Formal Verification — Proving Correctness of Cryptographic Code**

**Course:** CS408 — Post-Quantum Cryptographic Engineering  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

Testing can show the presence of bugs but not their absence. **Formal verification** proves the absence of bugs — for specific properties, with mathematical certainty. This lecture covers the application of formal methods to cryptographic code: **theorem proving** (using Coq, Isabelle/HOL, or Lean to write machine-checked proofs of algorithm correctness), **symbolic execution** (exploring all execution paths of a program to find bugs), **SMT-based verification** (using satisfiability modulo theories solvers to check assertions), and **cryptographic proof assistants** (tools specifically designed for game-based cryptographic proofs). We examine the Yggdrasil formally verified ML-KEM implementation as a case study: how it was specified, what properties were proved, what assumptions were made, and what gaps remain.

### Key Topics

- **Specification and Correctness Properties:** What does it mean for ML-KEM to be "correct"? Three levels: **functional correctness** (the implementation matches the mathematical specification), **memory safety** (no buffer overflows, use-after-free, or null dereferences), and **security properties** (constant-time execution, no secret leakage). Each level requires different verification techniques and different levels of effort.
- **Theorem Proving with Coq/Lean:** The highest-assurance approach. The algorithm is specified in the proof assistant's logic, the implementation is written in the proof assistant's programming language (Gallina for Coq, Lean for Lean), and a proof script demonstrates that the implementation refines the specification. The **CompCert** verified C compiler extends this to compiled code, proving that the generated assembly matches the source semantics. The cost: enormous effort (person-years for complex systems), specialized expertise, and limitations on what can be verified (non-determinism, external calls, hardware behavior).
- **Symbolic Execution with KLEE/Angr:** Automated exploration of all program paths, generating inputs that trigger each path and checking assertions at each step. Symbolic execution is powerful for finding bugs but suffers from path explosion (the number of paths grows exponentially with branches and loops). Techniques to manage path explosion: path merging, state pruning, and targeted symbolic execution (focusing on critical functions).
- **SMT-Based Verification with Z3/CVC5:** Programmers write assertions and invariants; the SMT solver checks whether they hold for all possible inputs. Tools: **F** (a functional programming language with SMT-based refinement types), **Dafny** (an imperative language with built-in verification), and **RustHorn** (a verification tool for Rust based on Horn clauses). These tools scale better than theorem provers but provide less assurance — they verify the properties you specify, not "correctness" in general.
- **The Yggdrasil Verified ML-KEM:** A hybrid verification approach. The NTT and polynomial arithmetic are verified in Coq (functional correctness and memory safety via VST — Verified Software Toolchain). The constant-time properties are verified using ct-verif (SMT-based). The top-level KEM algorithms are verified by refinement from the FIPS 203 pseudocode using the **cryptoline** tool. The result: the C implementation has machine-checked proofs of functional correctness, memory safety, and constant-time execution for the core components. The verification took ~18 person-months; the resulting confidence is proportional.

### Lecture Notes

Formal verification is the gold standard of software assurance, but it is not a panacea. A verified program is only as correct as its specification. If the specification omits a security property ("we forgot to require that decapsulation rejects malformed ciphertexts"), the verification proves nothing about that property. If the specification contains a bug ("we specified the wrong modulus"), the verification proves that the implementation matches a wrong specification. Verification shifts the problem from "is the code correct?" to "is the specification correct?" — a different but equally difficult question.

**Theorem proving** provides the highest assurance because the proof is checked by a small, trusted kernel (the proof assistant's type checker). The CompCert C compiler is the canonical example: it is proved in Coq that the generated assembly has the same semantics as the source C code, modulo memory layout. This means that a bug in CompCert would require a bug in Coq's kernel — which has been used for decades and is extremely small (~10,000 lines of OCaml). The Yggdrasil ML-KEM verification uses VST, which connects C code to Coq specifications via separation logic, a powerful logic for reasoning about pointer programs.

**Symbolic execution** is the bug-finding workhorse. Tools like KLEE can explore all paths through a cryptographic function and find assertion violations, division by zero, or out-of-bounds accesses. But symbolic execution struggles with loops (unrolling to a fixed depth misses bugs beyond that depth) and external calls (modeling the operating system and library functions is incomplete). For ML-KEM, symbolic execution found several off-by-one errors in reference implementations that had been missed by thousands of tests.

**SMT-based verification** occupies the middle ground: more automated than theorem proving, more complete than testing. The F* programming language, developed at Microsoft Research and used by the Yggdrasil verification team, allows programmers to write code with refinement types (types that include predicates, like `x:int{x >= 0 && x < 256}`) and have Z3 verify that these predicates hold. The **HACL*** library (verified cryptographic primitives in F*) is used by Mozilla Firefox, WireGuard, and the Linux kernel. By 2040, HACL* includes verified implementations of ChaCha20, Poly1305, Curve25519, SHA-3, and — in a research branch — ML-KEM.

The lesson of formal verification in cryptography is that it is feasible, valuable, and incomplete. Feasible: teams of 2-4 verification engineers can produce a verified core in under two years. Valuable: the verified components have had zero bugs in deployment, while unverified counterparts have had multiple vulnerabilities. Incomplete: the verification covers only the properties that were specified, and the trusted computing base (compiler, operating system, hardware) remains unverified. The goal is not perfect security but **demonstrable security** — the ability to show, with mathematical rigor, that specific critical properties hold.

### Required Reading

- Appel, A.W. (2036). *Verified Functional Algorithms in Coq*. Cambridge University Press. (Introduction to Coq verification; Chapters 1-4 for background.)
- Bhargavan, K. et al. (2037). "HACL*: A Verified Modern Cryptographic Library." *JACM*. (The HACL* verification project and its applications.)
- Protzenko, J. et al. (2036). "Verified Low-Level Programming Embedded in F*." *ICFP*. (The F* approach to verified systems programming.)

### Discussion Questions

1. Formal verification proves that implementation matches specification. But the specification for ML-KEM (FIPS 203) is pseudocode, not formal logic. How do you bridge this gap? What are the risks of formalizing pseudocode, and how does the Yggdrasil team handle ambiguity?
2. A verified compiler like CompCert generates slower code than GCC or Clang. For a performance-critical cryptographic library, is the assurance worth the speed penalty? Under what circumstances would you use a verified compiler, and when would you verify the assembly directly?
3. Symbolic execution found a bug in ML-KEM that testing missed. The bug was in error handling for an edge case that occurs with probability < 2^-128. Is finding such a bug valuable, or is it "academic" because it will never occur in practice? What is your criteria for judging the severity of rare bugs?

---

ᚺ **Lecture 9: Quantum Key Distribution and Hybrid Cryptographic Systems**

**Course:** CS408 — Post-Quantum Cryptographic Engineering  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

**Quantum Key Distribution (QKD)** offers information-theoretic security based on the laws of physics rather than computational hardness assumptions. Using quantum mechanical properties — particularly the **no-cloning theorem** (an unknown quantum state cannot be copied) and the **observer effect** (measuring a quantum state disturbs it) — QKD allows two parties to generate a shared secret key with security guaranteed by quantum physics. This lecture covers the **BB84 protocol** (the foundational QKD scheme), **entanglement-based QKD** (E91 and device-independent protocols), the practical challenges of QKD (distance limitations, detector side channels, trusted node problems), and the integration of QKD with post-quantum cryptography in **hybrid key management systems**. We examine the Yggdrasil Quantum Communication Testbed, which connects the university's main campus to the Nordic Research Network via a 150km fiber link with intermediate trusted nodes.

### Key Topics

- **BB84 Protocol:** Proposed by Bennett and Brassard (1984). Alice sends photons in one of four polarization states (0°, 45°, 90°, 135°), encoding bits in two non-orthogonal bases. Bob measures in randomly chosen bases; afterward, Alice and Bob compare bases over a public channel and discard mismatched measurements. Eavesdropping by Eve introduces errors (due to the no-cloning theorem and basis mismatch); Alice and Bob estimate the error rate and abort if it exceeds a threshold. The remaining bits, after privacy amplification, form a shared secret key.
- **Entanglement-Based QKD (E91):** Proposed by Ekert (1991). A source distributes entangled photon pairs to Alice and Bob. They measure their photons in randomly chosen bases and publicly compare a subset of results to violate Bell's inequality, certifying that the correlations are quantum (not classical) and that no eavesdropper has correlated classical information. Device-independent QKD extends this: even if the devices are untrusted, Bell violation guarantees security.
- **Practical QKD Challenges:** Distance: fiber attenuation limits QKD to ~100-200km without quantum repeaters (which do not yet exist in 2040; the Yggdrasil testbed uses trusted nodes). Rate: generating key material is slow (megabits per second at short distances, kilobits per second at long distances). Side channels: detector blinding attacks (forcing detectors to always click), Trojan horse attacks (injecting light into Alice's/Bob's devices), and timing attacks. Cost: QKD hardware is orders of magnitude more expensive than conventional cryptography.
- **Trusted Node Problem:** In a multi-hop QKD network, intermediate nodes must hold key material to perform key relay. These nodes are "trusted" in the sense that compromise reveals all keys passing through them. The Yggdrasil testbed mitigates this with hardware security modules (HSMs) at each node, tamper-evident enclosures, and continuous attestation. But the fundamental limitation remains: QKD provides end-to-end security only for direct fiber links; over longer distances, trusted nodes introduce vulnerability.
- **Hybrid QKD + Post-Quantum Systems:** The pragmatic approach: use QKD for high-value, short-distance key establishment (government communications, financial trading networks, critical infrastructure control), and use ML-KEM for everything else. In hybrid mode, the session key is derived from both a QKD key and an ML-KEM key, providing security if either mechanism is secure. The Yggdrasil National Research Network uses this hybrid model for its backbone infrastructure.

### Lecture Notes

Quantum Key Distribution is often misunderstood as "unbreakable encryption." It is not. QKD provides a secure key establishment mechanism, but the actual encryption is done with classical symmetric cryptography (AES), which is already post-quantum secure (Grover's algorithm provides only a quadratic speedup, doubling the required key length). The value of QKD is not replacing post-quantum algorithms but **augmenting** them with a different security foundation: physics rather than mathematics.

The **BB84 protocol** is elegant in its simplicity. The security does not rely on computational assumptions; it relies on the physical impossibility of cloning an unknown quantum state. If Eve intercepts and measures a photon, she must choose a basis. If she chooses the wrong basis, her measurement disturbs the state, introducing errors that Alice and Bob detect. If Eve tries to copy the photon and measure the copy, the no-cloning theorem prevents this. The security is information-theoretic: even a computationally unbounded adversary cannot break BB84 without introducing detectable errors.

But **practical QKD** is messy. The photon detectors have efficiency limits, dark counts (false clicks), and timing jitter. The quantum channel (fiber) has loss, depolarization, and dispersion. Real implementations have side channels: the **detector blinding attack** (discovered by Makarov et al., 2010) showed that shining a bright laser at Bob's detectors could force them to always click, allowing Eve to control the measurement outcome without introducing errors. Subsequent attacks exploited timing calibration, detector dead times, and device imperfections. "Device-independent" QKD promises security even with imperfect devices, but requires Bell violation — which is experimentally challenging and limits key rates.

The **trusted node problem** is the Achilles heel of QKD networks. A 1,000km link requires ~10 intermediate nodes to relay the key. Each node must decrypt and re-encrypt the key material, making it a point of compromise. The Yggdrasil testbed addresses this with HSMs and tamper detection, but the security guarantee is weaker than end-to-end QKD. Research into **quantum repeaters** — devices that entangle photons across long distances without decrypting them — is active but not yet practical. By 2040, quantum repeaters have been demonstrated in laboratory settings but not deployed in production networks.

**Hybrid systems** are the pragmatic path. The Yggdrasil National Research Network's backbone uses QKD for its highest-security links (government-research coordination, classified project management) and ML-KEM for general traffic. The hybrid key derivation combines both sources of entropy, providing defense in depth: an attacker must break both quantum physics and lattice assumptions to recover the key. This is the security philosophy of the post-quantum era: **no single point of cryptographic failure**.

### Required Reading

- Bennett, C.H. & Brassard, G. (1984/2035). "Quantum Cryptography: Public Key Distribution and Coin Tossing." *IEEE ICC*. (The original BB84 paper; read with the 2035 retrospective on implementation attacks.)
- Scarani, V. et al. (2037). "The Security of Practical Quantum Key Distribution." *Reviews of Modern Physics*. (A comprehensive survey of QKD security proofs and attacks.)
- Nordic Quantum Communication Consortium. (2040). "Trusted Node Architectures for Long-Distance QKD: The NQCC Standard." *NQCC Technical Report* 2040-03.

### Discussion Questions

1. QKD provides information-theoretic security, but practical implementations have been broken by side-channel attacks. Is QKD's theoretical security meaningful if the implementations are vulnerable? How does this compare to the security of well-implemented post-quantum cryptography?
2. The trusted node problem means that long-distance QKD networks are only as secure as their intermediate nodes. If quantum repeaters become practical, how would they change the security architecture? What new vulnerabilities might they introduce?
3. Your organization must choose between pure ML-KEM, pure QKD, and hybrid ML-KEM+QKD for securing its internal network. The network spans 500km, carries both routine and highly sensitive traffic, and has a limited budget. What is your recommendation, and how do you justify the cost?

---

ᚾ **Lecture 10: Cryptographic Agility and Migration Engineering — The Long Transition**

**Course:** CS408 — Post-Quantum Cryptographic Engineering  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

Cryptographic migration is not a flag day — it is a decade-long process of upgrading billions of devices, protocols, and institutions. This lecture covers the engineering discipline of **cryptographic agility**: designing systems that can switch algorithms without architectural overhaul. We examine the RSA-to-ECC migration (1990s-2010s) as a case study, the ongoing post-quantum migration (2020s-2040s), and the lessons for future transitions. Topics include: algorithm negotiation protocols (TLS cipher suites, SSH key exchange), certificate chain agility (root certificates with multiple signature algorithms), key escrow and recovery during transitions, backward compatibility risks (downgrade attacks), and the organizational challenges of coordinating migration across heterogeneous ecosystems. The Yggdrasil Cryptographic Migration Office provides a case study in large-scale transition management.

### Key Topics

- **Algorithm Agility in Protocol Design:** TLS cipher suites, SSH key exchange methods, and JWT algorithms are negotiated at connection time. This allows clients and servers to support multiple algorithms and select the strongest mutually supported option. But agility introduces risks: downgrade attacks (forcing peers to use weak algorithms) and configuration complexity (administrators must maintain long lists of supported algorithms and disable weak ones as they become obsolete).
- **Certificate Chain Agility:** A certificate binds an identity to a public key, signed by an issuer's key. During migration, a certificate may need multiple signatures (RSA and ML-DSA) to be accepted by both old and new verifiers. **Dual-signature certificates** and **transitional CAs** that issue both classical and post-quantum certificates are interim solutions with their own complexity. The Yggdrasil CA issues hybrid certificates: classical ECDSA + post-quantum ML-DSA, chained to a hybrid root.
- **The Downgrade Attack Problem:** During migration, systems support both old and new algorithms for compatibility. An attacker who can intercept and modify traffic can force peers to downgrade to the weakest supported algorithm. Defenses: **strict version enforcement** (rejecting connections that negotiate below a minimum version), **signed protocol parameters** (preventing tampering with the algorithm list), and **key separation** (using different keys for different algorithm versions so that compromise of one does not compromise the other).
- **Key Escrow and Recovery:** In classical cryptography, losing a private key means losing access to encrypted data. During migration, organizations must plan for key recovery: extracting classical keys before they are deprecated, transitioning encrypted archives to post-quantum encryption, and maintaining decryption capability for legacy data. The Yggdrasil Data Archival Standard requires all encrypted archives to include algorithm identifiers and sufficient metadata for future decryption, even if the original system is obsolete.
- **Organizational Migration:** Technical migration is the easy part. The hard part is coordinating across departments with different priorities, legacy systems that cannot be updated, vendors who have not released post-quantum products, and users who resist change. The Yggdrasil Cryptographic Migration Office uses a phased approach: inventory (what algorithms are in use?), assessment (what is the risk and priority?), pilot (test migration on non-critical systems), rollout (systematic upgrade with rollback plans), and verification (continuous monitoring for legacy algorithm usage).

### Lecture Notes

Cryptographic migration is one of the most underestimated challenges in cybersecurity. The RSA-to-ECC migration took twenty years and is still incomplete in some sectors. The post-quantum migration is larger: more algorithms to replace, more systems to upgrade, and more uncertainty about the new algorithms' long-term security. The engineer who designs for agility today saves their organization from crisis tomorrow.

**Algorithm agility** is the capacity to add, remove, or replace cryptographic algorithms without changing the system architecture. The TLS cipher suite negotiation is the canonical example: when a client connects, it sends a list of supported cipher suites; the server selects one; they proceed. This allowed the ecosystem to transition from DES to 3DES to AES, and from RSA to ECDHE, without changing the protocol format. But agility is not free: every supported algorithm is a potential vulnerability. A server that supports DES for backward compatibility is attackable via downgrade. The correct policy: support the current standard, the previous standard (for过渡期), and nothing older. The previous standard should have a sunset date.

**Dual-signature certificates** are the transitional bridge. During migration, a certificate authority may sign a certificate with both ECDSA and ML-DSA, producing a hybrid certificate that verifiers can validate with either algorithm. This allows incremental deployment: new verifiers check the ML-DSA signature; old verifiers check the ECDSA signature. The cost: larger certificates (~3,400 bytes for dual-signature vs. ~1,200 bytes for ECDSA alone). For TLS, where certificates are transmitted in every handshake, this increases latency on slow connections. The Yggdrisl CA mitigates this by caching and certificate compression (RFC 8879).

**The downgrade attack** is the shadow of agility. Every algorithm negotiation is an opportunity for an attacker to force weak parameters. The TLS 1.3 design (2018) learned from TLS 1.2's downgrade vulnerabilities: version negotiation is removed (the client guesses the version and includes it in the key exchange, so tampering is detectable), and the Finished message includes a transcript hash that binds the entire handshake. These mechanisms make downgrade attacks in TLS 1.3 computationally infeasible. Post-quantum migration protocols must incorporate similar protections.

**Key recovery during migration** is an often-overlooked problem. An organization with petabytes of encrypted backups must be able to decrypt them after the transition. If the backups were encrypted with RSA, and the RSA private key is destroyed after migration, the backups become unreadable. The migration plan must include: key archival (secure storage of old private keys for the retention period), re-encryption (decrypting old archives with old keys and re-encrypting with new keys), and metadata preservation (recording which algorithm was used for each archive). The Yggdrasil Data Archival Standard mandates algorithm-agnostic headers: every encrypted file begins with a header that identifies the algorithm, key derivation parameters, and key identifier, allowing future decryption even if the algorithm is obsolete.

### Required Reading

- Gillmor, D.K. (2036). "Negotiated Crypto: Algorithm Agility and Downgrade Protection." *IEEE S&P*. (A comprehensive analysis of agility mechanisms and their vulnerabilities.)
- Yggdrasil Cryptographic Migration Office. (2040). *The Post-Quantum Transition: A Field Guide for System Administrators*. Yggdrasil University Press. Chapters 1-4, 7.
- Barker, E. & Rogaway, P. (2035). "Recommendation for Key Management." *NIST SP 800-57*, Part 1, Rev. 6. (The definitive reference for key lifecycle management.)

### Discussion Questions

1. Your organization supports TLS 1.2 with RSA, TLS 1.3 with ECDHE, and TLS 1.4 with hybrid post-quantum. A security scan reveals that 5% of connections still negotiate TLS 1.2 with RSA. Do you disable TLS 1.2, knowing that some legacy clients will break? What is your decision framework?
2. Dual-signature certificates increase size by ~2,800 bytes. For a web service serving 10 billion requests per day, what is the total bandwidth cost? Is there a more efficient transitional mechanism?
3. An organization encrypted all backups with AES-256-GCM using RSA-2048 key wrapping in 2025. By 2040, RSA-2048 is deprecated. The backups must be retained until 2055. What is your migration plan? What are the risks of keeping RSA-2048 keys in escrow for 30 years?

---

ᛁ **Lecture 11: Privacy-Preserving Technologies — Beyond Encryption**

**Course:** CS408 — Post-Quantum Cryptographic Engineering  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

Encryption protects data in transit and at rest, but modern systems increasingly require **privacy-preserving computation** — processing data without revealing it. This lecture covers three advanced technologies: **homomorphic encryption** (computing on encrypted data), **differential privacy** (querying databases while bounding the leakage of individual records), and **functional encryption** (decrypting only a specific function of the plaintext, not the plaintext itself). We examine the 2040 state of the art: the **CKKS scheme** (homomorphic encryption for approximate arithmetic, used in machine learning), the **Google DP Library** (differential privacy in production systems), and the emerging **attribute-based encryption** standards. The lecture includes a hands-on exercise: training a logistic regression model on encrypted medical data using the SEAL homomorphic encryption library.

### Key Topics

- **Homomorphic Encryption (HE):** A scheme that allows computation on ciphertexts, producing an encrypted result that decrypts to the correct function of the plaintexts. **Partially homomorphic** schemes support one operation (addition OR multiplication). **Somewhat homomorphic** schemes support both but with limited depth. **Fully homomorphic** schemes support arbitrary computation. The breakthrough: Gentry's 2009 construction using bootstrapping (refreshing a ciphertext to reduce noise). By 2040, the **CKKS** (Cheon-Kim-Kim-Song) scheme is the standard for approximate arithmetic, supporting encrypted neural network inference with millisecond latency on optimized hardware.
- **Differential Privacy (DP):** A mathematical framework for bounding the leakage of individual records in database queries. A mechanism is ε-differentially private if the probability of any output changes by at most a factor of e^ε when any single record is added or removed. The **Laplace mechanism** adds Laplace-distributed noise scaled to the query's sensitivity; the **Gaussian mechanism** uses Gaussian noise for (ε, δ)-DP. Composition theorems bound the total privacy loss of multiple queries. Applications: census data release (the U.S. Census Bureau adopted DP in 2020; by 2040, all Nordic statistical agencies use it), machine learning (DP-SGD, differentially private stochastic gradient descent), and location analytics.
- **Functional and Attribute-Based Encryption:** In **functional encryption**, a secret key is associated with a function f; decrypting a ciphertext with this key yields f(m), not m. In **attribute-based encryption (ABE)**, ciphertexts and keys are labeled with attributes; decryption succeeds only if the key's attribute set satisfies the ciphertext's access policy. These primitives enable fine-grained access control: a hospital can encrypt patient data with an access policy "cardiologist OR emergency physician," and only doctors with those attributes can decrypt. By 2040, ABE is standardized in ISO/IEC 29100-5 and deployed in the Nordic Electronic Health Record system.
- **The Yggdrasil Privacy Computing Platform:** A university-industry collaboration that combines MPC, HE, and DP to enable privacy-preserving analytics across organizational boundaries. The platform's flagship application: the **Nordic Climate Data Consortium**, where twelve countries jointly compute carbon emission models without revealing their raw industrial data. The platform uses MPC for the coordination layer, HE for the computation layer (encrypted linear regression), and DP for the output layer (noised aggregate results).

### Lecture Notes

Privacy-preserving technologies represent a paradigm shift: from "encrypt data and process it decrypted" to "process data while it remains encrypted or statistically protected." This shift is driven by regulation (the European Data Protection Regulation 2035 and the Nordic Data Sovereignty Treaty 2038 mandate privacy-by-design), by business need (companies want to collaborate on data without sharing competitive secrets), and by ethics (the recognition that raw data about individuals is inherently sensitive, even when "anonymized").

**Homomorphic encryption** was theoretical for decades. Gentry's 2009 construction proved that fully homomorphic encryption was possible, but the initial implementation required 30 minutes to multiply two encrypted bits — utterly impractical. A decade of optimization (batching, single-instruction-multiple-data (SIMD) operations on ciphertexts, residue number systems, and hardware acceleration) brought HE to practicality for specific workloads. By 2040, encrypted neural network inference on the MNIST dataset takes ~50ms using optimized CKKS and hardware acceleration. This is not general-purpose computing — you cannot run an operating system on HE — but it is sufficient for machine learning, statistical analysis, and certain database queries.

**Differential privacy** is the mathematical formalization of "hiding in a crowd." The guarantee is subtle and powerful: no matter what auxiliary information an adversary has, they cannot determine whether any specific individual is in the dataset. The parameter ε controls the privacy-utility trade-off: ε = 0 means perfect privacy (no information released) but no utility; ε = ∞ means perfect utility (raw data released) but no privacy. In practice, ε is chosen between 0.1 and 10, depending on the sensitivity of the data and the number of queries. The composition problem: if you release 100 ε-DP queries, the total privacy loss is not 100ε but something smaller (due to advanced composition theorems). The Yggdrasil DP toolkit automates privacy budget tracking, refusing queries that would exceed the configured total ε.

**Attribute-based encryption** is the cryptographic realization of role-based access control. Traditional encryption encrypts to a recipient (who has the decryption key). ABE encrypts to a policy ("cardiologist during business hours"); anyone with attributes satisfying the policy can decrypt. The policy is encoded in the ciphertext as a boolean formula over attributes; the key is associated with a set of attributes. The cryptography ensures that collusion does not help: two users with attributes "cardiologist" and "business hours" cannot combine their keys to decrypt a ciphertext requiring "cardiologist AND business hours" unless one of them already has both attributes. This non-collusion property is what makes ABE secure.

### Required Reading

- Gentry, C. (2009/2035). "A Fully Homomorphic Encryption Scheme." *Stanford PhD Thesis*. (The foundational construction; read the bootstrapping chapter.)
- Dwork, C. & Roth, A. (2037). *The Algorithmic Foundations of Differential Privacy*, 2nd Edition. Now Publishers. (The definitive reference; Chapters 1-3 for the core concepts.)
- Waters, B. (2036). "Attribute-Based Encryption: A Survey and New Directions." *JACM*. (Covers CP-ABE, KP-ABE, and multi-authority extensions.)

### Discussion Questions

1. Homomorphic encryption adds ~1,000× overhead compared to plaintext computation. For what applications is this cost acceptable? What optimizations (hardware acceleration, approximate arithmetic, batching) make HE practical in 2040?
2. Differential privacy guarantees that no individual can be identified, but it does not guarantee that small groups cannot be identified. A query about "residents of apartment building 47" might satisfy ε-DP for individuals but reveal information about the building's demographics. How do you address this "group privacy" problem?
3. Attribute-based encryption requires a trusted authority to issue keys. What happens if the authority is compromised? What distributed ABE constructions exist, and what are their trade-offs?

---

ᛃ **Lecture 12: The Capstone Project — Designing a Post-Quantum Secure Messaging System**

**Course:** CS408 — Post-Quantum Cryptographic Engineering  
**Degree:** Bachelor of Science in Computer Science, University of Yggdrasil, 2040

---

### Overview

The capstone project for CS408 is the design and implementation of a **post-quantum secure messaging system** — an end-to-end encrypted messaging application that uses ML-KEM for key establishment, ML-DSA for authentication, and AES-256-GCM for message encryption, with forward secrecy (compromise of long-term keys does not reveal past messages) and post-compromise security (recovery after temporary compromise). This lecture frames the project: the threat model, the protocol design (a simplified variant of the Signal protocol adapted for post-quantum primitives), the implementation requirements (constant-time code, formal verification of critical components, comprehensive test coverage), and the evaluation criteria (security analysis, performance benchmarks, usability assessment). The project is completed in teams of 2-3 students over the final six weeks of the semester.

### Key Topics

- **Threat Model:** The adversary controls the network (can intercept, modify, and drop messages), knows the protocol specification, and has access to a large-scale quantum computer. The adversary does not control the endpoints (cannot read memory or extract keys from devices). The system must provide: confidentiality (messages are readable only by the intended recipient), integrity (messages cannot be modified undetectably), authentication (the recipient knows who sent the message), forward secrecy (past messages remain secret even if long-term keys are compromised), and post-compromise security (the system recovers security after a temporary compromise through continuous key ratcheting).
- **Protocol Design:** A simplified Signal-inspired protocol. Each user has a long-term ML-DSA signing key pair. The initial handshake uses X25519 + ML-KEM hybrid key exchange, producing an initial root key. The **Double Ratchet** algorithm provides forward secrecy and post-compromise security: each message includes a new ephemeral public key (Diffie-Hellman ratchet), and message keys are derived from a chaining key that updates with each message (symmetric ratchet). The adaptation for post-quantum: replace Curve25519 ephemeral keys with ML-KEM encapsulations, and replace Ed25519 signatures with ML-DSA signatures.
- **Implementation Requirements:** The protocol must be implemented in a memory-safe language (Rust is recommended; the Yggdrasil reference implementation uses Rust with `unsafe` prohibited except for verified foreign function interfaces). Critical components (the KEM encapsulation/decapsulation, the signature generation/verification, the key derivation) must be formally verified or use formally verified libraries (HACL*). All secret operations must be constant time. The implementation must include comprehensive property-based tests (testing protocol invariants: "after any sequence of messages, both parties have the same chaining key") and fuzz tests (random protocol runs with injected faults).
- **Security Analysis:** Each team submits a security analysis document that models the protocol using the **Tamarin** protocol verifier or the **ProVerif** tool, proving properties like "the adversary cannot learn the message content" and "if Alice believes she is talking to Bob, then Bob believes he is talking to Alice" (agreement). The analysis identifies any deviations from the ideal protocol and justifies them.
- **Performance and Usability:** The system must achieve end-to-end latency below 100ms for message delivery on the university network. Key generation must complete in under 1 second. The UI must be minimal but functional: contact list, message history, and send/receive with read receipts. The usability evaluation includes a heuristic evaluation by classmates and a cognitive walkthrough with a non-technical user.

### Lecture Notes

The messaging system capstone is the synthesis of everything you have learned in CS408: you must understand the quantum threat to design the threat model; you must understand lattice cryptography to select and parameterize ML-KEM and ML-DSA; you must understand side channels to implement them securely; you must understand formal verification to prove critical properties; and you must understand protocol design to build a system that is not merely a collection of algorithms but a coherent, secure whole.

**The Double Ratchet** is one of the most beautiful cryptographic protocols of the modern era. It combines two ratcheting mechanisms: the **DH ratchet** (each message includes a new ephemeral public key; when a party replies, they perform a Diffie-Hellman operation with the received ephemeral key, producing a new shared secret that the adversary cannot predict even with knowledge of past secrets) and the **symmetric ratchet** (message keys are derived from a chaining key using a one-way function; each message advances the chaining key, so compromise of a message key does not reveal future message keys). The combination provides both forward secrecy (past messages are protected by destroyed ephemeral keys) and post-compromise security (continuous DH operations recover security after a temporary key compromise).

Adapting the Double Ratchet for post-quantum primitives requires care. The classical DH ratchet relies on the commutativity of Diffie-Hellman: both parties can compute the same shared secret from each other's public keys. ML-KEM is not commutative: Bob cannot "complete" an encapsulation that Alice initiated in the same way that Bob can complete a DH handshake. The adaptation: each ratchet step involves a full KEM encapsulation (Alice generates a new ML-KEM key pair, sends the public key, Bob encapsulates to it and sends the ciphertext) rather than a simple DH exchange. This increases message size by ~1,200 bytes per ratchet step but preserves the security properties.

**The formal verification requirement** is ambitious but achievable. Tools like Tamarin and ProVerif allow you to specify the protocol as a set of rewriting rules and prove security properties automatically (for finite bounds) or with user guidance (for unbounded proofs). The Yggdrasil reference implementation includes a Tamarin model that proves: (1) message secrecy (only the intended recipient can decrypt), (2) authentication (the recipient knows who sent the message), (3) forward secrecy (past messages remain secret after long-term key compromise), and (4) post-compromise security (the system recovers after temporary compromise). Students are not expected to prove all four properties from scratch but must verify at least secrecy and authentication.

The capstone evaluation criteria emphasize **security over features**. A system with beautiful UI but a flawed ratchet receives a failing grade; a system with minimal UI but a verified secure protocol receives a high grade. This reflects the values of the course and the field: in cryptography, a single implementation error can destroy all security, and elegance is meaningless without correctness.

### Required Reading

- Cohn-Gordon, K. et al. (2036). "A Formal Security Analysis of the Signal Messaging Protocol." *JACM*. (The definitive analysis of Signal's security properties.)
- Marlinspike, M. & Perrin, T. (2035). "The Double Ratchet Algorithm." *Signal Specification*. (The original specification; read with the post-quantum adaptation notes.)
- Yggdrasil Secure Systems Lab. (2040). "Post-Quantum Messaging: A Reference Design and Tamarin Model." *UoY Technical Report* TR-2040-19.

### Discussion Questions

1. The Double Ratchet's post-quantum adaptation replaces DH with full KEM operations, increasing message size. Can you design a more efficient post-quantum ratchet that preserves forward secrecy and post-compromise security? What are the trade-offs?
2. Your team has implemented the protocol but has not formally verified it. A classmate discovers that your ratchet does not update the chaining key under a specific edge case (message received out of order). Is this a vulnerability? What is the attack, and how do you fix it?
3. The capstone prioritizes security over usability. In the real world, users abandon secure systems that are hard to use (the "usability-security trade-off"). How would you adapt your design for mass deployment while maintaining the security properties? What compromises are acceptable?

---

## Final Examination Preparation

The CS408 final examination is a **take-home applied cryptography assessment** distributed one week before the deadline. Students receive:

1. A partially implemented post-quantum messaging library in Rust with several intentional bugs (timing side channels, incorrect FO transform, weak randomness).
2. A protocol specification with ambiguous sections that must be resolved.
3. A set of test vectors that the implementation must satisfy.

The task: audit the code, identify and fix all vulnerabilities, resolve the specification ambiguities with justified decisions, and extend the test suite. The examination is open-book, open-internet, and collaborative (teams of 2 students). The deliverable is a corrected implementation, a security audit report, and a 10-page design justification.

### Sample Examination Tasks

| Task | Description | Points |
|------|-------------|--------|
| Vulnerability Audit | Identify all security bugs in the provided code | 30 |
| Bug Fixes | Implement correct, constant-time fixes | 25 |
| Specification Resolution | Resolve ambiguities in the protocol spec | 20 |
| Test Suite Extension | Add tests that would catch the bugs | 15 |
| Design Justification | Write the 10-page report | 10 |

### Sample Essay Questions (Choose 3 of 6)

1. Compare the security foundations of ML-KEM (Module-LWE), SLH-DSA (hash functions), and ECDH (elliptic curve discrete log). Which foundation do you trust most for a 50-year security horizon, and why?
2. Describe a concrete attack on a messaging system that has forward secrecy but lacks post-compromise security. How does the Double Ratchet provide post-compromise security, and what is the cost?
3. The post-quantum transition has been called "the largest cryptographic migration in history." What made it so difficult? What could have been done differently in the 2020s to ease the transition?
4. Zero-knowledge proofs and secure multi-party computation both allow computation without revealing inputs. When would you choose ZK proofs over MPC, and vice versa? Give specific application scenarios.
5. A nation-state mandates that all government communications use QKD for key establishment. Critique this policy: what are the benefits, risks, and hidden costs?
6. You are the Chief Cryptographer for a cryptocurrency exchange in 2040. Your exchange holds $50 billion in assets. Design your key management architecture: what algorithms do you use, how do you distribute keys, how do you handle migration, and what is your disaster recovery plan?

---

*"The best cryptographer is not the one who builds unbreakable walls, but the one who knows where the walls are weakest and strengthens them before the storm arrives." — Dr. Hákon Erlendsson, Inaugural Lecture, 2032*
