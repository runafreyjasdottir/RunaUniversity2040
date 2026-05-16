# CS405: Research Methods in Computer Science
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4
**Instructor:** Prof. Sigrún Hrafnsdóttir, Ph.D.
**Office:** Fenrir Hall, Room 407
**Email:** s.hrafnsdottir@yggdrasil.edu
**Semester:** Spring 2040

**Description:** A comprehensive introduction to research methodology in computing. Students learn systematic literature review, experimental design, statistical analysis, qualitative methods in HCI, academic writing and peer review, research ethics, and AI-assisted research workflows. By course end, each student produces a complete research proposal ready for capstone execution.

**Prerequisites:** CS208 Formal Methods or equivalent; proficiency in Python and statistical computing.

**Required Texts:**
- Wulfgar, E. & Chen, L. (2039). *The Digital Longhouse: Research Methods for 21st-Century Computing*. Yggdrasil Press.
- Liang, R., Müller, K., & Ogunleye, T. (2038). *Reproducible Research in the Age of AI*. Springer Nature.
- The ACM/IEEE-CS *Joint Curriculum Guidelines for Computing Research Methods*, 2037 Edition.

**Assessment:** Literature review (20%), experiment design (25%), full research proposal (35%), peer review portfolio (20%).

---

## Lecture 1: What Makes Computing a Science — The Seiðr of Systematic Inquiry

*"Science is a way of trying not to fool yourself. The first principle is that you must not fool yourself — and you are the easiest person to fool."* — Richard Feynman, 1974

Before we can do research, we must understand what research *is*. Computer science occupies a peculiar epistemological position — it is simultaneously a formal mathematical discipline, an engineering practice, and an empirical natural science. The early pioneers of our field debated whether "computer science" was even a science at all. Herbert Simon (1969) argued we study the "sciences of the artificial" — designed systems, not natural phenomena. Donald Knuth maintained that algorithm analysis is a branch of mathematics. Yet the past century has made the empirical dimension undeniable: we measure cache misses, A/B test user interfaces, benchmark neural architectures, and statistically evaluate the safety properties of autonomous systems.

The 2040 consensus recognises three complementary knowledge-generation modes in computing research. **Formal-deductive research** proceeds from axioms to theorems via logical proof — this is the tradition of Turing, Church, Hoare, and the verification community you encountered in CS208. **Engineering-constructive research** builds artefacts to demonstrate possibility — the compiler, the operating system, the language model that shows a new capability is achievable. **Empirical-inductive research** gathers data from systems, users, or the world and draws generalizable conclusions — this is where research methods proper become essential. Most modern computing research employs all three modes in concert. A self-driving car paper may include formal safety guarantees (deductive), a working prototype (constructive), and crash-rate statistics from 10 million kilometres (empirical).

The Norse parallel is instructive. The vǫlva — the seeress who practiced seiðr — did not simply "see" the future. She altered her state of consciousness through ritual, gathered data through trance-journeys, interpreted omens systematically, and presented her findings in poetic verse that could be evaluated by the community. Bad seiðr was vague and unfalsifiable; good seiðr produced actionable knowledge. The research method is our modern seiðr: a disciplined practice of altering our ignorance, gathering evidence systematically, and presenting conclusions that others can verify.

The lecture concludes by introducing the research lifecycle that structures this course: (1) question formulation, (2) literature grounding, (3) method design, (4) data collection, (5) analysis and interpretation, (6) dissemination and peer review, (7) reproduction and extension. Each subsequent lecture deepens one phase.

**Required Reading:**
- Wulfgar & Chen (2039), Chapter 1: "The Three Pillars of Computing Science."
- Simon, H. A. (1969). *The Sciences of the Artificial*. MIT Press. Chapter 1.
- Denning, P. J. (2005). "Is Computer Science Science?" *Communications of the ACM*, 48(4), 27–31.

**Discussion Questions:**
1. Is a benchmark result that cannot be reproduced by an independent lab "science"? Why or why not?
2. Consider a paper that proves a theorem about a protocol but never implements it. Is this "computer science" or "mathematics"? Does the distinction matter?
3. In what ways does the training of modern AI models violate or comply with the principles of empirical science? Are we doing seiðr, or just casting runes?

---

## Lecture 2: Literature Review — Mapping the Territory Before You Build

*"If I have seen further, it is by standing on the shoulders of giants."* — Isaac Newton, 1675

A researcher who does not know the literature is a builder who does not survey the land — their edifice may be magnificent, but it will almost certainly sink into a bog. The systematic literature review (SLR) is the cartographic phase of research: it maps what is known, identifies what is contested, and precisely locates the gap your work will fill.

This lecture teaches the modern SLR pipeline. **Phase 1: Search strategy.** Choose databases (ACM DL, IEEE Xplore, arXiv, dblp, Semantic Scholar, Scopus), craft boolean queries using controlled vocabularies (ACM Computing Classification System, IEEE Thesaurus), and document your search string so it is reproducible. By 2040, AI-assisted search tools like Semantic Scholar's "TLDR" generation and Elicit's automated screening can pre-filter thousands of papers — but the researcher must still validate inclusion/exclusion criteria.

**Phase 2: Screening.** The PRISMA 2035 flow diagram (an update to the classic 2009 PRISMA from medicine) tracks papers through title screening, abstract screening, and full-text assessment. A well-run SLR might start with 2,847 hits, screen down to 341, and ultimately include 47 papers. Every exclusion must be justified: wrong population, wrong intervention, insufficient rigour, language barrier, publication date outside scope.

**Phase 3: Data extraction and synthesis.** Build a structured extraction form: research question, methodology, sample size, effect size, threats to validity. For quantitative meta-analysis, extract means, standard deviations, and sample sizes per condition. For qualitative synthesis, use thematic analysis or meta-ethnography. The 2040 toolkit includes automated extraction tools (GROBID for PDF structure, LLM-assisted coding), but the researcher remains responsible for correctness.

**Phase 4: Writing the review.** A good literature review is not an annotated bibliography. It tells a story: "Here is what we knew, here is where the arguments were, here is the gap nobody noticed, and here is why that gap matters." Use synthesis matrices to group studies by finding rather than chronologically. Cite precisely — every factual claim about prior work needs a citation.

The lecture walks through a worked example: reviewing the literature on "formal verification of smart contracts" from 2015 to 2040, showing the search string, PRISMA diagram, extraction table, and final narrative synthesis.

