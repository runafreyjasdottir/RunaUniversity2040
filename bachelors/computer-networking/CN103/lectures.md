# CN103: Data Communications & Signal Processing
## Bachelor of Science in Computer Networking — University of Yggdrasil, 2040

**Credits:** 4
**Description:** Comprehensive study of how information is encoded, transmitted, and decoded across physical media. Covers analog and digital signal theory, modulation techniques (AM, FM, PM, QAM, OFDM), line coding, transmission media (copper, fiber, wireless), signal impairment and Shannon's theorem, multiplexing strategies, error detection and correction, source and channel coding, and the 2040 frontier: terahertz communications, orbital laser links, and quantum signal processing. Students design, simulate, and measure real signals in the Valhalla Network Lab.

**Instructor:** Dr. Sigrid Völundsdottir, Associate Professor of Signal Engineering & Lead Researcher, Bifrǫst PHY Lab
**Lab:** Valhalla Network Lab, Sublevel 2, Hákon Computing Centre — equipped with oscilloscopes, spectrum analyzers, SDR platforms, and the Bifrǫst Optical Testbed
**Office Hours:** Mondays 10:00-12:00, or by appointment via the UoY Mesh

---

## Lectures

ᚠ **Lecture 1: The Physics of Information — Signals, Symbols, and the Communication Channel**

**Course:** CN103 — Data Communications & Signal Processing
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

This opening lecture establishes the fundamental question that drives the entire course: how do we take abstract information — a bit, a byte, a packet — and make it travel through physical reality? By 2040, the answer spans copper traces on circuit boards, fiber-optic cables crossing ocean floors, laser beams connecting satellites, and quantum states encoding cryptographic keys. Yet beneath all this diversity lies a unified mathematical framework: the communication channel model. We introduce the Shannon-Weaver model of communication, the distinction between data and signals, the time-domain and frequency-domain representations that will be our analytical toolkit, and the layered abstraction that lets us design communication systems without drowning in complexity.

### Key Topics

- **The Communication Channel Model:** Source → Encoder → Channel → Decoder → Destination. Why this abstraction survives from Shannon's 1948 paper to 2040 quantum networks. Information as entropy, channel as capacity, noise as the fundamental adversary.
- **Data vs. Signals:** Data is abstract — bits, bytes, packets. A signal is physical — voltage on a wire, light in a fiber, radio waves in the air. The mapping between them is the art of data communications.
- **Time Domain and Frequency Domain:** Every signal has two faces. In the time domain, we see voltage varying over microseconds. In the frequency domain (via Fourier transform), we see power distributed across frequency components. A pure sine wave is a single spike in frequency; a square wave contains all odd harmonics. Understanding this duality is essential for everything that follows: bandwidth, filtering, modulation, and noise analysis.
- **The 2040 Communication Landscape:** Terahertz indoor links (100+ Gbps), orbital laser mesh (Starlink v3, Bifrǫst LEO ring), hollow-core fiber (99.7% speed of light in vacuum), quantum key distribution over satellite, and the persistent role of copper Ethernet (Cat 9, 40 Gbps over 100m). The physics changes; Shannon's limits do not.
- **The Layered Approach:** Physical layer → Data Link → Network → Transport → Application. This course focuses on the physical layer and its handshake with the data link layer. The physical layer doesn't understand packets; it only knows how to move symbols.

### Lecture Notes

Shannon's 1948 paper, "A Mathematical Theory of Communication," is arguably the most important applied mathematics paper of the 20th century. Shannon asked a deceptively simple question: given a noisy channel, what is the maximum rate at which information can be transmitted with arbitrarily low error? His answer — the channel capacity C = B log₂(1 + SNR) — remains the fundamental speed limit of all communication systems. No amount of cleverness can exceed it; the best we can do is approach it asymptotically.

The Shannon-Weaver model decomposes communication into five stages. The *information source* produces messages — a video stream, a sensor reading, a voice call. The *transmitter* encodes these messages into signals suitable for the channel — converting digital bits into voltage levels, modulating a carrier wave, or encoding photons. The *channel* is the physical medium — copper wire, optical fiber, free space — with its characteristic bandwidth, attenuation, and noise profile. The *receiver* decodes the signal back into messages, correcting errors where possible. The *destination* consumes the message. Shannon's genius was to treat the source and channel as statistical entities, quantifying information in bits and noise in probabilities.

The signal is the physical manifestation of data. Consider a simple binary transmission: we assign +5V to represent a 1-bit and 0V to represent a 0-bit. The receiver samples the voltage at regular intervals and decides which symbol was sent. But real wires have resistance, capacitance, and inductance; signals degrade, reflect, and pick up noise. A receiver seeing 3.2V must decide: was that a degraded 5V (bit 1) or noise on 0V (bit 0)? This decision problem — detection theory — is the foundation of receiver design.

The time-domain/frequency-domain duality is one of the most powerful analytical tools in communications. A signal s(t) — voltage as a function of time — can be decomposed into its frequency components via the Fourier transform: S(f) = ∫ s(t) e^(-j2πft) dt. This reveals which frequencies carry energy. A digital signal with sharp transitions (fast rise times) requires high-frequency components; a pure sine wave occupies a single frequency. Bandwidth — the range of frequencies a channel can pass — determines the maximum symbol rate. A channel that passes 0-4 kHz (like traditional telephony) cannot carry signals with higher frequency content; those components are filtered out, distorting the waveform.

In 2040, we operate in a radically expanded spectrum. The Bifrǫst PHY Lab maintains testbeds from 3 kHz (VLF submarine communications) through 300 GHz (terahertz indoor links) to 193 THz (1550 nm fiber optics) and beyond to 500 THz (visible light communication — LiFi). Each band has different propagation characteristics, regulatory constraints, and engineering challenges. The course will survey them all, but our primary focus is the 0-300 GHz range where most networking operates.

### Required Reading

- Shannon, C.E. (1948). "A Mathematical Theory of Communication." *Bell System Technical Journal*, 27(3), 379-423. Read the Introduction and Part I (pp. 379-387).
- Stallings, W. (2039). *Data and Computer Communications*, 12th Edition. Pearson. Chapter 2: "Transmission Fundamentals."
- Völundsdottir, S. & Chen, L. (2038). "The Bifrǫst PHY Architecture: A Unified Physical Layer for Terrestrial, Aerial, and Orbital Networks." *IEEE Communications Magazine*, 76(4), 22-35.
- UoY Network Engineering Handbook (2040), Section 1: "Physical Layer Primer."

### Discussion Questions

1. Shannon derived his channel capacity theorem in 1948, before transistors were common. Why has no communication system ever exceeded Shannon's limit, despite 80+ years of technological revolution? Is the Shannon limit a law of physics or a statement about information?
2. The time-domain representation of a signal is intuitive (voltage over time), but the frequency-domain representation often reveals more about signal behavior. Why does Fourier analysis work? What assumptions does it make about signals?
3. In 2040, we can transmit 400 Gbps over a single wavelength in hollow-core fiber. Yet many IoT sensors still use 9.6 kbps LoRa links. What factors determine the appropriate data rate for a given application? Is faster always better?

---

ᚢ **Lecture 2: Analog and Digital Signals — Continuous Waves Meet Discrete Symbols**

**Course:** CN103 — Data Communications & Signal Processing
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

The universe is analog. Sound waves, light waves, radio waves — all are continuous phenomena governed by differential equations. But computers are digital — they operate on discrete symbols, bits, and clock edges. The bridge between these two worlds is the central challenge of data communications. This lecture examines the mathematical description of analog signals (amplitude, frequency, phase, wavelength), the characteristics of digital signals (bit rate, baud rate, rise time, jitter), the Nyquist sampling theorem as the fundamental bridge, and the practical tradeoffs: why we use digital signaling even when the channel is inherently analog.

### Key Topics

- **Analog Signal Parameters:** Amplitude (signal strength, measured in volts or dBm), frequency (cycles per second, Hz), phase (offset within a cycle, degrees or radians), wavelength (λ = v/f, where v is propagation velocity in the medium). A signal s(t) = A sin(2πft + φ) is completely described by three numbers.
- **Decibels and Signal Strength:** The decibel (dB) is a logarithmic ratio: dB = 10 log₁₀(P₂/P₁) for power, 20 log₁₀(V₂/V₁) for voltage. A 3 dB increase doubles power; a 10 dB increase is ten times. dBm references 1 milliwatt (0 dBm = 1 mW). A WiFi signal at -70 dBm is 10^(-7) milliwatts — one ten-millionth of a milliwatt. The logarithmic scale compresses the vast dynamic range of communication signals.
- **Digital Signal Characteristics:** Bit rate (bits per second), baud rate (symbols per second), the relationship between them (bits per symbol depends on the modulation scheme), rise time (time to transition between levels), and jitter (timing variation). A 10 Gbps Ethernet signal has a bit period of 100 picoseconds — light travels only 3 cm in that time.
- **Nyquist Sampling Theorem:** To perfectly reconstruct a bandlimited signal, you must sample at least twice the highest frequency: f_sample ≥ 2f_max. This is why CD audio samples at 44.1 kHz (human hearing extends to ~20 kHz) and why a 1 GHz oscilloscope can capture signals up to 500 MHz.
- **Why Digital?** Analog signals degrade cumulatively — every amplifier adds noise. Digital signals can be regenerated — a repeater decides 0 or 1 and transmits a clean new signal. This regeneration capability is why digital communications conquered the world, from GSM (2G) to 6G.

### Lecture Notes

An analog signal s(t) = A sin(2πft + φ) contains three parameters, each of which can carry information. Amplitude modulation (AM radio) encodes information in A. Frequency modulation (FM radio) encodes information in f. Phase modulation encodes information in φ. In modern digital communications, we modulate all three simultaneously — Quadrature Amplitude Modulation (QAM) varies both amplitude and phase to encode multiple bits per symbol. 256-QAM encodes 8 bits per symbol by using 256 distinct amplitude-phase combinations. But as the constellation density increases, the symbols become harder to distinguish in the presence of noise — Shannon's limit reasserts itself.

The decibel scale is ubiquitous in communications engineering, and students must develop intuition for it. A typical conversation is ~60 dB SPL (sound pressure level). A jet engine at 30 meters is ~140 dB SPL — 80 dB higher, which means 10⁸ times the sound power. In RF, a typical WiFi access point transmits at +20 dBm (100 mW). A satellite receiving station might detect signals at -150 dBm — a factor of 10¹⁷ weaker. The receiver's sensitivity, measured in dBm, determines the maximum range of a link.

The relationship between bit rate and baud rate depends on the modulation scheme. In simple binary signaling (0V for 0, 5V for 1), each symbol carries one bit, so bit rate equals baud rate. In 256-QAM, each symbol carries 8 bits, so bit rate = 8 × baud rate. A 100 MHz baud rate with 256-QAM yields 800 Mbps. But higher-order modulation requires higher signal-to-noise ratio (SNR). Shannon's theorem formalizes this tradeoff: C = B log₂(1 + SNR). For a given bandwidth B, increasing the bit rate requires exponentially more SNR. This is why 5G and 6G use massive MIMO (multiple antennas) to improve effective SNR — the only way to increase capacity without more spectrum.

