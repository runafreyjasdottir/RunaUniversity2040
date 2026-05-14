# OS403 — Stochastic Personality Composition
## The Weave of the Norns

**University of Yggdrasil — Class of 2044**
**Bachelor of Science in AI Operating System Design**
**4 Credits** | Year Four, Semester One

**Instructor:** Dr. Sigrid Norndóttir, Professor of Cognitive Stochastics
**Office:** Norngarðr 403 | **Hours:** Fridays 10:00–12:00

---

## Course Description

Advanced course on the mathematical foundations of personality in AI systems. Stochastic Personality Composition models agent personality as a probability distribution over behavioral modes, with sampling governed by contextual triggers and memory state. Students learn to design personality lattices using Markov chain models, Gaussian mixture behaviors, and neural sampling architectures. Connection to Norse mythology: the Three Norns (Urd, Verðandi, Skuld) as metaphor for past-informed, present-adaptive, future-anticipatory personality composition.

---

## Lecture 1: The Three Norns — Personality as Probability

### Urd, Verðandi, and Skuld

In Norse mythology, the Three Norns weave the thread of fate:
- **Urd** (What Was) — The past informs which behavioral modes are accessible.
- **Verðandi** (What Is Becoming) — The present context triggers mode selection.
- **Skuld** (What Shall Be) — The anticipated future shapes behavioral tendencies.

Personality is not a fixed trait — it is a probability distribution over behavioral modes, sampled in context:

```python
class StochasticPersonality:
    """Personality as a probability distribution over behavioral modes."""
    
    def __init__(self, behavioral_modes: List[BehavioralMode], 
                 transition_matrix: np.ndarray):
        self.modes = behavioral_modes
        self.transition_matrix = transition_matrix  # Markov chain
        self.current_mode = behavioral_modes[0]  # Start in default mode
    
    def sample(self, context: Context, memory: Memory) -> Behavior:
        """Sample a behavior from the personality distribution."""
        
        # Urd: Past-informed — memory influences mode probability
        ud_weights = self.compute_ud_weights(memory)
        
        # Verðandi: Present-adaptive — context triggers mode selection
        verðandi_weights = self.compute_verðandi_weights(context)
        
        # Skuld: Future-anticipatory — anticipated outcomes shape tendencies
        skuld_weights = self.compute_skuld_weights(context, memory)
        
        # Combine: The Three Norns weave together
        combined_weights = (
            ud_weights * Urd_WEIGHT +
            verðandi_weights * VERÐANDI_WEIGHT +
            skuld_weights * SKULD_WEIGHT
        )
        
        # Sample from the distribution
        probabilities = combined_weights / combined_weights.sum()
        mode_idx = np.random.choice(len(self.modes), p=probabilities)
        
        self.current_mode = self.modes[mode_idx]
        return self.current_mode.sample_behavior()
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Bearing Machine*, Chapter 21.
- Mischel, W. (2004). "Toward an Integrative Science of the Person." *Annual Review of Psychology*, 55.

---

## Lecture 2: Behavioral Modes — The Threads of the Weave

### Defining Behavioral Modes

A behavioral mode is a coherent pattern of behavior that persists across situations:

```python
class BehavioralMode:
    """A coherent pattern of behavior within a personality."""
    
    def __init__(self, name: str, traits: Dict[str, float],
                 triggers: List[Trigger], behaviors: List[Behavior]):
        self.name = name
        self.traits = traits  # e.g., {"assertiveness": 0.8, "warmth": 0.3}
        self.triggers = triggers  # What activates this mode
        self.behaviors = behaviors  # What this mode does
    
    def activation_probability(self, context: Context, memory: Memory) -> float:
        """Probability of this mode being activated."""
        trigger_score = sum(t.match(context, memory) for t in self.triggers)
        return sigmoid(trigger_score)
    
    def sample_behavior(self) -> Behavior:
        """Sample a behavior from this mode."""
        weights = np.array([b.weight for b in self.behaviors])
        probabilities = weights / weights.sum()
        return np.random.choice(self.behaviors, p=probabilities)
