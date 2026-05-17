# IT107: Web Technologies & Internet Architecture
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4
**Description:** A comprehensive survey of the architecture, protocols, and infrastructure that constitute the modern World Wide Web, with emphasis on the 2040 landscape of edge-distributed, AI-mediated, and quantum-resilient web systems.

**Prerequisites:** IT101 (Introduction to Information Technology), CN101 (Introduction to Computer Networking)

**Instructor:** Dr. Eiríkr Bjarnarson, Department of Information Technology

**Course Philosophy:** The web is not merely a collection of hyperlinked documents — it is the digital agora where commerce, culture, governance, and human connection converge. Understanding its architecture is to understand the spine of modern civilization. This course treats the web as a living, evolving organism, one whose protocols encode political assumptions, whose infrastructure reflects economic power, and whose future demands both technical mastery and ethical wisdom.

---

## Lectures

---

### Lecture 1: The Architecture of the Web — Origins, Principles, and the 2040 Stack

**Course:** IT107 — Web Technologies & Internet Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

The World Wide Web was born at CERN in 1989, when Tim Berners-Lee proposed a system of linked hypertext documents accessible over the Internet. In the 51 years since, the web has transformed from a research tool into the substrate of global civilization — the platform for commerce, education, governance, social connection, and cultural production. This lecture surveys the web's architectural evolution, establishes the layered model that governs web communication, and introduces the 2040 web stack: a landscape shaped by edge computing, AI mediation, quantum-resistant cryptography, and decentralized identity protocols.

#### Key Topics

- **The Web vs. The Internet:** A foundational distinction: the Internet is the global network of interconnected computers communicating via TCP/IP; the World Wide Web is an application-layer system of hyperlinked resources accessed via HTTP and identified by URIs. By 2040, the distinction has blurred, as the web's protocols (HTTP/3, WebSocket, WebRTC) have absorbed functions previously handled at lower layers.
- **Architectural Principles of the Web:** Berners-Lee's original design principles remain influential: (1) universality — any resource can be linked; (2) decentralization — no central authority controls the web; (3) layering — protocols are modular and composable; (4) tolerance — "be conservative in what you send, liberal in what you accept" (Postel's Law, now controversially reconsidered in the era of zero-trust security). These principles have been challenged, modified, and reinterpreted across five decades of web evolution.
- **The 2040 Web Stack:** The contemporary web stack comprises: (1) Transport Layer — HTTP/3 over QUIC, with multipath extensions for seamless handoff between cellular, satellite, and fixed networks; (2) Security Layer — TLS 1.4 with post-quantum hybrid key exchange (X25519 + CRYSTALS-Kyber) mandated by the Global Data Stewardship Accord of 2038; (3) Application Layer — a landscape dominated by WebAssembly modules, React/Vue/Svelte descendants, and AI-generated UI frameworks; (4) Identity Layer — Self-Sovereign Identity (SSI) via W3C Verifiable Credentials and Decentralized Identifiers (DIDs), gradually replacing password-based authentication.
- **The End of Client-Server:** By 2040, the classical client-server dichotomy has dissolved. Every device is both consumer and producer of web resources. Edge nodes cache, transform, and serve content. AI agents negotiate API interactions autonomously. The web is a mesh, not a star topology.

#### Lecture Notes

The web's evolution can be understood through the metaphor of urbanization. Early web (1990s) was a scattering of homesteads — personal homepages, static HTML. The Web 2.0 era (2000s–2010s) was the rise of cities — centralized platforms (Google, Facebook, Amazon) that aggregated users and data. The Web 3.0 era (2020s–2030s) was the decentralization movement — blockchain, IPFS, federated protocols — a push to reclaim digital sovereignty. The 2040 web is a mature ecosystem where centralized and decentralized architectures coexist in a negotiated tension, mediated by AI orchestration layers and governed by transnational digital accords.

A crucial development of the 2030s was the **Web Environment Integrity (WEI) debate**. When major browser vendors proposed attestation APIs that would allow servers to verify client integrity, privacy advocates warned of a future where independent browsers and accessibility tools would be locked out. The compromise — the **Trondheim Protocol (2034)** — established that attestation must be optional, transparency must be verifiable, and no single entity may control the attestation infrastructure. This debate exemplifies the web's ongoing negotiation between security, openness, and power.

By 2040, the web processes over 4 zettabytes of data annually, serves 8.5 billion users (including non-human agents and IoT devices with web interfaces), and mediates approximately 65% of global GDP. Understanding its architecture is a form of civic literacy.

#### Required Reading

- Berners-Lee, T. (1989). "Information Management: A Proposal." CERN. (Original web proposal — historical context)
- Berners-Lee, T., Hendler, J., & Lassila, O. (2001). "The Semantic Web." *Scientific American*, 284(5), 34–43.
- UoY Web Architecture Lab. (2039). *The Trondheim Compromise: Attestation, Privacy, and Web Integrity in the 2030s*.
- IETF QUIC Working Group. (2038). RFC 9000 (QUIC) and RFC 9114 (HTTP/3) — Current Editions.

#### Discussion Questions

1. Postel's Law ("be liberal in what you accept") has been criticized as a security vulnerability — accepting malformed input creates attack surface. Should web protocol design prioritize strictness over tolerance? What are the architectural consequences of each approach?
2. The Trondheim Protocol balances web integrity and user privacy. Does this compromise satisfy both needs, or does it merely postpone a more fundamental conflict between platform control and user freedom?
3. In 2040, 35% of web traffic originates from non-human agents (AI assistants, IoT devices, autonomous systems). How should web architecture evolve to serve non-human users without compromising human accessibility?

#### Practice Problems

- Trace the complete request/response cycle of loading a modern web application (2040) from DNS resolution through TLS handshake, HTTP/3 stream multiplexing, CDN edge serving, and client-side WebAssembly execution. Diagram every protocol interaction.
- Analyze the WEI debate (2023–2034). Write a 1,000-word policy brief arguing for or against mandatory attestation, citing specific technical and social consequences.
- Compare the web stacks of 2004, 2014, 2024, and 2044. Identify which layers stabilized and which experienced paradigm shifts. What does this pattern predict for 2054?

---

### Lecture 2: HTTP/3, QUIC, and the Multipath Transport Revolution

**Course:** IT107 — Web Technologies & Internet Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

HTTP — the Hypertext Transfer Protocol — has been the web's lingua franca since 1991. HTTP/1.1 (1997) served the web for nearly two decades before HTTP/2 (2015) introduced multiplexing and header compression. But the true revolution came with HTTP/3 (2022), which abandoned TCP entirely in favor of QUIC — a transport protocol built on UDP that eliminates head-of-line blocking, reduces connection establishment latency to zero round trips (0-RTT), and enables seamless connection migration across network interfaces. This lecture examines the QUIC transport layer, HTTP/3's semantic mapping onto QUIC streams, and the 2040 extensions — multipath QUIC (MP-QUIC) and AI-optimized congestion control — that define modern web transport.

#### Key Topics

- **Why QUIC?** TCP's limitations were increasingly problematic by the 2010s: (1) head-of-line blocking — a lost packet in one stream blocks all streams; (2) connection establishment latency — TCP+TLS required 2–3 round trips; (3) ossification — middleboxes had frozen TCP's evolution, making protocol upgrades nearly impossible. QUIC addresses all three: it runs over UDP (bypassing middlebox ossification), multiplexes streams independently (eliminating HOL blocking), and integrates TLS 1.3 natively (0-RTT resumption).
- **QUIC's Architecture:** QUIC provides: (1) Reliable, ordered delivery per stream — each stream is independently flow-controlled, so packet loss in one stream doesn't affect others; (2) Connection migration — QUIC connections are identified by a Connection ID, not by IP/port tuples, so a connection survives a mobile device switching from WiFi to cellular; (3) Built-in encryption — all QUIC packets are encrypted (except the initial handshake), making QUIC traffic opaque to middleboxes; (4) Flexible congestion control — QUIC's pluggable congestion control architecture allows per-application or per-network optimization.
- **HTTP/3 Semantics:** HTTP/3 maps HTTP semantics (requests, responses, headers, status codes) onto QUIC streams. Each request-response pair occupies a bidirectional QUIC stream. Server push is deprecated in HTTP/3 (removed due to poor real-world adoption), replaced by the `103 Early Hints` status code and resource hints. QPACK replaces HPACK for header compression, using separate uni-directional streams for encoder and decoder state to avoid HOL blocking in header compression.
- **MP-QUIC and the 2040 Transport Layer:** Multipath QUIC (standardized in RFC 9480, 2037) enables a single QUIC connection to use multiple network paths simultaneously — aggregating bandwidth and providing seamless failover. A user on a 2040 device might simultaneously use satellite Internet (Starlink v4), 6G cellular, and local mesh WiFi, with MP-QUIC dynamically routing traffic across paths based on latency, cost, and reliability. The **AI Congestion Controller (AICC)** — standardized in 2039 — uses on-device ML models to predict network conditions and tune congestion control parameters per-path, achieving 15–30% throughput improvements over classical algorithms (CUBIC, BBRv3) in heterogeneous network environments.

#### Lecture Notes

QUIC's deployment accelerated dramatically in the late 2020s. By 2030, over 80% of web traffic used QUIC. The protocol's encryption-by-default design had an unintended consequence: it made network-level content filtering (used by schools, enterprises, and authoritarian governments) significantly more difficult, as QUIC traffic is opaque to deep packet inspection. This sparked a decade-long policy debate that culminated in the **Stockholm Net Neutrality Accord (2035)**, which established that (1) network operators may apply traffic management at the IP level but not inspect application-layer content, (2) content filtering must be endpoint-based (client or server), and (3) QUIC's encryption is a privacy right, not a circumvention tool.

