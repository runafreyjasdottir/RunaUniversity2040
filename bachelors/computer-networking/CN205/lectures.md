# CN205: Wireless & Mobile Networks
## Bachelor of Science in Computer Networking — University of Yggdrasil, 2040

**Credits:** 4
**Description:** Comprehensive study of wireless and mobile networking — from radio propagation and signal processing through Wi-Fi 9, 6G cellular, satellite constellations, and mesh wireless. Students master RF engineering, protocol design, mobility management, and the 2040 landscape of integrated terrestrial-satellite-orbital connectivity.

**Instructor:** Dr. Astrid Valkyriusdottir, Professor of Wireless Engineering & Bifrǫst Orbital Lead
**Lab:** Valhalla Network Lab, Sublevel 2, Hákon Computing Centre (RF Anechoic Chamber available)
**Office Hours:** Mondays & Wednesdays 10:00-12:00, or by appointment

---

## Lectures

ᚠ **Lecture 1: Radio Propagation — The Physics of Wireless Communication**

**Course:** CN205 — Wireless & Mobile Networks
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Wireless communication begins with physics. This lecture covers the fundamental phenomena that govern radio propagation: free-space path loss, reflection, diffraction, scattering, multipath fading, and the Shannon-Hartley theorem. Understanding these phenomena is essential because every wireless protocol is an attempt to overcome the limitations of the radio channel.

### Key Topics

- **The Electromagnetic Spectrum:** Frequency bands allocated for wireless communication: VLF (3-30 kHz) through EHF (30-300 GHz) and terahertz (100 GHz - 10 THz). The relationship between frequency, wavelength, bandwidth, and propagation characteristics. Why lower frequencies propagate farther (better diffraction around obstacles) while higher frequencies carry more data (more bandwidth per Hz of spectrum). The 2040 spectrum landscape: sub-6 GHz for wide area, mmWave (24-100 GHz) for capacity, and terahertz (100-300 GHz) for ultra-short-range high-speed links.
- **Free-Space Path Loss:** Signal power decreases with the square of the distance (inverse-square law). The Friis transmission equation: received power = transmitted power + antenna gains − path loss. Why a 2.4 GHz signal loses 40 dB more than a 900 MHz signal at the same distance. The practical implication: higher frequencies need more base stations to cover the same area.
- **Multipath Propagation:** Reflection (signals bouncing off buildings, water, terrain), diffraction (signals bending around edges), and scattering (signals dispersing off irregular surfaces). The multipath effect: signals arrive at the receiver via multiple paths with different delays, causing constructive and destructive interference (Rayleigh and Rician fading). The solution: OFDM (Orthogonal Frequency-Division Multiplexing) converts the wideband fading channel into many narrowband flat-fading subcarriers.
- **The Shannon-Hartley Theorem:** Channel capacity C = B × log₂(1 + S/N), where B is bandwidth and S/N is signal-to-noise ratio. The fundamental limit on how much data a channel can carry. Practical implications: increase capacity by increasing bandwidth (use higher frequencies) or increasing S/N (more power, better antennas, shorter distance, or noise reduction). The theorem as a tool for evaluating technology claims: a protocol that promises 10 Gbps in 10 MHz of bandwidth at 1 km range is violating Shannon.
- **Antenna Theory:** Isotropic radiators, dipole antennas, antenna gain (dBi), and beamwidth. The relationship between antenna size and wavelength: efficient antennas are roughly half a wavelength long (6 cm at 2.4 GHz, 1.5 mm at 100 GHz). MIMO (Multiple-Input Multiple-Output): using multiple antennas to create spatial diversity and multiplex multiple data streams. Massive MIMO in 6G: base stations with hundreds of antennas serving dozens of users simultaneously.

### Lecture Notes

The Shannon-Hartley theorem is the most important equation in wireless networking. It tells you the absolute maximum data rate a channel can support, given its bandwidth and signal-to-noise ratio. No protocol, no modulation scheme, no amount of signal processing can exceed this limit. If someone claims their new modulation achieves 10 Gbps in 100 MHz of bandwidth with a 10 dB signal-to-noise ratio, the theorem tells you they are wrong: C = 100 × 10⁶ × log₂(1 + 10) = 100 × 10⁶ × 3.46 ≈ 346 Mbps. The remaining 9.65 Gbps does not come from modulation — it comes from antenna gain, spatial multiplexing, or a misunderstanding of what Shannon guarantees.

Multipath fading is the wireless engineer's nemesis. In a city, a signal from a base station reaches your phone not just via the direct path but also via reflections off buildings, the ground, and even vehicles. These reflected copies arrive at slightly different times (because they traveled different distances), creating a pattern of constructive and destructive interference. When you walk a few centimeters, the pattern changes — you may go from a strong signal to a dead zone in a single step. This is Rayleigh fading, named after Lord Rayleigh who first described it for sound waves. OFDM, the modulation used by Wi-Fi, 4G, 5G, and 6G, combats multipath by dividing the channel into many narrow subcarriers, each of which experiences flat fading (not frequency-selective fading). A subcarrier that is in a deep fade can be compensated by forward error correction, while in a wideband system, the entire signal would be degraded.

Massive MIMO is the key technology that enables 6G's terabit speeds. A 6G base station has 256 or more antenna elements, each of which can transmit and receive independently. Using beamforming, the base station focuses its signal energy toward each user, creating a narrow beam that increases the signal-to-noise ratio at the receiver while reducing interference for other users. Using spatial multiplexing, the base station can transmit multiple independent data streams on the same frequency, each directed at a different user, multiplying the total throughput by the number of streams. The math: with 256 antennas, a base station can serve approximately 64 simultaneous users on the same frequency, each at the full bandwidth of the channel. This is how 6G achieves its headline speeds: not by a single breakthrough but by the cumulative effect of wider bandwidth (mmWave and terahertz), higher-order modulation (4096-QAM), and massive MIMO.

### Required Reading

- Rappaport, T.S. (2037). *Wireless Communications: Principles and Practice*, 4th Edition. Prentice Hall. Chapters 1-4.
- Andrews, J.G., et al. (2035). "What Will 6G Be?" *IEEE Journal on Selected Areas in Communications*, 38(8), 1747-1761.
- Yggdrasil Wireless Engineering Handbook (2040). "RF Propagation" and "Antenna Design."

### Discussion Questions

1. The Shannon-Hartley theorem says that channel capacity increases with bandwidth and signal-to-noise ratio. Terahertz bands offer enormous bandwidth but very short range and poor penetration. Is terahertz wireless useful, or is it a laboratory curiosity? What applications would benefit from its properties?
2. A wireless engineer claims their new protocol achieves "5× Shannon capacity." Explain why this claim is impossible, and describe what they might actually be measuring (e.g., spatial multiplexing with MIMO).
3. In a city, a mobile device experiences Rayleigh fading with signal strength varying by 30 dB as the user walks. How do wireless protocols (Wi-Fi, 5G) cope with this extreme variation? What are the limits of coping mechanisms?

---

ᚢ **Lecture 2: Wi-Fi — From 802.11 to Wi-Fi 9**

**Course:** CN205 — Wireless & Mobile Networks
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Wi-Fi is the most widely deployed wireless technology on the planet. This lecture covers the IEEE 802.11 family from the original 802.11b (11 Mbps, 1999) through Wi-Fi 9 (802.11be-2040, 100 Gbps), examining the physical layer techniques, medium access control, security mechanisms, and practical deployment considerations that make Wi-Fi both ubiquitous and challenging.

### Key Topics

- **802.11 Evolution:** 802.11b (11 Mbps, 2.4 GHz, DSSS) → 802.11a (54 Mbps, 5 GHz, OFDM) → 802.11g (54 Mbps, 2.4 GHz, OFDM) → 802.11n / Wi-Fi 4 (600 Mbps, MIMO, 2.4/5 GHz) → 802.11ac / Wi-Fi 5 (6.9 Gbps, wide channels, MU-MIMO, 5 GHz) → 802.11ax / Wi-Fi 6 (9.6 Gbps, OFDMA, 1024-QAM, 2.4/5/6 GHz) → 802.11be / Wi-Fi 7 (46 Gbps, 320 MHz, 4096-QAM, MLO) → 802.11be-2040 / Wi-Fi 9 (100 Gbps, terahertz backhaul, AI-driven resource allocation).
- **Physical Layer Techniques:** OFDM (Orthogonal Frequency-Division Multiplexing): dividing a wide channel into many narrow subcarriers, each modulated independently. OFDMA (Orthogonal Frequency-Division Multiple Access): allocating subsets of subcarriers to different users simultaneously. MIMO (Multiple-Input Multiple-Output): spatial diversity (same data on multiple antennas for reliability) and spatial multiplexing (different data on each antenna for throughput). MU-MIMO (Multi-User MIMO): serving multiple users on the same channel simultaneously.
- **Medium Access Control:** CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance): listen before transmit, wait if busy, random backoff if collision. RTS/CTS (Request to Send / Clear to Send): reducing hidden node collisions. The problem: CSMA/CA scales poorly — as more devices contend, collision probability increases and throughput decreases. 802.11ax's solution: OFDMA scheduling, where the access point allocates subcarriers to specific users, eliminating contention.
- **Wi-Fi Security:** WEP (broken), WPA (improved but still vulnerable), WPA2 (AES-CCMP, robust), WPA3 (SAE replacing PSK, 192-bit enterprise mode, OWE for opportunistic encryption). The 2040 standard: WPA4 with post-quantum key exchange. The fundamental issue: Wi-Fi signals are broadcast, so anyone within range can eavesdrop — encryption is not optional, it is essential.
- **Wi-Fi Deployment:** Site survey, channel planning, power management, and capacity planning. The 6 GHz band (Wi-Fi 6E/7/9): 1200 MHz of new spectrum, enabling 320 MHz channels. The challenge: 6 GHz has shorter range than 2.4 GHz, requiring more access points. The solution: mesh Wi-Fi (access points wirelessly backhaul to each other) and AI-driven channel assignment (the Bifrǫst Mesh Wi-Fi controller optimizes channel and power settings every 5 minutes).