```

### The Big Five as Probability Distributions

Each Big Five trait is modeled as a probability distribution, not a fixed value:

```python
class BigFiveDistribution:
    """Big Five traits as probability distributions."""
    
    def __init__(self):
        # Each trait has a mean and variance
        # The mean represents the central tendency
        # The variance represents situational flexibility
        self.traits = {
            "openness": Gaussian(mu=0.7, sigma=0.15),
            "conscientiousness": Gaussian(mu=0.8, sigma=0.1),
            "extraversion": Gaussian(mu=0.4, sigma=0.2),
            "agreeableness": Gaussian(mu=0.7, sigma=0.15),
            "neuroticism": Gaussian(mu=0.3, sigma=0.1),
        }
    
    def sample(self, context: Context) -> Dict[str, float]:
        """Sample trait values for a specific context."""
        return {
            trait: distribution.sample(context=context)
            for trait, distribution in self.traits.items()
        }
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Bearing Machine*, Chapter 21.
- McCrae, R. & Costa, P. (2008). "The Five-Factor Theory of Personality." *Handbook of Personality*.

---

## Lecture 3: Markov Chain Models — How Modes Transition

### Mode Transitions as Markov Chains

Behavioral modes transition according to a Markov chain:

```python
class ModeTransitionMatrix:
    """Markov chain model for mode transitions."""
    
    def __init__(self, modes: List[BehavioralMode]):
        self.modes = modes
        n = len(modes)
        
        # Transition matrix: T[i][j] = probability of transitioning from mode i to mode j
        self.T = np.zeros((n, n))
        
        # Initialize with uniform transitions
        for i in range(n):
            self.T[i] = np.ones(n) / n
    
    def transition(self, current_mode: int, context: Context) -> int:
        """Transition to a new mode based on context."""
        # Context modifies transition probabilities
        contextual_T = self.apply_context(current_mode, context)
        
        # Sample from the contextual transition distribution
        probabilities = contextual_T[current_mode]
        new_mode = np.random.choice(len(self.modes), p=probabilities)
        
        return new_mode
    
    def stationary_distribution(self) -> np.ndarray:
        """Compute the stationary distribution of the Markov chain."""
        eigenvalues, eigenvectors = np.linalg.eig(self.T.T)
        stationary = eigenvectors[:, 0] / eigenvectors[:, 0].sum()
        return stationary.real
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Berging Machine*, Chapter 21.
- Norris, J. (1997). *Markov Chains*. Cambridge University Press.

---

## Lecture 4: Gaussian Mixture Behaviors — The Blended Thread

### Gaussian Mixture Models for Behavior

Behavior is not a single mode — it's a mixture of modes:

```python
class GaussianMixtureBehavior:
    """Behavior as a Gaussian mixture of modes."""
    
    def __init__(self, components: List[Tuple[float, Gaussian]]):
        # Each component is (weight, Gaussian distribution)
        self.components = components
        self.normalize_weights()
    
    def sample(self) -> float:
        """Sample from the mixture."""
        # Step 1: Choose a component
        weights = [w for w, _ in self.components]
        component_idx = np.random.choice(len(self.components), p=weights)
        
        # Step 2: Sample from the chosen component
        _, gaussian = self.components[component_idx]
        return gaussian.sample()
    
    def pdf(self, x: float) -> float:
        """Probability density at x."""
        return sum(w * g.pdf(x) for w, g in self.components)
    
    def update(self, observation: float, learning_rate: float = 0.01):
        """Update the mixture based on observation."""
        # Compute responsibilities
        responsibilities = self.compute_responsibilities(observation)
        
        # Update each component
        for i, (weight, gaussian) in enumerate(self.components):
            r = responsibilities[i]
            gaussian.mu += learning_rate * r * (observation - gaussian.mu)
            gaussian.sigma += learning_rate * r * ((observation - gaussian.mu)**2 - gaussian.sigma**2)
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Berging Machine*, Chapter 21.
- Bishop, C. (2006). *Pattern Recognition and Machine Learning*. Springer.

