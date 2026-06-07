# SA104: Networking Fundamentals

## Overview

This course introduces the fundamental concepts of computer networking that form the backbone of modern systems administration. Students will learn how networks enable communication between systems, the protocols that govern this communication, and the essential tools for network troubleshooting and configuration.

**Course Credits**: 4  
**Term**: Year 1, Semester 2  
**Prerequisites**: SA101 (Introduction to Systems Administration), SA103 (Computer Hardware & Peripherals)  

## Learning Objectives

By the end of this course, students will be able to:

1. Explain the OSI and TCP/IP networking models and their layers
2. Configure and troubleshoot basic network interfaces on Linux systems
3. Understand IPv4 and IPv6 addressing, subnetting, and routing
4. Implement and manage common network services (DHCP, DNS)
5. Use network diagnostic tools (ping, traceroute, netstat, ss, Wireshark)
6. Configure basic firewall rules using nftables/iptables
7. Understand wireless networking principles and security
8. Apply networking knowledge to systems administration scenarios

## Week-by-Week Breakdown

### Week 1: Networking Models and Terminology
- OSI 7-layer model vs TCP/IP 4-layer model
- Encapsulation and decapsulation processes
- Network devices: hubs, switches, routers, bridges, access points
- Collision domains vs broadcast domains
- **Lab**: Network topology mapping using Cisco Packet Tracer or GNS3

### Week 2: Physical Layer and Media
- Copper media: Cat5e, Cat6, Cat6a, Cat8 standards
- Fiber optics: single-mode vs multi-mode, connectors
- Wireless media: RF spectrum, antennas, propagation
- Network interface controllers (NICs) and drivers
- **Lab**: Cable making and testing, NIC driver installation

### Week 3: Data Link Layer and Ethernet
- Ethernet framing and MAC addresses
- ARP (Address Resolution Protocol)
- Switch operation: CAM tables, flooding, learning
- VLANs (802.1Q) and trunking
- Spanning Tree Protocol (STP) and variants
- **Lab**: VLAN configuration on managed switches, STP observation

### Week 4: Network Layer - IP Addressing
- IPv4 address structure: network vs host portions
- Subnet masks and CIDR notation
- Subnetting practice and VLSM
- Private vs public address spaces (RFC 1918)
- Introduction to IPv6: address types and notation
- **Lab**: IPv4 subnetting exercises, IPv6 address configuration

### Week 5: Network Layer - Routing
- Routing vs switching: when each is used
- Static routing: configuration and limitations
- Dynamic routing protocols: RIP, OSPF, EIGRP, BGP basics
- Routing tables and longest prefix match
- Default routes and gateways of last resort
- **Lab**: Static route configuration, basic OSPF setup in lab environment

### Week 6: Transport Layer
- TCP vs UDP: connection-oriented vs connectionless
- TCP three-way handshake, sliding window, congestion control
- UDP characteristics and use cases
- Port numbers: well-known, registered, dynamic/private
- Socket programming basics
- **Lab**: Packet capture analysis of TCP/UDP flows with Wireshark

### Week 7: Application Layer Services
- DNS: namespace, record types, zone transfers, recursion
- DHCP: lease process, options, relay agents
- HTTP/HTTPS: basics for sysadmins
- SSH: secure remote administration
- NTP: time synchronization importance
- **Lab**: DNS and DHCP server configuration (BIND, ISC DHCPd)

### Week 8: Network Services for SysAdmins
- LDAP: directory services basics
- RADIUS/TACACS+: AAA protocols
- SNMP: network monitoring basics
- Syslog: centralized logging
- FTP/SFTP: file transfer considerations
- **Lab**: Centralized logging with rsyslog, basic SNMP monitoring

### Week 9: Linux Networking Fundamentals
- Network interface configuration (ip vs ifconfig)
- Routing table manipulation
- Network namespaces and containers
- Bridge interfaces and bonding
- TUN/TAP devices and VPN basics
- **Lab**: Linux network namespace experiments, bridge creation