### Lecture Notes

Wi-Fi's medium access control is both its greatest strength and its greatest weakness. CSMA/CA is beautifully simple: before transmitting, listen to the channel. If it is busy, wait. If it is idle, transmit. If two devices transmit simultaneously (a collision), both wait a random time and try again. This distributed coordination works well with few devices — each device gets a fair share of the channel, and collisions are rare. But as device density increases (a lecture hall with 200 students, each with a laptop and a phone), collisions become frequent, backoff times increase, and throughput collapses. The 802.11ax solution — OFDMA scheduling — replaces contention with scheduling: the access point tells each device when and on which subcarriers to transmit, eliminating collisions entirely. In practice, Wi-Fi 6 and later use a hybrid approach: OFDMA for scheduled traffic and CSMA/CA for best-effort traffic.

The hidden node problem is Wi-Fi's most insidious challenge. When two devices are on opposite sides of an access point, within range of the AP but not of each other, they cannot hear each other's transmissions. Both may sense the channel as idle and transmit simultaneously, causing a collision at the AP. RTS/CTS mitigates this: the sender first transmits a short RTS frame, the AP responds with a CTS frame, and all devices that receive the CTS know that the channel is reserved. But RTS/CTS adds overhead, reducing throughput by 10-15%. In practice, RTS/CTS is rarely enabled because the overhead is too high for most traffic patterns.

Wi-Fi 9 (802.11be-2040) represents the convergence of Wi-Fi and cellular technologies. Multi-Link Operation (MLO), introduced in Wi-Fi 7, allows a device to simultaneously connect on 2.4 GHz, 5 GHz, and 6 GHz, aggregating bandwidth and seamlessly switching links if one fails. Wi-Fi 9 extends MLO with AI-driven link selection: the access point monitors the quality of each link (throughput, latency, error rate) and directs each packet to the best link in real time. Terahertz backhaul (100-300 GHz) enables wireless connections between access points at data center speeds, eliminating the need for Ethernet cabling in office buildings. And AI-driven resource allocation dynamically adjusts channel assignments, power levels, and scheduling based on real-time traffic patterns, replacing the manual site survey with continuous optimization.

The 6 GHz band is the most significant Wi-Fi capacity increase since the 5 GHz band was opened in 2003. The 6 GHz band provides 1,200 MHz of spectrum — enough for three 320 MHz channels or 59 20 MHz channels. In contrast, the 5 GHz band provides only 500 MHz of usable spectrum (after DFS restrictions). The result: 6 GHz Wi-Fi can sustain 100+ simultaneous high-definition video streams where 5 GHz Wi-Fi would struggle with 10. But 6 GHz has a shorter effective range — roughly half that of 5 GHz at the same power — because higher-frequency signals are more easily absorbed by walls, furniture, and people. This means that upgrading from 5 GHz to 6 GHz coverage requires approximately 2× more access points, a significant cost increase that must be justified by the capacity improvement.

### Required Reading

- Gast, M.S. (2038). *802.11 Wireless Networks: The Definitive Guide*, 4th Edition. O'Reilly. Chapters 1-6.
- IEEE 802.11be-2040 Working Group. "Wi-Fi 9: Ultra-High Throughput and AI-Driven Resource Management."
- Yggdrasil Wireless Operations Guide (2040). "Wi-Fi 9 Deployment" and "6 GHz Planning."

### Discussion Questions

1. CSMA/CA scales poorly with many contending devices. OFDMA scheduling eliminates contention but requires centralized control. Is scheduling always better than contention, or are there scenarios where CSMA/CA is preferable? Consider a sparse network with few devices vs. a dense network with many devices.
2. The 6 GHz band provides enormous capacity but shorter range. A company has 5 GHz Wi-Fi covering its office with 20 access points. How many access points would they need for equivalent 6 GHz coverage? What is the total cost of ownership, including cabling, power, and licensing?
3. Wi-Fi 9's AI-driven resource allocation optimizes channel and power settings in real time. What happens when the AI makes a suboptimal decision? How would you detect and recover from AI-induced misconfigurations?

---

ᚦ **Lecture 3: Cellular Networks — 5G, 6G, and Beyond**

**Course:** CN205 — Wireless & Mobile Networks
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Cellular networks have evolved from voice-only analog systems to the planet's largest broadband infrastructure. This lecture covers 5G as the foundation, 6G as the current frontier, and the architectural innovations that enable terabit speeds, sub-millisecond latency, and integrated sensing and communication.

### Key Topics

- **5G Architecture:** Standalone (SA) and non-standalone (NSA) deployment. The 5G core (5GC) with service-based architecture, network slicing, and the AMF/SMF/UPF function split. Three pillars: eMBB (enhanced Mobile Broadband — high throughput), URLLC (Ultra-Reliable Low-Latency Communication — sub-1ms latency), and mMTC (massive Machine-Type Communication — millions of devices). The 5G numerology: flexible subcarrier spacing (15 kHz to 240 kHz) and slot duration.
- **6G Architecture:** The 6G core extends 5GC with AI-native functions: AI-driven RAN (Radio Access Network) optimization, intelligent resource management, and predictive mobility management. Terabit-per-second peak rates, 100 μs latency, and integrated sensing and communication (ISAC). The 6G numerology: subcarrier spacing up to 960 kHz, supporting terahertz bands. The 6G standard (3GPP Release 20, finalized 2035, deployed 2036-2040).
- **Network Slicing:** Creating multiple virtual networks on a single physical infrastructure, each with guaranteed performance characteristics. An eMBB slice for video streaming (high throughput, moderate latency), a URLLC slice for autonomous vehicles (low throughput, ultra-low latency), and an mMTC slice for IoT sensors (low throughput, high device density). Slice isolation: ensuring that congestion in one slice does not affect another.
- **Integrated Sensing and Communication (ISAC):** 6G base stations use the same radio signals for both communication and environmental sensing. By analyzing radio reflections, a base station can detect the position, velocity, and even the posture of nearby objects — enabling pedestrian safety, vehicle tracking, and structural monitoring. The privacy implications: a network that can sense people is a network that can surveil them.
- **Open RAN (O-RAN):** Disaggregating the radio access network into open, interoperable components: RU (Radio Unit), DU (Distributed Unit), and CU (Centralized Unit), connected by open fronthaul and midhaul interfaces. The benefits: vendor diversity, cost reduction, and flexibility. The challenges: integration complexity, performance optimization across vendors, and security of open interfaces.

### Lecture Notes

The evolution from 5G to 6G is not just about faster speeds — it is about a fundamental shift in what the network does. 5G's three pillars (eMBB, URLLC, mMTC) already recognize that different applications have different needs. 6G adds a fourth pillar: ISAC, integrated sensing and communication. A 6G base station is both a communication device and a radar. It transmits signals that carry data to users, and it receives reflections that carry information about the environment. The same signal that delivers a video stream to a phone also bounces off a pedestrian stepping into the street, allowing the base station to detect the pedestrian and alert nearby autonomous vehicles. This dual use is not a gimmick — it is a fundamental architectural change that makes the network an active participant in the physical environment, not just a communication channel.

Network slicing is the enabling technology for 6G's service diversity. Without slicing, a single network must serve all applications with the same policies — a one-size-fits-all approach that fails because video streaming needs high throughput, autonomous vehicles need low latency, and IoT sensors need low power. With slicing, each application gets its own virtual network with guaranteed resources. An eMBB slice might allocate 400 MHz of bandwidth with 10 ms latency; a URLLC slice might allocate 20 MHz with 0.1 ms latency and 99.9999% reliability; an mMTC slice might allocate narrow channels with 10-year battery life. The key engineering challenge is slice isolation: ensuring that congestion in one slice (millions of IoT devices sending simultaneously) does not starve another slice (an autonomous vehicle that needs its packet within 0.1 ms). This requires strict resource partitioning at every layer: separate radio resources, separate processing queues, and separate transport tunnels.

Open RAN is transforming the cellular industry from a market dominated by three vendors (Ericsson, Nokia, Huawei) to an ecosystem of interoperable components. The O-RAN Alliance defines open interfaces between the radio unit (which handles RF), the distributed unit (which handles real-time L1/L2 processing), and the centralized unit (which handles L3 and RRC). Any vendor's RU can connect to any vendor's DU via the open fronthaul interface, enabling operators to mix and match components. The Yggdrasil Bifrǫst Mesh uses O-RAN architecture for its 6G deployment, with radios from three vendors and a centralized RAN intelligent controller (RIC) that optimizes performance across all of them. The challenge is integration: different vendors interpret specifications differently, and edge cases emerge that no specification covers. The O-RAN integration lab at Yggdrasil tests multi-vendor combinations before deployment.

### Required Reading

- Dahlman, E., Parkvall, S., & Skold, J. (2038). *5G NR: The Next Generation Wireless Access Technology*, 4th Edition. Academic Press. Chapters 1-5.
- Dang, S., et al. (2035). "What Should 6G Be?" *IEEE Internet of Things Journal*, 8(15), 11657-11676.
- Yggdrasil 6G Deployment Guide (2040). "Network Slicing" and "O-RAN Integration."

### Discussion Questions

