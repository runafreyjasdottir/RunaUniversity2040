# IT105: Programming for IT (Python, Bash, PowerShell)
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4
**Prerequisites:** IT101 (Foundations of Information Technology)
**Description:** A practical, intensive course in programming for IT professionals. Students master three dominant scripting environments — Python, Bash, and PowerShell — learning to automate system administration tasks, manipulate data, orchestrate infrastructure, and build tools that solve real operational problems. By 2040, the IT professional who cannot code is as limited as the scribe who cannot write. This course treats programming not as software engineering but as **operational literacy**: the ability to express procedures in executable form, to compose reliable automation, and to reason about the behaviour of systems through the lens of code. All lab exercises are performed on live systems in the Yggdrasil IT Sandbox — a virtualised environment where mistakes are encouraged, logged, and analysed.

---

## Lecture 1: Programming as Operational Literacy — The IT Professional's Code

Programming is the craft of instructing machines to perform tasks. For software engineers, it is the primary vocation; for IT professionals, it is a **force multiplier** that transforms tedious manual work into reliable, repeatable automation. This lecture establishes the conceptual framework: what programming means in an IT context, why it matters, and how the three languages of this course — Python, Bash, and PowerShell — serve different but complementary roles.

**The automation imperative** in IT is driven by scale. A single administrator in 1990 might manage 10 servers; in 2010, 100; in 2040, a single platform engineer manages 10,000+ containerised services across multiple cloud providers. Manual administration at this scale is impossible; automation is not a luxury but a survival mechanism. **Infrastructure as Code (IaC)** — expressing infrastructure configuration in version-controlled, executable text — is the dominant paradigm. Tools like Terraform, Ansible, Pulumi, and the University's *Völundr* framework all rely on the ability to write and reason about code.

**Python** is the lingua franca of IT automation. It is a high-level, interpreted language with clean syntax, extensive libraries, and cross-platform support. Python's **standard library** includes modules for file I/O, networking, regular expressions, JSON/XML parsing, database access, and concurrent execution. The **third-party ecosystem** (PyPI, with 5+ million packages in 2040) provides tools for virtually every IT task: **Ansible** (configuration management), **SaltStack** (orchestration), **Paramiko** (SSH), **Requests** (HTTP), **Pandas** (data manipulation), **Psycopg2** (PostgreSQL), **Boto3** (AWS), and thousands more. Python's **readability** makes it ideal for scripts that must be maintained by teams, not just their original authors.

**Bash** (the Bourne Again Shell) is the native command language of Linux and macOS. It is not a general-purpose programming language but a **command interpreter** that excels at: chaining programs together with pipes and redirection; automating sequences of system commands; and writing portable scripts that run on virtually any Unix-like system. Bash's strength is its **integration**: every command-line tool on a Linux system is a Bash function waiting to be called. Its weakness is **maintainability**: complex Bash scripts become unreadable quickly, and debugging is notoriously difficult. The rule of thumb: use Bash for simple sequences (<100 lines), Python for anything more complex.

**PowerShell** is Microsoft's modern command shell and scripting language. Unlike Bash, which passes text between commands, PowerShell passes **objects** (structured data with properties and methods). This makes PowerShell exceptionally powerful for managing Windows systems, Active Directory, Azure, and Microsoft 365. In 2040, **PowerShell Core** (the cross-platform, open-source version) runs on Linux and macOS as well, making it a viable choice for heterogeneous environments. PowerShell's **cmdlets** (verb-noun commands like `Get-Process`, `Invoke-RestMethod`) are self-documenting and discoverable, and its **pipeline** preserves object structure across commands.

**The Yggdrasil IT Sandbox** is the live environment for all IT105 labs. Each student receives a **personal namespace** within a Kubernetes cluster: a Linux VM (for Bash and Python), a Windows container (for PowerShell), and a shared network segment where students can connect their environments and observe the effects of their scripts on live services. The Sandbox includes **deliberately faulted systems** that students must diagnose and repair using only scripts — no GUI access is permitted after the first two weeks.

**Required Reading:**
- Eric S. Raymond, "The Art of Unix Programming" (Addison-Wesley, 2003/2035), ch. 1 ("Philosophy") and ch. 7 ("Multiprogramming")
- Al Sweigart, *Automate the Boring Stuff with Python* (2nd ed., No Starch Press, 2019/2035), ch. 1–3
- Richard Blum & Christine Bresnahan, *Linux Command Line and Shell Scripting Bible* (4th ed., Wiley, 2021/2035), ch. 1–2
- Bruce Payette & Richard Siddaway, *Windows PowerShell in Action* (4th ed., Manning, 2035), ch. 1
- University of Yggdrasil, "The IT Sandbox: A Live Kubernetes Environment for IT Education" (2039)

**Discussion Questions:**
1. Python is often called a "scripting language," but it is Turing-complete and capable of building complex applications. Is the distinction between "scripting" and "programming" meaningful, or is it merely a social hierarchy that devalues certain kinds of code?
2. Bash scripts are notorious for becoming unmaintainable. Is this a fundamental limitation of the language, or a consequence of programmers using Bash for tasks that should be written in Python?
3. PowerShell's object pipeline is more powerful than Bash's text pipeline, but it is also more complex. For a heterogeneous environment (Linux and Windows), is PowerShell's cross-platform capability sufficient reason to adopt it as the primary shell, or does Bash's ubiquity on Linux make it the safer default?

---

## Lecture 2: Python Fundamentals — Variables, Types, Control Flow, and Functions

Python's elegance lies in its simplicity. This lecture covers the core language features that every IT professional must internalise: data types, control structures, functions, and the standard library.

**Variables and types.** Python is **dynamically typed**: variable types are determined at runtime, not declared in advance. The built-in types include: **int** (arbitrary-precision integers), **float** (IEEE 754 double-precision), **str** (Unicode strings), **bool** (True/False), **list** (ordered, mutable sequences), **tuple** (ordered, immutable sequences), **dict** (key-value mappings), **set** (unordered collections of unique elements), and **None** (the null value). **Type hints** (PEP 484, introduced in Python 3.5, standard by 2040) allow optional static type annotation: `def greet(name: str) -> str:`. While not enforced at runtime, type hints improve code clarity, enable IDE autocomplete, and support static analysis tools like **mypy**.

**Control flow.** Python provides **if/elif/else** for conditional execution, **for** and **while** for iteration, and **try/except/finally** for exception handling. The **with** statement manages resources (files, locks, database connections) that require setup and teardown. **List comprehensions** (`[x*2 for x in range(10) if x % 2 == 0]`) provide concise, readable ways to create lists. **Generator expressions** (`(x*2 for x in range(10))`) create iterators that yield values lazily, conserving memory for large sequences.

