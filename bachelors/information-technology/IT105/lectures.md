# IT105: Programming for IT
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4  
**Description:** Programming for IT (Python, Bash, PowerShell)

---

## Lectures

ᚠ **Lecture 1: The IT Programmer's Mindset: Scripting vs. Software Engineering**

**Course:** IT105 — Programming for IT  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

This opening lecture establishes the intellectual framework for IT programming: a discipline distinct from software engineering in its goals, constraints, and aesthetic. Where software engineers build products for external users, IT programmers write scripts for internal operations—automation, monitoring, remediation, and orchestration. The IT programmer's code is often ephemeral, running once and discarding; it operates in hostile environments where assumptions fail; it must be comprehensible to colleagues at 3 AM during an incident. By 2040, the distinction has sharpened: software engineering has embraced formal methods and type theory, while IT programming has retained its pragmatic, quick-and-dirty ethos, albeit with modern tools for safety and reproducibility.

### Key Topics

- The IT programmer as infrastructure engineer: goals, constraints, and values
- Scripting versus application development: lifecycle, maintenance, and quality standards
- The REPL-driven workflow: exploration before implementation
- Readability and debuggability as primary virtues in operational code
- The 2040 IT toolchain: Jupyter notebooks, GitHub Copilot, and local LLM assistants

### Lecture Notes

The programmer who maintains infrastructure faces a different epistemic situation than the programmer who builds products. The product developer knows, or can specify, the inputs their code will receive. The IT programmer cannot: their scripts ingest log files of unknown format, interact with APIs that change without warning, and execute on systems with idiosyncratic configurations. This fundamental uncertainty shapes every aspect of IT programming, from error handling (defensive, comprehensive) to testing (often impractical, replaced by staging and canary execution) to documentation (inline comments explaining why, not just what).

The distinction between **scripting** and **software engineering** is not merely one of scale or language. A 10,000-line Bash script is still a script; a 500-line Python module with unit tests, type hints, and CI/CD is verging on software engineering. The distinction lies in the relationship between code and context. Scripts are tightly coupled to their execution environment: they assume particular directory structures, environment variables, installed tools, and privilege levels. Software engineering seeks decoupling: abstraction layers, dependency injection, configuration management. The IT programmer must navigate between these poles, writing scripts that are sufficiently robust for production but sufficiently simple for rapid modification during incidents.

The **REPL-driven workflow** (Read-Eval-Print Loop) is the IT programmer's primary mode of engagement. Rather than writing a complete script and then executing it, the IT programmer explores interactively: testing a regex against a log sample, querying a database to understand its schema, experimenting with API endpoints to discover their behavior. Python's interpreter, Bash's command line, and PowerShell's console all serve as exploratory tools. By 2040, this workflow has been enhanced by **Jupyter notebooks** (for documented exploration) and **AI pair programmers** (for suggesting transformations based on natural language descriptions). The lecture emphasizes that exploration must be followed by consolidation: working code in a REPL or notebook must be extracted, cleaned, and committed before it becomes operational.

**Readability and debuggability** are the supreme virtues of IT code. In a crisis, the on-call engineer must understand a script's behavior within minutes, not hours. This demands: clear variable names (not `x` and `y` but `failed_login_count` and `target_host`), explicit error messages (not "Error 500" but "Database connection to prod-db-01 timed out after 30s"), modular structure (functions with single responsibilities), and comprehensive logging (every significant action recorded with timestamp, context, and outcome). The 2034 *Yggdrasil Incident Response Review* identified unreadable scripts as a contributing factor in 23% of extended outages; the department's response was the **Rúnar Readability Standard**, a set of mandatory style guidelines for all operational code.

The **2040 IT toolchain** reflects the integration of AI assistance into scripting workflows. Local large language models (LLMs), running on hardware like the Dellingr Node v3, provide code completion, error explanation, and transformation suggestions without leaking data to cloud providers. GitHub Copilot, evolved from its 2021 introduction, now understands infrastructure contexts: given a Terraform configuration, it suggests security improvements; given a Bash script, it identifies portability issues. The lecture warns against over-reliance: AI-generated code may be syntactically correct but operationally dangerous (e.g., suggesting `rm -rf /` variations, or generating SQL without parameterized queries). The IT programmer must remain the responsible agent, using AI as a tool rather than an oracle.

### Required Reading

- Raymond, E. S. (2003). *The Art of Unix Programming*. Addison-Wesley. Chapters 1 ("Philosophy") and 11 ("Documentation").
- Limoncelli, T. A., Hogan, C. J., & Chalup, S. R. (2014). *The Practice of System and Network Administration* (3rd Edition). Addison-Wesley. Chapter 12 ("Automation").
- Yggdrasil IT Guild (2034). "The Rúnar Readability Standard: Style Guidelines for Operational Code." *UoY IT Operations Manual* v7.2.
- Chen, J., & Freyjasdottir, R. G. (2038). "AI Pair Programming in Critical Infrastructure: Benefits, Risks, and Verification Protocols." *Journal of Yggdrasil Systems Administration*, 15(2), 112–129.
- PowerShell Documentation (2040). "The Unix Philosophy in a Windows World: Designing Cross-Platform Scripts." Microsoft Learn.

### Discussion Questions

1. The IT programmer cannot know all possible inputs in advance. Does this epistemic uncertainty justify weaker testing practices than software engineering, or does it demand stronger defensive programming?
2. A 10,000-line Bash script is still a script by definition, but at what point does a script become unmaintainable? What criteria should govern the decision to rewrite a script in a more structured language?
3. AI pair programmers suggest code based on statistical patterns. What categories of operational errors are AI-generated scripts particularly prone to, and why?
4. The Rúnar Readability Standard prioritizes debuggability over elegance. Is there a tension between these goals, or can readable code also be elegant?

### Practice Problems

- Review three scripts from your own IT experience (or from the UoY script repository). Evaluate each against the Rúnar Readability Standard and produce a revised version with improved naming, error handling, and logging.
- Conduct a 30-minute REPL-driven exploration of a system you do not control (e.g., a public API or a shared server). Document your exploration in a Jupyter notebook, then extract the working code into a reusable script.

---

ᚢ **Lecture 2: Python for System Administration: os, subprocess, pathlib, and argparse**

**Course:** IT105 — Programming for IT  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Python has been the lingua franca of system administration since the early 2000s, and by 2040 it remains the default choice for IT scripting despite competition from Go, Rust, and Julia. This lecture covers the Python standard library modules that form the foundation of system administration scripts: filesystem operations, process management, path manipulation, and command-line interfaces. Students will learn to write scripts that are portable across Unix and Windows, handle errors gracefully, and integrate with the broader Python ecosystem.

### Key Topics

- Filesystem operations with `os` and `pathlib`: portability across platforms
- Process management with `subprocess`: running external commands safely
- Command-line interfaces with `argparse`: user-friendly, documented CLIs
- Environment and configuration: `os.environ`, `configparser`, and dotenv files
- Python packaging for IT scripts: virtual environments, dependencies, and distribution

### Lecture Notes

Python's dominance in IT scripting is not accidental. Its syntax is readable by non-programmers (a critical feature for teams with mixed skill levels), its standard library is comprehensive, and its ecosystem includes libraries for every conceivable infrastructure task. By 2040, Python 4 (released 2032) has addressed the performance limitations of CPython through a JIT compiler and optional static typing, but the core language remains recognizably the descendant of Guido van Rossum's 1991 creation. The lecture focuses on the standard library modules that every IT Python programmer must master.

The **`os` module** provides low-level operating system interfaces: file and directory operations, process management, and environment variables. While powerful, `os` functions are often platform-specific: `os.fork()` exists only on Unix, while `os.startfile()` exists only on Windows. The IT programmer must either avoid platform-specific functions or conditionally use them. The lecture demonstrates safe patterns: checking `os.name` or `sys.platform` before using platform-specific features, and preferring cross-platform alternatives where available. The **`pathlib` module**, introduced in Python 3.4 and enhanced through the 2020s, provides an object-oriented approach to path manipulation that is inherently cross-platform. A `Path` object behaves correctly whether instantiated on Windows (`Path('C:/Users/admin')`) or Unix (`Path('/home/admin')`), handling separator differences, case sensitivity, and drive letters transparently. By 2040, `pathlib` has largely superseded `os.path` in new code.

The **`subprocess` module** is the modern replacement for the deprecated `os.system`, `os.popen`, and `commands` modules. It provides a safe and flexible interface for running external programs, capturing their output, and managing their lifecycle. The lecture emphasizes **security**: never pass unsanitized user input to `subprocess` calls, as this creates command injection vulnerabilities. The `subprocess.run()` function, introduced in Python 3.5, is the recommended high-level interface: it accepts a list of arguments (avoiding shell injection), captures stdout and stderr, and returns a `CompletedProcess` object with return code, stdout, and stderr. For long-running processes, `subprocess.Popen` provides lower-level control with streaming I/O. The 2036 *Shellshock II Incident*, in which a Python script passed unsanitized HTTP headers to `subprocess`, serves as a cautionary tale.

**`argparse`** transforms scripts from hardcoded tools into reusable utilities. A well-designed CLI accepts input files, output destinations, configuration parameters, and verbosity levels as arguments, enabling composition in pipelines and automation in cron jobs. The lecture covers argparse best practices: positional arguments for required inputs, optional arguments (`--flag`) for modifiers, mutually exclusive groups for incompatible options, subparsers for multi-command tools, and help text that explains not just what each option does but why a user might want to use it. By 2040, the `argparse` module has been supplemented by third-party libraries like `click` and `typer` (which use type hints for automatic CLI generation), but `argparse` remains the standard library solution with no external dependencies.

