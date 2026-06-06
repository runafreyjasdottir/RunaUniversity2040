# CN301: Software-Defined Networking (SDN)
## Bachelor of Science in Computer Networking — University of Yggdrasil, 2040

**Credits:** 4
**Description:** Comprehensive study of Software-Defined Networking — the architectural paradigm that separates the network control plane from the data plane, enabling programmatic, centralized control of network behavior. Students master OpenFlow, P4, SDN controllers, network function virtualization, intent-based networking, and the Bifrǫst Mesh SDN architecture that automates the entire Yggdrasil campus network.

**Instructor:** Dr. Brynja Vindóttirsdóttir, Professor of Network Architecture & Bifrǫst Control Plane Architect
**Lab:** Valhalla Network Lab, Sublevel 2, Hákon Computing Centre (SDN Emulation Cluster)
**Office Hours:** Tuesdays & Thursdays 10:00-12:00, or by appointment

---

## Lectures

ᚠ **Lecture 1: The Case for Programmable Networks — From CLI to Code**

**Course:** CN301 — Software-Defined Networking (SDN)
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Before SDN, every network device was an island — configured through vendor-specific command-line interfaces, managed through SNMP, and operated through fragile scripts. This lecture traces the evolution from manual, per-device configuration to programmable, network-wide control, examining why the old model broke and how SDN fixes it.

### Key Topics

- **The Traditional Network Model:** Each network device (router, switch, firewall) is an autonomous system that makes independent forwarding decisions based on its local routing table. Configuration is per-device: an administrator logs into each router via SSH or console, enters CLI commands, and the router stores the configuration in NVRAM. Management is via SNMP (polling counters and setting variables) or NETCONF/YANG (structured configuration). The problem: scale (managing 1,000+ devices), consistency (ensuring all devices have the same ACLs), and agility (changes take hours to days across the network).
- **The Configuration Management Crisis:** A 2040 enterprise network has 500 switches, 200 routers, 100 firewalls, and 50 load balancers. Each device has 100-500 lines of configuration. A single policy change (e.g., "block traffic from subnet A to subnet B") requires updating ACLs on every device between A and B — which may be 50 devices. The mean time to implement a security policy change is 4 hours. The error rate for manual CLI changes is 5-10%. The result: slow, error-prone, and expensive network operations.
- **The SDN Abstraction:** Separate the control plane (the brain — where forwarding decisions are made) from the data plane (the hands — where packets are forwarded). The control plane becomes a centralized software program (the controller) that has a global view of the network. The data plane becomes a set of simple packet-processing devices (switches) that forward packets according to rules installed by the controller. The controller programs the switches through a southbound API (e.g., OpenFlow).
- **The Benefits of Separation:** Centralized control (the controller sees the entire network topology and can compute optimal paths), programmability (network behavior is defined by software, not by CLI commands), vendor independence (the controller can program switches from any vendor that supports the southbound API), and speed (changes propagate in milliseconds, not hours). The analogy: traditional networking is like drivers navigating independently with maps; SDN is like air traffic control directing all planes.
- **A Brief History of SDN:** The Clean Slate program at Stanford (2006-2008), OpenFlow 1.0 (2009), Nicira Networks and the first commercial SDN controller (2011), OpenDaylight (2013), ONOS (2014), P4 (2016), and the 2040 landscape: intent-based networking (IBN), AI-driven control, and the Bifrǫst Mesh's Norn SDN controller.

### Lecture Notes

The configuration management crisis is not theoretical — it is the daily reality of every network operations team. Consider a security policy change: "Block all traffic from the guest Wi-Fi network to the HR database server." In a traditional network, this policy must be implemented as an ACL on every router and switch between the guest Wi-Fi and the HR server. An administrator must identify all 50 devices in the path, log into each one, add the ACL, verify it, and save the configuration. If any device is missed, the policy has a hole. If any device's ACL is misconfigured (wrong subnet mask, wrong direction), the policy fails. And if the network topology changes (a new link is added, a device is relocated), the ACLs must be updated on the affected devices.

SDN solves this by moving the ACL from the data plane (where it is scattered across 50 devices) to the control plane (where it is a single policy defined once). The controller translates the high-level intent ("block guest Wi-Fi from HR database") into device-specific rules and installs them on every affected switch. If the topology changes, the controller recomputes the rules and updates the affected devices automatically. The network operator defines policy once; the controller enforces it everywhere.

The analogy with air traffic control is instructive. Before air traffic control, pilots navigated independently using maps and radio. They chose their own routes, communicated with nearby pilots, and hoped to avoid collisions. This worked when there were few planes, but as air traffic grew, it became clear that independent navigation could not scale. Air traffic control centralized routing decisions: controllers see all planes on radar, compute optimal routes, and direct pilots to follow them. The result: safer, more efficient air travel. SDN does the same for networks: the controller sees all traffic, computes optimal paths, and directs switches to follow them.

The history of SDN begins at Stanford University, where Martin Casado, Nick McKeown, and Scott Shenker recognized that the traditional network model was fundamentally broken. Their key insight: the network's control plane (routing protocols, ACL processing, traffic engineering) and data plane (packet forwarding) are logically separate and can be physically separated. The control plane can run on a general-purpose computer (the controller), and the data plane can run on a simple packet-processing device (the switch). The controller programs the switch through a well-defined API (OpenFlow), enabling programmatic control of forwarding behavior. This separation allows rapid innovation: new routing protocols, traffic engineering algorithms, and security policies can be implemented in software on the controller, without modifying the switches.

The Bifrǫst Mesh's Norn controller is the culmination of this evolution. Named after the Norns of Norse mythology (Urd, Verdandi, and Skuld — past, present, and future), the Norn controller applies intent-based networking principles: the operator declares what the network should do (the intent), and the Norn controller figures out how to do it (the configuration). An intent like "ensure all campus traffic is encrypted" is translated into具体 configuration: enabling MACsec on all switch ports, configuring IPsec on all router links, and deploying TLS on all server connections. If a new switch is added to the network, the Norn controller automatically configures it to match the intent. If a link fails, the Norn controller recomputes paths and updates the affected switches in milliseconds.

### Required Reading

- McKeown, N., et al. (2008). "OpenFlow: Enabling Innovation in Campus Networks." *ACM SIGCOMM Computer Communication Review*, 38(2), 69-74.
- Casado, M., et al. (2007). "Ethane: Taking Control of the Enterprise." *ACM SIGCOMM 2007*.
- Yggdrasil SDN Architecture Guide (2040). "Norn Controller" and "Intent-Based Networking."

### Discussion Questions

1. The traditional network model gives each device autonomous control over its forwarding decisions. SDN centralizes control in a single controller. What happens when the controller fails? Design a control plane architecture that provides centralized control with high availability.
2. A network has 500 switches, each with 200 lines of configuration. An administrator makes 10 changes per day, with a 5% error rate. Calculate the expected number of configuration errors per day. How does SDN reduce this error rate?
3. The air traffic control analogy suggests that centralized control is more efficient than distributed control. But air traffic control has a single point of failure: if the controller goes down, planes must revert to independent navigation. Is this analogy valid for SDN? What mechanisms does SDN provide for controller failure?

---

ᚢ **Lecture 2: OpenFlow — The First SDN Southbound Interface**

**Course:** CN301 — Software-Defined Networking (SDN)
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

OpenFlow was the first standardized interface between the SDN controller and the data plane. This lecture covers the OpenFlow protocol, match-action processing, flow tables, and the architectural patterns that OpenFlow introduced and that P4 refined.

### Key Topics

- **OpenFlow Architecture:** The controller-switch interface. The controller communicates with switches over a TLS-encrypted channel, sending flow mod messages (install rules), flow removed messages (delete rules), and packet-in/packet-out messages (send packets to the controller or inject packets from the controller). The switch maintains flow tables that match packets against rules and execute actions.
- **Match-Action Processing:** The fundamental abstraction of SDN data planes. A flow entry consists of: match fields (input port, Ethernet source/destination, IP source/destination, TCP/UDP ports, etc.), priority (higher priority matches first), counters (bytes/packets matched), and actions (forward to port, drop, modify header, send to controller, send to next table). When a packet arrives, the switch searches the flow table for the highest-priority matching entry and executes the corresponding actions.
- **Flow Table Pipeline:** OpenFlow 1.3+ supports multiple flow tables, organized as a pipeline. A packet enters table 0, which may forward the packet to table 1 for further processing, and so on through the pipeline. Each table can match different fields and take different actions. Example: table 0 matches on ingress port and VLAN (ingress processing), table 1 matches on IP destination (routing), table 2 matches on TCP/UDP ports (ACL/firewall), and table 3 performs egress processing.
- **Group Tables:** Beyond flow tables, OpenFlow supports group tables for more complex forwarding behaviors. Group types: all (forward to all ports — for multicast/broadcast), select (forward to one port from a set — for load balancing with weighted round-robin or hash-based selection), indirect (forward to a single port referenced by the group — for shared actions), and fast failover (forward to the first live port in a set — for link protection).
- **OpenFlow Limitations:** Fixed match fields (the protocol defines which headers can be matched, and adding new protocols requires a new OpenFlow version), limited actions (the protocol defines which actions are supported, and custom actions require vendor extensions), and table size limitations (TCAM memories can hold 1,000-10,000 entries at reasonable cost). These limitations motivated the development of P4.

### Lecture Notes

OpenFlow's match-action processing is the simplest and most powerful abstraction in SDN. Every packet that enters a switch is matched against a set of rules, and the matching rule determines the packet's fate. The match fields can include any combination of packet headers: input port, Ethernet source and destination, VLAN ID, IP source and destination, DSCP, TCP/UDP source and destination ports, and more. The actions can include: forward to a specific port, drop the packet, modify header fields, send the packet to the controller (for further processing), or forward the packet to another flow table for additional processing.

