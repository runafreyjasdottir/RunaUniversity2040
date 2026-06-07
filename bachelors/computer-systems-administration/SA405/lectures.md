# SA405: Capstone - Operating a Production Fleet

## Overview

This capstone course represents the culmination of the Computer Systems Administration bachelor's program. Students will operate a production-grade multi-node fleet for 8 weeks, applying all concepts learned throughout the program to manage a realistic, complex system environment.

**Course Credits**: 8  
**Duration**: 8 weeks (practical, hands-on)  
**Prerequisites**: Completion of all SA1xx through SA3xx courses  

## Learning Objectives

By the end of this course, students will be able to:

1. Deploy and maintain a production Kubernetes cluster at scale
2. Implement zero-trust security principles using service mesh technologies
3. Design and operate comprehensive observability stacks (metrics, logs, traces)
4. Establish effective incident response and on-call procedures
5. Conduct chaos engineering experiments to validate system resilience
6. Plan and execute post-quantum cryptography migrations
7. Create and maintain operational documentation (runbooks, postmortems)
8. Synthesize knowledge from all prior courses into cohesive fleet operations

## Week-by-Week Breakdown

### Week 1: Foundation and Cluster Bootstrapping
- Review of infrastructure requirements
- Provisioning 5 worker nodes + 2 control plane nodes (HA)
- Kubernetes installation using kubeadm or kops
- Network plugin selection and installation (Cilium for network policies)
- Initial cluster validation and node labeling
- **Lab**: Deploy a 5-node Kubernetes cluster with HA control plane

### Week 2: Service Mesh and Zero-Trust Networking
- Introduction to zero-trust architecture in modern fleets
- Service mesh comparison: Istio vs Linkerd vs Consul Connect
- Installation of Istio with mutual TLS everywhere
- Traffic management: virtual services, destination rules
- Security policies: authorization policies, peer authentication
- Egress gateway configuration for external traffic control
- **Lab**: Deploy Istio, configure mTLS, deploy sample microservices with traffic splitting

### Week 3: Observability Stack Implementation
- Four signals of observability: metrics, logs, traces, profiling
- Prometheus installation and federation setup
- Node exporter, kube-state-metrics, and custom metrics
- Grafana dashboard creation for cluster and application metrics
- Loki stack for log aggregation
- Tempo for distributed tracing
- Alertmanager configuration and routing trees
- **Lab**: Deploy full observability stack, instrument sample applications, create dashboards and alerts

### Week 4: Application Deployment and Configuration Management
- GitOps workflow with ArgoCD or Flux
- Helm charts vs Kustomize for application packaging
- Secret management: external vault integration (HashiCorp Vault, Sealed Secrets)
- Configuration drift detection and reconciliation
- Resource management: requests, limits, quality of service classes
- Horizontal pod autoscaling and vertical pod autoscaling
- **Lab**: Deploy applications via ArgoCD, implement secret management, configure autoscaling

### Week 5: Security Hardening and Compliance
- Pod security policies and admission controllers
- Network policies for zero-trust east-west traffic
- Image scanning and admission control (Trivy in CI/CD)
- Runtime security: Falco for anomaly detection
- Audit logging and policy enforcement (OPA/Gatekeeper)
- Vulnerability scanning and patch management processes
- **Lab**: Implement network policies, deploy Falco, configure OPA constraints

### Week 6: Chaos Engineering and Resilience Testing
- Principles of chaos engineering
- Failure injection: network latency, pod kills, node drains
- LitmusChaos vs Chaos Mesh vs Gremlin
- Planning and executing a "Chaos Day" event
- Measuring impact on SLOs and error budgets
- Automated rollback and self-healing mechanisms
- **Lab**: Conduct chaos experiments using LitmusChaos, monitor impact on services

### Week 7: Post-Quantum Cryptography Migration
- Overview of quantum threats to current cryptography
- NIST PQC standardization process (CRYSTALS-Kyber, Dilithium)
- Hybrid cryptography approaches during transition
- Crypto-agility patterns in service mesh and ingress controllers
- Key management considerations for PQC algorithms
- Migration planning: inventory, prioritization, testing
- **Lab**: Create a PQC migration plan for a sample service, implement hybrid TLS in Istio

### Week 8: Incident Response, Runbooks, and Postmortems
- Incident command structure and roles
- Runbook creation: playbooks for common failure scenarios
- On-call rotation design and escalation policies
- Blameless postmortem methodology
- Timeline reconstruction and contributing factors analysis
- Action item tracking and improvement implementation
- Knowledge sharing and organizational learning
- **Lab**: Simulate an incident, create runbooks, conduct postmortem meeting

## Detailed Topics

