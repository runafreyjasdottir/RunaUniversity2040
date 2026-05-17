# IT305: Enterprise Architecture — The Great Hall Design of Digital Enterprises

**Program:** Bachelor of Information Technology, Year 3  
**Credits:** 4 ECTS  
**Prerequisites:** IT203, IT303  
**Instructor:** Prof. Sigrún Hrafnsdottir, TOGAF Certified, AWS Solutions Architect Professional  
**Office:** Heorot Hall, Room 315  
**Semester:** Fall 2041  

> *"A great hall is not merely a roof and walls — it is the relationship between them, the flow from hearth to high seat, the way light enters and smoke exits. So too, enterprise architecture is not merely servers and software — it is the relationships that make the whole function."* — Sigrún Hrafnsdottir, *Digital Longhouses: Architecture for the 2040 Enterprise*, 2038

---

## Course Description

Enterprise Architecture (EA) is the discipline of designing an organisation's technology landscape as a coherent whole, rather than as a collection of independently acquired and configured systems. This course teaches the frameworks (TOGAF, Zachman, ArchiMate), the patterns (microservices, event-driven architecture, API-led connectivity), and the governance structures that enable IT to align with business strategy. Students will model a fictional enterprise from business architecture through data, application, and technology architecture, producing EA artifacts — Architecture Vision, Business Architecture, Information Systems Architecture, Technology Architecture, and Migration Roadmap — that reflect 2040's cloud-native, AI-augmented, quantum-ready enterprise reality.

---

## Lecture 1: What Enterprise Architecture Is — and What It Is Not

### The Architect's Mandate

Enterprise Architecture sits at the intersection of business strategy and technology execution. It answers the questions: What capabilities does the organisation need? How should those capabilities be implemented in processes, data, applications, and infrastructure? How do we transition from the current state to the target state without breaking what already works? The EA is not a technology roadmap — though it includes one. It is not an infrastructure diagram — though it encompasses one. It is the structured description of the enterprise as a system, such that the relationships between its components are visible, analysable, and governable.

A common misconception in 2040 — amplified by vendor marketing — is that "cloud native" or "AI-first" or "platform engineering" makes enterprise architecture obsolete. The opposite is true. The more heterogeneous the technology landscape (and the 2040 enterprise typically spans three cloud providers, two SaaS generations, a legacy mainframe running COBOL from 1990, and an IoT fleet of 50,000 edge devices), the more critical the architecture function becomes. Without EA, the enterprise becomes a "spaghetti architecture" — point-to-point integrations, duplicated capabilities, inconsistent data models, and security policies that vary by whim rather than by design.

### Architecture Domains

TOGAF (The Open Group Architecture Framework), the dominant EA framework as of 2040 (version 11, released 2038), organises architecture into four domains:

| Domain | Question Answered | Artifacts |
|--------|-------------------|-----------|
| **Business Architecture** | What does the organisation do, and how? | Business capability map, value stream map, organisation model |
| **Data Architecture** | What information does the organisation need, and how is it structured? | Conceptual/logical/physical data models, data flow diagrams, data governance policies |
| **Application Architecture** | What software systems implement business capabilities? | Application portfolio catalogue, interface catalog, application communication diagrams |
| **Technology Architecture** | What infrastructure and platforms host the applications and data? | Platform decomposition diagram, technology standards catalog, network topology |

The 2040 extension adds a fifth domain: **Security Architecture**, elevated from a cross-cutting concern to a first-class domain in recognition that security is no longer a property that can be "added" but must be architected from the data centre to the edge device.

### Required Reading

- The Open Group, *TOGAF Standard*, Version 11 (2038), Part I: Introduction, Chapters 1-4.
- Ross, J., Weill, P. & Robertson, D. (2039), *Enterprise Architecture as Strategy*, 3rd ed., Harvard Business Review Press, Chs. 1-2.
- Hrafnsdottir, S. (2038), *Digital Longhouses: Architecture for the 2040 Enterprise*, University of Yggdrasil Press, Ch. 1, "The Longhouse Analogy."

### Discussion Questions

1. If "cloud native makes EA obsolete" is a fallacy, what specific EA functions become more critical in a multi-cloud environment?
2. How does the inclusion of Security Architecture as a first-class domain change the EA practice compared to treating it as a cross-cutting concern?
3. What does the spaghetti architecture pattern cost an enterprise in operational terms? Quantify where possible.

---

## Lecture 2: The TOGAF Architecture Development Method (ADM)

### The Iterative Cycle

The Architecture Development Method (ADM) is the core of TOGAF — an iterative process for developing an enterprise architecture. Its ten phases (Preliminary through Architecture Change Management) form a cycle that can be executed at the enterprise level, the segment level (a division or business unit), or the capability level (a specific capability increment). The 2040 practitioner understands that the ADM is a reference, not a prescription; every engagement tailors it.

The ADM phases:

```
                  [Preliminary]
                       |
              [A. Architecture Vision]
                       |
        +--------------+--------------+
        |              |              |
  [B. Business]  [C. Information]  [D. Technology]
  [Architecture] [Sys. Arch.]      [Architecture]
        |              |              |
        +--------------+--------------+
                       |
            [E. Opportunities & Solutions]
                       |
            [F. Migration Planning]
                       |
          [G. Implementation Governance]
                       |
          [H. Architecture Change Mgmt]
                       |
            (returns to A or any phase)
```