Nyquist's theorem has profound consequences. A channel with 4 kHz bandwidth (traditional telephone) can carry at most 8,000 symbols per second without intersymbol interference. If each symbol carries 8 bits (256-QAM), that's 64 kbps — the theoretical maximum for a phone line, and exactly what early modems approached (V.90 achieved 56 kbps downstream). A 100 MHz Ethernet channel (Cat 5e) can carry 200 million symbols per second — at 1 bit per symbol (simple line coding), that's 200 Mbps, close to the 100 Mbps Fast Ethernet standard. Gigabit Ethernet uses more sophisticated encoding (PAM-5 with 2 bits per symbol) to reach 1 Gbps within 100 MHz bandwidth.

Digital regeneration is the killer advantage of digital over analog. An analog amplifier takes a weak, noisy signal and amplifies both signal and noise equally — the signal-to-noise ratio stays the same or worsens. A digital repeater makes a hard decision (0 or 1) and transmits a pristine new signal with the original SNR. After 100 repeaters, an analog signal is buried in noise, but a digital signal is identical to the original (assuming no bit errors). This is why undersea fiber cables carry digital signals: the optical amplifiers (EDFAs) every 80 km do add noise, but the digital regeneration at terminal stations resets the signal quality.

### Required Reading

- Stallings, W. (2039). *Data and Computer Communications*, 12th Edition. Pearson. Chapter 2, Sections 2.2-2.4.
- Nyquist, H. (1928). "Certain Topics in Telegraph Transmission Theory." *Transactions of the AIEE*, 47(2), 617-644.
- Oppenheim, A.V. & Willsky, A.S. (2037). *Signals and Systems*, 4th Edition. Pearson. Chapter 7: "Sampling."
- UoY Lab Manual CN103-2: "Signal Measurement and Characterization." (Available on the Mesh Academic Portal)

### Discussion Questions

1. If the universe is fundamentally analog, and quantum mechanics suggests discrete states at the smallest scales, is the analog/digital distinction a property of nature or a property of our measurement frameworks? How does this debate play out in quantum communication?
2. The decibel scale compresses a trillion-to-one power range into 120 dB. What are the cognitive and engineering advantages of logarithmic scales? Could we design a communication system entirely without them?
3. Nyquist's theorem says we must sample at 2× the maximum frequency. What happens if we violate this? Can undersampling ever be useful? (Hint: consider bandpass sampling in software-defined radio.)

---

ᚦ **Lecture 3: Transmission Media — Copper, Glass, and Free Space**

**Course:** CN103 — Data Communications & Signal Processing
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Signals need something to travel through. The physical medium — copper wire, glass fiber, or free space — determines everything about the signal: how fast it propagates, how much it attenuates, what frequencies it can carry, and what impairments it suffers. This lecture surveys the three families of transmission media, their physics, their engineering tradeoffs, and their roles in the 2040 network. We examine twisted-pair copper (from Cat 5e to Cat 9), coaxial cable, single-mode and multi-mode optical fiber, hollow-core fiber, free-space optics, and the radio spectrum from VLF to sub-terahertz.

### Key Topics

- **Copper Media:** Twisted-pair cable reduces electromagnetic interference by ensuring equal exposure of both conductors. Category ratings (Cat 5e through Cat 9) specify bandwidth, crosstalk limits, and maximum length. Cat 9 (2040 standard) supports 40 Gbps over 100m using 2 GHz bandwidth per pair. Coaxial cable provides superior shielding — still used for cable internet (DOCSIS 4.0) and high-frequency lab connections.
- **Optical Fiber:** Total internal reflection traps light in a high-index core surrounded by lower-index cladding. Single-mode fiber (9 µm core) carries one spatial mode — no modal dispersion, ideal for long-haul. Multi-mode fiber (50 µm core) carries multiple modes — cheaper transceivers but limited by modal dispersion to ~500m at 100 Gbps. The 2040 revolution: hollow-core photonic bandgap fiber guides light in an air core, achieving 99.7% of c (vs. ~67% for standard fiber) and 50% lower latency.
- **Free Space:** Radio waves propagate through air or vacuum. Lower frequencies diffract around obstacles and reflect off the ionosphere (VLF, HF). Higher frequencies require line-of-sight (microwave, millimeter wave). Terahertz (100 GHz-10 THz) promises enormous bandwidth but attenuates severely in atmosphere — limited to indoor or short-range outdoor links. Optical free-space links (laser communication) achieve terabit rates between satellites and ground stations.
- **Propagation Delay and Velocity Factor:** Signals travel at v = c / n, where n is the refractive index of the medium. In copper, v ≈ 0.6-0.8c. In standard fiber, n ≈ 1.47 → v ≈ 0.68c. In hollow-core fiber, n ≈ 1.003 → v ≈ 0.997c. A 5,000 km fiber link across the Atlantic has a minimum one-way delay of 5,000/(0.68 × 300,000) ≈ 24.5 ms with standard fiber, vs. ~16.7 ms with hollow-core — a difference that matters for high-frequency trading and haptic telepresence.
- **Media Selection in 2040:** The Bifrǫst Mesh uses all three media: hollow-core fiber for inter-city backbone, Cat 9 copper for last-meter (cheap, power-efficient), free-space laser for orbital and cross-fjord links, and terahertz for indoor wireless backhaul.

### Lecture Notes

Copper twisted-pair is the oldest data communication medium still in active deployment. Alexander Graham Bell patented twisted-pair in 1881 to reduce crosstalk on telephone lines. The principle is elegant: twisting ensures that both conductors experience the same electromagnetic interference, which appears as common-mode voltage and can be rejected by a differential receiver. Category ratings represent a continuous improvement in manufacturing precision: tighter twists, better dielectric materials, and individual pair shielding. Cat 9 (IEEE 802.3, 2040) uses all four pairs bidirectionally with PAM-16 modulation and echo cancellation to achieve 40 Gbps — enough for most access networks and in-building distribution.

Optical fiber is the backbone of the global internet. The key innovation is the erbium-doped fiber amplifier (EDFA), developed in 1987, which amplifies optical signals directly without converting to electrical. A single fiber can carry 80+ wavelengths (dense wavelength division multiplexing, DWDM), each modulated at 400-800 Gbps, for a total capacity exceeding 60 Tbps per fiber pair. The Shannon limit for standard single-mode fiber is approximately 100 Tbps, constrained by the nonlinear Kerr effect — as power increases, the fiber's refractive index changes, distorting the signal. Hollow-core fiber sidesteps this by carrying light in air, dramatically reducing nonlinearity and latency.

The radio spectrum is a finite and fiercely regulated resource. The International Telecommunication Union (ITU) allocates frequency bands globally, and national regulators (FCC, Ofcom, PTS in Sweden) manage licensing. The "beachfront property" — frequencies below 6 GHz — offers good propagation and is saturated with cellular, WiFi, Bluetooth, and satellite services. The "frontier" — millimeter wave (24-100 GHz) and sub-terahertz (100-300 GHz) — offers vast bandwidth (10+ GHz channels) but requires beamforming (electronically steered antenna arrays) and dense deployment due to short range and atmospheric absorption. The Bifrǫst 2040 architecture uses adaptive band selection: a device might use 2.4 GHz WiFi for range, 60 GHz for high-throughput local links, and 300 GHz for wireless backhaul between buildings.

A crucial practical consideration is the link budget: Transmit Power + Antenna Gains − Path Loss − Atmospheric Loss − Receiver Sensitivity must be positive for a working link. Path loss grows with distance squared in free space: L = (4πd/λ)². At 60 GHz, λ ≈ 5 mm, so path loss over 100m is enormous (~108 dB). This is compensated by high-gain antennas and beamforming — a 64-element phased array can provide 18 dBi of gain, making 100m links practical. The link budget equation is the network designer's daily bread.

### Required Reading

- Keiser, G. (2038). *Optical Fiber Communications*, 6th Edition. McGraw-Hill. Chapters 2-3.
- Poletti, F. et al. (2039). "Hollow-Core Fiber: The Next Revolution in Optical Communications." *Nature Photonics*, 33(7), 411-425.
- Rappaport, T.S. et al. (2036). *Wireless Communications: Principles and Practice*, 3rd Edition. Prentice Hall. Chapter 4: "Mobile Radio Propagation."
- UoY Case Study: "Bifrǫst Fiber Backbone Deployment — Oslo to Tromsø." (Mesh Academic Portal)

### Discussion Questions

1. Hollow-core fiber promises near-vacuum propagation speed and lower nonlinearity. Why hasn't it replaced all standard fiber? What manufacturing and deployment challenges remain?
2. The radio spectrum is allocated by governments. In 2040, should spectrum be treated as private property (tradable licenses), public commons (unlicensed like WiFi), or something else? How does this affect innovation?
3. You're designing a network for a mining operation 2 km underground. Copper? Fiber? Wireless? What are the constraints, and which medium (or combination) would you choose?

---

ᚬ **Lecture 4: Signal Impairment — Attenuation, Distortion, Noise, and Shannon's Response**

**Course:** CN103 — Data Communications & Signal Processing
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

No signal arrives intact. Every communication channel degrades the signal through three fundamental mechanisms: attenuation (signal gets weaker with distance), distortion (different frequencies travel at different speeds, smearing the waveform), and noise (unwanted energy from thermal agitation, interference, and cosmic sources). This lecture quantitatively characterizes each impairment, derives the signal-to-noise ratio, presents Shannon's capacity theorem as the fundamental response, and explores how real systems approach the Shannon limit through coding and modulation. We'll compute link budgets and capacity limits for real 2040 scenarios: the Bifrǫst trans-Atlantic cable, a Starlink ground station, and an indoor terahertz link.

### Key Topics

- **Attenuation:** Signal power decreases exponentially with distance: P(d) = P(0) × 10^(-αd/10), where α is attenuation in dB/km. Standard single-mode fiber: α ≈ 0.2 dB/km at 1550 nm — after 100 km, 99% of the power is lost, requiring amplification. Cat 8 copper: α ≈ 50 dB/100m at 2 GHz. Free space: attenuation follows the inverse-square law plus atmospheric absorption (O₂ at 60 GHz, H₂O at 22 GHz and 183 GHz).
- **Distortion:** A channel's frequency response is not flat — different frequencies experience different attenuation and phase shift. This causes intersymbol interference (ISI): a symbol's energy spreads into adjacent time slots, confusing the receiver. Equalization — applying an inverse filter — is the standard remedy. In 2040, adaptive equalizers using neural networks can track rapidly changing channel conditions in real time.
- **Noise Sources:** Thermal noise (Johnson-Nyquist noise) is universal — any conductor at temperature T > 0 generates random voltage fluctuations: N = kTB, where k is Boltzmann's constant, T is temperature in Kelvin, and B is bandwidth. At room temperature with 1 GHz bandwidth, thermal noise power is -84 dBm. Intermodulation noise arises when nonlinear components create sum and difference frequencies. Impulse noise comes from lightning, switching transients, and in 2040, from directed-energy interference.
- **Signal-to-Noise Ratio (SNR):** SNR_dB = 10 log₁₀(P_signal / P_noise). A digital system typically needs SNR > 10 dB for reliable detection; 256-QAM requires SNR > 30 dB. SNR determines the maximum constellation density — and thus the bit rate — for a given error probability.
- **Shannon-Hartley Theorem:** C = B log₂(1 + SNR) bits per second. For a 1 GHz channel with 30 dB SNR, C = 10⁹ × log₂(1001) ≈ 10 Gbps. This is the theoretical maximum — practical systems achieve 50-80% of Shannon capacity. Closing the gap between practical throughput and the Shannon limit has driven 80 years of coding research, from Hamming codes (1950) to LDPC (1960, rediscovered 1996) to polar codes (2008, used in 5G).