**Required Reading:**
- Kitchenham, B. & Charters, S. (2007, updated 2038). *Guidelines for Performing Systematic Literature Reviews in Software Engineering*. EBSE Technical Report.
- Wulfgar & Chen (2039), Chapter 2: "Literature as Territory."
- Page, M. J. et al. (2035). "The PRISMA 2035 Statement: An Updated Guideline for Reporting Systematic Reviews." *ACM Computing Surveys*, 57(3), 1–36.

**Discussion Questions:**
1. At what point does an SLR become so large that no human can meaningfully synthesise it? Can an LLM do the synthesis, and if so, is the result still "science"?
2. How do you handle the grey literature problem — blog posts, preprints, corporate technical reports that contain crucial findings but lack peer review?
3. Search for "quantum computing supremacy" on three different databases using the same query. How different are the top 10 results? What does this tell you about database coverage bias?

---

## Lecture 3: Research Questions — Sharpening the Blade Before You Strike

*"The formulation of a problem is often more essential than its solution."* — Albert Einstein, 1938

A research question is the sharpened edge of inquiry. A dull question — "How can we make neural networks better?" — produces vague answers or none at all. A sharp question — "Does layer-wise learning rate decay improve adversarial robustness in vision transformers trained on ImageNet-scale data, and if so, through what mechanism?" — defines method, scope, and epistemological commitment in one sentence.

This lecture teaches question formulation frameworks. **The PICOC framework** (Population, Intervention, Comparison, Outcome, Context) adapts the medical PICO model for computing: *Population* (what system, algorithm, or users?), *Intervention* (what technique or tool?), *Comparison* (against what baseline?), *Outcome* (measured how?), *Context* (under what conditions?). Example: "For **Python developers** (P) working in small teams, does **property-based testing** (I) compared to **example-based unit testing** (C) reduce **production defect density** (O) in **startup environments** (C)?"

**The FINER criteria** (Feasible, Interesting, Novel, Ethical, Relevant), adapted from Hulley et al. (2007), provide a quality filter. *Feasible:* Can you actually get the data? A study requiring 10,000 GPU-hours may be infeasible for a student. *Interesting:* Will anyone care about the answer? *Novel:* Has someone already answered this? (This is why Lecture 2 came first.) *Ethical:* Does the research harm anyone? *Relevant:* Does the answer advance the field?

We then examine the **relationship between research questions and research paradigms**. A question like "What is the experience of underrepresented students in CS gateway courses?" calls for qualitative methods (interviews, phenomenology). A question like "Does compiler optimisation level O3 reduce execution time more than O2 for SPEC benchmark programs?" calls for quantitative experiment with statistical testing. A question like "Can we formalise the security guarantees of the Noise Protocol Framework in the symbolic model?" calls for formal proof. The question dictates the method, not the reverse — a common novice error is choosing a favourite method and then hunting for a question it can answer.

**Hypothesis formulation** — the transition from question to testable prediction — rounds out the lecture. A good hypothesis is falsifiable (Popper, 1959), directional when theory supports it, and operationalised in measurable terms. "Neural networks with attention mechanisms will achieve higher accuracy" is not a hypothesis — it's a vague hope. "Transformer models with multi-head self-attention will achieve at least 3% higher top-1 accuracy than equivalent-parameter CNNs on CIFAR-100 classification" is a hypothesis you can actually test.

**Required Reading:**
- Wulfgar & Chen (2039), Chapter 3: "The Question as Weapon."
- Easterbrook, S., Singer, J., Storey, M.-A., & Damian, D. (2008). "Selecting Empirical Methods for Software Engineering Research." In *Guide to Advanced Empirical Software Engineering*. Springer.
- Popper, K. (1959). *The Logic of Scientific Discovery*. Sections 1–6 (on falsifiability).

**Discussion Questions:**
1. Draft three PICOC-formatted research questions about the same topic (e.g., code review effectiveness). Which variant is sharpest and why?
2. Is a research question that is Feasible and Interesting but not at all Novel still worth pursuing? Under what circumstances?
3. Consider the hypothesis: "GitHub Copilot reduces coding time." Identify the missing operationalisation, comparison condition, and scope that make this untestable as stated.

---

## Lecture 4: Experimental Design — Constructing the Mead Hall of Evidence

*"To call in the statistician after the experiment is done may be no more than asking him to perform a post-mortem: he may be able to say what the experiment died of."* — R. A. Fisher, 1938

An experiment is a controlled intervention designed to isolate causal effects. In computing research, we experiment on algorithms (runtime comparisons), systems (throughput under load), humans (usability studies), and increasingly, AI agents (behaviour under prompt variations). This lecture covers the architecture of experimental design: how to build a structure that, when you pour data through it, filters out noise and leaves only signal.

**Fundamental principles.** *Randomisation* breaks confounding — if you randomly assign subjects to treatment and control, any pre-existing difference is, on average, balanced. *Blocking* increases precision by grouping similar experimental units (e.g., running all algorithms on the same hardware to control for machine variance; stratifying human subjects by programming experience level). *Replication* distinguishes real effects from random fluctuation — one run of a stochastic algorithm proves nothing; thirty runs with confidence intervals might. *Factorial designs* test multiple factors simultaneously and can detect interactions: does the new garbage collector help more with large heaps than small ones?