Each phase produces specific deliverables. For the Yggdrasil Health EHR migration, the Phase A deliverable would be an Architecture Vision document describing the target state, the business outcomes, the constraints, and the high-level scope of the architecture work. Phase B produces the Business Architecture — capability maps showing which capabilities the EHR migration affects (Patient Records Management, Clinical Decision Support, Billing and Claims, Regulatory Reporting). Phases C and D produce the Information Systems and Technology architectures — data models, application component models, and the cloud platform design.

### Architecture Principles

Every EA engagement is governed by Architecture Principles — general rules and guidelines that constrain how the architecture is designed and how decisions are made. Example principles for Yggdrasil Health:

1. **Primacy of Principles**: These principles apply to all architecture decisions. No exception without Architecture Board approval.
2. **Data is an Asset**: All patient data is owned by Yggdrasil Health, stewarded by the Chief Medical Officer, and governed by the Data Governance Council. Data shall be classified (Public, Internal, Confidential, Restricted) and handled accordingly.
3. **Cloud-First**: All new applications shall be deployed on cloud platforms unless a specific business, regulatory, or technical constraint requires on-premises deployment. The burden of proof is on the exception.
4. **API-First Integration**: All inter-system communication shall use well-defined, versioned, documented APIs. Point-to-point database links are prohibited.
5. **Security by Design**: Security controls shall be architected into every layer, not retrofitted. Every architecture decision shall be assessed against the NIST CSF 2.0 framework.

### Required Reading

- The Open Group, *TOGAF Standard*, V11, Part II: Architecture Development Method, all chapters.
- Greefhorst, D. & Proper, E. (2038), *Architecture Principles: The Cornerstones of Enterprise Architecture*, Springer.
- TOGAF Series Guide: *Applying the ADM Across the Architecture Landscape*, 2040.

### Discussion Questions

1. The ADM is explicitly iterative, yet many organisations execute it as a waterfall. What incentives cause this, and how can the EA team resist them?
2. Architecture Principle 3 ("Cloud-First") places the burden of proof on the exception. When would an on-premises exception be justified in a healthcare context?
3. What is the difference between an architecture principle and a technical standard? Give examples of each for Yggdrasil Health.

---

## Lecture 3: Business Architecture — Mapping What the Enterprise Does

### Business Capability Modelling

Business Architecture answers the question: what does this enterprise do, independent of how it does it? The primary artifact is the **Business Capability Map** — a structured decomposition of everything the enterprise does, organised into a hierarchy typically three levels deep. A capability is *what* the organisation does (e.g., "Manage Patient Records"), not *how* (e.g., "Epic EHR System"), *who* (e.g., "Medical Records Department"), or *where* (e.g., "Oslo Data Centre").

For Yggdrasil Health, Level 1 capabilities:

| Strategic Capabilities | Core Capabilities | Supporting Capabilities |
|------------------------|-------------------|------------------------|
| Strategy & Planning | Patient Care Delivery | Human Resources |
| Governance & Compliance | Clinical Decision Support | Finance & Accounting |
| Innovation & Research | Diagnostics & Imaging | IT Services |
| Partnership Management | Patient Engagement | Facilities Management |
| | Revenue Cycle Management | Legal & Regulatory |

Each capability maps to: the applications that realise it, the data entities it creates and consumes, the processes that orchestrate it, the roles that perform it, and the KPIs that measure its performance. **Capability-based planning** — the practice of funding and scoping projects based on the capabilities they improve rather than the technology they deploy — is the single most powerful technique for aligning IT investment with business strategy. Instead of "we are implementing Kubernetes," the conversation becomes "we are improving the Application Hosting capability from Level 2 (basic containerisation) to Level 3 (auto-scaling, self-healing, multi-region)."

### Value Stream Mapping

Where capabilities are structural (what we can do), value streams are dynamic (how we deliver value to a stakeholder). A value stream is an end-to-end sequence of activities that creates a result for a customer. Yggdrasil Health's primary value stream is "Patient Treatment": from Symptom Onset → Appointment Scheduling → Diagnosis → Treatment → Follow-up → Billing. Mapping this value stream reveals: which capabilities each stage depends on, where delays ("bottlenecks") occur, where handoffs between systems or departments introduce error or latency, and where automation could reduce cycle time. The 2040 value stream map is a living digital artifact, fed by process mining tools (Celonis, Apromore) that extract actual process flows from system logs rather than relying on stakeholder recollection.

### Required Reading

- TOGAF Series Guide: *Business Capabilities*, 2040 Edition.
- Martin, K. (2039), *Value Stream Mapping for the Digital Enterprise*, O'Reilly.
- Burlton, R. (2038), *Business Architecture: Collecting, Connecting, and Correcting the Dots*, Business Architecture Guild.

### Discussion Questions

1. What is the difference between a business capability and a business process? Why does this distinction matter for EA?
2. Map Yggdrasil Health's "Patient Treatment" value stream. Identify at least three capabilities that are cross-cutting (supporting multiple value stream stages).
3. How does capability-based planning change the annual IT budgeting process compared to project-based planning?

---

## Lecture 4: Data Architecture — The Well of Memory

### From Entities to Data Fabrics

Data Architecture defines how data is structured, stored, moved, governed, and consumed across the enterprise. The 2040 landscape has moved from monolithic data warehouses to **data meshes** — decentralised data ownership where each domain team publishes its data as a product, with standardised discoverability, quality, and access contracts. The data mesh principles (Zhamak Dehghani, 2030s) are now mainstream:

1. **Domain Ownership**: The team that creates the data owns it, models it, and publishes it.
2. **Data as a Product**: Each dataset is treated as a product with defined consumers, SLAs, and quality metrics.
3. **Self-Serve Data Platform**: A central platform team provides the infrastructure (catalog, pipeline orchestration, storage) but does not own any domain's data.
4. **Federated Computational Governance**: Governance policies (classification, retention, access control) are defined centrally but enforced computationally — automated policy engines that intercept access requests, not manual approval workflows.

For Yggdrasil Health, the data architecture must address: structured clinical data (FHIR R5 resources), unstructured clinical notes (NLP-indexed), medical imaging (DICOM, archived to tiered storage), genomic sequences (petabyte-scale, governed by GDPR special categories), IoT streams from patient wearables (time-series database), and administrative data (relational, ERP-hosted). Each category has distinct governance requirements: FHIR resources must conform to HL7 profiles; genomic data requires consent management tracking; IoT data has real-time latency requirements.

### Data Governance

Data governance ensures that data is available, usable, consistent, and secure. The 2040 governance framework (DAMA DMBOK v3, 2039) establishes:
- **Data Owners**: Senior business leaders accountable for data within their domain (the Chief Medical Officer owns all clinical data)
- **Data Stewards**: Operational roles responsible for data quality, metadata, and issue resolution
- **Data Custodians**: Technical roles responsible for data storage, backup, and access enforcement
- **Data Classification Schema**: Public, Internal, Confidential, Restricted
- **Data Retention Policies**: Clinical records retained 30 years post-last-encounter; administrative records 7 years; logs 3 years

### Required Reading

- Dehghani, Z. (2037), *Data Mesh: Delivering Data-Driven Value at Scale*, O'Reilly.
- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*, 3rd Ed. (2039), Chs. 3-5.
- HL7 International, *FHIR R5 Specification*, Healthcare Data Architecture Section.

### Discussion Questions

1. Compare a monolithic data warehouse to a data mesh. What governance challenges does a data mesh solve, and what new ones does it create?
2. Yggdrasil Health handles genomic data that could identify patients' relatives. How should this affect data governance compared to standard clinical data?
3. What is the difference between a data owner, a data steward, and a data custodian? Why is confusing these roles a common governance failure?

---

## Lecture 5: Application Architecture — The Tools of the Trade

### Application Portfolio Management

Every enterprise of scale accumulates applications like a longhouse accumulates tools — some are sharp and daily-used, some are rusted but irreplaceable, and some are mysterious objects whose original purpose no one remembers. Application Portfolio Management (APM) is the discipline of cataloguing, assessing, and rationalising the application estate. The 2040 APM process classifies each application along five dimensions:

| Dimension | Classification Options |
|-----------|----------------------|
| **Business Criticality** | Tier 0 (life-critical), Tier 1 (revenue-critical), Tier 2 (important), Tier 3 (supporting) |
| **Technical Health** | Modern (cloud-native), Current (supported), Ageing (vendor support ending), Legacy (unsupported), Obsolete (should be retired) |
| **Functional Fit** | Excellent, Adequate, Poor (workarounds required), None (not fit for purpose) |
| **Total Cost of Ownership** | Annual TCO (licence, hosting, support, integration, training) |
| **Strategic Alignment** | Strategic (aligned with target architecture), Tolerated (not strategic but necessary), Retirement Candidate |

Applications classified as "Legacy + Tier 1 + Poor Functional Fit + High TCO" represent architectural debt — they consume disproportionate resources and constrain innovation. The architect's role is to quantify this debt in business terms and champion its retirement, ideally redirecting the TCO savings into modern alternatives.

### Integration Patterns

How applications communicate defines the architecture's flexibility. The 2040 pattern language includes:

| Pattern | Description | When to Use | Anti-Pattern Alert |
|---------|-------------|-------------|-------------------|
| **API-Led Connectivity** | Three-layer API architecture: System APIs (access systems), Process APIs (orchestrate), Experience APIs (serve channels) | Bounded contexts; well-defined domains | Over-engineered for simple ETL |
| **Event-Driven Architecture** | Applications publish events; consumers subscribe. Asynchronous, decoupled. | Real-time data propagation; microservices communication | Eventual consistency challenges; debugging complexity |
| **Service Mesh** | Infrastructure layer for service-to-service communication (mTLS, retries, circuit breaking) | Kubernetes-native microservices | Overhead for small deployments |
| **Enterprise Service Bus (ESB)** | Centralised integration hub; message transformation, routing, orchestration | Legacy system integration; protocol translation | Becomes a monolith; single point of failure |
| **Extract-Transform-Load (ETL) / ELT** | Batch data movement between systems | Data warehousing; analytics | Not suitable for real-time; latency |

```yaml
# AsyncAPI specification for an event-driven integration (2040 standard)
asyncapi: '3.0.0'
info:
  title: Patient Admitted Event
  version: '1.0.0'
channels:
  yggdrasil/clinical/patient-admitted:
    publish:
      message:
        payload:
          type: object
          properties:
            patientId: {type: string, format: uuid}
            admissionTimestamp: {type: string, format: date-time}
            department: {type: string}
            attendingPhysicianId: {type: string}
            severity: {type: string, enum: [routine, urgent, critical]}
```

### Required Reading

- Newman, S. (2039), *Building Microservices: Designing Fine-Grained Systems*, 3rd ed., O'Reilly, Chs. 1-4.
- MuleSoft, *API-Led Connectivity: The Next Step in the API Journey*, 2040 Whitepaper.
- Nygard, M. (2038), *Release It! Design and Deploy Production-Ready Software*, 3rd ed., Pragmatic Bookshelf.

