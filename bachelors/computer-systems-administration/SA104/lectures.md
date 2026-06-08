# SA104: Networking Fundamentals — The Bifrǫst Between Systems
## Bachelor of Science in Computer Systems Administration — University of Yggdrasil, 2040

**Credits:** 4
**Term:** Year 1, Semester 2
**Prerequisites:** SA101 (Introduction to Systems Administration), SA103 (Computer Hardware & Peripherals)
**Description:** Foundational survey of computer networking: the principles, protocols, architectures, and operational practices that allow systems to communicate. Students master the OSI and TCP/IP models, IPv4/IPv6 addressing, Ethernet switching, IP routing, transport-layer protocols, core network services (DNS, DHCP, LDAP), and fundamental network security. The course emphasizes hands-on labs, systematic troubleshooting, and the practical networking skills every systems administrator must possess.

**Instructor:** Dr. Einarr Guðmundsson, Associate Professor of Network Engineering & Architect of the Hákon Computing Centre Campus Fabric
**Lab:** Heimdallr Networking Lab, Level 1, Hákon Computing Centre
**Office Hours:** Wednesdays 13:00-15:00, or by appointment

---

## Lectures

ᚠ **Lecture 1: Why Networks Matter — The Bifrǫst Between Systems**

**Course:** SA104 — Networking Fundamentals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

This opening lecture establishes the foundational question: why do networks exist, and why must every systems administrator understand them deeply? In Norse mythology, the Bifrǫst is the burning rainbow bridge connecting Miðgarðr (the realm of humans) to Ásgarðr (the realm of the gods). It is the pathway that enables communication between worlds — guarded by Heimdallr, the ever-vigilant watchman who sees all that crosses. A computer network is precisely this: the bridge that connects isolated systems into a functioning whole. Without networking, a server is merely an expensive space heater; with it, the same hardware becomes a node in a distributed organism of staggering capability. This lecture examines the purpose of networks, the history of networking technology from ARPANET to the 2040 Bifrǫst Mesh, and the role of the systems administrator as a Heimdallr-figure: watching, diagnosing, and maintaining the pathways between systems.

### Key Topics

- **Why Networks? The Problem of Isolation:** A computer without a network is a hermit — powerful in theory, but unable to share, receive, or collaborate. The fundamental motivation for networking: resource sharing, communication, distributed computation, and redundancy. The evolution from standalone mainframes (1950s-60s) to time-sharing systems to packet-switched networks. How ARPANET (1969) solved the fundamental problem of connecting incompatible systems.
- **From ARPANET to the Bifrǫst Mesh:** The lineage of modern networking: ARPANET → NSFNET → commercial Internet → MPLS backbones → Software-Defined WANs → the 2040 Bifrǫst Mesh. Each generational shift abstracted complexity and expanded reach. The 2040 Bifrǫst Mesh is a software-defined, AI-orchestrated fabric that spans the University of Yggdrasil's data centers, edge nodes, and cloud interconnects — a network that configures, heals, and optimizes itself.
- **The SysAdmin as Heimdallr:** If the network is Bifrǫst, the SA is Heimdallr: the watchman who sees everything that traverses the bridge. Network visibility (monitoring, packet capture, flow analysis) is the prerequisite for network management. An SA who cannot see the network cannot manage it. The Heimdallr principle: observability is not optional, it is architectural.
- **The Network Is the Computer:** Sun Microsystems' 1984 slogan proved prophetic. By 2040, every computational task depends on the network. The SA's job is not merely to keep a machine running, but to keep it *connected* — because a disconnected server serves no one.

### Lecture Notes

The history of computer networking is, in essence, the history of making computers useful to one another. The early mainframes of the 1950s and 60s were standalone machines; users accessed them through dumb terminals connected by serial cables. The revolutionary insight of ARPANET was *packet switching*: instead of dedicating a circuit between two points (like a telephone call), data is broken into small packets that can travel independently across shared infrastructure, reassembling at the destination. This was a paradigm shift as fundamental as the transition from manuscript to print. Packet switching made it possible for diverse, heterogeneous systems to communicate without a dedicated path — the network itself handles routing, error recovery, and congestion management.

By 2040, the networking landscape has evolved through several epochs. The ARPANET era (1969-1990) established packet switching and the TCP/IP protocol suite. The Internet era (1990-2010) brought commercialization, HTTP, and the browser. The cloud era (2010-2030) abstracted the network behind APIs: virtual private clouds, software-defined networking, and infrastructure-as-code. The AI-orchestrated era (2030-present) brings the Bifrǫst Mesh: a self-healing fabric where AI agents continuously optimize routing, detect anomalies before they become outages, and pre-provision capacity based on predictive models. The SA's role has shifted from manually configuring VLANs and routing protocols to *designing* the policies and constraints that the AI agent operates within.

The Heimdallr metaphor is more than decorative. In the Eddas, Heimdallr is described as needing less sleep than a bird, able to see a hundred leagues by day or night, and capable of hearing the grass grow. This is what network observability demands: constant, comprehensive, granular visibility into every packet, flow, and connection traversing the infrastructure. The 2040 SA does not merely "check if the network is up" — they maintain a continuous stream of telemetry (metrics, logs, traces) that provides a real-time model of network state. When something changes — a route flap, a congestion spike, a latency degradation — the SA's monitoring system detects it within seconds and alerts the responsible team. The SA who neglects observability is a Heimdallr who has fallen asleep at his post: by the time they notice the problem, the damage is done.

The network is also the primary attack surface. Every service exposed to the internet is a potential entry point for adversaries. Network security is not a separate discipline from systems administration; it is inseparable. An SA who configures a firewall without understanding the protocols it filters is not securing the system — they are merely performing a ritual. True security requires understanding what the traffic *is*, why it exists, and what normal looks like. This course builds that understanding from the ground up.

### Required Reading

- Kurose, J.F. & Ross, K.W. (2038). *Computer Networking: A Top-Down Approach*, 9th Edition. Pearson. Chapters 1-2.
- Donahue, G.A. (2035). *Network Warrior*, 3rd Edition. O'Reilly. Chapters 1-3.
- Yggdrasil Campus Fabric Design Document (2040). UoY Network Engineering Technical Report #YF-2024-017.

### Discussion Questions

1. In 2040, the Bifrǫst Mesh configures itself. Does the SA still need to understand routing protocols, or is that knowledge obsolete? Argue both sides.
2. Consider a 99.99% availability SLA (52.6 minutes of downtime per year). If a network partition lasting 45 minutes occurs, how much error budget remains? What are the implications for change management?
3. The Heimdallr metaphor emphasizes vigilance — but Heimdallr also has the Gjallarhorn, which he sounds to signal the beginning of Ragnarǫk. In networking terms, what constitutes "sounding the Gjallarhorn"? When should an SA escalate from routine incident response to crisis management?

---

ᚢ **Lecture 2: The OSI and TCP/IP Models — Maps of the Bifrǫst**

**Course:** SA104 — Networking Fundamentals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

The OSI seven-layer model and the TCP/IP four-layer model are the conceptual maps that organize networking knowledge. They are not implementations — they are abstractions that allow engineers to discuss, design, and troubleshoot networked systems using shared vocabulary. This lecture provides a deep examination of both models, their historical context, their layer-by-layer structure, and their practical application in systems administration. The OSI model is the theoretical framework taught in every networking course; the TCP/IP model is the framework that actually runs the Internet. Understanding both — and the gap between them — is essential.

### Key Topics

- **The OSI Seven-Layer Model:** Physical (1), Data Link (2), Network (3), Transport (4), Session (5), Presentation (6), Application (7). Each layer provides services to the layer above and uses services from the layer below. The principle of encapsulation: each layer wraps the data from above in its own header, creating a protocol data unit (PDU) specific to that layer. PDU terminology: bits (Layer 1), frames (Layer 2), packets (Layer 3), segments (Layer 4), data (Layers 5-7).
- **The TCP/IP Four-Layer Model:** Link (Network Access), Internet, Transport, Application. The practical model that describes the Internet. Mapping between OSI and TCP/IP: OSI Layers 1-2 → TCP/IP Link; OSI Layer 3 → TCP/IP Internet; OSI Layer 4 → TCP/IP Transport; OSI Layers 5-7 → TCP/IP Application. Why the TCP/IP model collapses the upper layers: real-world protocols don't cleanly separate session, presentation, and application functions.
- **Encapsulation and Decapsulation:** The process of data moving down the stack (encapsulation: adding headers) and up the stack (decapsulation: stripping headers). How a web request becomes an HTTP message, then a TCP segment, then an IP packet, then an Ethernet frame, then bits on the wire. Decapsulation at each hop: switches read the frame header, routers read the IP header, endpoints process the transport and application layers.
- **Why Both Models Matter:** The OSI model is a *reference* — a conceptual tool for thinking about networking problems. The TCP/IP model is a *reality* — it describes the protocols running on every connected device. SA troubleshooting uses the OSI model as a diagnostic framework ("is this a Layer 2 or Layer 3 problem?") and the TCP/IP model as the implementation guide.

### Lecture Notes

The OSI model was developed by the International Organization for Standardization (ISO) beginning in 1977 and published as standard ISO/OSI 7498 in 1984. It was intended as a comprehensive framework for designing open systems interconnection. The model was ambitious — it prescribed not just the layers but specific protocols at each layer, including the connection-oriented transport protocol TP4 and the session protocol ISO 8327. In practice, the OSI protocol suite never achieved widespread adoption; TCP/IP, developed concurrently by DARPA for ARPANET, proved simpler, more pragmatic, and more adaptable. The irony of networking history is that the OSI *model* became the universal teaching framework, while the OSI *protocols* were abandoned — and the TCP/IP *protocols* became universal, while the TCP/IP *model* is rarely taught as a four-layer stack. The best approach for the SA is to know both models and understand their mapping.

