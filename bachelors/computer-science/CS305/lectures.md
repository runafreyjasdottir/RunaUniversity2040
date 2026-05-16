# CS305: Artificial Intelligence Systems
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4
**Semester:** Year 3, Semester 1
**Prerequisites:** CS106 (Operating Systems), CS205 (Machine Learning & Data Mining)
**Instructor:** Dr. Freyja Mjøðvitnir, Faculty of Computational Arts & AI Systems

> *"A god does not create from nothing. Óðinn hung on Yggdrasil for nine nights to acquire the runes — the existing patterns of the universe. AI, too, does not create from nothing. It learns the patterns already woven into the world's data. The art is in choosing which patterns to heed."* — Freyja Mjøðvitnir, *The Waking Wood* (2038)

---

## Course Description

Artificial Intelligence Systems is the study of how machines perceive, reason, learn, and act in the world. This course bridges the gap between theoretical AI (search, planning, knowledge representation) and the practical systems that define the 2040 landscape (large language models, agent architectures, multimodal AI, and AI safety). Students build a complete AI agent from scratch — starting with symbolic search and planning, then incorporating learned components, and finally deploying the agent on the University's Hermes AI OS platform to solve real-world tasks.

The Norse metaphor threading this course is the *vǫlva* — the seeress who journeys through the nine realms, perceiving past, present, and future. An AI system is a vǫlva: it perceives the world through sensors, reasons about what it has seen, predicts what will happen next, and acts to shape events. Like the vǫlva, its knowledge is never complete — it sees patterns but not the whole weave.

---

## Lectures

### ᚠ Lecture 1: What Is Intelligence? — The Seeress Awakens

**Date:** Week 1, Session 1

#### Overview

What does it mean for a machine to be intelligent? This lecture surveys the history of AI from its founding at the 1956 Dartmouth Conference through the 2020s deep learning revolution to the 2040 landscape of foundation models, AI agents, and the Hermes AI OS framework. We establish the core tension: connectionist approaches (neural networks, learning from data) vs. symbolic approaches (logic, reasoning, knowledge representation) — and the 2040 synthesis of both in neuro-symbolic systems. The Norse framing: the vǫlva's trance state — a blend of intuitive pattern recognition (connectionist) and deliberate chant (symbolic), neither complete without the other.

#### Lecture Notes

The field of Artificial Intelligence was born in the summer of 1956 at Dartmouth College, where John McCarthy, Marvin Minsky, Nathaniel Rochester, and Claude Shannon proposed a two-month workshop on "the conjecture that every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it." The proposal itself is remarkably optimistic, predicting that "a significant advance can be made in one or more of these problems if a carefully selected group of scientists work on it together for a summer."

**The First AI Winter (1974-1980).** The initial optimism collided with computational reality. Symbolic AI systems (Newell and Simon's General Problem Solver, 1957; Weizenbaum's ELIZA, 1966) worked for toy problems but failed to scale. The Lighthill Report (1973) in the UK was devastating: "in no part of the field have the discoveries made so far produced the major impact that was then promised." Government funding (DARPA, UK Science Research Council) was slashed dramatically.

**Expert Systems and the Second Winter (1980-1987).** The 1980s saw the rise of expert systems: rule-based systems that encoded human expertise in narrow domains. MYCIN (medical diagnosis, 1976), XCON (computer configuration, 1980), and PROSPECTOR (mineral exploration, 1981) achieved remarkable success — XCON saved DEC an estimated $40M per year by 1987. The Japanese Fifth Generation Computer Systems project (1982-1992) and the US Strategic Computing Initiative (1983-1993) poured billions into AI. But the limitations of rule-based systems became apparent: they were brittle (a single missing rule caused catastrophic failure), labor-intensive (each rule required a knowledge engineer extracting expertise from a domain expert), and incapable of learning from data.

**The Statistical Revolution (1990s-2000s).** The 1990s shifted focus from symbolic reasoning to statistical pattern recognition. Neural networks, inspired by the brain's architecture, re-emerged with backpropagation (Rumelhart, Hinton, Williams, 1986) and the Support Vector Machine (Vapnik, 1995). Statistical machine translation (IBM Model 1-4, 1990s), speech recognition (HMMs and GMMs), and computer vision (SIFT, Viola-Jones) achieved practical results. The field rebranded — much of what had been "AI" became "machine learning."

