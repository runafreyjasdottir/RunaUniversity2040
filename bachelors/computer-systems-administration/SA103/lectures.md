# SA103: Computer Hardware & Peripherals
## Bachelor of Science in Computer Systems Administration — University of Yggdrasil, 2040

**Credits:** 4
**Prerequisites:** SA101
**Description:** Comprehensive study of modern computer hardware and peripheral technologies, covering CPU architectures, memory hierarchies, storage systems, I/O interfaces, and emerging technologies such as quantum processors, neuromorphic computing, and persistent memory. Students learn to evaluate, select, and manage hardware components for optimal performance, reliability, and cost-effectiveness in 2040 data centers and edge environments.

**Instructor:** Dr. Birgitte Ivarsdóttir, Professor of Computer Engineering
**Lab:** Valkyrie Hardware Lab, Sublevel 3, Hákon Computing Centre

---

## Lectures

ᚠ **Lecture 1: Foundations of Digital Logic and CPU Architecture**

**Course:** SA103 — Computer Hardware & Peripherals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview
This lecture establishes the foundational principles of digital logic design and central processing unit (CPU) architecture that underpin all modern computing systems. We examine transistor-level design, instruction set architectures (ISAs), pipelining, superscalar execution, and the 2040 trends toward heterogeneous computing and domain-specific architectures.

### Key Topics
- **Digital Logic Basics:** Boolean algebra, combinational vs. sequential logic, flip-flops, and finite state machines as building blocks of hardware.
- **Transistor Technology:** FinFET, gate-all-around (GAA), and the 2040 *2-nanometer nanosheet* transistors enabling 50 billion+ transistors per chip.
- **Instruction Set Architectures:** RISC-V dominance, x86-64 legacy, ARM v10, and the 2040 *Yggdrasil Secure ISA* (YSI) with built-in memory tagging and capability-based security.
- **CPU Pipelining and Superscalar Design:** 5-stage classic pipeline, out-of-order execution, branch prediction, and the 2040 *Adaptive Pipeline* that reconfigures stage depth based on workload characteristics.
- **Heterogeneous Computing:** CPU-GPU-FPGA-ASIC integration, coherent interconnects (CXL 4.0), and the 2040 *Modular Compute Fabric* allowing hot-swappable compute tiles.

### Lecture Notes
The relentless scaling described by Moore's Law has shifted from transistor density to specialized architectures. While transistor counts continue to grow (reaching 100 billion+ on flagship server chips in 2040), performance gains now come from parallelism, specialization, and improved memory hierarchies. The von Neumann bottleneck remains a challenge, prompting innovations like processing-in-memory (PIM) and neuromorphic approaches.

Instruction set architecture serves as the contract between hardware and software. RISC-V has become the dominant open ISA due to its modularity and extensibility, allowing vendors to add custom extensions for cryptography, AI acceleration, or real-time processing. The Yggdrasil Secure ISA (YSI) extends RISC-V with hardware-enforced memory safety, reducing reliance on software mitigations for buffer overflows and use-after-free errors.

Modern CPUs employ deep pipelining with aggressive out-of-order execution to maximize instruction-level parallelism. Branch predictors now achieve >99% accuracy using transformer-based models that analyze hundreds of branches of history. The Adaptive Pipeline concept allows the CPU to dynamically reconfigure its pipeline depth—shorter for latency-sensitive tasks, deeper for throughput-oriented workloads—based on runtime profiling.

Heterogeneous computing recognizes that no single processor type excels at all workloads. The 2040 Modular Compute Fabric, built on Compute Express Link (CXL) 4.0, enables seamless integration of CPUs, GPUs, FPGAs, and ASICs into a single coherent memory domain. This allows, for example, a database server to attach an FPGA accelerator for compression/decompression without data copying over PCIe.

### Required Reading
- Patterson, D.A. & Hennessy, J.L. (2038). *Computer Organization and Design: RISC-V Edition*, 6th Edition. Morgan Kaufmann. Chapters 1-4, 6-7.
- Yggdrasil Secure ISA Specification (2040). UoY Engineering Press.
- CXL Consortium. (2039). *Compute Express Link 4.0 Specification*. Chapters 1-3, 5-6.

### Discussion Questions
1. How does the end of Dennard scaling impact CPU design choices regarding clock frequency, power consumption, and thermal dissipation?
2. What are the trade-offs between a universal ISA like RISC-V and specialized ISAs for specific domains (e.g., AI, networking)?
3. Describe how an Adaptive Pipeline could improve energy efficiency for a mixed workload of web serving and batch analytics.

---

ᚢ **Lecture 2: Memory Hierarchy and Technologies**

**Course:** SA103 — Computer Hardware & Peripherals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview
The memory hierarchy bridges the speed gap between fast but expensive CPU registers and slow but inexpensive storage. This lecture covers SRAM caches, DRAM main memory, emerging non-volatile memory technologies, and the 2040 innovations in memory pooling, compression, and AI-driven prefetching.

### Key Topics
- **SRAM Cache Design:** L1/L2/L3 cache organization, coherence protocols (MESI, MOESI), and the 2040 *L4 Cache* using high-bandwidth memory (HBM4) stacked on-package.
- **DRAM Evolution:** DDR5, LPDDR5X, and the 2040 *DDR6* with 12.8 Gbps pins, on-die ECC, and support for 3DS stacking up to 16-high.
- **Non-Volatile Memory:** Persistent Memory (PMem), Compute Express Link (CXL) memory devices, and the 2040 *Neural Resistive RAM* (NRRAM) for AI weight storage.
- **Memory Pooling and Disaggregation:** CXL 3.0/4.0 enabling memory expansion and sharing across servers, and the 2040 *AI Memory Scheduler* that allocates memory based on application QoS requirements.
- **Memory Compression and Encryption:** Intel Memory Encryption Technology (MKTME), AMD Secure Memory Encryption (SME), and the 2040 *Adaptive Memory Compressor* that uses learned dictionaries for lossless compression.

### Lecture Notes
The memory hierarchy remains critical because processor speed improves faster than memory latency—a phenomenon known as the memory wall. Caches mitigate this by exploiting temporal and spatial locality, but cache misses still cost hundreds of cycles. The L4 cache, implemented as HBM4 stacked on the CPU package, provides a large (16-64 GB) low-latency buffer between last-level cache and main memory, reducing latency for working sets that exceed traditional cache sizes.

DRAM continues to evolve with higher densities and speeds. DDR6 introduces on-die error correction (ODECC) that corrects single-bit errors without requiring a retry, improving effective bandwidth. 3DS (three-dimensional die stacking) allows stacking up to 16 DRAM dies, enabling terabyte-capacity DIMMs for memory-intensive workloads like in-memory databases and AI training.