### Lecture Notes

Attenuation is the most visible impairment. Every medium has a characteristic attenuation that limits reach. In fiber optics, the 1550 nm window (C-band) is the "sweet spot" — minimum attenuation of ~0.2 dB/km and the wavelength where EDFAs operate. The earlier 1310 nm window has zero dispersion but higher attenuation (~0.4 dB/km). Modern systems use both: 1550 nm for long haul, 1310 nm for metro. The L-band (1565-1625 nm) extends the C-band, and S-band (1460-1530 nm) is newly exploited with semiconductor optical amplifiers (SOAs) — together, C+L+S bands provide ~15 THz of bandwidth per fiber.

Distortion is subtler. A pulse transmitted through a dispersive channel broadens in time. If the broadening exceeds the symbol period, adjacent symbols overlap — this is intersymbol interference (ISI). In fiber, chromatic dispersion causes different wavelengths to travel at different speeds, and polarization mode dispersion (PMD) causes different polarizations to travel differently. Dispersion-compensating fiber (DCF) was the historical solution; digital signal processing (DSP) in coherent receivers is the 2040 solution. The receiver samples at 2-4× the symbol rate, applies an adaptive finite impulse response (FIR) filter, and recovers the original symbols.

Noise is the ultimate adversary. Thermal noise sets the noise floor: at 290 K (room temperature), the noise power spectral density N₀ = kT = 4 × 10⁻²¹ W/Hz = -174 dBm/Hz. Over a 1 GHz bandwidth, the total thermal noise is -84 dBm. To achieve a 20 dB SNR, the received signal must be at least -64 dBm. If the transmitter outputs +20 dBm, the total path loss (attenuation + free-space loss + connector losses) must not exceed 84 dB. This simple budget dictates link feasibility.

Shannon's theorem is both inspiring and humbling. It says that error-free communication is possible at any rate below capacity, using sufficiently long and clever codes. But it doesn't tell us how to construct those codes. The quest to approach Shannon capacity has been one of the great engineering challenges. Turbo codes (1993) shocked the community by achieving performance within 0.7 dB of the Shannon limit. LDPC codes, invented by Gallager in 1960 but impractical until the 1990s, come within 0.0045 dB. Polar codes, the first codes provably achieving symmetric channel capacity, are used in 5G control channels. In 2040, neural network-based decoders are approaching the Shannon limit for channels with unknown or time-varying statistics.

### Required Reading

- Shannon, C.E. (1948). "A Mathematical Theory of Communication." Part IV: "The Continuous Channel."
- Sklar, B. (2037). *Digital Communications: Fundamentals and Applications*, 4th Edition. Prentice Hall. Chapter 3: "Channel Capacity and Coding."
- Arikan, E. (2009). "Channel Polarization: A Method for Constructing Capacity-Achieving Codes." *IEEE Transactions on Information Theory*, 55(7), 3051-3073.
- Völundsdottir, S. (2039). "Neural Equalization for Coherent Optical Receivers: Exceeding the Nonlinear Shannon Limit?" *Journal of Lightwave Technology*, 57(11), 882-895.

### Discussion Questions

1. Shannon's theorem proves that error-free communication is possible below capacity. But it assumes infinite coding delay and complexity. In practice, we trade off throughput, latency, and reliability. How should these tradeoffs be made for (a) a video stream, (b) a surgical robot teleoperation link, (c) a deep-space probe?
2. Thermal noise is fundamental — it comes from the Boltzmann constant, not from engineering flaws. Could we reduce the noise floor by cooling receivers? (Yes — radio telescopes use liquid helium cooling.) Is this practical for data centers?
3. Neural equalizers are outperforming classical DSP in coherent optical receivers. But they're harder to analyze and verify. Should we deploy systems whose behavior we don't fully understand?

---

ᚱ **Lecture 5: Modulation — Encoding Information onto Carrier Waves**

**Course:** CN103 — Data Communications & Signal Processing
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Information must be impressed onto a carrier wave to traverse a channel. Modulation is the art and science of varying a carrier's amplitude, frequency, or phase to encode data. This lecture covers the complete modulation family tree: analog modulation (AM, FM, PM), digital passband modulation (ASK, FSK, PSK, QAM), advanced schemes (OFDM, spread spectrum), and the 2040 frontier (probabilistic constellation shaping, neural modulation). We'll analyze spectral efficiency, error performance in AWGN channels, and how different schemes map to different physical media.

### Key Topics

