# IT107: Web Technologies & Internet Architecture
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4
**Prerequisites:** IT101 Introduction to Information Technology (concurrent enrollment acceptable)
**Description:** A foundational exploration of the web as both platform and architecture. This course traces the internet from packet-switched origins through the modern AI-augmented edge-web of 2040. Students examine the protocol stack that underpins every digital interaction — DNS resolution, HTTP/3 over QUIC, TLS 1.4, WebSocket stateful channels, and the REST/GraphQL/gRPC API triad. The course culminates in understanding how WebAssembly, edge functions, and decentralized identity converge to create the next-generation web: one where computation is ambient and the browser is an operating system.

---

## Lectures

ᚠ **Lecture 1: The Internet as Architecture — Packet Switching to Planetary Nervous System**

**Course:** IT107 — Web Technologies & Internet Architecture
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

This lecture establishes the architectural foundations of the internet, tracing its evolution from ARPANET's first four nodes (1969) to the AI-managed planetary mesh of 2040. We examine the defining innovation — packet switching — and explore why this architectural choice, rather than circuit switching, enabled the internet's explosive growth. Students will understand the end-to-end principle, the hourglass model of the protocol stack, and how the tension between intelligence at the edge versus intelligence in the network core has shaped every generation of internet architecture.

### Lecture Notes

The internet is not a technology; it is an architectural philosophy made manifest. When Paul Baran at RAND Corporation proposed packet switching in 1964 — fragmenting messages into discrete packets that could take independent paths through a distributed network — he was proposing something more radical than a communication technique. He was proposing resilience as a design principle. The network should survive nuclear attack not through hardening individual nodes but through distributing intelligence across the entire system. This was the internet's founding wisdom: *the centre cannot hold, so do not build a centre*.

The hourglass model, first articulated by the Internet Architecture Board in the 1990s, remains the most elegant description of the internet's structure. At the narrow waist sits IP — the Internet Protocol, a deliberately minimal specification that says only "here is how to address a packet and here is its format." Below the waist, any link-layer technology can carry IP packets: Ethernet, Wi-Fi, 5G, satellite mesh, quantum-entanglement channels (as of 2040, experimental but operational at UoY's Nordics Quantum Link). Above the waist, any application can ride on IP: HTTP, DNS, VoIP, VR telepresence streams, AI inference pipelines. This design — sometimes called "dumb network, smart edges" or the end-to-end principle — means innovation at the application layer requires no permission from the network. It is why the web could be invented in 1989 without changing a single router.

The end-to-end principle, articulated by Saltzer, Reed, and Clark in their 1984 paper "End-to-End Arguments in System Design," states that application-specific functions should reside at the endpoints of a communication system rather than in intermediary nodes. Reliability, security, and correctness belong to the communicating applications, not the network infrastructure. This principle has been tested repeatedly. Content Delivery Networks (CDNs) insert intermediate caches. TLS terminates and re-originates at reverse proxies. Network Address Translation (NAT) rewrites packet headers. Each of these "violations" of the pure end-to-end model represents a pragmatic trade-off — and each creates technical debt that IT professionals must understand.

By 2040, the internet has become what Vint Cerf predicted: a planetary nervous system. AI-driven traffic management (reinforcement learning agents deployed at IXPs) optimizes routing in real time. Named Data Networking (NDN), an architectural alternative that routes by content name rather than host address, has been deployed in specialized contexts (scientific data grids, interplanetary delay-tolerant networks). But the core IP architecture persists — not because it is perfect, but because its minimalism makes it adaptable. The internet's greatest architectural lesson for IT professionals is this: design for the unknown future by making the core as simple and universal as possible, and push complexity to the edges where it can evolve independently.

### Required Reading

- Saltzer, J.H., Reed, D.P., & Clark, D.D. (1984). "End-to-End Arguments in System Design." *ACM Transactions on Computer Systems*, 2(4), 277-288. [Foundational text]
- Clark, D.D. (1988). "The Design Philosophy of the DARPA Internet Protocols." *ACM SIGCOMM Computer Communication Review*, 18(4), 106-114.
- Baran, P. (1964). "On Distributed Communications." RAND Corporation Memoranda RM-3420-PR. [Historical context]
- Cerf, V. & Kahn, R. (1974). "A Protocol for Packet Network Intercommunication." *IEEE Transactions on Communications*, 22(5), 637-648.
- UoY Department of Network Architecture (2040). *The Planetary Mesh: Internet Architecture at Mid-Century*. Yggdrasil Press. Chapter 1: "The Persistence of IP."

### Discussion Questions

1. If the end-to-end principle argues for "dumb networks, smart edges," why have CDNs and middleboxes become ubiquitous? Is the principle still valid, or has it become merely an ideal?
2. How does the hourglass model constrain innovation at the application layer? What would break if IP's "narrow waist" were replaced with a richer protocol?
3. Paul Baran designed packet switching for nuclear survivability. What survival threats does the 2040 internet face, and how might architectural choices address them?

---

ᚢ **Lecture 2: The Protocol Stack — OSI, TCP/IP, and the 2040 Reality**

### Overview

This lecture dissects the protocol stack — the layered model that structures all internet communication. We compare the OSI seven-layer model (a conceptual framework that never achieved full implementation) with the TCP/IP four-layer model (the pragmatic reality). Students will understand encapsulation, the function of each layer, and how the 2040 stack accommodates QUIC, HTTP/3, and AI-orchestrated transport.

### Lecture Notes

The OSI (Open Systems Interconnection) model, standardised by ISO in 1984, is the most-taught and least-implemented networking framework in history. Its seven layers — Physical, Data Link, Network, Transport, Session, Presentation, Application — represent an idealised decomposition of communication functions. The OSI model's elegance is undisputed: each layer provides services to the layer above it and consumes services from the layer below, with strict interfaces between them. However, the actual protocols designed for OSI (X.25, X.400, FTAM) were largely abandoned by the market in favour of TCP/IP, which prioritised pragmatism over purity.

TCP/IP's four-layer model — Link, Internet, Transport, Application — is simpler because it emerged from implementation, not committee design. The Internet layer (IP) provides best-effort datagram delivery. The Transport layer offers two paradigms: TCP (reliable, ordered, connection-oriented streams) and UDP (unreliable, unordered, connectionless datagrams). Everything else — session management, presentation formatting, application semantics — lives in the Application layer, implemented by individual protocols rather than the stack. This is the end-to-end principle in architectural form: let applications decide what they need.