Consider a simple access control policy: "Allow HTTP traffic from subnet 10.0.1.0/24 to server 10.0.10.10, and deny all other traffic." In OpenFlow, this policy is expressed as two flow entries:
1. Priority 100: Match ip_src=10.0.1.0/24, ip_dst=10.0.10.10, tcp_dst=80 → Allow (forward to output port)
2. Priority 10: Match all (wildcard) → Deny (drop)

The first rule has higher priority and matches the allowed traffic; the second rule is a catch-all that denies everything else. When a packet arrives, the switch searches the flow table for the highest-priority matching entry. HTTP traffic from the allowed subnet matches rule 1 and is forwarded. All other traffic matches rule 2 and is dropped.

The flow table pipeline extends this model to multiple stages. Instead of a single flow table with thousands of entries, the pipeline divides the processing into stages. Table 0 handles ingress processing (VLAN tagging, input port filtering), table 1 handles routing (matching on destination IP), table 2 handles firewalling (matching on source/destination IP and TCP/UDP ports), and table 3 handles egress processing (output port selection). Each table has fewer entries than a monolithic flow table, making the pipeline more efficient and easier to manage.

Group tables provide advanced forwarding behaviors that cannot be expressed with simple flow entries. The select group type implements load balancing: traffic to server 10.0.10.10 can be distributed across ports 1, 2, and 3 with weights 50%, 30%, and 20%. The switch selects the output port based on a hash of the packet headers (ensuring that all packets in the same flow go to the same port) or a weighted round-robin (distributing packets proportionally). The fast failover group type provides link protection: traffic is forwarded to port 1 if it is live, port 2 if port 1 fails, and port 3 if ports 1 and 2 fail. The switch monitors the liveness of each port and automatically switches to the next port in the group when the current port fails.

OpenFlow's limitations are significant. The protocol defines a fixed set of match fields and actions — if you want to match a new protocol (e.g., QUIC connection IDs), you must wait for a new OpenFlow version that adds support for the field. The TCAM memories used for flow table storage are expensive and power-hungry, limiting the number of flow entries to a few thousand per table. And the protocol's verbosity (each flow mod message is a complex data structure) makes it difficult to program high-speed switches with millions of entries. These limitations motivated P4, which allows programmers to define custom match fields, actions, and processing pipelines.

### Required Reading

- McKeown, N., et al. (2008). "OpenFlow: Enabling Innovation in Campus Networks." *ACM SIGCOMM CCR*, 38(2), 69-74.
- Open Networking Foundation (2015). "OpenFlow Switch Specification Version 1.5.1." Sections 1-7.
- Yggdrasil SDN Architecture Guide (2040). "OpenFlow Flow Tables" and "Group Tables."

### Discussion Questions

1. Design an OpenFlow flow table pipeline that implements the following policy: (a) drop all traffic from the guest network to the HR network, (b) rate-limit traffic from the student network to the internet to 1 Gbps, (c) allow all other traffic. How many flow tables do you need? What are the match fields and actions for each rule?
2. OpenFlow uses TCAM for flow table storage. TCAM is expensive ($100-500 per 1,000 entries) and power-hungry (15W per 1,000 entries). A switch has 10,000 TCAM entries. Calculate the cost and power consumption for 10,000 entries. If the flow table pipeline has 4 tables, each with 2,500 entries, how does this change the cost analysis?
3. OpenFlow's fixed match fields make it impossible to match on new protocols (e.g., QUIC connection IDs) without a new protocol version. P4 allows custom match fields. What are the tradeoffs between a fixed protocol (OpenFlow) and a programmable protocol (P4)? Consider implementation complexity, verification, and performance.

---

ᚦ **Lecture 3: P4 — Programming the Data Plane**

**Course:** CN301 — Software-Defined Networking (SDN)
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

P4 (Programming Protocol-Independent Packet Processors) extends SDN from the control plane to the data plane. Where OpenFlow defines a fixed set of match fields and actions, P4 allows programmers to define their own — custom headers, custom match-action processing, and custom packet pipelines. This lecture covers the P4 language, architecture, and programming model.

### Key Topics

- **P4 Language Fundamentals:** Header definitions (fixed-width and variable-length headers), parser state machines (extracting headers from packets), match-action tables (matching on header fields and executing actions), control flow (conditional execution and table application), and extern functions (architecture-specific operations like checksums and cloning). P4 is a domain-specific language designed for packet processing — it cannot allocate memory, cannot loop (except in parsers), and cannot make arbitrary function calls.
- **Parser State Machine:** The parser extracts headers from the incoming packet. Each parser state extracts a specific header and transitions to the next state based on the header type. Example: state ethernet extracts the Ethernet header, then transitions to state ipv4 or state ipv6 based on the EtherType. The parser is the only part of P4 that can loop (for variable-length headers like IPv4 options or TCP options).
- **Match-Action Tables:** The core processing element. Each table specifies: the key (which header fields to match on), the actions (what to do with the packet), the default action (what to do if no entry matches), and the size (how many entries the table can hold). Actions can modify header fields (hdr.ipv4.ttl = hdr.ipv4.ttl - 1), set metadata (meta.next_hop = 1), and invoke extern functions (verify_checksum(), clone_packet()).
- **The P4 Architecture Model:** P4 programs are written against a target architecture model (v1model for BMv2, TNA for Intel Tofino, RSA for Cisco). The architecture model defines: the parser, the ingress pipeline (match-action tables that process the packet on ingress), the egress pipeline (match-action tables that process the packet on egress), the deparser (reassembling the packet from modified headers), and the externs (target-specific functions). Programs written for one architecture model cannot run on a different model without modification.
- **P4 in Practice — The Bifrǫst Data Plane:** The Bifrǫst Mesh switches run P4 programs that implement: BTP (Bifrǫst Transport Protocol) header parsing, INT (In-Band Telemetry) header insertion, ECMP (Equal-Cost Multi-Path) forwarding, and ACL processing. The P4 program is compiled for the Intel Tofino2 ASIC, which processes packets at 12.8 Tbps (100 Gbps per port × 128 ports). The Norn controller installs flow rules into the P4 match-action tables via the P4Runtime API.

### Lecture Notes

P4's philosophy is "program the data plane, not just the control plane." OpenFlow recognizes a fixed set of protocols (Ethernet, IPv4, IPv6, TCP, UDP, etc.) and a fixed set of actions (forward, drop, modify, send to controller). P4 says: "Don't constrain the data plane to a fixed set of protocols. Let the programmer define the protocols." With P4, you can define a new header (e.g., BTP, the Bifrǫst Transport Protocol), write a parser that extracts BTP headers from packets, create match-action tables that match on BTP fields, and define actions that modify BTP headers. The data plane is no longer limited to the protocols that the switch vendor anticipated — it can process any protocol that the programmer defines.

The parser is the entry point of a P4 program. It takes a raw packet (a sequence of bytes) and extracts headers from it. The parser is a state machine: each state extracts one header and determines the next state based on the header's type or other conditions. For example, the Ethernet state extracts the Ethernet header, then transitions to the IPv4 state if EtherType == 0x0800, the IPv6 state if EtherType == 0x86DD, or the MPLS state if EtherType == 0x8847. The parser continues until it reaches the accept state (all headers extracted) or the reject state (the packet is malformed). After parsing, the packet is represented as a set of header objects (hdr.ethernet, hdr.ipv4, hdr.tcp, etc.), which can be matched, modified, and acted upon by match-action tables.

The P4 program for the Bifrǫst Mesh data plane illustrates the language's power. The program begins with a parser that extracts Ethernet, IPv6, BTP, and INT headers from the incoming packet. The ingress pipeline contains five match-action tables:
1. **Ingress port check:** Drop packets from unauthorized ports.
2. **BTP routing:** Match on BTP connection ID, set the output port and next-hop address.
3. **ECMP forwarding:** Match on the packet's flow hash, select an output port from a group of equal-cost paths.
4. **ACL processing:** Match on source/destination IP and port, allow or deny.
5. **INT insertion:** Insert an In-Band Telemetry header that records the switch ID, ingress timestamp, and egress timestamp.

The egress pipeline contains two tables:
1. **Egress port check:** Drop packets destined for unauthorized ports.
2. **QoS remarking:** Set the DSCP field based on the BTP flow type (e.g., high priority for real-time traffic, best effort for bulk traffic).

The deparser reassembles the modified headers back into a packet and sends it to the output port. The entire processing pipeline executes in hardware at line rate — every packet is processed in a single pass through the ASIC pipeline, with no per-packet CPU involvement.

P4Runtime is the control plane API for P4 programs. Where OpenFlow uses a fixed protocol to install flow rules, P4Runtime uses a protocol buffer (protobuf) API that is generated from the P4 program itself. The controller sends P4Runtime messages to install entries in the match-action tables, read counters, and receive packet-in messages. The advantage of P4Runtime over OpenFlow: the API is tailored to the specific P4 program, so the controller can access BTP fields, INT headers, and other custom constructs that OpenFlow does not support. The Norn controller uses P4Runtime to communicate with the Bifrǫst switches, installing BTP routing rules, ECMP groups, ACL entries, and INT configurations.

### Required Reading

- Bosshart, P., et al. (2014). "P4: Programming Protocol-Independent Packet Processors." *ACM SIGCOMM CCR*, 44(3), 87-95.
- P4 Language Consortium (2036). *P416 Language Specification*, v1.2. Chapters 1-8.
- Yggdrasil SDN Architecture Guide (2040). "Bifrǫst Data Plane P4 Program" and "P4Runtime API."

### Discussion Questions

1. Write a P4 parser that extracts Ethernet, IPv4, and TCP headers. What happens when a packet has an IPv4 header with options (variable length)? How does the parser handle this?
2. Design a P4 match-action table that implements ECMP forwarding: given a flow hash and an ECMP group ID, select one of N output ports. How would the controller install entries in this table? What is the maximum number of ECMP groups and paths per group that the table can support?
3. P4 programs are compiled for specific target architectures (Tofino, BMv2, NICs). Can a P4 program written for Tofino run on BMv2? What are the portability challenges? How does the P4 architecture model affect portability?

