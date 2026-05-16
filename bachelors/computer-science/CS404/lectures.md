# CS404: Neuromorphic & Edge Computing
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4  
**Prerequisites:** CS205 (Computer Architecture), CS302 (Parallel & Distributed Systems)  
**Description:** Spiking neural networks, neuromorphic chips (Intel Loihi, IBM TrueNorth), edge inference architectures, sensor fusion at the boundary, and the convergence of brain-inspired computing with resource-constrained deployment. This course bridges the synapse and the sensor — where silicon learns to think like a neuron at the edge of the network.

**Norse Framing:** The Hraesvelgr sits at the edge of the world, a giant in eagle form whose wingbeats stir the winds of all realms. Edge computing, likewise, processes at the boundary — sensing, computing, deciding — without needing to fly back to the cloud. Neuromorphic engineering is the carving of runes into silicon so that the chip itself remembers and adapts.

---

## Lectures

ᚠ **Lecture 1: The Edge of the World — Why Compute at the Boundary?**

**Course:** CS404 — Neuromorphic & Edge Computing  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

We begin at the boundary. Edge computing is the practice of processing data near its source — on the device, at the sensor, in the factory, on the drone — rather than shipping raw bytes to a distant data centre. By 2040, the edge-cloud continuum is the dominant computing paradigm: trillions of IoT devices generate zettabytes of sensor data annually, and shipping all of it to the cloud is economically, energetically, and physically impossible. This lecture frames why the edge matters, what constraints define it, and how the old Norse metaphor of the boundary — the *útgarðr*, the wild outer realm — illuminates the technical challenges of partial connectivity, intermittent power, and hostile environments.

### Key Concepts

- **The bandwidth wall:** Global IP traffic exceeded 5 zettabytes/year by 2025. At current growth rates, centralised cloud processing cannot absorb all sensor data. Edge computing performs *filtering, aggregation, and inference* locally — transmitting only semantically meaningful events.
- **Latency physics:** Light travels ~200 km/ms in fibre. A self-driving car at highway speed covers 1.5 metres in 10 ms. Safety-critical decisions (braking, obstacle avoidance) must close the sense-act loop within single-digit milliseconds — impossible if every frame travels to a cloud data centre and back.
- **Energy proportionality:** Transmitting 1 KB over a cellular link consumes roughly the same energy as 50,000 CPU instructions. For battery-powered sensors, local inference is often *cheaper* than transmission.
- **The privacy boundary:** Processing health data, home audio, or industrial telemetry locally keeps sensitive information within the user's domain. This aligns with the Norse concept of *heimr* — the protected inner space — versus the exposed outer realm.
- **The 2040 landscape:** Edge-native operating systems (ÆgirOS, FenrirRT), 5G/6G private networks, satellite IoT constellations, and neural processing units in every smartphone have made edge computing the default architecture for all new sensor-driven applications.

### Required Reading

- Satyanarayanan, M. "The Emergence of Edge Computing." *IEEE Computer*, 2017. (The foundational manifesto — still cited in 2040.)
- Shi, W. et al. "Edge Computing: Vision and Challenges." *IEEE Internet of Things Journal*, 2016.
- University of Yggdrasil Edge Lab Technical Report 01: *Útgarðr: A Taxonomy of Edge Deployment Archetypes* (2039).

### Discussion Questions

1. Is the edge-cloud continuum a temporary architectural compromise, or a fundamental rebalancing of where computation belongs?
2. Consider a wildlife tracking collar in the Norwegian highlands: what specific edge processing would you perform before satellite transmission, and why?
3. How does the privacy argument for edge computing interact with the Norse Heathen concept of *frith* (sacred peace within a bounded community)?

### Practice Problems

- Calculate the minimum edge inference latency required for a drone travelling at 30 m/s to detect and avoid an obstacle appearing 15 metres ahead. Account for sensor capture, neural network inference, and actuator response.
- Estimate the energy budget for a solar-powered soil moisture sensor that must operate through a Scandinavian winter. Determine whether local inference or raw data transmission is more sustainable.

---

ᚢ **Lecture 2: The Neuron in Silicon — Principles of Neuromorphic Engineering**

**Course:** CS404 — Neuromorphic & Edge Computing  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Neuromorphic computing is not merely "neural networks on a chip" — it is a fundamentally different approach to computation, inspired by the brain's architecture rather than its abstracted mathematics. Where a GPU multiplies matrices in lockstep, a neuromorphic chip pulses spikes asynchronously across a reconfigurable synaptic fabric. This lecture introduces the biological neuron as a computational primitive, the Leaky Integrate-and-Fire (LIF) model, spike-timing-dependent plasticity (STDP), and the deep conceptual shift from von Neumann architectures to event-driven, sparse, temporally coded computation.

### Key Concepts

- **The biological neuron as a computational model:** A neuron integrates incoming charge on its membrane; when the potential crosses a threshold, it fires a spike down its axon to connected neurons, then resets. This *spike* is the fundamental unit of information — not a floating-point number, but a precisely timed electrical event.
- **Leaky Integrate-and-Fire (LIF) model:** The canonical abstraction. Membrane potential *V(t)* evolves according to τ_m · dV/dt = -(V - V_rest) + R_m · I_syn(t). When V ≥ V_thresh, a spike is emitted and V resets. The "leak" term models the passive diffusion of ions across the membrane — without input, the neuron returns to rest.
- **Spike-Timing-Dependent Plasticity (STDP):** The biological learning rule. If a pre-synaptic spike arrives *just before* a post-synaptic spike fires, the synapse strengthens (LTP — long-term potentiation). If pre follows post, the synapse weakens (LTD). The STDP window is typically ~20-40 ms wide, a timescale that neuromorphic chips must honour in hardware.
- **Asynchronous event-driven computation:** Unlike synchronous clocked logic, a neuromorphic core processes events only when spikes arrive. This yields *massive* energy efficiency for sparse, real-world signals — the chip is quiescent between events, consuming only leakage current.
- **Carver Mead's vision (1989):** The Caltech physicist who coined "neuromorphic" argued that silicon could model ion channels directly using sub-threshold transistor physics. His early analogue VLSI cochlea and retina chips demonstrated orders-of-magnitude energy advantages over digital DSP — a principle rediscovered by the 2040 generation.

### Required Reading

- Mead, C. *Analog VLSI and Neural Systems.* Addison-Wesley, 1989. (Chapters 1-4.)
- Gerstner, W. et al. *Neuronal Dynamics: From Single Neurons to Networks and Models of Cognition.* Cambridge, 2014. Sections on LIF and STDP.
- Indiveri, G. and Liu, S.-C. "Memory and Information Processing in Neuromorphic Systems." *Proceedings of the IEEE*, 2015.