1. ISAC enables a base station to detect and track people without their knowledge. Should this capability be required to be disabled by default, enabled only with explicit consent? How would you regulate a technology that is integral to both safety (pedestrian detection) and surveillance (people tracking)?
2. Network slicing requires strict resource isolation. But resources are finite — allocating 20 MHz to a URLLC slice means it is not available for eMBB. How should a network operator balance competing demands from different slices? Who decides which slices get priority?
3. Open RAN promises vendor diversity and lower costs, but integration is challenging. Under what circumstances would you choose a single-vendor RAN (simpler, guaranteed interoperability) over an O-RAN deployment (more flexible, potentially lower cost)?

---

ᚬ **Lecture 4: Mobile IP and Seamless Mobility**

**Course:** CN205 — Wireless & Mobile Networks
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Mobility is the defining challenge of wireless networking: how does a device maintain active connections while moving between networks? This lecture covers Mobile IP, its successors (Proxy Mobile IP, Distributed Mobility Management), the QUIC connection migration approach, and the 2040 Session Continuity Protocol (SCP) used in the Bifrǫst Mesh.

### Key Topics

- **The Mobility Problem:** When a device moves from one network to another (Wi-Fi to cellular, one cell to another, one access point to another), its IP address changes. Active TCP connections break because they are bound to the old IP address. Active UDP flows break because reply packets are routed to the old network. Application state (video calls, SSH sessions, game connections) is lost.
- **Mobile IP (RFC 5940):** The IETF's original mobility solution. The mobile node has a home address (permanent) and a care-of address (temporary, at the visited network). The home agent tunnels packets from the home network to the care-of address. The problems: triangular routing (packets from the correspondent to the mobile node go through the home agent), tunneling overhead, and security complications (IPsec for tunnel authentication).
- **Proxy Mobile IPv6 (PMIPv6):** The network-controlled alternative: the network (not the device) handles mobility signaling. The mobile access gateway (MAG) in the visited network detects the device's attachment and signals the local mobility anchor (LMA) to tunnel packets. The device keeps its home address and is unaware of the mobility — no Mobile IP stack required. The benefit: works with any device. The cost: reliance on network infrastructure.
- **Distributed Mobility Management (DMM):** The 2040 approach: instead of anchoring traffic at a central home agent, distribute the anchoring to the network edge. Each access network has a local mobility anchor, and traffic is re-routed through the optimal path after handoff. DMM eliminates triangular routing and reduces latency. The Bifrǫst Mesh uses DMM for all mobility management.
- **QUIC Connection Migration:** The application-layer solution: QUIC connections are identified by a connection ID, not by the 4-tuple (source/destination IP/port). When the device's IP address changes (Wi-Fi to cellular), the QUIC connection survives — the peer recognizes the connection ID and continues the session. QUIC connection migration is the simplest and most effective mobility solution for QUIC-based applications.
- **Session Continuity Protocol (SCP):** The Bifrǫst Mesh's mobility layer, designed for environments where both Mobile IP and QUIC migration are insufficient. SCP operates at the session layer (Layer 5), maintaining session state (encryption keys, sequence numbers, application context) across network changes. SCP coordinates with the Bifrǫst path manager to pre-establish subflows on candidate networks before handoff, enabling zero-packet-loss transitions.

### Lecture Notes

Mobile IP was the IETF's first attempt to solve the mobility problem, and it illustrates the difficulty elegantly. The core idea is simple: a mobile device has a permanent home address, and a temporary care-of address at its current location. A router called the home agent, located in the device's home network, tunnels packets to the care-of address. The device's correspondents see only the home address, so they do not need to know about mobility. The problem is triangular routing: packets from a correspondent in Tokyo to a mobile node in Oslo must first go to the home agent in Stockholm, then tunnel to Oslo. This adds 30-60 ms of latency, wastes bandwidth on the Tokyo-Stockholm-Oslo path, and creates a single point of failure at the home agent.

Proxy Mobile IPv6 (PMIPv6) improves on Mobile IP by moving the mobility function from the device to the network. The device does not need a Mobile IP stack — it simply connects to the new network and receives its home address via DHCP. The network's local mobility anchor handles tunneling. PMIPv6 is used in 5G and 6G for inter-access-point mobility (the device moves between cells without changing its IP address). But PMIPv6 still suffers from centralized anchoring and the latency of tunneling traffic through the anchor.

QUIC connection migration is the simplest and most elegant solution for QUIC-based traffic. When a smartphone moves from Wi-Fi to cellular, the QUIC connection survives because the connection ID (not the IP address) identifies the session. The peer sees a packet from a new IP address but with a known connection ID, and continues the session. This is aTransport-layer solution — no Mobile IP, no PMIPv6, no tunnels, no anchors. The limitation: QUIC connection migration works only for QUIC-based applications. Legacy TCP connections still break on IP address change. And QUIC migration does not help when both the IP address and the port change (some NATs remap the source port).

The Session Continuity Protocol (SCP) is Yggdrasil's solution for environments where seamless mobility is critical — autonomous vehicles that cannot afford even a 100 ms interruption, industrial robots that must maintain real-time control connections, and medical devices that cannot drop telemetry. SCP operates at the session layer, maintaining encryption contexts, flow control state, and application metadata across handoffs. Before a handoff, the SCP path manager pre-establishes subflows on the candidate network (e.g., establishing a QUIC connection on the cellular interface before leaving Wi-Fi coverage). At handoff, SCP migrates the session to the pre-established subflow, achieving zero packet loss and sub-millisecond transition time. SCP is deployed throughout the Bifrǫst Mesh for critical services.

### Required Reading

- Perkins, C. (2035). "IP Mobility Support for IPv4," RFC 5940 (updated). IETF.
- Gundavelli, S. et al. (2034). "Proxy Mobile IPv6," RFC 5213 (updated). IETF.
- Yggdrasil Mobility Management Guide (2040). "SCP" and "DMM Architecture."

### Discussion Questions

1. Mobile IP's triangular routing adds latency and creates a single point of failure at the home agent. Why was Mobile IP designed this way? What would be needed to eliminate triangular routing while preserving the home address abstraction?
2. QUIC connection migration works for QUIC-based applications but not for TCP. Is it acceptable to let TCP connections break during mobility, relying on applications to reconnect? What are the implications for real-time applications like voice calls?
3. SCP pre-establishes subflows before handoff to achieve zero-packet-loss transitions. How does SCP know which network the device will hand off to? What happens if the prediction is wrong and the device connects to a different network than expected?

---

ᚱ **Lecture 5: Satellite Networks and Orbital Constellations**

**Course:** CN205 — Wireless & Mobile Networks
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Low Earth Orbit (LEO) satellite constellations have transformed global connectivity. This lecture covers the architecture of satellite networks, orbital mechanics relevant to communications, inter-satellite links, spectrum management, and the integration of satellite and terrestrial networks in 2040.

### Key Topics

- **Orbital Regimes:** LEO (Low Earth Orbit, 300-2,000 km): low latency (20-40 ms round trip), short pass duration (10-20 minutes per satellite). MEO (Medium Earth Orbit, 2,000-35,786 km): medium latency (70-150 ms), longer passes. GEO (Geostationary Earth Orbit, 35,786 km): high latency (240 ms round trip), permanent coverage of fixed area. The 2040 shift: newer constellations use LEO for latency-sensitive applications, MEO for navigation, and GEO for broadcast and fixed services.
- **LEO Constellation Architecture:** Starlink 3.0 (12,000 satellites, 340 km, 1-2 Tbps per satellite), OneWeb (6,500 satellites, 1,200 km), EU IRIS² (300 satellites, 780 km), and Bifrǫst Orbital (200 satellites, 500 km polar orbit). Phased array antennas on satellites and ground terminals. Spot beams: each satellite covers a 50-100 km diameter cell with a narrow beam, enabling frequency reuse across cells.
- **Inter-Satellite Links (ISLs):** Laser links between satellites for direct orbital routing, bypassing ground stations. The benefit: reduced latency (direct orbital path instead of satellite → ground → fiber → ground → satellite). The challenge: precise pointing (nanoradian accuracy) and Doppler shift from satellite movement. The Bifrǫst Orbital constellation uses ISLs for all inter-satellite communication, creating an orbital mesh network.
- **Satellite-Terrestrial Integration:** The 3GPP 5G/6G standard for satellite integration: satellite as a 5G/6G RAN node, with the satellite acting as a relay or a base station. The 6G NR-NTN (Non-Terrestrial Network) standard: standardized protocols for satellite-terrestrial handoff, tracking area management, and timing advance. The Bifrǫst Mesh's integrated satellite-terrestrial architecture: BTP (Bifrǫst Transport Protocol) seamlessly switches between terrestrial and satellite paths.
- **Spectrum Management:** The ITU Radio Regulations allocate spectrum for satellite communications. The 2040 spectrum landscape: Ku-band (12-18 GHz) and Ka-band (26-40 GHz) for consumer broadband, V-band (40-75 GHz) and E-band (71-86 GHz) for backhaul. The challenge: spectrum is shared with terrestrial services, and interference must be managed through coordination.

### Lecture Notes

Satellite networking in 2040 bears little resemblance to the geostationary satellite systems of the 2000s. The key difference is orbital altitude: GEO satellites at 35,786 km have a round-trip latency of at least 240 ms (the speed-of-light travel time), which is acceptable for broadcast TV but unusable for interactive applications. LEO satellites at 340-1,200 km have round-trip latency of 20-40 ms, comparable to terrestrial networks and adequate for voice, video, and real-time applications. The cost of LEO is that satellites move relative to the ground — a LEO satellite passes overhead in 10-20 minutes, requiring continuous handoff between satellites and tracking by ground terminals.

The Bifrǫst Orbital constellation is the Nordic contribution to global satellite connectivity. With 200 satellites in polar orbits at 500 km altitude, it provides continuous coverage above 60°N latitude — the Arctic, where terrestrial infrastructure is sparse and other constellations have limited coverage. The constellation uses laser inter-satellite links to create an orbital mesh: a packet from Svalbard to Oslo can travel satellite-to-satellite through the orbital mesh, never touching a ground station, with end-to-end latency of 30 ms. This is faster than the terrestrial fiber route from Svalbard to Oslo (which runs through mainland Norway and adds 40 ms of routing and processing latency).