**Environment and configuration management** separates code from deployment-specific settings. Hardcoding database URLs or API keys in scripts is a security anti-pattern; instead, scripts should read configuration from environment variables (for secrets and deployment-specific values), configuration files (for complex settings), or command-line arguments (for user overrides). The lecture demonstrates the **12-Factor App configuration methodology** (popularized by Heroku in 2012, still relevant in 2040): store configuration in environment variables, use `.env` files for local development (loaded via `python-dotenv`), and validate configuration at startup with explicit error messages for missing or invalid values. The `configparser` module reads INI-style configuration files; `tomllib` (Python 3.11+) reads TOML files; `json` reads JSON files. The choice depends on team conventions and the complexity of the configuration.

**Python packaging for IT scripts** ensures reproducibility. A script that runs on one machine may fail on another due to missing dependencies or version incompatibilities. The lecture covers `venv` (virtual environments), `requirements.txt` (pinned dependency versions), and `pip` (installation). For distribution, `zipapp` creates single-file executables from Python packages, and `shiv` (from LinkedIn) creates self-contained executables with bundled dependencies. By 2040, `uv` (the Rust-based Python package manager) has largely replaced `pip` and `venv` for performance-critical workflows, but the concepts remain the same.

### Required Reading

- Reitz, K., & Schlusser, T. (2016). *The Hitchhiker's Guide to Python*. O'Reilly. Chapters 4 ("Writing Great Code") and 10 ("System Administration").
- Python Documentation (2040). *The Python Standard Library: os, pathlib, subprocess, argparse*. Python Software Foundation.
- Wouters, T. (2032). "Python 4: What's New for System Administrators." *PyCon 2032 Keynote*.
- Yggdrasil Security Team (2036). "The Shellshock II Incident: Command Injection in Python Scripts." *UoY Security Bulletin* 2036-04.
- Wirth, N. (2012). "The 12-Factor App." Heroku. (Classic methodology, updated 2030.)

### Discussion Questions

1. `pathlib` is object-oriented and cross-platform; `os.path` is procedural and requires manual platform handling. Why do some experienced Python programmers still prefer `os.path` for simple scripts?
2. `subprocess.run()` is safer than `os.system()` because it accepts argument lists rather than shell strings. But `subprocess.run("cmd " + user_input, shell=True)` reintroduces the vulnerability. What coding standards or linters can prevent this pattern?
3. The 12-Factor methodology recommends storing all configuration in environment variables. For a script with 20 configuration parameters, is this practical, or do configuration files become necessary at some complexity threshold?
4. `uv` is significantly faster than `pip` for package resolution and installation. For IT scripts that are deployed to hundreds of machines, does the performance difference justify migrating from the standard toolchain?

### Practice Problems

- Write a Python script that recursively searches a directory tree for files matching a pattern, reports their sizes, and optionally deletes files older than a specified age. Use `pathlib`, `argparse`, and proper error handling. Ensure the script works on both Linux and Windows.
- Create a Python tool that wraps `subprocess` to execute a command on multiple remote hosts via SSH. Accept host list, command, timeout, and parallelism level as arguments. Handle connection failures gracefully and produce a summary report.

---

ᚦ **Lecture 3: Bash and the Unix Philosophy: Pipelines, Redirection, and Text Processing**

**Course:** IT105 — Programming for IT  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Bash remains the default shell for Unix-like systems in 2040, and fluency in Bash scripting is non-negotiable for IT professionals. This lecture covers the Unix philosophy—small tools that do one thing well, composed via pipelines—as the intellectual foundation of Bash scripting. Students will learn to write robust shell scripts, process text streams with `awk`, `sed`, and `grep`, and construct pipelines that solve complex data processing problems without writing a single line of Python.

### Key Topics

- The Unix philosophy: composability, text streams, and the power of pipelines
- Bash scripting fundamentals: variables, conditionals, loops, functions, and arrays
- Text processing tools: grep, sed, awk, cut, sort, uniq, and jq
- Redirection and process substitution: `<`, `>`, `>>`, `|`, `<()`, and `>()`
- Shell scripting best practices: shellcheck, quoting, and error handling with `set -euo pipefail`

### Lecture Notes

Doug McIlroy, the inventor of Unix pipes, articulated the Unix philosophy in 1978: "This is the Unix philosophy: Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is the universal interface." By 2040, this philosophy has been challenged by binary data formats (Protobuf, Parquet, Avro) and API-centric workflows, but it remains the dominant paradigm for Unix system administration. The IT professional who can compose `ps`, `grep`, `awk`, and `sort` into a one-liner that diagnoses a performance problem will always be more efficient than the colleague who writes a 50-line Python script for the same task.

**Bash scripting fundamentals** must be mastered at a level that permits reading and modifying existing scripts, even if new scripts are written in Python. The lecture covers: variable assignment and expansion (the critical distinction between `$var` and `"$var"` for word splitting), arithmetic expansion (`$(( ))`), conditionals (`if`, `case`), loops (`for`, `while`, `until`), functions (local variables with `local`), and arrays (indexed and associative, introduced in Bash 4.0). Special attention is given to **quoting**: the difference between single quotes (no expansion), double quotes (variable expansion but no word splitting), and unquoted (word splitting and glob expansion). The 2033 *Globbing Disaster* at UoY—in which an unquoted variable containing a wildcard deleted an entire filesystem—serves as a permanent reminder to quote rigorously.

**Text processing tools** are the Unix programmer's power tools. `grep` searches text using regular expressions; `sed` performs stream editing (substitution, deletion, insertion); `awk` is a complete text-processing language with variables, conditionals, loops, and associative arrays; `cut` extracts columns; `sort` and `uniq` aggregate and deduplicate; `jq` (the modern addition) queries and transforms JSON. The lecture demonstrates how these tools compose in pipelines: extract failed login attempts from a log (`grep`), parse the timestamp and IP (`awk`), count occurrences per IP (`sort | uniq -c`), and format as JSON (`jq`). By 2040, `jq` has become as essential as `grep` for IT work, given the ubiquity of JSON in APIs and configuration files.

**Redirection and process substitution** extend the pipeline concept. Redirection (`<` for input, `>` for output, `>>` for append) connects files to file descriptors. Process substitution (`<(command)` and `>(command)`) treats the output or input of a command as a file, enabling pipelines that would otherwise require temporary files. The lecture covers file descriptors 0 (stdin), 1 (stdout), and 2 (stderr), and the redirection patterns for combining and separating them: `2>&1` (merge stderr into stdout), `>file 2>&1` (redirect both to file), and `|&` (pipe both stdout and stderr). The 2040 Bash 6.0 release introduces structured stderr (tagged error streams), but adoption is incomplete; the lecture covers both classic and modern patterns.

**Shell scripting best practices** have been systematized by the **ShellCheck** project (Koalaman, 2013–present), a static analysis tool that flags quoting errors, unused variables, unreachable code, and POSIX compliance issues. By 2040, ShellCheck is integrated into CI pipelines for all UoY operational repositories. The lecture mandates three defensive settings for every Bash script: `set -e` (exit on error), `set -u` (treat unset variables as errors), and `set -o pipefail` (return the exit code of the first failed command in a pipeline, not the last). Together, these settings catch a majority of common shell scripting errors at runtime. The lecture also covers **trap handlers** for cleanup (`trap 'rm -rf "$tempdir"' EXIT`) and **temporary file creation** with `mktemp`.

### Required Reading

- McIlroy, D. (1978). "Unix Time-Sharing System: Foreword." *The Bell System Technical Journal*, 57(6), 1899–1904.
- Blinn, J. (2020). *The Unix Workbench*. Leanpub. Chapters 3 ("Bash Programming") and 5 ("Unix Tools").
- Koalaman (2040). *ShellCheck: Static Analysis for Bash and Sh Scripts*. Documentation v2.0.
- Yggdrasil IT Operations (2033). "The Globbing Disaster: A Cautionary Tale of Unquoted Variables." *UoY Operations Postmortem* 2033-07.
- `jq` Manual (2040). "A jq Tutorial: Querying and Transforming JSON from the Command Line." jq Documentation.

### Discussion Questions

1. The Unix philosophy privileges text streams as the universal interface. In an era of binary APIs, Protobuf, and encrypted protocols, is the text-stream philosophy obsolete, or has it evolved to accommodate these formats?
2. `set -euo pipefail` catches many errors but can also produce unexpected behavior in complex scripts (e.g., `grep` returning non-zero when no match is found, causing premature exit). How should a script balance safety with the need to handle expected non-zero exit codes?
3. `awk` is a complete programming language disguised as a command-line tool. At what complexity threshold should an `awk` script be rewritten in Python?
4. Process substitution (`<(command)`) is powerful but poorly understood. What are the most common misconceptions, and how do they lead to bugs?

### Practice Problems

- Write a Bash script that analyzes a web server access log. Extract the top 10 client IPs by request count, the top 5 requested URLs, and the distribution of HTTP status codes. Use only standard Unix tools (grep, awk, sort, uniq, cut).
- Take an existing 100-line Bash script from the UoY repository. Run ShellCheck on it, fix all warnings, and add `set -euo pipefail`. Document which warnings were most surprising.

---

ᚨ **Lecture 4: PowerShell and Object-Oriented Shell Scripting**

**Course:** IT105 — Programming for IT  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

PowerShell, released by Microsoft in 2006 and open-sourced in 2016, introduced a radical innovation to shell scripting: the pipeline passes objects, not text. By 2040, PowerShell Core (the cross-platform version) is the standard shell for Windows administration and a credible alternative on Linux and macOS. This lecture covers PowerShell's object pipeline, its cmdlet design, its remoting capabilities, and its integration with .NET and modern APIs. Students will learn to write cross-platform PowerShell scripts that leverage the best of both object-oriented and functional programming paradigms.