### Discussion Questions

1. How does the energy profile of a spiking neural network differ from a comparable artificial neural network running on GPU? Where does the advantage come from?
2. STDP is a *local* learning rule — each synapse adjusts based only on the two neurons it connects. Contrast this with backpropagation's global error signal. What are the implications for on-chip learning?
3. If the LIF model is a first-order approximation of a real neuron, what second-order effects matter for practical neuromorphic computation?

### Practice Problems

- Implement a single LIF neuron in Python. Drive it with a Poisson-distributed spike train at 20 Hz. Plot membrane potential over time and identify the firing rate.
- Simulate a pair of LIF neurons connected by a synapse undergoing STDP. Vary the relative timing of pre- and post-synaptic spikes and plot the resulting weight change curve.

---

ᚦ **Lecture 3: Intel Loihi — Architecture of a Production Neuromorphic Processor**

**Course:** CS404 — Neuromorphic & Edge Computing  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Intel's Loihi, first unveiled in 2017 and reaching its third generation (Loihi 3 "Yggdrasil") by 2038, is the most widely deployed neuromorphic research and production platform. This lecture dissects Loihi's architecture in detail: the neurocore microarchitecture, the Network-on-Chip (NoC) fabric, the x86 Lakemont companion cores for host interaction, and the Lakemont-to-neurocore programming model. Students completing this lecture should be able to explain how a spike travels from one neurocore to another across the mesh, how synaptic weights are stored and decayed, and how Loihi achieves its ~10 pJ per synaptic operation energy envelope.

### Key Concepts

- **Neurocore microarchitecture (Loihi 2):** Each neurocore contains 1,024 spiking neuron compartments, 128 KB of SRAM for synaptic state, and a programmable learning engine. Neurons are not simple LIF units — Loihi supports a *programmable* neuron model with configurable membrane dynamics, dendritic compartments, and stochastic thresholds.
- **The Network-on-Chip (NoC) mesh:** Loihi 2's 128 neurocores are arranged in an 8×16 2D mesh. Spikes are routed as *graded packets* — not destination-addressed, but broadcast through a spanning tree with fan-out determined by synaptic connectivity. This is neuromorphic routing: efficient for sparse, many-to-many connectivity.
- **Lakemont x86 cores:** Each Loihi 2 chip includes six Lakemont cores running a real-time OS (FenrirRT by 2040). These handle chip management, spike encoding/decoding, and off-chip communication. The programmer writes host code on the Lakemont cores and neurocore code in the Lava framework.
- **The Lava software framework:** Intel's open-source neuromorphic programming environment (Python-based). Lava provides a *process-library* abstraction: neurons, synapses, learning rules, and input/output encoders are composable processes connected by channels. Loihi 3 adds a direct PyTorch integration layer called *Bifröst Bridge*.
- **Energy numbers:** Loihi 2 achieves ~10 pJ per synaptic operation (SOP) in typical workloads, compared to ~50-100 pJ for equivalent operations on GPU. For sparse spiking workloads (olfactory classification, gesture recognition), the advantage can reach 1,000× due to event-driven quiescence.
- **Loihi 3 "Yggdrasil" (2038):** 512 neurocores, 3D-stacked with HBM, on-chip STDP and reward-modulated learning, integrated 6G IoT radio for direct edge deployment. The chip that powers the University of Yggdrasil's *Huginn* sensor satellite.

### Required Reading

- Davies, M. et al. "Loihi: A Neuromorphic Manycore Processor with On-Chip Learning." *IEEE Micro*, 2018.
- Intel Labs. *Loihi 2 Technical Brief.* 2021.
- Orchard, G. et al. "Efficient Neuromorphic Signal Processing with Loihi 2." *Nature Machine Intelligence*, 2035.

### Discussion Questions

1. The NoC mesh broadcasts spikes as graded packets rather than routing them with destination addresses. What are the trade-offs of this approach — when does it win, and when does it break down?
2. Loihi's programmable neuron model allows users to define their own membrane dynamics. Why is this necessary beyond the standard LIF? Give a concrete use case.
3. Compare Loihi's on-chip STDP to GPU-based backpropagation for an edge deployment with intermittent connectivity. Which learning approach is more practical, and why?

### Practice Problems

- Write a Lava process that implements a winner-take-all (WTA) network of 100 LIF neurons on a single Loihi 2 neurocore. Measure the total energy consumed per classification decision.
- Design a spike-encoding scheme for a continuous-valued temperature sensor reading (range -40°C to 85°C) suitable for processing on Loihi. Justify your encoding rate and precision.

---

ᚬ **Lecture 4: Spike Encoding and Temporal Coding — How Information Lives in Time**

**Course:** CS404 — Neuromorphic & Edge Computing  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

A digital image is an array of pixels. A spike train is a sequence of precisely timed events. The bridge between these two representations — *spike encoding* — is one of the most creative and consequential design decisions in neuromorphic systems. This lecture surveys the major encoding schemes: rate coding, temporal coding, population coding, rank-order coding, and the emerging *phase coding* that exploits the theta-gamma rhythms discovered in biological hippocampus. We explore the Shannon information capacity of spike trains, the trade-off between temporal precision and robustness to jitter, and the implications for edge sensor design.

### Key Concepts

- **Rate coding:** The classic scheme. A neuron's firing rate (spikes/second) encodes the stimulus intensity. Simple and robust — but slow. To distinguish 256 intensity levels at 10% precision, a rate code needs ~100 ms of integration time. For a drone dodging a tree, that is 3 metres of travel — unacceptable.
- **Temporal coding (Time-to-First-Spike):** The *latency* of the first spike after stimulus onset encodes the information. Faster than rate coding by the integration window. Precision depends on spike timing jitter, typically 1-5 ms on Loihi.
- **Population coding:** Many neurons encode the same stimulus, each with a slightly different tuning curve. The population vector decodes the stimulus from the collective activity. This is how the cricket's cercal system encodes wind direction — ~400 neurons, each tuned to a preferred angle, with population vector resolution of ~1°.
- **Rank-order coding:** The *order* in which neurons in a population fire encodes the stimulus. The earliest-spiking neuron carries the most information. Biologically plausible (retinal ganglion cells) and extremely efficient — the code is complete once every neuron has fired once.
- **Phase coding:** Neurons fire at specific phases of an underlying oscillatory rhythm. In the hippocampus, *place cells* fire at progressively earlier theta phases as the rat moves through the place field — a phenomenon called *phase precession*. Phase codes can multiplex multiple variables onto the same spike train. Loihi 3 supports on-chip theta oscillators for phase-referenced computation.
- **Information-theoretic bounds:** A Poisson spike train of duration T and mean rate r carries ~rT · log₂(1 + 1/(r·Δt)) bits, where Δt is the temporal precision. The practical takeaway: improving temporal precision from 10 ms to 1 ms roughly doubles the information capacity — if the downstream decoder can use it.