### Discussion Questions

1. Under what circumstances is an ESB the right integration pattern in 2040, given the dominance of API-led and event-driven patterns?
2. Yggdrasil Health's legacy EHR uses a proprietary binary protocol for integration. What integration pattern would you use to connect it to a cloud-native FHIR API gateway?
3. How does the "Strangler Fig" pattern apply to application modernisation, and what metrics indicate readiness to retire the legacy component?

---

## Lecture 6: Technology Architecture — The Ground Beneath the Longhouse

### Platform Design for the 2040 Enterprise

Technology Architecture defines the logical and physical technology infrastructure that hosts applications and data. For the 2040 enterprise, the dominant patterns are:

- **Hybrid Multi-Cloud**: Workloads distributed across AWS, Azure, GCP, and potentially on-premises or edge locations, connected by software-defined WAN (SD-WAN) or cloud interconnect (AWS Direct Connect, Azure ExpressRoute). The architecture specifies which workloads go where based on: latency requirements (edge for real-time inference), data residency (EU patient data stays in EU regions), cost (spot instances for batch processing), and provider-specific capabilities (GCP for AI/ML, Azure for Microsoft ecosystem integration).
- **Container Orchestration**: Kubernetes (K8s) has become the universal control plane, abstracting cloud provider differences. The 2040 enterprise runs K8s clusters managed by the cloud provider's service (EKS, AKS, GKE) or, for provider-agnostic requirements, a multi-cluster management layer (Rancher, Google Anthos, AWS EKS Anywhere).
- **Infrastructure as Code (IaC)**: Every infrastructure component is defined declaratively (Terraform, Pulumi, Crossplane) and stored in version control. No manual provisioning. The CI/CD pipeline runs `terraform plan` on every pull request and `terraform apply` on merge to main.
- **Serverless and FaaS**: For event-driven, variable-load workloads, serverless functions (AWS Lambda, Azure Functions, Google Cloud Functions) eliminate infrastructure management entirely. The architecture specifies which workloads are serverless-appropriate (event processing, API backends, scheduled jobs) and which require persistent infrastructure (databases, ML training clusters, legacy application servers).

### Technology Standards and Roadmaps

The EA function maintains a **Technology Standards Catalog** — the approved list of technologies for each architectural building block. For Yggdrasil Health:

| Building Block | Standard | Exception Process |
|----------------|----------|-------------------|
| Compute | Kubernetes (EKS/AKS) | Legacy Windows VMs require exception waiver |
| Database (Relational) | PostgreSQL (RDS / Cloud SQL) | EHR vendor's Oracle requirement → waiver |
| Database (NoSQL) | DynamoDB / Cosmos DB | Redis for caching (standard) |
| Message Broker | Apache Kafka (Confluent Cloud) | RabbitMQ for legacy integration |
| Observability | Prometheus + Grafana + OpenTelemetry | Datadog (existing investment) |
| CI/CD | GitHub Actions / ArgoCD | Jenkins (legacy pipelines) |

Each standard includes a **Technology Lifecycle Status**: Emerging (evaluate), Current (deploy), Containment (no new deployments), Retirement (migrate off, target date). PostgreSQL is Current; Oracle is Containment with a retirement target of Q4 2043.

### Required Reading

- TOGAF Series Guide: *Technology Architecture*, 2040 Edition.
- Beyer, B., Jones, C. et al. (2038), *Site Reliability Engineering: How Google Runs Production Systems*, 3rd ed., O'Reilly, Chs. 2-3.
- Morris, K. (2039), *Infrastructure as Code: Dynamic Systems for the Cloud Age*, 3rd ed., O'Reilly.

### Discussion Questions

1. A development team wants to use MongoDB for a new application, but PostgreSQL is the standard. How does the EA governance process evaluate this exception request?
2. What are the architectural implications of running Kubernetes across three cloud providers vs. standardising on one?
3. How does the Technology Lifecycle Status mechanism prevent technology sprawl, and what are its limitations?

---

## Lecture 7: Microservices, SOA, and the Modularity Spectrum

### Beyond the Buzzwords

"Microservices" has been the dominant architectural paradigm since the 2010s, but by 2040 the term has accumulated so much baggage that it is more useful to think in terms of **modularity on a spectrum**. At one end: the monolith (single deployable, single codebase, single database). At the other: nanoservices (single-function deployables, extreme distribution). Between them lie modular monolith, Service-Oriented Architecture (SOA), microservices, and miniservices. Each point on the spectrum has a distinct cost profile:

| Architecture | Deployment Units | Typical Team Size | Coordination Cost | Infrastructure Cost |
|-------------|-----------------|-------------------|-------------------|-------------------|
| Monolith | 1 | 5-50 | Low | Low |
| Modular Monolith | 1 (logical separation) | 5-30 | Low-Medium | Low |
| SOA | 5-20 services | 20-100 | Medium-High | Medium |
| Microservices | 20-200+ services | 50-500+ | High | High |
| Nanoservices | 200-1000+ functions | 100-1000+ | Very High | Very High |

The 2040 architect selects the right point on this spectrum for each bounded context, not the right point for the entire enterprise. The EHR integration context may warrant microservices (independent deployability of FHIR APIs, patient portal, and AI diagnostic service). The billing context may be better served by a modular monolith (tight transactional consistency, simpler regulatory audit trail). **Architectural dogmatism** — "everything must be microservices" — has caused as many project failures as "everything is a monolith."

### Domain-Driven Design (DDD) as the Compass

