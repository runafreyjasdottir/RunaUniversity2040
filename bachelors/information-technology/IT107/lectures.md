# IT107: Web Technologies & Internet Architecture
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4  
**Description:** Web Technologies & Internet Architecture

---

## Lectures

ᚠ **Lecture 1: The Internet as Infrastructure: History, Governance, and the Physical Layer**

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

The internet is not a cloud but a physical infrastructure of cables, routers, data centers, and satellites. This opening lecture establishes the material reality of internet architecture, tracing its evolution from ARPANET (1969) to the 2040 global mesh. Students will learn the organizational structures that govern the internet—the IETF, ICANN, RIRs, and the emerging supranational bodies of the 2030s—and understand how physical geography constrains and shapes digital connectivity.

### Key Topics

- The internet's layered history: ARPANET, NSFNET, the commercial internet, and the 2030s mesh
- Physical infrastructure: submarine cables, fiber backbones, IXPs, and satellite constellations
- Internet governance: IETF standards, ICANN domain management, RIR address allocation
- The 2032 Global Connectivity Treaty: public internet as a utility and digital sovereignty
- Latency, bandwidth, and the speed of light as fundamental constraints

### Lecture Notes

The internet's origin is well-documented: ARPANET, established by the U.S. Department of Defense's Advanced Research Projects Agency in 1969, connected four university computers via 50-kilobit-per-second lines. By 2040, this experimental network has evolved into a planetary nervous system carrying zettabytes annually. Yet the physical substrate remains surprisingly similar: packets traverse copper, fiber, and radio waves; routers switch traffic based on destination addresses; and the speed of light imposes hard limits on round-trip time. The lecture insists on this material foundation, countering the tendency to treat the internet as an immaterial "cloud."

The **submarine cable network** carries approximately 99% of intercontinental internet traffic by 2040. The first transatlantic telegraph cable was laid in 1858; the first fiber-optic cable (TAT-8) in 1988; by 2040, there are over 500 submarine cables totaling 1.4 million kilometers. The lecture surveys major cable systems: the **Nordic Bifrost** (2034, connecting Scandinavia to North America with 400 Tbps capacity), the **Arctic Fiber Ring** (2036, exploiting melting ice routes for shorter Europe-Asia paths), and the **Equatorial Mesh** (2038, connecting Africa, South America, and Southeast Asia). Each cable landing point is a geopolitical chokepoint: the 2031 *Lisbon Cable Incident*, in which an anchor strike severed three cables simultaneously, caused 40% traffic loss between Europe and Africa for 72 hours.

**Internet Exchange Points (IXPs)** are the local markets of the internet—physical locations where networks peer and exchange traffic without intermediate transit. The largest IXPs (AMS-IX in Amsterdam, DE-CIX in Frankfurt, LINX in London) handle terabits per second of traffic. By 2040, **distributed IXPs** have emerged in smaller cities, enabled by software-defined networking (SDN) that virtualizes peering infrastructure. The UoY **Trondheim IXP** (2035) exemplifies this trend: a regionally operated exchange serving Northern Europe with 50 Tbps capacity, reducing dependency on distant major hubs.

**Internet governance** has evolved from U.S.-centric control to a multistakeholder model with increasing government oversight. The **IETF** (Internet Engineering Task Force) remains the primary standards body, producing RFCs through rough consensus and running code. **ICANN** (Internet Corporation for Assigned Names and Numbers) manages the DNS root zone and IP address allocation, though its authority has been challenged by the 2032 *Global Connectivity Treaty*, which established the **International Digital Commons Authority (IDCA)** to oversee critical internet resources as global public goods. The lecture covers the tension between the IETF's technical libertarianism and national governments' demands for digital sovereignty, content filtering, and data localization.

The **2032 Global Connectivity Treaty** was a watershed moment, signed by 142 nations. It declared internet access a fundamental human right, mandated net neutrality for public infrastructure, and established the IDCA to manage the DNS root as a global commons rather than a U.S.-contracted function. The treaty also addressed **digital sovereignty**: nations gained the right to require data localization for sensitive categories (health, finance, government) while agreeing not to fragment the global routing table. By 2040, the treaty has been implemented unevenly—some nations enforce strict localization, others maintain open borders—but the principle of internet-as-utility is broadly accepted.

### Required Reading

- Abbate, J. (1999). *Inventing the Internet*. MIT Press. Chapters 1–3.
- Blum, A. (2012). *Tubes: A Journey to the Center of the Internet*. Ecco. Chapters 4–6.
- Submarine Cable Map (2040). *TeleGeography Submarine Cable Map*. Interactive atlas.
- Global Connectivity Treaty (2032). *Treaty on the International Status of the Internet*. United Nations Treaty Series, vol. 2891.
- Yggdrasil Infrastructure Lab (2035). "The Trondheim IXP: Distributed Peering in the 2030s." *UoY Network Research Report* 2035-02.

### Discussion Questions

1. The internet's physical infrastructure is concentrated in a small number of cable landing points and IXPs. Does this concentration create unacceptable systemic risk, or is it an efficient specialization?
2. The 2032 Global Connectivity Treaty established internet access as a human right but allows data localization. Is this compromise sustainable, or will localization requirements eventually fragment the global internet?
3. The IETF's motto is "rough consensus and running code." In an era of AI-generated code, does "running code" still serve as a valid consensus criterion?
4. The Arctic Fiber Ring exploits climate change (melting ice) to create shorter cable routes. What ethical tensions arise when infrastructure development benefits from environmental harm?

### Practice Problems

- Calculate the theoretical minimum round-trip time between Oslo and Tokyo via submarine fiber (assume great-circle distance, fiber path 1.2× longer, refractive index 1.5). Compare this to actual measured latency from traceroute data and account for the difference.
- Research the submarine cables serving your region. Map their landing points, capacities, and ownership. Identify single points of failure in the regional connectivity graph.

---

ᚢ **Lecture 2: DNS: The Distributed Database That Names the World**

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

The Domain Name System (DNS) is simultaneously a distributed database, a hierarchical naming convention, and the most critical piece of infrastructure that users never see. This lecture explores DNS from root to leaf: the namespace hierarchy, zone delegation, record types, resolution algorithms, security extensions (DNSSEC), and the emerging privacy-preserving protocols of the 2030s.

### Key Topics

- DNS namespace: root zone, TLDs, second-level domains, and subdomains
- Resolution process: recursive resolvers, iterative queries, and caching
- Record types: A, AAAA, MX, TXT, CNAME, NS, SOA, PTR, and SRV
- DNSSEC: chain of trust, ZSK/KSK, and the root signing ceremony
- DNS privacy: DoH, DoT, Oblivious DNS, and the tension with filtering

### Lecture Notes

Paul Mockapetris's design of DNS in 1983 solved the scaling problem of early internet name services by distributing authority. Rather than a single host file maintained centrally, DNS delegates naming authority hierarchically: the root zone delegates `.com`, `.com` delegates `example.com`, and `example.com` delegates `www.example.com`. This delegation is not merely administrative; it is encoded in the protocol itself via NS (Name Server) records and glue records. By 2040, the DNS namespace has expanded to include over 1,500 top-level domains, internationalized domain names (IDNs) in Unicode scripts, and specialized TLDs for cities, brands, and communities.

The **resolution process** begins with a stub resolver on the user's device, which forwards queries to a recursive resolver (typically operated by the ISP, a public DNS service like Cloudflare or Quad9, or a local resolver like Unbound). The recursive resolver performs **iterative queries**: it asks the root servers for the `.com` nameservers, asks the `.com` nameservers for the `example.com` nameservers, and asks the `example.com` nameservers for the `www` record. Each step may be **cached**: positive answers are cached for their TTL (Time To Live), negative answers (NXDOMAIN) may be cached for a shorter period. The lecture traces a complete resolution with `dig +trace`, showing each query and response.

**DNS record types** encode different kinds of information in the namespace. **A** and **AAAA** records map names to IPv4 and IPv6 addresses. **MX** records specify mail servers with priority values. **TXT** records hold arbitrary text, increasingly used for verification (domain ownership for SSL certificates, SPF for email authentication, DKIM for cryptographic email verification). **CNAME** records create aliases but introduce complexity (a CNAME cannot coexist with other records at the same name). **NS** records delegate zones. **SOA** records define zone parameters (serial number, refresh interval, retry interval, expiry, and minimum TTL). **PTR** records implement reverse DNS (IP address to name). **SRV** records specify services by protocol and port, used for VoIP, XMPP, and Active Directory. By 2040, new record types have been added: **HTTPS** (SVCB/HTTPS, specifying HTTPS service endpoints and Encrypted Client Hello parameters) and **NFT** (Name-Function Translation, mapping names to serverless function endpoints).

**DNSSEC (DNS Security Extensions)** adds cryptographic authentication to DNS responses, preventing cache poisoning and spoofing. DNSSEC signs zone data with a **Zone Signing Key (ZSK)**, which is signed by a **Key Signing Key (KSK)**. The KSK's hash is published in the parent zone as a **DS (Delegation Signer)** record, creating a chain of trust from the root. The **root signing ceremony**, conducted quarterly at secure facilities in the U.S. and Europe, generates and distributes the root zone's KSK. By 2040, DNSSEC is deployed for 85% of TLDs and 60% of second-level domains, but validation by recursive resolvers remains incomplete due to performance concerns and the complexity of key rollover. The lecture covers the 2033 *KSK Rollover Incident*, in which a mismanaged rollover in the `.org` zone caused 12 hours of validation failures.