Persistent memory technologies like Intel Optane DC Persistent Memory (now evolved into CXL-attached memory devices) offer byte-addressable non-volatile memory with performance closer to DRAM than SSD. This enables innovative applications like fast restartable databases and persistent key-value stores. The Neural Resistive RAM (NRRAM) mimics synaptic weights, allowing direct storage of AI model parameters in memory, reducing the need to load weights from storage during inference.

Memory disaggregation via CXL allows pooling memory resources across a rack, enabling elastic allocation where memory-intensive jobs can borrow memory from underutilized servers. The AI Memory Scheduler predicts memory demand patterns and proactively moves data to minimize remote memory access latency.

Memory compression reduces effective memory footprint, allowing more data to reside in fast memory. Adaptive compression algorithms learn data patterns (e.g., repeating sequences in logs or databases) and achieve 2:1 or 3:1 compression ratios with minimal CPU overhead, effectively increasing usable memory capacity.

### Required Reading
- Jacob, B. et al. (2037). *Memory Systems: Cache, DRAM, Disk*, 3rd Edition. IEEE Press. Chapters 2-4, 7-9.
- SNIA. (2039). *Persistent Memory Programming Model*, Version 2.0. Chapters 1-3.
- Yggdrasil Memory Technologies Whitepaper (2040). UoY Research Press.

### Discussion Questions
1. How does on-die ECC in DDR6 improve system reliability and availability compared to traditional ECC that requires a retry?
2. Discuss the advantages and disadvantages of persistent memory for database workloads versus traditional DRAM+SSD hierarchies.
3. In what scenarios would memory disaggregation via CXL provide significant cost savings over traditional symmetric multiprocessing (SMP) servers?

---

ᚦ **Lecture 3: Storage Technologies and Architectures**

**Course:** SA103 — Computer Hardware & Peripherals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview
Storage systems have evolved from spinning hard drives to NVMe solid-state drives and beyond. This lecture covers storage hierarchies, NVMe over Fabrics, storage class memory, distributed storage systems, and the 2040 innovations in computational storage and AI-driven storage optimization.

### Key Topics
- **Storage Hierarchy:** Registers → Cache → DRAM → Storage Class Memory → SSD → HDD → Tape/Object Storage, with 2040 additions of computational storage and neural storage.
- **NVMe and NVMe over Fabrics:** NVMe 2.0 specification, NVMe over TCP/RDMA/FC, and the 2040 *NVMe over CXL 3.0* for sub-microsecond latency.
- **Storage Class Memory (SCM):** Persistent Memory, Zoned Namespaces (ZNS), and the 2040 *Computational Storage Drive* (CSD) with embedded Arm cores for in-situ data processing.
- **Distributed Storage:** Ceph, SeaweedFS, and the 2040 *Yggdrasil Object Mesh* that uses erasure coding and AI-driven data placement for geo-distributed objects.
- **AI-Driven Storage Optimization:** Predictive prefetching, anomaly detection for ransomware, and the 2040 *Storage Genome Project* that maps application I/O patterns to optimal storage configurations.

### Lecture Notes
The storage hierarchy has expanded with the introduction of Storage Class Memory (SCM), which sits between DRAM and traditional SSD in terms of performance, cost, and persistence. Technologies like Intel Optane DC Persistent Memory and CXL-attached memory devices offer microsecond latency, enabling use cases like persistent databases and fast rebootable containers.

NVMe has revolutionized storage access by providing a streamlined, PCIe-based interface with deep command queues and low overhead. NVMe 2.0 introduces features like persistent reservations, namespace management, and end-to-end data protection. NVMe over Fabrics extends NVMe's benefits over network fabrics: NVMe over TCP enables use of standard Ethernet infrastructure, while NVMe over RDMA provides microsecond latency for clustered applications. The 2040 NVMe over CXL 3.0 leverages CXL's cache coherence to allow direct memory access to storage devices with minimal computational overhead.

Computational Storage Drives (CSDs) embed processing power (typically Arm-based SoCs) directly on the storage device, enabling data to be processed where it resides. This reduces data movement and can accelerate operations like compression, encryption, regex matching, and database query pushdown. For example, a CSD can evaluate SQL WHERE clauses on stored data and return only matching rows, significantly reducing host CPU load.

Distributed storage systems like Ceph provide scalable, fault-tolerant object, block, and file storage. The Yggdrasil Object Mesh enhances this with machine learning models that predict object access patterns and proactively replicate or erase-code data to optimize for latency, durability, and cost. The Storage Genome Project analyzes I/O traces from thousands of applications to classify workloads (e.g., streaming, random, mixed) and recommend optimal storage tiering and configuration strategies.

AI-driven storage optimization includes predictive prefetching that anticipates future disk accesses based on historical patterns, and anomaly detection systems that identify ransomware encryption patterns by detecting sudden increases in entropy and write cycles.

### Required Reading
- Anderson, R. & Jensen, C. (2038). *Designing Data-Intensive Applications*, 2nd Edition. O'Reilly Media. Chapters 3-4, 8-9.
- NVM Express, Inc. (2039). *NVMe 2.0 Specification*. Chapters 1-3, 6-7.
- Yggdrasil Storage Optimization Toolkit Documentation (2040). UoY Digital Press.

### Discussion Questions
1. How does computational storage change the traditional CPU-centric model of data processing, and what types of workloads benefit most from in-storage processing?
2. Compare and contrast NVMe over TCP and NVMe over RDMA in terms of performance, complexity, and use cases.
3. Discuss how AI-driven storage optimization could reduce total cost of ownership (TCO) for a large-scale cloud provider.

---

ᚨ **Lecture 4: I/O Interfaces and Connectivity**

**Course:** SA103 — Computer Hardware & Peripherals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview
Input/output (I/O) interfaces connect the computer to the external world. This lecture covers PCI Express, USB, Thunderbolt, Ethernet, and the 2040 advancements in optical I/O, memory-semantic interconnects, and AI-driven link training and optimization.

### Key Topics
- **PCI Express Evolution:** PCIe 5.0, 6.0, and the 2040 *PCIe 7.0* with PAM4 signaling, flit-mode operation, and 512 GT/s raw bandwidth.
- **USB and Thunderbolt:** USB4 Version 3.0, Thunderbolt 5, and the 2040 *Optical USB4* using polymer waveguides for 100-meter reach.
- **Ethernet and Data Center Networking:** 800GbE, 1.6TbE, and the 2040 *Photonic Ethernet* using silicon photonics for terabit-per-second links.
- **Memory-Semantic Interconnects:** Compute Express Link (CXL) 3.0/4.0, OpenCAPI 4.0, and the 2040 *Norn Interconnect* that combines cache coherence with message-passing for heterogeneous systems.
- **AI-Driven Link Training and Optimization:** Machine learning algorithms that adapt equalization, pre-emphasis, and link width based on channel conditions and temperature.