Eric Evans' Domain-Driven Design (2003) provides the intellectual foundation for defining service boundaries. Bounded Contexts — explicit boundaries within which a domain model applies — map naturally to microservices. Yggdrasil Health's bounded contexts include: Patient Management, Clinical Documentation, Medication Management, Laboratory, Radiology, Billing, Scheduling, and Regulatory Reporting. Each context owns its data; cross-context communication uses events or APIs, never direct database access. The 2040 architect uses **Event Storming** workshops — collaborative modelling sessions where domain experts and technologists map business processes using sticky notes on a wall (physical or digital — Miro, MURAL, Lucid) to discover bounded contexts organically.

### Required Reading

- Evans, E. (2003/2038), *Domain-Driven Design: Tackling Complexity in the Heart of Software*, 20th Anniversary Edition, Addison-Wesley.
- Vernon, V. (2039), *Implementing Domain-Driven Design*, 3rd ed., Addison-Wesley.
- Newman, S. (2039), *Monolith to Microservices: Evolutionary Patterns to Transform Your Monolith*, O'Reilly.

### Discussion Questions

1. A team designs 40 microservices for a system with 6 developers. What architecture smell does this represent, and what should the architect do?
2. How would you use Event Storming to define bounded contexts for Yggdrasil Health? What domain experts would you invite?
3. When is a modular monolith a better choice than microservices, and how do you prevent it from degrading into a "big ball of mud"?

---

## Lecture 8: API Design and Management — The Doors of the Longhouse

### REST, GraphQL, gRPC, and AsyncAPI

APIs are the doors of the enterprise — the controlled interfaces through which capability is accessed. The 2040 API architect must select the right API paradigm for each use case:

| Paradigm | Protocol | Strengths | Weaknesses |
|----------|----------|-----------|------------|
| **REST** | HTTP/2, JSON | Universal tooling; cacheable; self-describing (HATEOAS) | Over-fetching/under-fetching; chatty for complex queries |
| **GraphQL** | HTTP/2, JSON | Client-specified queries; single endpoint; strong typing | Complex server-side; caching challenges; N+1 query risk |
| **gRPC** | HTTP/2, Protocol Buffers | High performance; bidirectional streaming; strong contracts | Limited browser support; binary debugging; less tooling |
| **AsyncAPI** | WebSocket, Kafka, MQTT | Event-driven; real-time; decoupled | Eventual consistency; schema evolution management |
| **FHIR** | REST, JSON/XML | Healthcare-specific; semantic interoperability; profiles | Domain-specific; steep learning curve |

For Yggdrasil Health: FHIR REST APIs for clinical data interoperability; GraphQL for the patient portal (flexible queries combining clinical, scheduling, and billing data); gRPC for internal microservice communication where latency matters; AsyncAPI for event propagation (patient admitted, lab result available).

### API Management and Governance

API Management platforms (Apigee, Kong, AWS API Gateway, Azure API Management) provide: authentication and authorisation (OAuth 2.1, OIDC, API keys), rate limiting and throttling, request/response transformation, analytics and monitoring, developer portal and documentation, and API versioning management. The EA API governance mandates:

- **API-First Design**: The API contract (OpenAPI 3.1+ specification) is written and reviewed before implementation begins. This ensures that the API reflects consumer needs, not implementation convenience.
- **Versioning**: URL path versioning (/v1/, /v2/) for breaking changes. Deprecation policy: old versions supported for 12 months after new version release; sunset date communicated in HTTP `Sunset` header.
- **Naming Standards**: Resources are nouns (plural: /patients, not /getPatients); actions are HTTP methods; query parameters for filtering; consistent error format (RFC 7807 Problem Details).

### Required Reading

- OpenAPI Initiative, *OpenAPI Specification 3.1+*, https://spec.openapis.org/oas/latest.html.
- GraphQL Foundation, *GraphQL Specification*, October 2040 Edition.
- Richardson, L. & Amundsen, M. (2039), *RESTful Web APIs*, 2nd ed., O'Reilly.

### Discussion Questions

1. When would you choose gRPC over REST for internal service communication? What operational challenges does gRPC introduce?
2. An API consumer is still using /v1/ nine months after deprecation was announced. What is your next step as API product owner?
3. Design the REST API resource model for Yggdrasil Health's patient records, including sub-resources, query parameters, and HATEOAS links.

---

## Lecture 9: Cloud-Native Architecture — Born in the Clouds

### The Twelve-Factor App at Age 30

The Twelve-Factor App methodology, originally published by Heroku engineers around 2011, has been updated for 2040 as the **Sixteen-Factor App**, adding four factors for the cloud-native era:

| # | Factor | Practice |
|---|--------|----------|
| 1 | Codebase | One codebase per app, tracked in version control; many deploys |
| 2 | Dependencies | Explicitly declare and isolate dependencies |
| 3 | Config | Store configuration in the environment (secrets in a vault) |
| 4 | Backing Services | Treat backing services (DB, queue, cache) as attached resources |
| 5 | Build, Release, Run | Strictly separate build and run stages |
| 6 | Processes | Execute the app as stateless processes |
| 7 | Port Binding | Export services via port binding |
| 8 | Concurrency | Scale out via the process model |
| 9 | Disposability | Fast startup; graceful shutdown |
| 10 | Dev/Prod Parity | Keep development, staging, and production as similar as possible |
| 11 | Logs | Treat logs as event streams |
| 12 | Admin Processes | Run admin/management tasks as one-off processes |
| **13** | **Observability** | Instrument with traces, metrics, and logs; OpenTelemetry standard |
| **14** | **Security** | Zero-trust networking; mTLS; identity-based access; secrets rotation |
| **15** | **FinOps** | Resource tagging; cost allocation; right-sizing automation |
| **16** | **Sustainability** | Carbon-aware scheduling; region selection based on grid carbon intensity |

