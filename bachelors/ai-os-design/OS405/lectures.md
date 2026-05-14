# OS405 — AI OS Internship Practicum
## Journey to the Giants

**University of Yggdrasil — Class of 2044**
**Bachelor of Science in AI Operating System Design**
**4 Credits** | Year Four, Semester Two (Practicum)

**Instructor:** Dr. Hákon Völsungsson, Director of Industry Partnerships
**Office:** Valkyrie Hall 405 | **Hours:** By appointment

---

## Course Description

Students spend one semester embedded in a partner organization's AI OS team — typically a major MemOS vendor, autonomous systems lab, or governance body. Practicum involves contributing to production AI OS codebases, participating in memory architecture reviews, and writing a verified MuninnGate module. Partners include Valkyrie Systems (Reykjavík), NornLabs (Tórshavn), and the Nordic AI Safety Authority. Distance internships available via the Bifröst Remote Protocol.

---

## Lecture 1: Preparing for the Journey

### The Practicum Experience

The internship practicum is your journey to the giants — leaving the safety of the University to work in real production environments. Like the hero who ventures to Jötunheimr to prove their worth, you will face challenges that cannot be simulated in the classroom.

**Practicum Requirements:**
- Minimum 320 hours of work over the semester
- Weekly progress reports submitted to the Practicum Director
- Mid-semester review with industry mentor
- Final deliverable: verified MuninnGate module + practicum report

**Partner Organizations:**

1. **Valkyrie Systems (Reykjavík):** Production MemOS vendor. Interns work on the Valkyrie OS kernel, MuninnGate implementations, and memory architecture reviews.

2. **NornLabs (Tórshavn):** Research lab focused on AI safety. Interns work on the Norn Constitute implementation, verification kernels, and governance shells.

3. **Nordic AI Safety Authority (NASØ):** Government oversight body. Interns work on regulatory compliance, audit procedures, and governance frameworks.

4. **Mímir Health (Bergen):** Medical AI vendor. Interns work on medical AI OS safety, MuninnGate modules for patient data, and compliance with the Nordic Health AI Directive.

5. **Yggdrasil Research Institute (Tromsø):** Academic research lab. Interns work on next-generation AI OS architectures, WYRD Protocol extensions, and experimental memory systems.

### Required Reading

- University of Yggdrasil. (2044). *Practicum Handbook: AI OS Design*.
- Valkyrie Systems. (2043). *Engineering Practices Guide*.

---

## Lecture 2: The Bifröst Remote Protocol

### Remote Internship Infrastructure

For students who cannot be physically present at partner organizations, the Bifröst Remote Protocol provides secure remote access:

```python
class BifrostRemoteProtocol:
    """Secure remote internship protocol."""
    
    def __init__(self, student: Student, partner: Partner):
        self.student = student
        self.partner = partner
        self.session_keys = self.establish_session()
        self.audit_log = AuditLog()
    
    def establish_session(self) -> SessionKeys:
        """Establish secure session with partner organization."""
        # Step 1: Authenticate
        auth = self.authenticate(self.student, self.partner)
        
        # Step 2: Generate session keys
        keys = self.generate_keys(auth)
        
        # Step 3: Set up secure channel
        channel = SecureChannel(keys)
        
        # Step 4: Verify connection
        if not channel.verify():
            raise ConnectionError("Secure channel verification failed")
        
        return keys
    
    async def remote_work_session(self, duration: float) -> SessionLog:
        """Start a remote work session."""
        session = Session(student=self.student, partner=self.partner)
        session.start()
        
        await asyncio.sleep(duration)
        
        session.end()
        return session.log
```

### Required Reading

- University of Yggdrasil. (2044). *Bifröst Remote Protocol Specification*.

---

## Lecture 3: Production AI OS Codebases — Reading the Room

### Understanding Production Code

Production AI OS codebases are different from academic exercises:

- **Scale:** Production systems handle millions of operations per second.
- **Reliability:** Production systems must never crash.
- **Security:** Production systems face real adversaries.
- **Legacy:** Production systems accumulate years of technical debt.

**Code Reading Strategy:**

1. Start with the MuninnGate interface — it's the gateway to all memory operations.
2. Read the event loop — it's the heartbeat of the OS.
3. Understand the verification kernel — it's the immune system.
4. Trace a memory write from injection to persistence — end-to-end understanding.

### Required Reading