### Week 10: Network Troubleshooting Methodology
- OSI model troubleshooting approach
- Common symptoms and their likely layers
- Packet capture analysis with tcpdump/Wireshark
- Using ping, traceroute, and MTR effectively
- Netstat, ss, and lsof for connection troubleshooting
- **Lab**: Troubleshooting common network issues in lab environment

### Week 11: Network Security Fundamentals
- Defense in depth for networks
- Firewall types: packet filtering, stateful, next-gen
- Basic nftables/iptables ruleset creation
- VPN concepts: IPsec vs SSL/TLS VPNs
- Wireless security: WEP, WPA, WPA2, WPA3
- Network segmentation and DMZ concepts
- **Lab**: Basic firewall setup with nftables, wireless security configuration

### Week 12: Modern Networking Trends
- Software-defined networking (SDN) basics
- Network functions virtualization (NFV)
- Intent-based networking
- IPv6 transition technologies
- Data center networking: spine-leaf, VXLAN
- Network automation basics with Python/Ansible
- **Lab**: Simple network automation script, mininet SDN demo

## Detailed Topics

### The OSI Model Deep Dive
- Layer 1 (Physical): bits, voltages, pinouts
- Layer 2 (Data Link): frames, MAC addresses, LLC
- Layer 3 (Network): packets, IP addresses, routing
- Layer 4 (Transport): segments, port numbers, reliability
- Layer 5 (Session): session establishment, maintenance
- Layer 6 (Presentation): data formatting, encryption
- Layer 7 (Application): user applications, protocols

### IPv4 Addressing and Subnetting
- Binary math for network professionals
- Classful vs classless addressing
- Subnet calculations: network, broadcast, host ranges
- Supernetting and route summarization
- Variable Length Subnet Masking (VLSM) examples
- Common subnet masks and their uses

### IPv6 Essentials
- 128-bit address structure and compression
- Address types: unicast, multicast, anycast
- Global unicast, link-local, unique local addresses
- Stateless Address Autoconfiguration (SLAAC)
- DHCPv6 for stateful address assignment
- Neighbor Discovery Protocol (NDP) replacing ARP

### Routing Protocols Overview
- Distance Vector: RIP, RIPng
- Link State: OSPF, OSPFv3, IS-IS
- Path Vector: BGP
- Administrative distance and metric concepts
- Route redistribution between protocols
- Basic BGP peering and route advertisement

### Linux Networking Tools
- iproute2 suite: ip, ss, nstat
- Legacy tools: ifconfig, netstat, route (for reference)
- Packet capture: tcpdump, Wireshark, tshark
- Network scanning: nmap, masscan
- Bandwidth testing: iperf3, netperf
- WiFi tools: iw, wpa_supplicant, hostapd

### Network Services Architecture
- Client-server vs peer-to-peer models
- Service discovery mechanisms
- Load balancing basics: L4 vs L7
- Caching principles and CDN basics
- Proxy concepts: forward vs reverse proxy
- Authentication protocols: LDAP, Kerberos basics

### Wireless Networking
- 802.11 standards: a/b/g/n/ac/ax/be
- Frequency bands: 2.4GHz, 5GHz, 6GHz
- CSMA/CA medium access
- Authentication and association process
- Wireless site survey basics
- Common wireless issues and troubleshooting

## Hands-On Labs

### Lab 1: Network Topology Discovery
- Use LLDP/CDP to discover network topology
- Map physical and logical connections
- Document findings in network diagram

### Lab 2: IPv4 Configuration and Testing
- Configure static IP addresses on Linux
- Test connectivity with ping and arp
- Observe ARP table population
- Practice subnetting calculations

### Lab 3: VLAN Implementation
- Configure VLANs on managed switch
- Create trunk links between switches
- Verify inter-VLAN communication requires routing
- Observe broadcast domain separation