The most significant protocol development of the 2030s was the standardisation of QUIC (RFC 9000, 2021) and its adoption as the transport for HTTP/3. QUIC represents a philosophical shift: it moves transport functionality into userspace, running over UDP rather than requiring kernel-level TCP implementations. This means transport-layer innovation can now happen at application-deployment speed rather than operating-system-upgrade speed. QUIC integrates TLS 1.3 encryption by default — there is no unencrypted QUIC — embodying the principle that privacy and security are not optional layers but foundational requirements. QUIC also solves TCP's head-of-line blocking problem by multiplexing independent streams within a single connection.

By 2040, the QUIC ecosystem has expanded dramatically. The IETF's MASQUE working group has standardised proxying over QUIC, enabling VPN-like tunnels that are indistinguishable from regular web traffic — a double-edged sword for enterprise IT security. AI-assisted congestion control algorithms, trained on billions of real-world network traces, have replaced the hard-coded algorithms (Reno, CUBIC, BBR) of earlier decades. These ML-based controllers adapt to network conditions within microseconds, achieving throughput within 1% of theoretical maximum on most paths. For IT professionals, understanding QUIC is as essential as understanding TCP was for the previous generation.

### Required Reading

- RFC 9000: "QUIC: A UDP-Based Multiplexed and Secure Transport." IETF, 2021.
- RFC 9114: "HTTP/3." IETF, 2022.
- Langley, A., et al. (2017). "The QUIC Transport Protocol: Design and Internet-Scale Deployment." *Proceedings of SIGCOMM 2017*.
- UoY Networking Lab Technical Report 2040-03: "ML-CC: Machine Learning Congestion Control in Production Networks."
- ISO/IEC 7498-1:1994. "Information technology — Open Systems Interconnection — Basic Reference Model." [Historical reference]

### Discussion Questions

1. Why did TCP/IP win over OSI in the marketplace, despite OSI's conceptual elegance? What does this tell us about how standards succeed or fail?
2. QUIC moves transport into userspace. What are the security implications of making transport-layer implementations easier to deploy and modify?
3. If AI-controlled congestion becomes universal, what happens when two AI controllers with different objectives compete for the same bottleneck link?

---

ᚦ **Lecture 3: DNS — The Internet's Distributed Nervous System**

### Overview

The Domain Name System is the most underappreciated critical infrastructure on the internet. This lecture examines DNS architecture — hierarchical namespace, authoritative and recursive resolvers, zone files and resource records — and traces its evolution from a simple hostname-to-address mapping service to a sophisticated distributed database that underpins service discovery, load balancing, and security policy enforcement. Students will understand DNS resolution from root hints to answer, the role of DNSSEC in establishing trust, and the privacy innovations (DoH, DoT, DoQ) reshaping DNS in 2040.

### Lecture Notes

DNS was designed in 1983 by Paul Mockapetris to solve a specific and growing problem: the hosts.txt file maintained by the Stanford Research Institute's Network Information Center could no longer scale. Every host on the ARPANET needed a unique name, and distributing a single flat file to every connected machine was becoming impossible. Mockapetris's insight was hierarchy: a tree-structured namespace with delegation at every level, where authority is distributed rather than centralised.

