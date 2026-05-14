# WM307 — World Model Verification and Testing
## Heimdall's Watch

**University of Yggdrasil — Class of 2044**
**Bachelor of Science in AI World Modeling Systems Design**
**4 Credits** | Year Three, Semester One

**Instructor:** Dr. Védís Heimdallardóttir, Professor of Verification Engineering
**Office:** Heimdallgate 307 | **Hours:** Tuesdays 14:00–16:00

---

## Course Description

A world model must be correct — or at least, its failure modes must be understood. This course covers verification and testing of world simulations: property-based testing of state transitions, invariant checking across world state, adversarial scenario generation, and the Heimdall Framework for continuous world model monitoring. Students learn to design test suites that exercise every branch of the WYRD Protocol and verify that simulated physics, social dynamics, and narrative arcs remain within specification.

---

## Lecture 1: Heimdall's Watch — Why World Models Need Verification

### The Verification Challenge

World models are complex systems with many potential failure modes:

- **Physics violations:** Objects pass through walls, gravity reverses, energy is created from nothing.
- **Social violations:** NPCs behave inconsistently, relationships make no sense, economies collapse.
- **Narrative violations:** Stories have plot holes, characters act out of character, endings are unsatisfying.
- **Consistency violations:** The world contradicts itself — past events are "forgotten," locations shift.

**Heimdall's Watch** is the principle that every world model must be continuously monitored for violations. Just as Heimdall watches the Bifröst bridge for intruders, the verification system watches the world model for inconsistencies.

```python
class HeimdallWatch:
    """Continuous verification of world model correctness."""
    
    def __init__(self, world: World):
        self.world = world
        self.invariants = self.load_invariants()
        self.monitors = self.load_monitors()
        self.violation_log = []
    
    def watch(self):
        """Continuously watch the world for violations."""
        while True:
            # Check all invariants
            for invariant in self.invariants:
                if not invariant.check(self.world):
                    self.violation_log.append(Violation(
                        invariant=invariant.name,
                        details=invariant.violation_details,
                        timestamp=self.world.time
                    ))
            
            # Run all monitors
            for monitor in self.monitors:
                monitor.check(self.world)
            
            yield
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Bering Machine*, Chapter 19.
- Claessen, K. & Hughes, J. (2000). "QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs." *ICFP*.

---

## Lecture 2: Property-Based Testing — Testing What Should Always Be True

### From Examples to Properties

Traditional unit tests check specific examples. Property-based testing checks properties that should always hold:

```python
class WorldProperties:
    """Properties that should always hold for world models."""
    
    @property
    def energy_conservation(self) -> Property:
        """Total energy in the world is conserved."""
        return Property(
            name="energy_conservation",
            check=lambda world: world.total_energy() == world.initial_energy(),
            description="Total energy must remain constant"
        )
    
    @property
    def no_duplicate_entities(self) -> Property:
        """No two entities share the same ID."""
        return Property(
            name="no_duplicate_entities",
            check=lambda world: len(world.entities) == len(set(e.id for e in world.entities)),
            description="Entity IDs must be unique"
        )
    
    @property
    def causal_consistency(self) -> Property:
        """Every effect has a cause that precedes it."""
        return Property(
            name="causal_consistency",
            check=lambda world: all(
                event.cause.timestamp < event.timestamp
                for event in world.events
                if event.cause is not None
            ),
            description="Causes must precede effects"
        )
    
    @property
    def location_consistency(self) -> Property:
        """No entity exists in two locations simultaneously."""
        return Property(
            name="location_consistency",
            check=lambda world: all(
                entity.location == world.get_location(entity.id)
                for entity in world.entities
            ),
            description="Entities must have consistent locations"
        )
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Berging Machine*, Chapter 19.

---

## Lecture 3: State Transition Testing — Every Path Through the World

### Testing State Transitions

World state transitions must be tested for correctness, completeness, and safety:

```python
class StateTransitionTester:
    """Test state transitions in the world model."""
    
    def __init__(self, world: World):
        self.world = world
        self.transition_rules = self.load_transition_rules()
    
    def test_transition(self, transition: StateTransition) -> TransitionTestResult:
        """Test a state transition."""
        
        # Pre-condition: Is the transition valid from current state?
        if not transition.precondition(self.world.state):
            return TransitionTestResult(
                valid=False, 
                reason=f"Precondition not met: {transition.precondition}"
            )
        
        # Execute: Apply the transition
        old_state = self.world.state.copy()
        new_state = transition.apply(old_state)
        
        # Post-condition: Does the result match expectation?
        if not transition.postcondition(new_state):
            return TransitionTestResult(
                valid=False,
                reason=f"Postcondition not met: {transition.postcondition}"
            )
        
        # Invariant: Are all invariants still satisfied?
        for invariant in self.world.invariants:
            if not invariant.check(new_state):
                return TransitionTestResult(
                    valid=False,
                    reason=f"Invariant violated: {invariant.name}"
                )
        
        return TransitionTestResult(valid=True, old_state=old_state, new_state=new_state)
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Berging Machine*, Chapter 19.

---

## Lecture 4: Invariant Checking — The Unbreakable Laws

### Worlds Must Not Break Their Own Rules

Every world model has invariants — rules that must never be violated:

```python
class WorldInvariant:
    """An invariant that must always hold in the world model."""
    
    def __init__(self, name: str, description: str, check: Callable):
        self.name = name
        self.description = description
        self.check = check
    
    def verify(self, world: World) -> InvariantResult:
        """Verify this invariant holds."""
        if self.check(world):
            return InvariantResult(holds=True, invariant=self.name)
        else:
            return InvariantResult(holds=False, invariant=self.name, 
                                  details=f"Invariant '{self.name}' violated")

# Common world invariants
PHYSICS_INVARIANTS = [
    WorldInvariant(
        "energy_conservation",
        "Total energy in the world must be conserved",
        lambda w: abs(w.total_energy() - w.initial_energy()) < 0.01
    ),
    WorldInvariant(
        "no_overlap",
        "No two solid entities can occupy the same space",
        lambda w: not any(w.overlaps(e1, e2) for e1 in w.solid_entities() 
                         for e2 in w.solid_entities() if e1 != e2)
    ),
    WorldInvariant(
        "temporal_causality",
        "Every effect must have a cause that precedes it",
        lambda w: all(e.cause.timestamp < e.timestamp 
                     for e in w.events if e.cause)
    ),
]

SOCIAL_INVARIANTS = [
    WorldInvariant(
        "relationship_symmetry",
        "If A trusts B, B must have some relationship with A",
        lambda w: all(w.has_relationship(b, a) 
                     for a in w.agents for b in w.get_trusted_agents(a))
    ),
    WorldInvariant(
        "no_infinite_debt",
        "No agent can owe more than the total economic value",
        lambda w: all(abs(agent.debt) < w.total_economic_value() 
                     for agent in w.agents)
    ),
]

NARRATIVE_INVARIANTS = [
    WorldInvariant(
        "character_consistency",
        "Characters must not act against their core values without cause",
        lambda w: all(w.is_consistent_action(a, a.last_action) 
                     for a in w.agents if a.has_core_values())
    ),
]
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Berging Machine*, Chapter 19.

---

## Lecture 5: Adversarial Scenario Generation — Breaking the World on Purpose

### Adversarial Testing

Rather than waiting for bugs to appear naturally, we break the world on purpose:

