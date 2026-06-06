# CN203: Transport & Application Layer Protocols
## Bachelor of Science in Computer Networking — University of Yggdrasil, 2040

**Credits:** 4  
**Prerequisites:** CN101 Introduction to Computer Networking, CN102 OSI Model & TCP/IP Architecture  
**Description:** A rigorous exploration of the transport and application layers of the networking stack — from the venerable TCP three-way handshake and UDP's fire-and-forget model to the 2040 dominance of QUIC as the default transport and HTTP/3 as the default application protocol. Students master congestion control theory (Reno, CUBIC, BBRv3), flow control mechanics, reliability mechanisms, and the architecture of application-layer protocols including HTTP/3, gRPC, MQTT 6.0, CoAP, and DNS-over-QUIC. The course emphasizes the interplay between transport semantics and application requirements, equipping students to design, deploy, and troubleshoot modern distributed systems at the transport-application boundary.

---

## Lectures

## Lecture 1: ᚠ The Architecture of End-to-End — Transport Layer Theory from First Principles

### 1.1 Overview

The transport layer is where the rubber meets the road in network architecture. Everything below it — physical signaling, link-layer framing, IP routing — is concerned with moving packets across hops. The transport layer transforms this unreliable, best-effort packet delivery into the semantics applications actually need: reliable ordered byte streams, unreliable datagrams, flow-controlled delivery, or somewhere in between. It is, in the language of the end-to-end principle, the place where the network's responsibility ends and the endpoint's responsibility begins.

This foundational lecture establishes the theoretical framework for the entire course. We begin with the end-to-end principle — arguably the most influential architectural idea in networking — and its implications for where functionality should reside. We then examine the service models that transport protocols can provide: reliable ordered delivery (TCP), unreliable datagram delivery (UDP), partially reliable delivery (SCTP, QUIC), and the emerging class of determinism-aware transports for real-time and industrial IoT. We trace the evolution from the 1970s ARPANET NCP protocol through the TCP/UDP split that defined Internet transport for five decades, and examine why QUIC — designed at Google in 2012 and standardized as RFC 9000 in 2021 — has displaced TCP as the dominant transport in 2040.

The transport layer, in Norse metaphor, is the Bifröst between Midgard (the application) and Asgard (the network infrastructure) — the structured pathway that transforms the chaos of routed packets into the orderly realm that applications inhabit.

### 1.2 The End-to-End Principle

The end-to-end principle, articulated by Saltzer, Reed, and Clark in their seminal 1984 paper "End-to-End Arguments in System Design," holds that functions placed at low levels of a system may be redundant or of marginal value compared to the cost of providing them. The canonical example: reliable file transfer. If the network guarantees reliable delivery between adjacent hops but the application requires end-to-end reliability, the hop-by-hop guarantees are insufficient and may be wasteful — the application must implement end-to-end checks regardless, so the lower-level mechanisms add cost without adding value.

This principle has shaped the Internet's architecture profoundly. IP provides no reliability, no ordering, no duplicate suppression, and no congestion control. These are all transport-layer (or application-layer) responsibilities. The resulting "thin waist" — IP as the universal interconnection layer, with diverse transports above and diverse links below — has enabled extraordinary innovation. New link technologies (6G, satellite, quantum) can be deployed below IP without changing any transport or application code. New applications can be built above TCP or QUIC without understanding the network's internals.

In 2040, the end-to-end principle faces new challenges. Middleboxes — firewalls, NATs, traffic shaping appliances, and deep packet inspection engines — have inserted themselves into the data path, violating the principle that intelligence belongs at the endpoints. QUIC's encryption of nearly all transport headers is, in part, a response to this technology drift: by making the transport layer opaque to middleboxes, QUIC forces the network back toward the end-to-end model.

### 1.3 Transport Service Models

Transport protocols differ in the service semantics they provide to applications. Understanding these models is essential for choosing the right transport for a given application.

**Reliable Ordered Byte Stream (TCP):** The application sees a continuous, error-free, ordered stream of bytes. The protocol handles retransmission, reordering, flow control, and congestion control. This is the model that made the web, email, and file transfer possible. Its limitation: head-of-line blocking — if byte 1001 is lost, the application cannot read byte 1002 through 2000 until 1001 is retransmitted and received, even though those later bytes are already in the receiver's buffer.

**Unreliable Datagram (UDP):** The application sends discrete messages (datagrams) with no guarantee of delivery, ordering, or duplicate suppression. UDP provides only multiplexing (port numbers) and a checksum. It is the transport of choice for real-time applications (voice, video, gaming) that value timeliness over reliability, and for application-layer protocols that build their own reliability (DNS, QUIC itself).

**Partially Reliable / Multiplexed Streams (QUIC):** QUIC provides reliable ordered delivery within individual streams, but different streams are independent — loss on one stream does not block other streams. This eliminates head-of-line blocking across streams. QUIC also provides connection migration (connections survive IP address changes), 0-RTT connection establishment, and built-in encryption (TLS 1.4 integrated into the protocol).

**Reliable Multistream (SCTP):** The Stream Control Transmission Protocol (RFC 4960) provides reliable ordered delivery within streams, like QUIC, and also supports multi-homing (connections that span multiple IP addresses). SCTP saw deployment in telephony signaling (SS7 over IP) and financial systems but has limited general deployment.

**Deterministic / Time-Sensitive (DetNet, TSN):** For industrial IoT, robotic surgery, and autonomous vehicles, neither "reliable" nor "unreliable" is adequate — the requirement is deterministic latency. IEEE 802.1 Time-Sensitive Networking (TSN) and IETF Deterministic Networking (DetNet) provide bounded latency at Layer 2 and Layer 3, but the transport layer for these applications is still evolving in 2040.

### 1.4 The TCP/UDP Dichotomy and Its Decline

For decades, the Internet had two widely deployed transport protocols: TCP and UDP. This was an accident of history — the ARPANET used NCP (Network Control Protocol), which provided reliable ordered delivery. When NCP was replaced by TCP/IP on January 1, 1983 (the "flag day"), TCP inherited the reliable stream model and UDP was defined as a minimal alternative for applications that did not need TCP's overhead.

The TCP/UDP dichotomy forced application designers into a binary choice: accept TCP's overhead and head-of-line blocking, or accept UDP's lack of reliability and congestion control. Many applications chose UDP and then rebuilt TCP-like functionality at the application layer — DNS with retry logic, RTP with sequence numbers, QUIC itself (which runs over UDP datagrams but implements its own reliability and congestion control).

By 2040, QUIC has emerged as the de facto third transport. Running over UDP (itself a pragmatic choice to avoid NAT and firewall traversal problems that block unknown IP protocols), QUIC provides TCP's reliability without TCP's head-of-line blocking, connection setup latency, and middlebox sensitivity. HTTP/3 — which uses QUIC as its transport — accounted for over 35% of web traffic by 2030 and exceeds 70% by 2040. The dichotomy is dead; the era of three viable transports (TCP, UDP, QUIC) has arrived.

### 1.5 Required Reading

- Saltzer, J. H., Reed, D. P., & Clark, D. D. (1984). "End-to-End Arguments in System Design." *ACM Transactions on Computer Systems*, 2(4), 277-288.
- Iyengar, J., & Thomson, M. (2021). RFC 9000: *QUIC: A UDP-Based Multiplexed and Secure Transport*.
- Peterson, L., & Davie, B. (2039). *Computer Networks: A Systems Approach* (7th ed.). Chapter 5: End-to-End Protocols.
- Ros, D., & Welzl, M. (2023). "The Evolution of Internet Transport." *ACM SIGCOMM Computer Communication Review*, 53(2), 14-25.

### 1.6 Discussion Questions

1. The end-to-end principle argues for minimal network-layer functionality. How do middleboxes (NATs, firewalls, traffic shapers) challenge this principle, and does QUIC's encryption represent a restoration or a further violation of end-to-end?
2. If QUIC provides TCP's reliability without its limitations, why hasn't TCP been formally deprecated? What scenarios still favor TCP in 2040?
3. Design a transport service model for a real-time surgical robotics application that needs both reliability (no packet loss) and timeliness (bounded latency). Which existing transport comes closest, and what modifications would you need?

---

## Lecture 2: ᚢ TCP — The Reliable Stream Protocol and Its Five-Decade Reign

### 2.1 Overview

The Transmission Control Protocol (TCP) is the most successful transport protocol in the history of digital networks. Defined in RFC 793 (1981) and refined through dozens of subsequent RFCs, TCP has carried the overwhelming majority of Internet traffic for over five decades — web pages, email, file transfers, remote shells, database connections. Its design reflects a deep understanding of the problems that arise when building a reliable service atop an unreliable network: packet loss, reordering, duplication, and variable delay. TCP's solutions — sequence numbers, cumulative acknowledgments, sliding windows, retransmission timers, and congestion control — are mandatory knowledge for any network engineer.

This lecture covers TCP's core mechanisms: the three-way handshake, sequence numbers and cumulative ACKs, sliding window flow control, retransmission and timeout computation, and the subtle art of deciding when a segment is lost. We examine the 2040 state of TCP: its continued deployment in legacy systems, its interaction with modern middleboxes, and the ongoing maintenance of its specification by TCPM (the IETF TCP Maintenance and Minor Extensions Working Group).

### 2.2 The Three-Way Handshake

TCP's connection establishment uses the famous three-way handshake. The client sends a SYN segment (Synchronize) with an Initial Sequence Number (ISN). The server responds with a SYN-ACK segment carrying its own ISN and acknowledging the client's SYN. The client sends an ACK acknowledging the server's SYN. At this point, both sides have confirmed each other's ISN and the connection is established.

The ISN deserves careful attention. It cannot be zero (an attacker could easily predict it) and it cannot be truly random (the sequence number space wraps around, and two connections between the same endpoints must not have overlapping sequence spaces). RFC 793 specified a clock-based ISN incremented every 4 microseconds, which in practice was predictable — enabling TCP spoofing attacks. Modern implementations use cryptographically random ISNs, with RFC 6528 specifying a counter-based method as a fallback.

In 2040, the three-way handshake is largely a historical curiosity for new connections. QUIC's 0-RTT (Zero Round-Trip Time) establishment eliminates the latency cost — a client that has previously connected to a server can begin sending data immediately, without waiting for a handshake round trip. TCP's one-RTT overhead (the SYN, SYN-ACK, and the time before data flows) was acceptable in an era of sub-100ms round-trip times but became increasingly burdensome as applications demanded sub-10ms response times and mobile networks introduced high-latency paths. TCP Fast Open (RFC 7413) attempted to reduce this to 0-RTT for subsequent connections, but its deployment was limited by middlebox interference and security concerns about replay attacks.

### 2.3 Sequence Numbers and the Sliding Window

TCP's reliability rests on two mechanisms: sequence numbers and acknowledgments. Each byte of data is assigned a sequence number. The receiver sends cumulative acknowledgments — an ACK with sequence number N means "I have received all bytes up to but not including byte N." This is elegant in its simplicity: a single ACK can confirm receipt of a large window of data, and lost ACKs are automatically compensated for by later cumulative ACKs.

The sliding window controls how much unacknowledged data the sender can have in flight. The window size is the minimum of three constraints: (1) the receiver's advertised window (rwnd) — how much buffer space the receiver has, (2) the congestion window (cwnd) — how much the congestion control algorithm permits, and (3) the send buffer size — how much the application has written that has not been acknowledged. The sender may transmit data up to the minimum of these three constraints. When ACKs arrive, the window slides forward, allowing more data to be sent.