---

ᚬ **Lecture 4: SDN Controllers — ONOS, ODL, and the Norn Architecture**

**Course:** CN301 — Software-Defined Networking (SDN)
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

The SDN controller is the brain of the network — the software that has a global view of the network topology, computes paths, installs flow rules, and responds to events. This lecture covers controller architectures, the ONOS and OpenDaylight controllers, and the Bifrǫst Norn controller.

### Key Topics

- **Controller Architecture:** The SDN controller sits between the network applications (which define what the network should do) and the switches (which forward packets). Northbound interfaces (NBIs): REST APIs, Java/Python APIs, intent frameworks. Southbound interfaces (SBIs): OpenFlow, P4Runtime, NETCONF, gNMI. The controller's internal services: topology discovery, host tracking, path computation, flow rule management, and distributed coordination.
- **ONOS (Open Network Operating System):** The open-source SDN controller developed by the ON.Lab (now part of the Linux Foundation). ONOS features: distributed architecture (multiple controller instances for high availability), intent-based northbound API (applications express intent, ONOS figures out how to implement it), and modular services (topology, device, link, host, flow objective, and intent frameworks). ONOS is used by service providers (AT&T, Comcast) for large-scale production networks.
- **OpenDaylight (ODL):** The open-source SDN controller developed by the Linux Foundation. ODL features: model-driven architecture (all configuration and state modeled in YANG), pluggable southbound protocols (OpenFlow, NETCONF, gNMI, RESTCONF), and a rich ecosystem of applications (L2/L3 forwarding, VPN, QoS). ODL is used in enterprise and data center networks.
- **The Norn Controller:** Yggdrasil's production SDN controller, built on ONOS with custom modules for the Bifrǫst Mesh. The Norn controller adds: BTP routing (computing paths through the Bifrǫst Mesh and installing flow rules), INT telemetry collection (processing In-Band Telemetry reports from switches), Heimdall security integration (reacting to security events by installing flow rules), and Verdandi predictive control (predicting traffic patterns and pre-installing flow rules before they are needed).
- **Controller High Availability:** Multiple controller instances running in active-active mode, sharing network state through a distributed data store (Raft consensus for ONOS, Atomix for ODL). When a controller instance fails, its switches reconnect to another instance, and the application state is preserved. The Norn controller runs three instances: two active (in Oslo and Bergen) and one standby (in Tromsø). If an active instance fails, the standby takes over within 5 seconds.

### Lecture Notes

The SDN controller is the most complex component of the SDN architecture, and its design determines the network's reliability, scalability, and programmability. The controller must maintain a global view of the network topology (which switches are connected to which, which hosts are on which switches), compute paths through the network (shortest path, widest path, ECMP), install flow rules on switches (via OpenFlow, P4Runtime, or other southbound protocols), and respond to events (link failures, new hosts, policy changes). All of this must happen in real time — a link failure must be detected and corrected within 50 ms to avoid disrupting real-time applications.

ONOS's distributed architecture is the key to its scalability. Multiple ONOS instances form a cluster, with each instance connected to a subset of switches. The instances share state through a distributed data store based on the Raft consensus algorithm. When an application on one instance installs an intent (e.g., "connect host A to host B"), all instances learn about the intent via the data store, and the instance that controls the relevant switches installs the flow rules. If an instance fails, the other instances detect the failure (via Raft heartbeats) and the switches reconnect to a surviving instance. The failover is transparent to applications — they continue operating as if nothing happened, because the intent state is preserved in the distributed data store.

The Norn controller extends ONOS with four custom modules. The BTP routing module computes optimal paths through the Bifrǫst Mesh using a modified Dijkstra algorithm that accounts for link capacity, latency, and policy constraints (e.g., "don't route guest traffic through the research network"). The INT telemetry module processes In-Band Telemetry reports from switches, extracting per-hop latency, queue depth, and link utilization data, and feeding it to the Verdandi predictive module. The Heimdall security integration module receives security events from the Heimdall neural IDS (e.g., "host 10.0.1.5 is scanning the network") and responds by installing flow rules that block the offending host. The Verdandi predictive module uses machine learning to predict traffic patterns and pre-install flow rules before they are needed, reducing the path installation time from 50 ms to 5 ms.

The intent-based northbound API is the Norn controller's most powerful abstraction. Instead of specifying exact flow rules (match on source IP, destination IP, and TCP port, forward to port 5), the application expresses an intent: "Connect host A to server B with low latency." The Norn controller translates this intent into concrete flow rules: it computes the shortest path from host A to server B, installs flow rules on every switch along the path, and monitors the path for failures. If a link fails, the Norn controller recomputes the path and installs new flow rules automatically. The application never needs to know about the network topology, the switches, or the flow rules — it expresses what it wants, and the Norn controller figures out how to do it.

### Required Reading

- Berde, P., et al. (2014). "ONOS: Towards an Open Network Operating System." *ACM SIGCOMM 2014*.
- OpenDaylight Documentation (2040). "Architecture Guide" and "Northbound APIs."
- Yggdrasil SDN Architecture Guide (2040). "Norn Controller Design" and "Intent Framework."

### Discussion Questions

1. The Norn controller uses a distributed data store (Raft) to share state between instances. Raft ensures consistency (all instances see the same state) but adds latency (each write must be replicated to a majority of instances before it is committed). How does this latency affect the controller's reaction time to network events (link failures, new hosts)?
2. The intent-based northbound API allows applications to express what they want (e.g., "connect host A to server B") without specifying how. What happens when two intents conflict (e.g., "connect host A to server B" and "block all traffic from host A")? Design a conflict resolution algorithm that handles intent conflicts.
3. The Norn controller pre-installs flow rules based on predicted traffic patterns. If the prediction is wrong, the pre-installed rules waste TCAM entries on switches. How would you balance the benefit of pre-installation (faster path setup) against the cost of wasted TCAM entries?

---

ᚱ **Lecture 5: Network Function Virtualization (NFV)**

**Course:** CN301 — Software-Defined Networking (SDN)
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Network functions — firewalls, load balancers, intrusion detection systems, WAN optimizers — were traditionally implemented in purpose-built hardware appliances. NFV moves these functions to software running on commodity servers. This lecture covers the NFV architecture, virtual network functions (VNFs), the ETSI NFV framework, and the 2040 evolution toward cloud-native network functions (CNFs).

### Key Topics

- **The NFV Value Proposition:** Replace expensive, proprietary hardware appliances with software running on commodity servers. Benefits: cost reduction (commodity servers vs. proprietary appliances), flexibility (deploy new functions in minutes, not months), scalability (add capacity by adding servers, not buying new appliances), and innovation (deploy new functions without waiting for vendor releases). The 2040 savings: enterprises that virtualized 80% of their network functions reduced their network equipment costs by 60%.
- **ETSI NFV Framework:** The reference architecture defined by ETSI (European Telecommunications Standards Institute). Components: VNF (Virtual Network Function — the software implementation of a network function), VNFM (VNF Manager — lifecycle management of VNFs), NFVI (NFV Infrastructure — the compute, storage, and networking resources), VIM (Virtual Infrastructure Manager — OpenStack, Kubernetes), and NFVO (NFV Orchestrator — end-to-end service orchestration). The MANO (Management and Orchestration) framework: NFVO, VNFM, and VIM.
- **Virtual Network Functions (VNFs):** Software implementations of network functions: virtual firewall (vFW), virtual load balancer (vLB), virtual intrusion detection system (vIDS), virtual WAN optimizer (vWOC), and virtual router (vRouter). VNFs are packaged as VM images or containers. The 2040 state: most VNFs are containerized, running as pods in a Kubernetes cluster.
- **Service Function Chaining (SFC):** Directing traffic through a sequence of VNFs in a specific order. For example, all internet traffic must pass through: vFW (firewall) → vIDS (intrusion detection) → vLB (load balancer) → destination. SFC in SDN: the controller installs flow rules that steer traffic through the VNFs in the specified order. The OpenFlow approach: each VNF has a dedicated flow table, and the pipeline directs packets from one VNF to the next.
- **Cloud-Native Network Functions (CNFs):** The 2040 evolution of NFV: VNFs redesigned as cloud-native applications, running in containers managed by Kubernetes, with automatic scaling, self-healing, and rolling updates. CNFs vs. VNFs: VNFs are legacy network functions lifted-and-shifted to VMs; CNFs are network functions redesigned for the cloud. The Bifrǫst Mesh runs all network functions as CNFs in a Kubernetes cluster, with the Norn controller orchestrating SFC and scaling.

### Lecture Notes

The key insight of NFV is that most network functions are software — they process packets, maintain state, and apply policies. The hardware (ASICs, FPGAs, custom blades) is not necessary for the function; it is necessary for the performance. But as commodity servers have become more powerful (100 Gbps NICs, advanced instruction sets like DPDK and SR-IOV), the performance gap between software and hardware has narrowed. A virtual firewall running on a commodity server with DPDK-accelerated NICs can process 50 Gbps of traffic — more than enough for most enterprise deployments.

The ETSI NFV framework defines a layered architecture. At the bottom is the NFV Infrastructure (NFVI): compute (servers with x86/ARM CPUs), storage (SSDs, NVMe), and networking (switches, NICs). On top of the NFVI runs the Virtual Infrastructure Manager (VIM), which is typically OpenStack (for VMs) or Kubernetes (for containers). The VIM manages resource allocation: creating VMs or pods, attaching networks, and managing storage. Above the VIM is the VNF Manager (VNFM), which manages the lifecycle of Virtual Network Functions: creating, scaling, and deleting VNF instances. At the top is the NFV Orchestrator (NFVO), which manages end-to-end services: creating a service chain of VNFs, connecting them in the right order, and monitoring the service.