### Required Reading

- Rieke, F. et al. *Spikes: Exploring the Neural Code.* MIT Press, 1997. Chapters 1-3.
- Thorpe, S. "Spike-Based Strategies for Rapid Processing." *Neural Networks*, 2001.
- UoY Neuromorphic Lab Technical Report 04: *Phase Coding on Loihi 3: A Hippocampus-Inspired Architecture* (2040).

### Discussion Questions

1. If rate coding is too slow and temporal coding is fragile, what hybrid scheme would you design for a drone collision-avoidance system? Defend your choice.
2. Phase precession in the hippocampus allows a rat to encode spatial position at a resolution finer than the place field size. How might this principle be applied to an edge SLAM (Simultaneous Localisation and Mapping) system?
3. The information capacity of a spike train depends on temporal precision — but precision costs energy (low-jitter spike generation is power-hungry). Where is the optimal trade-off for a battery-powered edge device?

### Practice Problems

- Encode a 10-second segment of 16 kHz audio into spike trains using a bank of 64 gammatone filters, each feeding a LIF neuron with rate coding. Compute the spike rate per neuron and total spike count.
- Design a rank-order coding scheme for a 28×28 MNIST digit. How many input neurons are needed, and what is the information latency (time until all neurons have fired once)?

---

ᚱ **Lecture 5: IBM TrueNorth and the SyNAPSE Legacy**

**Course:** CS404 — Neuromorphic & Edge Computing  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Before Loihi, there was TrueNorth. IBM's DARPA SyNAPSE programme produced, in 2014, a chip of astonishing ambition: one million programmable neurons and 256 million configurable synapses on a 5.4-billion-transistor die, consuming 70 mW — roughly the power of a hearing aid battery. This lecture honours the architectural innovations of TrueNorth — its deterministic crossbar scheduler, its corelet programming model, its rigid but elegant separation of computation and communication — and traces its influence through to the 2040 generation of neurosynaptic processors. We also examine why TrueNorth commercially failed, and what lessons that failure teaches about the gap between research prototyping and production deployment.

### Key Concepts

- **TrueNorth's neurosynaptic core:** 256 axons (inputs) × 256 neurons (outputs) interconnected by a 256×256 crossbar of binary synapses. Every neuron has a configurable LIF model with 4 synaptic types (excitatory, inhibitory, reset, and leak). The core operates on a 1 kHz synchronous tick — radically different from Loihi's asynchronous spikes.
- **Deterministic many-core architecture:** TrueNorth's 4,096 cores are arranged in a 2D mesh. Communication is synchronous, time-multiplexed, and *deterministic by construction* — every spike arrives at its destination core in a fixed number of ticks. This makes TrueNorth programs formally verifiable. You can prove that a network never deadlocks.
- **The corelet programming model:** A corelet is an abstraction of a neurosynaptic network with typed input/output ports. Corelets compose hierarchically — a 1,024-neuron network built from 4-core sub-networks, each a corelet. IBM's Corelet Language was a Python DSL that compiled to TrueNorth's low-level configuration bitstream.
- **Energy and performance:** 46 billion synaptic operations per second per watt. A single TrueNorth chip at 70 mW could run a real-time 2,400 fps multi-object tracking pipeline that would consume ~200 W on a contemporary GPU. The trade-off: 1-bit synaptic weights (no graded learning) and fixed 1 kHz tick — no temporal dynamics faster than 1 ms.
- **Why TrueNorth didn't conquer the world:** Three reasons. (1) The programming model was alien — corelet composition required a mental model radically different from the sequential/TensorFlow paradigm developers knew. (2) 1-bit weights limited accuracy on deep networks. (3) IBM didn't open-source the toolchain until 2021, by which time the AI community had committed to GPU deep learning.
- **The TrueNorth legacy:** IBM's follow-on NorthPole chip (2023) adapted TrueNorth principles for server inference, achieving 25× energy improvement over GPU on ResNet-50. In 2040, NorthPole-derived accelerator tiles are standard in IBM Z-series mainframes for real-time fraud detection.

### Required Reading

- Merolla, P. et al. "A Million Spiking-Neuron Integrated Circuit with a Scalable Communication Network and Interface." *Science*, 2014.
- Cassidy, A.S. et al. "Cognitive Computing Building Block: A Versatile and Efficient Digital Neuron Model for Neurosynaptic Cores." *IJCNN*, 2013.
- Modha, D. "Introducing a Brain-Inspired Computer: TrueNorth's Neurons to Revolutionise System Architecture." IBM Research, 2014.

### Discussion Questions

1. TrueNorth's deterministic tick-based architecture makes it verifiable. Loihi's asynchronous event-driven architecture makes it energy-efficient. Is there a way to have both — determinism *and* sparsity? Propose an architecture.
2. The corelet hierarchical composition model was elegant but adoption was low. Compare this to Lava's process-library approach. Which is more likely to gain traction, and why?
3. NorthPole achieves GPU-class accuracy with neuromorphic energy efficiency. Is neuromorphic computing destined to remain a niche for extreme low-power edge, or will it challenge GPU dominance in the data centre?

### Practice Problems

- Implement a corelet (in Python, simulated) that performs a 4-neuron winner-take-all computation using lateral inhibition. Trace the spike timing for three different input patterns.
- Estimate the total energy consumed by a TrueNorth chip processing 100,000 MNIST images at 1,000 classifications/second. Compare to a contemporary edge GPU (e.g., NVIDIA Jetson Orin Nano at 7 W).

---

ᚲ **Lecture 6: Edge Inference — Running Neural Networks on Microcontrollers**

**Course:** CS404 — Neuromorphic & Edge Computing  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Not every edge device has a Loihi or a GPU. The vast majority of edge nodes — smart sensors, wearables, agricultural monitors, industrial vibration detectors — run on ARM Cortex-M microcontrollers with 256 KB of RAM and no floating-point unit. Running a neural network on such silicon requires a different set of skills: quantisation, pruning, operator fusion, and the art of fitting a model into a memory budget smaller than a single JPEG. This lecture covers TinyML — the discipline of machine learning on microcontrollers — and the toolchains that make it practical: TensorFlow Lite Micro, Edge Impulse, and the University of Yggdrasil's *MímirCore* framework.