### Lecture Notes
PCI Express remains the dominant I/O interconnect for attaching high-bandwidth devices like GPUs, NVMe SSDs, and FPGA accelerators. PCIe 6.0 introduced PAM4 (Pulse Amplitude Modulation with 4 levels) signaling to double the data rate per lane without doubling the baud rate, and flit-mode operation to reduce latency. PCIe 7.0, expected in late 2040, pushes raw bandwidth to 512 GT/s per lane (approximately 128 GB/s per lane) using advanced signal processing and tighter tolerances.

USB and Thunderbolt have converged, with USB4 incorporating Thunderbolt protocols. The 2040 Optical USB4 uses polymer waveguides embedded in the cable to achieve 100-meter reach without repeaters, enabling peripheral connectivity in large laboratories or industrial settings. Thunderbolt 5 aims for 80 Gbps symmetric bandwidth using PAM3 modulation over four lanes.

Ethernet continues to scale, with 800GbE deployments expanding in 2040 and 1.6TbE prototypes in laboratories. Photonic Ethernet, using silicon photonics to integrate lasers and modulators directly on the silicon chip, promises terabit-per-second links with low power consumption, enabling spine-leaf architectures in massive AI clusters.

Compute Express Link (CXL) has emerged as the key interconnect for memory-semantic acceleration, allowing coherent access to memory and devices attached to the CXL bus. CXL 3.0 adds switching and pooling capabilities, while CXL 4.0 introduces persistent memory and enhanced security features. The Norn Interconnect concept extends CXL with integrated message-passing interfaces, allowing devices to communicate via both shared memory and explicit messaging, optimizing for different communication patterns.

AI-driven link training optimizes high-speed serial links by continuously adjusting equalization, pre-emphasis, and voltage levels based on real-time bit error rate (BER) feedback. Machine learning models predict optimal settings based on temperature, voltage droop, and cable aging, reducing the need for frequent retraining and improving link uptime.

### Required Reading
- PCI-SIG. (2039). *PCI Express 6.0 Specification*. Chapters 1-4, 7-8.
- USB-IF. (2039). *USB4 Version 3.0 Specification*. Chapters 2-3, 5-6.
- IEEE. (2039). *802.3ck 800GbE and 802.3cm 400GbE over Copper Standard*. Clauses 1-4, 90-95.
- Yggdrasil I/O Connectivity Whitepaper (2040). UoY Engineering Press.

### Discussion Questions
1. How does PAM4 signaling in PCIe 6.0 and Ethernet increase bandwidth while presenting new challenges for signal integrity and power consumption?
2. What are the advantages of optical I/O for data center interconnects compared to traditional copper-based solutions?
3. Describe how the Norn Interconnect could improve performance for a distributed database that requires both shared memory access and message-passing coordination.

---

ᚧ **Lecture 5: GPU Architecture and Accelerators**

**Course:** SA103 — Computer Hardware & Peripherals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview
Graphics Processing Units (GPUs) have evolved from graphics rendering to general-purpose parallel computing. This lecture covers GPU architecture, memory systems, software ecosystems, and the 2040 trends toward AI-specific accelerators, optical interconnects, and chiplet-based designs.

### Key Topics
- **GPU Architecture:** SIMT execution, warp scheduling, memory hierarchy (L1/L2 cache, shared memory, HBM), and the 2040 *Mesh Shader Pipeline* for flexible geometry processing.
- **GPU Memory:** High Bandwidth Memory (HBM) generations, HBM4 with 2 TB/s stack bandwidth, and the 2040 *HBM-PIM* that integrates processing cores into the memory stack.
- **GPU Software:** CUDA, ROCm, and the 2040 *Yggdrasil Unified Accelerator Framework* (YUAF) that supports multiple ISAs and memory models.
- **AI Accelerators:** Tensor cores, sparse tensor cores, and the 2040 *Neuromorphic Core* that implements spiking neural networks with memristive synapses.
- **Optical Interconnects and Chiplets:** Silicon photonics for GPU-to-GPU communication, and the 2040 *Chiplet-Based GPU* using advanced packaging (EMIB, Foveros) for heterogeneous integration.

### Lecture Notes
GPUs excel at data-parallel workloads due to their Single Instruction, Multiple Threads (SIMT) architecture, where thousands of cores execute the same instruction on different data points. The warp scheduler groups threads into warps (typically 32 threads) and schedules them for execution, hiding memory latency by switching to other warps when one warp stalls.

The GPU memory hierarchy is critical for performance. Each SM (Streaming Multiprocessor) has a small L1 cache and shared memory for low-latency data sharing within a warp or thread block. The L2 cache is shared across all SMs, and the high-bandwidth memory (HBM) provides massive bandwidth (up to 2 TB/s with HBM4) for feeding the hundreds of SMs with data. HBM-PIM integrates programmable cores (e.g., simple RISC vectors) into the memory stack, enabling operations like vector addition or matrix multiplication to be performed inside the memory die, reducing data movement.

The software ecosystem has matured, with CUDA and ROCm providing robust platforms for GPU computing. The Yggdrasil Unified Accelerator Framework (YUAF) aims to provide a single programming model that targets GPUs, FPGAs, ASICs, and neuromorphic chips, reducing the complexity of managing heterogeneous accelerators.

AI accelerators have evolved from repurposed GPUs to specialized designs. Tensor cores provide mixed-precision matrix multiply-accumulate operations essential for deep learning. Sparse tensor cores exploit the sparsity in neural network weights and activations to achieve 2x or more effective throughput. Neuromorphic cores implement spiking neural networks using memristive devices that emulate synapses, offering extreme energy efficiency for event-driven AI applications.

Optical interconnects using silicon photonics enable high-bandwidth, low-latency communication between GPU chiplets or between GPUs in a multi-GPU module. Chiplet-based designs allow mixing and matching of different technologies (e.g., a high-performance CPU chiplet with an AI accelerator chiplet) using advanced packaging techniques like Embedded Multi-die Interconnect Bridge (EMIB) or Foveros Direct.

