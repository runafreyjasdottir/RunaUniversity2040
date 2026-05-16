# CS405: Research Methods in Computer Science
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4
**Prerequisites:** CS208 — Formal Methods & Verification; minimum of four 300-level CS courses completed.
**Description:** A rigorous seminar on the craft of computer science research. Students learn to survey literature systematically, design reproducible experiments, apply both quantitative and qualitative methods, write publishable papers, navigate peer review, and uphold research ethics in an era of autonomous systems and planetary-scale computation. The course culminates in a mini research project — from hypothesis formation through peer-reviewed manuscript — conducted on the University of Yggdrasil's own Yggdrasil Research Cloud. By 2040, CS research has expanded beyond algorithms and systems into ethics of AGI, environmental computing, and neurosymbolic architectures; this course equips students to contribute meaningfully to all of them.

---

## Lecture 1: The Scientific Method in Computer Science — From Hypothesis to Knowledge

*"The smith does not strike the iron and hope; she measures, heats to the right glow, and knows what shape she seeks before the hammer falls." — A Norse framing for research design.*

Computer science occupies a peculiar position among the sciences. Unlike physics, which studies phenomena that exist independent of human construction, CS studies artifacts we ourselves build — algorithms, systems, languages, architectures. This makes the scientific method in CS simultaneously more controlled (we can build from scratch) and more slippery (we are studying our own creations, not nature). The 2040 landscape, with autonomous AI systems, quantum processors, and planet-scale distributed infrastructure, demands research methods that are rigorous, reproducible, and honest about their limitations.

The scientific method in CS follows a recognizable arc: **observation** (a performance anomaly, a user need, a theoretical gap), **hypothesis formation** (a proposed explanation or solution), **experiment design** (how to test the hypothesis), **data collection** (running the experiment), **analysis** (interpreting results), and **publication** (sharing findings for scrutiny). But each step has CS-specific nuances. Hypotheses in CS are often *constructive* rather than *descriptive* — "we can build X that achieves Y" rather than "X causes Y." Experiment design in CS frequently involves benchmarking, where the choice of benchmark suite, hardware, and measurement methodology can dramatically influence conclusions. The SPEC CPU benchmark controversy of the 2020s — where compiler optimizations targeted specific benchmarks rather than improving general performance — taught the field that *what you measure shapes what you build*.

A central tension in CS research methodology is the divide between **formal methods** (proofs, static analysis, model checking — the territory of CS208) and **empirical methods** (measurements, user studies, A/B tests). Neither is sufficient alone. A formal proof that an algorithm is O(n log n) tells you nothing about cache behavior on real hardware; a benchmark showing 20% speedup on one dataset tells you nothing about worst-case guarantees. The mature CS researcher in 2040 wields both, using formal methods to establish *correctness bounds* and empirical methods to establish *practical performance*. This course emphasizes the latter while acknowledging the former — research methods are the bridge between the theoretical *possible* and the empirically *observed*.

The **replication crisis** that swept through psychology and medicine in the 2010s–2020s did not spare computer science. A 2023 study of 400 papers from top systems conferences found that fewer than 40% provided sufficient artifacts (code, data, configuration) for independent replication. The **ACM Artifact Review and Badging** initiative (introduced 2016, mandatory at many venues by 2030) was the field's response: papers can earn "Artifacts Available," "Artifacts Evaluated," and "Results Reproduced" badges. By 2040, artifact evaluation is no longer optional — it is the baseline expectation for empirical CS research. Students in this course will earn all three badges on their mini-project.

Finally, the 2040 researcher must understand the **epistemological status** of their claims. "Our system achieves 95% accuracy on ImageNet" is a different kind of claim than "attention mechanisms enable compositional generalization." The former is a *performance claim* about a specific artifact on a specific dataset; the latter is a *mechanistic claim* about how a class of architectures works. Each requires different evidence standards. Performance claims demand rigorous benchmarking with error bars, ablations, and multiple datasets. Mechanistic claims demand controlled experiments isolating the proposed mechanism from confounds. The sloppiest research conflates the two — reporting a performance number and implying it validates a mechanism. Throughout this course, you will learn to distinguish these claim types and design experiments appropriate to each.

**Required Reading:**
- Denning, P.J. (2005). "Is Computer Science Science?" *Communications of the ACM*, 48(4), 27–31.
- Vitek, J. & Kalibera, T. (2011). "R3: Repeatability, Reproducibility, and Rigor." *ACM SIGPLAN Notices*, 47(4a), 30–36.
- ACM (2020). "Artifact Review and Badging — Version 2.0." *ACM Publications Board*.
- Cockburn, A., Dragicevic, P., Besançon, L., & Gutwin, C. (2020). "Threats of a Replication Crisis in Empirical Computer Science." *Communications of the ACM*, 63(8), 70–79.
- Fjǫrgyn, S. (2039). *The Rune-Carver's Method: Research Design for Constructive Sciences*. Yggdrasil University Press. Chapters 1–3.

**Discussion Questions:**
1. Is computer science a natural science, a formal science (like mathematics), or an engineering discipline? How does your answer change what constitutes valid evidence in CS research?
2. Consider a paper claiming "our new database index improves throughput by 30%." What information would you need to assess whether this is a performance claim, a mechanistic claim, or both? What would a rigorous experiment design look like?
3. The ACM Badging system requires artifacts to be "available" and "evaluated." What are the practical barriers to artifact availability in 2040 — consider proprietary datasets, cloud-only services, and hardware dependencies? Are there research contributions that cannot be artifact-evaluated?

---

## Lecture 2: Literature Review and Systematic Survey — Mapping the Known

*"Before carving a new rune, the wise skald reads every stone in the valley — lest she spend years rediscovering what was already written."*

The literature review is the most underrated skill in the CS researcher's toolkit. Done poorly, it is a perfunctory ritual of citing the same five papers everyone cites. Done well, it is the intellectual foundation that prevents rediscovery of known results, reveals genuine gaps, and positions new work within the living conversation of the field. By 2040, with arXiv hosting over 3 million preprints and conference proceedings growing at 15% annually, the sheer volume of CS literature makes systematic review a computational problem as much as an intellectual one.

A **systematic literature review (SLR)** follows a protocol: define research questions, specify search terms and databases, apply inclusion/exclusion criteria, extract data from each included paper, synthesize findings, and report. This methodology, imported from evidence-based medicine (the Cochrane Collaboration) and adapted for CS by Kitchenham et al. (2004/2007), transforms the literature review from an essay into a reproducible study in its own right. The key insight: your literature review should be reproducible — another researcher following your protocol should find the same papers and draw comparable conclusions. In 2040, tools like **Elicit** (semantic paper search), **Semantic Scholar's TLDRs**, and the University of Yggdrasil's own **Huginn Literature Engine** (which uses graph neural networks to map citation networks and detect research clusters) have made systematic review far more efficient, but the methodological rigor remains human-driven.

A well-constructed SLR begins with a **PICOC framework** (Population, Intervention, Comparison, Outcome, Context). For example: "In autonomous vehicle perception systems (Population), how do transformer-based architectures (Intervention) compare with CNN-based architectures (Comparison) in terms of detection latency and accuracy (Outcome) under adverse weather conditions (Context)?" This sharpens the research question from the vague ("neural networks for self-driving cars") to the answerable. The search strategy should span multiple databases: the ACM Digital Library, IEEE Xplore, arXiv, DBLP, and Google Scholar — each with its own biases (ACM favors systems, IEEE favors hardware, arXiv favors deep learning). Snowballing — following citations forward and backward — catches papers the keyword search missed.

