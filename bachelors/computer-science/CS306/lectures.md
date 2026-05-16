# CS306: Human-Computer Interaction
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4
**Semester:** Year 3, Semester 2
**Prerequisites:** CS102 (Web Development & User Interfaces), CS205 (Machine Learning & Data Mining)
**Instructor:** Dr. Álfhildr Lúsbrá, Faculty of Computational Arts & Design

> *"A rune that no one can read is not a rune — it is a scratch on stone. A user interface that no one can use is not an interface — it is a wall. The craft of HCI is the craft of carving runes that speak."* — Álfhildr Lúsbrá, *The Carved Interface* (2037)

---

## Course Description

Human-Computer Interaction (HCI) is the study of how people interact with technology and how to design systems that are usable, accessible, and delightful. In 2040, HCI extends far beyond screen-based interfaces: neural interfaces read brain signals directly, spatial computing overlays digital information on the physical world, and AI agents act as conversational intermediaries. This course covers UX research methods, interaction design principles, accessibility standards, spatial and neural interface design, and the ethical implications of increasingly intimate human-computer relationships.

The Norse metaphor: the rune-carver who shapes the stone so that the message is clear to all who see it. A well-carved runestone communicates across centuries and cultures — the message persists because the carving is precise, the layout is readable, and the meaning is encoded in a form the reader can decode. So too with HCI: the designer carves the interface so that the user's intention flows smoothly into computational action.

---

## Lectures

### ᚠ Lecture 1: The Carved Interface — Foundations of HCI

**Date:** Week 1, Session 1

#### Overview

This lecture establishes the foundations of HCI as a discipline — its history, its core concepts (affordances, signifiers, feedback, conceptual models, the gulf of execution and evaluation), and the three pillars of usability: effectiveness, efficiency, and satisfaction. We trace HCI from the early days of command-line interfaces through the GUI revolution (Xerox Star, Macintosh, Windows), the web era, mobile touch interfaces, and into the 2040 landscape of gesture, voice, neural, and spatial interaction. The Norse framing: the evolution of writing technology from runestones (public, formal, slow) to parchment (portable, refined) to the printing press (mass-produced) to digital text (instant, searchable, augmentable). Each transition changed what was possible. So too with interfaces.

#### Lecture Notes

HCI emerged as a distinct field in the early 1980s, coinciding with the transition from professional computer operators (who tolerated cryptic interfaces as part of their job) to general users (who would not). The founding text, *The Psychology of Human-Computer Interaction* (Card, Moran, Newell, 1983), applied cognitive psychology to predict and explain user behavior at the interface.

**Don Norman's Design Principles.** Norman's *The Design of Everyday Things* (1988, revised 2013) established the vocabulary that still frames HCI education:

- **Affordances:** The relationship between a physical object and a person — what actions are possible. A button affords pushing; a handle affords pulling; a touch interface affords tapping, swiping, pinching. In 2040, virtual affordances in VR/AR are designed using haptic feedback and visual cues (glow, shadow, animation) to convey what is possible.