The sliding window mechanism is where flow control and congestion control meet. Flow control (the receiver's advertised window) protects the receiver from being overwhelmed. Congestion control (the congestion window) protects the network. Both are essential: without flow control, a fast sender overflowing a slow receiver's buffer causes packet loss; without congestion control, a fast sender overwhelming the bottleneck link causes congestion collapse — the phenomenon observed on the early Internet in 1986, when throughput dropped by a factor of 100 due to uncontrolled TCP senders.

### 2.4 Retransmission and Timeout Computation

How does TCP know when a segment is lost? The sender starts a retransmission timer when it sends a segment. If the timer expires before an ACK is received, the segment is retransmitted. The critical question: how long should the timer be?

Too short, and the sender retransmits segments that are merely delayed (spurious retransmissions), wasting bandwidth and causing duplicate data at the receiver. Too long, and the sender waits excessively before recovering from genuine loss, degrading throughput and application latency.

TCP's solution is the Retransmission Timeout (RTO), computed from Smoothed Round Trip Time (SRTT) and RTT variance. The SRTT is an exponential weighted moving average of measured RTT samples: SRTT = (7/8) × SRTT + (1/8) × RTT_sample. The RTT variance is similarly smoothed: RTTVAR = (3/4) × RTTVAR + (1/4) × |SRTT - RTT_sample|. The RTO is then RTO = SRTT + 4 × RTTVAR, with a minimum of 1 second.

The challenge of RTT measurement: when a segment is retransmitted and then an ACK arrives, is the ACK for the original transmission or the retransmission? This is the retransmission ambiguity problem, and Karn's Algorithm (named after Phil Karn) provides the solution: RTT samples from retransmitted segments are not used to update SRTT. Only segments that are acknowledged on the first transmission contribute to the RTT estimate. The retransmission timer is also doubled for each successive retransmission (exponential backoff), preventing the sender from overwhelming a congested network with rapid retransmissions.

TCP Selective Acknowledgments (SACK, RFC 2018) address a related problem: without SACK, the receiver can only tell the sender "I have received everything up to byte N." If bytes 1001-2000 were received but 1000 was lost, the receiver can only ACK up to 999 — forcing the sender to retransmit 1000-2000, even though 1001-2000 arrived successfully. SACK allows the receiver to report the specific blocks of data it has received, enabling the sender to retransmit only the missing bytes. In 2040, SACK is universally supported and has eliminated one of TCP's most significant inefficiencies.

### 2.5 Required Reading

- RFC 793 (1981). *Transmission Control Protocol*. The original specification.
- RFC 2581 (1999, obsoleted by RFC 5681). *TCP Congestion Control*.
- Karn, P., & Partridge, C. (1987). "Improving Round-Trip Time Estimates in Reliable Transport Protocols." *ACM SIGCOMM '87*.
- Mathis, M., et al. (1996). RFC 2018: *TCP Selective Acknowledgment Options*.
- Cheng, Y., & Cardwell, N. (2023). "TCP at 40: A Protocol That Refused to Die." *IEEE Internet Computing*, 27(4), 6-14.

### 2.6 Discussion Questions

1. Why does TCP use cumulative acknowledgments rather than per-segment ACKs? What efficiency does this buy, and what limitation does it impose?
2. The three-way handshake consumes one full RTT before data can flow. In a world where RTTs can exceed 200 ms on satellite links, how did applications work around this latency? Why is QUIC's 0-RTT approach superior, and what security tradeoff does it introduce?
3. A TCP sender's offered load exactly matches the bottleneck link capacity. A single packet is lost. Describe the exact sequence of events (timer, retransmission, ACK) that follows, and explain why the sender's throughput temporarily drops below capacity after the loss.

---

## Lecture 3: ᚦ Congestion Control — From Reno to CUBIC to BBR

### 3.1 Overview

Congestion control is the transport layer's most important contribution to network stability. Without it, the Internet would collapse — as it nearly did in October 1986, when throughput on the NSFNET backbone dropped from 32 Kbps to 40 bps due to uncontrolled TCP senders overwhelming the network. Van Jacobson's 1988 paper "Congestion Avoidance and Control" introduced the algorithms — slow start, congestion avoidance, fast retransmit, and fast recovery — that saved the Internet and became the foundation for all modern congestion control.

This lecture traces the evolution of TCP congestion control from Jacobson's original algorithms through Reno, NewReno, CUBIC, and BBR. We examine the theoretical underpinnings (AIMD — Additive Increase, Multiplicative Decrease — and its optimality properties), the practical challenges (high-bandwidth long-distance networks, bufferbloat, cellular networks with rapidly changing capacity), and the 2040 landscape where BBRv3 is the dominant congestion control for QUIC connections and CUBIC remains the default for TCP on Linux.

### 3.2 The Congestion Collapse of 1986 and Jacobson's Response

In October 1986, the early Internet experienced a dramatic performance collapse. The NSFNET backbone, running at 56 Kbps, saw effective throughput drop to as low as 40 bps — less than 0.2% of capacity. The cause: TCP senders, unaware of network congestion, continued to increase their sending rates until queues overflowed, causing massive packet loss and retransmission. The lost packets triggered more retransmissions, which further congested the network — a positive feedback loop driving throughput to near zero.

Van Jacobson's 1988 paper introduced four algorithms that became TCP Reno (the dominant TCP variant through the late 1990s). Each addresses a specific aspect of congestion:

**Slow Start:** When a connection begins (or restarts after a timeout), the sender has no information about the available bandwidth. Rather than starting at full rate and risking congestion, the sender begins with cwnd = 1 MSS (Maximum Segment Size, typically 1460 bytes) and doubles cwnd for each RTT in which all segments are acknowledged. This exponential growth quickly discovers available bandwidth: after 10 RTTs, cwnd = 1024 MSS ≈ 1.5 MB, which at a 100 ms RTT corresponds to a 120 Mbps sending rate. The sender exits slow start when cwnd reaches the slow start threshold (ssthresh) — a memory of the last known good operating point.

**Congestion Avoidance:** Once cwnd exceeds ssthresh, the sender switches from exponential to linear growth: cwnd increases by 1 MSS per RTT (i.e., cwnd += MSS × (MSS / cwnd) per ACK for TCP Reno). This additive increase probes for more bandwidth conservatively, adding roughly one packet per RTT. The tradeoff is clear: slow start discovers bandwidth quickly but risks overshooting; congestion avoidance is safe but slow — it can take hundreds of RTTs to fill a long-fat pipe.

**Fast Retransmit and Fast Recovery:** The original TCP used only timeouts to detect loss. But timeouts are expensive — the RTO is typically 1-2 seconds, an eternity in network terms. Fast retransmit uses duplicate ACKs as an early signal: when the receiver receives an out-of-order segment, it sends a duplicate ACK for the last in-order byte received. Three duplicate ACKs (i.e., three ACKs for the same sequence number) indicate that a segment was likely lost — the sender retransmits immediately without waiting for a timeout. Fast recovery keeps the connection flowing after fast retransmit: instead of resetting cwnd to 1 MSS (as slow start would), the sender sets cwnd to half the current window and continues with congestion avoidance. This avoids the drastic throughput collapse that resetting to slow start would cause.

### 3.3 AIMD and the Congestion Control Design Space

Jacobson's congestion control uses Additive Increase, Multiplicative Decrease (AIMD): increase the window by 1 MSS per RTT when no loss occurs, and decrease the window by half when loss is detected. Why AIMD specifically, and not, say, additive increase with additive decrease?

The answer lies in the concept of convergence to efficiency and fairness. Chiu and Jain's 1989 analysis showed that AIMD converges to both efficiency (full link utilization) and fairness (equal bandwidth sharing among competing flows) when multiple flows share a bottleneck. Additive increase causes all flows to slowly increase their sending rates until the bottleneck capacity is exceeded. Multiplicative decrease causes all flows to back off, and the one that backs off the most is the one that was sending the most — pushing the system toward fairness. Linear increase and multiplicative decrease are the minimum conditions for convergence to both properties.

Different congestion control algorithms occupy different points in the AIMD parameter space. TCP Reno uses (1, 0.5) — increase by 1 MSS per RTT, multiply by 0.5 on loss. CUBIC uses a cubic function for increase (allowing faster ramp-up on high-BDP networks) and the same 0.5 multiplicative decrease. BBR uses a model-based approach (discussed below) that does not use loss as a congestion signal at all. The design space also includes delay-based algorithms (Vegas, COPA) that use RTT increases as a congestion signal rather than packet loss, and hybrid approaches (Compound TCP in Windows, BBRv2/v3 which blends model-based and loss-based behavior).

### 3.4 CUBIC — The High-BDP Workhorse

TCP CUBIC (RFC 8312, originally by Ha, Rhee, and Xu, 2008) replaced TCP Reno's linear congestion avoidance with a cubic function, enabling faster window growth on high-bandwidth, high-delay (High-BDP) networks. The intuition: on a 10 Gbps link with 100 ms RTT, the bandwidth-delay product is 1 MB ≈ 700 MSS. After a loss event, cwnd drops to 350 MSS, and Reno's linear increase would take 350 RTTs (35 seconds!) to recover — an absurdly long time. CUBIC's concave-convex function grows cwnd quickly when it is far from the target and slowly near the target, achieving faster convergence.

The CUBIC window update function is: W(t) = C × (t - β × W_max)³ + W_max, where C is a scaling factor (0.4), t is time since the last loss, β is the multiplicative decrease factor (0.7 for CUBIC, compared to 0.5 for Reno), and W_max is the window size at the last loss. The cubic shape means: after a loss, cwnd grows slowly (the concave portion), then accelerates past the previous operating point, and finally grows more cautiously near the new equilibrium (the convex portion).

CUBIC became the default congestion control in Linux kernel 2.6.25 (2008) and remains the TCP default in 2040. Its strength is robust performance on high-BDP networks; its weakness is that it fills buffers (causing bufferbloat on links with large queues) because it increases cwnd until loss occurs. In a network where the bottleneck queue can hold 10 seconds of data at line rate, CUBIC will fill that queue before backing off — adding 10 seconds of latency to every packet.

### 3.5 BBR — Model-Based Congestion Control

BBR (Bottleneck Bandwidth and Round-trip propagation time), introduced by Google's Neal Cardwell and colleagues in 2016 and continuously refined through BBRv2 (2019) and BBRv3 (2023), represents a fundamental departure from loss-based congestion control. Instead of treating packet loss as a congestion signal, BBR builds an explicit model of the network path: the bottleneck bandwidth (BtlBw) and the minimum round-trip propagation time (RTprop). The sending rate is set to BtlBw, and the volume of in-flight data is set to BtlBw × RTprop (the bandwidth-delay product).

BBR operates in four phases: (1) **Startup** — exponential cwnd increase (like slow start) to quickly discover BtlBw. (2) **Drain** — after reaching the estimated BtlBw, BBR drains the queue by sending at BtlBw for one RTprop while the queue empties. (3) **ProbeBW** — BBR's steady state. It cycles through eight phases: six at the estimated BtlBw, one at 0.75× BtlBw (to probe for lower RTprop), and one at 1.25× BtlBw (to probe for higher BtlBw). This gentle probing keeps BBR's model current without causing significant queue. (4) **ProbeRTT** — periodically, BBR reduces its sending rate to 4 packets for 1 RTprop to measure the true minimum RTT (which can only be observed when the queue is empty).

BBRv2 addressed two major issues with the original BBR: (1) **Unfairness to CUBIC/Reno flows** — original BBR could consume more than its fair share on shared bottlenecks because it did not back off in response to loss (it maintained its sending rate even as queues built and other flows experienced loss). BBRv2 incorporates loss signals and reduces its rate when loss exceeds a threshold. (2) **RTT inflation** — BBR's Probing could fill queues, inflating RTT measurements. BBRv2's ECN (Explicit Congestion Notification) support and more conservative probing reduce this effect. BBRv3 further refines the model with improved RTT min filtering, better coexistence with CUBIC, and support for multipath connections.

In 2040, BBRv3 is the default congestion control for QUIC connections on major platforms (Google, Meta, Cloudflare) and is increasingly used for TCP as well. Its model-based approach is particularly effective on networks with variable capacity (cellular, satellite, Wi-Fi) where loss-based algorithms misinterpret congestion-induced loss as capacity signals.

### 3.6 Bufferbloat — The Hidden Latency Crisis

Bufferbloat, identified by Jim Gettys and Kathleen Nichols in 2011, is the excess latency caused by overly large network buffers. The problem: network equipment vendors, interpreting buffer size as a feature, shipped routers and switches with megabytes of buffer per port. When CUBIC or Reno fills these buffers before detecting loss, every packet in the queue adds latency — 10 MB of buffer at 10 Gbps adds 8 ms, but at 1 Mbps (a slow uplink), it adds 80 seconds of queuing delay. Bufferbloat explains why Internet latency was often 100-1000 ms even on "fast" connections.

BBR addresses bufferbloat by not filling queues: it sends at the estimated bottleneck bandwidth, which should result in nearly empty queues. CUBIC and Reno, by contrast, increase their sending rate until queues fill and packets are lost — adding the full buffer latency to every packet. The difference between a 5 ms RTT (empty queue) and a 500 ms RTT (full buffer) is entirely due to bufferbloat.

Solutions include: (1) Active Queue Management (AQM) — CoDel (Controlled Delay) and PIE (Proportional Integral controller Enhanced) algorithms that drop packets before queues grow to pathological sizes, signaling to CUBIC/Reno to back off earlier. (2) Fair Queuing (FQ-CoDel) — per-flow queuing with CoDel on each queue, ensuring that one flow's queue doesn't affect another's latency. (3) BBR and other model-based algorithms that avoid filling queues. In 2040, FQ-CoDel is the default qdisc (queuing discipline) on Linux, and BBRv3 is the recommended congestion control for latency-sensitive traffic.

### 3.7 Required Reading

- Jacobson, V. (1988). "Congestion Avoidance and Control." *ACM SIGCOMM '88*. The paper that saved the Internet.
- Ha, S., Rhee, I., & Xu, L. (2008). "CUBIC: A New TCP-Friendly High-Speed TCP Variant." *ACM SIGOPS Operating Systems Review*, 42(5), 64-74.
- Cardwell, N., Cheng, Y., Hassab, A., Wang, I., & Jagnandan, M. (2023). "BBRv3: Congestion-Based Congestion Control." *IETF Draft*.
- Gettys, J., & Nichols, K. (2011). "Bufferbloat: Dark Buffers in the Internet." *ACM Queue*, 9(11), 40-54.
- Chiu, D., & Jain, R. (1989). "Analysis of the Increase and Decrease Algorithms for Congestion Avoidance in Computer Networks." *Computer Networks and ISDN Systems*, 17(1), 1-14. The AIMD optimality proof.

### 3.8 Discussion Questions

1. CUBIC increases cwnd until loss occurs, then backs off by 30%. BBR sends at the estimated bottleneck bandwidth without waiting for loss. Under what conditions would each approach produce better throughput? Better latency?
2. Bufferbloat adds hundreds of milliseconds of latency on connections with large queues. Why didn't the Internet "fix" this by simply reducing buffer sizes? What are the tradeoffs of small vs. large buffers?
3. Two BBR flows share a 10 Mbps bottleneck. Two CUBIC flows share the same bottleneck. Describe how each pair converges to a fair allocation, and why BBR's convergence properties differ from CUBIC's.

---

## Lecture 4: ᚨ UDP — The Datagram Service and Its Surprising Renaissance

### 4.1 Overview

UDP (User Datagram Protocol), defined in RFC 768 (1980), is the simplest transport protocol in the Internet suite: 8 bytes of header (source port, destination port, length, checksum) and no reliability, ordering, flow control, or congestion control. For decades, UDP was the "also-ran" of transport protocols — used for DNS queries, SNMP, and not much else. The Internet's reliability expectations were so strong that UDP was considered a niche protocol for applications that explicitly did not want the network's help.

This changed dramatically in the 2010s. The rise of real-time media (VoIP, video conferencing, game streaming), the development of QUIC (which runs over UDP datagrams), and the widespread deployment of WebRTC elevated UDP from a niche protocol to a first-class transport. By 2040, UDP carries an estimated 40-50% of Internet traffic — not because applications use UDP directly, but because QUIC encapsulates its own reliable transport within UDP datagrams.

This lecture covers UDP's design, its strengths and weaknesses, the applications that use UDP directly (DNS, NTP, SNMP, RTP/RTCP, game protocols), the phenomenon of "UDP over UDP" (QUIC-in-UDP), and the critical issue of UDP congestion control. We also examine the emerging protocol Datagram Congestion Control Protocol (DCCP) and the 2030s development of L4S (Low Latency, Low Loss, Scalable Throughput) which uses ECN to provide congestion signals for UDP-based real-time traffic.

### 4.2 UDP's Minimalist Design

UDP's header is 8 bytes: Source Port (2 bytes), Destination Port (2 bytes), Length (2 bytes), Checksum (2 bytes). This minimalism is by design: UDP provides exactly two functions — multiplexing (via port numbers, allowing multiple applications on the same host to send and receive datagrams) and integrity checking (via the checksum, which covers the UDP header, the data, and a pseudo-header containing source and destination IP addresses). Everything else — reliability, ordering, flow control, congestion control — is the application's responsibility.

The checksum deserves note. In IPv4, the UDP checksum is optional (a value of 0 means "no checksum"). In IPv6, the UDP checksum is mandatory. The difference reflects the increasing understanding that corrupted data is worse than no data: without a checksum, a bit error in the data can change a bank transfer amount, a file's contents, or a DNS response's IP address — with no detection at the transport layer. In 2040, UDP checksums are universally enabled on all platforms.

UDP's lack of congestion control is its most controversial feature. A UDP sender can blast packets at line rate, consuming all available bandwidth and starving TCP flows that back off in response to congestion. RFC 8085 ("UDP Usage Guidelines") strongly recommends that UDP applications implement congestion control, either by using a standardized algorithm (e.g., TFRC — TCP-Friendly Rate Control, now RFC 5348) or by embedding a full transport protocol (e.g., QUIC). Applications that do not implement congestion control are considered "unfriendly" and may be rate-limited or dropped by network operators.

### 4.3 DNS-over-UDP and the Quest for Fast Name Resolution

DNS is the most visible UDP application. A DNS query fits in a single UDP datagram (typically 60-200 bytes), and a DNS response usually fits in a single datagram as well. The low overhead of UDP (no handshake, no connection state) makes it ideal for the request-response pattern of DNS: send a query, wait up to a few seconds, retransmit if no response. DNS-over-UDP is the default for all queries with responses under 512 bytes (traditional limit) or 4096 bytes (with EDNS0, RFC 6891).

DNS-over-TCP is used for responses that exceed the UDP size limit (zone transfers, DNSSEC-signed responses) and for DNS-over-TLS (DoT, RFC 7858) and DNS-over-HTTPS (DoH, RFC 8484), which provide privacy by encrypting DNS queries. DNS-over-QUIC (DoQ, RFC 9250) combines the low latency of UDP with the encryption and stream multiplexing of QUIC, providing both fast resolution and privacy.

In 2040, the DNS ecosystem is in transition. The traditional UDP port 53 is increasingly subject to eavesdropping, spoofing, and manipulation by middleboxes and ISPs. DoH (over HTTPS/3) and DoQ (over QUIC) provide encrypted DNS resolution, and major resolvers (Google, Cloudflare, Quad9) support both. The latency cost of encryption has been minimized: DNS-over-QUIC achieves 0-RTT resolution for repeated queries, matching or exceeding the latency of unencrypted UDP.

### 4.4 RTP/RTCP — Real-Time Media over UDP

The Real-Time Transport Protocol (RTP, RFC 3550) is the standard for carrying real-time media (audio, video) over IP networks. RTP provides payload type identification, sequence numbering, timestamping, and source identification — everything an application needs to reconstruct a media stream, but without the reliability guarantees that would add latency. RTP is typically paired with RTCP (RTP Control Protocol), which provides session statistics (packet loss, jitter, round-trip time) to senders, enabling adaptive bitrate adjustments.

RTP runs over UDP precisely because real-time media cannot wait for retransmission. A video frame that arrives 200 ms late is useless — the display has already moved on. RTP's sequence numbers allow the receiver to reorder packets that arrive out of order (common on the Internet), and RTP's timestamps allow the receiver to play back audio and video at the correct rate even if the network introduces jitter (variable inter-packet delay).

WebRTC (Web Real-Time Communication), standardized by the W3C and IETF, uses RTP over UDP as its media transport, with additional protocols for signaling (SDP over WebSocket), NAT traversal (ICE, STUN, TURN), and security (DTLS-SRTP). WebRTC's adoption — every major browser supports it natively — made UDP a first-class transport for web applications in the 2010s, foreshadowing QUIC's later adoption.

### 4.5 QUIC over UDP — The Transport Within a Transport

QUIC's decision to run over UDP datagrams rather than as a new IP protocol number was one of the most consequential architectural choices in Internet history. The alternative — a new IP protocol number (like TCP is protocol 6, UDP is protocol 17) — would have required changes to every NAT, firewall, and middlebox on the Internet. Given that middleboxes are typically configured to allow only TCP (protocol 6) and UDP (protocol 17), a new protocol number would have been blocked by a significant fraction of the Internet's infrastructure.

UDP encapsulation avoids this problem: QUIC packets are carried as UDP datagrams, which pass through existing NATs and firewalls. The cost is a small overhead (8 bytes of UDP header per QUIC packet, plus the IP header) and the limitation that middleboxes cannot apply transport-layer intelligence to QUIC traffic (they cannot see the QUIC headers inside the encrypted payload). This is considered a feature, not a bug: it prevents middleboxes from ossifying the transport layer and enables QUIC to evolve without middlebox interference.

The UDP encapsulation approach has been so successful that it has become the standard method for deploying new transport protocols. SCTP-over-UDP (for WebRTC data channels), DCCP-over-UDP (for congestion-controlled streaming), and SPUD (Smart Protocol Underneath Deliverables, an experimental approach to making transport features visible to middleboxes without ossification) all follow QUIC's pattern.

### 4.6 The Congestion Control Requirement for UDP

The IETF's position on UDP congestion control, codified in RFC 8085, is clear: "Any protocol or application that uses UDP for a bulk transfer MUST employ congestion control." This means that a UDP application that sends data at a rate that exceeds the path's available capacity must respond to congestion signals (packet loss, ECN marks, increased RTT) by reducing its sending rate.

The rationale is the Internet's stability. If UDP applications do not back off in the face of congestion, they will steal bandwidth from TCP flows that do back off — this is the classic "unfriendly flow" problem. In the worst case, widespread deployment of unfriendly UDP flows could cause another congestion collapse.

In 2040, the congestion control landscape for UDP is dominated by QUIC (which implements BBRv3 or CUBIC as its congestion control algorithm) and by WebRTC's GCC (Google Congestion Control) algorithm for real-time media. Standalone UDP applications that do not embed a congestion controller are increasingly rare and may be actively rate-limited by ISPs and enterprise networks.

### 4.7 Required Reading

- RFC 768 (1980). *User Datagram Protocol*. The original specification — all 3 pages of it.
- RFC 8085 (2017). *UDP Usage Guidelines*. The IETF's guidance on congestion control for UDP.
- RFC 9250 (2022). *DNS over Dedicated QUIC Connections*. DoQ specification.
- Perkins, C. (2003). *RTP: Audio and Video for the Internet*. Addison-Wesley. The definitive RTP reference.
- Fairhurst, G., & Welzl, M. (2023). "The Long Shadow of the End-to-End Principle: UDP in the Age of QUIC." *IEEE Internet Computing*, 27(6), 52-59.

### 4.8 Discussion Questions

1. QUIC runs over UDP but implements its own reliability and congestion control. Is QUIC "really" UDP, or is UDP just a convenient encapsulation? What are the implications for middleboxes that apply QoS or security policies based on protocol numbers?
2. DNS-over-UDP has no encryption, making DNS queries observable by anyone on the path. What are the security and privacy implications, and do DoH and DoQ fully address them?
3. A real-time video application sends 30 fps at 2 Mbps over UDP. The path has a 1 Mbps bottleneck. Describe what happens if the application does not implement congestion control, and propose a rate adaptation scheme that would be "TCP-friendly."

---

## Lecture 5: ᚱ QUIC — The Transport Protocol for the Next Generation

### 5.1 Overview

QUIC (Quick UDP Internet Connections) is the most significant development in Internet transport since the introduction of TCP itself. Originally designed at Google in 2012, standardized by the IETF as RFC 9000 in 2021, and deployed at scale by Google, Meta, Cloudflare, and others throughout the 2020s, QUIC addresses every major limitation of TCP: head-of-line blocking, connection setup latency, middlebox ossification, and lack of connection migration.

This lecture provides a comprehensive treatment of QUIC's architecture: its connection establishment (including 0-RTT), its stream multiplexing model, its loss detection and recovery mechanisms, its congestion control (BBRv3 default), its connection migration design, and its integration with TLS 1.4. We also examine the practical deployment considerations: QUIC's UDP encapsulation, the middlebox traversal challenges that remain, and the performance characteristics observed in production networks.

QUIC, in the Norse mythological framework, represents the bridge-builder Heimdallr — the guardian who sees all paths, who enables swift passage between realms (streams) without blocking, and who is ever-vigilant against the disorder that would disrupt the Bifröst of data.

### 5.2 QUIC Connection Establishment — 1-RTT and 0-RTT

QUIC's connection establishment is its most immediately visible advantage over TCP. A TCP connection requires one full RTT for the three-way handshake (SYN → SYN-ACK → ACK) before data can be sent. If TLS is used (as it should be in 2040), an additional 1-2 RTTs are needed for the TLS handshake, bringing the total to 2-3 RTTs before application data flows.

QUIC combines the transport and cryptographic handshakes into a single exchange. For a first connection to a new server (1-RTT handshake), the client sends an Initial packet containing: (1) a QUIC Version negotiation, (2) a random Connection ID, (3) the TLS ClientHello (embedded in the QUIC CRYPTO frame), and (4) any application data the client wishes to send (in 0-RTT, discussed below). The server responds with its own Initial packet containing the TLS ServerHello, Certificate, ServerFinished, and application data. The client sends a final packet with its TLS Finished message. Total: 1 RTT for connection establishment with full TLS 1.4 security — compared to TCP+TLS's 2-3 RTTs.

For subsequent connections to the same server, QUIC supports 0-RTT: the client includes application data in the very first packet, encrypted with session keys derived from the previous connection. The server can process this data immediately upon receipt, without waiting for any handshake round trip. This eliminates the latency penalty entirely — the connection establishment cost is zero RTTs. The tradeoff: 0-RTT data is vulnerable to replay attacks (an attacker can capture and resend the client's first packet), so it must not be used for idempotent-unsafe operations (e.g., "transfer $100 from account A to B" would be replay-unsafe).

### 5.3 Stream Multiplexing — Eliminating Head-of-Line Blocking

QUIC's most significant architectural improvement over TCP is stream multiplexing without head-of-line blocking. In TCP, all data flows over a single bytestream. If a packet carrying byte 1000 is lost, the receiver cannot deliver bytes 1001-2000 to the application until byte 1000 is retransmitted and received — even though those later bytes are sitting in the receiver's buffer. This is head-of-line blocking, and it is devastating for multiplexed protocols like HTTP/2, where a single lost packet can block multiple simultaneous requests.

QUIC solves this by providing multiple independent streams within a single connection. Each stream has its own flow control and reliable delivery, but loss on one stream does not block data on other streams. A QUIC connection can carry thousands of concurrent streams, each identified by a 62-bit Stream ID. Streams are created implicitly: the first frame sent on a new Stream ID creates the stream. Stream IDs also encode the stream type: client-initiated bidirectional (0, 4, 8, ...), server-initiated bidirectional (1, 5, 9, ...), client-initiated unidirectional (2, 6, 10, ...), and server-initiated unidirectional (3, 7, 11, ...).

HTTP/3 maps each HTTP request/response pair to a QUIC stream. A web page that loads 50 resources over HTTP/2 would use 50 streams within a single QUIC connection. If a packet carrying data for stream 7 is lost, streams 5, 9, 11, and all other streams continue to deliver data to the application without interruption. Only stream 7 is blocked, and only until the lost data is retransmitted. The performance difference on lossy networks (mobile, Wi-Fi) is dramatic: measurements show 30-50% improvement in page load time for HTTP/3 over HTTP/2 on networks with 1-2% packet loss.

### 5.4 Loss Detection and Recovery in QUIC

QUIC's loss detection borrows heavily from TCP's proven mechanisms (ACK-based detection, SACK, RTO) but improves them in several ways:

**Ack-Based Detection:** QUIC uses ack-based loss detection as the primary mechanism. When an ACK frame acknowledges packet N but not packet M (where M was sent before N), packet M is suspected lost after a threshold number of subsequent ACKs fail to acknowledge it. QUIC uses a packet number threshold (3 subsequent packets) rather than TCP's duplicate ACK threshold, which is more robust against reordering.

**RTO and Exponential Backoff:** If ack-based detection fails (e.g., all packets in flight are lost), QUIC falls back to a Retransmission Timeout similar to TCP's RTO. The RTO is computed using the same SRTT/RTTVAR formula as TCP but with tighter initial values and a minimum RTO of 1/8 second (compared to TCP's 1 second).

**Explicit Probing:** QUIC explicitly probes the network after an RTO by sending a single packet. If the probe is acknowledged, the sender can resume sending. This avoids the "RTO reset" problem in TCP where the sender resets cwnd to 1 MSS after a timeout.

**No Retransmission Ambiguity:** Because QUIC uses monotonically increasing packet numbers (not sequence numbers that wrap), there is no retransmission ambiguity. Each packet has a unique number, and the ACK frame explicitly acknowledges specific packet numbers. This eliminates the need for Karn's Algorithm and makes RTT measurement more accurate.

### 5.5 Connection Migration

TCP connections are identified by the 4-tuple (source IP, source port, destination IP, destination port). If any element of this tuple changes — the client moves from Wi-Fi to cellular, the client's NAT binding changes, the server's IP address changes — the TCP connection breaks. The application must establish a new connection, re-authenticate, and restart any in-progress operations. On mobile devices that switch networks frequently, this causes significant latency and disruption.

QUIC connections are identified by Connection IDs (CIDs) — 1-20 byte values chosen by each endpoint. When a QUIC endpoint's IP address changes (e.g., switching from Wi-Fi to cellular), it sends packets with the same CID on the new address. The peer recognizes the CID and associates the packets with the existing connection. No new handshake is needed, no application state is lost, and the connection survives the address change.

Connection migration is not without challenges. The peer must verify that the new address belongs to the same endpoint (Otherwise, an attacker could hijack the connection by sending packets with the victim's CID from a different address). QUIC implements path validation: the peer sends a PATH_CHALLENGE frame containing a random nonce to the new address, and waits for a PATH_RESPONSE frame with the same nonce. Only after successful path validation does the peer update its address mapping for the connection.

### 5.6 QUIC and TLS 1.4 — Encryption by Default

QUIC integrates TLS 1.4 (the successor to TLS 1.3) as a mandatory sublayer. Unlike TCP+TLS, where TLS is an optional layer on top of an unencrypted transport, QUIC encrypts nearly all of its own headers — including packet numbers, acknowledgement information, and connection-level metadata. Only the QUIC Version, Connection ID, and a few fields needed for middlebox compatibility are sent in the clear.

This design choice has two major implications. First, it provides confidentiality and integrity for all transport-layer information, preventing passive eavesdroppers from observing connection state (which packets have been acknowledged, what the RTT is, how much data is in flight). Second, and more importantly, it prevents middleboxes from inspecting or modifying QUIC's transport headers. This is deliberate: middlebox ossification — the tendency of middleboxes
 to fossilize protocol behavior by assuming specific header formats and rejecting unknown extensions — was a major obstacle to TCP evolution. QUIC's encryption makes the transport headers invisible to middleboxes, enabling protocol evolution without deployment barriers.

The integration of TLS into QUIC also simplifies the implementation. Instead of maintaining separate TCP and TLS state machines that must interoperate (the "TCP and TLS layering violation" that plagues middleboxes and implementations alike), QUIC manages encryption as a native part of the connection. Key generation, handshake, and rekeying are all handled by the QUIC connection state machine, reducing implementation complexity and avoiding the subtle bugs that arise from the TCP/TLS interface.

### 5.7 QUIC Deployment in 2040

QUIC's deployment has been remarkable. As of 2040, all major browsers (Chrome, Firefox, Safari, Edge) support HTTP/3 over QUIC by default. Major CDNs (Cloudflare, Akamai, Fastly) serve a majority of their traffic over HTTP/3. Social media platforms (Meta, TikTok) use QUIC internally for their mobile applications. Google's services (Search, YouTube, Gmail) have used QUIC since 2015. The protocol's market share continues to grow: from less than 5% of Internet traffic in 2020 to over 70% of web traffic in 2040.

Deployment challenges remain. Some enterprise networks block UDP traffic on all ports except 53 (DNS) and 443 (HTTPS/QUIC). Some ISPs rate-limit UDP traffic, assuming it is either real-time media (which tolerates some loss) or potential abuse. QUIC's encryption makes traffic classification and QoS enforcement difficult for network operators. The IETF's response has been to standardize QUIC Version Negotiation (RFC 9000 Section 6) and Encrypted Client Hello (ECH, RFC 9460) to ensure that QUIC traffic on port 443 is indistinguishable from TLS traffic on the same port, reducing the incentive for network operators to block it.

### 5.8 Required Reading

- Iyengar, J., & Thomson, M. (2021). RFC 9000: *QUIC: A UDP-Based Multiplexed and Secure Transport*. The authoritative specification.
- Thomson, M., & Turner, S. (2021). RFC 9001: *Using TLS to Secure QUIC*. The TLS integration specification.
- Iyengar, J., & Thomson, M. (2021). RFC 9002: *QUIC Loss Detection and Congestion Control*. QUIC's ACK and loss recovery mechanisms.
- Langley, A., et al. (2017). "The QUIC Transport Protocol: Design and Internet-Scale Deployment." *ACM SIGCOMM 2017*. Google's original QUIC paper.
- Marx, R., et al. (2023). "HTTP/3: From Theory to Deployment." *IEEE Communications Surveys & Tutorials*, 25(3), 1980-2015.

### 5.9 Discussion Questions

1. QUIC encrypts nearly all transport headers, preventing middleboxes from inspecting connection state. Is this a net positive or negative for the Internet? Consider the tradeoffs between protocol evolution (which QUIC enables) and network management (which QUIC hinders).
2. 0-RTT data is vulnerable to replay attacks. Design a web application that can safely use 0-RTT for initial page loads while protecting against replay for sensitive operations.
3. Compare QUIC's connection migration mechanism to MPTCP (Multipath TCP). Under what conditions would each be preferable? Can they be combined?

---

## Lecture 6: ᚲ HTTP/3 — Application Protocol on a QUIC Foundation

### 6.1 Overview

HTTP/3 is the third major version of the Hypertext Transfer Protocol, and the first to use QUIC as its transport. Where HTTP/1.1 used TCP directly and HTTP/2 multiplexed streams over a single TCP connection (suffering from head-of-line blocking at the TCP layer), HTTP/3 maps each HTTP request/response exchange to an independent QUIC stream, eliminating HOL blocking entirely. HTTP/3 also integrates TLS 1.4 compression and header encoding (QPACK) as core components, and its binary framing is derived from HTTP/2's design but simplified and optimized for QUIC.

This lecture covers HTTP/3's architecture: its framing layer, stream mapping, QPACK header compression, connection coalescing, and the practical differences between HTTP/2 and HTTP/3 that network engineers must understand. We also cover the Alt-Svc mechanism for HTTP/3 discovery, the 0-RTT Early Data model, and the implications for content delivery networks and server infrastructure.

### 6.2 HTTP/3 Framing and Stream Mapping

HTTP/3 uses QUIC streams in a specific pattern. Each HTTP request/response exchange uses a single QUIC stream: the client sends the request headers and body on a new bidirectional stream, and the server sends the response headers and body on the same stream. This is simpler than HTTP/2, which used a single TCP connection with multiplexed frames mapped to stream IDs — and it eliminates the need for HTTP/2's stream prioritization and dependency mechanisms (which were rarely implemented correctly).

In addition to request streams, HTTP/3 uses several control streams: (1) **Stream 0:** The client's bidirectional control stream, carrying QPACK encoder instructions. (2) **Stream 3:** The server's bidirectional control stream, carrying QPACK decoder instructions. (3) **Stream 2:** The client's unidirectional control stream, carrying the HTTP/3 SETTINGS frame. (4) **Stream 6:** The server's unidirectional push stream (if server push is used, though HTTP/3 de-emphasizes server push).

HTTP/3 frames are similar to HTTP/2 frames but with key simplifications: (1) **DATA frame:** Carries request/response body data. (2) **HEADERS frame:** Carries compressed request/response headers using QPACK. (3) **SETTINGS frame:** Exchanges HTTP/3 configuration parameters. (4) **GOAWAY frame:** Gracefully terminates a connection, indicating the last processed stream ID. (5) **MAX_PUSH_ID frame:** Controls server push. (6) **CANCEL_PUSH frame:** Cancels a promised server push.

The most important simplification over HTTP/2 is the elimination of HPACK's dynamic table synchronization problem. HTTP/2's HPACK header compression uses a dynamic table that is shared between encoder and decoder; if a packet containing a dynamic table update is lost, the encoder and decoder tables diverge, blocking all subsequent header processing until the loss is recovered. HTTP/3's QPACK (described below) fixes this by using explicit acknowledgments for table updates.

### 6.3 QPACK — Header Compression for QUIC

QPACK (RFC 9204) is HTTP/3's header compression scheme, designed to avoid the HOL blocking that HPACK creates on lossy connections. QPACK uses two dynamic tables (one on the encoder side, one on the decoder side) and an explicit acknowledgment mechanism that ensures table entries are used only after the decoder has confirmed their insertion.

The key difference from HPACK: in HTTP/2, all frames are multiplexed on a single TCP stream, so a lost HPACK table update blocks all subsequent header decoding, even for unrelated streams. In HTTP/3, each request/response is on an independent QUIC stream, so a lost QPACK instruction blocks only the streams that reference the affected table entry — other streams can continue processing their headers independently.

QPACK's design also includes: (1) **Static table:** 99 pre-defined common header field values (e.g., ":method GET", "content-type text/html"). These are always available without any dynamic table updates. (2) **Dynamic table:** A FIFO table that stores recently used header field values. The encoder inserts entries and references them by index; the decoder acknowledges insertions using dedicated acknowledgment streams. (3) **Blocking references:** A stream can temporarily block if its headers reference dynamic table entries that have not yet been acknowledged. The encoder can choose to never block (by using only static table entries and literal values) or to allow blocking (by referencing recent dynamic entries that may not yet be acknowledged). The encoder specifies a maximum number of blocking references, giving the application control over the blocking/efficiency tradeoff.

In 2040, QPACK achieves compression ratios of 80-90% for typical web traffic (compared to uncompressed headers), comparable to HPACK. The performance difference between QPACK and HPACK is negligible on low-loss networks but significant on lossy networks: QPACK's independence from cross-stream blocking can improve page load times by 20-30% on mobile networks with 1% packet loss.

### 6.4 Alt-Svc and HTTP/3 Discovery

A client cannot simply start sending HTTP/3 requests to a server — it needs to know that the server supports HTTP/3 and on which port. HTTP/3 uses the Alt-Svc HTTP header (RFC 7838) and the Alt-Svc HTTP/2 and HTTP/3 frames to advertise alternative services: "I also speak HTTP/3 on port 443." The client attempts an HTTP/3 connection on the advertised port and uses it for subsequent requests if successful.

The Alt-Svc mechanism is critical for HTTP/3 deployment because it allows servers to offer HTTP/3 alongside HTTP/2 without breaking existing clients. A client that doesn't support HTTP/3 simply ignores the Alt-Svc header and continues using HTTP/2. A client that does support HTTP/3 caches the Alt-Svc advertisement and attempts HTTP/3 on subsequent connections. This graceful migration path has been essential for HTTP/3's adoption.

In 2040, most HTTPS servers advertise HTTP/3 via Alt-Svc, and most browsers prefer HTTP/3 when available. The "upgrade dance" — client connects with HTTP/2, receives Alt-Svc, reconnects with HTTP/3 — has been optimized to minimize latency: the initial HTTP/2 connection can be used for the first request while the HTTP/3 connection is established in parallel, and the browser switches to HTTP/3 for subsequent requests.

### 6.5 HTTP/3 and Content Delivery Networks

CDNs have been the primary drivers of HTTP/3 adoption. Cloudflare, Akamai, and Fastly all support HTTP/3 on their edge servers, and Google's and Meta's infrastructure has used QUIC internally since the mid-2010s. For CDNs, the performance advantages of HTTP/3 are most pronounced on mobile networks (where packet loss is high and connection migration is valuable) and on long-distance connections (where the 0-RTT handshake saves significant time).

CDN deployment of HTTP/3 has also driven improvements in QUIC implementation quality. The QUIC implementations in major CDN servers (Cloudflare's quiche, Google's Chromium QUIC, Meta's mvfst, Microsoft's msquic, Mozilla's Neqo) are now mature and interoperable. The IETF's interoperability testing events (called "QUIC bakeoffs" in the 2019-2021 period) verified that all major implementations could communicate successfully.

### 6.6 Required Reading

- Bishop, M. (2022). RFC 9114: *HTTP/3*. The HTTP/3 specification.
- Krasic, C., et al. (2020). RFC 9204: *QPACK: Header Compression for HTTP/3*.
- RFC 7838 (2016). *HTTP Alternative Services*. The Alt-Svc mechanism.
- Marx, R., & Quax, P. (2023). "HTTP/3 Performance in Practice: A Large-Scale Measurement Study." *ACM IMC 2023*.
- Wei, L., et al. (2024). "From HTTP/2 to HTTP/3: A Decade of Web Protocol Evolution." *IEEE Network*, 38(2), 42-50.

### 6.7 Discussion Questions

1. HTTP/2's HPACK header compression causes head-of-line blocking because dynamic table updates are carried on the same TCP stream as other frames. QPACK's dynamic table uses dedicated streams. Explain why this eliminates the HOL blocking and what performance impact it has on lossy networks.
2. Alt-Svc allows servers to advertise HTTP/3 support without dropping HTTP/2 clients. Describe a deployment scenario where a server operator might choose NOT to enable Alt-Svc for HTTP/3, and what the implications would be.
3. A CDN serves 10 million requests per second over HTTP/3. Each request creates a new QUIC stream. What are the memory implications of maintaining millions of concurrent QUIC connections and streams? How do QUIC implementations manage this state efficiently?

---

## Lecture 7: ᚹ gRPC — High-Performance RPC over HTTP/3

### 7.1 Overview

gRPC (gRPC Remote Procedure Call) is a high-performance, open-source RPC framework originally developed at Google and now a CNCF (Cloud Native Computing Foundation) graduated project. gRPC uses Protocol Buffers (protobuf) for interface definition and serialization, and HTTP/3 (or HTTP/2 in legacy deployments) as its transport, providing efficient binary serialization, bidirectional streaming, and built-in service discovery and health checking. In 2040, gRPC is the dominant RPC framework for microservice architectures, replacing REST for internal service-to-service communication while coexisting with REST for external APIs.

This lecture covers gRPC's architecture: its four communication patterns (unary, server streaming, client streaming, bidirectional streaming), its use of protobuf for serialization, its integration with HTTP/3 and QUIC, its load balancing and service mesh integration, and the operational considerations for deploying gRPC at scale.

### 7.2 gRPC Communication Patterns

gRPC defines four communication patterns, each mapping to a different combination of request and response streams:

**Unary RPC:** The simplest pattern — the client sends a single request and receives a single response. This is the familiar request-response model, equivalent to a REST GET or POST. gRPC's unary pattern is used for point lookups, status queries, and any operation where the request and response fit in a single message.

**Server Streaming RPC:** The client sends a single request and receives a stream of responses. The server pushes results to the client as they become available, closing the stream when complete. Use cases: real-time stock quotes, log tailing, search-as-you-type, and any scenario where the server produces results incrementally.

**Client Streaming RPC:** The client sends a stream of requests and receives a single response. This pattern is used for bulk uploads, streaming aggregation, and any scenario where the client generates data incrementally and the server processes it all at once. Example: uploading a large file in chunks, where the server assembles the chunks and returns a summary.

**Bidirectional Streaming RPC:** Both client and server send streams of messages. Either side can send at any time — the streams are independent. This is the most flexible pattern, used for real-time collaboration, chat applications, and any scenario where both sides produce data asynchronously. In a QUIC context, each gRPC stream maps to a QUIC stream, and bidirectional streaming takes full advantage of QUIC's multiplexing without HOL blocking.

### 7.3 Protocol Buffers — Serialization and Interface Definition

Protocol Buffers (protobuf) is gRPC's interface definition language (IDL) and serialization format. A .proto file defines services and messages:

```protobuf
syntax = "proto3";

service NetworkManager {
  rpc GetInterface(InterfaceRequest) returns (Interface);
  rpc StreamMetrics(MetricsRequest) returns (stream MetricsSnapshot);
  rpc UploadConfig(stream ConfigChunk) returns (ConfigResult);
  rpc MonitorLink(stream LinkEvent) returns (stream LinkAlert);
}

message InterfaceRequest {
  string name = 1;
}

message Interface {
  string name = 1;
  string ip_address = 2;
  int64 speed_bps = 3;
  bool admin_up = 4;
}
```

Protobuf serializes messages into a compact binary format: each field is encoded as a (field number, wire type, value) triple. Variable-length integers use varint encoding, strings are length-prefixed, and repeated fields use length-delimited encoding. A typical protobuf message is 3-10 times smaller than the equivalent JSON and 20-50 times faster to serialize/deserialize.

Protobuf's evolution story is well-designed: new fields can be added to messages without breaking existing code (old code simply ignores unknown fields), and old fields can be deprecated but not removed. This forward and backward compatibility is critical for microservice architectures where different services may be running different versions of the same .proto definition.

### 7.4 gRPC over HTTP/3 — The 2040 Standard

In the 2010s and 2020s, gRPC was deployed over HTTP/2. The mapping was straightforward: each gRPC RPC maps to an HTTP/2 stream, request headers are sent as HTTP/2 HEADERS frames, request bodies are sent as DATA frames, and response headers and bodies follow the same pattern. The gRPC status code (OK, CANCELLED, UNKNOWN, etc.) is carried in a trailing HEADERS frame (the "grpc-status" trailer).

In 2040, gRPC-over-HTTP/3 is the recommended deployment. The mapping is identical to HTTP/2, but each gRPC stream maps to an independent QUIC stream, eliminating the head-of-line blocking that plagued gRPC-over-HTTP/2. This is particularly important for bidirectional streaming RPCs, where a single lost TCP packet in an HTTP/2 connection would block all active streams — with QUIC, only the affected stream is blocked.

gRPC-over-HTTP/3 also benefits from QUIC's 0-RTT connection establishment. In microservice architectures, where a service may make millions of gRPC calls per second to other services, the one-RTT overhead of establishing a new TCP+TLS connection for each call (in connection pool exhaustion scenarios) is eliminated: QUIC's 0-RTT allows the first gRPC request to be sent immediately, and connection migration allows in-flight requests to survive network changes.

### 7.5 gRPC in Service Meshes and Kubernetes

gRPC's adoption has been driven in large part by its integration with service mesh technologies. In a Kubernetes cluster with Istio, Linkerd, or Consul Connect, gRPC traffic is automatically load-balanced, encrypted (with mTLS), and observability-instrumented without application code changes. The sidecar proxy (Envoy in Istio) intercepts gRPC traffic, performs L7 load balancing (distributing requests based on gRPC method, not just IP:port), and exports metrics to Prometheus.

gRPC's built-in health checking (the grpc.health.v1.Health service) and service reflection (the grpc.reflection.v1.ServerReflection service) make it easy for service meshes and load balancers to monitor service health and discover available methods. In 2040, Kubernetes-native gRPC deployments use these features extensively: the kubelet probes gRPC health endpoints, the ingress controller routes external traffic to gRPC services, and the service mesh provides circuit breaking, rate limiting, and retry policies.

### 7.6 Required Reading

- gRPC authors (2023). *gRPC: Up and Running* (2nd ed.). O'Reilly. The practical guide to gRPC deployment.
- Protobuf Language Guide (2024). *Protocol Buffers, Edition 2023*. Google documentation.
- Liu, D., et al. (2024). "gRPC at Scale: Lessons from Operating 10 Million gRPC Streams." *ACM SIGCOMM 2024*.
- CNCF gRPC WG (2023). "gRPC over HTTP/3: Deployment Guide." Cloud Native Computing Foundation.

### 7.7 Discussion Questions

1. gRPC uses protobuf for serialization, which is 3-10x more compact than JSON. Is this always an advantage? Consider scenarios where protobuf's binary format is a disadvantage (debugging, browser clients, schema evolution) and propose mitigations.
2. A microservice architecture has 50 services, each communicating via gRPC over HTTP/3. Describe the connection pooling strategy: how many QUIC connections should each service maintain to each other service? What are the tradeoffs between many short-lived connections and few long-lived connections?
3. gRPC's bidirectional streaming pattern allows both client and server to send messages freely. Design a network monitoring system that uses bidirectional streaming to push real-time alerts while receiving configuration updates, and explain how QUIC's stream multiplexing benefits this design.

---

## Lecture 8: ᚺ DNS — The Internet's Directory Service and Its Protocol Evolution

### 8.1 Overview

The Domain Name System (DNS) is the Internet's single most important application-layer protocol — the directory that translates human-readable names (www.university-of-yggdrasil.edu) into machine-readable IP addresses (203.0.113.42). Every web request, every email, every SSH connection begins with a DNS lookup. In 2040, DNS handles an estimated 2 trillion queries per day, making it the highest-volume application protocol on the Internet.

This lecture covers DNS's architecture: its hierarchical namespace, its distributed query-resolution mechanism, its record types, and its caching behavior. We then examine the critical protocol evolution from DNS-over-UDP to DNS-over-TLS (DoT), DNS-over-HTTPS (DoH), and DNS-over-QUIC (DoQ) — a progression driven by the need for privacy, security, and performance in an era of pervasive surveillance and DNS manipulation.

DNS, in Norse terms, is Heimdallr's horn — the signal that reaches across all the realms, translating one identity into another, announcing arrivals and departures, and standing guard against threats to the credibility of name-to-address mappings.

### 8.2 The DNS Hierarchy and Resolution Process

DNS is a distributed, hierarchical database. The namespace is organized as an inverted tree, with the root zone at the top, top-level domains (TLDs) like .com, .org, .edu below, and second-level domains like yggdrasil.edu below the TLDs. Each zone is managed by a designated authority — the root zone by IANA/ICANN, .com by Verisign, yggdrasil.edu by the University of Yggdrasil's DNS administrators.

The resolution process for "www.cs.yggdrasil.edu" illustrates the hierarchy: (1) The client's stub resolver sends a query to its configured recursive resolver (typically run by the ISP, enterprise, or a public resolver like 1.1.1.1 or 8.8.8.8). (2) The recursive resolver queries the root server for "www.cs.yggdrasil.edu" and receives a referral to the .edu TLD servers. (3) The recursive resolver queries the .edu TLD servers and receives a referral to yggdrasil.edu's authoritative servers. (4) The recursive resolver queries yggdrasil.edu's authoritative server for "www.cs.yggdrasil.edu" and receives the authoritative answer (e.g., an A record with the IP address). (5) The recursive resolver caches the answer (for the duration specified in the TTL — Time To Live — field) and returns it to the client.

Caching is essential for DNS's scalability. Without caching, every resolution would require 4 queries (root, TLD, authoritative, response). With caching, most resolutions require 0 queries (the answer is already cached) or 1 query (only the authoritative server needs to be contacted). The TTL determines how long a cached answer is valid; typical TTLs range from 60 seconds (for dynamic content) to 86,400 seconds (1 day for stable infrastructure records).

### 8.3 DNS Record Types

DNS supports numerous record types, each carrying different information:

- **A:** Maps a domain name to an IPv4 address. Example: `www.cs.yggdrasil.edu. 300 IN A 203.0.113.42`
- **AAAA:** Maps a domain name to an IPv6 address. Example: `www.cs.yggdrasil.edu. 300 IN AAAA 2001:db8::42`
- **CNAME:** Canonical name — an alias that points to another domain name. Example: `web.cs.yggdrasil.edu. 300 IN CNAME www.cs.yggdrasil.edu`
- **MX:** Mail exchange — specifies the mail servers for a domain. Example: `yggdrasil.edu. 3600 IN MX 10 mail.yggdrasil.edu`
- **NS:** Name server — specifies the authoritative DNS servers for a zone. Example: `yggdrasil.edu. 86400 IN NS ns1.yggdrasil.edu`
- **TXT:** Text record — carries arbitrary text data, used for SPF, DKIM, DMARC, and domain verification.
- **SRV:** Service record — specifies the hostname and port for a particular service. Example: `_grpc._tcp.cs.yggdrasil.edu. 300 IN SRV 10 5 443 grpc.cs.yggdrasil.edu`
- **HTTPS:** HTTPS-specific service binding (SVCB) record — specifies the supported HTTP versions, supported protocols, and other hints for HTTPS clients. This is the successor to the ALPN extension in TLS and is critical for HTTP/3 discovery. Example: `www.cs.yggdrasil.edu. 300 IN HTTPS 1 . alpn=h3,h2`

In 2040, the HTTPS record type (defined in RFC 9460) is increasingly important: it allows clients to discover HTTP/3 support,ECH (Encrypted Client Hello) configuration, and alternative endpoints without making an initial HTTP connection. This solves the "bootstrapping problem" for HTTP/3 — how does a client learn that a server supports HTTP/3 before making its first request?

### 8.4 DNS-over-HTTPS (DoH) and DNS-over-QUIC (DoQ)

Traditional DNS-over-UDP is sent in cleartext, observable by anyone on the path. This enables ISPs to track browsing, governments to censor specific domains, and attackers to inject false DNS responses (DNS spoofing/cache poisoning). The Kaminsky attack (2008) demonstrated that DNS-over-UDP is vulnerable to transaction ID prediction, allowing attackers to poison DNS caches with arbitrary responses.

DNS-over-TLS (DoT, RFC 7858) encrypts DNS queries using TLS on port 853, providing confidentiality and integrity. DoT is supported by most recursive resolvers and is the standard for DNS privacy in enterprise networks. However, DoT uses a separate port (853), making it easy for network administrators to block or redirect.

DNS-over-HTTPS (DoH, RFC 8484) encrypts DNS queries using HTTPS on port 443, making DNS traffic indistinguishable from regular web traffic. DoH is supported by all major browsers (Chrome, Firefox, Safari) and is the default for many users. The IETF's position is that DoH should respect enterprise network policies (using canary domains to detect managed networks), but the debate over who controls DNS resolution — the user, the enterprise, or the ISP — remains unresolved.

DNS-over-QUIC (DoQ, RFC 9250) encrypts DNS queries using QUIC, providing the same privacy as DoH with lower latency (QUIC's 0-RTT handshake enables fast resolution for repeated queries) and better performance on lossy networks (QUIC's stream multiplexing avoids HOL blocking when multiple queries are in flight). DoQ is a natural fit for stub-to-recursive resolver communication, and several public resolvers (Cloudflare, AdGuard) support it on port 853 (shared with DoT, with ALPN negotiation).

### 8.5 DNS Security — DNSSEC, DANE, and Beyond

DNSSEC (DNS Security Extensions) provides cryptographic signatures for DNS records, allowing resolvers to verify that DNS responses have not been tampered with. DNSSEC adds new record types (RRSIG, DNSKEY, DS, NSEC) that chain trust from the root zone down to individual zones. The root zone was signed in 2010, and most TLDs support DNSSEC by 2040.

DANE (DNS-Based Authentication of Named Entities, RFC 6698) uses DNSSEC to authenticate TLS certificates, providing an alternative to the CA (Certificate Authority) system. With DANE, a domain publishes its TLS certificate (or its hash) in a TLSA record, and clients verify that the server's certificate matches the published record. DANE eliminates the need to trust hundreds of CAs, reducing the attack surface for certificate misissuance.

In 2040, DNSSEC adoption remains below 30% of signed zones, primarily because key management complexity and the risk of signer-side outages (a broken DNSSEC signature makes the entire zone unreachable). DANE adoption is even lower, limited to specific communities (email servers using SMTP DANE, some government systems). The dominant model for DNS security remains DoH/DoQ for confidentiality and DNSSEC for authenticity, with the CA system still providing TLS certificate validation.

### 8.6 Required Reading

- Mockapetris, P. (1987). RFC 1034/1035: *Domain Names — Concepts and Facilities / Implementation and Specification*. The original DNS specification.
- Hoffman, P., & McManus, P. (2018). RFC 8484: *DNS Queries over HTTPS (DoH)*.
- Huitema, C., et al. (2022). RFC 9250: *DNS over Dedicated QUIC Connections*.
- Aviv, M., et al. (2024). "DNS Privacy at Scale: A Decade of DoH and DoQ Deployment." *ACM SIGCOMM Computer Communication Review*, 54(1), 32-45.
- RFC 9460 (2023). *Service Binding and Parameter Specification via the DNS (SVCB/HTTPS)*.

### 8.7 Discussion Questions

1. DoH makes DNS traffic indistinguishable from HTTPS traffic, preventing ISPs from observing or blocking DNS queries. But it also prevents enterprise networks from enforcing DNS-based security policies (blocking malware domains, enforcing content filters). What is the right balance between user privacy and enterprise security?
2. DNSSEC provides data integrity but not data confidentiality — a DNSSEC-signed response can be observed by anyone on the path. How do DoH and DoQ complement DNSSEC? What threats does DNSSEC address that DoH/DoQ do not, and vice versa?
3. The HTTPS record type (SVCB/HTTPS) allows clients to discover HTTP/3 support and ECH configuration before connecting. Describe the full resolution process for a first-time visitor to "www.example.com" using HTTPS records, and explain how many round trips are saved compared to the traditional approach of connecting with HTTP/2 and receiving an Alt-Svc header.

---

## Lecture 9: ᛁ MQTT and CoAP — Application Protocols for IoT and Edge Computing

### 9.1 Overview

The Internet of Things (IoT) and edge computing present fundamentally different requirements from traditional web applications. IoT devices are resource-constrained (limited CPU, memory, battery), connected over lossy networks (LoRa, Zigbee, 6LoWPAN, satellite), and often require asynchronous communication patterns (sensors pushing data, actuators receiving commands). The application protocols that serve these environments must be lightweight, efficient, and tolerant of intermittent connectivity.

MQTT (Message Queuing Telemetry Transport) and CoAP (Constrained Application Protocol) are the two dominant application-layer protocols for IoT and edge computing in 2040. MQTT, originally developed by IBM in 1999 and standardized by OASIS, uses a publish-subscribe model that decouples producers from consumers. CoAP, developed by the IETF CoRE Working Group (RFC 7252), brings RESTful semantics (GET, PUT, POST, DELETE) to constrained devices over UDP. Both protocols have evolved significantly since their original specifications: MQTT 6.0 (2028) adds QUIC transport, request-response patterns, and shared subscriptions; CoAP over QUIC (RFC 9116, 2022) provides reliable delivery and congestion control without TCP overhead.

This lecture covers MQTT's architecture (topics, QoS levels, retained messages, last will), CoAP's architecture (resources, observe, blockwise transfers, confirmed messages), and the practical considerations for deploying these protocols at scale in IoT networks of thousands to millions of devices.

### 9.2 MQTT — Publish/Subscribe for the Internet of Things

MQTT's architecture is centered on the broker — a server that receives published messages from clients and routes them to subscribed clients. The communication pattern is publish-subscribe: a publisher sends a message to a topic (e.g., "sensors/temperature/floor3/room307"), and the broker delivers the message to all clients that have subscribed to that topic (or a wildcard pattern like "sensors/temperature/floor3/+"). This decoupling of publishers and subscribers is MQTT's key advantage: publishers don't need to know how many subscribers exist, and subscribers don't need to know where data originates.

**Topics and Wildcards:** MQTT topics are hierarchical, with levels separated by forward slashes. The single-level wildcard (+) matches exactly one topic level: "sensors/+/room307" matches "sensors/temperature/room307" and "sensors/humidity/room307" but not "sensors/temperature/floor3/room307". The multi-level wildcard (#) matches any number of levels: "sensors/temperature/#" matches all temperature topics regardless of depth.

**QoS Levels:** MQTT defines three Quality of Service levels, each with increasing reliability and overhead:
- QoS 0 (At most once): The message is sent and forgotten. No acknowledgment, no retry. The message may be lost or delivered exactly once. Suitable for sensor data that is frequently updated and where occasional loss is acceptable.
- QoS 1 (At least once): The message is acknowledged by the broker. If the broker doesn't receive an acknowledgment, the publisher retransmits. The message is guaranteed to be delivered at least once, but duplicates may occur. Suitable for commands that must be received but can tolerate deduplication.
- QoS 2 (Exactly once): A four-part handshake (PUBLISH, PUBREC, PUBREL, PUBCOMP) ensures the message is delivered exactly once. This is the most expensive QoS level and should be used only for critical messages where duplicates are unacceptable (e.g., payment confirmations, safety-critical actuator commands).

**Retained Messages:** A publisher can mark a message as "retained," causing the broker to store the last retained message for each topic and deliver it to new subscribers immediately upon subscription. This eliminates the "first message" problem: without retained messages, a subscriber that connects after a sensor has published its value wouldn't receive the current value until the sensor publishes again.

**Last Will and Testament (LWT):** When a client connects to the broker, it can register a "will" — a message that the broker will publish to a specified topic if the client disconnects unexpectedly (without sending a DISCONNECT message). LWT is essential for monitoring device health: if a sensor loses power or connectivity, the broker publishes its LWT, notifying other clients that the sensor is offline.

**MQTT 6.0 (2028):** The latest version adds several features critical for large-scale deployment. QUIC transport provides 0-RTT connection establishment (important for battery-powered devices that wake up periodically to publish data). Shared subscriptions (a feature from MQTT 5.0, refined in 6.0) allow multiple subscribers to share a subscription, with the broker load-balancing messages across the group — essential for horizontal scaling of message consumers. Request-response patterns (a new feature in 6.0) add a correlation data field for matching responses to requests, enabling synchronous RPC-like interactions over the async publish-subscribe model.

### 9.3 CoAP — RESTful Constrained Environments

CoAP (RFC 7252) brings the REST architectural style to constrained devices. It maps HTTP methods (GET, PUT, POST, DELETE) to UDP datagrams, with optional reliability provided by confirmable (CON) messages that require an acknowledgment (ACK) and a retransmission mechanism. Non-confirmable (NON) messages are fire-and-forget, like UDP, but with CoAP formatting.

**Message Types:** CoAP defines four message types. CON (Confirmable) messages require an ACK from the receiver; if no ACK is received within a timeout, the sender retransmits with exponential backoff. NON (Non-confirmable) messages do not require an ACK and are suitable for frequent sensor readings where occasional loss is acceptable. ACK messages acknowledge a CON message. RST (Reset) messages indicate that the receiver cannot process the message (e.g., the endpoint is offline).

**Observe Extension (RFC 7641):** CoAP's Observe extension allows clients to subscribe to resource changes, similar to MQTT's publish-subscribe but with a RESTful interface. A client sends a GET request with the Observe option set, and the server responds with the current state and then sends additional responses whenever the resource changes. This is useful for sensor data: a client subscribes to "/sensors/temperature/307" and receives updates whenever the temperature changes, without polling.

**Blockwise Transfers (RFC 7959):** CoAP messages are limited to ~1 KB (the UDP datagram size). For larger resources, CoAP defines blockwise transfers: the client requests blocks of the resource one at a time, using the Block1 and Block2 options to specify the block number and size. This enables firmware updates and large resource transfers over constrained networks.

**CoAP over QUIC (RFC 9116, 2022):** CoAP over QUIC provides reliable delivery, congestion control, and encryption without the overhead of TCP. Each CoAP CON message is mapped to a QUIC stream, enabling parallel reliable transfers without the HOL blocking that would occur over TCP. NON messages are sent over QUIC datagrams (an extension that provides unreliable delivery over QUIC). CoAP over QUIC is particularly valuable for satellite and cellular IoT networks, where the high latency and variable bandwidth of these networks make TCP-based approaches unreliable.

### 9.4 Scaling MQTT and CoAP — From Thousands to Millions of Devices

In 2040, IoT deployments range from a few hundred sensors in a smart building to millions of devices in a smart city or agricultural monitoring network. The scaling challenges are different at each order of magnitude:

**Thousands of devices:** A single MQTT broker (EMQX, HiveMQ, Mosquitto) or CoAP server can handle tens of thousands of concurrent connections. The primary concerns are topic design (hierarchical topics that enable efficient filtering) and QoS selection (using QoS 0 for frequent sensor data, QoS 1 for commands, QoS 2 only when absolutely necessary).

**Hundreds of thousands of devices:** Broker clustering becomes necessary. EMQX and HiveMQ support multi-node clusters that distribute connections across multiple servers, with shared subscription support for horizontal scaling of message consumers. The CoAP side typically uses a load balancer (HAProxy, nginx) with DTLS session resumption to distribute connections across multiple CoAP servers.

**Millions of devices:** At this scale, the broker itself becomes a distributed system. MQTT 5.0's shared subscriptions and MQTT 6.0's QUIC transport enable federation across multiple broker clusters, each handling a fraction of the total connections. CoAP at this scale uses anycast DNS and geographic load balancing to route devices to the nearest server. The key challenge is not connection handling (QUIC and CoAP are designed for massive fan-in) but topic management and message routing — ensuring that a message published to "sensors/temperature/europe/germany/munich/#" is efficiently routed to all subscribers without requiring the broker to maintain a topic tree with millions of entries.

### 9.5 Required Reading

- OASIS (2028). *MQTT Version 6.0 Specification*. The latest MQTT specification with QUIC transport support.
- Shelby, Z., Hartke, K., & Bormann, C. (2014). RFC 7252: *The Constrained Application Protocol (CoAP)*.
- RFC 7641 (2012). *Observing Resources in CoAP*.
- RFC 9116 (2022). *CoAP over QUIC*.
- Singh, D., et al. (2027). "MQTT at Scale: Operating 10 Million Concurrent Connections." *IEEE Internet of Things Journal*, 14(3), 2045-2058.
- Al-Fuqaha, A., et al. (2025). "Internet of Things: A Survey on Protocols, Edge Computing, and Integration with 6G." *IEEE Communications Surveys & Tutorials*, 27(1), 45-87.

### 9.6 Discussion Questions

1. MQTT QoS 2 provides exactly-once delivery, but it requires a four-part handshake. Calculate the total message overhead for a QoS 2 message compared to QoS 0 and QoS 1. When is QoS 2 worth the overhead?
2. A smart city deployment has 500,000 sensors publishing temperature data every 60 seconds and 1,000 actuators subscribing to commands. Design an MQTT topic hierarchy and choose QoS levels for each message type. Calculate the broker's message throughput requirements.
3. CoAP over QUIC and MQTT 6.0 over QUIC both use QUIC as their transport. Compare the two approaches: when would you choose CoAP over QUIC, and when would you choose MQTT over QUIC, for an IoT application?

---

## Lecture 10: ᛃ Email Protocols — SMTP, IMAP, and the Reinvention of Electronic Mail

### 10.1 Overview

Electronic mail is the Internet's oldest application-layer protocol and, in 2040, still one of its most important. SMTP (Simple Mail Transfer Protocol, RFC 5321) for message submission and relay, and IMAP (Internet Message Access Protocol, RFC 9051) for mailbox access, form the two-pillar architecture of Internet email. Despite predictions of email's demise — "email is dead" has been declared every year since 2005 — email remains the universal identity and communication layer of the Internet, with an estimated 400 billion messages per day in 2040.

This lecture covers the architecture of Internet email: the submission agent (MUA → MSA), the relay agents (MTA → MTA), and the delivery agent (MDA → MUA). We examine SMTP's protocol mechanics (EHLO, MAIL FROM, RCPT TO, DATA), its authentication extensions (SMTP AUTH, SPF, DKIM, DMARC), and the encryption mechanisms (STARTTLS, DANE, MTA-STS). On the IMAP side, we cover mailbox operations (SELECT, FETCH, SEARCH, COPY, MOVE), IDLE push notifications, and the modern extensions (CONDSTORE, QRESYNC, LIST-EXTENDED) that make IMAP efficient for large mailboxes.

### 10.2 SMTP — The Mail Submission and Relay Protocol

SMTP is the protocol for submitting email messages from a client to a server and relaying them between servers. In the modern architecture, SMTP is used in two contexts:

**Submission (port 587 or 465):** The user's Mail User Agent (MUA) — e.g., Thunderbird, Gmail web interface, Apple Mail — submits outgoing messages to a Mail Submission Agent (MSA). The MSA authenticates the user (via SMTP AUTH, typically using OAuth 2.0 bearer tokens in 2040), validates the message headers (ensuring From address matches the authenticated user), applies rate limits, and submits the message to the mail queue for delivery. Port 587 uses STARTTLS (upgrading a plaintext connection to TLS after the initial SMTP greeting), while port 465 uses implicit TLS (the connection is encrypted from the start — SMTPS).

**Relay (port 25):** Mail Transfer Agents (MTAs) relay messages between themselves using SMTP on port 25. When a message is addressed to a domain not hosted by the sending MTA, the MTA looks up the domain's MX (Mail Exchanger) records in DNS, connects to the destination MTA on port 25, and transmits the message. Port 25 traffic is typically unencrypted or opportunistically encrypted (STARTTLS if available), though MTA-STS (SMTP MTA Strict Transport Security, RFC 8461) and DANE (DNS-Based Authentication of Named Entities) are increasingly requiring encryption for server-to-server relay.

The SMTP protocol is straightforward: the client sends EHLO (Extended HELO) to announce its capabilities, the server responds with supported extensions. The client then issues MAIL FROM (sender address), RCPT TO (recipient address, one per recipient), and DATA (the message body, terminated by a line containing only a period). The server confirms acceptance with a 250 response code. The entire exchange is synchronous: the client waits for each response before sending the next command.

### 10.3 Email Authentication — SPF, DKIM, and DMARC

In the early Internet, anyone could send email claiming to be from any address — SMTP had no built-in authentication. This made email spoofing trivial and enabled the spam epidemic that still plagues email in 2040. Three authentication mechanisms have been deployed to address this:

**SPF (Sender Policy Framework, RFC 7208):** The domain owner publishes a DNS TXT record listing the IP addresses authorized to send email on behalf of the domain. Example: `yggdrasil.edu. IN TXT "v=spf1 ip4:203.0.113.0/24 include:_spf.google.com ~all"`. The receiving MTA checks the connecting IP address against the SPF record. If the IP is not authorized, the message is rejected or marked as suspicious.

**DKIM (DomainKeys Identified Mail, RFC 6376):** The sending MTA signs selected headers and the message body with a private key, and publishes the corresponding public key in a DNS TXT record. The receiving MTA verifies the signature, confirming that the message was sent by the domain owner and was not modified in transit. DKIM provides both authentication and integrity.

**DMARC (Domain-based Message Authentication, Reporting, and Conformance, RFC 7489):** DMARC ties SPF and DKIM together and adds a policy enforcement mechanism. The domain owner publishes a DMARC policy in DNS: "if SPF and DKIM both fail, reject the message" (p=reject), "quarantine it" (p=quarantine), or "monitor it" (p=none). DMARC also specifies reporting: the domain owner receives aggregate reports from receivers showing which messages passed or failed authentication, enabling monitoring of unauthorized use.

In 2040, DMARC adoption exceeds 90% for large email providers (Google, Microsoft, Yahoo) and is increasingly required by enterprise email gateways. The combination of SPF, DKIM, and DMARC has not eliminated spam (spammers can register their own domains and publish valid SPF/DKIM records), but it has made domain spoofing difficult and enabled receivers to block or quarantine unauthenticated messages with confidence.

### 10.4 IMAP — Mailbox Access and Synchronization

IMAP (Internet Message Access Protocol) is the protocol for accessing and synchronizing email messages stored on a server. Unlike POP3 (Post Office Protocol version 3, which downloads and deletes messages), IMAP keeps messages on the server, allowing multiple clients (desktop, phone, web) to access the same mailbox simultaneously.

IMAP's core operations are: (1) **LOGIN/AUTHENTICATE:** Authenticate the user (typically via OAuth 2.0 in 2040). (2) **SELECT/EXAMINE:** Open a mailbox (e.g., INBOX, Sent, Drafts) for reading. (3) **FETCH:** Retrieve message data — headers, body structure, specific MIME parts, flags, or the entire message. (4) **SEARCH:** Find messages matching criteria (sender, subject, date range, flags, full-text search). (5) **STORE:** Modify message flags (\Seen, \Answered, \Flagged, \Deleted, \Draft). (6) **COPY/MOVE:** Copy or move messages between mailboxes. (7) **EXPUNGE:** Permanently remove messages marked as \Deleted.

Modern IMAP extensions have dramatically improved efficiency for mobile and high-latency clients. **IDLE (RFC 2177):** Allows the client to request server push notifications — the server sends mailbox updates (new messages, flag changes) in real time without the client polling. **CONDSTORE (RFC 7162):** Enables incremental mailbox synchronization — the client stores a modification sequence number (modseq) and requests only the changes since that modseq, instead of downloading the entire mailbox state. **QRESYNC (RFC 7162):** Combines CONDSTORE with quick mailbox resurrection — after a disconnection, the client can quickly resynchronize without re-downloading the entire mailbox. **LIST-EXTENDED (RFC 5258):** Allows the client to subscribe to specific mailbox hierarchies and receive notifications of mailbox creation and deletion.

### 10.5 Email Encryption — STARTTLS, MTA-STS, and DANE

Encrypted email transport has been available since the introduction of STARTTLS (RFC 3207, 2001), which upgrades a plaintext SMTP connection to TLS after the initial EHLO exchange. By 2040, STARTTLS is supported by over 99% of mail servers, and most major providers (Google, Microsoft, Yahoo) require encryption for incoming mail.

However, STARTTLS is vulnerable to downgrade attacks: an active attacker can strip the STARTTLS keyword from the server's EHLO response, causing the client to fall back to plaintext. Two mechanisms address this: **MTA-STS (RFC 8461):** The domain owner publishes an MTA-STS policy in DNS (and via HTTPS at a well-known URL), specifying that all incoming mail must use TLS. Receiving MTAs cache the policy and refuse to deliver mail over a plaintext connection if the policy requires TLS. **DANE (DNS-Based Authentication of Named Entities, RFC 6698):** The domain owner publishes the server's TLS certificate fingerprint in a DNS TLSA record. Receiving MTAs verify the server's certificate against the TLSA record, preventing both downgrade attacks and certificate misissuance.

End-to-end email encryption (PGP/GPG, S/MIME) remains a niche practice in 2040, used primarily by security-conscious individuals and organizations. The fundamental challenge — key distribution and discovery — has not been solved at scale. Autocrypt (an email encryption standard that automates key exchange) and the Automatic Email Encryption proposals in the IETF are making progress, but the dream of universal end-to-end encrypted email remains unrealized.

### 10.6 Required Reading

- RFC 5321 (2008). *Simple Mail Transfer Protocol*. The core SMTP specification.
- RFC 9051 (2021). *Internet Message Access Protocol (IMAP) — Version 4rev2*. The current IMAP standard.
- Kucherawy, M. (2024). *Email Authentication: SPF, DKIM, and DMARC in Practice* (3rd ed.). O'Reilly.
- RFC 8461 (2018). *SMTP MTA Strict Transport Security (MTA-STS)*.
- Ramakrishnan, K., & Sherry, J. (2025). "The State of Email Encryption in 2025: STARTTLS, MTA-STS, and DANE." *ACM SIGCOMM 2025*.

### 10.7 Discussion Questions

1. DMARC requires alignment between the From address domain and either the SPF or DKIM domain. Explain why this alignment is necessary and how a misconfigured DMARC policy can cause legitimate email to be rejected.
2. IMAP IDLE allows the server to push notifications to the client. Compare this approach to the "long polling" and "webhook" patterns used in HTTP-based email APIs (Gmail API, Microsoft Graph). What are the advantages and disadvantages of each approach for a mobile email client?
3. Email encryption (PGP, S/MIME) has been available for decades but has seen less than 5% adoption. Analyze the technical, social, and economic reasons for this failure, and propose a mechanism that could achieve greater than 50% end-to-end email encryption adoption.

---

## Lecture 11: ᛏ Application Protocol Design — Building Protocols for the 2040s

### 11.1 Overview

Having studied the major application-layer protocols — HTTP/3, gRPC, DNS, MQTT, CoAP, and email — this lecture steps back to examine the art and science of designing new application protocols. In 2040, the Internet continues to evolve: new application categories (XR/AR streaming, autonomous vehicle telemetry, quantum key distribution) create requirements that existing protocols do not fully address. This lecture covers the design principles, specification techniques, and implementation considerations for building application protocols that are efficient, extensible, and secure.

We examine the IETF's design principles (rough consensus, running code, protocol layering), the choice between binary and text protocols, the use of protocol buffers and other serialization formats, the role of protocol versioning and extensibility, and the security considerations that must be addressed from the start (authentication, authorization, transport encryption, downgrade protection).

### 11.2 The Tussle Between Binary and Text Protocols

The Internet's history is a pendulum between binary and text protocol formats. Early protocols (SMTP, FTP, HTTP/0.9, POP3) were text-based: commands and responses were human-readable ASCII strings, separated by CRLF line terminators. This made debugging easy (you could telnet to a server and type commands by hand) but parsing expensive and error-prone (line length limits, character encoding issues, ambiguous grammar).

The binary pendulum swung with ASN.1 (used in SNMP and LDAP), then with HTTP/2 and HTTP/3's binary framing, gRPC's protobuf encoding, and QUIC's variable-length integer encoding. Binary formats are more compact, faster to parse, and less ambiguous. They are also harder to debug (you need a protocol disassembler like Wireshark) and less resilient to extension (adding a new field requires updating the specification and all implementations).

The 2040 consensus is to use binary formats for performance-critical protocols (transport, RPC) and text-based formats (JSON, YAML, TOML) for configuration and human-facing APIs. gRPC uses protobuf for serialization but provides a JSON transcoding layer for debugging and browser clients. HTTP/3 uses binary framing internally but preserves human-readable headers for developer convenience. The key lesson: choose the format that optimizes for the protocol's primary users — machines (binary) or humans (text).

### 11.3 Serialization Formats — Protobuf, JSON, CBOR, and FlatBuffers

The choice of serialization format impacts a protocol's performance, extensibility, and developer experience:

**Protocol Buffers (protobuf):** Binary format with a schema (the .proto file). Pros: compact encoding, fast serialization/deserialization, forward and backward compatibility, strongly typed. Cons: requires a schema and code generation, not human-readable, debugged only with specialized tools. Best for: service-to-service RPC (gRPC), high-throughput data pipelines.

**JSON (JavaScript Object Notation):** Text-based, schema-optional format. Pros: human-readable, universally supported, no schema required, easy to debug. Cons: verbose (5-10x larger than protobuf), slow to parse, no native binary data support, vulnerable to type confusion (number/string ambiguity). Best for: REST APIs, configuration files, web-facing endpoints.

**CBOR (Concise Binary Object Representation, RFC 8949):** Binary format that is a superset of JSON. Pros: compact, fast to parse, self-describing (no schema required), supports binary data, extensible. Cons: not human-readable, less tooling than JSON or protobuf. Best for: IoT protocols (CoAP uses CBOR), constrained environments, protocol payloads that need binary efficiency.

**FlatBuffers / Cap'n Proto:** Zero-copy serialization formats. Data is accessed directly from the serialized buffer without parsing. Pros: extremely fast (no serialization/deserialization step), minimal memory allocation. Cons: complex schema, no forward compatibility guarantees, larger encoded size. Best for: game engines, real-time systems, inter-process communication where latency is critical.

In 2040, the ecosystem has converged on protobuf for service-to-service communication (via gRPC), JSON for external APIs and configuration, and CBOR for IoT protocols. FlatBuffers and Cap'n Proto are niche choices used in specific high-performance domains.

### 11.4 Protocol Versioning and Extensibility

Designing a protocol for extensibility is one of the hardest problems in protocol design. HTTP/1.1's extension mechanism (new headers) was too permissive (any entity could add any header), leading to semantic conflicts and middlebox ossification. HTTP/2's extension mechanism (new frames and settings) is more structured but requires implementations to negotiate extensions during connection setup. HTTP/3 follows HTTP/2's approach but adds QUIC transport parameters and HTTP/3 settings as additional extension points.

The general principles for extensible protocol design in 2040 are:

1. **Reserve extension points early:** Define capacity for new message types, flags, and parameters even if they are not used in the initial version. QUIC's variable-length integer encoding (2, 4, or 8 byte integers) and HTTP/3's SETTINGS frame (key-value pairs for extensible configuration) are examples.

2. **Require clients to ignore unknowns:** The "be liberal in what you accept" principle from Jon Postel's Robustness Principle (RFC 760) has been revised for 2040: "be conservative in what you send, be liberal in what you accept — but validate what you accept." Unknown fields, parameters, and frames should be ignored (not rejected), enabling newer servers to send information that older clients can safely skip.

3. **Version negotiation:** Always include a version negotiation mechanism. QUIC's version negotiation (the server responds with a list of supported versions if the client's version is not supported) is a model: it allows new versions to be deployed incrementally without breaking old clients.

4. **Code points for experiments:** Reserve ranges of code points (frame types, error codes, settings IDs) for experimental use. This allows implementers to prototype new features without allocating permanent code points.

### 11.5 Security by Design — Authentication, Encryption, and Downgrade Resistance

In 2024 and beyond, new protocols must be designed with mandatory encryption. The IETF's policy, formalized in RFC 9325 ("Recommendations for Secure Use of Transport Layer Security") and the broader IETF consensus that "new protocols must use encryption," means that any protocol designed in 2040 without encryption is dead on arrival.

Key security considerations for protocol design:

**Authentication:** Every protocol must define how endpoints authenticate each other. Options include: (1) TLS client certificates (mutual TLS, mTLS), (2) OAuth 2.0 bearer tokens, (3) API keys, (4) public key fingerprints (similar to SSH's known_hosts model). The choice depends on the deployment model: service-to-service (mTLS), user-facing (OAuth), IoT (pre-shared keys or certificates).

**Downgrade resistance:** A protocol must resist active downgrade attacks, where an attacker tricks the endpoints into using a weaker version or cipher suite. TLS 1.3's downgrade sentinel (a random value in the ServerHello that the client can verify) and QUIC's version negotiation (which always prefers the highest mutually supported version) are examples of downgrade resistance.

**Forward secrecy:** Every connection should use ephemeral key exchange (ECDHE, X25519) so that compromise of a long-term private key does not compromise past session keys. Forward secrecy is mandatory in TLS 1.3 and QUIC.

**Traffic analysis resistance:** Protocols that carry sensitive data should be designed to resist traffic analysis — the inference of user behavior from packet timing, size, and direction. Padding, traffic shaping, and packet size normalization are techniques used in QUIC, Tor, and other privacy-focused protocols.

### 11.6 Required Reading

- Rose, M. (2019). *On the Design of Application Protocols*. IETF Draft. A short, incisive guide to protocol design principles.
- RFC 9325 (2022). *Recommendations for Secure Use of Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)*.
- Bormann, C., & Hoffman, P. (2022). RFC 8949: *Concise Binary Object Representation (CBOR)*.
- Thomson, M. (2023). "Protocol Design for the Next Decade." *ACM SIGCOMM Computer Communication Review*, 53(4), 18-28.

### 11.7 Discussion Questions

1. You are designing a new protocol for autonomous vehicle telemetry (latency under 10ms, bandwidth 1-10 Mbps per vehicle, 100,000 vehicles per cell tower). Choose a serialization format, transport protocol, and authentication mechanism, and justify each choice.
2. Protocol extensibility requires that implementations ignore unknown fields. What are the security implications of this design choice? How can an attacker abuse a server that silently ignores unknown but malicious parameters?
3. Compare the version negotiation strategies of HTTP (version in the first line/header), TLS (version in the ClientHello/ServerHello), and QUIC (version in the first packet). What are the tradeoffs of each approach in terms of extensibility, security, and deployability?

---

## Lecture 12: ᛜ The Synthesis — Transport and Application Protocols in the Age of Quantum, 6G, and AI

### 12.1 Overview

This final lecture synthesizes the entire course, examining the transport and application layer landscape of 2040 and projecting forward to the challenges and opportunities of the coming decade. Three forces are reshaping the protocol landscape:

**Quantum networking and post-quantum cryptography:** Quantum Key Distribution (QKD) promises unbreakable encryption for transport-layer security, while post-quantum cryptographic algorithms (CRYSTALS-Kyber, CRYSTALS-Dilithium) are being deployed in TLS 1.4 and QUIC to protect against quantum attacks on classical key exchange. The transition to PQC is the most significant cryptographic migration in the Internet's history, and transport protocols are at the center of it.

**6G and satellite mesh networks:** 6G's terahertz communication and intelligent surfaces will create new transport challenges: extremely high bandwidth (100 Gbps+) with extremely short range, requiring rapid handoff between access points. Satellite mesh constellations (Starlink, OneWeb, and their successors) create high-latency, high-bandwidth paths with variable RTT (20-600ms depending on the satellite orbit). Transport protocols must adapt to these extremes.

**AI-managed networks (AIOps):** AI is increasingly used to manage transport-layer parameters — congestion control (BBR's model-based approach), traffic engineering (predictive path selection), and fault detection (anomaly detection in telemetry streams). The question is not whether AI will manage transport protocols, but how much autonomy the AI should have and what guardrails are needed.

### 12.2 Post-Quantum Cryptography in Transport Protocols

The transition from classical public-key cryptography (RSA, ECDH) to post-quantum cryptography (PQC) is the most significant deployment challenge for transport protocols since the introduction of TLS 1.0. Classical key exchange (ECDH with X25519 or P-256) is vulnerable to Shor's algorithm, which a sufficiently large quantum computer could use to break the discrete logarithm problem in polynomial time. In 2040, such a computer does not yet exist, but the "harvest now, decrypt later" threat — an adversary who captures encrypted traffic today and stores it until a quantum computer can break the key exchange — is real.

PQC algorithms are being deployed in two phases. Phase 1 (2024-2028): Hybrid key exchange, combining classical ECDH with CRYSTALS-Kyber. If either algorithm is broken, the connection remains secure. TLS 1.3 with hybrid Kyber-ECDH is supported by all major browsers and servers. Phase 2 (2029+): Full PQC key exchange, using CRYSTALS-Kyber (ML-KEM) alone, with CRYSTALS-Dilithium (ML-DSA) for digital signatures. The larger key sizes of PQC algorithms (ML-KEM public keys are 1,188 bytes for Kyber-768, compared to 32 bytes for X25519) impact transport protocol design: QUIC's Initial packet must carry the PQC key exchange material, increasing the handshake size and potentially requiring multiple Initial packets for the ClientHello.

The impact on QUIC's 0-RTT is particularly significant. PQC key exchange adds approximately 1,500 bytes to the ClientHello (Kyber-768 plus X25519 for hybrid). This exceeds the typical Initial packet size, requiring QUIC implementations to handle fragmented Initial packets. The 0-RTT data, which previously fit in the same packet as the ClientHello, now requires a separate packet or a larger Initial packet. The IETF's TLS Working Group and QUIC Working Group are coordinating the PQC migration to ensure that 0-RTT remains usable with PQC.

### 12.3 6G Transport Challenges

6G networks (expected commercial deployment 2030-2035) will introduce transport challenges that current protocols are not designed for:

**Terahertz communication (100 GHz - 3 THz):** Terahertz links provide 100 Gbps+ bandwidth but require line-of-sight and have extremely short range (10-100 meters). Devices will frequently hand off between terahertz access points, causing rapid IP address changes and connection disruptions. QUIC's connection migration mechanism is essential for maintaining connection continuity across these handoffs.

**Intelligent surfaces (reconfigurable metasurfaces):** 6G envisions building surfaces that can shape RF propagation, reflecting or focusing signals to create virtual line-of-sight paths. The handoff between different surface configurations will cause rapid changes in link quality — bandwidth may jump from 1 Gbps to 100 Gbps and back within milliseconds. Congestion control algorithms must adapt to these rapid capacity changes. BBR's model-based approach (estimating bottleneck bandwidth and updating it continuously) is better suited than CUBIC's loss-based approach (which treats capacity changes as congestion events).

**AI-native air interface:** 6G's physical layer will use AI-designed waveforms, modulation, and coding schemes that are not human-specified. The transport layer will see these as variable-capacity links with unpredictable loss patterns. Transport protocols must be robust to physical-layer behaviors they cannot predict or model.

### 12.4 AI-Managed Transport — BBR and Beyond

BBR's model-based approach represents the first step toward AI-managed transport. BBR explicitly models the network path (bottleneck bandwidth, minimum RTT, queuing delay) and adjusts its sending rate based on the model. The model is simple (two parameters) and the adaptation rules are deterministic (fixed probing schedules, fixed gain/loss factors).

The next step is reinforcement learning (RL) — an agent that learns an optimal sending policy by interacting with the network and receiving a reward signal (throughput, latency, loss rate). Research RL-based congestion controllers (Aurora, Orca, Vivace) have demonstrated throughput improvements of 10-30% over CUBIC and BBR in simulation, but face significant deployment challenges: (1) **Safety:** RL agents can explore harmful actions (sending at line rate, causing congestion collapse) before learning to avoid them. Guardrails are needed to prevent the agent from harming the network during exploration. (2) **Convergence:** RL agents must converge to stable policies — they cannot oscillate between sending rates, causing oscillatory congestion. (3) **Fairness:** An RL agent that learns an aggressive policy can starve TCP flows sharing the same bottleneck. Fairness to non-RL flows must be a training objective. (4) **Generalization:** An RL agent trained on one network path may not generalize to others. Domain randomization and meta-learning are promising approaches.

In 2040, BBRv3 remains the dominant congestion controller, with RL-based controllers in research prototypes. The gap between BBRv3 and RL controllers is narrowing, but safety and fairness concerns have prevented RL controllers from being deployed at scale. The IETF's ICCRG (Internet Congestion Control Research Group) is developing guidelines for the safe deployment of AI-based congestion controllers.

### 12.5 The Bifröst of Protocols — Transport and Application in the Age of Yggdrasil

As we conclude this course, we return to the Norse metaphor that has woven through our lectures. The transport layer is the Bifröst — the shimmering bridge between realms — connecting the world of applications (Midgard) to the world of network infrastructure (Asgard). Like Heimdallr, who guards the Bifröst and sees all who cross it, the transport layer must be vigilant: detecting congestion, recovering from loss, adapting to changing conditions, and ensuring that the bridge remains open for all who need it.

The application layer is the realm of purpose — the reasons why data flows across the Bifröst. DNS resolves names because applications need addresses. HTTP transfers documents because people need information. MQTT delivers sensor data because cities need to be smart. gRPC invokes remote procedures because microservices need to communicate. Every application protocol is an expression of human need, translated into structured messages that traverse the transport bridge.

The Norns — Urðr (What Was), Verðandi (What Is Becoming), and Skuld (What Shall Be) — weave the threads of protocol evolution. What Was: TCP and UDP, the twin pillars of the Internet's first five decades. What Is Becoming: QUIC, HTTP/3, and the multiplexed, encrypted, model-based protocols of the 2040s. What Shall Be: AI-managed transport, quantum-secured key exchange, and the protocols of 6G and beyond. The tapestry is never complete; new threads are always being added.

As network engineers of the 2040s, your role is to understand both the bridge and the realms it connects. You must know when to use TCP's reliable streams and when to use UDP's fire-and-forget datagrams. You must understand QUIC's stream multiplexing and choose the right gRPC communication pattern for your application. You must design application protocols that are efficient, extensible, and secure. And you must prepare for the quantum transition, the 6G revolution, and the AI-managed networks that will define the next decade.

This course has given you the foundations. The Bifröst awaits.

---

## Final Examination Preparation

### Exam Format

The final examination for CN203 consists of **8 essay questions**. You must answer **4 of 8** questions. Each answer should demonstrate mastery of the relevant protocols, their design rationale, and their practical tradeoffs. Strong answers will reference specific RFC numbers, protocol mechanisms, and real-world deployment considerations.

### Sample Essay Questions

1. **Transport Service Models:** Compare and contrast TCP's reliable ordered byte stream, UDP's unreliable datagram, and QUIC's multiplexed stream model. For each, describe an application that benefits from that model and explain why the alternatives are inferior. Discuss the implications of QUIC's stream multiplexing for HTTP/3's performance compared to HTTP/2 over TCP.

2. **Congestion Control Evolution:** Trace the evolution of TCP congestion control from Reno through CUBIC to BBR. For each algorithm, explain the congestion signal it uses, the window adjustment function it applies, and the deployment context (network characteristics) for which it is best suited. Analyze why BBR's model-based approach is better suited for cellular and satellite networks than CUBIC's loss-based approach.

3. **QUIC Design Justifications:** QUIC runs over UDP, encrypts nearly all transport headers, uses monotonically increasing packet numbers, and supports connection migration. For each of these design choices, explain the problem it solves, the alternative approaches that were considered, and the tradeoffs involved. Discuss how each choice affects middlebox behavior and protocol evolution.

4. **DNS Privacy and Security:** Describe the attack vectors against traditional DNS-over-UDP (eavesdropping, spoofing, cache poisoning, censorship). Evaluate the effectiveness of DoH, DoQ, and DNSSEC in addressing each vector. What threats remain even with full deployment of all three?

5. **Application Protocol Design:** Design an application protocol for a real-time collaborative document editing system (similar to Google Docs) that must support 50+ concurrent editors with sub-100ms latency. Choose a transport protocol (TCP, UDP, or QUIC), a serialization format (protobuf, JSON, CBOR), a synchronization model (operational transformation, CRDT, or state-based), and a reliability mechanism. Justify each choice and describe the protocol's message format, flow control, and conflict resolution strategy.

6. **MQTT and CoAP for IoT:** A smart agricultural operation deploys 10,000 soil moisture sensors across 500 farms. Each sensor publishes a reading every 5 minutes. 50 actuators subscribe to irrigation commands. Design the MQTT topic hierarchy, choose QoS levels for each message type, and calculate the broker's throughput and connection requirements. Then compare this with a CoAP-based design: what are the advantages and disadvantages of each approach?

7. **Post-Quantum Migration:** Describe the impact of post-quantum cryptographic algorithms on QUIC's connection establishment. Calculate the approximate increase in handshake size for hybrid ML-KEM-768 + X25519 key exchange compared to X25519 alone. Discuss the implications for 0-RTT, middlebox behavior, and the deployment timeline.

8. **Email Authentication and Encryption:** Trace the evolution of email authentication from SPF through DKIM to DMARC. Explain how each mechanism addresses a specific attack vector and how DMARC unifies them. Then analyze why end-to-end email encryption (PGP/S/MIME) has seen less than 5% adoption despite being available for decades. Propose a strategy that could achieve greater than 50% adoption.

---

*ᛟ The threads of Wyrd are woven through every packet. May your connections be reliable, your streams unblocked, and your congestion windows ever-wise.*