The most common failure mode in CS literature reviews is **selection bias**: the reviewer reads what they already know, cites their friends, and ignores dissenting findings. The SLR protocol forces transparency: you must report *how many* papers were found, *how many* were excluded and why, and *what* the inclusion criteria were. A PRISMA-style flow diagram (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) should appear in any serious CS survey paper. At the University of Yggdrasil, the CS405 midterm requires students to produce a mini-SLR with a PRISMA diagram showing at least 50 candidate papers narrowed to 15–20 included studies.

Beyond systematic reviews, the 2040 researcher must master **narrative synthesis** — the art of telling a coherent story across heterogeneous studies. CS papers are rarely homogeneous enough for statistical meta-analysis (unlike medical trials, where many studies test the same drug); instead, you synthesize by theme, by method, by finding. A strong lit review has a **thesis** — an argument about the state of the field, not just a laundry list of summaries. It identifies **consensus** (findings replicated across multiple groups), **controversy** (conflicting results with plausible explanations), and **gaps** (questions no one has asked). The best lit reviews change how the field thinks about itself; they become canonical references cited for decades.

**Required Reading:**
- Kitchenham, B. & Charters, S. (2007). "Guidelines for Performing Systematic Literature Reviews in Software Engineering." *EBSE Technical Report*, Keele University/Durham University.
- Webster, J. & Watson, R.T. (2002). "Analyzing the Past to Prepare for the Future: Writing a Literature Review." *MIS Quarterly*, 26(2), xiii–xxiii.
- Moher, D., Liberati, A., Tetzlaff, J., & Altman, D.G. (2009). "Preferred Reporting Items for Systematic Reviews and Meta-Analyses: The PRISMA Statement." *PLoS Medicine*, 6(7), e1000097.
- Bornmann, L. & Mutz, R. (2015). "Growth Rates of Modern Science: A Bibliometric Analysis." *Journal of the Association for Information Science and Technology*, 66(11), 2215–2222.
- Sigrúnardóttir, K. (2040). *Huginn's Eye: Computational Literature Discovery with Graph Neural Networks*. Yggdrasil Technical Report YTR-2040-07.

**Discussion Questions:**
1. A student finds 200 candidate papers, reads 20, and writes a lit review. Is this a systematic review? What's the minimum information you'd need to assess its quality?
2. How should literature reviews handle contradictory findings? If Paper A says technique X is 30% better and Paper B says technique X is 10% worse, what are the possible explanations — and how should a reviewer present this?
3. In 2040, LLMs can generate literature review drafts automatically. What are the risks? Where does human judgment remain irreplaceable in the review process?

---

## Lecture 3: Experiment Design I — Variables, Controls, and Threats to Validity

*"You cannot measure the length of a shadow without knowing where the torch stands."*

Experiment design is where research methods become concrete. A well-designed experiment isolates the effect of a **treatment** (the thing you changed) on an **outcome** (the thing you measured), while controlling for everything else. In CS, the treatment is typically a new algorithm, system, architecture, or interface; the outcome is a performance metric, accuracy score, user satisfaction rating, or energy consumption. The gap between "I built X and it seems fast" and "X is faster than Y by Z% with p < 0.01 under conditions A, B, and C" is the entire discipline of experiment design.

The first step is identifying your **variables**. The **independent variable** is what you manipulate (e.g., algorithm version: baseline vs. proposed). The **dependent variable** is what you measure (e.g., throughput in queries/second). The **controlled variables** are everything you hold constant (hardware, dataset, compiler flags, ambient temperature — yes, thermal throttling has invalidated many a CS paper). **Confounding variables** are the hidden factors that correlate with your independent variable and could explain the outcome — the most dangerous kind. For example, if your "faster" algorithm happens to have better cache locality because you wrote it more carefully (not because of algorithmic superiority), implementation quality is a confound. In 2040, with heterogeneous hardware (CPU+GPU+NPU+Loihi), confounds multiply: is your algorithm faster because it's better, or because the scheduler happened to map it to faster cores?

**Internal validity** asks: did the treatment *cause* the observed effect, or could something else explain it? Threats to internal validity include **history** (something happened between measurements), **maturation** (the system changed over time), **instrumentation** (the measurement tool changed), **selection bias** (non-random assignment to conditions), and **attrition** (data points lost during the experiment). In CS systems research, a classic internal validity threat is **caching**: the second run of a benchmark is faster because data is cached in memory, not because the system is better. The fix is simple but often neglected: warm the cache before measuring, or report both cold-start and warm-cache performance separately.

**External validity** asks: do these results generalize beyond the specific conditions of this experiment? This is the Achilles' heel of CS research. A paper showing Algorithm A beats Algorithm B on dataset D, hardware H, with hyperparameters HP tells you exactly nothing about what happens on a different dataset, different hardware, or different hyperparameters — unless you've argued for generalizability. The standard defenses: test on **multiple datasets** from different domains, report results on **multiple hardware configurations**, use **sensitivity analysis** (vary hyperparameters and show the conclusion holds), and explicitly state the **scope of claims** ("We show X on natural language tasks with Transformer architectures; generalizability to vision tasks remains to be tested").

A concept from psychology that CS researchers should internalize is the **demand characteristic**: subjects (or systems) behave differently when they know they're being tested. In CS, the analog is **benchmark specialization** — algorithms optimized to the specific quirks of a benchmark suite rather than the general problem. The solution: hold-out test sets, cross-validation, and "contest" evaluation where the test set is truly unseen (e.g., Kaggle-style private leaderboards). In 2040, with AI systems that can meta-learn benchmark patterns, benchmark integrity requires constant vigilance — new test sets must be generated periodically, and evaluation protocols must anticipate adaptive behavior.

**Required Reading:**
- Montgomery, D.C. (2017). *Design and Analysis of Experiments* (9th ed.). Wiley. Chapters 1–4.
- Tichy, W.F. (1998). "Should Computer Scientists Experiment More?" *IEEE Computer*, 31(5), 32–40.
- Mytkowicz, T., Diwan, A., Hauswirth, M., & Sweeney, P.F. (2009). "Producing Wrong Data Without Doing Anything Obviously Wrong!" *ASPLOS 2009*. The classic demonstration of measurement bias in CS.
- Krishnamurthi, S. & Vitek, J. (2015). "The Real Software Crisis: Repeatability in CS Research." *Communications of the ACM*, 58(4), 32–36.
- Rúnheimr, E. (2038). *Valid Threats: A Taxonomy of Confounds in AI Systems Research*. Springer. Chapters 2–5.

**Discussion Questions:**
1. A student benchmarks her new sorting algorithm against quicksort using a single array of 10,000 random integers, running each 10 times on her laptop, reporting the mean. Identify at least four threats to internal and external validity.
2. In deep learning research, "the same hyperparameters as prior work" is commonly claimed as a control. Why is this insufficient? What additional controls would strengthen causal claims?
3. Your algorithm is 5% more accurate than baseline on CIFAR-100 but 2% less accurate on ImageNet. Is your algorithm "better"? How should this be reported?