### Lab 4: Static and Dynamic Routing
- Configure static routes on Linux routers
- Set up OSPF between two Linux routers (using Quagga/FRR)
- Verify route propagation and convergence
- Test failover scenarios

### Lab 5: DNS and DHCP Services
- Install and configure BIND9 DNS server
- Create forward and reverse zones
- Set up ISC DHCP server with reservations
- Test client acquisition of addresses and DNS

### Lab 6: Network Monitoring and Troubleshooting
- Use Wireshark to capture and analyze traffic
- Simulate common network issues (disconnected cable, wrong IP)
- Practice systematic troubleshooting approach
- Document symptoms, hypothesis, tests, and resolution

### Lab 7: Linux Networking Advanced
- Create and manage network namespaces
- Set up bridge interfaces for container networking
- Configure bonding for link aggregation
- Implement basic VLAN tagging on Linux

### Lab 8: Basic Firewall Configuration
- Create nftables ruleset for basic protection
- Allow SSH, HTTP/HTTPS, block other inbound
- Implement simple outbound restrictions
- Test with nmap from external host

### Lab 9: Wireless Network Setup
- Configure wireless access point with hostapd
- Implement WPA2-PSK security
- Test client connection and roaming
- Monitor signal strength and interference

### Lab 10: Network Automation Introduction
- Use Python with netmiko or napalm to configure devices
- Ansible playbook for basic switch configuration
- Git version control for network configurations
- Validate configuration compliance

## Assessment and Grading

### Evaluation Components
- **Lab Exercises** (40%): Weekly hands-on networking labs
- **Quizzes** (20%): Bi-weekly knowledge checks
- **Midterm Exam** (15%): Written and practical components
- **Final Project** (15%): Design and implement a small office network
- **Participation and Attendance** (10%): Engagement in discussions and lab work

### Lab Requirements
- Complete all assigned lab exercises
- Maintain a network engineering lab journal
- Submit lab reports with diagrams, configurations, and analysis
- Demonstrate troubleshooting proficiency

### Exam Structure
- Multiple choice and short answer questions
- Network diagram interpretation
- Subnetting calculations
- Basic configuration tasks
- Troubleshooting scenario analysis

## Recommended Resources

### Textbooks
- "Computer Networking: A Top-Down Approach" - Kurose & Ross
- "Network Warrior" - Gary A. Donahue
- "Linux Networking Cookbook" - Carla Schroder
- "TCP/IP Illustrated, Volume 1" - W. Richard Stevens

### Online Resources
- Cisco Networking Academy materials (free introductory content)
- The TCP/IP Guide (http://www.tcpipguide.com/)
- Linux Documentation Project networking guides
- Wireshark Wiki and tutorials
- IANA protocol numbers and port assignments

### Tools and Software
- Wireshark for packet analysis
- GNS3 or Cisco Packet Tracer for network simulation
- Linux with full networking tool suite
- Managed switches for VLAN and STP labs
- Wireless access points for wireless labs
- Raspberry Pi or similar for low-cost networking projects

## Professional Applications

### Systems Administration Relevance
- Understanding network fundamentals is essential for:
  - Diagnosing application connectivity issues
  - Working effectively with network teams
  - Securing systems through proper network configuration
  - Performance tuning network-dependent applications
  - Implementing monitoring and alerting for network services

### Career Pathways
- Network Systems Administrator
- DevOps Engineer (networking aspects)
- Cloud Infrastructure Engineer
- Security Operations Center (SOC) Analyst
- Technical Support Engineer
- Network Technician

## Conclusion

SA104 provides the essential networking foundation that all systems administrators need. Whether managing cloud infrastructure, securing enterprise networks, or troubleshooting application connectivity, the concepts covered in this course will be used daily throughout a sysadmin's career. By combining theoretical knowledge with extensive hands-on practice, students will develop both the understanding and practical skills required to work confidently with network technologies.

*Remember: In systems administration, you're not just managing computers — you're managing the conversations between them.*