### Required Reading
- Owens, J.D. et al. (2037). *GPU Computing Gems Emerald Edition*, 2nd Edition. Morgan Kaufmann. Chapters 1-3, 5-6.
- NVIDIA. (2039). *Whitepaper: NVIDIA Hopper Architecture 2.0*. Sections 2-4.
- Yggdrasil Accelerator Technologies Report (2040). UoY Research Press.

### Discussion Questions
1. How does HBM-PIM change the traditional CPU-GPU data movement model, and what types of algorithms benefit most from in-memory processing?
2. Compare and contrast the architectural approaches of tensor cores versus sparse tensor cores for accelerating deep learning workloads.
3. Discuss the trade-offs between a monolithic GPU design and a chiplet-based GPU in terms of yield, cost, and flexibility.

---

ᚩ **Lecture 6: FPGA Technology and Reconfigurable Computing**

**Course:** SA103 — Computer Hardware & Peripherals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview
Field-Programmable Gate Arrays (FPGAs) provide hardware-level parallelism and low-latency processing. This lecture covers FPGA architecture, design flows, high-level synthesis, and the 2040 advancements in AI-driven placement and routing, partial reconfiguration, and FPGA-as-a-Service models.

### Key Topics
- **FPGA Architecture:** Logic blocks (LUTs, flip-flops), DSP blocks, block RAM, and the 2040 *Adaptive Logic Block* that reconfigures its functionality based on workload characteristics.
- **Design Flows:** Traditional HDL (Verilog/VHDL), high-level synthesis (HLS) from C/C++, and the 2040 *Neural HDL* that generates hardware from natural language descriptions.
- **AI-Driven Placement and Routing:** Machine learning models that predict congestion and optimize placement for power, performance, and area (PPA).
- **Partial Reconfiguration:** Dynamic reconfiguration of FPGA regions while the rest of the device continues operation, and the 2040 *Live Update Framework* for zero-downtime accelerator upgrades.
- **FPGA-as-a-Service and Cloud FPGAs:** AWS F1, Azure NP-series, and the 2040 *Yggdrasil FPGA Mesh* that provides virtualized FPGA resources with QoS guarantees.

### Lecture Notes
FPGAs consist of an array of programmable logic blocks interconnected by a hierarchical routing network. Each logic block typically contains a Look-Up Table (LUT) that can implement any Boolean function of its inputs, along with flip-flops for sequential logic. DSP blocks provide optimized structures for multiply-accumulate operations, and block RAM offers distributed memory for buffers and caches.

The Adaptive Logic Block concept extends traditional logic blocks with the ability to change their internal structure based on configuration bits, allowing a single block to function as a LUT, a distributed RAM, or a shift register as needed, improving utilization for diverse workloads.

Design flows have evolved from low-level HDL to high-level synthesis (HLS), where designers write algorithms in C/C++ and the HLS tool generates RTL (Register Transfer Level) code. This significantly reduces development time and allows software engineers to contribute to hardware acceleration. The 2040 Neural HDL takes this further by accepting natural language descriptions (e.g., "create a FIFO buffer that doubles its depth when full") and generating corresponding hardware, lowering the barrier to FPGA adoption.

AI-driven placement and routing uses machine learning models trained on thousands of previous placements to predict congestion hotspots and suggest optimal placements that minimize wirelength and power consumption. These models can also predict routing congestion and suggest adjustments to achieve timing closure faster.

Partial reconfiguration allows updating a portion of the FPGA (e.g., replacing a cryptographic accelerator with a newer version) while the rest of the device continues processing, enabling field upgrades without system downtime. The Live Update Framework extends this by providing versioning, rollback capabilities, and automated testing to ensure safety.

FPGA-as-a-Service offerings in the cloud provide access to FPGA acceleration without the need to purchase and manage physical hardware. The Yggdrasil FPGA Mesh takes this further by pooling FPGA resources across a data center and providing virtualized FPGAs with guaranteed bandwidth and latency, allowing multiple tenants to share the same physical FPGA with isolation.

### Required Reading
- Trimberger, S.M. (2038). *FPGA Architecture: Survey and Challenges*. Springer. Chapters 2-4, 6-7.
- Xilinx. (2039). *Vitis Unified Software Platform Documentation*, 2024.1. Chapters 3-4, 6-8.
- Intel. (2039). *FPGA Programmable Acceleration Card (PAC) Guide*. Sections 1-3, 5-6.
- Yggdrasil FPGA Orchestration Toolkit Documentation (2040). UoY Digital Press.

### Discussion Questions
1. How does high-level synthesis (HLS) improve productivity for FPGA design, and what limitations does it have compared to manual HDL design for performance-critical applications?
2. Discuss the benefits and challenges of partial reconfiguration for mission-critical systems that require high availability.
3. Describe how an FPGA-as-a-Service model could change the economics of hardware acceleration for startups and small businesses.

---

ᚪ **Lecture 7: Networking Hardware and Smart NICs**

**Course:** SA103 — Computer Hardware & Peripherals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview
Networking hardware has evolved from simple network interface cards (NICs) to smart NICs that offload processing from the host CPU. This lecture covers NIC architectures, TCP/IP offload, RDMA, and the 2040 innovations in programmable data planes, in-network computing, and AI-driven network analytics.

### Key Topics
- **NIC Architecture:** MAC layer, offload engines (TCP/UDP checksum, TSO/LRO), and the 2040 *Smart NIC 3.0* with embedded Arm cores and hardware accelerators for encryption and compression.
- **TCP/IP Offload:** Checksum calculation, segmentation, and the 2040 *TLS Offload* that performs encryption/decryption in hardware.
- **RDMA and RoCE:** Remote Direct Memory Access, RDMA over Converged Ethernet (RoCE v2), and the 2040 *RoCE over Photonic Ethernet* for terabit-per-second memory access.
- **Programmable Data Planes:** P4 language, programmable switches, and the 2040 *In-Network AI Accelerator* that performs inference directly in the network path.
- **AI-Driven Network Analytics:** Telemetry streaming, anomaly detection, and the 2040 *Network Twin* that creates a real-time digital replica of the network for predictive analysis.

### Lecture Notes
Modern Network Interface Cards (NICs) have evolved beyond simple frame transmitters to sophisticated devices that offload processing from the host CPU. The MAC layer handles framing, CRC calculation, and address filtering. Offload engines compute TCP/UDP checksums, perform TCP segmentation offload (TSO) and large receive offload (LRO), reducing CPU utilization for network-intensive workloads.

Smart NIC 3.0 integrates Arm-based processors (typically dual or quad-core Cortex-A78) alongside fixed-function hardware accelerators. These Smart NICs can offload entire network functions: a firewall Smart NIC can perform stateful packet inspection, SSL/TLS offload can handle encryption and decryption, and a storage Smart NIC can implement NVMe target functionality, presenting NVMe namespaces to the host as if they were local devices.

