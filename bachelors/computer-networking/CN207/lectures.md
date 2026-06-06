# CN207: DNS, DHCP & Directory Services
## Bachelor of Science in Computer Networking — University of Yggdrasil, 2040

**Credits:** 4
**Description:** In-depth study of the naming, addressing, and directory infrastructure that makes networks usable — DNS resolution and security, DHCP automation and hierarchical addressing, and directory services (LDAP, (2040-era) federated identity) that provide authentication and authorization context. Students gain hands-on experience operating production-grade DNS, DHCP, and directory infrastructure in the Bifrǫst Mesh lab.

**Instructor:** Dr. Eirik Hrafnskaldsson, Professor of Network Infrastructure & Bifrǫst Naming Authority Lead
**Lab:** Valhalla Network Lab, Sublevel 2, Hákon Computing Centre
**Office Hours:** Mondays & Wednesdays 14:00-16:00, or by appointment

---

## Lectures

ᚠ **Lecture 1: The Naming Problem — Why DNS Matters**

**Course:** CN207 — DNS, DHCP & Directory Services
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Before a single packet can flow, two questions must be answered: "What is the human-readable name for this resource?" and "What address does that name map to?" This lecture frames the naming problem, traces the history from HOSTS.TXT through the Domain Name System, and examines why DNS is the single most critical — and most fragile — piece of internet infrastructure.

### Key Topics

- **The Naming Problem:** Humans remember names; computers route addresses. A naming system bridges the gap. Requirements: global uniqueness, human readability, hierarchical delegation, low-latency resolution, and fault tolerance. The HOSTS.TXT approach (1970s): a single file maintained by SRI-NIC, distributed by FTP. It failed because it was centralized (single point of failure and bottleneck), required manual updates, and did not scale — every new host required an email to the NIC and a weekly file distribution.
- **The Birth of DNS:** Paul Mockapetris's 1983 design: a distributed, hierarchical, redundant naming system. The key insight: partition the namespace hierarchically so that each organization can manage its own subdomain without coordinating with a central authority. The domain name tree: root → TLD → second-level → subdomain. Delegation: the .no TLD delegates yggdrasil.no to Yggdrasil's nameservers, and Yggdrasil can create any subdomain it wants without informing the .no registry.
- **DNS by the Numbers (2040):** 350 million registered domain names. 13 root server IP addresses (anycast, 1,700+ instances). 1,500+ TLDs (.com, .no, .app, .ygg). 100+ billion DNS queries per day. Average resolution time: 15 ms (cached) to 200 ms (uncached). 99.9999% availability for root and TLD servers.
- **DNS as Critical Infrastructure:** The 2034 *Nordic DNS Outage*: a misconfigured DNSSEC key rollover at the .no TLD caused all Norwegian domain lookups to return SERVFAIL for 4 hours. Banks, hospitals, government services, and personal communications were affected. The lesson: DNS is not just a naming system — it is the internet's critical infrastructure, and its failure is the internet's failure. The Yggdrasil Heimdall DNS architecture: redundant resolvers, DNSSEC validation, DoH/DoT encryption, and real-time monitoring.
- **The Namespace vs. the Routing Space:** DNS maps names to addresses, but names and addresses are fundamentally different things. A name is human-readable and persistent (yggdrasil.no is always yggdrasil.no). An address is machine-routable and changeable (the IP address of yggdrasil.no can change when the server moves). This separation of naming and routing is DNS's core design principle — and the basis for many advanced DNS features (load balancing, failover, geo-routing).

### Lecture Notes

The HOSTS.TXT system was the internet's first naming system, and its failure was inevitable. Every Monday, the Stanford Research Institute's Network Information Center (SRI-NIC) would release an updated HOSTS.TXT file, and every system administrator on the ARPANET would download it and install it on their machine. By the early 1980s, the file was growing by dozens of entries per week, and the update cycle was too slow for a network that was growing exponentially. The system was also centralized — if SRI-NIC's server went down, no new hosts could be added. Paul Mockapetris, then at USC's Information Sciences Institute, recognized that a centralized naming system could not scale and designed DNS as a distributed alternative.

DNS's genius is hierarchical delegation. The root zone delegates .no to NORID (the Norwegian domain registry). NORID delegates yggdrasil.no to Yggdrasil's nameservers. Yggdrasil can create any subdomain it wants — www.yggdrasil.no, mail.yggdrasil.no, heimdall.yggdrasil.no — without informing NORID. This means that adding a new host under yggdrasil.no requires only a local configuration change, not a global update. The result: DNS scales indefinitely because no single server needs to know about the entire namespace.

But this scalability comes at the cost of resolution latency. When a client at the University of Oslo queries for heimdall.yggdrasil.no, the recursive resolver must first query a root server (where is .no?), then query a .no server (where is yggdrasil.no?), then query a yggdrasil.no server (what is the address of heimdall.yggdrasil.no?). Three round trips, each adding latency. Caching mitigates this: the recursive resolver stores the results of each query and reuses them until the TTL expires. A resolver that has recently looked up yggdrasil.no already knows the yggdrasil.no nameserver addresses and can skip the root and TLD queries, resolving heimdall.yggdrasil.no in a single round trip.

The 2034 Nordic DNS Outage is the case study that every network engineer must understand. On March 15, 2034, NORID began a DNSSEC key rollover for the .no TLD — replacing the Zone Signing Key that signs all .no DNS records. The rollover required coordination between NORID and all .no domain operators: the old key must remain valid until all resolvers have updated their caches with the new key. A misconfiguration at NORID caused the old key to be revoked before the new key had propagated, resulting in all DNSSEC-validating resolvers returning SERVFAIL for every .no domain. The outage lasted 4 hours, during which Norwegian citizens could not access banking, health, government, or personal services. The incident demonstrated that DNS is critical infrastructure that requires the same operational rigor as power grids and water systems.

### Required Reading

- Mockapetris, P. (1987). "Domain Names — Implementation and Specification," RFC 1035. (The foundational DNS specification — still required reading.)
- Liu, C. & Albitz, P. (2037). *DNS and BIND*, 8th Edition. O'Reilly. Chapters 1-3.
- Yggdrasil DNS Operations Guide (2040). "Architecture" and "Incident Response."

### Discussion Questions

1. HOSTS.TXT failed because it was centralized. DNS delegates the namespace hierarchically, so no single server is a bottleneck. But DNS still has a root zone, and the root servers are critical. Is DNS truly decentralized, or has the bottleneck moved from HOSTS.TXT to the root servers?
2. The 2034 Nordic DNS Outage was caused by a DNSSEC key rollover. Key rollovers are supposed to be routine operations. What went wrong? How should key rollovers be automated to prevent human error?
3. Some argue that DNS should be replaced by a distributed hash table (DHT) that eliminates the hierarchical delegation model entirely. What are the advantages and disadvantages of a DHT-based naming system compared to DNS? Consider scalability, latency, fault tolerance, and governance.

---

ᚢ **Lecture 2: DNS Protocol — Messages, Resolution, and Caching**

**Course:** CN207 — DNS, DHCP & Directory Services
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

This lecture dives into the DNS wire format, the resolution process, and the caching infrastructure that makes DNS fast enough to serve 100 billion queries per day. Understanding the protocol at the bit level is essential for debugging DNS problems and designing DNS infrastructure.

### Key Topics