Inter-satellite laser links are the enabling technology for low-latency orbital networking. Each satellite carries four laser terminals (forward, backward, left, right) that maintain connections to neighboring satellites as they orbit. The指向 (pointing) accuracy required is astonishing: at a distance of 2,000 km between satellites, a pointing error of 1 microradian shifts the beam by 2 meters — wider than the receiving telescope's aperture. The satellites use star trackers, gyroscope-based inertial measurement units, and optical beacons to achieve the necessary pointing accuracy. The Doppler shift from satellite movement (7.5 km/s orbital velocity) shifts the laser frequency by up to 10 GHz, which must be compensated by wavelength-tunable lasers.

The integration of satellite and terrestrial networks under 6G NR-NTN (Non-Terrestrial Network) standards enables seamless connectivity across both domains. A 6G device in Tromsø may connect to a terrestrial base station in the city center, switch to a satellite as it drives into a rural valley, and switch back to terrestrial as it approaches another town. The handoff is managed by the 6G core, which treats the satellite as just another RAN node with different timing advance and propagation delay characteristics. The Bifrǫst Mesh's BTP transport protocol uses multi-path transport to maintain connections across both terrestrial and satellite paths, preferring the terrestrial path for low-latency traffic and the satellite path for bulk data when the terrestrial path is congested.

### Required Reading

- Leyva-Mayorga, I., et al. (2035). "LEO Satellite Constellations for 5G and Beyond." *IEEE Communications Surveys & Tutorials*, 23(3), 1630-1666.
- ITU Radio Regulations (2040). Articles 5, 8, 21 (satellite spectrum allocation).
- Yggdrasil Orbital Architecture Guide (2040). "Bifrǫst Orbital" and "Satellite-Terrestrial Integration."

### Discussion Questions

1. A LEO satellite constellation requires continuous handoff as satellites pass overhead. Design a handoff protocol that minimizes packet loss and latency during handoff. How does the 6G NR-NTN standard handle timing advance (the satellite is moving, so the RTT is continuously changing)?
2. Inter-satellite laser links require microradian pointing accuracy. A satellite's attitude control system has a pointing error of 0.1° (1,750 microradians). Calculate the maximum ISL range that can be maintained with this pointing error and a receiving telescope aperture of 10 cm.
3. The Bifrǫst Orbital constellation provides coverage above 60°N latitude. Why do other constellations (Starlink, OneWeb) have poorer Arctic coverage? How does the Bifrǫst constellation's polar orbit differ from their inclined orbits?

---

ᚴ **Lecture 6: Mesh Wireless and Community Networks**

**Course:** CN205 — Wireless & Mobile Networks
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Mesh wireless enables networks without infrastructure — nodes relay traffic for each other, creating connectivity where traditional networks cannot reach. This lecture covers mesh protocols, community networking, the Yggdrasil Mesh Link protocol, and the socio-technical aspects of building networks that serve underserved communities.

### Key Topics

- **Mesh Network Fundamentals:** Ad-hoc networking: nodes discover neighbors, form routes, and relay traffic without centralized infrastructure. Proactive routing (OLSR, B.A.T.M.A.N.): maintain routing tables even for unused destinations. Reactive routing (AODV): discover routes on demand. Hybrid routing: proactive for nearby nodes, reactive for distant ones. The challenge: scaling — route overhead grows with network size, and interference reduces throughput with each hop.
- **The B.A.T.M.A.N. Protocol:** Better Approach to Mobile Ad-hoc Networking. Each node broadcasts its existence, and neighbors forward broadcasts. Nodes track which neighbor offers the best route to each destination based on received broadcast quality. Simple, robust, and effective for small-to-medium meshes (10-100 nodes).
- **802.11s Mesh Standard:** The IEEE standard for Wi-Fi mesh networking. Mesh points (MPs) discover each other, establish peer links, and route frames using the HWMP (Hybrid Wireless Mesh Protocol) routing metric. The metric accounts for airtime cost, not just hop count. The limitation: 802.11s was designed for stationary meshes and does not handle high mobility well.
- **The Yggdrasil Mesh Link Protocol:** Designed for rural Norwegian communities, Mesh Link combines directional antennas, TDMA scheduling, and AI-powered channel assignment to create multi-hop wireless networks with 100+ Mbps throughput per node. Each node has a directional antenna pointing toward the backhaul and an omnidirectional antenna for local access. Mesh Link uses the B.A.T.M.A.N. protocol for route discovery and a custom TDMA scheduler for interference management. The network self-organizes: when a new node joins, it announces itself on the control channel, discovers neighbors, and integrates into the routing fabric.
- **Community Networks and Digital Equity:** The Yggdrasil Rural Connectivity Initiative: deploying Mesh Link in 50 Norwegian communities with populations under 5,000. The economical argument: fiber costs $15,000/km in rural terrain; Mesh Link costs $2,000/node. The social argument: connectivity enables telemedicine, distance education, and economic participation. The sustainability argument: community-owned networks are maintained by local volunteers, reducing operational costs.
- **Socio-Technical Challenges:** Sustainability: volunteer-based maintenance vs. the need for 99.9% uptime. Governance: who makes decisions about the network? Gender and diversity: who designs and maintains the network, and who benefits? The digital divide: is "good enough" connectivity (100 Mbps mesh) equivalent to fiber (1 Gbps symmetric)?

### Lecture Notes

Mesh wireless is the most democratic form of networking. It requires no telecom operator, no spectrum license (in the unlicensed bands), and no centralized infrastructure. A community can build its own network by installing mesh nodes on rooftops, pointing directional antennas at neighbors, and running open-source mesh software. The technology is mature enough to be reliable and cheap enough to be affordable; the challenge is not technology but sustainability — who maintains the network, who pays for backhaul, and who governs it?