---

## Lecture 4: Experiment Design II — Statistical Power, Effect Sizes, and Sample Size

*"One raven's flight is random; a thousand ravens point to carrion."*

Statistical thinking separates the amateur researcher from the professional. Too many CS papers report "X is better than Y" based on a single run or a mean of three runs with no measure of uncertainty. In 2040, with reviewers trained to demand statistical rigor, such papers are desk-rejected. This lecture covers the statistical toolkit every CS researcher needs: hypothesis testing, confidence intervals, effect sizes, statistical power, and sample size justification.

**Null Hypothesis Significance Testing (NHST)** is the dominant framework — and also the most abused. The logic: assume the null hypothesis H₀ (no difference between conditions), compute the probability p of observing data at least as extreme as yours under H₀, and reject H₀ if p < α (typically α = 0.05). The pitfalls are legendary: p-hacking (trying multiple analyses until p < 0.05), the file-drawer problem (null results go unpublished), confusion of statistical significance with practical importance, and the base-rate fallacy (in fields where most hypotheses are false, most p < 0.05 results are false positives). The American Statistical Association's 2016 statement on p-values — an unprecedented institutional intervention — warned against these abuses, and by 2040, CS venues increasingly require **effect sizes** and **confidence intervals** alongside (or instead of) p-values.

**Effect size** answers the question NHST does not: *how large* is the difference? Cohen's d = (μ₁ - μ₂) / σ_pooled measures the standardized mean difference, with conventions: d = 0.2 is "small," 0.5 "medium," 0.8 "large." In CS benchmarking, the raw difference (e.g., 15% throughput improvement) is often more interpretable than a standardized measure, but reporting *both* is best practice. A 1% improvement with p < 0.001 (large sample, tiny effect) may be statistically significant but practically useless; a 50% improvement with p = 0.08 (small sample, large effect) may be practically important but statistically inconclusive. The researcher must report all three: estimate, uncertainty, and practical interpretation.

**Statistical power** is the probability of detecting an effect if one truly exists. Underpowered studies — those with too few samples to reliably detect plausible effect sizes — are unethical (wasting participant time and compute resources) and scientifically wasteful (producing inconclusive results). Power analysis answers: given an expected effect size, desired α, and desired power (typically 0.80), how many samples do I need? For simple comparisons (t-test), power is a function of sample size, effect size, and α, computable with tools like G*Power or Python's `statsmodels`. For complex CS experiments (A/B tests on live systems, multi-factorial benchmarks), power analysis often requires simulation — generating synthetic data under the alternative hypothesis and checking detection rates. In 2040, the University of Yggdrasil's **RavnPower** library automates power analysis for common CS experiment designs.

**Sample size justification** is now required by many CS journals. The statement must explain *why* this sample size was chosen, not just *what* it was. Acceptable justifications include: a priori power analysis, resource constraints (with acknowledgment of limitation), saturation (in qualitative studies — see Lecture 6), or precedent (matching sample sizes in comparable published work). "We used N=5 because that's what everyone does" is not acceptable. For machine learning experiments, sample size means number of independent training runs (for variance estimation), number of datasets, and number of cross-validation folds — each must be justified.

**Required Reading:**
- Wasserstein, R.L. & Lazar, N.A. (2016). "The ASA Statement on p-Values: Context, Process, and Purpose." *The American Statistician*, 70(2), 129–133.
- Cumming, G. (2014). "The New Statistics: Why and How." *Psychological Science*, 25(1), 7–29.
- Cohen, J. (1992). "A Power Primer." *Psychological Bulletin*, 112(1), 155–159.
- Arcuri, A. & Briand, L. (2014). "A Hitchhiker's Guide to Statistical Tests for Assessing Randomized Algorithms in Software Engineering." *Software Testing, Verification and Reliability*, 24(3), 219–250.
- Hrafnsdóttir, Þ. (2039). *RavnPower: Automated Statistical Power Analysis for Computing Research*. Yggdrasil Open Source. Documentation v3.1.

**Discussion Questions:**
1. You run 20 benchmarks comparing your system against baseline and find significant differences (p < 0.05) on 3 of them. Is this evidence that your system is better? What correction for multiple comparisons should you apply?
2. A paper reports "accuracy improved from 92.3% to 92.8%, p < 0.001" with N=1,000,000 test examples. Is this finding meaningful? How would you report it differently?
3. Your power analysis says you need N=120. You can only afford N=40. Should you run the experiment? How should you present the results?

---

## Lecture 5: Quantitative Methods — Benchmarking, Profiling, and Performance Measurement

*"The weight of a sword is not known by its look, but by the arm that swings it."*

Quantitative methods in CS research center on measurement — turning the behavior of a system into numbers that can be compared, analyzed, and interpreted. The central tool is **benchmarking**: executing a standardized workload and recording performance metrics. Yet benchmarking is deceptively hard. The 2009 paper "Producing Wrong Data Without Doing Anything Obviously Wrong" (Mytkowicz et al.) showed that linking order, environment variable size, and even the username length could produce ±5% variance in benchmark results — on the *same binary*. Twenty years later, with heterogeneous multi-core processors, NUMA architectures, GPU boost clocks, and thermal management firmware, the problem has only intensified.

The first principle of rigorous benchmarking is **environmental control**. Every measurement must document: exact hardware specifications (CPU model, microcode version, memory configuration, storage type), OS version and kernel, compiler version and flags, library versions, and ambient conditions (temperature, power state). In 2040, the Yggdrasil Research Cloud provides **benchmark containers** — immutable, versioned environments that guarantee bit-for-bit reproducibility of the software stack. Hardware, however, remains the irreproducible variable; even two nominally identical CPU chips have different thermal characteristics, different voltage-frequency curves, and different defect maps (part of the chip disabled). The best you can do is document, randomize, and measure variance.

**Warm-up and steady-state** are critical concepts in performance measurement. Many systems exhibit transient behavior at startup — JIT compilation, cache warming, connection pool establishment, memory allocation. Measurements taken during the transient phase reflect start-up cost, not steady-state performance. Standard practice: run the benchmark for a warm-up period (discarded), then measure during a steady-state period. But how long is warm-up? You must verify empirically: plot the performance metric over time and identify when it stabilizes. For JIT-compiled languages (Java, JavaScript, Python/PyPy), warm-up can take thousands of iterations. For databases, warm-up means filling the buffer pool. For ML inference, warm-up includes GPU kernel compilation and memory allocation. Every CS405 student project must include a warm-up verification plot.

**Metric selection** shapes conclusions. Common CS metrics: **latency** (time to complete a single operation), **throughput** (operations per unit time), **tail latency** (p99, p99.9 — the worst-case user experience), **efficiency** (throughput per watt or per dollar), **utilization** (fraction of resource capacity used), and **scalability** (how throughput changes as resources increase). The rookie mistake is reporting only the mean. Means hide outliers — a system with mean latency 10 ms and p99 latency 5000 ms is a terrible system for interactive use, regardless of the mean. Always report the **distribution**: mean, median, standard deviation, and key percentiles (p50, p95, p99, p99.9). Better yet, show a histogram or CDF. In 2040, CS venues increasingly require distributional reporting — a single-number summary is considered incomplete.