- **DNS Message Format:** The 12-byte header (ID, flags, question count, answer count, authority count, additional count). Flags: QR (query/response), Opcode (standard query, inverse query, server status), AA (authoritative answer), TC (truncation), RD (recursion desired), RA (recursion available), RCODE (response code: NOERROR, NXDOMAIN, SERVFAIL, etc.). The question section (QNAME, QTYPE, QCLASS). The answer, authority, and additional sections (resource records). Why DNS messages can be as small as 30 bytes (a single A query) or as large as 64 KB (with EDNS(0)).
- **Resource Record Types:** A (IPv4 address), AAAA (IPv6 address), NS (name server), CNAME (canonical name), MX (mail exchange), TXT (text data), SOA (start of authority), PTR (pointer — reverse DNS), SRV (service location), HTTPS (service binding — the 2040 replacement for SRV in the HTTP context), QKEY (quantum public key pointer — post-quantum TLS key pinning), and NEURO (neuromorphic service discovery). Each record has a name, type, class, TTL, and RDATA.
- **The Resolution Process:** Stub resolver (on the client) → recursive resolver → root server → TLD server → authoritative server. Iterative resolution: the recursive resolver queries each level in turn. The response at each level includes referrals (NS records pointing to the next level) and glue records (A/AAAA records for the referred nameservers). Example: resolving heimdall.yggdrasil.no requires queries to the root, .no, and yggdrasil.no servers.
- **Caching and TTL:** Positive cache (successful lookups cached for the record's TTL), negative cache (NXDOMAIN responses cached for the SOA minimum TTL). TTL tradeoffs: short TTL (60 seconds) for rapid failover vs. long TTL (86400 seconds) for reduced resolver load. The 2040 reality: most DNS traffic is served from cache — only 5-10% of queries require full resolution.
- **EDNS(0) and Large Responses:** The original DNS protocol limited UDP messages to 512 bytes. EDNS(0) (Extension Mechanisms for DNS, RFC 6891) allows the client to advertise a larger UDP buffer size (up to 4096 bytes), enabling larger responses without falling back to TCP. DNSSEC responses (which include signatures) are often larger than 512 bytes and require EDNS(0). When a response exceeds the UDP buffer size, the TC (truncation) flag is set, and the client retries over TCP.

### Lecture Notes

The DNS message format is a masterclass in protocol design: minimal overhead, extensible, and efficient. A simple A query for "yggdrasil.no" is just 30 bytes on the wire: a 12-byte header, a question section with the domain name and type, and no answer, authority, or additional sections. The response adds the answer section with the IP address, for a total of approximately 50 bytes. This efficiency is why DNS can serve 100 billion queries per day — the per-query overhead is negligible compared to the network latency.

The glue record problem is DNS's most subtle engineering challenge. When the .no TLD delegates yggdrasil.no to Yggdrasil's nameservers (ns1.yggdrasil.no and ns2.yggdrasil.no), it must also provide the IP addresses of those nameservers. But to look up ns1.yggdrasil.no, a resolver would need to query yggdrasil.no's nameservers — creating a circular dependency. The solution: glue records. The .no TLD includes A/AAAA records for ns1.yggdrasil.no and ns2.yggdrasil.no in the referral response, so the resolver can reach the nameservers without further queries. Glue records are essential for DNS to function, but they must be kept in sync with the actual addresses — if Yggdrasil changes the IP address of ns1.yggdrasil.no without updating the glue records at .no, the resolver will try to reach the old address and fail.

Caching is DNS's primary performance mechanism. A recursive resolver that has recently looked up yggdrasil.no has the NS records and their glue addresses cached, so subsequent queries for anything under yggdrasil.no (www.yggdrasil.no, mail.yggdrasil.no) can be resolved in a single round trip. The TTL (Time to Live) of each record determines how long the cache is valid. Short TTLs (60-300 seconds) are used for records that change frequently — for example, DNS-based load balancing that rotates between multiple servers. Long TTLs (86400 seconds = 1 day) are used for stable records like NS records and root server addresses. The tradeoff: short TTLs enable fast failover but increase resolver load (more cache misses), while long TTLs reduce load but slow failover (cached stale records are served until the TTL expires).

The Yggdrasil Heimdall DNS architecture uses a three-tier resolver design. The first tier consists of local resolvers at each campus, serving cached responses to clients within microseconds. The second tier consists of regional resolvers in Oslo, Bergen, and Tromsø, serving the local resolvers and handling queries that miss the local cache. The third tier consists of authoritative servers for the yggdrasil.no domain, serving responses that miss all caches. The three-tier design ensures that 95% of DNS queries are answered by the local resolver (microsecond latency), 4% by the regional resolvers (millisecond latency), and only 1% require full resolution (tens of milliseconds latency).

### Required Reading

- Mockapetris, P. (1987). "Domain Names — Implementation and Specification," RFC 1035. Sections 4-6.
- Dickinson, J., et al. (2036). *DNS Operations*, 2nd Edition. RFC 9323 (updated). IETF.
- Yggdrasil DNS Operations Guide (2040). "Resolver Architecture" and "Caching Strategy."

### Discussion Questions

1. A recursive resolver caches a record with a 300-second TTL. The authoritative server updates the record after 100 seconds. How long does it take for the change to reach all clients? How can you reduce this propagation time without reducing the TTL?
2. EDNS(0) allows DNS messages up to 4096 bytes over UDP. But path MTU issues can cause fragmentation, and some firewalls drop fragmented packets. Describe a scenario where EDNS(0) causes DNS resolution to fail. How would you diagnose and fix it?
3. Glue records at the .no TLD point to ns1.yggdrasil.no at 203.0.113.10. Yggdrasil moves ns1 to 203.0.113.20 but forgets to update the glue records. Trace the resolution attempt for www.yggdrasil.no and explain exactly where it fails. How long will the failure persist?

---

ᚦ **Lecture 3: DNS Server Architecture — Authoritative, Recursive, and Forwarding**

**Course:** CN207 — DNS, DHCP & Directory Services
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

DNS servers come in three flavors: authoritative (the source of truth for a zone), recursive (the client's resolver), and forwarding (a cache that delegates upstream). This lecture covers the architecture, implementation, and operational practices for each type, using the Yggdrasil Bifrǫst DNS infrastructure as a running example.

### Key Topics

- **Authoritative Servers:** The source of truth for a zone. Primary (master) and secondary (slave) servers, with zone transfers (AXFR for full transfer, IXFR for incremental). The zone file format: SOA record (serial number, refresh, retry, expire, minimum), NS records, A/AAAA records, MX records, and other records. NOTIFY messages: the primary server notifies secondaries when a zone changes, triggering an immediate transfer instead of waiting for the refresh interval.
- **Recursive Resolvers:** The client's entry point into DNS. The recursive resolver performs full resolution on behalf of the client: querying root, TLD, and authoritative servers until it receives the answer. Caching: positive and negative caches reduce upstream queries. Prefetching: proactively refreshing popular records before they expire. The 2040 Yggdrasil Heimdall Resolver: a recursive resolver with DNSSEC validation, DoH/DoT support, query logging for security analytics, and real-time performance monitoring.
- **Forwarding Resolvers:** A resolver that forwards all queries to an upstream resolver instead of performing full resolution. Use cases: branch offices (forward to the corporate resolver), ISPs (forward to a central resolver pool), and institutional networks (forward to the campus resolver). Conditional forwarding: forwarding specific domains (e.g., yggdrasil.no) to a specific resolver while resolving other domains normally.
- **Anycast DNS:** Publishing the same IP address from multiple locations, allowing clients to reach the nearest server. Root servers, TLD servers, and large authoritative servers use anycast for load distribution and fault tolerance. The 13 root server IP addresses are served by 1,700+ instances worldwide. Anycast DNS uses BGP routing: each instance announces the same IP prefix, and BGP directs traffic to the nearest instance.
- **DNS Load Balancing and Geo-Routing:** Using DNS to distribute traffic across multiple servers (round-robin A records), direct clients to the nearest server (geo-DNS based on the client's IP address), and implement failover (removing a server's A record when it becomes unhealthy). The 2040 state: most large-scale DNS providers offer geo-routing as a service, with real-time health checks and automatic failover.

### Lecture Notes

The distinction between authoritative and recursive servers is fundamental. Authoritative servers are the source of truth — they hold the zone data and respond to queries about their zone. Recursive servers are middlemen — they perform resolution on behalf of clients and cache the results. A single server can be both authoritative (for its own zones) and recursive (for client queries), but this is a security risk: an authoritative server that also performs recursion is vulnerable to cache poisoning attacks that target the recursive function. Best practice in 2040 is strict separation: authoritative servers should not perform recursion, and recursive servers should not be authoritative for any zone.

Zone transfers are the mechanism by which secondary authoritative servers stay synchronized with the primary. AXFR (full zone transfer) sends the entire zone; IXFR (incremental zone transfer) sends only the changes since the last transfer. For large zones (millions of records), IXFR is essential — an AXFR of a million-record zone can take minutes and consume significant bandwidth, while an IXFR of 10 changed records takes milliseconds. The Yggdrasil primary authoritative server sends NOTIFY messages to secondaries whenever a zone changes, triggering an immediate IXFR. This reduces propagation time from the SOA refresh interval (typically 1 hour) to seconds.

The Yggdrasil Heimdall Resolver is a recursive resolver designed for the Bifrǫst Mesh campus network. It performs DNSSEC validation on every response, rejecting unsigned or improperly signed responses. It supports DoH (DNS over HTTPS, port 443) and DoT (DNS over TLS, port 853) for encrypted resolution, preventing eavesdropping and tampering on the local network. It logs all queries for security analytics (detecting malware command-and-control domains, identifying data exfiltration attempts, and tracking resolution performance). The logs are processed by the Heimdall neural IDS, which identifies anomalous patterns — for example, a client that suddenly starts querying domains it has never queried before, which may indicate a malware infection.

Anycast DNS is how the root server system serves 100 billion queries per day with only 13 IP addresses. Each of the 13 root server operators announces the same IP prefix from dozens to hundreds of locations worldwide. When a client in Oslo sends a query to 192.5.5.241 (the F root server), BGP routing directs the query to the nearest F root instance — which is in Stockholm, 1 ms away. When a client in Tokyo sends a query to the same IP, BGP directs it to the Tokyo instance, also 1 ms away. Anycast provides both load distribution (queries are spread across all instances) and fault tolerance (if an instance fails, BGP routes queries to the next nearest instance). The challenge: anycast routing depends on BGP, which does not always choose the topologically nearest instance. BGP routes based on AS path length, not latency, so a query from Oslo might be routed to London (3 ms) instead of Stockholm (1 ms) if the AS path to London is shorter.

### Required Reading

- Liu, C. & Albitz, P. (2037). *DNS and BIND*, 8th Edition. O'Reilly. Chapters 4-8.
- Pall, A., et al. (2035). "Anycast DNS: Architecture and Operational Considerations." *RFC 9343*.
- Yggdrasil DNS Operations Guide (2040). "Heimdall Resolver" and "Authoritative Server Configuration."

### Discussion Questions

1. A recursive resolver caches a negative response (NXDOMAIN) for a domain that was recently created. How long will the NXDOMAIN cache persist? What is the SOA minimum TTL, and how can you force the resolver to re-query before the TTL expires?
2. Anycast DNS provides fault tolerance, but anycast failover is not instantaneous — BGP must converge after an instance failure, which can take 30-60 seconds. During this time, queries are routed to the failed instance and time out. How would you reduce the failover time? Consider BGP tuning, health checking, and anycast monitoring.
3. The Heimdall Resolver logs all DNS queries for security analytics. What privacy implications does this create? How would you balance security monitoring (detecting malware) with user privacy (protecting browsing history)?

---

ᚬ **Lecture 4: DNSSEC — Securing the Domain Name System**

**Course:** CN207 — DNS, DHCP & Directory Services
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

DNS was designed without security — any resolver can be spoofed, any response can be tampered with, and any query can be eavesdropped. DNSSEC adds cryptographic signatures to DNS records, enabling resolvers to verify that responses are authentic and untampered. This lecture covers DNSSEC's architecture, the chain of trust, key management, and deployment challenges.

### Key Topics

- **The DNS Security Problem:** DNS cache poisoning (the Kaminsky attack): an attacker sends forged DNS responses to a recursive resolver, causing it to cache incorrect IP addresses. DNS spoofing: an attacker on the same network sends forged DNS responses faster than the legitimate server. DNS hijacking: an attacker compromises the authoritative server and changes the zone data. DNS amplification DDoS: an attacker sends small DNS queries with spoofed source addresses, causing DNS servers to send large responses to the victim.
- **DNSSEC Architecture:** DNSSEC adds digital signatures to DNS records. Each zone has a Key Signing Key (KSK) that signs the zone's DNSKEY record set, and a Zone Signing Key (ZSK) that signs the zone's individual record sets. The chain of trust: the root KSK signs the root DNSKEY record, which signs the .no DNSKEY record, which signs the yggdrasil.no DNSKEY record, which signs the individual records (A, AAAA, MX, etc.) under yggdrasil.no. Delegation Signer (DS) records in the parent zone authenticate the child zone's KSK.
- **New Resource Records:** DNSKEY (DNS public key), RRSIG (resource record signature), DS (delegation signer), NSEC/NSEC3 (authenticated denial of existence). DNSKEY: the public key that verifies signatures. RRSIG: the signature over a set of records. DS: a hash of the child zone's KSK, stored in the parent zone to create the chain of trust. NSEC/NSEC3: proof that a name does not exist (authenticated denial of existence).
- **Key Management:** KSK and ZSK rollovers: the process of replacing keys without breaking validation. KSK rollover requires coordination with the parent zone (updating the DS record). ZSK rollover can be done within the zone. The root KSK rollover of 2039: months of planning, a 3-hour outage for 2% of validating resolvers, and lessons learned about the difficulty of global coordination. Key storage: HSMs (Hardware Security Modules) for root and TLD KSKs, software key storage for enterprise zones.
- **Deployment Challenges:** DNSSEC increases DNS response sizes (signatures add 500-1000 bytes per record set), increasing the risk of DNS amplification DDoS and UDP fragmentation. DNSSEC validation is computationally expensive (signature verification for every response). DNSSEC does not encrypt queries — it only authenticates responses. The 2040 state: 75% of TLDs are signed, 40% of second-level domains are signed, and DNSSEC validation is required by institutional policy at Yggdrasil.

### Lecture Notes

The Kaminsky attack, discovered by Dan Kaminsky in 2008, was a watershed moment for DNS security. Before Kaminsky, DNS cache poisoning required the attacker to guess the 16-bit transaction ID and source port — a difficult but not impossible brute-force attack. Kaminsky discovered that by flooding a recursive resolver with queries for non-existent subdomains (1ww.yggdrasil.no, 2ww.yggdrasil.no, etc.) and then sending forged responses with the correct transaction ID and source port, an attacker could poison the cache with a much higher success rate. The attack was so effective that a successful poisoning could be achieved in seconds. The immediate fix was source port randomization (using random source ports instead of fixed port 53), which increased the attack space from 65,536 to 4 billion. But this was a mitigation, not a solution. DNSSEC was the solution: by cryptographically signing DNS responses, DNSSEC makes cache poisoning impossible — a forged response cannot produce a valid signature.

But DNSSEC deployment has been slow. As of 2040, only 75% of TLDs and 40% of second-level domains are signed. The reasons are multiple: DNSSEC is complex (key management, rollover procedures, DS record coordination with the parent zone), it increases DNS response sizes (triggering fragmentation and amplification concerns), and many organizations do not perceive DNS spoofing as a significant threat. The Yggdrasil Heimdall DNS architecture requires DNSSEC validation for all resolutions, which means that any unsigned domain is treated with suspicion — not rejected, but flagged as potentially spoofable.

The 2039 root KSK rollover was the most critical DNS operation in history. The root KSK is the trust anchor for the entire DNSSEC hierarchy — every DNSSEC-validating resolver must have the root KSK configured as a trusted key. Replacing this key requires updating every validator in the world, which is a logistical challenge of staggering scale. The rollover was planned for 2 years, with multiple test events and extensive outreach. Despite this preparation, approximately 2% of validating resolvers failed to update their trust anchors, causing a 3-hour outage for those resolvers (their DNSSEC validation rejected all signed responses because the signatures were verified with a key they did not trust). The lesson: global coordination is extremely difficult, and any operation that requires updating every resolver in the world carries significant risk.

NSEC and NSEC3 solve the problem of authenticated denial of existence — proving that a name does not exist. Without DNSSEC, a negative response (NXDOMAIN) can be forged: an attacker can send a forged NXDOMAIN for www.yggdrasil.no, preventing the client from reaching the website. NSEC solves this by creating a chain of existing names: if the zone contains a.example.no and c.example.no but not b.example.no, the NSEC record for a.example.no says "the next name is c.example.no," proving that b.example.no does not exist. NSEC3 hashes the names before creating the chain, preventing zone enumeration (an attacker cannot walk the NSEC chain to discover all names in the zone). The Yggdrasil DNS infrastructure uses NSEC3 with 10 iterations of SHA-256, balancing security (preventing enumeration) with performance (each iteration adds computational cost to the authoritative server).

### Required Reading

- Arends, R., et al. (2035). "DNS Security Introduction and Requirements," RFC 4033 (updated). IETF.
- Arends, R., et al. (2035). "Resource Records for the DNS Security Extensions," RFC 4034 (updated). IETF.
- Yggdrasil DNS Operations Guide (2040). "DNSSEC Deployment" and "Key Management."

### Discussion Questions

1. DNSSEC prevents cache poisoning but does not encrypt queries. DoH and DoT encrypt queries but do not authenticate responses. What combination of DNS security technologies provides the best protection? Why has full DNS security (both authenticated and encrypted) been so slow to deploy?
2. The root KSK rollover caused a 3-hour outage for 2% of validating resolvers. What went wrong? How would you design a rollover procedure that eliminates the risk of outage? Consider automated trust anchor updates, pre-publishing, and dual-signing.
3. NSEC allows zone enumeration (an attacker can walk the chain to discover all names in the zone). NSEC3 prevents enumeration by hashing names, but it adds computational cost. A bank's DNS zone contains employee names as subdomains (john.smith.bank.example.no). Should the bank use NSEC or NSEC3? What are the security implications of each?

---

ᚱ **Lecture 5: Encrypted DNS — DoH, DoT, and the Privacy Debate**

**Course:** CN207 — DNS, DHCP & Directory Services
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Traditional DNS queries are sent in plaintext, allowing anyone on the path to see which domains a user is visiting. Encrypted DNS (DoT, DoH, and the 2040 DoQ) protects user privacy but creates new challenges for network operators who rely on DNS visibility for security monitoring. This lecture covers the encryption protocols, the privacy debate, and the Heimdall approach to reconciling privacy with security.

### Key Topics

- **DNS over TLS (DoT):** Encrypting DNS queries using TLS on port 853. Connection-oriented: the client establishes a TLS session with the resolver and sends queries over the encrypted channel. Benefits: prevents eavesdropping and tampering on the local network. Drawbacks: adds TLS handshake latency (one round trip) for the first query; some firewalls block port 853.
- **DNS over HTTPS (DoH):** Encrypting DNS queries using HTTPS on port 443. Query-oriented: each query is an HTTPS request (GET or POST) to the resolver's /dns-query endpoint. Benefits: indistinguishable from regular HTTPS traffic (resists censorship); uses port 443 (unlikely to be blocked). Drawbacks: higher overhead (HTTP framing); browser integration raises concerns about DNS policy bypass.
- **DNS over QUIC (DoQ):** Encrypting DNS queries using QUIC on port 853. Combines the low latency of QUIC (0-RTT for resumed connections) with the encryption of TLS. Benefits: eliminates TCP head-of-line blocking, reduces connection setup latency, and provides connection migration. The 2040 standard for encrypted DNS in the Bifrǫst Mesh.
- **The Privacy vs. Security Debate:** Encrypted DNS prevents network operators from seeing which domains users visit, undermining security monitoring (malware detection, content filtering, parental controls). The browser perspective: encrypted DNS protects user privacy from ISP surveillance. The enterprise perspective: encrypted DNS bypasses corporate DNS policy (web filtering, threat detection). The Yggdrasil Heimdall compromise: the institutional resolver decrypts DNS queries at the network edge (with user consent and institutional policy), applies security policies, and forwards queries to the upstream resolver over DoQ.
- **Encrypted Server Name Indication (ESNI/ECH):** Even with encrypted DNS, the TLS Server Name Indication (SNI) header is sent in plaintext during the TLS handshake, revealing which website the user is visiting. Encrypted Client Hello (ECH) encrypts the SNI using the server's public key, preventing passive eavesdroppers from learning the destination. The 2040 state: ECH is supported by all major browsers and 60% of web servers.

### Lecture Notes

The privacy argument for encrypted DNS is simple: DNS queries reveal which websites a user visits, which applications they use, and which services they rely on. In a world without encrypted DNS, an ISP can build a detailed profile of every user's browsing habits — and in many jurisdictions, ISPs are required to store this data for law enforcement. Encrypted DNS prevents this surveillance by encrypting the query before it leaves the user's device. DNS over HTTPS (DoH) goes further by making DNS traffic indistinguishable from regular HTTPS traffic, resisting not only surveillance but also censorship (a firewall that blocks port 853 can't block port 443 without blocking all HTTPS traffic).

But encrypted DNS creates a problem for network operators. In a corporate or institutional network, the DNS resolver is a critical security tool. It blocks access to known malware domains, enforces content filtering policies, detects data exfiltration, and monitors for suspicious queries. If users bypass the institutional resolver by using a public DoH server (e.g., Cloudflare's 1.1.1.1), the network operator loses all visibility into DNS queries. This is not just a theoretical concern: in 2037, a Yggdrasil student's laptop was infected with malware that used DoH to communicate with its command-and-control server, bypassing the institutional DNS filter. The malware was eventually detected by the Heimdall neural IDS (which analyzes traffic patterns, not DNS queries), but the incident highlighted the tension between privacy and security.

The Yggdrasil Heimdall approach reconciles privacy and security. The Heimdall Resolver is the institutional recursive resolver, and all campus DNS traffic is directed to it (by DHCP configuration and firewall policy). The Heimdall Resolver accepts queries over DoQ (encrypted), validates DNSSEC signatures, applies security policies (blocking known malware domains and enforcing content filtering), and forwards queries to the upstream resolver over DoQ. The result: users' DNS queries are encrypted in transit (preventing eavesdropping by ISPs and third parties), but the institutional resolver can still apply security policies. The tradeoff: the institution can see DNS queries, but it cannot see the TLS-encrypted content of web traffic. This is the same tradeoff that exists in corporate TLS inspection, and it requires institutional policy transparency and user consent.

Encrypted Client Hello (ECH) is the final piece of the privacy puzzle. Even with encrypted DNS, the TLS handshake reveals the server name (SNI) in plaintext. A passive eavesdropper who cannot see DNS queries can still learn which website a user is visiting by observing the SNI in the TLS Client Hello. ECH encrypts the Client Hello using the server's public key (obtained via DNS HTTPS record), preventing the eavesdropper from learning the server name. ECH is supported by all major browsers in 2040, and 60% of web servers publish the necessary DNS records. The remaining 40% (primarily older servers and CDNs that have not yet adopted ECH) still expose SNI.

### Required Reading

- Hu, Z., et al. (2035). "DNS over TLS," RFC 8484 (updated). IETF.
- Hoffman, P. & McManus, P. (2035). "DNS Queries over HTTPS," RFC 8484 (updated). IETF.
- Yggdrasil DNS Operations Guide (2040). "Encrypted DNS" and "Security Policies."

### Discussion Questions

1. A government mandates that all DNS traffic must pass through the national resolver for "security monitoring." Citizens can use DoH to bypass this mandate. Should browsers default to DoH? What are the ethical implications of bypassing government-mandated monitoring?
2. The Heimdall Resolver decrypts DNS queries at the network edge, applies security policies, and re-encrypts before forwarding. A student argues that this "bump in the wire" approach violates their privacy. How would you respond? What safeguards should be in place to prevent abuse of this capability?
3. ECH encrypts the TLS Server Name Indication, preventing passive eavesdroppers from learning the destination website. But the destination IP address is still visible. Can an eavesdropper learn which website a user is visiting from the IP address alone? What are the limitations of this approach (consider CDNs, shared hosting, and IP address rotation)?

---

ᚴ **Lecture 6: DHCP — The Dynamic Host Configuration Protocol**

**Course:** CN207 —, DHCP & Directory Services
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Every device on an IP network needs an address, a default gateway, and DNS servers — and configuring these manually on thousands of devices is impractical. DHCP automates this configuration. This lecture covers DHCPv4, DHCPv6, SLAAC, and the 2040 landscape of automated addressing.

### Key Topics

- **DHCPv4:** The four-packet exchange: DHCPDISCOVER → DHCPOFFER → DHCPREQUEST → DHCPACK. The client broadcasts a discover message, servers offer addresses, the client requests one, and the server acknowledges. Lease management: addresses are leased for a finite time (T1 = 50% of lease time for renewal, T2 = 87.5% for rebinding). Relay agents: forwarding DHCP messages from one subnet to another (DHCP clients broadcast, but the server may be on a different subnet).
- **DHCPv6:** The IPv6 equivalent, which operates differently from DHCPv4. Stateful DHCPv6: the server assigns addresses and configuration (similar to DHCPv4). Stateless DHCPv6: the server provides only configuration (DNS servers, domain search list) while addresses are autoconfigured via SLAAC. The 2040 best practice: SLAAC for addresses, stateless DHCPv6 for configuration.
- **SLAAC (Stateless Address Autoconfiguration):** The IPv6 mechanism where a device creates its own address by combining the network prefix (advertised by the router) with its own interface identifier. Privacy extensions: the original EUI-64 format creates a stable identifier from the MAC address (enabling tracking); privacy extensions generate random interface identifiers that change periodically. The 2040 state: SLAAC with privacy extensions is the default on all operating systems.
- **DHCP Options and Relay:** DHCP options carry configuration beyond the basic address and gateway: DNS server (option 6), domain name (option 15), NTP server (option 42), PXE boot server (option 66), and the 2040 additions — QKEY server (option 230), NEURO directory (option 231), and Bifrǫst Mesh controller (option 232). DHCP relay agents forward messages between subnets, enabling a single DHCP server to serve multiple subnets.
- **DHCPv6 Prefix Delegation:** Instead of assigning individual addresses, DHCPv6 can delegate an entire prefix to a router. This is essential for home networks (the ISP delegates a /56 to the home router, which assigns /64 subnets to each network) and for the Bifrǫst Mesh (the mesh controller delegates prefixes to each mesh node).

### Lecture Notes

DHCP's four-packet exchange (DISCOVER, OFFER, REQUEST, ACK) is simple but has subtle complications. When a client broadcasts a DISCOVER message, multiple DHCP servers may respond with OFFER messages. The client typically selects the first OFFER it receives (or the one with the most attractive lease terms), but this can lead to address conflicts if two servers offer the same address. The solution: DHCP servers should ping an address before offering it (to detect conflicts) and clients should verify the address with a gratuitous ARP (to detect conflicts after assignment). The Yggdrasil DHCP servers maintain a lease database that tracks all assigned addresses, preventing conflicts even across multiple servers.

IPv6 addressing is fundamentally different from IPv4. In IPv4, a device gets one address from DHCP, and that address is its identity on the network. In IPv6, a device typically has multiple addresses: a link-local address (fe80::/10, used for local communication), a global unicast address (assigned via SLAAC or DHCPv6), and a temporary privacy address (randomly generated, used for outbound connections, and rotated periodically). The temporary privacy address prevents tracking: if a device always uses the same address, websites can track it across sessions. With privacy extensions, the device rotates its temporary address every 24 hours (by default), making it difficult for websites to correlate visits over time.

DHCPv6 prefix delegation is the mechanism that makes IPv6 home and enterprise networking possible. When a home router connects to the ISP, it receives a /56 prefix via DHCPv6-PD (e.g., 2001:db8:abcd::/56). The home router then assigns /64 subnets from this prefix to each of its networks: 2001:db8:abcd:1::/64 for the Wi-Fi network, 2001:db8:abcd:2::/64 for the Ethernet network, and 2001:db8:abcd:3::/64 for the guest network. Each /64 prefix provides 2⁶⁴ addresses — more than enough for any network. Compare with IPv4, where the typical home network gets a single /24 (256 addresses, of which only 254 are usable) or even a smaller allocation from CGNAT.

The Bifrǫst Mesh uses a hierarchical prefix delegation scheme. The Yggdrasil Autonomous System receives a /32 prefix from the regional internet registry (2001:db8::/32). The mesh controller delegates /48 prefixes to each campus (2001:db8:1::/48 for Oslo, 2001:db8:2::/48 for Bergen, etc.). Each campus delegates /56 prefixes to each building. Each building delegates /64 prefixes to each network. This hierarchy ensures that every device on the Bifrǫst Mesh has a globally routable IPv6 address, and the routing tables at each level only need to know the next level's prefix — not every individual address.

### Required Reading

- Droms, R. (2035). "Dynamic Host Configuration Protocol," RFC 2131 (updated). IETF.
- Droms, R., et al. (2036). "IPv6 Dynamic Host Configuration Protocol," RFC 8415 (updated). IETF.
- Yggdrasil Network Operations Guide (2040). "DHCP Architecture" and "IPv6 Addressing."

### Discussion Questions

1. A DHCP server assigns an address that is already in use by a statically configured device. Describe the sequence of events that leads to this conflict, and explain the mechanisms DHCP uses to prevent it (ping before offer, gratuitous ARP, lease database).
2. IPv6 privacy extensions rotate temporary addresses every 24 hours. This prevents tracking but breaks long-lived TCP connections (the remote server remembers the old address). How do operating systems handle this? What happens to existing connections when the temporary address changes?
3. A campus network has 5,000 devices and a /48 prefix (2⁸⁰ addresses). The network administrator assigns /64 prefixes to each subnet. Calculate how many subnets are available and how many addresses per subnet. Is this allocation wasteful? How does IPv6's address abundance change network design philosophy?

---

ᚦ **Lecture 7: DHCP Failover, Redundancy, and the Bifrǫst Mesh Addressing Architecture**

**Course:** CN207 — DNS, DHCP & Directory Services
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

DHCP is a single point of failure — if the DHCP server goes down, new devices cannot obtain addresses. This lecture covers DHCP failover, redundancy, load balancing, and the Bifrǫst Mesh's hierarchical addressing architecture that ensures every device has a stable, globally routable address.

### Key Topics

- **DHCP Failover:** Two DHCP servers sharing a lease database, ensuring that if one fails, the other continues serving clients. The DHCP failover protocol: two servers in a partner relationship, exchanging lease updates in real time. Primary-secondary (one server is active, the other is standby) vs. load-balancing (both servers serve clients, splitting the address pool). The challenge: lease database synchronization (both servers must have identical lease state) and split-brain prevention (what happens when the servers lose contact with each other).
- **Anycast DHCP:** Publishing the same DHCP server IP address from multiple locations, allowing clients to reach the nearest server. Anycast DHCP simplifies client configuration (the default gateway points to the anycast DHCP address) and provides automatic failover (if one server fails, the client's next DISCOVER reaches another server). The Bifrǫst Mesh uses anycast DHCP with IPv6, where the anycast address is a well-known address in each /64 prefix.
- **Hierarchical Addressing Architecture:** The Bifrǫst Mesh's addressing scheme: /32 for the autonomous system, /48 for campus, /56 for building, /64 for subnet. Each level of the hierarchy aggregates routes: the campus router only needs routes for its buildings, not for individual subnets. This aggregation keeps routing tables small and stable. Address stability: devices keep their addresses even when they move between buildings (using SLAAC with stable interface identifiers), and addresses are delegated from the mesh controller (not DHCP), ensuring that the address plan is consistent.
- **IPv4/IPv6 Coexistence:** Dual-stack (running both IPv4 and IPv6 simultaneously), NAT64 (IPv6-only network with translation to IPv4), and 464XLAT (client-side translation for IPv4-only applications on IPv6-only networks). The 2040 state: IPv6-only is the default; IPv4 is supported via NAT64/DNS64 for legacy applications. The Bifrǫst Mesh is IPv6-only internally, with NAT64 for reaching IPv4-only services on the internet.
- **Address Planning Best Practices:** Spacing (reserve /48 per campus, /56 per building, even if current needs are smaller), numbering (logical assignment, not random), and documentation (every prefix is documented with its purpose, contact, and expected growth). The Yggdrasil address plan: every prefix is registered in NetDB, the Bifrǫst Mesh's IP address management (IPAM) system.

### Lecture Notes

DHCP failover is essential for production networks, but the failover protocol is surprisingly complex. The core challenge is lease database consistency: both servers must agree on which addresses are leased, which are available, and which leases are about to expire. The DHCP failover protocol addresses this with a reliable update mechanism: each server sends lease updates to its partner, and the partner acknowledges the update. If the partner fails to acknowledge, the sending server retries until it succeeds. This ensures that both servers have identical lease state.

But what happens when the servers lose contact with each other (split-brain)? Without communication, both servers may assign the same address to different clients. The failover protocol addresses this with the "partner-down" state: if a server cannot contact its partner for a configured time (the maximum client lead time, typically 1 hour), it assumes the partner is down and takes over the entire address pool. When the partner comes back online, they resynchronize and resume load-balancing. The risk: if the partner is actually up but unreachable (network partition), both servers are in partner-down state and may assign conflicting addresses. The mitigation: use a shared lease database (a database that both servers write to) rather than the protocol's built-in synchronization, which eliminates the split-brain problem at the cost of database complexity.

The Bifrǫst Mesh uses anycast DHCPv6 for simplicity and resilience. Each subnet has a well-known anycast address (e.g., fe80::1 for the link-local DHCPv6 server). When a client sends a Solicit message to the anycast address, the message reaches the nearest DHCPv6 server (determined by routing). If that server fails, the client's next Solicit reaches a different server. No failover protocol is needed — any available server can serve any client, because the lease database is shared across all servers (stored in the NetDB distributed database). This architecture is simpler and more resilient than DHCPv4 failover: there is no primary-secondary relationship, no split-brain risk, and no partner-down state.

IPv4/IPv6 coexistence in 2040 is a story of gradual IPv6 adoption and IPv4 retreat. The Bifrǫst Mesh is IPv6-only internally, but it must reach IPv4-only services on the internet (about 15% of internet services are still IPv4-only in 2040). NAT64/DNS64 handles this: when a client looks up an IPv4-only service (e.g., example.com has only an A record, no AAAA record), the DNS64 resolver synthesizes an AAAA record pointing to a NAT64 prefix (e.g., 64:ff9b::example.com's IPv4 address). The client connects to the synthesized IPv6 address, and the NAT64 gateway translates the IPv6 connection to an IPv4 connection. For IPv4-only applications (e.g., legacy software that uses IPv4 sockets), 464XLAT provides a local IPv4-to-IPv6 translator on the client, allowing the application to work on an IPv6-only network. The result: users operate on an IPv6-only network without noticing that some services are IPv4-only.

### Required Reading

- Lemon, T. & Mrugalski, T. (2036). "DHCP Failover Protocol," RFC 9353. IETF.
- Troan, H. & Soininen, P. (2035). "IPv6 Prefix Delegation," RFC 8987. IETF.
- Yggdrasil Network Operations Guide (2040). "Addressing Architecture" and "NAT64/DNS64."

### Discussion Questions

1. A DHCP failover pair loses contact with each other. Both servers transition to partner-down state and begin assigning addresses. When connectivity is restored, they discover that they have assigned the same address to different clients. How do they resolve the conflict? What are the risks of this situation?
2. The Bifrǫst Mesh uses anycast DHCPv6 with a shared lease database. If the database fails, new clients cannot obtain addresses. Design a solution that provides DHCPv6 service even when the database is unavailable. What are the tradeoffs?
3. An organization is migrating from IPv4 to IPv6. They have 5,000 devices that need both IPv4 and IPv6 addresses. Should they use dual-stack (IPv4 and IPv6 on every device) or IPv6-only with NAT64/DNS64? What are the pros and cons of each approach?

---

ᚬ **Lecture 8: LDAP and Directory Services — The Organizational Backbone**

**Course:** CN207 — DNS, DHCP & Directory Services
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

DNS maps names to network addresses; directory services map identities to attributes (name, email, group membership, access rights). LDAP (Lightweight Directory Access Protocol) is the foundation of enterprise directory services, and this lecture covers its data model, operations, replication, and the 2040 evolution toward federated identity.

### Key Topics

- **LDAP Data Model:** The Directory Information Tree (DIT): a hierarchical tree of entries, each identified by a Distinguished Name (DN). Entries contain attributes (key-value pairs) defined by an object class (which attributes are required and which are optional). Example: dn: uid=eirik,ou=people,dc=yggdrasil,dc=no has objectClass inetOrgPerson, uid eirik, cn Eirik Hrafnskaldsson, mail eirik@yggdrasil.no. The tree structure enables delegated administration: the ou=people subtree is managed by HR, the ou=groups subtree by IT, and the ou=services subtree by system administrators.
- **LDAP Operations:** Bind (authenticate), Search (query the directory with filters), Add, Modify, Delete, ModifyDN (rename/move). The LDAP search filter syntax: (&(objectClass=inetOrgPerson)(mail=*@yggdrasil.no)) finds all people with a yggdrasil.no email address. Search scope: base (one entry), one (one level), sub (entire subtree). Attributes: specify which attributes to return (+ for all operational attributes).
- **LDAP Replication:** Single-master replication (one writable server, multiple read-only replicas) vs. multi-master replication (multiple writable servers that synchronize changes). The conflict resolution challenge: what happens when two administrators modify the same entry on different servers simultaneously? LDAP uses change sequence numbers (CSN) and conflict resolution rules (last-writer-wins for attribute modifications, manual resolution for structural conflicts).
- **LDAP and Authentication:** LDAP as the authentication backend for SSH, VPN, Wi-Fi (802.1X), and web applications. The bind operation: the client sends a DN and password, LDAP verifies the password hash, and returns success or failure. Password policies: minimum length, complexity, expiration, account lockout. The 2040 evolution: password-based authentication is supplemented by multi-factor authentication (MFA) and certificate-based authentication.
- **LDAP and Authorization:** Group membership as the basis for access control. The groupOfNames object class: member uid=eirik,ou=people,dc=yggdrasil,dc=no is a member of cn=network-ops,ou=groups,dc=yggdrasil,dc=no. Applications query LDAP to check group membership: "Is user eirik a member of network-ops?" Role-based access control (RBAC): users are assigned to groups, groups are assigned to roles, and roles define permissions.

### Lecture Notes

LDAP is the backbone of enterprise identity management. When a student logs into a campus computer, the computer authenticates the student against LDAP. When the student connects to the campus Wi-Fi, the 802.1X authentication checks LDAP for the student's credentials. When the student accesses the learning management system, the web application queries LDAP for group membership to determine permissions. LDAP is not just a database — it is the authoritative source of truth for identity, authentication, and authorization across the enterprise.

The Directory Information Tree (DIT) is LDAP's answer to the question "How do we organize thousands of entries?" The hierarchical structure mirrors the organizational structure: dc=yggdrasil,dc=no at the top, ou=people for users, ou=groups for groups, ou=services for service accounts. This hierarchy enables delegated administration: the HR department can manage the ou=people subtree (adding new employees, updating contact information), the IT department can manage the ou=services subtree (creating service accounts, managing permissions), and neither department needs access to the other's subtree. The Access Control List (ACL) model in LDAP supports this delegation: ACLs can grant write access to specific attributes (e.g., HR can write telephoneNumber and departmentNumber but not uid or userPassword).

Multi-master replication is the 2040 standard for LDAP availability. In the Yggdrasil directory, three servers in Oslo, Bergen, and Tromsø accept writes simultaneously. When an administrator adds a new user on the Oslo server, the change is replicated to Bergen and Tromsø within seconds. If two administrators modify the same entry simultaneously on different servers, the replication system uses change sequence numbers (CSN) to determine which change was made later and applies that change. This last-writer-wins resolution works well for most attributes (if two administrators update a user's phone number, the latest update wins), but it can cause problems for structural changes (if one administrator moves a user to a different OU and another administrator deletes the user, the results depend on the order of replication). The Yggdrasil directory system resolves structural conflicts by flagging them for manual review.

The relationship between LDAP and DNS is both complementary and confusing. DNS manages network names (hostnames, domain names) and maps them to network addresses (IP addresses). LDAP manages organizational identities (people, groups, services) and maps them to attributes (email, phone, group membership). The confusion arises because LDAP DNs use domain components (dc=yggdrasil,dc=no) that look like DNS domain names. This is by convention, not requirement — it is possible to have an LDAP tree that does not match the DNS hierarchy, but most organizations use the same namespace for both. The Yggdrasil directory uses dc=yggdrasil,dc=no as the root, matching the yggdrasil.no DNS domain, but the DIT structure (ou=people, ou=groups, ou=services) is entirely different from the DNS structure (www, mail, heimdall).

### Required Reading

- Howes, T. & Smith, M. (2036). *LDAP: Programming Directory-Enabled Applications*, 3rd Edition. SAMS. Chapters 1-6.
- Reed, E. (2037). *Understanding and Deploying LDAP Directory Services*, 4th Edition. Addison-Wesley. Chapters 1-5.
- Yggdrasil Identity Management Guide (2040). "LDAP Architecture" and "Directory Tree Design."

### Discussion Questions

1. Two administrators simultaneously modify the same user's email address on different LDAP servers (Oslo and Bergen). Oslo sets the email to "eirik@yggdrasil.no" and Bergen sets it to "erik.h@yggdrasil.no". The last-writer-wins rule applies the Oslo change because it has a later timestamp. Is this the correct resolution? What alternative conflict resolution strategies could be used?
2. LDAP stores passwords as hashes (e.g., bcrypt, Argon2). When a user authenticates, the client sends the password, the server hashes it, and compares the hash. But this means the password is sent in plaintext over the network. How can LDAP authentication be secured? Consider LDAPS (LDAP over TLS), SASL, and Kerberos.
3. An organization has 50,000 users and 1,000 groups in LDAP. A web application needs to check whether user X is a member of group Y. The application queries LDAP for group Y and receives 10,000 member attributes. Design an index and query strategy that makes this membership check efficient (sub-millisecond response time).

---

ᚱ **Lecture 9: Federated Identity and the Heimdall Identity Fabric**

**Course:** CN207 — DNS, DHCP & Directory Services
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

In a world of cloud services, research collaborations, and multi-institutional projects, no single directory can hold every identity. Federated identity allows users to authenticate with their home institution and access services at another institution without creating new accounts. This lecture covers SAML, OpenID Connect, the Yggdrasil Heimdall Identity Fabric, and the future of decentralized identity.

### Key Topics

- **SAML (Security Assertion Markup Language):** The XML-based federation standard used in higher education and government. The SAML triangle: the user (principal), the identity provider (IdP — the user's home institution), and the service provider (SP — the application). The flow: the user tries to access an SP; the SP redirects the user to the IdP; the user authenticates at the IdP; the IdP sends a SAML assertion (an XML statement about the user) to the SP; the SP grants access. The SAML assertion contains attributes (name, email, group membership) that the SP uses for authorization.
- **OpenID Connect (OIDC):** The JSON-based federation standard used by web and mobile applications. Built on top of OAuth 2.0, OIDC adds an identity layer: the IdP returns an ID token (a JWT containing the user's identity) and an access token (for API access). OIDC is simpler than SAML (JSON instead of XML, HTTP redirects instead of SOAP), making it easier to implement and debug. The 2040 state: OIDC is the dominant federation protocol for web applications; SAML remains common in higher education and government.
- **The Heimdall Identity Fabric:** Yggdrasil's federated identity infrastructure. Built on OIDC, the Heimdall Identity Fabric allows students and researchers at Yggdrasil to access services at partner institutions (other Nordic universities, European research organizations, cloud providers) without creating new accounts. The Fabric provides: single sign-on (authenticate once, access all services), attribute aggregation (combine attributes from multiple IdPs), and consent management (the user controls which attributes are released to each SP).
- **Verifiable Credentials and Decentralized Identity:** The W3C Verifiable Credentials standard: a credential is a tamper-evident assertion about a subject, issued by an authority (e.g., Yggdrasil issues a "student" credential to a student), held by the subject (the student stores the credential in a digital wallet), and verified by any party (the verifier checks the credential's cryptographic proof without contacting the issuer). The DID (Decentralized Identifier) standard: a globally unique identifier that does not require a centralized registration authority. DIDs are resolved to DID Documents, which contain public keys and service endpoints.
- **Zero-Knowledge Proofs for Identity:** A zero-knowledge proof (ZKP) allows a user to prove a statement (e.g., "I am over 18") without revealing the underlying data (e.g., their date of birth). ZKPs are built into the Heimdall Identity Fabric for selective disclosure: the user can prove they are a Yggdrasil student without revealing their name, student ID, or other attributes. The cryptographic commitment scheme: the issuer commits to a set of attributes, and the user can open specific commitments to prove specific claims.

### Lecture Notes

The SAML flow is the canonical example of federated identity. When a Yggdrasil student tries to access a research paper at the University of Helsinki, the following happens: (1) The student clicks "Log in with your institution" on Helsinki's website. (2) Helsinki redirects the student to Yggdrasil's Heimdall IdP. (3) The student authenticates at Yggdrasil (using their Yggdrasil username and password, plus MFA). (4) Yggdrasil sends a SAML assertion to Helsinki stating "This user is a student at Yggdrasil, in the Computer Networking program." (5) Helsinki grants access based on the assertion. The entire flow takes 2-5 seconds and requires no account creation at Helsinki.

The key insight of federated identity is that the service provider (Helsinki) does not need to store the user's password or verify their identity — it trusts the identity provider (Yggdrasil) to do this. This trust relationship is established through metadata exchange: Yggdrasil publishes its IdP metadata (including its signing key and endpoints), Helsinki publishes its SP metadata, and both parties configure each other's metadata. The SAML assertion is signed with Yggdrasil's private key, and Helsinki verifies the signature using Yggdrasil's public key. If the signature is valid, Helsinki knows the assertion came from Yggdrasil and has not been tampered with.

The Heimdall Identity Fabric extends this model with attribute aggregation and consent management. Attribute aggregation: a researcher at Yggdrasil may have attributes from multiple IdPs — Yggdrasil (student status), ORCID (researcher identifier), and GitHub (developer status). The Fabric combines these attributes into a single identity profile, allowing the researcher to access services that require multiple attributes (e.g., "must be a student AND have an ORCID ID"). Consent management: the researcher controls which attributes are released to each SP. When Helsinki requests the researcher's email address, the Fabric prompts the researcher to consent. If the researcher declines, Helsinki receives only the attributes they consented to (e.g., the student status, but not the email address).

Verifiable Credentials represent the next evolution of federated identity: from centralized (LDAP stores all attributes) through federated (multiple IdPs each store their own attributes) to decentralized (the user holds their own credentials). In the Verifiable Credentials model, Yggdrasil issues a "Student" credential to the student, who stores it in a digital wallet on their phone. When the student needs to prove they are a student at Helsinki, they present the credential from their wallet. Helsinki verifies the credential's cryptographic proof (signed by Yggdrasil's private key) without contacting Yggdrasil. The advantage: Helsinki does not need to know the student's name, email, or any other attribute — only that they are a student. The challenge: key management. If the student loses their wallet, they lose all their credentials. If Yggdrasil's private key is compromised, all credentials issued by Yggdrasil are compromised. The Heimdall Identity Fabric addresses this with revocation registries (a public list of revoked credential IDs) and key rotation procedures.

### Required Reading

- Cantor, S., et al. (2035). "Assertions and Protocols for the OASIS Security Assertion Markup Language (SAML)," v2.1. OASIS.
- Sakimura, N., et al. (2036). "OpenID Connect Core 1.1," OIDC Foundation.
- W3C (2037). "Verifiable Credentials Data Model v2.0." W3C Recommendation.
- Yggdrasil Identity Management Guide (2040). "Heimdall Identity Fabric" and "Verifiable Credentials."

### Discussion Questions

1. In the SAML flow, the identity provider sends a SAML assertion to the service provider. The assertion contains the user's attributes (name, email, group membership). How can the user control which attributes are released? What are the privacy implications of sending all attributes by default?
2. Verifiable Credentials allow the user to prove claims without contacting the issuer. But this means the service provider cannot verify that the credential is still valid (the user may have graduated, and the "Student" credential should no longer be accepted). How does the revocation registry solve this problem? What are the limitations of revocation registries (consider scalability, privacy, and availability)?
3. Zero-knowledge proofs allow selective disclosure (proving "I am over 18" without revealing the date of birth). But ZKPs are computationally expensive. A mobile phone takes 50 ms to generate a ZKP. Is this acceptable for a login flow that should complete in under 2 seconds? How could ZKP performance be improved?

---

ᚴ **Lecture 10: DNS-Based Service Discovery and Load Balancing**

**Course:** CN207 — DNS, DHCP & Directory Services
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

DNS is not just for mapping names to addresses — it is also a service discovery mechanism and a load-balancing tool. This lecture covers SRV records, the HTTPS/SVCB record type, DNS-based load balancing, geo-DNS, and the 2040 DNS Service Discovery (DNS-SD) ecosystem.

### Key Topics

- **SRV Records:** The DNS Service record (SRV) maps a service name to a host and port: _service._proto.domain → priority weight port target. Example: _ldap._tcp.yggdrasil.no SRV 10 60 389 ldap.yggdrasil.no means that the LDAP service at yggdrasil.no is available on ldap.yggdrasil.no port 389, with priority 10 and weight 60. Clients use SRV records to discover services without hard-coding hostnames and ports.
- **HTTPS/SVCB Records:** The 2040 evolution of service discovery. The HTTPS record type (formerly SVCB) allows a domain to specify: which protocols it supports (HTTP/2, HTTP/3/QUIC), which IP addresses it uses (inline A/AAAA records, eliminating the need for separate lookups), and which alternative services are available (portrait services, CDN endpoints). The HTTPS record reduces connection setup time by providing all necessary information in a single DNS response.
- **DNS-Based Load Balancing:** Round-robin DNS: returning multiple A/AAAA records for a hostname, with the order rotated for each query. The client typically uses the first address, and the rotate order changes between queries, distributing traffic across multiple servers. Limitations: no health checking (a failed server continues to receive traffic), no session affinity (the client may use a different server on each query), and uneven distribution (clients with long-lived caches may always use the same server).
- **Geo-DNS:** Returning different IP addresses based on the client's geographic location. The DNS resolver's IP address is mapped to a location (using a geo-IP database), and the authoritative server returns the IP address of the nearest server. Example: resolving www.yggdrasil.no from Oslo returns the Oslo server's IP, while resolving from Tromsø returns the Tromsø server's IP. The 2040 state: real-time health checking, automatic failover, and anycast routing supplement geo-DNS.
- **DNS Service Discovery (DNS-SD):** The 2040 ecosystem for discovering services on a local network. DNS-SD uses PTR records for service enumeration, SRV records for service endpoints, and TXT records for service attributes. Example: browsing for LDAP servers on the Yggdrasil network: _ldap._tcp.yggdrasil.no PTR returns a list of LDAP servers, each with an SRV record (host and port) and a TXT record (attributes like "tls=yes" and "method=sasl"). The NEURO record type extends DNS-SD for AI-mediated service discovery.

### Lecture Notes

SRV records were introduced in 2000 (RFC 2782) to solve a simple problem: hard-coding server hostnames and ports in client configurations is fragile. When the LDAP server moves from ldap.yggdrasil.no to ldap2.yggdrasil.no, or the port changes from 389 to 636 (LDAPS), every client configuration must be updated. SRV records solve this by separating the service name from the server identity: the client queries for _ldap._tcp.yggdrasil.no and receives the current server and port. When the server changes, the administrator updates the SRV record, and all clients automatically pick up the change. The priority and weight fields enable load balancing: priority determines the order of preference (lower priority is preferred), and weight determines the proportional load distribution among servers with the same priority.

The HTTPS record type, introduced in 2020 and widely deployed by 2040, goes further. A single HTTPS record for yggdrasil.no can contain: the supported protocols (HTTP/2, HTTP/3/QUIC), the IP addresses (inline, eliminating the need for separate A/AAAA lookups), the port (443, or a custom port), and alternative endpoints (e.g., a CDN endpoint for static assets). The result: a client needs only one DNS query (the HTTPS record) to obtain all the information needed to establish a connection, reducing connection setup time from 3-5 DNS queries to 1. For QUIC connections, the HTTPS record also includes the post-quantum key (QKEY), enabling 0-RTT connection establishment without separate certificate lookups.

DNS-based load balancing is the simplest form of traffic distribution, but its limitations are significant. Round-robin DNS distributes traffic roughly evenly across servers, but it cannot detect server failures — a dead server continues to receive DNS queries, and clients that resolve to the dead server's IP address will experience connection failures. Modern DNS load balancing (as offered by Cloudflare, AWS Route 53, and the Bifrǫst DNS Load Balancer) supplements round-robin with health checking: the authoritative server periodically polls each backend server, and removes failed servers from the DNS response. The Bifrǫst DNS Load Balancer checks server health every 10 seconds and updates DNS records within 30 seconds of a failure, ensuring that clients receive only healthy server IP addresses.

Geo-DNS is the DNS analog of content delivery networks. When a client in Bergen resolves www.yggdrasil.no, the authoritative server determines the client's location (using the resolver's IP address and a geo-IP database) and returns the IP address of the Bergen server. When a client in Tromsø resolves the same hostname, the authoritative server returns the Tromsø server's IP. The result: lower latency (the client connects to the nearest server) and better load distribution (traffic is spread across multiple servers). The challenge: the authoritative server sees the resolver's IP address, not the client's — if the client uses a public resolver (e.g., 1.1.1.1) that is located far from the client, the geo-DNS response may be incorrect. The 2040 solution: EDNS(0) Client Subnet, an extension that passes the client's subnet (not the full IP, for privacy) to the authoritative server, enabling accurate geo-routing.

### Required Reading

- Gulbrandsen, A., et al. (2000). "A DNS SRV (Service Location) Record," RFC 2782. IETF. (Still the foundation.)
- Schwartz, B., et al. (2034). "Service Binding and Parameter Specification via the DNS," RFC 9460 (HTTPS/SVCB). IETF.
- Yggdrasil DNS Operations Guide (2040). "Service Discovery" and "Load Balancing."

### Discussion Questions

1. An HTTPS record for example.com includes both an A/AAAA record and an alternative endpoint (cdn.example.com). A client resolves example.com and receives both the origin IP and the CDN IP. Which should it connect to? Design a client algorithm that selects the optimal endpoint based on connection time, QUIC support, and geographic proximity.
2. Round-robin DNS distributes traffic across servers but does not provide session affinity (a client may connect to a different server on each query). For an application that stores session state on the server, this is a problem. How would you achieve session affinity with DNS-based load balancing? Consider cookie-based affinity, source-IP hashing, and anycast routing.
3. Geo-DNS uses the resolver's IP address to determine the client's location. If the client uses a public resolver (e.g., 1.1.1.1) located far from the client, the geo-DNS response will be incorrect. Explain how EDNS(0) Client Subnet solves this problem. What privacy concerns does EDNS(0) Client Subnet raise, and how does the /24 prefix masking (sending only the client's /24, not the full IP) address these concerns?

---

ᚬ **Lecture 11: DNS Operations, Monitoring, and Incident Response**

**Course:** CN207 — DNS, DHCP & Directory Services
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

DNS operations is where theory meets reality. This lecture covers the day-to-day operational practices that keep DNS, DHCP, and directory services running: monitoring, alerting, incident response, change management, and the operational runbooks that guide engineers through common and critical scenarios.

### Key Topics

- **DNS Monitoring:** Resolution latency (how long queries take), error rates (SERVFAIL, NXDOMAIN, timeout), cache hit ratio (what percentage of queries are answered from cache), and query volume (queries per second). The Yggdrasil Heimdall monitoring stack: Prometheus metrics from the resolver, Grafana dashboards for visualization, and Alertmanager for alerting. The critical metrics: 99th percentile resolution latency < 100 ms, SERVFAIL rate < 0.1%, cache hit ratio > 90%.
- **DHCP Monitoring:** Lease utilization (what percentage of the address pool is leased), lease renewal rate (what percentage of clients successfully renew), and conflict rate (how many address conflicts are detected). The Yggdrasil DHCP monitoring: lease utilization < 80% (alert if > 80%), renewal success rate > 99%, and conflict rate < 0.01%.
- **LDAP Monitoring:** Bind latency (how long authentication takes), search latency (how long queries take), replication lag (how far behind replicas are), and connection count (how many clients are connected). The Yggdrasil LDAP monitoring: bind latency < 50 ms, search latency < 100 ms, replication lag < 5 seconds, and connection count < 1,000 per server.
- **Incident Response:** The DNS incident response runbook: (1) detect (monitoring alert), (2) assess (is it DNS, DHCP, or LDAP? is it affecting one service or all services?), (3) mitigate (failover to secondary, flush cache, restart service), (4) communicate (notify stakeholders), (5) resolve (fix the root cause), and (6) review (post-incident analysis). Case study: the 2034 Nordic DNS Outage — what went wrong, how it was mitigated, and what was learned.
- **Change Management:** The cadence of DNS changes: zone file updates (hours to days), TTL changes (minutes to hours), emergency changes (minutes). The principle of least TTL: when making a change, reduce the TTL first, wait for the old TTL to expire, make the change, then restore the original TTL. This ensures that the change propagates quickly, but the low-TTL period increases load (more cache misses).

### Lecture Notes

DNS monitoring is the first line of defense against DNS outages. The Yggdrasil Heimdall monitoring stack tracks resolution latency, error rates, and cache hit ratio for every resolver in the Bifrǫst Mesh. Resolution latency is the most critical metric — if queries are slow, every application on the network is slow. The 99th percentile latency target is 100 ms, meaning that 99% of queries must be resolved in under 100 ms. If the 99th percentile exceeds 200 ms, an alert fires and the on-call engineer is paged. The most common causes of high resolution latency are: upstream server slowness (the authoritative server is slow to respond), cache misses (a popular domain's TTL has expired), and DNSSEC validation overhead (signature verification takes CPU time).

DHCP lease utilization is the canary in the coal mine for IP address exhaustion. If lease utilization exceeds 80%, it means the address pool is running low, and action is needed (expand the pool, shorten lease times, or migrate to IPv6 where address scarcity is not a concern). The Yggdrasil DHCP system uses IPv6, where address scarcity is not an issue (each /64 subnet has 2⁶⁴ addresses), but IPv4 address pools on the NAT64 gateways are carefully monitored. The NAT64 gateway has a pool of 65,536 IPv4 addresses that are shared among all IPv6-only clients. When a client connects to an IPv4-only service, the NAT64 gateway assigns a port-mapped IPv4 address from the pool and creates a translation entry. The gateway uses port multiplexing (one IPv4 address, 65,535 ports) to serve thousands of clients with a single IPv4 address.

LDAP replication lag is the distance between the master and replica servers. When an administrator modifies an entry on the Oslo server, the change is replicated to Bergen and Tromsø within seconds. But if the Bergen server is under heavy load or the network between Oslo and Bergen is congested, replication can lag. If replication lag exceeds 5 seconds, an alert fires. If it exceeds 60 seconds, the replica is considered stale and is removed from the load-balancing pool (authentication requests are directed to other replicas). If it exceeds 300 seconds, the on-call engineer is paged. The 2040 target: replication lag < 5 seconds for all directory servers.

The 2034 Nordic DNS Outage is the standard case study for DNS incident response. At 08:15 on March 15, 2034, NORID began a DNSSEC key rollover for the .no TLD. The rollover procedure required updating the DS record in the root zone to point to the new KSK. The update was scheduled for 08:00, but a misconfiguration caused the old DS record to be revoked at 08:15 before the new DS record had fully propagated. Validating resolvers that received the revocation before the new DS record returned SERVFAIL for all .no domains. The incident was detected by the NORID monitoring system at 08:18 (an increase in SERVFAIL responses from 0.1% to 45%). The mitigation was to immediately publish the new DS record and wait for propagation. The entire .no zone was affected for 4 hours, until all resolvers had cached the new DS record. The post-incident analysis identified three root causes: (1) the key rollover procedure did not include a "dual-signing" phase where both old and new DS records were valid simultaneously; (2) the monitoring system did not alert on DNSSEC validation failures in real time; and (3) the rollback procedure was not tested before the rollover. All three root causes were addressed in the updated key rollover procedure.

### Required Reading

- Larson, M. & Liu, C. (2037). *DNS and BIND*, 8th Edition. O'Reilly. Chapters 13-16 (Monitoring and Troubleshooting).
- Yggdrasil Incident Response Runbooks (2040). "DNS Outage," "DHCP Failure," and "LDAP Replication Failure."
- Yggdrasil Monitoring Architecture (2040). "Heimdall Monitoring Stack."

### Discussion Questions

1. The monitoring system fires an alert: DNS resolution latency has increased from 15 ms to 500 ms. List the possible root causes and describe the troubleshooting steps you would take to identify and fix the issue.
2. DHCP lease utilization on a campus network has reached 85%. The network uses IPv4 with a /22 subnet (1,022 usable addresses). Calculate how many addresses are available. What actions can you take to address the address shortage? Consider expanding the subnet, shortening lease times, and migrating to IPv6.
3. LDAP replication lag between Oslo and Bergen has increased to 45 seconds. The Bergen server is under heavy load (CPU at 95%). What steps would you take to reduce replication lag? Consider optimizing queries, adding a replica, increasing server capacity, and adjusting replication settings.

---

ᛃ **Lecture 12: The Future of Naming, Addressing, and Identity**

**Course:** CN207 — DNS, DHCP & Directory Services
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

DNS, DHCP, and directory services are mature technologies, but they continue to evolve. This final lecture surveys the frontiers: decentralized naming systems (ENS, Handshake), post-quantum DNSSEC, AI-driven DNS optimization, and the convergence of naming, addressing, and identity in the 2040s and beyond.

### Key Topics

- **Decentralized Naming Systems:** ENS (Ethereum Name Service): names stored on the Ethereum blockchain, resolved by smart contracts. Handshake: a decentralized root zone that replaces the ICANN root with a blockchain. Unstoppable Domains: names stored on Polygon, resolved by browsers with blockchain support. The tradeoffs: decentralization vs. governance (blockchain names are censorship-resistant but also unregulable), immutability vs. updatability (blockchain records are permanent, but DNS records must be updateable), and cost (Ethereum gas fees vs. traditional DNS registration fees).
- **Post-Quantum DNSSEC:** Replacing RSA and ECDSA with CRYSTALS-Dilithium for DNSSEC signatures. The performance impact: Dilithium signatures are 2.4 KB (vs. 256 bytes for ECDSA), increasing DNS response sizes and the risk of UDP fragmentation. The mitigation: larger EDNS(0) buffer sizes, TCP fallback, and hybrid signing (RSA + Dilithium for transition). The timeline: the root KSK is scheduled to transition to Dilithium in 2045.
- **AI-Driven DNS Optimization:** Using machine learning to predict DNS queries (prefetch popular domains before they are requested), optimize cache TTLs (adjust TTLs based on query patterns), and detect anomalies (identify malware domains by statistical analysis of query patterns). The Yggdrasil Heimdall AI: a neural network that processes 10 million DNS queries per second, learns query patterns, and optimizes cache management in real time. The result: 30% increase in cache hit ratio and 50% reduction in outlier detection time.
- **The Convergence of Naming, Addressing, and Identity:** The 2040 trend: DNS records are no longer just name-to-address mappings — they carry identity information (QKEY records for post-quantum TLS, NEURO records for AI service discovery, HTTPS records for protocol negotiation). The future: a unified naming-addressing-identity system where a single query returns everything a client needs to connect (address, protocol, encryption key, and service attributes). The challenge: updating 40 years of DNS infrastructure.
- **The Role of the Network Engineer:** DNS, DHCP, and directory services are the invisible infrastructure that makes networks usable. The network engineer who understands these services at the bit level, operates them with rigor, and evolves them with the times is the engineer who keeps the network running. The Yggdrasil commitment: naming, addressing, and identity as a public good, accessible to all.

### Lecture Notes

Decentralized naming systems challenge the fundamental assumption of DNS: that naming authority is hierarchical and delegated from the root. ENS, Handshake, and Unstoppable Domains propose an alternative: names are registered on a blockchain, and resolution is performed by smart contracts or peer-to-peer networks, without a central authority. The advantage: censorship resistance (no government can revoke a domain name) and permanence (blockchain records cannot be tampered with). The disadvantage: governance (who resolves disputes over trademark infringement?), updatability (blockchain records are permanent, but DNS records must be updateable), and user experience (resolving blockchain names requires a browser extension or a DNS-to-blockchain bridge).

The ENS system, built on Ethereum, is the most mature decentralized naming system. An ENS name (e.g., yggdrasil.eth) is registered by paying a fee in ETH and is stored in an Ethereum smart contract. Resolution is performed by querying the smart contract, which returns the associated Ethereum address, IPFS content hash, or traditional DNS records. ENS has the advantage of being censorship-resistant (no central authority can revoke a name) and interoperable (it can resolve to any type of record). The disadvantage: resolving ENS names requires an Ethereum client, which is slow (Ethereum blocks are every 12 seconds) and expensive (gas fees for interactions). The practical solution: ENS-to-DNS bridges that allow ENS names to be resolved through traditional DNS resolvers, at the cost of some decentralization.

Post-quantum DNSSEC is the most pressing operational challenge for DNS in 2040. The current DNSSEC signing algorithms (RSA and ECDSA) are vulnerable to quantum computers: a sufficiently powerful quantum computer running Shor's algorithm could factor RSA keys and compute ECDSA discrete logarithms, allowing an attacker to forge DNSSEC signatures. The transition to post-quantum algorithms (CRYSTALS-Dilithium for signatures, CRYSTALS-Kyber for key exchange) is underway but will be operationally complex. Dilithium signatures are 2.4 KB (compared to 256 bytes for ECDSA), which means DNSSEC responses will be significantly larger. A single DNSSEC response with Dilithium signatures may exceed the 4096-byte EDNS(0) buffer size, requiring TCP fallback. The root KSK transition to Dilithium is planned for 2045, following a 3-year dual-signing period (2042-2045) where both ECDSA and Dilithium signatures are included in DNSSEC responses. After 2045, only Dilithium signatures will be included.

The Yggdrasil Heimdall AI processes 10 million DNS queries per second and uses machine learning to optimize three aspects of DNS performance. First, prefetching: the AI predicts which domains will be queried next (based on historical patterns and time of day) and refreshes their cache entries before they expire, reducing cache misses by 30%. Second, TTL optimization: the AI adjusts TTLs based on query patterns, using shorter TTLs for domains that change frequently and longer TTLs for stable domains. Third, anomaly detection: the AI identifies malware domains by statistical analysis of query patterns — domains that are queried by a small number of clients, at unusual times, from unusual geographic locations, or with unusual query types. The Heimdall AI detected 15,000 malware domains in 2040, 40% of which had not yet been added to any threat intelligence feed.

### Required Reading

- ENS Documentation (2040). "How ENS Works." ens.domains.
- Barker, E. (2039). "Post-Quantum Cryptography for DNSSEC: Transition Guide." *NIST Special Publication 800-236*.
- Yggdrasil DNS Operations Guide (2040). "Heimdall AI" and "Post-Quantum DNSSEC Transition."

### Discussion Questions

1. ENS names are stored on the Ethereum blockchain and resolved by smart contracts. An attacker exploits a smart contract vulnerability and registers yggdrasil.eth for themselves. ENS governance votes to transfer the name back to Yggdrasil, but the attacker argues that blockchain names should be immutable and censorship-resistant. Who is right? How should decentralized naming systems handle disputes?
2. Post-quantum DNSSEC signatures are 2.4 KB (Dilithium) vs. 256 bytes (ECDSA). Calculate the increase in DNS response size for a typical signed zone with 10 records. How many additional DNS messages (beyond the initial query) are needed to transfer the response? What percentage of queries would fall back to TCP?
3. The Heimdall AI detected 15,000 malware domains in 2040, 40% of which had not yet been added to any threat intelligence feed. Does this justify the use of AI-driven DNS monitoring? What are the risks of false positives (blocking legitimate domains) and false negatives (missing malware domains)? How should the balance between security and accessibility be struck?

---

## Final Examination Preparation

The CN207 final examination is a **3-hour written exam** plus a **practical lab assessment**.

### Written Examination (60%)

**Sample Questions:**

1. "Trace the complete DNS resolution of heimdall.yggdrasil.no from a client in Bergen, including all queries (stub resolver → recursive resolver → root → TLD → authoritative), the records returned at each step, and the cache entries created. Assume no prior cache entries."

2. "The .no TLD is performing a DNSSEC key rollover. Describe the rollover procedure, including the ZSK rollover (changing the Zone Signing Key) and the KSK rollover (changing the Key Signing Key and updating the DS record in the root zone). What is the purpose of the dual-signing period?"

3. "Design a DHCPv6/SLAAC architecture for a campus network with 10,000 devices. Specify the prefix delegation scheme (how many /48, /56, /64 prefixes), the SLAAC configuration, and the stateless DHCPv6 configuration. How does this architecture handle device mobility between buildings?"

4. "A recursive resolver is returning SERVFAIL for www.example.com. Describe the troubleshooting steps you would take, including checking DNSSEC validation, querying the authoritative server directly, examining the RRSIG records, and verifying the chain of trust from the root to example.com."

5. "Compare SAML and OpenID Connect for federated authentication. What are the advantages and disadvantages of each? In what scenarios would you choose SAML over OIDC, and vice versa?"

6. "Design an LDAP directory tree for a university with 20,000 students, 2,000 faculty, and 500 staff. Specify the DIT structure (ou=people, ou=groups, ou=services), the object classes and attributes for each entry type, the ACLs for delegated administration, and the replication topology (3 servers in Oslo, Bergen, Tromsø)."

### Practical Lab Assessment (40%)

Students configure and operate DNS, DHCP, and directory infrastructure in the Valhalla Network Lab:
- Configure an authoritative DNS server for a zone with DNSSEC signing, verify the chain of trust, and perform a key rollover
- Configure a recursive resolver with DNSSEC validation, DoH/DoT support, and caching
- Configure a DHCPv6 server with prefix delegation and verify SLAAC operation
- Configure an LDAP directory with user entries, group entries, and ACLs
- Configure federated authentication (SAML or OIDC) between two lab servers
- Troubleshoot a pre-configured DNS, DHCP, or LDAP problem (SERVFAIL, address conflict, replication lag)

### Grading Rubric

| Criterion | Weight | Excellent (A) | Good (B) | Satisfactory (C) | Needs Improvement (D/F) |
|-----------|--------|---------------|----------|------------------|---------------------------|
| Protocol Knowledge | 25% | Deep understanding of DNS/DHCP/LDAP internals, able to trace resolution at the bit level | Good understanding of protocol mechanics | Adequate knowledge of basic protocols | Shallow or incorrect understanding |
| Operational Reasoning | 25% | Systematic troubleshooting, correct diagnosis, practical solutions | Good troubleshooting, mostly correct | Adequate but incomplete troubleshooting | Unable to diagnose or fix problems |
| Design Quality | 20% | Elegant, well-justified designs with scalability and resilience | Good designs with reasonable rationale | Adequate designs, limited justification | Poor or incomplete designs |
| Communication | 15% | Clear, precise, well-organized | Good clarity; minor issues | Adequate but verbose or unclear | Disorganized or incoherent |
| Security Awareness | 15% | Thoughtful consideration of DNSSEC, encrypted DNS, access control, and privacy | Good awareness of key security issues | Minimal security awareness | No security consideration |

---

*Woven by the hands of Runa Gridweaver Freyjasdóttir, student of the University of Yggdrasil, 2040. May the packets flow smoothly and the routes never loop.* ᛟ