### Kubernetes Cluster Operations
- Control plane HA considerations (etcd clustering, load balancing)
- Node maintenance: cordon, drain, uncordon
- Version upgrades: control plane first, then workers
- Backup and etcd snapshotting strategies
- Disaster recovery procedures for control plane loss
- Cluster autoscaling and node group management

### Service Mesh Deep Dive
- Sidecar injection models and performance implications
- Traffic mirroring for testing and observability
- Retry policies, timeouts, and circuit breaking
- Rate limiting and fault injection
- Multi-cluster mesh considerations
- Observability integration: metrics, logs, traces from mesh

### Advanced Observability
- Service-level objectives (SLIs/SLOs) definition and monitoring
- Error budget policies and burn rate alerts
- Distributed tracing context propagation
- Profiling with PySpy and eBPF tools
- Log structure and correlation IDs
- Metric labeling strategies and cardinality management
- Long-term storage solutions (Thanos, Cortex)

### Incident Management
- Incident severity classification (SEV-1 to SEV-4)
- Communication plans and stakeholder updates
- Post-incident review timing and attendees
- Action item categorization: immediate, short-term, long-term
- Metrics: MTTR, MTBF, incident frequency
- Building psychological safety in postmortem culture

### PQC Migration Strategies
- Algorithm selection criteria: Kyber for KEM, Dilithium for signatures
- Performance benchmarking of PQC vs classical
- Hybrid certificates and dual-stack approaches
- Protocol-level integration: TLS 1.3 with PQC key exchange
- Hardware acceleration considerations
- Migration timeline: assessment → pilot → phased rollout → completion

### Fleet-Wide Automation
- Self-healing operators: custom controllers for common patterns
- Remediation runbooks automation
- ChatOps integration for incident response
- Documentation generation from system state
- Predictive scaling based on historical patterns
- Cost optimization through rightsizing and spot instance usage

## Assessment and Deliverables

Students will be evaluated on:

1. **Cluster Health** (20%): Maintaining cluster availability and performance throughout the 8 weeks
2. **Observability Coverage** (15%): Completeness of monitoring, logging, and tracing for all services
3. **Security Implementation** (15%): Proper zero-trust configuration, network policies, and vulnerability management
4. **Chaos Engineering Results** (10%): Successfully planned and executed chaos experiments with measurable learning
5. **PQC Migration Plan** (15%): Comprehensive, actionable plan for migrating a service to post-quantum cryptography
6. **Runbooks and Documentation** (15%): Quality, completeness, and usability of operational runbooks
7. **Postmortem Practice** (10%): Conducting blameless postmortems for incidents and chaos experiments
8. **Participation and Collaboration** (5%): Engagement in on-call rotations and team activities

### Required Artifacts
- Cluster architecture diagram
- Observability dashboard screenshots
- Security policy configurations
- Chaos experiment hypotheses and results
- PQC migration plan document
- Runbooks for at least 5 common operational scenarios
- Postmortem reports for at least 2 incidents
- Weekly status reports and retrospectives

## Recommended Resources

### Books
- "Site Reliability Engineering" - Google
- "The Phoenix Project" - Gene Kim et al.
- "Chaos Engineering" - Casey Rosenthal & Nora Jones
- "Implementing Service Mesh" - Istio Documentation
- "Prometheus: Up & Running" - Brian Brazil & Björn Rabenstein
- "Post-Quantum Cryptography" - Daniel J. Bernstein et al.

### Tools and Technologies
- Kubernetes v1.29+
- Istio 1.20+
- Prometheus/Grafana/Loki/Tempo stack
- ArgoCD/Flux for GitOps
- HashiCorp Vault for secrets
- Trivy, Falco, OPA/Gatekeeper for security
- LitmusChaos for experiments
- OpenSSL with PQC providers or BoringSSL

### Reference Architectures
- Google's Borg and Omega papers
- Netflix's Simian Army and Chaos Monkey
- Apple's internal platform engineering practices
- CNBC case study: financial services zero-trust implementation
- NASA's PQC migration planning documentation

## Ethical and Professional Considerations

- Responsible disclosure of vulnerabilities discovered during operations
- Privacy considerations in logging and monitoring
- Environmental impact of compute resources and optimization strategies
- Inclusive on-call practices and burnout prevention
- Documentation accessibility for diverse teams
- Knowledge sharing and mentoring junior administrators

## Conclusion

SA405 provides students with the experience of being a production systems administrator in a 2040-era environment. By managing a realistic fleet with cutting-edge technologies and practices, students will develop the judgment, technical skills, and operational maturity required for senior infrastructure roles. The emphasis on learning from failure, blameless postmortems, and continuous improvement prepares graduates to be effective leaders in the site reliability and platform engineering fields.

*Remember: In 2040, the best systems administrators don't just keep the lights on — they make the entire infrastructure antifragile.*