TCP/IP offload extends to higher-layer protocols. TLS Offload in hardware significantly reduces CPU utilization for secure web servers, as the expensive cryptographic operations of AES-GCM and ECDHE are performed in dedicated hardware. This is particularly important for web servers handling thousands of TLS connections per second.

RDMA allows direct memory access between computers without involving the operating system, bypassing the kernel and eliminating copying overhead. RoCE v2 implements RDMA over standard Ethernet with congestion control, enabling its use in data centers without specialized InfiniBand fabric. The 2040 RoCE over Photonic Ethernet extends this to terabit-per-second links using silicon photonics, enabling memory-sharing between GPUs in different racks with microsecond latency.

Programmable data planes, using languages like P4, allow the behavior of network switches and routers to be customized. The In-Network AI Accelerator places trained neural network models directly in the data path of a switch, enabling real-time inference on packet metadata—for example, to detect DDoS attacks or classify traffic flows without sending packets to a central analyzer.

AI-driven network analytics leverages streaming telemetry (int counters, flow records) and applies machine learning to detect anomalies, predict failures, and optimize traffic engineering. The Network Twin concept creates a real-time simulation of the network that mirrors traffic flows, allowing operators to test configuration changes or predict the impact of a link failure before it occurs.

### Required Reading
- Mellanox Technologies. (2039). *Smart NIC Architecture Whitepaper*. Sections 2-4, 6-7.
- The P4 Language Consortium. (2039). *P4_16 Language Specification*, Version 1.2.3. Chapters 1-3, 5-6.
- Jones, C. & Petkovšek, M. (2038). *High Performance Data Center Networking*, 2nd Edition. Springer. Chapters 2-4, 6-8.
- Yggdrasil Networking Hardware Toolkit Documentation (2040). UoY Digital Press.

### Discussion Questions
1. How does TCP Segmentation Offload (TSO) reduce CPU utilization for network transmission, and what are the potential drawbacks if the NIC's segmentation engine malfunctions?
2. Compare and contrast RDMA over InfiniBand and RoCE v2 in terms of performance, ecosystem, and use cases.
3. Discuss the security implications of in-network AI accelerators that inspect packet payloads. How would you ensure privacy and compliance?

---

ᚫ **Lecture 8: Power Supply and Thermal Management**

**Course:** SA103 — Computer Hardware & Peripherals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview
Reliable power delivery and effective thermal management are critical for system stability and longevity. This lecture covers voltage regulation, power stages, cooling technologies, and the 2040 advancements in AI-driven power capping, liquid cooling, and thermoelectric generation.

### Key Topics
- **Voltage Regulation:** Buck converters, multiphase VRMs, and the 2040 *Digital VRM with AI Load Prediction* that anticipates current demands and adjusts phases proactively.
- **Power Stages:** Server power supplies (80 Plus Titanium), DC-DC conversion, and the 2040 *48V DC Distribution* that reduces conversion losses in racks.
- **Cooling Technologies:** Air cooling, liquid cooling (direct-to-chip, immersion), and the 2040 *Two-Phase Thermosyphon* that uses evaporative cooling for high-density GPUs.
- **Thermal Interface Materials:** Thermal pastes, phase-change materials, and the 2040 *Nanotube-Enhanced Thermal Grease* with 5x thermal conductivity of traditional compounds.
- **AI-Driven Power and Thermal Management:** Machine learning models that predict power consumption and temperature based on workload, and the 2040 *Dynamic Voltage and Frequency Scaling* (DVFS) that optimizes for performance-per-watt.

### Lecture Notes
Power delivery begins with the AC-to-DC conversion in the power supply unit (PSU). Modern server PSUs achieve 94-96% efficiency (80 Plus Titanium or better), minimizing wasted energy as heat. The 48V DC distribution architecture reduces losses by distributing power at a higher voltage (48V) and converting to lower voltages (12V, 5V, 3.3V) at the point of load, reducing I^2R losses in the power distribution network.

Voltage regulation is handled by Voltage Regulator Modules (VRMs) that convert the bus voltage (12V or 48V) to the precise voltages required by CPUs, GPUs, and memory. Multiphase VRMs distribute the load across multiple phases (e.g., 6-phase for CPU Vcore), reducing thermal stress on individual components and enabling faster transient response. The Digital VRM with AI Load Prediction uses machine learning to anticipate current spikes based on instruction pipelines and memory access patterns, adjusting the number of active phases before the load change occurs, reducing voltage droop and overshoot.

Cooling is essential to maintain junction temperatures within safe limits. Air cooling uses heatsinks and fans to convect heat away from components. Liquid cooling comes in two forms: direct-to-chip, where cold plates are attached directly to the die, and immersion, where the entire server is submerged in dielectric fluid. The Two-Phase Thermosyphon uses evaporative cooling: liquid absorbs heat at the evaporator, vapor rises to the condenser where it releases heat and returns as liquid, providing high heat flux with minimal pump power.

Thermal interface materials (TIMs) fill microscopic air gaps between the die and the heatsink. Traditional thermal paste has thermal conductivity of 5-8 W/m·K. The 2040 Nanotube-Enhanced Thermal Grease incorporates carbon nanotubes or graphene to achieve thermal conductivity of 25-40 W/m·K, significantly reducing thermal resistance.

AI-driven power and thermal management uses telemetry from power sensors and temperature sensors to build predictive models. These models forecast power consumption and temperature rise for upcoming workloads, allowing proactive adjustments to fan speeds, pump rates, and voltage frequencies. Dynamic Voltage and Frequency Scaling (DVFS) adjusts the operating voltage and frequency of processors based on real-time demand, optimizing for performance-per-watt rather than peak performance.

### Required Reading
- Dixon, L. & Wittig, R. (2038). *Power Supply Design for Motherboards*, 2nd Edition. Springer. Chapters 1-3, 5-6.
- IBM. (2039). *Liquid Cooling for Data Centers: Best Practices*. Sections 2-4, 6-7.
- Yggdrasil Power and Thermal Management Toolkit Documentation (2040). UoY Digital Press.

### Discussion Questions
1. How does a multiphase VRM improve transient response compared to a single-phase VRM when the CPU suddenly demands more current?
2. Compare and contrast direct-to-chip liquid cooling and immersion cooling in terms of complexity, maintenance, and cooling efficiency.
3. Discuss how AI-driven power prediction could reduce energy waste in a data center while maintaining performance SLAs.

---

ᚬ **Lecture 9: Peripheral Devices and Human-Computer Interaction**