**Functions** are first-class objects: they can be assigned to variables, passed as arguments, and returned from other functions. **Keyword arguments** (`def connect(host, port=22, timeout=30)`) improve readability and flexibility. **Variable-length arguments** (`*args` for positional, `**kwargs` for keyword) enable flexible APIs. **Lambda expressions** (`lambda x: x**2`) create anonymous functions for short operations. **Decorators** (`@retry`) modify function behaviour without changing the function definition — a powerful pattern for logging, caching, authentication, and retry logic.

**The standard library** is Python's greatest asset for IT work. **os** and **pathlib** provide cross-platform file system operations. **subprocess** executes external commands and captures output. **sys** and **argparse** handle command-line arguments. **json**, **csv**, and **xml.etree** parse common data formats. **re** provides regular expressions for pattern matching. **datetime** and **time** handle dates and timestamps. **hashlib** computes cryptographic hashes. **socket**, **urllib**, and **http.client** provide low-level network access. **threading** and **multiprocessing** enable concurrent execution. In 2040, **asyncio** (introduced in Python 3.4, mature by 2040) is the standard for high-performance network programming: `async def` and `await` enable thousands of concurrent connections without the complexity of threads.

**Lab Exercise:** Students write a Python script that: reads a CSV file of server inventory; filters for servers with CPU utilisation > 80%; generates an HTML report with colour-coded warnings; and emails the report to the operations team. This single exercise integrates file I/O, data parsing, conditionals, string formatting, and external communication.

