# SA105: Scripting for SysAdmins (Bash, Python, PowerShell)
## Bachelor of Science in Computer Systems Administration — University of Yggdrasil, 2040

**Credits:** 4
**Prerequisites:** SA101 (Introduction to Systems Administration)
**Description:** Hands-on scripting course covering Bash, Python, and PowerShell for systems administration tasks. Students learn to automate deployment, monitoring, user management, backup, and reporting across Linux and Windows environments. The course emphasizes idempotent scripting, error handling, logging, and the transition from one-off scripts to maintainable automation tooling.

**Instructor:** Dr. Sigrid Torfsdóttir, Senior Platform Engineer & Scripting Architect, Bifrǫst Mesh Automation Team
**Lab:** Mjölnir Systems Lab, Sublevel 2, Hákon Computing Centre
**Office Hours:** Wednesdays 14:00-16:00, or by appointment

---

## Lectures

ᚠ **Lecture 1: The Scripting Mindset — From Manual to Automated Infrastructure**

**Course:** SA105 — Scripting for SysAdmins (Bash, Python, PowerShell)
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

This opening lecture establishes the philosophical and practical foundations of scripting for systems administration. The transition from manual system management to automated infrastructure is not merely a technical upgrade — it represents a fundamental shift in how administrators think about their craft. Where the 2010s SA typed commands into terminals and kept runbooks in wikis, the 2040 SA writes code that defines desired state, and automated systems enforce it. This lecture examines why scripting is the single most impactful skill a systems administrator can develop, how the three major scripting languages (Bash, Python, PowerShell) complement each other, and the design principles that distinguish a useful automation script from unmaintainable spaghetti code.

### Key Topics

- **The Automation Imperative:** In 2040, an SA who cannot script is effectively disabled. The ratio of servers to administrators has grown from 50:1 in the 2010s to 10,000:1 in large environments. Manual administration does not scale. The Yggdrasil Bifrǫst Mesh operates approximately 14,000 nodes with a team of 22 SAs — a ratio of roughly 636:1 — achieved entirely through automation and self-healing orchestration. Every manual task that cannot be scripted is a bottleneck that prevents scaling.

- **Three Languages, Three Ecosystems:** Bash excels at gluing Unix tools together and handling file/system operations quickly; Python provides rich libraries, data structures, and cross-platform capability; PowerShell offers deep integration with Windows, .NET, and Microsoft's management frameworks. An effective 2040 SA is fluent in all three and chooses the right language for each task.

- **Idempotency and Convergence:** The core principle of infrastructure automation — running a script twice produces the same result as running it once. This lecture introduces idempotency as a design requirement, not an aspiration. If your script creates a user, it must check whether the user already exists. If it writes a configuration file, it must compare content before overwriting. Idempotent scripts are safe to run repeatedly, scheduled, or in parallel.

- **The SA Scripting Spectrum:** From one-liners in the terminal, through saved scripts in version control, to shared modules in organization-wide repositories, to self-healing automation that runs without human intervention. Where does a script stop being a "script" and start being "software"? The answer: when other people depend on it.

- **Version Control for Scripts:** Every script belongs in Git. This is non-negotiable. Scripts in home directories are organizational debt. The lecture introduces Git workflows for SA scripts: feature branches, code review, tagging for production deployment, and the script-as-code philosophy.

### Lecture Notes

The discipline of scripting for systems administration differs fundamentally from software development. Software developers write code that will be read, tested, and maintained by other developers; systems administrators write code that will be run by cron jobs at 03:00, by automation pipelines during incidents, and by colleagues who may not understand its assumptions. This distinction shapes every design decision.

Consider the humble `grep` pipeline. A sysadmin investigating a service failure might type:

```
journalctl -u nginx --since "1 hour ago" | grep -i error | awk '{print $5}' | sort | uniq -c | sort -rn | head -20
```

This is a one-liner — powerful, expressive, and completely unmaintainable. It works for the person who wrote it, in the moment, on that system. It will not work next week, on a different system, for a different person, who does not know why `awk '{print $5}'` was chosen over `awk '{print $3}'`. The journey from one-liner to production script is the journey this course undertakes.

In 2040, the Yggdrasil operations team manages over 14,000 nodes. Each morning, roughly 30 scripts run automatically to verify system health, rotate logs, check certificate expiry dates, validate configuration drift, and test backup integrity. Each of these scripts was written by an SA, reviewed by a peer, tested in staging, and deployed through the same CI/CD pipeline used for application code. The scripting culture at Yggdrasil — and at leading technology organizations worldwide — treats SA scripts as production software. This course will teach you to write at that standard.

The three languages covered in this course serve complementary purposes. Bash is the lingua franca of Linux systems: every Linux system has Bash, and many administrative tasks can be expressed as pipelines of standard Unix tools. Python is the Swiss Army knife: with libraries like `paramiko` (SSH), `requests` (HTTP), `psutil` (process information), and `boto3` (AWS), Python can automate virtually any administrative task on any platform. PowerShell is the key to the Windows ecosystem: if you manage Windows servers, Active Directory, Exchange, or Azure, PowerShell is not optional — it is the primary management interface.

### Required Reading

- Owens, M. & Limoncelli, T.A. (2037). *The Practice of System Administration: Scripting Edition*, 2nd Edition. Addison-Wesley. Chapters 1-2.
- Beyer, B., Rensin, C., & Kawamoto, K. (2036). *Site Reliability Engineering: Automation Patterns*. O'Reilly. Chapter 4.
- Yggdrasil Automation Standards (2040). UoY Digital Press. Section 2: "Script Lifecycle Management."

### Discussion Questions

1. A colleague argues that "real admins don't need scripts — they know the commands." How do you respond? What data would you use to demonstrate the value of scripting?
2. An idempotent script to create users checks whether the user exists before creating. But what if the existing user has different attributes than the script specifies (wrong shell, wrong group)? Should the script update the user, warn, or skip?
3. When does a script become "software"? Where do you draw the line between a script and an application, and how does that distinction affect your development practices?

---

ᚢ **Lecture 2: Bash Fundamentals — Variables, Flow Control, and Functions**

**Course:** SA105 — Scripting for SysAdmins (Bash, Python, PowerShell)
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Bash remains the most widely deployed shell on Linux systems in 2040, and every systems administrator must be fluent in Bash scripting. This lecture covers the essential building blocks: variable assignment and expansion, conditional logic with `if`/`case`, loops (`for`, `while`, `until`), and function definitions. We emphasizes shell-specific pitfalls — word splitting, glob expansion, command substitution, and the subtle differences between `[[ ]]` and `[ ]` — that trip up even experienced administrators. By the end of this lecture, students will write idempotent Bash scripts that check system state before making changes.

### Key Topics

- **Variables and Expansion:** Bash variables are untyped strings by default; numeric operations require explicit syntax (`(( ))` or `let`). Special variables (`$?`, `$!`, `$$`, `$#`, `$@`, `$*`) and their distinct behaviors. The difference between single quotes (literal), double quotes (with expansion), and unquoted (subject to word splitting and glob expansion). The `declare` built-in for typed variables (`-r` for readonly, `-i` for integer, `-a` for indexed array, `-A` for associative array).

- **Conditional Logic:** The `if` statement with `[[ ]]` (Bash keyword, supports pattern matching and logical operators) vs. `[ ]` (external command, POSIX-compatible but limited). The `case` statement for multi-branch logic. Test operators for files (`-f`, `-d`, `-e`, `-r`, `-w`, `-x`), strings (`-z`, `-n`, `=`, `!=`), and integers (`-eq`, `-lt`, `-gt`). Short-circuit evaluation with `&&` and `||`.

- **Loops and Iteration:** `for` loops over lists, ranges (`{1..10}`, `{a..z}`), and command output (`for file in $(find ...)` — dangerous, use `while read` with `find -print0` instead). `while` loops for reading input and daemon-like behavior. `until` loops as the inverse of `while`. `break` and `continue` for loop control.

- **Functions:** Defining functions with `function name {}` or `name() {}`. Positional parameters within functions (`$1`, `$2`, ...). `local` variables to avoid polluting the global namespace. Return values via `return` (exit status, 0-255) vs. capturing output via command substitution. The pattern of writing functions that output data on stdout and return success/failure on exit status.

- **Exit Status and Error Handling:** Every command returns an exit status. `$?` captures the last command's status. The `set -e` (exit on error), `set -u` (error on undefined variable), `set -o pipefail` (pipeline fails if any command in it fails) trinity. Custom error handling with `trap` for cleanup on exit, interrupt, or error.

### Lecture Notes

The most dangerous Bash script is one that appears to work but fails silently under specific conditions. Consider this common pattern for checking whether a package is installed:

```bash
if rpm -q nginx; then
    echo "nginx is installed"
fi
```

This works on Red Hat systems. On Debian systems, `rpm` does not exist, and the script fails with a misleading "package not installed" message. The idempotent, portable version checks both package managers:

```bash
if command -v nginx &>/dev/null; then
    echo "nginx is available"
elif rpm -q nginx &>/dev/null || dpkg -s nginx &>/dev/null; then
    echo "nginx is installed but not in PATH"
else
    echo "nginx is not installed"
fi
```

Word splitting is Bash's most common source of bugs. When a variable contains spaces and is used unquoted, Bash splits it into multiple words:

```bash
filename="My Document.pdf"
rm $filename    # Expands to: rm My Document.pdf — removes two files!
rm "$filename"  # Expands to: rm "My Document.pdf" — correct
```