A fascinating development is **AI-Negotiated Transport (ANT)** — a 2040 proposal where AI agents on client and server negotiate transport parameters (congestion control algorithm, stream prioritization, retransmission policy) based on application requirements. A video conference AI might negotiate low-latency unreliable delivery for video frames while requesting reliable ordered delivery for chat messages — all within a single QUIC connection. ANT is experimental but represents the direction of travel toward application-aware transport.

#### Required Reading

- Langley, A., et al. (2017). "The QUIC Transport Protocol: Design and Internet-Scale Deployment." *ACM SIGCOMM*.
- IETF. (2037). RFC 9480: Multipath Extensions for QUIC (MP-QUIC).
- Cardwell, N., Cheng, Y., et al. (2036). "BBRv3: Model-Based Congestion Control for the AI Era." *ACM SIGCOMM Computer Communication Review*, 66(4).
- UoY Transport Lab. (2039). *AI-Negotiated Transport: A Research Agenda for 2040–2050*.

#### Discussion Questions

1. QUIC's encryption prevents middleboxes from inspecting traffic. Does this enhance user privacy at the expense of network management? Or is the loss of middlebox visibility a feature, not a bug — a nudge toward endpoint-based security?
2. MP-QUIC enables bandwidth aggregation across paid and free networks. Should operating systems expose per-path cost information to applications, allowing them to route expensive traffic differently? What are the privacy implications?
3. AI-Negotiated Transport could optimize individual application performance but might lead to transport-layer fragmentation — different applications using incompatible congestion control strategies. Is this a problem, or is application diversity a strength of the Internet architecture?

#### Practice Problems

- Set up a QUIC connection between two virtual machines and use Wireshark to capture the handshake. Identify the ClientHello, ServerHello, and the encrypted extensions. Measure the handshake latency compared to TCP+TLS 1.3.
- Implement a simple MP-QUIC scheduler that distributes traffic across two network interfaces (e.g., WiFi and cellular) using weighted round-robin. Test under varying loss conditions and compare throughput to single-path QUIC.
- Research the history of middlebox ossification. Write a 500-word analysis explaining how QUIC's design deliberately resists middlebox interference and whether this strategy has succeeded by 2040.

---

### Lecture 3: DNS — The Distributed Directory That Names the World

**Course:** IT107 — Web Technologies & Internet Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

The Domain Name System (DNS) is the Internet's phonebook — the distributed, hierarchical database that translates human-readable domain names (e.g., `yggdrasil.university`) into machine-routable IP addresses. Designed by Paul Mockapetris in 1983, DNS has grown from a simple name-to-address lookup service into a critical infrastructure component that handles load balancing, service discovery, email routing, and — by 2040 — cryptographic identity verification, content reputation scoring, and AI-driven traffic steering. This lecture traces DNS's evolution from RFC 882 to the 2040 landscape of DNS-over-QUIC (DoQ), Oblivious DNS (ODNS), and the Verifiable Domain Resolution (VDR) framework.

#### Key Topics