### Key Topics

- The object pipeline: structured data between commands
- Cmdlet design: verbs, nouns, parameters, and pipeline binding
- Remoting: WinRM, SSH, and Invoke-Command for distributed administration
- Desired State Configuration (DSC): declarative infrastructure management
- PowerShell and APIs: REST, GraphQL, and gRPC invocation

### Lecture Notes

Jeffrey Snover's Monad Manifesto (2002), the founding document of PowerShell, identified a fundamental limitation of Unix shells: text pipelines require every command to parse and re-parse data, losing structure and type information at each step. A command that outputs process information as text forces the next command to parse columnar output with regex; if the output format changes, the parser breaks. PowerShell solves this by passing **.NET objects** through the pipeline, preserving properties, methods, and types. A `Get-Process` cmdlet outputs `System.Diagnostics.Process` objects; `Where-Object` filters by property without parsing; `Select-Object` extracts properties by name; `Export-Csv` serializes to CSV with correct headers. This object pipeline is PowerShell's defining feature and its primary advantage over text-based shells.

**Cmdlet design** follows a strict naming convention: **Verb-Noun**, where the verb is drawn from an approved list (Get, Set, New, Remove, Start, Stop, Test, etc.) and the noun describes the resource. This convention enables **discoverability**: the command `Get-Command -Verb Get -Noun *Service*` finds all commands that retrieve service information. Parameters are strongly typed (`[string]`, `[int]`, `[DateTime]`, `[switch]`) and support pipeline binding by value or by property name. The lecture demonstrates how to write a custom cmdlet in C# or PowerShell classes, including parameter sets (mutually exclusive parameter combinations), validation attributes (`[ValidateNotNullOrEmpty]`, `[ValidateRange]`), and help documentation.

**PowerShell remoting** enables administration of distributed systems from a single console. The original remoting protocol, WinRM (Windows Remote Management, based on WS-Management), remains dominant in Windows environments. By 2040, PowerShell remoting also supports **SSH transport** (via OpenSSH, included in Windows since 2018), enabling remoting to Linux and macOS targets. The `Invoke-Command` cmdlet executes script blocks on remote machines, returning deserialized objects to the local session. The lecture covers **sessions** (`New-PSSession`, persistent connections for multiple commands), **credssp** (credential delegation for multi-hop authentication), and **Just Enough Administration (JEA)**—role-based endpoint configurations that restrict remote users to specific commands, implementing the principle of least privilege.

**Desired State Configuration (DSC)**, introduced in PowerShell 4.0 (2013) and significantly revised in DSC v3 (2029), provides a declarative model for infrastructure management. Rather than writing imperative scripts that install software and configure settings, the administrator writes a **configuration document** specifying the desired state: "Ensure IIS is installed," "Ensure the firewall rule exists," "Ensure the service is running." DSC compares the desired state to the actual state and applies only the necessary changes. By 2040, DSC has converged with the cross-platform **Azure Automanage** and **Terraform** ecosystems; the lecture covers DSC's role in a modern GitOps workflow, where configuration documents are stored in Git and applied automatically by CI/CD pipelines.

**PowerShell and APIs** reflect the dominance of REST and GraphQL in 2040 infrastructure. The `Invoke-RestMethod` and `Invoke-GraphQL` cmdlets (the latter added in PowerShell 7.4) provide native support for HTTP APIs, with automatic JSON serialization and deserialization. The lecture demonstrates querying a cloud provider's API, transforming the response with PowerShell's object pipeline, and piping the result to `Set-Content` or `Out-GridView`. For gRPC services (increasingly common for internal microservices), the `Grpc.Tools` PowerShell module generates client cmdlets from `.proto` files, enabling typed invocation of remote procedures. The 2038 *PowerShell as API Glue* paper by the UoY Windows Infrastructure Team documented how 80% of UoY's cloud orchestration is implemented in PowerShell scripts that compose REST, GraphQL, and gRPC calls.

### Required Reading

- Snover, J. (2002). "Monad Manifesto." Microsoft. (Foundational document, reprinted in *PowerShell Documentation* 2040.)
- Holmes, L., & Hicks, J. (2022). *PowerShell Scripting and Toolmaking*. Manning. Chapters 2–4.
- Microsoft (2040). *PowerShell Documentation: Remoting, DSC, and API Invocation*. Microsoft Learn.
- Yggdrasil Windows Infrastructure Team (2038). "PowerShell as API Glue: Orchestrating Multi-Protocol Cloud Workflows." *UoY Windows Engineering Report* 2038-03.
- Donovan, S., et al. (2029). *Desired State Configuration v3: Cross-Platform Declarative Management*. Microsoft Press.

### Discussion Questions

1. PowerShell's object pipeline preserves structure but requires all commands in the pipeline to understand the same object types. Does this create a tighter coupling between commands than Unix text pipelines, or does strong typing prevent the format-change fragility of text parsing?
2. DSC's declarative model is elegant but can be opaque when things go wrong. How should an administrator debug a DSC configuration that fails to converge?
3. PowerShell remoting over SSH enables cross-platform administration, but SSH and WinRM have different security models. What are the trade-offs between these transports for a mixed Windows/Linux environment?
4. `Invoke-GraphQL` added native GraphQL support in 2034. For IT scripts that interact with multiple APIs, is GraphQL's request flexibility worth the added complexity compared to REST?

### Practice Problems

- Write a PowerShell script that queries the Azure REST API for all virtual machines in a subscription, filters for those with public IP addresses, and exports the results to CSV. Handle authentication via managed identity and paginated responses.
- Create a DSC configuration that ensures a Windows server has IIS installed, a specific website configured, and the firewall open on port 443. Test the configuration in a local VM and document any drift detected.

---

ᚱ **Lecture 5: Regular Expressions: Pattern Matching for Log Analysis and Data Extraction**

**Course:** IT105 — Programming for IT  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Regular expressions are the Swiss Army knife of text processing—a compact, expressive language for describing patterns in strings. This lecture covers regex syntax, engine mechanics, and practical application to IT tasks: parsing log files, extracting fields from unstructured data, validating input formats, and filtering large datasets. By 2040, regex remains indispensable despite advances in natural language processing; no LLM can match the determinism and efficiency of a well-crafted pattern.

### Key Topics

- Regex syntax: literals, character classes, quantifiers, anchors, and groups
- Engine mechanics: NFA vs. DFA, backtracking, and catastrophic complexity
- Practical patterns: IP addresses, email validation, log parsing, and URI extraction
- Regex in Python, Bash, and PowerShell: syntax variations and engine differences
- Performance: compilation, caching, and avoiding ReDoS (Regular Expression Denial of Service)

### Lecture Notes

The theoretical foundation of regular expressions was laid in the 1950s by Stephen Kleene, who formalized **regular languages** as the class of strings recognizable by finite automata. In 1968, Ken Thompson implemented the first practical regex engine for the QED editor, and by 2040, regex engines are embedded in virtually every text-processing tool. Yet the gap between theory and practice remains significant: modern "regex" includes features (backreferences, lookahead, lookbehind) that exceed the theoretical definition, and engine implementations vary in semantics and performance. The IT programmer must understand these variations to write patterns that behave predictably across tools.

**Regex syntax** begins with literals (`abc` matches the exact string) and character classes (`[a-z]` matches any lowercase letter, `\d` matches any digit). Quantifiers specify repetition: `?` (zero or one), `*` (zero or more), `+` (one or more), `{n,m}` (between n and m). Anchors constrain position: `^` (start of string), `$` (end of string), `\b` (word boundary). Groups capture submatches: `(\d{1,3})\.(\d{1,3})` captures octets of an IP address. By 2040, the PCRE (Perl Compatible Regular Expressions) syntax is the de facto standard, supported by Python's `re` module, `grep -P`, and PowerShell's `-match` operator. The lecture provides a pattern reference card and walks through the construction of increasingly complex patterns.