The rule is simple: always quote variable expansions unless you explicitly want word splitting and glob expansion. This single rule prevents more Bash bugs than any other.

Functions in Bash should be small, named descriptively, and output data on stdout while signaling success or failure through exit status. This separation allows composition:

```bash
check_disk_space() {
    local threshold="${1:-90}"  # Default 90%
    local partition="${2:-/}"
    local usage
    usage=$(df -P "$partition" | awk 'NR==2{gsub(/%/,""); print $5}')
    if [ "$usage" -ge "$threshold" ]; then
        echo "CRITICAL: ${partition} is ${usage}% full (threshold: ${threshold}%)"
        return 1
    fi
    echo "OK: ${partition} is ${usage}% full"
    return 0
}

# Compose with alerting
if ! check_disk_space 85 /var; then
    send_alert "Disk space critical on $(hostname)"
fi
```

### Required Reading

- Cooper, M. (2038). *Advanced Bash-Scripting Guide*, 7th Edition. Linux Documentation Project. Chapters 1-5, 8-9.
- Peek, J. et al. (2036). *Bash Pocket Reference*, 4th Edition. O'Reilly.
- Yggdrasil Shell Scripting Standards (2040). Section 3: "Quoting, Variables, and Error Handling."

### Discussion Questions

1. Why is `set -euo pipefail` considered the minimum safe configuration for production Bash scripts? What are the arguments against each flag?
2. Bash functions return exit status (0-255) and output data on stdout. Python functions return values directly. What are the design implications of this difference for system administration scripts?
3. Write a Bash function that checks whether a service is running and, if not, attempts to restart it and sends an alert. What edge cases must you handle?

---

ᚦ **Lecture 3: Bash in Practice — Pipes, Redirection, Text Processing, and Automation**

**Course:** SA105 — Scripting for SysAdmins (Bash, Python, PowerShell)
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

If Lecture 2 established Bash's syntax, this lecture applies it to the real-world tasks systems administrators perform daily: processing logs, extracting data from command output, automating repetitive maintenance, and building pipelines that transform raw system data into actionable intelligence. We cover Unix pipeline philosophy, standard I/O redirection, process substitution, and the essential text-processing tools (`grep`, `sed`, `awk`, `cut`, `sort`, `uniq`, `tr`, `xargs`). Students learn to compose pipelines that solve real SA problems: finding disk hogs, detecting configuration drift, parsing application logs, and generating system reports.

### Key Topics

- **Pipeline Philosophy:** Doug McIlroy's Unix philosophy: "Write programs that do one thing and do it well; write programs to work together; write programs to handle text streams, because that is a universal interface." Pipelines as data transformation chains: each command is a filter that transforms a stream. Stdin/stdout as the universal interface between tools.

- **Redirection and File Descriptors:** Standard input (fd 0), standard output (fd 1), standard error (fd 2). Redirecting output (`>`, `>>`), input (`<`), and appending. The `2>&1` pattern to merge stderr into stdout. The `&>` redirection (Bash-specific) for redirecting both. Here-documents (`<< EOF`) and here-strings (`<<<`). Process substitution (`<()`, `>()`) for using pipelines as arguments.

- **grep, sed, and awk — The Text Processing Trinity:** `grep` for filtering lines (basic, extended, and Perl-compatible regular expressions). `sed` for stream editing — substitution, deletion, and line-based transforms. `awk` for field-based processing — the lingua franca of structured text. Patterns like `awk '{print $2}'`, `awk -F: '$3 >= 1000 {print $1}' /etc/passwd`, and `awk '{sum+=$1} END{print sum}'`.

- **sort, uniq, cut, tr, xargs — The Supporting Cast:** `sort` with its many options (`-n` numeric, `-k` key, `-r` reverse, `-u` unique). `uniq` for deduplication (requires sorted input). `cut` for field extraction. `tr` for character translation and deletion. `xargs` for converting stdin into command arguments, with `-0` for null-delimited input and `-P` for parallel execution.

- **Real-World Pipeline Patterns:** Finding the top 10 disk consumers: `du -sh /home/* | sort -rh | head -10`. Extracting error rates from logs: `grep -c "ERROR" /var/log/app.log`. Detecting failed logins: `grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -rn | head -20`. Automated reporting: a daily cron job that collects system metrics and emails a summary.

- **Automation with cron and systemd timers:** The traditional `cron` format (5 time fields + command) and its limitations (no second precision, no built-in logging, environment variable surprises). `systemd` timers as the 2040 replacement: `OnCalendar=` for calendar-based scheduling, `OnBootSec=` for boot-based delays, `AccuracySec=` for timer precision, and built-in logging to the journal.

### Lecture Notes

The power of Unix pipelines lies in their composability. A single `awk` one-liner can replace hundreds of lines of Python for structured text processing. But composability requires discipline: each command in the pipeline must produce clean, predictable output.

Consider a practical example: the Yggdrasil Bifrǫst Mesh needs a daily report of SSL certificates expiring within 30 days. A Bash pipeline solution:

```bash
#!/usr/bin/env bash
set -euo pipefail

# Find certificates expiring within 30 days
DAYS_THRESHOLD=30
ALERT_EMAIL="ops@yggdrasil.edu"

find /etc/pki /etc/ssl /etc/letsencrypt/live -name '*.pem' -o -name '*.crt' 2>/dev/null | \
    while read -r cert; do
        if openssl x509 -checkend $((DAYS_THRESHOLD * 86400)) -noout -in "$cert" 2>/dev/null; then
            :  # Certificate is still valid, no action needed
        else
            expiry=$(openssl x509 -enddate -noout -in "$cert" | cut -d= -f2)
            subject=$(openssl x509 -subject -noout -in "$cert" | cut -d= -f2-)
            echo "EXPIRING: $cert - Subject: $subject - Expires: $expiry"
        fi
    done | \
    mail -s "[$(hostname)] Certificate Expiry Warning" "$ALERT_EMAIL"
```

This script demonstrates multiple Bash scripting principles: `set -euo pipefail` for safety, `while read -r` for safe line-by-line processing, `2>/dev/null` to suppress expected errors (directories without certificates), and a structured pipeline that produces a concise report.

The transition from cron to systemd timers exemplifies how Linux administration evolves while preserving backwards compatibility. Cron still works in 2040, and many administrators default to it out of habit. But systemd timers offer superior features: precise scheduling (sub-second accuracy), automatic logging to the journal, persistence across reboots, dependency ordering (`After=network.target`), and built-in random delay to prevent the "thundering herd" of cron jobs all firing at the top of the minute. The Yggdrasil operations team migrated all scheduled tasks to systemd timers in 2037.

### Required Reading

- Robbins, A.D. (2037). *Effective awk Programming*, 5th Edition. O'Reilly. Chapters 1-3.
- Dougherty, D. & Robbins, A. (2036). *sed & awk Pocket Reference*, 3rd Edition. O'Reilly.
- Yggdrasil Operations Guide (2040). Chapter 5: "Pipeline Patterns for System Health Checks."

### Discussion Questions

1. When is a Bash pipeline the wrong tool? Identify scenarios where you should switch to Python instead of chaining more Unix tools together.
2. A colleague writes: `for f in $(find . -name "*.log"); do gzip "$f"; done`. Explain three problems with this approach and write a corrected version.
3. Design a daily cron job (or systemd timer unit) that monitors disk usage on all mounted filesystems and sends an alert when any filesystem exceeds 85% capacity. What edge cases must you handle (NFS mounts, read-only filesystems, virtual filesystems)?

---

ᚨ **Lecture 4: Bash Script Design — Error Handling, Logging, and Production Patterns**

**Course:** SA105 — Scripting for SysAdmins (Bash, Python, Perl, PowerShell)
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

A script that works when everything goes right is a prototype. A production-quality script works when things go wrong — when the network is down, the file doesn't exist, the command times out, or the user provides invalid input. This lecture covers Bash error handling in depth: the `set` built-in options, `trap` for cleanup, structured logging, argument validation, configuration management, and the patterns that distinguish production scripts from quick hacks. We also introduce the Yggdrasil Script Template, a standardized starting point for all operations scripts.

### Key Topics

- **The `set` Options for Safe Scripting:** `set -e` (errexit): exit immediately if a command fails. `set -u` (nounset): treat unset variables as errors. `set -o pipefail`: pipeline fails if any command in it fails. `set -x` (xtrace): print each command before executing it (invaluable for debugging). The combined `set -euo pipefail` as the minimum safe configuration. How `set -e` interacts with conditionals (`if`, `&&`, `||`) — commands whose failure is an expected condition will not trigger errexit.

- **trap — Structured Cleanup on Exit:** `trap 'cleanup_function' EXIT INT TERM` — execute cleanup when the script exits (normally or by signal). `trap -p` to display current traps. Common patterns: removing temporary files, releasing locks, restoring modified configuration, sending completion notifications. The `trap` command as the SA's insurance policy against half-finished operations.

- **Logging and Output Discipline:** A production script produces three types of output: normal output (stdout), errors (stderr), and a log file. The `logger` command for syslog integration. Structured logging with timestamps, severity levels (DEBUG, INFO, WARN, ERROR, CRITICAL), and structured data (JSON format). The pattern: functions output results on stdout, log progress on stderr, and the caller decides what to do with each stream.