- **DNS Hierarchy and Resolution:** DNS is a tree-structured namespace. The root zone (managed by ICANN/IANA) delegates to Top-Level Domains (TLDs: `.com`, `.org`, `.university`, country-code TLDs like `.uk`), which delegate to authoritative name servers for individual domains. Resolution proceeds recursively: a client queries a recursive resolver (e.g., the ISP's resolver or a public resolver like Cloudflare's 1.1.1.1), which walks the tree from root to authoritative server, caching results at each level. By 2040, the root zone contains over 2,000 TLDs, and the average domain resolution requires 3.2 queries (optimized by aggressive caching and AI-predictive prefetching).
- **DNS Security (DNSSEC):** DNSSEC (RFC 4033–4035) adds cryptographic signatures to DNS records, enabling resolvers to verify that responses haven't been tampered with. DNSSEC uses a chain of trust: each zone's public key is signed by its parent zone, up to the root zone's Key Signing Key (KSK). Despite being standardized in 2005, DNSSEC adoption was slow — by 2025, only ~30% of domains signed their zones. By 2040, the **Mandatory DNSSEC Accord (2033)** requires all TLD operators and major registrars to support DNSSEC, pushing adoption above 85%. However, DNSSEC does not encrypt DNS queries — it only authenticates responses. Privacy requires separate mechanisms.
- **Encrypted DNS — DoH, DoT, DoQ:** Query privacy has been one of DNS's most contentious issues. Traditional DNS queries are sent in cleartext over UDP port 53, visible to any network observer. Three encrypted DNS protocols address this: (1) DNS-over-TLS (DoT, RFC 7858, 2016) — DNS queries tunneled over TLS on port 853; (2) DNS-over-HTTPS (DoH, RFC 8484, 2018) — DNS queries embedded in HTTP/2 or HTTP/3 requests, indistinguishable from other HTTPS traffic; (3) DNS-over-QUIC (DoQ, RFC 9250, 2022) — DNS over native QUIC, combining the performance benefits of QUIC with encrypted transport. By 2040, DoQ has emerged as the dominant encrypted DNS protocol, leveraging QUIC's 0-RTT handshake and connection migration. DoH remains popular in browser implementations due to its ability to blend with web traffic.
- **Oblivious DNS (ODNS) and Privacy-Preserving Resolution:** Even with encrypted DNS, the recursive resolver sees both the client's IP address and the queried domain — a privacy concern when resolvers are operated by ISPs or commercial entities. Oblivious DNS (RFC 9230, 2022) addresses this by separating the resolver into two parties: a **proxy** (which knows the client's IP but not the query) and a **target** (which knows the query but not the client's IP). By 2040, ODNS is standard in privacy-conscious browsers and mandated by the European Digital Sovereignty Directive (2037) for government and healthcare DNS traffic.

#### Lecture Notes

DNS has become a battleground for Internet governance. Because DNS controls which names resolve to which addresses, it is a powerful tool for content control. Governments have used DNS blocking to censor websites; copyright holders have sought DNS-based piracy enforcement; and corporations have used DNS to redirect competitors' traffic. The **ICANN 3.0 reforms (2031)** established that DNS policy must be developed through multistakeholder governance (including technical community, civil society, governments, and private sector) with a presumption against content-based blocking.

A 2040 development is **Verifiable Domain Resolution (VDR)** — a framework where domains publish cryptographic commitments to their DNS records on a transparency log (inspired by Certificate Transparency). Clients can verify that the DNS response they receive matches the domain owner's published intent, detecting both censorship and cache poisoning. VDR is implemented via the **Yggdrasil Transparency Log (YTL)** — a Merkle tree-based append-only log operated by a consortium of universities (including UoY) and nonprofit organizations.

Another emerging trend is **AI-Predictive DNS Prefetching**. By 2040, on-device AI models predict which domains a user is likely to visit next (based on browsing patterns, time of day, location, and application context) and prefetch DNS resolutions, reducing perceived latency. The privacy implications are significant — the prefetching model itself encodes a predictive model of user behavior, which is sensitive data.

#### Required Reading

- Mockapetris, P. (1987). RFC 1034/1035: Domain Names — Concepts and Facilities / Implementation and Specification.
- IETF. (2030). RFC 9499: DNS Terminology (Updated).
- Schmitt, P., Edmundson, A., & Feamster, N. (2024). "Oblivious DNS: Practical Privacy for DNS Queries." *Proceedings on Privacy Enhancing Technologies*.
- UoY DNS Research Group. (2039). *Verifiable Domain Resolution: A Transparency Log for DNS*.

#### Discussion Questions

1. DNS blocking is used by some governments to censor political speech and by some ISPs to enforce copyright. Is DNS an appropriate layer for content regulation, or should content decisions be made at endpoints? What principle distinguishes legitimate DNS policy from censorship?
2. Oblivious DNS protects query privacy but adds latency and infrastructure complexity. In a world where AI-predictive prefetching already leaks behavioral patterns, is ODNS still worth its costs? Or should privacy efforts shift to other layers?
3. The DNS root zone is managed by ICANN under a contract with the U.S. Department of Commerce (historically) and now under a multistakeholder model. Is DNS governance adequately global and democratic, or does it still concentrate power in Western institutions?

#### Practice Problems

- Use `dig +dnssec` to query a DNSSEC-signed domain and verify the RRSIG records. Trace the chain of trust from the root zone's DNSKEY to the domain's DNSKEY.
- Set up an Oblivious DNS proxy using a public ODNS relay and measure the latency overhead compared to direct DoQ resolution. Analyze the trade-off between privacy and performance.
- Research a historical DNS-based censorship incident (e.g., Turkey's DNS blocking of Twitter in 2014, or the U.S. SOPA/PIPA DNS provisions). Write a 500-word analysis of the technical and policy responses.

---

### Lecture 4: TLS, PKI, and the Post-Quantum Web Security Architecture

**Course:** IT107 — Web Technologies & Internet Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

Transport Layer Security (TLS) is the cryptographic protocol that secures the web. TLS provides three guarantees: (1) confidentiality — data is encrypted so only the intended recipient can read it; (2) integrity — data cannot be modified in transit without detection; (3) authentication — the server (and optionally the client) is who it claims to be. This lecture examines TLS's evolution from SSL 2.0 (1995) to TLS 1.4 (2038), the Public Key Infrastructure (PKI) that underpins TLS authentication, the Certificate Transparency ecosystem, and the massive migration to post-quantum cryptography (PQC) that defined the 2030s.

#### Key Topics

- **TLS Handshake and Cipher Suites:** A TLS connection begins with a handshake: the client and server negotiate protocol version, select cipher suites, authenticate (typically the server via X.509 certificate), and establish shared session keys. TLS 1.3 (2018) streamlined the handshake to 1-RTT (one round trip) for new connections and 0-RTT for resumed connections. TLS 1.4 (2038) further refines this with **hybrid post-quantum key exchange** — combining classical ECDH (X25519) with a post-quantum KEM (CRYSTALS-Kyber) so that the connection is secure against both classical and quantum adversaries.
- **Public Key Infrastructure (PKI):** TLS authentication relies on X.509 certificates issued by Certificate Authorities (CAs). The Web PKI is the set of CAs trusted by major browser root programs (Mozilla, Microsoft, Apple, Google). A CA vouches for a domain owner's identity by signing their certificate. The trust model is hierarchical: root CAs → intermediate CAs → end-entity certificates. This model has known weaknesses: (1) any CA can issue a certificate for any domain, so a compromised CA undermines the entire system; (2) certificate revocation (via CRLs or OCSP) is unreliable in practice.
- **Certificate Transparency (CT):** Mandated by browsers since the late 2010s, CT requires CAs to log all issued certificates to public, append-only, cryptographically verifiable logs. Domain owners can monitor these logs to detect misissued certificates. By 2040, CT has expanded into **Universal Certificate Transparency (UCT)** — all TLS certificates, not just web server certificates, are logged. UCT has virtually eliminated undetected certificate misissuance, though sophisticated attackers have shifted to other vectors (compromising the domain's DNS or web server directly).
- **Post-Quantum Cryptography Migration:** The 2030s were defined by the PQC migration — the largest cryptographic transition in Internet history. NIST's PQC standardization process (2016–2024) selected CRYSTALS-Kyber (KEM), CRYSTALS-Dilithium (signatures), and SPHINCS+ (stateless hash-based signatures) as standards. The migration was complex: every TLS implementation, every CA, every certificate management system, and every application that pinned certificates needed updating. The **2030 PQC Deadline** (set by the Global Cryptographic Standards Body) required all public-facing web services to support hybrid PQC by 2030 and to prefer PQC-only by 2035. By 2040, over 95% of web traffic uses hybrid or pure PQC.

#### Lecture Notes

The PQC migration was less dramatic than feared. Early predictions of widespread outages proved unfounded because the IETF and browser vendors coordinated a phased rollout: (1) **Phase 1 (2024–2028):** Browser and server implementations added hybrid PQC support, negotiated via TLS extensions; (2) **Phase 2 (2028–2032):** Major web properties enabled hybrid PQC by default, collecting telemetry on performance and compatibility; (3) **Phase 3 (2032–2036):** PQC-preferred became the default, with classical fallback for legacy clients; (4) **Phase 4 (2036–2040):** Pure PQC connections became common, though hybrid mode remains supported for backward compatibility.

The surprise of the PQC migration was **performance**. Kyber-1024 key exchange adds approximately 2KB to the TLS handshake (compared to 64 bytes for ECDH), and Dilithium signatures are significantly larger than ECDSA. Initial deployments saw 5–15% latency increases. However, protocol optimizations (caching Kyber public keys at CDN edges, using session resumption aggressively, and dedicated hardware acceleration for lattice-based cryptography on 2040-era CPUs) have reduced the overhead to under 3%.

A 2040 frontier is **Continuous Authentication** — moving beyond the one-time TLS handshake to per-request or per-stream authentication using short-lived tokens derived from the initial TLS session. This enables fine-grained access control (different API endpoints requiring different authentication levels) and rapid credential rotation (tokens expire in seconds rather than hours).

#### Required Reading

- Rescorla, E. (2018). RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3.
- NIST. (2024). FIPS 203, 204, 205: Module-Lattice-Based Key-Encapsulation Mechanism, Digital Signature, and Stateless Hash-Based Digital Signature Standard.
- Laurie, B., Langley, A., & Kasper, E. (2013). RFC 6962: Certificate Transparency.
- UoY Cryptography Lab. (2039). *Post-Quantum TLS: Performance, Pitfalls, and the Road to 2050*.

#### Discussion Questions

1. The Web PKI's trust model is often described as "broken but the best we have." Is Certificate Transparency sufficient to remedy PKI's weaknesses, or does the fundamental model — trusting any CA to vouch for any domain — need replacement?
2. The PQC migration was a centrally coordinated, multi-decade effort. Could a similar migration happen for a less visible protocol (e.g., SSH, VPNs)? What lessons from the TLS PQC transition apply to other infrastructure migrations?
3. Continuous authentication improves security but also generates fine-grained behavioral data about API usage. Does the security benefit justify the privacy cost? Where should the line be drawn?

#### Practice Problems

- Use OpenSSL to establish a TLS 1.3 connection, capture the handshake with Wireshark, and identify each message (ClientHello, ServerHello, EncryptedExtensions, Certificate, CertificateVerify, Finished). Annotate which messages are encrypted.
- Research Let's Encrypt (launched 2015) and its impact on HTTPS adoption. Calculate the fraction of the web that was encrypted over HTTP in 2015 vs. 2025 vs. 2040 (estimated). What drove the adoption curve?
- Implement a simple Certificate Transparency log monitor that watches for certificates issued for a given domain and alerts on unexpected issuers.

---

### Lecture 5: REST, GraphQL, and the 2040 API Landscape

**Course:** IT107 — Web Technologies & Internet Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

APIs (Application Programming Interfaces) are the connective tissue of the modern web. They allow applications to exchange data, invoke services, and compose functionality across organizational boundaries. This lecture surveys the three dominant API paradigms — REST (Representational State Transfer), GraphQL, and the emerging Agent-Native Protocol (ANP) — examining their architectural assumptions, trade-offs, and suitability for the 2040 landscape of AI-mediated, event-driven, and privacy-regulated web services.

#### Key Topics

- **REST — The Architectural Style:** Defined by Roy Fielding in his 2000 doctoral dissertation, REST is not a protocol but an architectural style characterized by: (1) Resource identification through URIs; (2) Uniform interface (HTTP methods: GET, POST, PUT, DELETE); (3) Statelessness — each request contains all information needed to process it; (4) Hypermedia as the Engine of Application State (HATEOAS) — clients navigate resources through links provided in responses. In practice, most "RESTful" APIs implement only Levels 1–2 of the Richardson Maturity Model (resource URIs + HTTP methods), ignoring HATEOAS. By 2040, REST remains the most widely deployed API style, valued for its simplicity, cacheability, and alignment with HTTP semantics.
- **GraphQL — The Query Language for APIs:** Developed by Facebook in 2012 and open-sourced in 2015, GraphQL inverts REST's model: instead of the server defining fixed endpoints, the client specifies exactly what data it needs in a query. Benefits: (1) No over-fetching or under-fetching — clients get precisely the fields they request; (2) Strong typing — the GraphQL schema serves as a contract between client and server; (3) Single endpoint — all queries go to one URL, simplifying infrastructure. Drawbacks: (1) Query complexity — a simple-looking query can trigger expensive server-side joins; (2) Caching difficulty — HTTP caching doesn't apply cleanly to POST-based GraphQL; (3) N+1 problem — naive resolvers generate cascading database queries. By 2040, GraphQL is dominant for interactive applications (dashboards, mobile apps) where dynamic data requirements justify its complexity, while REST dominates service-to-service communication where fixed schemas and HTTP caching are advantageous.
- **Agent-Native Protocol (ANP) — The 2040 Frontier:** ANP is an emerging API paradigm designed for autonomous AI agents rather than human-driven UIs. Key features: (1) **Capability Discovery** — agents discover what an API can do via machine-readable capability manifests (extending OpenAPI/GraphQL introspection); (2) **Intent-Based Requests** — agents express goals ("book a flight to Reykjavík next Tuesday") rather than procedural sequences; (3) **Negotiated Contracts** — agents and servers negotiate SLAs, pricing, and data-use policies before interaction; (4) **Verifiable Execution** — API responses include cryptographic proofs of correct execution (useful for high-stakes transactions). ANP is being standardized by the W3C Agent Web Working Group (est. 2037) and is expected to become the dominant API paradigm by 2050.
- **API Security and Governance in 2040:** API security has evolved beyond simple API keys. The 2040 standard is **scoped, short-lived tokens with proof of possession** — DPoP (Demonstration of Proof-of-Possession, RFC 9449) bound to TLS connections. API gateways enforce rate limiting, schema validation, and data minimization (stripping fields the client isn't authorized to see). The **API Transparency Directive (2036)** requires public APIs to publish data-use policies that are machine-readable and auditable.

#### Lecture Notes

The API economy is a trillion-dollar sector by 2040. Companies like Twilio, Stripe, and AWS pioneered the model of selling API access as a product; by 2040, API-first businesses are the default, not the exception. The **API Commons** — a registry of open API specifications maintained by the OpenAPI Initiative — contains over 50,000 machine-readable API descriptions, enabling automated client generation, testing, and integration.

A defining debate of the 2030s was **API copyright**. When Oracle sued Google over Java API copyright (2010–2021), the case raised fundamental questions: Are API signatures copyrightable? The U.S. Supreme Court ruled in Google's favor (2021), establishing that API declarations are functional and thus not copyrightable — a ruling that protected the API economy. By 2040, the **API Openness Accord** extends this principle globally, establishing that API interfaces are functional elements not subject to copyright, though API implementations (code) remain protected.

Another 2040 development is **AI-Generated APIs**. With the maturation of code generation AI, it's increasingly common for API endpoints to be generated on-the-fly from natural language descriptions. A developer describes the desired API in prose, and the AI generates spec, implementation, tests, and documentation. The challenge is quality assurance: without careful review, AI-generated APIs can contain subtle security vulnerabilities, inconsistent semantics, or unintended data leakage.

#### Required Reading

- Fielding, R. T. (2000). *Architectural Styles and the Design of Network-Based Software Architectures*. Doctoral dissertation, UC Irvine. (Chapter 5: Representational State Transfer)
- Facebook Engineering. (2015). "GraphQL: A Data Query Language."
- W3C Agent Web Working Group. (2038). *Agent-Native Protocol Specification, Draft 4*.
- UoY API Lab. (2040). *The API Economy at Scale: Governance, Security, and AI Generation*.

#### Discussion Questions

1. GraphQL's flexibility enables over-fetching on the *server side* (resolving complex queries requires substantial backend work). Is the developer experience improvement worth the operational complexity? Under what circumstances would you recommend REST over GraphQL?
2. Agent-Native Protocol shifts APIs from procedural interfaces to intent-based negotiation. Does intent-based interaction give agents too much autonomy? What guardrails prevent an agent from making harmful decisions through a well-intentioned API call?
3. If AI systems can generate APIs from natural language descriptions, does the concept of an "API specification" become obsolete? Or does automated generation make specifications *more* important as contracts for verification?

#### Practice Problems

- Design a RESTful API for a university course registration system. Define resources, URIs, HTTP methods, request/response formats, and error codes. Compare your design to a GraphQL schema for the same domain.
- Write a GraphQL query that retrieves a student's enrolled courses, including instructor names and meeting times, while avoiding the N+1 problem. Explain how DataLoader or a similar batching mechanism resolves this.
- Draft an ANP capability manifest for a travel booking service. Include actions (search, book, cancel), parameters with constraints, and the data-use policy for each action.

---

### Lecture 6: CDNs, Edge Computing, and the Geography of Content

**Course:** IT107 — Web Technologies & Internet Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

The web is not a cloud — it is a fog. Content Delivery Networks (CDNs) distribute web content to servers at the network edge, close to users, reducing latency and origin server load. By 2040, CDNs have evolved into general-purpose edge computing platforms that run application logic, enforce security policies, and host AI inference models within 5 milliseconds of 95% of the world's population. This lecture examines CDN architecture, the economics of content distribution, edge computing paradigms (Cloudflare Workers, AWS Lambda@Edge, Fastly Compute), and the geopolitical implications of a web whose physical infrastructure is concentrated in a handful of global providers.

#### Key Topics

- **CDN Architecture:** A CDN is a distributed network of edge servers (Points of Presence, or PoPs) that cache content close to users. When a user requests content (e.g., an image or video), the CDN's DNS-based request routing directs them to the nearest PoP. If the content is cached (a "cache hit"), it's served directly from the edge; if not (a "cache miss"), the edge fetches it from the origin server, caches it, and serves it. Key concepts: (1) **Anycast routing** — multiple PoPs share the same IP address, and BGP routes traffic to the nearest one; (2) **Cache hierarchies** — multiple caching layers (browser cache, edge cache, regional cache, origin shield) minimize origin traffic; (3) **Cache invalidation** — purging stale content, either by TTL (Time-To-Live) or explicit purge API.
- **From Caching to Compute:** The 2020s saw CDNs transform from static content caches into edge compute platforms. **Cloudflare Workers (2017)** pioneered the model: JavaScript/WebAssembly functions deployed globally, executing at the edge with access to a key-value store (Workers KV) and eventually a SQL database (D1). By 2040, edge compute is a mature paradigm: developers write applications that run entirely at the edge, with the origin server used only for durable storage and coordination. Edge databases (distributed SQL with sub-10ms latency) have made this architecture viable for transactional applications, not just static content.
- **The 2040 Edge Landscape:** The edge is no longer just HTTP. Edge platforms in 2040 offer: (1) **AI inference at the edge** — small language models and specialized AI models run on edge GPUs/NPUs, serving personalized recommendations, content moderation, and real-time translation without sending data to a central server; (2) **WebSocket and WebRTC at the edge** — real-time communication is terminated at the edge, minimizing latency for gaming, video conferencing, and collaborative editing; (3) **Edge-native security** — DDoS mitigation, bot detection, and WAF (Web Application Firewall) rules execute at the edge, blocking malicious traffic before it reaches the origin.
- **Geopolitics of the Edge:** By 2040, three companies control over 70% of global CDN/edge infrastructure: Cloudflare, Akamai, and AWS CloudFront. This concentration raises concerns: (1) **Single points of failure** — a Cloudflare outage (as occurred in 2020, 2022, and 2031) can take down a significant fraction of the web; (2) **Jurisdictional reach** — a U.S. court order to Cloudflare can affect websites globally; (3) **Surveillance capability** — edge providers can observe traffic patterns across their entire customer base. The **Edge Neutrality Accord (2034)** established that edge providers must not discriminate based on content, must publish transparency reports, and must offer customers control over which jurisdictions their traffic traverses.

#### Lecture Notes

The environmental footprint of CDNs is substantial but improving. By 2040, edge data centers are carbon-neutral, powered by on-site renewables and participating in carbon-aware computing — shifting non-urgent computation to times and locations with excess renewable energy. The **Green Edge Initiative (2032)** standardizes carbon accounting for edge compute, enabling developers to make carbon-aware deployment decisions.

A fascinating 2040 development is **Peer-to-Peer CDNs**. WebRTC-based P2P CDNs (pioneered by Peer5 in the 2010s) use viewers of a stream to relay content to other viewers, reducing CDN bandwidth costs. While initially used mainly for video, P2P CDN has expanded to general web content. Browsers in 2040 support a **Web Distributed Cache API** that enables sites to share cached resources directly between users, with cryptographic integrity verification. This transforms every web user into a potential edge node — a truly distributed web.

#### Required Reading

- Nygren, E., Sitaraman, R. K., & Sun, J. (2010). "The Akamai Network: A Platform for High-Performance Internet Applications." *ACM SIGOPS Operating Systems Review*, 44(3).
- Cloudflare. (2038). *Edge Computing at Global Scale: Architecture and Lessons Learned*.
- UoY Distributed Systems Lab. (2039). *The Geopolitics of CDN Concentration: Risk, Resilience, and Regulation*.
- IETF. (2036). RFC 9560: Web Distributed Cache API.

#### Discussion Questions

1. Three companies control over 70% of the CDN market. Is this concentration a market failure requiring regulation, or an efficient outcome of network effects? What would a decentralized CDN architecture look like?
2. Edge AI inference keeps user data local (no central server) but requires distributing AI models globally. How do intellectual property concerns (protecting the model) interact with privacy concerns (protecting the user)?
3. Peer-to-Peer CDNs reduce infrastructure costs but introduce trust and reliability challenges. Under what conditions is P2P distribution appropriate, and when should it be avoided?

#### Practice Problems

- Deploy a static website to a CDN (Cloudflare Pages or similar). Measure latency from multiple global locations (using tools like `ping` or HTTP benchmarking). Explain how Anycast routing delivers the site from the nearest PoP.
- Write a Cloudflare Worker (or simulate one locally) that modifies HTTP responses — adding security headers, redirecting based on geography, or A/B testing two versions of a page. Measure the latency overhead of edge compute.
- Analyze a major CDN outage (e.g., Fastly 2021 or Cloudflare 2031). Write a 500-word postmortem: root cause, blast radius, recovery time, and architectural lessons.

---

### Lecture 7: WebSockets, WebRTC, and the Real-Time Web

**Course:** IT107 — Web Technologies & Internet Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

The early web was strictly request-response: the client asked, the server answered. Real-time interaction — chat, gaming, video conferencing, collaborative editing — required workarounds (polling, long-polling, Flash sockets). The 2010s brought two transformative standards: WebSockets (2011, RFC 6455) for bidirectional streaming, and WebRTC (2011–2021) for peer-to-peer audio, video, and data. By 2040, these technologies have matured into the real-time substrate of the web, supporting everything from immersive VR conferences to AI-mediated collaborative workspaces. This lecture examines the protocols, architectures, and 2040 extensions that power the real-time web.

#### Key Topics

- **WebSockets:** WebSocket upgrades an HTTP connection to a full-duplex, bidirectional TCP socket. After the initial HTTP upgrade handshake, both client and server can send messages at any time with minimal framing overhead (2–8 bytes per message). Use cases: chat, live notifications, financial tickers, multiplayer game state, collaborative editing. By 2040, WebSockets over QUIC (WebTransport, standardized 2023) offers WebSocket-like semantics over QUIC streams, eliminating head-of-line blocking and enabling connection migration. WebTransport is the preferred protocol for new 2040 applications, though WebSockets remain widely deployed.
- **WebRTC — Peer-to-Peer Media and Data:** WebRTC enables direct peer-to-peer communication between browsers without server relay — audio, video, and arbitrary data. Key components: (1) **MediaStream (getUserMedia)** — access to camera and microphone; (2) **RTCPeerConnection** — establishes a peer-to-peer connection, handling NAT traversal (via ICE/STUN/TURN), media encoding, and encryption (DTLS-SRTP); (3) **RTCDataChannel** — peer-to-peer data channel with configurable reliability (TCP-like or UDP-like). By 2040, WebRTC has expanded to support: (1) **AV1 and AV2 video codecs** — royalty-free, high-compression codecs for 8K+ video; (2) **Spatial audio** — immersive audio for VR/AR conferencing; (3) **End-to-end encryption** — E2EE for multi-party calls via MLS (Messaging Layer Security, RFC 9420); (4) **AI-enhanced media** — on-device AI for background replacement, noise suppression, real-time translation, and sign language interpretation.
- **Signaling and NAT Traversal:** WebRTC requires a signaling channel (not specified by the standard) to exchange session descriptions (SDP) and ICE candidates. Common signaling approaches: WebSockets, REST APIs, or XMPP. NAT traversal — the challenge of connecting peers behind NATs and firewalls — uses ICE (Interactive Connectivity Establishment): gather candidates (host, STUN-reflexive, TURN-relayed), test connectivity, and select the best pair. TURN (Traversal Using Relays around NAT) servers relay media when direct connection fails, adding infrastructure cost. By 2040, TURN usage has declined as IPv6 adoption (over 70% globally) and standardized NAT behaviors have made direct connections more reliable.
- **The Immersive Web (WebXR):** By 2040, the real-time web extends into virtual and augmented reality via WebXR (successor to WebVR, standardized 2020s). WebXR enables browsers to render 3D environments and accept input from VR/AR headsets, controllers, and hand tracking. Combined with WebRTC, this enables immersive telepresence — meeting in a shared virtual space with spatial audio, 3D avatars, and shared virtual objects. UoY's **Yggdrasil Commons** project (2037) built a WebXR campus where remote students attend lectures, collaborate in virtual labs, and socialize in digital recreations of historical Norse sites.

#### Lecture Notes

The scalability of real-time web applications presents unique challenges. A chat application with 10,000 concurrent users requires managing 10,000 persistent connections per server. By 2040, the standard architecture is: (1) **Edge termination** — WebSocket/WebTransport connections terminate at edge servers close to users; (2) **Pub/Sub backend** — messages are published to a distributed pub/sub system (e.g., Apache Pulsar, Redis Streams, or a custom NCCL-based system) that delivers to interested subscribers across all edge nodes; (3) **State synchronization** — CRDTs (Conflict-free Replicated Data Types) enable collaborative editing without a central server for ordering, reducing latency.

A 2040 frontier is **AI-mediated real-time communication**. AI agents participate in real-time channels as moderators, translators, summarizers, and fact-checkers. An AI agent in a video call can: transcribe the conversation in real time, translate between languages with sub-second latency, flag potential misinformation with inline corrections, and generate meeting summaries with action items. The challenge is ensuring that AI mediation is transparent (participants know when AI is active), controllable (participants can disable or configure AI features), and unbiased (AI models must serve all participants equally).

#### Required Reading

- Fette, I., & Melnikov, A. (2011). RFC 6455: The WebSocket Protocol.
- IETF. (2023). WebTransport over HTTP/3.
- IETF. (2032). RFC 9420: The Messaging Layer Security (MLS) Protocol.
- UoY Immersive Media Lab. (2039). *The Yggdrasil Commons: WebXR for Distributed Higher Education*.

#### Discussion Questions

1. WebRTC enables end-to-end encryption for peer-to-peer communication, but multi-party calls typically require a Selective Forwarding Unit (SFU) that decrypts and re-encrypts media. MLS promises E2EE for groups. Does widespread E2EE for real-time communication create a "going dark" problem for lawful interception, or is it a fundamental right?
2. AI-mediated real-time communication (translation, moderation, summarization) processes spoken conversation in real time. Who controls the AI models? What happens when participants disagree with the AI's moderation decisions?
3. WebXR enables immersive telepresence, but VR/AR hardware remains expensive and physically isolating. Is the immersive web a democratic medium or an elite one? How can universities like UoY ensure equitable access?

#### Practice Problems

- Implement a simple WebSocket chat server and client. Add features: rooms, usernames, typing indicators. Measure message latency from client A to client B through the server.
- Set up a WebRTC peer connection between two browser tabs. Capture the SDP offer/answer and ICE candidate exchange. Measure the time from `createOffer()` to media flowing.
- Design an architecture for AI-mediated live translation in a WebRTC video call. Where does the AI model run (client, edge, cloud)? What latency constraints must it meet?

---

### Lecture 8: Microservices, Containers, and Cloud-Native Web Architecture

**Course:** IT107 — Web Technologies & Internet Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

The monolithic web application — a single deployable unit containing all logic — dominated the early web. By the 2010s, the microservices paradigm had emerged: decompose an application into small, independently deployable services, each responsible for a single business capability, communicating over the network. By 2040, cloud-native architecture — microservices orchestrated by Kubernetes, deployed via GitOps, observed through distributed tracing — is the default for web-scale applications. This lecture examines the architectural principles, operational practices, and 2040 innovations in cloud-native web architecture.

#### Key Topics

- **From Monolith to Microservices:** The microservices paradigm, articulated by Martin Fowler and James Lewis (2014), promises: (1) Independent deployability — teams can deploy their services without coordinating with others; (2) Technology heterogeneity — each service can use the most appropriate language/framework/database; (3) Organizational alignment — service boundaries map to team boundaries (Conway's Law). Costs: (1) Network complexity — inter-service communication adds latency and failure modes; (2) Data consistency — distributed transactions are hard, requiring eventual consistency and compensating patterns; (3) Operational overhead — monitoring, tracing, and debugging a distributed system is harder than a monolith. By 2040, the pendulum has swung toward a pragmatic middle: **modular monoliths** for early-stage projects, **microservices** for scaling organizations, and **macroservices** (domain-aligned services, larger than microservices but still independent) as a common compromise.
- **Containers and Orchestration:** Containers (Docker, standardized via OCI) package applications with their dependencies, ensuring consistency across environments. Kubernetes (K8s) emerged as the dominant container orchestration platform, providing: scheduling, service discovery, load balancing, rolling updates, and self-healing. By 2040, Kubernetes has evolved significantly: (1) **Serverless Containers** — services scale to zero when idle, reducing cost; (2) **AI-driven scheduling** — K8s schedulers use ML to predict resource usage and preemptively scale or move workloads; (3) **Multi-cluster federation** — organizations operate dozens or hundreds of clusters across regions and providers, with unified control planes; (4) **Wasm on K8s** — WebAssembly modules run alongside containers, offering faster cold start and stronger sandboxing for untrusted code.
- **Service Mesh and Observability:** The service mesh (Istio, Linkerd, Cilium) offloads cross-cutting concerns — service discovery, load balancing, encryption (mTLS), retries, circuit breaking — from application code to a sidecar proxy (Envoy). By 2040, the service mesh has absorbed additional responsibilities: (1) **API governance** — enforcing schemas, rate limits, and data-use policies at the mesh level; (2) **Cost attribution** — tracking per-service, per-team cloud resource consumption for FinOps; (3) **AI traffic management** — dynamically routing traffic based on model predictions of service health and user experience. Observability has converged on the OpenTelemetry standard for traces, metrics, and logs, with AI-driven anomaly detection identifying problems before humans notice.
- **GitOps and Continuous Delivery:** GitOps (pioneered by Weaveworks, 2017) treats Git repositories as the single source of truth for declarative infrastructure and application configuration. An operator (e.g., Flux, Argo CD) continuously reconciles the desired state in Git with the actual state in the cluster. By 2040, GitOps has expanded to: (1) **Policy-as-Code** — security policies, compliance rules, and cost controls are defined in Git and enforced automatically; (2) **AI-Assisted Operations** — AI agents propose configuration changes (scaling, tuning, dependency updates) as pull requests, which humans review and approve; (3) **Progressive Delivery** — canary deployments, feature flags, and A/B testing are managed through GitOps workflows.

#### Lecture Notes

The cloud-native ecosystem has been shaped by the **CNCF (Cloud Native Computing Foundation)** , which by 2040 hosts over 300 graduated, incubating, and sandbox projects. The CNCF's role as a vendor-neutral home for open-source infrastructure has been crucial in preventing any single cloud provider from controlling the ecosystem, though concerns about hyperscaler influence persist.

A 2040 development is **Sustainability-Driven Architecture**. The **GreenOps framework** extends FinOps (cloud financial operations) to include carbon accounting. Kubernetes clusters report per-workload carbon emissions, and scheduling decisions consider carbon intensity. The **Carbon-Aware K8s Scheduler** (CNCF Graduated, 2038) can delay non-urgent batch jobs to times of day when renewable energy is abundant, reducing a cluster's carbon footprint by 20-40%.

Another frontier is **Confidential Computing in the cloud**. By 2040, all major cloud providers offer confidential VMs and containers where memory is encrypted even from the hypervisor, enabled by hardware trusted execution environments (Intel TDX, AMD SEV-SNP, ARM CCA). This enables multi-party computation where multiple organizations collaborate on sensitive data without exposing it to each other or the cloud provider — transformative for healthcare, finance, and government applications.

#### Required Reading

- Fowler, M., & Lewis, J. (2014). "Microservices: A Definition of This New Architectural Term." martinfowler.com.
- Burns, B., Beda, J., & Hightower, K. (2035). *Kubernetes: Up and Running* (5th ed.). O'Reilly Media.
- CNCF. (2039). *Cloud Native Sustainability Report 2040*.
- UoY Cloud Lab. (2040). *Confidential Computing for Multi-Party Web Applications*.

#### Discussion Questions

1. Microservices solve organizational scaling (teams can work independently) but introduce technical complexity (distributed systems are hard). Is this a good trade-off? Could organizational scaling be solved without microservices?
2. GitOps puts infrastructure configuration in Git. But Git was designed for source code, not infrastructure state. Does GitOps introduce a category error, or is it a legitimate extension of software engineering practices to operations?
3. Confidential computing promises that even the cloud provider cannot see your data. But hardware TEEs have had security vulnerabilities (e.g., various side-channel attacks). Is the promise of confidential computing deliverable, or will it remain a cat-and-mouse game?

#### Practice Problems

- Deploy a simple microservices application (two services + API gateway) to a local Kubernetes cluster (minikube or kind). Implement health checks, rolling updates, and horizontal pod autoscaling.
- Install Istio and configure mTLS between your services. Use Kiali to visualize the service mesh. Observe how Istio's sidecar proxies handle retry and circuit breaking.
- Implement a GitOps workflow: define your application in a Git repository and use Argo CD or Flux to deploy it to Kubernetes. Make a change to the Git repo and observe the automatic reconciliation.

---

### Lecture 9: Semantic Web, Linked Data, and Knowledge Graphs

**Course:** IT107 — Web Technologies & Internet Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

The original web was a web of documents — HTML pages connected by hyperlinks, designed for human readers. The Semantic Web (Tim Berners-Lee, 2001) envisioned a web of data — machine-readable, semantically annotated, interlinked data that software agents could query, reason about, and act upon. By 2040, the Semantic Web vision has partially materialized in the form of knowledge graphs, linked data platforms, and schema.org annotations, though Berners-Lee's more ambitious vision of autonomous agents reasoning across the open web remains aspirational. This lecture examines the Semantic Web stack (RDF, OWL, SPARQL), its practical implementations, and the 2040 convergence with large language models.

#### Key Topics

- **The Semantic Web Stack:** The core technologies: (1) **RDF (Resource Description Framework)** — a data model based on subject-predicate-object triples, serializable in formats like Turtle, JSON-LD, or RDF/XML; (2) **RDFS and OWL (Web Ontology Language)** — schema and ontology languages for defining classes, properties, and relationships with formal semantics; (3) **SPARQL** — a query language for RDF data, analogous to SQL for relational databases; (4) **Linked Data** — the practice of publishing RDF data on the web using HTTP URIs, with links between datasets (the "Linked Open Data cloud" contains thousands of interconnected datasets by 2040).
- **Knowledge Graphs:** A knowledge graph is a structured representation of entities and their relationships, typically grounded in an ontology. Notable examples: (1) **Google Knowledge Graph** — powers Google's infoboxes and entity understanding, containing billions of entities; (2) **Wikidata** — the structured data backbone of Wikipedia, with over 200 million items by 2040; (3) **DBpedia** — extracts structured data from Wikipedia infoboxes; (4) **Yggdrasil Knowledge Graph (YKG)** — UoY's own academic knowledge graph, linking research papers, courses, concepts, and historical Norse sources. Knowledge graphs enable: semantic search (finding entities, not just keywords), question answering, recommendation systems, and AI reasoning.
- **Schema.org and Web Annotations:** Schema.org (launched 2011 by Google, Microsoft, Yahoo, and Yandex) provides a shared vocabulary for marking up web pages with structured data. By 2040, over 70% of web pages include schema.org markup (JSON-LD or Microdata), enabling search engines and AI assistants to extract structured information from web pages. The schema vocabulary has expanded from e-commerce and events to include scientific datasets, legislative documents, cultural heritage, and educational resources.
- **The LLM-Linked Data Convergence:** The rise of large language models (LLMs) in the 2020s–2030s reshaped the Semantic Web landscape. LLMs can extract structured data from unstructured text, reducing the need for manual annotation. LLMs can also consume structured data to improve factual grounding. By 2040, the dominant paradigm is **Neuro-Symbolic Web Architecture**: LLMs handle natural language understanding and generation, while knowledge graphs provide structured, verifiable, auditable ground truth. The **RDF-GPT framework** (2035) enables LLMs to query knowledge graphs in natural language, with the LLM translating to SPARQL, executing the query, and composing a response — combining the flexibility of LLMs with the precision of structured queries.

#### Lecture Notes

The Semantic Web's original vision — a web where autonomous agents discover, compose, and negotiate services without human intervention — was ahead of its time. The technology stack (RDF, OWL, SPARQL) was powerful but complex, and the chicken-and-egg problem (no data without applications, no applications without data) limited adoption. However, by 2040, the vision has been vindicated in more targeted forms:

1. **Enterprise Knowledge Graphs** — internal knowledge management, connecting siloed data sources, enabling cross-departmental analytics — are standard practice in large organizations.
2. **Scientific Knowledge Graphs** — connecting research papers, datasets, methods, and results — are transforming scientific discovery, enabling automated meta-analysis and hypothesis generation.
3. **Cultural Heritage Linked Data** — museums, archives, and libraries publish their collections as Linked Data, creating a global, interconnected cultural record. UoY's **Norse Digital Archive** links runic inscriptions, saga manuscripts, archaeological sites, and linguistic data in a knowledge graph queried by researchers worldwide.

#### Required Reading

- Berners-Lee, T., Hendler, J., & Lassila, O. (2001). "The Semantic Web." *Scientific American*, 284(5), 34–43.
- Bizer, C., Heath, T., & Berners-Lee, T. (2009). "Linked Data — The Story So Far." *International Journal on Semantic Web and Information Systems*, 5(3).
- UoY Knowledge Systems Lab. (2039). *Neuro-Symbolic Web Architecture: LLMs and Knowledge Graphs in Symbiosis*.
- Wikidata. (2040). *The State of Wikidata: 200 Million Items and Counting*.

#### Discussion Questions

1. LLMs can answer questions from unstructured text, so some argue that structured knowledge graphs are obsolete. What can knowledge graphs do that LLMs cannot? Where does structured data remain essential?
2. The Semantic Web stack (RDF, OWL, SPARQL) was designed for machines, not humans. Did this complexity doom it to niche adoption? Could a simpler, more human-friendly linked data format have succeeded where RDF stumbled?
3. Knowledge graphs encode ontological commitments — choices about what entities exist and how they relate. Who gets to define these ontologies? How do we prevent ontological colonialism where Western categories are imposed on non-Western knowledge systems?

#### Practice Problems

- Model a simple domain (e.g., university courses, Norse mythology, or music albums) as RDF triples. Write a SPARQL query that traverses relationships (e.g., "find all courses taught by professors who studied at a given institution").
- Extract structured data from a web page using JSON-LD and schema.org vocabulary. Validate your extraction against the Schema.org specification.
- Use SPARQL to query Wikidata for all Norse archaeological sites with their geographic coordinates and associated time periods. Visualize the results on a map.

---

### Lecture 10: WebAssembly and Browser-Native Computing

**Course:** IT107 — Web Technologies & Internet Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

For the first two decades of the web, JavaScript was the only programming language that ran natively in browsers. Efforts to break this monopoly — Java applets, Flash, Silverlight, Google Native Client — failed for reasons of security, performance, or platform lock-in. WebAssembly (Wasm), standardized in 2019, finally succeeded: a binary instruction format for a stack-based virtual machine, designed as a portable compilation target for languages like C, C++, Rust, and Go. By 2040, WebAssembly has transformed from a browser complement to JavaScript into a universal runtime running in browsers, servers, edge devices, and embedded systems. This lecture examines WebAssembly's architecture, the Component Model, WASI (WebAssembly System Interface), and the implications of a language-independent web.

#### Key Topics

- **WebAssembly Architecture:** Wasm is a low-level binary format with a structured stack machine design. Key properties: (1) **Safe** — Wasm runs in a sandboxed memory environment, with no access to the host system except through explicitly imported functions; (2) **Fast** — near-native execution speed, achieved through streaming compilation and aggressive optimization; (3) **Portable** — a Wasm module runs identically across all major browsers and standalone runtimes; (4) **Compact** — the binary format is designed for efficient transmission over the network. By 2040, Wasm has evolved through several versions: SIMD, multi-threading, garbage collection (GC), exception handling, and tail calls are all standardized and deployed.
- **The Component Model and WASI:** Initially, Wasm was limited to computation — it couldn't access files, networks, or system resources. The **WebAssembly System Interface (WASI)** provides a standardized set of system interfaces (filesystem, networking, random numbers, clocks) that Wasm modules can import. The **Component Model** (standardized 2030) goes further: it defines a language-independent interface description language (WIT) enabling components written in different languages to compose. A Rust component can call a Go component, which calls a JavaScript component — all within the same sandbox, with interface-level type checking. By 2040, the Component Model enables a global ecosystem of composable Wasm components — a "npm for Wasm" where components are language-agnostic and secure by construction.
- **Wasm on the Server and Edge:** Wasm's sandboxing and fast startup make it ideal for serverless and edge computing. Platforms like Cloudflare Workers, Fastly Compute, and Fermyon Spin execute Wasm modules at the edge. Compared to containers: Wasm modules start in microseconds (vs. seconds for containers), consume minimal memory, and provide stronger isolation (no shared kernel). The **Wasm-on-K8s** ecosystem (Krustlet, runwasi, wasmCloud) enables running Wasm workloads alongside containers in Kubernetes. By 2040, a significant fraction of new serverless applications are deployed as Wasm, not containers.
- **Wasm Beyond the Browser:** The Wasm runtime has escaped the browser entirely. By 2040, Wasm runs in: (1) **Database UDFs** — user-defined functions in databases (e.g., SingleStore, PostgreSQL extensions) are written in Wasm for safety and portability; (2) **Smart contracts** — blockchain platforms (Ethereum 3.0, Polkadot) use Wasm as their execution engine; (3) **Plugin systems** — applications from Figma to Blender embed Wasm runtimes for user extensions; (4) **IoT and embedded** — Wasm's small footprint (a minimal runtime is ~50KB) makes it viable for microcontrollers.

#### Lecture Notes

The relationship between JavaScript and WebAssembly has been a subject of ongoing debate. Early rhetoric framed Wasm as a "JavaScript killer," but the reality is symbiotic. JavaScript remains the dominant language for web UI, benefiting from decades of framework investment (React, Vue, Svelte) and an enormous developer community. Wasm excels at computationally intensive tasks — image/video processing, 3D rendering, scientific simulation, cryptography, AI inference — where JavaScript's dynamic typing and garbage collection introduce unacceptable overhead.

By 2040, the typical web application architecture is: **JavaScript for UI orchestration, Wasm for computation**. UI frameworks compile their rendering engines to Wasm for performance, while application logic (auth, routing, state management) remains in JavaScript/TypeScript for development velocity. AI models run in Wasm (compiled from Python/PyTorch via tools like Wasky), enabling client-side inference without sending data to servers.

A 2040 frontier is **WebAssembly as a Universal Bytecode**. If LLVM can compile any language to Wasm, and every platform runs a Wasm runtime, then Wasm becomes the Java "write once, run anywhere" promise — finally fulfilled, but with better performance, stronger sandboxing, and language neutrality. The **Wasm-Native Cloud** vision, where cloud providers expose raw Wasm execution rather than Linux containers, is being prototyped by multiple providers.

#### Required Reading

- Haas, A., et al. (2017). "Bringing the Web Up to Speed with WebAssembly." *ACM SIGPLAN Conference on Programming Language Design and Implementation (PLDI)*.
- W3C WebAssembly Working Group. (2030). *WebAssembly Component Model Specification*.
- Cloudflare. (2039). *Wasm at the Edge: Five Years of Production Experience*.
- UoY Programming Languages Lab. (2040). *Wasm as Universal Bytecode: Security, Performance, and Composability*.

#### Discussion Questions

1. The "web platform" was historically synonymous with JavaScript/HTML/CSS. WebAssembly breaks this trinity — any language can now target the web. Does this enrich the web ecosystem or fragment it? What is lost when web development is no longer universally accessible through a single language?
2. WebAssembly's sandbox model provides strong isolation but limits what modules can do without explicit capability grants. Is this "capability-based security" the right model for the web, or does it add friction without proportional benefit?
3. "Write once, run anywhere" failed for Java applets due to performance and security issues. Why has WebAssembly succeeded where Java failed? Is Wasm's success durable, or will the next platform shift repeat the cycle?

#### Practice Problems

- Write a simple function in Rust (e.g., Fibonacci or image blur) and compile it to WebAssembly using `wasm-pack`. Call the Wasm function from JavaScript and measure the performance difference compared to a pure JavaScript implementation.
- Create a Wasm component using the Component Model, defining a WIT interface and implementing it in one language (e.g., Rust). Then create a consumer in a different language (e.g., JavaScript) that imports and uses the component.
- Deploy a Wasm module to Cloudflare Workers. Compare cold start time and memory usage to an equivalent Node.js worker.

---

### Lecture 11: Privacy, Accessibility, and the Ethical Web

**Course:** IT107 — Web Technologies & Internet Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

The web's architecture is not neutral — it encodes values. Decisions about what data is collected, how users are identified, whether content is accessible to people with disabilities, and whose languages and cultures are represented shape who can participate in digital society. By 2040, privacy, accessibility, and ethics are not afterthoughts but first-order architectural concerns, regulated by law and demanded by users. This lecture examines the technical and policy frameworks that define the ethical web.

#### Key Topics

- **Privacy by Architecture:** Privacy on the web has evolved from the "notice and consent" model (cookie banners, privacy policies) to architectural privacy — embedding data protection into protocols themselves. Key 2040 privacy technologies: (1) **Oblivious HTTP (OHTTP)** — relays HTTP requests through a proxy so the server doesn't know the client's IP; (2) **Private Information Retrieval (PIR)** — retrieves database records without revealing which record was accessed; (3) **Differential Privacy** — adds calibrated noise to aggregate statistics, protecting individual contributions while preserving analytical utility; (4) **On-Device Processing** — AI models run locally on user devices via WebAssembly/WebGPU, processing data without sending it to servers. The **European Digital Sovereignty Directive (2037)** mandates that personal data processing must default to on-device unless server processing is demonstrably necessary.
- **Web Accessibility (a11y):** The Web Content Accessibility Guidelines (WCAG) have evolved from WCAG 2.0 (2008) through WCAG 3.0 (2030) to WCAG 4.0 (2040). The 2040 standard is more holistic, covering not just visual and motor accessibility but cognitive accessibility, neurodiversity accommodation, and AI-mediated accessibility. Key 2040 technologies: (1) **AI screen readers** — understand page semantics, summarize complex content, and navigate by intent ("find the contact form"); (2) **Adaptive interfaces** — automatically adjust contrast, font size, layout density, and interaction mode based on user needs; (3) **Sign language avatars** — real-time translation of text and audio into sign language using 3D avatars; (4) **Cognitive load management** — interfaces that detect user confusion and offer simplified views. The **Global Accessibility Mandate (2035)** requires all public-facing web services (government, education, healthcare, finance, large commercial) to meet WCAG 4.0 Level AA by 2038.
- **Language Justice and the Multilingual Web:** By 2040, the web supports all 7,000+ human languages through Unicode 16.0 and standardized language tags (BCP 47). However, support is uneven: the top 10 languages account for over 70% of web content. The **Language Justice in Digital Spaces Accord (2036)** establishes that: (1) critical public information must be available in all official languages of the jurisdiction; (2) research funding should prioritize NLP for under-resourced languages; (3) machine translation should be freely available for low-resource languages via public API. UoY contributes through the **Norse Digital Archive**, which provides Old Norse content with translations, linguistic annotations, and cultural context.
- **The Right to Not Be Tracked:** The surveillance advertising model that dominated the 2010s–2020s web has been substantially constrained by regulation. The **Global Privacy Framework (2032)** — building on GDPR (EU, 2018), CCPA (California, 2020), and similar laws — establishes: (1) opt-in consent for behavioral tracking; (2) right to access and delete personal data; (3) data portability between services; (4) algorithmic transparency for automated decisions; (5) prohibitions on dark patterns that manipulate consent. By 2040, the web advertising market has shifted from behavioral targeting to contextual advertising and direct publisher relationships, with blockchain-based ad auditing for transparency.

#### Lecture Notes

The ethical web is not just about compliance — it's about dignity. Every design decision either includes or excludes. A web form that requires a phone number excludes people without phones. A CAPTCHA that relies on visual pattern recognition excludes blind users. A website available only in English excludes non-English speakers. These are not edge cases — collectively, people with disabilities, non-English speakers, and people without reliable Internet access constitute the majority of the world's population.

The **University of Yggdrasil's Web Ethics Lab** (est. 2030) researches these questions empirically: measuring the accessibility of the top 10,000 websites annually, auditing privacy practices, and developing open-source tools for ethical web development. One finding: by 2040, AI-generated web content (articles, product descriptions, educational materials) often fails accessibility audits because AI models are trained on existing content that already has accessibility issues. The lab's **Accessible-by-Default AI** project trains AI content generators to produce WCAG 4.0-compliant output — a contribution to breaking the cycle of inaccessibility.

#### Required Reading

- W3C. (2040). *Web Content Accessibility Guidelines (WCAG) 4.0*.
- European Commission. (2037). *Digital Sovereignty Directive: Data, Identity, and AI*.
- UN Internet Governance Forum. (2036). *Language Justice in Digital Spaces Accord*.
- UoY Web Ethics Lab. (2039). *The State of Web Accessibility 2040: Annual Report*.

#### Discussion Questions

1. "Privacy by architecture" embeds data protection into protocols, making surveillance structurally impossible rather than legally prohibited. Is this approach more effective than legal regulation, or does it risk creating a web that is private but ungovernable?
2. WCAG 4.0 requires AI-generated content to be accessible. But AI models are trained on existing content that often lacks accessibility. How do we break this chicken-and-egg problem?
3. The shift from behavioral advertising to contextual advertising reduces tracking but may concentrate ad revenue among large publishers who can offer premium contexts. Does privacy regulation inadvertently disadvantage small publishers and independent creators?

#### Practice Problems

- Audit a website using an automated accessibility tool (e.g., Axe, Lighthouse). Identify WCAG violations and propose fixes. Test with a screen reader to understand the user experience.
- Implement a web form that respects privacy by design: no unnecessary fields, clear purpose statements, opt-in consent, and data minimization. Compare to a typical signup form that collects excessive data.
- Use browser developer tools to analyze the tracking mechanisms on a popular website. Identify cookies, fingerprinting scripts, and third-party requests. Write a 500-word analysis of the website's privacy posture.

---

### Lecture 12: The Future of the Web — DWeb, IPFS, and Post-Cloud Architectures

**Course:** IT107 — Web Technologies & Internet Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

#### Overview

The web's centralized architecture — where a few companies control the platforms, infrastructure, and protocols — has been the subject of critique and counter-movement since the 2000s. The decentralized web (DWeb) movement advocates for protocols that distribute power: content-addressed storage (IPFS), peer-to-peer networking (libp2p), decentralized identity (DIDs), and blockchain-based coordination. By 2040, the DWeb has not replaced the centralized web but has carved out significant niches: scientific data archiving, censorship-resistant publishing, community-owned social networks, and verifiable credentials. This lecture surveys the DWeb landscape, evaluates what has succeeded and what has failed, and projects the web's architecture toward 2060.

#### Key Topics

- **IPFS and Content Addressing:** The InterPlanetary File System (IPFS) replaces location-based addressing ("fetch this file from server X") with content-based addressing ("fetch the file whose cryptographic hash is Y"). This means: (1) content integrity is verified automatically; (2) identical content is deduplicated (same hash = same file); (3) content can be served by any node that has it, not just the original publisher. By 2040, IPFS is widely used for scientific data, open-access publishing, NFT storage, and archival purposes. The **IPFS Gateway Network** — a federated system of HTTP gateways run by universities, nonprofits, and companies — makes IPFS content accessible to standard browsers. UoY operates an IPFS gateway as part of the **Norse Digital Preservation Initiative**.
- **Decentralized Identity (DIDs and VCs):** The W3C's Decentralized Identifiers (DIDs) and Verifiable Credentials (VCs) standards enable identity that is not controlled by any central authority. A DID is a globally unique identifier (e.g., `did:example:123`) resolved to a DID Document containing public keys and service endpoints. VCs are cryptographically signed claims ("University of Yggdrasil certifies that Runa Freyjasdottir earned a B.S. in Information Technology") that can be verified without contacting the issuer. By 2040, the **Global Credential Network** — an open, federated system of credential issuers, holders, and verifiers — has largely replaced centralized academic credentialing, professional licensing, and age verification. UoY issues all degrees as VCs.
- **Federated Social Media (ActivityPub, AT Protocol):** The fediverse — a federation of independently operated social media servers communicating via the ActivityPub protocol (W3C standard, 2018) — has grown significantly. Mastodon (microblogging), PeerTube (video), Pixelfed (photos), and BookWyrm (books) provide decentralized alternatives to centralized platforms. By 2040, approximately 15% of social media users are on federated platforms. The **AT Protocol** (Bluesky, 2023) offers a different decentralization model: a shared "big world" indexed by independent relays, with users choosing their own algorithms for content curation. The competition between these models — full federation vs. shared index with algorithmic choice — is one of the defining architectural debates of the 2040 web.
- **Blockchain and Web3:** The blockchain/web3 movement of the 2020s promised to decentralize everything — finance, governance, identity, computing. By 2040, the hype has settled into a more realistic assessment. Blockchain is useful for: (1) **Auditability** — append-only logs of financial transactions, supply chain events, or certificate issuance that anyone can verify; (2) **Coordination** — smart contracts that automate multi-party agreements without a trusted intermediary; (3) **Digital ownership** — verifiable ownership of digital assets (though the cultural value of "owning" a JPEG remains debated). Blockchain is not useful for general-purpose computation, high-throughput applications, or anything requiring low latency. The **Energy-Efficient Consensus Accord (2030)** has largely eliminated proof-of-work, with proof-of-stake and proof-of-authority becoming the norm.

#### Lecture Notes

The DWeb's greatest success has been in **archiving and preservation**. Content-addressed storage naturally resists link rot and content drift. The **InterPlanetary Wayback Machine** — a collaboration between the Internet Archive and the IPFS project — archives the web into IPFS, ensuring that historical web content remains accessible even if original servers go offline. By 2040, the IPFS network stores over 50 exabytes of data, making it one of the world's largest distributed storage systems.

The DWeb's greatest failure has been **user experience**. Early DWeb applications required users to run local nodes, manage cryptographic keys, and understand concepts like gas fees and content hashing. By 2040, usability has improved — browsers integrate IPFS resolution natively, key management is handled by secure hardware, and progressive decentralization (applications that work centralized-first but support decentralized fallback) has become the norm. But the friction is real, and centralized platforms still offer a smoother experience for most users.

The **Post-Cloud Architecture** — the synthesis of centralized cloud, edge computing, and decentralized protocols — is the emerging paradigm for 2050. Applications will be: (1) **cloud-orchestrated** — centralized services for coordination, discovery, and complex computation; (2) **edge-executed** — latency-sensitive logic runs at CDN edges or on user devices; (3) **content-addressed** — data is identified by hash and can be served from anywhere; (4) **verifiably governed** — protocol rules are transparent and auditable. This hybrid architecture captures the efficiency of centralization and the resilience of decentralization — not either/or, but both/and.

#### Required Reading

- Benet, J. (2014). "IPFS — Content Addressed, Versioned, P2P File System." arXiv:1407.3561.
- W3C. (2022). *Decentralized Identifiers (DIDs) v1.0* and *Verifiable Credentials Data Model v1.1*.
- Bluesky. (2035). *The AT Protocol: A Self-Authenticating Social Web*.
- UoY Decentralized Systems Lab. (2040). *Post-Cloud Architecture: The Synthesis of Centralized, Edge, and Decentralized Computing*.

#### Discussion Questions

1. The DWeb promises to distribute power away from centralized platforms. But running a reliable IPFS node or ActivityPub server requires technical skill and resources — a form of digital privilege. Does the DWeb democratize the web, or does it create a new elite of node operators?
2. Blockchain-based "ownership" of digital assets is philosophically contested — can you truly own an infinitely reproducible sequence of bits? What does "ownership" mean on the decentralized web, and is it a coherent concept?
3. The post-cloud architecture is a hybrid: centralized where efficient, decentralized where resilient. Who decides which functions are handled centrally vs. decentrally? If the same companies that control the cloud also control the decentralized infrastructure, is it truly decentralized?

#### Practice Problems

- Publish a website to IPFS and access it through a public gateway. Observe how content addressing works: modify the content and observe that the CID (Content Identifier) changes. Discuss the implications for link persistence.
- Create a Decentralized Identifier (DID) and issue a simple Verifiable Credential (e.g., a "course completion" credential). Verify the credential using a DID resolver.
- Compare two federated social media protocols (ActivityPub and AT Protocol). Analyze their architectural differences: how does content discovery work? How is moderation handled? Which approach is more resistant to platform capture?

---

## Final Examination Preparation

The final examination for IT107 will consist of 8 essay questions, from which students choose 4 to answer in depth (1,000–1,500 words each). Answers should demonstrate not only technical knowledge but also architectural reasoning and ethical awareness.

### Sample Essay Questions

1. **QUIC and the End of TCP:** HTTP/3 over QUIC represents the largest transport-layer shift in web history. Analyze the architectural decisions that QUIC makes (UDP-based, built-in encryption, stream multiplexing, connection migration) and evaluate their consequences for web performance, network management, and user privacy. Has QUIC's encryption-by-default design been a net positive for the web?

2. **DNS as Infrastructure and Battleground:** DNS is simultaneously a technical protocol, a critical infrastructure, and a political battleground. Trace how DNS has been used for content control (censorship, copyright enforcement), analyze the privacy implications of DNS resolution, and evaluate whether the multistakeholder governance model (ICANN) adequately balances technical, commercial, and human rights interests.

3. **The API Paradigm Shift:** REST, GraphQL, and Agent-Native Protocol represent three generations of API design. Compare their architectural assumptions about who the client is (human developer, application, AI agent), how data is modeled, and where complexity lives. Which paradigm is best suited for a 2040 web dominated by AI-mediated interactions?

4. **Edge Computing and the Geography of the Web:** CDNs have evolved from static caches to general-purpose edge compute platforms. Analyze the architectural implications: does pushing computation to the edge improve user experience at the cost of infrastructure centralization? Discuss the geopolitical dimensions of a web where three companies control the majority of edge infrastructure.

5. **WebAssembly and the Language-Neutral Web:** WebAssembly breaks JavaScript's monopoly on browser execution. Evaluate the architectural, security, and social implications: does a language-neutral web increase or decrease the diversity of the web ecosystem? Is the "universal bytecode" vision achievable, or will platform-specific runtimes always be necessary?

6. **The Decentralized Web: Success and Failure:** The DWeb movement has achieved notable successes (IPFS for archiving, DIDs for credentials, ActivityPub for social media) but has not displaced centralized platforms. Analyze the architectural, economic, and social factors that limit DWeb adoption. Is a hybrid "post-cloud" architecture the stable equilibrium, or will one paradigm eventually dominate?

7. **Privacy vs. Functionality on the Modern Web:** Many web features (personalization, recommendation, analytics, security) require data collection. Analyze the tension between privacy and functionality, evaluating architectural approaches (on-device processing, differential privacy, federated learning, zero-knowledge proofs) that attempt to preserve both. Can the web be simultaneously private and powerful?

8. **The Web at 60: Projecting to 2050:** Based on the architectural trends studied in this course (QUIC, edge computing, WebAssembly, AI mediation, decentralized protocols), project the web's architecture to 2050. What will have changed fundamentally? What will remain surprisingly stable? Defend your predictions with technical reasoning and historical precedent.

### Final Project Option

In lieu of the final examination, students may complete a substantial final project:

**Design and prototype a web application that exemplifies 2040 architectural principles.** The project must include: (1) a technical architecture document (10+ pages) justifying design decisions with reference to course concepts; (2) a working prototype demonstrating at least three of: HTTP/3, edge compute, WebAssembly, IPFS, DIDs/VCs, or AI-mediated interaction; (3) a privacy impact assessment; (4) an accessibility audit; and (5) a 15-minute presentation to the class.

---

**Þǫkk — Thank you for your attention. May the threads of the web ever hold strong.**