**DNS privacy** has become a major concern as DNS queries reveal browsing behavior. **DNS over HTTPS (DoH)**, standardized in RFC 8484 (2018), encrypts DNS queries within HTTPS connections, hiding them from network observers. **DNS over TLS (DoT)**, standardized in RFC 7858 (2016), encrypts queries over TLS on port 853. By 2040, DoH is the dominant privacy protocol, supported by all major browsers and operating systems. However, DoH centralizes trust in the DNS resolver (typically Cloudflare or Google), creating a new privacy risk. **Oblivious DNS (ODNS)**, developed by Paul Schmitt and colleagues (2030), separates the query sender from the resolver using a proxy, preventing any single party from linking queries to identities. The 2034 *Yggdrasil Privacy DNS* deployment uses ODNS for all campus queries, demonstrating practical privacy-preserving resolution at scale.

### Required Reading

- Mockapetris, P. (1987). *Domain Names — Concepts and Facilities*. RFC 1034. IETF.
- Mockapetris, P. (1987). *Domain Names — Implementation and Specification*. RFC 1035. IETF.
- Arends, R., et al. (2005). *DNS Security Introduction and Requirements*. RFC 4033. IETF.
- Hoffman, P., & McManus, P. (2018). *DNS over HTTPS (DoH)*. RFC 8484. IETF.
- Schmitt, P., et al. (2030). "Oblivious DNS: Practical Privacy for DNS Queries." *ACM CCS*, 2030.

### Discussion Questions

1. DNS is a distributed database but relies on centralized trust (the root zone). Is this tension resolvable, or is some centralization inherent to hierarchical naming?
2. DNSSEC validation adds latency to every query. For a high-traffic web application, what caching strategies can minimize this overhead without sacrificing security?
3. DoH encrypts DNS queries but centralizes trust in the resolver. Is the privacy gain from encrypting queries worth the privacy loss from centralizing trust?
4. The 2033 KSK Rollover Incident caused 12 hours of validation failures. What procedural and technical safeguards could prevent similar incidents during future key rollovers?

### Practice Problems

- Configure a local Unbound resolver with DNSSEC validation. Query a signed domain and an unsigned domain, capturing the AD (Authentic Data) bit and analyzing the validation chain.
- Implement a simple stub resolver in Python that sends UDP queries to a recursive resolver, parses the response, and extracts A records. Handle truncated responses by falling back to TCP.

---

ᚦ **Lecture 3: HTTP and the Web: Methods, Status Codes, Headers, and Semantics**

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

HTTP is the protocol of the web, yet it is often misunderstood as merely a transport mechanism. This lecture treats HTTP as an application-level protocol with rich semantics, exploring its methods, status codes, headers, caching model, and evolution from HTTP/1.1 through HTTP/2 to HTTP/3. By 2040, HTTP remains the universal API protocol, though its implementations have grown significantly more sophisticated.

### Key Topics

- HTTP methods: GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS, and their idempotency
- Status codes: 1xx informational, 2xx success, 3xx redirection, 4xx client error, 5xx server error
- Headers: Content-Type, Authorization, Cache-Control, ETag, and custom headers
- Caching: cache keys, validation, expiration, and surrogate caches (CDNs)
- HTTP/2 multiplexing, server push (deprecated), and HTTP/3 QUIC transport

### Lecture Notes

Tim Berners-Lee's original HTTP protocol (1991) was trivial: a client sent a GET request with a path, and the server returned the requested document. By 2040, HTTP has evolved into a complex protocol with dozens of methods, hundreds of headers, and multiple transport mappings. Yet the core semantics remain: HTTP is a request-response protocol in which clients send messages to servers, which return responses indicating success or failure. Understanding these semantics is essential for debugging, API design, and infrastructure operations.

**HTTP methods** define the intended action on a resource. **GET** retrieves a representation; it must be safe (no side effects) and idempotent (multiple identical requests produce the same result). **POST** submits data to be processed; it is neither safe nor idempotent. **PUT** replaces a resource entirely; it is idempotent. **DELETE** removes a resource; it is idempotent. **PATCH** applies partial modifications; idempotency depends on the patch document. **HEAD** is identical to GET but returns headers only. **OPTIONS** returns supported methods. The lecture emphasizes idempotency: network retries make it likely that the same request will be sent multiple times, and idempotent methods handle this gracefully. The 2031 *Duplicate Charge Incident*, in which a non-idempotent POST for payment processing was retried after a timeout, cost a merchant $2.3 million in duplicate transactions.

**Status codes** communicate the outcome of a request. The 2xx class indicates success: 200 OK, 201 Created, 204 No Content. The 3xx class indicates redirection: 301 Moved Permanently, 302 Found, 304 Not Modified. The 4xx class indicates client errors: 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests. The 5xx class indicates server errors: 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable, 504 Gateway Timeout. The lecture covers each code's semantics, when to use it, and common misuses (e.g., using 401 for authentication failures when it technically means "unauthenticated"; using 500 for predictable business logic errors). By 2040, the IETF has added 418 I'm a Teapot (RFC 2324, 1998, reaffirmed 2035 as an official Easter egg) and 451 Unavailable For Legal Reasons (RFC 7725, 2016).

**HTTP headers** carry metadata about requests and responses. **Content-Type** declares the media type (MIME type) of the body. **Authorization** carries credentials (Basic, Bearer, Digest). **Cache-Control** directives manage caching behavior (max-age, no-cache, no-store, must-revalidate). **ETag** provides an opaque identifier for cache validation (conditional requests with If-None-Match return 304 if the ETag matches). **CORS headers** (Access-Control-Allow-Origin, etc.) manage cross-origin resource sharing. By 2040, custom headers proliferate in API design, but the lecture warns against header bloat: each header adds bytes to every request, and excessive headers can exceed TCP initial congestion window limits, adding a round trip.

**HTTP caching** reduces latency and server load by storing responses near clients. The lecture covers cache keys (method + URI + Vary headers), cache hierarchies (browser cache, CDN cache, reverse proxy cache, origin server), and validation mechanisms (If-Modified-Since with Last-Modified, If-None-Match with ETag). **Surrogate caches** (CDNs) act on behalf of the origin server, serving cached content from edge locations. By 2040, **cache tagging** (pioneered by Fastly and standardized in RFC 9211, 2032) enables fine-grained cache invalidation: rather than purging by URL, operators purge by tag (e.g., "all product pages" or "all pages referencing user 12345"), dramatically improving cache hit ratios for dynamic content.

**HTTP/2** (RFC 7540, 2015) introduced binary framing, multiplexing (multiple requests on a single TCP connection), header compression (HPACK), and server push (deprecated in 2030 due to complexity and misuse). **HTTP/3** (RFC 9114, 2022) replaces TCP with QUIC (a UDP-based transport with built-in encryption and connection migration), eliminating head-of-line blocking. By 2040, HTTP/3 dominates public web traffic (85% of requests), with HTTP/2 persisting in internal networks. The lecture analyzes the performance implications: HTTP/3 reduces latency on lossy networks (mobile, satellite) but adds CPU overhead due to QUIC's user-space implementation. For high-throughput data centers, HTTP/2 with kernel-bypass networking (DPDK, RDMA) remains competitive.

### Required Reading

- Berners-Lee, T. (1991). *The Original HTTP as Implemented in WorldWideWeb*. CERN.
- Fielding, R. T., et al. (2014). *Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content*. RFC 7231. IETF.
- Belshe, M., Peon, R., & Thomson, M. (2015). *Hypertext Transfer Protocol Version 2 (HTTP/2)*. RFC 7540. IETF.
- Bishop, M. (2022). *HTTP/3*. RFC 9114. IETF.
- Yggdrasil Performance Lab (2032). "HTTP/3 Adoption at Scale: Performance, CPU, and Operational Lessons." *UoY Network Research Report* 2032-07.

### Discussion Questions

1. HTTP methods have well-defined semantics, but APIs often misuse them (e.g., using POST for deletion). Does semantic correctness matter if the API is well-documented and consistent in its misuse?
2. The 418 I'm a Teapot status code was an April Fools' joke that became an RFC. Does its formalization honor internet culture, or does it undermine the protocol's seriousness?
3. Cache tagging enables precise invalidation but requires applications to tag responses proactively. What organizational processes are necessary to ensure consistent tagging across development teams?
4. HTTP/3's QUIC transport eliminates head-of-line blocking but increases CPU usage. For a data center serving 1 million requests per second, is the latency reduction worth the computational overhead?

### Practice Problems

- Use `curl` to issue HTTP requests with different methods and headers. Capture and analyze the request and response headers, documenting the cache behavior (Cache-Control, ETag, Last-Modified) of a major website.
- Configure an Nginx server with HTTP/2 and HTTP/3 support. Benchmark throughput and latency under packet loss conditions (using `tc` to simulate loss) and compare the protocols' resilience.

---

ᚨ **Lecture 4: TLS and HTTPS: Cryptographic Foundations of Trust**

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Transport Layer Security (TLS) is the cryptographic backbone of the modern internet, protecting web traffic, APIs, and messaging from eavesdropping and tampering. This lecture covers TLS from the handshake through the record layer: cipher suites, certificate infrastructure, protocol versions, and the post-quantum transition of the 2030s. By 2040, TLS 1.4 with hybrid post-quantum key exchange is mandatory for all public-facing services.

### Key Topics

- TLS handshake: key exchange, authentication, and session resumption
- Certificates: X.509, chain validation, revocation (CRL, OCSP, OCSP Stapling)
- Cipher suites: symmetric encryption, MAC, and key exchange algorithms
- Certificate transparency: logs, monitors, and the CT ecosystem
- Post-quantum TLS: hybrid key exchange with CRYSTALS-Kyber and Dilithium

