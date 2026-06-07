# SA108: Documentation & Change Management

## Overview

This course focuses on the critical but often overlooked aspects of systems administration: documentation and change management. In modern IT environments, especially those aiming for high availability and compliance, proper documentation and controlled change processes are essential. Students will learn how to create effective documentation, implement change management procedures, and use tools to maintain knowledge and control over system modifications.

**Course Credits**: 4  
**Term**: Year 1, Semester 2  
**Prerequisites**: SA101 (Introduction to Systems Administration)  

## Learning Objectives

By the end of this course, students will be able to:

1. Understand the importance of documentation and change management in systems administration
2. Create and maintain various types of technical documentation (runbooks, diagrams, procedures)
3. Implement a change management process (request, approval, implementation, review)
4. Use version control systems for configuration and documentation
5. Implement knowledge sharing practices and tools (wikis, blogs, etc.)
6. Automate documentation generation where possible
7. Conduct effective post-incident reviews and update documentation accordingly
8. Ensure compliance with documentation standards (ITIL, ISO, etc.)

## Week-by-Week Breakdown

### Week 1: The Importance of Documentation
- Why documentation matters: knowledge transfer, compliance, troubleshooting
- Cost of poor documentation: downtime, errors, security risks
- Types of documentation: strategic, tactical, operational
- Documentation as code philosophy
- **Lab**: Assessing documentation quality in a sample environment

### Week 2: Documentation Types and Structure
- Runbooks and playbooks for operations
- Architecture diagrams and network maps
- Configuration baselines and inventories
- Policies, procedures, and standards
- User guides and FAQs
- **Lab**: Creating a runbook for a common task (e.g., adding a user)

### Week 3: Writing Effective Documentation
- Audience analysis and tailoring content
- Clarity, conciseness, and consistency
- Use of templates and style guides
- Diagramming standards and tools (draw.io, Mermaid, PlantUML)
- Writing procedures: step-by-step, decision trees
- **Lab**: Rewriting a poorly written procedure, creating a diagram

### Week 4: Documentation Tools and Platforms
- Wikis (MediaWiki, Confluence, DokuWiki)
- Static site generators (MkDocs, Hugo, Jekyll)
- Documentation generators (Sphinx, Javadoc, Doxygen)
- Markdown and lightweight markup
- Integrated documentation in DevOps platforms (GitLab, GitHub)
- **Lab**: Setting up a internal wiki, publishing markdown documentation

### Week 5: Change Management Fundamentals
- What is change management? Goals and benefits
- Types of changes: standard, normal, emergency
- Change management models (ITIL, COBIT)
- Change advisory board (CAB) and roles
- Risk assessment and impact analysis
- **Lab**: Simulating a change request process for a minor change

### Week 6: The Change Management Process
- Request for Change (RFC) creation
- Change logging and tracking
- Change evaluation and approval
- Change scheduling and communication
- Change implementation and verification
- Change review and closure
- **Lab**: End-to-end change management for a server patch

### Week 7: Change Management Tools
- Ticketing systems (Jira Service Management, Zendesk, ServiceNow)
- Specialized change management tools
- Integrating change management with monitoring and CMDB
- Automation of change notifications and approvals
- **Lab**: Using a ticketing system to manage a change request

### Week 8: Configuration Management and CMDB
- What is a Configuration Management Database (CMDB)?
- Discovery vs manual entry
- Configuration items (CI) and relationships
- Configuration baselines and drift detection
- Integrating CMDB with change management
- **Lab**: Populating a simple CMDB, detecting configuration drift

### Week 9: Version Control for Documentation and Code
- Git basics for documentation
- Branching strategies for documentation (main, feature, release)
- Pull requests and review process for docs
- Continuous documentation: CI/CD for documentation sites
- **Lab**: Managing documentation in GitHub, using pull requests for review

### Week 10: Automation in Documentation and Change
- Generating diagrams from code (Mermaid, PlantUML, Graphviz)
- Auto-generating API documentation (Swagger/OpenAPI, Javadoc)
- Chatbots for documentation lookup
- Infrastructure as Code (IaC) as documentation
- Self-documenting systems and introspection
- **Lab**: Creating a diagram from a Terraform file, setting up Swagger UI

### Week 11: Knowledge Sharing and Culture
- Beyond documentation: communities of practice
- Blogs, tech talks, and brown bag sessions
- Mentoring and shadowing
- Measuring documentation effectiveness (usage, search success)
- Creating a documentation-positive culture
- **Lab**: Conducting a knowledge sharing session, creating a blog post