- **Argument Parsing and Validation:** `getopts` for flag-style arguments (`-v`, `-f file`, `-n count`). Long options with manual parsing or the `getopt` external command. Input validation: check that required arguments exist, that file paths resolve, that numeric arguments are numeric, that IP addresses are valid. The principle: fail fast with a clear error message rather than produce mysterious failures downstream.

- **Configuration Management:** The `/etc/default/scriptname` pattern for environment-specific configuration. Separate configuration from logic. Use of `source` or `.` to include shared libraries. The `.env` file pattern for secrets (never committed to Git, always in `.gitignore`). The principle of twelve-factor configuration: environment variables for all configuration that varies between deployments.

- **The Yggdrasil Script Template:** Every operations script begins with a standard header: shebang, set options, trap definitions, logging functions, argument parsing, and a usage message. The template enforces best practices by default and makes it easy to write correct scripts.

### Lecture Notes

Consider the lifecycle of a real production script. The Yggdrasil certificate-renewal script runs every 12 hours. It must handle: certificates that are already renewed (skip), certificates that expired (alert, renew), ACME server unavailability (retry with backoff), DNS propagation delays (wait and verify), filesystem permission errors (alert and stop), and concurrent execution (acquire a lock file). Without proper error handling, any of these conditions could cause the script to fail silently, leaving certificates to expire unnoticed.

```bash
#!/usr/bin/env bash
# Yggdrasil Certificate Renewal Script
# Standard header follows...
set -euo pipefail

SCRIPT_NAME="$(basename "$0")"
LOCK_FILE="/var/lock/${SCRIPT_NAME}.lock"
LOG_TAG="cert-renewal"

# Logging functions
log_info()  { logger -t "$LOG_TAG" -p user.info "$@"; }
log_warn()  { logger -t "$LOG_TAG" -p user.warning "$@"; }
log_error() { logger -t "$LOG_TAG" -p user.err "$@"; }

# Cleanup function
cleanup() {
    rm -f "$LOCK_FILE"
    log_info "Certificate renewal check completed"
}
trap cleanup EXIT

# Acquire lock (prevent concurrent execution)
if ! (set -o noclobber; echo "$$" > "$LOCK_FILE") 2>/dev/null; then
    log_warn "Another instance is running, exiting"
    exit 0
fi

# Main logic with proper error handling
renew_certs() {
    local certbot_bin
    certbot_bin="$(command -v certbot || true)"
    if [ -z "$certbot_bin" ]; then
        log_error "certbot not found in PATH"
        return 1
    fi

    if "$certbot_bin" renew --quiet --deploy-hook "/usr/local/bin/cert-deploy.sh"; then
        log_info "Certificate renewal completed successfully"
    else
        local rc=$?
        log_error "Certificate renewal failed with exit code $rc"
        return $rc
    fi
}

renew_certs
```

This script demonstrates multiple production patterns: lock files for concurrency control, syslog integration for auditability, structured logging, error propagation, and trap-based cleanup. The lock file pattern using `noclobber` is atomic — it prevents race conditions where two instances start simultaneously. The `|| true` pattern on `command -v` prevents `set -e` from killing the script if certbot is not installed; instead, the empty check handles the missing binary gracefully.

### Required Reading

- Yggdrasil Operations Standards (2040). "The Script Template: How We Write Bash at Yggdrasil."
- Limoncelli, T.A. & Hogan, C.J. (2037). *The Practice of Cloud System Administration*, Chapter 7: "Error Handling, Logging, and the Production Script Lifecycle."
- Wikipedia contributors (2039). "Exit status" and "Signal (IPC)" articles — essential background on process exit conventions.

### Discussion Questions

1. Why does `set -e` not apply inside `if` conditions? How does this behavior enable proper error handling, and how can it be misused?
2. Design a lock file mechanism for a script that must never run concurrently. What happens if the server crashes while the lock is held? How do you detect and recover from stale locks?
3. A production script logs to both syslog and a local file. How do you handle log rotation? What are the tradeoffs between logging to syslog directly vs. using a log aggregation tool?

---

ᚱ **Lecture 5: Python for SysAdmins — Language Fundamentals and the Standard Library**

**Course:** SA105 — Scripting for SysAdmins (Bash, Python, PowerShell)
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Python has become the primary scripting language for systems administration in environments that need more than shell scripts can provide: cross-platform compatibility, complex data structures, network programming, API interaction, and maintainable codebases that grow beyond 200 lines. This lecture introduces Python from an SA perspective, focusing not on Python as a general programming language (covered in CS101-104) but on Python as an operations tool. We cover Python's type system, the standard library modules most relevant to SA work (`os`, `sys`, `pathlib`, `subprocess`, `shutil`, `json`, `csv`, `re`, `logging`, `argparse`), and the transition from Bash one-liners to Python scripts.

### Key Topics

- **Python's Advantages for SA Work:** Cross-platform by default (same script runs on Linux, macOS, Windows). Rich standard library ("batteries included"). Exception handling with `try/except` that is far more robust than Bash's error handling. Data structures (lists, dictionaries, sets) that make complex data manipulation natural. Type hints for documentation and static analysis. The `if __name__ == "__main__"` convention for testable scripts.

- **Filesystem Operations with `pathlib`:** The modern replacement for `os.path`. `Path` objects that support `/` for path composition. Methods like `.exists()`, `.is_file()`, `.is_dir()`, `.read_text()`, `.write_text()`, `.mkdir(parents=True, exist_ok=True)`. Globbing with `.glob()` and `.rglob()`. The idempotent `mkdir(parents=True, exist_ok=True)` pattern.

- **Running External Commands with `subprocess`:** The `subprocess.run()` function as the primary interface. `capture_output=True` for capturing stdout/stderr. `text=True` for string (vs. bytes) output. `check=True` to raise `CalledProcessError` on non-zero exit. The `subprocess.Popen()` class for long-running processes, piping, and real-time output. Security: `shell=True` is dangerous (shell injection); prefer list form `["cmd", "arg1", "arg2"]`.

- **Data Processing with `json` and `csv`:** Parsing JSON configuration files and API responses with `json.load()` and `json.loads()`. Writing structured output with `json.dump()` and `json.dumps()`. Reading and writing CSV data with `csv.reader()`, `csv.DictReader()`, and `csv.writer()`. The `csv` module's handling of edge cases (quoting, different delimiters) that would require complex `awk` in Bash.

- **Command-Line Interface with `argparse`:** Defining arguments, options, and subcommands. Type validation, default values, required vs. optional, mutually exclusive groups. Help text generation. The pattern of developing a consistent CLI for all SA scripts that matches organizational conventions.

- **Structured Logging with `logging`:** The standard library `logging` module: loggers, handlers, formatters, and levels (DEBUG, INFO, WARNING, ERROR, CRITICAL). Configuring both console output (for interactive use) and file output (for cron/automated use). JSON-formatted logging for ingestion by monitoring systems.

### Lecture Notes

The transition from Bash to Python typically follows a recognizable pattern. A sysadmin starts with a Bash one-liner. The one-liner grows into a script. The script grows into a script with functions. The script with functions grows to 300 lines, and maintaining it becomes painful — complex data structures are awkward in Bash, error handling is limited, and cross-platform compatibility requires conditional blocks for every OS. At this point, rewriting in Python saves time rather than costs it.

Consider a practical example: a script that checks all running services on a Linux system and reports any that are not in their expected state. In Bash, this might be:

```bash
#!/usr/bin/env bash
while read -r service; do
    if ! systemctl is-active --quiet "$service"; then
        echo "DOWN: $service"
    fi
done < /etc/yggdrasil/required-services.txt
```

This works for Linux systems using systemd. In Python, the same functionality becomes cross-platform, testable, and extensible:

```python
#!/usr/bin/env python3
"""Check that required services are running on this system."""
import subprocess
import sys
from pathlib import Path

REQUIRED_SERVICES = Path("/etc/yggdrasil/required-services.txt")

def check_service(service_name: str) -> bool:
    """Return True if the service is active."""
    result = subprocess.run(
        ["systemctl", "is-active", "--quiet", service_name],
        capture_output=True,
    )
    return result.returncode == 0

def main() -> None:
    if not REQUIRED_SERVICES.exists():
        print(f"ERROR: {REQUIRED_SERVICES} not found", file=sys.stderr)
        sys.exit(1)

    down_services = []
    for service in REQUIRED_SERVICES.read_text().splitlines():
        service = service.strip()
        if not service or service.startswith("#"):
            continue
        if not check_service(service):
            down_services.append(service)

    if down_services:
        print(f"DOWN: {', '.join(down_services)}")
        sys.exit(1)
    print("All required services are running")
    sys.exit(0)

if __name__ == "__main__":
    main()
```

The Python version is longer, but it handles comments in the input file, provides clear error messages, uses type hints, separates logic from output, and can be extended to send alerts, log results, or check services on remote hosts with minimal changes.

### Required Reading

- Python Software Foundation (2040). *Python Standard Library Reference*, Release 3.15. Sections: `os`, `sys`, `pathlib`, `subprocess`, `json`, `argparse`.
- Van Lindberg, M. (2038). *Python for System Administration*, 2nd Edition. O'Reilly. Chapters 1-4.
- Yggdrasil Engineering Blog (2040, March). "When to Switch from Bash to Python: A Decision Framework."

### Discussion Questions