**Statistical comparisons** of benchmarking results require care. If you run each configuration 30 times and compare means with a t-test, you've assumed independence, normality, and equal variance — assumptions that are frequently violated in systems data (autocorrelated due to state, heavy-tailed, heteroscedastic). Non-parametric tests (Mann-Whitney U, bootstrap confidence intervals) are safer defaults. When comparing more than two configurations, use ANOVA with post-hoc correction (Tukey HSD) rather than multiple t-tests. The key is to match the statistical test to the data's structure, not to force the data into the test you know.

**Required Reading:**
- Jain, R. (1991). *The Art of Computer Systems Performance Analysis*. Wiley. Chapters 10–13, 17.
- Mytkowicz, T., Diwan, A., Hauswirth, M., & Sweeney, P.F. (2009). "Producing Wrong Data Without Doing Anything Obviously Wrong!" *ASPLOS '09*.
- He, S., Manns, G., Saunders, J., Wang, W., Pollock, L., & Soffa, M.L. (2021). "A Statistics-Based Performance Testing Methodology for Cloud Applications." *FSE 2021*.
- Chen, J. & Revels, J. (2018). "Generating Robust Benchmarks for Deep Learning." *SysML 2018*.
- Þorsteinsson, B. (2037). *Mjǫtviðr: A Framework for Rigorous Performance Measurement*. Yggdrasil Technical Report YTR-2037-02.

**Discussion Questions:**
1. You benchmark a new cache replacement policy against LRU on five different trace files. On three traces it's 10–15% better; on two it's 3–5% worse. How do you report this? Is your policy "better"?
2. Mean latency is 8 ms, p99 is 450 ms. A competitor's system has mean 12 ms, p99 is 15 ms. Which is "faster"? What application characteristics would make you choose one over the other?
3. How would you benchmark an LLM inference server where each query has a different output length? What metric captures both speed and quality?

---

## Lecture 6: Qualitative Methods — Case Studies, Grounded Theory, and Thematic Analysis

*"Not all knowledge is weighed in pounds and ounces. The skald's song measures truth in memory, in resonance, in the tears of those who hear it."*

Computer science has historically been hostile to qualitative methods — the attitude that "if you can't measure it with numbers, it isn't science." This is both philosophically naive and practically self-defeating. Many of the most important CS research questions — Why do programmers adopt some tools and ignore others? How do users form trust in AI systems? What makes a codebase maintainable? — resist quantitative reduction. By 2040, the human-centered turn in computing (HCI, software engineering, AI alignment, tech ethics) has made qualitative literacy essential for every CS researcher.

A **case study** is an in-depth investigation of a single instance — one development team, one software project, one deployment, one community. The goal is not statistical generalization (how common is this?) but **analytical generalization** (what mechanisms does this case reveal that may apply elsewhere?). Flyvbjerg (2006) defends the case study against the charge that "you can't generalize from N=1": crucial scientific insights — Galileo's inclined planes, Darwin's finches, Piaget's children — came from deep study of single cases. In CS, a case study of how one team at Google migrated from a monolith to microservices can reveal patterns, pitfalls, and design principles that inform theory, even if they don't produce a p-value. The case study methodology follows a structure: define the research question, select the case (purposeful sampling — choose an information-rich case, not a random one), collect data from multiple sources (interviews, documents, code repositories, observational notes), analyze through pattern-matching or explanation-building, and report with rich description.

**Grounded theory** (Glaser & Strauss, 1967) is a systematic qualitative methodology where theory *emerges from the data* rather than being imposed a priori. The researcher collects data (interviews, observations, artifacts), codes it line-by-line (open coding), groups codes into categories (axial coding), and identifies a core category that becomes the central theoretical insight (selective coding). The distinctive feature of grounded theory is **theoretical sampling**: you collect initial data, begin analysis, and then decide *what data to collect next* based on emerging theory — iterating until **theoretical saturation** (new data no longer yields new insights). In CS, grounded theory has been used to develop theories of debugging practice, open-source governance, and developer information needs. The 2040 researcher has an advantage: automated transcription and LLM-assisted coding can accelerate the mechanical aspects, but the interpretive leap — identifying what is theoretically significant — remains irreducibly human.

**Thematic analysis** (Braun & Clarke, 2006) is the most accessible qualitative method: read the data carefully, generate initial codes, search for themes, review themes, define and name themes, write the report. It is flexible (can be inductive or deductive, essentialist or constructionist) and appropriate when the research question is about experiences, perceptions, or practices. In CS, thematic analysis of developer forum posts might reveal barriers to adopting a new programming paradigm; analysis of user interviews might surface unarticulated needs for an AI assistant. The key to quality thematic analysis is **reflexivity** — the researcher acknowledges their own position, assumptions, and influence on the analysis. A 2040 AI systems researcher analyzing user trust in autonomous vehicles must disclose whether they work for an autonomous vehicle company.

**Required Reading:**
- Flyvbjerg, B. (2006). "Five Misunderstandings About Case-Study Research." *Qualitative Inquiry*, 12(2), 219–245.
- Seaman, C.B. (1999). "Qualitative Methods in Empirical Studies of Software Engineering." *IEEE Transactions on Software Engineering*, 25(4), 557–572.
- Braun, V. & Clarke, V. (2006). "Using Thematic Analysis in Psychology." *Qualitative Research in Psychology*, 3(2), 77–101.
- Stol, K.-J., Ralph, P., & Fitzgerald, B. (2016). "Grounded Theory in Software Engineering Research: A Critical Review and Guidelines." *ICSE 2016*.
- Alþjófsdóttir, S. (2040). *Listening to the Loom: Qualitative Methods for AI Systems Research*. Yggdrasil University Press.

**Discussion Questions:**
1. A quantitative CS researcher says: "Qualitative research is just anecdotes." Formulate a defense of qualitative methods that a quantitative colleague would find intellectually serious.
2. You're studying how developers use Copilot-like AI assistants. Design a qualitative study. What data would you collect? How would you know when you've reached saturation?
3. Reflexivity requires acknowledging your biases. If you are studying bias in AI hiring systems and you have strong prior beliefs about algorithmic fairness, how do you prevent your beliefs from distorting your analysis?

---

## Lecture 7: Survey Design and Human Subjects Research in CS

*"Ask a Norseman what he fears, and he'll say dishonor. Ask what he ate for breakfast, and you'll learn more from his silence than his words."*

Surveys are the most abused research instrument in computer science. A hastily written Google Form distributed on Twitter, analyzing Likert-scale responses as if they were continuous variables, drawing causal conclusions from correlational data — this describes a depressing fraction of published CS surveys. This lecture covers how to do surveys properly, and the ethical and regulatory framework governing research with human participants.