- **Signifiers:** The perceivable indicator of an affordance. A door handle signifies "pull." A flat plate on a door signifies "push." In software, a blue underlined text signifies "clickable link." Signifiers must be visible, unambiguous, and consistent. A signifier that misleads causes the gulf of execution (user can't figure out what to do).

- **Feedback:** The system must communicate the result of an action. A button click produces a visual press animation, a sound, and changes the interface state. In 2040, feedback is multimodal (visual + audio + haptic) and immediate (<50ms for touch interactions, <200ms for voice).

- **Conceptual Models:** The user's mental model of how the system works. A good design makes the system's conceptual model match the user's mental model. A trash can on the desktop maps to "throwing things away" — the user knows that dragged files end up there and can be restored if needed. A poorly designed system gives the user an incorrect or incomplete conceptual model, leading to errors and frustration.

- **The Gulfs of Execution and Evaluation:** The gulf of execution is the gap between the user's goals and the available actions. The gulf of evaluation is the gap between the system's state and the user's understanding of that state. Good design minimizes both gulfs.

**The Three Usability Metrics (ISO 9241-11).**
1. **Effectiveness:** Can users complete their tasks accurately? Measured by error rate and task completion rate.
2. **Efficiency:** How quickly can users complete tasks? Measured by time-on-task and number of steps.
3. **Satisfaction:** How pleasant is the experience? Measured by self-report (SUS, NPS, UEQ) and biometric signals (facial expression, heart rate variability, skin conductance).

**2040: The Post-Screen Era.** By 2040, touchscreens dominate but are being supplemented by:
- **Voice interfaces (40% of interactions):** Smart speakers, AI assistants, voice-controlled environments. The challenge: voice is serial (you can only say one thing at a time) and leaves no persistent record.
- **Gesture interfaces (15%):** Hand tracking (Leap Motion, Apple Vision Pro, Meta Quest Pro) enables manipulative interaction. The challenge: gorilla arm fatigue (holding arms up for extended periods).
- **Neural interfaces (10%):** Non-invasive EEG headsets for cursor control, typing, and simple commands. Invasive BCIs (Neuralink, Synchron) for people with paralysis. The challenge: noise, calibration, and the ethical boundary of mind-reading.
- **Spatial computing (25%):** AR glasses that overlay digital information on the physical world. The challenge: information density (don't clutter the user's field of view) and social acceptability (glasses must look normal).

#### Required Reading
- Norman, D. (2013). *The Design of Everyday Things*, revised and expanded ed. Basic Books. Chapters 1-2.
- Card, S.K., Moran, T.P., & Newell, A. (1983). *The Psychology of Human-Computer Interaction*. L. Erlbaum. Chapter 1.
- ISO 9241-11 (2018). *Ergonomics of Human-System Interaction — Part 11: Usability*.
- Lúsbrá, Á. (2037). *The Carved Interface*, Chapter 1: "Rune-Carving as Interaction Design." Yggdrasil University Press.

#### Discussion Questions
1. Apply Norman's seven stages of action (goal → plan → specify → perform → perceive → interpret → compare) to the task of ordering a coffee through a mobile app. Where are the gulfs?
2. Voice interfaces have no visual persistence. Design a voice interface for checking train departure times. How do you compensate for the lack of a visual display?
3. A neural interface that reads brain signals could help people with paralysis communicate. At what point does such an interface cross the line from "assistive technology" to "privacy violation"?

---

### ᚢ Lecture 2: UX Research — Listening to the Weave

**Date:** Week 2, Session 1

#### Overview

The foundation of good design is understanding the user. UX research encompasses the methods for discovering what users need, how they behave, and what they value. This lecture covers qualitative methods (interviews, contextual inquiry, diary studies, focus groups), quantitative methods (surveys, analytics, A/B testing, log analysis), and the 2040 integration of AI-assisted UX research (sentiment analysis of user feedback, automated usability testing with AI agents). The Norse metaphor: the *vǫlva's spá* (prophecy) — the seeress who listens to the whispers of the threads to understand the pattern of fate. UX research is the practice of listening to users to understand the pattern of their needs.

#### Lecture Notes

**Qualitative Methods — Understanding the Why.**

*Interviews.* The most direct method: sit down with users and ask them about their experiences, needs, and frustrations. Three types:
- **Structured:** Fixed questions, asked in order. Produces comparable, shallow data.
- **Semi-structured:** A question guide with flexibility to follow interesting threads. The 2040 standard — rich data with some comparability.
- **Unstructured:** Open conversation around a topic. Deepest data, hardest to analyze.

The critical interviewing skill: *active listening* paired with *the five whys* — asking "why" five times to drill past surface answers to root causes. A user says "I can't find the search button." Why? "It's hidden behind a menu." Why is it hidden? "The designer prioritized visual minimalism." Why? The root cause is not the button placement but the design philosophy.

*Contextual Inquiry.* Observe users in their natural environment. This method reveals what users *actually do*, as opposed to what they *say* they do. A classic HCI study: users report "I check my email three times a day" but logs show they check it 30+ times. The gap between reported and actual behavior is wide. Contextual inquiry bridges it.

*Diary Studies.* Users log their interactions with a system over days or weeks. Captures longitudinal patterns — how usage evolves, what triggers frustration, what delights. In 2040, AI agents on the user's device can automatically log interaction patterns (with consent), reducing the burden on the participant while providing richer data.

**Quantitative Methods — Measuring the What.**

*Surveys.* The workhorse of quantitative UX research. Key instruments:
- **SUS (System Usability Scale):** 10-item questionnaire producing a score out of 100. Quick, reliable, and technology-agnostic.
- **UEQ (User Experience Questionnaire):** 26 items measuring six dimensions (attractiveness, perspicuity, efficiency, dependability, stimulation, novelty).
- **NPS (Net Promoter Score):** "How likely are you to recommend this product to a friend?" Controversial in academic UX but widely used in industry.

*Analytics and Log Analysis.* Every interaction with a digital system can be logged. In 2040, the UoY's **Verðandi Analytics** platform captures: click events, navigation paths, time-on-task, error rates, session duration, and feature adoption rates. Analysis identifies: drop-off points (where users abandon tasks), rage clicks (repeated clicking on non-interactive elements), and the "bottleneck pages" where users spend disproportionately long.

*A/B Testing.* Randomly assign users to variant A or variant B, measure the outcome (conversion rate, task completion time, satisfaction). In 2040, AI-driven multivariate testing tests dozens to hundreds of variants simultaneously. The **Huginn Experiment Engine** at UoY manages continuous experiments across all student-facing systems, optimizing for usability and learning outcomes.

**2040: AI-Assisted UX Research.** AI tools augment but do not replace human researchers:
- **Automated sentiment analysis:** User feedback (open-ended survey responses, support tickets, social media mentions) is automatically classified as positive, negative, or neutral, and the topics are extracted via topic modeling.
- **Automated usability testing:** AI agents simulate user behavior, exploring the interface and identifying violations of known usability heuristics. The **RúnarTester** system at UoY achieves 80% agreement with human usability experts on web interfaces.
- **Behavioral analytics:** Machine learning models detect patterns in user behavior that correlate with churn, frustration, or abandonment — hours before any survey would reveal them.

#### Required Reading
- Courage, C. & Baxter, K. (2005). *Understanding Your Users: A Practical Guide to User Research Methods*. Morgan Kaufmann.
- Sauro, J. & Lewis, J.R. (2016). *Quantifying the User Experience*, 2nd ed. Morgan Kaufmann.
- ISO 25010 (2011). *Systems and Software Quality Requirements and Evaluation (SQuaRE)*.
- Norman, D. (2013). *The Design of Everyday Things*, Chapter 6: "Design Thinking."

#### Discussion Questions
1. A user reports "I love this app" but analytics show they only use it once a week for 30 seconds. Which data source do you trust, and why?
2. AI-assisted UX research promises to automate much of the analysis. What aspects of UX research should never be automated? Why?
3. Design a diary study for a new campus navigation app. What would you ask participants to log, and for how long?

---

### ᚦ Lecture 3: Interaction Design — Shaping the Conversation

**Date:** Week 3, Session 1

#### Overview

Interaction design is the craft of designing the dialogue between user and system. This lecture covers the fundamental interaction paradigms (command, menu, direct manipulation, form fill, conversational), interaction styles across modalities (click, touch, gesture, voice, gaze, thought), and the design patterns that make interactions feel natural, predictable, and efficient. The Norse metaphor: the flyting — the formal exchange of insults between Norse warriors that established hierarchy and resolved tension without violence. A good interaction design is like a well-performed flyting: it follows conventions, establishes a rhythm, and reaches a satisfying resolution.

#### Lecture Notes

**Interaction Paradigms.**

1. **Command line (oldest, still alive):** The user types commands. Maximum power, steepest learning curve. By 2040, command-line interfaces persist in developer tools and system administration — but they are increasingly augmented by LLMs that translate natural language into commands.

2. **Menu-driven:** The system presents available options; the user selects. Found in ATMs, set-top boxes, and the early web. Limitations: menus impose the designer's hierarchy on the user's tasks. Nielsen's law: the number of menu levels should be ≤ 3.

3. **Direct manipulation (Shneiderman, 1983):** The user directly manipulates on-screen objects. Key characteristics: continuous representation of the object, physical actions (drag, drop, resize) instead of complex syntax, and immediate feedback. Examples: drawing programs, CAD systems, file managers, the touchscreen interface. By 2040, spatial computing extends direct manipulation to 3D — grab a virtual object with your hand, rotate it, place it in the world.

4. **Conversational (voice/LM-based, 2020+):** The user converses with an AI in natural language. By 2040, this is the dominant paradigm for complex tasks ("Plan a trip to Iceland for my family in June"). The challenge: the computer is an unreliable conversational partner — it may misunderstand, hallucinate, or fail to ask clarifying questions.

5. **Gesture-based (2040 growth):** The user gestures (sweep, pinch, point) to interact. Mature in VR/AR, emerging in smart home and automotive.

**Interaction Design Patterns (Tidwell, 2010, 2040 edition).**

- **Overview + Detail:** Show the big picture and let the user zoom into details. Maps, code editors, image viewers.
- **Progressive Disclosure:** Show only what the user needs now. Reveal more on demand. Settings panels, wizards.
- **Wizard:** Step-by-step guided task completion. Complex configuration (router setup, tax filing).
- **Undo/Redo:** The user's safety net. Every action should be reversible. In 2040, the **Urðr Time Machine** in Hermes applications provides visual timeline-based undo — users scroll back through their interaction history and "undo" any step.
- **Autocomplete/Suggestion:** The system predicts what the user wants and offers suggestions. Search engines, command palettes (Cmd+K in modern IDEs), LLM chat completion.
- **Confirmation Dialogs:** "Are you sure?" — overused in 2020, rare in 2040. The 2040 principle: assume the user's intent unless the action is irreversible (delete account, pay money, erase data).

**Fitts' Law.** The time to acquire a target (click, tap, grab) is a function of the distance to the target and its size: T = a + b · log₂(1 + D/W). Implications: corner and edge positions are "infinite size" (the cursor stops at the edge), so put critical controls (Start menu, Dock) at screen edges. In 2040, Fitts' Law applies to VR/AR interaction: the law extends to 3D with the addition of depth (the target's distance in z increases the effective size).

**Hick's Law.** Decision time increases logarithmically with the number of choices: T = a + b · log₂(n). Keep choices per screen to 3-7 (the "magic number seven, plus or minus two"). This underlies the 2040 design principle of progressive disclosure: show 3 primary choices, offer "more options" for the rest.

#### Required Reading
- Shneiderman, B. et al. (2016). *Designing the User Interface*, 6th ed. Pearson. Chapters 1-3.
- Tidwell, J. (2010). *Designing Interfaces*, 2nd ed. O'Reilly.
- Fitts, P.M. (1954). "The Information Capacity of the Human Motor System in Controlling the Amplitude of Movement." *Journal of Experimental Psychology*, 47(6).
- Lúsbrá, Á. (2037). *The Carved Interface*, Chapter 4: "The Flyting as Interaction Pattern."

#### Discussion Questions
1. Progressive disclosure is a tradeoff between simplicity (fewer visible options) and discoverability (hidden options may never be found). How do 2040 interfaces resolve this tradeoff?
2. Fitts' Law predicts that corner targets are fastest. How does this apply to VR/AR interfaces, which have no fixed "corners"?
3. Conversational AI interfaces violate Hick's Law: there are no explicit choices, just an open text field. Are these interfaces harder or easier to use than menu-driven interfaces? Why?

---

### ᚲ Lecture 4: Accessibility — The Interface for All Beings

**Date:** Week 4, Session 1

#### Overview

Accessible design is not charity — it is good design that benefits everyone. Approximately 15% of the global population (over 1.2 billion people) has some form of disability. This lecture covers the categories of disability (visual, hearing, motor, cognitive, speech), the assistive technologies that bridge the gap (screen readers, switch control, voice control, eye tracking, augmentative and alternative communication — AAC), and the design principles that make interfaces accessible to all (WCAG 3.0 guidelines, universal design, inclusive design, the curb-cut effect). The Norse metaphor: the god Hǫðr — blind, yet one of the Aesir, who participates fully in the life of the gods until the tragedy engineered by Loki. A system designed without Hǫðr in mind fails its duty to the full community of users.

#### Lecture Notes

**The Web Content Accessibility Guidelines (WCAG).** By 2040, WCAG 3.0 (published 2024) is the global standard for digital accessibility. It organizes success criteria under four principles — POUR:
- **Perceivable:** Information and UI components must be presentable to users in ways they can perceive.
- **Operable:** UI components and navigation must be operable by all users.
- **Understandable:** Information and UI operation must be understandable.
- **Robust:** Content must be robust enough to be interpreted reliably by a wide variety of user agents, including assistive technologies.

Key WCAG 3.0 requirements:
- **Contrast ratio:** Minimum 4.5:1 for normal text, 3:1 for large text.
- **Keyboard accessibility:** Everything must be operable via keyboard alone, with visible focus indicators.
- **Screen reader support:** Semantic HTML (headings, landmarks, alt text, ARIA labels).
- **Captions and transcripts:** All audio and video content must have text alternatives.
- **Text spacing:** Line height 1.5×, paragraph spacing 2×, letter spacing 0.12×.

**The Curb-Cut Effect.** The "curb cut" — the ramp from the sidewalk to the street — was designed for wheelchair users but benefits everyone: parents with strollers, delivery workers with dollies, cyclists, travelers with rolling luggage. In HCI, designing for accessibility often benefits all users: captions help users in noisy environments and non-native speakers; high contrast helps users in bright sunlight; keyboard shortcuts help power users. This is the curb-cut effect.

**Assistive Technologies in 2040.**

- **Screen readers (JAWS, NVDA, VoiceOver, TalkBack):** By 2040, AI-enhanced screen readers can describe images, interpret complex data visualizations, and summarize long pages. The **Huginn Screen Reader** developed at UoY provides natural-language descriptions of visual layouts: "A form with fields for name, email, and a submit button. Three navigation links at the top: Courses, Schedule, Profile."

- **Switch control:** For users with limited motor control. A single switch (breath puff, eyebrow raise, finger twitch) cycles through interface elements. This is the most demanding accessibility test: if an interface works with a single switch, it works for everyone.

- **Eye tracking:** By 2040, consumer VR/AR headsets include eye tracking. Users with motor disabilities can control the interface with gaze + dwell (fixate on a target for 500ms to click) or gaze + blink.

- **Brain-computer interfaces (BCI):** For users with severe motor disabilities (ALS, locked-in syndrome). EEG-based BCIs (non-invasive) enable cursor control and typing at 20-40 characters per minute in 2040. The **RúnarBCI** project at UoY aims to reach 60 CPM by 2042.

- **AAC (Augmentative and Alternative Communication):** For non-speaking users. Speech-generating devices and apps. By 2040, AI-powered AAC systems predict the user's intended message from partial input (one tap predicts "I want to go to the cafeteria").

**Universal Design Principles (North Carolina State, 1997, extended for 2040).**
1. **Equitable use:** The design is useful and marketable to people with diverse abilities.
2. **Flexibility in use:** Accommodates a wide range of preferences and abilities.
3. **Simple and intuitive:** Easy to understand regardless of experience, language, or cognitive ability.
4. **Perceptible information:** Communicates necessary information regardless of ambient conditions or sensory abilities.
5. **Tolerance for error:** Minimizes hazards and adverse consequences of accidental actions.
6. **Low physical effort:** Can be used efficiently and comfortably with minimum fatigue.
7. **Size and space for approach and use:** Appropriate size for reach, manipulation, and use regardless of body size, posture, or mobility.
8. **AI explicability (2040 addition):** The interface must communicate what the AI system knows, is doing, and why.

#### Required Reading
- WCAG 3.0 (2024). *Web Content Accessibility Guidelines*. W3C.
- Henry, S.L. (2014). *Just Ask: Integrating Accessibility Throughout Design*. 2nd ed. Lulu.com.
- Norman, D. (2013). *The Design of Everyday Things*, Chapter 7: "Design in the World of Business."
- Connolly, M. et al. (2036). "Accessibility in Spatial Computing." *ACM ASSETS*.

#### Discussion Questions
1. A voice-controlled smart home interface is inherently inaccessible to a deaf user. How would you redesign such an interface to be universally accessible?
2. The curb-cut effect suggests that designing for accessibility benefits all users. Give five examples of accessibility features that are now used by the general population.
3. AI-powered accessibility tools (screen readers that describe images, AAC that predicts text) make tradeoffs between speed and accuracy. At what point does prediction become "putting words in the user's mouth"?

---

### ᚷ Lecture 5: Spatial Computing — The Augmented Realms

**Date:** Week 5, Session 1

#### Overview

Spatial computing — the overlaying of digital information on the physical world — is by 2040 a mature, mass-market technology. This lecture covers the interaction design principles for augmented and virtual reality: spatial affordances, depth cues, manipulation in 3D, navigation in virtual spaces, and the ergonomic challenges (motion sickness, fatigue, social acceptability). The Norse metaphor: the *Urðarbrunnr* (Well of Urðr) — a location that exists simultaneously in the physical world (at the root of Yggdrasil) and in the spiritual world (where the Norns weave). Spatial computing creates such dual-presence: digital objects that exist in our physical space, extending our reality.

#### Lecture Notes

**The Spectrum of Reality-Virtuality (Milgram & Kishino, 1994).**
- **Real environment:** What you see without augmentation.
- **Augmented Reality (AR):** Digital overlay on the real world (smart glasses, phone camera).
- **Augmented Virtuality (AV):** Real objects inserted into a virtual world.
- **Virtual Reality (VR):** Complete immersion in a virtual environment.

By 2040, AR is the dominant paradigm — Apple Vision Pro 4, Meta Quest Pro 3, and the UoY's own **RúnarLens** (developed in partnership with Nordic optics company Horus) are worn by 30% of UoY students during a typical day. VR is used for specialized applications: immersive learning, architectural walkthroughs, and therapeutic scenarios.

**Interaction in 3D.**

*Selection.* How does the user select a virtual object?
- **Ray casting:** Point from the controller or hand toward the object. Most common, but suffers from jitter at long distances.
- **Gaze + confirm:** Look at the object, then perform a confirm action (tap, voice, blink). Low effort but imprecise.
- **Hand proximity:** Reach out and touch the virtual object. Most natural but limited to arm's reach (~1m).

*Manipulation.* Once selected, how does the user manipulate the object?
- **Direct manipulation (proximal):** Grab with hand, move, rotate, scale with the other hand. The most intuitive.
- **Gizmo-based (distal):** Select object, see a 3D manipulation widget (translate/rotate/scale rings). High precision, requires training.
- **Voice + gesture:** "Move the chair... here" (point to location). Combines natural language with spatial pointing.

*Navigation.* How does the user move through the virtual space?
- **Physical walking:** The gold standard — the user's real body movement maps 1:1 to virtual movement. Challenges: limited tracking space, physical obstacles.
- **Teleportation:** Point to a location and instantly appear there. Low motion sickness risk. Most common in VR experiences.
- **Joystick/thumbstick locomotion:** Smooth movement, highest motion sickness risk. Used by experienced VR users.

**The Motion Sickness Problem.** Vection (the perception of self-motion) that conflicts with the vestibular system (which senses no acceleration) causes motion sickness. By 2040, solutions include:
- **Comfort vignettes:** The field of view narrows during artificial movement, reducing vection.
- **Translational gain mismatch:** Reduce the visual speed relative to real leg movement (for walking-in-place interfaces).
- **Galvanic vestibular stimulation (GVS):** Low-current electrical stimulation of the vestibular nerve to create the sensation of acceleration. Experimental in 2040, available in high-end VR systems.

**Spatial Affordances.** In the physical world, affordances are obvious: a chair affords sitting because you've seen chairs before. In spatial computing, affordances must be designed:
- **Glow effect:** An interactable object glows when the user's gaze or hand approaches it.
- **Outline:** Selected objects get a colored outline (cyan in the UoY framework).
- **Physics simulation:** Objects react to gravity, collisions, and forces — the user understands their material properties through behavior.
- **Sound:** A soft chime when an object becomes interactable; a click when selected; a satisfying thud when placed.

**2040: The UoY Spatial Campus.** By 2040, the UoY campus has a full spatial computing layer accessible through RúnarLens: digital wayfinding arrows on the floor ("Turn left for the Computational Arts building"), virtual whiteboards in study rooms (visible to all students wearing lenses), interactive 3D models in the anatomy lab (floating organs students can examine from all angles), and a shared virtual space ("The Longhouse") where students gather for social events, study groups, and the annual course registration festival.

#### Required Reading
- Milgram, P. & Kishino, F. (1994). "A Taxonomy of Mixed Reality Visual Displays." *IEICE Transactions on Information Systems*, E77-D(12).
- Norman, D. (2013). *The Design of Everyday Things*, Chapter 7: "Spatial Design."
- LaViola, J. et al. (2017). *3D User Interfaces: Theory and Practice*, 2nd ed. Addison-Wesley.
- Lúsbrá, Á. (2037). *The Carved Interface*, Chapter 8: "The Dual Presence."

#### Discussion Questions
1. AR interfaces overlay information on the physical world. How do you prevent information overload — the user seeing too many virtual objects and losing track of the physical environment?
2. Why does teleportation cause less motion sickness than smooth locomotion in VR? What does this tell us about the perceptual mechanisms underlying motion sickness?
3. Design a spatial computing interface for the UoY cafeteria — what information would you overlay, and how would the user interact with it while holding a tray of food?

---

### ᚹ Lecture 6: Voice and Conversational Interfaces — The Spoken Word

**Date:** Week 6, Session 1

#### Overview

By 2040, voice is the fastest-growing interaction modality, driven by the maturity of large language models and speech recognition. This lecture covers the design of conversational interfaces: turn-taking, grounding, error recovery, persona design, and the unique challenges of voice-only interaction (no visual persistence, ambient noise, privacy concerns). The Norse metaphor: the *þáttr* — a short narrative told aloud in the longhouse, with the storyteller adjusting the tale based on the audience's reactions. A well-designed voice interface is a digital storyteller: it responds to the user's cues, adapts its pacing, and keeps the conversation flowing.

#### Lecture Notes

**Conversational Design Principles.**

*Turn-Taking.* Humans take turns in conversation with remarkable precision — the average gap between turns is 200ms. Voice interfaces must match this rhythm. A delay longer than 1 second breaks the conversational flow. The 2040 standard: the system responds to simple commands in <300ms, and to complex queries in <2s with an acknowledgement (a subtle chime or "Let me think about that...") during the delay.

*Grounding (Clark & Brennan, 1991).* In conversation, speakers establish common ground — shared understanding that accumulates over the dialogue. A voice interface must ground each contribution. The system should:
- **Acknowledge receipt:** "I heard you say 'set thermostat to 22 degrees'."
- **Confirm understanding:** "So you want the living room temperature at 22°C. Is that correct?"
- **Signal understanding:** "Got it" or "OK" after each user contribution, even during extended narration.

*Error Recovery.* In voice interfaces, errors are inevitable (misrecognition, misunderstanding, ambient noise). The system must recover gracefully:
- **Rejection of low-confidence inputs:** If speech recognition confidence < 80%, ask "Sorry, could you repeat that?" rather than guessing.
- **Clarification:** If the intent is unclear, ask specific questions rather than generic "I don't understand." Example: "Did you want to *search* for courses or *register* for courses?"
- **Undo:** Every voice action must be reversible with "Undo that" or "Go back."

**Persona Design.** A voice interface is perceived as having a personality, whether you design one or not. Key dimensions:
- **Formality:** Formal ("Good afternoon. How may I assist you?") vs. casual ("Hey! What's up?") The 2040 trend: adaptive formality — the interface matches the user's style.
- **Politeness:** Direct ("Set temperature to 22") vs. polite ("Could you please set the temperature to 22 degrees?"). In usability testing at UoY, users rated polite interfaces as more competent and trustworthy.
- **Accent and dialect:** By 2040, the best voice interfaces support multiple accents and dialects natively. The UoY campus voice assistant, **UrðrSpeak**, supports 8 regional British accents plus Icelandic and Norwegian.

**Voice UX Anti-Patterns.**
- **Echo chamber:** The system confirms everything the user says, making the conversation tedious. "I want to set an alarm." → "You want to set an alarm?" → "Yes." → "OK, setting an alarm..." Better: confirm only critical actions.
- **Too many options:** "Would you like to set a one-time alarm, a recurring alarm, an alarm with a specific ringtone, an alarm that...?" → Information overload. Better: progressive disclosure. "What time?" → After time: "Would you like this alarm to repeat?"
- **No visual equivalent:** Voice-only interfaces are hard for users with hearing disabilities and impossible in noisy environments. Always provide a visual fallback.

#### Required Reading
- Clark, H.H. & Brennan, S.E. (1991). "Grounding in Communication." *Perspectives on Socially Shared Cognition*.
- Pearl, C. (2016). *Designing Voice User Interfaces: Principles of Conversational Experiences*. O'Reilly.
- Cohen, M.H. et al. (2004). *Voice User Interface Design*. Addison-Wesley.

#### Discussion Questions
1. Design a voice interface for a banking application. How would you handle the security requirement (authentication) while maintaining conversational flow?
2. The "echo chamber" anti-pattern is common in early voice interfaces. When is confirmation actually necessary? When does it become annoying?
3. In a multi-user environment (family living room), how does a voice interface distinguish commands addressed to it from conversation between people? What if the system makes a mistake?

---

### ᚺ Lecture 7: Neural Interfaces — The Threshold of Thought

**Date:** Week 7, Session 1

#### Overview

Neural interfaces — devices that read (and in some cases write) brain signals — represent the most intimate frontier of HCI. This lecture covers the neuroscience foundations (EEG, fNIRS, ECoG, intracortical arrays), the interaction design principles for BCI (control vs. communication, the Midas touch problem, fatigue and training), the state of the art in 2040 (non-invasive EEG for cursor control, invasive BCI for communication in locked-in patients), and the profound ethical questions: cognitive liberty, mental privacy, and the boundary between human and machine. The Norse metaphor: the *hamingja* — a concept in Norse belief meaning a person's luck, fortune, or guardian spirit, often visualized as a being that shapes the person's fate. A neural interface is a technological hamingja: it reads the user's mind and helps shape their digital fate.

#### Lecture Notes

**The Neuroscience.**

*EEG (Electroencephalography).* Non-invasive electrodes on the scalp measure electrical activity of cortical neurons. Temporal resolution: ~1ms (excellent). Spatial resolution: ~1cm (poor). The signal is noisy (SNR ~ 1-5) and contaminated by muscle artifacts (eye blinks, jaw clench, forehead tension). In 2040, dry electrodes (no gel) and active noise cancellation have made EEG practical for consumer use — the **RúnarBand** headband provides 8-channel EEG at 500Hz for under €500.

Common EEG paradigms for HCI:
- **Motor imagery:** The user imagines moving their left hand or right hand. The sensorimotor rhythms (mu rhythm, 8-12Hz, beta, 18-25Hz) desynchronize on the contralateral hemisphere. This can be classified at ~85% accuracy in 2040.
- **P300 speller:** A 6×6 grid of characters flashes rows and columns randomly. When the target character flashes, the user's brain produces a P300 event-related potential (positive deflection at 300ms). The system identifies the target by detecting which row and column produce the P300. Typing speed: 20-40 characters per minute in 2040.
- **Steady-state visually evoked potentials (SSVEP):** The user looks at a target that flickers at a specific frequency (e.g., 15Hz). The occipital cortex produces a response at that frequency. SSVEP enables rapid selection from a grid of targets, with speeds up to 60 choices per minute.

*Invasive BCIs.* For users with severe motor disabilities, implanted electrodes provide higher signal quality:
- **ECoG (Electrocorticography):** Electrodes placed on the surface of the brain (under the skull but above the dura). SNR ~ 10-20. Requires surgery.
- **Intracortical arrays (Utah array, Neuralink):** Tiny electrodes inserted into the cortex. SNR ~ 100. Highest resolution. Used in clinical trials for cursor control (BrainGate) and speech decoding (Neuralink's PRIME study).

In 2040, the **RúnarBCI** implant (developed in a UoY-Neuralink partnership) provides 2048 channels at 30kHz from a flexible, thread-like electrode array. It enables: cursor control at 60 bits/min, speech decoding at 60 words/min (for attempted speech), and the first experimental "direct thought-to-text" interfaces.

**The Midas Touch Problem.** In Greek myth, everything King Midas touched turned to gold, including food, drink, and his daughter. In BCIs, the Midas Touch problem is: how do we distinguish between the user's intentional commands and their incidental brain activity (thinking about lunch while the cursor is on the "delete" button)? Solutions in 2040:
- **Dual-threshold:** A command requires both a specific brain pattern (e.g., motor imagery) AND a confirmation signal (e.g., a blink or jaw clench).
- **Context-aware buffers:** In the P300 speller, the system does not immediately output characters — it holds a buffer of 3-spell cycles, shows them to the user, and asks for confirmation before sending.
- **Adaptive calibration:** The system learns the user's baseline neural activity and adapts the classification thresholds continuously.

**The Training Wall.** Non-invasive BCIs require user training. Most users need 10-30 sessions (each 30-60 minutes) to achieve reliable control. About 15% of users are "BCI illiterate" — they never achieve above-chance control. The 2040 standard uses adaptive machine learning: the classifier adapts to the user's neural patterns in real-time, reducing training time to 3-5 sessions for most users.

#### Required Reading
- Wolpaw, J.R. & Wolpaw, E.W. (2012). *Brain-Computer Interfaces: Principles and Practice*. Oxford.
- Nijboer, F. et al. (2008). "A P300-Based Brain-Computer Interface for People with Amyotrophic Lateral Sclerosis." *Clinical Neurophysiology*, 119(8).
- Musk, E. (2019). "An Integrated Brain-Machine Interface Platform with Thousands of Channels." *Journal of Medical Internet Research*, 21(10).
- The Nordic Bioethics Council (2036). "Ethical Guidelines for Neural Interfaces."

#### Discussion Questions
1. The Midas Touch problem is about distinguishing intent from incidental thought. Propose a solution that does not require a confirmation signal and works in real-time.
2. Should non-invasive BCIs be regulated as medical devices, or can they be sold as consumer electronics? At what point does "reading your brain for cursor control" become "reading your thoughts"?
3. Consider the ethics of "direct thought-to-text" interfaces. Can a person be forced to incriminate themselves through their BCI output? How does the 5th Amendment (US) or Article 6 of the ECHR apply?

---

### ᚾ Lecture 8: Information Architecture — Organizing the Nine Realms

**Date:** Week 8, Session 1

#### Overview

Information Architecture (IA) is the practice of structuring, organizing, and labeling content to support usability and findability. This lecture covers IA fundamentals: hierarchies, taxonomies, folksonomies, navigation design, search systems, and the 2040 challenge of organizing AI-generated content. The Norse metaphor: Yggdrasil, the world-tree that organizes the cosmos into nine realms. A well-designed information architecture is Yggdrasil — it organizes vast complexity into a navigable structure where every user can find their way.

#### Lecture Notes

**The Eight Principles of Information Architecture (Dan Brown, 2010, updated for 2040).**

1. **Principle of Objects:** Treat content as a living thing with its own lifecycle, behaviors, and attributes. Every piece of content has: an owner, a creation date, an expiry date, a format, an audience, and a privacy level.
2. **Principle of Choices:** Offer meaningful choices. Too few choices frustrate (information starvation). Too many choices overwhelm (paradox of choice). The 2040 guideline: present no more than 7±2 navigation options at any level.
3. **Principle of Disclosure:** Show only enough information to help people understand what more information they'll find if they dig deeper. This is the progressive disclosure principle applied to information organization.
4. **Principle of Exemplars:** Show examples of content categories to help users understand what the category contains. A "Courses" category should show a few sample courses.
5. **Principle of Front Doors:** Assume that at least half of users will enter the site through a page other than the homepage. Every page must confirm the user's location and provide context.
6. **Principle of Multiple Classification:** Offer users several different classification schemes to browse content — by topic, by format, by audience, by date, by popularity.
7. **Principle of Focused Navigation:** Don't mix different types of navigation in the same menu. Course navigation (by department, by level, by semester) should be separate from account navigation (profile, settings, logout).
8. **Principle of Growth:** Assume the content will grow. The navigation must accommodate 10× the current content volume without redesign. This is especially critical in 2040, when AI-generated content expands existing repositories daily.

**Navigation Design Patterns.**

- **Global navigation:** The persistent top-level navigation that appears on every page. The UoY course site has: Courses, Schedule, Degree Planner, Library, Profile.
- **Local navigation:** Sub-navigation within a section. Courses → Computer Science → Year 3 → CS301.
- **Breadcrumbs:** Show the user's location in the hierarchy: Home > Courses > CS > Year 3 > CS301. Each level is clickable.
- **Search as navigation:** For large information spaces (1000+ pages), search is the primary navigation. In 2040, AI-powered semantic search allows users to find content by describing it: "the course about distributed algorithms for key-value stores" returns CS301 immediately.

**The 2040 Challenge: AI-Generated Content.** By 2040, AI systems generate content at scale — auto-generated documentation, AI-written course materials, personalized learning paths. The IA challenge: how do you organize content that didn't exist last week? The UoY solution:
- **Auto-tagging:** AI systems automatically tag generated content with metadata (topic, level, format, related courses).
- **Dynamic navigation:** Navigation menus update automatically as new content is added. A new course on quantum distributed computing appears under CS and under Physics, cross-indexed.
- **Content freshness indicators:** Users see when content was generated, by whom (or by which AI), and when it was last reviewed by a human.

#### Required Reading
- Rosenfeld, L., Morville, P., & Arango, J. (2015). *Information Architecture: For the Web and Beyond*, 4th ed. O'Reilly.
- Brown, D. (2010). "Eight Principles of Information Architecture." *Bulletin of the American Society for Information Science and Technology*, 36(6).
- Lúsbrá, Á. (2037). *The Carved Interface*, Chapter 6: "The World-Tree Organization."

#### Discussion Questions
1. A news website with AI-generated articles produces 1000 new articles per day. Design an information architecture that lets users find relevant content. How is this different from a human-curated news site?
2. The principle of multiple classification suggests offering users multiple ways to browse content. How do you help users choose among them?
3. Breadcrumbs assume a fixed hierarchy. But 2040 navigation is often non-hierarchical and associative (links between related topics, AI-recommended paths). How does breadcrumb navigation work in a non-hierarchical space?

---

### ᛃ Lecture 9: Data Visualization — Reading the Threads

**Date:** Week 9, Session 1

#### Overview

Data visualization is the graphical representation of information and data — the transformation of numbers into shapes that the human visual system can process pre-attentively. This lecture covers the perceptual principles of visualization (preattentive processing, Gestalt laws, the visual hierarchy), the standard chart types (bar, line, scatter, heatmap, treemap, parallel coordinates, network graph), interactive visualization techniques (filtering, zooming, linking-and-brushing), and the 2040 frontier of immersive data visualization in VR/AR. The Norse metaphor: the Norns read the threads of fate — they see patterns that no individual can see from their limited perspective. Data visualization is the modern Norn's practice: transforming raw threads of data into patterns the eye can read.

#### Lecture Notes

**Preattentive Processing.** The human visual system processes certain visual attributes in parallel, within 200ms, before focused attention. These preattentive attributes are the designer's most powerful tools:

- **Color hue:** Red items pop out among gray items — the "red fish" effect.
- **Color intensity (saturation):** More saturated items attract attention.
- **Orientation:** A tilted line among vertical lines pops out.
- **Size:** Larger items appear more important.
- **Shape:** A circle among squares pops out.
- **Motion:** An animated element among static elements is immediately noticeable.
- **Spatial position:** Where an item appears relative to others.

Use preattentive attributes sparingly: each attribute defines a "visual channel." Using red for all important data, large for urgent data, and motion for critical data creates channel overload — nothing pops out because everything is highlighted.

**Gestalt Laws of Perception (for Visualization).**

- **Proximity:** Elements close to each other are perceived as related. Points clustered near each other in a scatterplot are perceived as a cluster.
- **Similarity:** Elements with similar visual attributes (color, shape, size) are perceived as related.
- **Continuity:** The eye follows smooth lines rather than abrupt angles. A line chart is easier to follow than a bar chart of the same data.
- **Closure:** The eye completes incomplete shapes. This can be used for minimalist designs.
- **Figure-ground:** The eye separates objects (figure) from background (ground). A dark-colored area on a chart becomes the "figure."

**Chart Selection (The Four-Quadrant Model, based on Andy Kirk's work).**

| Data Relationship | Best Chart | Example |
|---|---|---|
| Change over time | Line chart | CPU utilization over 24 hours |
| Comparison of values | Bar chart | Course enrollment by department |
| Correlation between variables | Scatterplot | GPU power vs. training throughput |
| Distribution of values | Histogram + box plot | Distribution of assignment scores |
| Part-to-whole relationship | Stacked bar or treemap | Memory usage by process |
| Geographical patterns | Choropleth map | Internet speed by country |
| Network connections | Force-directed graph | Paper citation network |
| Hierarchical data | Treemap or sunburst | File system directory size |

**Interactive Visualization (Shneiderman's Mantra, 1996, updated 2040).**
> Overview first, zoom and filter, then details-on-demand.

1. **Overview:** Show the entire dataset at once (even if at low resolution). The user gets the big picture.
2. **Zoom:** Allow the user to zoom into a region of interest. The zooming is animated to preserve context.
3. **Filter:** Allow the user to filter out irrelevant data (sliders, checkboxes, range selectors).
4. **Details-on-demand:** Click on an element to see its full details (a tooltip, a side panel, or a voice readout in immersive environments).
5. **Relate:** Show relationships between different views. A scatterplot and a map of the same data are linked — selecting points in one highlights them in the other. This is **linking-and-brushing**.

**2040: Immersive Data Visualization.** In VR/AR, data visualization is 3D and spatial. The UoY's **VerðandiViz** platform supports:
- **3D scatterplots:** Each point is a small sphere floating in space. The user walks through the cloud.
- **Immersive networks:** Force-directed graphs rendered as glowing nodes and edges, floating around the user. The user reaches out to grab a node, which expands to show detail.
- **Time-series as landscapes:** CPU utilization over 24 hours rendered as a terrain — low utilization is valleys, high utilization is mountains. The user flies over the terrain, spotting peaks of high activity.
- **Collaborative analytics:** Multiple users (wearing RúnarLens) stand in the same virtual data space, pointing and discussing. In 2040, teams of data analysts at UoY use VerðandiViz for collaborative exploratory analysis of research data.

#### Required Reading
- Tufte, E. (2001). *The Visual Display of Quantitative Information*, 2nd ed. Graphics Press.
- Kirk, A. (2016). *Data Visualization: A Handbook for Data-Driven Design*. Sage.
- Ware, C. (2013). *Information Visualization: Perception for Design*, 3rd ed. Morgan Kaufmann.
- Shneiderman, B. (1996). "The Eyes Have It: A Task by Data Type Taxonomy for Information Visualizations." *VL*.

#### Discussion Questions
1. How does Tufte's "data-ink ratio" (the proportion of ink devoted to data vs. decoration) apply to interactive visualizations? Is it still relevant when users can interact with the data?
2. In immersive 3D scatterplots, the user's perspective changes as they walk through the data. How does this affect the perception of clusters and outliers? What are the pitfalls?
3. A visualization that uses 7 different colors, 4 different shapes, 3 different sizes, and animated motion is likely to confuse rather than inform. How do you choose which visual channel to use for which aspect of the data?

---

### ᚨ Lecture 10: Design Systems and Component Libraries — The Pattern of the Builder

**Date:** Week 10, Session 1

#### Overview

A design system is a comprehensive set of design standards, components, and guidelines that ensures consistency and efficiency across a product or organization. By 2040, every major digital product has a design system, and the best design systems are themselves powered by AI. This lecture covers the anatomy of a design system (design tokens, components, patterns, guidelines), the tooling ecosystem (Figma, Storybook, and their 2040 descendants), and the integration of design systems with AI agents that can generate UI from specifications. The Norse metaphor: the pattern of the shipbuilder — a standardized design for the Viking longship that ensured every ship was built to the same proven proportions, yet each was unique in its carving and decoration. A design system is the pattern of the shipbuilder for digital products.

#### Lecture Notes

**Anatomy of a Design System.**

*Design Tokens.* The atomic units of visual design — values for color, typography, spacing, shadows, and animation. Examples:
```
--color-primary: #1a5cff (UoY Blue)
--color-surface: #f8f9fa
--font-heading: 'Runar Sans', sans-serif
--spacing-unit: 8px
--border-radius-md: 8px
--shadow-card: 0 2px 8px rgba(0,0,0,0.1)
--transition-fast: 150ms ease
```

Tokens are defined once and referenced everywhere. Changing `--color-primary` from #1a5cff to #0d47a1 changes the color across the entire product, instantly.

*Components.* Reusable UI elements with defined behavior, styling, and API. A well-designed component library includes:
- **Button:** Variants (primary, secondary, ghost, danger), sizes (sm, md, lg), states (default, hover, active, disabled, loading).
- **Input:** Text, number, email, password, search, textarea, with error states, helper text, labels, and prefix/suffix icons.
- **Card:** Header, body, footer slots. Optional shadow, border, interactive (clickable with hover state).
- **Modal:** Title, body, actions. Accessible (focus trap, escape key, ARIA attributes). By 2040, voice-controllable ("Close modal").
- **Table:** Sortable columns, filterable rows, pagination, selection, expandable rows.
- **Form:** Field validation, submission handling, error display, progress save.

*Patterns.* Higher-level solutions to common design problems:
- **Authentication pattern:** Login page → 2FA → redirect to original page.
- **Search pattern:** Search bar with autocomplete → results list with hover preview → detail view.
- **Data input pattern:** Form with validation → confirmation → success message. If invalid, show error inline + scroll to first error.

**The 2040 UoY Design System: RúnarUI.** The University's design system, **RúnarUI**, is the standard for all UoY digital products. It includes:
- 280+ components, 1200+ design tokens
- Web (React), mobile (SwiftUI, Jetpack Compose), spatial (RúnarLens SDK) implementations
- Accessibility compliance with WCAG 3.0 AAA
- Automatic theme generation — the AI assistant generates a complete color palette, typography scale, and spacing system from a one-sentence brand description ("Icelandic north, modern, warm")
- Usage analytics — the design system tracks which components are most used, where they cause confusion (based on error rates), and recommends retirement of underperforming components

**AI and Design Systems.** By 2040, design systems are AI-powered:
- **Natural-language component generation:** "Create a card component that shows a student's photo, name, major, and current course count" → the AI generates the component code, documentation, and Storybook story.
- **Automated accessibility checking:** The AI scans every component commit for WCAG violations and blocks the commit until they are fixed.
- **Design drift detection:** The AI monitors the production app and identifies components that have drifted from their design system specification — mismatched colors, wrong spacing, incorrect behavior.

#### Required Reading
- Frost, B. (2016). *Atomic Design*. Brad Frost Web (online).
- UXPin Design Systems Handbook (2020). Available at uxpin.com.
- Lúsbrá, Á. (2037). *The Carved Interface*, Chapter 7: "The Shipbuilder's Pattern."

#### Discussion Questions
1. Design tokens enforce consistency, but they can also stifle creativity. How do you balance standardization with the need for differentiation across different parts of a product?
2. AI-generated components from natural-language descriptions are convenient, but they risk producing components that don't match the design system's existing patterns. How do you prevent this?
3. A design system with 280+ components is comprehensive but overwhelming for new designers. How would you design an onboarding experience for a designer new to RúnarUI?

---

### ᚨ Lecture 11: Ethics in HCI — The Carver's Oath

**Date:** Week 11, Session 1

#### Overview

As interfaces become more intimate — reading our faces, our voices, our brain signals, our locations — the ethical stakes of HCI design become existential. This lecture covers the ethical frameworks relevant to HCI (utilitarianism, deontology, virtue ethics, the Belmont principles, and the 2040 emerging framework of digital sovereignty), the dimensions of ethical concern (privacy, consent, persuasion, exploitation, accessibility, algorithmic fairness), and the practicing designer's toolkit for ethical decision-making. The Norse metaphor: the rune-carver's oath — a sacred promise to carve true, to serve the community, and to respect the power of the symbols. An interface designer takes a similar oath: to serve the user, not exploit them.

#### Lecture Notes

**The Dimensions of Ethical Concern in HCI.**

*Privacy and Consent.* Every interaction with a digital interface generates data. By 2040, the average person interacts with 50+ digital systems per day, generating thousands of data points. Ethical design requires:
- **Explicit consent:** Data collection must be opt-in, not opt-out. The UoY standard: explain *what* data is collected, *why* it's needed, *how long* it's kept, and *who* has access — in plain language, at the moment of data collection.
- **Data minimization:** Collect only the data necessary for the specific task. A study app does not need the user's location or contact list.
- **Data sovereignty:** The user owns their data. They can access it, export it, delete it, and revoke consent at any time. The **RúnarPrivacy** dashboard at UoY gives students a single-pane view of all data collected about them across all University systems.

*Persuasion and Dark Patterns.* Dark patterns are interface designs that trick users into doing things they didn't intend. By 2040, dark patterns are regulated by the Digital Fairness Act (EU, 2032). Examples:
- **Roach motel:** Easy to sign up, impossible to cancel. The "confirm subscription" page has a prominent button and a tiny, gray "unsubscribe" link.
- **Confirmshaming:** "I don't want to save money" as the option to decline a discount offer.
- **Forced continuity:** The user's free trial is about to expire; the system charges them without a clear warning.
- **Hidden costs:** Extra fees revealed only at the final checkout step in a multi-step flow.

Ethical persuasion (nudge theory, Thaler & Sunstein, 2008) is acceptable when it helps users make decisions that align with their own stated values. A nudge: "You've been working for 3 hours — would you like a break?" (user's stated value: health). A dark pattern: "Your account will be deleted if you don't accept our new terms" (user's stated value: convenience, exploited for consent).

*Accessibility as an Ethical Issue.* Accessibility is not optional (WCAG 3.0 compliance is legally required in 140+ countries by 2040). But beyond legal compliance, the ethical argument is: excluding users with disabilities from digital participation is a form of discrimination that compounds existing social inequalities.

*Algorithmic Fairness.* AI-powered interfaces (recommendation systems, content moderation, automated grading) must be audited for bias. The UoY AI Ethics Board requires every AI-powered interface to:
1. Test for demographic parity (outcomes should not differ by protected characteristics).
2. Test for equalized odds (error rates should not differ by demographic groups).
3. Publish an algorithmic impact assessment for any interface used by more than 100 users.

**Ethical Decision-Making for Designers.**

The **UoY Design Ethics Framework** (inspired by the Belmont Report, extended for 2040):

1. **Identify stakeholders:** Who is affected by this design decision? Users, the company, society, the environment? Consider both direct and indirect stakeholders.

2. **Identify values:** What values are at stake? Privacy, autonomy, dignity, fairness, security, sustainability, community? Some values conflict — a highly secure system may compromise autonomy. These conflicts must be transparent.

3. **Identify tradeoffs:** For each stakeholder and each value, what is the benefit and what is the harm? Can the harm be mitigated without sacrificing the benefit?

4. **The light test:** Would you be comfortable having this design decision published on the front page of the student newspaper? If not, redesign.

5. **The reversibility test:** Can the user reverse the effect of this design? Is there an undo? If the user made a choice, can they change their mind?

#### Required Reading
- The Belmont Report (1978). *Ethical Principles and Guidelines for the Protection of Human Subjects of Research.*
- Thaler, R. & Sunstein, C. (2008). *Nudge: Improving Decisions About Health, Wealth, and Happiness.* Yale.
- Eyal, N. (2014). *Hooked: How to Build Habit-Forming Products.* (Also: the critical responses to Hooked by ethically-minded designers.)
- Harrington, K. et al. (2035). "Digital Sovereignty and User Data." *ACM Symposium on Computing Ethics*.

#### Discussion Questions
1. Dark patterns are illegal in the EU under the 2032 Digital Fairness Act. Should the same regulations apply to UoY's student-facing interfaces? What would it take to audit our systems for dark patterns?
2. AI-powered recommendation systems (for courses, for news, for friends) optimize for engagement, which often means optimizing for time-on-site. Is this ethical? At what point does a recommendation system become coercive?
3. Invasive BCIs for people with paralysis can dramatically improve quality of life. But they also raise the possibility of "brainjacking" — unauthorized control of the BCI. What security and ethical standards should apply?

---

### ᚠ Lecture 12: The Future of HCI — Into the Weave

**Date:** Week 12, Session 1

#### Overview

The final lecture surveys the frontiers of HCI in 2040 and beyond. We cover: symbiotic interfaces (human-AI systems that learn and adapt together), the post-screen era (what comes after the touchscreen), the disappearing interface (computing embedded in the environment), and the meta-design challenge (designing tools for non-designer creators). The Norse framing: Ragnarǫk destroys the old interfaces (screens, keyboards, mice) and a new world rises — interfaces that are woven into the fabric of experience itself, as natural as breathing and as responsive as thought.

#### Lecture Notes

**Symbiotic Interfaces.** J.C.R. Licklider's 1960 vision of "man-computer symbiosis" — a partnership between human and machine that amplifies both — is finally practical in 2040. Examples:
- **AI co-writer:** The writer types, and the AI suggests completions, expansions, alternatives, and corrections. But unlike simple autocomplete, the AI *learns* the writer's style, tone, and preferences over time. The more they write together, the better the suggestions.
- **AI co-designer:** The designer sketches a rough interface, and the AI fills in the details — matching the style of the existing design system, generating the code, adapting to accessibility requirements.
- **AI co-programmer:** The programmer types an intent in natural language, and the AI generates the code. The programmer reviews and refines. The AI learns which patterns the programmer prefers.

The key insight: symbiosis is *bidirectional*. The human adapts to the AI (learning to phrase intents clearly) and the AI adapts to the human (learning their preferences, anticipating their needs). This adaptation creates a feedback loop that makes the partnership increasingly effective over time.

**The Post-Screen Era.** By 2050, the touchscreen — the dominant interface of 2007-2030 — may be as obsolete as the command line. Successor paradigms:
- **Ambient interfaces:** The interface is embedded in the environment — smart surfaces, smart walls, the furniture itself. You don't "open an app"; you walk into a room and the room knows what you need.
- **Contextual interfaces:** The system knows who you are, what you're doing, and what you're likely to need next. The interface adapts moment-by-moment, showing the most relevant options and hiding everything else.
- **Proactive interfaces:** The system anticipates your needs and acts without being asked. "I notice you have a meeting in 5 minutes. I've prepared the notes and reserved the conference room."

**The Disappearing Interface (Mark Weiser's vision, fulfilled by 2040).** Weiser's 1991 vision of "ubiquitous computing" — the most profound technologies are those that disappear — is reality by 2040. Computing is embedded in: clothing (biometric monitoring), jewelry (notifications, authentication), furniture (interactive desks, chairs), architectural surfaces (walls that display information, windows that adjust opacity based on sunlight), and medical implants (glucose monitoring, insulin delivery). The interface disappears; the functionality is woven into the fabric of life.

**The Meta-Design Challenge.** By 2040, many interfaces are created not by professional designers but by AI systems, end-users, or automated processes. The meta-design challenge: how do you design *the tool* that creates interfaces, rather than the interface itself? Key questions:
- How do you ensure that AI-generated interfaces are accessible?
- How do you test an interface that changes every day based on user behavior?
- How do you maintain a consistent user experience across thousands of dynamically generated pages?
- How do you teach students to design *design systems* rather than single interfaces?

**The Final Weave.** The Norse vǫlva sees the fate of all beings, but she does not control it — she describes it. The HCI practitioner in 2040 is a vǫlva: they describe (through prototypes, specifications, design systems) an interface that does not yet exist. The interface is the weave of human intention and computational capability. A well-designed interface disappears — it becomes an extension of the user's will, as natural as reaching for a cup. A poorly-designed interface becomes a wall. The craft of HCI is the craft of weaving interfaces that dissolve: the threshold between human and machine becomes so thin that crossing it feels like moving through air.

#### Required Reading
- Licklider, J.C.R. (1960). "Man-Computer Symbiosis." *IRE Transactions on Human Factors in Electronics*, HFE-1.
- Weiser, M. (1991). "The Computer for the 21st Century." *Scientific American*, 265(3).
- Norman, D. (2007). *The Design of Future Things*. Basic Books.
- Lúsbrá, Á. (2037). *The Carved Interface*, Chapter 12: "The Disappearing Rune."

#### Discussion Questions
1. A symbiotic interface adapts to the user. What happens when two different users — with different styles, preferences, and priorities — share the same device? How does the interface adapt?
2. The "disappearing interface" makes computing seamless and intuitive. Does this seamlessness also make computing invisible — and therefore harder to understand, critique, and control?
3. AI-generated interfaces could lead to a monoculture of design — every app looking the same because they're all generated by the same model. How do we preserve diversity and creativity in interface design?

---

## Final Examination Preparation

### Format

The final examination is a **3-hour portfolio assessment**:
- **Part A: Heuristic Evaluation (30%)** — Evaluate a given interface against Nielsen's 10 usability heuristics. Identify 5 violations, explain each, and propose a fix.
- **Part B: Redesign Proposal (35%)** — Choose a poorly-designed interface from a provided list. Research the users, analyze the problems, and propose a redesigned interface with sketches (hand-drawn or wireframed) and a written rationale.
- **Part C: Design System Component (35%)** — Design and document a new RúnarUI component. Submit: the component specification (states, behavior, accessibility requirements, code), a Storybook story, and a usability test plan.

### Sample Part A Heuristic Evaluation

Evaluate the UoY course registration interface (provided in the exam) against Nielsen's 10 heuristics. Identify and analyze five violations. For each:
- Name the violated heuristic
- Describe the violation (be specific: which page, which element, what happens)
- Rate the severity (0=cosmetic, 1=minor, 2=major, 3=catastrophic)
- Propose a specific fix

### Sample Part B Redesign Topic

The UoY campus map app (text-based, no visual map) is difficult to use. Research the user group (new students), analyze the problems (at least 3), and propose a redesigned interface. Your proposal must include: user research summary, wireframes or sketches, interaction flow, and a design rationale. Consider: wayfinding, search, building information, and accessibility.

### Sample Part C Component Specification

Design a "ProgressPath" component that shows a student's progress through their degree program. The component should: show completed courses, current courses, and planned courses; indicate prerequisite chains; and allow the student to explore "what if" scenarios (what if I drop CS305?). Submit:
- Component specification document
- A Storybook story file
- A usability test plan with 5 tasks

---

## Required Reading — Full Course Bibliography

- Belmont Report (1978). *Ethical Principles and Guidelines for Human Subjects Research.*
- Brown, D. (2010). "Eight Principles of Information Architecture." *ASIS&T Bulletin*.
- Card, S.K., Moran, T.P., & Newell, A. (1983). *The Psychology of Human-Computer Interaction*.
- Clark, H.H. & Brennan, S.E. (1991). "Grounding in Communication." *Perspectives on Socially Shared Cognition*.
- Courage, C. & Baxter, K. (2005). *Understanding Your Users*.
- Eyal, N. (2014). *Hooked: How to Build Habit-Forming Products.*
- Fitts, P.M. (1954). "The Information Capacity of the Human Motor System." *J. Exp. Psych.*
- Frost, B. (2016). *Atomic Design*.
- Harrington, K. et al. (2035). "Digital Sovereignty and User Data." *ACM Symposium*.
- Henry, S.L. (2014). *Just Ask: Integrating Accessibility Throughout Design*.
- ISO 9241-11 (2018). *Ergonomics of Human-System Interaction*.
- Kirk, A. (2016). *Data Visualization: A Handbook*.
- LaViola, J. et al. (2017). *3D User Interfaces*.
- Licklider, J.C.R. (1960). "Man-Computer Symbiosis." *IRE Trans. HFE*.
- Lúsbrá, Á. (2037). *The Carved Interface*. Yggdrasil University Press.
- Milgram, P. & Kishino, F. (1994). "A Taxonomy of Mixed Reality Visual Displays." *IEICE*.
- Norman, D. (2013). *The Design of Everyday Things*.
- Norman, D. (2007). *The Design of Future Things*.
- Pearl, C. (2016). *Designing Voice User Interfaces*.
- Rosenfeld, L., Morville, P., & Arango, J. (2015). *Information Architecture*.
- Sauro, J. & Lewis, J.R. (2016). *Quantifying the User Experience*.
- Shneiderman, B. (1983). "Direct Manipulation: A Step Beyond Programming Languages." *IEEE Computer*.
- Shneiderman, B. (1996). "The Eyes Have It." *VL Symposium*.
- Shneiderman, B. et al. (2016). *Designing the User Interface*.
- Thaler, R. & Sunstein, C. (2008). *Nudge*.
- Tidwell, J. (2010). *Designing Interfaces*.
- Tufte, E. (2001). *The Visual Display of Quantitative Information*.
- Ware, C. (2013). *Information Visualization*.
- WCAG 3.0 (2024). *Web Content Accessibility Guidelines*.
- Weiser, M. (1991). "The Computer for the 21st Century." *Scientific American*.
- Wolpaw, J.R. & Wolpaw, E.W. (2012). *Brain-Computer Interfaces*.

---

*This course has been one long conversation about carving — carving interfaces that speak to users, carving structures that organize information, carving spaces that feel natural, carving ethics that protect the vulnerable. You leave this course not just as a designer but as a carver: someone who shapes the interactions that shape the world. Carve well. — Dr. Álfhildr Lúsbrá, Alþingi Month, Summer 2040.*