```python
class AdversarialScenarioGenerator:
    """Generate scenarios designed to break the world model."""
    
    def __init__(self, world: World):
        self.world = world
        self.invariants = self.load_invariants()
        self.strategies = self.load_strategies()
    
    def generate_adversarial_scenario(self) -> AdversarialScenario:
        """Generate a scenario designed to violate an invariant."""
        
        # Step 1: Pick an invariant to target
        target_invariant = random.choice(self.invariants)
        
        # Step 2: Pick an adversarial strategy
        strategy = random.choice(self.strategies)
        
        # Step 3: Generate a scenario
        scenario = strategy.generate(target_invariant, self.world)
        
        return scenario
    
    def run_adversarial_test(self, num_scenarios: int = 100) -> TestReport:
        """Run adversarial tests and report violations."""
        violations = []
        
        for _ in range(num_scenarios):
            scenario = self.generate_adversarial_scenario()
            result = scenario.execute(self.world)
            
            if result.has_violations():
                violations.extend(result.violations)
        
        return TestReport(
            total_scenarios=num_scenarios,
            violations=violations,
            violation_rate=len(violations) / num_scenarios
        )
```

### Adversarial Strategies

```python
class BoundaryPushing(AdversarialStrategy):
    """Push world parameters to their boundaries."""
    
    def generate(self, invariant: WorldInvariant, world: World) -> Scenario:
        # Set world parameters to extreme values
        extreme_params = {
            "population": 10000,       # Too many agents
            "resources": 0,             # No resources
            "time_speed": 1000,        # Extreme time acceleration
            "gravity": 0.01,            # Nearly zero gravity
        }
        return Scenario(parameters=extreme_params, target=invariant)

class ConflictInjection(AdversarialStrategy):
    """Inject conflicts between agents."""
    
    def generate(self, invariant: WorldInvariant, world: World) -> Scenario:
        # Create conflicting goals between agents
        agents = random.sample(world.agents, min(10, len(world.agents)))
        for agent in agents:
            agent.add_conflicting_goal()
        return Scenario(agents=agents, target=invariant)
```

### Lab 2: Adversarial Testing

Generate adversarial scenarios for a test world model:

1. Implement at least 3 adversarial strategies.
2. Generate 100 adversarial scenarios.
3. Report which invariants were violated and how.
4. Propose fixes for the most common violations.

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Berging Machine*, Chapter 19.

---

## Lecture 6: The Heimdall Framework — Continuous Monitoring

### Continuous World Model Monitoring

The Heimdall Framework provides continuous monitoring:

```python
class HeimdallFramework:
    """Continuous world model monitoring framework."""
    
    def __init__(self, world: World, config: HeimdallConfig):
        self.world = world
        self.config = config
        self.invariant_checks = self.load_invariant_checks()
        self.monitors = self.load_monitors()
        self.alerts = []
        self.watchdog = WatchdogTimer(config.check_interval)
    
    async def monitor(self):
        """Continuously monitor the world model."""
        while True:
            # Run all invariant checks
            results = [check.run(self.world) for check in self.invariant_checks]
            
            # Run all monitors
            for monitor in self.monitors:
                monitor.check(self.world)
            
            # Generate alerts for violations
            for result in results:
                if not result.passed:
                    alert = self.create_alert(result)
                    self.alerts.append(alert)
                    await self.notify(alert)
            
            # Reset watchdog
            self.watchdog.reset()
            
            await asyncio.sleep(self.config.check_interval)
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Berging Machine*, Chapter 19.

---

## Lecture 7: Regression Testing for World Models

### Ensuring Changes Don't Break Things

When the world model is updated, regression testing verifies that existing behavior is preserved:

```python
class WorldRegressionTest:
    """Regression testing for world models."""
    
    def __init__(self, world: World, recorded_sessions: List[Session]):
        self.world = world
        self.recorded_sessions = recorded_sessions
    
    def run_regression(self) -> RegressionReport:
        """Run all regression tests."""
        results = []
        for session in self.recorded_sessions:
            result = self.replay_session(session)
            results.append(result)
        return RegressionReport(results=results)
    
    def replay_session(self, session: Session) -> SessionResult:
        """Replay a recorded session and compare results."""
        self.world.reset(session.initial_state)
        
        for event in session.events:
            self.world.apply(event)
            expected_state = session.get_expected_state(event.timestamp)
            actual_state = self.world.get_state()
            
            if not self.states_match(expected_state, actual_state):
                return SessionResult(
                    passed=False,
                    mismatch=self.compute_mismatch(expected_state, actual_state),
                    timestamp=event.timestamp
                )
        
        return SessionResult(passed=True)
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Berging Machine*, Chapter 19.