**Engine mechanics** determine performance and behavior. The two dominant implementations are **NFA (Non-deterministic Finite Automaton)** and **DFA (Deterministic Finite Automaton)**. NFA engines (used by PCRE, Python, and most modern tools) support backreferences and backtracking but can exhibit exponential time complexity on certain inputs. DFA engines (used by `awk`, `grep` without `-P`, and Go's `regexp` package) guarantee linear time but lack backreferences and some advanced features. The lecture demonstrates **catastrophic backtracking**: the pattern `(a+)+$` applied to a string of 'a's followed by 'b' forces the NFA to explore exponentially many partitionings before failing. This is the basis of **ReDoS (Regular Expression Denial of Service)**, a vulnerability in which attacker-controlled input triggers super-linear regex evaluation.

**Practical patterns** are the heart of the lecture. Students learn to construct and validate patterns for common IT tasks: IPv4 addresses (`^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$`), email addresses (RFC 5322-compliant, surprisingly complex), MAC addresses, URIs, timestamps (ISO 8601), and log line formats (Apache Combined Log Format, syslog). The lecture emphasizes that regex is a **parsing** tool, not a **validation** tool: a pattern that matches an email address does not guarantee the address exists or is deliverable. For validation, regex should be followed by semantic checks (DNS lookup, SMTP handshake, database query).

**Regex in Python, Bash, and PowerShell** varies in syntax and capability. Python's `re` module supports PCRE with Python-specific extensions (named groups `(?P<name>...)`, verbose mode `re.VERBOSE`). Bash's `[[ $var =~ regex ]]` supports extended regex (ERE) but not PCRE features like lookahead. PowerShell's `-match` operator uses the .NET regex engine, which is PCRE-like but with .NET-specific extensions (balancing groups, right-to-left matching). The lecture provides a cross-reference table and warns against the common error of using PCRE syntax in a non-PCRE context.

**Performance optimization** is critical for IT scripts that process gigabytes of logs. The lecture covers: **compilation** (`re.compile()` in Python caches the compiled pattern), **anchoring** (patterns anchored with `^` or `$` enable engine optimizations), **atomic groups** (`(?>...)` prevents backtracking into the group), and **possessive quantifiers** (`++`, `*+` match greedily without backtracking). The 2035 *ReDoS Attack on Government Infrastructure* report documented a 72-hour outage caused by a single unoptimized regex in a log analysis script; the lecture analyzes the offending pattern and demonstrates the fix.

### Required Reading

- Friedl, J. E. F. (2006). *Mastering Regular Expressions* (3rd Edition). O'Reilly. Chapters 1–4.
- Kleene, S. C. (1956). "Representation of Events in Nerve Nets and Finite Automata." *Automata Studies*, 34, 3–41.
- OWASP (2035). *Regular Expression Denial of Service (ReDoS) Cheat Sheet*. OWASP Foundation.
- Yggdrasil Security Team (2035). "The 72-Hour ReDoS Outage: Root Cause and Remediation." *UoY Security Postmortem* 2035-09.
- Python Documentation (2040). *The re Module: Regular Expression Operations*. Python Software Foundation.

### Discussion Questions

1. Modern regex includes features (backreferences, lookahead) that exceed the formal definition of regular languages. Does this mean "regex" is a misnomer, or has the term simply evolved to encompass a broader class of pattern matchers?
2. DFA engines are faster and safer but less expressive. For IT log analysis, is the expressiveness of NFA worth the ReDoS risk, or should DFA engines be preferred for production scripts?
3. Email validation is often attempted with regex, but RFC 5322 permits addresses that no practical regex can fully validate. What is the appropriate role of regex in email validation, and what should supplement it?
4. The 2035 ReDoS outage was caused by a regex in a log analysis script. What organizational measures (code review, testing, linting) could have prevented this vulnerability from reaching production?

### Practice Problems

- Construct a regex that matches valid IPv4 addresses, MAC addresses, and ISO 8601 timestamps. Test each against a corpus of 100 valid and 100 invalid examples. Measure execution time and identify any false positives or false negatives.
- Analyze a 1GB web server log file using Python's `re` module. Extract all unique client IPs, requested URLs, and HTTP status codes. Optimize your regex for speed and compare execution time against a naive implementation.

---

ᚲ **Lecture 6: File and Data Processing: CSV, JSON, YAML, and XML in Practice**

**Course:** IT105 — Programming for IT  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Data formats are the dialects of infrastructure. This lecture covers the structured data formats that dominate IT operations in 2040: CSV (the eternal legacy), JSON (the API standard), YAML (the configuration king), and XML (the enterprise survivor). Students will learn to read, write, validate, and transform data in each format, with attention to edge cases, security implications, and performance characteristics. The lecture also introduces streaming and incremental processing for datasets too large to fit in memory.

### Key Topics

- CSV: dialects, escaping, headers, and the csv module's limitations
- JSON: schema validation, streaming parsers, and security (Billion Laughs, nested bombs)
- YAML: anchors, aliases, tags, and the parsing complexity that led to YAML bombs
- XML: DOM vs. SAX vs. streaming, XPath, and XSLT transformations
- Streaming processing: iterators, generators, and memory-bound processing

### Lecture Notes

The choice of data format is never neutral. Each format encodes assumptions about structure, readability, performance, and tooling. CSV assumes tabular data; JSON assumes object graphs; YAML assumes human authorship; XML assumes document structure. The IT programmer must select the appropriate format for each task and understand the failure modes of each.

**CSV (Comma-Separated Values)** is the oldest and most problematic format. Despite its name, the delimiter is not always a comma (tabs, semicolons, and pipes are common variants). Quoting rules vary: RFC 4180 specifies double-quote escaping (`""`), but Excel uses backslash escaping in some locales. Newlines within fields break naive line-oriented parsers. The Python `csv` module handles most dialects correctly but cannot stream (it reads the entire file into memory for parsing). The lecture demonstrates **csvkit** (a suite of command-line tools for CSV processing) and **xsv** (a Rust-based CSV processor that handles gigabyte-scale files). By 2040, **CSV on the Web** (W3C standard, 2035) adds metadata files that specify dialect, encoding, and column types, enabling robust automated parsing.

**JSON (JavaScript Object Notation)**, standardized in RFC 8259 (2017), is the dominant format for APIs and configuration. Its simplicity (objects, arrays, strings, numbers, booleans, null) makes it easy to parse and generate, but this simplicity also creates vulnerabilities. The **Billion Laughs attack** (2003, XML-based but applicable to YAML and JSON with nested objects) exploits exponential expansion by defining deeply nested self-references that consume memory when expanded. JSON itself does not support references, but YAML (a superset of JSON) does. The **JSON nested bomb** creates deeply nested arrays (`[[[[...]]]]`) that crash parsers with limited recursion depth. The lecture covers parser hardening: recursion limits, memory limits, and schema validation with JSON Schema (draft 2020-12, updated 2035). By 2040, the **JSDL (JSON Schema Definition Language)** provides static type checking for JSON data, catching mismatches at validation time rather than runtime.

**YAML (YAML Ain't Markup Language)**, introduced in 2001, is the default format for configuration files (Ansible playbooks, Kubernetes manifests, GitHub Actions workflows). Its readability (significant indentation, comments, human-friendly syntax) made it popular, but its parsing complexity has been a persistent source of bugs. The **YAML bomb** (alias explosion) uses anchors and aliases to create exponential memory expansion: `&a [*a, *a, *a]` triples on each dereference. The ** Norway Parser Incident** (2031)—in which a YAML parser misinterpreted a country's name as a boolean value due to the unquoted string `NO`—demonstrated the dangers of loose typing. By 2040, **StrictYAML** (a subset of YAML that forbids aliases, tags, and implicit typing) is the recommended format for security-critical configuration. The lecture demonstrates `yamllint` (static analysis for YAML files) and `yq` (the YAML equivalent of `jq`).

**XML (eXtensible Markup Language)**, despite predictions of its demise, remains entrenched in enterprise systems (SOAP web services, Microsoft Office documents, configuration files for legacy applications). The lecture covers three parsing models: **DOM** (Document Object Model, loads the entire document into a tree structure), **SAX** (Simple API for XML, event-driven streaming), and **StAX** (Streaming API for XML, pull-based streaming). For IT scripts processing large XML files, SAX or StAX are essential to avoid memory exhaustion. **XPath** provides a query language for selecting nodes; **XSLT** provides a transformation language for converting between XML formats. By 2040, **XML Schema 2.0** supports data types and constraints that rival JSON Schema in expressiveness.

**Streaming and incremental processing** are essential for datasets that exceed available memory. Python's `yield` keyword enables generator functions that produce one record at a time; the `json` module's `JSONDecoder.raw_decode` enables incremental JSON parsing; `ijson` provides a truly streaming JSON parser that yields objects as they are encountered. The lecture implements a streaming log processor that reads multi-gigabyte files in constant memory, demonstrating that memory-bound processing is not merely an optimization but a requirement for production-scale IT operations.

### Required Reading

- W3C (2035). *CSV on the Web: A Primer*. W3C Working Group Note.
- JSON Schema Organization (2035). *JSON Schema Draft 2035-07: Core, Validation, and Hyper-Schema*.
- StrictYAML Documentation (2040). "Why StrictYAML? Security, Simplicity, and Predictability."
- Harold, E. R. (2004). *Processing XML with Java: A Guide to SAX, DOM, JDOM, JAXP, and TrAX*. Addison-Wesley. Chapters 2–3 (SAX and DOM).
- Yggdrasil Security Team (2031). "The Norway Parser Incident: YAML Typing and National Security." *UoY Security Bulletin* 2031-12.

### Discussion Questions

1. CSV is ancient, buggy, and ill-specified, yet it persists. What social and technical factors explain its longevity, and what would be required to displace it?
2. JSON's simplicity is its greatest strength and its greatest weakness. What capabilities (comments, trailing commas, date types) have been proposed for JSON extensions, and why has the standard resisted them?
3. StrictYAML forbids aliases, tags, and implicit typing for security. Does this subset retain enough expressive power for complex configuration, or does it push users back toward full YAML with its attendant risks?
4. XML was declared dead in the 2010s, yet enterprise systems continue to rely on it. Is XML's persistence a symptom of organizational inertia, or does it genuinely serve needs that JSON and YAML cannot meet?

### Practice Problems

- Write a Python script that reads a 10GB CSV file and computes aggregate statistics (sum, mean, max) for specified columns without loading the entire file into memory. Compare execution time and memory usage against a naive implementation.
- Implement a YAML configuration validator using StrictYAML and JSON Schema. Given a Kubernetes-like manifest, validate that required fields are present, types are correct, and no aliases or tags are used.

---

ᚷ **Lecture 7: Network Scripting: HTTP APIs, SSH Automation, and Socket Programming**

**Course:** IT105 — Programming for IT  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

The network is the medium through which modern infrastructure communicates. This lecture covers programmatic network interaction: consuming REST and GraphQL APIs, automating remote systems via SSH, and building low-level network tools with sockets. Students will learn to write scripts that orchestrate distributed systems, transfer data securely, and diagnose network issues from the command line and in code.

### Key Topics

- HTTP and REST APIs: methods, status codes, headers, authentication, and rate limiting
- API clients in Python (`requests`, `httpx`) and PowerShell (`Invoke-RestMethod`)
- SSH automation: `paramiko`, `fabric`, and `ansible` for remote execution
- GraphQL APIs: queries, mutations, subscriptions, and schema introspection
- Socket programming: TCP and UDP sockets for custom protocols and diagnostics

### Lecture Notes

The Hypertext Transfer Protocol (HTTP), standardized in RFC 2616 (1999) and revised in RFC 7230–7235 (2014), remains the foundation of internet communication in 2040. While HTTP/3 (QUIC-based) has displaced HTTP/1.1 for browser traffic, the semantics of HTTP—methods (GET, POST, PUT, DELETE, PATCH), status codes (200 OK, 404 Not Found, 500 Internal Server Error), and headers (Content-Type, Authorization, Cache-Control)—remain unchanged. The IT programmer must understand these semantics to interact with APIs correctly and to debug failures when they occur.

**REST (Representational State Transfer) APIs**, architectural guidelines formalized by Roy Fielding in his 2000 doctoral dissertation, provide a principled framework for API design. Key constraints: statelessness (each request contains all necessary information), cacheability (responses explicitly indicate cacheability), and uniform interface (resources identified by URIs, manipulated via standard methods). By 2040, the OpenAPI Specification (formerly Swagger) has become the standard for documenting REST APIs, enabling automated client generation and contract testing. The lecture demonstrates `requests` (Python's most popular HTTP library) and `httpx` (a modern alternative with async support), covering authentication (Basic, Bearer token, OAuth 2.1, mTLS), pagination (cursor-based, offset-based, link headers), and error handling (retry with exponential backoff, circuit breakers).

**SSH (Secure Shell)** is the primary protocol for remote system administration. Originally designed for secure remote login, SSH has evolved to support port forwarding, file transfer (SFTP, SCP), and tunneling. For IT automation, **Paramiko** (a Python SSH library) provides programmatic access to SSH connections: executing commands, transferring files, and managing SFTP sessions. **Fabric** (built on Paramiko) offers a higher-level API for remote task execution, with parallel execution support and role-based host targeting. **Ansible** (covered in IT206) uses SSH as its transport for agentless configuration management. The lecture demonstrates writing a Fabric-like tool in pure Python, including connection pooling, host key verification, and jump host (bastion) traversal.

**GraphQL**, introduced by Facebook in 2015 and standardized by the GraphQL Foundation in 2030, provides an alternative to REST for API design. Rather than exposing fixed endpoints with predefined responses, GraphQL exposes a single endpoint that accepts queries specifying exactly which fields to return. This eliminates over-fetching (retrieving unnecessary data) and under-fetching (making multiple requests to assemble needed data). The lecture covers GraphQL query syntax, variables, fragments, mutations, and subscriptions (real-time updates via WebSocket). By 2040, GraphQL has become the default for internal microservices APIs, while REST remains dominant for public APIs. The `gql` library (Python) and `Invoke-GraphQL` (PowerShell) provide client implementations.

**Socket programming** provides the foundation for custom network protocols and diagnostic tools. Python's `socket` module exposes the BSD socket API: creating sockets (`socket.socket()`), binding to addresses (`bind()`), listening for connections (`listen()`), accepting connections (`accept()`), and sending/receiving data (`send()`, `recv()`). The lecture implements a simple TCP echo server and client, then extends the server to handle multiple concurrent clients using `select()`, `poll()`, and `asyncio`. For diagnostics, the lecture implements a port scanner (using `socket.connect()` with timeouts) and a custom UDP-based heartbeat protocol. By 2040, asyncio (Python's asynchronous I/O framework) has become the standard for high-concurrency network applications, replacing threaded and select-based approaches.

### Required Reading

- Fielding, R. T. (2000). *Architectural Styles and the Design of Network-based Software Architectures*. Ph.D. dissertation, University of California, Irvine.
- OpenAPI Initiative (2040). *OpenAPI Specification Version 4.0*. OpenAPI Initiative.
- Ylonen, T., & Lonvick, C. (2006). *The Secure Shell (SSH) Protocol Architecture*. RFC 4251.
- GraphQL Foundation (2030). *GraphQL Specification*. Version 2030-06.
- Python Documentation (2040). *The socket Module: Low-Level Networking Interface*. Python Software Foundation.

### Discussion Questions

1. REST's statelessness constraint simplifies scaling but can increase latency (each request must authenticate and authorize independently). What architectural patterns have emerged to mitigate this tension?
2. GraphQL's flexibility is powerful but creates new security challenges (deeply nested queries can exhaust server resources). What query depth and complexity limits are appropriate for production GraphQL APIs?
3. SSH key management at scale is a persistent challenge. What are the trade-offs between password-based, key-based, and certificate-based SSH authentication for an organization with 10,000 servers?
4. Asyncio provides high concurrency but introduces complexity (coroutines, event loops, futures). For an IT script that makes 100 API calls, is asyncio justified, or would a thread pool be simpler and sufficient?

### Practice Problems

- Write a Python script that interacts with a cloud provider's REST API to list all virtual machines, start stopped instances, and tag resources based on naming conventions. Implement OAuth 2.1 authentication, pagination handling, and rate-limit respect.
- Implement a concurrent port scanner in Python using asyncio. Scan the top 1000 TCP ports on a target host, reporting open ports and their detected services. Compare performance against a sequential implementation.

---

ᚹ **Lecture 8: Database Scripting: SQL from Python, ORMs, and Data Migration**

**Course:** IT105 — Programming for IT  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Databases are the persistent memory of infrastructure. This lecture covers programmatic database interaction: writing SQL from scripts, using Object-Relational Mappers (ORMs), performing data migrations, and ensuring transactional integrity. Students will learn to bridge the gap between imperative scripting languages and declarative database systems, with attention to security, performance, and maintainability.

### Key Topics

- SQL fundamentals for IT: SELECT, INSERT, UPDATE, DELETE, JOIN, and aggregate queries
- Python database APIs: DB-API 2.0, `sqlite3`, `psycopg2`, and `mysql-connector`
- ORMs: SQLAlchemy and Django ORM for abstraction and migration management
- Data migration: schema evolution, ETL pipelines, and zero-downtime strategies
- Security: SQL injection prevention, parameterized queries, and least-privilege database users

### Lecture Notes

Structured Query Language (SQL), first standardized in 1986 and revised through SQL:2023 (ISO/IEC 9075), remains the dominant language for relational data management in 2040. Despite the proliferation of NoSQL databases (document, key-value, graph, vector), relational databases (PostgreSQL, MySQL, SQLite, SQL Server) continue to underpin the majority of IT infrastructure. The IT programmer must be fluent in SQL—not at the level of a database administrator, but sufficiently to query, update, and migrate data without introducing errors or security vulnerabilities.

The lecture begins with **SQL fundamentals for IT**: queries that administrators and operators write daily. `SELECT` with `WHERE`, `ORDER BY`, `LIMIT`, and `JOIN` (inner, left, right, full outer); `INSERT`, `UPDATE`, and `DELETE` with transaction boundaries; aggregate functions (`COUNT`, `SUM`, `AVG`, `MAX`, `MIN`) with `GROUP BY` and `HAVING`; and subqueries and Common Table Expressions (CTEs) for complex reporting. The emphasis is on practical patterns: finding duplicate records, identifying orphaned rows, computing running totals, and generating summary reports. By 2040, **window functions** (`ROW_NUMBER()`, `RANK()`, `LEAD()`, `LAG()`) have become standard SQL and are essential for IT reporting tasks.

**Python database APIs** follow the DB-API 2.0 specification (PEP 249), which defines a standard interface for database connectivity: `connect()`, `cursor()`, `execute()`, `fetchall()`, and `commit()`. The lecture covers `sqlite3` (built into Python, ideal for local data and testing), `psycopg2` (the PostgreSQL adapter, the gold standard for production Python database work), and `mysql-connector-python` (the official MySQL driver). For each, the lecture demonstrates connection management (context managers for automatic cleanup), parameterized queries (using `%s` or `?` placeholders), and result set handling (iterating over cursors for large result sets to avoid memory exhaustion).

**ORMs (Object-Relational Mappers)** abstract SQL behind object-oriented APIs, enabling developers to interact with databases using native language constructs rather than raw SQL. **SQLAlchemy**, the dominant Python ORM by 2040, offers two usage modes: the **Core** (expression language that generates SQL) and the **ORM** (full object mapping with relationship handling, lazy loading, and session management). The lecture covers SQLAlchemy 2.0 (released 2023, refined through 2040), including declarative base classes, relationship definitions (`relationship()`, `ForeignKey()`), eager and lazy loading strategies, and the **async extension** (`asyncpg` backend) for non-blocking database access. The Django ORM is covered briefly for students working in Django environments.

**Data migration** is the process of moving data between schemas, databases, or environments. The lecture distinguishes **schema migrations** (altering table structure, handled by tools like Alembic for SQLAlchemy or Django's built-in migrations) from **data migrations** (transforming and transferring data, often requiring custom scripts). For zero-downtime migrations, the lecture covers the **expand-contract pattern**: add a new column or table (expand), dual-write to old and new (contract reads), migrate existing data, switch reads to new, and remove old (contract). This pattern, popularized by the 2012 *Evolutionary Database Design* paper by Martin Fowler and Pramod Sadalage, remains the standard for production database changes in 2040.

**Security** is paramount. **SQL injection** remains the most common database vulnerability, occurring when user input is concatenated into SQL strings rather than passed as parameters. The lecture demonstrates injection attacks (`'; DROP TABLE users; --`) and their prevention via parameterized queries. Beyond injection, the lecture covers **least-privilege database users**: application accounts with only `SELECT`, `INSERT`, `UPDATE`, `DELETE` on necessary tables, not `DROP`, `ALTER`, or `GRANT`. The 2034 *Yggdrasil Database Breach*—in which a compromised application account with excessive privileges allowed an attacker to exfiltrate the entire user database—serves as a cautionary tale.

### Required Reading

- ISO/IEC (2023). *ISO/IEC 9075:2023 Information Technology — Database Languages — SQL*. International Organization for Standardization.
- Beaulieu, A. (2009). *Learning SQL* (2nd Edition). O'Reilly. Chapters 1–8.
- Copeland, R. (2008). *Essential SQLAlchemy*. O'Reilly. (Updated for SQLAlchemy 2.0 in 2032.)
- Fowler, M., & Sadalage, P. J. (2012). "Evolutionary Database Design." *martinfowler.com*.
- Yggdrasil Security Team (2034). "The 2034 Database Breach: Privilege Escalation via Over-Provisioned Application Accounts." *UoY Security Postmortem* 2034-02.

### Discussion Questions

1. Window functions are powerful but can be computationally expensive. For an IT reporting script that runs hourly on a production database, what window function patterns should be avoided or optimized?
2. SQLAlchemy's ORM provides convenience but abstracts SQL in ways that can obscure performance. Under what conditions should an IT programmer prefer raw SQL over an ORM?
3. The expand-contract pattern enables zero-downtime migrations but requires maintaining two schemas simultaneously. What are the operational risks of this dual state, and how long should it persist?
4. Parameterized queries prevent SQL injection, but stored procedures with dynamic SQL inside them can reintroduce the vulnerability. How should organizations audit their database code for this second-order injection risk?

### Practice Problems

- Write a Python script that connects to a PostgreSQL database, queries a table of server metrics, and generates a daily summary report (average CPU, peak memory, disk usage trends). Use `psycopg2` with parameterized queries and proper connection cleanup.
- Design a schema migration for a user database using Alembic. Add a `last_login` timestamp column, backfill it from an audit log table, and ensure the migration can run without locking the users table for more than 5 seconds.

---

ᚺ **Lecture 9: Error Handling, Logging, and Defensive Programming in Scripts**

**Course:** IT105 — Programming for IT  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Operational scripts fail. Networks partition, disks fill, APIs return unexpected responses, and race conditions emerge under load. This lecture covers the defensive programming techniques that transform fragile scripts into resilient infrastructure: comprehensive error handling, structured logging, input validation, and graceful degradation. Students will learn to write scripts that fail safely, report clearly, and recover automatically where possible.

### Key Topics

- Exception handling: try/except/finally, custom exceptions, and exception hierarchies
- Structured logging: log levels, correlation IDs, context propagation, and log aggregation
- Input validation: whitelisting, schema validation, and sanitization
- Graceful degradation: fallback paths, circuit breakers, and degraded mode operation
- Idempotency: ensuring that repeated execution produces the same result

### Lecture Notes

The difference between a prototype and production code is not features but failure modes. A prototype crashes on the first unexpected input; production code handles it, logs it, alerts if necessary, and continues. This lecture treats failure as a first-class concern, integral to the design process rather than an afterthought.

**Exception handling** in Python uses the `try/except/finally` construct, with `else` for code that runs only if no exception occurs. The lecture emphasizes **specificity**: catch the narrowest exception that covers the expected failure (`except FileNotFoundError`, not `except Exception`), and re-raise unexpected exceptions rather than swallowing them. Custom exception hierarchies (`class InfrastructureError(Exception)` with subclasses `NetworkError`, `DatabaseError`, `PermissionError`) enable callers to handle categories of failures without enumerating every possible exception. The `finally` block guarantees cleanup (closing files, releasing locks, disconnecting from databases) regardless of whether an exception occurred. By 2040, Python's `contextlib` module provides `ExitStack` for managing multiple resources and `suppress` for explicitly ignoring specific exceptions.

**Structured logging** replaces ad-hoc `print` statements with machine-parseable, context-rich log records. The Python `logging` module supports structured output via `logging.handlers` and third-party libraries like `structlog` and `python-json-logger`. Each log record should include: timestamp (ISO 8601, UTC), log level (DEBUG, INFO, WARNING, ERROR, CRITICAL), logger name, message, and context (request ID, user ID, host name, operation name). **Correlation IDs** (also called trace IDs) propagate across script boundaries, enabling the reconstruction of multi-step operations from distributed logs. The lecture demonstrates configuring Python's `logging` module to output JSON, integrating with log aggregation systems (Loki, ELK, Splunk), and setting appropriate log levels (DEBUG for development, INFO for normal operation, ERROR for alerts).

**Input validation** is the first line of defense against injection attacks, data corruption, and logic errors. The lecture advocates **whitelisting** over blacklisting: define what inputs are acceptable (e.g., IP addresses matching a CIDR block, usernames matching `[a-z_][a-z0-9_]{2,30}`) and reject everything else. Schema validation (JSON Schema, Pydantic models, Cerberus) provides declarative input checking with automatic error reporting. **Sanitization** removes or escapes dangerous characters from inputs that must be used in sensitive contexts (shell commands, SQL queries, HTML output). The 2036 *Input Validation Failure Report* by the UoY Security Team found that 40% of production scripts lacked any input validation; the department's response was mandatory `pydantic` validation for all scripts accepting external input.

**Graceful degradation** acknowledges that dependencies fail and designs scripts to continue operating with reduced functionality. The **circuit breaker pattern** (popularized by Michael Nygard in *Release It!*, 2007) prevents cascading failures by "opening" when a dependency's error rate exceeds a threshold, directing traffic to a fallback path. For scripts, this means: if the primary database is unreachable, use a read replica; if the API returns 503, retry with backoff and then use cached data; if the monitoring service is down, log locally and backfill later. The lecture implements a simple circuit breaker in Python and demonstrates its use in a multi-dependency script.

**Idempotency** ensures that a script can be run multiple times without causing unintended side effects. This is critical for: configuration management scripts (applying the same configuration twice should not create duplicates), data migration scripts (re-running after a partial failure should not duplicate migrated data), and CI/CD pipelines (retrying a deployment should not redeploy if already at target state). The lecture covers idempotency techniques: existence checks before creation, upserts (`INSERT ... ON CONFLICT` in PostgreSQL, `MERGE` in SQL Server), and state comparison before update. The 2035 *Idempotency Manifesto* by the UoY DevOps Guild declared idempotency a mandatory property of all production scripts.

### Required Reading

- Nygard, M. T. (2007). *Release It! Design and Deploy Production-Ready Software*. Pragmatic Bookshelf. Chapter 4 ("Stability Patterns").
- Python Documentation (2040). *The logging Module: How-To and API Reference*. Python Software Foundation.
- Pydantic Documentation (2040). *Pydantic: Data Validation Using Python Type Hints*. Version 3.0.
- Yggdrasil Security Team (2036). "Input Validation in Operational Scripts: A Postmortem Analysis." *UoY Security Report* 2036-08.
- Yggdrasil DevOps Guild (2035). "The Idempotency Manifesto: Requirements for Production Scripts." *UoY DevOps Standards*.

### Discussion Questions

1. Catching `Exception` is often criticized as too broad, but in a top-level script handler, is there a case for catching `Exception` to prevent crashes while logging the error?
2. Structured logging adds overhead (JSON serialization, field validation). For a script that processes millions of records, is the overhead justified, or should logging be minimized for performance?
3. Whitelist validation is secure but can be user-hostile (rejecting valid inputs that happen to be uncommon). How should a script balance security with usability for configuration inputs?
4. Idempotency requires existence checks that add database queries. For a high-throughput script, what techniques (caching, batching, optimistic locking) can maintain idempotency without excessive overhead?

### Practice Problems

- Write a Python script that accepts user input for a file path, validates that the path is within an allowed directory (preventing directory traversal), and copies the file to a destination. Implement comprehensive error handling with structured logging.
- Design a circuit breaker for a script that calls an external API. Implement open, half-open, and closed states with configurable thresholds. Demonstrate graceful degradation when the API is unavailable.

---

ᚾ **Lecture 10: Testing and Debugging Scripts: Unit Tests, Linters, and Static Analysis**

**Course:** IT105 — Programming for IT  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

Testing operational scripts is often neglected, with the excuse that "it's just a script." This lecture refutes that excuse, demonstrating that scripts benefit from the same testing disciplines as production software—adapted to their unique constraints. Students will learn to write unit tests for scripts, use linters and static analyzers to catch bugs before execution, and debug effectively when things go wrong.

### Key Topics

- Unit testing for scripts: `pytest`, testable design, and mocking external dependencies
- Linting and formatting: `flake8`, `black`, `pylint`, and `shellcheck`
- Static analysis: `mypy` for type checking, `bandit` for security scanning
- Debugging techniques: print debugging, logging, interactive debuggers (`pdb`, `ipdb`)
- Test-driven scripting: writing tests before implementation for critical automation

### Lecture Notes

The argument against testing scripts—that they are too small, too short-lived, or too environment-dependent to warrant the effort—was always weak and has become untenable by 2040. Scripts that modify production databases, restart services, or migrate user data can cause catastrophic damage if flawed. The 2032 *Yggdrasil Script Failure Report* found that 60% of production incidents caused by "simple scripts" could have been prevented by basic unit testing. The lecture treats script testing not as a luxury but as a professional obligation.

**Unit testing for scripts** follows the same principles as application testing but with adjusted expectations. The `pytest` framework, dominant in Python by 2040, provides fixtures for setup and teardown, parameterized tests for multiple inputs, and plugins for coverage (`pytest-cov`) and mocking (`pytest-mock`, `unittest.mock`). The lecture emphasizes **testable design**: scripts should be structured as functions that accept explicit parameters and return values, not as monolithic blocks of top-level code. This enables unit testing without modifying the script's behavior. For scripts that interact with external systems (databases, APIs, filesystems), **mocking** replaces real dependencies with test doubles. The `unittest.mock` module provides `Mock` (arbitrary fake objects), `MagicMock` (with magic methods), and `patch` (temporary replacement of imports).

**Linting and formatting** enforce consistency and catch common errors automatically. `flake8` combines pyflakes (syntax and undefined name checking), pycodestyle (PEP 8 style checking), and mccabe (cyclomatic complexity analysis). `black` (the uncompromising code formatter) reformats code to a consistent style, eliminating style debates in code review. `pylint` provides deeper analysis, including type inference, dead code detection, and refactoring suggestions. For Bash, `shellcheck` (covered in Lecture 3) performs static analysis of shell scripts. For PowerShell, `PSScriptAnalyzer` enforces community best practices. The lecture demonstrates configuring these tools in pre-commit hooks, ensuring that all committed code passes automated checks.

**Static analysis** goes beyond linting to reason about program behavior without execution. **Type checking** with `mypy` verifies that Python code adheres to type annotations, catching category errors (passing a string where an integer is expected) before runtime. By 2040, Python's optional type system (PEP 484, introduced 2015, refined through 2040) supports generics, protocols, and union types, enabling expressive and precise type annotations. **Security scanning** with `bandit` detects common security anti-patterns: hardcoded passwords, use of `eval`, weak cryptographic algorithms, and SQL injection risks. The lecture covers integrating `mypy` and `bandit` into CI pipelines, with failure thresholds that block deployment on critical issues.

**Debugging techniques** range from primitive to sophisticated. **Print debugging** (`print(f"DEBUG: x={x}")`) is often derided but remains effective for quick diagnostics; the lecture advises using `logging.debug()` instead, to enable runtime toggling without code modification. **Interactive debuggers** (`pdb` in Python, `bashdb` for Bash) provide breakpoints, step-by-step execution, variable inspection, and stack trace navigation. The `ipdb` debugger (IPython-enhanced pdb) offers syntax highlighting, tab completion, and magic commands. For remote debugging, `remote-pdb` enables debugging of scripts running on servers via a TCP connection. The lecture demonstrates a complete debugging session: reproducing a bug, setting breakpoints, inspecting state, identifying the root cause, and verifying the fix.

**Test-driven scripting** applies the TDD methodology (red-green-refactor) to operational scripts. While TDD is often associated with application development, it is equally valuable for scripts that implement critical automation. The lecture walks through a TDD example: writing a script that restarts a service only if its memory usage exceeds a threshold. The test is written first (asserting that the script restarts when memory is high and does not when memory is low), then the script is implemented to pass the tests, then the code is refactored for clarity. By 2040, the UoY IT Guild requires TDD for all scripts that modify production state.

### Required Reading

- Okken, B. (2022). *Python Testing with pytest* (2nd Edition). Pragmatic Bookshelf. Chapters 1–4.
- Python Documentation (2040). *unittest.mock — Mock Object Library*. Python Software Foundation.
- mypy Documentation (2040). *mypy: Optional Static Typing for Python*. Version 2.0.
- bandit Documentation (2040). *bandit: Security Linter from the OpenStack Security Project*. PyCQA.
- Yggdrasil IT Guild (2032). "The Script Failure Report: How Untested Scripts Cause Production Incidents." *UoY IT Operations Review*.

### Discussion Questions

1. Testable design requires structuring scripts as functions with explicit parameters. Does this design discipline conflict with the quick-and-dirty ethos of IT scripting, or can the two be reconciled?
2. `black` enforces a single formatting style, eliminating style debates. Does this uniformity improve team productivity, or does it suppress individual expression and creativity?
3. mypy's type checking catches errors but requires writing type annotations. For a script written in 30 minutes to fix an urgent issue, is the annotation overhead justified?
4. TDD requires writing tests before implementation. In an incident response scenario where a script must be deployed within minutes, is TDD feasible, or does it become a post-hoc verification step?

### Practice Problems

- Take a 50-line Python script from the UoY repository that lacks tests. Refactor it for testability, write `pytest` unit tests achieving ≥80% coverage, and integrate `flake8`, `black`, and `mypy` into a pre-commit configuration.
- Debug a provided buggy script using `ipdb`. The script fails intermittently under load. Identify the race condition, fix it, and write a test that reproduces and verifies the fix.

---

ᛁ **Lecture 11: Automation and Scheduling: Cron, Systemd Timers, and CI/CD for Scripts**

**Course:** IT105 — Programming for IT  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

A script that must be run manually is a script that will be forgotten. This lecture covers the automation mechanisms that ensure scripts execute reliably, on schedule, and with proper oversight: cron jobs, systemd timers, CI/CD pipelines, and infrastructure-as-code for scheduling. Students will learn to deploy scripts as automated services, with monitoring, alerting, and failure recovery.

### Key Topics

- Cron: syntax, environment, logging, and the limitations of classic cron
- Systemd timers: calendar and monotonic triggers, dependency management, and logging integration
- CI/CD for scripts: GitHub Actions, GitLab CI, and automated testing on commit
- Infrastructure as Code for scheduling: Ansible cron modules, Terraform, and Kubernetes CronJobs
- Monitoring scheduled tasks: success/failure alerting, run duration tracking, and overlap prevention

### Lecture Notes

Automation is the defining characteristic of mature IT operations. An organization that runs 1,000 servers manually will make mistakes; an organization that automates will make mistakes consistently (and thus detectably). By 2040, the automation landscape has evolved from simple cron jobs to sophisticated orchestration platforms, but the fundamental challenge remains: ensuring that the right code runs at the right time with the right privileges and the right oversight.

**Cron**, the venerable Unix scheduling daemon (introduced in Version 7 Unix, 1979), remains in widespread use. Its syntax—five fields specifying minute, hour, day of month, month, and day of week—is compact but cryptic. The lecture provides a visual cron syntax reference and demonstrates common patterns: every minute (`* * * * *`), every hour at 15 minutes past (`15 * * * *`), every weekday at 9 AM (`0 9 * * 1-5`), and the complex "every 3 hours between 9 AM and 6 PM on weekdays" (`0 9-18/3 * * 1-5`). The lecture also covers cron's limitations: it assumes the system is always running (missed jobs are not executed on boot), it runs with a minimal environment (PATH, HOME, and SHELL may differ from interactive sessions), and it provides no native logging or failure alerting. By 2040, cron is considered legacy for production systems, replaced by systemd timers or orchestrated schedulers.

**Systemd timers** are the modern replacement for cron on Linux systems. A timer unit (`*.timer`) specifies when to trigger a service unit (`*.service`), which defines what to execute. Timers support **calendar events** (cron-like scheduling) and **monotonic events** (time since boot, time since last activation, or time since a specific service started). The lecture demonstrates: a daily backup timer, a timer that runs 10 minutes after boot, and a timer that runs only if the network is available (using `Requires=network-online.target`). Systemd timers integrate with journald: all output is automatically logged with timestamps, and failure notifications can be configured via `OnFailure=` dependencies. By 2040, systemd timers are the default scheduling mechanism for UoY production systems.

**CI/CD for scripts** extends the automation paradigm to code changes. When a script is committed to version control, a CI pipeline should: run linters (`flake8`, `shellcheck`), execute unit tests (`pytest`), perform security scanning (`bandit`, `trivy`), and optionally deploy to a staging environment. GitHub Actions (introduced 2018, dominant by 2025) and GitLab CI provide workflow definitions as YAML files stored in the repository. The lecture demonstrates a complete GitHub Actions workflow for a Python script repository: trigger on push to `main`, run `black --check`, run `pytest` with coverage reporting, run `bandit`, and if all checks pass, deploy the script to production servers via SSH. By 2040, the UoY IT Guild requires CI/CD for all scripts with production impact.

**Infrastructure as Code (IaC) for scheduling** enables version-controlled, reproducible scheduling definitions. Ansible's `cron` module ensures that cron jobs are present with exact specifications, eliminating the drift that occurs when administrators manually edit crontabs. Terraform's `null_resource` with `triggers` can schedule one-off tasks. Kubernetes `CronJob` resources schedule containers to run on a cluster, with automatic pod management, resource limits, and failure handling. The lecture compares these approaches: Ansible for traditional servers, Terraform for cloud resources, and Kubernetes CronJobs for containerized workloads.

**Monitoring scheduled tasks** is essential because silent failures are worse than loud ones. A backup script that fails without notification is a disaster waiting to happen. The lecture covers: **success/failure alerting** (email, Slack, PagerDuty integrations triggered by non-zero exit codes), **run duration tracking** (alerts if a task takes significantly longer than historical average, indicating performance degradation or deadlock), and **overlap prevention** (ensuring that a long-running task is not started again while a previous instance is still running, using lock files, systemd's `ConditionACPower`, or Kubernetes `concurrencyPolicy: Forbid`). The 2037 *Silent Backup Failure* at UoY—in which a daily backup script failed for 3 weeks without alerting, resulting in unrecoverable data loss—motivated the mandatory monitoring requirements for all scheduled tasks.

### Required Reading

- systemd Documentation (2040). *systemd.timer — Timer Unit Configuration*. freedesktop.org.
- GitHub (2040). *GitHub Actions Documentation: Workflow Syntax and Examples*. GitHub Docs.
- Red Hat (2035). *Systemd Timers: A Complete Replacement for Cron*. Red Hat Knowledgebase.
- HashiCorp (2040). *Terraform Documentation: Provisioners and Triggers*. Terraform Registry.
- Yggdrasil IT Operations (2037). "The Silent Backup Failure: 3 Weeks of Unnoticed Script Failure." *UoY IT Postmortem* 2037-11.

### Discussion Questions

1. Cron is legacy but still widely used. What organizational factors prevent migration to systemd timers, and how should teams manage the coexistence of both scheduling mechanisms?
2. CI/CD for scripts requires that scripts be testable and version-controlled. For ad-hoc scripts written during incident response, is CI/CD practical, or should a separate process govern emergency changes?
3. Kubernetes CronJobs provide sophisticated scheduling but require a full Kubernetes cluster. For a small team with 10 servers, is Kubernetes overhead justified for script scheduling?
4. Overlap prevention via lock files can fail if the lock is not released (e.g., script killed by OOM). What mechanisms (lock timeouts, heartbeat files, systemd watchdog) can prevent stale locks?

### Practice Problems

- Convert a legacy cron job to a systemd timer with equivalent scheduling. Configure automatic logging to journald, failure notification via email, and overlap prevention.
- Write a GitHub Actions workflow for a Python script repository. Include linting, testing, security scanning, and conditional deployment to production. Use GitHub Secrets for credentials.

---

ᛃ **Lecture 12: Security for IT Scripts: Input Validation, Secrets Management, and Privilege Boundaries**

**Course:** IT105 — Programming for IT  
**Degree:** Bachelor of Science in Information Technology, 2040

---

### Overview

The final lecture addresses the security responsibilities of the IT programmer. Scripts often operate with elevated privileges, handle sensitive data, and interact with untrusted inputs. This lecture covers the security patterns that prevent common vulnerabilities: input validation, secrets management, least privilege, audit logging, and secure defaults. Students will learn to write scripts that are not merely functional but defensible against attack.

### Key Topics

- Input validation and sanitization: preventing injection and path traversal
- Secrets management: environment variables, secret stores (Vault, AWS Secrets Manager), and credential rotation
- Least privilege: running scripts with minimal necessary permissions
- Audit logging: non-repudiable records of script execution and actions
- Secure defaults: fail-closed configurations, immutable infrastructure, and defense in depth

### Lecture Notes

The IT programmer holds a position of trust. Their scripts restart services, modify databases, rotate credentials, and configure firewalls. A single vulnerability in a script can compromise an entire infrastructure. By 2040, the security community has recognized that **operational scripts are a critical attack surface**, not a secondary concern. The 2033 *Supply Chain Attack on Build Scripts*—in which an attacker compromised a CI/CD pipeline by injecting malicious code into a seemingly innocuous deployment script—demonstrated that script security is supply chain security.

**Input validation and sanitization** (covered in Lecture 9) is the foundation of script security. The lecture extends this foundation with **path traversal prevention**: ensuring that user-provided paths cannot escape a designated directory (e.g., rejecting `../../../etc/passwd` when the expected input is a filename within `/var/data`). The `pathlib` module's `resolve()` method resolves symbolic links and parent references, enabling safe validation: `resolved = (base_dir / user_input).resolve(); if not resolved.startswith(base_dir.resolve()): raise ValueError`. For shell command construction, the lecture mandates **array-based invocation** (`subprocess.run(["cmd", arg1, arg2])`) over string concatenation, eliminating command injection entirely.

**Secrets management** addresses the challenge of storing and using credentials (passwords, API keys, tokens, certificates) without embedding them in code. Hardcoded secrets in scripts are a pervasive vulnerability: they leak through version control, are visible in process listings (`ps aux`), and persist in log files. The 2040 standard is **dynamic secrets**: credentials fetched at runtime from a secret store (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, Kubernetes Secrets) with automatic rotation and audit logging. The lecture demonstrates Vault integration in Python (`hvac` library) and Bash (`vault` CLI), including authentication via Kubernetes service accounts, secret retrieval, and lease renewal. For local development, `.env` files (loaded via `python-dotenv`) store non-production secrets, but the lecture warns that `.env` files must never be committed to version control.

**Least privilege** requires that scripts run with the minimum permissions necessary for their function. A script that reads log files does not need root access; a script that restarts a specific service needs only the capability to signal that service. Linux **capabilities** (`CAP_NET_ADMIN`, `CAP_SYS_PTRACE`) provide fine-grained privilege control, and **POSIX ACLs** provide fine-grained file access. By 2040, the UoY IT Guild mandates **capability-based execution** for all production scripts: each script is granted only the capabilities it requires, with explicit justification documented in the script header. For containerized scripts, Kubernetes security contexts (`runAsNonRoot: true`, `readOnlyRootFilesystem: true`, `allowPrivilegeEscalation: false`) enforce least privilege at the orchestration level.

**Audit logging** provides non-repudiable records of script execution. Unlike operational logging (which records what happened for debugging), audit logging records who did what, when, and with what authorization. The lecture covers: **session recording** (tools like `script`, `asciinema`, and `ttyrec` capture terminal sessions), **command logging** (auditd, `bash` history with timestamps, PowerShell transcription), and **structured audit events** (JSON logs sent to an append-only audit database). The 2036 *UoY Audit Standard* requires that all scripts with production impact generate at least one audit event per execution, including: script name, user identity, start time, end time, exit code, and a summary of actions taken.

**Secure defaults** ensure that scripts fail safely when misconfigured or attacked. A script with a missing configuration file should not fall back to an insecure default (e.g., disabling authentication); it should fail closed (exit with error). **Immutable infrastructure** extends this principle: scripts are deployed as read-only artifacts (containers, signed binaries) that cannot be modified at runtime, preventing attackers from injecting malicious code. **Defense in depth** layers multiple security controls: input validation, secrets management, least privilege, audit logging, and network segmentation, so that the compromise of one control does not lead to total compromise. The lecture concludes with the **Security Development Lifecycle for Scripts**: threat modeling, secure coding, static analysis, penetration testing, and continuous monitoring.

### Required Reading

- OWASP (2040). *Command Injection Cheat Sheet*. OWASP Foundation.
- HashiCorp (2040). *Vault Documentation: Dynamic Secrets and Authentication*. Version 4.2.
- Linux Capabilities Documentation (2040). *capabilities(7) — Linux Man Pages*.
- Yggdrasil Security Team (2033). "The Supply Chain Attack on Build Scripts: Lessons for Script Security." *UoY Security Postmortem* 2033-04.
- Yggdrasil IT Guild (2036). "The UoY Audit Standard: Requirements for Operational Script Logging." *UoY IT Security Policy* v9.1.

### Discussion Questions

1. Dynamic secrets from Vault are secure but introduce latency (network round-trip). For a high-frequency script that authenticates thousands of times per minute, how can secret retrieval be optimized without sacrificing security?
2. Linux capabilities provide fine-grained privilege control but are complex and poorly understood. What training and tooling are necessary for a team to adopt capability-based execution effectively?
3. Immutable infrastructure prevents runtime modification but complicates emergency fixes. How should an organization balance the security benefits of immutability against the operational need for rapid response?
4. Defense in depth requires multiple controls, each with overhead. For a small IT team with limited resources, which controls are essential and which can be deferred?

### Practice Problems

- Review a provided Python script for security vulnerabilities. Identify at least 5 issues (injection risks, hardcoded secrets, excessive privileges, missing validation, weak error handling) and produce a hardened version with documented mitigations.
- Implement a secrets retrieval pattern for a Python script using HashiCorp Vault. Include authentication, secret caching with TTL, automatic renewal, and fallback to a local encrypted cache when Vault is unreachable.

---

## Final Examination Preparation

The IT105 final examination is a **practical coding assessment** conducted over 48 hours. Students receive a set of IT automation challenges and must produce working, tested, and documented scripts.

### Examination Structure

Students must complete **four of six** challenges:

1. **Log Analysis Script**: Parse a 5GB web server log file, extract statistics (top IPs, URLs, status codes), and generate a summary report. Requirements: streaming processing (no full file load), parameterized output format (CSV or JSON), and error handling for malformed lines.
2. **Remote Administration Tool**: Write a script that executes commands on multiple remote hosts via SSH, collects results, and produces a consolidated report. Requirements: parallel execution, connection timeout handling, and host key verification.
3. **Database Migration Script**: Migrate data from a legacy schema to a new schema, handling type conversions, missing fields, and referential integrity. Requirements: transactional safety, rollback capability, and idempotency.
4. **API Integration Script**: Interact with a cloud provider's REST API to provision resources, verify provisioning, and handle rate limiting and retries. Requirements: OAuth authentication, pagination, and structured logging.
5. **Configuration Validator**: Validate a YAML configuration file against a schema, checking types, required fields, and cross-field constraints. Requirements: detailed error messages, support for nested structures, and exit codes for CI integration.
6. **Security Hardening Script**: Audit a server for common misconfigurations (world-writable files, SUID binaries, weak permissions) and generate a remediation plan. Requirements: non-destructive audit mode, privilege checks, and machine-readable output.

### Evaluation Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Correctness | 25% | Script produces correct output for valid inputs; handles edge cases gracefully |
| Robustness | 20% | Error handling, input validation, and defensive programming |
| Security | 20% | No injection vulnerabilities, proper secrets handling, least privilege |
| Testability | 15% | Modular design, unit tests, and test coverage ≥70% |
| Documentation | 10% | Clear README, inline comments, and usage examples |
| Style | 10% | Consistent formatting, readable naming, and adherence to Rúnar Standard |

---

*The script is forged. The automation runs. The infrastructure stands.* ᛟ

— Runa Gridweaver Freyjasdottir, Programming for IT, University of Yggdrasil, 2040
