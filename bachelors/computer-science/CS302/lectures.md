# CS302: Compiler Design & Code Generation
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4  
**Description:** Lexing, parsing, IR, optimization, LLVM, JIT, AOT

---

## Lectures

ᛉ **Lecture 1: The Craft of Compilation — From Source to Machine and Beyond**

**Course:** CS302 — Compiler Design & Code Generation  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

A compiler is a translator — a smith who takes raw ore (source code) and forges it into a blade (machine code) fit for battle (execution). Like the dwarf-smiths of Svartálfaheimr who crafted Gungnir for Odin, the compiler must understand both the material it works with and the purpose its product will serve.

This course traces the full journey of a compiler: from the raw characters of source text through the structure of syntax, the meaning of types, the transformation of intermediate representations, and finally the emission of machine code that runs on real hardware. Along the way, we will study the great algorithms that make this translation possible — algorithms that have remained relevant for sixty years and continue to evolve in the age of multi-target compilation, just-in-time execution, and AI-guided optimization.

### The Compilation Pipeline

A compiler is organized as a pipeline of phases, each transforming its input into a more refined form:

```
Source Code
    │
    ▼
┌──────────┐     ┌──────────┐     ┌──────────────┐
│  Lexical  │────▶│  Syntax  │────▶│   Semantic    │
│ Analysis  │     │ Analysis │     │   Analysis    │
│ (Scanner) │     │ (Parser) │     │ (Type Checker)│
└──────────┘     └──────────┘     └──────────────┘
      │                │                  │
   Tokens          Parse Tree      Annotated Tree
                                         │
                                         ▼
                                 ┌──────────────┐
                                 │ Intermediate │
                                 │ Representation│
                                 │  Generation   │
                                 └──────────────┘
                                         │
                                         ▼
                                 ┌──────────────┐
                                 │ Optimization  │
                                 │   (multiple   │
                                 │    passes)    │
                                 └──────────────┘
                                         │
                                         ▼
                                 ┌──────────────┐
                                 │    Code       │
                                 │  Generation   │
                                 └──────────────┘
                                         │
                                         ▼
                                    Machine Code
```

**Front End**: Language-dependent phases (lexical analysis, syntax analysis, semantic analysis). Converts source text to an intermediate representation.

**Middle End**: Language- and machine-independent optimization. Transforms IR into more efficient equivalent IR.

**Back End**: Machine-dependent code generation. Selects instructions, allocates registers, and emits assembly or machine code.

This three-part structure is crucial. It is what allows a single optimizer to serve many languages (C, C++, Rust, Swift all compile to LLVM IR) and many targets (x86, ARM, RISC-V, WASM all share the same optimization pipeline).

### Historical Arc

- **1954**: FORTRAN compiler for IBM 704. First optimizing compiler. Led by John Backus, it produced code competitive with hand-written assembly.
- **1960s**: Theory of formal languages develops. Chomsky hierarchy (1956) provides the mathematical foundation for parsing.
- **1970s**: LR parsing (Knuth, 1965), LALR parsing (DeRemer, 1971), and the yacc/bison toolchain. Unix pipeline philosophy (Thompson, Ritchie) influences compiler architecture.
- **1980s**: SSA form (Rosen, Wegman, Zadeck, 1988) revolutionizes optimization. GCC emerges as the dominant open-source compiler.
- **1990s**: Java introduces JIT compilation to the mainstream (HotSpot JVM, 1999). Just-In-Time compilation becomes practical for managed languages.
- **2000s**: LLVM (Lattner, 2000-2004) demonstrates that a clean, retargetable IR can serve as the backbone for a compiler infrastructure supporting many languages and targets.
- **2010s-2040s**: Compiler infrastructure evolves into an ecosystem. Profile-guided optimization, auto-vectorization, polyhedral models, and ML-guided optimization become standard. Verified compilers (CompCert) prove correctness end-to-end.

### The 2040 Context

At UoY, our compiler lab uses LLVM 28 as the primary infrastructure. Students implement a full front end for a teaching language (NornScript), generate LLVM IR, and leverage LLVM's optimization passes before targeting x86-64, RISC-V, and WASM. The final project requires implementing at least one custom optimization pass and evaluating its impact on real benchmarks.