**Required Reading:**
- Guido van Rossum et al., *The Python Language Reference* (3.15, 2040), §3 ("Data Model") and §4 ("Execution Model")
- Luciano Ramalho, *Fluent Python* (2nd ed., O'Reilly, 2022/2035), ch. 1–5
- Jake VanderPlas, *Python Data Science Handbook* (O'Reilly, 2016/2035), ch. 1 ("IPython: Beyond Normal Python")
- University of Yggdrasil, "Python Style Guide for IT Operations: PEP 8, Type Hints, and Documentation Standards" (2039)

**Discussion Questions:**
1. Dynamic typing makes Python code concise but can lead to runtime errors that static typing would catch. Does the productivity gain of dynamic typing outweigh the reliability cost, or should IT scripts always use type hints and static analysis?
2. Python's Global Interpreter Lock (GIL) prevents true parallelism in threads. For CPU-bound IT tasks, is multiprocessing (which uses separate processes and more memory) an acceptable workaround, or should Python be avoided for CPU-intensive automation?
3. asyncio enables massive concurrency but introduces complexity (event loops, coroutines, futures). For a typical IT script that makes a few API calls, is asyncio worth the learning curve, or are synchronous requests with a session pool sufficient?

---

## Lecture 3: Python for System Administration — os, subprocess, pathlib, and shutil

Python's true power for IT professionals emerges when it is applied to system administration. This lecture covers the modules and patterns that enable Python to inspect, manipulate, and orchestrate systems.

**os** and **os.path** provide low-level operating system interfaces. `os.listdir()` enumerates directory contents. `os.walk()` traverses directory trees recursively. `os.environ` accesses environment variables. `os.getpid()`, `os.getuid()`, `os.getgid()` inspect process and user identity. `os.path.join()`, `os.path.exists()`, `os.path.getsize()` manipulate file paths portably. In 2040, **pathlib** (introduced in Python 3.4, standard by 2040) is the preferred approach: `Path('/etc/hosts')` creates a path object with methods like `.exists()`, `.read_text()`, `.write_text()`, `.glob('*.conf')`, and `.chmod(0o644)`. Pathlib is more readable and less error-prone than string-based path manipulation.

**subprocess** executes external commands. `subprocess.run(['ls', '-la'], capture_output=True, text=True)` runs a command and captures its output. The **shell=True** parameter allows shell syntax but introduces security risks (shell injection); it should be avoided when possible. `subprocess.Popen` provides lower-level control: non-blocking execution, streaming output, and bidirectional communication. For complex pipelines, **plumbum** (a third-party library) provides a Pythonic interface: `(ls['-la'] | grep['python'])()`.

**shutil** (shell utilities) provides high-level file operations: `shutil.copy()`, `shutil.move()`, `shutil.rmtree()`, `shutil.make_archive()`, `shutil.disk_usage()`. **tempfile** creates temporary files and directories that are automatically cleaned up. **glob** finds files matching wildcard patterns. **fnmatch** provides Unix shell-style pattern matching.

**Monitoring and inspection** scripts are a staple of IT operations. A script that checks disk usage on all servers and alerts when usage exceeds 90% might: read a list of servers from a configuration file; SSH into each server using **Paramiko**; execute `df -h` and parse the output; compare usage to thresholds; and send alerts via email, Slack, or a ticketing system. A script that rotates log files might: find all `.log` files older than 30 days; compress them with `gzip`; move them to an archive directory; and delete archives older than 1 year.

**Configuration management** with Python is more flexible than shell scripts but requires discipline. **Dataclasses** (Python 3.7+) provide concise class definitions for structured configuration. **Pydantic** (a third-party library) validates configuration against schemas, catching errors at startup rather than runtime. **YAML** and **TOML** parsers (PyYAML, tomli) read human-friendly configuration files. The University's *Völundr* framework uses Pydantic models to validate infrastructure configurations before applying them.

**Lab Exercise:** Students write a **server health check** script in Python that: reads a YAML configuration specifying health check parameters (CPU threshold, memory threshold, disk threshold, endpoints to check); collects metrics from the local system (CPU via `psutil`, memory via `/proc/meminfo`, disk via `shutil.disk_usage`); checks HTTP endpoints with `requests` and `asyncio`; writes results to a JSON log; and exits with code 0 (healthy) or 1 (unhealthy) for integration with monitoring systems.

**Required Reading:**
- Doug Hellmann, *The Python Standard Library by Example* (Addison-Wesley, 2011/2035), ch. 5 ("File System"), ch. 17 ("Subprocesses")
- Kenneth Reitz & Tanya Schlusser, *The Hitchhiker's Guide to Python* (O'Reilly, 2016/2035), ch. 14 ("System Administration")
- Giancarlo Zaccone & Alessandro Molina, *Python Parallel Programming Cookbook* (2nd ed., Packt, 2035), ch. 3 ("Asyncio")
- University of Yggdrasil, "Völundr Framework: Python-Based Infrastructure as Code" (2039)

**Discussion Questions:**
1. subprocess.run is powerful but dangerous: shell=True can lead to command injection, and capturing large outputs can exhaust memory. What are the best practices for using subprocess safely in production IT scripts?
2. pathlib is more Pythonic than os.path, but many existing scripts use os.path. Is it worth refactoring legacy scripts to use pathlib, or is consistency with existing code more important than using the latest idiom?
3. psutil is a third-party library that provides cross-platform system metrics. Should the Python standard library include functionality like psutil, or is the division between standard library and third-party packages healthy for the ecosystem?

---

## Lecture 4: Python for Data Processing — Parsing, Transformation, and Reporting

IT professionals spend a significant portion of their time processing data: log files, configuration files, inventory databases, monitoring metrics, and API responses. This lecture covers the tools and techniques for extracting, transforming, and reporting data in Python.

**Text processing** is the foundation. **String methods** (`split()`, `strip()`, `replace()`, `find()`, `startswith()`) handle basic manipulation. **Regular expressions** (`re` module) provide powerful pattern matching: `re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', log_line)` extracts IP addresses. **f-strings** (`f"Server {hostname} has {cpu}% CPU usage"`) provide readable string formatting. In 2040, **structured pattern matching** (`match/case`, introduced in Python 3.10) enables elegant handling of complex data shapes.

**CSV processing** uses the **csv** module for simple cases and **Pandas** for complex analysis. `csv.DictReader` reads CSV files as dictionaries; `csv.DictWriter` writes them. Pandas **DataFrames** provide spreadsheet-like manipulation: filtering (`df[df['cpu'] > 80]`), grouping (`df.groupby('datacenter').mean()`), merging (`pd.merge(df1, df2, on='server_id')`), and pivoting (`df.pivot_table(...)`). For large datasets that do not fit in memory, **Dask** provides parallel, out-of-core DataFrame operations.

**JSON processing** is essential for API work. `json.loads()` parses JSON strings; `json.dumps()` serialises Python objects. The **Requests** library (`requests.get(url).json()`) is the standard for HTTP API interaction. **JMESPath** provides query languages for JSON: `jmespath.search("servers[?status=='running'].name", data)` extracts running server names. **jq** (a command-line tool, not Python, but often used alongside Python scripts) provides similar functionality for shell pipelines.

**XML processing** uses **xml.etree.ElementTree** for simple cases and **lxml** for performance-critical or schema-validated work. XPath expressions navigate XML trees: `tree.findall('.//server[@status="active"]')`. For configuration files, **YAML** (PyYAML) and **TOML** (tomli) are preferred over XML for human readability.

**Reporting and visualisation** transform raw data into actionable information. **Jinja2** templates generate HTML, XML, or configuration files from data. **Matplotlib** and **Seaborn** create static plots for dashboards. **Plotly** and **Bokeh** create interactive web-based visualisations. In 2040, **Streamlit** and **Gradio** enable rapid creation of data apps with minimal code. The **Yggdrasil Operations Dashboard** — used by the University IT team — is built with Streamlit and displays real-time metrics from 50,000+ campus devices.

**Lab Exercise:** Students analyse a 1 GB Apache access log file. They write a Python script that: parses each line to extract IP, timestamp, URL, status code, and response size; identifies the top 10 most requested URLs; calculates the 95th percentile response time; detects potential DDoS attacks (IPs with >1000 requests in a 1-minute window); and generates an HTML report with tables and charts.

**Required Reading:**
- Jeffrey E. F. Friedl, *Mastering Regular Expressions* (3rd ed., O'Reilly, 2006/2035), ch. 1–4
- Wes McKinney, *Python for Data Analysis* (3rd ed., O'Reilly, 2022/2035), ch. 5–8
- Kenneth Reitz, "Requests: HTTP for Humans" (documentation, 2040)
- Armin Ronacher, "Jinja2 Documentation" (2040)
- University of Yggdrasil, "The Operations Dashboard: Building Real-Time IT Metrics Apps with Streamlit" (2039)

**Discussion Questions:**
1. Regular expressions are powerful but notoriously difficult to read and maintain. For complex log parsing, are regexes still the best tool, or should structured logging (e.g., JSON-formatted logs) eliminate the need for regex parsing?
2. Pandas is the standard for data manipulation in Python, but it is memory-intensive and single-threaded. For IT workloads that process large datasets (e.g., analysing months of log data), is Dask or Polars a better choice, or should such workloads be handled by dedicated data pipeline tools (Spark, Flink)?
3. Streamlit and Gradio enable rapid dashboard creation, but they are not as customisable as React or Vue. For IT dashboards that need to be maintained for years, is the speed of development worth the long-term maintainability trade-off?

---

## Lecture 5: Python for Networking — socket, requests, paramiko, and asyncio

Networks are the circulatory system of IT. This lecture covers Python's networking capabilities, from low-level socket programming to high-level HTTP clients and SSH automation.

**Socket programming** is the foundation of network communication. The **socket** module provides access to the BSD socket interface: `socket.socket(socket.AF_INET, socket.SOCK_STREAM)` creates a TCP socket. **Server sockets** bind to an address, listen for connections, and accept clients; **client sockets** connect to remote addresses. Low-level socket programming is rarely needed in 2040 (higher-level libraries handle the details), but understanding sockets is essential for debugging network issues and optimising performance. **socketserver** and **http.server** provide simple server frameworks for prototyping.

**HTTP clients** are the workhorses of API interaction. **Requests** (`requests.get()`, `requests.post()`, `requests.put()`, `requests.delete()`) provides a clean, intuitive API for HTTP operations. **Session objects** (`requests.Session()`) persist cookies and connection pools across requests, improving performance for repeated API calls. **Authentication** (Basic Auth, Bearer tokens, OAuth2) is handled through parameters or adapters. **Retries** and **timeouts** prevent hung connections. In 2040, **httpx** is the emerging standard: it provides a Requests-compatible API with **HTTP/2 support** and **async compatibility**. The University's *Bifröst API Client* is built on httpx and is used for all internal API interactions.

**SSH automation** enables secure remote administration. **Paramiko** is the standard Python library for SSHv2: it can execute commands (`exec_command`), transfer files (SFTP), and tunnel ports. **Fabric** (built on Paramiko) provides a higher-level API for running commands across multiple hosts in parallel. **Ansible** (discussed in Lecture 8) uses Paramiko under the hood for its SSH connections. For Windows remote management, **pywinrm** provides WinRM (Windows Remote Management) access from Python.

**asyncio for networking** enables massive concurrency without threads. An asyncio HTTP client might: create an `aiohttp.ClientSession`; launch hundreds of `async` tasks, each fetching a URL; `await` the results; and process them as they complete. This pattern is essential for: scanning thousands of hosts for open ports; fetching metrics from hundreds of servers; and orchestrating concurrent API calls. The **async/await** syntax (introduced in Python 3.5) is now the standard for high-performance network code. **uvloop** (a Cython-based event loop) provides 2–4x performance improvement over the default asyncio loop.

**Lab Exercise:** Students write a **network scanner** in Python using asyncio: it reads a list of IP ranges from a configuration file; concurrently probes common ports (22, 80, 443, 3306, 5432, 8080) on all hosts; identifies the service version by banner grabbing; writes results to a SQLite database; and generates an HTML report with interactive tables. The scanner must handle 10,000+ hosts in under 5 minutes.

**Required Reading:**
- W. Richard Stevens, Bill Fenner & Andrew M. Rudoff, *UNIX Network Programming, Volume 1: The Sockets Networking API* (3rd ed., Addison-Wesley, 2003/2035), ch. 1–4
- Cory Benfield, "httpx Documentation" (2040)
- Jeff Forcier, "Paramiko Documentation" (2040)
- Andrew Svetlov, "aiohttp Documentation" (2040)
- University of Yggdrasil, "The Bifröst API Client: asyncio-Based Internal API Orchestration" (2039)

**Discussion Questions:**
1. Python's socket module provides low-level control, but most IT tasks are better served by high-level libraries (Requests, Paramiko). Is socket programming still a necessary skill for IT professionals, or is it an obsolete artefact of a bygone era?
2. asyncio enables massive concurrency but can be difficult to debug (stack traces become complex, deadlocks are subtle). Does the performance gain justify the complexity, or should threads or processes be preferred for simplicity?
3. Network scanning is a legitimate administrative task, but the same techniques can be used maliciously. What ethical and legal guidelines should govern the use of automated network scanning in IT operations?

---

## Lecture 6: Bash Fundamentals — The Unix Philosophy in Action

Bash is the command interpreter of Linux and the glue that binds the Unix toolchain. This lecture covers Bash fundamentals: command execution, redirection, pipelines, variables, conditionals, loops, and functions.

**Command execution** in Bash follows a simple grammar: `command [options] [arguments]`. Options typically begin with `-` (single character) or `--` (long form). **Quoting** is essential: single quotes (`'...'`) prevent all expansion; double quotes (`"..."`) allow variable expansion but prevent word splitting; backticks (`` `...` ``) or `$()` execute commands and capture output. **Wildcards** (`*`, `?`, `[...]`) match filenames. **Brace expansion** (`{a,b,c}`) generates sequences. **Tilde expansion** (`~` becomes the home directory).

**Redirection** controls input and output streams. `>` redirects stdout to a file (overwrite); `>>` appends; `2>` redirects stderr; `&>` redirects both stdout and stderr; `<` redirects stdin from a file; `<<` creates a here-document; `<<<` creates a here-string. **Pipes** (`|`) connect the stdout of one command to the stdin of another, enabling powerful composition: `cat access.log | awk '{print $1}' | sort | uniq -c | sort -rn | head -10` extracts the top 10 IP addresses from an Apache log. In 2040, **process substitution** (`<(...)` and `>(...)`) and **named pipes** (FIFOs) extend the pipeline model for complex workflows.

**Variables and expansion.** Bash variables are untyped strings by default. `name=value` assigns a variable; `$name` or `${name}` expands it. **Special variables** include: `$0` (script name), `$1`, `$2`, ... (positional parameters), `$@` (all parameters), `$#` (parameter count), `$?` (exit status of last command), `$$` (PID), and `$!` (PID of last background job). **Parameter expansion** provides powerful string manipulation: `${name:-default}`, `${name:=default}`, `${name:?error}`, `${name:offset:length}`, `${name#pattern}`, `${name%pattern}`, `${name//old/new}`. In 2040, **associative arrays** (`declare -A arr`) enable dictionary-like data structures in Bash 5.x+.

**Control structures.** `if [ condition ]; then ... fi` tests conditions; `[` is actually a command (`test`), and conditions use string or numeric comparison operators (`-eq`, `-ne`, `-lt`, `-gt`, `-le`, `-ge`, `=`, `!=`, `-z`, `-n`, `-e`, `-f`, `-d`). `for var in list; do ... done` iterates over lists. `while [ condition ]; do ... done` and `until [ condition ]; do ... done` provide loop constructs. `case word in pattern) ... ;; esac` provides pattern matching. **Functions** (`function_name() { ... }`) enable code reuse. **Arithmetic** uses `$((expression))` or `let`.

**Lab Exercise:** Students write a Bash script that: parses `/proc/meminfo` to calculate memory usage percentage; checks all running processes with `ps` and reports any using >50% CPU; finds the 10 largest files in `/var/log` using `find` and `du`; compresses logs older than 7 days with `gzip`; and emails a summary report using `mail` or `sendmail`.

**Required Reading:**
- Brian W. Kernighan & Rob Pike, *The Unix Programming Environment* (Prentice Hall, 1984/2035), ch. 3–5
- Arnold Robbins & Nelson H. F. Beebe, *Classic Shell Scripting* (O'Reilly, 2005/2035), ch. 2–6
- Greg Wooledge ("GreyCat") & others, "BashFAQ" and "BashPitfalls" (<http://mywiki.wooledge.org/>, 2040)
- GNU Bash Reference Manual (v5.4, 2035), §3 ("Basic Shell Features")

**Discussion Questions:**
1. Bash scripts are notoriously fragile: spaces in filenames break unquoted variables, `set -e` behaves unpredictably with pipelines, and error handling is verbose. Is Bash fundamentally unsuited for robust automation, or do these problems stem from programmer ignorance of best practices?
2. The Unix philosophy ("do one thing well, compose with pipes") is elegant but assumes that all tools agree on a common text format. When tools output structured data (JSON, XML), pipes become awkward. Is the Unix philosophy still relevant in 2040, or has it been superseded by object pipelines (PowerShell) and API-driven workflows?
3. Bash is the default shell on Linux, but **zsh** and **fish** offer superior interactive features (autocompletion, syntax highlighting, history search). Should IT professionals switch to modern shells for interactive use while keeping Bash for scripting, or does the proliferation of shells create more confusion than benefit?

---

## Lecture 7: Bash for System Administration — find, awk, sed, and cron

Beyond basic scripting, Bash for IT requires mastery of the Unix toolchain: the classic utilities that have been refined over 50 years. This lecture covers the most powerful tools in the administrator's arsenal.

**find** is the most versatile file search tool. `find /var/log -name "*.log" -mtime +7` finds log files older than 7 days. `find /home -type f -size +100M` finds large files. `find . -name "*.py" -exec grep -l "TODO" {} \;` searches for Python files containing "TODO". `find` supports complex logical expressions (`-and`, `-or`, `-not`), actions (`-print`, `-delete`, `-exec`, `-ok`), and optimisation (`-maxdepth`, `-prune`). In 2040, **fd** (a Rust-based `find` alternative) is popular for interactive use due to its speed and intuitive syntax, but `find` remains the standard for scripts.

**awk** is a pattern-scanning and processing language. It processes input line by line, splitting each line into fields (`$1`, `$2`, ...). `awk '{print $1, $4}' access.log` prints the first and fourth fields. `awk '/error/ {count++} END {print count}'` counts lines matching "error". `awk '{sum+=$2} END {print sum/NR}'` calculates the average of the second field. awk supports variables, conditionals, loops, arrays, and functions. It is Turing-complete and can replace many small Python scripts. In 2040, **gawk** (GNU awk) is the standard implementation, with extensions for networking, CSV parsing, and arbitrary-precision arithmetic.

**sed** (stream editor) performs basic text transformations: substitution (`s/old/new/g`), deletion (`/pattern/d`), insertion, and extraction. `sed -i 's/localhost/127.0.0.1/g' config.txt` replaces all occurrences in a file. `sed -n '/START/,/END/p'` extracts lines between two patterns. sed is less powerful than awk but faster for simple transformations. In 2040, **ripgrep** (`rg`) and **sd** (a sed alternative with intuitive syntax) are popular for interactive use, but `sed` remains essential for scripts.

**cron** is the Unix job scheduler. `crontab -e` edits the user's cron table; entries specify minute, hour, day of month, month, day of week, and command. `0 2 * * * /usr/local/bin/backup.sh` runs a backup at 2 AM daily. **systemd timers** (the modern replacement for cron) provide more flexibility: dependencies, randomized delays, persistent timers (run missed jobs after downtime), and integration with journal logging. In 2040, **systemd timers** are the default on most Linux distributions, but cron is still widely used and understood. The University's *Skuld Scheduler* (named after the Norn of the future) is a systemd-based job orchestrator that manages 5,000+ automated tasks across campus systems.

**Lab Exercise:** Students write a **log rotation and analysis** pipeline entirely in Bash: a `find` command identifies Apache logs older than 30 days; `gzip` compresses them; `awk` extracts the hour of day and counts requests per hour; `sort` and `uniq` identify the busiest hours; and a `systemd timer` runs the pipeline daily. The script must handle errors gracefully (e.g., no logs to rotate) and log its actions to syslog.

**Required Reading:**
- Dale Dougherty & Arnold Robbins, *sed & awk* (2nd ed., O'Reilly, 1997/2035), ch. 1–5, 7–8
- Michael J. Pilone & Matthew Russell, *cron: The Job Scheduler* (O'Reilly, 2005/2035) — available as systemd timer documentation
- Julia Evans, *Bite Size Linux* (Wizard Zines, 2035) — zines on find, awk, sed, and cron
- University of Yggdrasil, "The Skuld Scheduler: systemd-Based Job Orchestration at Scale" (2039)

**Discussion Questions:**
1. awk is a complete programming language that is older than Python. Is it still worth learning awk in 2040, or has Python rendered it obsolete for all but the most performance-critical text processing?
2. cron is simple but lacks dependencies, retries, and distributed execution. systemd timers add some of these features, but they are Linux-specific. For cross-platform scheduling, should IT professionals use Python-based schedulers (APScheduler, Celery), or is the simplicity of cron/systemd worth the platform limitation?
3. find, awk, sed, and grep are powerful but have cryptic syntax. Modern alternatives (fd, ripgrep, sd) are more user-friendly but not universally installed. Should IT scripts use modern tools (and require their installation) or stick to POSIX-standard utilities for maximum portability?

---

## Lecture 8: PowerShell Fundamentals — Cmdlets, Objects, and the Pipeline

PowerShell is the modern command shell for Windows and, increasingly, for cross-platform administration. This lecture covers PowerShell's unique features: the object pipeline, cmdlets, providers, and remoting.

**Cmdlets** are PowerShell commands with a **verb-noun** naming convention: `Get-Process`, `Stop-Service`, `Invoke-RestMethod`, `Set-Location`. This convention makes commands **self-documenting** and **discoverable**: `Get-Command -Verb Get -Noun Process` finds all commands that get processes. **Aliases** provide familiar names for users coming from other shells: `ls`, `dir`, `cat`, `rm`, `ps`, `curl` are all aliases for PowerShell cmdlets. **Parameters** are strongly typed and support tab completion, validation, and dynamic help.

**The object pipeline** is PowerShell's defining feature. Unlike Bash, which passes text between commands, PowerShell passes **.NET objects** with properties and methods. `Get-Process | Where-Object {$_.CPU -gt 100} | Sort-Object CPU -Descending | Select-Object -First 5` finds the top 5 CPU-intensive processes. Each command outputs objects; the next command operates on those objects without parsing text. This eliminates the fragile text-parsing that plagues Bash pipelines. **Methods** can be invoked on piped objects: `(Get-Date).AddDays(7)` returns the date one week from now. **Properties** are accessed with dot notation: `$process.Name`, `$process.Id`, `$process.CPU`.

**Providers** expose data stores as if they were file systems. `Get-PSProvider` lists providers: **FileSystem** (directories and files), **Registry** (Windows registry keys and values), **Certificate** (certificate stores), **Environment** (environment variables), **Variable** (PowerShell variables), **Function** (PowerShell functions), **Alias** (aliases), and **WSMan** (WS-Management configuration). `cd Cert:\LocalMachine\My` navigates to the certificate store; `Get-ChildItem` lists certificates; `Remove-Item` deletes them. This unified namespace simplifies administration: the same commands manage files, registry, certificates, and remote sessions.

**Remoting** enables remote administration over WinRM (Windows Remote Management). `Invoke-Command -ComputerName Server01 -ScriptBlock { Get-Process }` runs a command on a remote machine. `Enter-PSSession -ComputerName Server01` opens an interactive session. **PowerShell Direct** enables remoting into Hyper-V VMs without network connectivity. **SSH remoting** (PowerShell 7+) allows PowerShell to connect to Linux and macOS systems over SSH, enabling cross-platform administration from a single shell. In 2040, **PowerShell Universal** (Ironman Software) provides a web-based dashboard and API for running PowerShell scripts across thousands of machines.

**Lab Exercise:** Students write a PowerShell script that: connects to a remote Windows server using `Invoke-Command`; retrieves a list of services with `Get-Service`; filters for services that are running but set to manual start (potential security risks); stops suspicious services with `Stop-Service`; writes results to a CSV file; and emails the report using `Send-MailMessage`. The script must handle authentication (using credential objects or certificate-based auth) and error cases (unreachable servers, insufficient permissions).

**Required Reading:**
- Bruce Payette & Richard Siddaway, *Windows PowerShell in Action* (4th ed., Manning, 2035), ch. 2–5
- Don Jones & Jeffery Hicks, *Learn PowerShell in a Month of Lunches* (4th ed., Manning, 2035), ch. 1–10
- Adam Bertram, *PowerShell for Sysadmins* (No Starch Press, 2020/2035), ch. 1–4
- Microsoft, "PowerShell 7 Documentation" (2040)
- University of Yggdrasil, "Cross-Platform Administration with PowerShell 7: The Yggdrasil Experience" (2039)

**Discussion Questions:**
1. PowerShell's object pipeline is more powerful than Bash's text pipeline, but it requires understanding .NET object models. For administrators who are not programmers, is the learning curve worth the productivity gain?
2. PowerShell is cross-platform in theory (PowerShell Core runs on Linux and macOS), but many cmdlets are Windows-specific. Is PowerShell genuinely a cross-platform solution, or is it primarily a Windows administration tool with limited Linux utility?
3. PowerShell remoting uses WinRM, which is a SOAP-based protocol. In an era where REST and gRPC dominate API design, is WinRM an anachronism, or does its integration with Windows authentication (Kerberos, NTLM) justify its continued use?

---

## Lecture 9: PowerShell for Advanced Administration — DSC, Desired State, and Automation

Beyond interactive administration, PowerShell enables **Desired State Configuration (DSC)** — declarative infrastructure management that ensures systems maintain a specified configuration. This lecture covers DSC, advanced scripting patterns, and PowerShell's role in modern DevOps.

**Desired State Configuration (DSC)** is PowerShell's declarative configuration management framework. A **DSC configuration** is a script that defines the desired state of a system: "the Web-Server feature must be installed, the C:\InetPub directory must exist with specific permissions, and the Default Web Site must be running." DSC **compiles** the configuration into a MOF (Managed Object Format) file, which is **enacted** by the **Local Configuration Manager (LCM)** on the target node. The LCM periodically checks the actual state against the desired state and **remediates** drift (self-healing). DSC resources are **idempotent**: running the same configuration multiple times produces the same result. In 2040, **DSC v3** supports cross-platform resources (Linux and Windows) and integrates with Azure Policy and AWS Config.

**Advanced scripting patterns** in PowerShell include: **splatting** (`@params` passing parameters as hashtables); **error handling** (`try/catch/finally`, `$ErrorActionPreference`, `-ErrorAction` parameter); **logging** (`Start-Transcript`, `Write-EventLog`, structured logging with **PSFramework**); **progress reporting** (`Write-Progress`); **parallel execution** (`ForEach-Object -Parallel`, introduced in PowerShell 7); and **modularisation** (functions, modules, and the PowerShell Gallery). **Classes** (introduced in PowerShell 5) enable object-oriented scripting for complex automation frameworks.

**PowerShell in DevOps** bridges the gap between Windows administration and modern CI/CD pipelines. **Pester** is the PowerShell testing framework: it supports unit tests, integration tests, and infrastructure tests (verifying that a system is in the desired state). **Invoke-Build** and **psake** are build automation tools. **PowerShell Universal** provides a web dashboard and REST API for scheduling and executing scripts. **Azure PowerShell** and **AWS Tools for PowerShell** manage cloud resources. In 2040, **PowerShell is the standard** for Windows-based CI/CD pipelines, and its cross-platform capabilities make it viable for heterogeneous environments.

**Lab Exercise:** Students write a **DSC configuration** that: ensures IIS is installed on a Windows server; creates a website with a specific physical path and binding; configures SSL with a certificate from the local store; sets appropriate NTFS permissions; and ensures the Application Pool is running. They then write a Pester test suite that verifies the configuration was applied correctly and remains in the desired state after a simulated configuration drift.

**Required Reading:**
- Ritesh Modi, *Windows PowerShell Desired State Configuration Revealed* (Apress, 2014/2035), ch. 1–5
- Mike F. Robbins, *The Pester Book: A Practical Guide to Testing PowerShell Code* (2020/2035)
- Michael Greene et al., "DSC v3: Cross-Platform Desired State Configuration" (Microsoft, 2035)
- University of Yggdrasil, "DSC in the Yggdrasil Data Centre: Managing 500 Windows Servers with Declarative Configuration" (2039)

**Discussion Questions:**
1. DSC is declarative (specify what, not how), but writing DSC resources often requires imperative code. Is DSC genuinely declarative, or is it a thin declarative veneer over imperative PowerShell scripts?
2. Pester enables infrastructure testing, but infrastructure tests are slower and more brittle than unit tests. Should infrastructure testing be part of the CI pipeline (where slow tests delay feedback) or run separately (where failures may be discovered too late)?
3. PowerShell's integration with Windows is deep and powerful, but Linux administration remains dominated by Bash and Python. Will PowerShell ever achieve parity with Bash on Linux, or will the two coexist as domain-specific tools?

---

## Lecture 10: Cross-Platform Scripting — Choosing the Right Tool for the Job

The modern IT environment is heterogeneous: Linux servers, Windows desktops, macOS laptops, embedded devices, and cloud services. This lecture provides a decision framework for choosing between Python, Bash, and PowerShell, and introduces patterns for writing scripts that run across platforms.

**Decision matrix:**
- **Linux-only server tasks** (log rotation, process monitoring, file management): Bash for simple tasks (<100 lines, no complex data structures), Python for complex tasks.
- **Windows-only server tasks** (Active Directory management, IIS configuration, registry manipulation): PowerShell is the clear choice.
- **Cross-platform server tasks** (API interaction, data processing, cloud resource management): Python is the most portable choice.
- **Quick one-liners and interactive exploration**: Bash on Linux, PowerShell on Windows.
- **Configuration management and orchestration**: Ansible (Python-based) for Linux, DSC (PowerShell-based) for Windows, Terraform (HCL) for cloud-agnostic infrastructure.
- **High-performance networking**: Python with asyncio, or Go (which compiles to a single binary and is increasingly popular for IT tools).

**Writing portable scripts** requires discipline. **Python portability** is generally excellent: the same script runs on Linux, Windows, and macOS with minimal changes. Key considerations: use `pathlib` instead of hardcoded paths; use `os.pathsep` and `os.linesep` for platform-specific separators; use `subprocess` with lists (not shell strings) to avoid shell syntax differences; and handle line endings (Windows CRLF vs. Unix LF). **Cross-platform Bash** is possible but limited: Git Bash and WSL (Windows Subsystem for Linux) provide Bash on Windows, but native Windows tools have different command-line syntax. **Cross-platform PowerShell** (PowerShell Core) runs on Linux but lacks many Windows-specific cmdlets.

**Hybrid scripts** combine languages for maximum effect. A common pattern: a Python script orchestrates the workflow, calling Bash scripts on Linux nodes and PowerShell scripts on Windows nodes. **Polyglot pipelines** use the right tool for each step: Bash for text processing, Python for data analysis, PowerShell for Windows management, and Go for high-performance components. The **Yggdrasil Standard Automation Stack** is a polyglot framework: Python provides the orchestration layer; Bash modules handle Linux-specific tasks; PowerShell modules handle Windows-specific tasks; and all modules communicate through a shared JSON interface.

**The future of IT scripting** in 2040 includes **AI-assisted code generation** (GitHub Copilot, Amazon CodeWhisperer, and the University's *Skald* assistant generate Bash, Python, and PowerShell from natural language descriptions). While AI accelerates development, it also introduces risks: generated code may contain subtle bugs, security vulnerabilities, or deprecated patterns. The IT professional must remain the **critical reviewer** of AI-generated scripts, not merely the requester.

**Lab Exercise:** Students write a **cross-platform server inventory script**. The script: detects the operating system (Linux or Windows); collects system information (hostname, OS version, CPU model, total memory, disk usage, running services); formats the data as JSON; and uploads it to a central API. On Linux, it uses Python with `psutil` and `subprocess`; on Windows, it uses Python with `wmi` or `pywin32`. The script must handle errors gracefully, retry failed uploads, and log its actions.

**Required Reading:**
- Al Sweigart, *Automate the Boring Stuff with Python* (2nd ed.), ch. 6 ("Manipulating Strings") and ch. 10 ("Organising Files")
- Brendan Gregg, *BPF Performance Tools* (Addison-Wesley, 2019/2035), ch. 1 ("Introduction") — for Linux performance scripting
- Don Jones, "The Monad Manifesto" (Microsoft, 2002/2035) — the original vision for PowerShell
- University of Yggdrasil, "The Standard Automation Stack: A Polyglot Framework for Heterogeneous Environments" (2039)

**Discussion Questions:**
1. In a heterogeneous environment, is it better to standardise on one language (e.g., Python for everything) and accept the limitations on certain platforms, or to embrace polyglot scripting and manage the complexity of multiple languages?
2. AI code generation promises to eliminate the need to learn syntax, but it also produces code that the user may not fully understand. Is AI-assisted scripting a genuine productivity gain, or does it create a generation of administrators who cannot debug the code they deploy?
3. Go is increasingly popular for IT tools (Docker, Kubernetes, Terraform are all written in Go). Should Python, Bash, and PowerShell administrators learn Go, or is it a specialist language that does not belong in the general IT toolkit?

---

## Lecture 11: Version Control, Testing, and Documentation for IT Scripts

Professional scripts are not written once and forgotten; they are maintained, improved, and shared. This lecture covers the software engineering practices that distinguish professional automation from throwaway hacks.

**Version control** with **Git** is mandatory for IT scripts. A Git repository for automation scripts should: have a clear directory structure (`scripts/`, `modules/`, `configs/`, `tests/`, `docs/`); use meaningful commit messages ("Fix memory threshold in health_check.py" not "Update"); follow a branching strategy (e.g., GitFlow or trunk-based development); and include a README with installation instructions, usage examples, and contribution guidelines. **Git hooks** can enforce code quality: pre-commit hooks run linters (pylint, flake8, shellcheck, PSScriptAnalyzer) before allowing commits. **GitLab CI/CD** or **GitHub Actions** can run tests and deploy scripts automatically. In 2040, **the University's automation repositories** are public (where appropriate) and follow the same standards as open-source projects.

**Testing** ensures that scripts behave correctly. **Unit tests** verify individual functions in isolation (using **pytest** for Python, **bats** for Bash, **Pester** for PowerShell). **Integration tests** verify that scripts interact correctly with external systems (databases, APIs, file systems). **Linting** (`pylint`, `flake8`, `black`, `mypy` for Python; `shellcheck` for Bash; `PSScriptAnalyzer` for PowerShell) catches syntax errors, style violations, and potential bugs before execution. **Static analysis** (`bandit` for Python security scanning; `psalm` for type checking) identifies vulnerabilities and type mismatches. In 2040, **AI-assisted testing** (e.g., **Hypothesis** for property-based testing, which generates random inputs to find edge cases) is standard for critical scripts.

**Documentation** is the bridge between the script author and future maintainers. **Inline comments** explain *why* (not *what* — the code should explain what). **Docstrings** (Python) or **comment-based help** (PowerShell) document functions, parameters, and return values. **README files** provide installation, usage, and troubleshooting guidance. **CHANGELOG** files track versions and changes. **Architecture Decision Records (ADRs)** document why specific technologies or approaches were chosen. In 2040, **AI-assisted documentation** (e.g., tools that generate docstrings from code analysis) reduces the burden, but human review remains essential.

**Lab Exercise:** Students take a "spaghetti script" (a poorly written, undocumented Bash script provided by the instructors) and refactor it into a professional-quality Python module: add functions with docstrings; write pytest unit tests; add type hints; run pylint and mypy; write a README; and commit the changes to Git with meaningful messages. This exercise teaches that professional scripting is not about writing new code but about maintaining and improving existing code.

**Required Reading:**
- Karl Fogel, *Producing Open Source Software* (2nd ed., O'Reilly, 2017/2035), ch. 4 ("Social and Political Infrastructure") and ch. 6 ("Communications")
- Brian Okken, *Python Testing with pytest* (2nd ed., Pragmatic Bookshelf, 2022/2035), ch. 1–4
- Michael W. Lucas, *PAM Mastery* (Tilted Windmill Press, 2035) — for understanding the Unix authentication stack that many scripts interact with
- University of Yggdrasil, "IT Automation Style Guide: Git, Testing, and Documentation Standards" (2039)

**Discussion Questions:**
1. Many IT professionals view version control as unnecessary for "just a script." Is this attitude justified for small scripts, or does it create a culture where critical automation is unmaintainable?
2. Testing IT scripts is difficult because they interact with external systems (databases, APIs, file systems) that are hard to mock. Are integration tests worth the effort for scripts, or is manual testing sufficient?
3. Documentation is often neglected because it is not immediately rewarding. What organisational incentives (or disincentives) would encourage IT professionals to document their scripts properly?

---

## Lecture 12: Automation Architecture — Designing Reliable, Scalable, and Maintainable Systems

The final lecture synthesises the course into a holistic view of automation architecture. A collection of scripts is not an automation system; a system requires design principles that ensure reliability, scalability, and maintainability.

**Reliability** means that automation works correctly and consistently. **Idempotency** (applying the same operation multiple times produces the same result) is the foundational principle: a script that installs a package should check if it is already installed before attempting installation. **Error handling** (graceful degradation, retries with exponential backoff, circuit breakers) prevents cascading failures. **Observability** (logging, metrics, tracing) enables operators to understand what the automation is doing and why it failed. **State management** (storing state in databases, files, or configuration management systems) ensures that automation can resume after interruption. In 2040, **event-driven architectures** (using message queues like RabbitMQ, Apache Kafka, or cloud-native services like AWS EventBridge) decouple automation components and improve resilience.

**Scalability** means that automation can handle growth. **Horizontal scaling** (adding more workers) is preferred over **vertical scaling** (bigger machines). **Distributed execution** (Ansible with multiple forks, Celery workers, Kubernetes Jobs) parallelises work across machines. **Caching** (memoising expensive operations) reduces redundant work. **Lazy evaluation** (computing results only when needed) conserves resources. **Asynchronous processing** (queues, callbacks, event loops) prevents blocking and improves throughput. The **Yggdrasil Automation Platform** (built on Kubernetes, RabbitMQ, and Python) scales from managing 10 servers to 10,000 by adding worker pods dynamically.

**Maintainability** means that automation can be understood, modified, and extended by people other than the original author. **Modularity** (small, focused functions and modules) reduces cognitive load. **Abstraction** (hiding implementation details behind clear interfaces) enables changes without breaking consumers. **Configuration externalisation** (storing environment-specific settings in files or databases, not hardcoded in scripts) enables the same code to run in development, staging, and production. **Dependency management** (pinning package versions, using virtual environments, containerising scripts) prevents "it works on my machine" problems. In 2040, **AI-assisted refactoring** (tools that suggest code improvements, detect dead code, and modernise deprecated patterns) augments human maintainers.

**The Yggdrasil Automation Philosophy** — codified in the University's IT runbook — emphasises: **start simple** (Bash for one-off tasks, Python for recurring tasks, dedicated platforms for enterprise orchestration); **compose, don't duplicate** (reuse existing modules and tools); **fail fast and loud** (scripts should exit with descriptive errors, not silently corrupt data); **audit everything** (every automated action is logged and attributable); and **design for humans** (automation should reduce toil, not create new forms of it). The IT105 course culminates in a **capstone project**: students design and implement an automation system for a real University operational problem (e.g., automated software license auditing, dynamic classroom scheduling, or predictive maintenance for lab equipment).

**Required Reading:**
- Niall Murphy et al., *Site Reliability Engineering: How Google Runs Production Systems* (O'Reilly, 2016/2035), ch. 6 ("Monitoring Distributed Systems"), ch. 8 ("Release Engineering")
- Gene Kim et al., *The DevOps Handbook* (2nd ed., IT Revolution, 2021/2035), ch. 7 ("The Three Ways")
- Charity Majors et al., *Observability Engineering* (O'Reilly, 2022/2035), ch. 1–3
- Mark Burgess, *In Search of Certainty: The Science of Our Information Infrastructure* (2nd ed., xt Axis Press, 2035), ch. 4 ("Promises and Implications")
- University of Yggdrasil, "The Yggdrasil Automation Philosophy: Principles and Practices" (2040)

**Discussion Questions:**
1. Reliability, scalability, and maintainability are often in tension: making a system more reliable (e.g., adding retries) can reduce maintainability (more complex code). How should automation architects balance these competing concerns?
2. Event-driven architectures improve resilience but introduce new failure modes (lost messages, duplicate processing, out-of-order events). Are event-driven systems fundamentally more complex than synchronous systems, or is the complexity merely shifted?
3. The Yggdrasil Automation Philosophy emphasises "design for humans." In an era of AI-generated automation, does the human operator remain the primary user, or should automation be designed primarily for machine-to-machine interaction?

---

## Final Examination Preparation

The final examination for IT105 is a **practical coding assessment** (4 hours, 60% of grade) combined with a **code review and architecture document** (40% of grade).

**Practical Coding Assessment (60%):**
Students receive a scenario (e.g., "A new web application has been deployed. Write automation to: monitor its health, rotate its logs, back up its database nightly, and alert the team on failure") and must implement a complete solution using Python, Bash, or PowerShell (or a combination). The solution is evaluated on: correctness (does it work?); robustness (does it handle errors?); readability (can another administrator understand it?); and professionalism (is it tested, documented, and version-controlled?).

**Code Review and Architecture Document (40%):**
Students submit their capstone project (or the practical assessment solution) along with: a README explaining the design; a test suite with ≥80% coverage; and an architecture document (500 words) explaining the design decisions, trade-offs, and future extensions.

**Sample Practical Scenarios:**

1. **Log Anomaly Detection:** Write a Python script that tails an Apache log file in real time, detects anomalous request patterns (e.g., sudden spikes in 404 errors, repeated login failures from a single IP), and sends alerts to a Slack webhook. The script must run continuously, handle log rotation, and be resilient to temporary network failures.

2. **Cross-Platform User Provisioning:** Write a script (Python + Bash/PowerShell) that reads a CSV file of new employees and creates their accounts on both Linux (LDAP) and Windows (Active Directory) systems. The script must generate random passwords, enforce complexity requirements, and email credentials securely.

3. **Infrastructure Health Dashboard:** Write a Python script using asyncio that collects health metrics (CPU, memory, disk, network) from 50 servers concurrently, stores the results in a SQLite database, and generates a static HTML dashboard with tables and charts. The script must complete in under 30 seconds.

**Grading:**
- A (Excellent): Correct, robust, readable, and professional code. Architecture document demonstrates deep understanding of trade-offs. Code review reveals no significant issues.
- B (Good): Correct and robust code with minor readability or documentation gaps. Architecture document is competent but lacks depth.
- C (Satisfactory): Code works but has significant gaps in error handling, testing, or documentation. Architecture document is superficial.
- D (Poor): Code has functional errors or is poorly structured. Little or no testing or documentation.
- F (Fail): Code does not work or is missing. No architecture document.