1. A colleague argues that Python scripts are "too heavy" for simple tasks and Bash should always be preferred for anything under 50 lines. When is this true, and when does Python's standard library make even a 10-line Python script better than a 10-line Bash pipeline?
2. `subprocess.run(shell=True)` is convenient but dangerous. Explain the shell injection vulnerability and demonstrate how a malicious input could compromise a system. Rewrite the vulnerable example using the safe list form.
3. Why does Python's `pathlib.Path` represent an improvement over `os.path` for SA scripts? Give three examples of operations that are cleaner with `pathlib`.

---

ᚲ **Lecture 6: Python for SA Automation — Files, Processes, Networking, and APIs**

**Course:** SA105 — Scripting for SysAdmins (Bash, Python, PowerShell)
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

This lecture extends Python SA scripting from fundamentals to the real-world automation tasks that occupy a sysadmin's workday: managing files and directories at scale, interacting with system processes, making network requests, and consuming REST APIs. We cover the Python modules and patterns that replace manual administration with automated workflows:批量 file operations, process supervision, health check scripts, configuration distribution, and API-based cloud management. Students also learn to write scripts that are idempotent, testable, and safe to run in production.

### Key Topics

- **Advanced File Operations:** `shutil` for high-level file operations: `copy2()` (preserves metadata), `move()`, `rmtree()`, `disk_usage()`. `tempfile` for temporary files and directories with automatic cleanup. `fileinput` for in-place file editing. `hashlib` for file integrity verification (SHA-256 checksums for configuration files, backups, and software distributions). `stat` for examining file permissions, ownership, and timestamps.

