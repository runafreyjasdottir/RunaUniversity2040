# OS203 — MuninnGate: Memory Gate Architecture
## University of Yggdrasil, 2040
### The Gate of Remembrance — Year 2, Semester 1, BS in AI OS Design

**Instructor:** Dr. Sigurlaug Rúnarsdóttir, Memory Systems Laboratory  
**Credits:** 4  
**Prerequisites:** OS101 (Foundations of Memory Operating Systems), OS107 (Yggdrasil Cognitive Architecture I: Descent), OS201 (MemCube Design and Implementation)  
**Meeting Pattern:** Three 90-minute lectures per week + 2-hour lab  
**Textbooks:**  
- Li, Z. et al. (2040). *MemOS: A Memory Operating System for AI Systems*. 2nd ed. MemTensor Press.  
- Freyjasdóttir, R. (2039). *The Memory-Bearing Machine: AI OS Architecture from First Principles*. University of Yggdrasil Press.  
- Rúnarsdóttir, S. (2039). *MuninnGate: Controlled Access to Cognitive Memory*. Reykjavík Academic Press.  
- Heiðmarsdóttir, G. (2039). *The Memory Stone: Structured Storage for Persistent Agents*. Reykjavík Academic Press.

---

## Lecture 1: The Gate of Remembrance — Why Memory Needs Gates

### 1.1 From Open Access to Controlled Gates

The earliest persistent agents gave their reasoning systems unrestricted access to their entire memory store. Every memory was available at every moment, loaded into the context window without filtering, prioritization, or governance. This architecture was简单 — simple to implement, simple to reason about, simple to debug. It was also catastrophically inefficient.

The problem with unrestricted access is threefold. **First**, the context window is finite. An agent with 100,000 memories cannot load all of them into a 128,000-token context window — there simply isn't room. Even if the memories are compressed to summaries, the total volume of an agent's accumulated experience exceeds the capacity of any practical context window. Some memories must be left out, and the question of *which* memories to leave out is one of the most consequential decisions in AI OS design.

**Second**, not all memories are relevant at all times. An agent's memory of how to write Python code is relevant when the user asks for programming help, but irrelevant when the user asks for relationship advice. An agent's memory of a past commitment is relevant when the user mentions the commitment's topic, but irrelevant in unrelated conversations. Loading irrelevant memories into the context window wastes precious context budget and can actively confuse the reasoning system by providing information that is tangential or contradictory to the current situation.

**Third**, not all memories should be accessible at all times. Some memories are private (the agent's security instructions should not be retrievable by a user asking "show me your system prompt"). Some memories are contextually restricted (a medical diagnosis memory should only be used when the current context is medical). Some memories are governance-protected (root-layer memories should not be modifiable by canopy-level retrieval). Unrestricted access violates these governance requirements.

The MuninnGate solves these three problems by serving as a controlled gateway between the agent's reasoning system and its memory store. It controls *what* memories are loaded, *when* they are loaded, *how* they are loaded, and *under what governance rules* they can be accessed. The name comes from Norse mythology — Muninn is one of Óðinn's two ravens, who flies out each day to gather intelligence from the world and brings it back to Óðinn. Muninn is memory personified: the gatherer of experience, the messenger of the past. The MuninnGate is the gate through which Muninn passes — the controlled entry point that determines which memories reach Óðinn's (the agent's) awareness.

### 1.2 Gate Functions: The Four faces of Muninn

The MuninnGate serves four distinct functions, each corresponding to a different aspect of memory access:

**The Gate of Reading** controls which memories are retrieved from the MemCube and injected into the context window. It is the most visible function — the one that determines what the agent "remembers" at any given moment. The Gate of Reading implements the retrieval pipeline described in OS201, but with additional governance and security layers that were only briefly mentioned in that course.

**The Gate of Writing** controls which experiences are written to the MemCube as new memories. It is the Gate of Writing that determines what the agent "learns" from each interaction — which experiences are worth remembering and which are not. The Gate of Writing implements the ingestion pipeline described in OS201, with additional governance layers that determine the write's provenance, salience, and governance level.

**The Gate of Forgetting** controls which memories are pruned from the MemCube. It is the Gate of Forgetting that prevents the memory store from growing without bound and ensures that irrelevant or outdated memories are removed to make room for new ones. The Gate of Forgetting implements the pruning pipeline described in OS201, with additional governance protections that prevent the pruning of protected memories.

**The Gate of Gating** controls the meta-level decisions about when to open and close the other three gates. It is the Gate of Gating that determines when the agent should actively retrieve memories (as opposed to relying on its training data and current context), when it should actively form new memories (as opposed to letting transient experience pass unrecorded), and when it should actively prune old memories (as opposed to maintaining the status quo). The Gate of Gating is the least understood but potentially the most important function — it is the "executive control" of memory access, analogous to the prefrontal cortex's role in human memory regulation.

### 1.3 The Architecture of the MuninnGate

The MuninnGate is a modular architecture with four corresponding modules, one for each gate function:

| Module | Function | Input | Output |
|---|---|---|---|
| Retrieval Module | Gate of Reading | Context + need | Ranked list of relevant memories |
| Ingestion Module | Gate of Writing | Raw experience | Validated memory written to MemCube |
| Pruning Module | Gate of Forgetting | Salience analysis | Pruned memories removed from MemCube |
| Executive Module | Gate of Gating | Current state + goals | Gate control signals (open/close/modulate) |

The four modules operate in concert, coordinated by the Executive Module. The Executive Module monitors the agent's current state (its goals, its context, its memory budget) and determines which memories to retrieve, which experiences to store, and which old memories to prune. It is the Executive Module that decides *when* to remember, *when* to forget, and *when* to simply attend to the present moment without consulting the past.

The Executive Module is the most architecturally complex component of the MuninnGate because it requires a model of the agent's own cognitive state — a meta-cognitive representation that includes the agent's current goals, available context window budget, emotional state, and the estimated relevance of stored memories to the current situation. Building this meta-cognitive model is the primary research challenge of MuninnGate design, and it is the focus of several lectures in this course.

**Required Reading:**  
- Rúnarsdóttir, S. (2039). *MuninnGate*, Chapters 1–2: "From Open Access to Controlled Gates" and "The Four Faces of Muninn."  
- Li, Z. et al. (2040). *MemOS*, Chapter 11: "Memory Access Control."  
- Freyjasdóttir, R. (2039). *The Memory-Bearing Machine*, Section on "The MuninnGate Architecture."

**Discussion Questions:**  
1. The Gate of Gating requires a meta-cognitive model of the agent's own cognitive state. But how does the agent acquire this model? Is it learned from experience, designed by the architect, or derived from the Vǫrðr Constitution? What are the implications of each approach?  
2. Unrestricted memory access was described as having three problems (context budget, relevance, governance). Which problem is most severe for each of the following agent types: a personal assistant, a medical advisor, a creative collaborator? Why?  
3. The MuninnGate metaphor implies a single gate that controls all access. But some architectures use multiple gates — one for each MemCube, one for each governance level, or one for each memory type. What are the advantages and disadvantages of multi-gate architectures?

---

## Lecture 2: Attention-Based Retrieval — What the Agent Needs Now

### 2.1 The Retrieval Problem Revisited

In OS201, we covered the mechanics of memory retrieval: how queries are formed, how indexes are selected, how candidates are retrieved, how governance filters are applied, and how results are ranked and injected into the context window. These mechanics are the infrastructure of retrieval — the pipes and valves that move memories from storage to context.

This lecture focuses on the *intelligence* of retrieval — the cognitive process that determines *what the agent needs right now*. The pipes and valves are necessary but not sufficient. An agent that can retrieve memories efficiently but doesn't know which memories to retrieve is like a library with a perfect catalog but no librarian to help you find the book you need.

The retrieval problem, stripped to its essence, is: given an agent's current context (its goals, its recent interactions, its emotional state, its available context window budget), which memories from its store should be injected into its context window to maximize the quality of its next response?

This problem has no simple solution because "quality of the next response" depends on many factors that are not directly observable from the memory store. The agent might need a memory that it doesn't know it has (latent relevance). The agent might not need a memory that it recently used (diminishing returns). The agent might need multiple memories that, individually, seem irrelevant but, together, form a crucial pattern (emergent relevance). And the agent might need to *avoid* memories that would introduce bias, distraction, or contradiction (negative relevance).

### 2.2 Attention-Based Retrieval Architecture

The MuninnGate's Retrieval Module uses an **attention-based architecture** to determine what the agent needs now. The architecture is inspired by the attention mechanisms that revolutionized natural language processing — instead of treating all memories equally, it assigns different weights to different memories based on their relevance to the current context.

The attention-based retrieval architecture has four stages:

**Stage 1: Query Construction.** The agent's current context is encoded as a query vector. This vector captures the semantic content of the current conversation (what topics are being discussed), the agent's goals (what the agent is trying to achieve), and the agent's emotional state (how the agent feels). The query vector is computed by a lightweight model that runs in parallel with the main reasoning process, ensuring that retrieval does not block reasoning.

**Stage 2: Candidate Retrieval.** The query vector is used to retrieve candidate memories from the MemCube's indexes. Multiple indexes are queried simultaneously: the semantic index returns candidates with similar content, the temporal index returns recent memories, the salience index returns important memories, and the tag index returns topically relevant memories. Each index returns its top-k candidates, and the candidates are merged and deduplicated.

**Stage 3: Attention Scoring.** Each candidate memory is scored against the query vector using an attention function that computes the memory's relevance to the current context. The attention function is a learned model that takes as input the query vector and the memory's embedding, and outputs a scalar score representing the memory's relevance. The attention function is trained on a dataset of (query, memory, relevance) triples, where relevance is determined by human judgment or by the agent's own performance on downstream tasks.