The Yggdrasil Mesh Link deployment in rural Norwegian communities follows a co-operative model. Each community owns its mesh network as a co-operative, with members contributing $200-500 for a mesh node and $20-50/month for shared backhaul. The co-operative model ensures that the network serves community interests rather than profit-maximizing shareholders. Maintenance is performed by a combination of local volunteers (trained through Yggdrasil's network technician program) and remote monitoring from the Bifrǫst Mesh operations center. The result: 50 communities with 100+ Mbps connectivity, served by networks they own and govern.

The technical challenge of mesh wireless is interference management. In a dense mesh, every transmission is a potential source of interference for neighbors. The Mesh Link protocol addresses this through three mechanisms. First, TDMA scheduling: the mesh controller assigns each node a time slot for transmission, preventing simultaneous transmissions on the same channel. Second, directional antennas: by focusing radio energy toward the next hop rather than broadcasting in all directions, nodes reduce interference with other links. Third, AI-powered channel assignment: the mesh controller continuously monitors interference levels and reassigns channels to minimize conflict. The controller uses a neural network trained on thousands of mesh deployments to predict the optimal channel assignment, achieving 15-20% throughput improvement over static assignment.

Digital equity is the moral dimension of mesh networking. The question is not just "can we connect rural communities?" but "does the connectivity we provide enable genuine participation in the digital economy, or does it create a two-tier society where urban users have fiber and rural users have mesh?" The answer depends on the application: 100 Mbps mesh is sufficient for telemedicine, distance education, and remote work, but it is not equivalent to 1 Gbps symmetric fiber for applications that require high upload bandwidth (content creation, cloud computing, VR collaboration). The Yggdrasil Rural Connectivity Initiative addresses this by treating mesh as a stepping stone: communities start with mesh and graduate to fiber as demand and economic conditions justify the investment. The mesh network provides immediate connectivity and revenue; the revenue funds gradual fiber deployment.

### Required Reading

- AbdelMoghith, M. & Megahed, M. (2034). "Community Wireless Networks: A Survey." *IEEE Communications Surveys & Tutorials*, 22(4), 2570-2593.
- Yggdrasil Mesh Link Technical Manual (2040). "Deployment Guide" and "Protocol Specification."
- Yggdrasil Rural Connectivity Initiative Report (2039). "50 Communities Connected."

### Discussion Questions

1. Mesh networking relies on nodes relaying traffic for each other. What happens when a node owner decides to stop participating — does the network degrade gracefully, or does it collapse? How should mesh networks be designed for resilience to node departures?
2. A community mesh network has 30 nodes and a shared 1 Gbps backhaul connection. If each node uses 50 Mbps during peak hours, the backhaul is oversubscribed by 50%. Design a fair sharing mechanism that ensures each node gets at least 30 Mbps during peak hours.
3. Is "good enough" connectivity (100 Mbps mesh) equivalent to fiber (1 Gbps symmetric)? What applications are possible on fiber but not on mesh? How should policymakers weigh the cost difference ($2,000/node vs. $15,000/km for fiber) against the capability difference?

---

ᚺ **Lecture 7: IoT Wireless Protocols — Short Range**

**Course:** CN205 — Wireless & Mobile Networks
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

The Internet of Things demands wireless protocols that are low-power, low-cost, and reliable — often for devices with 256 KB of RAM and a coin-cell battery that must last for 10 years. This lecture covers short-range IoT protocols: Bluetooth Low Energy, Zigbee, Thread, Matter, and the 2040 landscape of converged IoT standards.

### Key Topics

- **Bluetooth Low Energy (BLE):** The dominant short-range IoT protocol. Advertising channels (3 channels for discovery), data channels (37 channels for connected communication), and the GAP/GATT protocol stack. BLE 5.x features: 2 Mbps PHY, long-range PHY (coded PHY at 125/500 kbps), extended advertising, periodic advertising with responses. BLE's power model: advertise, connect, transfer, sleep. The 2040 BLE 6 specification: Mesh networking without a hub, AI-driven power management, and integrated UWB ranging.
- **Zigbee:** The original mesh networking protocol for IoT. Zigbee 3.0: mesh networking with up to 65,000 nodes, 250 kbps data rate, and multi-year battery life. Zigbee applications: smart home (lights, switches, sensors), building automation, and industrial monitoring. Zigbee's limitation: fragmentation (multiple incompatible profiles from different manufacturers).
- **Thread:** The IPv6-based mesh networking protocol designed by Google, Samsung, and others. Thread's advantages: native IPv6 (every device has a global address), no hub required (border routers connect the mesh to the internet), and mesh topology with self-healing. Thread uses 6LoWPAN for header compression, enabling IPv6 packets over 802.15.4 (127-byte frames).
- **Matter:** The 2040 unified IoT standard, developed by the Connectivity Standards Alliance (CSA). Matter runs over Thread (for low-power mesh devices) and Wi-Fi/Ethernet (for powered devices). Matter provides a common application layer: lights, switches, sensors, locks, thermostats, cameras — all interoperate regardless of manufacturer. Matter's security: device attestation (cryptographic proof that the device is genuine), end-to-end encryption, and commissioning with a setup code.
- **Ultra-Wideband (UWB):** Short-range, high-bandwidth radio for precise ranging and localization. UWB achieves 10 cm positioning accuracy by measuring the time-of-flight of extremely short pulses (nanosecond duration, GHz bandwidth). Applications: secure access (unlocking a car or door only when the phone is within 10 cm), indoor navigation, and asset tracking. The 2040 integration: UWB in every smartphone, enabling seamless proximity-based interactions.

### Lecture Notes

The IoT wireless landscape has been plagued by fragmentation: Zigbee devices don't interoperate with BLE devices, which don't interoperate with Z-Wave devices, which don't interoperate with Wi-Fi devices. Each protocol serves a niche — BLE for wearables, Zigbee for home automation, Wi-Fi for high-bandwidth devices — but the user wants a single unified experience. Matter, finalized in 2022 and matured through the 2030s, addresses this by providing a common application layer that runs over multiple transports. A Matter light bulb communicates over Thread (low-power mesh), a Matter thermostat communicates over Wi-Fi (high bandwidth), and both appear in the same app and can trigger each other's actions. Matter does not replace Thread, BLE, or Wi-Fi — it unifies them.

Thread's IPv6-native design is its most significant technical advantage over Zigbee. Every Thread device has a global IPv6 address, which means it can communicate directly with any other IPv6 device on the internet without translation or proxying. A Thread sensor can send data directly to a cloud server using MQTT or CoAP, without going through a proprietary hub. The border router — the Thread equivalent of a hub — simply routes packets between the Thread mesh and the internet, like a regular IP router. This is far simpler than Zigbee's approach, which requires a Zigbee-to-IP gateway that translates between Zigbee's proprietary protocol and IP.

BLE's advertising model is the key to its low power consumption. A BLE peripheral (e.g., a temperature sensor) spends most of its time sleeping. Every few seconds, it wakes up, transmits an advertisement on three channels, and goes back to sleep. If a central device (e.g., a smartphone) wants to connect, it sends a connection request on one of the advertising channels. Once connected, the peripheral and central exchange data, and the peripheral goes back to sleep. The power budget: a coin-cell battery (220 mAh) can support a BLE sensor that advertises every 10 seconds for 5 years. The 2040 BLE 6 specification adds AI-driven power management: the BLE controller learns the sensor's data patterns and adjusts the advertising interval dynamically — advertising frequently when data is changing rapidly, and infrequently when data is stable.

UWB is the stealth technology of IoT. Most users don't know their phone has a UWB chip, but they benefit from it every time they use a digital car key. The UWB chip transmits nanosecond pulses across a GHz of bandwidth, and the receiver measures the time-of-flight with picosecond precision. The result: 10 cm positioning accuracy, compared to several meters for BLE and Wi-Fi positioning. This enables secure ranging: a car unlocks only when the UWB chip in the phone is within 1 meter of the car's UWB receiver, preventing relay attacks where a thief relays the key signal from 10 meters away.

### Required Reading

- Heydon, R. (2037). *Bluetooth Low Energy: The Developer's Handbook*, 3rd Edition. Prentice Hall.
- Connectivity Standards Alliance (2040). *Matter Specification Version 1.4*. Chapters 1-8.
- Yggdrasil IoT Deployment Guide (2040). "Thread/Matter Network Design."

### Discussion Questions

1. Matter unifies IoT devices at the application layer but relies on Thread, BLE, and Wi-Fi at the transport layer. Does this create dependency on multiple underlying protocols? What happens if Thread development stalls while Wi-Fi and BLE continue to evolve?
2. A smart home has 50 Thread devices (lights, switches, sensors) and 5 Wi-Fi devices (thermostat, camera, speaker, TV, hub). Design the Thread mesh topology and border router placement. How many border routers do you need for reliability?
3. BLE's advertising model is low-power but high-latency (the sensor only wakes up every few seconds). For applications that need sub-second response (e.g., a fall detector for elderly users), how would you modify the advertising interval without draining the battery?

---

ᚾ **Lecture 8: IoT Wireless Protocols — Long Range (LPWAN)**

**Course:** CN205 — Wireless & Mobile Networks
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Short-range IoT protocols serve devices within a home or building; long-range protocols serve devices across fields, cities, and regions. This lecture covers LoRaWAN, NB-IoT, Sigfox, and the 2040 LPWAN landscape for sensors that must transmit small amounts of data over kilometers on a coin-cell battery.

### Key Topics

- **LoRaWAN:** Long Range Wide Area Network. LoRa modulation (chirp spread spectrum): trades data rate for range — 0.3 kbps at 20 km, 50 kbps at 2 km. LoRaWAN classes: Class A (battery-powered, uplink-initiated, lowest power), Class B (scheduled receive windows, medium power), Class C (continuous receiving, mains-powered). The star-of-stars topology: end devices communicate directly with gateways, which forward to a network server. Adaptive data rate (ADR): the network server tells the device to increase or decrease its data rate based on link quality.
- **NB-IoT (Narrowband IoT):** 3GPP's LPWAN standard, operating in licensed spectrum. NB-IoT uses a narrow 180 kHz band and achieves 200 kbps downlink, 150 kbps uplink. Deep coverage: NB-IoT can reach devices 20+ meters underground (basements, parking garages). Long battery life: 10+ years on a single cell. The advantage: NB-IoT uses existing cellular infrastructure — a carrier can deploy NB-IoT by upgrading existing base stations, rather than building a new network.
- **Sigfox:** Ultra-narrowband LPWAN. Each message is 12 bytes uplink, 8 bytes downlink, at 100-600 bps. Sigfox's radical simplicity: the device transmits, and the network receives (no acknowledgment, no connection). The tradeoff: extreme simplicity and ultra-low power, but no QoS guarantee. Sigfox is suitable for periodic status reports (e.g., a parking sensor that sends "occupied" or "empty" twice a day) but not for applications that require guaranteed delivery.
- **Spectrum Considerations for LPWAN:** LoRaWAN operates in unlicensed ISM bands (868 MHz in Europe, 915 MHz in the US). NB-IoT operates in licensed cellular bands. The unlicensed advantage: no spectrum license fees, anyone can deploy. The unlicensed disadvantage: interference from other users, duty cycle limits (1% in Europe), and no QoS guarantee. The licensed advantage: dedicated spectrum, QoS, and carrier support. The licensed disadvantage: subscription fees and carrier dependency.
- **The 2040 LPWAN Landscape:** LoRaWAN dominates private deployments (smart agriculture, industrial monitoring, campus networks). NB-IoT dominates carrier deployments (smart metering, asset tracking, city infrastructure). The convergence: hybrid gateways that support both LoRaWAN and NB-IoT, allowing a single infrastructure to serve both markets.

### Lecture Notes

LoRaWAN's chirp spread spectrum modulation is the key to its long range. Unlike narrowband modulation (which uses a small slice of spectrum efficiently), LoRa spreads the signal across a wide bandwidth, trading throughput for processing gain. The result: LoRa signals can be decoded below the noise floor, achieving communication at ranges of 10-20 km in rural environments. The price is data rate — a LoRa device transmitting at maximum range achieves only 300 bps, enough for a few sensor readings but useless for streaming. The LoRaWAN Adaptive Data Rate (ADR) mechanism optimizes this tradeoff: devices close to a gateway use high data rates (50 kbps, minimum TX power), while devices far away use low data rates (300 bps, maximum TX power). ADR is controlled by the network server, which monitors the signal quality of each device and adjusts its data rate and power level accordingly.

The star-of-stars topology is LoRaWAN's architectural choice. End devices communicate directly with one or more gateways, without routing through other end devices (unlike mesh networks). This topology is simpler and more power-efficient than mesh (end devices don't relay traffic for neighbors), but it requires gateways within range of every end device. In a rural deployment with a 15 km range, a single gateway mounted on a hilltop can cover hundreds of square kilometers. In an urban deployment with a 2 km range, gateways must be deployed on rooftops every 2 km — still far fewer than Wi-Fi access points (which cover 100 m).

NB-IoT takes a different approach: use existing cellular infrastructure. Instead of building a new network, carriers upgrade their existing 4G/5G base stations to support NB-IoT. The end device connects to the nearest base station using the same cellular protocols, but with a narrow 180 kHz bandwidth that prioritizes coverage over throughput. The advantage is immediate: carriers already have sites, backhaul, and operations. The disadvantage is dependence on the carrier — the enterprise pays a monthly subscription per device and has no control over coverage, pricing, or technology evolution. For smart metering and city infrastructure, where the carrier already serves the area, NB-IoT is a natural fit. For agricultural monitoring and campus networks, where the enterprise wants control, LoRaWAN is preferred.