**Course:** SA103 — Computer Hardware & Peripherals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview
Peripheral devices extend the computer's capabilities for input, output, and storage. This lecture covers keyboards, mice, displays, printers, and the 2040 advancements in augmented reality (AR), virtual reality (VR), brain-computer interfaces (BCI), and haptic feedback systems.

### Key Topics
- **Input Devices:** Mechanical keyboards, optical mice, touchpads, and the 2040 *Neural Input Interface* that uses EEG and EMG signals for intent-based control.
- **Display Technologies:** LCD, OLED, microLED, and the 2040 *Retinal Projector* that beams images directly onto the retina for augmented reality.
- **Output Devices:** Printers, plotters, and the 2040 *3D Bioprinter* that prints living tissues and organs for medical applications.
- **Storage Peripherals:** External SSDs, tape drives, and the 2040 *DNA Storage Archiver* that encodes digital data into synthetic DNA for long-term archival.
- **Human-Computer Interaction:** Brain-computer interfaces, haptic suits, and the 2040 *Yggdrasil Presence Cube* that provides full-body haptic feedback for virtual environments.

### Lecture Notes
Peripheral devices have evolved significantly, with many traditional peripherals being enhanced or replaced by emerging technologies. Keyboards remain the primary text input device, with mechanical keyboards gaining popularity due to tactile feedback and durability. Optical mice use CMOS sensors to track movement, offering high DPI and low latency. The 2040 Neural Input Interface takes a different approach, using electroencephalography (EEG) to detect brain signals and electromyography (EMG) to detect muscle signals, allowing users to control computers through thought or subtle muscle movements—particularly beneficial for accessibility.

Display technology has seen remarkable advances. LCDs dominate due to cost-effectiveness, but OLEDs offer superior contrast and flexibility. MicroLED combines the benefits of both: high brightness, infinite contrast, and long lifespan without burn-in. The Retinal Projector represents a leap toward seamless augmented reality: by projecting photons directly onto the retina, it bypasses the need for external displays, allowing virtual objects to appear as if they exist in the real world with minimal latency and vergence-accommodation conflict.

Output devices have expanded beyond paper. 3D bioprinters use bio-inks containing living cells to print tissues and organs, enabling research in regenerative medicine and potentially reducing the need for organ transplants. DNA storage archivists synthesize DNA strands to encode digital data, offering extraordinary density (up to 215 petabytes per gram) and longevity (thousands of years) for archival preservation of critical data.

Human-computer interaction is moving beyond traditional peripherals. Brain-computer interfaces (BCIs) are becoming more practical, with non-invasive EEG-based systems allowing users to control cursors or type text through motor imagery. Haptic suits provide force feedback across the body, enhancing immersion in virtual reality and enabling remote tactile communication. The Yggdrasil Presence Cube is a small platform that users stand on, using arrays of actuators to simulate walking, running, and jumping in virtual environments, providing proprioceptive feedback that reduces motion sickness.

These peripherals are increasingly integrated with AI: neural interfaces use machine learning to decode neural signals, retinal projectors use eye-tracking to stabilize the projected image, and presence cubes use force feedback models grounded in physics to simulate realistic interactions.

### Required Reading
- Buxton, B. (2037). *Sketching User Experiences: The Workbook*, 2nd Edition. Morgan Kaufmann. Chapters 2-4, 6-7.
- Samsung Display. (2039). *Whitepaper: MicroLED Technology for AR/VR*. Sections 1-3, 5-6.
- Yggdrasil Peripheral Technologies Report (2040). UoY Research Press.

### Discussion Questions
1. How does a Neural Input Interface based on EEG and EMG differ from traditional brain-computer interfaces that rely on implanted electrodes?
2. Discuss the advantages and challenges of retinal projection for augmented reality compared to head-mounted displays with see-through optics.
3. Describe how DNA storage could be used for long-term archival of scientific data, and what error correction mechanisms are necessary to ensure data integrity over centuries.

---

ᚭ **Lecture 10: Hardware Security and Trusted Execution**

**Course:** SA103 — Computer Hardware & Peripherals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview
Hardware security is essential for protecting data and ensuring system integrity. This lecture covers trusted execution environments, cryptographic accelerators, physical unclonable functions, and the 2040 advancements in AI-driven threat detection, post-quantum cryptography, and hardware-based attestation.

### Key Topics
- **Trusted Execution Environments (TEEs):** Intel SGX, AMD SEV, and the 2040 *Yggdrasil Secure Enclave* (YSE) that provides isolated execution with runtime encryption and remote attestation.
- **Cryptographic Accelerators:** AES-NI, SHA extensions, and the 2040 *Post-Quantum Cryptography Accelerator* that supports lattice-based and hash-based algorithms.
- **Physical Unclonable Functions (PUFs):** SRAM PUFs, ring oscillator PUFs, and the 2040 *Quantum Dot PUF* that uses nanoscale quantum variations for device identification.
- **Hardware-Based Attestation:** TPM 2.0, FIDO2, and the 2040 *Yggdrasil Attestation Chain* that links boot firmware, hypervisor, and OS measurements to a root of trust.
- **AI-Driven Threat Detection:** Side-channel analysis, fault injection detection, and the 2040 *Neural Side-Channel Analyzer* that uses deep learning to detect power and electromagnetic leaks.

### Lecture Notes
Trusted Execution Environments (TEEs) create isolated areas of memory where code and data are protected from privilege software, including the operating system and hypervisor. Intel SGX provides enclaves that are encrypted in memory and decrypted only inside the CPU. AMD SEV encrypts the entire virtual machine's memory, protecting it from the hypervisor and other VMs on the same host. The Yggdrasil Secure Enclave (YSE) extends these concepts with a focus on ease of use and integration with cloud orchestration platforms, offering APIs for secure key management and secure computation offloading.

Cryptographic accelerators offload expensive cryptographic operations from the CPU. AES-NI provides fast AES encryption/decryption, while SHA extensions accelerate hashing algorithms. The 2040 Post-Quantum Cryptography Accelerator is critical as quantum computers threaten to break current public-key cryptography (RSA, ECC). This accelerator supports lattice-based algorithms (e.g., CRYSTALS-Kyber) and hash-based signatures (e.g., SPHINCS+), enabling a smooth transition to post-quantum security.

Physical Unclonable Functions (PUFs) exploit manufacturing variations to create a unique fingerprint for each chip. SRAM PUFs power up the SRAM array in an uninitialized state and read the stable values that emerge due to transistor mismatch. Ring oscillator PUFs measure the frequency of oscillators that vary slightly due to process variations. The 2040 Quantum Dot PUF uses the size and composition of quantum dots embedded during manufacturing, which vary at the nanoscale, to generate cryptographically secure responses.