A valid survey begins with **construct validity**: does the survey actually measure what it claims to measure? If you want to measure "programmer productivity," what does that mean — lines of code? Tasks completed? Self-reported satisfaction? Each operationalization captures a different aspect of the construct, and none is complete. The solution is **multi-item scales**: measure each construct with multiple questions, test internal consistency (Cronbach's α ≥ 0.70 is conventional minimum), and validate against external criteria (e.g., do high scores on your productivity scale correlate with manager ratings?). Developing a new scale is a multi-study, multi-year undertaking; in CS405, you should use or adapt existing validated scales whenever possible — the **ACM Digital Library** and **APA PsycTESTS** are good sources.

**Sampling** determines who you can generalize to. A convenience sample (undergraduates in your department, Twitter followers, Mechanical Turk workers) tells you about those specific populations, not about "programmers" or "users" in general. In 2040, CS venues increasingly require authors to state the target population, sampling frame, and limitations on generalizability explicitly. If you survey 200 undergraduate CS majors about their AI tool usage, you have learned something about undergraduate CS majors at your institution — not about "software developers." Representativeness matters more than sample size: a representative sample of 200 beats a biased sample of 20,000.

**Question design** is a craft. Common errors: **double-barreled questions** ("Is the system fast and easy to use?" — these are two questions), **leading questions** ("How much did you enjoy the excellent new feature?"), **vague quantifiers** ("often," "sometimes" — these mean different things to different people), **unbalanced scales** (more positive than negative options), and **acquiescence bias** (tendency to agree). The solution: pilot test your survey with a small group, conduct cognitive interviews (ask respondents to think aloud while answering), and revise before full deployment. A well-designed survey in 2040 also includes **attention checks** (e.g., "For this question, please select 'Strongly Disagree'") to filter out careless respondents — a practice that has become standard following evidence that 5–15% of online survey responses are low-quality.

**Human subjects research ethics** is governed by the **Belmont Report** principles: **respect for persons** (informed consent, protection of vulnerable populations), **beneficence** (maximize benefits, minimize harms), and **justice** (fair distribution of research burdens and benefits). In practice, this means obtaining **Institutional Review Board (IRB)** approval before collecting data from human participants. At the University of Yggdrasil, the **Yggdrasil Ethics Board (YEB)** reviews all human-subjects CS research. Students must complete the **CITI Program** training in human subjects research before collecting any data for CS405. By 2040, new ethical challenges have emerged: studying user behavior in VR environments (where immersion raises consent questions), analyzing public social media data (where "public" doesn't necessarily mean "consented"), and experiments with AI systems that affect human participants (where the AI's behavior may cause unanticipated harm).

**Required Reading:**
- Kitchenham, B.A. & Pfleeger, S.L. (2008). "Personal Opinion Surveys." In *Guide to Advanced Empirical Software Engineering*, Springer, 63–92.
- Fowler, F.J. (2013). *Survey Research Methods* (5th ed.). Sage. Chapters 3–7.
- The Belmont Report (1979). "Ethical Principles and Guidelines for the Protection of Human Subjects of Research."
- Singer, J., Pham, R., & Hoang, L. (2020). "Broadening the Range of Designs and Methods in Software Engineering Research." *IEEE Software*, 37(5), 24–31.
- Yggdrasil Ethics Board (2040). *Guidelines for Human-Subjects Research in Computing*. YEB-POL-2020-04.

**Discussion Questions:**
1. You want to study how developers debug. You consider: (a) a survey, (b) an observational study in a lab, (c) an analysis of GitHub commit logs. Compare the strengths and weaknesses of each for understanding debugging behavior.
2. A survey on Stack Overflow asks developers about mental health. What ethical considerations arise? Is a public forum post "consent" for research use?
3. Design three attention-check questions appropriate for a survey about programmer experience with AI code assistants.

---

## Lecture 8: Writing the Research Paper — Structure, Argument, and Clarity

*"A saga poorly told is a battle forgotten. A paper poorly written is a discovery lost."*

The best research in the world is worthless if no one can understand it. Writing is not an afterthought to research — it is part of research. The act of writing clarifies thinking, exposes gaps in logic, and forces precision that "I know it in my head" never delivers. This lecture covers the craft of the CS research paper: the standard structure, the art of argument, and the discipline of clarity.

The canonical CS paper follows the **IMRaD structure**: Introduction, Methods, Results, and Discussion. The **Introduction** answers: What is the problem? Why does it matter? What has been done before (brief lit review)? What is the gap? What is your contribution? The last paragraph should enumerate contributions explicitly: "This paper makes the following contributions: (1) ..., (2) ..., (3) ..." The **Methods** section describes what you did in sufficient detail that a competent researcher could replicate it — this is the most commonly skimped section, and the most commonly criticized. The **Results** section presents findings without interpretation; it is a factual report, supported by tables, figures, and statistical tests. The **Discussion** interprets the results, compares to prior work, acknowledges limitations, and suggests future directions. A strong Discussion does not merely restate results; it draws out implications, proposes mechanisms, and honestly addresses weaknesses.

Beyond structure, a strong CS paper has a **narrative arc**. The reader should feel tension (a problem unsolved), journey (your approach), and resolution (what we now know). This does not mean hype or exaggeration — it means clear stakes. "We propose a new sorting algorithm" has no stakes. "Existing sorting algorithms leave 40% of memory bandwidth unused on modern NUMA architectures; we close this gap, achieving 1.7× speedup on TPC-H benchmarks" has stakes. The **contribution** must be specific and falsifiable: if your paper says "we contribute a framework for understanding X," that's vague; if it says "we contribute a taxonomy of six bug patterns in distributed consensus protocols, validated on 500 Apache ZooKeeper issues," that's concrete.

**Clarity** is a moral obligation. Obfuscated writing wastes reviewer time, impedes replication, and excludes non-native English speakers from participating in the scientific conversation. Specific disciplines: use the **active voice** ("We measured throughput" not "Throughput was measured"), define all **acronyms** on first use (and minimize them — a paper with 15 acronyms is unreadable), place **figures and tables** close to where they're first referenced, caption them with complete descriptions (a reader should understand the figure without reading the body text), and use **parallel structure** in lists and comparisons. For non-native English writers, tools like Grammarly, Writefull, and the University's own **SkaldWrite** (an LLM-based academic writing assistant that preserves author voice while improving clarity) are standard in 2040 — but they must be disclosed in the acknowledgments if substantially used.

The **abstract** deserves special attention — it is the most-read part of any paper, often the only part read by casual browsers. A strong abstract follows a formula: context (1 sentence), problem (1 sentence), approach (1–2 sentences), key results (1–2 sentences with numbers), implication (1 sentence). It should be self-contained; don't use undefined acronyms or reference the paper itself ("in this paper we show..."). Most CS conference abstracts are 150–250 words. Write the abstract last, after the paper is complete, so it accurately reflects what you actually found (not what you hoped to find).

**Required Reading:**
- Zobel, J. (2014). *Writing for Computer Science* (3rd ed.). Springer. Chapters 1–5, 9.
- Knuth, D.E., Larrabee, T., & Roberts, P.M. (1989). *Mathematical Writing*. MAA Notes No. 14.
- Sheard, J. (2012). "The Structure and Presentation of Computing Research Papers." *ACM Inroads*, 3(3), 32–36.
- Peyton Jones, S. (2004). "How to Write a Great Research Paper." *Microsoft Research Cambridge*. [Video and slides — watch before attempting your manuscript.]
- Ljósaskáld, R. (2038). *Runes on the Page: Academic Writing as Skaldic Craft*. Yggdrasil University Press.

**Discussion Questions:**
1. Read the abstract of a recent paper from a top CS venue. Does it follow the formula? Could you understand the contribution from the abstract alone? Rewrite it to be clearer.
2. "The system was designed, and experiments were conducted. Results were obtained and they were found to be significant." Rewrite this in active voice with specific details. What's missing?
3. A student writes a methods section that says "We used Python with scikit-learn." Is this sufficient for replication? What minimum information is required?

---

## Lecture 9: Peer Review — The Gatekeeping Mechanism of Science

*"The þing was no place for the thin-skinned. Every law, every claim, every dispute was tested in the fire of public scrutiny. So too is peer review the modern þing of science."*

Peer review is the quality-control mechanism of science: before publication, your work is evaluated by anonymous experts who assess its correctness, novelty, clarity, and significance. It is simultaneously the best system we have and deeply flawed — biased, noisy, slow, and vulnerable to gatekeeping. Understanding peer review from both sides (as author and reviewer) is essential for any research career.

The **review process** varies by venue but follows a general pattern. For CS conferences (the dominant publication model in CS, unlike journals in most sciences), papers are submitted to a program committee (PC) of 20–50 experts. Each paper receives 3–5 reviews. Reviewers rate the paper (strong accept / accept / weak accept / weak reject / reject / strong reject), provide detailed comments, and discuss with other reviewers during a PC meeting or online discussion period. The area chair or program chair makes the final decision. Most top CS conferences accept 15–25% of submissions; the bar is high. By 2040, many venues have adopted **open review** (reviewer identities are public) or **collaborative review** (authors and reviewers interact during the review period), but **double-blind review** (neither side knows the other's identity) remains the most common model, as it reduces bias against authors from less-prestigious institutions or underrepresented groups.

**Writing a good review** is a skill that CS405 explicitly teaches. The review should: (1) summarize the paper to demonstrate you understood it (this is also a sanity check — if your summary is wrong, the authors can point to it in rebuttal); (2) identify strengths (what did the paper do well? — reviews that are entirely negative are not constructive); (3) identify weaknesses, organized by severity (fatal flaws vs. fixable issues); (4) provide specific, actionable suggestions for improvement (not "the writing is bad" but "the threat model in Section 3.2 is unclear because it doesn't specify the attacker's capabilities — please add a capabilities table"); and (5) give a clear recommendation with justification. A review that says "Reject. This is not novel" without explaining *what prior work* covers the same ground is useless. A review that provides detailed, constructive feedback on a paper it recommends rejecting can still be a good review.

**Responding to reviews** (the rebuttal) is a delicate art. The principles: (1) thank the reviewers for their time and insight (sincerely — they volunteered); (2) address every substantive criticism, quoting the reviewer's text and responding point-by-point; (3) be specific about what you changed ("We added a new experiment with 10 datasets, showing our method's robustness — see new Figure 5 and Table 3"); (4) never be defensive or dismissive — if a reviewer misunderstood, assume your writing was unclear, not that the reviewer was lazy; (5) if you disagree, do so respectfully and with evidence ("The reviewer suggests Method X as a baseline. We did not include it because X requires labeled data while our method is unsupervised, but we have added a discussion of this limitation in Section 5.3"). The rebuttal tone matters enormously: a gracious, thorough rebuttal can flip a borderline reject to accept; a dismissive, argumentative rebuttal can flip a borderline accept to reject.

The **ethics of reviewing** include: confidentiality (don't share the paper or reviews), conflict of interest (recuse yourself if you have a personal or professional relationship with the authors), timeliness (submit reviews by the deadline), and constructive engagement (review to improve the work, not to punish rivals). In 2040, with LLMs capable of generating plausible reviews, CS venues have established policies requiring reviewers to disclose AI assistance and to personally verify all AI-generated content. A reviewer who pastes an LLM's output without critical engagement is violating both the letter and spirit of peer review.

**Required Reading:**
- Smith, A.J. (1990). "The Task of the Referee." *IEEE Computer*, 23(4), 65–71. Still the canonical advice — read before every review.
- Ragone, A., Mirylenka, K., Casati, F., & Marchese, M. (2013). "On Peer Review in Computer Science." *Communications of the ACM*, 56(10), 74–79.
- Shah, N.B. (2022). "Challenges, Experiments, and Computational Solutions in Peer Review." *Communications of the ACM*, 65(6), 70–75.
- Tomkins, A., Zhang, M., & Heavlin, W.D. (2017). "Reviewer Bias in Single- Versus Double-Blind Reviewing." *PNAS*, 114(48), 12707–12713.
- Yggdrasil Computing Conference (YCC) 2040. *Reviewing Guidelines for YCC 2040*. Includes the University's AI-assisted review policy.

**Discussion Questions:**
1. You receive a review that says "The paper is poorly written and the results are unimpressive." Is this an actionable review? How would you respond as an author? As a PC chair reading this review, how would you evaluate the reviewer?
2. Double-blind review aims to reduce bias. But can you really anonymize a paper when the work builds on the authors' prior publications? Where is the line between "blind" and "practically identifiable"?
3. In 2040, some venues experiment with LLM-assisted triage — using AI to flag papers with obvious methodological problems before human review. What are the risks? What problems is this most appropriate for?

---

## Lecture 10: Reproducibility, Replicability, and Open Science in 2040

*"A rune that only one carver can read is no rune at all — it's a scratch."*

The reproducibility crisis has been the defining methodological challenge of early 21st-century science. In computer science, the crisis manifested as the realization that most published results could not be independently verified: code not released, data not shared, experimental configurations not documented, computational environments not preserved. This lecture covers the institutional response, the tools enabling reproducibility, and the evolving norms of open science in 2040.

Terminology matters. The ACM distinguishes **repeatability** (same team, same setup → same result), **reproducibility** (different team, same setup → same result), and **replicability** (different team, different setup → same finding). Most CS "reproducibility" efforts actually target repeatability — getting the authors' code to produce the reported numbers. True replication — re-implementing the method from the paper description and getting comparable results on new data — is rarer, harder, and more scientifically valuable. A result that survives independent replication across labs, datasets, and implementations earns confidence; a result that only works on the authors' laptop under specific conditions does not.

The **artifact evaluation (AE)** process, now standard at top CS venues by 2040, requires authors to submit a Docker container or equivalent with their code, data, and scripts. AE reviewers attempt to reproduce the key results within a time budget (typically 2–4 hours). Badges awarded: **Artifacts Available** (code/data publicly accessible), **Artifacts Evaluated** (artifacts are complete and functional), **Results Reproduced** (main claims verified within acceptable tolerance). The system has been transformative: venues that adopted AE report that 60–80% of accepted papers submit artifacts, and 40–60% of those earn the "Results Reproduced" badge. The fraction that cannot be reproduced — because of proprietary data, specialized hardware, or simply broken artifacts — is a humbling reminder of how fragile computational results can be.

The **FAIR principles** — Findable, Accessible, Interoperable, Reusable — provide the framework for data management in 2040. Data should have persistent identifiers (DOIs), rich metadata, clear licenses, and standard formats. The University of Yggdrasil's **Yggdrasil Data Repository (YDR)** archives all CS405 project data with FAIR compliance. For code, the standard is a public repository (GitHub, GitLab, or the University's **Yggdrasil Code Forge**) with a clear README, dependency specification (Dockerfile, requirements.txt, conda environment), and a single script to regenerate all results from raw data. The "Works on My Machine" (WOMM) badge — an ironic sticker some researchers put on their laptops — is a reminder of what not to do.

**Open science** extends beyond reproducibility to encompass open access publishing, open peer review, preregistration of studies, and registered reports (journals accept the study design before results are known, eliminating publication bias against null results). By 2040, the University of Yggdrasil mandates that all university-funded research be published open access (gold OA with CC-BY license), with article processing charges covered by the university's **Open Knowledge Fund**. Preprints on arXiv or the University's own **Yggdrasil Preprint Server** are the norm; papers appear publicly before peer review, accelerating dissemination while trusting the community to distinguish preprint from peer-reviewed version. CS405 requires students to post their final project as a preprint and to cite it in their CV as "CS405 Project, Yggdrasil University (2040), preprint."

**Required Reading:**
- ACM (2020). "Artifact Review and Badging — Version 2.0." (Updated 2038.)
- Wilkinson, M. et al. (2016). "The FAIR Guiding Principles for Scientific Data Management and Stewardship." *Scientific Data*, 3, 160018.
- Collberg, C. & Proebsting, T.A. (2016). "Repeatability in Computer Systems Research." *Communications of the ACM*, 59(3), 62–69.
- Peng, R.D. (2011). "Reproducible Research in Computational Science." *Science*, 334(6060), 1226–1227.
- University of Yggdrasil Senate (2040). *Open Science Policy*. YGG-POL-2040-01. Mandates open access, FAIR data, and preprint deposition for all university-funded research.

**Discussion Questions:**
1. A groundbreaking ML paper achieves state-of-the-art results but requires a cluster of 4096 GPUs and a proprietary dataset (Twitter internal data). Is this reproducible? Is it good science? How should the community handle irreproducible but important work?
2. You attempt to reproduce a paper's results and get numbers that are directionally similar (same trends) but numerically different (within 5%). Does the paper earn "Results Reproduced"? What threshold is appropriate?
3. Preregistration requires committing to your analysis plan before seeing the data. How does this interact with exploratory data analysis, where you discover patterns you didn't anticipate? Can both coexist?

---

## Lecture 11: Research Ethics in Computing — Bias, Privacy, and Dual-Use

*"The smith who forges a sword cannot claim ignorance of its purpose."*

Computing research in 2040 operates in a landscape of heightened ethical stakes. AI systems make decisions about loans, bail, hiring, and healthcare. Social media platforms shape political discourse for billions. Autonomous vehicles make life-and-death choices. Facial recognition enables both convenience and surveillance. The researcher cannot claim neutrality — every technical contribution has ethical implications, and ignoring them is itself an ethical choice.

**Algorithmic bias** is the most visible ethical challenge. Bias enters ML systems through multiple pathways: **training data bias** (historical data reflects existing discrimination), **label bias** (human annotators encode their prejudices), **representation bias** (some groups are underrepresented in the data), **measurement bias** (the chosen metric doesn't capture what matters for all groups), and **deployment bias** (the system is used in contexts for which it wasn't designed). The COMPAS recidivism prediction algorithm (Angwin et al., 2016) — which was no more accurate than random humans but exhibited racial disparities in false positive rates — became the canonical case study. By 2040, "fairness" has matured into a subfield with its own conferences (FAccT, AIES) and its own methodological toolkit: fairness metrics (demographic parity, equalized odds, individual fairness), bias mitigation techniques (pre-processing, in-processing, post-processing), and documentation frameworks (Model Cards, Datasheets for Datasets). Every CS405 project involving ML must include a **fairness analysis** — even if only to document why fairness is not a concern for this particular application.

**Privacy** is the second pillar. CS research routinely involves user data — and even "anonymized" data can often be re-identified (Sweeney, 2000, showed that 87% of the U.S. population is uniquely identifiable by ZIP code, gender, and date of birth). Differential privacy (Dwork et al., 2006) provides a mathematical guarantee: the output of a computation should be nearly indistinguishable whether any individual's data is included or not, parameterized by ε (the privacy budget). By 2040, differential privacy has moved from theory to practice — the U.S. Census Bureau used it for the 2020 Census, Apple and Google use it for telemetry, and the University's research cloud provides differentially-private query APIs. Federated learning — training models across decentralized data without centralizing it — addresses a different aspect of privacy but introduces its own research challenges (heterogeneous data distributions, communication efficiency, Byzantine resilience).

**Dual-use** refers to research with both beneficial and harmful applications. Every CS researcher must ask: "What is the worst thing someone could do with my work, and does the expected benefit justify that risk?" Facial recognition can find missing children — and enable mass surveillance. Language models can help people write — and generate disinformation at scale. Vulnerability discovery can improve security — and enable attacks. There is no formula for resolving dual-use dilemmas, but the ethical researcher engages with the question honestly, discloses risks in the paper's **Broader Impact Statement** (now required by many CS venues), and, where possible, includes mitigations or "defensive" applications alongside the primary contribution. The 2040 researcher also considers **environmental ethics**: the carbon footprint of training large models (Strubell et al., 2019) must be reported and, where disproportionate, justified.

**Required Reading:**
- Angwin, J., Larson, J., Mattu, S., & Kirchner, L. (2016). "Machine Bias." *ProPublica*, May 23, 2016.
- Dwork, C. & Roth, A. (2014). "The Algorithmic Foundations of Differential Privacy." *Foundations and Trends in Theoretical Computer Science*, 9(3–4), 211–407. Chapters 1–3.
- Mitchell, M. et al. (2019). "Model Cards for Model Reporting." *FAT* 2019.
- Strubell, E., Ganesh, A., & McCallum, A. (2019). "Energy and Policy Considerations for Deep Learning in NLP." *ACL 2019*.
- Heimsdóttir, F. (2039). *The Sword and the Plow: Dual-Use Ethics in AI Research*. Yggdrasil University Press. Chapters 1, 4, 7.

**Discussion Questions:**
1. You develop a technique that makes language models 10× more efficient at generating persuasive text. What beneficial applications can you imagine? What harmful ones? Does the benefit justify the risk? What, if anything, should you do to mitigate harm?
2. A startup releases a "fair" hiring algorithm that achieves demographic parity by adjusting scores. A qualified candidate is rejected because their group's adjustment is negative. Is this algorithm fair? To whom? What's the tension between group fairness and individual fairness?
3. Your research requires user data. You anonymize it by stripping names and email addresses. Is this sufficient? What re-identification risks remain, and what additional protections would you implement?

---

## Lecture 12: The Research Career — From Proposal to Publication to Impact

*"The longship is not built for the harbor. Research is not done for the file drawer."*

The final lecture zooms out from methods to career: how does one actually become a productive, impactful CS researcher? This is not a "how to get tenure" lecture (though that's part of it) — it's about building a sustainable practice of inquiry that produces work you're proud of, that influences your field, and that maintains your intellectual vitality across decades.

**Finding your research question** is the hardest step. The best research questions emerge from a combination of: (1) deep technical mastery (you understand the state of the art so well that you can see what's missing), (2) practical exposure (you've built systems and encountered real problems), and (3) intellectual taste (you can distinguish a deep, fundamental question from a shallow, trendy one). The 2040 CS landscape is vast — from quantum algorithms to AI ethics to bio-computing to HCI — and finding your niche requires exploration. The University of Yggdrasil's **Research Rotation Program** allows CS405 students to spend 4 weeks embedded in a research lab before committing to a project. Use it. Read broadly across subfields; the most innovative work often comes from cross-fertilization (bringing database ideas to programming languages, or cognitive science ideas to systems design).

**The research workflow** in 2040 is supported by a rich ecosystem of tools. Literature discovery: Semantic Scholar, Elicit, the Yggdrasil Huginn Engine. Experiment management: Weights & Biases, MLflow, the Yggdrasil Experiment Tracker. Writing: Overleaf (collaborative LaTeX), the University's SkaldWrite assistant. Version control: Git with the University's Code Forge. Preprint distribution: arXiv, the Yggdrasil Preprint Server. But tools don't replace discipline. The most productive researchers have systems: they maintain research notebooks (Obsidian, Notion, or plain Markdown — the medium doesn't matter, the habit does), they block deep-work time on their calendars (3–4 uninterrupted hours, at least 3× per week), they read one paper per day (not just skimming — reading with a critical lens, asking "what would I do differently?"), and they write every day (even 200 words of a draft, even just refining a figure caption — the project stays alive in your mind).

**Mentorship** is the hidden infrastructure of a research career. Find mentors who are generous with their time, honest in their feedback, and invested in your growth (not just in your output). A good advisor does not tell you what to do; they help you figure out what you want to do and then hold you to a standard you didn't know you could meet. In 2040, mentorship extends beyond the traditional advisor-student dyad: peer mentoring groups, online research communities (the **Yggdrasil Research Discord** has 4,000 members), and reverse mentoring (junior researchers teaching senior ones about new tools and methods) are all part of the ecosystem. Be a mentor to someone junior to you — teaching is the deepest form of learning.

**Measuring impact** — not just counting papers. The pressure to publish can distort research: safe, incremental papers that "fill a gap" in the literature but move nothing forward. Instead, ask: "If my paper didn't exist, would anyone notice? Would anyone's research be harder to do? Would anyone's system be worse?" Impact comes in many forms: a paper that changes how people think (the conceptual contribution), a system that people actually use (the engineering contribution), a dataset that enables a hundred other papers (the infrastructure contribution), a teaching method that transforms CS education (the pedagogical contribution). Your career will span 40+ years. The goal is not to maximize your h-index in year 5 — it's to look back at year 40 and feel that computing is different, and better, because you were here.

**Required Reading:**
- Hamming, R. (1986). "You and Your Research." *Bell Communications Research Colloquium*. [Transcript widely available online; one of the most-cited talks on research strategy.]
- Levin, L. & Redmiles, D. (2023). "On the Ph.D.: A Guide for the Perplexed." *Communications of the ACM*, 66(2), 30–32.
- Guo, P. (2014). "The Productive Researcher." *Communications of the ACM*, 57(3), 30–31.
- Rúnarsson, A. (2038). *The Longship and the Harbor: Sustaining a Research Life*. Yggdrasil University Press.
- University of Yggdrasil Office of Research (2040). *Research Rotation Program Guide 2040–2041*.

**Discussion Questions:**
1. Hamming's talk asks: "What are the most important problems in your field, and why aren't you working on them?" What are the most important problems in CS in 2040? Which one would you work on, and what's stopping you?
2. A junior researcher can either: (a) publish 4 incremental papers per year on a hot topic, or (b) spend 2 years on a risky, fundamental question that might produce nothing. Which path would you choose at different career stages? What institutional incentives push researchers toward (a)?
3. What does it mean for a piece of CS research to "have impact"? Give examples of impactful work that wasn't highly cited, and highly cited work that wasn't impactful.

---

## Final Examination Preparation

The CS405 final examination consists of two components:

### Part A: Research Methods Exam (40%)
You will be given a short research paper (8–10 pages) from a recent CS venue. You must write a critical analysis addressing: (1) Is the research question well-defined and appropriately scoped? (2) Evaluate the experiment design — identify at least three threats to validity and propose mitigations. (3) Assess the statistical analysis — are the right tests used? Are effect sizes and confidence intervals reported? (4) Is the paper reproducible based on the information provided? What's missing? (5) Does the broader impact statement adequately address ethical concerns?

### Part B: Mini Research Project (60%)
Over the final four weeks of the term, you will complete a mini research project following the full CS research pipeline. The project must:
1. **Proposal (Week 1):** A 1-page research proposal with research question, hypothesis, proposed methodology, and expected contributions. Reviewed by peers and instructor.
2. **Systematic Literature Review (Week 2):** A PRISMA-style review of at least 30 candidate papers narrowed to 12–18 included studies, with a narrative synthesis identifying consensus, controversy, and gaps.
3. **Experiment & Analysis (Weeks 3–4):** Execute your experiment on the Yggdrasil Research Cloud. Report results with proper statistics (effect sizes, confidence intervals, distributional summaries). Submit an artifact container for reproducibility evaluation.
4. **Manuscript (Week 5):** A full conference-style paper (6–8 pages, ACM format) with IMRaD structure, proper citations, and a broader impact statement.
5. **Peer Review (Week 5):** Review two classmates' manuscripts using YCC reviewing standards. Provide constructive, specific feedback. Your review quality is graded.
6. **Rebuttal & Revision (Week 6):** Respond to peer reviews, revise your manuscript, and submit the final version. Post the camera-ready preprint to the Yggdrasil Preprint Server.

### Sample Essay Questions (Choose 4 of 8):
1. "Computer science is not a science but an engineering discipline." Defend or refute this claim with reference to specific methodologies discussed in this course. What are the implications for how CS research should be conducted and evaluated?
2. A colleague proposes benchmarking their new database system by running the TPC-H benchmark once on their laptop and reporting the time. Using concepts from Lectures 3, 4, and 5, write a detailed critique and prescribe a rigorous alternative methodology.
3. Compare and contrast systematic literature reviews, case studies, and grounded theory as approaches to knowledge generation in CS. For each, describe: (a) the type of research question it best addresses, (b) the standards for rigor, and (c) a concrete CS research scenario where it would be the preferred method.
4. The reproducibility crisis has been called "science's self-correcting mechanism at work." Evaluate this claim. Is the crisis a sign of health (problems being identified and fixed) or pathology (systemic dysfunction)? Use specific evidence from the CS reproducibility literature.
5. You are the PC chair of a top CS conference. Propose three reforms to the peer review process that would improve fairness, quality, or efficiency. For each reform, discuss potential unintended consequences and how you'd mitigate them.
6. Design a quantitative study to evaluate whether pair programming improves code quality. Specify: research question, independent and dependent variables, controls, sample size justification, statistical analysis plan, and threats to validity with proposed mitigations.
7. "Algorithmic fairness is impossible — you cannot satisfy all fairness criteria simultaneously, so the pursuit is futile." Critically evaluate this claim using the fairness impossibility theorems (e.g., Kleinberg et al., 2017). What does "fairness" mean in the face of mathematical impossibility?
8. You've developed a technique that dramatically improves AI system performance. A defense contractor wants to license it for autonomous drone targeting. A medical nonprofit wants it for cancer detection. Using the dual-use ethics framework, analyze your obligations and possible courses of action.

---

*This course was woven at the University of Yggdrasil, 2040 — where research is not merely about finding answers, but about learning to ask questions worthy of a lifetime.*