### Kubernetes Architecture Patterns

For Kubernetes-native deployments, the 2040 architect applies:

- **Sidecar Pattern**: Auxiliary containers in the same Pod that enhance the primary container (e.g., Envoy proxy for mTLS, Fluent Bit for log forwarding, Cloud SQL Auth Proxy for database authentication)
- **Operator Pattern**: Custom controllers that encode operational knowledge (backup, scaling, upgrade) into software. Instead of a runbook, the operator acts.
- **GitOps**: The desired state of the cluster is declared in a Git repository. ArgoCD or Flux continuously reconciles the cluster to the Git state. Changes to production require a merged pull request, not `kubectl apply` from a laptop.

```yaml
# Kubernetes Deployment with sidecar (Istio proxy) and health probes
apiVersion: apps/v1
kind: Deployment
metadata:
  name: patient-api
  labels:
    app: patient-api
    cost-centre: clinical-systems
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 1
  template:
    metadata:
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "9090"
      labels:
        app: patient-api
        version: v3.2.1
    spec:
      serviceAccountName: patient-api
      containers:
      - name: patient-api
        image: yggdrasil-health/patient-api:v3.2.1
        ports:
        - containerPort: 8080
        envFrom:
        - secretRef:
            name: patient-api-secrets
        resources:
          requests: {memory: "256Mi", cpu: "500m"}
          limits: {memory: "512Mi", cpu: "1000m"}
        livenessProbe:
          httpGet: {path: /healthz, port: 8080}
          initialDelaySeconds: 30
        readinessProbe:
          httpGet: {path: /ready, port: 8080}
          initialDelaySeconds: 10
```

### Required Reading

- Wiggins, A. (2040), *The Sixteen-Factor App*, https://16factor.net.
- Burns, B., Beda, J. & Hightower, K. (2039), *Kubernetes: Up and Running*, 4th ed., O'Reilly.
- Beetz, F. (2040), *GitOps: Cloud-Native Continuous Deployment*, O'Reilly.

### Discussion Questions

1. Factor 15 (FinOps) and Factor 16 (Sustainability) are new. How do they interact — can a FinOps-optimised architecture also be sustainability-optimised?
2. How does the GitOps model change incident response? If production is broken and the fix requires editing a YAML file in Git, what is the latency from fix to deployment?
3. The Sidecar pattern adds resource overhead. How do you decide whether the operational benefit justifies the cost?

---

## Lecture 10: Security Architecture — The Walls, the Guards, the Locks

### Security as an Architectural Domain

In TOGAF v11, Security Architecture is elevated from a cross-cutting concern to a first-class domain. The 2040 security architect designs controls across five layers:

| Layer | Controls |
|-------|----------|
| **Identity** | SSO, MFA, passkeys, identity federation, privileged access management (PAM) |
| **Network** | Microsegmentation, mTLS, WAF, DDoS protection, zero-trust networking |
| **Compute** | Immutable infrastructure, host hardening, runtime protection (Falco), vulnerability scanning |
| **Data** | Encryption at rest and in transit, data classification, DLP, tokenisation, key management |
| **Application** | SAST, DAST, dependency scanning, RASP, API authentication/authorisation |

The **NIST Cybersecurity Framework (CSF) 2.0** (2038) organises these controls into six functions: **Govern** (organisational context), **Identify** (asset management, risk assessment), **Protect** (access control, awareness, data security), **Detect** (continuous monitoring, anomaly detection), **Respond** (incident response planning, communications), and **Recover** (recovery planning, improvements). The security architect maps each control to a CSF function and tier, producing evidence of coverage for auditors and the board.

### Zero Trust Architecture Implementation

Zero Trust Architecture (ZTA, NIST SP 800-207 Rev. 3) is the security architecture paradigm of 2040. Its implementation requires:

1. **Identity-Aware Proxy**: Every access request is intercepted by a proxy that authenticates the principal, verifies authorisation against policy, and evaluates device posture before allowing connection. No implicit trust based on network location.
2. **Microsegmentation**: East-west traffic between workloads is governed by identity-based policies, not IP-based firewall rules. Kubernetes NetworkPolicy + Istio AuthorizationPolicy enforce this at the application layer.
3. **Continuous Verification**: Access is not granted once and trusted forever. Behavioural analytics detect anomalies mid-session (sudden data volume spike, unusual access pattern, geolocation change) and trigger re-authentication or session termination.

### Required Reading

- NIST SP 800-207 Rev. 3 (2038), *Zero Trust Architecture*.
- NIST, *The NIST Cybersecurity Framework (CSF) 2.0*, 2038.
- SANS, *Security Architecture: Designing a Defensible Network*, 2040 Edition.

### Discussion Questions

1. Zero Trust requires continuous verification. What is the acceptable latency for a continuous verification check, and how does this constrain architecture?
2. How would you implement microsegmentation for Yggdrasil Health's Kubernetes workloads spanning both AWS EKS and Azure AKS?
3. What security controls belong in the application layer vs. the network layer? Is there a clean boundary, or is it a spectrum?

---

## Lecture 11: Architecture Governance and the Architecture Board

### Governing the Unseen