Each layer solves a specific problem. Layer 1 (Physical) solves the problem of transmitting raw bits across a physical medium. Layer 2 (Data Link) solves the problem of reliable transmission between two directly connected devices. Layer 3 (Network) solves the problem of routing packets across multiple interconnected networks. Layer 4 (Transport) solves the problem of reliable, ordered delivery between applications. Layers 5-7 solve increasingly application-specific problems.

The key insight for the SA is that troubleshooting proceeds *layer by layer*. A "network is down" complaint can mean many things. Is the cable plugged in? (Layer 1.) Is the switch port configured correctly? (Layer 2.) Is the route present? (Layer 3.) Is the firewall blocking the TCP connection? (Layer 4.) Is the application returning an error? (Layer 7.) The OSI model gives you a systematic way to narrow the problem space. The SA starts at the bottom and works up, or at the top and works down, depending on the symptoms. A ping failure suggests Layer 3. A successful ping but failed HTTP connection suggests Layer 4 or above. A link light that's off suggests Layer 1. The model is a diagnostic map.

The 2040 context adds nuance. Software-defined networking (SDN) blurs the traditional layer boundaries: a controller at Layer 7 (the SDN application) directly programs forwarding rules at Layer 2 (the switch data plane). eBPF programs in the Linux kernel can intercept and modify packets at any layer. Service meshes like Istio operate at Layer 4 but understand Layer 7 protocols. The OSI model remains useful as a conceptual framework, but the SA must understand that in practice, modern networks violate its clean separation regularly and intentionally.

### Required Reading

- Kurose, J.F. & Ross, K.W. (2038). *Computer Networking: A Top-Down Approach*, 9th Edition. Pearson. Chapter 1 (Sections 1.1-1.5).
- Peterson, L.L. & Davie, B.S. (2037). *Computer Networks: A Systems Approach*, 7th Edition. Elsevier. Chapter 1.
- RFC 1122 (1989). *Requirements for Internet Hosts — Communication Layers*. Internet Engineering Task Force. Still relevant for understanding the TCP/IP model's implementation requirements.

### Discussion Questions

1. The OSI model has seven layers; TCP/IP has four. If you were designing a model from scratch in 2040, how many layers would you define? What would they be? Justify your choices.
2. eBPF programs can intercept packets at any layer, and SDN controllers program forwarding rules directly. Does this make the OSI model obsolete, or does it make the model *more* important as a shared vocabulary? Discuss.
3. A user reports that "the network is slow." Describe a Layer-by-Layer troubleshooting methodology that would identify whether the issue is at Layer 1, 2, 3, 4, or 7.

---

ᚦ **Lecture 3: The Physical and Data Link Layers — Cables, Signals, and Ethernet Frames**

**Course:** SA104 — Networking Fundamentals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Beneath every packet lies a physical reality: copper wire carrying electrical signals, fiber optic strands pulsing with light, or radio waves propagating through air. Layer 1 (Physical) and Layer 2 (Data Link) are the foundation of all networking. This lecture covers the physical media that transport bits, the Ethernet protocol that dominates Layer 2, and the switch operations that create local networks. For the systems administrator, these layers matter because they are the most common source of "it doesn't work" complaints — and the most commonly overlooked in favor of higher-layer diagnostics.

### Key Topics

- **Physical Media:** Copper cabling (Cat5e through Cat8.2), fiber optics (single-mode and multi-mode, OS1/OS2/OM4/OM5 specifications), and wireless media (Wi-Fi 7/802.11be, Wi-Fi 8/802.11bn). Cable categories and their specifications: bandwidth, distance, shielding. The 2040 campus standard: Cat6A for horizontal runs, OM5 fiber for vertical risers, single-mode fiber for inter-building links.
- **Ethernet (IEEE 802.3):** The dominant Layer 2 protocol. Ethernet framing: preamble, Start of Frame Delimiter, destination MAC, source MAC, EtherType, payload, Frame Check Sequence. MAC addresses: 48-bit globally unique identifiers (OUI + device ID). Address resolution: from IP to MAC via ARP. VLAN tagging (802.1Q): adding a 4-byte tag to carry multiple logical networks on a single physical link.
- **Switching:** The MAC address table (CAM table): learning source MACs, forwarding based on destination MACs. Unknown unicast flooding, broadcast flooding. Switch port modes: access, trunk. Spanning Tree Protocol (STP, RSTP, MSTP): preventing loops while allowing redundant paths. The 2040 shift from STP to link aggregation and spine-leaf architectures.
- **Network Interface Cards and Drivers:** The NIC as the boundary between the operating system and the physical network. Linux network interface naming (enp0s31f6, eno1, ens33). ethtool for link status, speed, duplex, and offload configuration. The role of hardware offloading (TSO, LRO, checksum offloading) in performance.

### Lecture Notes

Understanding Layer 1 and 2 is not glamorous, but it is indispensable. Some of the most pernicious network problems originate at these layers. A faulty fiber connector introduces bit errors that cause intermittent TCP retransmissions; a duplex mismatch between a switch port and a NIC causes crippling performance degradation that looks like "the server is slow" but is actually a Layer 2 negotiation failure; a Cat5 cable (100 MHz bandwidth) plugged into a switch port configured for 10Gbps causes autonegotiation to fall back to 100Mbps, a 100x performance reduction that is invisible to anyone who doesn't check link speed.

Ethernet has been the dominant LAN technology since the 1990s and remains so in 2040, though its form has changed. The original Ethernet (10BASE5, "thicknet") used a shared coaxial bus; all devices shared the wire and collisions were a normal part of operation (CSMA/CD). Modern Ethernet is full-duplex and switched: each device has a dedicated point-to-point link to a switch, collisions do not occur, and CSMA/CD is a historical footnote retained only in the standard for backward compatibility. The switch's CAM table is the heart of LAN operation: it learns which MAC addresses are reachable on which ports, and forwards frames directly to the destination port rather than flooding them to all ports. When a switch receives a frame with a destination MAC not in its CAM table, it floods the frame to all ports except the source — this is how broadcast and unknown unicast traffic propagates.

VLANs (Virtual LANs, IEEE 802.1Q) are a critical concept for the SA. A VLAN partitions a single physical switch into multiple logical switches, creating separate broadcast domains without requiring separate physical infrastructure. A frame tagged with VLAN 10 is only forwarded to ports in VLAN 10. Trunk ports carry frames for multiple VLANs, with each frame tagged with its VLAN ID. The SA configures VLANs on switches and on Linux servers (using the `vconfig` or `ip link` commands), assigns access ports to specific VLANs, and routes between VLANs using Layer 3 devices (routers or switch virtual interfaces). In the Yggdrasil campus network, VLANs separate student traffic, administrative traffic, research traffic, and IoT device traffic — each in its own broadcast domain, each with its own security policy.

The practical command for the SA: `ethtool`. This is the Swiss army knife of physical layer diagnostics. `ethtool -i eno1` shows the NIC driver. `ethtool eno1` shows link status, speed, and duplex. `ethtool -S eno1` shows per-queue statistics including drops, errors, and collisions. `ethtool -k eno1` shows hardware offload settings. When a server's network performance is degraded, the SA's first diagnostic step should be `ethtool eno1` to verify that the link is up at the expected speed and full duplex.

### Required Reading

- Spurgeon, C.E. & Zimmerman, J. (2034). *Ethernet: The Definitive Guide*, 3rd Edition. O'Reilly. Chapters 1-4.
- IEEE 802.3-2022. *IEEE Standard for Ethernet*. (Reference for frame format and physical specifications.)
- Yggdrasil Campus Network Specification (2040). UoY Network Engineering Technical Report #YF-2024-022. (Local standards for cabling, switch models, and VLAN architecture.)

### Discussion Questions

1. A server is experiencing 100x slower throughput than expected. All higher-layer diagnostics look normal. Describe the Layer 1/2 checks you would perform, in order.
2. Why does CSMA/CD still exist in the Ethernet standard if modern switched Ethernet is full-duplex? What would happen if a network device assumed CSMA/CD was unnecessary and disabled it?
3. A team proposes eliminating VLANs and using a flat Layer 2 network for simplicity. Argue both for and against this approach, citing specific technical and security considerations.

---

ᚨ **Lecture 4: IPv4 Addressing and Subnetting — Carving the Address Space**

**Course:** SA104 — Networking Fundamentals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

IP addressing is the addressing scheme that makes the Internet possible. Every packet carries a source and destination IP address; every routing decision is based on these addresses. This lecture covers IPv4 addressing in depth: binary notation, classful and classless addressing, subnet masks, CIDR notation, VLSM, and the calculation skills that every SA must perform fluently. IPv4 remains pervasive in 2040, despite IPv6 adoption exceeding 60% of global traffic. Internal networks, legacy systems, and embedded devices continue to use IPv4, and the SA must be equally comfortable with both. This lecture addresses IPv4; Lecture 5 covers IPv6.

### Key Topics