### Lecture Notes

The need for TLS became apparent in the mid-1990s as e-commerce emerged and plaintext HTTP exposed credit card numbers and passwords. Netscape developed SSL (Secure Sockets Layer) in 1994; TLS 1.0 standardized it in 1999. By 2040, TLS has evolved through versions 1.0, 1.1, 1.2, 1.3 (2018), and 1.4 (2031), with each version addressing vulnerabilities and improving performance. The lecture traces this evolution, emphasizing that TLS is not merely "encryption" but a comprehensive security protocol providing confidentiality, integrity, and authentication.

The **TLS handshake** establishes a secure channel. In TLS 1.3 (the baseline for 2040 understanding), the handshake requires one round trip (1-RTT) for new connections and zero round trips (0-RTT) for resumed connections. The client sends a ClientHello with supported cipher suites and key shares; the server responds with ServerHello, its certificate, and an encrypted ServerFinished; the client verifies the certificate, generates session keys, and sends ClientFinished. The lecture walks through each message, explaining the cryptography: ephemeral Diffie-Hellman key exchange (X25519 or P-256), RSA or ECDSA certificate authentication, and AES-GCM or ChaCha20-Poly1305 record encryption.

**X.509 certificates** bind public keys to identities. A certificate contains: the subject (domain name), issuer (Certificate Authority), public key, validity period, serial number, and extensions (Subject Alternative Names for multi-domain certificates, Key Usage for permitted operations). **Chain validation** verifies that the leaf certificate is signed by an intermediate CA, which is signed by a root CA, which is trusted by the client (pre-installed in operating system trust stores). **Revocation** checks whether a certificate has been invalidated before expiry: **CRL** (Certificate Revocation Lists, downloaded periodically) and **OCSP** (Online Certificate Status Protocol, queried per certificate). **OCSP Stapling** (RFC 6961) has the server attach a timestamped OCSP response, eliminating client-side OCSP queries and their associated privacy leaks. By 2040, **OCSP Must-Staple** is mandatory for UoY services, and **short-lived certificates** (24-hour validity, automated via ACME) are the default, reducing the impact of compromise.

**Certificate Transparency (CT)**, introduced after the 2011 DigiNotar compromise (in which a Dutch CA was hacked and issued fraudulent certificates for major domains), requires that all certificates be logged in public, append-only logs. **CT logs** (operated by Google, Cloudflare, and independent operators) record every issued certificate; **monitors** scan logs for unauthorized issuance; and **auditors** verify that logs remain consistent and append-only. By 2040, CT has prevented multiple attempted compromises and is legally mandated in the EU and North America. The lecture demonstrates querying a CT log for certificates issued to a domain, revealing subdomains and certificate history.

**Post-quantum TLS** is the defining security challenge of the 2030s. Shor's algorithm (1994) proves that quantum computers can break RSA and elliptic curve cryptography, rendering TLS vulnerable to "harvest now, decrypt later" attacks. The NIST post-quantum cryptography standardization (2016–2024) produced CRYSTALS-Kyber (key encapsulation) and CRYSTALS-Dilithium (digital signatures). TLS 1.4 (2031) mandates **hybrid key exchange**: classical X25519 plus post-quantum Kyber, ensuring security even if one algorithm is broken. The lecture covers the deployment challenges: Kyber public keys are 1,568 bytes (vs. 32 bytes for X25519), increasing handshake size; Dilithium signatures are 2,420 bytes (vs. 64 bytes for ECDSA), increasing certificate chain size. By 2040, these overheads are manageable with optimized implementations, but the transition required years of coordinated effort across browsers, servers, and CAs.

### Required Reading

- Rescorla, E. (2018). *The Transport Layer Security (TLS) Protocol Version 1.3*. RFC 8446. IETF.
- Rescorla, E. (2031). *The Transport Layer Security (TLS) Protocol Version 1.4*. RFC 9420. IETF.
- Cooper, D., et al. (2008). *Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile*. RFC 5280. IETF.
- Laurie, B., et al. (2033). *Certificate Transparency Version 3.0*. RFC 9562. IETF.
- NIST (2024). *Post-Quantum Cryptography Standardization: Selected Algorithms*. NISTIR 8547.

### Discussion Questions