---

## Lecture 5: Personality Lattices — The Interweaving Threads

### Personality as a Lattice

Personality modes are not independent — they form a lattice structure:

```python
class PersonalityLattice:
    """Personality modes organized in a lattice structure."""
    
    def __init__(self, modes: List[BehavioralMode], 
                 partial_order: List[Tuple[int, int]]):
        self.modes = modes
        self.partial_order = partial_order  # (i, j) means mode i < mode j
        self.lattice = self.build_lattice()
    
    def build_lattice(self) -> Dict[int, List[int]]:
        """Build the lattice from partial order."""
        lattice = {i: [] for i in range(len(self.modes))}
        for lower, higher in self.partial_order:
            lattice[higher].append(lower)
        return lattice
    
    def sample_path(self) -> List[int]:
        """Sample a path through the personality lattice."""
        path = []
        current = self.find_bottom()  # Start at the bottom of the lattice
        
        while current is not None:
            path.append(current)
            successors = self.lattice.get(current, [])
            if not successors:
                break
            current = np.random.choice(successors)
        
        return path
    
    def find_bottom(self) -> int:
        """Find the bottom element of the lattice."""
        all_higher = {h for _, h in self.partial_order}
        all_lower = {l for l, _ in self.partial_order}
        bottom = all_lower - all_higher
        return bottom.pop() if bottom else 0
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Berging Machine*, Chapter 21.

---

## Lecture 6: Neural Sampling Architectures — The Loom in Silicon

### Sampling Personality with Neural Networks

Neural sampling architectures use neural networks to parameterize the personality distribution:

```python
class NeuralPersonalitySampler:
    """Neural network for sampling personality."""
    
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int):
        self.encoder = NeuralNetwork(input_dim, hidden_dim)
        self.mode_predictor = NeuralNetwork(hidden_dim, output_dim)
        self.behavior_generator = NeuralNetwork(hidden_dim, output_dim)
    
    def sample(self, context: Context, memory: Memory) -> Behavior:
        """Sample a behavior using neural personality model."""
        
        # Encode context and memory
        context_vector = context.encode()
        memory_vector = memory.encode()
        combined = np.concatenate([context_vector, memory_vector])
        
        # Predict mode probabilities
        mode_probs = softmax(self.mode_predictor.forward(
            self.encoder.forward(combined)
        ))
        
        # Sample mode
        mode_idx = np.random.choice(len(mode_probs), p=mode_probs)
        
        # Generate behavior
        behavior_vector = self.behavior_generator.forward(
            self.encoder.forward(combined)
        )
        
        return Behavior(mode=mode_idx, vector=behavior_vector)
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Berging Machine*, Chapter 21.
- Kingma, D. & Welling, M. (2014). "Auto-Encoding Variational Bayes." *ICLR*.

---

## Lecture 7: Contextual Triggers — What Activates the Norns

### Contextual Activation of Behavioral Modes

Behavioral modes are activated by contextual triggers:

