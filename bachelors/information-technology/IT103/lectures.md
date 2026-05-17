# IT103: Computer Hardware and Systems
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4
**Prerequisites:** IT101 (Foundations of Information Technology)
**Description:** A hands-on, technically rigorous exploration of computer hardware architecture, component-level functionality, and systems administration fundamentals. Students learn to assemble, configure, troubleshoot, and maintain physical computing systems ranging from embedded IoT devices to rack-mounted servers. The course covers processor architectures, memory technologies, storage subsystems, power delivery, thermal management, peripheral interfaces, and the diagnostic methodologies that distinguish professional technicians from amateur tinkerers. By 2040, hardware is increasingly abstracted behind virtualisation and cloud layers, yet the physical layer remains the irreducible foundation upon which all software rests. Understanding hardware is not nostalgia; it is the bedrock of reliable system design.

---

## Lecture 1: The Physical Layer — Electrons, Silicon, and the Limits of Computation

All computation is, at bottom, a physical process. Electrons flow through semiconductor channels, magnetic domains align in storage media, photons carry data through fibre-optic cables, and quantum states evolve in cryogenic processors. This lecture examines the physics of computation and the engineering constraints that shape hardware design.

**Semiconductor physics** is the foundation of modern computing. A **semiconductor** (typically silicon, though gallium nitride and silicon carbide are increasingly used for power electronics) has electrical conductivity between that of a conductor and an insulator. By **doping** — introducing impurity atoms — semiconductors can be made **n-type** (excess electrons) or **p-type** (electron deficiencies, called holes). A **transistor** is a semiconductor device that uses a small voltage to control a larger current flow. The **MOSFET** (Metal-Oxide-Semiconductor Field-Effect Transistor) is the dominant transistor type: it has a gate, source, and drain, and the voltage at the gate controls the current between source and drain. The **CMOS** (Complementary MOS) technology pairs n-type and p-type MOSFETs to create logic gates that consume power only during switching — the basis of virtually all modern digital logic.

**The physics of scaling** has driven the exponential growth of computing power. As transistors shrink, they switch faster and consume less power per operation. However, scaling below ~5 nanometres introduces **quantum tunnelling**: electrons leak through the thin gate oxide even when the transistor is supposedly off, causing standby power consumption. **Thermal noise** becomes significant as the energy per bit approaches kT (the thermal energy at room temperature, ~26 meV). **Variability** increases: dopant atoms are countable, and random fluctuations in dopant placement cause variations in transistor characteristics. **Interconnect delay** dominates: as transistors shrink, the wires connecting them do not scale proportionally, and signal propagation delays across the chip become the limiting factor. By 2040, the industry has shifted from pure geometric scaling to **3D integration** (stacking multiple silicon dies vertically) and **chiplets** (assembling multiple smaller dies into a single package) to continue performance improvements.

**Emerging physical technologies** in 2040 include: **spintronics** (using electron spin rather than charge to represent information); **memristors** (non-volatile resistive memory that can also perform computation); **photonic interconnects** (using light for on-chip and chip-to-chip communication); **superconducting logic** (using Josephson junctions for ultra-low-power, high-speed computation); and **quantum dots** (semiconductor nanocrystals that confine electrons in three dimensions, used in some quantum computing platforms). None of these has yet displaced CMOS for general-purpose computing, but each is active in research and niche applications.

The **University of Yggdrasil's Materials Lab** maintains a cleanroom facility for student experimentation with semiconductor fabrication at the 100-nanometre node — ancient by industry standards but sufficient for teaching the principles of photolithography, etching, deposition, and doping. Students in IT103 fabricate simple transistors and logic gates as a capstone hardware exercise, connecting the abstract Boolean algebra of IT101 to the physical reality of electrons in silicon.

**Required Reading:**
- Jan M. Rabaey, Anantha Chandrakasan & Borivoje Nikolić, *Digital Integrated Circuits: A Design Perspective* (2nd ed., Prentice Hall, 2003/2035), ch. 1–3
- Mark Bohr, "The Evolution of Scaling from the Homogeneous Era to the Heterogeneous Era," *Intel Technology Journal* 15, no. 2 (2011/2035): 1–12
- Sayeef Salahuddin & Supriyo Datta, "Use of Negative Capacitance to Provide Voltage Amplification for Low Power Nanoscale Devices," *Nano Letters* 8 (2008): 405–410
- University of Yggdrasil, "Student Cleanroom Fabrication Manual: 100nm CMOS Process" (2039)

**Discussion Questions:**
1. CMOS scaling has been the engine of computing progress for 50 years. Is the shift to 3D integration and chiplets a genuine continuation of exponential progress, or an admission that the old paradigm has ended?
2. Quantum tunnelling is a quantum mechanical effect that becomes problematic at small scales. Is tunnelling an engineering problem to be solved, or a fundamental physical limit that will eventually halt all scaling?
3. The Yggdrasil cleanroom uses a 100nm process for teaching. Does hands-on fabrication at an obsolete node provide meaningful educational value, or would simulation tools provide equivalent understanding at lower cost?

---

## Lecture 2: Processor Architecture — x86, ARM, RISC-V, and Beyond

The processor is the brain of the computer, and its architecture determines what the machine can do, how fast it can do it, and how efficiently it uses power. This lecture examines the major processor architectures of 2040 and the design trade-offs that distinguish them.

**x86** (originally Intel 8086, 1978) is the dominant architecture for desktops, laptops, and servers. It is a **CISC** (Complex Instruction Set Computer) architecture: instructions are variable-length, complex (a single instruction can perform a multi-step operation), and backward-compatible across decades. This compatibility is both x86's greatest strength and its greatest burden: modern x86 processors decode CISC instructions into internal RISC-like micro-operations, adding complexity and power overhead. **Intel** and **AMD** are the primary x86 vendors. In 2040, x86 processors have evolved into **hybrid architectures** (Intel's 14th–20th generation Core processors, AMD's Ryzen 9000–15000 series) combining high-performance cores and power-efficient cores on the same die, similar to the ARM big.LITTLE approach.