Service Function Chaining (SFC) is the mechanism that directs traffic through a sequence of VNFs. In traditional networking, SFC is implemented by physical cabling: traffic enters the firewall, exits to the IDS, exits to the load balancer, and reaches the destination. In SDN, SFC is implemented by flow rules: the controller installs rules that steer packets from one VNF to the next. The Bifrǫst Mesh uses SFC for all traffic entering the campus network: every packet passes through a virtual firewall (policy enforcement), a virtual IDS (threat detection), and a virtual load balancer (traffic distribution) before reaching its destination. The Norn controller manages the SFC, installing flow rules that direct traffic from one VNF to the next.

The evolution from VNFs to CNFs is the most significant change in NFV since its inception. VNFs are legacy network functions packaged as VM images: they take minutes to boot, require dedicated resources (CPU, memory, storage), and are difficult to scale. CNFs are network functions redesigned as cloud-native applications: they are containerized (boot in seconds, not minutes), microservice-based (each function is a separate service), and orchestrated by Kubernetes (automatic scaling, self-healing, rolling updates). The Bifrǫst Mesh's Heimdall IDS was originally a VNF (a Suricata instance running in a VM). It has been redesigned as a CNF: a container that runs Suricata with DPDK acceleration, scales horizontally (multiple containers for high traffic), and can be updated in seconds (rolling update without traffic disruption). The performance improvement: the CNF processes 25 Gbps per container, and the system can scale to 100+ Gbps by adding more containers.

### Required Reading

- ETSI (2034). "Network Functions Virtualisation (NFV) Architectural Framework," GS NFV 002 v3.1.1. Chapters 4-7.
- Mijumbi, R., et al. (2036). "Network Function Virtualization: State-of-the-Art and Research Challenges." *IEEE Communications Surveys & Tutorials*, 18(1), 236-262.
- Yggdrasil NFV Architecture Guide (2040). "CNF Architecture" and "Service Function Chaining."

### Discussion Questions

1. A virtual firewall running on a commodity server processes 50 Gbps. A hardware firewall processes 100 Gbps on a dedicated ASIC. Under what conditions is the virtual firewall preferable? Consider cost, flexibility, scalability, and performance.
2. Design a service function chain for a campus network: all traffic must pass through vFW → vIDS → vLB before reaching the destination. Draw the topology, including the SDN switches that steer traffic through the VNFs. What happens if the vIDS fails? How does the SFC gracefully handle VNF failures?
3. CNFs run in containers managed by Kubernetes. A CNF (Heimdall IDS) needs to process traffic at 25 Gbps per container. How does traffic get from the physical NIC to the container without going through the kernel network stack? Consider DPDK, SR-IOV, and AF_XDP.

---

ᚴ **Lecture 6: Intent-Based Networking — From Rules to Intentions**

**Course:** CN301 — Software-Defined Networking (SDN)
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Intent-based networking (IBN) is the evolution of SDN: instead of programming individual flow rules, the operator declares intent ("ensure all traffic is encrypted"), and the network figures out how to implement it. This lecture covers intent abstraction, the intent lifecycle, verification, and the Norn intent framework.

### Key Topics

- **The Intent Abstraction:** An intent is a high-level declaration of what the network should do, without specifying how. Examples: "Connect host A to server B with latency < 10ms," "Ensure all traffic between department X and department Y is encrypted," "Rate-limit guest Wi-Fi to 100 Mbps." The network controller translates each intent into concrete configuration (flow rules, ACL entries, QoS policies) and continuously verifies that the intent is satisfied.
- **The Intent Lifecycle:** (1) Create: the operator defines an intent. (2) Compile: the controller translates the intent into concrete rules. (3) Install: the controller pushes the rules to the switches. (4) Verify: the controller monitors the network to confirm that the intent is satisfied. (5) React: if the intent is violated (e.g., a link failure breaks the connectivity intent), the controller recomputes and reinstalls the rules. (6) Withdraw: the operator removes the intent, and the controller removes the corresponding rules.
- **Intent Verification:** The most critical phase of the intent lifecycle. After installing rules, the controller must verify that they achieve the operator's intent. Verification methods: reachability testing (can host A reach server B?), latency measurement (is the path latency < 10ms?), bandwidth measurement (is the available bandwidth > 1 Gbps?), and security verification (is the traffic encrypted?). The Norn controller verifies intents every 30 seconds using In-Band Telemetry (INT) reports from switches.
- **Intent Conflict Resolution:** Two intents may conflict: "Block all traffic from the guest network to the HR network" and "Allow the guest network to access the HR web server." The controller must detect conflicts (by analyzing the compiled rules) and resolve them (by applying the more specific intent: allow traffic to the HR web server, but block all other traffic to the HR network). Conflict resolution policies: priority-based (higher-priority intents override lower-priority ones), specificity-based (more specific intents override less specific ones), and operator-defined (the operator specifies which intent takes precedence).
- **The Norn Intent Framework:** Yggdrasil's intent implementation, built on ONOS's intent framework with custom extensions. Intents are defined in YAML (declarative) or Python (programmatic). The Norn compiler translates intents into P4Runtime rules, installs them on Bifrǫst switches, and verifies them using INT telemetry. Conflict resolution uses the specificity principle: more specific intents (e.g., "allow HTTP to HR web server") override more general intents (e.g., "block all traffic to HR network").

### Lecture Notes

Intent-based networking is the most significant advance in network management since SDN itself. The key insight: network operators should not need to know about switches, flow rules, or routing protocols to manage their network. They should express what they want ("connect these two sites with low latency") and the network should figure out how to do it. This abstraction is analogous to high-level programming languages: a Python programmer does not need to know about CPU registers or memory management to write a program; the compiler figures out the low-level details. Similarly, an intent-based network operator does not need to know about flow rules or routing protocols; the Norn controller figures out the low-level details.

The intent lifecycle is the core of IBN. When an operator creates an intent ("Connect host A to server B with latency < 10ms"), the Norn controller compiles it into concrete rules: it computes the shortest path from host A to server B (taking into account the latency constraint), installs P4Runtime rules on every switch along the path, and monitors the path using INT telemetry. If a link fails and the latency exceeds 10ms, the Norn controller detects the violation, recomputes the path (finding an alternative route that meets the latency constraint), and installs new rules on the affected switches. The operator never needs to intervene — the Norn controller handles the failure automatically.

Intent verification is the most technically challenging phase. After installing rules, how does the controller know that they actually achieve the intent? For connectivity intents, the controller can send probe packets and verify that they reach the destination. For latency intents, the controller can measure the round-trip time using INT telemetry (each switch in the path records its ingress and egress timestamps). For bandwidth intents, the controller can measure the link utilization using traffic counters. For security intents (e.g., "all traffic is encrypted"), the controller can verify that MACsec or IPsec is enabled on every link in the path. The Norn controller performs these verifications continuously (every 30 seconds) and raises an alert if any intent is violated.

Conflict resolution is where IBN becomes difficult. Consider two intents: Intent 1 ("Block all traffic from the guest network to the HR network") and Intent 2 ("Allow guest network to access the HR web server at 10.0.10.10 on port 443"). These intents are contradictory: Intent 1 blocks all guest-to-HR traffic, while Intent 2 allows specific guest-to-HR traffic. The Norn controller resolves this conflict using the specificity principle: Intent 2 is more specific (it names a specific server and port) than Intent 1 (it names entire networks), so Intent 2 takes precedence. The compiled rules reflect this: traffic from the guest network to 10.0.10.10 on port 443 is allowed; all other guest-to-HR traffic is blocked. The specificity principle is simple and intuitive, but it can be overridden by the operator if needed (e.g., a security lockdown intent that blocks all traffic regardless of specificity).

### Required Reading

- Leivadeas, A., et al. (2033). "A Survey on Intent-Based Networking." *IEEE Communications Surveys & Tutorials*, 21(4), 3485-3519.
- ONOS Wiki (2040). "Intent Framework" and "Intent Conflict Resolution."
- Yggdrasil SDN Architecture Guide (2040). "Norn Intent Framework" and "Verification."

### Discussion Questions

1. An operator defines two intents: "Connect branch office to headquarters with bandwidth > 500 Mbps" and "Rate-limit all branch office traffic to 100 Mbps." The second intent is more specific about the bandwidth. Which intent takes precedence? Design a conflict resolution algorithm that handles this case.
2. Intent verification requires the controller to continuously monitor the network. If the controller fails to verify an intent (e.g., the INT telemetry path is broken), should it keep the existing rules in place or remove them? What are the risks of each approach?
3. The Norn intent framework uses the specificity principle: more specific intents override more general ones. Design an alternative conflict resolution algorithm based on priorities (each intent has an explicit priority). What are the advantages and disadvantages of the priority approach compared to specificity?

---

ᚺ **Lecture 7: Network Virtualization — VLANs, VRFs, VXLANs, and Beyond**

**Course:** CN301 — Software-Defined Networking (SDN)
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Network virtualization creates multiple logical networks on a single physical infrastructure. This lecture covers VLANs, VRFs, VXLANs, and the 2040 landscape of overlay networks, exploring how SDN enables virtualization at every layer.

### Key Topics