Architecture governance ensures that the enterprise's technology decisions align with the target architecture. Without governance, architecture is a consulting exercise — interesting, but not influential. With governance, architecture becomes a decision-making framework with teeth. The governance mechanism is the **Architecture Board** — a cross-functional body (CIO, Chief Architect, business unit representatives, CISO, CTO) that:

- Reviews and approves architecture deviations (exceptions to standards)
- Resolves architecture disputes between projects or domains
- Approves technology standards and their lifecycle status
- Reviews project compliance with architecture at key stage gates (concept, design, build, deploy)
- Maintains the architecture repository and ensures artifacts are current

The 2040 Architecture Board operates with **compliance reviews** that are increasingly automated. Instead of a project team presenting a PowerPoint deck, the CI/CD pipeline generates a compliance report: every deployed resource is checked against the Technology Standards Catalog (Is this EC2 instance using an approved AMI? Is this database encrypted with a KMS key managed by the enterprise HSM?). Non-compliant resources are flagged to the Architecture Board, which decides: grant an exception (with a time-bound remediation plan), or reject and block deployment.

### Architecture Debt Management

Architecture debt is the gap between the current state and the target architecture, multiplied by the cost of not closing it. It accumulates when projects take shortcuts: "We'll use this unapproved database now and migrate later" (later never comes); "We'll integrate via direct database link and refactor to APIs in Phase 2" (Phase 2 is descoped). The EA function quantifies architecture debt in financial terms — the cost of maintaining non-standard technologies, the risk premium of unsupported versions, the integration tax of point-to-point connections — and presents a debt reduction business case alongside the annual budget cycle.

### Required Reading

- TOGAF Series Guide: *Architecture Governance*, 2040 Edition.
- Weill, P. & Ross, J. (2037), *IT Governance: How Top Performers Manage IT Decision Rights for Superior Results*, 2nd ed., Harvard Business Review Press.
- Kruchten, P., Nord, R. & Ozkaya, I. (2038), "Technical Debt: From Metaphor to Theory and Practice," *IEEE Software*, 35(6).

### Discussion Questions

1. An Architecture Board that approves every exception undermines its own purpose. What metrics would indicate the Board is too permissive? Too rigid?
2. How would you calculate the financial cost of architecture debt for Yggdrasil Health's legacy Oracle database?
3. Should the Architecture Board have veto power over project go-live decisions, or is its role advisory? Justify.

---

## Lecture 12: The Migration Roadmap and the Architect's Legacy

### From Current State to Target State

The Migration Roadmap is the bridge between "where we are" and "where we need to be." It is not an implementation plan — that is the project manager's domain — but a sequenced set of architecture transitions, each delivering a defined increment of capability. The TOGAF ADM Phase F (Migration Planning) organises these transitions into:

- **Transition Architectures**: Intermediate states that deliver value while progressing toward the target. Yggdrasil Health Transition 1: migrate patient demographics and scheduling to cloud (lowest risk, highest user impact). Transition 2: migrate clinical documentation and lab integration. Transition 3: migrate AI diagnostic module. Transition 4: decommission on-premises data centre.
- **Work Packages**: Groupings of projects and activities that deliver a transition. A work package has a scope, a business owner, a cost estimate, and success criteria.
- **Dependencies**: Between transitions, between work packages, and between the architecture programme and other enterprise initiatives (e.g., the ERP modernisation programme, the network refresh project).

The roadmap is a living artifact, updated quarterly. Each update assesses: progress against the previous roadmap, changes in business strategy that warrant architecture revision, new technology opportunities or threats, and architecture debt accrued or retired.

### The Architect's Ethical Responsibility

Enterprise architects wield outsized influence over an organisation's technical destiny — and therefore over its employees, customers, and the public. The 2040 architect's ethical obligations include:

- **Sustainability**: Architecture decisions with 15-year consequences (platform choices, data models, API contracts) must account for the environmental impact of those choices.
- **Accessibility**: Systems must be designed for all users, including those with disabilities. The WCAG 3.0 standard and the European Accessibility Act (2035) make this a legal requirement; architecture makes it a design choice.
- **Vendor Neutrality**: The architect serves the enterprise, not any vendor. Architecture decisions must be defensible on technical and economic merits, not influenced by vendor relationships.
- **Transparency**: The architecture's assumptions, trade-offs, and risks must be communicated clearly to decision-makers. "The architecture will work" without qualification is professional negligence.

### The Heathen Reflection: The Longhouse That Outlasts Its Builder

The Old Norse longhouse was designed to last generations — its postholes set deep, its roof pitched against the heaviest snow, its hearth positioned for warmth and ventilation. The architect who designed it would never see its final years, but their design choices echoed through the lives of their descendants. The 2040 enterprise architect faces the same reality: the systems they design today will outlast their tenure. The cloud platform they select, the API contract they ratify, the data model they approve — these decisions persist, for better or worse, long after the architect moves on.

Thus the architect's most important deliverable is not a diagram but a **decision record** — the Architecture Decision Record (ADR) that captures: the context in which the decision was made, the options considered, the criteria applied, the chosen option, and the consequences (positive and negative). The next architect, five years hence, can read the ADR and understand why a decision was made — and whether the context has changed enough to warrant a different decision now. This is the architect's legacy: not the architecture itself, which will inevitably be replaced, but the reasoning that enables its orderly evolution.

### Required Reading

- TOGAF Standard, V11, Part II: Phase F — Migration Planning.
- Nygard, M. (2037), *Documenting Architecture Decisions*, ThoughtWorks.
- Hrafnsdottir, S. (2038), *Digital Longhouses*, Ch. 12, "The Postholes."

### Discussion Questions

