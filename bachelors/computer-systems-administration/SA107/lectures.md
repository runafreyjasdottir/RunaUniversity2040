# SA107: User & Identity Management — Who May Enter the Hall
## Bachelor of Science in Computer Systems Administration — University of Yggdrasil, 2040

**Credits:** 4
**Description:** Comprehensive study of identity and access management (IAM) in modern distributed systems. Students master directory services (LDAP, Active Directory), federated identity (SAML, OAuth 2.1, OpenID Connect), privilege management (RBAC, ABAC, ReBAC), multi-factor authentication, zero-trust identity architecture, and the Yggdrasil Heimdall ID platform. The course covers provisioning lifecycle (joiner-mover-leaver), secrets management, certificate lifecycle, and compliance frameworks. Hands-on labs deploy production-grade identity infrastructure on the Bifrǫst Mesh.

**Instructor:** Dr. Sigrid Heiðarsdóttir, Professor of Identity Architecture & Director of the Heimdall ID Consortium
**Lab:** Heimdall Identity Lab, Sublevel 1, Hákon Computing Centre
**Office Hours:** Wednesdays 14:00-16:00, or by appointment

---

## Lectures

ᚠ **Lecture 1: The Identity Problem — From Gatekeeping to Trust Architecture**

**Course:** SA107 — User & Identity Management
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

This opening lecture frames identity management as the foundational challenge of distributed computing. Every system interaction begins with a question: "Who are you, and what are you allowed to do?" In the Norse mythological tradition, Heimdallr guards the Bifrǫst bridge, challenging all who seek passage — a metaphor that resonates deeply in 2040's zero-trust architecture, where every request must be authenticated, authorized, and audited. We examine the evolution of identity from local password files to global federated identity, the cost of poor identity management (data breaches, compliance failures, operational chaos), and the philosophical dimensions of digital identity in an age of AI agents, neuromorphic personas, and post-quantum cryptography.

### The Identity Problem in Three Acts

The identity problem has evolved through three distinct eras. In the **Mainframe Era** (1960s-1990s), identity was simple: a username and password stored in `/etc/passwd` or a RACF database on a single system. The administrator of that system was the absolute authority. There was one system, one identity store, one access decision point. The gate was the serial terminal, and the gatekeeper was the mainframe's security module.

In the **Client-Server Era** (1990s-2015), identity fragmented. Every application built its own user table. Employees at a mid-size company might have 15 different usernames for 15 different systems — email, HR portal, file server, CRM, VPN, database, and more. Password fatigue drove users to reuse passwords across systems, creating cascading security failures. The industry responded with directory services (LDAP, Active Directory) that centralized identity stores, and with federated protocols (Kerberos, SAML) that allowed single sign-on. But identity was still fundamentally perimeter-based: once you were inside the corporate network, you were trusted.

In the **Cloud-Native Era** (2015-2040), the perimeter dissolved. Employees work from anywhere on any device. Partners, contractors, IoT devices, service accounts, and AI agents all need identity. The average enterprise manages 180,000 identities across 3,000 applications (Gartner, 2038). Identity is no longer a people problem; it is an *entity* problem. The Bifrǫst Mesh at University of Yggdrasil authenticates 47,000 human identities, 12,000 service accounts, 3,400 IoT device identities, and 800 AI agent identities — and every single one must be uniquely identified, authenticated, authorized, and audited.

### The Price of Identity Failure

Identity-related breaches account for 74% of all data breaches in 2040 (Verizon DBIR, 2040). The pattern is consistent: an attacker obtains credentials through phishing, social engineering, or credential stuffing; escalates privileges through misconfigured access controls; and exfiltrates data or deploys ransomware. The average cost of an identity-related breach is $5.2 million. The root causes are almost always the same: over-provisioned accounts (users with more access than they need), orphaned accounts (users who left the organization but whose accounts remain active), and lack of multi-factor authentication.