### Key Concepts

- **Quantisation:** Converting 32-bit floating-point weights and activations to 8-bit integers (int8). A well-quantised model loses <1% accuracy while reducing memory by 4× and enabling integer-only inference. The key insight: neural networks are surprisingly robust to reduced precision because the training process already builds in redundancy.
- **Post-training quantisation (PTQ) vs. quantisation-aware training (QAT):** PTQ calibrates scaling factors after training — fast but can degrade accuracy on small models. QAT simulates quantisation during training — the model learns to compensate — at the cost of longer training. For microcontrollers with <256 KB RAM, QAT is usually necessary to stay above 90% of floating-point accuracy.
- **Pruning and sparsity:** Removing weights with magnitude below a threshold. Structured pruning (removing entire channels or filters) improves speed on hardware; unstructured pruning (individual weights) improves memory but requires sparse computation support. The ARM Ethos-U55 NPU supports structured sparsity natively.
- **Operator fusion:** Combining adjacent layers (e.g., convolution + batch-normalisation + ReLU) into a single fused kernel eliminates intermediate memory buffers and reduces latency. For a 3-layer fused block, this can reduce RAM usage by 40%.
- **TinyML hardware landscape (2040):** ARM Cortex-M85 with Helium vector extensions, Ethos-U65 NPU with 0.5 TOPS at 100 mW, GreenWaves GAP9 for ultra-low-power audio, and the RISC-V based *Urd* microcontroller designed here at UoY with native 4-bit spiking support.
- **The 256 KB challenge:** A full MobileNetV2 is ~3.5 MB. After QAT, structured pruning (50% channels), and operator fusion, it fits in 240 KB with 92% of original accuracy. This is the "Mímir Squeeze" — the research area pioneered by the UoY TinyML group.

### Required Reading

- Warden, P. and Situnayake, D. *TinyML: Machine Learning with TensorFlow Lite on Arduino and Ultra-Low-Power Microcontrollers.* O'Reilly, 2019.
- Jacob, B. et al. "Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference." *CVPR*, 2018.
- UoY TinyML Lab. *MímirCore: A RISC-V Toolchain for 4-bit Spiking Inference.* Technical Report, 2040.

### Discussion Questions

1. Quantisation is lossy compression. What classes of neural network architectures are most fragile under quantisation, and why?
2. Operator fusion reduces memory but can increase code size due to specialised kernels. On a device where both RAM and flash are scarce, how do you decide what to fuse?
3. The ARM Ethos-U65 delivers 0.5 TOPS at 100 mW. Compare this to Loihi 2's energy efficiency. When would you choose one over the other?

### Practice Problems

- Take a pre-trained MobileNetV2 in TensorFlow and apply post-training int8 quantisation using TFLite. Measure the accuracy change on a 1,000-image validation set.
- Profile the memory usage (ROM, RAM, peak activation memory) of a 3-layer CNN before and after operator fusion. Use the MímirCore simulator.

---

ᚷ **Lecture 7: Sensor Fusion at the Edge — Combining Modalities Under Constraint**

**Course:** CS404 — Neuromorphic & Edge Computing  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

A self-driving car sees with cameras, hears with radar, feels with ultrasonic pulses, and orients with IMU and GPS. A wearable health monitor fuses PPG (photoplethysmography), ECG, accelerometer, and skin temperature. An autonomous underwater vehicle navigating a kelp forest combines sonar, depth, and optical flow. None of these sensors is perfect alone — cameras fail in fog, radar struggles with stationary objects, PPG is ruined by motion artefacts. *Sensor fusion* is the mathematics of combining imperfect, asynchronous, heterogeneous measurements into a coherent world state — and doing it within the power and latency budget of an edge device. This lecture covers Kalman filters, complementary filters, attention-based fusion networks, and the emerging field of *neuromorphic fusion* where spike-encoded sensor streams are integrated on-chip.

### Key Concepts

- **The Kalman filter:** The workhorse of sensor fusion since 1960. A recursive Bayesian estimator: predict the next state from a dynamics model, then update with a noisy measurement weighted by the Kalman gain. The equations are compact — five lines of linear algebra — but the assumptions (linear dynamics, Gaussian noise, known covariances) are brittle. Extensions: Extended KF (EKF) for non-linear dynamics, Unscented KF (UKF) for non-Gaussian uncertainty, particle filters for multi-modal distributions.
- **Complementary filters for IMU:** Accelerometers measure orientation from gravity but are noisy at high frequency; gyroscopes integrate angular velocity but drift at low frequency. A complementary filter fuses them: high-pass the gyro integration, low-pass the accelerometer measurement, add them together. This is the magic that keeps a quadcopter stable — simple enough to run on an 8-bit microcontroller, robust enough for aerobatics.
- **Deep sensor fusion:** A neural network that ingests raw or lightly processed data from multiple sensors and learns to produce a fused representation. Architectures: early fusion (concatenate sensor features at input), late fusion (process each sensor through separate encoders, then fuse at the decision layer), and *cross-attention fusion* where each modality attends to the others at each layer — expensive but state-of-the-art for autonomous driving in 2040.
- **Neuromorphic fusion:** Both Intel and IBM have demonstrated spike-based sensor fusion — event cameras (DVS) providing visual spikes, neuromorphic cochleae providing audio spikes, both fed directly into a Loihi or TrueNorth chip without digital conversion. The chip performs spatio-temporal pattern recognition on the fused spike stream. Latency from photon/sound-wave to classification decision: < 5 ms.
- **The edge-specific challenge:** A Kalman filter on a Cortex-M4 needs ~2 KB of RAM. A cross-attention fusion transformer needs 200 MB. The edge fusion engineer's job is to find the Pareto-optimal point on the accuracy-vs-resource curve for each deployment.

### Required Reading