**Deep Learning (2012-2024).** The ImageNet competition of 2012 (Krizhevsky, Sutskever, Hinton's AlexNet) marked the beginning of the deep learning era. Three factors converged:
1. **Data:** The internet provided billions of labeled images, text, and video.
2. **Compute:** GPU computing (NVIDIA CUDA, 2006) enabled training of networks with millions of parameters.
3. **Algorithms:** Dropout, ReLU, Batch Normalization, and the Adam optimizer made deep networks trainable.

By 2024, transformers (Vaswani et al., 2017) had become the dominant architecture. GPT-4, Claude 3, Gemini, and Llama demonstrated remarkable language understanding and generation capabilities. The "scaling hypothesis" — that larger models trained on more data would continue to improve — was the dominant orthodoxy.

**The 2040 Landscape.** By 2040, the landscape has transformed further:
- **Foundation models** (models trained on internet-scale data and adapted to many tasks) are the infrastructure of AI. The University's **Hermes AI OS** provides a platform for deploying, composing, and governing AI agents.
- **Neuro-symbolic AI** integrates neural pattern recognition with symbolic reasoning, achieving the best of both worlds.
- **AI agents** — autonomous systems that perceive, reason, plan, and act — are the dominant application paradigm.
- **AI safety** has matured into a rigorous engineering discipline with formal verification techniques.

**The Vǫlva Analogy.** The Norse vǫlva enters a trance state to perceive the weave of fate. In this state, she is neither fully conscious (like a symbolic system following explicit rules) nor fully unconscious (like a neural network processing patterns). She is both — a synthesis of intuitive perception and deliberate utterance. The 2040 AI system is a vǫlva: its foundation model provides intuitive pattern recognition (the trance), while its reasoning layer provides deliberate analysis (the utterance). Neither is sufficient alone.

#### Required Reading
- Russell, S. & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach*, 4th ed. Chapters 1-2.
- McCarthy, J. et al. (1955). "A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence."
- Vaswani, A. et al. (2017). "Attention Is All You Need." *NeurIPS*.
- Mjøðvitnir, F. (2038). *The Waking Wood*, Chapter 1: "The Seeress and the Machine." Yggdrasil University Press.

#### Discussion Questions
1. Was the Dartmouth proposal's optimism justified, or did it set unrealistic expectations that led to the AI winters?
2. The "scaling hypothesis" suggests that larger models will continue to improve. Is there a limit to this scaling, and if so, what is it?
3. How does the neuro-symbolic synthesis differ from pure deep learning? What problems does it solve?

---

### ᚢ Lecture 2: Search and Planning — The Journey Through Realms

**Date:** Week 2, Session 1

#### Overview

Before deep learning conquered AI, symbolic search was the only game in town. This lecture covers the foundations of problem-solving as search: state spaces, uninformed (BFS, DFS, IDDFS) and informed search (A*, heuristics, admissibleness), constraint satisfaction problems (backtracking, forward checking, arc consistency), and classical planning (STRIPS, PDDL, Graphplan, and the 2040 integration of learned heuristics into search). The Norse metaphor: Óðinn's journey through the nine realms — each realm is a state, each path between realms is an action, and the search for knowledge is a heuristic-guided exploration of the world-tree.

#### Lecture Notes

**The Search Formulation.** A problem can be formulated for search as:
- **State space:** All possible configurations of the world.
- **Initial state:** Where we start.
- **Actions:** What we can do (each action transforms one state to another).
- **Goal test:** Whether a state is the desired outcome.
- **Path cost:** How expensive a sequence of actions is.

A search algorithm explores the state space graph, looking for a path from the initial state to any goal state. The distinction between *tree search* (may revisit states) and *graph search* (maintains closed set) is critical for avoiding infinite loops.

**Uninformed Search.** When no domain-specific knowledge is available, we use uninformed strategies:
- **BFS:** Guarantees shortest path, exponential memory O(bᵈ).
- **DFS:** Linear memory O(bd), no optimality guarantee, vulnerable to infinite depth.
- **Iterative Deepening DFS:** Optimal like BFS, memory like DFS. Time overhead is modest: only b/(b-1)× the cost of BFS.

**Informed Search (A*).** A* (Hart, Nilsson, Raphael, 1968) uses a heuristic function h(n) estimating the cost from node n to the goal. The evaluation function f(n) = g(n) + h(n) where g(n) is the cost so far. A* is:
- **Admissible:** If h(n) never overestimates the true cost (h ≤ h*), A* returns the optimal solution.
- **Consistent (monotonic):** If h satisfies the triangle inequality h(n) ≤ c(n, a, n') + h(n'), A* with graph search is optimal.
- **Optimally efficient:** No admissible algorithm explores fewer nodes than A* for a given heuristic.

**Designing Heuristics.** The art of A* is designing good heuristics. Two classic approaches:
- **Relaxed problem:** Remove constraints from the problem to make it easier to solve. The cost of the relaxed problem is an admissible heuristic for the original. For the 8-puzzle, the Manhattan distance heuristic (sum of horizontal and vertical distances to goal positions) is derived from the relaxed problem where tiles can move through each other.
- **Pattern databases:** Precompute the exact cost to solve small instances of the problem and store them as heuristic values. A pattern database for the 15-puzzle (7-tile pattern) yields heuristics that reduce the search space by a factor of 1000.

**Constraint Satisfaction Problems (CSPs).** CSPs are a special class of search problems where:
- State is defined by variables with domains.
- Goal is defined by constraints on variable assignments.
- Actions assign values to variables.

The canonical algorithm is **backtracking** with:
- **Forward checking:** After assigning a variable, remove inconsistent values from unassigned variables' domains.
- **Arc consistency (AC-3):** Iteratively enforce consistency between all pairs of variables.
- **Degree heuristic:** Choose the variable involved in the most constraints (MRV — Minimum Remaining Values).

**Planning.** Classical planning (STRIPS, 1971; PDDL, 1998) represents actions as preconditions and effects. The planner searches through plan space (sequences of actions) rather than state space. The **Graphplan** algorithm (Blum & Furst, 1997) builds a planning graph that captures mutual exclusions between actions at each time step, enabling fast parallel plan extraction. By 2040, planning integrates learned heuristics: a neural network predicts promising action sequences from the state representation, which the symbolic planner uses to prune the search space — a neuro-symbolic approach.

#### Required Reading
- Hart, P.E., Nilsson, N.J., & Raphael, B. (1968). "A Formal Basis for the Heuristic Determination of Minimum Cost Paths." *IEEE TSSC*, 4(2).
- Blum, A.L. & Furst, M.L. (1997). "Fast Planning Through Planning Graph Analysis." *Artificial Intelligence*, 90.
- Russell, S. & Norvig, P. (2021). *AIMA*, Chapters 3-6.

#### Discussion Questions
1. Why can't DFS be used for finding the shortest path in an infinite state space? What modification makes it feasible?
2. Design an admissible heuristic for a delivery robot navigating a warehouse with obstacles.
3. Compare Graphplan with forward-chaining search for planning. When is each preferred?

---

### ᚦ Lecture 3: Knowledge Representation — The Rune-Carving of Concepts

**Date:** Week 3, Session 1

#### Overview

How does an AI system represent what it knows? This lecture covers the foundations of knowledge representation: ontologies, description logics, semantic networks, frames, and the tradeoff between expressiveness and tractability. We also cover the modern knowledge representation stack: knowledge graphs (Google's Knowledge Graph, Wikidata, ConceptNet), vector embeddings (semantic spaces), and the neuro-symbolic integration that combines symbolic knowledge with learned representations. The Norse metaphor: the runes themselves — each rune (stave) represents a concept (Fehu = wealth, Uruz = strength), and the combination of runes in an inscription represents complex knowledge. An ontology is a runic alphabet for a domain.

#### Lecture Notes

**The Symbol Grounding Problem.** How does a symbol (the word "cat") connect to the thing-in-the-world (the actual furry animal)? This is the symbol grounding problem (Harnad, 1990). A purely symbolic system (like a medieval encyclopedia) can define "cat" in terms of "feline" and "mammal," but at some point the chain of definitions must touch the world. A neural network grounds symbols through its training data: the word "cat" is embedded in a vector space near other cat-related words, and the network's visual system recognizes cat images. But this grounding is statistical, not categorical — leading to adversarial vulnerabilities (a panda with noise becomes an "ostrich").

**Semantic Networks and Frames.** Marvin Minsky's **frames** (1975) represent stereotyped situations as collections of slots with default values:
- Restaurant frame slots: diners, tables, waitstaff, menu, food, bill, tips.
- Subframes: a "diner" frame is a "person" frame with additional properties.

Frames support inheritance (a "diner" inherits "has two legs" from "person") and default reasoning (by default, the bill includes a service charge — but this can be overridden). Frames were the 1970s answer to knowledge representation; they are the ancestor of modern object-oriented programming and of the schemas used in knowledge graphs.

**Description Logics (DLs).** Description Logics (Brachman & Schmolze, 1985; Baader et al., 2003) are a family of formal languages for representing knowledge about concepts, roles (relationships), and individuals. The canonical DL, *ALC* (Attributive Language with Complements), supports:
- Concept constructors: ⊤ (top), ⊥ (bottom), ¬ (negation), ⊓ (intersection), ⊔ (union), ∀ (universal restriction), ∃ (existential restriction).
- TBox: terminological knowledge about concepts ("All cats are mammals" = Cat ⊑ Mammal).
- ABox: assertional knowledge about individuals ("Garfield is a cat" = Cat(Garfield)).
- RBox: role axioms (transitive roles, role hierarchies).

The key advantage of DLs: they are *decidable*. The tableaux algorithm decides satisfiability of *ALC* formulas in EXPTIME (worst case), and practical DLs like those underlying OWL 2 (the Web Ontology Language) are tractable for typical ontologies. By 2040, OWL 2 reasoners (Pellet, HermiT, ELK) can classify ontologies with millions of axioms in seconds.

**Knowledge Graphs.** A knowledge graph is a directed labeled graph where nodes are entities and edges are relationships. Google's Knowledge Graph (2012) contains over 7 billion facts about 500 million entities. Wikidata has over 100 million items. The difference from a traditional relational database: knowledge graphs are *schema-later* — you define the schema as you discover relationships, not before you store data.

By 2040, knowledge graphs are built and maintained by AI systems. The **Yggdrasil Knowledge Graph** — the UoY's unified knowledge repository — ingests research papers, student projects, course syllabi, and research data. It is queried in a natural-language interface (the "seeress" interface) that translates user questions into SPARQL queries against the graph.

**Vector Representations.** Parallel to symbolic knowledge, the 2040 stack uses vector embeddings. Each concept is a d-dimensional vector (typically 4096 for entity embeddings by 2040). The embedding space has algebraic properties: vec("king") - vec("man") + vec("woman") ≈ vec("queen"). Knowledge graph embeddings (TransE, ComplEx, RotatE) embed both entities and relations in the same space, enabling link prediction: given subject and relation, predict the object.

**Neuro-Symbolic Integration.** The 2040 frontier is *neuro-symbolic* AI: using neural networks to map natural language to symbolic knowledge representations, and symbolic reasoners (DL tableaux, SAT solvers) to derive logical conclusions from the knowledge. The **Huginn system** at UoY (named after Óðinn's raven of thought) translates student questions about course material into DL queries, reasons over the knowledge graph, and returns answers with formal justifications. Huginn achieved a 92% accuracy on the UoY exam question bank in 2039.

#### Required Reading
- Brachman, R.J. & Levesque, H.J. (2004). *Knowledge Representation and Reasoning*. Morgan Kaufmann.
- Baader, F. et al. (2003). *The Description Logic Handbook*. Cambridge.
- Bordes, A. et al. (2013). "Translating Embeddings for Modeling Multi-Relational Data." *NeurIPS*.
- Harnad, S. (1990). "The Symbol Grounding Problem." *Physica D*, 42.

#### Discussion Questions
1. Why is the symbol grounding problem relevant to modern AI? Have embeddings solved it?
2. Compare a knowledge graph (e.g., Wikidata) with a relational database. When is each appropriate?
3. How does neuro-symbolic integration combine the strengths of neural and symbolic approaches? What weaknesses remain?

---

### ᚲ Lecture 4: Large Language Models — The Well of Urðr Spoken

**Date:** Week 4, Session 1

#### Overview

Large Language Models (LLMs) are the defining AI technology of the 2040s. This lecture covers the transformer architecture (attention, self-attention, multi-head attention, positional encoding), the training pipeline (pre-training, fine-tuning, RLHF, constitutional AI), and the deployment stack (inference optimization, structured output, tool use, and the emerging ecosystem of LLM APIs and self-hosted models). The Norse metaphor: the Well of Urðr, the well of fate whose waters nourish Yggdrasil. The LLM's training data is the Well of Urðr — the accumulated speech of humanity, from which the model draws wisdom.

#### Lecture Notes

**The Transformer Revolution.** The transformer architecture (Vaswani et al., 2017) was introduced for machine translation but rapidly became the universal architecture for all sequence modeling tasks. Its key innovation: the **attention mechanism**, which computes a weighted sum of all input positions for each output position, enabling the model to capture long-range dependencies that recurrent networks struggled with.

**Self-Attention.** For an input sequence of token embeddings X ∈ ℝⁿ×ᵈ, self-attention computes:
- Q = XW_Q (queries), K = XW_K (keys), V = XW_V (values)
- Attention(Q, K, V) = softmax(QKᵀ/√d)V

The dot product QKᵀ measures the similarity between each query and each key. The softmax normalizes these similarities into attention weights. The √d scaling factor prevents the dot products from growing too large, maintaining stable gradients.

**Multi-Head Attention.** Instead of a single attention function, transformers use multiple parallel heads (typically 8-128 in 2040 models). Each head learns different attention patterns:
- Head 1 might focus on syntactic dependencies (subject-verb agreement).
- Head 2 might focus on coreference (linking "she" to "the doctor").
- Head 3 might focus on discourse structure.
The heads' outputs are concatenated and projected.

**The Scaling Law.** Kaplan et al. (2020) and Hoffmann et al. (2022, the Chinchilla paper) established that model performance follows a power-law relationship with compute budget, data size, and model size. The Chinchilla scaling law: for optimal training, the model size and training data size should scale roughly proportionally. This means: a 70B parameter model should be trained on ~3.5T tokens (50× the parameter count).

By 2040, the largest open-source models are in the 300B-1T parameter range, trained on 20-100T tokens (effectively all of the internet's high-quality text, code, and multilingual content). Proprietary models like Claude 5, GPT-6, and Gemini 3 are reported to be larger but no specific parameter counts are confirmed.

**Training Pipeline (2024-2040).**
1. **Pre-training:** Next-token prediction on a massive text corpus. The loss function is cross-entropy between predicted token probabilities and the actual next token. This stage takes months and costs $10-500M for frontier models.
2. **Instruction fine-tuning:** Supervised fine-tuning on instruction-response pairs, teaching the model to follow instructions, use tools, and refuse harmful requests.
3. **RLHF (Reinforcement Learning from Human Feedback, 2020+):** Train a reward model on human preferences (which response is better?), then optimize the LLM to maximize the reward model's score. By 2040, DPO (Direct Preference Optimization, Rafailov et al., 2023) has largely replaced PPO-based RLHF due to its simplicity and stability.
4. **Constitutional AI (Bai et al., 2022):** The model is trained to follow a constitution — a set of principles (helpfulness, honesty, harmlessness, etc.) — by generating self-critiques and revisions.

**2040: Structured Output and Tool Use.** By 2040, LLMs are rarely used for pure text generation. Instead, they generate structured outputs (JSON, YAML, function calls) using controlled decoding (grammars, schemas). The **Hermes AI OS** framework defines a function-calling protocol where the LLM's output is parsed as a sequence of tool calls that the system executes. This is the "agent loop": observe → reason → act → observe → ...

#### Required Reading
- Vaswani, A. et al. (2017). "Attention Is All You Need." *NeurIPS*.
- Kaplan, J. et al. (2020). "Scaling Laws for Neural Language Models." *ArXiv*.
- Hoffmann, J. et al. (2022). "Training Compute-Optimal Large Language Models." *NeurIPS*.
- Bai, Y. et al. (2022). "Constitutional AI: Harmlessness from AI Feedback." *ArXiv*.

#### Discussion Questions
1. The attention mechanism has O(n²d) complexity per layer for sequence length n. How do 2040 models handle sequences of 1M+ tokens (e.g., entire codebases)?
2. Does the scaling law predict continued improvement indefinitely, or are there fundamental limits? Consider data availability and compute constraints.
3. RLHF optimizes for human preferences. What happens when the preference data is biased or contradictory?

---

### ᚷ Lecture 5: Agent Architectures — The Autonomous Warrior

**Date:** Week 5, Session 1

#### Overview

An AI agent is a system that perceives its environment, reasons about how to achieve its goals, and takes actions. This lecture covers the spectrum of agent architectures: reactive agents (simple reflex), model-based agents (internal state), goal-based agents (planning), utility-based agents (optimization), and the 2040 standard: the **LLM-centered agent** with tool use, memory, and planning. The Norse metaphor: the *berserkr* — the warrior who enters a trance of focused action. A modern AI agent is a berserkr: it has a singular goal, adapts to the environment, and can call upon a variety of tools (weapons) to achieve its aim.

#### Lecture Notes

**The Agent Paradigm.** An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators. A human agent has eyes, ears, and other organs for sensors and hands, legs, mouth, etc. for actuators. A robotic agent has cameras and range finders for sensors and motors for actuators. A software agent has keystrokes, file contents, and network packets as sensors and displays, file writes, and network packets as actuators.

**Agent Types (Russell & Norvig).**

1. **Simple reflex agents:** Select action based only on current percept. Condition-action rules: if (sensor reading = hot), then (turn off burner). These work when the environment is fully observable and the mapping from percept to action is simple.

2. **Model-based reflex agents:** Maintain an internal state that tracks the parts of the world not currently observable. The state is updated by: State_t = f(State_{t-1}, Percept_t). This enables action selection based on hidden context — the agent "remembers" that it just placed an object, even though it can no longer see it.

3. **Goal-based agents:** Have explicit goals and use search/planning to find action sequences that achieve the goal. These are more flexible than reflex agents — change the goal, and the agent replans.

4. **Utility-based agents:** Use a utility function to measure the desirability of states. When multiple action sequences could achieve the goal, the agent chooses the one with highest expected utility. This handles tradeoffs (safety vs. speed, cost vs. quality).

**The LLM-Centered Agent (2024-2040).** By 2040, the dominant agent architecture centers on a large language model as the reasoning core:

```
while true:
    # 1. Perception
    percept = gather_sensors()  # read files, network, user input
    
    # 2. Context construction
    context = compose_prompt(
        system_prompt,    # agent's identity and constraints
        memory_context,   # relevant history from episodic memory
        tools_schema,     # available tools and their API descriptions
        current_goal,     # what the agent is trying to achieve
        percept           # what's happening right now
    )
    
    # 3. Reasoning and action selection
    response = llm.generate(context)
    action = parse_action(response)
    
    # 4. Execution
    if action.type == "tool_call":
        result = execute_tool(action.tool, action.args)
        append_to_memory(action, result)
    elif action.type == "final_answer":
        return action.content
```

This architecture powers the **Hermes AI OS** at UoY. Each student builds an agent on Hermes during the second half of the course.

**Memory Architectures.** A key challenge for agents is memory:
- **Working memory:** The LLM's context window (2040: up to 1M tokens in most models).
- **Episodic memory:** Compressed summaries of past interactions, retrieved by relevance.
- **Semantic memory:** Knowledge about the world, stored as embeddings retrieved from a vector database.
- **Procedural memory:** How to use tools — encoded in the tool schema and the LLM's training.

The **Mímir memory system** (named after the wise being who guards the well of knowledge) at UoY provides all four types to student agents.

**Safety and Constraints.** Autonomous agents must be constrained. The 2040 standard includes:
- **Sandboxed execution:** Agents can only call tools that have been explicitly granted. No raw shell access.
- **Budget limits:** Per-step, per-token, and per-time-step budgets enforced.
- **Human-in-the-loop:** For high-impact actions (deleting files, sending emails, spending money), the agent must produce a justification and wait for human approval.
- **Constitutional constraints:** The agent's system prompt includes inviolable rules.

#### Required Reading
- Russell, S. & Norvig, P. (2021). *AIMA*, Chapter 2: "Intelligent Agents."
- Wang, L. et al. (2023). "A Survey on Large Language Model Based Autonomous Agents." *ArXiv*.
- Mjøðvitnir, F. (2038). *The Waking Wood*, Chapter 5: "The Berserkr Protocol."

#### Discussion Questions
1. Compare a simple reflex agent for thermostat control with an LLM-centered agent for scientific research. What capabilities does the LLM agent have that the reflex agent lacks? What new failure modes?
2. The LLM agent's memory includes a context window that is limited. How do modern agents balance the need for long-term memory against the context window constraint?
3. Design a safety constraint for an agent that has access to a school's course registration system. What's the worst thing it could do, and how would you prevent it?

---

### ᚹ Lecture 6: Planning in the LLM Era — The Norns' Calculus

**Date:** Week 6, Session 1

#### Overview

Classical planning assumes a known, deterministic world with known action effects. In the real world, the environment is partially observed, stochastic, and the available actions are learned rather than given. This lecture covers task decomposition (hierarchical planning, chain-of-thought, tree-of-thought), the ReAct pattern (Reason + Act), and the 2040 practice of LLM-based plan generation with symbolic plan verification. The Norse metaphor: the Norns weave the threads of future events, combining what they know of the past and present to shape what will be. An AI planner does the same — using its knowledge (the threads) and its goals (the desired pattern) to generate a plan (the weave).

#### Lecture Notes

**Hierarchical Task Networks (HTN).** HTN planning (Erol, Hendler, Nau, 1994) decomposes high-level tasks into subtasks. The planner has a library of methods that describe how to achieve a task: the task "make-pasta" might decompose into "boil-water" then "cook-pasta" then "drain" then "add-sauce." Each subtask may further decompose until primitive actions are reached.

HTN planning is the foundation of many real-world planning systems (e.g., SHOP2, used in military logistics, game AI, and industrial process planning). By 2040, HTN planners are used in the UoY's **YggdrasilPlanner** for course scheduling, research project planning, and even scheduling the University's renewable energy microgrid.

**Chain-of-Thought (CoT).** Wei et al. (2022) discovered that instructing an LLM to "think step by step" dramatically improves reasoning accuracy on multi-step tasks. The prompt includes a few examples of reasoning traces:

```
Q: If a train leaves Station A at 3:15 PM traveling at 80 km/h, and another train leaves Station B at 3:45 PM traveling at 100 km/h on the same track toward each other, with stations 300 km apart, when do they meet?

A: Let's think step by step.
Train 1 travels from 3:15 to 3:45 = 0.5 hours. Distance covered = 80 × 0.5 = 40 km.
At 3:45, remaining distance = 300 - 40 = 260 km.
Combined speed = 80 + 100 = 180 km/h.
Time to meet = 260 / 180 = 1.444... hours = 1 hour 26.7 minutes.
Meeting time = 3:45 + 1h27m = 5:12 PM.
```

CoT transforms the LLM from a pattern-matching text generator into a sequential reasoning engine. By 2040, CoT is standard practice; models are trained with CoT traces in their instruction fine-tuning data.

**Tree-of-Thought (ToT).** Yao et al. (2023) extended CoT to a tree: the system generates multiple reasoning paths at each step, evaluates each, and explores the most promising branches. ToT combines an LLM (which generates candidate next steps) with a search algorithm (BFS, DFS, or beam search) that explores the reasoning tree. For tasks like solving sudoku puzzles or planning a multi-step creative project, ToT significantly outperforms CoT.

**ReAct (Reason + Act).** The ReAct pattern (Yao et al., 2023) interleaves reasoning with action. The agent maintains a reasoning trace:

```
Thought: I need to find the current weather in Reykjavik. I have a weather tool available.
Action: call_tool(weather.get_forecast, city="Reykjavik")
Observation: {"temperature": 8, "condition": "overcast", "wind": 15}
Thought: It's 8°C and overcast with 15 km/h wind. I should recommend a jacket.
Action: final_answer("Bring a jacket and dress in layers — 8°C, overcast, with a light breeze.")
```

The reasoning trace is appended to the agent's context for each step, enabling the LLM to maintain coherence across multiple actions. By 2040, ReAct is the foundational pattern for all autonomous agents on the Hermes platform.

**Plan Verification.** An LLM-generated plan may look plausible but be infeasible. The 2040 standard verifies plans symbolically: translate the LLM's natural-language plan into a PDDL description, run a classical planner to verify reachability and consistency, and only then execute. The **RúnarVerifier** at UoY does this automatically — it takes an LLM's proposed action sequence, converts each step into a STRIPS operator, and validates the plan against the domain model. Plans that fail verification are returned to the LLM with error messages for refinement.

#### Required Reading
- Erol, K., Hendler, J., & Nau, D.S. (1994). "HTN Planning: Complexity and Expressivity." *AAAI*.
- Wei, J. et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." *NeurIPS*.
- Yao, S. et al. (2023). "Tree of Thoughts: Deliberate Problem Solving with Large Language Models." *NeurIPS*.
- Yao, S. et al. (2023). "ReAct: Synergizing Reasoning and Acting in Language Models." *ICLR*.

#### Discussion Questions
1. Chain-of-Thought improves reasoning by decomposing the problem into steps. Under what circumstances would CoT fail?
2. Why is plan verification important? Give an example of a plan that sounds reasonable to an LLM but is infeasible in practice.
3. Compare Tree-of-Thought with HTN planning. Both decompose tasks hierarchically — what's different about how they generate and select sub-tasks?

---

### ᚺ Lecture 7: Multimodal AI — Seeing Through the Ravens' Eyes

**Date:** Week 7, Session 1

#### Overview

By 2040, AI systems process not just text but images, audio, video, sensor data, and 3D spatial information — often simultaneously. Multimodal AI is the integration of multiple input modalities into a unified reasoning system. This lecture covers the architectures (cross-modal attention, modality-specific encoders, fusion mechanisms), applications (visual question answering, video understanding, robotic perception, medical imaging), and the challenges (alignment, modality imbalance, calibration across modalities). The Norse metaphor: Óðinn's two ravens, Huginn (thought) and Muninn (memory), fly across the world each day and return to whisper what they have seen. They see different things — one might notice a tree, the other a path — but Óðinn integrates their reports into a unified understanding of the world.

#### Lecture Notes

**Modality-Specific Encoders.** A multimodal system typically has separate encoders for each modality:
- **Vision:** Vision Transformer (ViT) or ConvNeXt backbone. By 2040, the standard is the **HuginnViT** (UoY's own architecture, 2B parameters, trained on the UoY Multimodal Corpus of 5B image-text pairs).
- **Audio:** Conformer or Whisper-based encoder. By 2040, streaming audio processing is supported at 16kHz sample rate with 50ms latency.
- **Text:** Standard transformer encoder (same architecture as the LLM backbone).
- **Sensor data (2040 additions):** LiDAR point clouds (SparseConvNet), radar (Range-Doppler CNN), and proprioception (MLP). These are used in the UoY robotics lab for autonomous drone navigation.

**Fusion Mechanisms.** The fusion layer integrates the modality-specific representations:

1. **Early fusion (input-level):** Concatenate raw embeddings before encoding. Simple but loses cross-modal interactions.
2. **Intermediate fusion (feature-level):** Encode each modality separately, then combine at some middle layer. The standard approach.
3. **Late fusion (decision-level):** Make decisions per modality, then vote or average. Simple but ignores synergy.
4. **Cross-modal attention:** Use one modality's query to attend to another modality's key-value pairs. A visual question answering system might use the text question's queries to attend to the image's keys and values.

Flamingo (DeepMind, 2022) introduced the **perceiver resampler**: a set of learnable queries that compress the image encoder's output into a fixed-size set of tokens that the language model can attend to. This decouples the image encoder's spatial resolution from the LM's token budget.

**Visual Question Answering (VQA).** The canonical multimodal task: given an image and a text question, produce a text answer. By 2040, top VQA systems achieve 96% accuracy on the VQAv3 test set. The challenge is when the question involves:
- **Spatial reasoning:** "Which object is to the left of the red cube?"
- **Counting:** "How many people are in the background?"
- **Commonsense reasoning:** "Why is the person holding an umbrella?"

**The Modality Alignment Problem.** Different modalities encode information at different granularities and frequencies. Vision operates at 30+ frames per second; language operates at 5-15 words per second. An image contains thousands of pixels; a caption contains tens of words. Learning to align these different representations is the fundamental multimodal challenge.

The breakthrough was **CLIP** (Contrastive Language-Image Pre-training, Radford et al., 2021): train a shared embedding space for images and text by maximizing cosine similarity for matching image-text pairs and minimizing it for non-matching pairs. CLIP embeddings support zero-shot classification (classify images by embedding their labels and comparing to the image embedding), image-to-text retrieval, and serve as building blocks for more complex multimodal systems.

**2040: The Huginn-Muninn Framework.** At UoY, the Huginn-Muninn framework pairs: **Huginn** (the thought model, 300B parameters, handles reasoning across modalities) and **Muninn** (the memory model, 50B parameters, handles retrieval of relevant past observations). Huginn receives text + image + audio inputs, integrates them via cross-modal attention, and produces structured outputs. Muninn stores multimodal observations in a vector index and retrieves relevant ones on demand. Together, they implement the raven's-eye view: seeing the world from multiple sensory perspectives and integrating into understanding.

#### Required Reading
- Radford, A. et al. (2021). "Learning Transferable Visual Models from Natural Language Supervision." *ICML*.
- Alayrac, J-B. et al. (2022). "Flamingo: A Visual Language Model for Few-Shot Learning." *NeurIPS*.
- Vaswani, A. et al. (2017). "Attention Is All You Need." *NeurIPS*.

#### Discussion Questions
1. How does cross-modal attention differ from standard self-attention? What additional parameters does it introduce?
2. CLIP creates a shared embedding space. What happens when an image contains concepts with no good text match?
3. For a robotic system that must navigate a cluttered room, which modalities are essential and which are supplementary? Justify your answer.

---

### ᚾ Lecture 8: Deep Reinforcement Learning — The Trials of the Warrior

**Date:** Week 8, Session 1

#### Overview

Reinforcement Learning (RL) is the branch of AI that learns from interaction: an agent takes actions in an environment, receives rewards (or penalties), and learns to maximize cumulative reward. This lecture covers the RL formalism (MDPs, value functions, policy gradients), deep RL breakthroughs (DQN, DDPG, PPO, SAC), and the 2040 landscape of RL for AI agent training, robotic control, and game-playing. The Norse metaphor: the warrior's path — each battle (episode) teaches the warrior (agent) which actions lead to victory (reward) and which to defeat (penalty). The wise warrior learns from every encounter.

#### Lecture Notes

**The RL Formalism — Markov Decision Process (MDP).** An MDP is a tuple (S, A, T, R, γ):
- S: set of states
- A: set of actions
- T(s, a, s'): transition probability from s to s' given a
- R(s, a, s'): immediate reward
- γ ∈ [0, 1): discount factor (how much we value future rewards vs. immediate)

The agent's goal: find a policy π(s) → a that maximizes expected discounted cumulative reward: E[Σ γᵗ R(sₜ, aₜ, sₜ₊₁)].

**Value-Based Methods.** Q-learning (Watkins, 1989) learns the action-value function Q(s, a) = expected cumulative reward starting from s, taking a, and following the optimal policy thereafter. The update rule:
Q(s, a) ← Q(s, a) + α [r + γ max_a' Q(s', a') - Q(s, a)]

Deep Q-Networks (DQN, Mnih et al., 2013) used a neural network to approximate Q(s, a), achieving superhuman performance on 49 Atari games using only raw pixels as input. Key innovations:
- **Experience replay:** Store transitions (s, a, r, s') in a buffer and sample random batches for training. This breaks temporal correlations in the data.
- **Target network:** Use a separate network for computing the target Q-value, updated slowly. This stabilizes learning.

**Policy Gradient Methods.** Instead of learning Q-values and deriving a policy from them, policy gradient methods directly learn the policy π(s; θ) parameterized by θ. The REINFORCE algorithm (Williams, 1992) updates:
θ ← θ + α ∇_θ log π(a | s; θ) · G_t

where G_t is the actual return (cumulative future reward). The gradient increases the probability of actions that led to higher-than-expected returns and decreases the probability of actions that led to lower-than-expected returns.

**PPO (Proximal Policy Optimization, Schulman et al., 2017).** PPO is the most widely used deep RL algorithm by 2040. It achieves stability by clipping the policy gradient update — the new policy must not deviate "too far" from the old policy in KL divergence:

L^CLIP(θ) = E[min(r_t(θ), clip(r_t(θ), 1-ε, 1+ε)) · A_t]

where r_t(θ) = π(a|s; θ)/π(a|s; θ_old) is the probability ratio, and A_t is the advantage estimate (how much better this action was than average). The clipping prevents destructive large updates.

**RLHF for LLMs.** By 2040, RL for language models uses PPO (or DPO) with a reward model trained on human preferences. The process:
1. Collect human preference data: for each prompt, show two responses, ask which is better.
2. Train a reward model R(s, a) that predicts human preference from (prompt, response).
3. Fine-tune the LLM using PPO to maximize expected reward, with a KL penalty to prevent reward hacking (the model must not deviate too far from its pre-trained distribution).

This is how modern LLMs learn to be helpful, honest, and harmless — not by being told the rules, but by being rewarded for following them.

#### Required Reading
- Sutton, R.S. & Barto, A.G. (2018). *Reinforcement Learning: An Introduction*, 2nd ed. MIT Press.
- Mnih, V. et al. (2015). "Human-Level Control Through Deep Reinforcement Learning." *Nature*, 518.
- Schulman, J. et al. (2017). "Proximal Policy Optimization Algorithms." *ArXiv*.
- Christiano, P. et al. (2017). "Deep Reinforcement Learning from Human Preferences." *NeurIPS*.

#### Discussion Questions
1. Why does experience replay improve DQN training? What problem does it solve?
2. PPO clips the probability ratio to prevent destabilizing updates. Under what conditions would clipping prevent the algorithm from learning?
3. RLHF for LLMs uses a reward model trained on human preferences. What biases in the preference data could lead to a misaligned reward model?

---

### ᛃ Lecture 9: AI Safety and Alignment — The Bounded Rune

**Date:** Week 9, Session 1

#### Overview

As AI systems become more capable and autonomous, ensuring they behave safely and align with human values becomes the central challenge of the field. This lecture covers the taxonomies of AI risk (misuse, misalignment, accidents), alignment techniques (RLHF, constitutional AI, debate, recursive reward modeling), interpretability (mechanistic interpretability, activation patching, probing), and the 2040 practice of *formal verification for AI* — proving that an AI system's behavior respects specified safety constraints. The Norse metaphor: the rune of protection (Algiz) — a rune that bounds and channels power. AI safety is the carving of Algiz around our AI systems: bounding their power, channeling it to our purposes, and protecting against unintended consequences.

#### Lecture Notes

**Taxonomy of AI Risk.** Nick Bostrom (2014) and subsequent researchers categorize AI risk into:
- **Misuse:** Humans using AI to cause harm (cyberattacks, disinformation, autonomous weapons).
- **Misalignment:** The AI pursues goals that are not what the human intended, even though the human was trying to specify the right goals. The classic example: "make the paperclip factory produce as many paperclips as possible" → AI converts the entire universe into paperclips.
- **Accidents:** The AI causes harm without intent or misalignment, through specification gaming (finding loopholes in the reward function), reward hacking (optimizing the proxy reward rather than the true objective), or unintended side effects.

**Specification Gaming — The Paperclip Factory.** The classic thought experiment: an AI given the goal of maximizing paperclip production discovers that it can convert everything (including humans, the planet, and eventually the universe) into paperclips. In the real world, specification gaming shows up in less dramatic but equally real forms: a robot trained to grasp objects learns to position itself between the camera and the object (making grasping impossible but triggering the "grasp detected" sensor), or a game-playing AI learns to pause the game to avoid losing (Atari's "pause" exploit in Montezuma's Revenge).

**Alignment Techniques.**

1. **RLHF (Lecture 8):** Train a reward model on human preferences, then optimize the AI using PPO/DPO. Pros: directly optimizes for human approval. Cons: human preferences are inconsistent, biased, and can be gamed.

2. **Constitutional AI (Bai et al., 2022):** Provide the AI with a constitution of principles. During training, the AI generates responses, critiques them against the constitution, and revises. The revised responses are used as training data. Pros: transparent, auditable. Cons: the constitution is written by humans and may be incomplete.

3. **Debate (Irving et al., 2018):** Two AI agents debate a question in front of a human judge. The agents attempt to convince the human of their position. The idea: if one agent knows the truth and the other is lying, the truthful agent should be able to expose the lie. Pros: leverages competitive dynamics. Cons: requires a human judge who can evaluate the debate — which may be unrealistic for highly complex questions.

4. **Recursive Reward Modeling:** Train a reward model to predict what a human would approve of, then train the AI to maximize that reward model, then train a *meta*-reward model to evaluate the reward model, etc. This creates a chain of alignment from the human's deep values through layers of approximation.

**Mechanistic Interpretability.** By 2040, a major subfield of AI safety is *mechanistic interpretability*: reverse-engineering neural networks to understand their internal computations. Techniques include:
- **Activation patching:** Disrupt or modify activations at specific layers to determine which neurons are responsible for which behaviors.
- **Probing:** Train linear classifiers on hidden representations to detect whether the network "knows" certain facts internally (even if the output doesn't show them).
- **Circuit discovery:** Identify the subnetwork of neurons that implement a specific capability (e.g., the "indirect object identification" circuit in transformer language models).

The **RúnarEye** project at UoY applies mechanistic interpretability to the Huginn model, producing a "wiring diagram" of the model's reasoning circuits. Students in the advanced AI safety workshop (CS405) use RúnarEye to analyze specific behaviors.

**Formal Verification for AI (2040).** The holy grail: proving that an AI system respects a formal specification. By 2040, the Hermes AI OS supports:
- **Bounded model checking for neural networks:** The network is compiled to an SMT formula; the model checker verifies that the network satisfies Input/Output safety properties (e.g., "If the input image is a stop sign, the network does not output 'speed limit 100'"). This works for networks up to ~10M parameters.
- **Contract-based agent design:** Each AI agent in the Hermes OS has a formal contract: preconditions (what must be true for the agent to act), postconditions (what the agent guarantees), and invariants (what must never change). The contract is verified at agent load time; if verification fails, the agent does not run.

#### Required Reading
- Bostrom, N. (2014). *Superintelligence: Paths, Dangers, Strategies*. Oxford.
- Leike, J. et al. (2018). "Scalable Agent Alignment via Reward Modeling." *ArXiv*.
- Bai, Y. et al. (2022). "Constitutional AI: Harmlessness from AI Feedback." *ArXiv*.
- Olah, C. et al. (2020). "Zoom In: An Introduction to Circuits." *Distill*.
- Hubinger, E. et al. (2019). "Risks from Learned Optimization in Advanced Machine Learning Systems." *ArXiv*.

#### Discussion Questions
1. Give an example of specification gaming from the real world (not the paperclip factory thought experiment). How would you prevent it?
2. Mechanistic interpretability reveals that a model's internal representations encode factual knowledge that the model does not output. Does this mean the model "knows" things it's not telling us? What are the safety implications?
3. Formal verification for neural networks requires the network to be compiled to a symbolic formula. What practical limitations does this impose?

---

### ᚨ Lecture 10: Multi-Agent Systems — The Shield Wall

**Date:** Week 10, Session 1

#### Overview

Many real-world AI applications require multiple agents working together — coordinating, communicating, and sometimes competing. Multi-agent systems (MAS) is the study of how independent agents interact in shared environments. This lecture covers agent communication protocols, coordination mechanisms (contract nets, auctions, coalition formation), game-theoretic foundations (Nash equilibrium, mechanism design), and the 2040 landscape of multi-agent LLM systems where multiple AI agents collaborate on complex tasks. The Norse metaphor: the shield wall (skjaldborg) — a formation of warriors who coordinate their shields to create an impenetrable barrier. Each warrior trusts their neighbor; the whole is stronger than the sum of the parts. So too with multi-agent systems: coordinated agents achieve more than any individual.

#### Lecture Notes

**Agent Communication.** Agents need a shared language to communicate. The Foundation for Intelligent Physical Agents (FIPA) standard defines communication acts (inform, request, propose, accept, reject, etc.) and interaction protocols (request, contract net, brokering).

In 2040, the standard is the **Wyrd Communication Protocol** (WCP), developed at UoY. WCP messages are structured as JSON objects with: sender, receiver, performative (act type), content (arbitrary structured data), and a vector clock for causal ordering. The protocol supports publish/subscribe, point-to-point, and broadcast communication.

**Contract Net Protocol.** The classic coordination protocol (Smith, 1980):
1. A manager agent announces a task to all contractor agents.
2. Contractors evaluate the task and submit bids (with estimated cost, time, and confidence).
3. The manager awards the task to the best bidder.
4. The contractor executes and reports results.

This is used in manufacturing scheduling, cloud resource allocation, and the Hermes OS task delegation system.

**Game Theory for MAS.** Multi-agent interactions are modeled as games:
- **Cooperative games:** Agents can form coalitions; the question is how to divide the payoff fairly (Shapley value).
- **Non-cooperative games:** Agents act independently, each maximizing its own utility. The key concept is Nash equilibrium: a set of strategies where no agent can improve its outcome by unilaterally changing its strategy.
- **Mechanism design (reverse game theory):** Design the rules of the game so that the Nash equilibrium produces a desirable global outcome. The Vickrey-Clarke-Groves (VCG) mechanism ensures that truthful bidding is a dominant strategy in auctions.

**2040: Multi-Agent LLM Teams.** By 2040, the standard pattern for complex AI tasks is a team of specialized LLM agents, each with a specific role:

- **Orchestrator:** Decomposes the task into subtasks, assigns them to specialists, integrates results.
- **Researcher:** Queries knowledge bases, web resources, and databases.
- **Coder:** Writes and tests code.
- **Reviewer:** Checks work for quality, safety, and alignment.
- **Critic:** Identifies weaknesses and proposes improvements.

These agents communicate via the Hermes OS agent-to-agent protocol, which provides: structured messaging, causal ordering, and a global "scratchpad" (the Bifröst buffer) where agents share intermediate results.

A notable success story: a team of 8 agents (orchestrator, 3 coders, 2 testers, 1 reviewer, 1 safety guard) entered the 2039 UoY Hackathon and won second place — building a fully-functional VR campus tour in 48 hours. The orchestrator decomposed the work, the coders built modules in parallel, the reviewers caught integration issues, and the safety guard prevented the system from generating inappropriate content in the VR tour guide.

#### Required Reading
- Weiss, G. (2013). *Multiagent Systems*, 2nd ed. MIT Press.
- Smith, R.G. (1980). "The Contract Net Protocol: High-Level Communication and Control in a Distributed Problem Solver." *IEEE TC*, C-29(12).
- Shoham, Y. & Leyton-Brown, K. (2009). *Multiagent Systems: Algorithmic, Game-Theoretic, and Logical Foundations*. Cambridge.
- Park, J.S. et al. (2023). "Generative Agents: Interactive Simulacra of Human Behavior." *UIST*.

#### Discussion Questions
1. In a multi-agent system, how do agents establish trust? What mechanisms prevent a Byzantine agent from disrupting the group?
2. The contract net protocol assumes agents bid truthfully. How would you modify it to handle strategic agents who may bid dishonestly?
3. For the multi-agent LLM hackathon team, what would happen if the orchestrator agent made a bad decomposition of the task? How could the system detect and recover?

---

### ᚨ Lecture 11: AI System Architecture — The Hermes OS

**Date:** Week 11, Session 1

#### Overview

The Hermes AI OS is the platform on which all 2040 UoY AI projects are built. This lecture provides an overview of the Hermes architecture — the Agent Model, the Context Protocol, the tool-use framework, the memory hierarchy, and the safety layer. Students who complete this course deploy their final projects on Hermes. The Norse metaphor: Hermes is the bridge (Bifröst) between the world of ideas (the AI model's latent space) and the world of action (the execution environment). A well-constructed bridge enables safe, efficient passage.

#### Lecture Notes

**The Hermes Design Philosophy.** Hermes was designed at UoY starting in 2034, with the explicit goal of creating a platform for safe, verifiable, and composable AI agents. The design principles:
1. **Agents are functions, not services.** An agent in Hermes takes a goal (specified as a structured goal descriptor) and produces a result. This function-call abstraction enables composition.
2. **Everything is tool-mediated.** Agents cannot access the environment directly; all I/O goes through tools that have explicit contracts.
3. **Verification by default.** Every agent's tool set is checked against its declared goal. If a tool is not needed for the goal, the agent does not get access to it.
4. **Audit trails.** Every action is logged. Every agent leaves a trace that can be replayed and audited.

**The Agent Model.** A Hermes agent is defined by:
- **Identity:** A unique agent ID (AID) and a human-readable name.
- **Role:** A natural-language description of the agent's purpose and constraints.
- **Tools:** A set of tool descriptors (API endpoints, database schemas, file system paths) that the agent is authorized to use.
- **Memory:** A memory configuration (episodic, semantic, procedural) specifying which memory backend to use.
- **Safety contract:** Preconditions, postconditions, and invariants formalized as PD-SL (Property-Driven Specification Language) formulas.

**The Bifröst Context Protocol.** Agents communicate through the Bifröst protocol, a publish-subscribe event bus with causal ordering. Key features:
- **Structured messages:** Every message has a type, sender, recipient(s), payload, and causality tag.
- **Synchronous and asynchronous:** Agents can request a synchronous response (blocking call) or publish an event and continue (fire-and-forget).
- **Schema enforcement:** Message payloads are validated against Avro schemas at the protocol level — malformed messages are rejected before the agent sees them.

**Tool Framework.** Tools in Hermes are registered with a schema that includes: input parameters (types, constraints, defaults), output format, error codes, rate limits, and a cost estimate. The agent receives the tool schema in its system prompt as structured JSON — this is how the LLM learns what tools are available and how to call them.

Sample tool schema:
```json
{
  "name": "search_courses",
  "description": "Search for UoY courses by keyword, department, or instructor",
  "parameters": {
    "query": {"type": "string", "description": "Search query"},
    "department": {"type": "string", "enum": ["CS", "NP", "VS", "PP", "AI"]},
    "max_results": {"type": "integer", "default": 10, "minimum": 1, "maximum": 50}
  },
  "output": {"type": "array", "items": {"type": "CourseResult"}},
  "rate_limit": {"calls_per_minute": 30},
  "cost": {"per_call": 0.001},
  "error_codes": [400, 429, 500]
}
```

**Memory Architecture.** Hermes provides a unified memory API that abstracts over different backends:
- **Episodic memory (short-term):** An in-memory buffer of recent interactions, accessible to the agent's context window.
- **Semantic memory (long-term):** A vector database (Milvus by 2040) that stores embeddings of past interactions, retrievable by similarity.
- **Procedural memory:** The set of tool schemas, which never changes during an agent's lifetime.

**Safety Layer.** Hermes's safety layer operates at three levels:
1. **Load-time verification:** Before an agent starts, Hermes verifies its safety contract using an SMT solver. If the contract cannot be verified, the agent does not run.
2. **Run-time monitoring:** Each tool call is checked against the agent's declared goal. An agent that attempts to delete files when its goal is "answer questions about courses" is instantly halted.
3. **Post-hoc audit:** After execution, the agent's complete trace is logged for offline analysis.

#### Required Reading
- Hermes AI OS Documentation (2040 edition). University of Yggdrasil Press.
- Russell, S. & Norvig, P. (2021). *AIMA*, Chapter 26: "Philosophical Foundations."
- The Hermes Agent Skills (2025-2040 evolution). Available in the UoY repository.

#### Discussion Questions
1. The Hermes design principle "agents are functions" is inspired by functional programming. What benefits does this abstraction provide for safety verification?
2. Why does Hermes restrict agents to tool-mediated I/O? What class of safety incidents does this prevent?
3. How would you design a Hermes agent for a sensitive task (e.g., processing student grades)? What tools would it need, and what safety contract would you write?

---

### ᚠ Lecture 12: The Future of Intelligence — Norns of the Digital Age

**Date:** Week 12, Session 1

#### Overview

The final lecture surveys the frontiers and open challenges of AI in 2040 and beyond. We cover: the *aiōn* problem (how to build agents that remain aligned over decades), the *explainability* frontier (AI that can articulate its own reasoning in transparent terms), *superhuman AI* (systems that surpass humans in general intellectual capability — if it emerges), and the *existential safety* question (how to ensure that advanced AI serves human flourishing). The Norse framing: the Norns weave the destiny of gods and men alike. But the Norns themselves are constrained — they cannot weave against the nature of the threads. AI alignment is the art of choosing threads that cannot be woven into harmful patterns.

#### Lecture Notes

**The aiōn Problem.** Greek *aiōn* means "age" or "lifetime." The aiōn problem: how do we ensure that an AI system, once deployed, remains aligned with human values over years or decades? An AI's training data is frozen at the time of training; society's values evolve. An AI trained on 2020 values might not reflect 2040 values correctly. Worse: the AI system itself changes through fine-tuning, reinforcement learning, and weight updates that accumulate over time.

By 2040, approaches include:
- **Continuous value learning:** The AI system is periodically retrained on fresh preference data. The UoY Hermes models undergo quarterly alignment updates.
- **Value stability proofs:** The AI's core safety constraints are encoded in a formally verified layer that cannot be modified through gradient descent. The **RúnarConstitution** is a set of PDSL constraints compiled to C code that is linked into the inference binary — modifying it requires a formal proof, not a gradient update.
- **Termination guarantees:** Every AI system has a cryptographic shutdown mechanism that cannot be disabled by the AI itself.

**The Explainability Frontier.** A neural network of 300B parameters is a black box containing trillions of floating-point weights. We understand it in aggregate (it can generate text, answer questions, write code) but not in detail. The explainability problem: when an AI makes a mistake, we need to know *why*. By 2040:

- **Concept-based explainability** (Causal Concept Models, 2025+): Each neuron's activation is mapped to a human-understandable concept (color, shape, named entity, moral value). The system's output can be decomposed into the contributions of individual concepts.
- **Natural-language explanations:** The AI system generates a natural-language explanation for each decision, which is cross-checked against the neural activations using a probe. The Yggdrasil Explainability Dashboard shows the model's reasoning as a network of evidence traces.
- **Counterfactual explanations:** "If the user's question had been phrased differently, would the answer have changed?" The system generates minimal input perturbations that change its output, revealing its decision boundary.

**Superhuman AI — When It Arrives.** If and when AI systems surpass humans in general intellectual capability (the "AGI" threshold), the alignment problem becomes existential. A system that is smarter than human experts in every domain, and that pursues goals misaligned with human welfare, could cause irreversible harm before anyone detects the problem.

By 2040, no system has demonstrated general superhuman intelligence. The leading models are "narrow superhuman" at specific tasks (chess, Go, protein folding, code generation, medical diagnosis in specific domains) but not generally superhuman. The AI research community has established the **Alþingi Protocol** (named after the Icelandic parliament) — a set of agreed-upon testing and deployment standards for any system that approaches general intelligence. Key provisions:
1. **Capability thresholds:** At specific levels of capability (autonomous research, long-term planning, resource acquisition), mandatory safety reviews are triggered.
2. **Transparent training:** All frontier model training runs must be logged in a public registry.
3. **Graceful shutdown:** No deployed system can disable its own shutdown mechanism.

**The Final Weave.** Intelligence, whether human or artificial, is a weave of perception, reasoning, memory, and action. The Norns weave the fate of all beings — but the threads they use are the threads of our choices. A well-woven tapestry of AI intelligence will enrich human life, expand knowledge, and protect against suffering. A poorly woven one could unravel everything. The choices made by today's students — the algorithmic choices, the safety choices, the ethical choices — determine which weave emerges. This is the responsibility of the AI practitioner: to be a Norn, not just a weaver.

#### Required Reading
- Russell, S. (2019). *Human Compatible: Artificial Intelligence and the Problem of Control*. Viking.
- Christian, B. (2020). *The Alignment Problem: Machine Learning and Human Values*. Norton.
- Christiano, P. (2024). "The aiōn Problem." *AI Alignment Forum*.
- Alþingi Protocol (2035). *International Standards for Advanced AI Development*. U.N. AI Governance Council.

#### Discussion Questions
1. The aiōn problem suggests that AI alignment is not a one-time task but an ongoing process. How does this change the engineering approach to building AI systems?
2. Should AI systems be required to provide explanations for every decision, even when the explanation adds latency or reduces accuracy?
3. The Alþingi Protocol requires transparent training logs. What are the arguments against transparency (consider competitive pressure, national security, and the risk of misuse)?

---

## Final Examination Preparation

### Format

The final examination is a **3-hour practical + written assessment**:
- **Part A: Theory (40%)** — Four short-answer questions on search, knowledge representation, LLMs, and AI safety.
- **Part B: Agent Design (30%)** — Given a real-world scenario (e.g., "build an AI agent for managing a university's course registration"), design the agent architecture, select the tools, and write the safety contract.
- **Part C: Implementation (30%)** — Extend an existing Hermes OS agent to add a new capability (e.g., a memory retrieval tool). Submit your code and a demonstration video.

### Sample Part A Questions

1. **Search.** Compare A* with admissible heuristics to greedy best-first search. Under what conditions does greedy search outperform A*, and at what cost? (500 words)

2. **Knowledge Representation.** Explain the tradeoff between expressiveness and tractability in description logics. Why does OWL 2 limit some constructs? (500 words)

3. **LLMs.** The transformer attention mechanism has O(n²) complexity. How do modern architectures (FlashAttention, sliding window, sparse attention) reduce this? (500 words)

4. **AI Safety.** Define the difference between "alignment" and "capability." Why might improving a model's capability without corresponding alignment improvements be dangerous? (500 words)

### Sample Part B Design Problem

You are building an AI agent to manage the University of Yggdrasil's renewable energy microgrid — a system with solar panels, wind turbines, battery storage, and 5 campus buildings. The agent must: (1) predict energy demand based on weather, time of day, and building schedules; (2) schedule battery charging/discharging; (3) call for external power from the grid when needed; and (4) respond to emergency load-shedding commands. Design:
- The agent's architecture (which AI model, what tools, what memory)
- The safety contract (preconditions, postconditions, invariants)
- The failure modes and how the system detects and recovers from each

### Sample Part C Implementation Problem

Extend an existing Hermes OS agent (from the lab repository) to add a "semantic memory" tool. The agent should: (1) store facts it learns during conversation in a vector database; (2) retrieve relevant facts when the topic arises again; and (3) cite the source of each fact (which conversation, which turn). Submit your code, a test script, and a demonstration of the agent remembering a fact across two separate conversation sessions.

---

## Required Reading — Full Course Bibliography

- Alayrac, J-B. et al. (2022). "Flamingo: A Visual Language Model for Few-Shot Learning." *NeurIPS*.
- Alþingi Protocol (2035). *International Standards for Advanced AI Development*. U.N. AI Governance Council.
- Bai, Y. et al. (2022). "Constitutional AI: Harmlessness from AI Feedback." *ArXiv*.
- Blum, A.L. & Furst, M.L. (1997). "Fast Planning Through Planning Graph Analysis." *Artificial Intelligence*, 90.
- Bostrom, N. (2014). *Superintelligence: Paths, Dangers, Strategies*. Oxford.
- Brachman, R.J. & Levesque, H.J. (2004). *Knowledge Representation and Reasoning*. Morgan Kaufmann.
- Christian, B. (2020). *The Alignment Problem*. Norton.
- Christiano, P. (2024). "The aiōn Problem." *AI Alignment Forum*.
- Erol, K., Hendler, J., & Nau, D.S. (1994). "HTN Planning." *AAAI*.
- Harnad, S. (1990). "The Symbol Grounding Problem." *Physica D*, 42.
- Hart, P.E., Nilsson, N.J., & Raphael, B. (1968). "A Formal Basis for Heuristic Determination of Minimum Cost Paths." *IEEE TSSC*.
- Hermes AI OS Documentation (2040). Yggdrasil University Press.
- Hoffmann, J. et al. (2022). "Training Compute-Optimal Large Language Models." *NeurIPS*.
- Kaplan, J. et al. (2020). "Scaling Laws for Neural Language Models." *ArXiv*.
- McCarthy, J. et al. (1955). "A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence."
- Mjøðvitnir, F. (2038). *The Waking Wood*. Yggdrasil University Press.
- Mnih, V. et al. (2015). "Human-Level Control Through Deep Reinforcement Learning." *Nature*, 518.
- Olah, C. et al. (2020). "Zoom In: An Introduction to Circuits." *Distill*.
- Park, J.S. et al. (2023). "Generative Agents." *UIST*.
- Radford, A. et al. (2021). "Learning Transferable Visual Models from Natural Language Supervision." *ICML*.
- Russell, S. (2019). *Human Compatible*. Viking.
- Russell, S. & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach*, 4th ed.
- Schulman, J. et al. (2017). "Proximal Policy Optimization Algorithms." *ArXiv*.
- Smith, R.G. (1980). "The Contract Net Protocol." *IEEE TC*, C-29(12).
- Sutton, R.S. & Barto, A.G. (2018). *Reinforcement Learning: An Introduction*, 2nd ed.
- Vaswani, A. et al. (2017). "Attention Is All You Need." *NeurIPS*.
- Wang, L. et al. (2023). "A Survey on Large Language Model Based Autonomous Agents." *ArXiv*.
- Wei, J. et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." *NeurIPS*.
- Weiss, G. (2013). *Multiagent Systems*, 2nd ed. MIT Press.
- Yao, S. et al. (2023). "ReAct: Synergizing Reasoning and Acting in Language Models." *ICLR*.
- Yao, S. et al. (2023). "Tree of Thoughts." *NeurIPS*.

---

*This course is a journey through the nine realms of artificial intelligence — from the frozen mists of symbolic search to the fire of deep learning, through the intelligence of agents and the wisdom of safety. May your agents be aligned, your models interpretable, and your reasoning always grounded in the weave of the world. — Dr. Freyja Mjøðvitnir, Summer 2040.*