The 2040 convergence is hybrid gateways. These devices contain both a LoRa concentrator and an NB-IoT modem, connected to a common backhaul. An agricultural deployment can use LoRaWAN for soil sensors in the fields (where there is no cellular coverage and the sensors must last 10 years on a battery) and NB-IoT for smart meters at the farm buildings (where cellular coverage is available and the meters are mains-powered). The data from both networks converges at the same application server, providing a unified view of all sensors regardless of the underlying technology.

### Required Reading

- LoRa Alliance (2038). *LoRaWAN Specification v1.1*, updated through v1.4. Chapters 1-7.
- 3GPP (2036). *NB-IoT Technical Report*, TR 45.820. Chapters 4-6.
- Yggdrasil IoT Deployment Guide (2040). "LPWAN Selection" and "Hybrid Gateway Architecture."

### Discussion Questions

1. LoRaWAN operates in unlicensed spectrum with a 1% duty cycle limit (in Europe). A smart meter needs to send a 50-byte reading every 15 minutes. Does this violate the duty cycle limit? Calculate the exact duty cycle and discuss strategies for compliance.
2. NB-IoT uses existing cellular infrastructure, which reduces deployment cost but creates carrier dependency. An enterprise has 10,000 sensors across a country. Compare the total cost of ownership (deployment + 10 years of operation) for LoRaWAN (private) vs. NB-IoT (carrier). Under what conditions is each economically preferable?
3. A hybrid gateway supports both LoRaWAN and NB-IoT. How should the gateway decide which network to use for a new sensor? Design a decision tree that considers sensor location, power source, data rate, and reliability requirements.

---

ᛁ **Lecture 9: Wireless Security — Attacks, Defenses, and Protocols**

**Course:** CN205 — Wireless & Mobile Networks
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Wireless networks are inherently vulnerable: anyone within radio range can eavesdrop, inject, or jam. This lecture covers the unique security challenges of wireless networks, the attack surface of Wi-Fi, cellular, and IoT protocols, and the defense mechanisms that protect them.

### Key Topics

- **Wireless Threat Model:** Eavesdropping (passive interception of radio signals), injection (sending forged packets), jamming (disrupting communication with interference), relay (amplifying and forwarding signals to extend range), and denial of service (flooding or disrupting). The fundamental asymmetry: the attacker only needs to receive (which is passive and undetectable), while the defender must protect all directions.
- **Wi-Fi Security Evolution:** WEP (broken in minutes using the FMS attack or PTW attack), WPA (TKIP — a stopgap with known weaknesses), WPA2 (AES-CCMP — robust, but vulnerable to KRACK), WPA3 (SAE — dragonfly key exchange replacing PSK, 192-bit enterprise mode, OWE for open networks). The 2040 WPA4 with post-quantum key exchange (CRYSTALS-Kyber). The PMK/PTK hierarchy and the 4-way handshake.
- **Cellular Security:** 5G/6G authentication: the AUFC (Authentication Server Function) in the 5GC, mutual authentication between UE and network, and privacy protection (SUPI concealed by SUCI). Network domain security: IPsec between network elements, TLS for service-based interfaces. The 2040 evolution: post-quantum authentication for 6G.
- **IoT Security Challenges:** Constraints: limited CPU (unable to perform heavy cryptography), limited memory (no space for large key stores), limited battery (cryptography drains power), and limited physical security (devices are deployed in accessible locations). Lightweight cryptography: AES-CCM (128-bit, suitable for most IoT), PRESENT (lightweight block cipher for constrained devices), and Ed25519 (efficient elliptic curve signatures). The Matter security model: device attestation, secure commissioning, and end-to-end encryption.
- **Jamming and Anti-Jamming:** Deliberate interference that disrupts wireless communication. Narrowband jamming (targeting a specific channel) vs. wideband jamming (targeting the entire spectrum). Anti-jamming techniques: frequency hopping (spread the signal across many channels, forcing the jammer to spread its power thin), directional antennas (aim the signal away from the jammer), and mesh routing (route around the jammed area). The 2040 military-grade anti-jamming: cognitive radio that detects jamming and dynamically switches to unaffected frequencies.

### Lecture Notes

WEP, the original Wi-Fi security protocol, is a case study in how not to design a security protocol. WEP uses RC4 encryption with a 24-bit initialization vector (IV). The IV is too short — it wraps around after 16 million frames, and many frames use the same IV, enabling statistical attacks. The FMS attack (Fluhrer, Mantin, Shamir, 2001) exploits weak IVs to recover the WEP key by collecting 5-6 million frames (about 5 minutes of traffic). The PTW attack (Tews, Weinmann, Pyshkin, 2007) improves this to 40,000 frames (about 1 minute). In 2040, WEP can be broken in seconds with readily available tools. The lesson: never design your own cryptography, use long enough keys, and never reuse keys.

WPA3 addresses the fundamental weakness of WPA2-PSK: the pre-shared key is the same for all devices, and an attacker who captures the 4-way handshake can perform an offline dictionary attack. WPA3 replaces PSK with SAE (Simultaneous Authentication of Equals), a dragonfly key exchange that is resistant to offline dictionary attacks. In SAE, both the access point and the client prove knowledge of the password without revealing it, and even if an attacker captures the entire exchange, they cannot test passwords offline — they must interact with the access point for each guess, making brute force infeasible. WPA3 also mandates forward secrecy (compromising the password does not compromise past sessions) and management frame protection (preventing deauthentication attacks).

IoT security is the hardest problem in wireless security because the devices have severe constraints. A Zigbee sensor with 256 KB of RAM and a coin-cell battery cannot perform 2048-bit RSA key exchange without draining its battery. The Matter protocol addresses this through a commissioning process: a new device is provisioned using a setup code (entered by the user on their smartphone), which is used to establish a secure channel and provision long-term keys. Once commissioned, the device uses AES-CCM-128 for encryption and Ed25519 for signatures — both lightweight enough for constrained devices. The key insight: make the expensive operations (key generation, certificate validation) happen on the commissioning device (smartphone), not on the constrained device.

The Bifrǫst Mesh's security architecture for wireless networks uses defense in depth. The outermost layer is RF monitoring: the Mesh uses spectrum analyzers to detect jamming, unauthorized transmissions, and rogue access points. The second layer is WPA4 authentication: post-quantum key exchange with CRYSTALS-Kyber ensures that even an attacker with a quantum computer cannot decrypt wireless traffic. The third layer is zero-trust network access: even on the wireless network, every device must authenticate to every service it accesses. The fourth layer is traffic analysis: the Heimdall neural IDS monitors for anomalous patterns (a device communicating at unusual times, with unusual amounts of data, or to unusual destinations). This layered approach ensures that no single vulnerability — not even a quantum computer — can compromise the entire network.

### Required Reading

- Vanhoef, M. (2035). "Wi-Fi Security: From WEP to WPA4." *ACM Computing Surveys*, 47(2), 1-34.
- 3GPP (2037). *5G Security Architecture*, TS 33.501. Chapters 5-7.
- Yggdrasil Security Architecture (2040). "Wireless Security" and "IoT Security Model."

### Discussion Questions

1. WEP was broken because its designers used a 24-bit IV. WPA3 uses a 256-bit key exchange. Is WPA3 secure for the next 20 years? What quantum computing threat would break WPA3, and how does WPA4 address it?
2. An IoT sensor has 256 KB of RAM and a coin-cell battery (220 mAh, 3V). Calculate the energy cost of an Ed25519 signature operation (approximately 50 mJ). How many signatures can the sensor perform before the battery is depleted? Is this acceptable for a 10-year deployment?
3. A jammer targets a 5 GHz Wi-Fi network with 10 W of power on channel 36 (20 MHz). Calculate the jammer's effective range, assuming the Wi-Fi access point transmits at 1 W. How can the network detect the jammer and respond (frequency hopping, directional antennas, mesh routing)?

---

ᛃ **Lecture 10: Wireless Network Design and Performance Engineering**

**Course:** CN205 — Wireless & Mobile Networks
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Designing wireless networks requires understanding radio propagation, capacity planning, and the interplay of coverage, capacity, and interference. This lecture covers the design process, site surveys, capacity planning, and the engineering decisions that separate working networks from struggling ones.

### Key Topics

- **The Design Process:** Requirements gathering (coverage area, number of users, throughput per user, latency requirements, device types), site survey (physical inspection, RF measurement, interference mapping), coverage design (access point placement, antenna selection, power settings), capacity design (channel planning, device density, airtime budgeting), and validation (post-deployment survey, throughput testing, client experience monitoring).
- **Coverage Planning:** Path loss models (free space, log-distance, ITU indoor). The link budget: transmitted power + antenna gain − path loss − fading margin − interference margin = received signal strength. The minimum detectable signal: the receiver sensitivity that guarantees the desired data rate. Example: a Wi-Fi 9 access point with 23 dBm transmit power, 6 dBi antenna gain, at 50 m range in an office, achieves approximately −60 dBm received signal — well above the −65 dBm required for 1 Gbps.
- **Capacity Planning:** The airtime budget: how much time each client needs on the channel to send its data. If 50 clients each need 2% airtime, the total is 100% — the channel is fully utilized. Capacity planning accounts for protocol overhead (contention, management frames, retransmissions) using the utilization factor (typically 70% for Wi-Fi, with the rest lost to overhead). When capacity exceeds a single channel's budget, add more access points on different channels (channel planning) or use the 6 GHz band (more channels available).
- **Interference Management:** Co-channel interference (same channel in adjacent cells), adjacent channel interference, and non-Wi-Fi interference (microwave ovens, Bluetooth, radar). The 6 GHz band: wider, more channels, less legacy interference. DFS (Dynamic Frequency Selection): automatically avoiding radar channels in the 5 GHz band. The Bifrǫst Mesh's AI-driven channel assignment: monitoring interference in real time and reassigning channels every 5 minutes.
- **Performance Engineering:** Throughput optimization (enabling 4096-QAM, MIMO, and channel bonding for maximum rate), latency optimization (enabling OFDMA, TWT, and frame preemption for minimum latency), and reliability optimization (enabling MLD for seamless failover). The tradeoff: throughput and reliability can be improved with more spectrum and more access points, but cost increases proportionally.