- Kalman, R.E. "A New Approach to Linear Filtering and Prediction Problems." *Journal of Basic Engineering*, 1960. (Yes, still assigned — it's only 13 pages, and it changed the world.)
- Thrun, S., Burgard, W., and Fox, D. *Probabilistic Robotics.* MIT Press, 2005. Chapters on Kalman and particle filters.
- Gallego, G. et al. "Event-Based Vision: A Survey." *IEEE TPAMI*, 2020. (Event cameras as spike sources.)

### Discussion Questions

1. The Kalman filter assumes Gaussian noise. When is this assumption violated in real sensor data, and what breaks when it is?
2. Compare early fusion, late fusion, and cross-attention fusion for a drone with camera + LiDAR + IMU. Which would you deploy on a Cortex-M85 with 512 KB RAM, and why?
3. Neuromorphic fusion's 5 ms latency is compelling for autonomous driving. What are the barriers to deploying neuromorphic sensor fusion in production vehicles in 2040?

### Practice Problems

- Implement a 1D Kalman filter in Python to fuse a noisy GPS position measurement (σ=5m, once per second) with an IMU velocity estimate (σ=0.1 m/s, 100 Hz). Plot the state estimate and covariance over 60 seconds.
- Design a complementary filter for a drone's roll angle, fusing a gyroscope (1000 Hz, drift 0.01°/s) with an accelerometer (100 Hz, noise 0.5°). Specify the crossover frequency and explain your choice.

---

ᚹ **Lecture 8: On-Device Learning — When the Edge Must Adapt**

**Course:** CS404 — Neuromorphic & Edge Computing  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Inference at the edge is common; *learning* at the edge is the frontier. A wildlife classifier deployed in the Amazon must adapt as new species are discovered. A predictive maintenance model on a wind turbine must learn the specific vibrational signature of *this particular turbine's* gearbox as it ages. Shipping data back to the cloud for retraining is often impossible — no connectivity, too much data, or privacy constraints. This lecture covers the techniques that make on-device learning practical: transfer learning with frozen backbones, federated averaging, meta-learning for few-shot adaptation, and the unique capability of neuromorphic chips to learn *continuously* without catastrophic forgetting.

### Key Concepts

- **Transfer learning at the edge:** Keep the feature extractor (backbone) frozen — its 5 million weights were trained on massive cloud datasets. Train only a small classifier head (a few thousand parameters) on the device. The forward pass runs normally; the backward pass only computes gradients for the head. Works on microcontrollers with <100 KB of additional RAM for training state.
- **Federated learning:** Many edge devices train local models on their private data. A central server aggregates only the *model updates* (gradients or weights), never the raw data. The Federated Averaging (FedAvg) algorithm: each device runs SGD locally for a few epochs, sends the weight delta to the server, which averages all deltas and broadcasts the updated global model. Privacy-preserving by design, but assumes devices are cooperative and not adversarial.
- **Catastrophic forgetting:** When a neural network trained on task A is then trained on task B, its performance on task A plummets. This is the central obstacle to continuous on-device learning. Mitigations: Elastic Weight Consolidation (EWC) — penalise changes to weights that are important for previous tasks; replay buffers — interleave old examples with new ones; and progressive networks — freeze old columns, add new columns for new tasks.
- **Neuromorphic continuous learning:** Loihi's on-chip STDP is inherently local and continuous — it doesn't have a "training phase" distinct from "inference." The chip learns as spikes flow, adapting synaptic weights incrementally. Early results show that STDP-based neuromorphic networks experience *less* catastrophic forgetting than backprop-trained ANNs, because weight changes are local and gradual rather than global and coordinated.
- **Few-shot and meta-learning:** Model-Agnostic Meta-Learning (MAML) trains a model to be *easy to fine-tune* — the initial weights are optimised such that one or a few gradient steps on a new task produce good performance. MAML's inner loop (the few-shot adaptation) is lightweight enough to run on an edge device; only the outer loop (learning how to learn) needs cloud-scale compute.
- **The 2040 landscape:** Loihi 3 supports fully on-chip continual learning with EWC-inspired synaptic consolidation. The *MímirCore* framework provides a federated learning API for RISC-V microcontrollers. And the UoY Neuromorphic Lab's *Jörmungandr* system (2039) demonstrated a snake-like inspection robot that learned to recognise new pipe corrosion patterns in the field using Loihi 3 + few-shot meta-learning, without any cloud connection for 6 months.

### Required Reading

- McMahan, B. et al. "Communication-Efficient Learning of Deep Networks from Decentralized Data." *AISTATS*, 2017. (The FedAvg paper.)
- Kirkpatrick, J. et al. "Overcoming Catastrophic Forgetting in Neural Networks." *PNAS*, 2017. (Elastic Weight Consolidation.)
- Finn, C., Abbeel, P., and Levine, S. "Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks." *ICML*, 2017.
- UoY Jörmungandr Project. *Six Months of Autonomous Learning in Industrial Environments.* Technical Report, 2039.

### Discussion Questions

1. Federated learning assumes clients are honest. What attacks can a malicious client mount, and how can the server defend against them?
2. Neuromorphic chips appear resistant to catastrophic forgetting. Is this a fundamental advantage of local learning rules, or can backprop-based systems achieve the same with enough engineering?
3. A Jörmungandr robot learns to recognise 47 pipe corrosion patterns over 6 months of autonomous operation. Design a protocol to verify that it hasn't forgotten pattern #3 while learning pattern #47.

### Practice Problems

- Implement a simple federated averaging simulation in Python: 10 clients, each with non-IID data, training a small CNN. Plot the global model's accuracy over 100 communication rounds.
- Simulate catastrophic forgetting: train a 3-layer MLP on MNIST digit classification (0-4), then on digits (5-9). Measure accuracy on the original task before and after fine-tuning, with and without EWC.

---

ᚺ **Lecture 9: Energy-Harvesting Edge — Computing Without a Plug**

**Course:** CS404 — Neuromorphic & Edge Computing  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Some edge devices have no battery. No solar panel. No reliable power of any kind. They harvest energy from their environment — a piezoelectric strip on a vibrating motor, a thermoelectric generator on a hot pipe, a tiny RF rectenna capturing ambient WiFi — and must compute *between* energy bursts, saving state before the capacitor drains. This is *intermittent computing*, and it demands a radical rethinking of program execution: checkpointing at the instruction level, non-volatile processors, and the art of making progress one microjoule at a time. This lecture covers energy-harvesting hardware, intermittent computing models, and the surprising fit between neuromorphic event-driven execution and energy-intermittent environments.

### Key Concepts

- **Energy-harvesting sources:** Thermoelectric generators (TEGs) produce ~10-100 μW/cm² from a 5-20°C gradient. Indoor photovoltaic cells yield ~10 μW/cm² under office lighting. Piezoelectric harvesters capture ~100 μW from industrial vibration. RF harvesters capture nanowatts to microwatts from ambient radio — enough to wake a sensor, take a reading, and transmit a packet once per minute.
- **Intermittent computing model:** The device powers on when the energy buffer (capacitor or supercapacitor) reaches a threshold voltage, executes for a few milliseconds to seconds until the buffer drops below a brownout threshold, then powers off — losing all volatile state. Progress is made through *checkpoints*: the program periodically saves its state to non-volatile memory (FRAM or MRAM). On reboot, it restores the checkpoint and resumes.
- **Task-based intermittent execution:** Rather than checkpointing arbitrary program state, the programmer decomposes work into idempotent *tasks* with explicit inputs, outputs, and commit points. The *InK* (Intermittent Kernel) and *Chain* task-based systems pioneered this model. A task either completes entirely (atomically from the energy perspective) or rolls back — no partial execution.
- **Non-volatile processors (NVPs):** A processor whose flip-flops and SRAM are backed by ferroelectric or magnetic tunnel junctions, allowing instant state preservation on power loss and instant restore on power-up. ARM's *NVP* prototype (2025) and the commercial RISC-V based *Urd-NV* (UoY, 2040) make intermittent computing transparent to the programmer — but at a 20-30% area and energy overhead compared to volatile logic.
- **Neuromorphic + intermittent = natural allies:** Neuromorphic event-driven execution is inherently interruptible at the spike boundary. A Loihi 2 core can save its membrane potentials and synaptic weights to on-chip NVM in ~2 μs — fast enough to complete before the capacitor drains. The UoY *Sólarsteinn* project (2040) demonstrated a Loihi 3 chip powered entirely by indoor light, running a continuous gesture-recognition network for 18 months without a battery.
- **The Sólarsteinn architecture:** A 2 cm² indoor photovoltaic cell charges a 100 μF supercapacitor. When voltage reaches 3.3 V, the Loihi core wakes, processes up to 25 spikes (~500 μJ total per wake cycle), writes state to FRAM, and sleeps. When the next gesture occurs, event-camera spikes arrive and the cycle repeats. Average power consumption: 4.7 μW.

### Required Reading

- Lucia, B. et al. "A Simpler, Safer Programming and Execution Model for Intermittent Systems." *PLDI*, 2015. (The Chain task-based model.)
- Ma, K. et al. "Architecture Exploration for Ambient Energy Harvesting Nonvolatile Processors." *HPCA*, 2015.
- UoY Sólarsteinn Project. *Battery-Free Neuromorphic Computing: 18 Months of Continuous Operation.* Technical Report, 2040.

### Discussion Questions

1. Compare checkpoint-based and task-based intermittent computing. Which is more suitable for a neuromorphic chip, and why?
2. A non-volatile processor eliminates the need for software checkpointing — but costs 20-30% in energy overhead. For a device that browns out every 50 ms, does the NVP overhead pay for itself? Quantify your answer.
3. The Sólarsteinn project ran for 18 months without a battery. What are the environmental and sustainability implications of battery-free edge computing at scale?

### Practice Problems

- Calculate the minimum supercapacitor size needed to power a Loihi 2 core (20 mW active, 50 μW sleep) through a 10 ms spike-processing burst, given a supply voltage range of 3.3 V down to 2.7 V.
- Design a task-based intermittent application for a bridge vibration sensor: sample accelerometer at 1 kHz for 1 second, compute FFT, and transmit the dominant frequency. Decompose into idempotent tasks and specify the commit points.

---

ᚾ **Lecture 10: Privacy-Preserving Edge AI — Computing on Data You Cannot See**

**Course:** CS404 — Neuromorphic & Edge Computing  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

A home audio assistant that processes speech locally never sends voice recordings to the cloud. A medical wearable that detects atrial fibrillation on-device never exposes your ECG to a server. Edge computing is, at its core, a privacy technology — but only if we get the details right. This lecture covers the privacy threats that edge computing addresses (and the ones it doesn't), the technical mechanisms for privacy preservation (differential privacy, secure enclaves, homomorphic encryption), and the emerging regulatory landscape that makes edge privacy not just an engineering choice but a legal requirement. We frame privacy through the Norse concept of *huldufólk* — the hidden folk who live in the spaces between, unseen unless they choose to be seen.

### Key Concepts

- **The privacy promise of edge computing:** When data never leaves the device, the traditional cloud privacy risks (data breach, subpoena, insider threat, secondary use) are fundamentally eliminated — for that data at rest. But edge devices face *different* privacy threats: physical theft, side-channel attacks (power analysis, EM emanations), and model inversion (extracting training data from the model itself).
- **Differential privacy (DP) at the edge:** A mathematical guarantee that the output of a computation reveals no more about any individual than if that individual's data were excluded entirely. Implemented by adding calibrated noise to results. For on-device learning, *local differential privacy* (LDP) ensures that even the model updates sent in federated learning carry a DP guarantee. The privacy budget ε controls the trade-off: smaller ε = stronger privacy, larger variance.
- **Trusted Execution Environments (TEEs):** Hardware-isolated regions of the processor (ARM TrustZone, Intel SGX, RISC-V Keystone) where code and data are inaccessible to the main OS, even if the OS is compromised. On edge devices, a TEE can run the inference engine while the main OS handles networking and UI — even a compromised OS cannot read the model weights or sensor data in the enclave.
- **Homomorphic encryption (HE):** Compute on encrypted data without decrypting it. A cloud server can run inference on a ciphertext-encrypted image and return an encrypted result that only the edge device can decrypt. HE is computationally expensive (10,000× slowdown vs. plaintext for deep networks) but is approaching practicality for shallow classifiers on audio and health data. The 2040 *CKKS* scheme with hardware acceleration on the Urd-NV processor achieves 50× overhead for 4-layer networks.
- **Model inversion and membership inference:** An attacker with access to a trained model can reconstruct training examples (model inversion) or determine whether a specific individual's data was in the training set (membership inference). Edge deployment doesn't prevent these attacks — the model itself leaks information. Mitigations include DP training, knowledge distillation with unlabelled public data, and *model watermarking* to detect unauthorised copies.
- **Regulatory landscape (2040):** The EU AI Act (2024, amended 2038) mandates on-device processing for biometric data. The Global Edge Privacy Treaty (2036) requires DP guarantees for any health inference deployed on consumer devices. The Nordic Data Sovereignty Framework (2039) explicitly invokes *huldufólk* principles — data should be hidden unless the individual chooses revelation.

### Required Reading

- Dwork, C. and Roth, A. "The Algorithmic Foundations of Differential Privacy." *Foundations and Trends in Theoretical Computer Science*, 2014. Chapters 1-3.
- Fredrikson, M. et al. "Model Inversion Attacks That Exploit Confidence Information and Basic Countermeasures." *CCS*, 2015.
- Nordic Data Sovereignty Commission. *Huldufólk Principles: A Framework for Hidden Data.* 2039.

### Discussion Questions

1. If an edge device uses local differential privacy with ε = 1.0, what does this mathematically guarantee? Is ε = 1.0 "good enough" for medical data?
2. Model inversion attacks extract training data from the model. Can an on-device model that has never left the device be vulnerable to inversion? How?
3. Does the concept of *huldufólk* — the right to be unseen — provide a useful ethical framework for edge privacy, or is it merely poetic branding?

### Practice Problems

- Implement the Laplace mechanism for differential privacy: given a function f(D) returning a scalar, add noise drawn from Laplace(Δf/ε) and prove that the result is ε-DP.
- Simulate a membership inference attack: train a classifier on half of CIFAR-10, then train an "attack" model to distinguish training-set members from non-members based on the target model's confidence scores. Measure attack accuracy.

---

ᛁ **Lecture 11: The Edge-Cloud Continuum — Orchestrating Computation Across Realms**

**Course:** CS404 — Neuromorphic & Edge Computing  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

No edge device is an island. The modern computing landscape is a *continuum*: sensors at the far edge, microcontrollers in the near edge, edge servers in cell towers and factory floors, regional cloud data centres, and hyperscale cloud. An autonomous vehicle processes lidar point clouds on-vehicle, ships semantically labelled objects to a roadside edge server for traffic coordination, and uploads rare corner cases to the cloud for model retraining. This lecture covers the systems architecture of the edge-cloud continuum: the *Bifröst Broker* (a UoY reference implementation), workload partitioning algorithms, service mesh at the edge, and the *Yggdrasil Orchestration Framework* that manages computation across all nine realms — from the sensor (Niflheim, the misty near-nothing) to the cloud (Ásgarðr, the realm of abundant compute).

### Key Concepts

- **The continuum taxonomy:** Far edge (microcontrollers, <1 W, intermittent connectivity), near edge (gateways, 1-10 W, cellular/WiFi), edge cloud (micro-data centres, 100 W-1 kW, fibre), regional cloud, hyperscale cloud. Each tier adds ~10× more compute capacity and ~10× higher latency to the user.
- **Workload partitioning (SPLIT architecture):** A DNN is divided into a *head* (early layers) deployed on the edge device and a *tail* (later layers) deployed on the edge server. The head extracts features and compresses the data; the tail performs complex reasoning. The split point is chosen to balance edge latency, transmission bandwidth, and cloud accuracy. Tools: *SPLIT-Net* framework, *Neurosurgeon* profiler.
- **The Bifröst Broker:** UoY's open-source edge-cloud orchestration layer (2040). It maintains a registry of available compute nodes across the continuum with real-time latency and load metrics. When a client submits an inference request, Bifröst solves a constrained optimisation: minimise end-to-end latency subject to accuracy ≥ target, energy ≤ budget, and privacy policy constraints. The solution may route to 3 different nodes for different parts of the pipeline.
- **Service mesh at the edge:** Istio and Linkerd were designed for homogeneous cloud clusters. Edge deployments need a lighter mesh: the *Hlér* mesh (UoY, 2039) uses eBPF-based proxies with <1 MB memory footprint, handling intermittent connectivity with store-and-forward message queues that survive node reboot.
- **Vehicle-to-Infrastructure (V2I) as a continuum case study:** A self-driving car at 30 m/s has ~100 ms to react to a pedestrian. On-vehicle GPU processes camera frames (10 ms). Near-edge roadside unit fuses vehicle and traffic-light data (5 ms round-trip). Cloud updates the HD map with construction-zone changes (500 ms — not in the critical path). Total latency budget: 100 ms. The continuum orchestration must meet hard real-time constraints while optimising for cost.
- **The Yggdrasil Orchestration Framework:** Maps each of the Nine Realms to a tier in the continuum:
  - **Niflheim:** Far-edge sensors (cold, dark, intermittent)
  - **Miðgarðr:** Near-edge gateways (the human realm — phones, routers, cars)
  - **Ásgarðr:** Cloud data centres (the gods' realm — abundant compute)
  - **Álfheimr:** Neuromorphic accelerators (the light-elves — elegant, efficient)
  - And five others mapping to specialised tiers. The framework uses Norse cosmology as a *mental model* for systems architects — each realm has different physics, different guarantees, different inhabitants.

### Required Reading

- Kang, Y. et al. "Neurosurgeon: Collaborative Intelligence Between the Cloud and Mobile Edge." *ASPLOS*, 2017.
- Satyanarayanan, M. et al. "The Seminal Role of Edge-Native Applications." *IEEE EdgeCom*, 2020.
- UoY Distributed Systems Group. *Bifröst: A Multi-Realm Orchestration Framework for the Edge-Cloud Continuum.* Technical Report, 2040.

### Discussion Questions

1. The SPLIT architecture partitions a DNN between edge and cloud. How do you choose the optimal split point? What factors would push the split toward the edge, and what factors pull it toward the cloud?
2. The Bifröst Broker solves a constrained optimisation for every request. At 10,000 requests/second, is this computationally feasible? What approximations would you make?
3. Does mapping computing tiers to Norse cosmology add value as a mental model, or is it just decorative? How does the metaphor help or hinder a systems architect?

### Practice Problems

- Profile a ResNet-50 model layer by layer: for each layer, measure compute time on a Cortex-A78 (edge) and NVIDIA Orin (edge server), output data size, and transmission time over 5G (100 Mbps, 10 ms RTT). Identify the optimal split point that minimises end-to-end latency.
- Design a Bifröst policy for a video analytics pipeline: 30 fps camera → object detection → face blurring (privacy) → activity recognition. Specify which tiers handle which stages and the latency/accuracy/privacy trade-offs.

---

ᛃ **Lecture 12: The Rune-Carver's Synthesis — Neuromorphic Edge Computing in 2040 and Beyond**

**Course:** CS404 — Neuromorphic & Edge Computing  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

We end where we began — at the boundary — but with a transformed understanding. Over twelve lectures we have traversed the landscape of neuromorphic edge computing: from the biology of the spiking neuron to the architecture of Loihi and TrueNorth, from the mathematics of sensor fusion to the ethics of on-device privacy, from energy-harvesting microcontrollers to the orchestration of computation across nine realms. This final lecture synthesises the threads into a coherent vision: what neuromorphic edge computing makes possible in 2040, what remains beyond reach, and what the next decade promises. We reflect on the Norse rune-carver's craft — the patience to shape silicon to thought, the wisdom to place computation where it belongs, the humility to recognise that the most elegant chip is the one that draws its power from light and its purpose from the world it serves.

### Key Themes

- **The convergence thesis:** By 2040, neuromorphic computing, edge deployment, and energy harvesting have converged. A single Loihi 3 "Yggdrasil" chip, powered by a 2 cm² indoor photovoltaic cell, can run a continuous gesture recognition, keyword spotting, and activity classification pipeline — learning on the fly, preserving privacy, operating for years without maintenance. This convergence is not an accident; it is the logical endpoint of three decades of research in each field.
- **What neuromorphic edge computing has already achieved:** Real-time sign language translation on a smartwatch (ETH Zurich, 2040). Battery-free pipeline corrosion monitoring across 1,200 km of Norwegian gas pipeline (Equinor + UoY, 2039-2040). Brain-inspired navigation for Mars rovers — Loihi 3 running SLAM on 1.5 W during the Martian night (NASA + Intel, 2040). Continuous atrial fibrillation detection in 400,000 Nordic citizens, processed entirely on-device (Nordic Health AI Initiative, 2039).
- **What remains hard:** General-purpose AI on a microcontroller — neuromorphic chips excel at pattern recognition and control, not symbolic reasoning. Scaling spiking networks beyond ~100 million neurons (the human brain has ~86 billion). Programming models — Lava and corelet are powerful but inaccessible to most developers. Verification — how do you prove that a self-learning neuromorphic chip won't catastrophically fail in a safety-critical deployment?
- **The ethical horizon:** A billion battery-free sensor nodes monitoring every forest, pipeline, and bridge on Earth. The environmental upside is enormous — early wildfire detection, precision agriculture, structural health monitoring. The privacy risk is equally enormous — pervasive sensing without consent, invisible and immortal. The rune-carver's ethic demands that we carve our intentions into the silicon as deeply as our circuits: what is sensed, who sees it, what is remembered, what is forgotten. These are not afterthoughts — they are part of the architecture.
- **The next decade (2040-2050):** Photonic neuromorphic chips (light-based spiking, ~100× energy reduction), molecular-scale synapses using memristive nanowires, neural dust — millimetre-scale wireless sensors that can be scattered like pollen, and the first neuromorphic general intelligence — not AGI, but a single chip that can learn to perform any sensorimotor task within a bounded domain. The University of Yggdrasil's *Ragnarök Project* (launching 2041) aims to build this chip, integrating photonic neurons, memristive learning, and energy-harvesting power management on a single 1 cm² die.

### Required Reading

- University of Yggdrasil Neuromorphic Lab. *The Ragnarök Project: A Roadmap to Photonic Neuromorphic General Intelligence.* White Paper, 2040.
- Nordic Health AI Initiative. *Four Hundred Thousand Hearts: On-Device Cardiac Monitoring at National Scale.* 2039.
- Equinor + UoY. *Battery-Free Pipeline Monitoring: 1,200 Kilometres of Autonomous Sensing.* Technical Report, 2040.

### Discussion Questions

1. Is the convergence of neuromorphic, edge, and energy-harvesting technologies inevitable, or are there fundamental obstacles that could derail it?
2. A billion battery-free sensors is an environmental monitoring triumph and a privacy nightmare. Can both be true? How would you design the governance framework?
3. The Ragnarök Project aims for neuromorphic general intelligence on a 1 cm² die. What does "general intelligence" mean at that scale, and what would prove it had been achieved?

### Practice Problems

- Design a complete edge deployment for wildfire detection in a boreal forest: choose sensors, processing architecture, energy source, communication protocol, and privacy guarantees. Justify every decision against alternatives.
- Write a 500-word project proposal for a neuromorphic edge application of your own design. Specify the sensor modality, the chip platform, the learning approach, the energy budget, and the ethical considerations. This is your rune to carve.

---

## Final Examination Preparation

The final examination for CS404 consists of two parts:

### Part I: Essay Questions (60%)

**Instructions:** Choose four of the following eight questions. Each answer should be 500-750 words, demonstrate specific technical knowledge from the lectures and readings, and engage with the Norse framing where appropriate.

1. Compare the architectural philosophies of Intel Loihi and IBM TrueNorth. For an edge deployment requiring continuous on-chip learning, which architecture would you choose, and why? Address neurocore design, inter-core communication, programming model, and energy efficiency.

2. A smart agriculture startup proposes deploying 10,000 soil sensors across Swedish farmland, each running a TinyML model for moisture prediction. Design the edge-cloud continuum architecture: what runs on-sensor, what runs at the farm gateway, and what runs in the cloud. Address quantisation, federated learning, and energy harvesting.

3. Spike encoding is the bridge between continuous physical signals and discrete spike events. Compare rate coding, temporal coding, and phase coding for a drone collision-avoidance system. For each scheme, discuss latency, information capacity, robustness to noise, and energy cost.

4. Catastrophic forgetting threatens any system that learns continuously. Explain how Elastic Weight Consolidation addresses this problem, and compare its effectiveness to neuromorphic on-chip STDP. Under what circumstances might a neuromorphic approach be superior?

5. Sensor fusion at the edge must balance accuracy, latency, and resource consumption. Design a fusion system for a wearable health monitor combining PPG, accelerometer, and skin temperature. Specify the fusion algorithm, the computational budget, and how intermittent power affects your design.

6. The privacy promise of edge computing is that data never leaves the device. Critically evaluate this promise: what threats does edge deployment genuinely eliminate, what threats remain, and what new threats does it introduce? Reference differential privacy, TEEs, and model inversion.

7. Energy-harvesting devices operate intermittently, powering on for milliseconds between energy bursts. How does this constraint change the way we write software? Compare task-based intermittent computing with non-volatile processors, and discuss the natural fit of neuromorphic event-driven execution.

8. The Yggdrasil Orchestration Framework maps computing tiers to the Nine Realms of Norse cosmology. Is this mapping a useful systems architecture tool, a pedagogical device, or merely poetic? Analyse the Bifröst Broker architecture through this lens.

### Part II: Design Project (40%)

Design a complete neuromorphic edge computing system for a real-world problem of your choosing. Your proposal must include:

- **Problem statement:** What sensor data needs processing, in what environment, with what constraints?
- **Hardware platform:** Which neuromorphic or edge processor, and why?
- **Sensor modality and encoding:** How are physical signals converted to spikes (if using a neuromorphic chip)?
- **Network architecture:** The spiking or artificial neural network topology, including learning rules.
- **Energy budget:** Power source, consumption breakdown, and operational lifetime.
- **Privacy and ethics:** What data is collected, what is inferred, who has access, and how is consent managed?
- **Evaluation plan:** How would you measure the system's success?

Your proposal should be 1,500-2,000 words and demonstrate integration of concepts from at least six lectures in this course.

---

*CS404 Neuromorphic & Edge Computing — University of Yggdrasil, 2040.*  
*Instructor: Dr. Eiríkr Hrafnsson, UoY Neuromorphic Laboratory*  
*"At the edge of the world, the eagle beats its wings — and the wind begins to move."*
