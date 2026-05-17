# IT107: Web Technologies & Internet Architecture
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4  
**Prerequisites:** IT101 (Introduction to Information Technology)  
**Description:** The web and the internet are the connective tissue of 2040 civilisation. This course provides the IT professional's working understanding of how data moves across the globe: the protocol stacks that underpin every HTTP request, the DNS infrastructure that translates human names into machine addresses, the web servers and reverse proxies that serve content at planetary scale, the TLS ecosystem that secures every connection, and the emerging paradigms — QUIC, WebAssembly, edge computing — that define the web of the 2040s. Students build, break, and rebuild real web infrastructure in the YggLab Cloud Sandbox, emerging with the diagnostic intuition that distinguishes the professional from the ticket-closer.

**Instructor:** Dr. Sigrún Vérendóttir, Department of Information Technology  
**Lab:** YggLab NetForge, Muninn Computing Centre, Third Floor  
**Office Hours:** Tuesdays and Thursdays, 14:00–16:00 UTC

---

## Lectures

---

### Lecture 1: The Internet Architecture — How Packets Cross the World

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

#### Overview

Every web page you load is the culmination of a miracle of engineering: a request generated in your browser traverses local networks, ISP routers, transit providers, undersea cables, and data centre fabrics to reach a server, which generates a response that retraces the entire path — all in under 100 milliseconds. This lecture unpacks the layered architecture that makes this possible: the OSI model as a conceptual framework, the TCP/IP stack as its practical implementation, and the physical infrastructure — fibre, copper, radio, satellite — that carries the bits. By the end of this lecture, students should be able to trace a packet's journey from browser to server and back, naming every protocol and device involved.

#### Key Topics

- **The Layered Model:** The OSI seven-layer model (Physical, Data Link, Network, Transport, Session, Presentation, Application) as a conceptual tool for understanding how abstraction enables interoperability. The lecture emphasises that OSI is a teaching model — the real internet runs on the four-layer TCP/IP model (Link, Internet, Transport, Application) — but the OSI framework provides vocabulary (Layer 2 vs. Layer 3 switching, Layer 7 load balancing) that IT professionals use daily.
- **The TCP/IP Stack in Detail:** Each layer and its protocols. Link Layer: Ethernet, Wi-Fi (802.11), and the MAC addressing that governs local network communication. Internet Layer: IP (v4 and v6), ICMP (ping and traceroute), and the routing protocols (BGP, OSPF) that determine how packets cross autonomous systems. Transport Layer: TCP (reliable, ordered, connection-oriented) and UDP (unreliable, unordered, connectionless — the foundation of QUIC, DNS, and streaming). Application Layer: HTTP, DNS, TLS, SMTP, SSH — the protocols IT professionals interact with daily.
- **Physical Infrastructure:** The internet is not a cloud; it is cables. The lecture maps the physical internet: Tier 1 networks (Level 3, NTT, Telia, Tata), Internet Exchange Points (IXPs — AMS-IX, DE-CIX, LINX, Equinix), undersea cable landing stations (Marseille, Singapore, New York, Mombasa), and the 2040 expansion of satellite internet constellations (Starlink v3, Kuiper, GuoWang) that bring connectivity to previously unreachable regions. Students examine the submarine cable map and trace routes between continents.
- **Packet Journey:** A concrete example: a student in Reykjavík types `https://yggdrasil.edu` into a browser. What happens? DNS resolution (recursive resolver → root servers → TLD servers → authoritative nameserver), TCP three-way handshake, TLS handshake (ClientHello, ServerHello, certificate verification, key exchange), HTTP request, server processing, HTTP response, browser rendering. The lecture traces every step with Wireshark captures and `curl -v` output.
- **The 2040 Internet:** IPv6 adoption (94% globally as of 2040, compared to 42% in 2024), the sunset of IPv4 except in legacy enterprise environments, the rise of named data networking (NDN) as a research paradigm for content-centric routing, and the integration of AI-driven traffic engineering (Google's B4 SDN, Microsoft's SWAN) that optimises wide-area network utilisation through machine-learned traffic predictions.

#### Lecture Notes

The IT professional's relationship with the network is diagnostic. When a web application is slow, the cause could be anywhere in the stack: DNS resolution taking 2 seconds, TCP retransmissions due to packet loss on a congested link, TLS negotiation stalling because of an expired intermediate certificate, or the application server queueing requests behind a blocking database query. The skill of the IT diagnostician is the ability to isolate the layer where the problem lives. The tools for this — `ping`, `traceroute`/`mtr`, `dig`, `curl -v`, `openssl s_client`, `tcpdump`/Wireshark — are the IT professional's stethoscope.

The lecture introduces the concept of "network empathy" — the ability to think like a packet. Every decision a network device makes (routing, queuing, dropping, prioritising) can be understood by asking: "If I were this packet, what would happen to me at this router?" This mental model is more valuable than memorising every RFC.

The Norse metaphor: the internet is not a cloud but a sea — like the North Atlantic that the Vikings crossed. Packets are ships; routers are harbours; DNS is the navigational chart; BGP is the oral tradition by which harbours learn which routes are open. A network engineer is a modern navigator, understanding winds (latency), currents (bandwidth), storms (DDoS attacks), and reefs (misconfigured firewalls).

#### Required Reading

- Kurose, J.F. & Ross, K.W. (2038). *Computer Networking: A Top-Down Approach*, 10th Edition. Pearson. Chapters 1–2.
- Fall, K.R. & Stevens, W.R. (2035). *TCP/IP Illustrated, Volume 1: The Protocols*, 3rd Edition. Addison-Wesley. Chapters 1–3.
- Clark, D.D. (2030). *Designing an Internet*. MIT Press. Chapter 4 (The Architecture of the Internet).
- Telegeography Submarine Cable Map (2040 edition). Interactive resource at `cablemap.yggdrasil.edu`.

#### Discussion Questions

1. The OSI model was standardised in 1984, yet the internet was built on TCP/IP, which predates OSI. Why did TCP/IP win, and what does this victory tell us about the relationship between standards bodies and engineering practice?
2. IPv6 was standardised in 1998. It took over 40 years to achieve global majority adoption. Analyse the technical, economic, and organisational barriers to IPv6 migration. What does this history suggest about the adoption timeline for post-quantum cryptography?
3. A traceroute from London to Tokyo shows a hop in New York. Why might this happen, and what does it reveal about the difference between geographic distance and network topology?

---

### Lecture 2: DNS — The Internet's Phonebook and Its Hidden Complexity

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

#### Overview

The Domain Name System (DNS) is the most underappreciated service on the internet. Every internet interaction begins with a DNS query, yet most users — and many IT professionals — treat it as a black box. This lecture opens that box: the hierarchical architecture of the DNS (root, TLD, authoritative), the query resolution process (recursive vs. iterative), the record types that encode different kinds of information, and the security extensions (DNSSEC, DNS-over-HTTPS, DNS-over-TLS) that protect the system from poisoning and surveillance. By the end, students configure their own authoritative DNS server for a domain and observe real query resolution with `dig +trace`.

#### Key Topics