Hardware-based attestation allows a remote party to verify that a system is running genuine, untampered software. TPM 2.0 stores measurements of boot components (BIOS, bootloader, OS kernel) and can quote them to a verifier. FIDO2 enables passwordless authentication using public-key cryptography stored in a secure element. The Yggdrasil Attestation Chain extends this by creating a chain of trust from the boot firmware through the hypervisor to the guest operating system, allowing verification of the entire software stack.

AI-driven threat detection complements traditional security measures. Side-channel analysis attempts to extract secrets by measuring power consumption, electromagnetic emissions, or timing variations. The Neural Side-Channel Analyzer uses deep learning models trained on labeled power traces to detect subtle leaks that might indicate cryptographic key extraction. Fault injection detection uses sensors to detect abnormal voltage, clock, or temperature fluctuations that could indicate an active attack.

### Required Reading
- Moshchuk, A. et al. (2038). *Hardware Security: A Hands-on Approach*, 2nd Edition. Springer. Chapters 1-3, 5-6.
- National Institute of Standards and Technology (NIST). (2039). *Post-Quantum Cryptography Standardization Project*. Round 3 Finalists.
- Yggdrasil Hardware Security Toolkit Documentation (2040). UoY Digital Press.

### Discussion Questions
1. How does Intel SGX protect enclave memory from a compromised operating system, and what are the limitations of SGX regarding side-channel attacks?
2. Compare and contrast the security properties of SRAM PUFs and Quantum Dot PUFs in terms of uniqueness, reliability, and resistance to modeling attacks.
3. Discuss how AI-driven threat detection could improve the security posture of a hardware security module (HSM) used for key management.

---

ᚮ **Lecture 11: Emerging Technologies: Quantum and Neuromorphic Computing**

**Course:** SA103 — Computer Hardware & Peripherals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview
Beyond classical von Neumann architectures, emerging computing paradigms offer new possibilities. This lecture covers quantum computing fundamentals, neuromorphic engineering, and the 2040 integration of these technologies into heterogeneous systems for specialized workloads.

### Key Topics
- **Quantum Computing:** Qubits, superposition, entanglement, and the 2040 *Error-Corrected Logical Qubit* using surface codes with 99.9% fidelity.
- **Quantum Hardware:** Superconducting qubits, trapped ions, and the 2040 *Photonic Quantum Processor* that uses integrated waveguides and single-photon sources.
- **Neuromorphic Computing:** Spiking neural networks, memristive synapses, and the 2040 *Yggdrasil Neuromorphic Core* that implements online learning with spike-timing-dependent plasticity.
- **Heterogeneous Integration:** Quantum-classical interfaces, neuromorphic-CPU coupling, and the 2040 *CXL for Quantum* that enables coherent access to quantum memory.
- **Application-Specific Acceleration:** Quantum annealers for optimization, neuromorphic sensors for event-driven processing, and the 2040 *Yggdrasil Quantum-Enhanced AI* that uses quantum co-processors for specific machine learning subroutines.

### Lecture Notes
Quantum computing leverages quantum bits (qubits) that can exist in superpositions of 0 and 1, enabling quantum parallelism. Entanglement allows qubits to be correlated in ways that classical bits cannot. However, qubits are fragile and susceptible to decoherence from interactions with the environment. Quantum error correction (QEC) encodes logical qubits into multiple physical qubits to detect and correct errors. The 2040 Error-Corrected Logical Qubit achieves 99.9% fidelity using surface codes, allowing complex algorithms like Shor's factoring or quantum simulation to run reliably.

Quantum hardware platforms vary. Superconducting qubits, operated at millikelvin temperatures, offer fast gate times but require elaborate cryogenic systems. Trapped ions provide long coherence times and high connectivity but slower gate speeds. The 2040 Photonic Quantum Processor uses silicon photonics to generate, manipulate, and detect single photons, offering the potential for room-temperature operation and easy integration with classical photonic interconnects.

Neuromorphic computing mimics the brain's architecture using spiking neurons and memristive synapses. Neurons communicate via spikes (action potentials), and synaptic strength changes based on the timing of spikes (spike-timing-dependent plasticity, STDP). The Yggdrasil Neuromorphic Core implements large arrays of neurons and synapses on a single chip, enabling low-power pattern recognition and sensory processing. Online learning allows the network to adapt to changing statistics without external training.

Heterogeneous integration is key to practical adoption. The CXL for Quantum initiative aims to extend Compute Express Link to quantum systems, allowing coherent access to quantum memory from classical CPUs. This enables hybrid algorithms where classical processors handle control flow and quantum co-processors execute speedup-intensive subroutines. Neuromorphic-CPU coupling allows neuromorphic sensors to preprocess data (e.g., edge detection in vision) before sending results to a CPU for higher-level processing.

Application-specific acceleration highlights where these technologies excel. Quantum annealers excel at optimization problems (e.g., traveling salesman, portfolio optimization) by exploiting quantum tunneling to escape local minima. Neuromorphic sensors are ideal for always-on, low-power sensing (e.g., audio keyword spotting, vibration monitoring) due to their event-driven nature. The Yggdrasil Quantum-Enhanced AI explores using quantum co-processors to accelerate specific subroutines in machine learning pipelines, such as sampling in Bayesian networks or solving linear systems in quantum machine learning.

### Required Reading
- Nielsen, M.A. & Chuang, I.L. (2038). *Quantum Computation and Quantum Information*, 2nd Edition. Cambridge University Press. Chapters 1-4, 7-8.
- Mead, C. (2039). *Neuromorphic Electronic Systems*, 2nd Edition. Proceedings of the IEEE. Chapters 2-4, 6-7.
- Yggdrasil Emerging Computing Technologies Report (2040). UoY Research Press.

### Discussion Questions
1. How does quantum error correction enable scalable quantum computing despite the fragility of individual qubits, and what overhead does it impose in terms of physical qubits per logical qubit?
2. Compare and contrast superconducting qubits and trapped ions in terms of gate speed, coherence time, and scalability to large numbers of qubits.
3. Discuss how neuromorphic computing could enable always-on sensor nodes that operate for years on a small battery, and what types of applications benefit most from this approach.

---

ᚯ **Lecture 12: System Design, Evaluation, and Benchmarking**

**Course:** SA103 — Computer Hardware & Peripherals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview
Designing and evaluating computer systems requires a systematic approach. This lecture covers workload characterization, performance metrics, benchmarking suites, and the 2040 methodologies for AI-driven performance prediction, energy-proportional design, and total cost of ownership analysis.