1. TLS 1.3 eliminated RSA key exchange in favor of ephemeral Diffie-Hellman, providing forward secrecy. Should forward secrecy be mandatory for all TLS connections, or are there legitimate use cases for static RSA (e.g., passive monitoring by security appliances)?
2. Short-lived certificates (24-hour validity) reduce the impact of compromise but increase automation dependency. What are the systemic risks if the ACME infrastructure (Let's Encrypt, etc.) experiences prolonged outage?
3. Certificate Transparency prevents unauthorized issuance but creates a public database of all certificates, revealing infrastructure details. Is this transparency worth the reconnaissance value it provides to attackers?
4. Hybrid post-quantum key exchange uses both classical and post-quantum algorithms. If a quantum computer breaks the classical algorithm, does the hybrid still provide security, or does the weakest link principle apply?

### Practice Problems

- Use OpenSSL to inspect a website's certificate chain. Verify the chain manually: extract the leaf, intermediate, and root certificates; confirm the signatures; check the validity period; and query OCSP for revocation status.
- Capture a TLS 1.3 handshake with Wireshark. Identify the ClientHello, ServerHello, certificate message, and key exchange. Measure the handshake latency and compare it to a TLS 1.2 handshake on the same server.

---

ᚱ **Lecture 5: Web Servers and Reverse Proxies: Nginx, Apache, and Caddy in 2040**

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Web servers are the front door of internet services. This lecture covers the architecture, configuration, and operational concerns of the three dominant web server platforms in 2040: Nginx, Apache httpd, and Caddy. Students will learn to configure virtual hosts, SSL termination, load balancing, rate limiting, and request routing, with attention to performance tuning and security hardening.

### Key Topics

- Web server architecture: process-based, thread-based, and event-driven models
- Nginx: reverse proxy, load balancing, SSL termination, and Lua scripting
- Apache httpd: .htaccess, modules, and the transition to event MPM
- Caddy: automatic HTTPS, JSON configuration, and the Caddyfile
- Performance tuning: connection pools, buffer sizes, worker processes, and kernel parameters

### Lecture Notes

The web server's role has evolved from file server to application gateway. In 1995, Apache httpd served static HTML files from disk. By 2040, web servers terminate SSL, route requests to backend applications, cache responses, enforce rate limits, and inject security headers—often without ever touching a filesystem. Understanding this evolution is essential for IT professionals who must configure, debug, and scale these critical components.

**Web server architectures** fall into three categories. **Process-based** servers (Apache prefork MPM) spawn a new process for each connection, providing isolation but consuming significant memory. **Thread-based** servers (Apache worker MPM) use threads within processes, reducing memory overhead but introducing shared-state complexity. **Event-driven** servers (Nginx, Caddy, Apache event MPM) use a small number of worker processes that handle many connections via non-blocking I/O and event loops (epoll on Linux, kqueue on BSD). By 2040, event-driven architectures dominate production due to their memory efficiency and scalability to millions of concurrent connections.

**Nginx**, released by Igor Sysoev in 2004, is the dominant web server and reverse proxy by 2040, serving approximately 40% of all websites. Its configuration uses a declarative language organized into contexts (main, events, http, server, location). The lecture covers essential directives: `server` (virtual host definition), `location` (URI matching and handler selection), `proxy_pass` (reverse proxy to backends), `ssl_certificate` and `ssl_certificate_key` (TLS configuration), `limit_req` (rate limiting), and `add_header` (security headers). Nginx's `ngx_http_lua_module` enables Lua scripting for dynamic request processing, though by 2040, this has been largely superseded by application-layer logic in WebAssembly modules.

**Apache httpd**, the original dominant web server (released 1995), remains relevant in 2040 due to its module ecosystem and `.htaccess` capability (per-directory configuration without server reload). The lecture covers Apache's Multi-Processing Modules (MPMs): prefork (process-based), worker (thread-based), and event (event-driven, default since Apache 2.4). Apache's configuration uses directives in a hierarchical structure, with modules providing additional functionality (mod_ssl, mod_rewrite, mod_proxy, mod_cache). The 2030s saw Apache's resurgence in enterprise environments due to its mature WebSocket proxying and gRPC support via mod_h2.

**Caddy**, released in 2015 by Matthew Holt, introduced two innovations that reshaped the industry: **automatic HTTPS** (obtaining and renewing certificates via ACME without manual configuration) and **dynamic configuration** (reloading without dropping connections). By 2040, Caddy's market share has grown to 15%, particularly in small-to-medium deployments and edge computing. Caddy's configuration uses a Caddyfile (a human-friendly DSL) or JSON (for programmatic management). The lecture demonstrates a complete Caddy configuration: reverse proxy to a backend, automatic HTTPS, header injection, rate limiting, and logging. Caddy's plugin architecture, based on Go modules, enables extensibility without recompilation.

**Performance tuning** requires understanding both the web server and the underlying operating system. Key parameters: **worker processes** (Nginx) or **threads** (Apache) should match CPU cores; **connection pools** to backends prevent connection establishment overhead; **buffer sizes** (send buffer, receive buffer) should be tuned to the network latency and bandwidth; **file descriptors** (ulimit) must be sufficient for concurrent connections; and **kernel parameters** (`net.core.somaxconn`, `tcp_tw_reuse`, `tcp_fastopen`) optimize TCP behavior. The lecture provides a tuning checklist and demonstrates measuring performance with `wrk`, `ab` (Apache Bench), and `h2load` (HTTP/2 benchmarking).

### Required Reading

- Sysoev, I. (2004). *Nginx Documentation*. nginx.org. (Current version for 2040 context.)
- Apache Software Foundation (2040). *Apache HTTP Server Documentation*. httpd.apache.org.
- Holt, M. (2015). *Caddy Documentation*. caddyserver.com. (Current version for 2040 context.)
- Fielding, R. T. (1999). "Performance of HTTP-Based Systems." *Web Protocols and Practice*. Addison-Wesley.
- Yggdrasil Performance Lab (2033). "Web Server Tuning for the 2040s: A Comparative Study of Nginx, Apache, and Caddy." *UoY Systems Research Report* 2033-05.

### Discussion Questions

1. Nginx, Apache, and Caddy each have distinct strengths. For a large enterprise with legacy Apache modules and a small startup with no infrastructure team, which server is appropriate, and why?
2. Automatic HTTPS in Caddy eliminates manual certificate management but creates dependency on ACME infrastructure. Is this trade-off justified, or does it introduce systemic risk?
3. Event-driven servers scale better than process-based servers, but process-based servers provide memory isolation. For a shared hosting environment, does the isolation benefit outweigh the scalability cost?
4. Web servers increasingly perform functions once reserved for application servers (SSL termination, request routing, caching). Where should the boundary between web server and application server be drawn?

### Practice Problems

- Configure Nginx as a reverse proxy for a backend application, with SSL termination, rate limiting, and security headers (HSTS, CSP, X-Frame-Options). Test with `curl` and verify each configuration element.
- Benchmark Nginx, Apache (event MPM), and Caddy serving static files under concurrent load. Measure requests per second, latency percentiles, and memory usage. Document your tuning parameters and justify your choices.

---

ᚲ **Lecture 6: CDNs and Edge Caching: Content Distribution at Scale**

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Content Delivery Networks (CDNs) are the invisible infrastructure that accelerates the web. By caching content at thousands of edge locations worldwide, CDNs reduce latency, absorb traffic spikes, and improve resilience. This lecture covers CDN architecture, cache policies, origin shielding, edge computing, and the emerging paradigm of programmable CDNs that execute code at the edge.

### Key Topics

- CDN architecture: PoPs, edge servers, origin servers, and anycast routing
- Cache policies: TTL, stale-while-revalidate, surrogate keys, and cache hierarchies
- Origin shielding: protecting origins from cache miss floods
- Edge computing: Cloudflare Workers, Fastly Compute@Edge, and WASM at the edge
- Multi-CDN strategies: load balancing across providers for resilience and cost optimization

### Lecture Notes

Akamai launched the first commercial CDN in 1998, using DNS-based redirection to route users to nearby servers. By 2040, the CDN market has consolidated around a few global providers (Cloudflare, Fastly, Akamai, Amazon CloudFront) but also fragmented into specialized providers for video streaming (Netflix Open Connect), gaming (Valve's Steam CDN), and regional content (local providers in Africa and Southeast Asia). The UoY network peers with multiple CDNs, and the lecture uses the university's own CDN deployment as a case study.

**CDN architecture** relies on **Points of Presence (PoPs)**—data centers or server clusters located close to end users. Each PoP contains **edge servers** that cache content from **origin servers** (the customer's infrastructure). **Anycast routing** advertises the same IP address from multiple PoPs, causing users' traffic to be routed to the nearest PoP via BGP shortest-path selection. The lecture traces a user's request: DNS resolution returns an anycast IP, BGP routes to the nearest PoP, the edge server checks its cache, and either serves the cached content or fetches from the origin.

**Cache policies** determine how long content remains in the edge cache and how stale content is handled. The **TTL (Time To Live)**, set by the origin via Cache-Control headers, specifies the maximum cache duration. **Stale-while-revalidate** (RFC 5861) allows serving stale content while fetching fresh content in the background, balancing freshness with availability. **Surrogate keys** (cache tags, RFC 9211) enable purging by logical category rather than URL. The lecture covers cache hierarchy: browser cache (closest, smallest), edge cache (PoP, medium), regional cache (super PoP, large), and origin (source of truth). Each layer uses different TTLs, with shorter TTLs closer to the user to balance freshness and efficiency.

**Origin shielding** protects origin servers from traffic spikes caused by cache misses. Without shielding, a viral event (e.g., a popular news article shared on social media) can cause thousands of edge servers to simultaneously request the same uncached content, overwhelming the origin. An **origin shield** (also called a tiered cache or mid-tier cache) is a designated cache layer between edges and origin that absorbs these miss floods. Only the shield fetches from origin; edges fetch from shield. The lecture analyzes the 2030 *Celebrity Tweet Incident*, in which a single tweet with a link caused 50,000 requests per second to an unshielded origin, resulting in a 4-hour outage.

**Edge computing** transforms CDNs from passive caches to active compute platforms. By 2040, major CDNs support **serverless functions at the edge**: Cloudflare Workers (JavaScript/WASM), Fastly Compute@Edge (Rust/WebAssembly), and Akamai EdgeWorkers (JavaScript). These functions execute in milliseconds at PoPs worldwide, enabling: A/B testing (route users to different origins based on cookies), personalization (inject user-specific content into cached pages), bot detection (analyze request patterns before reaching origin), and API aggregation (combine multiple backend responses into one edge response). The lecture implements a Cloudflare Worker that adds security headers, blocks requests from embargoed countries (geofencing via IP geolocation), and logs requests to a Durable Object for analytics.

**Multi-CDN strategies** distribute traffic across multiple CDN providers to improve resilience (avoiding single-provider outages), optimize cost (selecting the cheapest provider for each region), and enhance performance (routing to the provider with the best latency for each user). The lecture covers **global server load balancing (GSLB)**: DNS-based routing that selects a CDN based on health checks, performance metrics, and business rules. The 2034 *Cloudflare Outage* (a configuration error that blackholed traffic for 30 minutes) motivated many organizations to adopt multi-CDN. The UoY deployment uses a primary CDN (Cloudflare) with automatic failover to a secondary (Fastly) if health checks fail.

### Required Reading

- Nygren, E., et al. (2010). "The Akamai Network: A Platform for High-Performance Internet Applications." *ACM SIGOPS Operating Systems Review*, 44(3), 2–19.
- Cloudflare (2040). *Cloudflare Workers Documentation: Edge Computing Platform*. Cloudflare Docs.
- Fastly (2040). *Compute@Edge Documentation: Rust and WebAssembly at the Edge*. Fastly Docs.
- Fielding, R. T., et al. (2032). *Cache Tagging for Fine-Grained Cache Invalidation*. RFC 9211. IETF.
- Yggdrasil Network Operations (2034). "Multi-CDN Deployment: Lessons from the Cloudflare Outage." *UoY Network Postmortem* 2034-03.

### Discussion Questions

1. Anycast routing sends users to the nearest PoP by BGP shortest path, but "nearest" by AS-path hops may not be nearest by latency. What metrics should CDNs use for PoP selection, and how should they be measured?
2. Edge computing enables serverless functions at PoPs, but these functions have CPU and memory limits (e.g., 128MB, 50ms). For what classes of computation is edge execution appropriate, and when should computation remain at origin?
3. Multi-CDN improves resilience but adds complexity (two configurations, two bills, two monitoring dashboards). For a small organization, is multi-CDN worth the overhead?
4. Origin shielding adds a cache tier, increasing latency for cache misses. Under what traffic patterns does shielding improve overall latency despite this cost?

### Practice Problems

- Configure a CDN (Cloudflare or Fastly) for a static website. Set cache TTLs, enable stale-while-revalidate, and implement cache tagging for a content category. Measure cache hit ratio and time-to-first-byte before and after optimization.
- Write an edge function (Cloudflare Worker or Fastly Compute@Edge) that inspects incoming requests, blocks requests from a specified country, adds security headers, and logs anonymized traffic data. Deploy and test.

---

ᚷ **Lecture 7: WebSockets, gRPC, and Real-Time Protocols**

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

HTTP is request-response, but many applications require persistent, bidirectional communication: chat, gaming, financial trading, and IoT telemetry. This lecture covers the protocols that enable real-time web communication: WebSockets, Server-Sent Events (SSE), gRPC, and MQTT. Students will learn to select the appropriate protocol for each use case, configure infrastructure to support persistent connections, and manage the operational challenges of long-lived sessions.

### Key Topics

- WebSockets: handshake, framing, and full-duplex communication over TCP
- Server-Sent Events (SSE): unidirectional server push over HTTP
- gRPC: HTTP/2-based RPC with Protocol Buffers, streaming, and deadlines
- MQTT: lightweight pub/sub for IoT and mobile messaging
- Operational concerns: connection limits, heartbeat/keepalive, and graceful shutdown

### Lecture Notes

The real-time web emerged in the late 2000s as applications demanded lower latency than HTTP polling could provide. Early solutions—long polling, BOSH, and Comet—were hacks around HTTP's request-response model. By 2040, native protocols have displaced these workarounds, each optimized for specific patterns of real-time communication.

**WebSockets** (RFC 6455, 2011) upgrade an HTTP connection to a persistent, full-duplex TCP channel. The handshake begins with an HTTP request including the `Upgrade: websocket` header; the server responds with `101 Switching Protocols`, and subsequent communication uses a lightweight binary framing protocol. WebSocket frames can carry text or binary payloads, with opcodes for ping/pong (heartbeat), close, and continuation. By 2040, WebSockets are the standard for chat applications, collaborative editing, and gaming, supported by all browsers and most server frameworks. The lecture covers **WebSocket infrastructure**: load balancers must support TCP pass-through or WebSocket-aware proxying; sticky sessions may be required if state is maintained per connection; and heartbeats (ping/pong or application-level keepalives) are essential to detect zombie connections.

**Server-Sent Events (SSE)** provides unidirectional server-to-client push over HTTP. Unlike WebSockets, SSE uses standard HTTP: the server sends a response with `Content-Type: text/event-stream` and writes events as `data: ...\n\n` lines. The client reconnects automatically if the connection drops, using the `Last-Event-ID` header to resume from the last received event. SSE is simpler than WebSockets (no handshake upgrade, no binary framing, works through proxies and firewalls) but limited to server-to-client communication. By 2040, SSE is the default for live updates (sports scores, stock prices, news feeds) where only server push is needed.

**gRPC**, developed by Google and open-sourced in 2015, is an RPC framework built on HTTP/2 and Protocol Buffers. It supports four communication patterns: **unary** (single request, single response), **server streaming** (single request, multiple responses), **client streaming** (multiple requests, single response), and **bidirectional streaming** (multiple requests and responses interleaved). By 2040, gRPC has become the dominant protocol for internal microservices communication, displacing REST in many organizations due to its performance (binary serialization, HTTP/2 multiplexing) and type safety (generated client/server stubs from `.proto` definitions). The lecture covers gRPC infrastructure: HTTP/2 load balancing (required for multiplexed streams), deadlines (client-specified timeouts propagated to all downstream services), and health checking (`grpc.health.v1.Health` service).

**MQTT** (Message Queuing Telemetry Transport), standardized by OASIS in 2014, is a lightweight pub/sub protocol designed for IoT and mobile devices with limited bandwidth and intermittent connectivity. MQTT uses a broker (e.g., Mosquitto, HiveMQ, AWS IoT Core) that receives messages on **topics** (hierarchical strings like `sensors/building3/floor2/temperature`) and forwards them to all subscribers. QoS levels (0 = at most once, 1 = at least once, 2 = exactly once) provide trade-offs between reliability and overhead. By 2040, MQTT is the default for IoT telemetry, smart home devices, and mobile push notifications. The lecture covers MQTT infrastructure: broker clustering for scalability, TLS termination, and ACL (Access Control Lists) for topic-level authorization.

**Operational concerns** for real-time protocols differ fundamentally from HTTP. **Connection limits**: each persistent connection consumes file descriptors and memory; a server handling 100,000 WebSocket connections requires careful tuning (epoll, kernel parameters, application-level connection management). **Heartbeat/keepalive**: TCP connections can remain open indefinitely without data, but NAT gateways, firewalls, and mobile networks may drop idle connections. Protocols implement heartbeats (WebSocket ping/pong, MQTT keepalive) to keep connections alive and detect failures. **Graceful shutdown**: when a server must restart, existing connections must be closed cleanly (sending close frames, allowing in-flight messages to complete) rather than abruptly, which causes client reconnect storms. The lecture covers the **drain pattern**: stop accepting new connections, wait for existing connections to close naturally, then shut down.

### Required Reading

- Fette, I., & Melnikov, A. (2011). *The WebSocket Protocol*. RFC 6455. IETF.
- gRPC Authors (2040). *gRPC Documentation: Core Concepts, Guides, and API Reference*. grpc.io.
- Banks, A., & Gupta, R. (2014). *MQTT Version 3.1.1*. OASIS Standard.
- Yggdrasil Real-Time Systems Lab (2036). "WebSocket at Scale: 100K Connections on a Single Server." *UoY Systems Research Report* 2036-04.
- Yggdrasil IoT Platform (2038). "MQTT Broker Clustering: Scaling to 10 Million Connected Devices." *UoY IoT Research Report* 2038-01.

### Discussion Questions

1. WebSockets provide full-duplex communication but require HTTP/2-aware infrastructure. For a chat application, is the complexity of WebSockets justified, or would SSE with separate HTTP requests for client-to-server messages suffice?
2. gRPC is dominant for internal microservices but rarely used for public APIs. What barriers prevent gRPC adoption for external-facing services, and are they surmountable?
3. MQTT's QoS 2 (exactly once) provides strong delivery guarantees but requires four-way handshakes per message. For a battery-powered IoT sensor, is QoS 2 worth the energy cost?
4. Graceful shutdown with connection draining improves user experience but increases deployment time. For a service that deploys 50 times per day, what drain timeout balances user experience with deployment velocity?

### Practice Problems

- Implement a WebSocket chat server in Python using `websockets` or `asyncio`. Support multiple rooms, user authentication via JWT in the connection URL, and heartbeat ping/pong. Load test with 1,000 concurrent connections.
- Design a gRPC service definition for a distributed key-value store. Define unary and streaming RPCs for Get, Set, and Watch operations. Implement a Python client and server, and benchmark latency under load.

---

ᚹ **Lecture 8: Search Engines and Information Retrieval: From PageRank to Neural Indexing**

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Search engines are the primary interface between users and the web's vast information space. This lecture covers the architecture of modern search engines: crawling, indexing, ranking, and retrieval. By 2040, search has evolved from keyword matching to neural understanding, with large language models interpreting queries and generating synthesized answers. Students will learn the technical foundations of both classical information retrieval and the AI-native search paradigms of the 2030s.

### Key Topics

- Web crawling: politeness, rate limiting, distributed architecture, and robots.txt
- Inverted indices: tokenization, stemming, posting lists, and compression
- Ranking algorithms: TF-IDF, BM25, PageRank, and neural rankers
- Query understanding: intent classification, entity recognition, and semantic matching
- AI-native search: retrieval-augmented generation (RAG), vector search, and answer synthesis

### Lecture Notes

The web's size is difficult to comprehend: by 2040, the indexed web contains over 100 billion pages, with the deep web (databases, private content, dynamic pages) estimated at 500 billion additional documents. Search engines must crawl, index, and rank this corpus in milliseconds, returning relevant results for billions of queries daily. This lecture demystifies the engineering behind this miracle.

**Web crawling** is the process of systematically discovering and fetching web pages. A **crawler** (also called a spider or bot) starts from a seed set of URLs, fetches pages, extracts links, and follows them recursively. Crawlers must be **polite**: they respect `robots.txt` (a file that specifies crawl restrictions), avoid overwhelming servers with requests (rate limiting), and identify themselves via User-Agent strings. Distributed crawlers (e.g., Apache Nutch, Scrapy Cluster) partition URLs across multiple workers, with a **frontier** (queue of URLs to crawl) and a **seen set** (deduplication of already-crawled URLs). By 2040, **crawl freshness** is managed dynamically: news sites are crawled every minute, Wikipedia every hour, static corporate pages every week. The lecture covers the 2032 *Crawl Stampede Incident*, in which a misconfigured crawler requested the same page 10,000 times per second, causing a widespread DDoS.

**Inverted indices** are the data structure that enables fast full-text search. Rather than storing documents as sequences of words (forward index), an inverted index stores a mapping from each word to the list of documents containing it (posting list). The lecture covers index construction: **tokenization** (splitting text into words, handling punctuation and Unicode), **normalization** (lowercasing, removing diacritics), **stemming** (reducing words to root forms, e.g., "running" → "run"), and **stop word removal** (excluding common words like "the" and "and"). Posting lists are compressed using techniques like **gamma coding** and **PForDelta**, achieving compression ratios of 10:1 or better. By 2040, **neural indices** augment traditional inverted indices with dense vector representations, enabling semantic search (finding documents related in meaning, not just keyword match).

**Ranking algorithms** determine the order of results. Classical IR uses **TF-IDF** (term frequency–inverse document frequency) to weight terms by their rarity across the corpus. **BM25** (Best Match 25), a probabilistic retrieval function, improves upon TF-IDF by incorporating document length normalization and saturation. **PageRank** (Brin & Page, 1998) ranks pages by their link graph importance: a page is important if important pages link to it. By 2040, **neural rankers** (BERT-based models, fine-tuned on click data) score query-document pairs by semantic similarity, often outperforming BM25 on natural language queries. The lecture covers **learning to rank**: training models on human relevance judgments (or implicit feedback from clicks) to optimize ranking metrics like nDCG (normalized Discounted Cumulative Gain).

**Query understanding** transforms raw keywords into structured intent. The 2030s saw the maturation of **query intent classification**: identifying whether a query seeks information ("what is DNS"), navigation ("UoY homepage"), transaction ("buy Yggdrasil Chip"), or local services ("neuromorphic computing courses near me"). **Entity recognition** identifies named entities in queries (people, places, organizations) and links them to knowledge graphs. By 2040, **semantic matching** using dense vectors (embeddings) enables search to understand synonyms, paraphrases, and contextual meaning. The lecture demonstrates: the query "jaguar" is ambiguous (animal vs. car vs. operating system), but entity recognition and user context (previous searches, location) resolve the ambiguity.

**AI-native search** represents the paradigm shift of the 2030s. Rather than returning a list of links, AI-native search engines (like the UoY **Mímir-Search** platform, 2037) generate synthesized answers using **Retrieval-Augmented Generation (RAG)**: the system retrieves relevant documents from the index, passes them to a large language model, and prompts the model to generate an answer grounded in the retrieved content. This approach reduces hallucination (compared to pure LLM generation) and provides citations. **Vector search** (using approximate nearest neighbor algorithms like HNSW and FAISS) retrieves semantically similar documents even without keyword overlap. The lecture covers the architecture of a RAG-based search engine: query embedding, vector retrieval, re-ranking, context assembly, and answer generation.

### Required Reading

- Brin, S., & Page, L. (1998). "The Anatomy of a Large-Scale Search Engine." *WWW Conference*.
- Robertson, S., & Zaragoza, H. (2009). "The Probabilistic Relevance Framework: BM25 and Beyond." *Foundations and Trends in Information Retrieval*, 3(4), 333–389.
- Devlin, J., et al. (2019). "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." *NAACL*, 4171–4186.
- Lewis, P., et al. (2021). "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." *NeurIPS*, 33, 9459–9474.
- Yggdrasil Search Lab (2037). "Mímir-Search: RAG-Based Neural Search for Academic Knowledge." *UoY Information Retrieval Report* 2037-06.

### Discussion Questions

1. Web crawling is inherently aggressive—crawlers consume server resources without providing direct value. What ethical obligations do crawlers have to website operators, and how should politeness be enforced?
2. Neural rankers outperform BM25 on natural language queries but are opaque and computationally expensive. For a search engine serving 1 billion queries per day, what is the appropriate balance between neural and classical ranking?
3. RAG-based search generates answers rather than returning links. Does this shift from "search" to "answer" reduce users' information literacy by eliminating the need to evaluate sources?
4. Vector search enables semantic retrieval but struggles with exact matches (e.g., error codes, part numbers). How should hybrid search systems combine keyword and vector retrieval?

### Practice Problems

- Implement a simple inverted index in Python. Tokenize a corpus of documents, build posting lists, and implement boolean AND/OR queries. Measure query latency and index size.
- Build a RAG-based question-answering system using an open-source vector database (e.g., Chroma, Milvus) and a local LLM. Index a set of documents, then answer questions using retrieved context. Evaluate answer accuracy against a ground-truth set.

---

ᚺ **Lecture 9: Web Security: XSS, CSRF, CSP, and the Modern Threat Landscape**

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

The web is the most attacked surface in computing. This lecture covers the vulnerability classes that have plagued web applications for decades and the defenses that mitigate them in 2040. Students will learn to identify, exploit (in controlled environments), and remediate common web vulnerabilities, with attention to modern threats like supply chain attacks, prototype pollution, and AI-generated exploit code.

### Key Topics

- XSS: reflected, stored, and DOM-based cross-site scripting
- CSRF: cross-site request forgery and token-based defense
- Injection: SQL, command, LDAP, and template injection
- Security headers: CSP, HSTS, X-Frame-Options, and Permission-Policy
- Modern threats: supply chain attacks, prototype pollution, and AI exploit generation

### Lecture Notes

Web security is a race between attackers and defenders, with the attackers often holding the advantage because they need find only one vulnerability, while defenders must secure every surface. By 2040, the fundamental vulnerability classes identified in the early 2000s—XSS, CSRF, injection—remain relevant, though their exploitation has evolved with web technology. New classes have emerged: prototype pollution (2018), supply chain attacks (2020s), and AI-assisted exploitation (2030s).

**Cross-Site Scripting (XSS)** occurs when an attacker injects malicious scripts into web pages viewed by other users. **Reflected XSS** embeds the payload in a URL (e.g., `https://example.com/search?q=<script>alert(1)</script>`); the server reflects the input in the response without sanitization. **Stored XSS** persists the payload in the database (e.g., a comment field that displays unescaped HTML). **DOM-based XSS** manipulates the page's Document Object Model via client-side JavaScript (e.g., `document.write(location.hash)`). Defenses: **output encoding** (escape HTML entities before rendering user input), **Content Security Policy (CSP)** (restrict script sources), and **template auto-escaping** (modern frameworks like React, Vue, and Angular escape output by default). By 2040, **trusted types** (a browser API that requires explicit sanitization before assigning to dangerous DOM sinks) provide an additional defense layer.

**Cross-Site Request Forgery (CSRF)** tricks a user's browser into performing unwanted actions on a site where the user is authenticated. For example, an attacker embeds `<img src="https://bank.com/transfer?to=attacker&amount=1000">` on a malicious page; the browser sends the request with the user's cookies, and the bank executes the transfer. Defense: **CSRF tokens** (unpredictable values included in forms and validated by the server), **SameSite cookies** (cookies marked `SameSite=Strict` or `Lax` are not sent with cross-site requests), and **referer validation** (checking the Origin or Referer header). By 2040, **SameSite=Lax** is the browser default, eliminating most CSRF vectors without developer intervention.

**Injection attacks** occur when untrusted data is interpreted as code. **SQL injection** (covered in IT105, Lecture 8) remains prevalent despite decades of awareness. **Command injection** passes user input to shell commands without sanitization. **LDAP injection** manipulates directory queries. **Template injection** occurs when user input is embedded in server-side templates (Jinja2, Twig) and executed. The lecture demonstrates each attack class with concrete examples and emphasizes that **parameterized queries**, **allowlist validation**, and **context-aware encoding** are the universal defenses.

**Security headers** are HTTP directives that harden the browser's security model. **Content Security Policy (CSP)** restricts the sources from which scripts, styles, images, and other resources can load. A strict CSP (`default-src 'self'; script-src 'self'`) prevents inline scripts and external script injection, eliminating most XSS vectors. **HTTP Strict Transport Security (HSTS)** (`Strict-Transport-Security: max-age=31536000; includeSubDomains`) forces HTTPS for a domain and its subdomains. **X-Frame-Options** (`DENY` or `SAMEORIGIN`) prevents clickjacking by restricting iframe embedding. **Permission-Policy** (formerly Feature-Policy) disables browser APIs (camera, microphone, geolocation) that the application does not use, reducing the attack surface. By 2040, the UoY Security Team mandates a minimum set of security headers for all public-facing services, enforced by automated scanning in CI.

**Modern threats** reflect the evolving attack landscape. **Supply chain attacks** compromise dependencies (npm packages, Docker images, CI/CD pipelines) to inject malicious code into applications. The 2031 *Codecov Breach Redux* (in which a malicious Bash uploader script compromised thousands of CI pipelines) demonstrated that build-time dependencies are as critical as runtime code. **Prototype pollution** (JavaScript) modifies the built-in `Object.prototype`, causing unexpected behavior in application code. **AI exploit generation** (2030s) uses large language models to automate vulnerability discovery: given source code, an AI system suggests inputs that trigger buffer overflows, format string bugs, or logic errors. The lecture covers defensive measures: dependency pinning, SBOM (Software Bill of Materials) tracking, automated vulnerability scanning, and AI-assisted code review.

### Required Reading

- OWASP (2040). *OWASP Top 10: Web Application Security Risks*. OWASP Foundation.
- West, M. (2033). "Trusted Types: Defending the DOM against XSS." *Google Security Blog*.
- Barth, A. (2011). *HTTP State Management Mechanism (Cookie SameSite)*. RFC 6265bis. IETF.
- Yggdrasil Security Team (2031). "The Codecov Breach Redux: Supply Chain Compromise via CI/CD." *UoY Security Postmortem* 2031-05.
- Yggdrasil Security Team (2034). "AI-Generated Exploits: Automated Vulnerability Discovery in the 2030s." *UoY Security Research Report* 2034-08.

### Discussion Questions

1. CSP is a powerful defense but can be bypassed if misconfigured (e.g., `'unsafe-inline'` in script-src). What organizational processes ensure that CSP policies are audited and tightened over time?
2. SameSite cookies have largely eliminated CSRF without developer effort. Does this mean CSRF is a solved problem, or have attackers found bypasses?
3. AI exploit generation can discover vulnerabilities faster than human researchers. Does this asymmetry favor attackers, or can defenders use the same AI to find and fix vulnerabilities first?
4. Supply chain attacks target build-time dependencies. Should organizations treat their build infrastructure with the same security rigor as production, or is the cost prohibitive?

### Practice Problems

- Perform a manual security audit of a provided web application. Identify at least 5 vulnerabilities (XSS, CSRF, injection, misconfigured headers, insecure dependencies). Document each finding with proof-of-concept and remediation steps.
- Implement a Content Security Policy for a web application. Start with `default-src 'none'` and iteratively add necessary sources, measuring the policy's effectiveness with CSP reporting (`report-uri` or `report-to`).

---

ᚾ **Lecture 10: Web APIs and Microservices: REST, GraphQL, and gRPC**

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Modern web applications are not monoliths but compositions of services communicating via APIs. This lecture covers the design, implementation, and operation of web APIs, with emphasis on the three dominant paradigms: REST, GraphQL, and gRPC. Students will learn to design APIs for clarity, version them for evolution, secure them against abuse, and monitor them for reliability.

### Key Topics

- REST principles: resources, representations, statelessness, and HATEOAS
- API design: URL structure, versioning, pagination, filtering, and error responses
- GraphQL: schemas, resolvers, mutations, subscriptions, and the N+1 problem
- gRPC: Protocol Buffers, streaming, deadlines, and service mesh integration
- API security: authentication, authorization, rate limiting, and throttling

### Lecture Notes

Roy Fielding's 2000 dissertation introduced REST as an architectural style, not a protocol. By 2040, "REST API" has become a colloquialism for any HTTP-based API, though few APIs fully adhere to Fielding's constraints. This lecture distinguishes REST-as-ideal from REST-as-practice, teaching students to design APIs that are pragmatically RESTful rather than dogmatically pure.

**REST principles** (Fielding's constraints) are: **client-server** (separation of concerns), **statelessness** (each request contains all necessary context), **cacheability** (responses explicitly indicate cacheability), **uniform interface** (resources identified by URIs, manipulated via standard methods), and **layered system** (intermediaries like proxies and caches are transparent to clients). **HATEOAS (Hypermedia as the Engine of Application State)**, the most neglected constraint, requires that responses include links to related resources, enabling clients to navigate the API without hardcoded URLs. By 2040, HATEOAS has seen renewed interest due to its synergy with AI agents: an API that describes its own capabilities via hypermedia can be consumed by autonomous systems without manual integration.

**API design** is the craft of making interfaces comprehensible and maintainable. The lecture covers **URL structure**: nouns (not verbs) for resources (`/users` not `/getUsers`), pluralization consistency, and nested resources (`/users/123/orders`). **Versioning** strategies: URL versioning (`/v1/users`), header versioning (`Accept: application/vnd.api.v1+json`), and no versioning (evolution via backward-compatible changes). **Pagination** patterns: offset-based (`?page=2&limit=10`), cursor-based (`?cursor=abc123`), and seek-based (`?after_id=456`). **Filtering** and **sorting** via query parameters (`?status=active&sort=-created_at`). **Error responses** following RFC 7807 (Problem Details for HTTP APIs), which standardizes error format (`type`, `title`, `status`, `detail`, `instance`).

**GraphQL** (2015, standardized 2030) addresses REST's over-fetching and under-fetching problems. Clients specify exactly which fields they need, and the server returns only those fields. The **schema** defines types, queries, mutations, and subscriptions. **Resolvers** are functions that fetch data for each field. The **N+1 problem** occurs when a query requests a list of objects and their nested objects, causing the resolver to make N+1 database queries (one for the list, one per item). The solution is **DataLoader**, a batching and caching layer that coalesces individual queries into batched requests. By 2040, **federated GraphQL** (Apollo Federation, standardized 2033) enables multiple services to contribute to a single schema, with a gateway that routes sub-queries to the appropriate services.

**gRPC** (covered in Lecture 7 for real-time protocols) is revisited from the API design perspective. Its **Protocol Buffers** schema language enforces type safety and backward compatibility: fields are numbered, and new fields can be added without breaking existing clients (forward compatibility). **Streaming** (server, client, bidirectional) enables real-time APIs. **Deadlines** (client-specified timeouts propagated through the call chain) prevent cascading timeouts. By 2040, **gRPC-Web** enables browser clients to call gRPC services via an HTTP/1.1-compatible proxy. The lecture covers **service mesh integration**: Istio and Linkerd automatically add mTLS, load balancing, retries, and circuit breaking to gRPC services without code changes.

**API security** encompasses authentication (who are you?), authorization (what can you do?), and abuse prevention (how much can you ask?). **Authentication** methods: API keys (simple but inflexible), OAuth 2.1 (authorization code flow with PKCE for public clients, client credentials for machine-to-machine), JWT (stateless tokens containing claims), and mTLS (mutual TLS for service-to-service). **Authorization** models: RBAC (Role-Based Access Control, coarse-grained), ABAC (Attribute-Based Access Control, fine-grained), and ReBAC (Relationship-Based Access Control, used by Google Zanzibar). **Rate limiting** prevents abuse: token bucket, leaky bucket, and fixed window algorithms. **Throttling** degrades service rather than blocking entirely (e.g., returning slower responses or reduced data for exceeded quotas). By 2040, the UoY API Gateway enforces rate limits, authentication, and authorization for all public APIs.

### Required Reading

- Fielding, R. T. (2000). *Architectural Styles and the Design of Network-based Software Architectures*. Ph.D. dissertation, UC Irvine. Chapters 5–6.
- GraphQL Foundation (2030). *GraphQL Specification*. Version 2030-06.
- gRPC Authors (2040). *gRPC Documentation: Best Practices for API Design*. grpc.io.
- Nottingham, M., & Wilde, E. (2021). *RFC 7807: Problem Details for HTTP APIs*. IETF.
- Yggdrasil API Design Guild (2035). "The UoY API Design Guide: REST, GraphQL, and gRPC Standards." *UoY Engineering Standards* v5.0.

### Discussion Questions

1. HATEOAS has been largely ignored in REST API design. Is this because it provides little practical value, or because developers lack the tooling to consume hypermedia APIs effectively?
2. GraphQL's flexibility is powerful but creates security challenges (complex queries can exhaust server resources). What query cost analysis and complexity limits are appropriate for production GraphQL APIs?
3. gRPC's type safety and performance are advantages, but its reliance on HTTP/2 and Protocol Buffers creates interoperability challenges. For a public API that must support diverse clients, is gRPC appropriate?
4. ReBAC (Zanzibar-style) provides fine-grained authorization but requires modeling all relationships in a graph database. For a small team, is the modeling overhead justified?

### Practice Problems

- Design a REST API for a library management system. Specify resources, URLs, methods, request/response schemas, error responses, and versioning strategy. Document with OpenAPI 4.0.
- Implement a GraphQL schema for the same library system. Define types, queries, mutations, and resolvers. Address the N+1 problem with DataLoader and measure query performance.

---

ᛁ **Lecture 11: The Semantic Web and Linked Data: From HTML to Knowledge Graphs**

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Tim Berners-Lee's original vision for the web was not merely a collection of linked documents but a universal graph of machine-readable knowledge. This lecture traces the evolution of the semantic web from the early 2000s through the knowledge graph revolution of the 2020s–2030s. Students will learn RDF, OWL, SPARQL, and the practical applications of linked data in search, AI, and enterprise integration.

### Key Topics

- The semantic web vision: from documents to data to knowledge
- RDF: triples, serialization formats (Turtle, JSON-LD), and vocabularies
- OWL: ontology languages, reasoning, and the open world assumption
- SPARQL: querying RDF graphs with graph patterns
- Knowledge graphs: Google's Knowledge Graph, Wikidata, and enterprise implementations

### Lecture Notes

The semantic web project, launched by Tim Berners-Lee, Jim Hendler, and Ora Lassila in a 2001 *Scientific American* article, proposed extending the web with machine-readable metadata. Rather than humans reading HTML pages and inferring meaning, machines would process structured data (RDF triples) to answer questions, discover relationships, and automate integration. The vision was ambitious and, for two decades, largely unrealized in the consumer web. But by 2040, the semantic web's technologies have found their place in search engines, enterprise data integration, and AI knowledge bases.

**RDF (Resource Description Framework)** is the data model of the semantic web. An RDF statement is a triple: **subject** (a resource, identified by URI), **predicate** (a property, identified by URI), and **object** (a resource or literal value). For example: `<http://example.org/alice> <http://xmlns.com/foaf/0.1/knows> <http://example.org/bob>`. The lecture covers RDF serialization formats: **Turtle** (human-friendly, terse syntax), **RDF/XML** (verbose, XML-based), **N-Triples** (line-based, simple parsing), and **JSON-LD** (JSON-based, the most popular format by 2040 due to its compatibility with web APIs). **Vocabularies** (schemas) define the properties and classes used in triples: FOAF (Friend of a Friend), Schema.org, Dublin Core, and the UoY **Yggdrasil Ontology** (2036, defining academic concepts, courses, and relationships).

**OWL (Web Ontology Language)** extends RDF with expressiveness for defining classes, properties, and constraints. OWL supports: **class hierarchies** (Course ⊑ Thing; ComputerScienceCourse ⊑ Course), **property characteristics** (transitive, symmetric, functional, inverse), **cardinality restrictions** (a Course has exactly one instructor), and **disjointness** (Undergraduate and Graduate are disjoint). OWL reasoning engines (HermiT, Pellet, FaCT++) infer implicit knowledge from explicit axioms. The lecture demonstrates: given that Alice is a PhD student and PhD students are graduate students, an OWL reasoner infers that Alice is a graduate student. By 2040, OWL reasoning is integrated into enterprise knowledge graphs, though scalability remains a challenge for billion-triple datasets.

**SPARQL** is the query language for RDF graphs. Its syntax resembles SQL but operates on graph patterns rather than tables. A basic SPARQL query: `SELECT ?name WHERE { ?person foaf:name ?name . ?person rdf:type foaf:Person }` returns all names of resources typed as Person. SPARQL supports: **FILTER** (conditions), **OPTIONAL** (left-join-like patterns), **UNION** (disjunction), **ORDER BY** and **LIMIT** (pagination), and **UPDATE** (INSERT/DELETE). By 2040, **Federated SPARQL** enables queries across multiple endpoints, and **SPARQL 2.0** adds property paths, aggregates, and subqueries. The lecture implements a SPARQL query against the UoY knowledge graph, retrieving all courses taught by a given professor, along with their prerequisites.

**Knowledge graphs** are the practical realization of the semantic web vision. **Google's Knowledge Graph** (introduced 2012, vastly expanded by 2040) contains billions of entities and trillions of facts, powering search result panels, question answering, and recommendation. **Wikidata** (the structured data companion to Wikipedia) provides a collaboratively edited knowledge base with SPARQL query access. **Enterprise knowledge graphs** integrate data from multiple silos (databases, documents, APIs) into a unified queryable graph. The UoY **Mímir-KG** (2038) integrates student records, course catalogs, research publications, and campus sensor data into a single RDF graph, enabling queries like "Which professors teach courses related to neuromorphic computing and have published in Nature in the last 5 years?"

### Required Reading

- Berners-Lee, T., Hendler, J., & Lassila, O. (2001). "The Semantic Web." *Scientific American*, 284(5), 34–43.
- Cyganiak, R., Wood, D., & Lanthaler, M. (2014). *RDF 1.1 Concepts and Abstract Syntax*. W3C Recommendation.
- Prud'hommeaux, E., & Buil-Aranda, C. (2013). *SPARQL 1.1 Query Language*. W3C Recommendation.
- Hogan, A., et al. (2035). "Knowledge Graphs: A Comprehensive Survey." *ACM Computing Surveys*, 58(4), 1–37.
- Yggdrasil Knowledge Engineering Lab (2038). "Mímir-KG: The University of Yggdrasil's Integrated Knowledge Graph." *UoY Semantic Web Report* 2038-04.

### Discussion Questions

1. The semantic web vision was criticized as overly ambitious and academic. Has the success of knowledge graphs vindicated the vision, or are knowledge graphs merely a pragmatic subset that abandoned the original ideals?
2. OWL reasoning is powerful but computationally expensive. For a knowledge graph with 1 billion triples, is OWL reasoning feasible, or should simpler rule engines be used?
3. SPARQL is expressive but unfamiliar to most developers. Should knowledge graphs expose SPARQL endpoints to general users, or should they provide higher-level APIs that generate SPARQL internally?
4. Google's Knowledge Graph is proprietary, while Wikidata is open. What are the risks of a single corporation controlling the world's largest structured knowledge base?

### Practice Problems

- Model a simple domain (e.g., university courses and students) in RDF. Define classes, properties, and instances in Turtle. Write SPARQL queries to retrieve: all courses in a department, all students enrolled in a course, and all prerequisites of a given course.
- Query the Wikidata SPARQL endpoint to retrieve all universities in Norway, their founding dates, and their number of students. Visualize the results and identify any data quality issues.

---

ᛃ **Lecture 12: The Future Web: Decentralized Architectures, Web3, and the Post-HTTP Internet**

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

The final lecture looks beyond current web architecture to emerging paradigms: decentralized web protocols, blockchain-based identity, peer-to-peer networking, and the protocols that may eventually succeed HTTP. By 2040, the web is in transition: centralized platforms dominate, but decentralized alternatives are gaining traction in identity, storage, and governance. Students will understand these alternatives and assess their viability.

### Key Topics

- Decentralized identity: DIDs, Verifiable Credentials, and self-sovereign identity
- IPFS and content-addressed storage: addressing data by hash, not location
- Blockchain and smart contracts: Ethereum, Layer 2s, and the 2030s scalability solutions
- ActivityPub and the fediverse: decentralized social networking
- Beyond HTTP: QUIC evolution, WebTransport, and speculative protocols

### Lecture Notes

The web of 2040 is still predominantly centralized: a handful of corporations operate the search engines, social networks, cloud platforms, and app stores that most users depend on. Yet the technological and ideological push for decentralization, which gained momentum in the 2010s with Bitcoin and the 2020s with Web3, has produced viable alternatives for specific use cases. This lecture surveys these alternatives without hype or dismissal, assessing their technical merits and practical limitations.

**Decentralized identity** addresses the problem of platform-controlled identity. The W3C **Decentralized Identifiers (DIDs)** standard (2022, updated 2030) defines identifiers that are not tied to a central registry: a DID like `did:ethr:0x1234...` is controlled by the cryptographic keypair that created it. **Verifiable Credentials** (W3C standard, 2031) enable assertions about a DID ("this person has a degree from UoY") that can be cryptographically verified without contacting the issuer. By 2040, the **Yggdrasil Student ID** is issued as a Verifiable Credential, enabling graduates to prove their qualifications without UoY maintaining a verification server indefinitely. The lecture covers DID methods (ethr, web, key, ion), credential revocation (cryptographic accumulators and status lists), and privacy (selective disclosure via zero-knowledge proofs).

**IPFS (InterPlanetary File System)** provides content-addressed storage: files are retrieved by their cryptographic hash (`QmXxYyZz...`) rather than by server location (`https://example.com/file.txt`). Content addressing enables deduplication (identical files have the same address), verifiability (the hash proves the content matches), and resilience (files can be served by any node that has them). By 2040, IPFS is used for: academic preprints (UoY publishes all research to IPFS), software distribution (package managers verify downloads by CID), and archival (the Internet Archive mirrors to IPFS). The lecture covers IPFS architecture: Merkle DAGs, the Distributed Hash Table (DHT) for peer discovery, and the Bitswap protocol for block exchange. Challenges: content persistence (who pins unpopular content?), gateway centralization (most users access IPFS via HTTP gateways, recreating centralization), and performance (DHT lookups add latency compared to DNS).

**Blockchain and smart contracts** have evolved from speculative assets to infrastructure layers. By 2040, **Ethereum** (launched 2015) operates on Proof-of-Stake with sharding, achieving thousands of transactions per second. **Layer 2 solutions** (rollups like Optimism and Arbitrum, validiums like StarkNet) process transactions off-chain and submit proofs to Ethereum, enabling microtransactions for IoT and content monetization. The lecture covers smart contract applications relevant to IT: **decentralized DNS** (ENS, Namecoin alternatives), **decentralized storage incentives** (Filecoin, Storj), and **DAO governance** (decentralized autonomous organizations managing shared infrastructure). The 2033 *DAO Hack Redux*—in which a bug in a governance contract allowed a single user to drain $400 million—demonstrates that smart contract security is as critical as traditional software security.

**ActivityPub** (W3C Recommendation, 2018) is the protocol powering the **fediverse**: a decentralized social network of interoperable servers (Mastodon, Pleroma, PeerTube, Pixelfed). ActivityPub defines actor-based federation: users on one server can follow, message, and interact with users on another via ActivityStreams JSON-LD messages. By 2040, the fediverse has grown to 500 million users, driven by dissatisfaction with centralized platforms and regulatory pressure for interoperability (the 2031 *Digital Services Act* mandated fediverse-compatible APIs for large social networks). The lecture covers ActivityPub's architecture: actors, activities, objects, inboxes, and outboxes. Operational challenges: moderation across federated instances, spam prevention, and the "instance defederation" problem (when instances block each other, fragmenting the network).

**Beyond HTTP**, the lecture speculates on future transport protocols. **WebTransport** (W3C standard, 2030) exposes QUIC's datagram and stream capabilities to JavaScript, enabling low-latency gaming, live video, and IoT communication without WebSocket overhead. **QUIC evolution** continues: multipath QUIC (using multiple network interfaces simultaneously), unreliable datagram extension (for real-time media), and congestion control innovations (BBRv3). The lecture concludes with a thought experiment: if HTTP were designed today, what would it look like? The consensus by 2040 is that it would be binary (like HTTP/2), multiplexed (like QUIC), content-addressed (like IPFS), and privacy-preserving (like Oblivious HTTP)—in other words, a synthesis of the innovations covered throughout this course.

### Required Reading

- W3C (2030). *Decentralized Identifiers (DIDs) v2.0*. W3C Recommendation.
- W3C (2031). *Verifiable Credentials Data Model 2.0*. W3C Recommendation.
- IPFS Documentation (2040). *IPFS Docs: Content Addressing, Merkle DAGs, and the DHT*. Protocol Labs.
- ActivityPub W3C Community Group (2040). *ActivityPub Specification: Federation Protocol*. W3C.
- Yggdrasil Digital Identity Lab (2038). "Yggdrasil Student ID: Verifiable Credentials in Practice." *UoY Identity Research Report* 2038-02.

### Discussion Questions

1. Decentralized identity promises self-sovereignty, but key management is hard. What recovery mechanisms are appropriate if a user loses their private key, and do these mechanisms reintroduce centralization?
2. IPFS content addressing enables resilience but does not guarantee persistence. Who should be responsible for pinning important content, and how should they be incentivized?
3. The fediverse's instance-based moderation model allows diverse communities but enables "filter bubbles" and fragmentation. Is this diversity a feature or a bug?
4. If HTTP were redesigned today, would it retain its request-response model, or would it embrace fully bidirectional, message-oriented communication?

### Practice Problems

- Create a decentralized identifier (DID) using the `did:key` method and issue a self-signed Verifiable Credential attesting to a skill or qualification. Verify the credential cryptographically.
- Set up an IPFS node, add a file, and retrieve it via a public gateway and via the local DHT. Measure the time to first byte for each method and discuss the trade-offs.

---

## Final Examination Preparation

The IT107 final examination is a **comprehensive design and analysis assessment** conducted over 48 hours. Students must complete **three of four** design challenges:

1. **Network Architecture Design**: Design a CDN-backed, HTTPS-enabled web infrastructure for a global e-commerce site. Specify DNS configuration, TLS setup, CDN cache policies, origin architecture, and failover mechanisms. Include a cost model and a security analysis.
2. **Protocol Analysis**: Given a packet capture of a web browsing session, reconstruct the HTTP requests and responses, identify the TLS version and cipher suite, analyze the caching behavior, and identify any security vulnerabilities (missing headers, weak ciphers, etc.).
3. **Search Engine Implementation**: Implement a simplified search engine for a corpus of 10,000 documents. Include a crawler, inverted index, BM25 ranking, and a web interface. Evaluate precision and recall on a provided query set.
4. **API Design and Security Audit**: Design a REST API for a ride-sharing service. Specify resources, methods, authentication, rate limiting, and error handling. Then conduct a security audit, identifying at least 5 potential vulnerabilities and their mitigations.

### Evaluation Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Technical accuracy | 30% | Correct application of protocols, standards, and technologies |
| Design quality | 25% | Clean architecture, appropriate trade-offs, scalability considerations |
| Security awareness | 20% | Identification and mitigation of relevant threats |
| Documentation | 15% | Clear explanation of decisions, with citations to standards and best practices |
| Innovation | 10% | Creative or insightful approaches to known problems |

---

*The web is woven, from root to leaf, from cable to cloud. The knowledge is linked, the data flows, and the future is semantic.* ᛟ

— Runa Gridweaver Freyjasdottir, Web Technologies & Internet Architecture, University of Yggdrasil, 2040