- **DNS Hierarchy:** The root zone (served by 13 logical root servers, operated by 12 organisations — Verisign, ICANN, USC-ISI, Cogent, University of Maryland, NASA Ames, Internet Systems Consortium, US Department of Defense, US Army Research Lab, Netnod, RIPE NCC, WIDE Project — with hundreds of physical instances via anycast). The Top-Level Domains: generic (gTLDs — `.com`, `.org`, `.net`, `.edu`, and the 2040-era `.ai`, `.cloud`, `.dev`) and country-code (ccTLDs — `.uk`, `.de`, `.jp`, `.is`, `.io`). The authoritative nameservers that hold the actual resource records for each domain.
- **DNS Query Resolution:** The difference between recursive resolvers (your ISP's DNS server, Google's `8.8.8.8`, Cloudflare's `1.1.1.1`) and authoritative servers. A step-by-step walkthrough of a recursive resolution: stub resolver → recursive resolver → root hint file → root server (returns TLD referral) → TLD server (returns authoritative referral) → authoritative server (returns answer). The role of caching at every level and the TTL (Time-To-Live) mechanism that controls freshness.
- **DNS Record Types:** The essential records every IT professional must know: A (IPv4 address), AAAA (IPv6 address), CNAME (canonical name alias), MX (mail exchanger with priority), NS (nameserver delegation), SOA (start of authority — serial number, refresh/retry/expire/minimum TTL), TXT (arbitrary text — used for SPF, DKIM, DMARC, and domain verification), SRV (service locator — used by SIP, LDAP, and Kubernetes service discovery), PTR (reverse DNS for IP→name mapping), and CAA (certification authority authorisation — restricts which CAs can issue certificates for a domain).
- **DNSSEC and DNS Security:** The cache poisoning attacks that DNSSEC was designed to prevent (the Kaminsky attack of 2008). How DNSSEC works: zone signing with public-key cryptography, the chain of trust from the root zone (signed since 2010) through TLDs to individual domains, and the RRSIG, DNSKEY, DS, and NSEC/NSEC3 record types. The lecture includes a live demonstration: `dig +dnssec yggdrasil.edu` and verification of the signature chain.
- **Encrypted DNS:** The privacy problem: traditional DNS is unencrypted UDP on port 53, visible to every network between the client and the resolver. DNS-over-TLS (DoT, RFC 7858, port 853), DNS-over-HTTPS (DoH, RFC 8484, port 443 — indistinguishable from web traffic), and DNS-over-QUIC (DoQ, RFC 9250). The controversy: DoH centralises DNS at a few providers (Cloudflare, Google), which some argue undermines the distributed architecture of DNS. The 2040 landscape: DoH is the default in all major operating systems and browsers, with Oblivious DNS-over-HTTPS (ODoH) providing an additional proxy layer that separates the resolver's knowledge of who is querying from what is being queried.

#### Lecture Notes

DNS failures are among the most common and most confusing outages in IT. When DNS breaks, everything breaks: email stops, websites become unreachable, internal services fail to discover each other. The IT professional must be fluent in DNS diagnosis: `dig` for querying specific record types from specific servers, `host` for simple lookups, `nslookup` (deprecated but still encountered), and the art of checking propagation (`whatsmydns.net` for global visibility). Common failure modes: expired domains, misconfigured NS records (lame delegation), DNSSEC validation failures due to expired signatures, negative caching of SERVFAIL responses, and the subtle hell of split-horizon DNS (different answers for internal vs. external queries).

The lecture covers the operational pattern of DNS changes: any modification must account for TTL. If a record has a TTL of 86400 seconds (24 hours), reducing it to 300 seconds must be done at least 24 hours in advance of a migration — otherwise, cached records will point to the old destination long after the change. The "TTL dance" is a rite of passage for every IT professional.

In the 2040 landscape, DNS is increasingly integrated with service mesh architectures. Kubernetes uses CoreDNS for internal service discovery; Consul and Istio use DNS interfaces for dynamic routing; cloud providers use DNS-weighted routing for multi-region traffic management (Route 53, Azure Traffic Manager, Google Cloud DNS). DNS is no longer just a phonebook — it is a programmable control plane for traffic.

#### Required Reading

- Liu, C. & Albitz, P. (2037). *DNS and BIND*, 8th Edition. O'Reilly Media. Chapters 1–4, 11.
- Hoffman, P. (2033). *DNSSEC: The Protocol, Deployment, and Operational Considerations*. RFC 9364.
- Cloudflare Research (2039). "Oblivious DNS-over-HTTPS: Deployment Experience at Scale."
- IETF RFC 1034/1035 (the original DNS specifications — read for historical appreciation, not implementation detail).

#### Discussion Questions

1. DNSSEC adoption has been slow (approximately 35% of domains as of 2040). Analyse the barriers: operational complexity, key management, the risk of self-inflicted outages due to signature expiry, and the "chicken-and-egg" problem of resolver validation. What would it take to reach 90% adoption?
2. DNS-over-HTTPS encrypts queries between the client and the resolver, but the resolver still sees all queries. Does DoH actually solve the privacy problem, or does it merely shift trust from the ISP to the resolver operator? Evaluate Oblivious DoH as an alternative.
3. A company migrates its website to a new IP address. The old A record has a TTL of 86400. Some users still reach the old server 48 hours after the change. Diagnose all possible causes beyond the TTL itself.

---

### Lecture 3: HTTP — The Protocol That Powers the Web

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

#### Overview

The Hypertext Transfer Protocol (HTTP) is the application-layer protocol that has carried the web since 1991. This lecture covers HTTP/1.1 in operational depth: the request-response model, methods and their semantics, status codes and their meanings, headers that control caching, content negotiation, and security, and the practical tools (`curl`, browser DevTools, `httpie`) that IT professionals use to inspect and debug HTTP traffic. Students leave this lecture able to read raw HTTP messages and diagnose common protocol-level failures.

#### Key Topics

- **The HTTP Request-Response Model:** HTTP is stateless — each request is independent, carrying all the information the server needs to generate a response. The structure of an HTTP request: method, path, protocol version, headers (key: value pairs), empty line, optional body. The structure of an HTTP response: protocol version, status code, reason phrase, headers, empty line, body. The lecture shows raw HTTP messages using `nc` (netcat) to demonstrate that HTTP is just text over TCP.
- **HTTP Methods and Semantics:** The core methods: GET (safe, idempotent, retrieves a resource), HEAD (like GET but returns only headers), POST (submits data, not idempotent — creates a new resource), PUT (idempotent — creates or replaces a resource at a known URI), DELETE (removes a resource), PATCH (partial update). The less common but important methods: OPTIONS (CORS preflight), CONNECT (tunnel for HTTPS proxies), TRACE (diagnostic — echo back the request). The lecture emphasises the distinction between idempotent and non-idempotent methods and the operational implications: retrying a failed GET is safe; retrying a failed POST may create duplicate resources.
- **HTTP Status Codes:** The categories: 1xx (Informational — 100 Continue, 101 Switching Protocols), 2xx (Success — 200 OK, 201 Created, 204 No Content, 206 Partial Content for range requests), 3xx (Redirection — 301 Moved Permanently, 302 Found, 304 Not Modified, 307/308 for preserving method on redirect), 4xx (Client Error — 400 Bad Request, 401 Unauthorised, 403 Forbidden, 404 Not Found, 405 Method Not Allowed, 429 Too Many Requests), 5xx (Server Error — 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable, 504 Gateway Timeout). The lecture covers: the often-misused difference between 301 and 302, the critical distinction between 401 (unauthenticated) and 403 (unauthorised), and the operational meaning of 502/503/504 in reverse proxy architectures.
- **HTTP Headers:** The headers that matter operationally. Request headers: `Host` (required in HTTP/1.1 — enables virtual hosting), `User-Agent` (identifies the client), `Accept` / `Accept-Encoding` / `Accept-Language` (content negotiation), `Authorization` (credentials), `Cookie` (session state), `Cache-Control` (client caching directives), `If-None-Match` / `If-Modified-Since` (conditional requests). Response headers: `Content-Type` (MIME type), `Content-Length`, `Content-Encoding` (gzip, br — Brotli), `Set-Cookie`, `Cache-Control` (server caching directives — `public`, `private`, `max-age`, `s-maxage`, `no-cache`, `no-store`), `ETag` / `Last-Modified` (validation tokens), `Location` (for redirects), `Server` (identifies the web server software). Security headers: `Strict-Transport-Security` (HSTS), `Content-Security-Policy` (CSP), `X-Frame-Options`, `X-Content-Type-Options` (nosniff), `Referrer-Policy`.
- **Content Negotiation and Caching:** How servers serve different representations of the same resource based on `Accept` headers (JSON vs. HTML, English vs. Icelandic, gzip vs. uncompressed). The caching ecosystem: browser caches, intermediary caches (CDNs, corporate proxies), and the `Cache-Control` directives that govern them. The lecture includes a practical demonstration: using `curl -I` to inspect response headers and `curl -H 'If-None-Match: "abc123"'` to test conditional requests.

#### Lecture Notes

HTTP is simple enough that a human can read it and complex enough that a lifetime can be spent mastering its nuances. The lecture's central theme: HTTP is a conversation. Every status code is a sentence the server speaks to the client. A 301 says "I've moved permanently — update your bookmarks." A 304 says "You already have the latest version — use your cache." A 429 says "You're asking too fast — slow down." A 502 says "The server behind me is not responding." The IT diagnostician reads these sentences and traces them to root causes.

The operational reality of HTTP in 2040: HTTP/3 (QUIC) is the dominant protocol for user-facing traffic, but HTTP/1.1 remains ubiquitous in internal service-to-service communication, legacy APIs, and embedded systems. The IT professional must be fluent in all three versions, understanding their different wire formats, performance characteristics, and diagnostic tools.

Common HTTP pitfalls covered in the lecture: redirect chains (a 301 pointing to a URL that also returns a 301 — browsers stop after 20 redirects, but intermediate proxies may not), the `Host` header mismatch (virtual hosting breaks when the `Host` header doesn't match any configured `ServerName`), and the subtle difference between `no-cache` (validate before using) and `no-store` (don't cache at all).

#### Required Reading

- Fielding, R.T. et al. (2022). *HTTP Semantics*. RFC 9110. Sections 1–9, 12, 15.
- Nottingham, M. (2035). *HTTP Caching*. RFC 9111.
- Grigorik, I. (2034). *High Performance Browser Networking*, 2nd Edition. O'Reilly Media. Chapters 9–11.
- MDN Web Docs. "HTTP" — the definitive reference at `developer.mozilla.org/en-US/docs/Web/HTTP`.

#### Discussion Questions

1. HTTP is stateless, yet the modern web is stateful (sessions, shopping carts, authentication). How is state built on top of a stateless protocol? Analyse the roles of cookies, tokens, and server-side session stores.
2. A CDN returns a 304 Not Modified for a resource, but the browser displays stale content. Diagnose all possible causes in the caching chain: origin server, CDN edge, browser cache, and the conditional request mechanism.
3. The `Host` header in HTTP/1.1 enabled virtual hosting — thousands of websites on a single IP address. HTTP/2 and HTTP/3 also require the `:authority` pseudo-header. What happens when TLS SNI (Server Name Indication) and the HTTP Host header disagree? How does this mismatch create both operational problems and security vulnerabilities?

---

### Lecture 4: HTTP/2 and HTTP/3 — The Modern Web Protocol Stack

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

#### Overview

HTTP/1.1 served the web for over 15 years, but its limitations — head-of-line blocking, verbose headers, and the six-connection-per-origin limit — became bottlenecks as web pages grew to hundreds of resources. HTTP/2 (2015, RFC 7540) addressed these with multiplexing, header compression, and server push. HTTP/3 (2022, RFC 9114) went further, replacing TCP with QUIC (a UDP-based transport) to eliminate head-of-line blocking entirely. This lecture covers the architecture of both protocols, their operational implications, and the diagnostic tools (`nghttp2`, `curl --http3`, Wireshark with QUIC decryption) for the modern web stack.

#### Key Topics

- **HTTP/2 — Multiplexing and Framing:** HTTP/2's core innovation: multiple requests and responses multiplexed over a single TCP connection using binary framing. Streams (independent bidirectional sequences), frames (DATA, HEADERS, PRIORITY, RST_STREAM, SETTINGS, PING, GOAWAY, WINDOW_UPDATE, CONTINUATION), and the flow control mechanism that prevents a fast sender from overwhelming a slow receiver. The lecture demonstrates multiplexing with `nghttp -nv https://yggdrasil.edu` and shows how a single connection carries dozens of simultaneous requests.
- **Header Compression (HPACK and QPACK):** HTTP/1.1 headers are uncompressed and repetitive — `Cookie`, `User-Agent`, and `Accept` headers are identical across requests to the same origin. HPACK (HTTP/2) uses a combination of static tables (61 predefined header key-value pairs), dynamic tables (learned during the connection), and Huffman coding to reduce header overhead by 85–90%. QPACK (HTTP/3) adapts HPACK for QUIC's independent streams, solving the head-of-line blocking that HPACK's dynamic table creates at the compression level.
- **Server Push (and Its Demise):** HTTP/2 introduced server push — the server proactively sends resources the client will need (e.g., pushing CSS and JavaScript when the client requests HTML). In theory, this eliminated a round-trip. In practice, it was difficult to implement correctly: servers pushed resources the browser already had cached, wasting bandwidth. By 2024, Chrome had removed server push support. The lecture covers this as a case study in the gap between protocol design and operational reality — a feature that was technically elegant but practically harmful.
- **HTTP/3 and QUIC:** QUIC (Quick UDP Internet Connections) is a transport protocol designed by Google, standardised as RFC 9000 in 2021, that replaces TCP for HTTP/3. QUIC's advantages: 0-RTT connection establishment (for resumed connections — the client sends data in the first flight), no head-of-line blocking (packet loss on one stream doesn't block others), connection migration (a QUIC connection survives IP address changes — critical for mobile devices switching between Wi-Fi and cellular), and mandatory encryption (QUIC always uses TLS 1.3). The lecture walks through a QUIC handshake with Wireshark, showing the TLS 1.3 integration and the stream multiplexing.
- **Operational Implications for IT:** The migration from HTTP/1.1 to HTTP/2 to HTTP/3 changes the IT professional's diagnostic toolkit. TCP-based tools (`tcpdump` filtering on port 80/443) don't directly apply to QUIC (UDP port 443). Load balancers that terminate TLS must be upgraded to support HTTP/3. Firewall rules must allow UDP 443. The lecture covers: UDP-based performance tuning (differing from TCP's congestion control assumptions), QUIC's requirement that connection IDs (not IP/port tuples) identify connections, and the challenge of debugging encrypted QUIC traffic (SSLKEYLOGFILE with Wireshark).

#### Lecture Notes

HTTP/3 is not an incremental improvement; it is a fundamental rearchitecture. By moving from TCP to QUIC, the web stack shed 40 years of accumulated TCP assumptions: three-way handshakes, in-order delivery requirements, and the connection's binding to a specific IP address. For the IT professional, this means rethinking everything from firewall rules to load balancer configuration to performance monitoring.

The 2040 landscape: HTTP/3 carries approximately 78% of global web traffic. HTTP/2 carries the remaining user-facing traffic (mostly older clients and enterprise environments). HTTP/1.1 persists in internal infrastructure and is likely to remain for decades — the COBOL of the web. The lecture's practical exercise: students configure an nginx server with HTTP/2 and HTTP/3 support, verify with `curl --http3`, and compare the performance of loading a complex web page over each protocol using browser DevTools waterfalls.

The Norse framing: HTTP/1.1 is a single-file bridge — one cart at a time. HTTP/2 is a multi-lane highway — many carts simultaneously, but a single accident blocks all lanes. HTTP/3 is a fleet of independent longships — each ship sails its own course, and the loss of one does not delay the others.

#### Required Reading

- Belshe, M. et al. (2015). *Hypertext Transfer Protocol Version 2 (HTTP/2)*. RFC 7540.
- Bishop, M. (2022). *HTTP/3*. RFC 9114.
- Iyengar, J. & Thomson, M. (2021). *QUIC: A UDP-Based Multiplexed and Secure Transport*. RFC 9000.
- Langley, A. et al. (2035). "The QUIC Transport Protocol: Design and Internet-Scale Deployment." *ACM SIGCOMM Computer Communication Review*.

#### Discussion Questions

1. HTTP/3 uses UDP, which is traditionally associated with unreliable, fire-and-forget communication (DNS, streaming, gaming). QUIC builds reliability on top of UDP. Why did the designers choose UDP rather than creating a new IP protocol? What does this choice reveal about internet architecture ossification?
2. Server push was removed from browsers despite being a core HTTP/2 feature. What does this tell us about the relationship between protocol designers and implementers? Can you think of other protocol features that were standardised but abandoned in practice?
3. QUIC connection migration allows a connection to survive an IP address change. How does this affect the operational model of load balancers that track sessions by client IP? What changes must network infrastructure make to support connection migration?

---

### Lecture 5: Web Servers and Reverse Proxies

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

#### Overview

The web server is the software that listens for HTTP requests and returns responses. In 2040, three web servers dominate: nginx (38% market share, widely used as a reverse proxy), Apache httpd (25%, still the workhorse of shared hosting), and Caddy (12%, automatic HTTPS with Let's Encrypt integration). This lecture covers the architecture, configuration, and operational patterns of each, with emphasis on the reverse proxy pattern that has become the standard deployment architecture: TLS termination at the edge, static file serving, and request routing to application backends.

#### Key Topics

- **Web Server Architecture:** The fundamental design choices. Process-based (Apache's prefork MPM — one process per connection, simple but memory-intensive), thread-based (Apache's worker and event MPMs), and event-driven (nginx, Caddy — a small number of worker processes handling thousands of connections asynchronously via `epoll`/`kqueue`). The lecture explains why event-driven architectures won: the C10K problem (handling 10,000 concurrent connections) is trivial for nginx but impossible for a process-per-connection model.
- **nginx Configuration:** The structure of an nginx configuration: `http` block, `server` blocks (virtual hosts), `location` blocks (URL routing). Key directives: `listen` (port and protocol — `listen 443 ssl http2`), `server_name` (virtual host matching), `root` (document root), `index` (default file), `proxy_pass` (reverse proxy to backend), `try_files` (static file serving with fallback). The lecture includes a complete nginx configuration for a typical 2040 deployment: TLS termination, static assets served directly, API requests proxied to a Go backend, WebSocket upgrade for real-time features.
- **Reverse Proxy Patterns:** The reverse proxy sits between clients and application servers, providing: TLS termination (offloading cryptographic operations), load balancing (`upstream` blocks with `least_conn`, `ip_hash`, or `random` algorithms), caching (`proxy_cache_path` and `proxy_cache` directives), compression (`gzip on`), rate limiting (`limit_req_zone` and `limit_req`), and request buffering (protecting backend servers from slow clients). The lecture covers the operational benefits: application servers focus on business logic; the reverse proxy handles cross-cutting concerns.
- **Caddy and Automatic HTTPS:** Caddy's defining feature: TLS certificates are obtained and renewed automatically via Let's Encrypt (ACME protocol) with zero configuration. The lecture demonstrates: `caddy run` with a Caddyfile, automatic HTTP→HTTPS redirect, and the ACME challenge process (HTTP-01 and DNS-01). The operational implications: Caddy eliminates the class of outages caused by expired TLS certificates, which historically accounted for approximately 3% of web infrastructure incidents.
- **Apache httpd in 2040:** Apache remains relevant in specific niches: shared hosting (cPanel/WHM integration), legacy enterprise applications, and environments where `.htaccess` files provide decentralised configuration. The lecture covers Apache's module system (`mod_rewrite`, `mod_proxy`, `mod_security`), the transition from prefork to event MPM, and the reasons an IT professional might choose Apache over nginx (e.g., dynamic module loading without recompilation, richer authentication modules).

#### Lecture Notes

The reverse proxy is the IT professional's most powerful architectural pattern. It is not merely a pass-through; it is the point at which authentication, authorisation, rate limiting, logging, caching, compression, and request routing are enforced. A well-configured reverse proxy can protect poorly written application servers from every class of HTTP-level attack. A misconfigured reverse proxy can expose internal services, leak sensitive headers, or become a single point of failure.

The lecture's practical exercise: students are given a vulnerable application server (written in Flask, with no TLS, no rate limiting, and error pages that leak stack traces) and must deploy an nginx reverse proxy in front of it that: terminates TLS with a Let's Encrypt certificate, rate-limits to 10 requests per second per IP, strips sensitive response headers, returns custom error pages, and caches static assets for 24 hours.

The Norse metaphor: the web server is the longhouse door. The reverse proxy is the shield-wall in front of it — every request must pass through the shield-wall before reaching the warmth of the hearth. A good shield-wall turns away raiders before they ever see the longhouse.

#### Required Reading

- Nedelcu, C. (2039). *Nginx HTTP Server*, 6th Edition. Packt Publishing. Chapters 1–4, 7–9.
- Holt, M. (2040). *Caddy: The Ultimate Server Guide*. Caddy Documentation. Sections on Caddyfile syntax, reverse proxy, and automatic HTTPS.
- Apache httpd Documentation (2040). "Reverse Proxy Guide" and "Performance Tuning."
- Yggdrasil IT Operations Runbook (2040). "Reverse Proxy Deployment Standard" — internal document specifying nginx configuration templates.

#### Discussion Questions

1. nginx's event-driven architecture uses non-blocking I/O with `epoll`. Apache's prefork MPM uses one process per connection with blocking I/O. For a workload of 10,000 simultaneous idle connections (clients connected but not actively sending requests), compare the memory consumption. What does this comparison reveal about the importance of architecture choice in infrastructure software?
2. The reverse proxy pattern centralises cross-cutting concerns — TLS, authentication, rate limiting — at a single point. What are the risks of this centralisation? How would you mitigate them?
3. Caddy's automatic HTTPS eliminates certificate expiry outages. But it also means a single company (Let's Encrypt, operated by the Internet Security Research Group) issues certificates for approximately 60% of the web. Analyse the concentration risk. What happens if Let's Encrypt's intermediate CA is compromised or revoked?

---

### Lecture 6: TLS, Certificates, and Web Security

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

#### Overview

Transport Layer Security (TLS) is the cryptographic protocol that secures every HTTPS connection — over 95% of web traffic in 2040. This lecture covers TLS from an operational perspective: the handshake that establishes a secure channel, the certificate ecosystem that binds domain names to cryptographic keys, and the common misconfigurations that create vulnerabilities. Students configure a TLS endpoint, inspect certificates with `openssl s_client`, and diagnose certificate chain failures.

#### Key Topics

- **The TLS Handshake (1.2 and 1.3):** TLS 1.2 (2008): ClientHello (supported cipher suites, random number) → ServerHello (chosen cipher suite, random number, certificate) → key exchange (RSA or ECDHE) → ChangeCipherSpec → Finished. Two round-trips. TLS 1.3 (2018): ClientHello (supported cipher suites, key share for ECDHE) → ServerHello (chosen cipher suite, key share, certificate, Finished) → Client Finished. One round-trip (1-RTT), or zero (0-RTT) for resumed connections. The lecture traces both handshakes with Wireshark and explains the security improvements: removal of obsolete algorithms (RSA key exchange, CBC-mode ciphers, SHA-1 hashing), mandatory forward secrecy (ECDHE for every connection), and encrypted ServerHello (the server's certificate is encrypted in TLS 1.3, protecting the domain name from passive observers).
- **X.509 Certificates:** The structure of an X.509 certificate: Subject (Common Name, Organisation), Issuer, Validity period (Not Before / Not After), Public Key, Signature Algorithm, Extensions (SAN — Subject Alternative Name, the modern replacement for CN; Basic Constraints — whether this is a CA certificate; Key Usage — what operations the key can perform; Extended Key Usage — serverAuth, clientAuth). The lecture shows how to decode a certificate: `openssl x509 -in cert.pem -text -noout`.
- **The Certificate Ecosystem:** The chain of trust: Root CA (self-signed, stored in browser/OS trust stores) → Intermediate CA (signed by the Root) → End-entity Certificate (signed by the Intermediate). The operational problem: if the Intermediate CA certificate is not served by the web server (incomplete chain), browsers that have cached the Intermediate will succeed while those that haven't will fail — an intermittent, client-dependent outage that is notoriously difficult to diagnose. The lecture covers the standard Root CA programmes: Mozilla (Firefox), Microsoft (Windows/Edge), Apple (iOS/macOS/Safari), Google (Chrome/Android).
- **TLS Best Practices in 2040:** The Mozilla SSL Configuration Generator as the authoritative source for server configuration. Modern cipher suites: TLS 1.3 only (`TLS_AES_256_GCM_SHA384`, `TLS_CHACHA20_POLY1305_SHA256`). Key exchange: ECDHE with Curve25519 or P-256. Certificate type: ECDSA (faster, smaller) or RSA 2048-bit minimum. HSTS (`Strict-Transport-Security` header with `max-age=31536000; includeSubDomains; preload`) to prevent downgrade attacks. OCSP stapling (the server includes a time-stamped OCSP response in the TLS handshake, eliminating the client's need to query the CA separately). The 2040 development: post-quantum TLS (CRYSTALS-Kyber for key exchange, CRYSTALS-Dilithium for signatures) is being deployed on experimental networks under the name "PQ/TLS hybrid" — combining classical and post-quantum algorithms to hedge against both current and future attacks.
- **Common TLS Failures:** Expired certificates (the most frequent cause of TLS outages). Mismatched SANs (the certificate covers `example.com` but not `www.example.com`). Incomplete certificate chains. Revoked certificates (OCSP responder unreachable → browsers hard-fail or soft-fail depending on implementation). Weak cipher suites (a server configured to accept `TLS_RSA_WITH_RC4_128_SHA` — vulnerable to the RC4 biases attack). The lecture includes real incident reports: the 2024 Let's Encrypt mass revocation (3 million certificates revoked in 24 hours due to a CAA checking bug), the 2031 DigiNotar-style CA compromise at a regional Asian CA, and the 2038 global shift to post-quantum certificates.

#### Lecture Notes

TLS is simultaneously the most important security protocol on the internet and the source of some of its most embarrassing outages. The IT professional's TLS responsibility is not cryptographic design but operational discipline: monitoring certificate expiry (automated with `certbot`, Caddy, or ACME clients — manual certificate renewal is a professional failure in 2040), enforcing modern configurations, and diagnosing TLS failures quickly.

The lecture's diagnostic exercise: students are given a server with a deliberately misconfigured TLS setup (expired certificate, missing intermediate, weak cipher) and must identify all issues using `openssl s_client`, `testssl.sh`, and the Mozilla Observatory.

A sobering fact: the median time to detect a TLS certificate expiry is 2.3 hours for organisations with monitoring and 17 hours for those without. The outage itself — the moment users see "Your connection is not private" — is instantaneous. The difference between a 5-minute outage (automated monitoring + automated renewal) and a 17-hour outage (neither) is the difference between professional IT and amateur hour.

#### Required Reading

- Rescorla, E. (2018). *The Transport Layer Security (TLS) Protocol Version 1.3*. RFC 8446.
- Barnes, R. et al. (2035). *Automatic Certificate Management Environment (ACME)*. RFC 8555.
- Mozilla Wiki. "Security/Server Side TLS" — the definitive configuration guide at `wiki.mozilla.org/Security/Server_Side_TLS`.
- Qualys SSL Labs. "SSL Server Test" — test any public HTTPS endpoint at `ssllabs.com/ssltest/`.

#### Discussion Questions

1. TLS 1.3 encrypts the server's certificate in the handshake, preventing passive observers from seeing which domain the client is connecting to (Encrypted ClientHello / ECH). SNI encryption has been a goal since 2018 but faced significant deployment barriers. Describe the operational challenges of encrypting SNI. If SNI is encrypted, how do CDNs and load balancers route requests to the correct backend?
2. The Web PKI relies on approximately 150 trusted Root CAs operated by organisations worldwide. Any one of them can issue a certificate for any domain. How does Certificate Transparency (RFC 6962, mandatory in Chrome since 2015) provide accountability for this trust model?
3. Your monitoring system alerts that a TLS certificate expires in 7 days. The ACME client's automatic renewal has failed, and the error log shows "rate limit exceeded" from Let's Encrypt. Diagnose the root cause and describe your remediation plan. What operational practices would prevent this scenario?

---

### Lecture 7: REST APIs — Design, Consumption, and Operation

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

#### Overview

REST (Representational State Transfer) is the architectural style that dominates web APIs in 2040. Defined by Roy Fielding in his 2000 doctoral dissertation, REST has evolved from a theoretical model to the practical backbone of service-to-service communication. This lecture covers: the principles of REST (resources, representations, statelessness, hypermedia), the operational patterns for consuming REST APIs (authentication, pagination, error handling, rate limit management), and the tools (`curl`, `httpie`, Postman/Insomnia, `jq` for JSON processing) that IT professionals use daily.

#### Key Topics

- **REST Principles:** The six architectural constraints: Client-Server (separation of concerns), Stateless (each request contains all necessary information — no server-side session state), Cacheable (responses must declare whether they can be cached), Uniform Interface (resources identified by URIs, manipulated through representations), Layered System (intermediaries — proxies, gateways — are invisible to the client), and Code-on-Demand (optional — servers can extend client functionality by sending executable code, e.g., JavaScript). The lecture emphasises: REST is not "JSON over HTTP." A JSON API that requires the client to maintain state (e.g., a session ID that must be sent with every request) violates the statelessness constraint and is not RESTful.
- **Resource Design:** Resources are nouns, not verbs. `/users` (collection), `/users/42` (individual resource), `/users/42/orders` (sub-collection). HTTP methods map to CRUD operations: GET (read), POST (create), PUT (replace), PATCH (partial update), DELETE (remove). Common anti-patterns: `/getUsers`, `/createOrder` (verbs in URLs), `/users?id=42` instead of `/users/42`, and using POST for every operation. The lecture covers the Richardson Maturity Model (Level 0: single URI, single method; Level 1: multiple URIs, single method; Level 2: multiple URIs, multiple methods — this is where most "REST" APIs actually live; Level 3: hypermedia controls / HATEOAS).
- **API Authentication:** The methods IT professionals encounter: API keys (simple, passed as header or query parameter — `X-API-Key: abc123`), HTTP Basic Authentication (Base64-encoded username:password — only acceptable over TLS), Bearer tokens (OAuth 2.0 — `Authorization: Bearer eyJhbGci...`), and mutual TLS (mTLS — both client and server present certificates, used for high-security service-to-service communication). The lecture covers OAuth 2.0 flows: Client Credentials (service-to-service — client ID + secret exchanged for an access token), Authorization Code (user-facing applications — the user authenticates at the authorisation server, the client receives an authorisation code, exchanges it for tokens), and the PKCE extension (Proof Key for Code Exchange — prevents authorisation code interception attacks, mandatory for mobile and single-page applications in 2040).
- **Consuming APIs:** The operational patterns for calling REST APIs from scripts. Using `curl` for ad-hoc requests and debugging. Using `httpie` for human-readable API interaction. Structured HTTP client libraries (Python's `httpx` or `requests`, Bash's `curl` with `jq`, PowerShell's `Invoke-RestMethod`). Handling pagination (offset-based, cursor-based, and Link header-based), rate limiting (exponential backoff with jitter), and error responses (retrying on 429 and 5xx, failing on 4xx). The lecture includes a lab: write a Python script that paginates through the GitHub API, collecting all repositories for an organisation, respecting rate limits, and outputting a CSV of repository names, star counts, and last-push dates.
- **API Versioning:** The eternal debate: URL versioning (`/v1/users`, `/v2/users`), header versioning (`Accept: application/vnd.yggdrasil.v2+json`), and query parameter versioning (`/users?version=2`). The lecture analyses the trade-offs and presents the University of Yggdrasil's API versioning standard (URL-based major version, header-based minor version), explaining why breaking changes require a new major version and how to maintain backward compatibility during transitions.

#### Lecture Notes

The IT professional's relationship with APIs is operational: consuming them, monitoring them, and troubleshooting them. When an API integration fails, the diagnostic process follows the OSI model from the bottom up: Can I reach the server? (`ping`). Is the port open? (`nc -zv`). Is TLS working? (`openssl s_client`). Is HTTP responding? (`curl -v`). Is the API returning errors? (`curl` with full output). Is the authentication token valid? (decode the JWT with `jq -R 'split(".") | .[1] | @base64d | fromjson'`). Is the response body what I expected? (`jq` to inspect structured data).

The lecture introduces the concept of "API empathy" — the ability to read an API documentation page and construct a mental model of the system behind it. What are the rate limits? What are the error responses? Is there a sandbox? What happens when I paginate to the end? An IT professional who can answer these questions without writing a single line of code is more valuable than one who can only follow a tutorial.

#### Required Reading

- Fielding, R.T. (2000). *Architectural Styles and the Design of Network-based Software Architectures*. Doctoral dissertation, UC Irvine. Chapter 5 (Representational State Transfer).
- Richardson, L. & Amundsen, M. (2035). *RESTful Web APIs*, 2nd Edition. O'Reilly Media. Chapters 1–5.
- Hardt, D. (2012). *The OAuth 2.0 Authorization Framework*. RFC 6749.
- GitHub REST API Documentation (2040). "Pagination," "Rate Limiting," and "Authentication."

#### Discussion Questions

1. Roy Fielding's original definition of REST requires hypermedia as the engine of application state (HATEOAS). Almost no API commonly described as "RESTful" implements HATEOAS. Does this mean most "REST" APIs are not actually REST? If they're not REST, what are they, and why did the simplified form win over the purist vision?
2. A third-party API you depend on changes its response format (a field you parse is renamed from `user_name` to `displayName`). Your integration breaks. Design an API consumption pattern that would have detected this change before deployment and prevented the outage.
3. OAuth 2.0's Client Credentials flow uses a client secret that must be stored securely. Compare the security properties of storing this secret: in environment variables, in a secrets manager (HashiCorp Vault, AWS Secrets Manager), and in a hardware security module (HSM). For each, describe the threat model and mitigation.

---

### Lecture 8: GraphQL, gRPC, and the Post-REST API Landscape

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

#### Overview

REST dominates, but it is not the only API paradigm in 2040. GraphQL (Facebook, 2015) addresses REST's over-fetching and under-fetching problems by letting clients specify exactly the data they need. gRPC (Google, 2015) addresses REST's performance limitations with binary Protocol Buffers serialisation, HTTP/2 multiplexing, and bidirectional streaming. This lecture compares the three paradigms, teaching IT professionals when to choose each and how to operate them in production.

#### Key Topics

- **GraphQL — Client-Driven Queries:** GraphQL's fundamental insight: the client, not the server, defines the shape of the response. A single `/graphql` endpoint accepts queries that specify fields, nested objects, and arguments. The lecture demonstrates: a GraphQL query that retrieves user profiles with their recent orders (a single request replacing three REST calls to `/users/42`, `/users/42/orders`, and `/orders/42/items`). The GraphQL type system: schemas (defined in SDL — Schema Definition Language), types (Object, Scalar — String, Int, Float, Boolean, ID — Enum, Input, Interface, Union), queries (read), mutations (write), and subscriptions (real-time via WebSockets). The operational challenges: the N+1 problem (a naive resolver fetches each author for a list of books individually, producing N+1 database queries — solved by Facebook's DataLoader batching pattern), query depth attacks (a malicious client sends a deeply nested query that exhausts server resources — mitigated by query cost analysis and depth limits), and caching (GraphQL's single-endpoint design breaks HTTP caching — solved by persisted queries and CDN-level GraphQL caching like Apollo GraphOS).
- **gRPC — High-Performance Service Communication:** gRPC uses Protocol Buffers (protobuf) as its Interface Definition Language (IDL) and serialisation format. A `.proto` file defines service methods and message types, compiled into client and server stubs in 12+ languages. Advantages over REST: binary serialisation (10–100× smaller payloads, 3–10× faster parsing than JSON), strong typing (compile-time guarantees for message structure), bidirectional streaming (client streaming, server streaming, bidirectional streaming — impossible with REST), and built-in deadlines/cancellation (every gRPC call carries a timeout, propagated through the call chain). The lecture demonstrates: a protobuf definition for a log aggregation service, compiled to Python and Go stubs, with streaming log ingestion.
- **Comparison and Selection:** When to use each. REST: public APIs, simple CRUD, broad client compatibility, caching requirements (CDN-friendly). GraphQL: complex UIs (mobile apps, SPAs) where multiple views need different slices of the same data, rapidly evolving frontend requirements, strong typing benefit. gRPC: internal microservice communication, high-throughput data pipelines, real-time streaming, polyglot environments. The lecture includes a decision matrix: latency sensitivity, payload complexity, client diversity, team expertise, and tooling maturity.
- **WebSockets and Real-Time Communication:** WebSockets (RFC 6455) provide a full-duplex, persistent connection between browser and server — the foundation of chat, live collaboration, gaming, and financial data feeds. The WebSocket handshake: an HTTP Upgrade request (`Connection: Upgrade`, `Upgrade: websocket`) that transitions to the WebSocket protocol. The operational concerns: connection management (reconnection with exponential backoff), authentication (token in initial handshake or first message), and the challenge of WebSocket-aware load balancers (sticky sessions or a dedicated WebSocket tier). The 2040 alternative: WebTransport (based on QUIC), providing multiplexed streams, unreliable datagrams, and partial reliability — the future of real-time web communication.

#### Lecture Notes

The API paradigm debate — REST vs. GraphQL vs. gRPC — is one of the most energetic in modern IT. The lecture's position: there is no single right answer; there is only the right answer for your context. GraphQL's flexibility comes at the cost of operational complexity (query depth attacks, cache invalidation). gRPC's performance comes at the cost of debuggability (binary protocols are opaque to `curl`). REST's simplicity comes at the cost of over-fetching and multiple round-trips.

The IT professional's role is not to champion one paradigm but to operate all of them competently. A 2040 infrastructure might serve a GraphQL API to mobile clients (reducing mobile data usage), gRPC between internal services (minimising latency), and REST for third-party integrations (maximising compatibility). The nginx reverse proxy configured in Lecture 5 routes requests to the appropriate backend based on path and content type.

The Norse metaphor: the API landscape is a set of tools in a smithy. GraphQL is the fine chisel — precise but requiring skill to avoid damage. gRPC is the power hammer — fast and forceful but needing careful setup. REST is the anvil — simple, reliable, and the foundation upon which everything else is built.

#### Required Reading

- GraphQL Foundation (2040). *GraphQL Specification*. October 2021 Edition. Sections 1–5.
- Google (2040). *gRPC Documentation*. "Core Concepts," "Protocol Buffers," and "Streaming."
- Fette, I. & Melnikov, A. (2011). *The WebSocket Protocol*. RFC 6455.
- Buecheler, C. (2038). *GraphQL in Production*. O'Reilly Media. Chapters on security, caching, and performance.

#### Discussion Questions

1. GraphQL's N+1 problem is a direct consequence of its resolver architecture. Explain the N+1 problem with a concrete example. How does Facebook's DataLoader pattern solve it, and what are its limitations?
2. gRPC uses HTTP/2 trailers to communicate status codes and error details. If your network infrastructure strips HTTP trailers (some legacy proxies do), gRPC calls will fail silently. How would you diagnose this failure, and what operational changes would prevent it?
3. A real-time dashboard uses WebSockets to push updates to 10,000 concurrent browsers. Each browser maintains an open WebSocket connection. Describe the server architecture required to handle this load. Compare: a single-threaded event-driven server (Node.js), a thread-per-connection server (Java with virtual threads), and a dedicated WebSocket-as-a-Service provider. What are the trade-offs?

---

### Lecture 9: CDNs, Caching, and Edge Computing

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

#### Overview

Content Delivery Networks (CDNs) serve approximately 72% of global web traffic in 2040. They are no longer optional — they are the standard deployment architecture for any web property serving a global audience. This lecture covers: CDN architecture (edge servers, regional caches, origin shielding), caching strategies (TTL-based, validation-based, and surrogate keys for cache invalidation), and the 2040 expansion of CDNs into edge computing platforms (Cloudflare Workers, Fastly Compute@Edge, AWS Lambda@Edge) that run application code at the network edge.

#### Key Topics

- **CDN Architecture:** The physical reality: a CDN is hundreds of thousands of servers distributed across thousands of points of presence (PoPs) worldwide. When a user in Tokyo requests `yggdrasil.edu`, the DNS resolves to the nearest CDN edge server (Tokyo PoP). If the content is cached, it's served from Tokyo with sub-millisecond latency. If not, the edge server requests it from the origin server (perhaps in Reykjavík), caches the response, and serves it to the user. Subsequent requests from Tokyo are served from cache. The lecture covers: anycast routing (how DNS directs users to the nearest PoP), tiered caching (edge → regional → origin — reducing origin load by aggregating cache misses), and origin shielding (a designated cache node that all edge servers query before hitting the origin, preventing the "thundering herd" of cache fill requests).
- **Caching Strategies:** The cache-control directives from Lecture 3 applied at CDN scale. `Cache-Control: public, max-age=3600, s-maxage=86400` (browsers cache for 1 hour; CDN caches for 24 hours). `Cache-Control: no-cache` (validate with origin before serving — the CDN sends a conditional request with `If-None-Match`/`If-Modified-Since` on every client request). `Cache-Control: private` (CDN must not cache; browser may cache). The operational art: choosing TTLs that balance freshness (users see up-to-date content) against origin load (every cache miss hits your application servers). The lecture includes the "cache stampede" problem: when a popular cached resource expires, thousands of simultaneous requests all miss the cache and hit the origin simultaneously — solved by "stale-while-revalidate" (`Cache-Control: max-age=600, stale-while-revalidate=30` — serve stale content while asynchronously refreshing).
- **Cache Invalidation:** The hardest problem in computer science (along with naming things and off-by-one errors). CDN purging: `PURGE /images/hero.jpg` (remove a specific URL from all edge caches), wildcard purging (`/images/*`), and surrogate keys (tag-based invalidation: tag a response with `Surrogate-Key: article-42 homepage`; purge by key rather than URL). The lecture covers: why purging is not instantaneous (global propagation takes seconds to minutes), the difference between "soft purge" (mark as stale — next request triggers a background refresh) and "hard purge" (remove immediately — next request blocks until origin responds), and the strategy of cache-busting URLs (`/app.js?v=abc123`) for immutable assets.
- **Edge Computing:** The 2040 paradigm: CDNs are no longer just caches; they are distributed application platforms. Cloudflare Workers, Fastly Compute@Edge, Deno Deploy, and AWS Lambda@Edge run JavaScript/WebAssembly at every PoP. Use cases: A/B testing (route users to different backends based on cookies — at the edge, not at the origin), authentication at the edge (validate JWT tokens before requests reach the origin), personalisation (inject user-specific content into cached HTML), bot management (challenge suspicious requests at the edge), and API gateways (route, transform, and rate-limit API requests at the edge). The lecture includes a lab: write a Cloudflare Worker that geolocates the user's IP, returns a greeting in their local language, and caches the response for 1 hour.
- **The 2040 CDN Landscape:** The major providers: Cloudflare (38% market share, integrated edge compute, DDoS protection, DNS), Akamai (22%, enterprise-focused, largest network), Fastly (12%, real-time purging, edge compute), AWS CloudFront (15%, integrated with AWS ecosystem), and emerging regional CDNs (Alibaba Cloud CDN, Tencent Cloud CDN, Yandex CDN). The lecture discusses vendor lock-in, multi-CDN strategies (using DNS to route between multiple CDNs for resilience), and the environmental impact of CDN infrastructure (CDN PoPs consume approximately 0.3% of global electricity — comparable to a mid-sized country).

#### Lecture Notes

The CDN is the IT professional's force multiplier. A properly configured CDN can absorb a DDoS attack that would overwhelm any origin server, serve content to users on every continent with LAN-like latency, and reduce infrastructure costs by 60–90% (cached content never touches your application servers). But a misconfigured CDN can cache sensitive data (a `Cache-Control: public` on a page containing personal information), fail open (serve stale content indefinitely), or become a single point of failure (when your CDN goes down, your entire web presence goes down).

The lecture's operational exercise: students configure CloudFront for a static website, set up cache behaviours for HTML (short TTL), CSS/JS (long TTL with cache-busting), and images (immutable — 1 year TTL), implement origin shield, and test cache invalidation with `aws cloudfront create-invalidation`.

The Norse metaphor: the CDN is the network of waystations along the Viking trade routes — Kaupang, Hedeby, Birka, Dublin, York. A trader doesn't sail back to the fjord for every transaction; goods are cached at the waystations. The origin server is the home fjord — it holds the source of truth, but the world interacts with the caches.

#### Required Reading

- Cloudflare Learning Center (2040). "What is a CDN?" and "How CDNs Work."
- Amazon CloudFront Documentation (2040). "Managing How Long Content Stays in the Cache" and "Cache Key and Origin Shield."
- Nottingham, M. (2035). *HTTP Caching*. RFC 9111. Sections 3–5.
- Souders, S. (2037). *Even Faster Web Sites*, 3rd Edition. O'Reilly Media. Chapters on CDN deployment.

#### Discussion Questions

1. A CDN caches a page containing `Cache-Control: public, max-age=86400`. Twenty minutes later, a critical error is discovered on the page and must be fixed immediately. Describe three methods for removing the cached content, ordered from fastest to slowest. For each, explain the propagation delay.
2. Edge computing blurs the line between CDN and application server. If your authentication logic runs at the edge (validating JWT tokens in a Cloudflare Worker), what happens when the Worker platform experiences an outage? Design a fallback architecture.
3. A multi-CDN strategy routes users to different CDNs via DNS (e.g., `cdn1.yggdrasil.edu` → Cloudflare, `cdn2.yggdrasil.edu` → Fastly). How do you ensure cache consistency across CDNs? If a purge request is sent to one CDN but not the other, users routed to the un-purged CDN will see stale content. Propose a solution.

---

### Lecture 10: Web Security — OWASP Top 10 and Operational Defences

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

#### Overview

Web application security is not a feature; it is a property of every architectural decision. The OWASP Top 10 — updated every four years — catalogues the most critical web application security risks. This lecture covers the 2040 edition of the Top 10 from an operational perspective: not just what the vulnerabilities are, but how IT professionals configure web servers, reverse proxies, and CDNs to mitigate them. Students deploy a deliberately vulnerable application and harden it using the defensive patterns covered.

#### Key Topics

- **OWASP Top 10 (2040 Edition):** 1. Broken Access Control (users accessing other users' data by manipulating URLs or API parameters). 2. Cryptographic Failures (weak TLS, hardcoded keys, unencrypted sensitive data). 3. Injection (SQL, NoSQL, OS command, LDAP — untrusted data interpreted as code). 4. Insecure Design (missing security requirements, no threat modelling). 5. Security Misconfiguration (default credentials, verbose error messages, unnecessary features enabled). 6. Vulnerable and Outdated Components (unpatched libraries with known CVEs). 7. Identification and Authentication Failures (weak password policies, credential stuffing, missing MFA). 8. Software and Data Integrity Failures (CI/CD pipeline compromise, unsigned updates, deserialisation of untrusted data). 9. Security Logging and Monitoring Failures (no detection of active attacks — breaches go unnoticed for months). 10. Server-Side Request Forgery (SSRF — the server fetches a URL controlled by an attacker, accessing internal services).
- **Reverse Proxy Defences (Lecture 5 applied to security):** The reverse proxy as a security enforcement point. `limit_req` and `limit_conn` (rate limiting — prevent brute-force attacks and credential stuffing). Custom error pages (`error_page 500 502 503 504 /50x.html` — avoid leaking stack traces and framework versions). Security headers: `Strict-Transport-Security` (force HTTPS), `Content-Security-Policy` (restrict which scripts can execute — the most powerful defence against XSS), `X-Frame-Options: DENY` (prevent clickjacking), `X-Content-Type-Options: nosniff` (prevent MIME type sniffing), `Referrer-Policy: strict-origin-when-cross-origin` (control referrer leakage). The lecture includes a complete nginx security configuration that implements all of these.
- **WAF (Web Application Firewall):** A WAF inspects HTTP requests and blocks those matching attack patterns — SQL injection (`' OR 1=1 --`), XSS (`<script>alert(1)</script>`), path traversal (`../../etc/passwd`). ModSecurity (open-source, rule-based — OWASP Core Rule Set), Cloudflare WAF (managed, machine-learning-driven), and AWS WAF (integrated with CloudFront/ALB). The lecture covers: WAF limitations (bypass techniques, false positives that block legitimate traffic, the performance cost of inline inspection), WAF logging (every blocked request should generate an alert — a blocked SQL injection attempt is an incident, not just a statistic), and the operational practice of WAF rule tuning (starting in "detect-only" mode, analysing logs, and progressively enabling blocking).
- **CORS (Cross-Origin Resource Sharing):** CORS is the mechanism by which browsers allow a web page from `example.com` to make requests to `api.other.com`. Without CORS, the Same-Origin Policy would block all cross-origin requests. The CORS headers: `Access-Control-Allow-Origin` (which origins can access the resource — `*` is dangerous and incompatible with credentials), `Access-Control-Allow-Methods`, `Access-Control-Allow-Headers`, `Access-Control-Allow-Credentials` (allow cookies — requires a specific origin, not `*`), `Access-Control-Max-Age` (cache the preflight response). The lecture covers: the preflight request (OPTIONS) that browsers send before cross-origin requests with non-simple methods or headers, the common misconfiguration of reflecting the `Origin` header verbatim without validation (effectively a wildcard), and the operational pattern of maintaining a CORS allowlist.
- **The 2040 Threat Landscape:** AI-driven attacks (language models generating convincing phishing pages, automated vulnerability scanning at internet scale), supply chain attacks (compromised npm packages, poisoned Docker images — the lesson of the 2034 Polyfill.io incident), and quantum threats (Shor's algorithm will break RSA and ECC — the migration to post-quantum cryptography is the largest cryptographic transition in internet history). The lecture frames security not as a product but as a continuous practice: patch, monitor, respond, learn, repeat.

#### Lecture Notes

The most important security principle in IT operations is "defence in depth" — no single layer of defence should be your only layer. A WAF is not a substitute for input validation. TLS is not a substitute for authentication. A firewall is not a substitute for least-privilege access control. Every security control can fail; the system must survive the failure of any single control.

The lecture's central practical exercise: students are given a Docker Compose environment containing a vulnerable web application (OWASP Juice Shop) and must harden it using: an nginx reverse proxy with security headers and rate limiting, TLS with a valid certificate, a ModSecurity WAF with the OWASP Core Rule Set, and application-level fixes for the three most severe vulnerabilities. The evaluation is a penetration test conducted by the instructor's automated scanner.

The Norse metaphor: security is not a wall but a longhouse. The longhouse has a door (authentication), a hearth that burns only authorised wood (authorisation), walls that keep out the wind and wolves (firewall/WAF), and a watchman who stays awake through the night (monitoring/logging). A single layer — a door with no walls — is no defence at all.

#### Required Reading

- OWASP Foundation (2040). *OWASP Top 10 — 2040 Edition*. Full document at `owasp.org/Top10`.
- OWASP Foundation (2040). *ModSecurity Core Rule Set*. Documentation and rule descriptions.
- Mozilla Observatory (2040). "HTTP Security Headers." Interactive testing tool at `observatory.mozilla.org`.
- NIST Special Publication 800-207 (2035). "Zero Trust Architecture." The architectural framework for defence in depth.

#### Discussion Questions

1. A WAF blocks a request containing `' OR 1=1 --` in a query parameter. Is this a false positive (a legitimate user whose input happens to contain those characters) or a true positive (an actual SQL injection attempt)? How would you determine which? What operational process should follow a WAF block?
2. `Content-Security-Policy` can prevent XSS by restricting which scripts can execute. But many real-world applications use inline scripts (`<script>...</script>`) that CSP blocks by default. Describe how to deploy CSP in a legacy application without rewriting the entire codebase. What are `'nonce-...'` and `'strict-dynamic'`, and how do they help?
3. The 2040 shift to post-quantum cryptography requires replacing every TLS certificate and every cryptographic library. Estimate the operational timeline for this transition in an organisation with 5,000 servers. What breaks first? What requires the longest lead time?

---

### Lecture 11: Internet Governance, Standards, and the Open Web

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

#### Overview

The internet is not a technical artefact alone; it is a socio-technical system governed by a complex ecosystem of standards bodies, non-profits, corporations, and governments. This lecture surveys the institutions that define the internet: the Internet Engineering Task Force (IETF — protocols, RFCs), the World Wide Web Consortium (W3C — web standards), the Internet Corporation for Assigned Names and Numbers (ICANN — domain names and IP addresses), the Internet Society (ISOC), and the regional Internet registries (RIRs — ARIN, RIPE NCC, APNIC, LACNIC, AFRINIC). The lecture also covers the political contestation over internet governance: the "splinternet" (national internets in China, Russia, Iran), net neutrality, and the 2040 debate over AI-generated content and the web.

#### Key Topics

- **The IETF and the RFC Process:** The IETF is not a membership organisation; it is an open community of engineers who produce RFCs (Request for Comments) through a process of working groups, draft proposals, and "rough consensus and running code." The lecture traces the lifecycle of an RFC: an individual draft → working group adoption → revisions based on mailing list discussion → last call → IESG review → publication as Proposed Standard → implementation experience → Internet Standard. Notable examples: RFC 2616 (HTTP/1.1) → RFC 7230-7235 (HTTP/1.1 revision) → RFC 9110-9114 (HTTP semantics, caching, HTTP/2, HTTP/3). The lecture highlights: RFCs are not imposed by authority; they succeed because implementers voluntarily adopt them.
- **W3C and Web Standards:** The W3C produces Recommendations that define web technologies: HTML, CSS, DOM, Web APIs, accessibility (WCAG), and the Web of Things. The standardisation process: Working Draft → Candidate Recommendation → Proposed Recommendation → W3C Recommendation. The lecture covers the 2040 W3C priorities: WebGPU (hardware-accelerated 3D graphics in the browser), WebAssembly (near-native performance for compiled languages in the browser), the Spatial Web (WebXR for augmented and virtual reality), and the ethical web (privacy, accessibility, internationalisation).
- **ICANN and the Domain Name System:** ICANN manages the root zone of the DNS, coordinates IP address allocation with the IANA (Internet Assigned Numbers Authority), and accredits domain registrars. The lecture covers the political structure of ICANN (multi-stakeholder model — governments, business, civil society, technical community), the process for creating new gTLDs (the 2012 round added 1,200+ new TLDs including `.guru`, `.ninja`, `.xyz`; the 2035 round added `.ai`, `.cloud`, `.dao`), and the ongoing tension between ICANN's US-based legal status and demands for international governance (the "IANA stewardship transition" of 2016, the WCIT debates).
- **The Splinternet:** The fragmentation of the global internet. China's Great Firewall (DNS poisoning, IP blocking, deep packet inspection, and the 2040 "Golden Shield 3.0" AI-powered censorship system). Russia's Sovereign Internet Law (2019, mandating the ability to disconnect from the global internet — exercised for 24 hours in a 2032 test). Iran's National Information Network. The lecture analyses: the technical mechanisms of internet fragmentation (BGP manipulation, DNS filtering, mandatory VPN blocks, state-mandated root CA certificates for TLS interception), the economic costs (fragmented internets cannot benefit from global network effects), and the human rights implications (the UN declared internet access a human right in 2016; fragmented internets selectively deny that right).
- **Net Neutrality and the 2040 Debate:** Net neutrality — the principle that internet service providers should treat all data equally, without blocking, throttling, or paid prioritisation — has been a policy battlefield for decades. The lecture traces the history: the FCC's 2015 Open Internet Order, its 2017 repeal, the 2024 restoration under the "Digital Commons Act," and the 2040 challenge of AI-traffic discrimination (ISPs prioritising their own AI services' traffic while throttling competitors). The technical reality: even with net neutrality regulations, CDN interconnection agreements (paid peering) create a de facto two-tier internet.

#### Lecture Notes

The IT professional cannot be merely technical. The protocols you configure, the standards you implement, and the networks you build exist within a governance framework that is the product of decades of political negotiation. Understanding who decides what `.com` means, how an RFC becomes a standard, and why your users in certain countries cannot reach your servers is as essential as understanding TCP handshakes.

The lecture's perspective: the internet is an example of one of the most successful examples of global governance in human history — a system that connects 5.5 billion people in 2040, operates across every border, and has survived wars, pandemics, and political upheaval. Its resilience is not accidental; it is a product of architectural choices (the end-to-end principle, permissionless innovation) and institutional choices (open standards, multi-stakeholder governance). The IT professional inherits this legacy and bears responsibility for its continuation.

The Norse metaphor: the internet is the modern Althing — the open assembly where all voices can be heard, governed by laws (protocols), presided over by lawspeakers (standards bodies), and sustained by the collective commitment to the process. A fragmented internet is the dissolution of the Althing into isolated chiefdoms.

#### Required Reading

- Russell, A.L. (2035). *Open Standards and the Digital Age: History, Ideology, and Networks*. Cambridge University Press. Chapters 6–8.
- Mueller, M. (2032). *Networks and States: The Global Politics of Internet Governance*. MIT Press. Chapters 1–4, 9.
- DeNardis, L. (2038). *The Internet in Everything: Freedom and Security in a World with No Off Switch*. Yale University Press. Chapters on splinternet and sovereignty.
- ICANN (2040). "What Does ICANN Do?" Introductory guide at `icann.org`.

#### Discussion Questions

1. The IETF's motto is "rough consensus and running code." Contrast this with the ITU's formal voting process (one country, one vote). What are the strengths and weaknesses of each approach for developing technical standards?
2. The "right to be forgotten" (EU GDPR, 2018) requires search engines to delist certain results. A court in one country orders a global delisting. Another country argues this is extraterritorial censorship. How should a global internet service resolve this conflict? What technical mechanisms exist for geo-limited content restrictions?
3. Your organisation's web application is blocked in a country that has mandated state-controlled root CA certificates for TLS interception. Users in that country are presented with a certificate warning when accessing your site. What are your options? Analyse the security, ethical, and business implications of each.

---

### Lecture 12: The 2040 Web — WebAssembly, Edge AI, and the Decentralised Frontier

**Course:** IT107 — Web Technologies & Internet Architecture  
**Degree:** Bachelor of Science in Information Technology, University of Yggdrasil, 2040

---

#### Overview

The web of 2040 is not the web of 2020. Three transformations define the decade: WebAssembly (Wasm) has broken the browser's language monopoly, enabling near-native performance for applications written in any compiled language. Edge AI runs machine learning inference at CDN PoPs and in browsers themselves, personalising experiences without sending data to centralised servers. And the decentralised web — IPFS, Solid, blockchain-based identity — challenges the platform concentration that defined the 2010s and 2020s. This final lecture surveys the frontier and asks students to imagine the web of 2050.

#### Key Topics

- **WebAssembly — The Browser as Universal Runtime:** WebAssembly (Wasm) is a binary instruction format that runs at near-native speed in the browser, alongside JavaScript. By 2040, Wasm has expanded beyond the browser: Wasm runtimes (Wasmtime, Wasmer, WasmEdge) execute Wasm modules on servers, edge devices, and embedded systems. The lecture covers: Wasm's security model (sandboxed execution with capability-based access — a Wasm module cannot access the filesystem, network, or OS unless explicitly granted), the Component Model (a standard for composing Wasm modules written in different languages — a Rust module for image processing called from a Python module for orchestration), and Wasm on the server (replacing Docker containers for some workloads — Wasm modules start in microseconds vs. seconds for containers, with stronger isolation guarantees). The practical demonstration: compile a C program to Wasm with Emscripten and run it in the browser and on the server.
- **Edge AI — Intelligence at the Periphery:** Machine learning models running at CDN edges (Cloudflare Workers AI, Fastly Compute@Edge ML) and in browsers (WebGPU-accelerated inference with Transformers.js or ONNX Runtime Web). Use cases: real-time content moderation (classifying uploaded images at the edge before they reach the origin), personalisation (inferring user preferences from local behaviour without sending data to servers), and assistive AI (real-time translation, text-to-speech, speech-to-text in the browser — no cloud API calls). The lecture covers the architectural implications: edge AI reduces latency (no round-trip to a central inference server), reduces bandwidth (raw data — images, audio — stays at the edge; only metadata is sent), and enhances privacy (sensitive data never leaves the user's device or the trusted edge). The operational challenge: model deployment at the edge requires synchronising model versions across hundreds of PoPs — the same problem as CDN cache invalidation, but for gigabytes of model weights.
- **The Decentralised Web:** A reaction against the platform concentration of the 2010s–2020s (Google, Meta, Amazon controlling the majority of web traffic and data). Three paradigms: IPFS (InterPlanetary File System) — content-addressed storage where files are identified by their cryptographic hash, not their location; Solid (Social Linked Data, Tim Berners-Lee's project) — users store their data in "pods" they control, granting applications access rather than surrendering data to platforms; and blockchain-based identity (self-sovereign identity using decentralised identifiers — DIDs — and verifiable credentials). The lecture analyses the adoption gap: these technologies exist and are technically functional, but network effects favour centralised platforms. The 2040 question: will regulation (the EU's Digital Markets Act, the US's DATA Act) succeed in forcing interoperability where market forces have not?
- **The Web of 2050 — Student Speculations:** The final segment of the lecture is interactive. Students are asked to propose and defend a vision of the web in 2050 based on current trends. Past student predictions that proved prescient: "By 2035, most web content will be generated by AI" (a 2025 prediction), "HTTP/3 will replace TCP for all user-facing traffic" (a 2020 prediction), and "TLS will be mandatory for all HTTP traffic" (a 2014 prediction, achieved by 2020). The lecture closes with the instructor's own prediction: by 2050, the distinction between "the web" and "computing" will dissolve. The browser will be the operating system; the CDN will be the data centre; the API will be the file system.

#### Lecture Notes

The unifying theme of the 2040 web is the movement of computation toward the user. In the 2000s, computation happened on the server; the browser was a thin client rendering HTML. In the 2010s–2020s, JavaScript SPA frameworks moved logic to the browser. In the 2030s–2040s, WebAssembly and edge computing have continued this trajectory: the user's device and the CDN edge node are not just rendering surfaces but active computational participants.

This has profound implications for the IT professional. The infrastructure you manage is no longer a cluster of servers in a data centre; it is a distributed mesh spanning user devices, CDN edges, regional caches, and central origins. Debugging a performance problem means tracing a request across four tiers of infrastructure, two protocol transitions (QUIC → HTTP/3 → gRPC → SQL), and three security contexts (browser sandbox, edge isolate, origin server).

The Norse closing: the web is not a destination but a journey — like the Viking voyages that connected the known world. The longships of the 2040s are QUIC packets; the navigational stars are DNS records; the trading posts are CDN PoPs. The IT professional is the navigator, understanding the winds and currents, maintaining the ship, and ensuring the cargo arrives. What new lands will the web discover by 2050? That question is yours to answer.

#### Required Reading

- Haas, A. et al. (2039). "Bringing the Web up to Speed with WebAssembly." *Communications of the ACM*, 62(12).
- Cloudflare Research (2040). "Edge AI: Running Machine Learning at the Network Edge." Technical report.
- Berners-Lee, T. (2035). "Solid: A Platform for Decentralised Social Applications." Technical specification.
- Benet, J. (2034). "IPFS: Content-Addressed, Versioned, P2P File System." *Proceedings of the IEEE*, 112(4).

#### Discussion Questions

1. WebAssembly's security model relies on capability-based sandboxing. Compare this to Docker's namespace-based isolation and to browser same-origin policies. Which provides the strongest isolation guarantee, and why?
2. Edge AI performs inference on user data at the CDN edge. The user's data never reaches a central server. Is this privacy-preserving, or does it merely shift trust from the application provider to the CDN provider? Analyse the threat model.
3. The original vision of the web (Tim Berners-Lee, 1989) was a decentralised, read-write information space. Thirty-five years of centralisation later, the decentralised web movement seeks to return to that vision. Is this technically achievable, or do network effects make platform concentration inevitable? Defend your answer with reference to specific technologies and economic forces.

---

## Final Examination Preparation

### Component A: Written Examination (60%)

Select **five** of the following eight questions. Each answer should demonstrate technical depth, operational reasoning, and the ability to connect concepts across multiple lectures.

1. **End-to-End Request Tracing:** A user in São Paulo reports that `yggdrasil.edu` takes 8 seconds to load. Trace the entire request lifecycle — from browser URL entry to fully rendered page — identifying every protocol, infrastructure component, and potential bottleneck. For each stage, specify the diagnostic tool you would use to measure latency and the normal expected time range. Distinguish between problems at the DNS layer, the TLS layer, the HTTP layer, the CDN layer, and the application layer.

2. **Protocol Evolution and Operational Impact:** HTTP has evolved from 1.0 (1996) through 1.1, 2, and now 3 (QUIC). For each major version transition, describe: (a) the key architectural change, (b) the operational problem it solved, (c) the new operational challenges it created, and (d) the changes required in IT infrastructure (firewalls, load balancers, monitoring tools). Conclude with an assessment of whether the web would be better or worse if we had stayed with HTTP/1.1 and optimised at higher layers.

3. **DNS Failure Scenario:** At 03:00 UTC, your monitoring system alerts that `api.yggdrasil.edu` is unreachable. The application servers are healthy, but DNS resolution returns SERVFAIL. Describe your diagnostic process step by step, including the specific `dig` commands you would run and what each output would tell you. Identify at least five distinct root causes that could produce this symptom, ordered from most to least likely. For each, describe the remediation.

4. **TLS Certificate Architecture:** You are responsible for TLS across 200 subdomains (`*.yggdrasil.edu`). Design a certificate management architecture that: provisions certificates automatically, monitors expiry with escalating alerts (30 days, 7 days, 24 hours), handles renewal failures gracefully, and supports both RSA and ECDSA certificates with automatic algorithm selection based on client capabilities. Include your choice of CA (Let's Encrypt, DigiCert, or private CA), ACME client, and validation method (HTTP-01 vs. DNS-01). Justify each choice.

5. **CDN and Cache Architecture:** A news organisation serves 50 million page views per day with a global audience. The homepage changes every 15 minutes; article pages are immutable after publication; images change rarely. Design the CDN caching strategy: specify `Cache-Control` headers for each content type, explain your choice of TTLs, describe the cache invalidation mechanism for homepage updates, and calculate the expected origin hit rate. Address the "thundering herd" problem for breaking news events when the homepage cache expires.

6. **API Security Architecture:** Design the security architecture for a REST API that serves both a mobile application (untrusted client) and internal microservices (trusted). Address: authentication (OAuth 2.0 flow selection and justification), authorisation (role-based access control with scopes), transport security (TLS configuration, certificate pinning considerations), rate limiting (per-user, per-IP, and global), and audit logging. For each layer, specify what would be implemented in the reverse proxy (nginx/Caddy) versus the application code, and justify that division.

7. **WAF Deployment:** Your organisation adopts a Web Application Firewall. Describe the deployment process from initial installation to full blocking mode: (a) initial configuration and rule selection (OWASP CRS vs. commercial rules), (b) the monitoring phase (what metrics to collect, how to identify false positives), (c) the progressive enablement strategy (which rules to enable first, how to escalate), and (d) the incident response process for a WAF-blocked attack. Include a discussion of WAF bypass techniques and how your architecture addresses them.

8. **The 2050 Web:** Based on the technologies and trends covered in this course — QUIC, WebAssembly, edge computing, AI, decentralised identity — construct a technically detailed vision of the web in 2050. Describe: the dominant protocols, the deployment architecture (where does computation happen?), the identity model (how do users authenticate and authorise?), and the role of the IT professional. Defend each element of your vision with reference to current trajectory and unresolved challenges.

### Component B: Practical Lab Examination (40%)

A 3-hour practical examination in YggLab NetForge. Students are given a scenario — "Deploy a secure, globally distributed web application" — and must:

1. Configure an nginx reverse proxy with TLS, security headers, rate limiting, and reverse proxying to a backend application.
2. Deploy the application behind a CDN (CloudFront or Cloudflare) with appropriate caching rules.
3. Configure DNS (Route 53 or Cloudflare DNS) with appropriate record types and TTLs.
4. Implement monitoring: synthetic checks for HTTPS validity, DNS resolution, and HTTP response codes.
5. Diagnose and fix a deliberately broken configuration (expired certificate, missing CORS headers, incorrect cache TTLs) introduced by the examiner.

**Evaluation Criteria:**
- Correctness (all services functional and secure)
- Security (TLS configuration, security headers, WAF rules)
- Performance (appropriate caching, CDN configuration, compression)
- Monitoring (health checks, alerting thresholds)
- Documentation (operational runbook describing the deployment)

---

*The web is the largest machine humanity has ever built. It carries our words, our commerce, our knowledge, and our dreams. To understand its architecture is to understand the nervous system of civilisation. To operate it with skill and integrity is to be a steward of that civilisation. Serve well.* ᛟ

— Dr. Sigrún Vérendóttir, University of Yggdrasil, 2040