**ARM** (Advanced RISC Machine) is a **RISC** (Reduced Instruction Set Computer) architecture: instructions are fixed-length, simple, and execute in a single cycle. ARM dominates mobile devices, embedded systems, and — increasingly — servers and laptops (Apple's M-series processors, Amazon's Graviton instances, Microsoft's Cobalt). ARM's **licensing model** (ARM designs the architecture and licenses it to other companies, who design their own implementations) has created a vibrant ecosystem of processor designs optimised for different power, performance, and cost points. In 2040, **ARMv10** is the latest architecture revision, introducing features for AI acceleration, memory tagging, and confidential computing.

**RISC-V** is an open-source instruction set architecture (ISA) developed at UC Berkeley. Unlike x86 and ARM, RISC-V is freely available: anyone can design, manufacture, and sell RISC-V processors without paying licensing fees. RISC-V has gained significant traction in embedded systems, AI accelerators, and educational environments. In 2040, **RISC-V International** (the governing body) has ratified the Vector extension (for SIMD operations), the Hypervisor extension (for virtualisation), and the Matrix extension (for AI/ML workloads). The University of Yggdrasil's **Hálogi Board** — a RISC-V-based single-board computer designed for IT education — is the standard platform for IT103 lab exercises.

**Specialised architectures** complement general-purpose processors. **GPUs** (NVIDIA, AMD) contain thousands of simple cores optimised for data-parallel workloads. **TPUs** and **NPUs** (Neural Processing Units) accelerate matrix operations for machine learning. **DSPs** (Digital Signal Processors) optimise for real-time signal processing. **FPGAs** (Field-Programmable Gate Arrays) allow hardware to be reconfigured for specific tasks. The **2040 server landscape** is increasingly **heterogeneous**: a typical server contains x86 or ARM CPUs, NVIDIA or AMD GPUs, and dedicated AI accelerators, all sharing memory through **CXL** (Compute Express Link) or **UCIe** (Universal Chiplet Interconnect Express) interconnects.

**Required Reading:**
- John L. Hennessy & David A. Patterson, *Computer Architecture: A Quantitative Approach* (6th ed., 2019/2035), ch. 2–3
- David A. Patterson, "Reduced Instruction Set Computers," *Communications of the ACM* 28, no. 1 (1985): 8–21
- Krste Asanović et al., "The Case for Open Instruction Sets," *Microprocessor Report* (2014)
- University of Yggdrasil, "The Hálogi Board: A RISC-V Platform for IT Education" (2039)

**Discussion Questions:**
1. x86's backward compatibility is a 40-year burden. Would the industry be better off if Intel had abandoned compatibility at some point, or is the cost of transition too high?
2. ARM's licensing model has created a diverse ecosystem, but it also fragments the software landscape (different ARM implementations have different performance characteristics). Is fragmentation a price worth paying for diversity?
3. RISC-V is open-source and free, but the most advanced RISC-V implementations are proprietary. Is the "open" nature of RISC-V genuine, or is it merely a marketing advantage for companies that build closed implementations?

---

## Lecture 3: Memory Systems — From DRAM to DNA

Memory is the workspace of computation: the place where data and instructions reside while they are being processed. The design of memory systems is a compromise between speed, capacity, cost, and persistence. This lecture examines the memory hierarchy and the technologies that populate it.

**DRAM** (Dynamic Random Access Memory) is the standard working memory for computers. Each bit is stored as a charge in a capacitor; because the charge leaks over time, DRAM must be **refreshed** (read and rewritten) every few milliseconds. DRAM is **volatile**: when power is removed, the data is lost. The latency of DRAM access is ~10–100 nanoseconds, and its bandwidth is ~20–100 GB/s per channel. In 2040, **DDR6** is the standard for desktop and server memory, with data rates of ~12,800 MT/s and improved power efficiency. **HBM** (High Bandwidth Memory) stacks multiple DRAM dies vertically with through-silicon vias (TSVs), providing extreme bandwidth (~1–2 TB/s) for GPUs and AI accelerators. **CXL.memory** is a new protocol that allows memory to be shared across multiple processors and accelerators in a rack, creating a **memory fabric** that transcends the boundaries of a single chip.

**SRAM** (Static Random Access Memory) is faster (~1–10 ns latency) and does not require refreshing, but it is less dense and more expensive than DRAM. SRAM is used for **processor caches** (L1, L2, L3): small, fast memories that hold frequently accessed data close to the CPU. **Cache design** is a critical aspect of processor performance: larger caches reduce misses but increase latency and power consumption; more associative caches reduce conflicts but increase complexity. In 2040, **last-level caches** (L3 or L4) have grown to 256–512 MB on high-end processors, and some server processors include **HBM as a cache layer** between DRAM and storage.

**Non-volatile memory** retains data without power. **NAND flash** (SSD) is the dominant non-volatile storage technology: it stores data as charge in floating-gate transistors, organised into pages and blocks. **QLC** (Quad-Level Cell) NAND stores 4 bits per cell, maximising density at the cost of endurance and performance. In 2040, **3D NAND** has reached 500+ layers, with capacities of 10–30 TB per drive. **NAND flash** wears out: each cell can withstand only a finite number of write/erase cycles (~1,000–10,000 for QLC). **Wear levelling** and **over-provisioning** are the techniques used to distribute writes evenly and extend drive lifetime. **PCIe 6.0** and **CXL** provide the high-speed interfaces for NVMe SSDs, achieving sequential read speeds of ~30 GB/s.

**Emerging memory technologies** in 2040 include: **MRAM** (Magnetoresistive RAM), which uses magnetic tunnel junctions for non-volatile, high-endurance storage; **ReRAM** (Resistive RAM), which changes resistance in metal oxides; **PCM** (Phase-Change Memory), which uses the phase of chalcogenide glasses; and **FeRAM** (Ferroelectric RAM). None of these has displaced NAND flash for bulk storage, but they are used in specialised applications (embedded systems, neuromorphic computing, persistent memory tiers). **DNA storage** (discussed in IT101) and **holographic storage** remain experimental for general-purpose computing.

**Required Reading:**
- Bruce Jacob, Spencer Ng & David Wang, *Memory Systems: Cache, DRAM, Disk* (Morgan & Claypool, 2008/2035), ch. 1–4
- Naveen Muralimanohar, Rajeev Balasubramonian & Norman P. Jouppi, "Optimizing NUCA Organizations and Wiring Alternatives for Large Caches with CACTI 6.0," *MICRO 2007*
- Micron Technology, "3D NAND Technology: Scaling to 500+ Layers" (2035 white paper)
- University of Yggdrasil, "CXL.memory Fabric Performance in the Muninn Cluster" (2039)

**Discussion Questions:**
1. The memory hierarchy is a response to the divergence in speed and cost between different memory technologies. If a single technology could provide the speed of SRAM, the capacity of DRAM, and the persistence of flash at a reasonable cost, would the memory hierarchy become obsolete?
2. QLC NAND maximises density but has poor endurance. For consumer workloads (where writes are relatively infrequent), is QLC a good trade-off? For data centre workloads (where writes are intensive), should TLC or MLC still be preferred?
3. CXL.memory enables memory pooling across multiple servers. Does this create a single point of failure, or does the redundancy of pooled memory actually improve reliability?

---

## Lecture 4: Storage Subsystems — HDDs, SSDs, and the Hierarchy of Persistence

While memory provides fast, volatile workspace, storage provides persistent, large-capacity data retention. This lecture examines the technologies, architectures, and performance characteristics of modern storage systems.

**Hard disk drives (HDDs)** use spinning magnetic platters and read/write heads to store data. Despite being a 60-year-old technology, HDDs remain relevant in 2040 for **cold storage** (infrequently accessed data) due to their low cost per gigabyte (~$0.01/GB). Modern HDDs use **HAMR** (Heat-Assisted Magnetic Recording) or **MAMR** (Microwave-Assisted Magnetic Recording) to achieve areal densities of 5–10 Tb/in², enabling capacities of 50–100 TB per drive. However, HDDs are **mechanical**: they have moving parts that wear out, they are sensitive to shock and vibration, and their random access performance is poor (~5–10 ms seek time). **SMR** (Shingled Magnetic Recording) overlaps tracks to increase density but reduces write performance, making SMR drives suitable only for sequential write workloads (archival, backup, video surveillance).

**Solid-state drives (SSDs)** have no moving parts: they store data in NAND flash memory and access it electronically. SSDs are **faster** (microsecond-level access times), **more durable** (no mechanical wear), **quieter**, and **more power-efficient** than HDDs. The trade-off is **cost** (~$0.05–0.10/GB in 2040) and **endurance** (finite write cycles). SSD performance depends on the **controller**: the chip that manages flash memory, performs wear levelling, handles error correction, and optimises read/write patterns. High-end SSD controllers include **DRAM caches** for mapping tables and **AI-based predictors** for prefetching and write coalescing. **ZNS** (Zoned Namespaces) SSDs expose the underlying erase-block structure to the host, allowing the file system to optimise write patterns and reduce write amplification.

**Storage architectures** range from direct-attached storage (DAS) to network-attached storage (NAS) to storage area networks (SAN). **DAS** is storage directly connected to a server (SATA, SAS, NVMe). **NAS** is storage accessed over the network via file protocols (NFS, SMB/CIFS). **SAN** is a dedicated network for block-level storage access (Fibre Channel, iSCSI, NVMe-oF). In 2040, **software-defined storage (SDS)** abstracts the physical storage into virtual pools that can be managed programmatically. **Distributed storage systems** (Ceph, GlusterFS, MinIO) aggregate storage from multiple servers into a unified namespace with replication and erasure coding for fault tolerance. **Object storage** (Amazon S3, OpenStack Swift, Ceph RADOS) is the dominant model for cloud storage: data is stored as objects with metadata and unique identifiers, accessed via HTTP APIs.

**The University of Yggdrasil's Mímir Archive** (introduced in IT101) uses a tiered storage architecture: **hot tier** (NVMe SSD, for active research data); **warm tier** (SATA SSD, for recently completed projects); **cold tier** (HDD, for historical data); **archive tier** (tape, for regulatory compliance); and **deep archive** (DNA and sapphire, for cultural heritage preservation). Students in IT103 design and implement a miniature version of this hierarchy using Raspberry Pi devices, USB SSDs, and simulated tape backups, gaining hands-on experience with tiering policies and migration workflows.

**Required Reading:**
- Richard E. Matick, *Computer Storage Systems and Technology* (Wiley, 1977/2035), ch. 1, 5, 8
- Nitin Agrawal, Vijayan Prabhakaran, Ted Wobber & John D. Davis, "Design Tradeoffs for SSD Performance," *ATC 2008*
- Ceph Documentation, "Ceph Architecture" (2040), <https://docs.ceph.com/en/latest/architecture/>
- University of Yggdrasil, "Mímir Archive: Tiered Storage Policy and Migration Workflows" (2039)

**Discussion Questions:**
1. HDDs are a mature technology with limited further improvement. Will HDDs eventually disappear, or will their low cost per gigabyte ensure a permanent niche in cold storage?
2. ZNS SSDs expose the flash translation layer to the host, shifting complexity from the SSD controller to the host software. Is this a genuine architectural improvement, or does it merely move the problem without solving it?
3. DNA and sapphire storage are used in the Mímir Archive for million-year preservation. What are the practical challenges of retrieving data from these formats, and how does the archive ensure that future generations will be able to decode them?

---

## Lecture 5: Power, Cooling, and the Thermodynamics of Data Centres

Computers consume electricity and generate heat. At the scale of a data centre, power and cooling are not afterthoughts; they are primary design constraints that determine location, architecture, and operational cost. This lecture examines the thermodynamics of computation and the engineering of data centre infrastructure.

**Power delivery** in a data centre begins at the utility substation and flows through transformers, UPS (Uninterruptible Power Supply) systems, PDUs (Power Distribution Units), and finally to the servers. **PUE** (Power Usage Effectiveness) is the ratio of total facility power to IT equipment power; a PUE of 1.0 would mean all power goes to computation, while a PUE of 2.0 means half is lost to cooling and other overheads. In 2020, average PUE was ~1.6; by 2040, hyperscale data centres achieve PUE of 1.05–1.15 through advanced cooling and waste heat recovery. The University of Yggdrasil's **Muninn Computing Centre** achieves a PUE of 1.08, powered by geothermal and hydroelectric energy, with waste heat directed to the campus district heating system.

**Server power consumption** is dominated by the CPU, memory, and storage. A high-end server CPU in 2040 consumes 200–400W under load; a GPU can consume 500–1000W; and a fully populated server rack can draw 50–100 kW. **Dynamic Voltage and Frequency Scaling (DVFS)** reduces power consumption when the system is idle or under light load. **Power capping** limits the maximum power draw of a server or rack to prevent overload. **Workload scheduling** can shift compute-intensive tasks to times or locations with cheaper or cleaner energy. In 2040, **carbon-aware scheduling** is standard practice: workloads are directed to data centres with low carbon intensity (high renewable generation) and away from data centres powered by fossil fuels.

**Cooling technologies** have evolved significantly. **Air cooling** (traditional computer room air conditioning, CRAC) is simple but inefficient at high densities. **Liquid cooling** (direct-to-chip, immersion, or rear-door heat exchangers) removes heat more efficiently and enables higher power densities. **Immersion cooling** submerges servers in a dielectric fluid (mineral oil or engineered fluorocarbons), achieving extremely efficient heat transfer and enabling rack densities of 100+ kW. **Free cooling** uses outside air or water when ambient temperatures are low, reducing or eliminating mechanical refrigeration. In the Nordic region, free cooling is available for 8–10 months per year, making it an ideal location for energy-efficient data centres. The **Nordic Cloud Collective** (discussed in IT101) leverages this advantage to offer carbon-negative cloud services.

**The thermodynamic limit** of computation is given by **Landauer's principle**: erasing one bit of information requires a minimum energy of kT ln(2) (~0.017 eV at room temperature, or ~3 × 10⁻²¹ joules). Current computers operate many orders of magnitude above this limit (~10⁻¹⁵ joules per logic operation), but as scaling continues, the gap narrows. **Reversible computing** (computing that does not erase information) could theoretically approach zero energy dissipation, but it requires new hardware paradigms and programming models that are not yet practical. In 2040, reversible computing remains an active research area at the University of Yggdrasil's Theoretical Computing Lab.

**Required Reading:**
- Jonathan G. Koomey, *Turning Numbers into Knowledge: Mastering the Art of Problem Solving* (Analytics Press, 2004/2035), ch. 12 ("Data Centre Energy")
- Luiz André Barroso, Jimmy Clidaras & Urs Hölzle, "The Datacenter as a Computer: An Introduction to the Design of Warehouse-Scale Machines* (3rd ed., Morgan & Claypool, 2019/2035), ch. 4–5
- Eric Masanet et al., "Recalibrating Global Data Centre Energy-Use Estimates," *Science* 367 (2020): 984–986
- ASHRAE, *Thermal Guidelines for Data Processing Environments* (5th ed., 2035)
- University of Yggdrasil, "Geothermal-Powered Data Centres: The Muninn PUE 1.08 Design" (2039)

**Discussion Questions:**
1. PUE is a useful metric but imperfect: it does not account for the carbon intensity of the electricity source. Should data centres be required to report **carbon usage effectiveness (CUE)** instead of or in addition to PUE?
2. Immersion cooling enables extreme power densities but introduces new challenges (fluid maintenance, component compatibility, fire safety). Is immersion cooling the future of high-density computing, or will it remain a niche technology?
3. Landauer's principle sets a thermodynamic limit on computation, but current computers are ~10²⁴ times above this limit. Is reversible computing a realistic goal, or is the engineering difficulty insurmountable?

---

## Lecture 6: Peripheral Interfaces and External Connectivity

A computer is not an island; it connects to the world through a variety of interfaces and protocols. This lecture examines the physical and logical connections that enable computers to interact with humans, other computers, and the physical environment.

**Display interfaces** connect the computer to monitors. **HDMI** (High-Definition Multimedia Interface) and **DisplayPort** are the dominant wired standards in 2040, supporting 8K and 16K resolutions at high refresh rates. **Wireless display** (Wi-Fi Direct, Miracast, AirPlay) is common for consumer devices but has higher latency than wired connections. **VR/AR headsets** use specialised interfaces (DisplayPort Alt Mode over USB-C, or proprietary wireless protocols) to deliver high-resolution, low-latency video to each eye. The **University of Yggdrasil's VR Lab** uses DisplayPort 3.0 over fibre-optic cables to drive 16K per-eye headsets with sub-10ms motion-to-photon latency.

**USB** (Universal Serial Bus) is the dominant general-purpose peripheral interface. **USB4** (based on Thunderbolt 3/4 technology) provides 40–80 Gbps of bandwidth, carrying data, video, and power over a single cable. **USB-C** is the universal connector: reversible, compact, and capable of delivering up to 240W of power (USB Power Delivery 3.1). In 2040, virtually all consumer devices use USB-C, and the European Union's mandate (effective 2024) has accelerated the elimination of proprietary connectors. **Thunderbolt 5** (Intel, 2030) extends USB4 with 120 Gbps bandwidth and improved daisy-chaining for professional workflows.

**Networking interfaces** connect computers to networks. **Ethernet** (wired LAN) operates at 100 Gbps in data centres and 10 Gbps in desktops, with **200G/400G Ethernet** emerging for backbone networks. **Wi-Fi 7** (802.11be, 2024) and **Wi-Fi 8** (802.11bn, 2032) provide multi-gigabit wireless speeds through **MIMO** (Multiple-Input Multiple-Output), **OFDMA** (Orthogonal Frequency Division Multiple Access), and **mmWave** (millimetre-wave) frequencies. **5G** and **6G** cellular networks provide wide-area connectivity for mobile devices, with 6G offering peak speeds of 1 Tbps and sub-millisecond latency. **Optical networking** (fibre optics) dominates long-distance and high-bandwidth connections, with **800G/1.6T coherent optics** standard in data centre interconnects.

**Industrial and embedded interfaces** include: **RS-232/RS-485** (legacy serial interfaces still used in industrial control); **CAN bus** (Controller Area Network, used in automotive and industrial systems); **I2C** and **SPI** (short-distance serial buses for connecting sensors and microcontrollers); **GPIO** (General-Purpose Input/Output, for direct digital control); **PCIe** ( Peripheral Component Interconnect Express, for high-speed internal expansion); and **NVMe** (Non-Volatile Memory Express, for high-speed storage). In 2040, **CXL** (Compute Express Link) is emerging as a universal interconnect for memory, accelerators, and peripherals, promising to unify the fragmented landscape of internal buses.

**Required Reading:**
- USB-IF, *USB4 Specification* (v2.0, 2035)
- IEEE 802.11bn-2032, *Standard for Information Technology — Telecommunications and Information Exchange Between Systems — Local and Metropolitan Area Networks — Specific Requirements — Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications — Amendment 14: Enhanced Ultra High Throughput*
- PCI-SIG, *PCI Express Base Specification* (v7.0, 2035)
- CXL Consortium, *Compute Express Link Specification* (v4.0, 2035)
- University of Yggdrasil, "CXL as a Universal Interconnect: Performance and Compatibility Study" (2039)

**Discussion Questions:**
1. USB-C has become the universal connector, but the protocol ecosystem behind USB-C is complex (USB 2.0, USB 3.x, USB4, Thunderbolt, DisplayPort Alt Mode, Power Delivery). Is the universal connector a genuine simplification, or does it create confusion when not all USB-C ports support all features?
2. 6G promises 1 Tbps peak speeds, but current mobile applications do not require such bandwidth. Is 6G driven by genuine demand, or is it a marketing treadmill that forces consumers to upgrade devices unnecessarily?
3. CXL promises to unify memory, accelerator, and peripheral interconnects. Will CXL succeed where previous universal interconnect attempts (PCI, PCI-X, AGP, etc.) have led to fragmentation?

---

## Lecture 7: System Assembly and Configuration

This lecture transitions from theory to practice: the physical assembly of a computer from components, the installation and configuration of an operating system, and the verification that the system operates correctly.

**Component selection** is the first step. The builder must choose: a **CPU** (matching socket type to motherboard); a **motherboard** (with appropriate chipset, expansion slots, and I/O); **memory** (matching type, speed, and capacity to motherboard and CPU specifications); **storage** (NVMe SSD for boot, possibly additional SSDs or HDDs for bulk storage); a **GPU** (if the CPU lacks integrated graphics or if discrete graphics are needed); a **power supply** (with sufficient wattage and efficiency rating); a **case** (with adequate cooling and space for components); and **peripherals** (monitor, keyboard, mouse). In 2040, **PC Part Picker** (and its AI-enhanced successor, *Völundr Build*) automates compatibility checking and suggests optimal component combinations based on budget, performance requirements, and availability.

**Assembly** requires attention to physical and electrical safety. **ESD** (Electrostatic Discharge) can destroy sensitive components; builders use anti-static wrist straps and mats. The **CPU** is installed in the socket (aligning the triangle markers), the **cooler** is mounted with thermal paste, **RAM** is inserted into DIMM slots (often in specific slots for dual-channel operation), the **M.2 SSD** is secured to the motherboard, the **GPU** is inserted into the PCIe slot, and the **power supply** is connected to the motherboard (24-pin main, 8-pin CPU, 6/8-pin GPU). **Cable management** ensures airflow and aesthetics. The University of Yggdrasil's IT103 lab includes a **build competition**: teams of students assemble systems from a parts bin, with scoring based on build time, cable management, POST (Power-On Self-Test) success, and benchmark performance.

**Firmware configuration** (BIOS/UEFI setup) is the next step. The **UEFI** (Unified Extensible Firmware Interface) is the modern replacement for BIOS: it provides a graphical interface, supports large drives (>2 TB), and includes security features like **Secure Boot** (verifying that the OS bootloader is cryptographically signed). Configuration tasks include: enabling **XMP** (Extreme Memory Profile) to run RAM at its rated speed; configuring **boot order** (prioritising the installation medium); enabling **virtualisation support** (Intel VT-x/AMD-V) if the OS will run virtual machines; and configuring **fan curves** for thermal management. In 2040, **AI-assisted UEFI** (e.g., ASUS AI BIOS, MSI Smart Setup) can recommend optimal settings based on the installed components and intended workload.

**OS installation** from USB media is the final step. The installer partitions the drive, copies files, configures drivers, and sets up user accounts. **Driver installation** ensures that all hardware components are recognised and function correctly; modern OSes include most drivers, but discrete GPUs often require manufacturer-specific drivers for optimal performance. **Verification** includes: running **memory tests** (MemTest86) to detect RAM errors; running **storage benchmarks** (CrystalDiskMark, fio) to verify SSD performance; running **stress tests** (Prime95, FurMark, AIDA64) to verify thermal stability under load; and checking **system information** (CPU-Z, HWiNFO) to confirm that components are recognised correctly.

**Required Reading:**
- Scott Mueller, *Upgrading and Repairing PCs* (24th ed., Que, 2015/2035), ch. 3–6, 17–19
- UEFI Forum, *UEFI Specification* (v2.11, 2035)
- Intel, *Intel 64 and IA-32 Architectures Software Developer's Manual* (Vol. 3A, 2035), ch. 2 ("System Architecture Overview")
- University of Yggdrasil, "IT103 Build Competition: Rules, Scoring, and Safety Guidelines" (2039)

**Discussion Questions:**
1. PC building was once a specialised skill; now AI-assisted tools can recommend components and even guide assembly. Is the art of PC building dying, or is it evolving into a higher-level design discipline?
2. UEFI Secure Boot prevents unauthorised bootloaders from running, but it also complicates the installation of alternative operating systems (Linux, BSD). Is Secure Boot a legitimate security measure or a tool for vendor lock-in?
3. The build competition emphasises speed and aesthetics. Are these the most important skills for an IT professional, or should the competition include diagnostic scenarios (e.g., "the system won't POST — find and fix the fault")?

---

## Lecture 8: Diagnostics and Troubleshooting Methodology

When a system fails, the technician's ability to diagnose and repair the fault is the difference between hours of downtime and minutes. This lecture introduces systematic troubleshooting methodologies and the tools used to diagnose hardware and software problems.

**The scientific method of troubleshooting** follows a structured process: **1. Gather information** (what changed? what are the symptoms? when did the problem start?); **2. Form hypotheses** (what could cause these symptoms?); **3. Test hypotheses** (design experiments that confirm or rule out each hypothesis); **4. Implement the fix** (repair or replace the faulty component); **5. Verify the fix** (confirm that the problem is resolved and that no new problems were introduced); **6. Document** (record the problem, the diagnosis, and the fix for future reference). This method is taught explicitly because ad-hoc troubleshooting (randomly replacing parts) is inefficient and often counterproductive.

**Hardware diagnostics** use a combination of built-in and external tools. **POST codes** and **beep codes** indicate hardware failures before the OS loads. **LED indicators** on motherboards show which component failed during POST. **Diagnostic software** (MemTest86 for RAM, CrystalDiskInfo for SSD health, HWiNFO for sensor readings, OCCT for stress testing) identifies failing components. **Multimeters** measure voltage, current, and resistance to verify power supply output and continuity. **Thermal cameras** identify overheating components. **Oscilloscopes** (in advanced diagnostics) analyse signal integrity on buses and interfaces. In 2040, **AI-assisted diagnostics** (e.g., Dell SupportAssist, Lenovo Vantage AI, and the open-source *Mimir Diagnose* developed at Yggdrasil) analyse telemetry data to predict failures before they occur and suggest remediation steps.

**Software diagnostics** address OS and application problems. **Event logs** (Windows Event Viewer, systemd journal, syslog) record system events and errors. **Process monitors** (Task Manager, htop, Process Explorer) show CPU, memory, and I/O usage per process. **Network diagnostics** (ping, traceroute, netstat, Wireshark) identify connectivity and routing problems. **File system checks** (chkdsk, fsck) detect and repair disk corruption. **Safe mode** (booting with minimal drivers and services) isolates software conflicts. **System restore** and **snapshots** (Windows Restore Points, ZFS snapshots, Timeshift) allow rollback to a known-good state. In 2040, **automated remediation** (self-healing systems) can restart failed services, roll back problematic updates, and reconfigure settings without human intervention.

**Common failure modes** and their symptoms: **No power** (dead PSU, faulty power button, motherboard short); **No POST** (failed CPU, RAM, or motherboard; loose connections); **Intermittent crashes** (overheating, failing RAM, unstable overclock, PSU voltage fluctuations); **Slow performance** (failing SSD, thermal throttling, malware, insufficient RAM); **Blue screen / kernel panic** (driver conflicts, hardware faults, memory corruption); **Network issues** (faulty cable, misconfigured settings, DNS problems, firewall blocking); and **Data corruption** (failing storage, RAM errors, power loss during writes). The **Yggdrasil Troubleshooting Lab** maintains a "zoo" of deliberately faulted systems that students must diagnose and repair under time pressure.

**Required Reading:**
- Scott Mueller, *Upgrading and Repairing PCs* (24th ed.), ch. 20–24
- Mark Russinovich, Aaron Margosis & David Solomon, *Troubleshooting with the Windows Sysinternals Tools* (2nd ed., Microsoft Press, 2016/2035), ch. 1–3
- Brendan Gregg, *Systems Performance: Enterprise and the Cloud* (2nd ed., 2019/2035), ch. 2–3
- University of Yggdrasil, "Mimir Diagnose: AI-Assisted Hardware Diagnostics for Educational Environments" (2039)

**Discussion Questions:**
1. AI-assisted diagnostics can predict failures before they occur. Does this reduce the need for human troubleshooting skills, or does it merely shift the technician's role from reactive repair to proactive maintenance?
2. The "zoo" of faulted systems teaches diagnostic skills, but the faults are artificially introduced. Are artificially induced faults representative of real-world failures, or do they teach students to recognise textbook symptoms rather than diagnose novel problems?
3. Automated remediation (self-healing systems) can resolve many issues without human intervention. Is this a liberating development that frees IT professionals for higher-value work, or does it create a generation of technicians who cannot diagnose problems when the automation fails?

---

## Lecture 9: Mobile and Embedded Systems

Not all computers are desktops or servers. Mobile devices (smartphones, tablets, laptops) and embedded systems (IoT devices, industrial controllers, automotive computers) constitute the vast majority of computing devices in 2040. This lecture examines the hardware characteristics, constraints, and design principles of these systems.

**Mobile processors** (Apple A-series, Qualcomm Snapdragon, Samsung Exynos, MediaTek Dimensity) are **system-on-chip (SoC)** designs that integrate the CPU, GPU, NPU (neural processing unit), ISP (image signal processor), modem, and memory controller onto a single die. SoCs are optimised for **power efficiency** rather than raw performance: a smartphone battery must last a full day of use, and thermal constraints limit sustained performance. **ARM big.LITTLE** (and its successor, **DynamIQ**) pairs high-performance cores with power-efficient cores, switching between them based on workload. **Thermal throttling** reduces clock speeds when the device gets too hot, preventing damage but reducing performance. In 2040, **active cooling** (vapour chambers, graphite sheets, and even tiny fans in gaming phones) is increasingly common in high-end mobile devices.

**Embedded systems** are computers designed for a specific purpose, often with severe constraints on cost, power, size, and reliability. **Microcontrollers** (ARM Cortex-M, RISC-V, AVR, PIC) are small processors with integrated memory and peripherals, used in appliances, sensors, and actuators. **Single-board computers** (Raspberry Pi, Hálogi Board, NVIDIA Jetson) provide more computing power for applications like digital signage, robotics, and edge AI. **FPGAs** (Field-Programmable Gate Arrays) allow hardware to be reconfigured for specific tasks, used in telecommunications, automotive, and aerospace. **ASICs** (Application-Specific Integrated Circuits) are custom-designed chips for high-volume applications (e.g., Bitcoin mining, AI inference). In 2040, **tinyML** (machine learning on microcontrollers) enables intelligence in the smallest devices: a $1 microcontroller can run voice recognition, gesture detection, or anomaly detection using neural networks with fewer than 100,000 parameters.

**IoT (Internet of Things)** devices are embedded systems with network connectivity. By 2040, there are an estimated 100 billion IoT devices worldwide: smart home devices (thermostats, lights, locks), industrial sensors (temperature, vibration, pressure), wearable health monitors, agricultural sensors, and connected vehicles. **IoT hardware constraints** include: limited processing power (often <100 MHz), limited memory (KB to MB), limited power (battery or energy harvesting), and limited bandwidth (LoRaWAN, NB-IoT, or intermittent Wi-Fi). **Edge computing** processes data locally on the device or a nearby gateway, reducing latency and bandwidth usage compared to cloud-only processing. The **University of Yggdrasil's Smart Campus** deploys 50,000+ IoT sensors for environmental monitoring, energy management, and predictive maintenance of buildings.

**Required Reading:**
- Joseph Yiu, *The Definitive Guide to ARM Cortex-M3 and Cortex-M4 Processors* (3rd ed., Newnes, 2014/2035), ch. 1–3
- Pete Warden & Daniel Situnayake, *TinyML: Machine Learning with TensorFlow Lite on Arduino and Ultra-Low-Power Microcontrollers* (O'Reilly, 2020/2035), ch. 1–2
- Raspberry Pi Foundation, *Raspberry Pi Documentation* (2040)
- University of Yggdrasil, "The Smart Campus: 50,000 IoT Sensors and the Edge Computing Architecture" (2039)

**Discussion Questions:**
1. Mobile SoCs integrate an ever-increasing number of functions (CPU, GPU, NPU, modem, ISP). Is this integration a genuine architectural advance, or does it create vendor lock-in and reduce flexibility?
2. TinyML enables intelligence on $1 microcontrollers, but the models are necessarily small and limited. For what classes of problems is tinyML sufficient, and for what classes is the constraint on model size prohibitive?
3. The Yggdrasil Smart Campus deploys 50,000 IoT sensors. What are the privacy implications of such dense environmental monitoring, and how should the University balance operational benefits against individual privacy?

---

## Lecture 10: Virtualisation and Containers — Hardware Abstraction Layers

Virtualisation is the technology that allows multiple operating systems to run on a single physical machine, sharing its resources securely and efficiently. Containers are a lighter-weight form of isolation that packages applications with their dependencies. Together, virtualisation and containers are the foundation of modern cloud computing and DevOps practices.

**Hardware virtualisation** uses a **hypervisor** to create and manage virtual machines (VMs). A **Type 1 hypervisor** (bare-metal: VMware ESXi, Microsoft Hyper-V, Xen, KVM) runs directly on the hardware, providing near-native performance. A **Type 2 hypervisor** (hosted: VMware Workstation, VirtualBox, Parallels) runs on top of a host OS, with higher overhead but easier setup. The hypervisor virtualises CPU, memory, storage, and network resources, presenting each VM with the illusion of dedicated hardware. **Hardware-assisted virtualisation** (Intel VT-x, AMD-V) provides CPU features that accelerate virtualisation: extended page tables (EPT) for memory virtualisation, VT-d for device passthrough, and VMCS shadowing for nested virtualisation. In 2040, **nested virtualisation** (running a hypervisor inside a VM) is standard for cloud provider environments, enabling customers to run their own hypervisors on rented VMs.

**Containers** (Docker, containerd, LXC) provide operating-system-level virtualisation: they share the host OS kernel but isolate processes, file systems, and networks using Linux kernel features (**namespaces** for isolation, **cgroups** for resource limiting, and **seccomp** for syscall filtering). Containers are **lighter** than VMs (megabytes rather than gigabytes, seconds to start rather than minutes) and **more efficient** (no guest OS overhead). However, containers provide **weaker isolation** than VMs: a kernel vulnerability can compromise all containers on the host. In 2040, **gVisor** and **Kata Containers** address this by running containers in lightweight VMs, combining the isolation of VMs with the efficiency of containers.

**Container orchestration** (Kubernetes, the de facto standard) automates the deployment, scaling, and management of containerised applications. Kubernetes concepts include: **Pods** (the smallest deployable units, containing one or more containers); **Deployments** (declarative specifications of desired application state); **Services** (stable network endpoints for accessing pods); **Ingress** (HTTP routing and load balancing); **ConfigMaps and Secrets** (configuration and sensitive data management); **Persistent Volumes** (storage for stateful applications); and **Namespaces** (logical isolation of resources). The **Kubernetes ecosystem** (Helm for packaging, Prometheus for monitoring, Grafana for visualisation, Istio for service mesh) has become the standard platform for cloud-native application development.

**The 2040 virtualisation landscape** includes several innovations. **Confidential computing** (Intel TDX, AMD SEV-SNP, ARM CCA) encrypts VM memory so that even the hypervisor cannot read it, protecting data from cloud provider administrators. **GPU virtualisation** (NVIDIA vGPU, AMD MxGPU) allows multiple VMs to share a physical GPU for AI and graphics workloads. **DPUs** (Data Processing Units, e.g., NVIDIA BlueField, Marvell OCTEON) are specialised processors that offload virtualisation, networking, and storage functions from the host CPU, improving performance and security. The University of Yggdrasil's **Muninn Cluster** uses DPUs in every server to offload hypervisor functions, achieving near-bare-metal performance for virtualised workloads.

**Required Reading:**
- Edouard Bugnion et al., "Bringing Virtualisation to the x86 Architecture with the Original VMware Workstation," *ACM TOCS* 30, no. 4 (2012): 1–51
- Brendan Burns, Joe Beda & Kelsey Hightower, *Kubernetes: Up and Running* (3rd ed., O'Reilly, 2035), ch. 1–5
- Liz Rice, *Container Security: Fundamental Technology Concepts That Protect Containerised Applications* (O'Reilly, 2020/2035), ch. 1–3
- NVIDIA, "BlueField DPU Architecture and Performance" (2035 white paper)
- University of Yggdrasil, "DPUs in the Muninn Cluster: Performance and Security Analysis" (2039)

**Discussion Questions:**
1. Containers provide weaker isolation than VMs but are more efficient. For what classes of applications is container isolation sufficient, and for what classes is VM isolation mandatory?
2. Confidential computing encrypts VM memory from the hypervisor, but it adds performance overhead and complicates debugging. Is the security benefit worth the operational cost?
3. Kubernetes has become the standard for container orchestration, but its complexity is notorious. Is Kubernetes a genuinely necessary abstraction, or has the industry standardised on a tool that is more complex than most applications require?

---

## Lecture 11: Hardware Security — Trusted Execution, Side Channels, and Supply Chain Integrity

Hardware security is the discipline of protecting computer systems at the physical and architectural level. It encompasses trusted execution environments, side-channel attack defences, and supply chain integrity. This lecture examines the threats and countermeasures that define hardware security in 2040.

**Trusted Execution Environments (TEEs)** are secure areas within a processor that guarantee confidentiality and integrity of code and data. **Intel SGX** (Software Guard Extensions) creates encrypted **enclaves** that are inaccessible to the OS, hypervisor, or physical attackers with DRAM access. **AMD SEV** (Secure Encrypted Virtualization) encrypts VM memory from the hypervisor. **ARM TrustZone** divides the processor into a secure world and a normal world, with hardware-enforced isolation. In 2040, **Intel TDX** (Trust Domain Extensions) and **ARM CCA** (Confidential Compute Architecture) are the latest TEE technologies, extending protection to entire VMs rather than just individual enclaves. **Limitations of TEEs**: side-channel attacks (discussed below) can extract data from enclaves; speculative execution vulnerabilities (Spectre, Meltdown) can bypass TEE isolation; and TEEs rely on the hardware manufacturer's root of trust, creating a single point of failure.

**Side-channel attacks** exploit information leaked through physical implementation rather than algorithmic weakness. **Timing attacks** measure the time taken by operations to infer secrets (e.g., cache timing attacks that distinguish between cache hits and misses). **Power analysis** measures the power consumption of a device to infer the operations it is performing (differential power analysis, DPA, can extract cryptographic keys from smart cards). **Electromagnetic analysis** measures the electromagnetic emissions of a device. **Acoustic cryptanalysis** analyses the sound produced by a device (e.g., coil whine from capacitors). **Cold boot attacks** extract data from RAM after power loss by freezing the memory chips to slow data decay. In 2040, **side-channel-resistant designs** (constant-time algorithms, power-balancing circuits, electromagnetic shielding) are standard for security-critical hardware.

**Supply chain attacks** compromise hardware or firmware before it reaches the end user. **Hardware trojans** are malicious modifications to integrated circuits (e.g., extra logic that leaks secrets or disables the chip on command). **Firmware implants** modify the BIOS/UEFI or peripheral firmware (e.g., the NSA's **DEITYBOUNCE** implant for Dell servers, revealed in the 2013 Snowden leaks). **Counterfeit components** (fake chips that fail under stress or contain hidden functionality) infiltrate the supply chain. **Mitigations** include: **hardware verification** (formal methods, simulation, and testing to detect trojans); **secure boot** (cryptographic verification of firmware); **supply chain transparency** (blockchain-based tracking of component provenance); and **domestic manufacturing** (reducing reliance on foreign supply chains). In 2040, the **Nordic Semiconductor Security Initiative** mandates hardware verification for all chips used in government and critical infrastructure systems.

**The University of Yggdrasil's Hardware Security Lab** researches: **formal verification of processor designs** (using tools like JasperGold and Cadence Conformal); **side-channel analysis of student-designed processors** (the Hálogi Board is analysed for power leakage as a teaching exercise); **supply chain integrity for the Muninn Cluster** (every component is tracked from manufacturer to installation); and **post-quantum secure hardware** (designing processors that resist attacks by quantum computers).

**Required Reading:**
- Victor Costan & Srinivas Devadas, "Intel SGX Explained," *Cryptology ePrint Archive* 2016/086
- Paul Kocher et al., "Spectre Attacks: Exploiting Speculative Execution," *S&P 2019*
- Matthew Hicks et al., "Overcoming an Untrusted Computing Base: Detecting and Removing Malicious Hardware Automatically," *S&P 2010*
- DARPA, "Supply Chain Hardware Integrity for Electronics Defense (SHIELD)" program final report (2030)
- University of Yggdrasil, "Formal Verification of the Hálogi RISC-V Core: A Student Project" (2039)

**Discussion Questions:**
1. TEEs rely on the hardware manufacturer's root of trust. If the manufacturer is compromised (by state actors, criminals, or insiders), the TEE provides no security. Is this a fundamental limitation of TEEs, or can it be mitigated by decentralised trust models?
2. Side-channel attacks exploit physical implementation details that are not part of the algorithmic specification. Is it possible to design hardware that is provably resistant to all side-channel attacks, or will there always be unanticipated leakage channels?
3. Supply chain attacks are difficult to detect because the compromised components function correctly under normal conditions. Is hardware verification (formal methods, testing) sufficient to detect trojans, or is physical inspection (delayering, microscopy) also necessary?

---

## Lecture 12: The Future of Hardware — Beyond Silicon

The final lecture looks beyond the current paradigm of silicon CMOS to examine the technologies that may define computing in the latter half of the 21st century. Some are incremental improvements; others are radical departures that could transform the nature of computation itself.

**3D integration and chiplets** (discussed in Lecture 1) are the near-term future. By stacking dies vertically and connecting them with through-silicon vias (TSVs), manufacturers can increase transistor density and reduce interconnect delay without further shrinking transistors. **Hybrid bonding** (direct copper-to-copper bonding at room temperature) enables finer pitch and higher density than traditional microbumps. In 2040, **3D-stacked processors** (AMD's 3D V-Cache, Intel's Foveros Direct) are standard in high-performance computing, and the **Universal Chiplet Interconnect Express (UCIe)** standard enables chiplets from different manufacturers to be combined in a single package.

**Photonic computing** uses light instead of electrons for computation and communication. **Silicon photonics** integrates optical components (lasers, modulators, detectors, waveguides) onto silicon chips, enabling high-bandwidth, low-power communication. **Optical computing** (performing computation with light rather than electricity) promises extreme speed for specific operations (matrix-vector multiplication, Fourier transforms) but faces challenges in integration and programmability. In 2040, **photonic interconnects** are standard in data centres and supercomputers, and **photonic AI accelerators** (Lightmatter, Lightelligence) are emerging for inference workloads.

**Neuromorphic computing** (discussed in IT101) uses brain-inspired architectures: spiking neurons, event-driven computation, and in-memory processing. **Intel Loihi 3** (2035) contains 10 million neurons and 1 billion synapses on a single chip, consuming milliwatts for tasks that would require watts on traditional processors. Neuromorphic chips excel at **sensory processing** (vision, audition, olfaction), **adaptive control** (robotics, drones), and **sparse pattern recognition**. In 2040, neuromorphic processors are deployed in **edge devices** (smart sensors, wearables, autonomous vehicles) where power efficiency is paramount.

**Quantum computing** (discussed in CS408) is the most radical departure from classical computation. By 2040, quantum processors with 1,000–10,000 qubits are available through cloud services, but they remain **specialised accelerators** for specific problems (quantum simulation, optimisation, cryptography). General-purpose quantum computing awaits **fault-tolerant architectures** with millions of physical qubits, projected for the 2050s. The University of Yggdrasil's **Quantum Materials Lab** researches **topological qubits** (Majorana zero modes in semiconductor-superconductor nanowires) as a path to inherently error-resistant quantum computing.

**Biological and chemical computing** are the most speculative frontiers. **DNA computing** (Adleman, 1994) uses DNA strands to perform parallel computations, but it is slow and error-prone compared to electronic computers. **Protein computing** (using protein conformational changes as logic gates) and **bacterial computing** (engineering bacteria to perform simple computations) are active research areas with no practical applications in 2040. The **University of Yggdrasil's Bio-Digital Convergence Lab** explores the interface between biological and electronic systems, with a focus on **neural interfaces** that could enable direct brain-computer communication.

**Required Reading:**
- IEEE, *International Roadmap for Devices and Systems (IRDS)* (2035 edition)
- Intel, "Foveros Direct and 3D Packaging: The Future of Moore's Law" (2035 white paper)
- Lightmatter, "Photonic AI Accelerators: Performance and Efficiency" (2035 white paper)
- Intel Labs, "Loihi 3: A Neuromorphic Research Processor" (2035 technical report)
- University of Yggdrasil, "The Bio-Digital Convergence: Neural Interfaces and Hybrid Biological-Electronic Systems" (2039)

**Discussion Questions:**
1. 3D integration and chiplets extend the life of silicon but do not fundamentally change the computing paradigm. Are these incremental improvements sufficient for the next 20 years, or is a radical new paradigm (photonics, neuromorphics, quantum) necessary?
2. Photonic computing promises speed and efficiency but is difficult to program and integrate with electronic systems. Will photonics remain a niche technology for specific workloads, or will it eventually replace electronics for general-purpose computation?
3. Biological computing is speculative but potentially transformative. If brain-computer interfaces become practical, what are the ethical implications of merging biological and digital cognition?

---

## Final Examination Preparation

The final examination for IT103 is a **practical skills assessment** (60% of grade) combined with a **written theory exam** (40% of grade). The practical assessment is conducted in the Yggdrasil IT Lab over a 4-hour session; the written exam is 2 hours.

**Practical Skills Assessment (60%):**
Students are given a partially assembled or malfunctioning computer and a set of tasks:
- Component identification and compatibility checking (10%)
- System assembly or repair (20%)
- OS installation and driver configuration (15%)
- Diagnostic troubleshooting of a hardware or software fault (15%)

**Written Theory Exam (40%):**
Choose 4 of 8 essay questions:

1. Explain the physics of CMOS transistors and the challenges of scaling below 5nm. Discuss the engineering solutions (3D integration, chiplets, new materials) and their limitations.

2. Compare x86, ARM, and RISC-V architectures across the dimensions of performance, power efficiency, ecosystem, and licensing model. For what classes of devices is each architecture best suited?

3. Analyse the memory hierarchy from registers to DNA storage. For each level, explain the trade-off between speed, capacity, cost, and persistence. Why does no single memory technology dominate all levels?

4. Describe the power and cooling infrastructure of a modern data centre. Calculate the PUE of a hypothetical facility and propose improvements. Discuss the environmental implications of data centre energy consumption.

5. A system fails to POST. Describe a systematic diagnostic process, including the tools and tests you would use at each step. What are the most likely failure modes, and how would you confirm each hypothesis?

6. Compare virtual machines and containers as hardware abstraction mechanisms. For what workloads is each appropriate? What are the security implications of each approach?

7. Describe a side-channel attack and a hardware trojan. For each, explain how it works, what defences exist, and why defending against it is difficult.

8. Choose one emerging hardware technology (photonics, neuromorphics, quantum, biological). Explain its principles, current state of development, and potential impact on computing. What are the most significant barriers to practical deployment?

**Grading:**
- A (Excellent): Flawless practical execution, comprehensive theoretical understanding, and insightful analysis of trade-offs and future directions.
- B (Good): Competent practical skills with minor errors; solid theoretical foundation; some gaps in analysis.
- C (Satisfactory): Basic practical competence; adequate theoretical knowledge; superficial analysis.
- D (Poor): Significant practical errors; fragmentary theoretical understanding; little analysis.
- F (Fail): Unable to complete basic tasks; fundamental misunderstandings of hardware principles.