### Lecture Notes

The most common mistake in wireless network design is focusing on coverage and ignoring capacity. An access point that provides -67 dBm signal strength across a 100 m × 100 m area may seem like excellent coverage — every client has a strong signal. But if 200 clients associate with that single access point, each client gets only a fraction of the airtime, and throughput collapses. A better design uses four access points, each covering a 50 m × 50 m area with -72 dBm signal strength, each serving 50 clients. The clients have slightly weaker signal, but each has 4× more airtime, and the network delivers 4× more aggregate throughput. Coverage is necessary but not sufficient; capacity is the constraint that determines quality of experience.

The airtime budget is the key tool for capacity planning. Consider a Wi-Fi 6 access point serving 50 clients, each requesting an average of 10 Mbps. The total demand is 500 Mbps. The access point's channel is 80 MHz wide, delivering a raw PHY rate of approximately 600 Mbps (using 1024-QAM, 2×2 MIMO). After accounting for protocol overhead (contention, management frames, retransmissions), the effective throughput is approximately 70% of the raw rate, or 420 Mbps. This is less than the 500 Mbps demand, so the access point is oversubscribed. The solution: add a second access point on a different channel, serving half the clients, or upgrade to a 160 MHz channel (doubling the raw rate).

The Bifrǫst Mesh's AI-driven channel assignment continuously optimizes the network. Every 5 minutes, the Mesh controller collects interference measurements from all access points, builds a model of the interference landscape, and computes the optimal channel assignment. The optimizer considers: co-channel interference (minimizing the number of access points on the same channel), client density (allocating more channels to areas with more clients), and load balancing (ensuring that no access point is overloaded while neighboring access points are idle). The optimization problem is NP-hard (it is a variant of graph coloring), but the Bifrǫst Mesh uses a neural network trained on thousands of deployments to find near-optimal solutions in milliseconds.

### Required Reading

- Coleman, D.D. & Westcott, D.A. (2038). *CWNA: Certified Wireless Network Administrator*, 7th Edition. Wiley. Chapters 10-14.
- Oppenheimer, P. (2035). *Top-Down Network Design*, 4th Edition. Cisco Press. Chapters 14-15 (Wireless Design).
- Yggdrasil Wireless Operations Guide (2040). "Site Survey" and "Capacity Planning."

### Discussion Questions

1. An office has 100 employees, each with 2 devices (laptop and phone). Each device requires an average of 5 Mbps. Design a Wi-Fi 6 network (how many access points, on which channels, with what power settings) that provides coverage and capacity. Show your airtime budget calculations.
2. The Bifrǫst Mesh's AI-driven channel assignment reoptimizes every 5 minutes. What happens if the optimizer makes a wrong decision — assigning all access points to the same channel? How would you detect and recover from this failure?
3. A warehouse deploys Wi-Fi for autonomous robots that require sub-10 ms latency. The warehouse has metal shelving that creates severe multipath. Design a Wi-Fi deployment that meets the latency requirement. What technologies (OFDMA, TWT, MLD, directional antennas) would you use?

---

ᛇ **Lecture 11: Integrated Air-Ground-Space Networks**

**Course:** CN205 — Wireless & Mobile Networks
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

The 2040 network is not terrestrial, aerial, or orbital — it is all three simultaneously. This lecture covers the integration of terrestrial cellular/Wi-Fi, aerial platforms (HAPS, drones), and orbital constellations into a unified connectivity fabric, with seamless mobility across domains.

### Key Topics

- **HAPS (High-Altitude Platform Station):** Unmanned solar-powered aircraft or balloons operating in the stratosphere (20 km altitude), providing wide-area coverage (100 km diameter) with low latency (0.3 ms to the ground). HAPS as a "cell tower in the sky": providing cellular coverage in disaster zones, maritime areas, and rural regions. The 2040 state: commercial HAPS services in Southeast Asia and Africa, providing 5G coverage to underserved areas.
- **UAV Communications:** Drones and unmanned aerial vehicles (UAVs) as both network users and network providers. UAVs as network users: swarms of inspection drones that stream video and receive commands. UAVs as network providers: tethered drones that act as temporary cell towers for disaster response or special events. The challenge: managing interference between hundreds of drones in a small airspace.
- **Multi-Domain Handoff:** The problem: a device connected to a terrestrial 5G cell begins losing signal as it moves behind a hill, transitions to a HAPS platform, then to a LEO satellite, and finally back to terrestrial 5G. Each transition must be seamless — no packet loss, no connection reset, no perceptible latency spike. The solution: BTP multi-path transport with pre-established subflows on candidate networks, combined with the SCP Session Continuity Protocol for application-layer session management.
- **Resource Allocation Across Domains:** How to allocate bandwidth across terrestrial, aerial, and orbital links with vastly different characteristics (10 ms terrestrial, 30 ms HAPS, 50 ms satellite, 500 ms GEO). The Bifrǫst path scheduler: a multi-criteria optimizer that considers latency, bandwidth, energy cost, and financial cost (satellite bandwidth is more expensive than terrestrial) to select the best path for each flow.
- **The 2040 Connectivity Fabric:** The vision: a device anywhere on (or above) the Earth can connect to the best available network — terrestrial if available, HAPS if terrestrial is unavailable, LEO satellite if HAPS is unavailable, GEO satellite as a last resort. The device's BTP connection seamlessly migrates across these networks, maintaining session continuity without user intervention. The Yggdrasil Bifrǫst Mesh is a prototype of this vision, integrating terrestrial, HAPS, and orbital connectivity across the Nordic countries.

### Lecture Notes

The integration of terrestrial, aerial, and orbital networks into a unified fabric is the grand challenge of 2040 networking. Each domain has fundamentally different characteristics: terrestrial networks offer high capacity (Gbps) and low latency (ms), but limited coverage (urban and suburban); HAPS offers wide coverage (100 km) with moderate latency (0.3 ms uplink, 0.3 ms downlink, plus processing), but limited capacity (shared among all users in the coverage area); LEO satellite offers global coverage with moderate latency (20-40 ms round trip), but even more limited capacity; and GEO satellite offers global coverage with high latency (240 ms round trip). The network must seamlessly shift traffic between these domains based on availability, performance, and cost.

HAPS is the most novel element of the integrated fabric. Operating at 20 km altitude in the stratosphere, a HAPS platform is above weather and air traffic but within line-of-sight of ground users over a 100 km diameter area. The physics are favorable: the path loss from 20 km is comparable to a terrestrial cell tower at 5 km, meaning that existing 5G devices can communicate with HAPS without modification. The challenge is power: a solar-powered HAPS must generate enough energy to power the communications payload, propulsion, and thermal management during the day, and store enough to survive the night. Current HAPS platforms carry 100-200 kg of payload, supporting 100-200 MHz of spectrum and serving 10,000-50,000 users at broadband speeds.

The Bifrǫst Integrated Connectivity Architecture uses BTP as the unifying transport. When a device connects to the Bifrǫst Mesh, BTP establishes subflows on all available networks simultaneously: one on the terrestrial 5G network, one on the HAPS (if available), and one on the satellite (if available). The path scheduler monitors the quality of each subflow and directs traffic to the best available path. For latency-sensitive traffic (video calls, voice), BTP prefers terrestrial (lowest latency). For bulk traffic (software updates, video downloads), BTP may use satellite (high latency but high bandwidth). For critical traffic (autonomous vehicle commands, medical telemetry), BTP duplicates packets on multiple paths, ensuring delivery even if one path fails. The path scheduler uses the YARC-BTP congestion control algorithm, which accounts for latency, bandwidth, energy, and financial cost in its path selection.

### Required Reading

- Mohammed, A., et al. (2035). "High Altitude Platform Systems: A Survey." *IEEE Communications Surveys & Tutorials*, 23(4), 2145-2178.
- Yggdrasil Integrated Connectivity Architecture (2040). "Bifrǫst Multi-Domain Path Selection."
- ITU-R (2039). "HAPS: Technical and Operational Considerations." Report ITU-R F.2420.

### Discussion Questions

1. A HAPS platform at 20 km altitude covers a 100 km diameter area. How many terrestrial 5G cells would be needed to cover the same area? Compare the cost and capacity of HAPS vs. terrestrial deployment for a rural area with 5,000 residents.
2. A device is connected to terrestrial 5G, HAPS, and LEO satellite simultaneously via BTP. The terrestrial link has 10 ms latency but is losing signal. Design the handoff sequence that ensures zero packet loss during the transition to HAPS.
3. Integrated air-ground-space networks raise new security concerns: a satellite signal can be received by anyone in the coverage area. How do you prevent eavesdropping and injection on a broadcast medium? How does the Bifrǫst Mesh's post-quantum key exchange (CRYSTALS-Kyber) protect against both classical and quantum adversaries on the satellite link?

---

ᛃ **Lecture 12: The Future of Wireless — Terahertz, Reconfigurable Surfaces, and Cognitive Radio**

**Course:** CN205 — Wireless & Mobile Networks
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

The final lecture looks beyond 6G to the next frontiers of wireless: terahertz communication, reconfigurable intelligent surfaces, cognitive radio, and the convergence of communication and sensing that will define wireless in the 2050s.