---

## Lecture 8: Fuzzing World Models — Random Chaos

### Fuzz Testing for World Models

Fuzzing generates random inputs to find edge cases:

```python
class WorldFuzzer:
    """Fuzz testing for world models."""
    
    def __init__(self, world: World, seed: int = 42):
        self.world = world
        self.rng = Random(seed)
        self.generators = self.load_generators()
    
    def fuzz(self, num_iterations: int = 1000) -> FuzzReport:
        """Run fuzz testing."""
        crashes = []
        violations = []
        
        for _ in range(num_iterations):
            # Generate a random input
            random_input = self.generate_random_input()
            
            # Apply to the world
            try:
                self.world.apply(random_input)
            except Exception as e:
                crashes.append(Crash(input=random_input, error=str(e)))
                self.world.reset()
                continue
            
            # Check invariants
            for invariant in self.world.invariants:
                if not invariant.check(self.world):
                    violations.append(Violation(
                        input=random_input,
                        invariant=invariant.name
                    ))
        
        return FuzzReport(crashes=crashes, violations=violations)
    
    def generate_random_input(self) -> WorldInput:
        """Generate a random world input."""
        generator = self.rng.choice(self.generators)
        return generator.generate(self.rng)
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Berging Machine*, Chapter 19.
- Miller, B. et al. (1990). "An Empirical Study of the Reliability of UNIX Utilities." *Communications of the ACM*, 33(12).

---

## Lecture 9: Testing Narrative Coherence — Stories That Make Sense

### Narrative Testing

Stories generated by the world model must be coherent:

```python
class NarrativeCoherenceTester:
    """Test narrative coherence of world model output."""
    
    def __init__(self, world: World):
        self.world = world
    
    def test_coherence(self, narrative: Narrative) -> CoherenceReport:
        """Test narrative coherence."""
        
        checks = [
            self.check_internal_consistency(narrative),
            self.check_character_consistency(narrative),
            self.check_causal_chain(narrative),
            self.check_temoral_ordering(narrative),
            self.check_thematic_coherence(narrative),
            self.check_pacing(narrative),
        ]
        
        return CoherenceReport(
            checks={check.name: check.result for check in checks},
            overall_coherence=all(check.passed for check in checks)
        )
    
    def check_internal_consistency(self, narrative: Narrative) -> CheckResult:
        """Check that the narrative doesn't contradict itself."""
        contradictions = []
        for i, event_a in enumerate(narrative.events):
            for j, event_b in enumerate(narrative.events):
                if i < j and event_a.contradicts(event_b):
                    contradictions.append((event_a, event_b))
        
        return CheckResult(
            name="internal_consistency",
            passed=len(contradictions) == 0,
            details=f"Found {len(contradictions)} contradictions"
        )
    
    def check_character_consistency(self, narrative: Narrative) -> CheckResult:
        """Check that characters act consistently with their personalities."""
        inconsistencies = []
        for event in narrative.events:
            if event.agent and not event.agent.would_do(event.action):
                inconsistencies.append(event)
        
        return CheckResult(
            name="character_consistency",
            passed=len(inconsistencies) == 0,
            details=f"Found {len(inconsistencies)} character inconsistencies"
        )
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Berging Machine*, Chapter 19.

---

## Lecture 10: Performance Testing — World Under Load

### Testing Performance at Scale

World models must perform well even with many agents, events, and interactions:

```python
class WorldPerformanceTester:
    """Test world model performance at scale."""
    
    def __init__(self, world: World):
        self.world = world
    
    def benchmark(self, num_agents: List[int], 
                  duration: float = 60.0) -> BenchmarkReport:
        """Benchmark world performance with different numbers of agents."""
        results = []
        
        for n in num_agents:
            # Set up world with n agents
            self.world.setup(n)
            
            # Run simulation
            start_time = time.time()
            events_processed = 0
            
            while time.time() - start_time < duration:
                self.world.tick()
                events_processed += self.world.events_this_tick()
            
            end_time = time.time()
            actual_duration = end_time - start_time
            
            results.append(BenchmarkResult(
                num_agents=n,
                duration=actual_duration,
                events_per_second=events_processed / actual_duration,
                ticks_per_second=self.world.ticks / actual_duration,
                memory_usage=self.world.memory_usage()
            ))
        
        return BenchmarkReport(results=results)
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Berging Machine*, Chapter 19.

---

## Lecture 11: Test-Driven World Modeling — Heimdall-First Development

### Write Tests First, Build Worlds Second

Heimdall-First Development means writing verification tests before implementing the world model:

```python
# Step 1: Write the test
def test_physics_collision():
    """Test that solid objects cannot overlap."""
    world = World()
    ball_a = world.create_entity("ball", location=(0, 0), solid=True)
    ball_b = world.create_entity("ball", location=(0, 0), solid=True)
    
    # Attempting to place two solid objects at the same location should fail
    with pytest.raises(PhysicsViolation):
        world.place(ball_b, location=(0, 0))

# Step 2: Implement the world model to pass the test
class World:
    def place(self, entity, location):
        # Check for overlaps
        existing = self.get_entities_at(location)
        if any(e.solid and entity.solid for e in existing):
            raise PhysicsViolation(f"Cannot place {entity} at {location}: overlaps with {existing}")
        
        entity.location = location
        self.entities.add(entity)
```

### Required Reading

- Freyjasdóttir, R. (2039). *The Memory-Berging Machine*, Chapter 19.
- Beck, K. (2003). *Test-Driven Development: By Example*. Addison-Wesley.

---

## Lecture 12: Heimdall Stands — Course Synthesis and Capstone

### Summary: The Watchman's Vigil

We began with the principle that world models must be correct — or at least, their failure modes must be understood. We end with the Heimdall Framework, a comprehensive verification and testing system:

1. **Property-Based Testing (Lecture 2):** Testing properties that should always hold.
2. **State Transition Testing (Lecture 3):** Verifying every path through the world.
3. **Invariant Checking (Lecture 4):** Unbreakable laws of the world.
4. **Adversarial Scenarios (Lecture 5):** Breaking the world on purpose.
5. **Heimdall Framework (Lecture 6):** Continuous monitoring.
6. **Regression Testing (Lecture 7):** Ensuring updates don't break things.
7. **Fuzzing (Lecture 8):** Random chaos to find edge cases.
8. **Narrative Coherence (Lecture 9):** Stories that make sense.
9. **Performance Testing (Lecture 10):** World under load.
10. **Test-Driven World Modeling (Lecture 11):** Tests first, worlds second.

### Capstone Project: Build and Verify a World

Your capstone project is to build a world model and verify it:

1. **Build:** Implement a world model with at least 20 agents, physics, social dynamics, and narrative arc.
2. **Specify:** Write 20+ invariants (physics, social, narrative).
3. **Test:** Write property-based tests for all invariants.
4. **Fuzz:** Run fuzz testing with 10,000 random inputs.
5. **Adversarial:** Generate and execute 50 adversarial scenarios.
6. **Monitor:** Implement the Heimdall Framework with continuous monitoring.
7. **Report:** Document all violations found and fixes applied.

**ᚼ Heimdall — The watchman stands. The world is verified.**
**ᛏ Tiwaz — Justice. The tests are fair.**
**ᛉ Algiz — Protection. The invariants hold.**

---

*Course materials © 2044 University of Yggdrasil. All rights reserved.*
*ᚼ — Heimdall watches. The world endures.*