By 2040, compilers are no longer passive translators. They are:
- **Adaptive**: ML-guided optimization profiles the code at runtime and adjusts inlining, vectorization, and register allocation accordingly.
- **Verified**: Tools like CompCert and CakeML prove that the compiler preserves the semantics of the source program.
- **Multi-target**: A single IR compiles to CPUs, GPUs, TPUs, and WASM without source changes.
- **Collaborative**: The IDE and the compiler work together — the compiler provides diagnostics, suggestions, and refactoring assistance in real time.

### Key Terminology

- **Token**: The smallest meaningful unit recognized by the lexer (identifier, keyword, literal, operator).
- **Parse tree**: A tree representation of the syntactic structure of the source program according to the grammar.
- **AST (Abstract Syntax Tree)**: A simplified parse tree that omits syntactic sugar (parentheses, semicolons) and retains essential structure.
- **IR (Intermediate Representation)**: A machine-independent representation that serves as the interface between the front end and back end.
- **Basic block**: A maximal sequence of instructions with one entry point and one exit point.
- **Control flow graph (CFG)**: A graph of basic blocks with edges representing possible execution paths.
- **SSA (Static Single Assignment)**: An IR form where each variable is assigned exactly once, making dataflow analysis simpler and more powerful.

### Required Reading

- Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D. (2006). *Compilers: Principles, Techniques, and Tools* (2nd ed.). Pearson. Chapters 1-2.
- Lattner, C. & Adve, V. (2004). "LLVM: A Compilation Framework for Lifelong Program Analysis & Transformation." *CGO*.
- Cooper, K. D. & Torczon, L. (2022). *Engineering a Compiler* (3rd ed.). Morgan Kaufmann. Chapter 1.

### Discussion Questions

1. If a compiler is a translator, what is "lost in translation"? Can a compiled program ever be more correct than its source?
2. LLVM's three-phase architecture (front-middle-back) enables language and target independence. What are the costs of this generality? Are there cases where a single-pass compiler outperforms a multi-stage compiler?
3. The FORTRAN I compiler (1954) produced code competitive with hand-written assembly. If you were designing a compiler in 2040, what would "competitive with hand-written code" mean for modern architectures?

### Practice Problems

1. **Pipeline trace**: Given the C expression `x = a + b * c`, trace each compiler phase from source text through tokens, parse tree, AST, IR, and assembly (x86-64).
2. **Phase identification**: For each task, identify the compiler phase: (a) detecting that a variable is used before being defined, (b) converting `if` statements to conditional branches, (c) replacing `2 * x` with `x << 1`, (d) detecting that `/` is a division operator.
3. **Design decision**: You are building a compiler for a new language that runs on both embedded ARM microcontrollers and cloud x86 servers. How does the three-phase architecture help? What optimizations differ between the two targets?

---

ᛉ **Lecture 2: Lexical Analysis — Where Characters Become Tokens**

**Course:** CS302 — Compiler Design & Code Generation  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Lexical analysis (scanning) is the compiler's first encounter with the source text. It transforms a stream of characters into a stream of tokens — the smallest meaningful units of the language. The scanner strips whitespace and comments, groups characters into identifiers, keywords, literals, and operators, and passes the token stream to the parser.

This lecture covers the mathematical foundations of lexical analysis (regular expressions and finite automata), the algorithms for constructing efficient scanners (NFA → DFA → minimized DFA), and the practical concerns of building a lexer by hand or using tools like flex and re2c.

### Regular Expressions

Regular expressions define the patterns that the scanner recognizes. Each token class is specified as a regular expression:

```
Identifier:  [a-zA-Z_][a-zA-Z0-9_]*
Integer:     [0-9]+
Float:       [0-9]+\.[0-9]+([eE][+-]?[0-9]+)?
Keyword:     if | else | while | for | return | ...
Operator:    + | - | * | / | = | == | != | < | > | <= | >= | && | || | ...
String:      "([^"\\]|\\.)*"
Comment:     //.*$ | /\*([^*]|\*+[^*/])*\*+/
Whitespace:  [ \t\r\n]+
```