The 2034 *Mjölnir Incident* at a Scandinavian university illustrates the cascading consequences of identity failure. A researcher's credentials were compromised through a targeted phishing email. The account had administrative access to the university's research compute cluster (unnecessary for the researcher's role). The attacker used this access to install cryptocurrency mining software on 200 GPU nodes, consuming €340,000 in electricity before detection. The incident prompted the Nordic University Identity Standards Consortium (NUISC), which developed the Heimdall ID framework that University of Yggdrasil now operates.

### The Norse Framing: Heimdallr and the Bifrǫst Gate

In Norse mythology, Heimdallr is the guardian of Bifrǫst, the burning rainbow bridge between Miðgarðr (the realm of humans) and Ásgarðr (the realm of the gods). He sees for a hundred leagues by day and by night, hears the grass growing and the wool on sheep, and needs less sleep than a bird. At Ragnarǫk, Heimdallr will blow the Gjallarhorn to warn the gods that the attackers are coming. Heimdallr does not trust by default; he verifies every arrival.

This is precisely the zero-trust identity model. In zero-trust, there is no "inside" the network where trust is assumed. Every request must prove its identity, prove its authorization, and be encrypted in transit — regardless of whether it originates from inside or outside the perimeter. Heimdallr's vigilance is not paranoia; it is the correct operational posture for a world where threats are pervasive and perimeters are illusions.

The Heimdall ID platform at University of Yggdrasil is named in his honor. It provides federated identity, multi-factor authentication, role-based and attribute-based access control, and continuous adaptive authentication across every system in the Bifrǫst Mesh. This course will teach you to build and operate such systems.

### The Course Roadmap

This course proceeds through four phases. **Phase 1 (Lectures 1-3)** covers identity foundations: authentication primitives, directory services, and the provisioning lifecycle. **Phase 2 (Lectures 4-6)** covers federation and single sign-on: SAML, OAuth 2.1, OpenID Connect, and the Heimdall ID platform. **Phase 3 (Lectures 7-9)** covers authorization and access control: RBAC, ABAC, policy engines, and secrets management. **Phase 4 (Lectures 10-12)** covers advanced topics: zero-trust identity, AI agent identity, compliance, and the future of digital identity.

### Required Reading

- W€llner, M. & Heiðarsdóttir, S. (2039). *Identity Architecture for Distributed Systems*, 3rd Edition. O'Reilly. Chapters 1-2.
- NIST Special Publication 800-63-4 (2038). *Digital Identity Guidelines*.
- Yggdrasil Heimdall ID Architecture Documentation (2040). UoY Digital Press.

### Discussion Questions

1. A university has 47,000 students, each with identities in the learning management system, email, library, VPN, printing, and 200+ cloud applications. What happens when a student graduates? Design a joiner-mover-leaver process that handles every identity touchpoint.
2. Heimdallr "sees for a hundred leagues" and "hears the grass growing." In identity terms, what does this omniscient vigilance correspond to? What are the privacy implications of monitoring every authentication event across an organization?
3. The shift from perimeter-based trust to zero-trust is fundamentally a philosophical shift from "trust by default, verify when suspicious" to "verify by default, trust only when verified." What are the operational costs of this shift? Under what circumstances might perimeter-based trust still be appropriate?

---

ᚢ **Lecture 2: Authentication Primitives — Passwords, Tokens, and the Three Factors**

**Course:** SA107 — User & Identity Management
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Authentication is the act of verifying a claim of identity. When a user says "I am sigfrid@yggdrasil.edu," authentication answers: "Prove it." This lecture covers the three factors of authentication (something you know, something you have, something you are), the mechanics and mathematics of password storage, the evolution from passwords to passkeys (FIDO2/WebAuthn), one-time password algorithms (HOTP/TOTP), and the authentication lifecycle in modern systems. We examine why passwords alone are insufficient, how multi-factor authentication (MFA) dramatically reduces breach risk, and why the industry is moving toward passwordless authentication with FIDO2 passkeys.

### Something You Know: Passwords and Their Discontents

Passwords remain the most common authentication factor in 2040, despite being the weakest link in identity security. The economics of passwords are brutal: humans cannot remember 100+ unique, high-entropy passwords, so they reuse passwords across services. Attackers exploit this with credential stuffing — automated attempts to use compromised username/password pairs from one service against others. The Have I Been Pwned database contained 13 billion compromised credentials by 2039.

Password storage on the server side has evolved through several generations. The naive approach (storing passwords in plaintext) was abandoned in the 1970s after the first major breaches. Cryptographic hashing (MD5, then SHA-1) replaced plaintext, but GPUs can compute billions of hashes per second, making simple hashing vulnerable to brute force. Salting (adding random data to each password before hashing) prevents rainbow table attacks, but does not prevent brute force. The current standard is **key derivation functions**: bcrypt, scrypt, and Argon2id (the 2035 Password Hashing Competition winner). These functions are deliberately slow (10-100ms per hash) and memory-hard (requiring significant RAM), making GPU and ASIC attacks economically infeasible.

The Yggdrasil password policy enforces Argon2id with the following parameters: memory cost 128MB, time cost 3 iterations, parallelism 4 threads. A single hash verification takes approximately 50ms on a modern server — negligible for legitimate authentication but devastating for brute force. The stored format is: `$argon2id$v=19$m=131072,t=3,p=4$<salt>$<hash>`.

### Something You Have: Tokens, Smart Cards, and FIDO2

The second factor — something you have — encompasses hardware tokens (YubiKey, Feitian), smart cards (PIV/CAC cards for government, NFC security keys for enterprise), and registered devices (smartphones with TOTP applications). The critical insight is that a physical token cannot be phished: an attacker in a different country cannot press the button on your YubiKey.

**HOTP** (HMAC-based One-Time Password, RFC 4226) and **TOTP** (Time-based One-Time Password, RFC 6238) are the algorithms behind the six-digit codes generated by authenticator apps. Both use a shared secret between the server and the client device. HOTP generates codes based on a counter; TOTP generates codes based on the current time (typically 30-second intervals). The security of TOTP depends on the secrecy of the shared key stored on the device — if the device is compromised, the TOTP secret is compromised.

**FIDO2/WebAuthn** (2018-2040) represents the next generation of hardware authentication. Instead of a shared secret, FIDO2 uses public-key cryptography: the authenticator generates a unique key pair for each service, stores only the private key, and registers the public key with the service. Authentication is performed by the authenticator signing a challenge from the server. The private key never leaves the authenticator. This eliminates phishing (the authenticator won't sign a challenge for the wrong domain), eliminates shared secrets (no secret to steal from the server), and provides attestation (the server can verify the authenticator's manufacturer and firmware).

By 2040, FIDO2 passkeys are the dominant second factor at University of Yggdrasil. Every student receives a YubiKey 6C NFC at enrollment. The Heimdall ID platform registered 47,000 YubiKeys, 3,400 device-bound passkeys, and 800 platform authenticators for AI agents. Passkeys are now available in the cloud (Apple iCloud Keychain, Google Password Manager, Microsoft Authenticator), enabling cross-device synchronization while maintaining the phishing-resistant properties of FIDO2.

### Something You Are: Biometrics and Their Limitations

Biometric authentication — fingerprint, iris, face, voice — is convenient and cannot be forgotten or lost. But biometrics have a fundamental problem: you cannot change your fingerprint the way you can change your password. If a biometric template is compromised, it is compromised forever. The 2038 *Deepprint* attack demonstrated that synthetic fingerprints could be generated from biometric metadata stored in national ID databases, affecting 120 million people across three countries.

The Yggdrasil approach to biometrics is **local-only, never centralized**. Biometric templates are stored exclusively on the user's FIDO2 authenticator (the YubiKey 6C NFC includes a fingerprint sensor). Authentication occurs on the device; the server never receives biometric data. This model aligns with the privacy-by-design principles in the EU AI Act (2036) and the NIST SP 800-63B Level of Assurance 3 requirements.

### Multi-Factor Authentication in Practice

MFA combines two or more factors. The industry standard in 2040 is **phishing-resistant MFA**: FIDO2 passkey + PIN or biometric on the same device. This provides two factors (something you have + something you know or something you are) in a single user action. The Heimdall ID platform enforces phishing-resistant MFA for all privileged operations: SSH access to production systems, administrative console access, and data export. Basic authentication (email, learning management) accepts password + TOTP as a fallback, but this is being deprecated.

The authentication flow in Heimdall ID:

1. User navigates to `id.yggdrasil.edu`
2. Browser loads the OpenID Connect authorization endpoint
3. User enters username; IdP sends a FIDO2 challenge
4. User taps their YubiKey (or uses a platform authenticator)
5. Authenticator signs the challenge; IdP verifies the signature
6. If step-up authentication is required (for privileged access), IdP prompts for biometric verification on the authenticator
7. IdP issues an access token (JWT) with the user's identity, groups, and claims

This entire flow takes under 3 seconds and requires a single user action.

### Required Reading

- NIST SP 800-63B-4 (2039). *Digital Identity Guidelines: Authentication and Lifecycle Management*.
- Jones, M. & Hodges, W. (2038). *FIDO2 and WebAuthn: The Passwordless Future*. O'Reilly. Chapters 1-4.
- Yggdrasil Heimdall ID Authentication Specification (2040). UoY Digital Press.

### Discussion Questions

1. Argon2id with 128MB memory cost takes 50ms per verification on a modern server. If an authentication service handles 10,000 requests per second, how many cores are needed? What caching strategies can reduce the authentication load?
2. FIDO2 eliminates shared secrets and phishing, but passkeys stored in cloud password managers create a new attack surface: if the user's cloud account is compromised, all passkeys are compromised. How does this compare to the risk of a stolen YubiKey? Design a threat model for each.
3. Biometric templates stored locally on authenticators protect privacy but create a recovery problem: if the authenticator is lost, the biometric is gone. Design a recovery mechanism that does not compromise the local-only principle.

---

ᚦ **Lecture 3: Directory Services — LDAP, Active Directory, and the组织 Tree**

**Course:** SA107 — User & Identity Management
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Directory services are the authoritative source of identity truth in an organization. They store user accounts, groups, organizational structure, contact information, and access policies in a hierarchical, queryable, replicated database. This lecture covers the Lightweight Directory Access Protocol (LDAP), Microsoft Active Directory (the dominant enterprise directory for 25 years), and the 2040 landscape of directory services including cloud-native directories (Azure AD / Entra ID, Google Workspace Directory), the Yggdrasil Heimdall ID directory, and the challenges of multi-directory environments.

### The Directory Information Tree

LDAP organizes data as a **Directory Information Tree (DIT)** — a hierarchical structure where each entry is identified by a **Distinguished Name (DN)**. The DIT is conceptually similar to a filesystem: the root is the organization, branches are organizational units, and leaves are users, groups, and devices.

A typical LDAP DIT for University of Yggdrasil:

```
dc=yggdrasil,dc=edu
├── ou=People
│   ├── uid=heintr odinsson,ou=People,dc=yggdrasil,dc=edu
│   ├── uid=brigta bjǫrndóttir,ou=People,dc=yggdrasil,dc=edu
│   └── uid=vǫlundr smithson,ou=People,dc=yggdrasil,dc=edu
├── ou=Groups
│   ├── cn=sysadmin,ou=Groups,dc=yggdrasil,dc=edu
│   ├── cn=faculty,ou=Groups,dc=yggdrasil,dc=edu
│   └── cn=students,ou=Groups,dc=yggdrasil,dc=edu
├── ou=Services
│   ├── cn=bifrost-proxy,ou=Services,dc=yggdrasil,dc=edu
│   └── cn=mjolnir-ci,ou=Services,dc=yggdrasil,dc=edu
└── ou=Policies
    └── cn=password-policy,ou=Policies,dc=yggdrasil,dc=edu
```

Each entry contains **attributes** — key-value pairs defined by an **objectClass** schema. A `person` entry has `cn` (common name), `sn` (surname), `mail`, `userPassword`, and `uid`. A `groupOfNames` entry has `cn`, `member` (DNs of group members), and `description`. The schema defines which attributes are required (`MUST`) and which are optional (`MAY`) for each objectClass.

LDAP operations follow the CRUD pattern: **Add** (create entry), **Modify** (update attributes), **Delete** (remove entry), and **Search** (query entries with filters). LDAP search filters use Polish notation: `(&(objectClass=person)(uid=heintr*))` finds all person entries whose uid starts with "heintr." The `Modify` operation is atomic — either all attribute changes succeed or none do, ensuring consistency.

### Replication and High Availability

A directory service must be highly available — if the directory is down, nobody can log in, and all dependent services fail. LDAP replication uses a **multi-master** model: any server can accept writes, and changes are propagated to replicas. This is achieved through the **LDAP Content Synchronization Operation** (LCUP, RFC 3928) or, in OpenLDAP, through **syncrepl** (sync replication).

At University of Yggdrasil, the Heimdall ID directory runs on a five-node OpenLDAP cluster with syncrepl replication. Three nodes in the Hákon Computing Centre form the primary replication group; two nodes in the Ásgarðr Edge Facility provide disaster recovery. All five nodes can accept writes; conflicts are resolved through operational timestamps and CSN (Change Sequence Number) ordering. The cluster handles 45,000 searches and 3,000 modifications per hour during peak class registration periods.

Active Directory replication uses a different model: a single **Flexible Single Master Operation** (FSMO) role holder for each partition, with multi-master replication within each domain. The Schema Master, Domain Naming Master, RID Master, PDC Emulator, and Infrastructure Master are five separate FSMO roles, each held by one domain controller at a time. This design ensures consistency but creates a single point of failure for each role — mitigated by role seizure in emergencies but adding operational complexity.

### Active Directory: The 25-Year Monolith

Microsoft Active Directory (AD), introduced in Windows 2000, became the de facto enterprise directory for Federal Express, the Fortune 500, and every organization running Windows. AD is LDAP-compatible but extends the schema with Microsoft-specific objectClasses and attributes: `user` (instead of `person`), `group` (instead of `groupOfNames`), `computer`, and `organizationalUnit`. AD adds Group Policy Objects (GPOs) — centralized configuration management that can enforce security policies, deploy software, and map drives across an entire domain.

In 2040, AD is still present in 60% of enterprises, but it is legacy. The migration to cloud-native identity (Entra ID, Okta, Ping Identity) is well advanced. University of Yggdrasil does not run Active Directory; it uses the Heimdall ID directory built on OpenLDAP with a custom schema and the Keycloak identity broker for federation. This decision was made in 2036 when the university's aging Windows Server 2019 domain controllers reached end-of-support, and the migration to a cloud-native, open-source identity platform was assessed as more future-proof than upgrading to a newer AD version.

### The Multi-Directory Problem

Most organizations have more than one directory. A typical university might have an on-premises AD for Windows systems, an LDAP directory for Linux systems, a Google Workspace directory for email and collaboration, a student information system (SIS) directory for course enrollment, and a human resources system directory for employee records. These directories contain overlapping data with inconsistent schemas, and keeping them synchronized is a significant operational challenge.

The solution is **identity governance**: a centralized platform that acts as the authoritative source of truth and propagates changes to all downstream directories. The Heimdall ID platform serves this role at University of Yggdrasil, using SCIM (System for Cross-domain Identity Management, RFC 7644) to provision and deprovision accounts across 47 connected systems in real-time. When a student's enrollment status changes in the SIS, Heimdall ID propagates the change to email, learning management, VPN, library, printing, and all 200+ cloud applications within 30 seconds.

### Required Reading

- Just, K.D. & van Wijk, A. (2037). *LDAP Directories Explained*, 2nd Edition. Addison-Wesley. Chapters 1-5.
- Microsoft Learn (2039). *Active Directory Domain Services Architecture*.
- Yggdrasil Heimdall ID Directory Schema Documentation (2040). UoY Digital Press.

### Discussion Questions

1. An organization has an on-premises AD with 50,000 user accounts and a cloud directory (Entra ID) with 40,000 accounts. 35,000 accounts exist in both directories. Design a synchronization architecture that keeps both directories consistent without creating duplicates or orphans.
2. LDAP multi-master replication allows any node to accept writes, but conflicts can occur when the same attribute is modified on two nodes simultaneously. Describe the conflict resolution strategy used by syncrepl and compare it to Active Directory's FSMO approach. Under what circumstances would each be preferable?
3. The Heimdall ID directory at University of Yggdrasil uses SCIM to propagate changes to 47 systems within 30 seconds. What happens when one of those systems is down during a propagation event? Design a retry mechanism that ensures eventual consistency without overwhelming the receiving system.

---

ᚼ **Lecture 4: Federation and Single Sign-On — SAML, OAuth 2.1, and OpenID Connect**

**Course:** SA107 — User & Identity Management
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Federated identity allows users to authenticate with one identity provider and access multiple services without re-entering credentials. This lecture covers the three major federation protocols — SAML 2.0 (Security Assertion Markup Language), OAuth 2.1 (authorization framework), and OpenID Connect (authentication layer on OAuth 2.0) — their roles, overlaps, and how they compose in modern identity architecture. We examine the SAML assertion flow, the OAuth authorization code grant with PKCE, the OpenID Connect ID token, and the Heimdall ID platform's implementation of all three protocols.

### The Federation Problem

Without federation, every application maintains its own user database. A user at Yggdrasil has 47 accounts across 47 services, each with its own username and password. This creates operational overhead (47 accounts to create, maintain, and deprovision), security risk (47 attack surfaces, 47 places for weak passwords), and user frustration (47 passwords to remember or manage).

Federated identity solves this by introducing a **trusting relationship** between an **Identity Provider (IdP)** and a **Service Provider (SP)** or **Relying Party (RP)**. The user authenticates once with the IdP; the IdP vouches for the user's identity to the SP. The SP trusts the IdP's assertion without needing to verify the user's credentials directly. The Norse metaphor is apt: Heimdallr identifies the traveler at the Bifrǫst gate; Ásgarðr's halls trust Heimdallr's judgment and admit the traveler without further questioning.

### SAML 2.0: The Enterprise Standard

SAML 2.0 (2005) is an XML-based federation protocol widely used in enterprise environments. The SAML flow:

1. User attempts to access a Service Provider (SP)
2. SP generates a SAML authentication request and redirects the user to the Identity Provider (IdP)
3. User authenticates with the IdP (username/password + MFA)
4. IdP generates a SAML assertion (an XML document containing the user's identity, attributes, and authentication statement)
5. IdP redirects the user back to the SP with the assertion
6. SP validates the assertion (checks signature, timestamp, audience) and grants access

SAML assertions contain three types of statements:
- **Authentication statements**: "The user identified as heintr@yggdrasil.edu authenticated at 2024-11-15T09:30:00Z using FIDO2."
- **Attribute statements**: "The user has the following attributes: department=Computer Science, role=student, groups=sysadmin."
- **Authorization decision statements**: "The user is permitted to access the requested resource."

The assertion is signed with the IdP's private key; the SP validates the signature with the IdP's public key (obtained from the IdP's metadata). This ensures that assertions cannot be forged. The SP also checks the assertion's conditions: `NotBefore` and `NotOnOrAfter` timestamps prevent replay attacks; `AudienceRestriction` prevents an assertion intended for one SP from being used at another.

SAML's weakness is its complexity. The XML schema is large, the binding profiles are numerous, and debugging SAML issues requires understanding XML Signature, XML Encryption, SAML protocol bindings, and name identifier formats. The Heimdall ID platform supports SAML 2.0 for legacy applications (Microsoft 365, Salesforce, SAP) that require it, but all new applications use OpenID Connect.

### OAuth 2.1: Delegated Authorization

OAuth 2.1 (2024, RFC 9728) is an authorization framework — not an authentication protocol. It allows a user to grant a third-party application limited access to their resources without sharing their credentials. The classic example: granting a photo printing service access to your Google Photos without giving it your Google password.

The **Authorization Code Grant with PKCE** (Proof Key for Code Exchange) is the recommended flow for all client types in 2040:

1. Client generates a code verifier (random string) and code challenge (SHA-256 hash of verifier)
2. Client redirects user to authorization endpoint with code_challenge
3. User authenticates and authorizes the client
4. Authorization server returns an authorization code
5. Client exchanges authorization code + code verifier for access token
6. Authorization server verifies code verifier matches code challenge
7. Client uses access token to access the resource server

The access token is typically a JWT (JSON Web Token) containing the user's identity, scopes (permissions), and expiration time. Scopes limit what the client can do: `read:profile` allows reading the user's profile; `write:documents` allows creating documents; `admin:systems` allows system administration.

PKCE prevents authorization code interception attacks. Without PKCE, an attacker who steals the authorization code (e.g., through a malicious callback URL) can exchange it for an access token. With PKCE, the attacker needs both the authorization code AND the code verifier, which is never sent over the network.

### OpenID Connect: Authentication on Top of OAuth 2.0

OpenID Connect (OIDC, 2014) adds an **authentication layer** on top of OAuth 2.0. Where OAuth provides authorization ("this token allows access to these resources"), OIDC provides **authentication** ("this user is who they claim to be, and here are their claims").

The OIDC flow adds one key element to the OAuth flow: the **ID token**. The ID token is a JWT signed by the IdP containing:
- `iss` (issuer): the IdP's identifier
- `sub` (subject): the user's unique identifier at the IdP
- `aud` (audience): the client identifier
- `auth_time`: when the user authenticated
- `nonce`: a value that correlates the authentication request with the ID token
- `acr`: authentication context reference (what authentication method was used)
- Various claims: name, email, groups, roles

The **UserInfo endpoint** provides additional claims on demand. The client calls the UserInfo endpoint with the access token and receives a JSON document with the user's profile information. This separates authentication (ID token) from profile data (UserInfo), allowing the client to request only the claims it needs.

Heimdall ID implements OIDC with the following custom claims:
- `yggdrasil:groups`: array of group DNs the user belongs to
- `yggdrasil:roles`: array of role identifiers (e.g., `sysadmin`, `faculty`, `student`)
- `yggdrasil:degree_program`: the student's enrolled degree program
- `yggdrasil:auth_method`: the authentication method used (FIDO2, TOTP, password)
- `yggdrasil:trust_level`: the assurance level (1-4, per NIST SP 800-63)

### The Heimdall ID Federation Architecture

The Heimdall ID platform at University of Yggdrasil acts as both an IdP (for internal services) and a SP (for external services like Google Workspace, Microsoft 365, and GitHub). The architecture:

```
                    ┌─────────────────────────────────────────┐
                    │         Heimdall ID Platform           │
                    │   ┌─────────────────────────────────┐   │
                    │   │   Keycloak (OIDC + SAML broker) │   │
                    │   └─────────────────────────────────┘   │
                    │   ┌──────────────┐  ┌───────────────┐   │
                    │   │ OpenLDAP      │  │ SCIM Gateway  │   │
                    │   │ (IdP Store)   │  │ (Provisioning)│   │
                    │   └──────────────┘  └───────────────┘   │
                    └────────────┬────────────────────────────┘
                                 │
            ┌────────────────────┼────────────────────┐
            │                    │                     │
    ┌───────▼──────┐  ┌────────▼───────┐  ┌─────────▼──────┐
    │ Bifrǫst Mesh  │  │ Mjölnir CI/CD  │  │ 47 Cloud Apps  │
    │ (SSH, OIDC)  │  │ (OIDC)         │  │ (SAML/OIDC)   │
    └──────────────┘  └────────────────┘  └─────────────────┘
```

### Required Reading

- Hardt, D. (2024). *The OAuth 2.1 Authorization Framework*. RFC 9728.
- Sakimura, N. et al. (2014). *OpenID Connect Core 1.0*. OpenID Foundation.
- Yggdrasil Heimdall ID Federation Configuration Guide (2040). UoY Digital Press.

### Discussion Questions

1. SAML 2.0 uses XML assertions signed with XML Signature. OIDC uses JWTs signed with JWS. Compare the security properties and operational complexity of each. Why is the industry moving from SAML to OIDC?
2. An application requests the scope `admin:systems` during OAuth authorization. The user approves, but the authorization server should not grant this scope to a standard user. Design a scope evaluation policy that considers the user's role, the client's trusted status, and the authentication method.
3. The Heimdall ID platform federates with 47 cloud applications. When a user's Yggdrasil account is suspended, all 47 applications should immediately revoke access. Design a session management architecture that achieves revocation within 30 seconds, even when some applications do not support back-channel logout.

---

ᚴ **Lecture 5: Privilege Management — RBAC, ABAC, and ReBAC**

**Course:** SA107 — User & Identity Management
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Authorization determines what an authenticated user is allowed to do. While authentication answers "who are you?", authorization answers "what may you do?" This lecture covers the three major authorization models — Role-Based Access Control (RBAC), Attribute-Based Access Control (ABAC), and Relationship-Based Access Control (ReBAC) — their strengths, limitations, and composition in the Heimdall ID platform. We examine policy engines (OPA, Cedar), the principle of least privilege, and the dreaded problem of role explosion.

### RBAC: Roles as Permission Bundles

Role-Based Access Control (RBAC), defined in NIST NCSC-TG-5 and standardized in INCITS 359-2004, organizes permissions into roles, and assigns users to roles. A role is a named collection of permissions: `sysadmin` can read/write all system configurations, `auditor` can read all logs but write nothing, `developer` can deploy to staging but not production. The principle is simple: rather than assigning 200 individual permissions to each new hire, assign them a role that bundles the appropriate permissions.

The RBAC model has three levels:
- **RBAC0** (Flat RBAC): Users are assigned to roles; roles have permissions. Simple but doesn't scale.
- **RBAC1** (Hierarchical RBAC): Roles can inherit permissions from other roles. `junior-sysadmin` inherits `read-only` and adds `restart-service`; `senior-sysadmin` inherits `junior-sysadmin` and adds `modify-configuration`.
- **RBAC2** (Constrained RBAC): Adds separation of duties (SoD) constraints. A user with the `payment-creator` role cannot also hold the `payment-approver` role. This prevents fraud by requiring two people to complete a transaction.

At University of Yggdrasil, the Heimdall ID RBAC model defines 47 roles across five domains: Student, Faculty, Staff, Research, and Operations. Each domain has a role hierarchy:

```
Operations Domain:
  ops-observer → ops-operator → ops-administrator → ops-architect
```

A student enrolled in the Computer Systems Administration program is automatically assigned the `ops-observer` role upon enrollment (via the joiner provisioning workflow). As they complete courses and labs, they are escalated to `ops-operator` (can restart services, view logs) and eventually `ops-administrator` (can modify configurations, deploy updates).

### Role Explosion

The fundamental weakness of RBAC is **role explosion**. In a large organization with diverse access requirements, the number of roles grows exponentially. Consider a hospital: nurses in the emergency department need different permissions than nurses in oncology, who need different permissions than nurses in pediatrics. If you create a role for each combination (emergency-nurse, oncology-nurse, pediatrics-nurse, emergency-nurse-supervisor, oncology-nurse-supervisor...), you quickly have hundreds of roles, each with subtle differences. This makes the role model incomprehensible and unmaintainable.

The Heimdall ID platform addresses role explosion with **attribute conditions** on role assignments. Instead of creating separate roles for each department, a single `nurse` role with attribute conditions: `{department: $user.department}`. When evaluating permissions, the policy engine substitutes the user's department attribute into the condition. This is the bridge between RBAC and ABAC.

### ABAC: Attribute-Based Access Control

Attribute-Based Access Control (ABAC), defined in NIST SP 800-162, makes authorization decisions based on attributes of the subject (user), resource (object), action, and environment. An ABAC policy is a logical expression over these attributes:

```
PERMIT subject.role == "sysadmin"
  AND resource.environment == "production"
  AND action == "deploy"
  AND environment.time.hour BETWEEN 06 AND 22
  AND subject.mfa_level >= 3
```

This policy allows sysadmins to deploy to production only during business hours and only with high-assurance MFA. ABAC is expressive and fine-grained, but it is also complex to reason about. The combination of many attributes and many policies can produce unexpected results — a policy that permits access in one context may permit it in an unintended context. Policy analysis tools (like OPA's policy debugging and Cedar's type system) help, but ABAC requires rigorous testing and audit.

The Heimdall ID platform uses ABAC for fine-grained access control within roles. The `ops-administrator` role grants broad permissions, but ABAC conditions constrain those permissions: production deployments require MFA level 3, database access requires a signed change ticket, and emergency root access requires a four-eyes approval.

### ReBAC: Relationship-Based Access Control

Relationship-Based Access Control (ReBAC) is the 2040 evolution of authorization modeling. Where RBAC uses roles and ABAC uses attributes, ReBAC uses **relationships between entities** to determine access. The model comes from Google's Zanzibar system (2019), which handles all authorization for Google Drive, YouTube, and Cloud.

In ReBAC, the authorization question is not "Does this user have the sysadmin role?" or "Does this user's department match the resource's department?" but rather "What is the relationship between this user and this resource?" Relationships form a graph:

```
User:brynhild --[owner]--> Document:norse-myth-paper
User:brynhild --[member]--> Group:cs-faculty
Group:cs-faculty --[editor]--> Folder:cs-papers
Folder:cs-papers --[parent]--> Document:norse-myth-paper
```

From this graph, we can compute: User:brynhild is an owner of Document:norse-myth-paper (direct relationship), AND she is a member of Group:cs-faculty, which is an editor of Folder:cs-papers, which is the parent of Document:norse-myth-paper (transitive relationship). ReBAC evaluates both direct and indirect relationships, enabling fine-grained sharing models without role explosion.

The Heimdall ID platform implements ReBAC using Open Policy Agent's (OPA) Rego language with SpiceDB (an open-source Zanzibar implementation) as the relationship store. Every access check in the Bifrǫst Mesh goes through the Heimdall ID policy engine: the service asks "Can user X do action Y on resource Z?" and the engine evaluates the relationship graph in under 5ms.

### Policy Engines: OPA and Cedar

**Open Policy Agent (OPA)** is a general-purpose policy engine that evaluates Rego policies against JSON input. Rego is a declarative language: you specify what the policy should decide, not how to compute it. OPA runs as a sidecar or daemon on every node in the Bifrǫst Mesh, evaluating access decisions in microseconds.

**Cedar** is a policy language developed by AWS (2023) that offers a more human-readable syntax than Rego:

```
permit(
  principal == User::"heintr@yggdrasil.edu",
  action == Action::"deploy",
  resource == Service::"bifrost-proxy"
) when {
  principal.mfaLevel >= 3 && context.changeTicket != null
};
```

The Heimdall ID platform uses OPA for infrastructure access decisions (SSH, API, Kubernetes) and Cedar for application-level access decisions (document sharing, course enrollment, lab access). Both engines evaluate policies in under 10ms and support hot-reloading of policies without downtime.

### Required Reading

- NIST SP 800-162 (2014, updated 2038). *Attribute-Based Access Control*.
- Authzed (2039). *SpiceDB: Zanzibar-Inspired Authorization*. authzed.com/docs.
- Anderson, A. (2037). *Rule-Based Access Control — From XACML to ReBAC*. IEEE Computer Society.

### Discussion Questions

1. A university has 47 roles in its RBAC model. After three years of operation, it has 312 roles. Propose a strategy to simplify the role model without reducing the granularity of access control. Specifically, which roles should be replaced with ABAC conditions, and which should remain as RBAC roles?
2. ReBAC computes transitive relationships (A is a member of B, which has editor access to C, which is the parent of D → A can edit D). This can create unexpected permissions when the relationship graph changes. Design a system that alerts administrators when a relationship change creates new access paths that were not previously possible.
3. OPA evaluates policies in microseconds but requires all policy data to be in memory. SpiceDB evaluates relationship graphs in milliseconds but supports distributed operation. Under what circumstances would you use OPA alone, SpiceDB alone, or both in combination?

---

ᚱ **Lecture 6: Provisioning Lifecycle — Joiner, Mover, Leaver**

**Course:** SA107 — User & Identity Management
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

The provisioning lifecycle — joiner, mover, leaver (JML) — is the operational backbone of identity management. A new student enrolls (joiner): accounts must be created in 47 systems within 24 hours. A student changes their name or transfers departments (mover): identity attributes must be updated across all systems consistently. An employee leaves the organization (leaver): all access must be revoked within 4 hours (the industry standard for termination, per NIST SP 800-53). Failure at any stage creates either access gaps (user can't work) or security gaps (user retains access they shouldn't have). This lecture covers the JML lifecycle, SCIM provisioning, automated workflows, and the Heimdall ID provisioning pipeline.

### The Joiner Workflow

When a new student enrolls at University of Yggdrasil, the following events occur:

**T+0 minutes:** The Student Information System (SIS) creates a record with the student's personal information, enrollment status, and degree program. The SIS publishes a SCIM event to the Heimdall ID platform.

**T+30 seconds:** Heimdall ID creates the identity in the OpenLDAP directory. The attributes populated from the SIS record include: `uid` (generated from name + random suffix to avoid collisions), `cn`, `sn`, `mail`, `yggdrasil:degreeProgram`, `yggdrasil:enrollmentStatus`. The initial password is set to a temporary value that must be changed at first login.

**T+60 seconds:** Heimdall ID provisions accounts in connected systems via SCIM:
- Email (Google Workspace): account created, email alias set, group memberships assigned
- Learning Management System (Canvas): account created, course enrollments set
- VPN (WireGuard): certificate generated, access profile assigned
- Git hosting (GitHub Enterprise): account created, organization membership assigned
- Printing (PaperCut): account created with initial print quota
- Library (Alma): account created with borrowing privileges

**T+2 minutes:** Heimdall ID sends the student a welcome email with instructions for first login, MFA enrollment (register their YubiKey or set up a TOTP app), and links to orientation resources.

**T+24 hours:** If the student has not enrolled in MFA, Heimdall ID sends a reminder. After 72 hours without MFA enrollment, the account is restricted to limited functionality (can access email and course materials, but not SSH, VPN, or administrative systems).

The entire joiner workflow takes under 5 minutes from SIS event to fully provisioned account. The previous manual process (used until 2036) took 2-3 business days and involved 7 different IT staff members filling out 7 different forms. Automation reduced the provisioning time by 99.9% and eliminated 100% of manual transcription errors.

### The Mover Workflow

When a user's attributes change — name change, department transfer, role promotion, degree program change — the mover workflow updates all connected systems:

**Trigger:** A change event in the SIS (enrollment change), HR system (job change), or a user-initiated request (name change) is published to the Heimdall ID event bus.

**Processing:** Heimdall ID evaluates the change against its attribute mapping rules. A `department` change from "Computer Science" to "Physics" triggers: removal from CS groups, addition to Physics groups, revocation of CS-specific resources (lab access, compute cluster quotas), and provisioning of Physics-specific resources.

**Propagation:** SCIM PATCH requests are sent to all affected systems. The PATCH operation updates only the changed attributes, avoiding full reprovisioning. Systems that don't support SCIM PATCH are handled via custom connectors that translate the change into the system's API.

**Verification:** After propagation, Heimdall ID runs a reconciliation check: it queries each system to confirm that the attributes match the expected state. Discrepancies are flagged for manual review.

The most common mover events at University of Yggdrasil are name changes (average 47 per year) and degree program changes (average 312 per year). Name changes are particularly sensitive because they affect email addresses, display names, and authentication identifiers. The Heimdall ID platform handles name changes by creating a new `uid` and `mail` alias, keeping the old `uid` as an alias for 90 days (so email continues to be delivered), and updating all SCIM-connected systems. After 90 days, the old alias is removed. This process is transparent to the user and requires no IT intervention.

### The Leaver Workflow

When a student graduates or an employee leaves, the leaver workflow must revoke access promptly and completely:

**Trigger:** A termination event from the SIS (graduation, withdrawal) or HR system (resignation, termination). The event includes the termination date and the reason (which affects the urgency).

**Immediate (T+0 to T+15 minutes):**
- Disable the account in OpenLDAP (set `loginDisabled=TRUE`)
- Revoke all OAuth 2.0 tokens and sessions
- Revoke VPN certificates
- Remove from all administrative groups
- Enable forwarding on email to alumni address

**Deferred (T+15 minutes to T+24 hours):**
- Convert email account to read-only alumni mailbox
- Archive home directory and research data
- Remove from non-sensitive groups
- Revoke lab access (physical and logical)

**Archival (T+24 hours to T+90 days):**
- Retain account record for audit purposes
- Delete personal data per GDPR requirements (right to be forgotten for EU students)
- Transfer research data to supervisor or archive

**Deletion (T+90 days):**
- Delete the account from all systems
- Confirm deletion via reconciliation check

The leaver workflow is the most security-critical phase of the JML lifecycle. A study by the Ponemon Institute (2038) found that 29% of data breaches involve former employees who still have active accounts. The Heimdall ID platform addresses this with automated leaver processing (zero IT involvement, zero delay) and continuous auditing (daily reconciliation of active accounts against active enrollment/employment records). Orphaned accounts — accounts with no corresponding active enrollment or employment record — are flagged and disabled within 4 hours.

### SCIM: The Provisioning Protocol

SCIM (System for Cross-domain Identity Management, RFC 7644) is the HTTP-based protocol for automated user provisioning. SCIM defines a standard schema for user and group resources and REST API operations (GET, POST, PUT, PATCH, DELETE) for managing them. The key innovation of SCIM is the PATCH operation, which allows partial updates without replacing the entire resource — essential for the mover workflow.

Heimdall ID implements a SCIM gateway that translates between the OpenLDAP directory and the SCIM API. Connected systems register their SCIM endpoints with Heimdall ID; when a user is created, modified, or deleted in the directory, Heimdall ID sends the corresponding SCIM operation to each connected system. The gateway handles error responses, retries, and reconciliation, ensuring eventual consistency across all systems.

### Required Reading

- Hunt, P. et al. (2015). *System for Cross-domain Identity Management: Protocol*. RFC 7644.
- NIST SP 800-53 Rev 5 (2038). Control AC-2: Account Management.
- Yggdrasil Heimdall ID Provisioning Pipeline Documentation (2040). UoY Digital Press.

### Discussion Questions

1. During the joiner workflow, Heimdall ID provisions accounts in 47 systems within 5 minutes. If one system (say, the library) is down for maintenance during this period, the provisioning for that system fails. Design a retry and reconciliation architecture that handles transient failures without creating inconsistencies.
2. The leaver workflow disables the account immediately but retains data for 90 days. Under the GDPR's "right to be forgotten," an EU student can request that all personal data be deleted upon departure. How does this interact with the audit retention requirement? Design a leaver workflow that satisfies both legal and compliance requirements for EU and non-EU students.
3. Name changes affect authentication identifiers (uid), email addresses, and display names across 47 systems. Design a rollback mechanism in case the name change propagation fails for some systems. How far can you roll back, and what are the irreversible side effects?

---

ᛁ **Lecture 7: Secrets Management — Tokens, Certificates, and the Vault**

**Course:** SA107 — User & Identity Management
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Secrets — passwords, API keys, certificates, encryption keys, and tokens — are the credentials that prove digital identity between machines, not between humans. This lecture covers the lifecycle of secrets: generation, distribution, rotation, revocation, and destruction. We examine the architecture of HashiCorp Vault and its alternatives, the TLS/PKI certificate lifecycle, the challenge of secrets in containers and Kubernetes, and the Heimdall ID secrets management platform. The Norse metaphor: Mímir's Well, where Óðinn sacrificed an eye for wisdom — secrets have a cost, and must be protected accordingly.

### The Secrets Problem

A modern application uses dozens of secrets: database credentials, API keys, OAuth client secrets, TLS certificates, SSH keys, encryption keys, and service tokens. In a typical enterprise:

- 60% of secrets are hardcoded in configuration files or source code (Ponemon Institute, 2038)
- 80% of data breaches involve compromised secrets (Verizon DBIR, 2040)
- The average enterprise manages 9,000 secrets across 500 applications (CyberArk, 2039)

The consequences of poor secrets management are severe. In 2037, a major cloud provider suffered a 6-hour outage caused by an expired TLS certificate that nobody had rotated. The certificate had been manually managed, the team responsible had been reorganized, and the expiry date was missed. This incident cost an estimated $45 million in lost revenue and SLA penalties.

### HashiCorp Vault: The Industry Standard

HashiCorp Vault (launched 2015, open-sourced 2016) is the industry-standard secrets management platform in 2040. Vault provides:

- **Dynamic secrets**: On-demand credentials for databases, cloud providers, and PKI. Instead of a long-lived database password, Vault generates a short-lived username/password pair when the application starts, valid for a configurable TTL (default: 1 hour). When the TTL expires, the credentials are automatically revoked. Database administrators never see application passwords.
- **Encryption as a service**: AES-256-GCM encryption/decryption without exposing the key. Applications call Vault's transit endpoint to encrypt data; Vault performs the operation and returns the ciphertext. The key never leaves Vault.
- **PKI as a service**: Certificate Authority (CA) management with automatic enrollment, renewal, and revocation. Vault issues TLS certificates with short TTLs (24 hours by default), making rotation automatic and CRL/OCSP management trivial.
- **Identity-based access**: Vault authenticates clients via AppRole (machine), Kerberos (enterprise), JWT/OIDC (cloud), and Kubernetes service accounts (containers). Each authentication method maps to a Vault policy that defines which secrets the client can access.
- **Audit logging**: Every Vault operation (secret read, secret write, policy change, authentication) is logged to an audit device. tamper-evident log. This provides a complete audit trail of who accessed what secret and when.

The Heimdall ID platform runs Vault in high-availability mode: three Vault servers in the Hákon Computing Centre with an auto-unseal configuration using AWS KMS. The root key is protected by a Shamir's Secret Sharing scheme requiring 3 of 5 key holders to unseal the vault. In practice, auto-unseal handles routine restarts; Shamir unsealing is only required after a complete disaster recovery.

### PKI and Certificate Lifecycle

Public Key Infrastructure (PKI) is the system for issuing, distributing, revoking, and verifying digital certificates. A certificate binds a public key to an identity (a domain name, a user, a service) and is signed by a Certificate Authority (CA) that vouches for the binding.

The TLS certificate lifecycle consists of six phases:

1. **Key generation**: The subscriber generates a key pair (private + public). The private key never leaves the subscriber's system.
2. **CSR submission**: The subscriber creates a Certificate Signing Request (CSR) containing the public key, the identity (domain name), and requested attributes, signed with the private key.
3. **Validation and issuance**: The CA validates the identity (domain control validation for TLS, identity proofing for client certificates) and issues a certificate signed with the CA's private key.
4. **Deployment**: The certificate and private key are deployed to the server or client.
5. **Renewal**: Before the certificate expires, it must be renewed (repeat steps 2-4 with a new key pair or the same key).
6. **Revocation**: If the private key is compromised or the identity changes, the certificate must be revoked. The CA publishes the revocation in a Certificate Revocation List (CRL) and/or via the Online Certificate Status Protocol (OCSP).

**ACME** (Automated Certificate Management Environment, RFC 8555) automates steps 1-5. Let's Encrypt popularized ACME for free TLS certificates, and ACME is now the standard for automated certificate management in production. Cert-manager (for Kubernetes) and ACME clients (certbot, acme.sh) handle the entire lifecycle without human intervention.

At University of Yggdrasil, Vault serves as the internal CA for the Bifrǫst Mesh. Vault issues certificates with 24-hour TTLs, automatically renewed 4 hours before expiry. This means that no certificate in the mesh is valid for more than 24 hours, dramatically reducing the window for misuse. External-facing certificates (for `yggdrasil.edu` and subdomains) are issued by Let's Encrypt using ACME with DNS-01 validation.

### Secrets in Containers and Kubernetes

Containers and Kubernetes introduce unique secrets management challenges:

- **Kubernetes Secrets** are Base64-encoded objects stored in etcd. They are NOT encrypted by default (only encoded) and should never be used for sensitive data without additional protection. Vault's Kubernetes integration replaces Kubernetes Secrets with dynamic, short-lived credentials.
- **Container images** should never contain secrets. Build-time secrets (API keys needed during `docker build`) are injected using Vault's Agent sidecar and removed after the build.
- **Runtime secrets** are injected into containers via Vault Agent or the CSI Secrets Driver. The application never sees the Vault token; the sidecar authenticates with the Kubernetes service account, retrieves secrets from Vault, and writes them to a shared memory filesystem (tmpfs) that the application reads.
- **Secret rotation** in Kubernetes is automatic: when a secret changes, the pod is restarted (for mounted secrets) or the application re-reads the secret (for environment-injected secrets). Vault's dynamic secrets make this seamless: the new pod gets new credentials automatically.

### Required Reading

- HashiCorp (2039). *Vault Documentation — Architecture, Secrets Engines, PKI*. hashiCorp.com.
- Barnes, R. et al. (2019). *Automatic Certificate Management Environment (ACME)*. RFC 8555.
- Yggdrasil Heimdall ID Secrets Architecture Documentation (2040). UoY Digital Press.

### Discussion Questions

1. Vault's dynamic secrets generate short-lived credentials (1-hour TTL). What happens when an application needs to maintain a database connection that lasts longer than 1 hour? Design a credential rotation strategy that does not drop active connections.
2. A compromised Vault root token grants unlimited access to all secrets. Design a break-glass procedure for emergencies that requires multiple people to cooperate, logs every action, and automatically expires the emergency token after 30 minutes.
3. Kubernetes Secrets are Base64-encoded, not encrypted, and stored in etcd (which is typically encrypted at rest but not in transit between etcd nodes). Contrast three approaches: (a) use Kubernetes Secrets with etcd encryption, (b) use Vault Agent sidecars, and (c) use the CSI Secrets Driver. What are the tradeoffs in complexity, performance, and security?

---

ᚻ **Lecture 8: Zero-Trust Identity Architecture — Beyond the Perimeter**

**Course:** SA107 — User & Identity Management
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Zero-trust architecture (ZTA) is the dominant security model in 2040, replacing the perimeter-based "castle-and-moat" model that treated internal networks as trusted. The core principle: never trust, always verify. Every access request is authenticated, authorized, and encrypted, regardless of its origin. This lecture covers the NIST SP 800-207 zero-trust architecture, the Google BeyondCorp model, the CISA Zero Trust Maturity Model, and the Heimdall ID implementation of zero-trust across the Bifrǫst Mesh.

### From Perimeter to Zero Trust: A Paradigm Shift

The perimeter security model assumed that threats were external and the internal network was safe. Firewalls, VPNs, and DMZs defined the boundary between "us" and "them." This model worked when employees worked in offices, connected to a corporate network, and accessed internal applications. It failed catastrophically when:

- **BYOD and remote work** meant that unmanaged devices connected to the network (the 2020 pandemic forced this transition overnight)
- **Cloud applications** meant that data and services were outside the perimeter
- **Supply chain attacks** meant that trusted software could be compromised (SolarWinds, 2020; 3CX, 2023)
- **Lateral movement** meant that once inside the perimeter, attackers could move freely between systems

The Google BeyondCorp initiative (2014-2017) demonstrated that zero-trust was feasible at scale. Google eliminated its corporate VPN and moved all applications to the internet, protected by identity-based access controls. Every access request required authentication, device health attestation, and contextual authorization. The result: employees could work from any device on any network, and the security team had visibility into every access decision.

NIST SP 800-207 formalized zero-trust architecture in 2020, defining three core components:
1. **Policy Engine (PE)**: Makes access decisions based on policy, subject attributes, resource attributes, and environmental context.
2. **Policy Administrator (PA)**: Executes the PE's decisions by establishing or terminating communication paths.
3. **Policy Enforcement Point (PEP)**: Sits in front of the protected resource and enforces the PE's decisions.

### The Five Pillars of Zero-Trust Identity

The CISA Zero Trust Maturity Model (2023, updated 2039) defines five pillars:

**1. Identity:** Every user, device, and service must be authenticated and authorized before accessing any resource. Phishing-resistant MFA is required for all human users. Service accounts use workload identity (spiffe/spire) with automatic rotation.

**2. Devices:** Every device must be registered, compliant with security policies, and continuously assessed. Device health signals (OS patch level, disk encryption, EDR status) are included in authorization decisions. A compromised device is denied access regardless of the user's identity.

**3. Networks:** Microsegmentation replaces network-level trust. Every service communication is encrypted (mTLS). Network policies allow only explicitly authorized traffic. There is no "internal" network where trust is assumed.

**4. Applications:** Every application is protected by an identity-aware proxy. Access is granted based on user identity, device health, and contextual risk — not network location. Session tokens are short-lived and continuously validated.

**5. Data:** Every data asset has a classification and an access policy. Data is encrypted at rest and in transit. Access is logged and audited. Data loss prevention (DLP) policies prevent unauthorized exfiltration.

The Heimdall ID platform is the identity pillar of the Yggdrasil zero-trust architecture. It authenticates every request, evaluates authorization policies, and provides continuous risk assessment. The policy engine is OPA running on every node, evaluating Rego policies with input from the identity service, device health service, and threat intelligence feeds.

### Continuous Adaptive Risk and Trust Assessment (CARTA)

The original zero-trust model was binary: either you're authenticated and authorized, or you're not. The 2036 Gartner CARTA model adds nuance: **risk and trust are not binary but continuous**. A user who authenticates from their office during business hours with a corporate laptop and FIDO2 key is low-risk. A user who authenticates from a new country at 3 AM with a password is high-risk. The policy engine considers:

- **User context**: role, group memberships, recent activity, past violations
- **Device context**: registration status, OS patch level, disk encryption, EDR status, compliance score
- **Network context**: source IP, geographic location, time of day, known threat intelligence
- **Resource context**: sensitivity level, classification, compliance requirements
- **Session context**: duration, volume of data, patterns of access

The policy engine computes a **trust score** (0-100) for each request. A trust score of 80+ allows full access. A score of 60-79 allows read-only access with step-up authentication for write operations. A score below 60 denies access and triggers a security alert.

The Heimdall ID platform implements CARTA with a real-time risk scoring engine that evaluates 47 signals per authentication request. The signals are weighted and combined using a machine learning model trained on historical access patterns and security incidents. When the trust score drops during a session (e.g., the request originates from an anomalous location), the engine prompts for step-up authentication or terminates the session.

### SPIFFE and Service Identity

Zero-trust applies to machines, not just humans. The SPIFFE (Secure Production Identity Framework for Everyone, spiffe.io) specification defines a standard for service identity. Every service in the Bifrǫst Mesh has a SPIFFE ID: `spiffe://yggdrasil.edu/bifrost-proxy/prod`. This ID is encoded in an X.509 SVID (SPIFFE Verifiable Identity Document) that the service presents during mTLS handshake. The SPIRE agent running on each node manages SVID issuance and rotation (with 1-hour TTLs), so certificates are always fresh and never manually managed.

Service identity eliminates the need for shared secrets between services. Instead of a database password stored in a configuration file, the database verifies the calling service's SPIFFE ID and grants access based on the service's authorized permissions. The Heimdall ID policy engine evaluates service-to-service access the same way it evaluates user-to-service access: based on identity, context, and policy.

### Required Reading

- NIST SP 800-207 (2020, updated 2038). *Zero Trust Architecture*.
- CISA (2023, updated 2039). *Zero Trust Maturity Model*.
- Scovetta, L. & Maru, R. (2037). *Beyond BeyondCorp: Zero-Trust in Practice*. O'Reilly. Chapters 1-5.
- SPIFFE specification (2038). spiffe.io.

### Discussion Questions

1. In a zero-trust architecture, every access decision requires authentication, authorization, and encryption. This adds latency to every request. The Heimdall ID policy engine evaluates requests in under 10ms, but the total authentication overhead (network round-trips, token validation, policy evaluation) adds 30-50ms per request. Design a caching strategy that reduces this overhead without compromising the zero-trust principle.
2. CARTA adjusts access based on risk scores. A legitimate user with a trust score of 55 (below the 60 threshold) is denied access. What could cause this false positive? Design a remediation workflow that helps the user regain access without weakening security.
3. SPIFFE SVIDs have 1-hour TTLs, meaning every service must re-attest every hour. If the SPIRE server is down, services cannot obtain new SVIDs, and mTLS connections begin failing after 1 hour. Design a high-availability architecture for SPIRE that ensures SVID availability even during server failures.

---

ᛃ **Lecture 9: Auditing, Compliance, and the纪委书记**

**Course:** SA107 — User & Identity Management
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Identity auditing and compliance are the accountability mechanisms that ensure identity policies are enforced, violations are detected, and evidence is available for regulatory review. This lecture covers identity audit logging, access certification, compliance frameworks (SOC 2, ISO 27001, NIST CSF, GDPR), and the Heimdall ID compliance engine. The Norse metaphor: the Norns — Urðr (What Was), Verðandi (What Is), Skuld (What Shall Be) — who record all events in the fabric of Yggdrasil. Audit logs are our Norns' records: they document what happened, when, and by whom, so that accountability cannot be evaded.

### The Audit Imperative

Identity systems generate audit events for every significant action: authentication, authorization, provisioning, deprovisioning, policy change, and administrative action. These events are the primary evidence for:

- **Security investigations**: When a breach occurs, audit logs tell the investigator who accessed what, when, and from where.
- **Compliance audits**: SOC 2, ISO 27001, and other frameworks require audit trails for access control.
- **Operational visibility**: Audit logs help operations teams understand system behavior and detect anomalies.
- **Legal proceedings**: Audit logs may be subpoenaed in legal cases involving data breaches, harassment, or intellectual property theft.

The Heimdall ID platform generates an average of 2.3 million audit events per day. These events flow through a pipeline: OpenLDAP audit log → Heimdall ID event bus → OpenSearch (for real-time search and alerting) → S3-compatible object storage (for long-term retention) → OpenSearch Dashboards (for visualization and reporting).

### Access Certification: The Periodic Review

Access certification (also called access review or recertification) is the process of periodically reviewing user access to ensure that it remains appropriate. The principle: every user should have only the access they need for their current role, and no more. Access certifications are required by SOC 2 (CC6.1), ISO 27001 (A.9.2.6), and most industry regulations.

The certification process:
1. **Generate reports**: For each resource (application, system, data set), list all users with access and their permission levels.
2. **Assign reviewers**: The resource owner (application owner, data steward) reviews the access list for their resources.
3. **Review and decide**: For each user, the reviewer decides to retain, modify, or revoke access. Retention should be justified by business need; modification reduces excessive permissions; revocation removes access that is no longer needed.
4. **Execute decisions**: Approved modifications and revocations are executed automatically by the Heimdall ID platform.
5. **Remediate exceptions**: Users who failed to complete certification are escalated to their manager and, if not resolved within 14 days, all questionable access is revoked by default.

At University of Yggdrasil, access certifications are conducted quarterly. The 2040 Q1 certification reviewed 47,000 identities across 23 systems and revoked 1,247 excessive permissions (2.6% of all permissions). The most common findings: employees who transferred departments but retained access from their previous role (46% of findings), students who graduated but retained access to research systems (31%), and service accounts with excessive privileges (23%).

### Compliance Frameworks

**SOC 2** (Service Organization Control 2) defines criteria for managing customer data based on five Trust Service Criteria: Security, Availability, Processing Integrity, Confidentiality, and Privacy. For identity management, SOC 2 requires:
- CC6.1: Logical and physical access controls
- CC6.2: Access permissions based on need
- CC6.3: Access provisioning and deprovisioning
- CC6.4: Periodic access review

**ISO 27001** defines an Information Security Management System (ISMS). Annex A Control A.9 covers access control:
- A.9.1.1: Access control policy
- A.9.2.1: User registration and de-registration
- A.9.2.2: User access provisioning
- A.9.2.3: Privileged access management
- A.9.2.6: Removal or adjustment of access rights

**GDPR** (General Data Protection Regulation) requires data minimization (Article 5(1)(c)) and purpose limitation (Article 5(1)(b)). For identity management, this means: collect only the identity data necessary for the purpose, and don't use identity data collected for authentication for marketing or other purposes without consent. The Heimdall ID platform enforces data minimization by storing only the attributes required by each connected system and deleting them when no longer needed.

The Heimdall ID compliance engine maps identity controls to SOC 2, ISO 27001, and GDPR requirements, producing audit-ready reports that demonstrate compliance. The engine continuously monitors identity events and generates alerts for policy violations: failed login attempts exceeding the threshold, privileged access outside business hours, dormant accounts, and separation-of-duty violations.

### Forensic Investigation: The Audit Trail

When a security incident occurs, the audit trail is the primary evidence for investigation. The Heimdall ID platform provides:
- **Timeline reconstruction**: Combine authentication logs, authorization logs, and application logs to reconstruct the attacker's actions minute by minute.
- **Lateral movement detection**: Identify accounts and systems accessed by a compromised user during the incident window.
- **Impact assessment**: Determine which data and systems were accessed, modified, or exfiltrated during the incident.
- **Chain of custody**: Audit logs are stored in append-only, tamper-evident storage (using Merkle tree hashing) to ensure they cannot be modified after the fact.

### Required Reading

- AICPA (2038). *SOC 2 Trust Services Criteria*. aicpa.org.
- ISO/IEC 27001:2022 (updated 2037). *Information Security Management Systems*.
- EU General Data Protection Regulation (2016, updated 2039). Articles 5, 25, 32, 35.

### Discussion Questions

1. An audit reveals that 2.6% of all permissions are excessive. The operations team argues that revoking these permissions will generate 1,247 support tickets from users who can no longer access resources they've been using (even if they shouldn't have had access in the first place). Design a remediation process that minimizes support burden while enforcing the principle of least privilege.
2. Audit logs stored in append-only, Merkle-hashed storage cannot be modified, but they can be deleted (an attacker with sufficient access could delete the entire log). Design a log storage architecture that guarantees immutability even against an attacker with administrative access.
3. GDPR requires data minimization, but the Heimdall ID platform stores identity attributes for 47 connected systems. After a user leaves the university, how long should identity data be retained? Consider the competing requirements of: (a) audit trail integrity (keep data as long as it may be needed for investigation), (b) GDPR right to erasure (delete data upon request), and (c) operational necessity (keep data long enough to support the leaver workflow).

---

ᛋ **Lecture 10: Identity for AI Agents and Non-Human Entities**

**Course:** SA107 — User & Identity Management
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

By 2040, non-human identities outnumber human identities in most organizations. The University of Yggdrasil operates 800 AI agent identities and 3,400 IoT device identities — nearly four times the 47,000 human identities. Service accounts, CI/CD pipelines, API keys, and automation bots all require identity, but they have fundamentally different characteristics than human users: they don't have MFA devices, they don't respond to phishing, and they never forget their credentials (but they can be compromised). This lecture covers the identity challenges of non-human entities, workload identity (SPIFFE/SPIRE), API authentication, and the Heimdall ID platform's approach to governing machine identity at scale.

### The Non-Human Identity Explosion

Non-human identities fall into several categories:

- **Service accounts**: Identities used by applications and services to authenticate to other services. A typical microservices architecture might have 50-200 service accounts.
- **API keys**: Static credentials used by external applications to access APIs. Long-lived, frequently over-privileged, and rarely rotated.
- **CI/CD pipeline identities**: Identities used by build and deployment pipelines to push artifacts, deploy services, and run tests.
- **IoT device identities**: Certificates and keys embedded in sensors, actuators, and edge devices.
- **AI agent identities**: Identities used by autonomous AI systems to interact with other systems on behalf of humans or organizations.

The problems with non-human identity in 2040 are well-documented:
- **Over-provisioned**: Service accounts often have admin-level access because it's easier than figuring out the minimum required permissions.
- **Long-lived**: API keys and service account passwords are rarely rotated because the impact of rotation is hard to predict.
- **Unaudited**: Non-human identities are often excluded from access certifications because they don't have a "manager" who can approve their access.
- **Unmonitored**: Non-human identities don't trigger anomaly detection because their behavior patterns are different from humans.

The Verizon DBIR (2040) found that 31% of breaches involving non-human identities were caused by over-provisioned service accounts. The CyberArk report (2039) found that the average enterprise has 40 non-human identities for every human identity, and 50% of those have secrets that never expire.

### Workload Identity: SPIFFE and SPIRE

The SPIFFE specification (described in Lecture 8) provides a standard for workload identity. Every workload (container, process, server) in the Bifrǫst Mesh has a SPIFFE ID that serves as its immutable identity. The SPIRE agent running on each node manages the lifecycle of SVIDs (X.509 certificates with SPIFFE IDs embedded).

The key advantage of workload identity over service accounts: **no passwords, no API keys, no static credentials.** Workloads authenticate using mTLS with their SPIFFE SVID, which is automatically issued and rotated by SPIRE. The workload never sees a password; it never stores a password; it never transmits a password. The attack surface for credential theft is eliminated.

Heimdall ID integrates SPIRE for all internal workloads. When a new pod is scheduled on the Bifrǫst Mesh, the SPIRE agent on that node:
1. Attests the pod's identity using Kubernetes workload attestation (verifying the pod's service account, namespace, and container image)
2. Issues an SVID with the pod's SPIFFE ID
3. Makes the SVID available to the pod via the SPIRE Workload API
4. Automatically rotates the SVID before expiry (default 1-hour TTL)

The pod then uses this SVID for all mTLS connections within the mesh. No code changes are needed; the Envoy sidecar proxy handles mTLS transparently.

### API Authentication: OAuth 2.0 for Machines

External API authentication (between organizations or between cloud services) uses OAuth 2.0 with the **client credentials grant**. Unlike the authorization code grant (which requires human interaction), the client credentials grant allows a machine to obtain an access token by presenting its client ID and client secret (or, preferably, a signed JWT assertion).

In the Heimdall ID platform, API authentication follows this flow:
1. Client (an external service) sends a token request to the Heimdall ID token endpoint with its client_id and a signed JWT assertion
2. Heimdall ID validates the JWT signature, checks the client's authorized scopes, and issues an access token
3. Client uses the access token in the Authorization header of API requests
4. Resource server validates the token with Heimdall ID (or locally using JWT verification)

The JWT assertion is preferred over client secrets because it uses asymmetric cryptography: the client signs the assertion with its private key, and Heimdall ID verifies it with the client's public key. No shared secret is transmitted, eliminating the risk of secret interception.

### AI Agent Identity: The Frontier

AI agents present a unique challenge for identity management. Unlike traditional service accounts, AI agents:

- **Act autonomously**: They make decisions and take actions without human initiation.
- **Act on behalf of humans**: They may represent a specific user (e.g., a personal AI assistant) or an organization (e.g., an automated customer service agent).
- **Have variable scope**: An AI agent's permissions may change dynamically based on context (e.g., an agent can approve purchases under $100 but requires human confirmation for larger amounts).
- **Require auditability**: Every action taken by an AI agent must be traceable to the agent and the human or organization it represents.

The Heimdall ID platform extends identity to AI agents through **delegated authority**:
1. The human (or organization) authenticates and authorizes the AI agent to act on their behalf.
2. Heimdall ID issues a **delegation token** that specifies the agent's identity, the delegator's identity, the scope of delegated authority, and the expiration time.
3. The AI agent presents the delegation token when accessing services.
4. Services verify the delegation token with Heimdall ID and enforce the scope restrictions.

This model ensures that AI agents never have more authority than their delegator, that all actions are attributed to both the agent and the delegator, and that delegation can be revoked at any time by the delegator or by a security administrator.

### Required Reading

- SPIFFE specification (2038). spiffe.io.
- Hardt, D. (2024). *The OAuth 2.1 Authorization Framework*. RFC 9728 (Section on Client Credentials).
- Evans, R. & Heiðarsdóttir, S. (2039). *Governing Autonomous AI Agents: Identity and Delegation Frameworks*. IEEE Security & Privacy.

### Discussion Questions

1. An AI agent authorized to approve purchases under $100 is tricked by a social engineering attack into approving a $99 purchase 100 times in one hour, totaling $9,900. The individual purchases are within scope, but the aggregate is abusive. Design a rate-limiting and anomaly detection system for AI agent actions that prevents this kind of abuse without blocking legitimate activity.
2. A service account used by a CI/CD pipeline has write access to the production deployment system. The pipeline configuration is in a Git repository. If an attacker gains write access to the Git repository, they can modify the pipeline to deploy malicious code — using the service account's legitimate permissions. How does workload identity (SPIFFE) address this threat? What additional controls are needed?
3. Delegation tokens allow humans to authorize AI agents to act on their behalf. But what happens when the human is no longer available (离开了 on vacation, incapacitated, or departed the organization)? Design a delegation lifecycle that includes expiry, revocation, and emergency transfer of delegated authority.

---

ᛏ **Lecture 11: Identity Governance and Administration (IGA)**

**Course:** SA107 — User & Identity Management
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

Identity Governance and Administration (IGA) is the organizational and policy framework that ensures the right people have the right access to the right resources at the right time, for the right reasons. IGA encompasses access requests, approvals, certifications, segregation of duties, role lifecycle management, and compliance reporting. This lecture covers the IGA lifecycle, the Gartner IGA market, role mining and optimization, and the Heimdall ID governance module.

### The IGA Lifecycle

IGA is a continuous process, not a one-time project. The lifecycle has six phases:

1. **Plan**: Define identity policies, role models, and access rules aligned with business objectives and compliance requirements. The policy defines who should have access to what, under what conditions, and for how long.
2. **Request**: Users (or their managers) request access through a self-service portal. The request includes the resource, the justification, and the duration. The IGA system routes the request to the appropriate approver(s).
3. **Approve**: Approvers review the request and approve, deny, or delegate. Approval workflows enforce segregation of duties (no single person can approve their own requests), escalation (unanswered requests are escalated to the next level), and delegation (approvers can delegate their authority to a deputy during absence).
4. **Provision**: Once approved, the IGA system provisions the access across all connected systems via SCIM, API, or custom connectors. Provisioning is auditable: every change is recorded with the request ID, approver, timestamp, and justification.
5. **Review**: Periodic access certifications (covered in Lecture 9) ensure that access remains appropriate over time.
6. **Revoke**: When access is no longer needed (leaver workflow, certification revocation, or explicit revocation request), the IGA system deprovisions access across all connected systems.

### Role Mining and Optimization

Role mining is the process of discovering roles from existing access data. In a mature organization, roles have grown organically: users have accumulated access over years, and the relationship between roles and actual job functions has become unclear. Role mining uses statistical analysis and machine learning to identify patterns of access that can be consolidated into roles.

The two approaches to role mining:

**Top-down role mining** starts with business functions and defines roles based on what people in each function need. This is the preferred approach for new deployments because it produces clean, well-understood roles. The Heimdall ID platform uses top-down role definition: each role is mapped to a job function with a clear description and a defined set of permissions.

**Bottom-up role mining** starts with existing access data and identifies clusters of users with similar permissions. This is useful for legacy environments where role definitions have drifted from reality. Tools like SailPoint IdentityIQ and Saviynt use correlation algorithms to identify candidate roles from access data.

At University of Yggdrasil, the Heimdall ID governance module performed a bottom-up role mining exercise in 2038 and discovered that the existing 312 roles could be consolidated into 47 well-defined roles with ABAC conditions for fine-grained access. The consolidation reduced the average number of roles per user from 4.3 to 2.1, eliminated 35 overlapping roles, and reduced the time for quarterly access certifications by 60%.

### Segregation of Duties

Segregation of Duties (SoD) ensures that no single person can complete a critical transaction alone. SoD rules prevent fraud by requiring that the person who creates a payment is different from the person who approves it, that the person who deploys code is different from the person who reviews it, and that the person who administers systems is different from the person who audits them.

SoD rules are expressed as mutually exclusive role or permission combinations:
- `payment-creator` and `payment-approver` are mutually exclusive
- `system-administrator` and `security-auditor` are mutually exclusive
- `code-deployer` and `code-reviewer` are mutually exclusive for the same application

The Heimdall ID platform enforces SoD rules at three levels:
1. **Preventive**: The access request workflow checks for SoD violations before granting access. If the user already holds a conflicting role, the request is blocked and routed to the SoD exception process.
2. **Detective**: The compliance engine monitors for SoD violations that may arise from organizational changes, role modifications, or manual provisioning overrides. Violations are flagged for review.
3. **Corrective**: When a SoD violation is detected, the IGA system generates a remediation workflow that removes one of the conflicting roles and notifies the affected user and their manager.

### Entitlement Management and the Principle of Least Privilege

Entitlement management is the process of defining, granting, and revoking fine-grained permissions. The principle of least privilege (PoLP) states that every user should have the minimum permissions necessary to perform their job functions and no more. In practice, this means:

- **Default deny**: Access is denied unless explicitly granted. No "grant all" or "admin by default" policies.
- **Just-in-time access**: Privileges are granted for the duration of a specific task, not permanently. An administrator who needs root access to debug an issue receives root access for 2 hours, after which it is automatically revoked.
- **Blast radius minimization**: Permissions are scoped to the smallest resource possible. Write access to one database table, not the entire database. Admin access to one server, not the entire cluster.
- **Time-bound access**: Access grants have expiration dates. Contractors receive access for the duration of their contract; project teams receive access for the duration of the project.

The Heimdall ID platform implements just-in-time access through **break-glass privileges**: emergency access to production systems is granted for a fixed duration (default: 2 hours), logged with a justification, and automatically revoked when the duration expires. Break-glass events are reviewed by the security team within 24 hours. In 2040 Q1, there were 847 break-glass events across the Bifrǫst Mesh, of which 12 were flagged for review (1.4% — indicating that the just-in-time model is working as intended).

### Required Reading

- Gartner (2039). *Market Guide for Identity Governance and Administration*. Gartner Research.
- SailPoint (2039). *Identity Governance for Dummies*, 3rd Edition. Wiley.
- NIST SP 800-53 Rev 5 (2038). Controls AC-2 (Account Management), AC-3 (Access Enforcement), AC-4 (Information Flow Enforcement), AC-6 (Least Privilege).

### Discussion Questions

1. Bottom-up role mining at University of Yggdrasil consolidated 312 roles into 47. The 47 roles cover 97% of access patterns, but 3% of access patterns don't fit neatly into any role. How should the IGA system handle these "long tail" access patterns? What are the trade-offs between creating additional roles (which increases complexity) and using ABAC conditions (which increases policy evaluation time)?
2. A break-glass request for root access to a production database is justified with "urgent production issue." The security team reviewing the request determines that the issue could have been resolved with read-only access, which the user already had. Design a post-incident review process that educates users about least privilege without creating a punitive culture that discourages legitimate break-glass requests.
3. SoD rules prevent a single person from both creating and approving payments. But in a small organization (5 people), every person wears multiple hats, and strict SoD is impossible. Design a compensating control for small organizations that provides similar fraud prevention without requiring more people.

---

ᛟ **Lecture 12: The Future of Identity — Post-Quantum, Decentralized, and Self-Sovereign**

**Course:** SA107 — User & Identity Management
**Degree:** Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

---

### Overview

The final lecture examines three forces reshaping digital identity: post-quantum cryptography (PQC), decentralized identity (DID), and self-sovereign identity (SSI). Each addresses a fundamental challenge: PQC addresses the threat that quantum computers pose to current cryptographic algorithms; DID addresses the centralization of identity in corporate silos; SSI addresses the user's lack of control over their own identity data. We examine the NIST PQC standards, the W3C DID specification, Verifiable Credentials, and the emerging European Digital Identity Framework (EUDI), and we project how these technologies will reshape identity management in the 2040s.

### The Post-Quantum Threat to Identity

Current identity protocols rely on public-key cryptography: RSA and Elliptic Curve Cryptography (ECC) for key exchange, digital signatures, and certificate verification. A cryptographically relevant quantum computer (CRQC) running Shor's algorithm could break RSA and ECC in polynomial time, rendering all current TLS certificates, digital signatures, and key exchanges vulnerable.

When will a CRQC arrive? The consensus in 2040 is "within 10-20 years" — meaning between 2050 and 2060. NIST responded by standardizing post-quantum cryptographic algorithms in 2024:

- **CRYSTALS-Kyber** (ML-KEM): Key encapsulation mechanism for key exchange. Replaces RSA and ECDH key exchange in TLS, VPNs, and S/MIME.
- **CRYSTALS-Dilithium** (ML-DSA): Digital signature algorithm. Replaces RSA and ECDSA signatures in certificates, code signing, and document signing.
- **FALCON** (FN-DSA): Alternative digital signature algorithm with smaller signatures than Dilithium.
- **SPHINCS+** (SLH-DSA): Hash-based signature algorithm. Conservative, well-understood security, but larger signatures.

The migration to PQC is already underway in 2040. The Heimdall ID platform uses **hybrid TLS**: classical (X25519) + post-quantum (ML-KEM-768) key exchange in parallel. If either the classical or the post-quantum algorithm is broken, the other still provides security. This is the approach recommended by NIST and the IETF for the transition period (2025-2055).

Certificate management under PQC requires rethinking. PQC signatures are larger than classical signatures: a Dilithium signature is 2,420 bytes (vs. 64 bytes for Ed25519). This affects TLS handshake size, certificate chain validation time, and storage requirements for large certificate repositories. The Heimdall ID platform has migrated all internal CA certificates to Dilithium and issues end-entity certificates with a hybrid Dilithium+Ed25519 signature chain.

### Decentralized Identity: The W3C DID Specification

Decentralized Identifiers (DIDs) are a W3C standard that enables self-sovereign identity: identifiers that are created, owned, and controlled by the subject, not by a central authority. A DID is a globally unique identifier that resolves to a DID Document, which contains the subject's public keys and service endpoints.

Example DID: `did:web:yggdrasil.edu:heintr-odinsson`

Its DID Document:
```json
{
  "@context": ["https://www.w3.org/ns/did/v1"],
  "id": "did:web:yggdrasil.edu:heintr-odinsson",
  "verificationMethod": [{
    "id": "#key-1",
    "type": "Multikey",
    "controller": "did:web:yggdrasil.edu:heintr-odinsson",
    "publicKeyMultibase": "z6MkhaXgBZDvotDkL5257fa8tiHeChG4p5H3..."
  }],
  "authentication": ["#key-1"],
  "service": [{
    "id": "#oidc",
    "type": "OpenIDConnect",
    "serviceEndpoint": "https://id.yggdrasil.edu/oidc/heintr-odinsson"
  }]
}
```

DIDs enable a fundamentally different identity architecture: instead of relying on a central IdP to assert identity, the user controls their own DID and presents Verifiable Credentials (VCs) issued by trusted authorities. A student's degree credential is issued by the university as a VC, stored in the student's digital wallet, and presented to employers without any call to the university's systems.

This model has profound implications for privacy: the verifier (employer) does not need to contact the issuer (university) to verify the credential. The credential is signed with the issuer's DID, and the verifier checks the signature against the issuer's DID Document. This eliminates the "phone home" problem where every credential verification creates a record at the issuing institution.

### Verifiable Credentials and the European Digital Identity Wallet

Verifiable Credentials (VCs) are the data model for expressing claims about a subject in a tamper-evident, privacy-respecting way. A VC contains:
- **Issuer**: The DID of the organization that issued the credential
- **Subject**: The DID of the person or entity the credential is about
- **Claims**: The attributes being asserted (e.g., "degree: Bachelor of Science", "graduationDate: 2040-06-15")
- **Proof**: A digital signature (or ZK proof) that the issuer created the credential

The European Digital Identity Framework (EUDI), passed in 2024 and mandatory for all EU member states by 2027, requires every EU citizen to have access to a digital identity wallet that can store and present VCs. The wallet is controlled by the citizen, not by the government or any corporation. VCs are issued by trusted authorities (governments, universities, employers, banks) and stored in the wallet. The citizen chooses which credentials to present to which verifiers.

The Heimdall ID platform is piloting EUDI wallet integration for the 2040-2041 academic year. Students can receive their enrollment verification, degree completion, and transcript credentials as VCs in their EUDI wallet. When applying for jobs or graduate programs, they present these VCs directly, without requiring the university to produce paper transcripts or respond to verification requests.

### Self-Sovereign Identity and Zero-Knowledge Proofs

The most advanced form of decentralized identity uses **zero-knowledge proofs (ZKPs)** to prove claims without revealing the underlying data. For example:

- Prove that you are over 21 without revealing your exact date of birth
- Prove that you have a university degree without revealing which university or what grade
- Prove that your credit score is above 700 without revealing the exact score

ZKPs in identity management are enabled by **Selective Disclosure** and **Predicate Proofs**. Selective Disclosure allows the holder to present only the claims they choose from a VC (e.g., present the "over 21" claim from a national ID card without revealing the card number or address). Predicate Proofs allow the holder to prove a mathematical property of a claim without revealing the claim itself (e.g., prove that birthDate < 2003-01-01 without revealing birthDate).

The Biryptographic foundation for ZKPs in identity management is the **zk-SNARK** (Zero-Knowledge Succinct Non-Interactive Argument of Knowledge) and **zk-STARK** (Scalable Transparent ARgument of Knowledge) families of proof systems. These allow a prover to convince a verifier of a statement's truth without revealing any information beyond the statement itself, in a format that is short (a few hundred bytes) and fast to verify (milliseconds).

The Heimdall ID platform is researching ZKP-based identity verification for the 2042-2043 academic year, with the goal of allowing students to prove enrollment status, degree program, and campus access rights without revealing their personal information to every service they interact with.

### The Heimdall ID Roadmap: 2040-2045

The Heimdall ID platform roadmap for the next five years:

- **2040-2041**: PQC migration (hybrid TLS, Dilithium certificate chains), EUDI wallet pilot
- **2041-2042**: Decentralized identity integration (DID/VC for enrollment verification), continuous adaptive authentication (CARTA) in production
- **2042-2043**: ZKP-based selective disclosure, AI agent identity governance framework
- **2043-2044**: Passwordless-only authentication (deprecate TOTP, require FIDO2), self-healing identity (automatic remediation of access anomalies)
- **2044-2045**: Full post-quantum cryptography (deprecate classical-only TLS), autonomous identity governance (AI-assisted access certification and role optimization)

### Course Synthesis: The Heimdallr Principle

This course began with Heimdallr, the guardian of the Bifrǫst bridge, and returns to him now. Heimdallr's vigilance — seeing for a hundred leagues, hearing the grass grow, needing less sleep than a bird — is the model for identity management in 2040: continuous verification, comprehensive visibility, and tireless attention.

The twelve lectures have covered the full spectrum of identity management: authentication, directory services, federation, authorization, provisioning, secrets management, zero-trust, auditing, compliance, non-human identity, governance, and the future. Each topic contributes to the Heimdallr principle: **every request is authenticated, every access is authorized, every action is audited, and every identity is governed.**

The systems administrator who masters identity management becomes the Heimdallr of their organization: the guardian who ensures that the right people have the right access at the right time, and that every interaction with the infrastructure is trustworthy. This is not a small responsibility, but it is an essential one. In a world where identity is the perimeter, the identity administrator is the first and last line of defense.

### Required Reading

- NIST FIPS 203 (2024). *Module-Lattice-Based Key-Encapsulation Mechanism Standard* (ML-KEM).
- W3C (2022, updated 2039). *Decentralized Identifiers (DIDs) v1.0*. w3.org/TR/did-core.
- EU Regulation 2024/1183. *European Digital Identity Framework (EUDI)*.
- European Commission (2039). *EUDI Wallet Architecture Reference*. europa.eu.

### Discussion Questions

1. The transition to post-quantum cryptography requires replacing every certificate, key exchange, and digital signature in the infrastructure. Estimate the number of certificates in a 10,000-node data center and design a migration plan that transitions from hybrid to pure-quantum TLS without service disruption.
2. Decentralized identity (DIDs and VCs) gives users control over their credentials, but it also means users must manage their own keys. If a user loses their wallet (and all their private keys), they lose their digital identity. Design a recovery mechanism for decentralized identity that balances security, usability, and privacy.
3. Zero-knowledge proofs allow selective disclosure of credential claims. But selective disclosure can be misused: a bar could require a ZKP that you are over 21 AND that you are not on a terrorist watch list, effectively performing a background check without your knowledge or consent. Design a governance framework for ZKP-based identity that prevents misuse while preserving privacy.

---

## Final Examination Preparation

### Course: SA107 — User & Identity Management
### Degree: Bachelor of Science in Computer Systems Administration, University of Yggdrasil, 2040

The final examination consists of eight essay questions. Choose four to answer. Each answer should be approximately 800-1200 words, demonstrating both theoretical understanding and practical application. Reference specific technologies, protocols, and frameworks discussed in the course.

**1.** The Heimdall ID platform experiences a total OpenLDAP outage during final exam week. Authentication requests for 47,000 students are failing. Design an emergency authentication architecture that allows students to authenticate during the outage, including: (a) the fallback mechanism, (b) the data synchronization strategy for restoring the primary directory after the outage, and (c) the security controls that must remain in place during the fallback period.

**2.** Compare and contrast RBAC, ABAC, and ReBAC as authorization models. For each model, provide: (a) a concrete example of an access control decision that the model handles well, (b) a concrete example of an access control decision that the model handles poorly, and (c) the computational complexity of policy evaluation for each model. Under what circumstances would you recommend each model?

**3.** Design a joiner-mover-leaver provisioning architecture for a multinational corporation with 150,000 employees across 30 countries, subject to GDPR (EU), CCPA (California), and PDPA (Singapore). Your design must address: (a) attribute synchronization across 200 applications in 30 jurisdictions, (b) data residency requirements (EU personal data must remain in EU data centers), (c) the leaver workflow for employees in different jurisdictions with different legal retention requirements.

**4.** A zero-trust architecture requires that every request be authenticated, authorized, and encrypted. This adds latency and complexity to every interaction. Analyze the performance impact of zero-trust on the following workload: a microservices application with 20 services, where each user request triggers an average of 7 service-to-service calls. Calculate the total authentication overhead per user request, and propose optimizations that reduce this overhead without compromising zero-trust principles.

**5.** Post-quantum cryptography migration requires replacing RSA and ECC with ML-KEM and ML-DSA across the entire infrastructure. Create a phased migration plan for a university with 47,000 students, 5,000 staff, 2,000 servers, 500 IoT devices, and 800 AI agents. For each phase, specify: (a) the scope (which systems are migrated), (b) the duration, (c) the risk rollback strategy, and (d) the testing approach. Your plan must ensure zero service disruption during migration.

**6.** Evaluate the claim that "decentralized identity (DIDs and VCs) will make centralized identity providers (IdPs) obsolete by 2050." Provide arguments for and against this claim, considering: (a) the technical feasibility of large-scale DID/VC deployment, (b) the user experience implications of self-managed keys, (c) the regulatory landscape (EUDI, NIST, GDPR), and (d) the economic incentives of current IdP providers (Okta, Microsoft, Google).

**7.** An attacker compromises a service account with admin-level access to the Bifrǫst Mesh. The account was created in 2036 by a departed employee and was never reviewed in quarterly access certifications. Design a comprehensive remediation plan that addresses: (a) immediate containment (how to detect and stop the attacker), (b) root cause analysis (why the account existed and why it wasn't reviewed), (c) systemic improvements (how to prevent this from happening again), and (d) compliance reporting (what to report to regulators and stakeholders).

**8.** AI agent identity introduces novel challenges: autonomous action, delegated authority, and variable scope. Propose an identity governance framework for AI agents that addresses: (a) agent identity issuance and lifecycle, (b) delegation of authority from humans to agents, (c) scope limitation and rate limiting, (d) audit and accountability, and (e) emergency revocation. Your framework should be general enough to apply to any organization deploying AI agents at scale.

---

*Heimdallr guards the bridge. So too must we guard the identities that cross our systems. Every authentication is a challenge; every authorization is a judgment; every audit entry is a record in the Norns' ledger. Guard wisely.*

— Dr. Sigrid Heiðarsdóttir, Professor of Identity Architecture, University of Yggdrasil, 2040