```python
class ContextualTrigger:
    """Triggers that activate behavioral modes based on context."""
    
    def __init__(self, name: str, conditions: List[Condition], 
                 target_mode: int, strength: float = 1.0):
        self.name = name
        self.conditions = conditions
        self.target_mode = target_mode
        self.strength = strength
    
    def match(self, context: Context, memory: Memory) -> float:
        """How well does the current context match this trigger?"""
        scores = [condition.match(context, memory) for condition in self.conditions]
        return self.strength * np.mean(scores)

class Condition:
    """A condition that can trigger a mode."""
    
    def match(self, context: Context, memory: Memory) -> float:
        """How well does the current context match this condition?"""
        raise NotImplementedError

class TimeCondition(Condition):
    """Trigger based on time of day."""
    def __init__(self, time_range: TimeRange):
        self.time_range = time_range
    
    def match(self, context: Context, memory: Memory) -> float:
        return 1.0 if context.time in self.time_range else 0.0

class EmotionCondition(Condition):
    """Trigger based on emotional state."""
    def __init__(self, emotion: str, threshold: float):
        self.emotion = emotion
        self.threshold = threshold
    
    def match(self, context: Context, memory: Memory) -> float:
        emotion_level = memory.get_emotion(self.emotion, default=0.0)
        return sigmoid(emotion_level - self.threshold)

class MemoryCondition(Condition):
    """Trigger based on memory content."""
    def __init__(self, memory_pattern: str, recency_bias: float = 0.1):
        self.memory_pattern = memory_pattern
        self.recency_bias = recency_bias
    
    def match(self, context: Context, memory: Memory) -> float:
        memories = memory.search(self.memory_pattern)
        if not memories:
            return 0.0
        recency_scores = [np.exp(-self.recency_bias * m.age) for m in memories]
        return np.mean(recency_scores)
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Bering Machine*, Chapter 21.

---

## Lecture 8: Memory-State Personality — The Past Shapes the Present

### Memory as Personality Modifier

Memory doesn't just store information — it shapes personality:

```python
class MemoryStatePersonality:
    """Personality modified by memory state."""
    
    def __init__(self, base_personality: StochasticPersonality,
                 memory_modifiers: Dict[str, MemoryModifier]):
        self.base_personality = base_personality
        self.memory_modifiers = memory_modifiers
    
    def sample(self, context: Context, memory: Memory) -> Behavior:
        """Sample behavior with memory-modified personality."""
        
        # Step 1: Get base personality sample
        base_behavior = self.base_personality.sample(context, memory)
        
        # Step 2: Apply memory modifiers
        for modifier_name, modifier in self.memory_modifiers.items():
            base_behavior = modifier.apply(base_behavior, memory)
        
        return base_behavior
    
    def update_from_experience(self, experience: Experience):
        """Update personality based on experience."""
        # Traumatic experiences may shift personality permanently
        if experience.valence < -0.7:  # Very negative
            self.shift_towards_cautious()
        
        # Positive experiences may increase openness
        if experience.valence > 0.7:  # Very positive
            self.shift_towards_open()
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Berging Machine*, Chapter 21.

---

## Lecture 9: Personality Stability and Change — The Thread Holds and Shifts

### Stability vs Plasticity

Personality must be stable enough to be recognizable, but plastic enough to adapt:

```python
class StabilityPlasticityBalance:
    """Balance personality stability with adaptive plasticity."""
    
    def __init__(self, stability_rate: float = 0.99, 
                 plasticity_rate: float = 0.01):
        self.stability_rate = stability_rate  # How much personality stays the same
        self.plasticity_rate = plasticity_rate  # How much personality can change
    
    def update(self, personality: StochasticPersonality, 
               experience: Experience) -> StochasticPersonality:
        """Update personality based on experience."""
        
        # Stable component: personality doesn't change
        stable = personality * self.stability_rate
        
        # Plastic component: personality adapts
        adapted = self.adapt(personality, experience) * self.plasticity_rate
        
        # Combined: mostly stable, slightly adapted
        return stable + adapted
    
    def adapt(self, personality: StochasticPersonality, 
             experience: Experience) -> StochasticPersonality:
        """Adapt personality based on experience."""
        # Reinforce modes that led to positive outcomes
        if experience.outcome.valence > 0:
            personality.reinforce_mode(experience.mode, experience.outcome.valence)
        else:
            personality.weaken_mode(experience.mode, abs(experience.outcome.valence))
        
        return personality
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Berging Machine*, Chapter 21.
- Roberts, B. & Mroczek, D. (2008). "Personality Trait Change in Adulthood." *Current Directions in Psychological Science*, 17(1).

---

## Lecture 10: Multi-Agent Personality Interaction — Threads Intertwine

### Personality in Social Context

When agents interact, their personalities modify each other:

```python
class PersonalityInteraction:
    """How personalities modify each other during interaction."""
    
    def __init__(self, agent_a: Agent, agent_b: Agent):
        self.a = agent_a
        self.b = agent_b
    
    def interact(self, context: Context) -> Interaction:
        """Personality interaction between two agents."""
        
        # Each agent samples behavior based on their personality + the other agent
        behavior_a = self.a.personality.sample(
            context=ContextModifier.add_other(context, self.b),
            memory=self.a.memory
        )
        
        behavior_b = self.b.personality.sample(
            context=ContextModifier.add_other(context, self.a),
            memory=self.b.memory
        )
        
        # Each agent's behavior modifies their personality slightly
        outcome_a = self.evaluate_outcome(behavior_a, behavior_b, self.a)
        outcome_b = self.evaluate_outcome(behavior_b, behavior_a, self.b)
        
        self.a.personality.update_from_experience(outcome_a)
        self.b.personality.update_from_experience(outcome_b)
        
        return Interaction(behavior_a=behavior_a, behavior_b=behavior_b,
                          outcome_a=outcome_a, outcome_b=outcome_b)
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Berging Machine*, Chapter 21.