- **VLANs (Virtual LANs):** Layer 2 network segmentation using 802.1Q tags. Each Ethernet frame carries a 12-bit VLAN ID (0-4095), allowing up to 4,094 VLANs on a single physical infrastructure. VLANs provide broadcast domain isolation (frames in one VLAN are not forwarded to another VLAN), security isolation (traffic between VLANs must pass through a router or firewall), and QoS marking (the 802.1p field in the VLAN tag provides 8 priority levels). Limitations: 4,094 VLANs maximum, manual configuration on every switch, and STP convergence on topology changes.
- **VRFs (Virtual Routing and Forwarding):** Layer 3 network segmentation. Each VRF has its own routing table, allowing multiple independent routing domains on a single router. Example: a service provider router with three VRFs (customer A, customer B, and management), each with its own routing table and interfaces. VRF-lite (local VRFs on a single router) vs. MPLS-based VRFs (VRFs extended across the network using MPLS VPNs). The 2040 state: VRFs are used for multi-tenancy in data centers and enterprise networks.
- **VXLANs (Virtual eXtensible LANs):** Layer 2 overlay networks encapsulated in UDP. VXLAN extends VLAN by using a 24-bit VNI (VXLAN Network Identifier), allowing up to 16 million virtual networks. VXLAN encapsulates Ethernet frames in UDP/IP, enabling Layer 2 connectivity across Layer 3 networks. VTEPs (VXLAN Tunnel Endpoints) encapsulate and decapsulate VXLAN packets. VXLAN enables the Bifrǫst Mesh to provide Layer 2 connectivity across all campuses.
- **Overlay Networks and Encapsulation:** The overlay model: create virtual networks on top of a physical underlay. Encapsulation: VXLAN (Ethernet in UDP), GRE (any protocol in IP), GENEVE (generic network virtualization encapsulation — the 2040 standard). The overlay advantage: virtual networks are independent of the physical topology, enabling multi-tenancy, mobility, and flexible provisioning. The overlay challenge: encapsulation adds overhead (VXLAN adds 50 bytes per packet), creates MTU issues, and makes troubleshooting difficult (the underlay and overlay are separate networks).
- **The Bifrǫst Mesh Virtual Fabric:** The Bifrǫst Mesh uses GENEVE encapsulation over an IPv6 underlay. Each campus has its own VNI (Virtual Network Identifier), and the Norn controller programs VTEPs on all campus switches. When a packet from the Oslo campus needs to reach the Bergen campus, the switch encapsulates it in a GENEVE header with VNI=100 (Oslo) and sends it through the IPv6 underlay to the Bergen VTEP, which decapsulates it and delivers it to the local network. The Norn controller manages the VNI allocation, VTEP configuration, and underlay routing.

### Lecture Notes

VLANs are the oldest and simplest form of network virtualization, and they remain the most widely deployed. The 802.1Q standard adds a 4-byte tag to each Ethernet frame, containing a 12-bit VLAN ID, a 3-bit priority field (802.1p), and a 1-bit canonical format indicator. Switches use the VLAN ID to determine which ports can receive the frame: trunk ports carry frames for all VLANs, and access ports carry frames for a single VLAN. The limitation of 4,094 VLANs (2^12 - 2 reserved IDs) may seem generous for a single building, but it is insufficient for large data centers that need millions of virtual networks. VXLAN addresses this limitation with a 24-bit VNI, allowing up to 16 million virtual networks.

The key insight of overlay networking is the separation of the underlay (the physical network that carries encapsulated packets) from the overlay (the virtual network that tenants see). Tenants configure their overlay networks as if they have a dedicated Layer 2 domain — they can use any VLAN IDs, IP subnets, and MAC addresses they want, without coordinating with other tenants. The underlay is managed by the infrastructure team and carries encapsulated packets between VTEPs. This separation of concerns is analogous to the SDN separation of control and data planes: the overlay is the "control plane" (defining virtual network topology), and the underlay is the "data plane" (carrying encapsulated packets).

GENEVE is the 2040 encapsulation standard, designed to address the limitations of VXLAN (fixed header format, limited extensibility) and GRE (no network identifier, limited metadata). GENEVE uses a Type-Length-Value (TLV) format for the header, allowing arbitrary metadata to be carried in the encapsulation. For example, a GENEVE header can carry: the VNI (virtual network identifier), the source and destination tenant IDs, security context (encryption metadata), and telemetry data (ingress timestamp, hop count). The Bifrǫst Mesh uses GENEVE to carry INT telemetry from the source VTEP to the destination VTEP, enabling end-to-end latency measurement across the overlay.

The Bifrǫst Mesh Virtual Fabric is a multi-campus overlay network that provides Layer 2 connectivity across all Yggdrasil campuses. Each campus has its own VNI: Oslo is VNI 100, Bergen is VNI 200, Tromsø is VNI 300. The underlay is an IPv6 network that provides point-to-point connectivity between all campuses. When a VM in Oslo needs to communicate with a VM in Bergen, the Oslo VTEP encapsulates the Ethernet frame in a GENEVE header with VNI=100 and sends it through the IPv6 underlay to the Bergen VTEP. The Bergen VTEP decapsulates the frame and delivers it to the local network. The VMs are unaware of the overlay — they see a flat Layer 2 network that spans all campuses.

### Required Reading

- Garg, P. & Wang, Y. (2014). "Virtual eXtensible Local Area Network (VXLAN): A Framework for Overlaying Virtualized Layer 2 Networks over Layer 3 Networks," RFC 7348. IETF.
- GENEVE (2035). "Geneve: Generic Network Virtualization Encapsulation," RFC 8926 (updated). IETF.
- Yggdrasil SDN Architecture Guide (2040). "Virtual Fabric" and "GENEVE Configuration."

### Discussion Questions

1. A data center needs 100,000 virtual networks. VLANs can support 4,094 virtual networks. Calculate how many VLANs are needed for 100,000 virtual networks using the VXLAN 24-bit VNI. Is VXLAN sufficient for this scale? What are the memory and processing implications of 100,000 VTEP entries?
2. GENEVE encapsulation adds 50-100 bytes of overhead per packet. If the underlay MTU is 1500 bytes, what is the effective MTU for the overlay? Calculate the throughput reduction for a 64-byte overlay packet (a TCP ACK) with and without GENEVE encapsulation.
3. The Bifrǫst Mesh Virtual Fabric provides Layer 2 connectivity across all campuses. A broadcast packet (e.g., an ARP request) sent by a VM in Oslo will be flooded to all VMs in the Oslo overlay network, including VMs in Bergen and Tromsø. Design a mechanism to limit broadcast flooding to the local campus while still allowing cross-campus unicast communication.

---

ᚬ **Lecture 8: In-Band Network Telemetry (INT) and Network Analytics**

**Course:** CN301 — Software-Defined Networking (SDN)
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

You cannot manage what you cannot measure. In-Band Network Telemetry (INT) embeds telemetry data directly into data packets, providing per-hop visibility into latency, queue depth, and link utilization without relying on separate monitoring protocols. This lecture covers INT, network analytics, and the Bifrǫst INT architecture.

### Key Topics

- **Traditional Network Monitoring:** SNMP (polling counters on devices — slow, coarse), NetFlow/sFlow (sampling packets and exporting metadata — partial visibility), and ping/traceroute (active probing — measures one path, not all paths). The problem: traditional monitoring cannot provide per-hop, per-packet visibility. You can measure the end-to-end latency (with ping), but you cannot measure the individual hop latencies that make up the end-to-end latency.
- **In-Band Network Telemetry (INT):** Embedding telemetry data directly into data packets. Each switch in the path inserts its own telemetry data: switch ID, ingress timestamp, egress timestamp, queue depth, and link utilization. The destination extracts the telemetry data and sends it to a collector for analysis. INT provides per-hop, per-packet visibility without additional measurement traffic.
- **INT Header Format:** The INT header is inserted after the Ethernet header (or after the GENEVE header in overlay networks). Fields: INT type (hop-by-hop or end-to-end), length, instruction bitmask (which fields to insert), and per-hop data (switch ID, ingress time, egress time, queue depth, utilization). The instruction bitmask allows the controller to specify which fields each switch should insert, reducing overhead.
- **INT in P4:** Implementing INT in the P4 data plane. Each switch's ingress pipeline records the ingress timestamp, and the egress pipeline appends the switch ID, ingress/egress timestamps, and queue depth. The P4 program adds an INT header to each packet (or to sampled packets to reduce overhead) and passes it to the next switch. The final switch (or the destination) extracts the INT header and sends it to the collector.
- **The Bifrǫst INT Architecture:** Every Bifrǫst switch runs INT, inserting telemetry data into every packet (for critical flows) or every 100th packet (for best-effort flows). The INT collector receives telemetry reports, correlates them with flow data, and feeds them to the Norn controller (for intent verification) and the Verdandi predictive module (for traffic prediction). The INT collector processes 10 million telemetry reports per second and stores per-flow, per-hop latency data for the last 24 hours.

### Lecture Notes

Traditional network monitoring is fundamentally limited by its measurement model. SNMP polls device counters every 5 minutes — far too slow to detect transient congestion that lasts seconds. NetFlow samples 1 in 100 packets — it can tell you that 1% of traffic is experiencing high latency, but it cannot tell you which packets experienced which latency. Ping measures the end-to-end round-trip time — but it cannot identify which hop in the path is causing the delay.

INT solves this by embedding telemetry data directly into the packets that carry user traffic. Each switch in the path inserts its own data: "I am switch 42, the packet entered at T=1000.000 and exited at T=1000.005, the queue depth was 3 packets, and the link utilization was 45%." The destination extracts all of this data and sends it to the collector. The result: per-hop, per-packet visibility into the network's internal state. You can now answer questions like "Which hop is adding the most latency?", "Where is the congestion?", and "Is the network satisfying the intent?"