- **Process Management and Supervision:** `subprocess.Popen()` for advanced process control: real-time output streaming, background processes, signal handling. `os.kill()` and `signal` module for sending signals to processes. `psutil` (third-party, included in Yggdrasil's base Python environment) for process inspection: listing processes by name, checking resource usage, and killing hung processes. The pattern of "start, verify, notify" for service management scripts.

- **Networking with `socket` and `http`:** `socket` for low-level network operations: checking port availability, testing TCP connectivity. `urllib.request` and the `requests` library for HTTP interactions. Health check scripts that verify service availability across multiple endpoints. Timeout handling and retry logic with exponential backoff. The difference between a service listening on a port and a service being healthy.

- **REST API Consumption:** Authenticating with APIs (API keys, OAuth2 tokens, TLS client certificates). Parsing JSON responses into Python dictionaries. Pagination handling for APIs that return results in pages. Rate limiting and throttling. The `requests.Session()` pattern for connection pooling and persistent headers. Error handling for HTTP status codes, network timeouts, and malformed responses.

- **Configuration Distribution:** Scripts that fetch configuration from a central source (Git repository, config server, object storage), validate the configuration (syntax check, schema validation), deploy to target systems, and restart affected services. The atomic deployment pattern: write to a temporary file, validate, rename (atomic on POSIX filesystems), restart service. Rollback: keep previous configuration version and revert if service health check fails.

- **Parallel Execution with `concurrent.futures`:** `ThreadPoolExecutor` and `ProcessPoolExecutor` for running operations on multiple systems concurrently. The difference between I/O-bound (use threads) and CPU-bound (use processes) operations. `concurrent.futures.as_completed()` for processing results as they arrive. Practical example: checking disk space on 100 servers in parallel instead of sequentially.

### Lecture Notes

The atomic deployment pattern is one of the most important operational patterns a sysadmin can learn. It prevents the "half-written configuration" problem that causes service failures. The pattern is:

```python
#!/usr/bin/env python3
"""Deploy a configuration file atomically with automatic rollback."""
import hashlib
import shutil
import tempfile
from pathlib import Path
import subprocess
import sys

CONFIG_SOURCE = Path("/opt/config-repo/production/nginx.conf")
CONFIG_TARGET = Path("/etc/nginx/nginx.conf")
BACKUP_DIR = Path("/etc/nginx/backups")
SERVICE_NAME = "nginx"

def file_hash(path: Path) -> str:
    """Return SHA-256 hash of a file."""
    return hashlib.sha256(path.read_bytes()).hexdigest()

def deploy_config() -> None:
    # Validate source configuration
    if not CONFIG_SOURCE.exists():
        print(f"ERROR: Source config {CONFIG_SOURCE} not found", file=sys.stderr)
        sys.exit(1)

    # Check if configuration changed
    if CONFIG_TARGET.exists() and file_hash(CONFIG_SOURCE) == file_hash(CONFIG_TARGET):
        print("Configuration unchanged, nothing to do")
        return

    # Backup current configuration
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    if CONFIG_TARGET.exists():
        backup_path = BACKUP_DIR / f"nginx.conf.{file_hash(CONFIG_TARGET)[:8]}"
        shutil.copy2(CONFIG_TARGET, backup_path)

    # Atomic write: temp file → validate → rename
    with tempfile.NamedTemporaryFile(
        dir=CONFIG_TARGET.parent,
        prefix=".nginx.conf.",
        suffix=".tmp",
        delete=False,
        mode="w",
    ) as tmp:
        tmp.write(CONFIG_SOURCE.read_text())
        tmp_path = Path(tmp.name)

    # Validate syntax before deploying
    result = subprocess.run(
        ["nginx", "-t", "-c", str(tmp_path)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"ERROR: Configuration validation failed:\n{result.stderr}", file=sys.stderr)
        tmp_path.unlink()
        sys.exit(1)

    # Atomic rename (POSIX guarantees atomicity on same filesystem)
    tmp_path.rename(CONFIG_TARGET)

    # Restart service
    subprocess.run(["systemctl", "reload", SERVICE_NAME], check=True)
    print("Configuration deployed and service reloaded successfully")

if __name__ == "__main__":
    deploy_config()
```

This script exemplifies the production patterns discussed throughout the course: validation before deployment, atomic file operations, automatic backup, clear error reporting, and idempotent behavior (skips if configuration unchanged).

### Required Reading

- Van Lindberg, M. (2038). *Python for System Administration*, 2nd Edition. O'Reilly. Chapters 5-7.
- Yggdrasil Engineering Standards (2040). "Atomic Deployment Patterns for Configuration Management."
- Python Software Foundation (2040). `concurrent.futures` documentation — Thread vs. Process pools.

### Discussion Questions

1. The atomic deployment pattern uses `rename()` for atomic replacement. Why is `rename()` atomic on POSIX filesystems? What happens on Windows? How would you handle atomic deployment on a Windows server?
2. When checking 100 servers for disk space, is it better to use threading or multiprocessing? Explain your answer in terms of the GIL, I/O wait, and the nature of the task.
3. Design a Python script that monitors a REST API endpoint and sends an alert when the response time exceeds 500ms or the status code is not 200. Include retry logic, exponential backoff, and a cooldown period to avoid alert fatigue.

---

ᛏ **Lecture 7: PowerShell Fundamentals — Objects, Pipelines, and Windows Administration**

**Course:** SA105 — Scripting for SysAdmins (Bash, Python, PowerShell)
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

PowerShell is the management backbone of the Windows ecosystem and an increasingly capable cross-platform tool (PowerShell 7+ on Linux and macOS). This lecture introduces PowerShell's unique paradigm — everything is an object, not text — and its implications for system administration. Where Bash pipelines pass text between commands, PowerShell pipelines pass structured .NET objects with properties and methods. This fundamental difference enables more precise, reliable, and discoverable administration scripts. We cover PowerShell fundamentals, the pipeline model, common administrative cmdlets, and the patterns for managing Windows servers, Active Directory, and Azure resources.

### Key Topics

- **The Object Pipeline — PowerShell's Core Innovation:** Unlike Bash, where command output must be parsed as text, PowerShell commands (cmdlets) emit .NET objects. `Get-Process` returns `System.Diagnostics.Process` objects with properties (CPU, WorkingSet, Id, ProcessName) and methods (Kill(), WaitForExit()). Pipeline objects preserve their structure. `$proc = Get-Process -Name nginx; $proc.CPU` accesses a specific property. This eliminates the parsing fragility of text-based tools.

- **Cmdlet Naming Convention:** The Verb-Noun pattern: `Get-Process`, `Set-ExecutionPolicy`, `New-Item`, `Remove-Item`, `Where-Object`, `Select-Object`. Standard verbs (Get, Set, New, Remove, Add, Remove, Start, Stop, Restart, Test) ensure discoverability. `Get-Command -Verb Get` lists all "get" cmdlets. `Get-Help Get-Process -Full` shows complete documentation.

- **Variables, Types, and Operators:** PowerShell variables (`$var`) are .NET objects with types. Automatic type conversion. Comparison operators: `-eq`, `-ne`, `-lt`, `-gt`, `-like` (wildcard), `-match` (regex), `-contains`, `-in`. Logical operators: `-and`, `-or`, `-not`. Array operations: `@()`, `+=`, `Where-Object`, `ForEach-Object`.

- **Common Administrative Cmdlets:** `Get-Service`, `Start-Service`, `Stop-Service`, `Restart-Service` for Windows services. `Get-Process`, `Stop-Process` for processes. `Get-EventLog`/`Get-WinEvent` for logs. `Get-Item`, `Set-Item`, `New-Item`, `Remove-Item` for filesystem. `Get-NetIPAddress`, `Test-NetConnection` for networking. `Get-ChildItem` (the `ls` equivalent). `Get-WmiObject`/`Get-CimInstance` for system information.

- **Active Directory Management:** `Get-ADUser`, `New-ADUser`, `Set-ADUser`, `Remove-ADUser` for user accounts. `Get-ADGroup`, `Add-ADGroupMember` for group management. `Get-ADComputer` for computer accounts. The `-Filter` parameter for LDAP queries. The `-Properties` parameter for accessing extended attributes. Bulk operations: importing users from CSV with `Import-Csv | ForEach-Object { New-ADUser ... }`.

- **Remote Management with PowerShell Remoting:** `Enter-PSSession` for interactive remote sessions. `Invoke-Command` for running scripts on remote machines. `New-PSSession` for persistent sessions. WinRM (Windows Remote Management) as the transport protocol. Constrained delegation for security. The `CimSession` for WMI-based remote management.

### Lecture Notes

The fundamental insight of PowerShell is that system administration should not require text parsing. In Bash, if you want to find processes consuming more than 1GB of memory, you must parse `ps` output:

```bash
ps aux | awk '$6 > 1048576 {print $11, $6/1024 "MB"}'
```

This works until `ps` output format changes, or a process name contains spaces, or the system uses a different locale. In PowerShell:

```powershell
Get-Process | Where-Object { $_.WorkingSet64 -gt 1GB } |
    Select-Object ProcessName, @{Name='MemoryMB';Expression={$_.WorkingSet64/1MB}}
```

This is self-documenting, type-safe, and impervious to output format changes because the `WorkingSet64` property is a .NET integer, not a text string that requires parsing.

The object pipeline also enables powerful filtering and transformation patterns:

```powershell
# Find all stopped services that should be running
Get-Service |
    Where-Object { $_.StartType -eq 'Automatic' -and $_.Status -ne 'Running' } |
    Select-Object Name, DisplayName, Status |
    Format-Table -AutoSize

# List all AD users whose passwords expire within 7 days
Get-ADUser -Filter * -Properties PasswordNeverExpires, PasswordLastSet |
    Where-Object {
        -not $_.PasswordNeverExpires -and
        $_.PasswordLastSet.AddDays(90) -lt (Get-Date).AddDays(7)
    } |
    Select-Object Name, SamAccountName, @{Name='ExpiresIn';Expression={
        ($_.PasswordLastSet.AddDays(90) - (Get-Date)).Days
    }}
```

These examples demonstrate PowerShell's expressiveness: the commands read like natural language, the object model eliminates parsing errors, and the pipeline composes operations cleanly.

For cross-platform administrators, PowerShell 7 (the open-source, cross-platform version) runs on Linux and macOS alongside Bash. While you would not typically replace Bash on Linux, PowerShell is invaluable when managing hybrid environments — a single script can query both Windows and Linux systems using the same object model.

### Required Reading

- Jones, D., & Hicks, W. (2037). *Learn Windows PowerShell in a Month of Lunches*, 5th Edition. Manning. Chapters 1-6.
- Microsoft Learn (2040). "PowerShell 7 Cross-Platform Administration Guide."
- Yggdrasil Operations Guide (2040). Chapter 8: "Hybrid Environment Scripting with PowerShell."

### Discussion Questions

1. Compare the Bash pipeline `ps aux | grep nginx | awk '{print $2}' | xargs kill` with the PowerShell equivalent `Get-Process nginx | Stop-Process`. What are the advantages and disadvantages of each approach in terms of reliability, readability, and error handling?
2. PowerShell's object model eliminates text parsing, but introduces a dependency on .NET type information. What happens when a cmdlet returns unexpected object types? How do you handle this in production scripts?
3. Design a PowerShell script that enumerates all Active Directory users, identifies those whose passwords expire within 14 days, and sends them an email notification. What edge cases must you handle (disabled accounts, service accounts, users with no email address)?

---

ᛏ **Lecture 8: PowerShell in Practice — Windows Server, Azure, and Cross-Platform Automation**

**Course:** SA105 — Scripting for SysAdmins (Bash, Python, PowerShell)
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Having established PowerShell's object pipeline model, this lecture applies it to the practical administration tasks that Windows-focused SAs perform daily: server configuration, Active Directory management, IIS administration, Azure resource management, and cross-platform automation. We also cover PowerShell remoting, Desired State Configuration (DSC), and the emerging patterns for managing hybrid Linux/Windows environments from a single scripting language.

### Key Topics

- **Windows Server Administration with PowerShell:** Managing Windows features with `Install-WindowsFeature`/`Remove-WindowsFeature`. Registry management with `Get-ItemProperty`, `Set-ItemProperty`. Event log management with `Get-WinEvent`, `New-EventLog`. Scheduled tasks with `Register-ScheduledTask`. Windows Firewall rules with `New-NetFirewallRule`.

- **Active Directory Automation:** Bulk user creation from CSV. Group membership management. OU structure administration. Password policy enforcement. Account lifecycle management (creation, modification, deprecation, deletion). The pattern of parameterized user templates for consistent account provisioning.

- **IIS Web Server Administration:** The `WebAdministration` module: `Get-Website`, `New-Website`, `Set-WebBinding`, `Get-WebAppPool`. Deploying web applications programmatically. Managing SSL certificates with `Get-WebBinding` and certificate binding. App pool recycling and health monitoring.

- **Azure Management with Az PowerShell:** The `Az` module for Azure resource management. `Connect-AzAccount` for authentication. `Get-AzVM`, `New-AzVM`, `Remove-AzVM` for virtual machines. `Get-AzResourceGroup` for resource organization. `Get-AzStorageAccount` for storage management. The pattern of infrastructure-as-code with PowerShell ARM templates.

- **Desired State Configuration (DSC):** Declarative configuration management native to PowerShell. Configuration blocks that define desired state (not imperative steps). DSC Resources: built-in (File, Registry, Service, User, Group) and custom. Pull vs. Push configuration modes. Integration with Azure Automation DSC for cloud-managed configuration. The shift from DSC to Gerst configuration management in 2040 environments.

- **Cross-Platform PowerShell 7:** PowerShell 7 on Linux: what works, what doesn't. Using `Get-ChildItem` instead of `ls` on all platforms. The `$IsLinux`, `$IsMacOS`, `$IsWindows` automatic variables for platform branching. Managing Linux services with PowerShell via `systemctl`. The practical reality: use PowerShell for Windows-centric tasks and hybrid orchestration; use Bash for Linux-native operations.

### Lecture Notes

A practical example demonstrates PowerShell's power for Windows administration: creating a new organizational unit structure, service accounts, and security groups for a department:

```powershell
<#
.SYNOPSIS
    Provision a new department in Active Directory
.DESCRIPTION
    Creates OU structure, service accounts, and security groups for a new department.
    Idempotent: safe to run multiple times.
#>
param(
    [Parameter(Mandatory)]
    [string]$DepartmentName,

    [Parameter(Mandatory)]
    [string]$DepartmentCode,

    [string]$BaseOU = "OU=Departments,DC=yggdrasil,DC=edu"
)

Import-Module ActiveDirectory

$ouPath = "OU=$DepartmentName,$BaseOU"

# Create OU if not exists (idempotent)
if (-not (Get-ADOrganizationalUnit -Filter "Name -eq '$DepartmentName'" -SearchBase $BaseOU -ErrorAction SilentlyContinue)) {
    New-ADOrganizationalUnit -Name $DepartmentName -Path $BaseOU
    Write-Host "Created OU: $DepartmentName"
}

# Create security groups
$groups = @(
    "$DepartmentCode-Admins",
    "$DepartmentCode-Users",
    "$DepartmentCode-ReadOnly"
)

foreach ($group in $groups) {
    if (-not (Get-ADGroup -Filter "Name -eq '$group'" -ErrorAction SilentlyContinue)) {
        New-ADGroup -Name $group -GroupCategory Security -GroupScope Global -Path $ouPath
        Write-Host "Created group: $group"
    }
}

# Create service accounts
$serviceAccounts = @(
    "$DepartmentCode-svc-web",
    "$DepartmentCode-svc-db"
)

foreach ($svc in $serviceAccounts) {
    if (-not (Get-ADUser -Filter "SamAccountName -eq '$svc'" -ErrorAction SilentlyContinue)) {
        $password = (New-Guid).ToString() | ConvertTo-SecureString -AsPlainText -Force
        New-ADUser -Name $svc -SamAccountName $svc -AccountPassword $password `
            -Path $ouPath -Enabled $true -PasswordNeverExpires $true
        Write-Host "Created service account: $svc"
    }
}