- **Amplitude Shift Keying (ASK):** The simplest digital modulation — carrier on = 1, carrier off = 0 (OOK). Used in early optical communications and still in some low-cost applications. Poor noise immunity and spectral efficiency.
- **Frequency Shift Keying (FSK):** Binary FSK uses two frequencies for 0 and 1. More robust than ASK but wider bandwidth. Used in Bluetooth (GFSK), LoRa (CSS — chirp spread spectrum, a variant), and legacy paging systems.
- **Phase Shift Keying (PSK):** BPSK uses two phases (0° and 180°), 1 bit per symbol. QPSK uses four phases (0°, 90°, 180°, 270°), 2 bits per symbol. 8-PSK extends to 3 bits. PSK has constant envelope (amplitude doesn't change), making it power-efficient — ideal for satellite and deep-space communications.
- **Quadrature Amplitude Modulation (QAM):** Varies both amplitude and phase. 16-QAM (4 bits/symbol), 64-QAM (6 bits), 256-QAM (8 bits), 1024-QAM (10 bits). Higher order QAM packs more bits per symbol but requires higher SNR. Cable modems (DOCSIS 4.0) use up to 4096-QAM. The constellation diagram — a scatter plot of I (in-phase) vs. Q (quadrature) components — is the visual language of QAM.
- **Orthogonal Frequency Division Multiplexing (OFDM):** Divides a high-rate data stream into many parallel low-rate streams, each on a separate subcarrier. The subcarriers are orthogonal (spaced exactly 1/symbol_period apart) so they don't interfere. OFDM is the basis of WiFi (802.11a/g/n/ac/ax/be), 4G LTE, 5G NR, and digital broadcasting (DVB-T). Its killer feature: robustness against frequency-selective fading, because each subcarrier experiences flat fading and can be equalized independently.
- **Spread Spectrum:** Deliberately spreads the signal over a wider bandwidth than needed. Direct Sequence Spread Spectrum (DSSS) multiplies the data by a high-rate pseudorandom chip sequence. Frequency Hopping Spread Spectrum (FHSS) rapidly switches carrier frequency. Benefits: resistance to narrowband interference, low probability of intercept/detection, and code-division multiple access (CDMA) — multiple users share the same spectrum. Used in GPS, 3G (WCDMA), and military communications.
- **2040 Frontier — Probabilistic Constellation Shaping (PCS):** Traditional QAM uses uniformly spaced constellation points. PCS uses non-uniform spacing — inner points (lower energy) are used more frequently than outer points (higher energy). This optimizes the signal for the actual SNR distribution, closing the gap to Shannon capacity by ~1 dB. PCS is deployed in 800 Gbps coherent optical transceivers (2028+).

### Lecture Notes

The I/Q (in-phase/quadrature) representation unifies all passband modulation schemes. Any passband signal can be expressed as s(t) = I(t) cos(2πf_c t) − Q(t) sin(2πf_c t), where I(t) and Q(t) are baseband signals (slowly varying compared to the carrier f_c). The I and Q components are orthogonal — a receiver can recover them independently by mixing with cos(2πf_c t) and sin(2πf_c t) respectively, then lowpass filtering. This quadrature demodulation is the workhorse of modern radio.

The constellation diagram plots I on the horizontal axis and Q on the vertical axis. Each modulation scheme produces a characteristic pattern. BPSK: two points at (±1, 0). QPSK: four points at (±1, ±1). 16-QAM: a 4×4 grid of 16 points. The minimum distance between constellation points determines error probability in Gaussian noise. For equal average power, denser constellations have smaller minimum distance — more bits per symbol, but more errors at a given SNR. The Shannon capacity curve precisely captures this tradeoff.

OFDM's elegance lies in the cyclic prefix. Multipath propagation creates delayed copies of the signal that arrive at the receiver, causing ISI. OFDM inserts a guard interval (cyclic prefix) before each symbol — a copy of the end of the symbol. If the cyclic prefix is longer than the maximum multipath delay, the receiver sees each symbol as if it were convolved with a circular channel, which becomes simple multiplication in the frequency domain. One-tap equalization per subcarrier replaces the complex time-domain equalizer. The cost: the cyclic prefix is overhead (typically 1/4 to 1/16 of the symbol duration).

The 2040 modulation landscape is shaped by two forces: the need for spectral efficiency (more bits/Hz) and the need for energy efficiency (more bits/Joule). In fiber, coherent QAM with PCS delivers 800 Gbps per wavelength at >8 bits/s/Hz. In 5G millimeter-wave, OFDM with 256-QAM delivers multi-Gbps to mobile users. In IoT, LoRa's chirp spread spectrum trades data rate for range, achieving 10+ km at <1 kbps. In quantum communications, discrete-variable protocols use single-photon modulation (polarization or phase states) that map onto the same I/Q formalism. The physics may change, but the mathematics of I and Q remains constant.

### Required Reading

- Proakis, J.G. & Salehi, M. (2038). *Digital Communications*, 6th Edition. McGraw-Hill. Chapters 4-5.
- Cho, K. & Yoon, D. (2035). "On the General BER Expression of One- and Two-Dimensional Amplitude Modulations." *IEEE Transactions on Communications*, 50(7), 1074-1080.
- Böcherer, G. et al. (2019). "Probabilistic Constellation Shaping: A Practical Guide." *IEEE Communications Magazine*, 57(3), 50-57.
- UoY Lab Manual CN103-5: "Modulation Schemes on SDR." (Mesh Academic Portal)

### Discussion Questions

1. OFDM dominates modern wireless, but it has high peak-to-average power ratio (PAPR), reducing transmitter efficiency. What alternatives exist, and why hasn't single-carrier modulation made a comeback?
2. Probabilistic constellation shaping approaches the Shannon limit within 0.1 dB. What's left? Is there still room for fundamentally new modulation inventions?
3. You need to design a communication system for nanosatellites in low Earth orbit — limited power (5W solar), 500 km range, 10 Mbps target. Which modulation scheme would you choose, and why?

---

ᚴ **Lecture 6: Line Coding — From Bits to Physical Symbols**

**Course:** CN103 — Data Communications & Signal Processing
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Before modulation, digital bits must be encoded into a form suitable for the physical channel. Line coding — also called baseband modulation — maps a sequence of 1s and 0s into voltage levels, transitions, or pulses. This lecture covers NRZ (non-return-to-zero), RZ, Manchester encoding, 4B/5B and 8B/10B block codes, scrambling, and the 2040 standards: 64B/66B for Ethernet, 128B/130B for PCIe 6.0, and PAM-4 for 400G Ethernet. We'll examine DC balance, clock recovery, spectral properties, and the engineering tradeoffs that drive code selection.

### Key Topics

- **NRZ (Non-Return-to-Zero):** The simplest code — high voltage = 1, low voltage = 0. Pros: uses full bit period, maximum data rate for given bandwidth. Cons: long runs of 1s or 0s create a DC component (bad for transformer-coupled channels) and no transitions for clock recovery. NRZ is used with scrambling (randomizing the bit sequence) in most high-speed serial links.
- **Manchester Encoding:** A transition in the middle of every bit period — high-to-low for 1, low-to-high for 0 (IEEE 802.3 convention). Guarantees a transition every bit (self-clocking) and zero DC component. Cost: uses twice the bandwidth of NRZ. Used in 10 Mbps Ethernet (10BASE-T), RFID, and near-field communication.
- **Block Codes (4B/5B, 8B/10B):** Map n-bit data words to m-bit code words (m > n) with desirable properties. 4B/5B (used in 100BASE-TX) maps 4 data bits to 5 code bits, ensuring at most 3 consecutive zeros. 8B/10B (used in Gigabit Ethernet, PCIe, SATA, USB 3.0, HDMI) maps 8 bits to 10 bits, guaranteeing a maximum run length of 5 identical bits and DC balance (equal number of 1s and 0s over time). The 25% overhead is the price of guaranteed clock recovery.
- **Scrambling:** XOR the data with a pseudorandom binary sequence (PRBS) before transmission. The receiver applies the same PRBS to recover data. Scrambling doesn't add overhead but makes long runs of identical bits statistically unlikely. Used in all high-speed Ethernet (combined with 64B/66B) and SONET/SDH.
- **64B/66B:** The workhorse of 10G+ Ethernet. 64 data bits + 2 sync bits = 66-bit frame. The sync bits (01 for data, 10 for control) provide block alignment; scrambling handles DC balance and clock recovery. Overhead: only 3.125%, vs. 25% for 8B/10B.
- **PAM-4 (Pulse Amplitude Modulation, 4 levels):** Instead of 2 voltage levels, use 4 (e.g., 0, 1/3, 2/3, 1 of full swing). Each symbol carries 2 bits — doubles the data rate for the same baud rate. PAM-4 drives 400 Gbps Ethernet (8 lanes × 50 Gbps) and PCIe 6.0. The cost: 4 levels are harder to distinguish, requiring higher SNR and more sophisticated equalization.
- **DC Balance and Baseline Wander:** Transformer-coupled or AC-coupled channels block DC. If a code has DC bias, the baseline voltage drifts, degrading the eye diagram. Balanced codes (equal 1s and 0s over time) prevent this. Running disparity tracking (8B/10B) or scrambling (64B/66B) maintains DC balance.

### Lecture Notes

The eye diagram is the oscilloscope view that reveals line code quality. By overlaying many bit periods, the eye diagram shows: (1) eye opening — the vertical space between 0 and 1 levels, indicating noise margin; (2) eye width — horizontal space, indicating timing margin; (3) jitter — horizontal variation at crossing points; (4) rise/fall time — slope of the transitions. A "closed eye" means the receiver can't reliably distinguish bits. Eye diagrams are the network engineer's diagnostic tool — one glance reveals signal integrity.

Clock recovery is the hidden requirement driving line code design. The receiver must synchronize its sampling clock to the transmitter's clock, using only the received signal. A phase-locked loop (PLL) adjusts its oscillator based on transitions in the received signal. A long run of identical bits means no transitions — the PLL drifts, and eventually samples at the wrong time (bit slip). Every line code addresses this: Manchester guarantees a transition every bit (at high bandwidth cost), 8B/10B limits run length to 5, and scrambling makes long runs probabilistically impossible.

The shift from 8B/10B to 64B/66B in Ethernet was driven by economics. At 1 Gbps, 25% overhead was tolerable. At 10 Gbps, the overhead meant 2.5 Gbps of wasted capacity — expensive in transceiver cost and power. 64B/66B reduced overhead to 3% while using scrambling to handle clock recovery and DC balance. The 2-bit sync header enables fast block alignment: the receiver looks for the 01 pattern that indicates a data block, while 10 indicates a control block. Two consecutive invalid sync headers trigger a resynchronization search.

PAM-4 represents the 2040 industry's answer to the bandwidth wall. As data rates push into hundreds of Gbps per lane, the Nyquist frequency (half the baud rate) exceeds what PCB traces and connectors can handle. Rather than fight physics with ever-higher bandwidth, PAM-4 packs more bits into the same bandwidth by using more voltage levels. The tradeoff is SNR: PAM-4 has 1/3 the voltage margin of NRZ for the same swing. Forward error correction (FEC) — Reed-Solomon for 400G Ethernet, concatenated codes for PCIe 6.0 — compensates for the higher error rate, bringing the system BER below 10⁻¹⁵.

### Required Reading

- Widmer, A.X. & Franaszek, P.A. (1983). "A DC-Balanced, Partitioned-Block, 8B/10B Transmission Code." *IBM Journal of Research and Development*, 27(5), 440-451.
- IEEE 802.3-2040, Clause 49: "Physical Coding Sublayer (PCS) for 64B/66B."
- PCI-SIG (2039). "PCI Express 6.0 Specification — PAM-4 Signaling and FEC."
- UoY Lab Manual CN103-6: "Line Coding and Eye Diagrams." (Mesh Academic Portal)

### Discussion Questions

1. 8B/10B has 25% overhead but guaranteed DC balance and short run length. 64B/66B has 3% overhead but requires scrambling. Why was 8B/10B used for so long despite the overhead? What changed to enable the transition?
2. PAM-4 doubles throughput at the cost of SNR. Could we use PAM-8 or PAM-16 in electrical channels? What are the practical limits, and how close are we to them?
3. Self-clocking codes were essential before ubiquitous crystal oscillators. In 2040, with atomic clocks in every data center, do we still need clock recovery from the data signal? Why or why not?

---

ᚷ **Lecture 7: Multiplexing — Sharing the Channel**

**Course:** CN103 — Data Communications & Signal Processing
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Communication channels are expensive. A single trans-Atlantic fiber cable costs $300 million to deploy. The radio spectrum is finite. The engineering response is multiplexing: sharing one physical channel among many logical streams. This lecture covers frequency-division multiplexing (FDM), time-division multiplexing (TDM), wavelength-division multiplexing (WDM), code-division multiplexing (CDM), space-division multiplexing (SDM — the 2040 multi-core fiber revolution), and statistical multiplexing (the packet-switching paradigm). We'll analyze the capacity gains, insertion losses, crosstalk limits, and the economics of multiplexing — why a 100 Gbps link costs much less than 100 × 1 Gbps links.

### Key Topics

- **Frequency-Division Multiplexing (FDM):** Assign each signal its own frequency band within the channel. Used since the earliest radio broadcasting — AM stations at 540-1600 kHz, spaced 10 kHz apart. Guard bands prevent adjacent-channel interference. OFDM is a sophisticated digital FDM variant. In 2040, FDM underlies 5G NR (orthogonal frequency resources) and cable broadband (DOCSIS subcarriers).
- **Time-Division Multiplexing (TDM):** Allocate fixed time slots to each stream in a repeating frame. T1 (1.544 Mbps) carries 24 voice channels × 8 bits + 1 framing bit every 125 µs. SONET/SDH scales this to OC-768 (40 Gbps). TDM guarantees bandwidth but wastes slots when a stream has nothing to send. The 2040 descendant: deterministic networking (DetNet) for industrial control and financial trading, where guaranteed latency matters more than average utilization.
- **Wavelength-Division Multiplexing (WDM):** The optical version of FDM. Coarse WDM (CWDM) spaces channels 20 nm apart, fitting 18 channels in the 1270-1610 nm range — cheap, unamplified, for metro. Dense WDM (DWDM) spaces channels 50 GHz (0.4 nm) or 25 GHz (0.2 nm) apart in the C-band, fitting 80-160 channels — amplified by EDFAs, for long-haul. Super-Channels group multiple carriers into a single logical channel using Nyquist-spaced subcarriers — the optical equivalent of OFDM. In 2040, a single fiber pair carries 64 Tbps using C+L-band DWDM with 800 Gbps per wavelength.
- **Code-Division Multiplexing (CDM):** All users transmit simultaneously in the same frequency band, distinguished by orthogonal spreading codes. The receiver correlates with the desired code; other users' signals appear as noise (multiple access interference). CDMA powered 3G cellular and is used in GPS (each satellite has a unique Gold code). In 2040, CDMA principles live on in quantum key distribution, where photon states are distinguished by measurement basis rather than code.
- **Space-Division Multiplexing (SDM):** The 2040 frontier. Multi-core fiber (MCF) contains 7, 19, or more cores in a single cladding — each core carries independent WDM signals. Few-mode fiber (FMF) uses multiple spatial modes within a single core. Together, SDM promises to multiply fiber capacity by 10-100×, potentially breaking the nonlinear Shannon limit of single-mode fiber. The challenge: crosstalk between cores/modes requires MIMO digital signal processing — essentially, WiFi-style MIMO at optical frequencies.
- **Statistical Multiplexing:** Unlike TDM, statistical multiplexing allocates channel capacity on demand. Packets from multiple streams share the channel; buffering absorbs bursts. Efficiency comes from the law of large numbers — with many streams, peak aggregate demand rarely exceeds capacity. This is the packet-switching principle that powers the internet. The cost: variable delay and potential packet loss. The 2040 tension: statistical multiplexing (efficient but unpredictable) vs. deterministic networking (predictable but less efficient).

### Lecture Notes

DWDM is the unsung hero of the global internet. A single optical amplifier (EDFA) can amplify all C-band wavelengths simultaneously, replacing the per-wavelength regenerators of earlier systems. This economy of scale — one amplifier for 80 channels — made intercontinental fiber economically viable. The 2040 DWDM system deploys "flex-grid" (ITU-T G.694.1), where channels can be 37.5 GHz, 50 GHz, 75 GHz, or flexible multiples, rather than the fixed 50 GHz grid of earlier systems. A 400 Gbps 16-QAM signal needs ~75 GHz; an 800 Gbps 64-QAM signal needs the same 75 GHz — flex-grid lets the network operator mix generations of transceivers on the same fiber.

TDM has a surprising 2040 revival in deterministic networking. While the internet's statistical multiplexing works beautifully for web browsing and streaming, it fails for applications that demand guaranteed latency bounds: factory automation (sub-ms control loops), autonomous vehicle coordination, remote surgery, and financial trading (where 1 µs advantage is worth millions). The IETF DetNet Working Group and IEEE 802.1 TSN (Time-Sensitive Networking) define TDM-like schedules over Ethernet. Frames are assigned to time slots in a repeating cycle; non-deterministic traffic fills the remaining slots. The 2040 challenge: making deterministic and statistical sharing coexist without the worst of both worlds.

Space-division multiplexing is the most exciting physical-layer development since the EDFA. Standard single-mode fiber has been within 3-5 dB of its nonlinear Shannon limit since ~2015. To continue scaling internet capacity (growing ~30% annually), we need a new degree of freedom. MCF provides it: a 19-core fiber with the same cladding diameter as standard fiber (125 µm) can carry 19× the capacity — potentially 1.2 Pbps per fiber. The catch: signals "leak" between cores through evanescent coupling, creating crosstalk. MIMO processing (multiple-input multiple-output), borrowed from wireless, can untangle the signals — but at the cost of DSP complexity that scales with the square of the core count. For 19 cores, a 19×19 MIMO equalizer must update at the symbol rate (tens of GHz) — a computational challenge being met by application-specific integrated circuits (ASICs) in 3 nm CMOS.

### Required Reading

- Kartalopoulos, S.V. (2039). *DWDM: Networks, Devices, and Technology*. Wiley-IEEE Press. Chapters 1-3.
- Saitoh, K. & Matsuo, S. (2036). "Multicore Fiber Technology." *Journal of Lightwave Technology*, 34(1), 55-66.
- Nasralla, A. et al. (2038). "Deterministic Networking for Industry 4.0: A Survey." *IEEE Communications Surveys & Tutorials*, 40(2), 897-934.
- UoY Case Study: "Bifrǫst Space-Division Multiplexing Trial — Trondheim to Bergen."

### Discussion Questions

1. Statistical multiplexing made the internet cheap but unpredictable. Is deterministic networking worth the efficiency loss? For which applications is it essential, and for which is it overkill?
2. MCF adds spatial parallelism to optical fiber, but increases crosstalk and DSP complexity. At what core count does the DSP cost outweigh the capacity gain? How would you find the optimal number of cores?
3. Could we eliminate multiplexing entirely by giving every device its own dedicated fiber or frequency? What would such a network look like, and why hasn't it happened?

---

ᚹ **Lecture 8: Error Detection — Parity, CRC, and Checksums**

**Course:** CN103 — Data Communications & Signal Processing
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Errors are inevitable. Thermal noise, interference, and signal degradation will occasionally flip a bit. The first line of defense is detection: recognizing that an error occurred so the receiver can request retransmission. This lecture covers the theory and practice of error detection: parity bits, checksums, and cyclic redundancy checks (CRC). We'll derive the mathematics of polynomial arithmetic in GF(2), analyze the error detection capability of standard CRCs (CRC-32, CRC-32C), and study how Ethernet, IP, TCP, and 5G each use layered error detection — and what happens when they fail.

### Key Topics

- **Error Models:** The binary symmetric channel (BSC) — each bit is flipped independently with probability p. Burst errors — a contiguous sequence of corrupted bits, common in wireless and magnetic storage. Understanding the error model is essential for choosing the right detection scheme.
- **Parity:** The simplest error detection: add one bit so the total number of 1s is even (or odd). Detects all single-bit errors, but fails for any even number of bit flips. Used in RAM (ECC memory uses 8 parity bits per 64 data bits, enabling single-error correction and double-error detection — SECDED).
- **Checksums:** Sum the data as N-bit words, take the complement. The Internet Checksum (RFC 1071) uses 16-bit one's complement addition. Simple to compute in software but weak: it can't detect swapped 16-bit words and misses many error patterns. Used in IP, TCP, UDP — supplemented by stronger link-layer CRCs.
- **Cyclic Redundancy Check (CRC):** Treat the data as a polynomial over GF(2) (binary coefficients, addition = XOR, no carries). Divide by a generator polynomial; the remainder is the CRC. A well-chosen generator polynomial of degree r detects: all single-bit errors, all double-bit errors (if the polynomial has a factor of at least three terms), all odd numbers of errors (if (x+1) is a factor), all burst errors of length ≤ r, and 1 − 2⁻ʳ of longer bursts. CRC-32 (Ethernet, gzip, PNG) uses r=32; CRC-32C (iSCSI, SCTP) uses a different polynomial with better performance on typical error patterns.
- **Generator Polynomials in Practice:** CRC-8-CCITT: x⁸ + x² + x + 1 (used in ATM headers). CRC-16-CCITT: x¹⁶ + x¹² + x⁵ + 1 (used in Bluetooth, XMODEM). CRC-32 (IEEE 802.3): x³² + x²⁶ + x²³ + x²² + x¹⁶ + x¹² + x¹¹ + x¹⁰ + x⁸ + x⁷ + x⁵ + x⁴ + x² + x + 1. CRC-32C (Castagnoli): x³² + x²⁸ + x²⁷ + x²⁶ + x²⁵ + x²³ + x²² + x²⁰ + x¹⁹ + x¹⁸ + x¹⁴ + x¹³ + x¹¹ + x¹⁰ + x⁹ + x⁸ + x⁶ + 1. Each was chosen after extensive analysis of error detection capability vs. hardware implementation cost.
- **Hamming Distance and Error Detection:** The Hamming distance d of a code is the minimum number of bit positions where any two valid codewords differ. A code with Hamming distance d can detect up to d−1 errors, or correct ⌊(d−1)/2⌋ errors. CRCs have large Hamming distance for short messages — CRC-32 provides d=4 for messages up to 2¹⁶−1 bits. The theory of error-correcting codes (Lecture 9) builds on this foundation.

### Lecture Notes

The mathematics of CRC is elegant and practical. A message M(x) is a polynomial with coefficients in {0,1}. The CRC uses a generator polynomial G(x) of degree r. The transmitter computes R(x) = (M(x) × xʳ) mod G(x) and appends R(x) as the r-bit CRC. The transmitted message T(x) = M(x) × xʳ + R(x). The receiver computes T(x) mod G(x). If the remainder is zero, the message is assumed error-free. If non-zero, an error is detected. This works because T(x) = M(x) × xʳ + (M(x) × xʳ mod G(x)) is necessarily divisible by G(x).

The hardware implementation is a linear feedback shift register (LFSR) — a chain of r flip-flops with XOR gates at positions corresponding to the 1s in G(x). The data is shifted in, and after processing, the register contains the CRC. This can run at line rate (100+ Gbps) in a few hundred gates — one of the most efficient error detection schemes ever invented.

Layered error detection is a defensive programming pattern in network protocols. Consider an HTTP response: the application payload may have no integrity check, but TCP adds a 16-bit checksum (weak), IP adds a 16-bit header checksum (weak), and Ethernet adds a 32-bit CRC (strong). Ethernet's CRC catches almost all errors that survive TCP and IP checksums. But this layering can fail: in 2008, a widely-deployed router had a bug where it corrupted data internally, then recomputed a correct CRC and TCP checksum for the corrupted data — passing all integrity checks with bad data. This is the end-to-end argument: integrity must ultimately be verified at the application layer (TLS MAC, application checksums).

The undetected error probability of CRC-32 is approximately 2⁻³² = 2.3 × 10⁻¹⁰ per message for random errors. For a 10 Gbps link carrying 1500-byte frames, that's ~830,000 frames per second, or one undetected error every ~5,200 seconds (~1.4 hours) — unacceptable for reliable data transfer. This is why high-reliability systems add stronger checks: iSCSI uses CRC-32C over the entire data digest, and ZFS uses 256-bit checksums. In 2040, post-quantum hashes (SHA-3, BLAKE3) provide 256-512 bit integrity tags with negligible performance cost.

### Required Reading

- Peterson, W.W. & Brown, D.T. (1961). "Cyclic Codes for Error Detection." *Proceedings of the IRE*, 49(1), 228-235.
- Koopman, P. & Chakravarty, T. (2004). "Cyclic Redundancy Code (CRC) Polynomial Selection for Embedded Networks." *DSN 2004*.
- RFC 1071: "Computing the Internet Checksum."
- Stone, J. & Partridge, C. (2000). "When the CRC and TCP Checksum Disagree." *ACM SIGCOMM 2000*.

### Discussion Questions

1. CRC-32 will miss roughly 1 in 4 billion random errors. Is that good enough for (a) a firmware update to a satellite, (b) a financial transaction, (c) a cat video? What stronger measures would you add?
2. The end-to-end argument says integrity should be verified at the highest layer. Yet every layer adds its own checks. Is this belt-and-suspenders redundancy, or is each layer solving a different problem?
3. CRC computation is embarrassingly serial — each bit depends on state from previous bits. How do 400 Gbps Ethernet MACs compute CRC at line rate? (Hint: parallel CRC, table lookup, and pipelining.)

---

ᚺ **Lecture 9: Error Correction — FEC from Hamming to LDPC and Polar Codes**

**Course:** CN103 — Data Communications & Signal Processing
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Detection tells you something is wrong; correction fixes it without retransmission. Forward Error Correction (FEC) adds structured redundancy so the receiver can recover the original data despite errors. This lecture traces the 80-year arc of error correction: Hamming codes (1950), Reed-Solomon codes (1960), convolutional codes with Viterbi decoding (1967), Turbo codes (1993), LDPC codes (rediscovered 1996), and polar codes (2008). We'll examine code rate, coding gain, decoding complexity, and how each generation has closed the gap to the Shannon limit. For 2040 networking, we focus on the codes that matter: LDPC (WiFi 7, 5G data channels, 400G Ethernet), polar codes (5G control channels), and the emerging class of neural decoders.

### Key Topics

- **Block Codes:** (n, k) codes take k data bits and produce n coded bits, with code rate R = k/n. Hamming codes (n=2ᵐ−1, k=2ᵐ−m−1 for m≥3) can correct single-bit errors. Perfect codes — they achieve the Hamming bound with equality, meaning they're optimally efficient for their error correction capability.
- **Reed-Solomon Codes:** Operate on symbols (bytes), not bits — an RS(n, k) code over GF(2⁸) takes k bytes and produces n bytes, correcting up to (n−k)/2 byte errors. Ideal for burst errors because a burst of 8 bit errors within one byte counts as a single symbol error. Used in CDs, DVDs, QR codes, DVB, DSL, and 400G Ethernet KP4 FEC over PAM-4 links.
- **Convolutional Codes:** Process a continuous stream of bits through a shift register, producing multiple output bits per input bit. The Viterbi algorithm (1967) performs maximum-likelihood decoding by finding the shortest path through a trellis. Constraint length K determines complexity: Viterbi complexity is O(2ᴷ). Used in 2G/3G cellular, 802.11a/g WiFi, and deep-space communications (Voyager used constraint-length-7 convolutional codes).
- **Turbo Codes:** The breakthrough of 1993. Two parallel convolutional encoders separated by an interleaver; iterative decoding passes soft information (log-likelihood ratios) between decoders, converging toward the maximum-likelihood solution. Turbo codes achieved BER = 10⁻⁵ within 0.7 dB of the Shannon limit — stunning the community. Used in 3G/4G cellular and deep-space communications.
- **LDPC (Low-Density Parity-Check) Codes:** Gallager's 1960 invention, ignored for 35 years because the decoders were too complex for the era's hardware. Rediscovered by MacKay and Neal in 1996. Defined by a sparse parity-check matrix; decoded by belief propagation (message passing on a Tanner graph). Regular LDPC codes approach capacity within 0.0045 dB — the closest any practical code has come. Used in WiFi (802.11n/ac/ax/be), 5G NR data channels, DVB-S2 (satellite TV), 10G-PON, and 400G Ethernet.
- **Polar Codes:** Arikan's 2008 invention, the first codes *provably* achieving symmetric channel capacity for any binary-input discrete memoryless channel. Based on channel polarization: recursively combining and splitting channels creates "good" channels (near-perfect) and "bad" channels (near-useless). Transmit data on good channels, freeze bad ones. Successive cancellation decoding with list size L=8 achieves near-ML performance. Used in 5G NR control channels.
- **Neural Decoders (2040):** Train a neural network to decode directly from received symbols. For structured codes (LDPC, polar), neural decoders can learn to handle non-Gaussian noise, nonlinear channels, and hardware impairments that violate the theoretical model. The 2040 frontier: hyperdimensional computing decoders that operate in 10,000-dimensional vector spaces, offering graceful degradation and one-shot learning of new channel conditions.

### Lecture Notes

The coding gain of an FEC scheme — the reduction in required SNR for a given BER — measures its value. A Hamming code provides ~0.5 dB gain. Reed-Solomon provides 3-4 dB. Convolutional codes with Viterbi provide 5-6 dB. Turbo and LDPC provide 8-10 dB. Each 3 dB of coding gain doubles the link distance (in free space) or quadruples the capacity (near the Shannon limit). The cumulative 10 dB gain from modern FEC means a wireless link that would need 100 mW transmit power uncoded can operate at 10 mW — extending battery life or range proportionally.

LDPC decoding via belief propagation is an elegant example of distributed computation. The Tanner graph has two types of nodes: variable nodes (bits) and check nodes (parity equations). Messages — log-likelihood ratios — flow iteratively: variable nodes sum incoming messages from connected checks and the channel observation; check nodes compute the probability that their parity equation is satisfied given the variable estimates. After 10-50 iterations, the messages converge (or don't — a decoding failure). The sparsity of the parity-check matrix keeps complexity linear in block length. A (2048, 1024) LDPC code decodes in ~50 µs on a modern ASIC.

Polar codes' theoretical importance is profound: they are the first code family to provably achieve Shannon capacity for all symmetric binary-input channels. The construction is recursive: two copies of a channel W → W⁻ (worse) and W⁺ (better). Repeating this polarization step log₂N times transforms N independent copies of W into channels that are either almost noiseless (capacity → 1) or almost useless (capacity → 0). The fraction of good channels approaches the original channel capacity — exactly Shannon's prediction. In practice, polar codes with CRC-aided successive cancellation list decoding (CA-SCL) match or exceed LDPC performance at short block lengths, which is why 5G chose polar codes for control channels (typically <1000 bits).

The 2040 practical reality: Ethernet and WiFi use LDPC, 5G uses LDPC + polar, storage uses Reed-Solomon (still!), and deep-space uses Turbo + LDPC. There is no universal best code — the choice depends on block length, target BER, latency budget, and decoder power/area constraints. A 400G Ethernet port's FEC consumes ~5W of the ~12W transceiver power budget — FEC efficiency directly impacts the thermal design of every switch and router.

### Required Reading

- Gallager, R.G. (1963). *Low-Density Parity-Check Codes*. MIT Press. (His 1960 PhD thesis, published as a monograph.)
- MacKay, D.J.C. & Neal, R.M. (1996). "Near Shannon Limit Performance of Low Density Parity Check Codes." *Electronics Letters*, 32(18), 1645-1646.
- Arikan, E. (2009). "Channel Polarization: A Method for Constructing Capacity-Achieving Codes." *IEEE Trans. Info. Theory*, 55(7), 3051-3073.
- Nachmani, E. et al. (2038). "Neural Decoders: From Hamming to Hyperdimensional Computing." *IEEE JSAC*, 56(4), 891-910.

### Discussion Questions

1. LDPC codes were invented in 1960, ignored, rediscovered in 1996, and now dominate high-speed communications. What other "ahead of its time" ideas might be sitting in the literature, waiting for hardware to catch up?
2. Neural decoders can outperform classical algorithms on real-world channels that don't match theoretical models. But they're black boxes — hard to certify, hard to prove error floors. Should safety-critical systems (aviation, medical) use neural decoders?
3. Polar codes are the first provably capacity-achieving codes. Does this mean code design is "solved" for symmetric channels? What open problems remain?

---

ᚾ **Lecture 10: Source Coding — Compression and the Limits of Representation**

**Course:** CN103 — Data Communications & Signal Processing
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Channel coding adds redundancy to combat errors; source coding removes redundancy to reduce bandwidth. Compression is the dual of error correction, governed by Shannon's source coding theorem: a source with entropy H can be compressed to H bits per symbol on average, and no further. This lecture covers lossless compression (Huffman coding, arithmetic coding, Lempel-Ziv, Burrows-Wheeler), lossy compression (JPEG, MP3, video codecs), and the 2040 frontier: neural compression (autoencoders), semantic compression (transmitting meaning rather than bits), and the compression-communication co-design that treats source and channel coding jointly.

### Key Topics

- **Entropy and Information Content:** Shannon entropy H(X) = −Σ p(x) log₂ p(x) measures the minimum bits per symbol to represent source X. English text has H ≈ 1.0-1.5 bits per character (much lower than 8 bits because of letter frequency and grammar). The source coding theorem: H ≤ average code length < H + 1 for optimal symbol-by-symbol coding.
- **Huffman Coding:** Build a binary tree bottom-up by repeatedly merging the two least-probable symbols. Produces an optimal prefix code — no codeword is a prefix of another, enabling instantaneous decoding. Used in JPEG, MP3, DEFLATE (gzip, PNG). Limitation: codes symbols individually, so the average code length can be up to 1 bit worse than entropy.
- **Arithmetic Coding:** Encodes the entire message as a single number in [0,1), with subintervals proportional to symbol probabilities. Achieves code length within 2 bits of entropy for the entire message — asymptotically optimal. Used in JPEG 2000, H.264/AVC, H.265/HEVC, and the 2040 AV2 standard.
- **Lempel-Ziv (LZ77/LZ78):** The workhorse of lossless compression. Rather than modeling probabilities, LZ discovers repeated patterns in the data and replaces them with back-references (distance, length) pairs. DEFLATE = LZ77 + Huffman, used in gzip, PNG, ZIP. LZMA (7-zip) uses a larger dictionary and arithmetic coding. Zstandard (Facebook, 2015) uses LZ77 + FSE (Finite State Entropy) + Huffman — the 2040 standard for general-purpose compression, offering 2-3× speed at equivalent ratios.
- **Lossy Compression:** Exploit human perception limitations. JPEG discards high-frequency DCT coefficients that the human eye barely notices. MP3 discards audio frequencies masked by louder nearby frequencies (psychoacoustic masking). Modern video codecs (AV1, VVC/H.266, the 2040 AV2 standard) use motion compensation, transform coding, and neural post-filters to achieve 1000:1 compression ratios for acceptable perceptual quality. The metric shifts from MSE (mean squared error) to VMAF (Netflix's perceptual quality metric) and the 2040 standard: neural MOS predictors.
- **Joint Source-Channel Coding:** Shannon proved that source and channel coding can be designed separately without loss of optimality — *in the limit of infinite complexity and delay*. In practice, joint design can outperform. The 2040 frontier: neural joint source-channel coding, where an autoencoder maps source data directly to channel symbols, trained end-to-end on the actual channel. Promises graceful degradation: as channel SNR drops, the reconstruction quality degrades smoothly rather than hitting a digital cliff.

### Lecture Notes

Shannon's separation theorem — "design source coding and channel coding independently" — is one of the most elegant and deceptive results in information theory. It's true asymptotically, but real systems have finite block lengths and latency constraints. A video call cannot wait for an ideal source code to compress a frame and an ideal channel code to protect it — the combined delay would make conversation impossible. This is why video conferencing uses layered coding: a base layer with strong FEC ensures basic intelligibility; enhancement layers with weaker or no FEC improve quality when the channel is good.

The entropy of real-world data sources is often far lower than naive analysis suggests. A 4K video frame is 3840 × 2160 × 3 bytes = 24.9 MB uncompressed. But adjacent pixels are highly correlated, and adjacent frames even more so. After motion compensation (encoding only the difference from a predicted frame), transform coding (DCT/DST), and quantization (discarding imperceptible detail), the actual information content might be 100-500 KB per frame — a 50-250:1 compression ratio. The remaining 500 KB might compress further losslessly (entropy coding) to 200-300 KB. Modern codecs squeeze 4K video into 8-25 Mbps — nearly 1000:1 compression from the raw pixel rate of 6 Gbps.

Neural compression is the 2040 revolution. Traditional codecs require human-designed transforms (DCT, wavelets) and hand-tuned quantization tables. Neural codecs learn these from data. An autoencoder — encoder network → bottleneck (low-dimensional representation) → decoder network — trained on millions of images, discovers transforms, quantization, and entropy models jointly. The 2040 state of the art: neural codecs achieve the same perceptual quality as AV2 at 40-60% of the bitrate. The challenge: decoder complexity — a neural decoder runs on specialized AI accelerators, not the fixed-function hardware in every TV and phone. The 2040 solution: standardized neural decoder IP blocks in 2 nm SoCs.

Semantic compression is the most radical idea: transmit the *meaning* rather than the *signal*. Rather than sending pixels for every frame of a video call, transmit a 3D facial model and expression parameters — the receiver renders the face locally. Used in Apple's FaceTime (Memoji) and Meta's Codec Avatars (2040, photorealistic). The bandwidth drops from Mbps to kbps — four orders of magnitude. The philosophical question: is the reproduced face the "same" communication? Shannon's theory doesn't answer this; it only concerns itself with reproducing the transmitted symbols, not their meaning. The 2040 debate: semantic communication vs. Shannon communication — are they complementary or fundamentally different paradigms?

### Required Reading

- Shannon, C.E. (1948). "A Mathematical Theory of Communication." Part I: "Discrete Noiseless Systems."
- Cover, T.M. & Thomas, J.A. (2036). *Elements of Information Theory*, 3rd Edition. Wiley. Chapters 5 (Data Compression) and 7 (Channel Capacity).
- Ballé, J. et al. (2038). "End-to-End Optimized Image Compression." *ICLR 2038*.
- UoY Case Study: "Semantic Communication over the Bifrǫst LEO Ring."

### Discussion Questions

1. Lossy compression throws away information. How should we decide what to keep? Is the "perceptual" standard (it looks/sounds good) sufficient, or should we minimize information loss by some objective metric?
2. Semantic compression transmits meaning, not bits. If an AI regenerates my face and voice from parameters, am I still "communicating," or has the AI become a co-author of my message?
3. Shannon proved that source and channel coding can be separated without loss. Yet all modern systems violate separation (layered video coding, joint source-channel neural coding). Are we being pragmatic, or is Shannon's theorem irrelevant for finite-length systems?

---

ᛁ **Lecture 11: Digital Modulation in Practice — SDR, OFDM Stacks, and the 2040 Air Interface**

**Course:** CN103 — Data Communications & Signal Processing
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

Theory meets practice. This lecture bridges the mathematical foundations from previous lectures to the operational reality of building communication systems. Using software-defined radio (SDR) as our platform, we walk through the complete transmit and receive chains: bit generation → FEC encoding → interleaving → constellation mapping → OFDM framing → IFFT → cyclic prefix insertion → digital-to-analog conversion → upconversion → power amplification → antenna. And the reverse. We examine real-world impairments — IQ imbalance, phase noise, PA nonlinearity, carrier frequency offset — and the DSP algorithms that compensate for them. Students in the Valhalla Network Lab will build an end-to-end OFDM link on SDR platforms and measure its performance.

### Key Topics

- **Software-Defined Radio Architecture:** An SDR digitizes the RF spectrum at the antenna (or after one downconversion stage), then performs all signal processing in software/FPGA. The ideal SDR: antenna → ADC → DSP → DAC → antenna. Practical SDRs (like the Bifrǫst SDR Platform, based on Xilinx RFSoC) integrate 16-bit ADCs sampling at 5 GS/s (Nyquist for 2.5 GHz bandwidth) with programmable logic and ARM cores. Students program the SDR in Python (PySDR) and C++ (GNU Radio framework).
- **The OFDM Transmitter Chain:** (1) Scramble bits to avoid long runs. (2) Encode with LDPC FEC. (3) Interleave to spread burst errors across multiple codewords. (4) Map bits to QAM constellation points (1-12 bits/symbol). (5) Insert pilot symbols (known reference signals for channel estimation). (6) Assign subcarriers (data, pilots, nulls for DC and guard bands). (7) IFFT — transform from frequency domain to time domain. (8) Append cyclic prefix. (9) Apply pulse-shaping filter. (10) DAC → analog IQ modulator → PA → antenna.
- **The OFDM Receiver Chain:** (1) Antenna → LNA → IQ demodulator → ADC. (2) Packet detection and coarse synchronization (Schmidl-Cox algorithm). (3) Carrier frequency offset estimation and correction. (4) FFT — back to frequency domain. (5) Channel estimation from pilots (least squares or MMSE). (6) Equalization (zero-forcing or MMSE per subcarrier). (7) Soft demapping (LLR per bit). (8) Deinterleaving. (9) LDPC decoding (belief propagation). (10) Descrambling. (11) CRC verification.
- **Real-World Impairments and Compensation:** IQ imbalance — the I and Q paths in the analog frontend have slightly different gains and phases, creating an image of the signal at the negative frequency. Digital pre-distortion (DPD) linearizes the power amplifier by applying an inverse nonlinearity in digital. Carrier frequency offset (CFO) arises from oscillator mismatch between Tx and Rx — even 1 ppm at 6 GHz means 6 kHz offset, which rotates the constellation. Schmidl-Cox uses a training sequence with two identical halves; the phase difference between them reveals the CFO.
- **The 2040 Air Interface — 6G and Beyond:** 6G (2030+) operates in sub-THz bands (100-300 GHz) with bandwidths up to 100 GHz per carrier. Key innovations: reconfigurable intelligent surfaces (RIS) — passive arrays that reflect and beamform signals without active amplification, turning walls into smart reflectors. Orbital angular momentum (OAM) multiplexing — using the spatial phase structure of electromagnetic waves to create orthogonal channels at the same frequency. AI-native air interfaces, where the entire PHY layer (modulation, coding, equalization) is a single neural network trained end-to-end, optimized for the specific deployment environment.

### Lecture Notes

The Schmidl-Cox algorithm is a beautiful example of signal processing elegance. The transmitter sends a training symbol where the first half and second half are identical in the time domain (achieved by loading only even subcarriers in frequency, then taking the IFFT). The receiver correlates the received signal with a delayed copy of itself — when the correlation peaks, a packet has arrived (packet detection). The phase of the correlation peak reveals the carrier frequency offset. Two training symbols (the second with a known differential pattern between even and odd subcarriers) provide fine synchronization. This algorithm, published in 1997, has been used in every OFDM standard since: WiFi, WiMAX, LTE, 5G.

Channel estimation is the receiver's hardest problem. The channel (multipath, Doppler, fading) distorts every subcarrier differently. Pilot symbols — known QAM points inserted at regular positions in the time-frequency grid — provide reference points. The receiver estimates the channel at pilot positions (simply received/transmitted pilot value) and interpolates to estimate the channel at data positions. The 2040 approach: neural channel estimation. A neural network trained on millions of channel realizations learns to estimate the channel from pilots more accurately than classical MMSE, especially in high-mobility scenarios where the channel changes within a single OFDM symbol.

The power amplifier (PA) is the most expensive, power-hungry, and nonlinear component in the transmitter chain. A Class-A PA is linear but only 30% efficient — 70% of the DC power becomes heat. A Class-AB PA achieves 50-60% efficiency but introduces nonlinear distortion at the signal peaks. OFDM is particularly vulnerable because its high peak-to-average power ratio (PAPR, typically 10-12 dB) drives the PA into saturation on peaks. Digital pre-distortion (DPD) solves this: measure the PA's AM-AM (amplitude) and AM-PM (phase) distortion curves, then apply the inverse distortion in the digital baseband before the DAC. The result: an efficient PA that behaves linearly. In 2040, AI-based DPD adapts in real time to temperature changes, aging, and channel conditions.

### Required Reading

- Schmidl, T.M. & Cox, D.C. (1997). "Robust Frequency and Timing Synchronization for OFDM." *IEEE Trans. Communications*, 45(12), 1613-1621.
- Tse, D. & Viswanath, P. (2035). *Fundamentals of Wireless Communication*, 3rd Edition. Cambridge. Chapter 3: "Point-to-Point Communication: Detection, Diversity and Channel Uncertainty."
- UoY Lab Manual CN103-11: "Building an OFDM Transceiver on the Bifrǫst SDR Platform."
- Björnson, E. et al. (2039). "Reconfigurable Intelligent Surfaces: A Signal Processing Perspective." *IEEE Signal Processing Magazine*, 56(5), 124-142.

### Discussion Questions

1. The Schmidl-Cox algorithm has been used for 40+ years. With modern AI techniques, could we design a better synchronization algorithm? What would the training data be?
2. OFDM's high PAPR has been called "the worst problem in wireless." Why hasn't a fundamentally better modulation scheme replaced it?
3. Reconfigurable intelligent surfaces turn passive walls into active signal reflectors. Does this change the fundamental channel model, or is it just a better antenna?

---

ᛃ **Lecture 12: The 2040 Frontier — Terahertz, Quantum, and Neuromorphic Communications**

**Course:** CN103 — Data Communications & Signal Processing
**Degree:** Bachelor of Science in Computer Networking, University of Yggdrasil, 2040

---

### Overview

The physical layer never stops evolving. This final lecture surveys the three frontiers that will define signal processing in the 2040s and beyond: terahertz communications (100 GHz-10 THz — the last great swath of unallocated spectrum), quantum communications (single-photon signals, entanglement-based security, quantum repeaters), and neuromorphic signal processing (brain-inspired chips that process signals with femtojoule energy efficiency). We examine the physics, the engineering challenges, the likely applications, and the philosophical implications of communication systems that operate at the very limits of physical law.

### Key Topics

- **Terahertz Communications:** The 0.1-10 THz band offers contiguous bandwidths of tens of GHz — enough for 1 Tbps wireless links. Challenges: (1) Atmospheric absorption — water vapor lines at 183, 325, 380, 448, 557, 752, 988 GHz create opaque windows, limiting range. (2) Semiconductor technology — CMOS cutoff frequency (f_max) is approaching ~500 GHz for 1 nm nodes; beyond that requires III-V materials (InP, GaN) or graphene. (3) Beamforming — at THz, wavelengths are <1 mm, enabling massive antenna arrays in tiny form factors. Applications: wireless backhaul, data center inter-rack links, and kiosk downloading (tap your device, get a movie in 0.1 seconds).
- **Quantum Communications:** Information encoded in quantum states — polarization of single photons, phase of coherent states, entanglement between photon pairs. Key protocols: BB84 (quantum key distribution, provably secure based on the no-cloning theorem), quantum teleportation (transferring a quantum state using entanglement + classical communication), and the embryonic quantum internet (entanglement distribution over fiber and satellite). The 2040 achievement: the Bifrǫst Quantum Backbone — 10 QKD nodes across Scandinavia, distributing symmetric keys for the classical network's MACsec encryption, with quantum repeaters extending the range beyond the ~100 km direct-transmission limit.
- **Entanglement and the No-Cloning Theorem:** An unknown quantum state cannot be perfectly copied. This is the foundation of quantum security — an eavesdropper measuring the quantum channel inevitably disturbs it, revealing their presence. In BB84, Alice sends photons in one of four polarization states (horizontal, vertical, +45°, −45°); Bob measures in a randomly chosen basis (rectilinear or diagonal). After transmission, they compare bases over a classical channel, discard mismatches, and the remaining bits form a shared secret key. Any eavesdropper introduces errors that are detectable through statistical testing of a subset of the key.
- **Quantum Repeaters:** Photon loss is the enemy of quantum communication — fiber attenuation of 0.2 dB/km means a photon has only a 1% chance of surviving a 100 km fiber. Classical amplifiers can't help (they would measure the photon, destroying the quantum state — no-cloning forbids copying). Quantum repeaters use entanglement swapping: create entangled pairs over short segments, then perform Bell-state measurements at intermediate nodes to extend entanglement to the full distance. The 2040 state of the art: first-generation quantum repeaters with 2-4 segments, achieving key rates of ~100 bps over 500 km.
- **Neuromorphic Signal Processing:** The human brain processes sensory signals with astounding efficiency — ~20 watts for the equivalent of exaflop-scale computation. Neuromorphic chips (Intel Loihi 3, IBM NorthPole, the Bifrǫst Synapse ASIC) use spiking neural networks: neurons communicate via spikes (brief pulses), with information encoded in spike timing rather than continuous values. For signal processing, this enables: (1) event-driven operation (no computation when the signal is quiet — 100-1000× power savings for sparse signals), (2) temporal processing (spike timing naturally encodes sequences, eliminating explicit buffering), (3) on-chip learning (synaptic plasticity adapts to changing channel conditions continuously).
- **The Limits of Physics:** What are the ultimate physical limits on communication? The Bekenstein bound: the maximum information content of a physical system with energy E and radius R is I ≤ 2πER/(ħc ln 2) bits. For a 1 kg, 0.1 m radius device, this is ~10³⁹ bits — so far beyond current technology that it's irrelevant. More practically: the Landauer limit — erasing one bit costs at least kT ln 2 ≈ 2.9 × 10⁻²¹ J at room temperature. A 1 Tbps link processing 10¹² bits per second would dissipate at least 2.9 nW — we are nowhere near this limit; current transceivers dissipate picojoules per bit, a million times above Landauer. The implication: there is enormous room for improvement in energy efficiency before we hit fundamental physical limits.

### Lecture Notes

THz communications sit at the intersection of electronics and photonics. Below ~300 GHz, we can generate signals electronically (frequency multipliers, harmonic oscillators). Above ~1 THz, we use photonic techniques (quantum cascade lasers, photomixers that beat two laser frequencies on a photodetector). The "THz gap" (0.3-3 THz) was historically difficult because it's too high for electronics and too low for efficient photonics. In 2040, the gap is closing: graphene-based plasmonic devices and resonant tunneling diodes (RTDs) operate at room temperature at 1-2 THz, with output powers of ~1 mW — enough for short-range communication.

Quantum communication is not a replacement for classical communication — it's a complement. Quantum channels are too low-bandwidth (kbps to Mbps) and too fragile (lossy, no amplification) for bulk data transfer. Their unique value is security: distributing encryption keys with information-theoretic security guarantees. The 2040 hybrid architecture runs classical 400 Gbps channels for data and parallel quantum channels for key distribution on the same fiber (using separate wavelengths — typically 1550 nm for classical and 1310 nm for quantum to avoid Raman scattering crosstalk). MACsec encrypts the classical data with keys refreshed every few seconds by QKD — achieving "perfect forward secrecy" where compromise of today's keys doesn't reveal yesterday's traffic.

Neuromorphic signal processing represents a paradigm shift from "compute everything, all the time" to "compute only when and where information exists." A traditional DSP pipeline computes every FFT, every equalizer tap, every decoder iteration on a rigid clock cycle. A spiking neural network (SNN) fires neurons only when their inputs change. For a communication system that's idle 90% of the time (typical for IoT, intermittent sensing), the SNN approach can reduce energy per bit by 100-1000×. The Bifrǫst Synapse ASIC, taped out in 2039 on Samsung 2 nm, achieves 10 fJ per synaptic operation — approaching biological efficiency (∼10 fJ per synaptic event in the brain). It runs a complete OFDM receiver — synchronization, channel estimation, equalization, and LDPC decoding — as a single SNN, consuming 50 mW for a 100 MHz bandwidth. That's 1/20th the power of the equivalent DSP ASIC.

### Required Reading

- Akyildiz, I.F. et al. (2038). "Terahertz Band Communications: The Last Frontier." *IEEE JSAC*, 56(9), 1621-1642.
- Gisin, N. et al. (2002). "Quantum Cryptography." *Reviews of Modern Physics*, 74(1), 145-195. (Still the best introduction — the physics hasn't changed.)
- Davies, M. et al. (2038). "Loihi 3: A Neuromorphic Manycore Processor with On-Chip Learning." *IEEE Micro*, 58(2), 82-99.
- UoY Vision Paper: "The Post-Shannon University — Communications Research 2040-2070." (Mesh Academic Portal)

### Discussion Questions

1. Terahertz communication promises terabit-per-second wireless links but can't penetrate walls or rain. Is this a feature (spatial reuse, security) or a fatal flaw? What applications justify THz's limitations?
2. Quantum key distribution guarantees security based on physics, not computational assumptions. But it requires dedicated hardware and has limited range. Should we build a quantum internet, or is post-quantum classical cryptography sufficient?
3. Neuromorphic chips approach the brain's energy efficiency. If a neuromorphic receiver uses 1/100th the power of a classical DSP receiver but occasionally makes different decoding decisions, is it "the same" communication system? Who's responsible when a spike-based decoder makes a mistake?

---

## Final Examination Preparation

### Exam Format

The CN103 final examination is a 3-hour closed-book assessment comprising:

**Part A — Theory (40%)**: 6 short-answer questions (choose 4), each requiring mathematical derivations or concise explanations. Topics drawn from Lectures 1-6.

**Part B — Design & Analysis (40%)**: 3 scenario-based problems (choose 2), each requiring link budget calculation, modulation/coding selection, and design justification. Topics drawn from Lectures 4-11.

**Part C — Frontier Essay (20%)**: 1 essay from a choice of 3 prompts, connecting course fundamentals to the 2040 frontiers covered in Lecture 12. Minimum 800 words.

### Sample Essay Questions (Part C practice)

1. Shannon's 1948 paper established the mathematical framework for all communication since. Yet 2040 systems increasingly use neural networks whose behavior Shannon's theory cannot fully characterize. Is the Shannon framework still sufficient to understand modern communications, or do we need a new theoretical foundation for learning-based systems?

2. The physical layer has progressed from copper to fiber to free-space optics to quantum channels, each exploiting different physics. What physical phenomena remain unexploited for communication? Consider gravitational waves, neutrino beams, and dark matter — are these practical communication media, or will we always be constrained to electromagnetic interactions?

3. Semantic communication transmits meaning rather than bits, challenging the Shannon model that treats information as independent of its interpretation. If an AI compresses my words into a semantic representation that another AI reconstructs into different but equivalent words, have I communicated? What does it mean for a communication system to preserve "meaning" across a channel?

### Practice Problem Set

1. **Link Budget:** Design a 10 km, 100 Gbps point-to-point wireless link in the 60 GHz band. Given: transmit power +20 dBm, transmit antenna gain 30 dBi, receive antenna gain 30 dBi, receiver sensitivity −60 dBm for 64-QAM at BER 10⁻⁶. Calculate the link margin. If atmospheric attenuation at 60 GHz is 15 dB/km, is the link feasible? If not, what changes would you make?

2. **OFDM Design:** You need an OFDM system with 20 MHz bandwidth, 15 kHz subcarrier spacing, and a cyclic prefix that handles multipath delay spread up to 5 µs. Calculate: (a) the number of subcarriers, (b) the OFDM symbol duration (without CP), (c) the cyclic prefix duration needed, (d) the overhead percentage, (e) the raw data rate if using 256-QAM (8 bits/symbol) with rate-3/4 LDPC coding, assuming 10% of subcarriers are pilots.

3. **CRC Analysis:** A system uses CRC-16-CCITT (generator polynomial x¹⁶ + x¹² + x⁵ + 1). (a) What is the maximum length burst error that is guaranteed to be detected? (b) If the bit error rate is 10⁻⁶ and frames are 1500 bytes, what is the probability of an undetected error? (c) Is this acceptable for a system requiring 99.999% reliability?

4. **Constellation Design:** Given a channel with SNR = 24 dB and bandwidth = 100 MHz, use Shannon's theorem to calculate the theoretical maximum data rate. If you want to achieve 80% of this capacity, what modulation order (QPSK, 16-QAM, 64-QAM, 256-QAM) is theoretically sufficient? What practical considerations might force you to use a lower order?

5. **LDPC Simulation:** Write a Python script to simulate a (1024, 512) regular LDPC code over an AWGN channel. Plot BER vs. Eb/N0 from 0 to 6 dB. At what Eb/N0 does the code achieve BER = 10⁻⁴? Compare to the uncoded BPSK curve. (Students should run this in the Valhalla Network Lab's simulation environment.)

---

## Course Assignments

### Assignment 1: Signal Analysis & Measurement

**Type:** Technical Analysis
**Objective:** Characterize real-world signals using laboratory equipment.

**Task:** Using the Valhalla Network Lab's oscilloscopes and spectrum analyzers, capture and analyze three signals: (a) a 10 MHz Ethernet (10BASE-T) signal, (b) a 2.4 GHz WiFi (802.11be) signal, (c) a 1550 nm optical signal. For each: measure amplitude, frequency/bandwidth, rise time, and eye diagram parameters. Write a report comparing theoretical predictions with measurements and explaining discrepancies.

**Deliverables:** Lab report with oscilloscope/spectrum analyzer screenshots, measurements table, and discrepancy analysis (1500-2000 words).

**Grading Rubric:** Measurement accuracy (25%), analysis depth (30%), discrepancy explanation (25%), report quality (20%).

**Due:** End of Week 4.

---

### Assignment 2: Modulation Design & Simulation

**Type:** Design & Simulation
**Objective:** Design and simulate a digital modulation scheme.

**Task:** Design a modulation scheme for a specified scenario (assigned individually: satellite link, underwater acoustic, indoor THz, orbital laser, or IoT LoRa-like). Simulate in Python (using NumPy/SciPy): generate random data, modulate, add channel impairments (noise, attenuation, multipath), demodulate, and measure BER. Compare at least two modulation schemes for your scenario. Produce constellation diagrams and BER curves.

**Deliverables:** Python code, simulation report with BER curves and constellation diagrams (1500-2000 words), and a 5-minute recorded presentation.

**Grading Rubric:** Simulation correctness (30%), modulation scheme comparison (25%), analysis quality (25%), presentation clarity (20%).

**Due:** End of Week 8.

---

### Assignment 3: SDR Transceiver Implementation

**Type:** Implementation & Measurement
**Objective:** Build a working OFDM transceiver on SDR hardware.

**Task:** On the Bifrǫst SDR Platform, implement an OFDM transceiver: transmitter chain (scrambler → LDPC encoder → QAM mapper → OFDM framer → IFFT → CP insertion) and receiver chain (synchronization → FFT → channel estimation → equalization → demapper → LDPC decoder → descrambler). Transmit real data over-the-air (2.4 GHz ISM band, low power, lab license). Measure: packet error rate vs. distance, constellation diagrams at different SNRs, and throughput.

**Deliverables:** SDR code, measurement report with PER curves and constellation plots (2000-2500 words), and a live demonstration in lab.

**Grading Rubric:** Implementation completeness (35%), measurement quality (25%), analysis (20%), demonstration (20%).

**Due:** End of Week 12.

---

### Assignment 4: Frontier Research Paper

**Type:** Research & Synthesis
**Objective:** Investigate a 2040 frontier topic in depth.

**Task:** Choose one frontier topic (terahertz communications, quantum communications, neuromorphic signal processing, or semantic communication) and write a critical literature review. Survey at least 8 sources from 2035-2040. Analyze: (a) the current state of the art, (b) the key technical challenges, (c) competing approaches and their tradeoffs, (d) your prediction for commercial deployment timeline, (e) implications for network architecture.

**Deliverables:** Research paper (2500-3000 words), properly cited (IEEE format), with at least one original analysis (e.g., link budget calculation, complexity comparison, or simulation).

**Grading Rubric:** Literature coverage (25%), technical depth (30%), critical analysis (25%), writing quality (20%).

**Due:** End of Week 15.

---

### Assignment 5: Comprehensive System Design

**Type:** Capstone Design
**Objective:** Integrate all course concepts in an end-to-end communication system design.

**Task:** Design a complete physical layer for a specified 2040 scenario (e.g., Arctic research station satellite link, deep-sea sensor network, lunar surface mesh, or in-body nanonetwork). Your design must specify: transmission medium, modulation scheme, line coding, multiplexing strategy, error detection/correction codes, link budget, and synchronization approach. Justify every choice with quantitative analysis. Include a failure mode analysis.

**Deliverables:** System design document (3000-4000 words), link budget spreadsheet, and a 10-minute recorded design review presentation.

**Grading Rubric:** Design completeness (25%), quantitative justification (25%), integration of course concepts (25%), failure analysis (15%), presentation (10%).

**Due:** End of Week 16 (final exam period).