**Common designs in CS research.** The simplest is the **completely randomised two-group design**: treatment vs. control, analysed with an independent-samples t-test or Mann-Whitney U. But computing often calls for more: **repeated measures** (the same code run under multiple compiler flags), **Latin squares** (counterbalancing order effects in usability studies where each participant sees multiple interfaces), and **fractional factorial designs** (when you have 12 compiler flags to test but can't run all 4,096 combinations).

**Internal validity threats** in computing experiments are specific and insidious. *Selection bias:* if your "random" sample of GitHub repositories is actually the top 100 most-starred, your findings don't generalise. *Maturation:* if your long-running benchmark sees performance degrade over hours due to memory fragmentation, that's not the algorithm's fault. *Instrumentation:* if your profiler overhead is larger than the effect you're measuring, you're measuring the profiler. *Diffusion of treatment:* if your "control group" of developers finds out about the new tool from the treatment group and starts using it anyway, your groups are contaminated.

**External validity** asks: does this finding hold outside the lab? A sorting algorithm benchmarked on random integers may behave completely differently on nearly-sorted real-world data. A usability study with 20 CS undergraduates may not predict the behaviour of 60-year-old doctors using your medical interface. The 2040 researcher must be explicit about the population, setting, and temporal scope to which results are claimed to generalise.

**Required Reading:**
- Wulfgar & Chen (2039), Chapter 4: "The Architecture of Evidence."
- Wohlin, C. et al. (2012, updated 2039). *Experimentation in Software Engineering*. Springer. Chapters 4–6.
- Montgomery, D. C. (2037). *Design and Analysis of Experiments*, 10th ed. Wiley. Chapter 1.

**Discussion Questions:**
1. Design an experiment to compare two code review tools. Identify at least three threats to internal validity and explain how you would mitigate each.
2. You benchmark a new database engine and find it's 40% faster than PostgreSQL. Your colleague says, "But you ran it on your laptop." Is this an internal or external validity problem, or both?
3. When is a quasi-experiment (no random assignment) acceptable in computing research? Give a concrete example and justify it.

---

## Lecture 5: Measurement — The Runes You Choose Determine What You Read

*"When you can measure what you are speaking about, and express it in numbers, you know something about it."* — Lord Kelvin, 1883

A measurement is a mapping from an empirical reality to a formal symbol system. The choice of measurement fundamentally constrains what can be known. Measure "lines of code" as a proxy for programmer productivity and you will discover — to nobody's genuine surprise — that the most productive programmers write the longest files. This is not a finding about programmers; it is a finding about your measurement.

**Scales of measurement.** Stevens (1946) classified four scale types, and every computing researcher should know them. *Nominal:* categories with no ordering (programming language, operating system, bug type). *Ordinal:* ordered categories where intervals are not meaningful (severity: low/medium/high, Likert scales: strongly disagree to strongly agree). *Interval:* equal intervals but no true zero (temperature in Celsius, dates). *Ratio:* equal intervals with a true zero (execution time in seconds, memory in bytes, defect count). The scale determines permissible statistics — means on Likert data are technically invalid (though widely used), while means on ratio data are perfectly interpretable.

**Construct validity** asks whether your measure actually captures the concept you intend. If you measure "code quality" by counting static analysis warnings, you are measuring warning count, not quality. Quality is a construct — a theoretical entity not directly observable. Validating a construct requires showing that it converges with related measures (developers rate warning-heavy code as lower quality), discriminates from unrelated measures (warning count doesn't correlate with developer IQ), and predicts relevant outcomes (code with more warnings actually has more post-release defects). This is the multi-trait multi-method matrix approach of Campbell and Fiske (1959), still foundational in 2040.

**Reliability** asks whether your measurement is consistent. *Test-retest reliability:* measure the same thing twice — do you get the same result? *Inter-rater reliability:* do two human raters coding the same bug reports agree on severity? (Use Cohen's κ or Krippendorff's α, not simple percent agreement — 90% agreement can mean nothing if the base rate is 95%.) *Internal consistency:* do items on a survey that are supposed to measure the same construct correlate? (Cronbach's α ≥ 0.70 is the conventional threshold, though better alternatives like McDonald's ω exist.)

**Measurement in the age of AI.** By 2040, many computing measurements come from AI systems: code quality scores from LLM-based reviewers, "safety" ratings from automated red-teaming, "fairness" metrics from bias detection tools. Each of these is a measurement instrument, and each has construct validity problems more severe than traditional metrics. An LLM that rates code quality may simply reproduce the biases of its training data — penalising functional programming styles it saw less of, or rewarding verbose comments because open-source projects with more comments tended to be better-maintained. The calibration and validation of AI-based measurement is one of the pressing methodological challenges of our era.

**Required Reading:**
- Wulfgar & Chen (2039), Chapter 5: "The Measure and the Thing."
- Fenton, N. & Bieman, J. (2038). *Software Metrics: A Rigorous and Practical Approach*, 4th ed. CRC Press. Chapters 1–3.
- Jacobs, A. Z. & Wallach, H. (2021). "Measurement and Fairness." *Proceedings of FAccT '21*, 375–385.

**Discussion Questions:**
1. You inherit a dataset where "developer productivity" is measured as commits per day. What construct validity threats does this present? Design a better measurement strategy with at least three indicators.
2. Compute Cohen's κ for two raters classifying 100 bug reports as "critical" or "non-critical." Rater A: 20 critical, 80 non-critical. Rater B: 25 critical, 75 non-critical. They agree on 85. What is κ, and why is it much lower than 85%?
3. How would you validate the construct validity of an LLM-based "code review helpfulness" score? Design a multi-trait multi-method study.

---

## Lecture 6: Statistical Inference — Drawing the Lots Without Fooling Yourself

*"The plural of anecdote is not data."* — Attributed to Roger Brinner (and many others)

Statistical inference is the formal process of drawing conclusions from data in the presence of uncertainty. In computing research, we use statistics to decide whether an observed difference between two algorithms, interfaces, or systems is real or merely noise. This lecture assumes basic probability and statistics (distributions, expectation, variance) and focuses on the logic of inference as applied in computing.

**The null hypothesis significance testing (NHST) framework** has been the dominant paradigm, and you must understand it — even though by 2040, computing research has largely moved beyond naive p-value rituals. The logic: assume the null hypothesis (e.g., "both algorithms have the same mean runtime"), compute the probability of observing data at least as extreme as what you saw, and if that probability (p) is below a threshold (traditionally 0.05), reject the null. The American Statistical Association's 2016 statement (updated 2036) on p-values clarified what they are not: a p-value is not the probability that the null is true, not the probability that your result is a fluke, and not a measure of effect size. A p-value of 0.049 and a p-value of 0.051 are not meaningfully different — yet how many papers hinge on this distinction?

**Effect sizes and confidence intervals** address the limitations of NHST. Cohen's d (standardised mean difference), η² (proportion of variance explained), and odds ratios tell you *how much* difference there is, not just *whether* there is one. A 95% confidence interval tells you the range of plausible values for the true effect. In computing, effect sizes matter enormously: an algorithm that is "significantly faster" (p < 0.001) but only by 0.3% on average is not practically significant unless you're Google and saving 0.3% of compute is worth millions. Report effect sizes with confidence intervals in every computing experiment — this is the 2040 standard required by top venues.

**Bayesian approaches** have gained ground in computing research, particularly in performance analysis, A/B testing, and machine learning evaluation. Rather than computing p(data | null hypothesis), Bayesian inference computes p(hypothesis | data) using Bayes' theorem: prior belief × likelihood = posterior belief. A Bayesian analysis of algorithm performance yields a posterior distribution over the true difference in means, from which you can directly state "there is a 94% probability that Algorithm A is faster than Algorithm B by at least 5%." This is closer to what researchers actually want to say.

**Multiple comparisons and the garden of forking paths.** If you test 20 different metrics on your new system and report only the 3 that reached p < 0.05, you have committed p-hacking — the family-wise error rate across 20 tests is not 0.05 but approximately 1 − (0.95)^20 ≈ 0.64. Corrections exist (Bonferroni, Benjamini-Hochberg FDR, Holm-Bonferroni), but the deeper solution is pre-registration: publicly committing to your analysis plan before seeing the data. By 2040, ACM and IEEE venues increasingly require pre-registration for empirical papers, following the model pioneered by clinical trials and adopted by experimental economics.

**Required Reading:**
- Wulfgar & Chen (2039), Chapter 6: "The Numbers and the Noise."
- Wasserstein, R. L. & Lazar, N. A. (2016, updated 2036). "The ASA Statement on p-Values: Context, Process, and Purpose." *The American Statistician*, 70(2), 129–133.
- McElreath, R. (2038). *Statistical Rethinking: A Bayesian Course with Examples in R and Stan*, 3rd ed. CRC Press. Chapters 1–2.
- Gelman, A. & Loken, E. (2014). "The Statistical Crisis in Science." *American Scientist*, 102(6), 460–465.

**Discussion Questions:**
1. You run an experiment comparing two sorting algorithms and get p = 0.04. Your colleague says, "So there's a 96% chance the difference is real." Why is this wrong? Reformulate the finding correctly.
2. A paper reports 40 hypothesis tests and flags 6 as significant at p < 0.05 without any correction. Using the rough formula, how many of those 6 would you expect to be false positives if all 40 nulls were true? What should the authors have done?
3. Pre-register an experiment to evaluate whether a new IDE feature improves code quality. What analyses do you commit to before seeing data? What do you do if the data reveals an interesting pattern that wasn't in your pre-registration?

---

## Lecture 7: Qualitative Methods — The Sagas of Human Experience

*"Not everything that counts can be counted, and not everything that can be counted counts."* — William Bruce Cameron (often misattributed to Einstein)

Quantitative methods answer "how much?"; qualitative methods answer "why?" and "how?" When your research question involves human experience — how developers understand code, why users trust or mistrust AI systems, what it feels like to be surveilled by workplace monitoring software — numbers alone are insufficient. You need to gather and analyse rich, contextual, narrative data.

**The qualitative research landscape.** Several traditions are relevant to computing research. *Grounded theory* (Glaser & Strauss, 1967; Charmaz, 2014) builds theory inductively from data through iterative coding — you do not start with a hypothesis; you let the theory emerge from systematic comparison. *Phenomenology* seeks the essence of lived experience — what is it like to debug a distributed system? *Ethnography* immerses the researcher in a community — spending months observing an open-source project's communication channels, rituals, and power structures. *Case study research* (Yin, 2018; Runeson & Höst, 2009) investigates a phenomenon in its real-world context, particularly when the boundaries between phenomenon and context are blurred — exactly the situation when studying a software team's adoption of a new practice.

**Data collection methods** in qualitative computing research include semi-structured interviews (prepare a guide but follow interesting tangents), think-aloud protocols (have a developer verbalise their thought process while coding), diary studies (participants log their experiences over weeks), and artefact analysis (studying commit messages, code review comments, Slack conversations). Each method has specific rigour requirements. Interviews require careful question design to avoid leading questions. Think-aloud protocols require training participants so they don't fall silent. Diary studies require regular prompts to combat attrition.

**Analysis: thematic analysis and grounded coding.** Thematic analysis (Braun & Clarke, 2006, updated 2037) is the most accessible and widely used qualitative analysis method in computing research. Its six phases: (1) familiarisation — read and re-read transcripts, noting initial impressions; (2) generating initial codes — label segments of text that seem meaningful; (3) searching for themes — cluster codes into candidate themes; (4) reviewing themes — check that themes coherently capture the coded data and tell a story; (5) defining and naming themes — write a concise, vivid description of each theme; (6) producing the report — weave themes into a narrative supported by vivid quotes. The 2040 toolkit includes AI-assisted coding tools that can suggest initial codes, but the researcher's interpretive judgement remains irreplaceable — an LLM can label a segment "frustration," but only a human who has debugged a race condition at 3 a.m. truly understands the texture of that frustration.

**Rigour in qualitative research.** Where quantitative research has validity and reliability, qualitative research has trustworthiness criteria (Lincoln & Guba, 1985): *credibility* (do participants recognise your findings as true to their experience? — use member checking), *transferability* (have you provided enough thick description that readers can judge applicability to their context?), *dependability* (is your process documented and auditable?), and *confirmability* (have you bracketed your own biases and shown how conclusions flow from data, not from your preconceptions?). A sufficiently rigorous qualitative study in computing research should make its coding scheme, theme development process, and raw data excerpts available for inspection — ideally in a supplementary appendix or a dedicated data repository.

**Required Reading:**
- Wulfgar & Chen (2039), Chapter 7: "The Human in the Machine."
- Braun, V. & Clarke, V. (2037). *Thematic Analysis: A Practical Guide*, 2nd ed. SAGE. Chapters 1–4.
- Hoda, R. (2022). "Socio-Technical Grounded Theory for Software Engineering." *IEEE Transactions on Software Engineering*, 48(10), 3850–3872.
- Seaman, C. B. (1999, updated 2039). "Qualitative Methods in Empirical Studies of Software Engineering." *IEEE TSE*, 25(4), 557–572.

**Discussion Questions:**
1. You want to understand how developers make decisions about using AI code completions. Would interviews, think-aloud protocol, or diary study be most appropriate? Justify your choice and identify its limitations.
2. A reviewer criticises your qualitative study as "not generalisable" because you only interviewed 12 developers. How do you respond using the concept of transferability rather than statistical generalisability?
3. Code the following excerpt from a developer interview using open coding: "I know Copilot is supposed to help, but sometimes it suggests something so confidently wrong that I waste more time checking it than I would have just writing the code myself. It's like having a junior dev who's really fast but also really confidently incorrect."

---

## Lecture 8: Writing the Paper — Forging the Sword of Persuasion

*"Writing is easy. All you have to do is cross out the wrong words."* — Mark Twain

A research finding that stays in your lab notebook does not exist in the scholarly record. Writing is not an afterthought to research — it *is* the final phase of research, the act by which raw results become knowledge. This lecture teaches the craft of the computing research paper as it is practiced in 2040.

**The IMRaD architecture** (Introduction, Methods, Results, and Discussion) has dominated scientific writing since the mid-20th century, but computing papers have evolved their own conventions. A modern systems paper structure: *Abstract* (200 words that sell the paper), *Introduction* (1 page: what problem, why it matters, what you did, what you found, what it means), *Related Work* (position yourself in the scholarly conversation — not a bibliography dump), *System Design / Method* (the hardest section to write well: enough detail to reproduce, not so much that readers drown), *Evaluation / Results* (the evidence: graphs, tables, statistical tests), *Discussion* (what the results mean, limitations, threats to validity), *Conclusion* (1–2 paragraphs: takeaway, future work). Each section has its own rhetoric and pitfalls.

**The Introduction is the most-read and most-important section.** The canonical formula: Paragraph 1 — the problem and why it matters (hook the reader). Paragraph 2 — what others have done and why it's insufficient (create the gap). Paragraph 3 — your approach at a high level (fill the gap). Paragraph 4 — your main results (the punchline). Paragraph 5 — contributions listed explicitly, usually as bullet points ("This paper makes the following contributions:"). Paragraph 6 — a reading roadmap ("The remainder of this paper is organised as follows..."). Write the Introduction last — you cannot introduce what you haven't yet fully understood.

**Writing style principles for 2040.** (1) *Active voice is permitted* — "We ran the benchmark" is clearer than "The benchmark was run." (2) *Define before use* — introduce every technical term before deploying it. (3) *One idea per paragraph* — if you find yourself writing "Additionally..." or "Furthermore..." mid-paragraph, you're merging two ideas into one. (4) *Figures tell the story* — a reader should be able to grasp your main results from figures and captions alone. Captions should describe what the reader should notice, not just label axes. (5) *Edit ruthlessly* — your first draft is for getting ideas down; your third draft is for making them precise. Remove hedge words ("seems to," "may," "possibly," "appears") unless they convey genuine uncertainty. Remove throat-clearing sentences ("In recent years, there has been growing interest in..."). Start with the subject and verb.

**LaTeX and modern tooling.** By 2040, LaTeX remains the standard for computing venues, but with modern enhancements. The `acmart` class handles ACM formatting automatically. Reference management has moved from BibTeX to Biber + `biblatex`. Collaborative writing happens in real-time via Overleaf Pro or Git-based workflows (write in Markdown, render via Pandoc, version-control everything). AI writing assistants can suggest rephrasings, check for common errors, and even generate initial Related Work sections from a topic description — but the researcher is responsible for every sentence. An LLM cannot know whether the paper you're citing actually says what the LLM claims it says. Verify every AI-generated citation against the original paper.

**The cover letter**, for venues that still use them (many in 2040 do not, having moved to fully anonymised double-blind review with structured review forms), is a brief argument for why your paper belongs in this venue and who might find it useful. Never summarise your paper — the reviewers will read it. Instead, say what's new and why it fits.

**Required Reading:**
- Wulfgar & Chen (2039), Chapter 8: "Forging the Sword."
- Shewchuk, J. R. (2000). "Three Sins of Authors in Computer Science and Math." Available online. (Still relevant in 2040.)
- Vardi, M. Y. (2020). "How to Write a Paper for a Scientific Journal." *Communications of the ACM*. (Read alongside the 2037 update.)
- Derek Dreyer's "How to Write a PLDI Paper" (the genre-specific advice, though tailored to PLDI, applies broadly).

**Discussion Questions:**
1. Find a published computing paper from a top venue (2020–2040). Analyse its Introduction using the 6-paragraph formula. How closely does it match? Where does it deviate and why?
2. Rewrite the following sentence in active voice with precise terminology: "It was determined by the analysis that there was an observable improvement in the response time metric following the deployment of the caching layer."
3. Should an AI language model be listed as a co-author on a research paper? Consider the ICMJE authorship criteria: (1) substantial contributions to conception or design, (2) drafting or revising critically, (3) final approval, (4) accountability for all aspects. Can an LLM satisfy all four?

---

## Lecture 9: Peer Review and Publication — The Thing of Scholars

*"The review process is not a trial. It is a conversation among scholars about what counts as knowledge in our community."* — Kathleen McKeown, 2025

Peer review is the gatekeeping mechanism of science: a distributed, largely volunteer process by which experts evaluate the validity, significance, and originality of each other's work before it enters the permanent scholarly record. It is simultaneously the worst system, except for all the others that have been tried. This lecture explains how peer review works in 2040, how to be an effective reviewer, and how to receive reviews — particularly harsh ones — without despairing.

**The 2040 review process.** Most computing venues use double-blind review: authors and reviewers are anonymous to each other. Some venues have experimented with triple-blind (editors also blinded), open review (identities known, reviews public), and post-publication review (publish first, review after), but double-blind remains the default. A typical paper receives 3–4 reviews. Each review includes: a summary (shows you understood the paper), a list of major concerns (fatal flaws, missing related work, insufficient evaluation), a list of minor concerns (typos, unclear figures, missing citations), and an overall recommendation (accept/weak accept/weak reject/reject). By 2040, many venues supplement free-text reviews with structured review forms that require raters to score specific dimensions (novelty, soundness, clarity, reproducibility) on defined scales — this improves inter-reviewer reliability and reduces the influence of charismatic but shallow writing.

**Writing a good review.** A good review is specific, constructive, and evidence-based. Instead of "This paper is poorly written," write "Section 3.2 introduces the Qux algorithm without defining its input constraints, making it impossible to assess correctness. The variable naming in Algorithm 1 (lines 12–17) uses single-letter identifiers that obscure the intended data flow." Instead of "The evaluation is weak," write "The evaluation compares against only two baselines (both from 2037) while omitting Chen et al. (2039) and Park & Müller (2039) which address the same problem with different approaches. The claimed speedup of 3.2× is based on 5 runs with no confidence intervals reported — this is insufficient to support the claim." A review should take 2–4 hours of focused work. If you cannot invest that time, decline the review.

**Receiving reviews.** Every researcher gets harsh reviews — the key is to separate the useful criticism from the noise. Read reviews once, then put them aside for 24 hours. Your first reaction to a rejection will be anger; your second reaction may be defensive dismissal; your third reaction, if you're honest, will often be "okay, they have a point about X." Address every specific criticism in your revision, and document your changes in a response letter that maps reviewer comments to your revisions. Even if you disagree with a reviewer, explain why respectfully and with evidence. Never argue with a reviewer's taste — if they say the paper is "boring," arguing that it's not won't help. Make it less boring.

**Publication ethics and the replication crisis in computing.** The replication crisis that rocked psychology in the 2010s and economics in the 2020s has come for computing. Key findings about software engineering practices, developer productivity, and even algorithm performance have failed to replicate. Contributing factors include: p-hacking and HARKing (hypothesising after results are known), publication bias towards positive results, small sample sizes, and insufficient methodological detail in papers. The 2040 response has been multi-pronged: pre-registration, registered reports (peer review of the study design before data collection), reproducibility badges (ACM's "Artifacts Available," "Artifacts Evaluated," "Results Reproduced"), and increased acceptance of negative results and replication studies at major venues. The *Journal of Negative Results in Software Engineering* (established 2033) specifically publishes well-conducted studies that found no effect — crucial for combating the file drawer problem.

**Required Reading:**
- Wulfgar & Chen (2039), Chapter 9: "The Thing of Scholars."
- Smith, R. (2006). "Peer Review: A Flawed Process at the Heart of Science and Journals." *Journal of the Royal Society of Medicine*, 99(4), 178–182. (Still relevant.)
- ACM (2038). *Artifact Review and Badging: Version 2.0*. Available at acm.org/publications/policies/artifact-review.
- Peng, R. D. (2011). "Reproducible Research in Computational Science." *Science*, 334(6060), 1226–1227.

**Discussion Questions:**
1. You receive a review that says "This paper adds nothing new." How do you determine whether this is a valid criticism (the paper truly isn't novel) or a lazy review (the reviewer didn't understand the contribution)? What evidence would you gather?
2. A paper you're reviewing makes a claim based on a study with 8 participants (4 per condition). Is this always a fatal flaw? Under what circumstances might 8 participants be sufficient? Under what circumstances is it clearly insufficient?
3. Find a paper with an ACM reproducibility badge. What evidence of reproducibility does it provide? Could you actually reproduce it with the provided artefacts? What's missing?

---

## Lecture 10: Research Ethics — The Web of Honor That Binds the Community

*"The first principle of ethical research is that the welfare of the research subject takes precedence over the interests of the researcher."* — Nuremberg Code, 1947 (adapted)

Computing research has ethical dimensions that are often invisible until a crisis reveals them. The Facebook emotional contagion study (2014) manipulated nearly 700,000 users' news feeds without consent. The Stanford Prison Experiment of the AI era — Microsoft's Tay chatbot (2016) — was turned by users into a racist hate-speech machine within hours of deployment. The Cambridge Analytica scandal (2018) showed how innocuous-seeming data collection could be weaponised for political manipulation. By 2040, computing researchers operate in an environment where IRB (Institutional Review Board) approval is required for any study involving human subjects, where data collection must comply with GDPR, CCPA, and the 2034 Global AI Research Ethics Framework, and where the downstream consequences of published research can include real-world harm.

**Human subjects research.** Any study that collects data from or about identifiable humans requires ethical review. This includes surveys, interviews, usability studies, analysis of GitHub commit histories (developers are human subjects too), and A/B tests on deployed systems. The core principles, inherited from the Belmont Report (1979): *respect for persons* (informed consent, protection of vulnerable populations), *beneficence* (maximise benefits, minimise harms), and *justice* (fair distribution of research burdens and benefits — don't only study undergraduates when your system is intended for the elderly). Informed consent means more than a checkbox: participants must understand what data is collected, how it will be used, who will access it, and that they can withdraw at any time without penalty.

**Dual use and foreseeable harm.** Some computing research can be used for both beneficial and harmful purposes. Face recognition research can help find missing children or enable mass surveillance. Vulnerability discovery research can help defenders patch systems or help attackers exploit them. Generative AI research can create educational content or mass-produce disinformation. The 2040 researcher's obligation is not to avoid all dual-use research — that would rule out most of computing — but to conduct a genuine dual-use assessment, to implement harm-reduction measures where possible, and to be transparent about risks. Many venues now require a "Broader Impact" or "Ethical Considerations" section in every paper, following the NeurIPS 2020 model. This is not boilerplate — a paper that says "Our work has no negative societal impact" when it clearly enables mass surveillance will be desk-rejected.

**Data ethics and privacy.** Research datasets that were public in 2030 may be privacy-violating by 2040 standards. The EU's GDPR established the principle of data minimisation: collect only what you need, keep it only as long as necessary. The 2034 Global AI Research Ethics Framework extends this: if a model trained on your dataset can be used to infer sensitive attributes (sexual orientation, political affiliation, health status) about individuals in the dataset, the dataset is effectively sensitive regardless of whether those attributes were explicitly collected. Differential privacy (Dwork et al., 2006) provides mathematical guarantees against such inference, and by 2040, it is expected — not optional — in datasets containing individual-level information.

**Algorithmic fairness in research.** Computing research does not exist in a social vacuum. If your evaluation dataset contains 95% male faces, your face recognition system will have higher error rates on women — this is not a neutral "technical" result; it is a fairness harm. Fairness-aware research methodology requires: (1) documenting the demographic composition of datasets, (2) disaggregating evaluation results by relevant subgroups, (3) using fairness metrics (demographic parity, equalised odds, equal opportunity) where appropriate, (4) acknowledging the limitations of any fairness metric — no single metric captures all dimensions of fairness, and optimising for one often trades off against another (the impossibility results of Kleinberg, Mullainathan, and Raghavan, 2017).

**Required Reading:**
- Wulfgar & Chen (2039), Chapter 10: "Ethics as Architecture."
- ACM (2038). *ACM Code of Ethics and Professional Conduct*. acm.org/code-of-ethics.
- Dwork, C. & Roth, A. (2014). "The Algorithmic Foundations of Differential Privacy." *Foundations and Trends in Theoretical Computer Science*, 9(3–4), 211–407. (Read the introduction.)
- Selbst, A. D. et al. (2019). "Fairness and Abstraction in Sociotechnical Systems." *Proceedings of FAT* '19, 59–68.

**Discussion Questions:**
1. You scrape 100,000 public GitHub repositories to study coding patterns. The data includes commit timestamps, author email addresses, and code content. What ethical issues does this raise? Does "it was public" constitute consent?
2. Design an informed consent form for a study that records developers' screens and eye movements while they debug. What must you disclose? What can you not hide even if you want to?
3. Your research improves the efficiency of password cracking by three orders of magnitude. Your paper has obvious defensive applications (testing password strength). It also has obvious offensive applications (actual cracking). What do you put in the Broader Impact section? Do you publish the code? Do you publish at all?

---

## Lecture 11: AI-Assisted Research — The New Tools of the Smithy

*"We shape our tools, and thereafter our tools shape us."* — John Culkin, 1967 (paraphrasing McLuhan)

The research landscape of 2040 is fundamentally shaped by AI tools. A researcher who refuses to use AI assistance is like a carpenter who refuses to use power tools — they may produce beautiful work, but they will do so slowly and at a competitive disadvantage. A researcher who uses AI uncritically is like a carpenter who lets a power saw guide their hand — they will produce work quickly but possibly of dangerously poor quality. The skilled 2040 researcher uses AI as an augmentation, not a replacement, for judgement.

**AI for literature discovery and synthesis.** Tools like Semantic Scholar, Elicit, Consensus, and ResearchRabbit have transformed literature review. You can now ask "What is the current evidence on the effectiveness of property-based testing compared to example-based testing?" and receive a synthesis of the top 20 relevant papers with extracted findings, methods, and effect sizes. But these tools have limitations: they are biased toward English-language and well-cited papers, they may miss grey literature entirely, and they can hallucinate findings when evidence is thin. The researcher must verify key claims by reading the original papers — AI synthesis is a starting point, not an endpoint.

**AI for code and data analysis.** LLM-based code assistants can generate analysis scripts from natural language descriptions: "Run a mixed-effects model with participant as a random intercept on this CSV, plot the fixed effects with 95% CIs, and report the marginal R²." This dramatically reduces the barrier between research idea and analysis. However, the researcher must understand what the AI is doing and why. If you cannot explain your statistical model to a colleague without the AI's help, you should not be running it. AI can implement bootstraps, but it cannot tell you that bootstrapping is inappropriate for your small-n repeated-measures design. That judgement is yours.

**AI for writing.** By 2040, most researchers use AI writing assistants for drafting, editing, and formatting. AI can suggest clearer phrasings, check grammar and spelling, format citations, and even restructure sections for better flow. It cannot write a paper from scratch — the *ideas*, the *argument*, the *evidence* must come from you. AI-generated text often has a characteristic flavour: hedgy, overly general, lacking in specific claims. It will tell you "Machine learning has revolutionised many fields" instead of "ResNet-152 reduced ImageNet top-5 error from 15.3% to 3.57% in 2015, demonstrating for the first time that deeper networks with skip connections could outperform shallower ones." Good writing is specific; AI writing, left unchecked, is generic. Edit AI-generated text with a knife in your hand.

**The researcher's ethical obligations with AI.** Three rules: (1) **Disclose.** If AI tools substantially contributed to your research — generating hypotheses, conducting analyses, writing sections — say so in an "AI Assistance" statement. (2) **Verify.** AI can hallucinate citations, invent data, and fabricate methodology. Every AI-generated claim must be checked. (3) **Own.** The researcher, not the AI, is accountable for everything in the paper. "The AI wrote it" is not a valid defence against misconduct. If you cannot stand behind every sentence, delete it.

**Required Reading:**
- Wulfgar & Chen (2039), Chapter 11: "The Augmented Researcher."
- ACM (2039). *Policy on AI-Assisted Authorship in ACM Publications*. acm.org/publications/policies/ai-authorship.
- Liang, R., Müller, K., & Ogunleye, T. (2038), Chapter 4: "AI as Collaborator or Tool."
- Birhane, A. et al. (2023). "The Values Encoded in Machine Learning Research." *Proceedings of FAccT '23*.

**Discussion Questions:**
1. An LLM suggests a novel hypothesis for your research area that you had not considered. You test it and it turns out to be correct. Who gets credit for the idea — you, the LLM, or both? How would you write the acknowledgements?
2. You ask an AI tool to find all papers citing a particular study. It returns 47 results, but on checking 5 of them, you find 2 don't actually exist (hallucinated DOIs for real-sounding titles). How does this affect your trust in the other 42? What verification protocol do you adopt?
3. Draft an "AI Assistance" statement for a paper where you used AI for: (a) initial literature screening, (b) suggesting alternative statistical tests, (c) editing for clarity. Be specific about what the AI did and did not do.

---

## Lecture 12: The Future of Computing Research — The Horizon We Sail Toward

*"The best way to predict the future is to invent it."* — Alan Kay, 1971

This final lecture steps back from methodology to consider the trajectory of computing research itself. What will — and should — our field look like in the decades after 2040? The methods taught in this course are not timeless; they evolved from particular historical conditions and will continue to evolve. The young researcher who understands where the river is flowing can position themselves to ride it, rather than being swept aside.

**The automation of research.** By 2040, we can already see the emergence of "AI scientists" — systems that autonomously generate hypotheses, design experiments, execute them on cloud infrastructure, analyse results, and write up findings. The *Automated Statistician* (2015) could discover patterns in tabular data; the *AI Scientist* (2028) could design and run simple ML experiments; by 2040, frontier systems can conduct literature reviews, identify gaps, and run multi-week experimental campaigns with minimal human intervention. This raises profound questions: If an AI system discovers a novel algorithm, who is the author? If AIs produce papers faster than humans can review them, what happens to peer review? If AI-generated research becomes indistinguishable from human-generated research, how do we maintain quality? The 2040 consensus, articulated in the ICML 2039 panel "The Human in the Loop," is that AI should accelerate and augment human research, not replace it — but maintaining that boundary will require active institutional effort, not passive hope.

**Open science and the end of the paywall.** The open access movement that began in the 1990s achieved a decisive victory in the 2030s: by 2040, essentially all publicly funded computing research is freely available, either through institutional repositories, pre-print servers (arXiv, Computing Research Repository), or open-access venues supported by article processing charges paid by funders rather than authors. Plan S, the 2018 European initiative requiring grant-funded research to be published open access, was extended globally by the 2032 UNESCO Open Science Recommendation. Yet "open access" is not "open science." True open science requires sharing data, code, and experimental protocols in reusable, documented forms — the FAIR principles (Findable, Accessible, Interoperable, Reusable). Many papers in 2040 still fail at this. The next frontier is *executable papers*: publications where figures, tables, and statistical results are generated live from the underlying data and code, enabling readers to modify parameters and explore the analysis space directly.

**Interdisciplinarity as necessity.** The most pressing computing research problems of the 21st century — climate modelling, pandemic response, AI safety, misinformation, algorithmic fairness, quantum advantage verification — do not respect disciplinary boundaries. The researcher of 2040 must be able to collaborate with domain scientists who do not speak the language of type theory or asymptotic complexity. This requires methodological pluralism: the ability to deploy formal methods, statistical modelling, qualitative inquiry, and design science as the problem demands, not as your comfort zone dictates. It also requires communication skills: explaining your kernel method to a biologist, understanding what the biologist means by "noise" (it's not your noise), and co-designing research that advances both computing and the partner discipline.

**The ethical scientist in a technological age.** Computing research has never been more powerful, and power without wisdom is destruction. The computing researcher of 2040 and beyond is not just a technician but a steward of technological capability. Every paper you publish, every dataset you release, every model you train, every system you deploy enters the world and changes it. The question is not whether your research has impact — all research has impact — but whether you have anticipated, assessed, and mitigated its harms while maximising its benefits. This is the ultimate research method: not a technique but a stance, a way of being in the world that couples technical brilliance with ethical seriousness. The Norse called it *orðstírr* — not just reputation but the enduring worth of one's deeds as judged by the community across time. Build your research legacy so that, when the Norns weave the final thread of your career, the pattern they reveal is one of integrity, rigour, and genuine contribution to human flourishing.

**Required Reading:**
- Wulfgar & Chen (2039), Chapter 12: "Horizons."
- Kitano, H. (2028). "AI Scientist: Grand Challenge for AI." *Nature Machine Intelligence*, 8, 489–493.
- Wilkinson, M. D. et al. (2016, updated 2036). "The FAIR Guiding Principles for Scientific Data Management and Stewardship." *Scientific Data*, 3, 160018.
- Nissenbaum, H. (2020). *Privacy in Context: Technology, Policy, and the Integrity of Social Life*. Stanford University Press. (Read the conclusion.)

**Discussion Questions:**
1. If an AI system autonomously discovers and proves a significant new theorem, should it be listed as an author on the paper? If not, should it be acknowledged? How? What does your answer imply about the nature of authorship?
2. Your research improves reinforcement learning to the point where it can beat humans at any finite, perfect-information game. A defence contractor adapts your open-source code for autonomous drone targeting. You published openly. Are you responsible? What could you have done differently?
3. Imagine it is 2060. Your grand-student is writing a history of computing research in the 2040s. What do you hope they say about our generation of researchers? What would you need to do differently, starting now, to make that hope realistic?

---

## Final Examination Preparation

The final examination for CS405 consists of a **Research Proposal** (7,500–10,000 words, including references) that demonstrates mastery of all phases of the research lifecycle. Your proposal must include:

1. **Research Question** — A sharply formulated research question using the PICOC framework, justified by a systematic mini-review of relevant literature (at least 15 papers from the past 10 years).
2. **Proposed Method** — Detailed description of your experimental or qualitative design, including sampling strategy, instrumentation (survey items, benchmark selection, interview protocol), and analysis plan (statistical tests or qualitative coding approach).
3. **Threats to Validity** — A structured assessment of construct, internal, external, and conclusion validity threats, with specific mitigation strategies for each.
4. **Ethical Considerations** — IRB considerations, data privacy protections, dual-use assessment, and a broader impact statement.
5. **Reproducibility Plan** — How you will ensure your research can be independently reproduced, including data sharing, code release, and documentation standards.
6. **AI Assistance Statement** — Disclosure of any AI tools used in developing the proposal.

### Sample Examination Essay Questions (Choose 4 of 8)

1. Compare and contrast the NHST and Bayesian approaches to statistical inference in computing research. For each, describe a scenario where it is the more appropriate framework and explain why.
2. A company claims their new database is "2x faster than industry standard." Design a comprehensive experimental protocol to evaluate this claim, addressing: experimental units, randomisation, blocking (if any), measurement instruments, statistical analysis plan, and threats to validity.
3. Qualitative methods have been criticised as "unscientific" by some computing researchers. Construct a defence of qualitative methods in computing research, drawing on at least three specific methodological traditions and their contributions to the field.
4. Discuss the ethical obligations of a computing researcher who discovers a vulnerability that affects over one billion devices. Address responsible disclosure, dual-use considerations, and the tension between open science and public safety.
5. How has the open science movement changed computing research in the past two decades? Evaluate both its successes (what problems has it solved?) and its failures (what problems has it created or left unsolved?).
6. Pre-registration of studies is increasingly required by computing venues. Argue for or against mandatory pre-registration in computing research, addressing both the philosophical rationale and the practical consequences for researchers.
7. Analyse the measurement challenges in evaluating "code readability." What is readability as a construct? How might you operationalise it? Design a validation study for your proposed measure using the multi-trait multi-method approach.
8. Imagine you are serving on the programme committee of a top computing venue in 2045. The field has evolved significantly from 2040. What changes to the peer review process would you advocate for, and why?

---

## Course Summary

CS405 has equipped you with the methodological toolkit of the professional computing researcher. You understand how to formulate testable research questions, ground them in the literature, design rigorous experiments or qualitative studies, analyse data with appropriate statistical tools, write clear and persuasive papers, navigate the peer review system, and confront the ethical dimensions of your work. These skills are not just for producing papers — they are for producing *knowledge*, the enduring contribution that distinguishes the scientist from the technician. May your research, like a well-forged blade, be sharp, true, and worthy of the name you carve upon it.

*Gangið ykkur vel, fræðimenn framtíðar. Go well, scholars of the future.*
— Prof. Sigrún Hrafnsdóttir

---

**Course Policies:**
- **Late submissions:** 10% deduction per day, maximum 5 days. After that, the Norns have already woven a failing grade.
- **Academic integrity:** All work must be your own. AI assistance is permitted but must be disclosed per the AI Assistance policy in Lecture 11. Undisclosed AI use is treated as plagiarism.
- **Office hours:** Tuesdays 14:00–16:00 and Thursdays 10:00–12:00, Fenrir Hall 407, or by appointment. Virtual office hours available in the Yggdrasil VR campus.
- **Accommodations:** Students requiring accommodations should contact the University Accessibility Office at least two weeks before any deadline.