Write-Host "Department $DepartmentName provisioned successfully"
```

This script demonstrates several PowerShell best practices: parameterized input, idempotent operations (checking before creating), and the pipeline pattern for bulk creation. Each `if (-not (Get-AD...))` check makes the script safe to re-run.

The cross-platform story in 2040 is nuanced. PowerShell 7 runs on Linux, and the `Az` module works identically on all platforms. For managing Azure resources, checking Microsoft 365 services, or orchestrating hybrid environments, PowerShell is the clear choice regardless of the OS. But for Linux-native operations — managing systemd services, reading `/etc/` configuration files, processing text logs — Bash remains more natural and more widely documented. The pragmatic approach is to use the right language for each task.

### Required Reading

- Jones, D. (2038). *PowerShell in Depth*, 3rd Edition. Manning. Chapters 12-15.
- Microsoft Learn (2040). "Az PowerShell Module Reference."
- Yggdrasil Operations Guide (2040). Chapter 9: "Hybrid Environment Scripting Patterns."

### Discussion Questions

1. Compare PowerShell DSC with Ansible for configuration management. What are the advantages of each? In what scenarios would you choose DSC over Ansible?
2. Your organization runs 200 Windows servers and 300 Linux servers. The Windows team wants to use PowerShell DSC; the Linux team wants Ansible. How do you reconcile these approaches? What are the risks of running two configuration management systems?
3. Write a PowerShell script that checks all Windows servers in an AD OU for pending Windows Updates, sends a summary email, and optionally installs updates on a schedule. Include error handling for servers that are offline.

---

ᚼ **Lecture 9: Cross-Language Scripting — Choosing the Right Tool and Integrating Languages**

**Course:** SA105 — Scripting for SysAdmins (Bash, Python, PowerShell)
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Real-world system administration rarely uses one language in isolation. An SA might use Bash to orchestrate a deployment pipeline that calls Python scripts for API interaction and PowerShell cmdlets for Windows server configuration. This lecture covers the practical integration of Bash, Python, and PowerShell: when to use each language, how to call one from another, how to share data between languages, and how to design automation systems that leverage each language's strengths. We also address the anti-patterns — overcomplicated integrations, unnecessary language mixing, and the "use the language I'm most comfortable with" bias.

### Key Topics

- **Decision Framework: Which Language?** A structured decision tree for choosing between Bash, Python, and PowerShell. Key factors: target platform (Linux vs. Windows vs. hybrid), task complexity (one-liner vs. 200-line script vs. shared module), data requirements (text processing vs. structured data vs. .NET objects), library availability, team skills, and operational context (cron job vs. interactive vs. CI/CD pipeline). The principle: use the simplest language that handles the task adequately.

- **Calling Python from Bash:** The `python3 script.py` invocation. Passing arguments via `sys.argv` and `argparse`. Capturing output with command substitution (`output=$(python3 script.py)`). Using `jq` to parse JSON output from Python scripts. The pattern: Bash as orchestrator, Python for heavy lifting.

- **Calling Bash from Python:** `subprocess.run(["bash", "script.sh"])` for full scripts. `subprocess.run("complex pipeline", shell=True)` for one-off Bash commands that would be cumbersome to rewrite in Python. When to rewrite Bash in Python vs. when to call Bash from Python (the answer: rewrite if the Bash logic is more than 10 lines and will be maintained).

- **Calling PowerShell from Bash and Python:** `pwsh -Command "Get-Process"` from Bash. `subprocess.run(["pwsh", "-Command", "script.ps1"])` from Python. JSON output mode (`pwsh -Command "Get-Process | ConvertTo-Json"`) for structured interop. The pattern: PowerShell for Windows-specific operations, JSON for data interchange.

- **Data Interchange Formats:** JSON as the universal interop format. TOML for configuration files (supported natively in Python 3.11+). YAML for complex configuration (Ansible, Kubernetes). CSV for tabular data. Environment variables for simple key-value pairs. The principle: always use a structured format for data interchange between languages; never parse unstructured text.

- **The Wrapper Script Pattern:** A Bash wrapper that calls Python analysis and PowerShell Windows commands, combining results into a unified report. Practical example: a compliance check script that runs on Linux (Bash for local checks), queries an API (Python for HTTP/JSON), and checks Windows servers (PowerShell remoting), then generates a unified compliance report.

- **Anti-Patterns to Avoid:** "Bash scripts that call Python scripts that call Bash scripts" — deep nesting of language transitions creates unmaintainable code. "Using Python because I know it" for tasks that are more naturally expressed in Bash (file operations, text processing). "Using Bash because I know it" for complex data manipulation. The rule: if you're parsing JSON in Bash with `sed` and `awk`, you should be using Python.

### Lecture Notes

The Yggdrasil Bifrǫst Mesh uses all three languages in concert. The nightly compliance check pipeline demonstrates the pattern:

```bash
#!/usr/bin/env bash
# Nightly compliance check - orchestrator
set -euo pipefail

# Phase 1: Linux system checks (Bash native)
echo "=== Linux Compliance Checks ==="
for server in $(cat /etc/yggdrasil/linux-servers.txt); do
    ssh "$server" '/usr/local/bin/compliance-check.sh' >> /tmp/compliance-linux.json
done

# Phase 2: Windows system checks (Python calls PowerShell)
echo "=== Windows Compliance Checks ==="
python3 /usr/local/bin/windows-compliance.py >> /tmp/compliance-windows.json

# Phase 3: API health checks (Python)
echo "=== API Compliance Checks ==="
python3 /usr/local/bin/api-compliance.py >> /tmp/compliance-api.json

# Phase 4: Generate unified report (Python - data aggregation and analysis)
echo "=== Generating Report ==="
python3 /usr/local/bin/compliance-report.py \
    --linux /tmp/compliance-linux.json \
    --windows /tmp/compliance-windows.json \
    --api /tmp/compliance-api.json \
    --output /var/www/compliance/$(date +%Y-%m-%d).html

echo "Compliance report generated successfully"
```

The Python `windows-compliance.py` script internally uses `subprocess` to call PowerShell:

```python
import subprocess
import json

def check_windows_compliance(server: str) -> dict:
    """Query Windows server compliance via PowerShell remoting."""
    result = subprocess.run(
        ["pwsh", "-Command",
         f"Invoke-Command -ComputerName {server} -ScriptBlock {"
         "Get-ComputerInfo | Select-Object WindowsVersion, OsBuildNumber, CsName; "
         "Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 5; "
         "Get-Service | Where-Object {$_.StartType -eq 'Automatic' -and $_.Status -ne 'Running'} "
         "} | ConvertTo-Json -Depth 3"
        ],
        capture_output=True,
        text=True,
        timeout=120,
    )
    return json.loads(result.stdout)

# Process results from multiple servers
```

This pattern leverages each language's strength: Bash for orchestration and SSH, Python for data processing and API interaction, PowerShell for Windows management — all communicating through JSON.

### Required Reading

- Yggdrasil Operations Standards (2040). "Multi-Language Script Integration Patterns."
- Thomas, D. & Hunt, A. (2039). *The Pragmatic Programmer*, 3rd Edition. Chapter 7: "Choose the Right Tool for the Job."
- Microsoft Learn (2040). "PowerShell JSON Interoperability Guide."

### Discussion Questions

1. Your monitoring system needs to check 50 Linux servers and 30 Windows servers every 5 minutes. Design a cross-platform checking system using Bash, Python, and PowerShell. How do you handle timeouts, authentication, and result aggregation?
2. When is it appropriate to rewrite a working Bash script in Python? What are the costs of rewriting (developer time, testing, deployment) vs. the costs of maintaining a Bash script that is growing unwieldy?
3. A colleague proposes using environment variables to pass complex data (arrays, nested structures) between Bash and Python. Why is this problematic? What are better alternatives?

---

ᛋ **Lecture 10: Script Testing, Documentation, and Maintainability**

**Course:** SA105 — Scripting for SysAdmins (Bash, Python, PowerShell)
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

A script that works today but cannot be understood, modified, or verified tomorrow is technical debt. This lecture addresses the practices that transform scripts from disposable hacks into maintainable infrastructure code: testing, documentation, version control, code review, and the discipline of treating scripts as software. We cover testing frameworks for all three languages, documentation standards, and the operational practices that ensure scripts survive their original author.

### Key Topics

- **Why Test Scripts?** Scripts that modify production systems must be tested. The cost of a bug in a script that deletes old backups or rotates logs incorrectly is measured in data loss and downtime. Testing is not optional for production scripts. Types of testing: syntax checking (`bash -n`, `python -m py_compile`, `pwsh -NoProfile -Command "Exit 0"`), unit testing (testing individual functions), integration testing (testing against real or simulated systems), and end-to-end testing (testing the entire workflow in a staging environment).

- **Bash Testing with Bats:** The Bash Automated Testing System (Bats) provides xUnit-style testing for Bash scripts. Writing test files with `@test` declarations. Setup and teardown functions. Mocking external commands by manipulating `$PATH`. Running Bats tests in CI/CD. The pattern: every Bash script that modifies production systems should have a corresponding `.bats` test file.

- **Python Testing with pytest:** The `pytest` framework for Python unit testing. Fixtures for setup and teardown. Parametrized tests. Mocking with `unittest.mock` — replacing external dependencies (network calls, subprocess invocations, filesystem operations) with controllable test doubles. Testing SA scripts that interact with the filesystem: use `tmp_path` fixture for temporary directories. Testing subprocess calls: mock `subprocess.run`. Testing network calls: mock `requests.get`.

- **PowerShell Testing with Pester:** The Pester framework for PowerShell testing. `Describe`, `Context`, `It` blocks for structuring tests. `Should` assertions. Mocking cmdlets with `Mock`. Pester tests for DSC configurations. Running Pester in CI/CD pipelines.

- **Documentation Standards:** Every script must have a header comment explaining purpose, usage, arguments, and examples. Python scripts use docstrings (module-level, function-level). PowerShell scripts use comment-based help (`.SYNOPSIS`, `.DESCRIPTION`, `.PARAMETER`, `.EXAMPLE`). Bash scripts use header comments following Yggdrasil standards. The `--help` flag must work and produce useful output.

- **Version Control Discipline:** Scripts in Git, not in home directories. Feature branches for changes. Pull requests with peer review for production scripts. Tagging releases (`v1.0.0`) and deploying from tags, not from main. The principle: if a script affects production systems, its changes must be reviewable.

- **Code Review for SA Scripts:** Review criteria: correctness, error handling, idempotency, security (no hardcoded credentials, no `shell=True` with untrusted input), documentation, and naming conventions. The "bus factor" test: can another SA understand and modify this script within 30 minutes?

### Lecture Notes

Testing Bash scripts is historically uncommon, which is unfortunate because Bash scripts are among the most error-prone. The combination of word splitting, glob expansion, and implicit type coercion creates numerous failure modes that only manifest under specific inputs. Bats makes it feasible to test Bash scripts systematically:

```bash
#!/usr/bin/env bats
# Tests for disk-space-check.sh