### Key Topics
- **Workload Characterization:** CPU-bound, memory-bound, I/O-bound, and the 2040 *Workload Genome Project* that classifies applications by resource usage patterns.
- **Performance Metrics:** Throughput, latency, response time, and the 2040 *Quality-of-Experience (QoE) Metric* that incorporates user perception for interactive applications.
- **Benchmarking Suites:** SPEC CPU, SPECjbb, TPC-C, and the 2040 *Yggdrasil System Benchmark Suite* (YSBS) that includes AI training, inference, and real-time analytics workloads.
- **AI-Driven Performance Prediction:** Machine learning models that predict performance based on hardware specifications and workload characteristics.
- **Energy-Proportional Design:** The principle that power scales with utilization, and the 2040 *Dynamic Power Gating* that powers down unused components in milliseconds.
- **Total Cost of Ownership (TCO):** Acquisition cost, energy cost, maintenance cost, and the 2040 *Carbon-Aware TCO* that includes environmental impact.

### Lecture Notes
Effective system design begins with understanding the workload. Workload characterization identifies whether an application is limited by CPU cycles, memory bandwidth, I/O operations, or network latency. The Workload Genome Project analyzes thousands of applications to classify them into categories (e.g., web server, database, AI training, HPC simulation) and provides detailed resource usage profiles (CPU instructions per second, memory bandwidth, disk I/O, network packets). This classification helps architects select appropriate hardware—for example, a memory-bound workload benefits from high-bandwidth memory and caching, while an I/O-bound workload benefits from fast storage and network interfaces.

Performance metrics must align with the goals of the system. Throughput measures the amount of work completed per unit time (e.g., requests per second). Latency measures the delay between request and response (e.g., time to first byte). For interactive applications, latency critically affects user experience. The 2040 Quality-of-Experience (QoE) Metric goes beyond traditional metrics by incorporating factors like jitter, packet loss, and user satisfaction surveys to provide a holistic view of service quality from the user's perspective.

Benchmarking suites provide standardized workloads for comparing systems. SPEC CPU measures integer and floating-point performance. SPECjbb evaluates Java-based server-side business logic. TPC-C simulates an online transaction processing workload. The Yggdrasil System Benchmark Suite (YSBS) extends these with modern workloads: AI training (using ResNet-50 on ImageNet), inference (using BERT for natural language processing), and real-time analytics (processing streaming financial data with complex event processing). This ensures benchmarks remain relevant to 2040 workloads.

AI-driven performance prediction uses machine learning models trained on benchmark results from thousands of hardware configurations. These models take as input hardware specifications (core count, cache size, memory bandwidth) and workload characteristics (from the Workload Genome) and predict metrics like throughput and latency. This enables rapid exploration of design options without building physical prototypes.

Energy-proportional design aims to make power consumption scale linearly with utilization. Ideally, a system at 50% utilization should consume 50% of its peak power. Dynamic Power Gating extends clock gating by completely powering down unused blocks (e.g., idle CPU cores, unused memory banks) in milliseconds, reducing leakage power to near zero. This is particularly important for data centers where servers often run at low utilization.

Total Cost of Ownership (TCO) considers all costs over the system's lifetime: acquisition, energy, maintenance, and disposal. The 2040 Carbon-Aware TCO extends this by incorporating the environmental impact of manufacturing and operation, measured in carbon dioxide equivalents. This encourages the selection of energy-efficient hardware and the use of renewable energy sources in data centers.

### Required Reading
- Hennessy, J.L. & Patterson, D.A. (2039). *Computer Architecture: A Quantitative Approach*, 7th Edition. Morgan Kaufmann. Chapters 1-3, 5-6.
- SPEC. (2039). *SPEC CPU 2039 Release Notes*. Chapters 1-2, 4-5.
- Yggdrasil System Benchmarking Toolkit Documentation (2040). UoY Digital Press.

### Discussion Questions
1. How does the Workload Genome Project help data center operators make informed hardware purchasing decisions, and what privacy considerations arise from collecting detailed workload profiles?
2. Compare and contrast traditional latency-focused metrics with the Quality-of-Experience (QoE) Metric for evaluating the performance of a video conferencing system.
3. Discuss the trade-offs between energy-proportional design and performance guarantees. How would you ensure that power-saving mechanisms do not violate latency SLAs for critical workloads?

---

## Final Examination Preparation

**Course:** SA103 — Computer Hardware & Peripherals
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Sample Essay Questions (Choose 4 of 8)

1. Compare and contrast the von Neumann architecture with emerging non-von Neumann paradigms (e.g., neuromorphic, in-memory computing). Discuss the advantages and limitations of each for general-purpose computing.
2. Explain how Compute Express Link (CXL) enables memory disaggregation and describe two use cases where this technology provides significant advantages over traditional symmetric multiprocessing (SMP) architectures.
3. Describe the evolution of GPU architecture from graphics rendering to general-purpose parallel computing and AI acceleration. How do tensor cores and sparse tensor cores differ in their approach to accelerating deep learning workloads?
4. Evaluate the trade-offs between air cooling, direct-to-chip liquid cooling, and immersion cooling for high-density GPU servers. Consider factors such as cooling efficiency, complexity, maintenance, and cost.
5. How does the Yggdrasil Secure Enclave (YSE) provide trusted execution for cloud workloads? Describe the mechanisms of memory encryption, isolation, and remote attestation that protect code and data from privileged software.
6. Discuss the role of AI in modern hardware design and optimization. Provide at least three specific examples of AI-driven innovations covered in this course (e.g., AI-driven placement and routing for FPGAs, predictive memory scheduling, neural side-channel analysis).
7. Compare and contrast quantum computing and neuromorphic computing in terms of their underlying principles, current technological maturity, and potential applications. Which paradigm is better suited for optimization problems, and which for sensory processing?
8. Describe the process of designing and evaluating a computer system for a specific workload. Include workload characterization, selection of performance metrics, benchmarking, and total cost of ownership analysis. How does AI-driven performance prediction enhance this process?

### Research Paper Prompt (Alternative to Essay Questions)

**Topic:** The Impact of Emerging Hardware Technologies on Data Center Architecture in 2040

**Requirements:**
- 3000-3500 words
- Minimum of 10 scholarly sources (real or plausible 2040 publications)
- Include sections on: historical evolution of data center hardware, specific emerging technologies (at least four), impact on system design and operational practices, energy efficiency and sustainability considerations, and future outlook
- Use proper academic citation format (APA or IEEE)
- Submit via the Yggdrasil Learning Management System by the deadline specified in the syllabus