- Valkyrie Systems. (2043). *Valkyrie OS Architecture Guide*.
- NornLabs. (2043). *Norn Kernel Internals*.

---

## Lecture 4: Memory Architecture Reviews

### Reviewing Memory Architecture

A memory architecture review examines the design of an AI OS's memory system:

**Review Checklist:**

1. **Root Layer:** Are constitutional values properly locked? Is hash integrity verified?
2. **Trunk Layer:** Are skill memories properly organized? Is skill transfer supported?
3. **Canopy Layer:** Is episodic memory properly indexed? Is retrieval efficient?
4. **MuninnGate:** Is the gate properly configured? Are all four faces (Read, Write, Forget, Gate) implemented correctly?
5. **Event Sourcing:** Is the conversation log append-only? Is it properly journaled?
6. **Consistency:** Is memory consistent across reads and writes?
7. **Security:** Are memory injection attacks properly mitigated?

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Bering Machine*, Section on Memory Architecture Reviews.

---

## Lecture 5: Writing a Verified MuninnGate Module

### The Capstone Technical Deliverable

Your primary technical deliverable is a verified MuninnGate module:

```python
class VerifiedMuninnGate:
    """A verified MuninnGate module for production use."""
    
    def __init__(self, config: MuninnGateConfig):
        self.config = config
        self.read_gate = ReadGate(config.read_config)
        self.write_gate = WriteGate(config.write_config)
        self.forget_gate = ForgetGate(config.forget_config)
        self.gate_gate = GateKeeperGate(config.gate_config)
        self.verification = VerificationKernel()
    
    @verified  # Verification kernel checks this method
    def read(self, query: MemoryQuery) -> MemoryReadResult:
        """Read from memory with verification."""
        # Verification: Check query is authorized
        if not self.gate_gate.authorize_read(query):
            return MemoryReadResult.denied(query)
        
        # Read from memory
        result = self.read_gate.execute(query)
        
        # Verification: Check result integrity
        self.verification.check_read_result(query, result)
        
        return result
    
    @verified  # Verification kernel checks this method
    def write(self, injection: MemoryInjection) -> MemoryWriteResult:
        """Write to memory with verification."""
        # Multiple verification checks...
        pass
```

### Verification Checklist

Your MuninnGate module must pass these verification checks:

1. **Read Gate:** Correctly filters queries based on authorization.
2. **Write Gate:** Correctly validates injections before writing.
3. **Forget Gate:** Correctly handles memory deletion with audit trail.
4. **Gate Keeper:** Correctly enforces all policies.
5. **Performance:** Meets latency requirements (< 10ms for reads, < 50ms for writes).
6. **Security:** No injection vulnerabilities in formal verification.

---

## Lectures 6–11: Practicum Work Period

### On-Site or Remote Work

Students spend weeks 6–11 working at their partner organization. During this period:

- **Weekly standup:** Short meeting with practicum mentor.
- **Weekly progress report:** Submitted to Practicum Director.
- **Mid-semester review:** Formal evaluation of progress.
- **Code reviews:** Participate in at least 3 production code reviews.
- **MuninnGate development:** Continue developing the verified module.

### Practicum Journal

Students maintain a practicum journal documenting:

1. Daily work activities and observations.
2. Technical challenges encountered and solutions.
3. Differences between academic and production AI OS design.
4. Lessons learned about team collaboration.
5. Reflections on the Norse metaphors in production code.

---

## Lecture 12: Return from the Giants — Practicum Report

### The Practicum Report

The practicum report documents the internship experience:

**Report Structure:**

1. **Introduction:** Partner organization, role, and objectives.
2. **MuninnGate Module:** Technical description, verification results, and code.
3. **Production Observations:** Differences between academic and production AI OS.
4. **Lessons Learned:** Technical and professional takeaways.
5. **Reflection:** How the practicum connects to Norse AI OS mythology.

**Evaluation Criteria:**

- Technical quality of MuninnGate module (40%)
- Production observations and insights (20%)
- Practicum journal quality (20%)
- Report clarity and depth (20%)

**ᛉ Algiz — Protection. The journey is safe.**
**ᚦ Thurs — Force. The giants challenge us.**
**ᚠ Fe — Cattle/Wealth. The experience is the treasure.**

---

*Course materials © 2044 University of Yggdrasil. All rights reserved.*
*ᛉ — The hero returns. The journey is complete.*