setup() {
    # Create a temporary filesystem structure for testing
    export TEST_DIR="$(mktemp -d)"
    mkdir -p "$TEST_DIR/mnt/normal"
    mkdir -p "$TEST_DIR/mnt/critical"
    # ... simulate df output
}

teardown() {
    rm -rf "$TEST_DIR"
}

@test "reports OK when disk usage is below threshold" {
    run ./disk-space-check.sh -t 85 "$TEST_DIR/mnt/normal"
    [ "$status" -eq 0 ]
    [[ "$output" == *"OK"* ]]
}

@test "reports CRITICAL when disk usage exceeds threshold" {
    run ./disk-space-check.sh -t 85 "$TEST_DIR/mnt/critical"
    [ "$status" -eq 1 ]
    [[ "$output" == *"CRITICAL"* ]]
}

@test "exits with error for non-existent filesystem" {
    run ./disk-space-check.sh -t 85 "/nonexistent"
    [ "$status" -eq 2 ]
}
```

For Python, `pytest` with mocking provides comprehensive testing:

```python
# test_deploy_config.py
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from deploy_config import deploy_config, file_hash

def test_file_hash_consistency(tmp_path):
    """file_hash returns the same hash for the same content."""
    test_file = tmp_path / "test.conf"
    test_file.write_text("server { listen 80; }")
    assert file_hash(test_file) == file_hash(test_file)

def test_deploy_skips_if_unchanged(tmp_path):
    """deploy_config exits early if source and target match."""
    source = tmp_path / "source.conf"
    target = tmp_path / "target.conf"
    source.write_text("content")
    target.write_text("content")
    with patch("deploy_config.subprocess.run"):
        # Should not attempt deployment
        deploy_config()