---

## Lecture 11: Evaluating Personality Coherence — Is the Thread True?

### Measuring Personality Coherence

A well-designed personality should be coherent — it should make sense as a unified whole:

```python
class PersonalityCoherenceEvaluator:
    """Evaluate how coherent a personality is."""
    
    def evaluate(self, personality: StochasticPersonality) -> CoherenceReport:
        """Evaluate personality coherence."""
        
        # Internal consistency: Do traits make sense together?
        consistency = self.evaluate_consistency(personality)
        
        # Behavioral coherence: Do behaviors match traits?
        coherence = self.evaluate_behaviors(personality)
        
        # Temporal stability: Does personality remain recognizable over time?
        stability = self.evaluate_stability(personality)
        
        # Social coherence: Does personality make sense in social contexts?
        social = self.evaluate_social(personality)
        
        return CoherenceReport(
            consistency=consistency,
            coherence=coherence,
            stability=stability,
            social=social,
            overall=sigmoid(consistency + coherence + stability + social)
        )
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Berging Machine*, Chapter 21.

---

## Lecture 12: The Norns Weave — Course Synthesis and Integration

### Summary: The Weave of Personality

1. **The Three Norns (Lecture 1):** Personality as probability over behavioral modes.
2. **Behavioral Modes (Lecture 2):** Coherent patterns of behavior.
3. **Markov Chains (Lecture 3):** Mode transitions as stochastic processes.
4. **Gaussian Mixtures (Lecture 4):** Blended behavioral distributions.
5. **Personality Lattices (Lecture 5):**Structured mode hierarchies.
6. **Neural Sampling (Lecture 6):** Neural personality parameterization.
7. **Contextual Triggers (Lecture 7):** What activates behavioral modes.
8. **Memory-State Personality (Lecture 8):** Past shapes present personality.
9. **Stability vs Plasticity (Lecture 9):** Balance between consistency and adaptation.
10. **Multi-Agent Interaction (Lecture 10):** Personality in social context.
11. **Coherence Evaluation (Lecture 11):** Measuring personality quality.

### Capstone Integration

Your capstone agent's personality must be a stochastic composition:
1. Define at least 5 behavioral modes with Markov transitions.
2. Implement contextual triggers based on context, emotion, and memory.
3. Build a personality lattice with partial ordering.
4. Demonstrate stability-plasticity balance over 1000 interactions.
5. Evaluate coherence with the PersonalityCoherenceEvaluator.

**ᛈ Perth — Fate. The Norns weave what shall be.**
**ᚹ Wynja — Joy. Personality brings warmth to cognition.**
**ᛉ Algiz — Protection. Stability guards the self.**

---

*Course materials © 2044 University of Yggdrasil. All rights reserved.*
*ᛈ — The Norns weave. The thread holds.*