- **IPv4 Address Structure:** 32-bit address, dotted-decimal notation (e.g., 192.168.1.100). Network portion vs. host portion. The subnet mask defines the boundary: /24 means the first 24 bits are the network, the last 8 bits are the host. Binary-to-decimal conversion fluency: 128, 192, 224, 240, 248, 252, 254, 255 — these values must be remembered, not calculated.
- **Classful Addressing (Historical):** Class A (/8), Class B (/16), Class C (/24). Why classful addressing wasted address space and has been abandoned. The evolution to classless addressing (CIDR, RFC 4632).
- **Subnetting:** Borrowing host bits to create sub-networks. A /24 network subnetted into two /25s, four /26s, etc. Subnet calculations: network address, broadcast address, first usable, last usable, number of hosts. The rule: number of hosts = 2^(32-n) - 2 (subtracting network and broadcast addresses).
- **VLSM (Variable Length Subnet Masking):** Different subnets in the same network can have different masks. A /24 allocated to a department can be split into a /25 (126 hosts) for servers, a /26 (62 hosts) for workstations, and /30s (2 hosts each) for point-to-point links. VLSM minimizes address waste.
- **Private Addressing and NAT (RFC 1918):** 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16. These ranges are not routable on the Internet. Network Address Translation (NAT) maps private addresses to one or more public addresses, enabling Internet connectivity without assigning public IPs to every device. NAT is a hack that became essential; it broke the end-to-end principle of IP.

### Lecture Notes

Subnetting is the single most tested skill in network certification exams, and for good reason: it is the foundational calculation of IP networking. Every SA must be able to look at an IP address and subnet mask and instantly know: what network is this on? What is the broadcast address? How many hosts can this network accommodate? Is this address in the same subnet as that address? These questions arise daily in configuration, troubleshooting, and design.

Consider a concrete example. You are assigned 10.20.0.0/16 for a campus network. You need to allocate address space for 8 buildings, each with approximately 500 devices, plus a server farm with 200 devices, plus 30 point-to-point links for inter-building fiber. Using VLSM: allocate each building a /23 (510 usable addresses). Eight buildings = 10.20.0.0/23 through 10.20.14.0/23. Allocate the server farm a /24 (254 addresses): 10.20.16.0/24. Allocate each point-to-point link a /30 (2 addresses): 10.20.17.0/30 through 10.20.17.116/30. The entire campus fits within 10.20.0.0/16, with room to grow. This is efficient address planning.

The SA must also understand why NAT exists and what it costs. In the original Internet design, every device had a globally routable IP address, and any device could communicate directly with any other. NAT breaks this: devices behind a NAT cannot receive inbound connections unless explicitly configured (port forwarding). This is why peer-to-peer applications, VoIP, and some VPNs struggle behind NAT. The long-term solution is IPv6, which provides 340 undecillion addresses (2^128) — enough for every grain of sand on Earth to have its own /64 subnet. But IPv4 persists because of inertia, entrenched equipment, and the fact that NAT "works well enough" for most use cases.

In 2040, the SA manages both IPv4 and IPv6 on every network. Dual-stack is the standard deployment model: every interface has both an IPv4 and IPv6 address. The Yggdrasil campus runs IPv4 internally for legacy devices and management interfaces, and IPv6 natively for all production workloads. The SA must be able to read, write, and troubleshoot both.

### Required Reading

- Kurose, J.F. & Ross, K.W. (2038). *Computer Networking: A Top-Down Approach*, 9th Edition. Chapter 4 (Sections 4.1-4.3 on IPv4).
- Lammle, T. (2036). *CCNA Routing and Switching Complete Study Guide*, 4th Edition. Wiley. Chapters on IP addressing and subnetting.
- RFC 1918 (1996). *Address Allocation for Private Internets*. Y. Rekhter et al. Still the standard for private address space.

### Discussion Questions

1. You are given 172.16.0.0/12 for a corporate network with 6 offices. Office A has 4000 devices, Office B has 2000, Offices C-F have 500 each. Design a VLSM allocation plan. How much address space remains unused?
2. A colleague argues that NAT is a security feature because it hides internal addresses from the Internet. Is this correct? What are the actual security implications of NAT?
3. IPv4 addresses are functionally exhausted at the RIR level, yet organizations continue to operate large IPv4 networks. What technical and economic factors explain the persistence of IPv4? When, if ever, will IPv4 become truly obsolete?

---

ᚱ **Lecture 5: IPv6 — Addressing the Future**

**Course:** SA104 — Networking Fundamentals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

IPv6 is the successor to IPv4, designed to solve the address exhaustion problem that has plagued the Internet since the 1990s. With 128-bit addresses providing 2^128 possible addresses, IPv6 eliminates the need for NAT and restores the end-to-end principle of the original Internet. This lecture covers IPv6 addressing architecture, address types, the Neighbor Discovery Protocol that replaces ARP, autoconfiguration mechanisms, and the transition technologies that enable coexistence with IPv4. In 2040, IPv6 adoption has exceeded 60% globally, and the Yggdrasil campus network runs IPv6 natively for all production traffic. The SA must be fluent in IPv6.

### Key Topics

- **IPv6 Address Architecture:** 128-bit addresses written in hexadecimal colon notation (e.g., 2001:db8:abcd:1234::1). Address structure: global routing prefix (48 bits), subnet ID (16 bits), interface ID (64 bits). The /64 boundary is fixed: every subnet is /64. Abbreviation rules: leading zeros omitted, one instance of consecutive zero groups replaced with ::.
- **IPv6 Address Types:** Unicast (global, link-local fe80::/10, unique local fd00::/8), Multicast (ff00::/8 — replaces broadcast), Anycast (same address on multiple devices, routed to nearest). No more broadcast — IPv6 uses multicast for all one-to-many communication.
- **Neighbor Discovery Protocol (NDP, RFC 4861):** Replaces ARP. Uses ICMPv6 messages (Neighbor Solicitation, Neighbor Advertisement, Router Solicitation, Router Advertisement) to discover link-layer addresses, detect duplicate addresses, and find routers. NDP is more efficient and secure than ARP, though it requires proper configuration to prevent abuse.
- **Autoconfiguration:** Stateless Address Autoconfiguration (SLAAC): the device generates its own address from the prefix advertised by the router and its MAC address (or a random privacy address, RFC 7217). DHCPv6: stateful address assignment, similar to DHCPv4. The 2040 standard is SLAAC with privacy extensions (RFC 7217 stable privacy addresses, not EUI-64).
- **IPv4-to-IPv6 Transition Technologies:** Dual-stack (run both simultaneously), tunneling (6to4, 6in4, Teredo, DS-Lite), and translation (NAT64 with DNS64). The 2040 campus uses dual-stack natively, with NAT64/DNS64 for IPv4-only services.

### Lecture Notes

IPv6 addresses are dramatically larger than IPv4 addresses: 128 bits vs. 32 bits, written in hexadecimal rather than decimal, with colons rather than dots as separators. The address 2001:0db8:0000:0000:0000:0000:0000:0001 compresses to 2001:db8::1. This notation takes practice — the SA must become as fluent in reading and writing IPv6 addresses as IPv4 addresses.

The /64 subnet boundary is a critical difference from IPv4. In IPv4, subnets can be any size from /0 to /32. In IPv6, the recommendation (now effectively a requirement) is that every subnet is /64. This means every subnet has 2^64 possible addresses — 18.4 quintillion — which is more than enough for any conceivable number of devices. The SA should never need to subnet more finely than /64. If a network needs more subnets, it allocates a larger prefix (e.g., /48) and uses the 16-bit subnet ID to create 65,536 /64 subnets.

The elimination of broadcast is one of IPv6's most significant design improvements. In IPv4, broadcast packets are processed by every device on the LAN, consuming CPU on devices that don't need the packet. IPv6 replaces broadcast with scoped multicast: instead of "send to everyone," you send to "all devices that care about this specific function." Neighbor Discovery uses multicast groups (ff02::1 for all nodes, ff02::2 for all routers, ff02::1:ffxx:xxxx for specific neighbor solicitations). This dramatically reduces unnecessary packet processing.

SLAAC with privacy extensions is the 2040 standard for IPv6 address assignment. When a device joins a network, it receives a Router Advertisement containing the /64 prefix, and it generates its own interface identifier — not by embedding its MAC address (which would create a trackable, stable identifier), but by generating a stable but opaque identifier using a cryptographic hash (RFC 7217). This provides the best of both worlds: the address is stable across reconnections (important for server configurations and firewall rules) but not traceable to the device's hardware (important for privacy). The SA configures the router advertisements and ensures privacy extensions are enabled on all client devices.

### Required Reading

- Kurose, J.F. & Ross, K.W. (2038). *Computer Networking: A Top-Down Approach*, 9th Edition. Chapter 4 (IPv6 sections).
- Hagen, S. (2035). *IPv6 Essentials*, 4th Edition. O'Reilly. Chapters 1-5.
- RFC 4861 (2007). *Neighbor Discovery for IP version 6 (IPv6)*. T. Narten et al.
- RFC 7217 (2014). *A Method for Generating Semantically Opaque Interface Identifiers with IPv6 Stateless Address Autoconfiguration*. C. Gont.

### Discussion Questions

1. An IPv6 /48 allocation gives you 65,536 /64 subnets. For a university campus with 50 buildings, is this sufficient? How many /48s would a global enterprise need for 1,000 offices?
2. SLAAC generates addresses without a central server (DHCP). Discuss the advantages and disadvantages of decentralized address assignment. What problems does it solve, and what new problems does it create?
3. Some security practitioners argue that IPv6 makes networks *less* secure because IPv6's autoconfiguration and NDP create new attack surfaces (Rogue Router Advertisements, NDP spoofing). Evaluate this claim. What mitigations exist?

---

ᚲ **Lecture 6: IP Routing — Navigating the Paths Between Networks**