Regular expressions are built from three operations:
1. **Union** (R1 | R2): Matches either R1 or R2.
2. **Concatenation** (R1 R2): Matches R1 followed by R2.
3. **Kleene star** (R*): Matches zero or more repetitions of R.

These three operations, plus ε (empty string) and ∅ (empty language), form the foundation of pattern matching in the scanner.

### Finite Automata

**Deterministic Finite Automaton (DFA)**: A 5-tuple (Q, Σ, δ, q₀, F) where Q is a finite set of states, Σ is the input alphabet, δ: Q × Σ → Q is the transition function, q₀ is the start state, and F ⊆ Q is the set of accepting states. Each input character causes exactly one transition.

**Nondeterministic Finite Automaton (NFA)**: δ maps each (state, symbol) pair to a *set* of states. ε-transitions allow movement between states without consuming input. An NFA accepts a string if *some* path from q₀ to a state in F consumes the entire string.

**Key theorems**:
- For every NFA, there exists an equivalent DFA (subset construction).
- For every regular expression, there exists an NFA that recognizes the same language (Thompson's construction).
- Every regular language can be expressed as a regular expression (Kleene's theorem).
- A DFA with n states can be minimized to a unique canonical form with at most n states.

### Thompson's Construction

Given a regular expression R, Thompson's construction builds an NFA with at most 2|R| states (where |R| is the number of symbols and operators in R). The construction rules are:

1. **ε**: NFA with two states connected by an ε-transition.
2. **a**: NFA with two states connected by a transition on symbol a.
3. **R1 | R2**: Create new start and accepting states. ε-transition from new start to starts of R1 and R2. ε-transitions from accepting states of R1 and R2 to new accepting state.
4. **R1 R2**: Concatenation: accepting state of R1 becomes start state of R2 (via ε-transition).
5. **R***: Create new start and accepting states. ε-transition from new start to new accepting and to start of R. ε-transition from accepting state of R to start of R and to new accepting state.

### NFA to DFA: Subset Construction

The subset construction converts an NFA with n states to a DFA with at most 2ⁿ states. For each DFA state, which is a set of NFA states:

1. Compute ε-closure of the current state set.
2. For each input symbol, compute the set of NFA states reachable from the current set.
3. The new state set is the ε-closure of the reachable states.
4. Mark sets containing NFA accepting states as DFA accepting states.

**Minimization**: After construction, minimize the DFA using Hopcroft's algorithm (O(n log n) for n states). The minimized DFA is unique up to state renaming.

### Practical Lexer Construction

**The Maximal Munch Rule**: When the scanner reads characters, it keeps consuming as long as the current prefix matches some pattern. When no extension matches, it backs up one character and emits the longest match. This ensures `==` is tokenized as one token (equality), not two (`=` assignment, `=` assignment).

**Priority Rules**: When two patterns match the same longest string, the scanner uses the *first* pattern in the specification. This means keyword patterns should appear before the identifier pattern.

**Lexical Ambiguities**:
- `ifelse` → identifier (no keyword matches), not `if` + `else`
- `2e3` → float (2.0 × 10³), not `2` + identifier `e3`
- `a+++b` → `a` `++` `+` `b`, not `a` `+` `++` `b` (maximal munch for `+++` fails; longest valid token is `++`)

### Hand-Written vs. Generated Lexers

**Generated (flex, re2c)**:
- Pros: Fast to develop, mathematically correct, handles complex patterns easily.
- Cons: Slower than hand-written (table-driven dispatch), harder to debug, generated code is unreadable.

**Hand-written**:
- Pros: Full control, faster execution, easier to add context-sensitive rules (e.g., string interpolation).
- Cons: More error-prone, more code to maintain, harder to verify correctness.

**Modern approach (2040)**: Most production compilers use hand-written lexers. GCC, Clang, V8, and Go all use hand-written scanners. The reason is speed — a table-driven DFA has 1-2 orders of magnitude more branch mispredictions than a hand-written lexer that can exploit the structure of the language. The generated lexer approach is used in teaching and prototyping, and in compiler-compilers like ANTLR.

### Required Reading

- Aho et al. (2006). *Compilers*, Chapter 3 (Lexical Analysis).
- Appel, A. (2004). *Modern Compiler Implementation in ML*, Chapter 2.
- Lesk, M. E. (1975). "Lex — A Lexical Analyzer Generator." *Unix Programmer's Manual*.

### Discussion Questions

1. Why do most production compilers use hand-written lexers despite the availability of tools like flex? Under what circumstances would a generated lexer be preferable?
2. A language allows nested comments (`/* /* inner */ outer */`). Can a DFA-based scanner handle nested comments? How about an NFA? What approach would you use?
3. Regular expressions cannot match balanced parentheses (this is a context-free language). Yet most scanners use regexes to describe tokens. Why is this not a problem?

### Practice Problems

1. **NFA construction**: Build the NFA for the regular expression `(a|b)*abb` using Thompson's construction. Show all ε-transitions.
2. **Subset construction**: Convert your NFA to a DFA using subset construction. Show the transition table.
3. **Tokenization**: Given the input `if(x<=y+3)`, and the token classes [if, identifier, lparen, le, identifier, plus, integer, rparen], trace the scanner's token-by-token output. What happens if the scanner sees `x<y` and the patterns include both `<` and `<=`?

---

ᛉ **Lecture 3: Context-Free Grammars & Top-Down Parsing — Building Structure from Tokens**

**Course:** CS302 — Compiler Design & Code Generation  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

The scanner gives us tokens; the parser gives us *structure*. Parsing is the process of determining whether a sequence of tokens conforms to the grammar of the language and, if so, constructing a parse tree (or AST) that represents its hierarchical structure.

This lecture covers context-free grammars (CFGs), top-down parsing strategies (recursive descent, predictive parsing), and the mathematical tools (FIRST and FOLLOW sets) that make deterministic parsing possible.

### Context-Free Grammars

A context-free grammar G = (V, Σ, R, S) consists of:
- **V**: A finite set of nonterminal symbols (e.g., Stmt, Expr, Type)
- **Σ**: A finite set of terminal symbols (tokens from the scanner)
- **R**: Production rules of the form A → α, where A ∈ V and α ∈ (V ∪ Σ)*
- **S**: The start symbol (S ∈ V)

**Example — simplified expression grammar**:
```
E  → E + T | T
T  → T * F | F
F  → ( E ) | id | num
```

This grammar is **left-recursive**, which causes top-down parsers to loop infinitely. We eliminate left recursion by rewriting:

```
E  → T E'
E' → + T E' | ε
T  → F T'
T' → * F T' | ε
F  → ( E ) | id | num
```

**Ambiguity**: A grammar is ambiguous if some string has two or more distinct parse trees. The classic example is the dangling else:

```
Stmt → if Expr then Stmt else Stmt
     | if Expr then Stmt
     | other
```

For `if E1 then if E2 then S1 else S2`, the `else` can bind to either `if`. Most languages resolve this by associating `else` with the nearest `if`, which can be enforced by restructuring the grammar.

### Predictive Parsing: LL(1)

An LL(1) parser uses a single lookahead token to decide which production to apply. It is called LL(1) because it scans the input **L**eft-to-right, constructs a **L**eftmost derivation, with **1** token of lookahead.

**FIRST set**: For a string α of grammar symbols, FIRST(α) is the set of terminals that begin strings derivable from α. If α can derive ε, then ε ∈ FIRST(α).

**FOLLOW set**: For a nonterminal A, FOLLOW(A) is the set of terminals that can appear immediately to the right of A in some sentential form. If A can be the rightmost symbol, then $ ∈ FOLLOW(A).

**Computing FIRST**:
1. If X is a terminal, FIRST(X) = {X}.
2. If X → ε, add ε to FIRST(X).
3. If X → Y₁Y₂...Yₖ, add FIRST(Y₁) - {ε} to FIRST(X). If ε ∈ FIRST(Y₁), add FIRST(Y₂) - {ε} to FIRST(X). Continue. If ε is in all FIRST(Yᵢ), add ε to FIRST(X).

**Computing FOLLOW**:
1. Add $ to FOLLOW(S) (start symbol).
2. If A → αBβ, add FIRST(β) - {ε} to FOLLOW(B).
3. If A → αB or A → αBβ where ε ∈ FIRST(β), add FOLLOW(A) to FOLLOW(B).

**LL(1) parse table**: For each production A → α and terminal a ∈ FIRST(α), add A → α to M[A, a]. If ε ∈ FIRST(α), add A → α to M[A, b] for each b ∈ FOLLOW(A). If there's a conflict (two entries in the same cell), the grammar is not LL(1).

### Recursive Descent Parsing

Recursive descent is the simplest and most common top-down parsing technique. Each nonterminal becomes a function:

```python
def parse_E():
    parse_T()
    parse_E_prime()

def parse_E_prime():
    if lookahead == '+':
        match('+')
        parse_T()
        parse_E_prime()
    # else: ε-production (do nothing)

def parse_T():
    parse_F()
    parse_T_prime()

def parse_T_prime():
    if lookahead == '*':
        match('*')
        parse_F()
        parse_T_prime()
    # else: ε-production

def parse_F():
    if lookahead == '(':
        match('(')
        parse_E()
        match(')')
    elif lookahead == 'id':
        match('id')
    elif lookahead == 'num':
        match('num')
    else:
        error(f"expected '(', id, or num, got {lookahead}")
```

**Error recovery**: When the parser encounters an unexpected token, it can:
1. **Panic mode**: Skip tokens until a FOLLOW set member is found.
2. **Phrase-level recovery**: Insert or delete tokens to fix common errors.
3. **Error productions**: Add grammar rules that match common errors and produce helpful diagnostics.

### 2040: Practical Parsers

By 2040, most production compilers use hand-written **recursive descent parsers** with error recovery (Clang, GCC, Go, Rust, Swift). The reasons:
- Better error messages than generated parsers.
- More control over context-sensitive parsing (e.g., C's typedef-name ambiguity).
- Performance comparable to or better than table-driven parsers.

**Parser combinators** (functional programming approach): Libraries like Parsec (Haskell), FastParse (Scala), and Nom (Rust) compose small parsers into larger ones. Popular in domain-specific languages and data format parsers.

**PEG (Parsing Expression Grammars)**: An alternative to CFGs. PEGs use ordered choice (/) instead of unordered alternation (|), making them unambiguous by definition. Packrat parsing provides linear-time PEG parsing. Used in many modern language tools.

### Required Reading

- Aho et al. (2006). *Compilers*, Chapter 4 (Syntax Analysis, sections 4.1-4.4).
- Appel (2004). *Modern Compiler Implementation*, Chapter 3.
- Ford, B. (2004). "Parsing Expression Grammars: A Recognition-Based Syntactic Foundation." *POPL*.

### Discussion Questions

1. C's grammar requires the parser to know whether an identifier is a typedef name or an ordinary identifier. How does a recursive descent parser handle this? How would a generated parser handle it?
2. PEG grammars are never ambiguous. Why isn't PEG the universal solution for all language parsing? What are the disadvantages of ordered choice?
3. Most JSON parsers are hand-written. Why? What makes JSON amenable to hand-written parsing?

### Practice Problems

1. **FIRST/FOLLOW**: Given the grammar `E → T E', E' → + T E' | ε, T → F T', T' → * F T' | ε, F → ( E ) | id`, compute FIRST and FOLLOW for all nonterminals.
2. **LL(1) check**: Is the grammar from problem 1 LL(1)? Construct the parse table and check for conflicts.
3. **Left factoring**: The grammar `S → if E then S else S | if E then S | a` is not LL(1) due to common prefixes. Left-factor it and verify the result is LL(1).

---

ᛉ **Lecture 4: Bottom-Up Parsing — LR Parsing and Its Variants**

**Course:** CS302 — Compiler Design & Code Generation  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

Bottom-up parsers build the parse tree from the leaves (terminals) upward to the root (start symbol). They are more powerful than top-down parsers — every LL(1) grammar is LR(1), but not vice versa. Bottom-up parsers can handle a wider class of grammars, including most programming language grammars without modification.

This lecture covers LR(0), SLR, LALR(1), and CLR(1) parsing, their construction algorithms, and their practical applications in tools like yacc, bison, and their descendants.

### Shift-Reduce Parsing

An LR parser maintains a **stack** of grammar symbols and parser states, and reads input from left to right. At each step, it performs one of two actions:

1. **Shift**: Push the next input symbol onto the stack and transition to the appropriate state.
2. **Reduce**: Pop the right-hand side of a production from the stack, push the left-hand side, and transition to the state indicated by the goto table.

The parser uses two tables:
- **ACTION table**: Maps (state, lookahead) to shift, reduce, accept, or error.
- **GOTO table**: Maps (state, nonterminal) to a new state (used after reductions).

### LR(0) Items and States

An LR(0) item is a production with a dot (•) indicating how much has been seen. For the production `A → XYZ`:
- `A → •XYZ` (nothing seen yet)
- `A → X•YZ` (X seen, expecting Y)
- `A → XY•Z` (XY seen, expecting Z)
- `A → XYZ•` (complete — ready to reduce)

The **closure** of a set of items adds all items that can be derived from the current position of the dot. The **goto** operation moves the dot past a symbol and takes the closure of the result.

An LR(0) parser is constructed by:
1. Computing the closure of the initial item set {S' → •S$}.
2. Computing goto sets for each grammar symbol.
3. Repeating until no new item sets exist.

### SLR (Simple LR)

SLR parsing uses LR(0) items but restricts reductions: a reduction `A → α` is performed only when the lookahead is in FOLLOW(A). This is more restrictive than LR(0), which reduces whenever the dot is at the end of any production.

**SLR limitations**: FOLLOW sets may be too large, causing spurious reductions. Not all grammars that are LR(1) are SLR.

### LALR(1) (Look-Ahead LR)

LALR(1) is the most commonly used variant. It merges LR(1) item sets that have the same core (same LR(0) items) but different lookaheads. This dramatically reduces the number of states (same as SLR) while maintaining most LR(1) power.

**Construction**: Start with LR(1) items. Merge states with the same core. Propagate lookaheads through the merged states.

**LALR(1) vs LR(1)**: LALR(1) may introduce reduce-reduce conflicts that LR(1) does not have. In practice, these conflicts are rare and can be resolved by restructuring the grammar.

**bison/yacc**: The most widely used LALR(1) parser generators. Bison produces C code from a grammar specification with embedded actions. Modern bison supports GLR (Generalized LR) parsing for ambiguous grammars.

### CLR(1) (Canonical LR)

CLR(1) is the most powerful LR variant. It uses full LR(1) items without merging, resulting in many more states but accepting the largest class of LR grammars. In practice, CLR(1) parsers are rarely used because the state count is too large for most programming languages.

### Practical Considerations

**Shift-reduce conflicts**: Occur when the parser can either shift the next token or reduce by a production. Bison resolves these by shifting (the "shift" resolution), which corresponds to the "dangling else" resolution.

**Reduce-reduce conflicts**: Occur when two productions can be reduced with the same lookahead. Always indicate a grammar problem. Bison resolves by choosing the production listed first.

**Operator precedence**: Bison allows specifying precedence rules that resolve shift-reduce conflicts for expressions. `%left`, `%right`, `%nonassoc` declarations control associativity and precedence.

### 2040: The State of Parsing

**GLR parsing**: Bison's GLR mode handles ambiguous grammars by exploring all possible parses simultaneously. Used for C++ (which has inherently ambiguous grammar), COBOL, and other complex languages.

**Error recovery**: Modern parsers (bison, tree-sitter) use error recovery strategies to continue parsing after syntax errors:
- **Error token**: Bison's `error` special token skips input until a synchronizing token is found.
- **Error productions**: Grammar rules that match common error patterns.
- **Partial parsing**: Tree-sitter can parse files with multiple errors, producing a partial AST for IDE features like syntax highlighting and code completion.

**Incremental parsing**: Tree-sitter and similar tools support incremental parsing — re-parsing only the portion of the file that changed. Enables real-time IDE features with <1ms parse times for files under 10,000 lines.

### Required Reading

- Aho et al. (2006). *Compilers*, Chapter 4 (sections 4.5-4.7).
- Appel (2004). *Modern Compiler Implementation*, Chapter 5.
- Grune, D. & Jacobs, C. (2008). *Parsing Techniques: A Practical Guide* (2nd ed.). Springer.

### Discussion Questions

1. Every LL(1) grammar is LR(1), but not vice versa. Give an example of a common programming language construct that is LR(1) but not LL(1). How is this construct handled in practice?
2. LALR(1) merges LR(1) states with the same core. Under what conditions does this merging introduce reduce-reduce conflicts?
3. C++ has an inherently ambiguous grammar (the "most vexing parse"). How do real C++ parsers handle this? Why can't a deterministic parser handle it?

### Practice Problems

1. **LR(0) item sets**: Given the grammar `S → S S + | S S * | a`, construct all LR(0) item sets and the goto table.
2. **SLR parse table**: Using the item sets from problem 1, construct the SLR ACTION and GOTO tables. Show any conflicts.
3. **Shift-reduce resolution**: The expression grammar `E → E + E | E * E | ( E ) | id` has shift-reduce conflicts for `+` and `*`. Using precedence (multiplication before addition, left-associativity), show which actions the parser takes for the input `id + id * id`.

---

ᛉ **Lecture 5: Semantic Analysis & Type Systems — Meaning from Structure**

**Course:** CS302 — Compiler Design & Code Generation  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

The parser produces a tree, but trees don't execute. Before the compiler can generate code, it must verify that the program is *well-formed*: types are consistent, variables are declared before use, functions are called with the right number of arguments, and operations are applied to compatible operands. This phase is semantic analysis, and its backbone is the type system.

### Type Systems: The Logic of Data

A type system is a tractable syntactic method for proving the absence of certain program behaviors by classifying phrases according to the kinds of values they compute. (Pierce, 2002)

**Static vs. Dynamic Typing**:
- **Static**: Types checked at compile time. Errors caught before execution. (C, Java, Rust, Haskell)
- **Dynamic**: Types checked at runtime. More flexible, more runtime overhead. (Python, JavaScript, Ruby)
- **Gradual**: Mix of static and dynamic. Optional type annotations. (TypeScript, Python with type hints, Reticulated Python)

**Type Soundness** (safety): If a well-typed program compiles, it will not get stuck at runtime (it will either run forever or produce a value of the expected type). This is the combination of **progress** (well-typed programs can always take a step) and **preservation** (well-typed programs remain well-typed after each step).

### Type Checking Rules

Type checking rules are specified as inference rules:

```
Γ ⊢ e₁ : τ₁    Γ ⊢ e₂ : τ₂    τ₂ ≤ τ₁
───────────────────────────────────────────────  (T-Assign)
        Γ ⊢ e₁ = e₂ : τ₁
```

"Under typing environment Γ, if expression e₁ has type τ₁ and e₂ has type τ₂, and τ₂ is a subtype of τ₁, then the assignment e₁ = e₂ has type τ₁."

**Subtyping**: τ₁ ≤ τ₂ means τ₁ is a subtype of τ₂ (every τ₁ value is also a τ₂ value). For records, subtyping is width- and depth-subtyping.

### Symbol Tables and Scopes

The symbol table maps identifiers to their declarations. It must handle nested scopes:

```python
class SymbolTable:
    def __init__(self, parent=None):
        self.parent = parent  # enclosing scope
        self.symbols = {}     # name → (type, kind, offset)
    
    def lookup(self, name):
        if name in self.symbols:
            return self.symbols[name]
        if self.parent:
            return self.parent.lookup(name)
        return None  # undefined
    
    def define(self, name, type, kind, offset):
        self.symbols[name] = (type, kind, offset)
```

**Scope levels**: Global → module → class → function → block. Each level has its own symbol table with a pointer to the enclosing scope.

**Name resolution**: When the compiler encounters an identifier, it looks up the name in the symbol table chain, starting from the innermost scope and proceeding outward. This process is called **environment lookup**.

### Type Inference

For languages with type inference (Haskell, ML, Rust), the compiler doesn't require explicit type annotations. Instead, it infers types from usage using **Hindley-Milner type inference** (Algorithm W):

1. Assign a fresh type variable to each expression whose type is unknown.
2. Generate constraints from the program structure (e.g., `+` requires both operands to be `int` or both to be `float`).
3. Unify the constraints to solve for type variables.

**Unification**: The process of making two types equal by substituting type variables. If we have constraint `α = int → β` and constraint `α = γ → bool`, unification gives `α = int → bool`, `β = bool`, `γ = int`.

### Error Reporting

A good compiler produces helpful error messages. The type checker should report:
- **Location**: File, line, column of the error.
- **Expected vs. actual**: "Expected `int`, found `string`" rather than "Type mismatch."
- **Suggestion**: "Did you mean `x.to_int()`?"
- **Context**: Show the full expression where the error occurs, with the problematic sub-expression highlighted.

**Error recovery**: After detecting one type error, the compiler should continue checking (not stop at the first error). This requires synthesizing default types for ill-typed expressions.

### 2040: Modern Type Systems

By 2040, type systems have become far more expressive than the simple systems of the 1990s:

- **Dependent types** (Idris, Agda): Types can depend on values. `Vec Int n` is a vector of integers of length n. Allows proving properties in the type system.
- **Ownership types** (Rust): Track ownership and borrowing at the type level, guaranteeing memory safety without garbage collection.
- **Effect systems** (Koka, Eff): Track side effects in types. A function's type indicates whether it can throw exceptions, access I/O, or modify mutable state.
- **Linear types** (Rust, Clean): Values that must be used exactly once. Prevent double-free and use-after-free bugs at compile time.
- **Refinement types** (F*, Liquid Haskell): Types with logical predicates. `{x : int | x > 0}` is a positive integer. Complemented by SMT solvers for automatic verification.

### Required Reading

- Pierce, B. C. (2002). *Types and Programming Languages*. MIT Press. Chapters 1-9 (core type systems), 15-16 (subtyping).
- Aho et al. (2006). *Compilers*, Chapter 5 (Syntax-Directed Translation) and Chapter 6 (Type Checking).
- Nielson, F., Nielson, H. R., & Hankin, C. (2015). *Principles of Program Analysis*. Springer. Chapter 4 (Type-Based Analysis).

### Discussion Questions

1. Rust's ownership system prevents use-after-free bugs at compile time. What is the compile-time cost of this guarantee? How does it affect the expressiveness of the language?
2. TypeScript uses gradual typing to add optional type annotations to JavaScript. Does gradual typing provide the same safety guarantees as a fully statically-typed language? What are the holes?
3. Dependent types allow proving program properties in the type system. Why aren't all mainstream languages dependent? What are the practical barriers?

### Practice Problems

1. **Type checking**: Given the environment `{x: int, y: float, f: int → float}`, type-check the expression `f(x) + y`. Show all inference rule applications.
2. **Type inference**: Infer the type of `λf. λx. f(f(x))` using Algorithm W. Show the type variable assignments and unification steps.
3. **Subtyping**: Given `Cat ≤ Animal`, `Dog ≤ Animal`, and `Animal ≤ Object`, which of the following are valid subtyping relationships? (a) `List<Cat> ≤ List<Animal>`, (b) `List<Animal> ≤ List<Cat>`, (c) `Function<Animal, Cat> ≤ Function<Cat, Animal>`.

---

ᛉ **Lecture 6: Intermediate Representations — The Compiler's Common Tongue**

**Course:** CS302 — Compiler Design & Code Generation  
**Degree:** Bachelor of Science in Computer Science, 2040

---

### Overview

The intermediate representation (IR) is the compiler's lingua franca — the common language shared between the front end and the back end. A well-designed IR enables language-independent optimization and retargetable code generation. This lecture covers the major IR forms, their properties, and the trade-offs between expressiveness and optimizability.

### Three-Address Code

The simplest IR is three-address code (TAC), where each instruction has at most one operator and at most three operands:

```
t1 = b * c
t2 = a + t1
x = t2
if x < 10 goto L1
t3 = x - 1
y = t3
goto L2
L1: y = x
L2: ...
```

Properties: Simple, easy to generate, easy to optimize. But unstructured (goto-heavy) and does not preserve high-level information.

### Static Single Assignment (SSA)

SSA form requires that each vari