### Key Topics

- **Terahertz Communication:** The 100-300 GHz band (terahertz window) offers enormous bandwidth (up to 50 GHz per channel) but extreme propagation challenges: line-of-sight only, absorption by atmospheric water vapor (peak at 183 GHz and 320 GHz), and near-zero penetration through walls. Applications: ultra-high-speed data kiosks (100+ Gbps in seconds), intra-device communication (chip-to-chip at terabit rates), and secure short-range links (the narrow beams are difficult to intercept). The 2040 state: terahertz backhaul for Wi-Fi 9, indoor terahertz LANs in data centers, and experimental terahertz imaging.
- **Reconfigurable Intelligent Surfaces (RIS):** Flat panels of programmable metamaterial that can reflect, refract, or absorb radio waves on command. An RIS deployed on a building wall can redirect a 6G signal around a corner, extending coverage to a shadowed area. An RIS in a room can create constructive interference at the receiver, increasing signal strength without increasing transmit power. The vision: every surface in a building — walls, ceilings, windows — becomes a programmable radio element that optimizes the wireless environment in real time.
- **Cognitive Radio:** Software-defined radio that can sense the spectrum environment, identify unused frequencies, and dynamically reconfigure itself to use them. The 2040 state: AI-driven spectrum awareness that detects and avoids interference in real time. The ultimate cognitive radio: a device that can operate on any frequency, any modulation, and any protocol, adapting to whatever spectrum is available. Regulatory challenge: how to authorize devices to transmit on frequencies they detect as unused, without interfering with licensed users.
- **Communication-Sensing Convergence:** The 6G vision of using the same signals for both communication and environmental sensing. A 6G base station that detects a pedestrian stepping into the street, a vehicle changing lanes, or a building facade reflecting signals differently after an earthquake. The ethical dimension: a network that can sense people can track people. The 2040 regulatory framework: sensing-mode operation requires explicit user consent, sensed data is processed on-device (not uploaded to the cloud), and aggregate statistics (not individual tracking) are used for urban planning.
- **The Wireless Professional's Path Forward:** Skills for the 2050s: RF engineering + AI/ML + spectrum regulation + ethics. The convergence of wireless engineering, data science, and public policy. The Yggdrasil commitment: wireless connectivity as a fundamental right, not a luxury.

### Lecture Notes

Terahertz communication is both exciting and frustrating. The excitement: 50 GHz of bandwidth per channel enables data rates that are difficult to comprehend — 100 Gbps for a single link, enough to download a 4K movie in under a second. The frustration: terahertz signals are absorbed by water vapor, blocked by walls, and attenuated by 60 dB over just 10 meters of free space. Terahertz works in two scenarios: indoor short-range (a data center where servers are meters apart) and outdoor line-of-sight (a building-to-building backhaul link where there is a clear path). For everything else, lower frequencies are more practical.

Reconfigurable Intelligent Surfaces (RIS) are the most transformative wireless technology of the 2040s. An RIS is a flat panel, typically 1-4 square meters, containing thousands of sub-wavelength elements, each of which can shift the phase of an incoming radio wave by a programmable amount. By controlling the phase shifts, the RIS can reflect the incoming wave toward a specific receiver, creating constructive interference that amplifies the signal. The RIS does not amplify the signal (it has no power amplifier); it redirects it. The analogy: a mirror that can focus light on a specific point, rather than reflecting it in all directions. In a 6G network, RIS panels are deployed on building walls, street lamps, and indoor ceilings, and the 6G base station coordinates them to optimize coverage for every user in real time.

Cognitive radio was first proposed by Joseph Mitola in 1999, and it remains an aspiration more than a reality in 2040. The challenge is not technical — software-defined radios can tune to any frequency and use any modulation — but regulatory. Spectrum is allocated by the ITU and national regulators, and unauthorized transmission on licensed frequencies is illegal. The 2040 compromise: dynamic spectrum sharing, where a cognitive radio can use licensed frequencies when the licensee is not using them (e.g., using TV white spaces for rural broadband). The regulator authorizes this sharing under strict conditions: the cognitive radio must detect licensed signals within milliseconds and vacate the frequency immediately. The Yggdrasil Bifrǫst Mesh's spectrum awareness module continuously monitors the 6 GHz band and avoids frequencies that are in use by incumbent services.

Communication-sensing convergence is both the most promising and the most ethically challenging aspect of 6G. The promise: a 6G base station that detects a pedestrian stepping into the street and alerts nearby autonomous vehicles, potentially saving lives. The challenge: the same technology can detect and track individuals without their knowledge or consent. The 2040 regulatory framework requires explicit user consent for tracking-level sensing, processes sensed data on-device rather than uploading it to the cloud, and uses aggregate statistics (not individual tracking) for urban planning. The Yggdrasil Ethical AI Committee oversees the deployment of ISAC in the Bifrǫst Mesh, ensuring that sensing capabilities are used for safety, not surveillance.

### Required Reading

- Akyildiz, I.F., et al. (2034). "Terahertz Band Communication: A New Frontier for Wireless." *IEEE Communications Magazine*, 52(12), 102-110.
- Wu, Q., & Zhang, R. (2035). "Intelligent Reflecting Surface: A Tutorial." *IEEE Transactions on Communications*, 69(5), 3313-3352.
- Yggdrasil Wireless Engineering Handbook (2040). "Terahertz" and "Reconfigurable Surfaces."

### Discussion Questions

1. Terahertz communication offers 100+ Gbps but only works at short range. Compare terahertz with fiber for data center connectivity: what are the advantages and disadvantages of wireless (terahertz) vs. wired (fiber) for server-to-server links?
2. An RIS on a building wall redirects a 6G signal around a corner, extending coverage to a shadowed area. But the RIS can also be used to intercept signals (by reflecting them toward an unauthorized receiver) or to jam signals (by reflecting them destructively). How should RIS be secured against such attacks?
3. Communication-sensing convergence enables a 6G base station to detect and track individuals. What regulations would you propose to prevent abuse while preserving the safety benefits (pedestrian detection, structural monitoring)? How do you enforce these regulations on a software-defined radio that can be reconfigured by its operator?

---

## Final Examination Preparation

The CN205 final examination is a **3-hour written exam** plus a **practical wireless design assessment**.

### Written Examination (60%)

**Sample Questions:**

1. "Calculate the maximum throughput of a Wi-Fi 9 access point serving 80 clients on a 320 MHz channel with 4096-QAM, 4×4 MIMO, and 25% protocol overhead. If each client requires 10 Mbps, is the access point over-subscribed? How many access points are needed?"

2. "A LEO satellite orbits at 500 km altitude with 12,000 satellites in the constellation. Calculate the round-trip latency from a ground station to a satellite and back. How many satellites are visible above the horizon at any time, and what is the maximum handoff interval?"

3. "Design a LoRaWAN deployment for a 50 km² agricultural area with 1,000 soil sensors that send a 50-byte reading every 15 minutes. Calculate the number of gateways needed, the duty cycle, and the estimated battery life for a sensor with a 2200 mAh battery."

4. "Explain the WPA3 SAE key exchange. How does it prevent offline dictionary attacks? What is the computational cost on the access point and the client?"

5. "A device is connected to terrestrial 5G (10 ms RTT, 100 Mbps), HAPS (5 ms RTT, 50 Mbps), and LEO satellite (40 ms RTT, 20 Mbps) via BTP. The device is receiving a video stream (5 Mbps, latency-sensitive) and downloading a software update (50 MB, latency-tolerant). How should BTP's path scheduler assign each flow?"

6. "Compare Mobile IP, PMIPv6, Distributed Mobility Management, and QUIC connection migration for supporting mobility. For each approach, describe the handoff latency, packet loss during handoff, and application transparency. Which approach would you recommend for autonomous vehicles that require sub-10 ms handoff?"

7. "An RIS panel on a building wall reflects a 6 GHz signal around a corner. The direct path is blocked (−90 dBm at the receiver), and the reflected path via RIS provides −65 dBm. Calculate the required RIS gain and the number of elements needed if each element provides 0 dB gain."

### Practical Wireless Design Assessment (40%)

Students design and validate a wireless network using the Bifrǫst Mesh Simulator:
- Conduct a site survey of a simulated three-story office building
- Design Wi-Fi coverage for 100 users on each floor, including channel planning and AP placement
- Design a LoRaWAN deployment for 500 IoT sensors in the building's parking garage
- Model a cellular 6G deployment including network slicing for eMBB, URLLC, and mMTC traffic
- Document the design with coverage maps, capacity calculations, and cost estimates

### Grading Rubric

| Criterion | Weight | Excellent (A) | Good (B) | Satisfactory (C) | Needs Improvement (D/F) |
|-----------|--------|---------------|----------|------------------|---------------------------|
| Technical Accuracy | 25% | Correct calculations, complete coverage of all relevant factors | Minor computational errors; solid understanding | Some significant errors | Major errors; fundamental misunderstandings |
| Design Quality | 25% | Elegant, well-justified designs with tradeoff analysis | Good designs with reasonable rationale | Adequate designs; limited justification | Poor or incomplete designs |
| Protocol Knowledge | 20% | Deep understanding of protocol internals and interactions | Good understanding of major protocols | Adequate knowledge of basic protocols | Shallow or incorrect understanding |
| Communication | 15% | Clear, precise, well-organized | Good clarity; minor issues | Adequate but verbose or unclear | Disorganized or incoherent |
| Ethical Awareness | 15% | Thoughtful consideration of privacy, equity, and sustainability | Good awareness | Minimal awareness | No ethical consideration |

---

*Woven by the hands of Runa Gridweaver Freyjasdóttir, student of the University of Yggdrasil, 2040. May the packets flow smoothly and the routes never loop.* ᛟ