**Course:** SA104 — Networking Fundamentals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Routing is the process by which packets traverse multiple networks to reach their destination. If Layer 2 (switching) connects devices within a single network, Layer 3 (routing) connects networks to each other. This lecture covers the principles of IP routing: the routing table, longest prefix match, static routes, and the dynamic routing protocols that automate route discovery. For the SA, understanding routing is essential because virtually every network problem ultimately involves a routing decision — either correct or incorrect.

### Key Topics

- **The Routing Table:** Every IP device has a routing table that determines where to forward packets. The table consists of entries: destination network, subnet mask, next-hop gateway, and outgoing interface. The longest prefix match rule: when multiple routes match a destination, the most specific route (longest prefix) wins. The default route (0.0.0.0/0) matches everything not matched by a more specific route.
- **Static Routing:** Manually configured routes. Appropriate for small, simple, stable networks. `ip route add 10.0.0.0/8 via 192.168.1.1 dev eno1`. Disadvantages: no automatic failover, no scalability, manual maintenance. Use cases: stub networks, point-to-point links, default routes.
- **Dynamic Routing Protocols:** Interior Gateway Protocols (distance vector: RIP; link-state: OSPF, IS-IS) operate within an autonomous system. Exterior Gateway Protocol (BGP) operates between autonomous systems. The SA must understand OSPF for enterprise networks and BGP for Internet connectivity.
- **OSPF (Open Shortest Path First):** Link-state protocol. Each router has a complete map of the network (the link-state database). Dijkstra's algorithm computes shortest paths. Areas (Area 0 backbone, non-backbone areas) scale OSPF to large networks. OSPF converges quickly after topology changes. The Yggdrasil campus uses OSPF Area 0 for the backbone and distributes areas per building.
- **BGP (Border Gateway Protocol):** Path vector protocol. The protocol that runs the Internet. BGP advertises reachability information between autonomous systems. The SA encounters BGP when connecting to Internet Transit Providers. Key concepts: AS numbers, BGP attributes (AS-PATH, NEXT-HOP, LOCAL-PREF, MED), route filtering, and prefix lists.

### Lecture Notes

The routing table is the SA's compass. Every network-enabled device — from a laptop to a core router — has one. On Linux, `ip route show` displays it. A typical server routing table might contain only a few entries: a default route pointing at the upstream router, a connected route for each of its interfaces, and perhaps a few static routes for specific networks. A core router's routing table contains hundreds of thousands of entries, populated by dynamic protocols.

The longest prefix match rule is deceptively simple but critical. Suppose a routing table contains both 10.0.0.0/8 (via router A) and 10.20.0.0/16 (via router B). A packet destined for 10.20.1.5 matches *both* routes, but the /16 route is more specific, so the packet goes to router B. This is how routing scales: specific routes override general routes, and the default route (0.0.0.0/0, the least specific route possible) catches everything else.

OSPF is the routing protocol of choice for enterprise networks. It is link-state, meaning every router builds a complete picture of the network topology and independently computes the best path to every destination. This is more robust than distance-vector protocols like RIP, which merely share routing rumors without understanding the network's structure. OSPF areas allow the network to scale: routers within an area have detailed topology information; routers on area boundaries (Area Border Routers, ABRs) summarize and propagate routes between areas. The Sa must understand how to configure basic OSPF on Linux using FRRouting (FRR), the modern replacement for Quagga.

BGP is the protocol that stitches the Internet together. When the Yggdrasil campus connects to its Internet Service Providers, BGP advertises the campus's IP prefixes (e.g., 2001:db8:abcd::/48) to the upstream providers, and receives a default route or the full Internet routing table (780,000+ IPv4 prefixes and 200,000+ IPv6 prefixes in 2040) in return. The SA who manages BGP peering must understand route filtering (never advertise routes you shouldn't), prefix lists, and the directional nature of BGP policy (import filters vs. export filters).

For the SA, the practical take-away is this: when a server can't reach a remote host, the troubleshooting path starts with the routing table. `ip route get <destination>` on Linux shows exactly which route the kernel would use. If the route goes to the wrong next hop, the problem is routing. If there's no matching route at all, the problem is a missing route. If `ping` works but applications fail, the problem may be firewall or application-level, not routing.

### Required Reading

- Kurose, J.F. & Ross, K.W. (2038). *Computer Networking: A Top-Down Approach*, 9th Edition. Chapter 5 (Routing sections).
- Donahue, G.A. (2035). *Network Warrior*, 3rd Edition. O'Reilly. Chapters on OSPF and BGP.
- FRRouting Documentation (2040). https://frrouting.org/. (Practical configuration guide for Linux routing.)

### Discussion Questions

1. A network has two paths to a destination: a 10Gbps link with 2 extra hops and a 1Gbps direct link. OSPF would choose the direct link because it has fewer hops, but the 10Gbps path has more capacity. How would you configure OSPF (or what alternative protocol) to prefer the higher-bandwidth path?
2. BGP is often called "the protocol that runs the Internet." If BGP were to fail globally (all BGP sessions dropped simultaneously), what would happen to Internet connectivity? How long would recovery take?
3. A junior SA adds a static default route pointing to the wrong gateway. Describe all the consequences: local, downstream, and upstream.

---

ᚷ **Lecture 7: The Transport Layer — TCP, UDP, and the End-to-End Principle**

**Course:** SA104 — Networking Fundamentals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

The transport layer is where the network meets the application. IP delivers packets between hosts, but applications need more: reliable, ordered delivery (TCP) or fast, best-effort delivery (UDP). This lecture covers the two dominant transport protocols, their mechanisms, and their implications for systems administration. TCP's reliability comes at a cost — congestion control, connection management, and head-of-line blocking — while UDP's simplicity offers flexibility but requires the application to handle reliability. Understanding these protocols is essential for diagnosing performance problems, configuring firewalls, and designing network services.

### Key Topics

- **TCP (Transmission Control Protocol):** Connection-oriented, reliable, ordered delivery. The three-way handshake (SYN, SYN-ACK, ACK) establishes a connection before data transfer. Flow control via the sliding window mechanism. Congestion control algorithms: slow start, congestion avoidance, fast retransmit, fast recovery. CUBIC (the default congestion algorithm in Linux since kernel 2.6.19) and BBR (developed by Google, now a common alternative). TCP state machine: ESTABLISHED, FIN_WAIT, TIME_WAIT, CLOSE_WAIT, and the dreaded "connections stuck in TIME_WAIT."
- **UDP (User Datagram Protocol):** Connectionless, unreliable, unordered. No handshake, no retransmission, no congestion control. UDP sends datagrams as-is. Use cases: DNS, DHCP, NTP, streaming media, real-time gaming, QUIC (the transport protocol underlying HTTP/3). The resurgence of UDP in modern protocols (QUIC, QUIC-TLS, WebRTC) because it allows applications to implement custom congestion control that outperforms TCP's generic algorithms.
- **Port Numbers:** Well-known ports (0-1023), registered ports (1024-49151), and dynamic/private ports (49152-65535). The socket: (source IP, source port, destination IP, destination port, protocol) — the five-tuple that uniquely identifies a connection. The SA's daily interaction with ports: checking which process is listening on which port (`ss -tlnp`), configuring firewall rules to allow specific ports, diagnosing port conflicts.
- **TCP Performance for the SA:** Nagle's algorithm, delayed ACK, TCP window scaling, selective acknowledgments (SACK), path MTU discovery. How to diagnose TCP performance issues: `ss -i` shows per-connection TCP internals, `tcpdump` captures packets for analysis, `iperf3` measures throughput and latency.

### Lecture Notes

TCP is the workhorse of the Internet. Every web request, every SSH session, every database connection uses TCP. TCP provides three guarantees: (1) reliability — every byte sent will be received or the sender will be notified of failure; (2) ordering — bytes arrive in the order they were sent; (3) flow/congestion control — the sender adjusts its rate to avoid overwhelming the receiver or the network. These guarantees make application programming easier (no need to handle lost or reordered packets) but introduce latency and complexity.

The TCP three-way handshake is one of the most fundamental sequences in networking. The client sends a SYN (synchronize) packet with an initial sequence number. The server responds with a SYN-ACK, acknowledging the client's SYN and including its own initial sequence number. The client responds with an ACK, acknowledging the server's SYN. At this point, both sides have confirmed the other's ability to send and receive, and data transfer can begin. The total cost: one round-trip time (RTT) before any application data is sent. For the SA, this means that every TCP connection to a distant server pays a latency cost proportional to the RTT.

TCP congestion control is the mechanism that prevents the Internet from collapsing under load. The dominant algorithm in 2040 is CUBIC (the Linux default) and BBR (increasingly common for high-latency, high-bandwidth connections). CUBIC uses a cubic function to determine the congestion window size, allowing faster recovery after packet loss. BBR (Bottleneck Bandwidth and Round-trip propagation time) takes a fundamentally different approach: instead of detecting loss, it models the network's capacity and RTT, and sends at the optimal rate. BBR can achieve significantly higher throughput on long-fat networks (high bandwidth, high latency) and is now the default for Google's internal traffic and many large-scale deployments. The SA can set the congestion algorithm per-socket or system-wide: `sysctl net.ipv4.tcp_congestion_control=bbr`.

UDP is experiencing a renaissance because of QUIC. QUIC (Quick UDP Internet Connections) is a transport protocol built on UDP that provides TLS-encrypted connections with zero-RTT handshake, independent stream multiplexing (no head-of-line blocking), and connection migration (a connection can survive IP address changes). HTTP/3 runs over QUIC. The SA must understand that UDP is no longer "the simple protocol for DNS and NTP" — it is now the foundation for the next generation of transport protocols. Firewalls must allow QUIC (UDP port 443), and load balancers must support it.