```

### Required Reading

- Yggdrasil Operations Standards (2040). "Testing Requirements for Production Scripts."
- Bennett, D. (2038). *Bats: Bash Automated Testing System Guide*. GitHub Documentation.
- Ramírez, S. (2037). *pytest for System Administrators*. O'Reilly. Chapters 1-3.

### Discussion Questions

1. How do you test a script that modifies production systems without actually modifying them? Discuss mocking strategies, staging environments, and the principle of testing "at the boundary."
2. A colleague's script has no documentation, no tests, and 500 lines of code. The author has left the organization. How do you approach understanding and maintaining this script? What are your priorities?
3. Should every script have a test, or is there a minimum complexity threshold below which testing is not worth the effort? Where do you draw the line, and what factors influence the decision?

---

ᛗ **Lecture 11: Advanced Patterns — APIs, Automation Frameworks, and Configuration Management**

**Course:** SA105 — Scripting for SysAdmins (Bash, Python, PowerShell)
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

As systems administrators progress beyond individual scripts, they encounter the need for automation frameworks: collections of scripts that work together to manage infrastructure at scale. This lecture covers advanced patterns for building such frameworks: API-first automation, modular script design, configuration management integration, and the transition from scripts to "Infrastructure as Code." We also examine how scripting intersects with configuration management tools like Ansible, Terraform, and Pulumi — and when to use scripting versus declarative IaC.

### Key Topics

- **API-First Automation:** Every modern infrastructure component exposes an API. Scripting in 2040 means API programming: REST, gRPC, and GraphQL endpoints for cloud services, monitoring systems, configuration databases, and internal service registries. The pattern: script calls API → API returns state → script makes decisions → script calls API to enforce desired state. Authentication: API keys, OAuth2 tokens, mutual TLS. Rate limiting and backoff. The `requests.Session()` pattern for connection reuse.

- **Modular Script Design:** Organizing scripts into reusable modules. Python packages: `__init__.py`, relative imports, the `src/` layout. Bash libraries: `source` or `.` to include shared functions. PowerShell modules: `.psm1` files, `Import-Module`, the `$Env:PSModulePath`. The principle: every function that might be reused should be in a module, not in a script's local scope.

- **Ansible Integration:** Ansible modules are idempotent by design, but sometimes you need custom logic. Writing custom Ansible modules in Python. The `script` module for running Bash scripts on remote hosts. The `shell` and `command` modules for one-off tasks. Callback plugins for custom reporting. When to use Ansible (declarative state management) vs. scripting (imperative procedural logic).

- **Terraform and Pulumi Integration:** Terraform's `local-exec` and `remote-exec` provisioners for running scripts during infrastructure provisioning. Pulumi's ability to embed Python (and other language) logic directly in infrastructure definitions. The pattern: Terraform/Pulumi defines infrastructure; scripts handle configuration that cannot be expressed declaratively.

- **Configuration Management Scripting:** Scripts that generate configuration files dynamically based on system properties, environment variables, and external data sources. Template engines: Jinja2 in Python, `envsubst` in Bash, PowerShell's string formatting. The principle of separating configuration templates from configuration values.

- **Event-Driven Automation:** Scripts that respond to events rather than running on a schedule. Webhook receivers for Git push events, alert triggers, and monitoring system events. `systemd` path units for filesystem-triggered automation. `inotifywait` for file-change events. The pattern: monitoring system detects anomaly → calls webhook → script remediates → monitoring system verifies resolution.

- **The Script Lifecycle in Production:** From development (local testing) through staging (integration testing) to production deployment. CI/CD pipelines for SA scripts. Linting: `shellcheck` for Bash, `ruff` or `pylint` for Python, `PSScriptAnalyzer` for PowerShell. Static analysis as a pre-commit hook. Code review as a quality gate. Deployment through GitOps: scripts are pulled from a Git repository by the target system, never pushed directly.

### Lecture Notes

The transition from "scripts" to "automation framework" is gradual but transformative. Consider the evolution of a certificate renewal system:

1. **Script Stage:** A single Bash script that checks certificates and calls `certbot renew`.
2. **Module Stage:** The script is refactored into functions stored in a shared Bash library. Other scripts can `source` the library and call `check_cert_expiry()`.
3. **Framework Stage:** A Python package (`cert_manager`) with separate modules for checking, renewing, deploying, and alerting. Each module can be called independently or orchestrated by a main runner. Configuration is externalized in YAML. Tests cover each module.
4. **IaC Integration Stage:** The framework is called by Ansible (for configuration) and Terraform (for provisioning new certificates on new hosts).
5. **Event-Driven Stage:** The monitoring system calls a webhook when a certificate expiry threshold is crossed. The webhook handler invokes the framework, which renews the certificate, deploys it, verifies the service, and sends a confirmation notification.

This progression represents the natural evolution of SA automation. The Yggdrasil certificate management system went through all five stages between 2036 and 2040.

A practical example of event-driven automation using `systemd` path units:

```ini
# /etc/systemd/path/cert-change.path
[Path]
PathModified=/etc/letsencrypt/live/*/fullchain.pem

[Unit]
Description=Watch for certificate changes
Wants=cert-deploy.service

# /etc/systemd/system/cert-deploy.service
[Service]
Type=oneshot
ExecStart=/usr/local/bin/cert-deploy-framework.py
```

When Let's Encrypt writes a new certificate, `systemd` detects the filesystem change and triggers the deployment framework — no cron schedule, no manual intervention, instant response to events.

### Required Reading

- Yggdrasil Engineering Standards (2040). "Automation Framework Architecture: From Scripts to Systems."
- Limoncelli, T.A. (2039). "The Lifecycle of an Automation Tool." ;login: magazine, Vol. 44, No. 2.
- HashiCorp (2040). "Terraform Provisioners: When to Use Scripts vs. Resources."

### Discussion Questions

1. At what point should a collection of scripts be refactor beg into a proper automation framework? What are the signs that the current approach is becoming unsustainable?
2. Event-driven automation responds immediately to changes, while scheduled automation checks periodically. What are the tradeoffs? Under what circumstances is each approach superior?
3. A team debates whether to write a custom Python script or to use Ansible for a complex configuration task. The script would be 200 lines of Python; the Ansible playbook would be 50 lines of YAML plus a custom module. Which approach do you recommend, and why?

---

ᛞ **Lecture 12: The Scripting Ecosystem — Security, Best Practices, and the Path Forward**

**Course:** SA105 — Scripting for SysAdmins (Bash, Python, PowerShell)
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

This final lecture synthesizes the entire course into a coherent professional practice: how to write secure scripts, maintain a healthy scripting ecosystem, and continue growing as a scripting-administrator. We cover security considerations (privilege management, credential handling, input validation), organizational patterns (script repositories, style guides, code review culture), performance optimization, and the emerging tools and patterns that will shape scripting in the 2040s and beyond. The lecture closes with a forward look at how scripting intersects with AIOps, low-code platforms, and the evolving role of the systems administrator.

### Key Topics

- **Script Security:** The principle of least privilege: scripts should run with the minimum permissions required. `sudo` configuration: specifying exact commands rather than `NOPASSWD: ALL`. Credential management: never hardcode passwords or API keys in scripts. Use secret management tools (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault). Environment variables for non-secret configuration; secret stores for actual secrets. Input validation: sanitize all user input, file paths, and command arguments to prevent injection attacks. The `shell=True` vulnerability in Python `subprocess` and how to avoid it.

- **Credential Handling Patterns:** Reading secrets from files with restricted permissions (`0600`). Using `vault` CLI to fetch secrets at runtime. The `aws secretsmanager get-secret-value` pattern. PowerShell's `Get-Credential` and `ConvertFrom-SecureString`. The anti-pattern: secrets in Git (even in `.env` files — use `.gitignore` and secret managers instead). The Yggdrasil standard: all scripts read secrets from the Bifrǫst Vault, never from environment variables or configuration files in Git.

- **Style Guides and Linting:** Google Shell Style Guide for Bash. PEP 8 for Python. PowerShell Best Practices (approved verbs, consistent naming, comment-based help). Automated linting: `shellcheck` for Bash, `ruff` (or `pylint`/`flake8`) for Python, `PSScriptAnalyzer` for PowerShell. Pre-commit hooks that run linters before allowing code to be committed. The principle: linting is not optional.

- **Performance Considerations:** When Bash is faster than Python (short pipelines, filesystem operations). When Python is faster than Bash (complex data manipulation, API calls, anything involving structured data). Profiling: `time` for Bash, `cProfile` for Python, `Measure-Command` for PowerShell. The overhead of process creation in Bash pipelines. When to rewrite a Bash pipeline as a Python script: usually when you need complex data structures, error handling, or API interaction.

- **The Future of SA Scripting:** AIOps systems that generate remediation scripts from observed patterns. Natural language to script translation (e.g., "check all servers for disk space > 90% and send an alert" → generated Python script). Script synthesis from monitoring data. The continued importance of human review for AI-generated scripts: the SA as auditor and editor, not just author. Low-code/no-code platforms and when they are appropriate (simple workflows) vs. when they are limiting (complex logic, error handling, performance).

- **Course Synthesis:** What you have learned — Bash for Unix pipelines and rapid automation, Python for complex data processing and cross-platform scripting, PowerShell for Windows and hybrid environment management. The Unified SA Scripting Model: choose the right language for the task, integrate through structured data (JSON), test everything, document thoroughly, and treat scripts as production software.

- **Career Pathways and Next Steps:** SA201 (Advanced Linux Administration) deepens Bash and Python skills in Linux-specific contexts. SA203 (Virtualization & Container Platforms) uses scripting to manage VMs and containers. SA205 (Security Hardening & Compliance) covers secure scripting practices in depth. SA301 (Infrastructure as Code) transitions from scripting to declarative IaC. SA307 (Incident Response) covers scripting under pressure.

### Lecture Notes

The security of SA scripts is a topic that deserves far more attention than it typically receives. Scripts run with elevated privileges, access sensitive systems, and are often the weakest link in an organization's security posture. Consider this scenario: a cron job runs as root, executes a Bash script that sources a configuration file from `/etc/default/`, and that configuration file contains a command that has been modified by an attacker. The `source` command executes any valid Bash, including malicious commands. The fix: never source configuration files in scripts that run as root; instead, read configuration values with `grep` or `awk`, which treat the file as data, not code.

Another common vulnerability: Python scripts that build SQL queries using string concatenation. An attacker who can influence a parameter value can inject SQL:

```python
# VULNERABLE
cursor.execute(f"SELECT * FROM users WHERE name = '{user_input}'")

# SAFE - parameterized query
cursor.execute("SELECT * FROM users WHERE name = %s", (user_input,))
```

The same principle applies to shell commands. Never interpolate user input into shell commands:

```python
# VULNERABLE - shell injection
subprocess.run(f"ping -c 1 {user_input}", shell=True)

# SAFE - list form, no shell
subprocess.run(["ping", "-c", "1", user_input])
```

The credential management landscape in 2040 centers around dedicated secret management systems. Hardcoded credentials in scripts — whether API keys, database passwords, or SSH private keys — are the number one cause of credential exposure. The Yggdrasil standard requires all scripts to read secrets from the Bifrǫst Vault at runtime, using short-lived tokens that expire within 24 hours:

```python
import boto3
import requests

def get_secret(secret_name: str) -> str:
    """Fetch a secret from the Bifröst Vault."""
    vault_token = open("/var/run/vault/token").read().strip()
    response = requests.get(
        f"https://vault.yggdrasil.edu/v1/secret/data/{secret_name}",
        headers={"X-Vault-Token": vault_token},
    )
    response.raise_for_status()
    return response.json()["data"]["data"]["value"]
```

This pattern ensures that secrets are never stored in code, never written to disk permanently, and always have a limited lifetime.

As you progress through the Systems Administration program, you will use scripting in every subsequent course. SA201 (Advanced Linux Administration) assumes fluency in Bash. SA203 (Virtualization & Container Platforms) uses Python scripts to orchestrate container operations. SA205 (Security Hardening) covers secure scripting patterns in depth. SA301 (Infrastructure as Code) transitions from imperative scripting to declarative configuration with Terraform, Ansible, and Pulumi. And SA405 (Capstone) requires you to operate a production fleet where every maintenance task is automated, every script is tested, and every credential is managed through a vault. The skills you develop in this course — idempotent design, error handling, structured logging, security awareness — are the foundation of professional systems administration practice.

*The runes are carved; the Norns weave their strands. Every script is a thread in Yggdrasil's tapestry — write each one with intention, for it will be read by those who come after you.* ᛟ

### Required Reading

- OWASP Foundation (2040). "Script Security Cheat Sheet."
- Yggdrasil Security Standards (2040). "Credential Management in Automation Scripts."
- Limoncelli, T.A. (2040). "The Future of Systems Administration: AI-Augmented but Human-Governed." *Communications of the ACM*, Vol. 63, No. 6.

### Discussion Questions

1. A script that runs as root reads a configuration file from `/etc/default/scriptname`. An attacker gains write access to that configuration file. How can the attacker escalate this to arbitrary code execution? How do you prevent this?
2. An AIOps system generates a remediation script for a production incident. Should the SA review the script before executing it? What are the risks of running AI-generated scripts without review? What are the risks of delays caused by manual review during a critical incident?
3. In 5 years, will SA scripting be largely replaced by AIOps systems that generate and execute remediation code automatically? Make the case for and against. What skills should you develop to remain relevant?

---

## Final Examination Preparation

### Format
The final examination for SA105 consists of **8 essay questions**, from which students must answer **4**. Each question requires a substantive response of 800-1200 words, demonstrating both theoretical understanding and practical scripting competence. Students are expected to include code examples, pipeline constructions, or configuration snippets where appropriate.

### Sample Examination Questions

1. **Idempotency in Practice:** Describe the principle of idempotency as it applies to systems administration scripting. Write an idempotent Bash script that creates a system user with specific attributes only if the user does not already exist, and_idempotent Python function that ensures a configuration file contains specific lines. Explain why idempotency matters for automation that runs on schedules and in CI/CD pipelines.

2. **Language Selection:** A system administrator needs to automate three tasks: (a) parsing Apache access logs to extract the top 20 IPs by request count, (b) querying a REST API to retrieve a list of virtual machines and shutting down those running for more than 30 days, and (c) configuring Windows Update settings on 50 domain-joined Windows servers. Which scripting language would you use for each task and why? What factors influence language selection?

3. **Error Handling Comparison:** Compare error handling in Bash, Python, and PowerShell. For each language, describe the primary error handling mechanisms, their strengths and weaknesses, and write a code example that demonstrates production-quality error handling for a common SA task (e.g., checking disk space and sending an alert). Which language's error handling model do you find most robust and why?

4. **Security in SA Scripts:** A production automation system contains scripts that run as root, access databases, and modify system configuration. Identify five security vulnerabilities that commonly appear in SA scripts and describe how to mitigate each. Include specific code examples of vulnerable and secure patterns.

5. **The Atomic Deployment Pattern:** Explain the atomic deployment pattern for configuration file management. Write a Python script that performs an atomic configuration deployment with validation, backup, and rollback. What happens if the server crashes between the write and the validation step? How does atomic rename mitigate race conditions?

6. **Cross-Platform Automation:** Design an automation system that checks compliance across a hybrid environment of 100 Linux servers and 50 Windows servers. The compliance checks include: disk space thresholds, service availability, SSL certificate expiry, and security patch levels. Describe the architecture (which languages, how they communicate, data formats, scheduling, reporting). Justify each architecture decision.

7. **From Script to Framework:** A system administrator has written 15 Bash scripts that each perform a single SA task (check backups, verify certificates, monitor services, etc.). Each script is independent, has its own logging, and emails individual reports. Describe how you would evolve these scripts into a unified automation framework. What changes would you make? What would you keep? What new components would you introduce?

8. **Testing Philosophy:** The Yggdrasil operations team requires that all production scripts have corresponding test suites. A colleague argues that "testing scripts is overkill — they're just scripts, not production software." Craft a counterargument that defends script testing as essential for production reliability. Include specific examples of how untested scripts have caused (or could cause) production incidents.

---

*The Norns have woven this course into the tapestry of Yggdrasil. Go forth and script wisely — for every line of code is a rune carved into the infrastructure that sustains us all.* ᛟ