### Week 12: Compliance, Audits, and Continuous Improvement
- Documentation for audits (SOC 2, ISO 27001, HIPAA)
- Retention and disposal policies
- Documentation in incident management and postmortems
- Continuous improvement: reviewing and updating documentation
- **Lab**: Preparing documentation for a mock audit, conducting a postmortem

## Detailed Topics

### Documentation Lifecycle
- Creation, review, publication, revision, archival, retirement
- Documentation ownership and maintenance schedules
- Handling obsolete documentation
- Documentation in the software development lifecycle (SDLC)

### Change Management Models
- ITIL Change Management process
- COBIT governance for change
- DevOps and Site Reliability Engineering (SRE) approaches
- Emergency changes and the role of blameless postmortems
- Change windows and freeze periods

### Risk Assessment in Change Management
- Identifying risks: service impact, security, compliance
- Risk matrices and scoring
- Mitigation strategies: rollback plans, testing, phased rollout
- Acceptance criteria and success metrics
- Communication plans for stakeholders

### Technical Writing Best Practices
- Active voice and imperative mood for procedures
- Consistent terminology and glossary
- Use of warnings, cautions, and notes
- Accessibility considerations (screen readers, color contrast)
- Localization and internationalization

### Diagramming Standards
- UML for software and systems
- C4 model for architecture diagrams
- Network diagram symbols and conventions
- Flowcharts for processes and decision trees
- Keeping diagrams in sync with infrastructure

### Wikis and Knowledge Bases
- Structuring a wiki: namespaces, categories, tags
- Search optimization and information architecture
- User permissions and editing workflows
- Integrating wikis with authentication (LDAP, SAML)
- Keeping wiki content fresh: gardeners and reviewers

### Ticketing and Change Management Systems
- Fields in a change request: description, risk, backout plan
- Approval workflows and notifications
- Change calendars and scheduled changes
- Integration with monitoring: auto-creating changes for detected issues
- Reporting and metrics: change success rate, failed changes

### Configuration Management Database (CMDB)
- Populating the CMDB: discovery agents, manual entry, import
- Relationship mapping: dependency tracking
- CMDB health: accuracy, completeness, stale data
- Using CMDB for impact analysis and root cause analysis
- CMDB vs asset management vs inventory

### Git for Documentation
- Markdown in GitHub/GitLab with rendering
- Using GitHub Pages or GitLab Pages for publishing
- Branch protection and required reviews for documentation
- Signing commits and tagging releases
- Collaborative editing and conflict resolution

### Automation Examples
- Generating network diagrams from LLDP/CDP data
- Creating runbooks from Ansible playbooks
- Updating documentation from CI/CD pipeline variables
- Using Kubernetes annotations to generate service documentation
- ChatOps: querying documentation from Slack/Teams

### Knowledge Sharing Techniques
- Brown bag sessions and lunch & learns
- Internal tech blogs and newsletters
- Communities of practice and guilds
- Pair programming and shadowing for tacit knowledge
- Documentation debt and allocation of time for maintenance

### Compliance and Audits
- What auditors look for: change records, documentation accessibility
- Evidence of review and approval
- Retention periods for different document types
- Secure storage and access controls for sensitive documentation
- Documentation as part of internal controls

### Incident Management and Postmortems
- Timeline creation and data collection
- Blameless postmortem culture
- Action item tracking and verification
- Updating documentation and runbooks based on incident findings
- Sharing lessons learned organization-wide

## Hands-On Labs

### Lab 1: Documentation Audit
- Evaluate a set of documentation samples for clarity, completeness, and correctness
- Identify gaps and areas for improvement
- Propose a documentation improvement plan

### Lab 2: Creating a Runbook
- Choose a common sysadmin task (e.g., restarting a service, checking logs)
- Write a step-by-step runbook with prerequisites, steps, and verification
- Include diagrams where helpful
- Review and revise based on peer feedback

### Lab 3: Setting Up a Wiki
- Install and configure a wiki (e.g., DokuWiki for simplicity)
- Create spaces for different teams or topics
- Set up user authentication and permissions
- Import existing documentation into the wiki

### Lab 4: Change Request Process
- Use a ticketing system (e.g., Jira, or a simple open-source alternative) to create a change request
- Go through the approval process (simulate CAB)
- Implement the change in a lab environment
- Close the change with a review

### Lab 5: Version Control for Docs
- Create a Git repository for documentation
- Write documentation in Markdown
- Use branches for feature documentation
- Create pull requests and practice code review for docs
- Publish the documentation via GitHub Pages

