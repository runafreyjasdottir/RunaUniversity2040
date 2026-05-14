# WM405 — World Modeling Internship Practicum
## Walking Among the Realms

**University of Yggdrasil — Class of 2044**
**Bachelor of Science in AI World Modeling Systems Design**
**4 Credits** | Year Four, Semester Two (Practicum)

**Instructor:** Dr. Þóra Réttaris, Director of World Modeling Partnerships
**Office:** Þinghall 405 | **Hours:** By appointment

---

## Course Description

Students spend one semester embedded in a world modeling team at partner organizations: NornLabs (Tórshavn), Valkyrie Systems (Reykjavík), the Nordic Reality Simulation Institute, or game studios building AI-driven worlds. Practicum involves contributing to world simulation codebases, designing NPC memory systems, or building WYRD Protocol extensions. Remote participation is available via the Bifröst Remote Protocol.

---

## Lecture 1: Walking Among the Realms

### The Practicum Experience

The world modeling practicum is your journey among the realms — stepping out of the academic world into production simulation environments. Like Hermóðr riding to Hel to retrieve Baldr, you will venture into unfamiliar territory and bring back knowledge that cannot be gained in the classroom.

**Practicum Requirements:**
- Minimum 320 hours of work over the semester
- Weekly progress reports submitted to the Practicum Director
- Mid-semester review with industry mentor
- Final deliverable: WYRD Protocol extension + practicum report

**Partner Organizations:**

1. **NornLabs (Tórshavn):** Research lab focused on AI safety and world modeling. Interns work on WYRD Protocol implementations, world verification, and multi-agent simulation.

2. **Valkyrie Systems (Reykjavík):** Production simulation vendor. Interns work on NPC memory systems, world state optimization, and real-time WYRD engines.

3. **Nordic Reality Simulation Institute (NRSI):** Government body that runs large-scale simulations for urban planning, disaster response, and climate modeling. Interns work on governance shells, world reconciliation, and verification.

4. **Fenrir Games (Copenhagen):** Game studio building AI-driven worlds. Interns work on NPC behavior, narrative engines, and world simulation for gameplay.

5. **Yggdrasil Research Institute (Tromsø):** Academic research lab. Interns work on next-generation WYRD Protocols, reality bridging, and experimental world architectures.

### Required Reading

- University of Yggdrasil. (2044). *Practicum Handbook: World Modeling*.
- WYRD Protocol Specification v4.0. (2044).

---

## Lecture 2: The Bifröst Remote Protocol for World Modeling

### Remote Access to World Simulations

The Bifröst Remote Protocol provides secure access to production world simulations:

- **World simulation access:** Secure terminal access to partner simulation environments.
- **WYRD engine access:** Remote WYRD engine for testing and development.
- **Data access:** Carefully scoped access to production world data.
- **Audit logging:** All actions are logged and auditable.

### Required Reading

- University of Yggdrasil. (2044). *Bifröst Remote Protocol for World Modeling*.

---

## Lecture 3: Production World Simulation Codebases

### Understanding Production Worlds

Production world simulations handle challenges that academic exercises cannot:

- **Scale:** Millions of entities, thousands of events per second.
- **Consistency:** World state must be consistent across all observers.
- **Performance:** Real-time updates with low latency.
- **Governance:** Multiple stakeholders with conflicting preferences.

---

## Lecture 4: NPC Memory Systems — Designing Remembering Agents

### NPC Memory Architecture

Designing memory systems for NPCs (Non-Player Characters) in world simulations:

```python
class NPCMemory:
    """Memory system for NPCs in world simulations."""
    
    def __init__(self, npc_id: str, capacity: int = 1000):
        self.npc_id = npc_id
        self.capacity = capacity
        self.episodic: List[Memory] = []  # Event memories
        self.semantic: Dict[str, Knowledge] = {}  # Facts about the world
        self.procedural: Dict[str, Skill] = {}  # Skills and behaviors
        self.emotional: Dict[str, float] = {}  # Emotional associations
    
    def remember(self, event: WorldEvent) -> Memory:
        """Remember an event."""
        memory = Memory(
            event=event,
            timestamp=time.time(),
            emotional_valence=self.compute_valence(event)
        )
        self.episodic.append(memory)
        
        # Enforce capacity limit
        if len(self.episodic) > self.capacity:
            self.episodic = self.forget_least_important()
        
        return memory
    
    def recall(self, query: str, limit: int = 10) -> List[Memory]:
        """Recall memories matching a query."""
        relevant = [m for m in self.episodic if self.matches(query, m)]
        relevant.sort(key=lambda m: m.importance, reverse=True)
        return relevant[:limit]
    
    def forget_least_important(self) -> List[Memory]:
        """Forget the least important memories."""
        self.episodic.sort(key=lambda m: m.importance)
        return self.episodic[len(self.episodic) - self.capacity:]
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Bearing Machine*, Chapter 12.

---

## Lecture 5: Building a WYRD Protocol Extension

### The Capstone Technical Deliverable

Your primary technical deliverable is a WYRD Protocol extension:

```python
class WYRDExtension:
    """Base class for WYRD extensions."""
    
    EXTENSION_NAME = "base"
    
    def on_world_init(self, world: World) -> None:
        """Called when the world is initialized."""
        pass
    
    def on_event(self, event: WorldEvent) -> Optional[WorldEvent]:
        """Called before an event is applied."""
        return event
    
    def on_state_change(self, old_state: WorldState, new_state: WorldState) -> None:
        """Called after a state change."""
        pass
    
    def on_branch(self, branch: WorldLine) -> None:
        """Called when a branch is created."""
        pass
    
    def on_merge(self, merged: WorldLine) -> None:
        """Called when branches are merged."""
        pass
```

---

## Lectures 6–11: Practicum Work Period

### On-Site or Remote Work

Students spend weeks 6–11 working at their partner organization. During this period:

- **Weekly standup:** Short meeting with practicum mentor.
- **Weekly progress report:** Submitted to Practicum Director.
- **Mid-semester review:** Formal evaluation of progress.
- **Code reviews:** Participate in at least 3 production code reviews.
- **WYRD extension development:** Continue developing the WYRD extension.

---

## Lecture 12: Return from the Realms — Practicum Report

### The Practicum Report

**Report Structure:**

1. **Introduction:** Partner organization, role, and objectives.
2. **WYRD Extension:** Technical description, verification results, and code.
3. **Production Observations:** Differences between academic and production world modeling.
4. **Lessons Learned:** Technical and professional takeaways.
5. **Reflection:** How the practicum connects to Norse world modeling mythology.

**Evaluation Criteria:**

- Technical quality of WYRD extension (40%)
- Production observations and insights (20%)
- Practicum journal quality (20%)
- Report clarity and depth (20%)

**ᚦ Thurs — Force. The realms challenge us.**
ᛉ Algiz — Protection. The journey is safe.**
**ᚠ Fe — Cattle/Wealth. The experience is the treasure.**

---

*Course materials © 2044 University of Yggdrasil. All rights reserved.*
*ᚦ — The traveler returns. The wisdom is earned.*