1. Transition Architectures deliver incremental value. How do you prevent a Transition Architecture from becoming the permanent state because "it's good enough"?
2. What belongs in an Architecture Decision Record that does NOT belong in a design document?
3. Reflect on a technology decision you have made (or observed) that had consequences five years later. What would an ADR have captured that was lost when the decision-maker left?

---

## Final Examination Preparation

The final examination for IT305 consists of two components:

### Component A: Written Examination (60%)

Choose **four** of the following eight essay questions.

1. Produce a complete TOGAF Architecture Vision for Yggdrasil Health's transition to a cloud-native, API-first enterprise architecture. Include: business drivers, stakeholders and concerns, architecture principles (at least six), high-level target architecture across all four domains, and critical success factors.

2. Compare the data mesh and the monolithic data warehouse as data architecture paradigms. For Yggdrasil Health — with its mix of clinical, genomic, imaging, IoT, and administrative data — which paradigm is more appropriate, and what are the specific risks of your recommendation?

3. Yggdrasil Health currently runs a monolithic EHR system with 200+ point-to-point integrations. Design a migration roadmap from this monolith to a microservices-based architecture using Domain-Driven Design bounded contexts. Address: bounded context identification, data decomposition strategy, integration patterns, and migration sequencing.

4. Evaluate the claim that "Zero Trust Architecture makes the network perimeter irrelevant." Does ZTA eliminate the need for network security controls (firewalls, IDS/IPS, WAF), or does it transform them? Support your analysis with specific ZTA implementation patterns.

5. Select three API paradigms (REST, GraphQL, gRPC, AsyncAPI) and design the API architecture for Yggdrasil Health. For each paradigm, specify: which bounded context it serves, why it is appropriate, and specific architectural constraints (versioning, error handling, security).

6. A project team proposes deploying a new clinical workflow application on AWS using EC2 instances with manual provisioning, a MySQL database with root credentials in a configuration file, and no CI/CD pipeline. As the enterprise architect, write the compliance review finding, specify which architecture principles are violated, and define the conditions under which the project may proceed.

7. Design the Architecture Board governance process for Yggdrasil Health. Define: Board composition (roles, not names), decision rights, exception management process (including time-bound remediation requirements), compliance review cadence, and metrics for Board effectiveness.

8. Select a real or hypothetical enterprise technology decision with multi-decade consequences (platform selection, data model, API standard). Write an Architecture Decision Record for it, demonstrating that you understand: context documentation, option analysis with clear criteria, trade-off transparency, and consequence anticipation.

### Component B: Architecture Modelling Exercise (40%)

Students are provided with a case study of a fictional 2040 enterprise (different from Yggdrasil Health) and must produce, in a 4-hour session:

1. **Business Capability Map** (Level 1 and 2) using ArchiMate 4.0 notation
2. **Application Communication Diagram** showing all major applications and their integration patterns
3. **Technology Platform Decomposition Diagram** showing the cloud infrastructure architecture
4. **Migration Roadmap** with at least three transition architectures and work packages

Grading criteria: completeness, consistency (do the diagrams agree with each other?), adherence to TOGAF and ArchiMate standards, and justification of architectural decisions.

### Grading Rubric

| Criterion | Weight | Excellent (A) | Good (B) | Adequate (C) | Insufficient (D/F) |
|-----------|--------|---------------|----------|--------------|-------------------|
| Framework mastery | 30% | TOGAF/ArchiMate applied correctly and insightfully | Minor framework errors; generally sound | Basic understanding; formulaic application | Frameworks misunderstood or ignored |
| Analytical rigour | 30% | Deep analysis; trade-offs explicitly evaluated; non-obvious insights | Good analysis; trade-offs considered | Surface-level; trade-offs ignored | Descriptive only; no analysis |
| Practical realism | 20% | Architecture is deployable; real constraints acknowledged | Mostly realistic; some hand-waving | Implausible or ignores resource constraints | Completely unrealistic |
| Communication quality | 20% | Diagrams and prose are clear, well-structured, and professional | Minor clarity issues | Disorganised but comprehensible | Incoherent or unprofessional |

---

## Course Resources

### Primary Textbooks
- The Open Group (2038), *TOGAF Standard*, Version 11.
- Hrafnsdottir, S. (2038), *Digital Longhouses: Architecture for the 2040 Enterprise*, University of Yggdrasil Press.
- Ross, J., Weill, P. & Robertson, D. (2039), *Enterprise Architecture as Strategy*, 3rd ed., HBR Press.

### Supplemental Texts
- Dehghani, Z. (2037), *Data Mesh*, O'Reilly.
- Newman, S. (2039), *Building Microservices*, 3rd ed., O'Reilly.
- Evans, E. (2003/2038), *Domain-Driven Design*, 20th Anniversary Ed.
- NIST SP 800-207 Rev. 3, *Zero Trust Architecture*.
- Burns, B. et al. (2039), *Kubernetes: Up and Running*, 4th ed., O'Reilly.

### Tools
- **Modelling**: Archi (ArchiMate), Sparx Enterprise Architect, Lucidchart, Draw.io
- **API Design**: Swagger Editor, Postman, Stoplight Studio
- **Infrastructure**: Terraform, Pulumi, Crossplane
- **Orchestration**: Kubernetes, ArgoCD, Flux
- **Diagramming Standards**: ArchiMate 4.0, UML 3.0, C4 Model

---

*ᛟ — Óðal er at byggja.* Heritage is to build.

*Course designed and maintained by the Faculty of Information Technology, University of Yggdrasil, 2040.*