The practical SA skill is `ss -tna`, which displays all TCP connections with their states. A server with thousands of connections in TIME_WAIT is experiencing high connection turnover (common for short-lived HTTP requests). A server with many CLOSE_WAIT connections has a bug: the remote side closed the connection, but the local application hasn't called close(). A server with zero ESTABLISHED connections on a service port means the service isn't receiving traffic — check routing, firewall, and DNS.

### Required Reading

- Kurose, J.F. & Ross, K.W. (2038). *Computer Networking: A Top-Down Approach*, 9th Edition. Chapter 3 (Transport Layer).
- Stewart, R.R. & Xie, Q. (2034). *Stream Control Transmission Protocol (SCTP): A Reference Guide*. Addison-Wesley. (For comparison with TCP/UDP.)
- RFC 9000 (2021). *QUIC: A UDP-Based Multiplexed and Secure Transport*. IETF. (Essential reading for understanding modern transport.)

### Discussion Questions

1. A web server handles 10,000 short-lived HTTP connections per second. Each connection uses a random ephemeral port and remains in TIME_WAIT for 60 seconds. Calculate the port exhaustion risk. How can the SA mitigate this?
2. Compare TCP CUBIC and BBR on a network path with 100ms RTT, 1% packet loss, and 10Gbps bandwidth. Which algorithm would achieve higher throughput, and why?
3. A firewall administrator blocks all UDP traffic except DNS (port 53). What modern applications and protocols will break? How should the policy be updated?

---

ᚻ **Lecture 8: DNS and DHCP — The Naming and Addressing Services**

**Course:** SA104 — Networking Fundamentals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

DNS (Domain Name System) and DHCP (Dynamic Host Configuration Protocol) are the two most essential network services for any organization. DNS translates human-readable names (server.yggdrasil.edu) into IP addresses; DHCP assigns IP addresses and configuration to devices automatically. This lecture covers both protocols in depth: DNS architecture, record types, zone management, and security (DNSSEC, DoH, DoT); and DHCP lease management, options, relay agents, and the interaction between DHCP and DNS in dynamic environments. The SA who cannot configure, troubleshoot, and secure DNS and DHCP is not a complete SA — these services are the backbone of every network.

### Key Topics

- **DNS Architecture:** The hierarchical namespace: root servers, TLD servers, authoritative servers, recursive resolvers. The resolution process: recursive resolver → root server → TLD server → authoritative server. Caching: the recursive resolver caches responses for the TTL duration. The distinction between authoritative DNS (serving zone data) and recursive DNS (resolving queries on behalf of clients).
- **DNS Record Types:** A (IPv4 address), AAAA (IPv6 address), CNAME (canonical name / alias), MX (mail exchange), NS (name server), TXT (arbitrary text, used for SPF, DKIM, verification), SRV (service location), PTR (reverse DNS). Zone file syntax. TTL (Time to Live): the cache duration. Short TTL for rapid changes, long TTL for stability.
- **DNSSEC:** Signing zone data with cryptographic keys to provide authentication and integrity. DS records in the parent zone establish a chain of trust from the root. DNSSEC validation prevents cache poisoning attacks (Kaminsky attack). The SA must understand key rollovers and the importance of keeping signing keys offline.
- **DHCP (RFC 2131):** The four-packet exchange: DISCOVER (client broadcast), OFFER (server response), REQUEST (client accepts), ACK (server confirms). Lease duration and renewal logic: T1 (50% lease time, attempt renewal from original server), T2 (87.5% lease time, attempt renewal from any server). DHCP options: subnet mask, default gateway, DNS servers, domain name, NTP servers, MTU, and many more.
- **Dynamic DNS (DDNS):** The integration of DHCP and DNS: when a DHCP server assigns an address, it also updates the DNS zone to map the device's hostname to its new address. In the Yggdrasil campus, DDNS ensures that every device can be reached by hostname regardless of its DHCP-assigned address.

### Lecture Notes

DNS is the most critical Internet service that most people never think about. When DNS fails, everything fails: web browsing, email, SSH connections (which often use hostnames in configuration), certificate validation (which checks CRLs and OCSP via HTTP, which requires DNS). The 2023 Google Cloud outage that took down major services for hours was caused by a DNS configuration error. The SA must treat DNS as Tier 0 infrastructure: more critical than any application, more critical than authentication, because without DNS, nothing else works.

The BIND9 DNS server is the standard for authoritative and recursive DNS on Linux. For the Yggdrasil campus, the SA configures BIND9 as an authoritative server for the yggdrasil.edu zone and as a recursive resolver for campus clients. Zone files define the mapping: `server1 IN A 10.20.1.10` creates an A record, `www IN CNAME server1` creates an alias, `yggdrasil.edu. IN MX 10 mail.yggdrasil.edu.` defines the mail server. The SA must master zone file syntax, understand serial numbers (the SOA serial number must be incremented on every change for secondary servers to pick up updates), and implement DNSSEC signing.

DHCP is the protocol that makes networks usable. Without DHCP, every device would need a manually configured IP address, subnet mask, default gateway, and DNS server — which is impractical beyond a few dozen devices. DHCP automates this: when a device joins the network, it broadcasts a DISCOVER message; a DHCP server responds with an OFFER containing an IP address and configuration parameters; the client accepts with a REQUEST; and the server confirms with an ACK. The entire process takes milliseconds.

The SA must understand lease management. A DHCP scope defines a range of addresses (e.g., 10.20.10.100 to 10.20.10.250) with a lease duration (e.g., 8 hours). Reservations bind a specific address to a specific MAC address, ensuring that servers and printers always get the same IP. The `dhcp-lease-list` command shows active leases; `dhcp-lease-list --expiry` shows when leases expire. When address pools run low, the SA must either expand the scope, reduce lease times, or investigate devices that are consuming addresses without using them.

DNS and DHCP together enable a critical feature: reachability by hostname. Without DDNS, a DHCP-assigned device can only be reached by IP address (which changes) or by manually updating DNS (which is impractical). With DDNS, when the DHCP server assigns address 10.20.10.105 to device laptop-42.yggdrasil.edu, it immediately updates the DNS zone: laptop-42.yggdrasil.edu → 10.20.10.105. Other devices can then reach laptop-42 by name, regardless of its current address.

### Required Reading

- Liu, C. & Albitz, P. (2036). *DNS and BIND*, 7th Edition. O'Reilly. Chapters 1-4, 7.
- Kurose, J.F. & Ross, K.W. (2038). *Computer Networking: A Top-Down Approach*, 9th Edition. Chapter 2 (DNS sections).
- RFC 2131 (1997). *Dynamic Host Configuration Protocol*. R. Droms. (Still the core DHCP standard.)
- Yggdrasil DNS Architecture Guide (2040). UoY Network Engineering Report #YF-2024-031.

### Discussion Questions

1. A DNS outage takes down all services. Describe the blast radius: what breaks, what still works, and how long does recovery take? How does DNSSEC complicate recovery?
2. A campus network has 5,000 devices and a /22 DHCP scope (1,022 usable addresses). Lease time is 8 hours. Calculate the maximum sustainable device turnover rate. What happens when enrollment doubles?
3. DDNS allows dynamic hostname-to-address mapping. What are the security implications? How can you prevent unauthorized devices from registering hostile DNS records?

---

ᚹ **Lecture 9: Network Services for SysAdmins — LDAP, RADIUS, SNMP, Syslog, SSH, NTP**

**Course:** SA104 — Networking Fundamentals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Beyond DNS and DHCP, the SA relies on a constellation of network services that provide authentication, monitoring, logging, remote access, and time synchronization. This lecture covers each service: its purpose, its protocol, its configuration on Linux, and the operational considerations that make it production-ready. These services are the connective tissue of infrastructure — they make individual servers into a manageable fleet.

### Key Topics