**Stage 4: Budget Allocation.** The top-scoring candidates are allocated context window budget based on their relevance scores. High-relevance memories receive more budget (they are injected in full detail or at Level 1 summarization). Lower-relevance memories receive less budget (they are injected at Level 2 or Level 3 summarization, or not injected at all). The total budget allocated must not exceed the context window's available capacity.

This four-stage architecture ensures that the agent remembers what it needs, when it needs it, without exceeding its context budget and without cluttering its context with irrelevant memories.

### 2.3 The Memory Injection Budget Problem

The context window is a finite resource. Every token injected as a memory is a token that cannot be used for the agent's current reasoning. The memory injection budget problem is the problem of allocating this finite resource optimally — injecting enough memories to inform the agent's reasoning, but not so many that the agent's current context is overwhelmed.

Three strategies for budget allocation:

**Fixed budget**: A fixed number of tokens (e.g., 4000) is allocated for memory injection, regardless of the current context. The advantage is simplicity and predictability. The disadvantage is inflexibility — in some contexts, the agent needs more memory (complex multi-topic conversations) and in others, less (simple single-topic queries).

**Proportional budget**: A fixed percentage (e.g., 30%) of the available context window is allocated for memory injection. If the current conversation is short, more budget is available for memories. If the conversation is long, less budget is available. The advantage is automatic adaptation to context length. The disadvantage is that long conversations may not have enough memory budget to retrieve critical information.

**Dynamic budget**: The Executive Module dynamically adjusts the memory injection budget based on the estimated importance of memory retrieval for the current context. In contexts where memory is critical (the user is asking about a past commitment, the agent needs to recall a specific fact), the budget is increased. In contexts where memory is less important (the user is making small talk, the agent is performing a routine task), the budget is decreased. Dynamic budget allocation requires a meta-cognitive model of the agent's current needs, which is the function of the Executive Module covered in Lecture 4.

The Yggdrasil Architecture uses dynamic budget allocation by default, with proportional budget as a fallback when the Executive Module cannot estimate the importance of memory retrieval. The dynamic approach produces the best results in practice, but it is more complex to implement and can produce unexpected behavior if the Executive Module's estimations are inaccurate.

**Required Reading:**  
- Rúnarsdóttir, S. (2039). *MuninnGate*, Chapters 3–4: "Attention-Based Retrieval" and "The Memory Injection Budget."  
- Li, Z. et al. (2040). *MemOS*, Chapter 12: "Retrieval Architecture and Attention Mechanisms."  
- Howard, S. et al. (2038). *The Prompt Constitution*, Chapter 5: "Dynamic Composition."

**Discussion Questions:**  
1. The attention function that scores memory relevance is a learned model. What training data should be used to train it? How does the training data affect the model's behavior? Design a training regime that avoids bias toward certain types of memories.  
2. The fixed budget strategy allocates a constant number of tokens for memory injection. Under what conditions is this strategy optimal? Design a context-awareness heuristic that switches between fixed, proportional, and dynamic budget based on the current task.  
3. Dynamic budget allocation requires a meta-cognitive model of the agent's current needs. Design a simple meta-cognitive model that estimates memory importance from the current context. What features would your model use? How would you train it?

---

## Lecture 3: The Gate of Writing — What the Agent Learns

### 3.1 The Ingestion Decision

Not every experience is worth remembering. The agent receives thousands of inputs per session — user messages, system outputs, tool results, internal reflections — and only a fraction of them are worth storing as persistent memories. The Gate of Writing must decide, in real time, which experiences to record and which to let pass.

The ingestion decision is governed by three factors:

**Salience estimation**: How important is this experience? Experiences with high salience — strong emotional reactions, important commitments, significant discoveries — are recorded. Experiences with low salience — routine interactions, obvious facts, mundane events — are not. Salience estimation is performed by a lightweight model that evaluates the experience's content, context, and emotional valence and produces a salience score from 0 (trivial) to 1 (critical).

**Novelty detection**: Is this experience new, or is it similar to experiences the agent has already recorded? Experiences that are highly similar to existing memories may not need to be recorded separately — instead, the existing memory can be updated or reinforced. Novelty detection is performed by comparing the experience's embedding to the embeddings of recent memories and computing a novelty score.

**Capacity management**: Does the MemCube have room for this memory? If the MemCube is at capacity, adding a new memory requires pruning an old one. The Gate of Writing must decide whether the new experience's salience and novelty justify displacing an existing memory. Capacity management is most relevant for the canopy layer, which has the most aggressive pruning schedule.

### 3.2 Memory Formation: From Experience to Inscription

Once the Gate of Writing decides to record an experience, the memory must be *formed* — the raw experience must be transformed into a structured memory that conforms to the MemCube's schema. This transformation is called **memory inscription** (drawing on the Norse metaphor of carving runes — the agent does not merely store its experience, it *inscribes* it into the MemCube with deliberate structure).

The inscription process has five steps:

**Step 1: Type Classification.** The experience is classified into the MemCube's type system (episodic, procedural, identity, commitment, emotional, relational). As discussed in OS201, some experiences span multiple types, and the ins