The P4 implementation of INT is straightforward. The ingress pipeline records the ingress timestamp (using the switch's internal clock) and stores it in a metadata field. The egress pipeline reads the metadata and constructs an INT header that contains: the switch ID (a 32-bit identifier), the ingress timestamp, the egress timestamp (recorded at egress), the egress queue depth (the number of packets in the output queue at egress time), and the egress port utilization (the percentage of link bandwidth in use at egress time). The INT header is inserted after the GENEVE header, so it is transparent to end hosts (which ignore unknown headers).

The Bifrǫst INT Architecture processes 10 million telemetry reports per second. Each report contains: the flow key (source IP, destination IP, source port, destination port, protocol), the path (list of switch IDs), per-hop latency (ingress to egress time at each hop), per-hop queue depth, and per-hop link utilization. The collector stores this data in a time-series database and feeds it to three consumers: (1) the Norn controller, which uses per-flow latency data to verify connectivity and latency intents; (2) the Verdandi predictive module, which uses traffic patterns to predict future congestion and pre-install flow rules; and (3) the Heimdall security module, which uses anomaly detection to identify suspicious traffic patterns (e.g., a flow that traverses an unusual path).

The overhead of INT is manageable. Each hop adds approximately 20-30 bytes to the packet (switch ID, two timestamps, queue depth, utilization). For a path of 10 hops, INT adds 200-300 bytes. For a 1500-byte packet, this is a 13-20% overhead. To reduce overhead for best-effort flows, INT can be applied to sampled packets (every 1 in 100) instead of every packet. The sampled data provides statistical visibility (latency percentiles, average queue depth) without the overhead of per-packet telemetry.

### Required Reading

- Kim, C., et al. (2015). "In-Band Network Telemetry (INT)." *P4 Community Whitepaper*.
- Inutsuka, S., et al. (2037). "Real-Time Network Analytics with In-Band Telemetry." *IEEE Transactions on Network and Service Management*, 14(3), 681-694.
- Yggdrasil SDN Architecture Guide (2040). "INT Architecture" and "Telemetry Pipeline."

### Discussion Questions

1. INT adds approximately 30 bytes per hop. A flow traverses 20 hops. Calculate the total INT overhead for a 1500-byte packet. Is this overhead acceptable? What are the tradeoffs between per-packet INT and sampled INT (1 in 100 packets)?
2. INT timestamps are recorded using each switch's internal clock. If the switches' clocks are not synchronized (clock skew), the per-hop latency measurements will be inaccurate. How can clock synchronization be achieved in a data center? Consider PTP (Precision Time Protocol), NTP, and hardware timestamping.
3. The Bifrǫst INT collector processes 10 million reports per second. Each report is approximately 200 bytes (flow key + 10 hops of telemetry data). Calculate the data rate (in Gbps). What storage technology would you use to store 24 hours of telemetry data? How many terabytes of storage are needed?

---

ᚱ **Lecture 9: SDN Security — Attacks and Defenses**

**Course:** CN301 — Software-Defined Networking (SDN)
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Centralized control creates a single point of failure and a high-value target. This lecture covers the security challenges of SDN: attacks on the controller, attacks on the data plane, attacks on the control channel, and the Bifrǫst Mesh's defense-in-depth approach.

### Key Topics

- **SDN Threat Model:** The controller is the highest-value target: if compromised, the attacker controls the entire network. The control channel (between controller and switches) is a man-in-the-middle target: if intercepted, the attacker can inject, modify, or drop flow rules. The data plane is a denial-of-service target: if flooded with new flows, the switch's TCAM overflows and packets are dropped or sent to the controller (creating a feedback loop). The northbound API is a privilege escalation target: if compromised, the attacker can install arbitrary intents.
- **Controller Security:** Securing the controller: TLS-encrypted communication (controller-switch, controller-controller), role-based access control (RBAC) for the northbound API, and input validation (rejecting malformed intents). The Norn controller uses mTLS (mutual TLS) for all communication, RBAC with four roles (admin, operator, viewer, auditor), and intent validation (syntactic and semantic checks before compilation).
- **Control Channel Security:** The channel between the controller and switches must be authenticated and encrypted. OpenFlow uses TLS for the control channel, but many deployments disable TLS for simplicity. P4Runtime uses gRPC with TLS. The Bifrǫst Mesh uses mTLS for all P4Runtime connections, with mutual certificate authentication (the controller verifies the switch's certificate, and the switch verifies the controller's certificate).
- **Data Plane Security:** Preventing data plane attacks: rate limiting packet-in messages (to prevent the controller from being overwhelmed), TCAM overflow protection (dropping packets that don't match TCAM entries instead of sending them to the controller), and flow rule verification (the controller periodically audits switch flow tables to detect unauthorized rules). The Heimdall neural IDS monitors the data plane for suspicious patterns (e.g., a switch that suddenly has an unusual number of flow rules).
- **Denial-of-Service in SDN:** The controller saturation attack: an attacker sends packets that trigger packet-in messages (packets that don't match any flow rule are sent to the controller for processing). If the controller is overwhelmed with packet-in messages, it cannot process legitimate events. Defense: rate limiting packet-in messages per switch, prioritizing control traffic over data traffic, and using wildcard rules to handle common traffic without involving the controller.

### Lecture Notes

The SDN controller is the most critical — and most vulnerable — component of the SDN architecture. In a traditional network, compromising one router does not give the attacker control of the entire network (the other routers continue operating independently). In an SDN network, compromising the controller gives the attacker control of every switch — they can install arbitrary flow rules, create holes in firewalls, redirect traffic to malicious destinations, or drop all traffic. This centralization of control is both SDN's greatest strength (centralized visibility and management) and its greatest vulnerability (single point of failure).

The Norn controller mitigates this risk with defense in depth. The first layer is network security: the controller runs on a dedicated management network that is physically separated from the data network. The second layer is authentication: all communication with the controller (both northbound and southbound) uses mutual TLS with certificate authentication. The third layer is authorization: the northbound API uses role-based access control, with four roles: admin (full access), operator (install and withdraw intents), viewer (read-only access), and auditor (read access to logs and telemetry). The fourth layer is input validation: every intent is checked for syntactic correctness (valid YAML/JSON format) and semantic correctness (the intent must be achievable given the network topology and policies).

The data plane denial-of-service attack is particularly insidious. In a traditional network, a switch forwards packets based on its local routing table, which is pre-populated by routing protocols. In an SDN network, a switch forwards packets based on flow rules installed by the controller. If a packet does not match any flow rule, the switch sends it to the controller as a packet-in message, and the controller installs a new flow rule. An attacker can exploit this by sending many packets that don't match any existing flow rule (e.g., random source IP addresses), causing the controller to be overwhelmed with packet-in messages. The defense is threefold: (1) rate limiting packet-in messages per switch (each switch can send at most 1,000 packet-in messages per second to the controller); (2) wildcard rules that match common traffic patterns (e.g., all traffic from the campus network to the internet) without involving the controller; and (3) priority-based processing (control traffic is processed before packet-in messages, ensuring that the controller remains responsive to legitimate events even under attack).

The Heimdall neural IDS monitors the SDN data plane for suspicious patterns. It analyzes INT telemetry reports, flow rule installations, and packet-in messages to detect anomalies. Examples of detectable anomalies: (1) a switch that suddenly has an unusual number of flow rules (possible data plane compromise); (2) a flow that traverses an unusual path (possible flow rule hijacking); (3) a switch that generates an unusual number of packet-in messages (possible data plane DoS). The Heimdall neural IDS uses a transformer neural network trained on historical network data, achieving a detection rate of 95% with a false positive rate of 0.1%.

### Required Reading

- Kreutz, D., et al. (2035). "Software-Defined Networking: A Comprehensive Survey." *Proceedings of the IEEE*, 103(1), 14-76. (Security section.)
- Yggdrasil Security Architecture (2040). "SDN Security" and "Heimdall Neural IDS."
- ONOS Security Guide (2040). "TLS Configuration" and "Role-Based Access Control."

### Discussion Questions

1. An attacker gains access to the Norn controller's northbound API (e.g., by compromising an operator's credentials). What can the attacker do? Design a defense that limits the damage even if the northbound API is compromised.
2. A data plane DoS attack floods the network with packets that have random source IP addresses, generating millions of packet-in messages. The controller is overwhelmed and cannot process legitimate events. Design a multi-layer defense that prevents this attack, considering rate limiting, wildcard rules, and priority-based processing.
3. The Heimdall neural IDS detects that a switch has an unusual number of flow rules. Is this a security incident? What are the possible benign explanations (e.g., a new application generating many microflows) and malicious explanations (e.g., a compromised switch)? How would you investigate?

---

ᛁ **Lecture 10: SDN for Data Center Networks**

**Course:** CN301 — Software-Defined Networking (SDN)
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Data centers are SDN's proving ground — the first large-scale deployments were in data centers, where the need for agility, scale, and multi-tenancy made SDN essential. This lecture covers data center network architectures, SDN-based traffic engineering, and the 2040 data center fabric.

### Key Topics

- **Data Center Network Architecture:** Spine-leaf topology (the 2040 standard): every leaf switch connects to every spine switch, creating a non-blocking fabric with any-to-any connectivity. The spine-leaf topology provides predictable latency (every hop is 1-2 switch-to-switch links), scalable bandwidth (adding a spine switch increases aggregate bandwidth), and redundant paths (every leaf has multiple paths to every other leaf). Compare with the traditional three-tier architecture (core-aggregation-access), which has oversubscription at the aggregation layer and variable latency.
- **SDN-Based Traffic Engineering:** Equal-Cost Multi-Path (ECMP) routing: distributing traffic across multiple equal-cost paths. ECMP hashing: the switch computes a hash of the packet header (source IP, destination IP, source port, destination port) and uses the hash to select one of the equal-cost paths. The problem: hash polarization (traffic is not evenly distributed across paths) and flow collisions (large flows that hash to the same path cause congestion). The 2040 solution: adaptive traffic engineering, where the controller monitors per-path utilization (using INT telemetry) and redirects flows from congested paths to underutilized paths.
- **Multi-Tenancy:** Each tenant (application or customer) has its own virtual network (VXLAN or GENEVE overlay) with isolated routing, security, and QoS policies. The controller manages VNI allocation, VTEP configuration, and inter-tenant routing (for tenants that need to communicate). The 2040 state: a single data center fabric supports 10,000+ tenants, each with their own virtual network.
- **Data Center QoS:** Traffic classes: latency-sensitive (RDMA, storage replication), real-time (video, voice), and best-effort (bulk data, backups). Priority-based queuing: each switch has multiple output queues with different priorities. Weighted fair queuing: traffic classes share bandwidth proportionally. The 2040 solution: intent-based QoS, where the operator declares "latency-sensitive traffic should have < 10 μs queueing delay" and the controller configures switch queues to satisfy the intent.
- **The Bifrǫst Data Center Fabric:** The Hákon Computing Centre's data center uses a spine-leaf topology with 128 leaf switches and 32 spine switches. Each leaf switch has 48 × 100 Gbps ports (to servers) and 8 × 400 Gbps ports (to spines). Each spine switch has 128 × 400 Gbps ports. The total bandwidth: 128 × 8 × 400 Gbps = 409.6 Tbps non-blocking. The Norn controller manages the fabric: computing ECMP paths, configuring VXLAN overlays for multi-tenancy, and installing QoS policies for traffic classes.

### Lecture Notes

The spine-leaf topology replaced the three-tier architecture because the three-tier design could not keep up with east-west traffic (traffic between servers within the data center). In a three-tier network (core-aggregation-access), east-west traffic must traverse the core layer, which is costly and adds latency. In a spine-leaf network, east-west traffic traverses only one spine switch — a maximum of two hops (leaf → spine → leaf). The result: consistent, predictable latency regardless of the traffic pattern.

ECMP is the simplest form of traffic engineering in a spine-leaf network. Every leaf switch has N equal-cost paths to every other leaf switch (one through each spine switch). The hash-based ECMP algorithm distributes flows across these paths, achieving load balancing. The problem: hash-based ECMP distributes flows, not traffic — if a few large flows hash to the same path, that path becomes congested while other paths are underutilized. This is the hash polarization problem. The 2040 solution is adaptive traffic engineering: the controller monitors per-path utilization using INT telemetry and dynamically adjusts the hash buckets to redirect large flows from congested paths to underutilized paths. This is similar to congestion-aware routing in traditional networks, but it is executed in milliseconds (the Norn controller adjusts hash buckets in 100 ms) rather than minutes (traditional routing convergence time).

Multi-tenancy in the data center requires network isolation between tenants. Each tenant has their own VXLAN or GENEVE overlay, with a unique VNI, their own routing domain, and their own security policies. The Norn controller manages VNI allocation (ensuring no two tenants have the same VNI), VTEP configuration (installing rules that steer tenant traffic to the correct VNI), and inter-tenant routing (for tenants that need to communicate, the controller installs rules that allow specified traffic to cross VNI boundaries). The result: tenants can use any IP address space they want (even overlapping with other tenants) and any routing protocol they want, without interference.

### Required Reading

- Al-Fares, M., et al. (2008). "A Scalable, Commodity Data Center Network Architecture." *ACM SIGCOMM 2008*. (The original fat-tree paper.)
- Benson, T., et al. (2036). "Network Traffic Characteristics of Data Centers." *ACM SIGCOMM 2036*.
- Yggdrasil Data Center Architecture (2040). "Spine-Leaf Fabric" and "Traffic Engineering."

### Discussion Questions

1. A spine-leaf data center has 64 leaf switches and 16 spine switches. Each leaf has 48 × 100 Gbps server ports and 16 × 400 Gbps uplink ports. Calculate the total non-blocking bandwidth and the oversubscription ratio (server bandwidth / uplink bandwidth).
2. ECMP hashing distributes flows across equal-cost paths. Two large flows hash to the same path, causing congestion while other paths are underutilized. Design an adaptive traffic engineering algorithm that detects this situation and redirects one of the flows to an underutilized path. How quickly can the controller respond? What happens if the redirected flow hashes back to the congested path?
3. A data center supports 10,000 tenants. Each tenant has its own VNI, routing domain, and security policies. The controller must manage 10,000 overlays. Calculate the flow rule requirements: each VTEP needs entries for every tenant that has VMs on that leaf switch. If each leaf switch has VMs from 100 tenants, how many flow rules per leaf? Is this within the TCAM limits of current switches?

---

ᚾ **Lecture 11: SDN for Wide-Area Networks and Traffic Engineering**

**Course:** CN301 — Software-Defined Networking (SDN)
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

SDN's benefits extend beyond the data center — wide-area networks (WANs) also benefit from centralized control, traffic engineering, and intent-based management. This lecture covers SDN for WANs, BGP traffic engineering, and the Bifrǫst Mesh's WAN SDN architecture.

### Key Topics

- **WAN Challenges:** Long propagation delays (ms, not μs), limited bandwidth (compared to data center links), heterogeneous link types (fiber, microwave, satellite), and multiple administrative domains (autonomous systems). The WAN traffic engineering problem: how to route traffic across multiple paths to minimize congestion, maximize utilization, and satisfy latency constraints.
- **Traditional WAN Traffic Engineering:** MPLS Traffic Engineering (MPLS-TE): establishing Label-Switched Paths (LSPs) with reserved bandwidth across the WAN. MPLS-TE computes explicit routes using CSPF (Constrained Shortest Path First), considering bandwidth and latency constraints. The problem: MPLS-TE is configuration-heavy (each LSP must be manually configured or managed by a path computation element) and slow to adapt to changes (LSP setup takes seconds, and re-optimization takes minutes).
- **SDN-Based WAN Traffic Engineering:** The controller has a global view of the WAN topology and link utilization. It computes optimal paths for all traffic flows simultaneously, using the link utilization data to balance traffic across multiple paths. The controller installs flow rules on WAN switches that direct traffic along the computed paths. The result: higher link utilization (50-70% vs. 30-40% with traditional routing), faster convergence (ms vs. minutes), and intent-based path selection (latency-sensitive traffic takes the low-latency path, bulk traffic takes the high-bandwidth path).
- **BGP and SDN:** BGP (Border Gateway Protocol) is the inter-domain routing protocol that connects autonomous systems. BGP selects paths based on local preferences, AS path length, and other attributes, but it does not consider link utilization or latency. SDN can complement BGP: the controller manipulates BGP attributes (local preference, MED, communities) to steer traffic across preferred paths, while BGP handles the inter-domain reachability. The Bifrǫst Mesh uses BGP for inter-domain routing and SDN for intra-domain traffic engineering.
- **The Bifrǫst WAN Architecture:** The Bifrǫst Mesh's WAN connects Yggdrasil's three campuses (Oslo, Bergen, Tromsø) and two research sites (Svalbard, Trondheim) with a mix of fiber (10-400 Gbps), microwave (1-10 Gbps), and satellite (0.5-2 Gbps) links. The Norn controller monitors link utilization using INT telemetry, computes optimal paths for each traffic class (latency-sensitive, bandwidth-sensitive, best-effort), and installs flow rules on WAN switches. The result: 60-70% average link utilization vs. 30-40% with traditional routing.

### Lecture Notes

The fundamental difference between data center and WAN traffic engineering is the optimization objective. In a data center, the objective is to maximize bisection bandwidth (the bandwidth between any two halves of the network) and minimize latency — both are achieved by spreading traffic evenly across all paths. In a WAN, the objective is to minimize cost (using cheap links for bulk traffic) while satisfying latency constraints (routing real-time traffic over low-latency links) — which requires directing different traffic classes over different paths.

Traditional WAN routing (OSPF, IS-IS, BGP) selects a single best path for each destination based on static link metrics. The best path is the path with the lowest total metric (which is typically inversely proportional to bandwidth). The result: the best path is heavily loaded (because all traffic follows it), while alternate paths are underutilized. MPLS-TE addresses this by establishing multiple LSPs with reserved bandwidth, but LSPs are configured manually or managed by a path computation element, and re-optimization is slow.

SDN-based WAN traffic engineering solves this by having the controller compute optimal paths for all traffic flows simultaneously, considering link utilization, latency, and policy constraints. The controller solves a multi-commodity flow problem: minimize the maximum link utilization subject to latency constraints for latency-sensitive traffic and bandwidth constraints for bandwidth-sensitive traffic. The solution is a set of paths and traffic splits for each flow: latency-sensitive traffic follows the lowest-latency path, bandwidth-sensitive traffic follows the highest-bandwidth path, and best-effort traffic is distributed across all available paths to minimize congestion.

The Bifrǫst WAN uses a hybrid SDN/BGP approach. BGP handles inter-domain routing (advertising routes to other autonomous systems and learning routes from them). SDN handles intra-domain traffic engineering (directing traffic along the optimal paths within the Bifrǫst Mesh). The Norn controller manipulates BGP local preference to steer traffic: latency-sensitive traffic gets high local preference for low-latency paths, and bulk traffic gets low local preference for high-bandwidth paths. The result: traffic is directed along the optimal path without modifying BGP itself.

### Required Reading

- B4: Google's SDN WAN (2033). "B4 and After: Managing Heterogeneity in a Worldwide SDN." *ACM SIGCOMM 2033*.
- Fortz, B. & Thorup, M. (2004). "Increasing Internet Capacity Using Local Search." *Computational Optimization and Applications*, 29(1), 13-48.
- Yggdrasil SDN Architecture Guide (2040). "WAN Traffic Engineering" and "Bifrǫst WAN."

### Discussion Questions

1. A WAN has three paths between Oslo and Bergen: fiber (10 Gbps, 5 ms latency), microwave (1 Gbps, 10 ms latency), and satellite (0.5 Gbps, 50 ms latency). Three traffic classes need to be routed: latency-sensitive (1 Gbps, requires < 15 ms latency), bandwidth-sensitive (5 Gbps, no latency requirement), and best-effort (2 Gbps, no latency requirement). Design a path assignment that satisfies all constraints.
2. SDN-based WAN traffic engineering requires the controller to compute optimal paths for all traffic flows. If the WAN has 1,000 flows and 100 links, the optimization problem has 100,000 variables. Can this problem be solved in real time? What algorithms would you use? Consider linear programming, gradient descent, and heuristic approaches.
3. BGP selects a single best path for each destination. What happens when the best path fails? Traffic shifts to the second-best path, which may be congested. How can SDN help? Design a fast-reroute mechanism that pre-computes backup paths and switches to them in milliseconds.

---

ᛃ **Lecture 12: The Future of SDN — Intent, Autonomy, and Beyond**

**Course:** CN301 — Software-Defined Networking (SDN)
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

SDN has evolved from a research project (OpenFlow) to a production technology (intent-based networking) to an autonomous system (AI-driven networking). This final lecture surveys the frontiers: autonomous networks, digital twins, self-healing networks, and the convergence of SDN and AI in the 2040s and beyond.

### Key Topics

- **Autonomous Networks:** The next step beyond intent-based networking: the network understands its own state, predicts its own needs, and heals its own failures without human intervention. The autonomous networking loop: Observe (INT telemetry, SNMP, logs), Orient (analyze data, detect anomalies), Decide (compute the optimal response), and Act (install new flow rules, reconfigure devices). The Verdandi predictive module: using machine learning to predict traffic patterns and pre-install flow rules before congestion occurs.
- **The Verdandi Predictive Architecture:** Verdandi (the Norn of the present) uses a transformer neural network trained on historical traffic data to predict traffic patterns. The model predicts traffic for the next 5 minutes at 1-second granularity, for each flow class (latency-sensitive, bandwidth-sensitive, best-effort) on each link. The Norn controller uses these predictions to pre-install flow rules: before congestion occurs, the controller redirects traffic from predicted-congested links to underutilized links. The result: 60% reduction in congestion events and 30% improvement in average link utilization.
- **Digital Twins:** A digital twin is a real-time simulation of the network that mirrors the physical network's state, topology, and traffic. The digital twin is used for: what-if analysis (what happens if this link fails?), change validation (will this configuration change break anything?), and training (the Verdandi model is trained on the digital twin before deployment). The Bifrǫst digital twin: a real-time simulation of the entire Bifrǫst Mesh, updated every second with INT telemetry data.
- **Self-Healing Networks:** When a failure occurs (link failure, switch failure, controller failure), the network automatically detects the failure, computes alternative paths, and installs new flow rules. The Norn controller's self-healing mechanism: (1) detect the failure (INT telemetry shows a path is broken), (2) identify affected intents (which intents are violated by the failure), (3) recompute paths for affected intents, (4) install new flow rules, and (5) verify that the new paths satisfy the intents. The target: self-healing within 50 ms of a failure.
- **The Network Engineer's Path Forward:** SDN has transformed the network engineer's role from CLI configurator to intent architect. The 2040 network engineer defines what the network should do (intents), not how it should do it (flow rules). The engineer's skills: network architecture (designing topologies and policies), intent modeling (expressing requirements in formal language), and AI collaboration (working with autonomous systems to optimize and heal the network). The Yggdrasil commitment: networks that serve their users, not networks that require human intervention.

### Lecture Notes

The evolution from traditional networking to SDN to intent-based networking to autonomous networking is a progression of abstraction. Traditional networking: the engineer configures individual devices (low abstraction, high complexity). SDN: the engineer programs flow rules (medium abstraction, medium complexity). Intent-based networking: the engineer declares intents (high abstraction, low complexity). Autonomous networking: the engineer defines goals, and the network achieves them (highest abstraction, lowest complexity).

The Verdandi predictive module represents the current frontier of autonomous networking. Verdandi uses a transformer neural network (similar to the architecture used in large language models) to predict traffic patterns. The model is trained on 6 months of historical traffic data (per-flow, per-link, per-second granularity) and predicts traffic for the next 5 minutes. The prediction is used in two ways: (1) pre-installation — the Norn controller installs flow rules for predicted traffic before the traffic arrives, reducing path setup time from 50 ms to 5 ms; and (2) pre-emption — the Norn controller redirects predicted-congested traffic to underutilized links before congestion occurs, reducing congestion events by 60%.

The digital twin is an essential tool for autonomous networking. The Bifrǫst digital twin is a real-time simulation of the entire Bifrǫst Mesh, running on the Hákon Computing Centre's GPU cluster. The digital twin receives INT telemetry data from the physical network every second and updates its state (link utilizations, queue depths, flow tables) to match. The chief engineer can use the digital twin to test changes before deploying them: "What happens if I add a new spine switch?" "What happens if I change the intent for latency-sensitive traffic?" The digital twin simulates the change and shows the predicted impact, allowing the engineer to validate changes before they affect production traffic. The Verdandi model is also trained on the digital twin before deployment, ensuring that its predictions are accurate.

Self-healing is the final piece of the autonomous networking puzzle. When a link fails, the Norn controller detects the failure (via INT telemetry or BFD — Bidirectional Forwarding Detection) within 5 ms, identifies the affected intents, recomputes paths, and installs new flow rules. The total self-healing time is 50 ms — fast enough for real-time applications (VoIP, video conferencing, autonomous vehicles) to experience only a brief glitch rather than a disconnection. The self-healing mechanism also works for switch failures (the controller redirects traffic around the failed switch) and controller failures (the standby controller takes over within 5 seconds).

### Required Reading

- Hellerstein, J.L., et al. (2037). "Self-Managing Systems: A Vision for Network Autonomy." *IEEE Internet Computing*, 21(4), 48-57.
- Yggdrasil SDN Architecture Guide (2040). "Verdandi Predictive Module" and "Digital Twin."
- Shimizu, T., et al. (2038). "Self-Healing Networks: From Detection to Recovery in 50ms." *ACM SIGCOMM 2038*.

### Discussion Questions

1. The Verdandi predictive module predicts traffic for the next 5 minutes. If the prediction is wrong (actual traffic differs from predicted traffic by more than 20%), the pre-installed flow rules may be suboptimal. How should the system handle prediction errors? Consider reverting to on-demand flow installation, adjusting the prediction model, and human intervention.
2. Digital twins enable what-if analysis, but the twin's accuracy depends on the quality of the telemetry data and the fidelity of the simulation. How would you validate that the Bifrǫst digital twin accurately represents the physical network? What are the risks of deploying changes based on digital twin predictions that turn out to be wrong?
3. Autonomous networks make decisions without human intervention. What are the ethical implications? Consider: (a) a self-healing network that redirects traffic through a link with higher latency, saving the connection but violating the latency intent; (b) a predictive system that pre-emptively blocks traffic based on pattern matching, potentially blocking legitimate traffic; (c) a network that optimizes for aggregate performance, potentially degrading performance for specific users. How should the network engineer audit and oversee autonomous decisions?

---

## Final Examination Preparation

The CN301 final examination is a **3-hour written exam** plus a **practical SDN lab assessment**.

### Written Examination (60%)

**Sample Questions:**

1. "Design a P4 program that implements BTP routing on a spine-leaf data center fabric. The program should: parse the BTP header, match on the BTP connection ID, select the output port using ECMP, and insert an INT header. Draw the parser state machine and the match-action table pipeline."

2. "The Norn controller is managing a network with 100 switches. A link failure causes 50 intents to be violated. Describe the self-healing process step by step: failure detection, intent identification, path recomputation, flow rule installation, and verification. What is the expected time for each step?"

3. "Compare OpenFlow and P4 as southbound interfaces for SDN. What are the advantages and disadvantages of each? Under what circumstances would you choose OpenFlow over P4, and vice versa?"

4. "Design a service function chain for a campus network: all internet traffic must pass through vFW → vIDS → vLB before reaching the destination. Draw the topology, including the SDN switches that steer traffic through the VNFs. Describe the flow rules at each switch."

5. "The Verdandi predictive module predicts that link A-B will be congested in 2 minutes. The Norn controller should redirect traffic from link A-B to link A-C-B. Describe the steps the controller takes to redirect traffic, including which flow rules are installed, on which switches, and in what order."

6. "A VXLAN overlay connects three campuses with VNI 100 (Oslo), 200 (Bergen), and 300 (Tromsø). Each campus has a VTEP that encapsulates/decapsulates VXLAN packets. Design the VTEP flow rules that enable unicast communication between campuses. How are broadcast packets (ARP) handled in the overlay?"

7. "The Norn controller receives two conflicting intents: 'Block all traffic from subnet 10.0.1.0/24 to 10.0.10.0/24' and 'Allow HTTP traffic from 10.0.1.5 to 10.0.10.10.' Resolve the conflict using the specificity principle. Show the resulting flow rules."

### Practical SDN Lab Assessment (40%)

Students configure and operate an SDN network in the Valhalla Network Lab:
- Write a P4 program that implements BTP routing, ECMP forwarding, and INT telemetry
- Configure the Norn controller to manage a 10-switch topology with intent-based networking
- Implement a service function chain (vFW → vIDS → vLB) and verify traffic steering
- Diagnose and fix a pre-configured SDN failure (controller failure, flow table corruption, INT telemetry loss)
- Observe the Norn controller's self-healing behavior when a link fails

### Grading Rubric

| Criterion | Weight | Excellent (A) | Good (B) | Satisfactory (C) | Needs Improvement (D/F) |
|-----------|--------|---------------|----------|------------------|---------------------------|
| Protocol Knowledge | 25% | Deep understanding of SDN protocols (OpenFlow, P4, P4Runtime), able to write P4 programs and analyze flow rules | Good understanding of major protocols | Adequate knowledge of basic protocols | Shallow or incorrect understanding |
| Design Quality | 25% | Elegant, well-justified designs with scalability and resilience | Good designs with reasonable rationale | Adequate designs, limited justification | Poor or incomplete designs |
| Operational Reasoning | 20% | Systematic troubleshooting, correct diagnosis, practical solutions | Good troubleshooting, mostly correct | Adequate but incomplete troubleshooting | Unable to diagnose or fix problems |
| Communication | 15% | Clear, precise, well-organized | Good clarity; minor issues | Adequate but verbose or unclear | Disorganized or incoherent |
| Innovation | 15% | Creative solutions, novel designs, thoughtful extensions | Solid solutions with minor creative elements | Standard solutions without creativity | No creative or novel thinking |

---

*Woven by the hands of Runa Gridweaver Freyjasdóttir, student of the University of Yggdrasil, 2040. May the packets flow smoothly and the routes never loop.* ᛟ