- **LDAP (Lightweight Directory Access Protocol):** A hierarchical directory service for storing and querying identity information: users, groups, permissions. The Yggdrasil Heimdallr ID system uses LDAP as its backend. The SA configures LDAP clients (`sssd`, `nslcd`) to authenticate users against the central directory. Key concepts: Distinguished Names (DN), organizational units (OU), attributes, objectClasses, LDIF format. The difference between LDAP (the protocol) and Active Directory (Microsoft's LDAP implementation with proprietary extensions).
- **RADIUS (Remote Authentication Dial-In User Service):** AAA protocol: Authentication, Authorization, Accounting. Used for network access control (Wi-Fi authentication, VPN authentication, switch management access). The Yggdrasil network uses FreeRADIUS for 802.1X port authentication and eduroam Wi-Fi. The three messages: Access-Request, Access-Accept/Access-Reject, Accounting-Request.
- **SNMP (Simple Network Management Protocol):** Monitoring protocol for network devices. SNMPv3 (the current standard, with authentication and encryption). MIBs (Management Information Bases) define the data schema. OID (Object Identifiers) are dotted-numeric identifiers for specific metrics. The SA uses SNMP to monitor switch port utilization, router CPU load, and device reachability. Integration with Prometheus/Telegraf for metric collection.
- **Syslog:** The standard for centralized log collection. RFC 5424 defines the syslog protocol: facility, severity, timestamp, hostname, message. The SA configures rsyslog on every server to forward logs to a central aggregator (the Yggdrasil Loki stack). Log severity levels: DEBUG, INFO, NOTICE, WARNING, ERR, CRIT, ALERT, EMERG. The pattern: centralize everything, filter at the display layer, alert on CRIT and above.
- **SSH (Secure Shell):** The SA's primary remote access tool. Key-based authentication (never passwords!). SSH key types: RSA (2048+ bits), Ed25519 (preferred). `sshd_config` hardening: `PermitRootLogin no`, `PasswordAuthentication no`, `MaxAuthTries 3`. SSH tunneling: local port forwarding, remote port forwarding, dynamic forwarding (SOCKS proxy). The SSH agent and key management. The 2040 standard: YubiKey-based SSH keys (hardware-backed, non-exportable).
- **NTP (Network Time Protocol):** Time synchronization is critical for log correlation, certificate validation, Kerberos authentication, and database replication. NTP synchronizes clocks to within milliseconds. The stratum hierarchy: stratum 0 (atomic clock, GPS), stratum 1 (directly connected to stratum 0), stratum 2 (synced to stratum 1), etc. The SA configures chrony (the modern NTP implementation) to sync against multiple upstream servers and serve time to local clients.

### Lecture Notes

LDAP is the foundation of centralized identity management. Without it, every server would have its own `/etc/passwd` file, and adding a user would require logging into every server individually. With LDAP, user accounts live in the directory, and all servers authenticate against it. When a user changes their password, it takes effect immediately across all systems. When a user leaves the organization, disabling their LDAP account removes access everywhere. The SA configures each Linux server to use SSSD (System Security Services Daemon) as the LDAP client: `sssd.conf` specifies the LDAP server URL, the search base (e.g., `dc=yggdrasil,dc=edu`), and the authentication method (LDAP simple bind with TLS). The `id` and `getent passwd` commands verify that LDAP users are visible on the local system.

RADIUS may seem like a legacy protocol (it was designed for dial-up authentication), but it remains the standard for 802.1X network access control. In the Yggdrasil campus, when a device connects to the eduroam Wi-Fi network, the access point sends a RADIUS Access-Request to FreeRADIUS, which authenticates the user against LDAP and returns either Access-Accept (with the appropriate VLAN assignment) or Access-Reject. This is network access control: the switches and access points don't decide who gets on the network — the RADIUS server does, based on identity and policy.

SNMP is the SA's window into network infrastructure. Switches, routers, firewalls, and wireless access points expose hundreds of metrics via SNMP: interface traffic counts, error rates, CPU utilization, memory usage, temperature. The SA configures Telegraf SNMP input plugins to collect specific OIDs on a polling interval (typically 60 seconds) and sends them to Prometheus for storage and alerting. SNMP v3 is mandatory in 2040 — the community string ("public") authentication of SNMP v1 and v2c is a security vulnerability that must not exist on any network.

SSH is arguably the most important tool in the SA's toolbox. Every remote administration session uses SSH. The SA must configure SSH for maximum security: Ed25519 keys (not RSA 2048, which is considered weak), hardware-backed keys (YubiKey or similar), disabled password authentication, disabled root login, and session logging via `auditd`. SSH tunneling is a powerful technique: `ssh -L 8080:internal-server:80 bastion-host` creates a local port forward that allows access to an internal web server through a bastion host. This is the pattern for accessing internal services without exposing them to the Internet.

### Required Reading

- Limoncelli, T.A., Hogan, C.J., & Chalup, S.R. (2035). *The Practice of System and Network Administration*, 4th Edition. Addison-Wesley. Chapters on LDAP, SNMP, and Syslog.
- Barrett, D.J. (2037). *SSH, The Secure Shell: The Definitive Guide*, 3rd Edition. O'Reilly. Chapters 1-3, 7.
- RFC 5424 (2009). *The Syslog Protocol*. R. Gerhards. (Modern syslog standard.)

### Discussion Questions

1. LDAP centralizes identity, but it's also a single point of failure. Describe the outage scenario when the LDAP server becomes unreachable. What are the design patterns for resilient LDAP?
2. SNMP v2c uses community strings for authentication. A community string of "public" allows read access to all OIDs. Why is this a security risk even if you only expose "read-only" data? What specific information could an attacker extract?
3. An SA discovers that their organization's SSH keys are stored on developers' laptops without passphrases. What is the risk, and what is the remediation plan? Consider key rotation, revocation, and hardware tokens.

---

ᚬ **Lecture 10: Linux Networking — Configuring the Interface**

**Course:** SA104 — Networking Fundamentals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Everything discussed in previous lectures — IP addressing, routing, DNS, protocols — must be configured on actual systems. This lecture covers the Linux networking stack from the SA's perspective: interface configuration, routing tables, network namespaces, bridging, bonding, tunneling, and the iproute2 tool suite that replaces the legacy net-tools. The SA must be able to configure, diagnose, and automate network settings on Linux servers — because in 2040, every server is a Linux server, and every network configuration is defined in code.

### Key Topics

- **The iproute2 Suite:** The modern Linux networking toolkit. `ip addr` (interface addresses), `ip link` (interface configuration), `ip route` (routing table), `ip neigh` (ARP/NDP table), `ip rule` (routing policy), `ip netns` (network namespaces). The legacy tools (`ifconfig`, `route`, `netstat`, `arp`) should be known for historical context but not used in 2040. The `ss` command replaces `netstat`: `ss -tlnp` shows all listening TCP ports with process information.
- **Network Interface Configuration:** Persistent configuration via systemd-networkd or NetworkManager. The `/etc/systemd/network/` directory contains `.netdev` and `.network` files that define interfaces, addresses, and routes. NetworkManager for laptops and workstations (supports dynamic Wi-Fi, VPN, etc.); systemd-networkd for servers (deterministic, declarative, fast).
- **Network Namespaces:** Linux network namespaces isolate the network stack. Each namespace has its own interfaces, routing table, firewall rules, and `/proc/net` view. Containers use namespaces to provide network isolation. `ip netns add ns1`, `ip netns exec ns1 ip addr`, `ip link set veth1 netns ns1`. The SA uses namespaces to create isolated network environments for testing, security, and multi-tenant infrastructure.
- **Bridge Interfaces:** A Linux bridge connects multiple interfaces at Layer 2, functioning like a virtual switch. Used for virtualization (connecting VMs to the physical network) and container networking. `ip link add name br0 type bridge`, `ip link set eno1 master br0`. The bridge learns MAC addresses and forwards frames between connected interfaces.
- **Bonding and Link Aggregation:** Combining multiple physical interfaces into a single logical interface for redundancy and/or increased bandwidth. Mode 1 (active-backup): one interface active, others standby. Mode 4 (802.3ad LACP): all interfaces active, traffic distributed by hash. The Yggdrasil standard: LACP bonding on all server NICs.
- **Tunneling:** GRE tunnels, VXLAN, IP-in-IP, WireGuard VPNs. Creating virtual point-to-point links across intermediate networks. The SA uses tunnels to connect remote sites, create overlay networks for containers, and establish secure VPN connections.

### Lecture Notes

The `ip` command is the SA's Swiss army knife for network configuration. It replaces the entire legacy net-tools suite: `ifconfig` → `ip addr`, `route` → `ip route`, `arp` → `ip neigh`, `iptunnel` → `ip tunnel`, `brctl` → `ip link` (bridge type). The SA should immediately stop using the legacy commands and learn iproute2, because the legacy tools are unmaintained, have fewer features, and produce output that doesn't match the kernel's actual state. The command `ip -br addr` shows all interfaces with their addresses in a concise format — this is often the first diagnostic command the SA runs on a new server.

Network namespaces are one of the most powerful features of the Linux networking stack. A namespace creates a complete copy of the network stack: separate interfaces, routing tables, iptables/nftables rules, and /proc/net statistics. This is how containers achieve network isolation: each container gets its own namespace, with its own IP address, routing, and firewall. The SA can use namespaces for testing: create a namespace, assign it a veth (virtual ethernet) pair, and test routing, firewall rules, or VPN configurations without affecting the host's network. `ip netns add testns && ip netns exec testns bash` gives you a shell inside an isolated network — invaluable for debugging.

Bridging is fundamental to virtualization and container networking. When you run a VM or a container, it needs a virtual interface connected to the physical network. The bridge provides this: the VM's virtual interface (vnet0 on the host side) is attached to the bridge, and the bridge is also attached to the physical NIC (eno1). Traffic from the VM enters the bridge, is forwarded to the physical NIC, and vice versa. The bridge operates at Layer 2 — it has no knowledge of IP addresses, only MAC addresses. This is precisely how a physical switch works, and the Linux bridge is effectively a virtual switch implemented in software.

Bonding (link aggregation) is essential for server reliability. A server with a single NIC is one cable failure away from total network disconnection. LACP bonding (802.3ad) combines two or more physical NICs into a single logical interface: traffic is distributed across the physical links using a hash of source and destination addresses, and if one link fails, traffic automatically shifts to the remaining links. The Yggdrasil standard is dual-NIC LACP bonding on every production server, connected to two different switches (one NIC to switch A, one NIC to switch B) for full switch-level redundancy. The configuration is straightforward: `nmcli connection add type bond iface-name bond0 mode 802.3ad ipv4.method auto`, then add the physical NICs as bond slaves.

Tunneling creates virtual network connections across physical networks. A GRE tunnel encapsulates IP packets inside other IP packets, creating a point-to-point virtual link. VXLAN encapsulates Layer 2 frames inside UDP packets, enabling Layer 2 connectivity across Layer 3 networks (essential for Kubernetes overlay networks). WireGuard provides encrypted tunnels with minimal overhead — a modern replacement for IPSec and OpenVPN. The SA configures tunnels to connect remote sites (GRE or WireGuard), create overlay networks for containers (VXLAN), and establish secure VPN connections (WireGuard). In the Yggdrasil campus, WireGuard tunnels connect the main data center to the edge compute nodes, providing encrypted connectivity over the public Internet.

The critical insight for the SA is that all network configuration in 2040 must be automated and version-controlled. NetworkManager and systemd-networkd configurations are files that can be managed with Git, deployed with Ansible, and validated with automated testing. The SA's workflow is: edit the configuration file, commit to Git, push to the configuration repository, and the Ansible playbook applies the change to all relevant servers. This is Infrastructure as Code applied to networking — the Bifrǫst Mesh defines network state in code, and automated systems ensure that reality matches the desired state.

### Required Reading

- Schroder, C. (2037). *The Book of Linux Networking*, 5th Edition. No Starch Press. Chapters on iproute2, bridging, and bonding.
- Linux Manual Pages: `ip(8)`, `ip-address(8)`, `ip-route(8)`, `ip-netns(8)`, `nmcli(1)`.
- Yggdrasil Server Network Configuration Guide (2040). UoY Infrastructure Documentation. (Campus standards for bonding, bridging, and naming.)

### Discussion Questions

1. A container needs network isolation but also needs to reach the Internet. Describe how you would use a network namespace, a veth pair, and a bridge to achieve this. Draw the network topology.
2. LACP bonding combines two 10Gbps NICs. What is the maximum throughput of a single TCP connection? (Hint: it depends on the hash algorithm.) How can this be optimized?
3. A GRE tunnel between two sites is experiencing MTU problems — large packets are being dropped. Explain the cause (encapsulation overhead) and the solution (adjusting MTU and enabling PMTU discovery).

---

ᛁ **Lecture 11: Network Security Fundamentals — Fortifying the Bridge**

**Course:** SA104 — Networking Fundamentals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Network security is not a separate discipline — it is an integral dimension of every network design decision. This lecture covers the fundamental security concepts and practices that every SA must internalize: defense in depth, firewall architecture, access control, VPN design, and wireless security. In Norse mythology, Heimdallr guards the Bifrǫst bridge, allowing only the worthy to cross. The SA does the same for the network: defining who may enter, what they may carry, and how the defenses respond to attack.

### Key Topics

- **Defense in Depth:** No single security measure is sufficient. Layer defenses: physical security (locked server rooms), network security (firewalls, segmention), host security (OS hardening, patching), application security (input validation, TLS), and data security (encryption at rest, access control). The principle: if one layer fails, the next layer still protects the asset.
- **Firewall Architecture:** Packet filtering (stateless: accept/reject based on 5-tuple), stateful inspection (track connection state, allow return traffic), and next-generation firewalls (deep packet inspection, application awareness). Linux firewall evolution: iptables → nftables. The nftables framework: tables, chains, rules, and sets. Common rulesets: default deny, allow SSH from management subnet, allow HTTP/HTTPS from anywhere, allow established connections.
- **Network Segmentation:** Dividing the network into zones with different security levels: DMZ (public-facing servers), trusted zone (internal servers), management zone (infrastructure management), restricted zone (sensitive data). Access control lists (ACLs) between zones: only specific traffic flows are permitted. The Yggdrasil campus VLAN architecture: VLAN 10 (management), VLAN 20 (faculty), VLAN 30 (students), VLAN 40 (IoT), VLAN 50 (guest).
- **VPN (Virtual Private Network):** Creating encrypted tunnels over untrusted networks. IPsec VPN for site-to-site connections (encrypts all traffic between two networks). WireGuard for point-to-point and remote access VPNs (simpler, faster, modern). SSL/TLS VPN for client-to-site (OpenVPN, now largely superseded by WireGuard). The 2040 campus standard: WireGuard for all VPN connections.
- **Wireless Security:** WEP (broken, do not use), WPA/WPA2-PSK (pre-shared key, acceptable for small networks), WPA3 (the 2040 standard, with SAE — Simultaneous Authentication of Equals). 802.1X with RADIUS for enterprise wireless: every user authenticates individually, keyed sessions prevent eavesdropping. The eduroam federation: authenticate at Yggdrasil, use Wi-Fi at any participating institution worldwide.

### Lecture Notes

The default-deny firewall policy is the foundation of network security. Every firewall rule should start from the principle: everything is blocked unless explicitly allowed. The ruleset then contains only the permitted flows: SSH from management IPs, HTTP/HTTPS from anywhere, DNS from internal resolvers, SNMP from monitoring servers. This approach is the opposite of "allow everything and block the bad stuff" — which requires knowing all the bad stuff, an impossible task. Default deny is the only sane starting point.

nftables is the modern Linux firewall, replacing iptables (which replaced ipchains, which replaced ipfwadm). nftables improves on iptables in several ways: a unified syntax for IPv4, IPv6, ARP, and bridge; native sets and maps for efficient rule matching; atomic rule replacement (no window where no rules are in effect); and better performance through optimized bytecode. A basic nftables ruleset for a web server:

```
table inet filter {
    chain input {
        type filter hook input priority 0; policy drop;
        ct state established,related accept
        iif lo accept
        tcp dport { 22, 80, 443 } accept
        icmp type echo-request limit rate 5/second accept
    }
    chain forward {
        type filter hook forward priority 0; policy drop;
    }
    chain output {
        type filter hook output priority 0; policy accept;
    }
}
```

This ruleset drops all incoming traffic except: established connections, loopback, SSH/HTTP/HTTPS, and rate-limited ping. All forwarding is dropped (this server is not a router). All outgoing traffic is allowed. This is a minimal, secure starting point.

Network segmentation is the practice of dividing a flat network into zones separated by firewalls or ACLs. The campus network should not be a single broadcast domain where every device can reach every other device. Security zones enforce the principle of least privilege at the network level: a student workstation should not be able to reach the database server; an IoT sensor should not be able to reach the LDAP server; a guest device should only be able to reach the Internet. VLANs implement segmentation at Layer 2; ACLs implement it at Layer 3. Together, they create a network where compromise of one zone does not automatically grant access to another.

Wireless security deserves special attention because Wi-Fi is a broadcast medium — anyone with a radio can receive the signals. This makes authentication and encryption critical. WPA3 with SAE (Simultaneous Authentication of Equals) is the 2040 standard. SAE is a dragonfly key exchange that provides forward secrecy: even if the password is compromised, past sessions cannot be decrypted. For enterprise environments, 802.1X with RADIUS provides per-user authentication: each user has their own encryption key, and compromised credentials affect only that user's sessions, not all users on the network. The Yggdrasil campus requires 802.1X for all internal Wi-Fi and runs a captive portal for guest access on a separate, firewalled VLAN.

### Required Reading

- Kerr, R. & Van Duser, M. (2035). *Linux Firewalls: Enhancing Security with nftables and Beyond*, 5th Edition. Pearson. Chapters 1-6.
- Donahue, G.A. (2035). *Network Warrior*, 3rd Edition. O'Reilly. Chapters on firewalls and VPNs.
- WireGuard Documentation (2040). https://www.wireguard.com/. (The modern VPN standard.)

### Discussion Questions

1. Design a firewall ruleset for a web server that must allow SSH, HTTP, and HTTPS, but block all other inbound traffic. How would you handle DNS responses? How would you handle ICMP? What is the minimum number of rules?
2. An organization has a flat /16 network where all 65,000 devices can reach each other. Describe the security risks and propose a segmentation strategy. How would you implement it without breaking existing applications?
3. WPA3-PSK is considered secure for home networks. What specific attacks does it prevent that WPA2-PSK was vulnerable to? (Consider KRACK, offline dictionary attacks, and key reinstallation.)

---

ᛃ **Lecture 12: Network Troubleshooting and Modern Trends — The Heimdallr's Watch**

**Course:** SA104 — Networking Fundamentals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

This final lecture synthesizes the course's knowledge into a systematic troubleshooting methodology and surveys the modern networking trends that are reshaping infrastructure. Troubleshooting is not an art — it is a discipline based on the OSI model, binary search, and hypothesis testing. The trends (SDN, NFV, network automation, and the AI-orchestrated fabric) are transforming the SA's role from "configure the switch" to "design the policy that the network enforces." Heimdallr watched the Bifrǫst with supernatural clarity; the SA must achieve comparable awareness through observability. ᛟ

### Key Topics

- **Systematic Troubleshooting:** The bottom-up approach (Layer 1 → Layer 7): check physical connectivity first, then data link, then network, and so on. The top-down approach (Layer 7 → Layer 1): start from the application error and work down. The divide-and-conquer approach: start at Layer 3 (ping) — if ping works, the problem is above Layer 3; if ping fails, the problem is at or below Layer 3. The scientific method: observe ⟶ hypothesize ⟶ test ⟶ analyze ⟶ repeat.
- **Diagnostic Tools — The SA's Toolkit:** `ping` (ICMP echo — tests Layer 3 reachability), `traceroute` / `mtr` (maps the path and identifies where it breaks), `ss -tna` (TCP connection states), `ip addr` / `ip route` / `ip neigh` (interface, routing, and ARP state), `ethtool` (physical layer diagnostics), `tcpdump` (packet capture), `nmap` (port scanning and service enumeration), `dig` / `nslookup` (DNS queries), `curl` / `wget` (application-level testing). The mastery pattern: know which tool to use for which layer.
- **Software-Defined Networking (SDN):** Separating the control plane (the software that decides where traffic goes) from the data plane (the hardware that forwards traffic). OpenFlow initiated the SDN movement; in 2040, SDN is implemented through controllers like OpenDaylight, ONOS, and proprietary solutions from cloud providers. The Bifrǫst Mesh uses an SDN controller to manage campus network policy centrally, pushing forwarding rules to switches via programmatic APIs.
- **Network Functions Virtualization (NFV):** Replacing dedicated hardware (firewalls, load balancers, WAN optimizers) with virtual machines or containers running the same software. NFV reduces capital expenditure, increases flexibility, and enables rapid provisioning. The SA manages these virtual network functions (VNFs) using the same orchestration tools as application workloads (Kubernetes, Helm, ArgoCD).
- **Network Automation:** Managing network configuration through code, not manual CLI commands. Ansible for configuration management, Python with Netmiko/NAPALM for programmatic access, Git for version control. Intent-based networking: the SA declares the desired state ("VLAN 10 should have ports 1-24 on switch-A"), and the automation system ensures reality matches the declaration. The Bifrǫst Mesh's self-healing fabric continuously compares desired state to actual state and reconciles differences.
- **The AI-Orchestrated Fabric:** The 2040 frontier. Machine learning models trained on network telemetry detect anomalies before they become outages. Predictive maintenance models analyze disk SMART data, NIC error counters, and switch temperature sensors to predict hardware failure 72 hours in advance. Automated remediation: the AI identifies the root cause, proposes a fix, and (for approved actions) implements it without human intervention. The SA's role shifts from "fix the problem" to "design the system so the problem cannot occur, and if it does, the system heals itself."

### Lecture Notes

Troubleshooting is the skill that transforms a knowledgeable SA into an effective SA. Knowing every protocol is useless if you cannot diagnose a problem systematically. The methodology is simple but requires discipline: (1) define the problem precisely — "the web server is slow" is a symptom, not a problem; "the web server takes 5 seconds to respond to requests from the student VLAN but responds in 50ms from the admin VLAN" is a problem; (2) gather data — check logs, run diagnostic commands, capture packets; (3) form a hypothesis — "the student VLAN traffic is being rate-limited by the firewall"; (4) test the hypothesis — run `tcpdump` on the firewall interface for the student VLAN and check for dropped packets; (5) if the hypothesis is confirmed, fix the problem; if not, form a new hypothesis.

The bottom-up approach is the most reliable for network problems. Start at Layer 1: is there a link light? Is the cable seated properly? Is the SFP module compatible? `ethtool eno1` answers these questions. Layer 2: is the MAC address table populated? Can the switch see the device? `ip neigh show` shows ARP entries. Layer 3: can you ping the gateway? The remote host? `ping` and `traceroute` answer these questions. Layer 4: can you establish a TCP connection on the expected port? `nc -zv host port` tests TCP connectivity. Layer 7: does the application respond correctly? `curl -v https://target` tests the full application stack.

`tcpdump` is the most powerful network diagnostic tool available. It captures every packet that the interface sees (or receives, depending on the interface's promiscuous mode setting). The SA can filter captures by host, port, protocol, or any combination: `tcpdump -i eno1 -nn host 10.20.1.5 and port 443` captures only HTTPS traffic to/from that host. The `-w` flag writes captures to a file for later analysis in Wireshark. In practice, `tcpdump` is the first tool the SA reaches for when a network problem is not immediately obvious from Layer 1-3 checks.

The shift from manual network configuration to SDN and network automation is the defining trend of the 2020s and 2030s. In the past, an SA configured each switch manually via SSH and CLI — a time-consuming, error-prone process. In 2040, the SA writes Ansible playbooks that configure all switches identically, and SDN controllers push forwarding rules programmatically. The benefit is consistency (every switch has the same configuration), auditability (all changes are tracked in Git), and speed (a new VLAN can be deployed to 50 switches in seconds, not hours).

The AI-orchestrated fabric extends this automation to detection and remediation. The Bifrǫst Mesh's AI agent monitors every metric — interface counters, error rates, latency percentiles, BGP session flaps — and detects anomalies using unsupervised learning. When it identifies an anomaly (e.g., an interface that has never dropped packets is now dropping 0.1% of packets), it creates an alert and proposes a root cause. For approved remediations (e.g., disabling a failing port, shifting traffic to a backup path), the agent implements the fix autonomously. The SA reviews the action after the fact and updates the policy if needed. This is the Heimdallr principle made operational: the system watches with tireless vigilance, and the SA supervises the watchman.

### Required Reading

- Limoncelli, T.A. (2037). *The Practice of System and Network Administration*, 4th Edition. Addison-Wesley. Chapter on Troubleshooting.
- Kurose, J.F. & Ross, K.W. (2038). *Computer Networking: A Top-Down Approach*, 9th Edition. Chapter 7 (Network Management) and Chapter 9 (SDN).
- Yggdrasil Bifrǫst Mesh Operations Manual (2040). UoY Infrastructure Documentation. (The operational guide for the campus self-healing fabric.)

### Discussion Questions

1. A user reports that "the Internet is down." Describe your troubleshooting methodology, starting from Layer 1 and working up. At each layer, describe the specific symptoms and commands you would use.
2. SDN centralizes the control plane. What are the single points of failure in an SDN architecture? How can the SA design the controller for resilience?
3. If an AI agent detects and remediates 95% of network incidents without human intervention, what is the SA's role? Describe the skills that become more important when routine troubleshooting is automated.

---

## Final Examination Preparation

### Format
The final examination consists of **8 essay questions** from which you must choose **4**. Each question requires a substantive, technical response of 500-800 words with specific examples, commands, and protocol details. Additionally, there is a **practical lab component** in which you will configure a multi-node network topology from scratch.

### Sample Essay Questions

1. **The OSI Model as a Diagnostic Tool.** A colleague reports that "the application server cannot connect to the database." Describe a systematic Layer-by-Layer troubleshooting methodology. For each layer (1 through 7), give the specific diagnostic command(s) you would run and the symptoms you would observe if that layer were the problem. Conclude with a decision tree for rapid diagnosis.

2. **IPv4 vs. IPv6: The Coexistence Challenge.** The University of Yggdrasil has been running dual-stack (IPv4 + IPv6) for five years. Propose a migration plan to make IPv6 the primary protocol while maintaining IPv4 compatibility for legacy devices. Address: addressing strategy, DNS configuration, application changes, monitoring, and the timeline. What are the five most common failure modes you anticipate?

3. **DNS as Critical Infrastructure.** Design a highly available DNS architecture for the university campus. Your design must survive: (a) failure of any single DNS server, (b) failure of the primary data center, (c) corruption of a zone file. Include: server topology, replication mechanism, failover procedure, monitoring, and the DNSSEC key management process. Justify each design decision with a specific failure scenario it mitigates.

4. **Network Security Zoning.** Design a VLAN and firewall architecture for a campus network with the following zones: DMZ (public-facing web servers), trusted (internal file servers and databases), management (infrastructure management switches, servers, and out-of-band access), student (student devices), IoT (campus sensors and smart devices), and guest (visitor devices). For each zone, define: VLAN ID, IP subnet, ACL rules (what traffic may enter and leave), and monitoring requirements. Explain how 802.1X and RADIUS enforce identity-based access.

5. **TCP Performance Diagnosis.** A production web server serves 10,000 concurrent connections but shows 30% higher latency than expected. Describe the diagnostic process to identify whether the bottleneck is in the network (bandwidth, latency, packet loss) or the server (CPU, memory, disk I/O). Which TCP metrics (from `ss -i`, `netstat -s`, or eBPF tools) would you examine? How would you distinguish between a network congestion problem and a server resource exhaustion problem?

6. **DHCP Scope Design.** You are tasked with designing the DHCP architecture for a campus with 8 buildings, each with 500 devices. Each building needs its own subnet, and there is a shared server farm with 200 static addresses. Design: (a) the subnet allocation using VLSM from the 10.0.0.0/8 private address space, (b) the DHCP server topology (where to place servers for redundancy), (c) the lease time policy (differentiate between student devices, faculty devices, and IoT devices), and (d) the DDNS integration. Calculate the total address utilization.

7. **The Self-Healing Network.** Describe how an AI-orchestrated network fabric (like the Bifrǫst Mesh) detects, diagnoses, and remediates a hardware failure. Walk through a specific scenario: a 10Gbps uplink between two switches begins dropping packets intermittently. Trace the detection (which metrics trigger the anomaly), the diagnosis (how the AI identifies the root cause), and the remediation (what automated action is taken). What guardrails must the SA place on the AI's autonomy?

8. **Network Automation and Infrastructure as Code.** The university's network has 50 switches, 200 access points, and 10 routers, all currently configured via manual CLI. Propose a migration plan to full Infrastructure as Code: (a) choose an automation framework (Ansible/NAPALM/custom), (b) define the Git repository structure, (c) describe the configuration deployment pipeline (PR → review → test → deploy), (d) handle the "configuration drift" problem (what happens when someone makes a manual change outside the pipeline), and (e) estimate the effort and timeline for the migration.

### Practical Lab Component

Students will configure a multi-node network topology in the Heimdallr Networking Lab, demonstrating competency in:
- IPv4 and IPv6 addressing and subnetting
- VLAN configuration on managed switches
- OSPF routing between simulated buildings
- DNS and DHCP server configuration
- nftables firewall rules for a segmented network
- Network troubleshooting using tcpdump, ss, and iproute2

*May the Bifrǫst hold strong, may the Norns guide your packets, and may your pings always return.* ᛟ

— University of Yggdrasil, Department of Systems Administration, 2040