### Lab 6: Automation Lab
- Use a tool like Mermaid to generate a flowchart from a text description
- Generate a network diagram from a CSV of devices and connections
- Set up a simple webhook to rebuild documentation on Git push

### Lab 7: CMDB Exercise
- Use a simple CMDB tool (or spreadsheet) to record configuration items
- Define relationships (e.g., server hosts application, application uses database)
- Run a report to show impact of a server failure
- Practice updating the CMDB after a change

### Lab 8: Knowledge Sharing Session
- Prepare a 15-minute talk on a topic covered in the course
- Deliver the session to peers (or record it)
- Collect feedback and identify improvement areas
- Write a blog post summarizing the session

### Lab 9: Mock Audit Preparation
- Given a list of audit requirements (e.g., for ISO 27001), identify the documentation needed
- Gather and organize the documentation
- Conduct a self-audit and note deficiencies
- Create a remediation plan

### Lab 10: Postmortem Simulation
- Simulate an incident (e.g., a service outage due to a failed change)
- Collect data and create a timeline
- Conduct a blameless postmortem meeting
- Identify action items and update documentation/runbooks
- Share the postmortem report

## Assessment and Grading

### Evaluation Components
- **Lab Exercises** (40%): Weekly hands-on labs focusing on documentation and change management tasks
- **Quizzes** (20%): Bi-weekly knowledge checks on concepts and terminology
- **Midterm Exam** (15%): Written and practical components (e.g., improve a document, design a change process)
- **Final Project** (15%): Create a complete documentation set and change management process for a hypothetical or real system
- **Participation and Attendance** (10%): Engagement in discussions, knowledge sharing, and lab work

### Lab Requirements
- Complete all assigned lab exercises
- Maintain a documentation and change management journal
- Submit lab reports with before/after samples, reflections, and metrics
- Demonstrate ability to create clear, useful documentation and manage changes effectively

### Exam Structure
- Multiple choice and short answer questions
- Document editing and improvement tasks
- Change management scenario analysis
- Designing a documentation structure for a given system

## Recommended Resources

### Books
- "The Phoenix Project" - Gene Kim et al. (for DevOps and change management context)
- "Site Reliability Engineering" - Google (chapters on documentation and postmortems)
- "Just Enough Documentation" - various authors (agile documentation)
- "Managing the Documentation Process" - JoAnn T. Hackos
- "ITIL Foundation" - AXELOS (for change management processes)

### Online Resources
- Write the Docs (https://writethedocs.org/) - community and guides for documentation
- ITIL Change Management overview (AXELOS website)
- Google's SRE workbook (postmortem templates)
- The Diagram Mermaid.js documentation
- GitHub Guides on documentation and wikis

### Tools and Software
- Documentation: MkDocs, Sphinx, Docusaurus, GitBook
- Diagramming: draw.io (diagrams.net), Mermaid, PlantUML, Graphviz
- Wikis: MediaWiki, Confluence (free trial), DokuWiki, TiddlyWiki
- Ticketing/Jira: Jira Service Management (free tier), Znuny, OTRS, Bugzilla (adapted)
- CMDB: iTop (open-source), Ralph, SambaCMDB
- Version Control: GitHub, GitLab, Bitbucket
- Automation: Jenkins, GitHub Actions, GitLab CI for documentation builds

## Professional Applications

### Systems Administration Relevance
- Documentation and change management skills are used daily for:
  - Onboarding new team members
  - Troubleshooting complex issues (having accurate docs saves time)
  - Planning and implementing changes with minimal risk
  - Meeting compliance requirements and passing audits
  - Preserving knowledge when team members leave
  - Enabling self-service through knowledge bases

### Career Pathways
- Technical Writer (specializing in IT/documentation)
- Change Manager or Release Manager
- Configuration Management Administrator
- Knowledge Manager
- IT Service Management (ITSM) Consultant
- DevOps Engineer (with focus on process and documentation)
- Systems Administrator (all levels benefit from these skills)

## Conclusion

SA108 emphasizes that systems administration is not just about technical skills with servers and networks, but also about managing information and processes effectively. In the complex, fast-changing environments of 2040, the ability to document clearly, manage changes safely, and share knowledge efficiently is what separates competent administrators from exceptional ones. By mastering these practices, students will ensure that their technical work is sustainable, scalable, and aligned with organizational goals.

*Remember: The most automated infrastructure still requires humans who understand it — and that understanding comes from good documentation.*