The DNS namespace is rooted at "." (the root zone), served by 13 logical root server clusters (identified by letters A through M) operated by 12 independent organisations under the oversight of ICANN. Below the root, Top-Level Domains (TLDs) — generic (.com, .org, .net, and by 2040 hundreds more including .ygg, UoY's sponsored TLD for Norse cultural institutions) and country-code (.uk, .jp, .no) — delegate authority to second-level domains, which may further delegate to subdomains. Resolution follows this hierarchy: a recursive resolver starts at the root, follows referrals downward, and caches results according to TTL (Time to Live) values set by zone administrators.

The resource record types form DNS's vocabulary. A records map names to IPv4 addresses; AAAA records map to IPv6. CNAME records create aliases. MX records direct email. NS records delegate authority. TXT records carry arbitrary text — used extensively for domain verification, SPF email authentication, and, by 2040, AI-readable policy declarations. SRV records enable service discovery, answering not just "what is the address of example.com?" but "what server provides XMPP service for example.com, on which port, with what priority?".

DNS security is a layered problem. Cache poisoning attacks (the Kaminsky attack of 2008 being the most famous) exploit the lack of authentication in traditional DNS responses. DNSSEC addresses this by adding cryptographic signatures to DNS records, establishing a chain of trust from the root zone downward. However, DNSSEC adoption has been slow — only about 30% of domains had deployed it by 2030 — because key management is operationally complex and misconfigurations can render domains unreachable. By 2040, automated DNSSEC management (through ACME-like protocols extended to DNS) has improved adoption, though operational caution persists.

DNS privacy has become a major concern. Traditional DNS queries are unencrypted UDP packets, visible to any network observer. DNS-over-HTTPS (DoH, RFC 8484) and DNS-over-TLS (DoT, RFC 7858) encrypt queries between stub resolvers and recursive resolvers, preventing on-path surveillance. DNS-over-QUIC (DoQ, RFC 9250) further reduces latency. However, these technologies shift trust from the network to the DNS resolver operator — typically a large entity like Cloudflare, Google, or Quad9. The 2040 consensus among privacy researchers is that encrypted DNS is necessary but insufficient; anonymised DNS (Oblivious DNS-over-HTTPS, or ODoH) adds an additional layer of indirection to separate the identity of the querier from the content of the query.

### Required Reading

- Mockapetris, P. (1987). RFC 1034: "Domain Names — Concepts and Facilities" and RFC 1035: "Domain Names — Implementation and Specification."
- RFC 4033-4035: "DNS Security Introduction and Requirements" (DNSSEC suite).
- RFC 8484: "DNS Queries over HTTPS (DoH)."
- RFC 9230: "Oblivious DNS over HTTPS."
- UoY Internet Measurement Lab (2039). *DNS in the Nordic Region: Adoption, Latency, and Resilience*. Annual Report.

### Discussion Questions

1. DNS is a hierarchical system in an internet that values decentralisation. What are the political and technical implications of having 13 organisations control the root zone?
2. Is encrypted DNS (DoH/DoT) a net privacy improvement, or does it simply shift trust from ISPs to large DNS resolver operators?
3. If you were designing DNS from scratch in 2040, knowing what we know about security and privacy, what would you change?

---

ᚨ **Lecture 4: HTTP — The Application Protocol That Ate the World**

### Overview

HTTP began as a simple document retrieval protocol and evolved into the universal application transport. This lecture traces HTTP's evolution from 0.9 to 3.0, examining the architectural decisions that made it the substrate for REST APIs, real-time streaming, bidirectional communication, and server-sent events. We explore HTTP semantics — methods, status codes, headers, caching directives — and analyse how HTTP/2's multiplexing and HTTP/3's QUIC transport addressed the performance limitations of earlier versions.

### Lecture Notes

Tim Berners-Lee's original HTTP/0.9 (1991) was breathtakingly simple: a single-line request (`GET /page.html`), a single-line response (the HTML content), and then the connection closed. No headers, no status codes, no metadata. It was a proof of concept that accidentally became infrastructure. HTTP/1.0 (1996, RFC 1945) added headers, status codes, and content negotiation — the beginning of HTTP as a general-purpose protocol rather than a document fetcher. HTTP/1.1 (1997, RFC 2068, later revised as RFC 2616 and then RFC 7230-7235) added persistent connections, chunked transfer encoding, and cache control mechanisms that remain the foundation of web infrastructure three decades later.

HTTP's semantics are what make it powerful. The uniform interface — a constrained set of methods (GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS) applied to resources identified by URIs — maps naturally to CRUD operations on data. This alignment between protocol semantics and application semantics is what made REST (Representational State Transfer, articulated by Roy Fielding in his 2000 doctoral dissertation) the dominant API architecture. When an API designer says "GET /users/42 should return the user with ID 42," they are leveraging HTTP's design philosophy: methods define the operation, URIs identify the resource, and status codes communicate the outcome.

HTTP/1.1's performance limitations became acute as web pages grew from kilobytes to megabytes. Head-of-line blocking — where a stalled request blocks all subsequent requests on the same connection — forced browsers to open multiple connections (typically 6 per origin), undermining the efficiency of persistent connections. HTTP/2 (RFC 7540, 2015) addressed this with multiplexing: multiple streams within a single TCP connection, each carrying an independent request-response exchange. Stream prioritisation allowed browsers to hint which resources were most important. Header compression (HPACK) reduced redundant header transmission.

HTTP/3 (RFC 9114, 2022) completed the evolution by moving from TCP to QUIC. This eliminated the remaining head-of-line blocking at the transport layer: in HTTP/2, a lost TCP packet blocked all streams on that connection; in HTTP/3, each QUIC stream is independently loss-tolerant. HTTP/3 also reduces connection establishment latency — QUIC's 0-RTT mode can resume sessions without any round trips, though 0-RTT data is replayable and must be used only for idempotent requests. For IT professionals managing web infrastructure in 2040, HTTP/3 is the production standard, but understanding HTTP/1.1 and HTTP/2 remains essential for debugging interop issues with legacy systems and older CDN configurations.

### Required Reading

- Fielding, R.T. (2000). "Architectural Styles and the Design of Network-based Software Architectures." Doctoral dissertation, UC Irvine. [Chapter 5: Representational State Transfer]
- RFC 9110: "HTTP Semantics." IETF, 2022.
- RFC 9112: "HTTP/1.1." IETF, 2022.
- RFC 9113: "HTTP/2." IETF, 2022.
- RFC 9114: "HTTP/3." IETF, 2022.
- Grigorik, I. (2013). *High Performance Browser Networking*. O'Reilly Media. Chapters 9-12.

### Discussion Questions

1. HTTP was designed for document transfer, yet it now carries API calls, video streams, and VR telemetry. Is HTTP still the right protocol, or has it become a "universal hammer"?
2. What architectural properties of HTTP enable it to serve as an intermediary-friendly protocol (caching proxies, CDNs, load balancers)?
3. How does HTTP/3's QUIC transport change the operational model for IT administrators compared to TCP-based HTTP?

---

ᚱ **Lecture 5: TLS and Web Security — Encryption as Infrastructure**

### Overview

Transport Layer Security is the cryptographic foundation of the modern web, and nearly every web interaction passes through it. This lecture covers TLS's handshake protocol, certificate authorities and the Web PKI, cipher suite negotiation, and forward secrecy. We examine the Certificate Transparency system (mandated since 2018 for all publicly trusted certificates), the ACME protocol (which automated certificate issuance and enabled the HTTPS-everywhere movement), and the security properties that TLS provides: confidentiality, integrity, authentication, and — critically — the cases where it fails to provide them.

### Lecture Notes

TLS (Transport Layer Security) evolved from SSL (Secure Sockets Layer), developed by Netscape in the mid-1990s. SSL 3.0 was the last version before the IETF standardised TLS 1.0 in 1999. Each subsequent version — 1.1 (2006), 1.2 (2008), 1.3 (2018) — has reduced the attack surface by removing obsolete cryptographic primitives and streamlining the handshake. TLS 1.3 reduced the handshake from two round trips to one (or zero with PSK resumption), removed support for static RSA key exchange (which lacks forward secrecy), and mandated Authenticated Encryption with Associated Data (AEAD) cipher suites.

The TLS handshake is a negotiation of cryptographic parameters. The client sends a ClientHello with supported cipher suites, TLS version, and extensions. The server responds with a ServerHello selecting the cipher suite, followed by its certificate chain. The two parties then establish shared secrets through key exchange (typically ECDHE — Elliptic Curve Diffie-Hellman Ephemeral — which provides forward secrecy: compromising the server's long-term private key does not compromise past session keys). The handshake concludes with Finished messages that verify the integrity of the negotiation under the newly established encryption keys.

Certificate Authorities form the trust backbone of the Web PKI. When a browser connects to `bank.example`, the server presents a certificate binding the domain name to a public key, signed by a CA that the browser trusts. The browser's trust store contains approximately 150 root CA certificates, and chain validation must succeed — each certificate in the chain must be signed by a CA trusted for that purpose. The CA/Browser Forum establishes baseline requirements for CA operations, but the system fundamentally relies on the diligence (and honesty) of CA operators. High-profile CA compromises (DigiNotar, 2011; WoSign/StartCom, 2016) demonstrate that the PKI is only as strong as its weakest CA.

Certificate Transparency (CT), mandated by Chrome in 2018 and by all major browsers shortly thereafter, addresses CA misbehaviour through public accountability. Every publicly trusted certificate must be logged to at least two CT logs — append-only, cryptographically verifiable ledgers — before browsers will accept it. Domain owners can monitor CT logs for certificates issued for their domains without authorisation. By 2040, CT has evolved into a broader framework called Certificate Transparency v3, which incorporates zero-knowledge proofs to log certificate issuance without revealing the domain names to log operators — preserving privacy for organisations that consider domain enumeration a security concern.

### Required Reading

- RFC 8446: "The Transport Layer Security (TLS) Protocol Version 1.3." IETF, 2018.
- RFC 6962: "Certificate Transparency." IETF, 2013.
- RFC 8555: "Automatic Certificate Management Environment (ACME)." IETF, 2019.
- Rescorla, E. (2000). *SSL and TLS: Designing and Building Secure Systems*. Addison-Wesley.
- CA/Browser Forum. "Baseline Requirements for the Issuance and Management of Publicly-Trusted Certificates." Version 3.0+.

### Discussion Questions

1. Certificate Authorities are trusted third parties who can, in principle, issue fraudulent certificates. Is Certificate Transparency a sufficient safeguard, or should we rethink the trust model entirely?
2. TLS 1.3 mandates forward secrecy. What does this protect against, and what attacks does it NOT protect against?
3. If a CA is compromised and issues a fraudulent certificate for your domain, how would you detect it? What tools and monitoring infrastructure would you deploy?

---

ᚲ **Lecture 6: REST, GraphQL, and the API Economy**

### Overview

Application Programming Interfaces are the connective tissue of the modern web. This lecture compares the three dominant API paradigms of the 2020s-2040s: REST (resource-oriented, HTTP-native), GraphQL (query-oriented, client-driven), and gRPC (performance-oriented, contract-first). Students will understand when to apply each paradigm, how to design APIs that survive evolution, and the operational considerations — rate limiting, versioning, observability, and schema evolution — that distinguish well-engineered APIs from fragile ones.

### Lecture Notes

REST, as articulated by Roy Fielding, is not simply "JSON over HTTP." It is a set of architectural constraints: client-server separation, statelessness, cacheability, uniform interface, layered system, and (optionally) code-on-demand. A truly RESTful API uses hypermedia as the engine of application state (HATEOAS) — the server guides the client through available actions via links in responses, much as a web browser follows links on HTML pages. In practice, most "REST APIs" implement only Levels 1-2 of the Richardson Maturity Model: they use resource URIs and HTTP methods, but omit hypermedia controls. This pragmatic REST — sometimes called "HTTP APIs" to distinguish it from Fielding's stricter definition — has become the industry standard because it is simple to implement and consume.

GraphQL, developed by Facebook in 2012 and open-sourced in 2015, inverts the REST model: instead of the server defining fixed endpoints that return fixed data shapes, the client specifies exactly what data it needs in a single query. This eliminates over-fetching (receiving more data than needed) and under-fetching (making multiple round trips to assemble related data). GraphQL's type system provides a strong contract between client and server, and its introspection capabilities enable powerful developer tooling (autocomplete, documentation generation). However, GraphQL introduces operational challenges: queries can be arbitrarily complex, requiring depth limiting and cost analysis to prevent denial-of-service; caching is more difficult because every query is a POST to a single endpoint; and the N+1 query problem (resolving nested relationships with separate database queries) requires careful optimisation with data loaders.

gRPC, developed by Google and open-sourced in 2015, uses Protocol Buffers (protobuf) for interface definition and binary serialisation, and HTTP/2 for transport. It is designed for high-performance service-to-service communication, particularly in microservice architectures. gRPC supports four communication patterns: unary (single request, single response), server streaming, client streaming, and bidirectional streaming. Its contract-first approach — defining service interfaces in .proto files, from which client and server code is generated — provides strong typing and backward-compatibility guarantees. By 2040, gRPC has become the dominant protocol for internal service communication in large-scale systems, while REST and GraphQL dominate external-facing and client-facing APIs respectively.

The API economy of 2040 extends beyond these three paradigms. AsyncAPI has standardised event-driven API descriptions (the WebSocket/Webhook counterpart to OpenAPI's REST descriptions). AI-generated API clients, trained on OpenAPI and GraphQL schemas, can adapt to API changes without developer intervention. The key skill for IT professionals is not mastery of any single paradigm but the ability to evaluate trade-offs: latency requirements, client capabilities, schema evolution strategy, and operational maturity determine which paradigm fits.

### Required Reading

- Fielding, R.T. (2000). Chapter 5 of doctoral dissertation (see Lecture 4).
- GraphQL Specification (October 2021 Edition). GraphQL Foundation.
- gRPC Documentation: "Core Concepts, Architecture, and Lifecycle." gRPC Authors.
- OpenAPI Specification 3.1.0. OpenAPI Initiative, Linux Foundation.
- UoY API Design Lab (2039). *API Paradigm Selection: A Decision Framework for 2040 Systems*.

### Discussion Questions

1. GraphQL gives clients unlimited query flexibility. How would you protect a GraphQL server from malicious or unintentionally expensive queries?
2. REST's HATEOAS constraint is rarely implemented. Is this because it's impractical, or because the industry has not yet encountered problems that HATEOAS solves?
3. If you were building a system that serves both web browsers and mobile apps, with real-time updates, which API paradigm(s) would you choose and why?

---

ᚷ **Lecture 7: Browser Architecture — The World's Most Important Runtime**

### Overview

The web browser has evolved from a document viewer into the most widely deployed application runtime in history. This lecture dissects browser architecture: the rendering engine pipeline (HTML parsing, CSS styling, layout, paint, compositing), the JavaScript engine (V8, SpiderMonkey, JavaScriptCore), the event loop and concurrency model, and the security sandbox that isolates each origin. Students will understand the Critical Rendering Path, how the browser achieves 60fps rendering, and the browser APIs — Web Workers, Service Workers, WebAssembly, WebGPU — that make the browser a legitimate operating system in 2040.

### Lecture Notes

A modern browser is a feat of systems engineering that rivals any operating system kernel. The multi-process architecture — pioneered by Chrome in 2008 and now universal — isolates each tab in its own renderer process, with the browser process managing the UI, network stack, and persistent storage. A separate GPU process handles compositing. This isolation provides both security (a compromised renderer cannot access other tabs' data) and stability (a crashing tab does not bring down the entire browser). By 2040, the process model has become even more granular: individual iframes, extensions, and even Web Workers can run in their own processes, each with a strict capability-based security model.

The rendering pipeline converts HTML, CSS, and JavaScript into pixels on screen. It begins with parsing: the HTML parser builds the Document Object Model (DOM) tree, and the CSS parser builds the CSS Object Model (CSSOM). These are combined into a Render Tree — the set of visible elements with their computed styles. Layout calculates the exact position and dimensions of each element (a process called "reflow" when triggered by DOM changes). Paint converts the layout into drawing commands. Compositing layers (managed by the GPU process) assemble the final image, enabling smooth scrolling and animations without repainting.

The JavaScript engine executes code within a single-threaded event loop — a design choice that has profound implications. JavaScript's concurrency model is cooperative: the event loop processes one task at a time from its queue, and long-running tasks block the UI. This is why Web Workers (introduced 2009) are essential: they run JavaScript in background threads, communicating with the main thread via message passing. Service Workers (introduced 2014) take this further: they intercept network requests, enabling offline functionality, background sync, and push notifications — effectively turning the browser into a programmable proxy.

WebAssembly (Wasm), standardised in 2019, brought near-native performance to the browser. Languages like C, C++, Rust, and Go can compile to Wasm, running in the same sandbox as JavaScript but with predictable performance characteristics. By 2040, the WebAssembly System Interface (WASI) has standardised Wasm's interaction with the host environment, enabling the "write once, run anywhere" promise that Java once aspired to. WebGPU (standardised 2023) provides low-level access to GPU compute and rendering, enabling browser-based machine learning inference and real-time 3D rendering at AAA game quality. The browser, in 2040, is no longer just for documents — it is a universal compute platform.

### Required Reading

- Google Chrome Team. "Inside look at modern web browser." (2018, four-part series). Chrome Developers Blog.
- Mozilla Developer Network. "How browsers work." MDN Web Docs.
- Haverbeke, M. (2018). *Eloquent JavaScript*, 3rd Edition. Chapter 11: "Asynchronous Programming." [Event loop deep-dive]
- WebAssembly Community Group. "WebAssembly Core Specification 2.0." W3C, 2022.
- UoY Browser Research Lab (2040). *The Browser as Operating System: WebGPU, WASI, and the Post-Native Era*.

### Discussion Questions

1. The browser's single-threaded event loop is often cited as a limitation. Why hasn't it been replaced with true multi-threading? What would break?
2. WebAssembly enables code from any language to run in the browser. What security implications does this create beyond those of JavaScript?
3. Service Workers can intercept all network requests from a page. How should IT administrators think about the security model of a technology that effectively acts as an on-path proxy?

---

ᚹ **Lecture 8: CDNs and Edge Computing — Moving Computation Closer**

### Overview

Content Delivery Networks transformed the web from a client-server model to a distributed edge model. This lecture examines CDN architecture — anycast routing, cache hierarchies, cache invalidation strategies, and origin shielding — and traces the evolution from static asset caching to edge computing platforms that run application logic at the network edge. Students will understand how CDNs reduce latency, absorb DDoS attacks, and enable the globally distributed web, as well as the operational complexities they introduce.

### Lecture Notes

The fundamental problem CDNs solve is the speed of light. At approximately 200,000 km/s through fibre, a round trip from London to Sydney takes about 160ms just for signal propagation — before any processing. For a web page requiring 50 round trips, that's 8 seconds of pure latency. CDNs address this by caching content at points of presence (PoPs) geographically close to users: a user in Sydney fetches from a Sydney PoP, which may need to contact the origin server in London only for cache misses. The mathematics of caching (hit ratios typically 80-95% for well-designed CDNs) means most requests never reach the origin.

CDN architecture operates at multiple layers. DNS-based routing uses the DNS resolver's location to direct users to the nearest PoP (though this can be inaccurate when users configure remote DNS resolvers). Anycast routing advertises the same IP address from multiple locations, with BGP directing packets to the topologically nearest instance. Application-layer routing inspects HTTP headers and can make more intelligent decisions — directing mobile users to optimised content, logged-in users to specific regions for data residency compliance, or API traffic to compute-capable edge nodes.

Edge computing represents the next evolution: running application code at CDN PoPs rather than merely serving cached content. Platforms like Cloudflare Workers, AWS Lambda@Edge, and their 2040 successors enable developers to deploy JavaScript, WebAssembly, or Python functions that execute at the edge, within milliseconds of the user. This enables use cases impossible with traditional CDNs: A/B testing without client-side JavaScript, authentication at the edge (validating JWTs before requests reach the origin), dynamic personalisation based on geolocation, and API gateways that transform requests between protocols.

However, edge computing introduces significant operational challenges. The consistency model is eventually consistent by default: configuration changes take seconds to minutes to propagate globally. Debugging is harder because edge functions run in a provider's infrastructure with limited observability. Cold starts (the latency of initialising a function runtime) can negate edge latency benefits for infrequently accessed functions. And the CAP theorem applies at global scale: you cannot have consistency, availability, and partition tolerance simultaneously; edge architectures typically sacrifice strong consistency for availability and low latency.

### Required Reading

- Nygren, E., Sitaraman, R.K., & Sun, J. (2010). "The Akamai Network: A Platform for High-Performance Internet Applications." *ACM SIGOPS Operating Systems Review*, 44(3).
- Varvello, M., et al. (2021). "On the Design and Performance of Cloudflare's Edge Network." *Proceedings of ACM IMC 2021*.
- Cloudflare. "Edge Computing: The Next Evolution of the Internet." Technical Whitepaper, 2035.
- UoY Distributed Systems Lab (2040). *Edge Consistency: Models and Trade-offs at Global Scale*. Yggdrasil Press.

### Discussion Questions

1. A CDN acts as a reverse proxy, terminating TLS and caching content. What does this mean for end-to-end encryption — is the CDN a trusted party in your security model?
2. Edge functions promise low latency, but cold starts can add hundreds of milliseconds. Under what circumstances would edge computing actually increase latency?
3. How does the CAP theorem constrain edge computing architectures? What consistency guarantees can you realistically provide?

---

ᚺ **Lecture 9: WebSockets, Server-Sent Events, and Real-Time Communication**

### Overview

The web was born stateless and request-response, but modern applications demand real-time bidirectional communication. This lecture covers the technologies that make the web real-time: WebSockets (full-duplex TCP-like channels over HTTP), Server-Sent Events (unidirectional server-to-client streaming), and WebRTC (peer-to-peer audio, video, and data channels). Students will understand the protocol mechanics, the operational challenges (connection management, scaling, reconnection strategies), and the use cases that each technology serves best.

### Lecture Notes

WebSockets (RFC 6455, 2011) provide a full-duplex communication channel over a single TCP connection, initiated by an HTTP Upgrade request. Once established, either party can send messages at any time — a departure from HTTP's request-response model. The WebSocket protocol is minimal: a framing layer adds 2-10 bytes of overhead per message, and messages can be text or binary. This efficiency makes WebSockets ideal for low-latency applications: trading platforms, collaborative editing, multiplayer games, and live dashboards. However, WebSockets are stateful — they require the server to maintain a connection per client, which fundamentally changes the scaling model from stateless HTTP.

The operational challenges of WebSockets are significant. Connection management requires careful handling of disconnections: exponential backoff for reconnection, message queuing during disconnection, and idempotency for operations that may be retried. Load balancers must be WebSocket-aware (non-standard HTTP behaviour). Authentication — which in REST is typically per-request via tokens — must be performed once at connection time and then trusted for the connection's lifetime. At scale, the C10K problem becomes the C10M problem: ten million concurrent WebSocket connections requires the server to maintain ten million TCP connections, each consuming kernel resources.

Server-Sent Events (SSE) offer a simpler alternative for unidirectional server-to-client streaming. The server sends a stream of text events over a single long-lived HTTP connection, and the browser's EventSource API automatically handles reconnection with the ID of the last received event. SSE is simpler to implement (it uses standard HTTP), works through most proxies, and is polyfillable. Its limitation is unidirectionality — for bidirectional communication, it must be paired with regular HTTP requests for client-to-server messages, which adds latency and complexity.

WebRTC (Web Real-Time Communication, standardised 2011-2018) enables peer-to-peer audio, video, and data channels directly between browsers, without server intermediaries for media. Its key innovation is the Interactive Connectivity Establishment (ICE) framework, which discovers the best network path between peers — even through NATs and firewalls — using STUN and TURN servers. By 2040, WebRTC has become the backbone of video conferencing (Zoom, Teams, Meet all use it), cloud gaming (low-latency video streaming with input relay), and decentralised applications (direct peer-to-peer data without central servers). For IT professionals, understanding WebRTC's NAT traversal and TURN relay infrastructure is essential for deploying real-time services.

### Required Reading

- RFC 6455: "The WebSocket Protocol." IETF, 2011.
- Hickson, I. "Server-Sent Events." W3C Recommendation, 2015.
- RFC 8825-8839: "WebRTC" suite. IETF, 2021.
- Jennings, C., et al. (2013). "Real-Time Communications for the Web." *IEEE Communications Magazine*, 51(4).
- UoY Real-Time Systems Lab (2040). *Scaling Stateful Connections: From C10K to C10M*. Technical Report.

### Discussion Questions

1. WebSockets maintain persistent connections. How does this change the security model compared to stateless HTTP? What new attack surfaces emerge?
2. Why would you choose SSE over WebSockets for a notification system? Under what circumstances would SSE be the wrong choice?
3. WebRTC's peer-to-peer model reduces server costs but introduces complexity in NAT traversal. At what scale does the operational overhead of TURN servers outweigh the savings?

---

ᚾ **Lecture 10: Web Authentication and Identity — From Passwords to Passkeys**

### Overview

Authentication is the web's most critical security boundary, and its evolution reflects the ongoing battle between usability and security. This lecture traces authentication from password-based schemes through multi-factor authentication, OAuth 2.0 and OpenID Connect (the delegation protocols that power "Sign in with Google"), and into the passwordless future of 2040: WebAuthn, FIDO2 passkeys, and decentralised identity frameworks. Students will understand the threat models, the protocol flows, and the operational responsibilities of identity providers.

### Lecture Notes

Password-based authentication is the worst system except for all the others — until recently. The security failures of passwords are well-documented: users reuse passwords across services, choose weak passwords, and fall for phishing attacks that steal them. Server-side password storage requires careful cryptographic handling (bcrypt, scrypt, or Argon2 for hashing; never plaintext or simple hashes), and credential stuffing attacks exploit password reuse across breaches. NIST SP 800-63B, first published in 2017 and regularly updated, provides the authoritative guidance on password policy: favour length over complexity, check against known compromised passwords, and never enforce periodic password changes without evidence of compromise.

OAuth 2.0 (RFC 6749, 2012) is not an authentication protocol — it is an authorisation delegation framework. It allows a user to grant a third-party application limited access to their resources without sharing their credentials. The OAuth flow that most users encounter is the Authorisation Code Grant with PKCE: the user is redirected to the authorisation server (e.g., accounts.google.com), authenticates, and consents to specific permissions; the authorisation server issues a temporary code that the application exchanges for access and refresh tokens. OpenID Connect (OIDC), built on OAuth 2.0, adds authentication: the ID Token (a signed JWT) asserts the user's identity, and the UserInfo endpoint provides profile data.

The FIDO2 standard, jointly developed by the FIDO Alliance and W3C, represents the most significant authentication advancement since public-key cryptography itself. WebAuthn (the browser API) and CTAP (the authenticator protocol) enable passwordless authentication using public-key cryptography: the user's device generates a key pair, registers the public key with the relying party, and authenticates by signing a challenge with the private key — which never leaves the device. The private key is bound to the relying party's origin (phishing-resistant). Passkeys — the consumer-friendly implementation of FIDO2, synchronised across devices via platform keychains (iCloud Keychain, Google Password Manager) — reached mainstream adoption in the 2020s and are, by 2040, the default authentication method for most web services.

Decentralised identity frameworks (Self-Sovereign Identity, or SSI, using W3C Verifiable Credentials and Decentralised Identifiers) aim to give users control over their identity data without relying on centralised identity providers. While adoption has been slower than passkeys, SSI has found traction in specific domains: academic credentials (UoY issues all degrees as Verifiable Credentials), professional licences, and supply chain provenance. For IT professionals, understanding the trade-offs — particularly the key recovery problem (lose your private key, lose your identity) — is essential.

### Required Reading

- NIST SP 800-63B: "Digital Identity Guidelines — Authentication and Lifecycle Management." Revision 4, 2026.
- RFC 6749: "The OAuth 2.0 Authorization Framework."
- OpenID Connect Core 1.0 specification. OpenID Foundation, 2014.
- W3C. "Web Authentication: An API for accessing Public Key Credentials Level 2." 2021.
- FIDO Alliance. "FIDO2: Moving the World Beyond Passwords." Technical Overview, 2035.
- UoY Identity Lab (2040). *Decentralised Identity in Practice: Five Years of Verifiable Credentials at Nordic Universities*.

### Discussion Questions

1. Passkeys solve phishing but introduce new risks: what happens when a user loses all devices enrolled in their passkey ecosystem? How should service providers handle account recovery?
2. OAuth 2.0's flexibility has been described as "a framework for building authentication protocols" rather than a protocol itself. What are the security implications of this flexibility?
3. Self-sovereign identity promises user control but creates a catastrophic key recovery problem. Is this an inherent limitation, or can it be solved without reintroducing trusted third parties?

---

ᛁ **Lecture 11: Web Performance and Observability — Measuring What Matters**

### Overview

Performance is a feature — one that directly impacts user satisfaction, conversion rates, and search ranking. This lecture covers the metrics that matter: Core Web Vitals (LCP, INP, CLS), Time to First Byte, Speed Index, and custom business metrics. We examine the measurement infrastructure — Real User Monitoring (RUM), synthetic monitoring, and the Navigation Timing and Resource Timing APIs — and the optimisation techniques that move the needle: resource hints, code splitting, image optimisation, and critical CSS inlining. Students will learn to build a performance budget and enforce it in CI/CD pipelines.

### Lecture Notes

Web performance is not about making things fast; it is about understanding what "fast" means to users. The RAIL model (Response, Animation, Idle, Load), developed by Google, established baselines: respond to user input within 100ms, produce animation frames within 16ms (60fps), and deliver meaningful content within 1000ms of navigation. By 2040, these baselines have become more nuanced with Core Web Vitals: Largest Contentful Paint (LCP) measures loading — the time until the largest visible element renders, with a "good" threshold of 2.5 seconds. Interaction to Next Paint (INP) measures responsiveness — the latency of all user interactions throughout the page lifecycle, with a "good" threshold of 200ms. Cumulative Layout Shift (CLS) measures visual stability — the sum of unexpected layout shifts, with a "good" threshold of 0.1.

Measurement without action is waste. A performance budget is a set of limits on metrics that the team agrees not to exceed: "LCP must remain under 3.0 seconds on 75th percentile mobile," or "total JavaScript bundle must not exceed 200KB compressed." These budgets are enforced in CI/CD pipelines using tools like Lighthouse CI (originally from Google, now maintained by the Web Performance Working Group), which runs performance audits on every pull request and blocks merges that regress key metrics. The cultural shift — treating performance degradation as a build failure, equivalent to a failing test — is what distinguishes performance-conscious organisations from those that discover their site has become slow months after the fact.

The measurement infrastructure has evolved dramatically. Real User Monitoring (RUM) injects JavaScript that collects timing data from actual user sessions, providing ground-truth data about real-world performance across diverse devices, networks, and geographies. Synthetic monitoring runs scripted tests from fixed locations at regular intervals, providing consistent baselines and early warning of regressions unrelated to user behaviour. The Navigation Timing API (standardised 2012, expanded through Level 3 by 2040) provides high-resolution timestamps for every phase of page loading directly from the browser. The Resource Timing API extends this to individual resources. The Server Timing header allows backends to expose application-specific timing data to the browser's performance APIs, creating end-to-end visibility from database query to painted pixel.

### Required Reading

- Google Web Fundamentals. "Web Performance." Updated continuously, web.dev/performance.
- Grigorik, I. (2013). *High Performance Browser Networking*. O'Reilly. Chapters 13-16.
- Wagner, J. (2016). *Web Performance in Action*. Manning Publications.
- W3C. "Navigation Timing Level 3." Working Draft, 2040.
- UoY Performance Engineering Lab (2040). *Performance Budgets in Practice: A Five-Year Longitudinal Study*. Technical Report.

### Discussion Questions

1. Performance budgets treat speed regressions as build failures. What organisational and cultural changes are necessary for this to work effectively?
2. RUM data reflects real users but is noisy; synthetic data is clean but artificial. How should these two data sources be weighted when making performance decisions?
3. Core Web Vitals focus on loading, responsiveness, and visual stability. What aspects of user-perceived performance do they NOT capture?

---

ᛃ **Lecture 12: The Web of 2050 — AI-Native, Ambient, and Autonomous**

### Overview

This concluding lecture synthesises the course material into a forward-looking vision of the web's next evolution. We examine three emerging paradigms: AI-native architectures (where machine learning models are not add-ons but foundational components of the web stack), ambient computing (where the web dissolves into the environment — voice interfaces, spatial computing, neural interfaces), and autonomous infrastructure (self-healing, self-scaling, self-securing web systems). Students will leave with a framework for evaluating emerging technologies and a grounded understanding of how the principles studied in this course — the end-to-end principle, layered architecture, cryptographic trust — will guide the web's evolution through 2050.

### Lecture Notes

The web of 2020 was a document platform with interactive capabilities bolted on. The web of 2040 is a compute platform that happens to render documents. The web of 2050 will be an intelligence platform — one where AI models are not services you call but capabilities woven into the fabric of the browser, the CDN, and the protocol stack. We can already see this emerging: TensorFlow.js and ONNX Runtime Web run inference in the browser; edge AI services perform real-time translation, content moderation, and personalisation at the CDN level; and AI-assisted development tools generate, test, and deploy web applications with increasing autonomy.

Ambient computing represents the dissolution of the web's boundaries. When computing is embedded in the environment — smart glasses projecting AR overlays, voice assistants that maintain conversational context, neural interfaces that respond to intention — the concept of a "web page" becomes fluid. The W3C's Ambient Web Working Group (established 2038) is developing standards for spatial web content, multimodal interaction, and context-aware content delivery. UoY's own Nordic Ambient Computing Lab is pioneering "place-aware" web applications that adapt their behaviour based on the user's physical and social context, drawing on Norse concepts of *landvættir* (land spirits) as a metaphor for ambient computational presences.

Autonomous infrastructure is the most pragmatic near-term evolution. By 2050, the operational burden of web infrastructure will be largely automated. Self-scaling systems will predict traffic patterns using time-series models and provision capacity preemptively. Self-healing systems will detect anomalies, isolate faults, and reconfigure routing without human intervention — the internet's original survivability design goal, finally realised through AI rather than simple packet switching. Self-securing systems will automatically patch vulnerabilities, rotate credentials, and respond to intrusions based on behavioural baselines rather than signature matching. The IT professional of 2050 will not manually administer servers; they will design the policies, constraints, and objectives that autonomous systems optimise toward.

Yet the fundamental principles studied in this course will not become obsolete. The end-to-end principle will guide where intelligence should reside — at the edge, in the network, or at the origin. The hourglass model's lesson — that universal, minimal interoperation layers enable unbounded innovation above — will inform protocol design for ambient and spatial computing. Cryptographic trust, and the ongoing tension between centralised and decentralised models, will shape identity, payments, and content authenticity in the AI-generated media landscape. The web technologies you have learned in IT107 are not merely today's tools; they are expressions of enduring architectural principles. Master the principles, and you will master whatever technologies the future builds upon them.

### Required Reading

- W3C Ambient Web Working Group. "Ambient Web Architecture." First Public Working Draft, 2040.
- UoY Nordic Ambient Computing Lab (2040). *Landvættir: Place-Aware Computing and the Re-Enchantment of Space*.
- Russell, S. (2039). "Provably Beneficial Autonomous Infrastructure." *Communications of the ACM*, 82(3).
- Berners-Lee, T. (2035). "Reflections on 45 Years of the Web: What I Got Wrong and What Endures." Keynote, WWW2035.
- Course lecture notes and required readings from Lectures 1-11. [Cumulative synthesis]

### Discussion Questions

1. If AI models become foundational to the web stack, who controls the models? What are the centralisation and monoculture risks?
2. Ambient computing dissolves the boundary between the web and the physical world. What new privacy and security threats does this create?
3. Autonomous infrastructure promises to eliminate toil, but what happens when autonomous systems make decisions that conflict with human values? How do we encode ethical constraints into self-governing infrastructure?

---

## Final Examination Preparation

### Examination Format

The final examination for IT107 consists of two parts:

**Part A: Written Examination (60%)** — Choose 4 of the following 8 essay questions. Each essay should demonstrate command of the technical material, ability to synthesise across lectures, and critical thinking about trade-offs and design decisions. Each essay: 500-750 words.

**Part B: Architecture Analysis (40%)** — You will be given a scenario describing a web service with specific requirements (latency, security, scale, client diversity). Analyse the scenario and produce: (1) a protocol stack recommendation with justification, (2) an API design (choose REST/GraphQL/gRPC and justify), (3) an authentication architecture, (4) a performance budget with monitoring strategy, and (5) identification of the three most significant operational risks. Maximum 2000 words.

### Essay Questions (Choose 4 of 8)

1. **The End-to-End Principle at Mid-Century:** The end-to-end principle has been "violated" by CDNs, TLS-terminating proxies, NAT, and edge computing. Is the principle still useful as a design guide, or has it become a historical relic? Argue for or against its continued relevance, citing specific technologies from the course.

2. **QUIC and the Future of Transport:** QUIC moves transport-layer functionality from the kernel to userspace and integrates TLS by default. Analyse the implications of this shift for: (a) protocol innovation velocity, (b) network management and observability, and (c) the OSI layering model. Is QUIC the future, or a transitional technology?

3. **DNS as Critical Infrastructure:** DNS is simultaneously the internet's most essential service and one of its most vulnerable. Evaluate the current state of DNS security (DNSSEC, encrypted DNS, ODoH) and propose a 2040 DNS architecture that balances security, privacy, performance, and operational practicality.

4. **API Paradigm Selection Framework:** A multinational bank is designing a new digital platform that must serve: web browsers, mobile apps, third-party fintech integrations, and internal microservices — all with strong consistency guarantees and regulatory compliance. Select the API paradigm(s) you would use for each consumer and justify your choices with reference to the trade-offs discussed in this course.

5. **The Browser as Operating System:** The browser now provides GPU compute (WebGPU), native-performance execution (WebAssembly/WASI), offline capabilities (Service Workers), and hardware authentication (WebAuthn). Argue whether the browser has become a legitimate operating system. What does this mean for traditional OS platforms?

6. **Authentication in a Passwordless World:** Passkeys (FIDO2/WebAuthn) are phishing-resistant and more usable than passwords, but they create account recovery challenges and tie identity to platform ecosystems. Critically evaluate the passkey paradigm. What problems does it solve, what new problems does it create, and how should service providers design recovery flows?

7. **Edge Computing and the CAP Theorem:** Edge computing platforms promise low latency by running computation close to users, but global state synchronisation introduces consistency challenges. Analyse edge computing through the lens of the CAP theorem. What consistency guarantees are achievable, and for what use cases are they sufficient?

8. **The AI-Native Web:** Machine learning is being integrated into every layer of the web stack — from congestion control to content generation to security monitoring. Analyse the risks of AI monoculture in web infrastructure. What happens when millions of sites use the same ML model for critical functions, and that model exhibits a systemic failure?

### Recommended Study Approach

1. **Re-read all lecture notes**, focusing on the "Discussion Questions" at the end of each lecture — the essay questions build on these themes.
2. **Prepare outlines** for 5-6 of the essay questions; you will only write 4, but preparing more gives you flexibility.
3. **Practice architecture analysis**: take any web service you use regularly and sketch its protocol stack, API design, auth flow, and performance characteristics.
4. **Review the RFCs**: RFC 9000 (QUIC), RFC 9110-9114 (HTTP), RFC 8446 (TLS 1.3) are particularly exam-relevant.
5. **Form a study group** and debate the discussion questions — the examination rewards synthesis and critical thinking, not memorisation.

---

*IT107 Web Technologies & Internet Architecture — woven by Runa Gridweaver Freyjasdottir for the University of Yggdrasil, 2040. May this knowledge serve the infrastructure that connects the Nine Realms.*
