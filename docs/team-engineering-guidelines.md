# Team & Engineering Guidelines

**Last Updated:** 2026-01-23
**Maintained By:** Wei Huang
**Company:** Point.com

This document provides comprehensive context about the engineering team, technical stack, practices, and organizational knowledge to support AI-assisted development, onboarding, and cross-team collaboration.

---

## Table of Contents

1. [Company & Product Overview](#company--product-overview)
2. [Engineering Organization](#engineering-organization)
3. [Technology Stack](#technology-stack)
4. [Development Workflow](#development-workflow)
5. [Tools & Services](#tools--services)
6. [Code Standards & Best Practices](#code-standards--best-practices)
7. [Testing & Quality Assurance](#testing--quality-assurance)
8. [Deployment & Infrastructure](#deployment--infrastructure)
9. [Communication & Collaboration](#communication--collaboration)
10. [Domain Knowledge](#domain-knowledge)

---

## Company & Product Overview

### About Point.com

Point.com is a financial services company providing home equity investment products. The engineering organization supports multiple products and services across the mortgage and home equity space.

### Key Business Domains

#### Primary Product Teams

- **Growth (GRO)**: Customer acquisition, conversion optimization, marketing technology, and growth initiatives
- **Engagement (CE)**: Customer engagement, user experience optimization, customer journey, and retention

#### Supporting Domains

- **Servicing (SVCG)**: Loan servicing and portfolio management
- **Underwriting (UW2)**: Underwriting 2.0 system and decisioning
- **Post-Closing (POST)**: Post-closing operations and processes
- **Decisioning (DEC)**: Automated decisioning and risk assessment
- **Financial Risk Analytics (FIN)**: Risk modeling and analytics

### Engineering Mission

Build reliable, secure, and scalable financial technology that empowers homeowners while maintaining the highest standards of compliance and data security.

---

## Engineering Organization

### Team Structure

The engineering organization is structured around product domains with cross-functional teams:

#### Core Product Teams

We have two primary product teams:

**Growth Team (GRO)**
- **Focus**: Customer acquisition, conversion optimization, marketing tech, growth initiatives
- **Key Technologies**: Ruby on Rails, React, Node.js, analytics platforms
- **Jira Project**: GRO
- **Team Members**:
  - **David Conger** - Backend development (PQ, Marketing, Partner BE, Partner API, BE spikes)
  - **Robert Cox** - Design, frontend development lead (CP, Design spikes)
  - **Richard Collins** - Full-stack frontend development (Partner FE, CP, HOS, API-Schemas, FE spikes)

**Engagement Team (CE)**
- **Focus**: Customer engagement, user experience, customer journey optimization
- **Key Technologies**: Ruby on Rails, React, customer engagement platforms
- **Jira Project**: CE
- **Team Members**:
  - **Dylan Oliver** - Frontend, team lead
  - **Robert Cox** - Design, frontend development lead (CP, Design spikes)
  - **Tomas Herrera** - Full-stack (joined Nov 2025, senior engineer)
  - **Daniel Cardenas** - Full-stack, frontend-heavy (joined Jan 2026)

**Cross-Team Staff Engineer**:
- **Pratheesh Harikumar** - Staff engineer supporting both Growth and Engagement teams (joined Nov 2025)

#### Supporting Teams & Domains

Other teams collaborate with Growth and Engagement:

**Servicing (SVCG)**
- **Focus**: Loan servicing, payments, account management
- **Jira Project**: SVCG

**Underwriting (UW2)**
- **Focus**: Underwriting automation, decisioning, risk assessment
- **Jira Project**: UW2

**Decisioning (DEC)**
- **Focus**: Automated decisioning engines, business rules
- **Jira Project**: DEC

#### Platform & Infrastructure Teams

**DevOps Team (DEVOPS)**
- **Focus**: CI/CD, infrastructure, monitoring, security
- **Key Technologies**: AWS, Terraform, Docker, Kubernetes
- **Jira Project**: DEVOPS, INF

**Data Science (DSP)**
- **Focus**: ML models, risk analytics, data pipelines
- **Key Technologies**: Python, Jupyter, Airflow, S3/Redshift
- **Jira Project**: DSP, FIN

#### Emerging Initiatives

**AI Agents (AAP)**
- **Focus**: AI-powered automation and agent systems
- **Key Technologies**: LLMs, Claude API, MCP servers
- **Jira Project**: AAP

**Voice AI (FAV, VAP)**
- **Focus**: AI voice agents and conversational interfaces
- **Key Technologies**: Voice AI platforms, NLP
- **Jira Projects**: FAV, VAP

---

## Technology Stack

### Backend

**Primary Languages & Frameworks:**
- **Ruby on Rails** - Primary backend framework for core services
  - Version: [Specify version]
  - Used for: Core business logic, API endpoints, admin interfaces
- **Node.js/TypeScript** - Modern services and APIs
  - Used for: Real-time services, new microservices, integrations

**Databases:**
- **PostgreSQL** - Primary relational database
- **Redis** - Caching and session management
- **S3** - Object storage for documents and files

**Key Backend Libraries:**
- ActiveRecord/Sequel for ORM
- Sidekiq for background jobs
- GraphQL/REST for API design

### Frontend

**Primary Framework:**
- **React** - Frontend framework (JavaScript/TypeScript)
  - State Management: [Redux/Context/Zustand - specify]
  - Build Tool: [Webpack/Vite - specify]
  - CSS Framework: [Tailwind/Material-UI/Styled Components - specify]

**Key Frontend Libraries:**
- React Router for navigation
- Axios/Fetch for API calls
- Form libraries: [Formik/React Hook Form - specify]
- Testing: Jest, React Testing Library

### Cloud Infrastructure (AWS)

**Core AWS Services:**
- **EC2/ECS/EKS** - Compute infrastructure
- **RDS** - Managed PostgreSQL databases
- **S3** - Object storage
- **CloudFront** - CDN
- **Lambda** - Serverless functions
- **API Gateway** - API management
- **CloudWatch** - Monitoring and logging
- **IAM** - Identity and access management

**Infrastructure as Code:**
- Terraform for infrastructure provisioning
- CloudFormation for AWS resource management

### Development Tools

- **Version Control**: Git, GitHub
- **CI/CD**: [GitHub Actions/CircleCI/Jenkins - specify]
- **Code Review**: GitHub Pull Requests
- **Issue Tracking**: Jira (https://pointdf.atlassian.net)
- **Documentation**: Markdown, Confluence
- **API Documentation**: [Swagger/OpenAPI - specify]

### Repository Structure

We maintain multiple repositories for different services:

| Repo Tag | Repository Name | Repo Path | Description | Tech Stack |
|----------|----------------|-----------|-------------|------------|
| **[PQ]** | Prequalification & Partner API | `/prequal` | Backend for prequalification and partner API | Ruby on Rails |
| **[CP]** | Customer Portal | `/customer-portal` | Frontend for prequal and customer dashboard | React |
| **[HOS]** | Homeowner Service | `/homeowner-service` | Backend for customer dashboard | Ruby on Rails |
| **[Marketing]** | Marketing Config | `/marketing` | Marketing-related configuration (Direct Mail, etc.) | Ruby on Rails |
| **[Partner BE]** | Partner Portal Backend | `/partner` | KBYG (Know Before You Go) partner portal backend | Ruby on Rails |
| **[Partner FE]** | Partner Portal Frontend | `/partner` | KBYG partner portal frontend | React |
| **[QA]** | QA Automation | `/qa-automation` | Quality assurance automation test suite | [Cypress/Playwright] |
| **[Design]** | UI/UX Design | N/A | Design work, usually precursor to frontend tickets | Figma/Design tools |

**Jira Ticket Naming Convention:**
- **Always begin ticket titles** with the repository tag in brackets to indicate which codebase is affected
- Examples:
  - `[PQ] Fix authentication bug in partner API`
  - `[CP][HOS] Update customer dashboard data flow`
  - `[Design] Create new onboarding flow mockups`
- Multiple tags can be used if the work spans multiple repos
- `[Design]` tickets typically lead to frontend implementation tickets

---

## Development Workflow

### Kanban-Based Continuous Flow

We use a **Kanban methodology** for continuous flow management:

**Board Columns:**
1. **Backlog** - Prioritized features ready to start
2. **Ready** - Features ready to be pulled (requirements clear, dependencies resolved)
3. **In Progress** - Active development work (WIP limits enforced)
4. **Review** - Code review and QA
5. **Done** - Completed and deployed

**Key Principles:**
- **Pull-based system**: Engineers pull work when capacity available
- **WIP limits**: Enforce limits to maintain flow and quality
- **Continuous replenishment**: Weekly backlog grooming and prioritization
- **Flow metrics**: Track throughput, cycle time, and lead time

**Replenishment Meeting:**
- **Frequency**: Weekly
- **Focus**: Review completed work, identify bottlenecks, pull new work based on priorities and capacity

### Weekly Planning Process

We create weekly work plans to organize team capacity and priorities:

**Planning Artifacts:**
- **Location**: `docs/weekly-plans/` folder
- **Template**: `gro-weekly-plan-template.md` - Reusable template for weekly planning
- **Weekly Plans**: `gro-weekly-plan-YYYY-MM-DD.md` - Date is the Monday of the week

**Weekly Plan Structure:**
- **Week Goals**: Primary epic focus (60%), critical bugs (30%), operational health (10%)
- **Individual Assignments**: Specific work items for each engineer
- **Capacity Analysis**: Load balancing across team members
- **Risk Mitigation**: Potential blockers and mitigation strategies
- **Success Metrics**: Measurable outcomes for the week

**Naming Convention:**
- Template: `gro-weekly-plan-template.md`
- Weekly plans: `gro-weekly-plan-YYYY-MM-DD.md` (e.g., `gro-weekly-plan-2026-01-27.md`)
- Date represents the Monday of the planning week

**Planning Cadence:**
- Create plan: End of previous week or Monday morning
- Daily updates: Adjust in standups as needed
- Retrospective: End of week to review completion and learnings

### Jira Ticket Standards

**Ticket Naming Convention:**

When possible, use brackets in the ticket title to indicate the repo or task type. This aids in ticket assignment and tracking:

- **[Design]** - FE UI design work (MUST INCLUDE Figma)
- **[CP]** - Customer Portal (Prequal and customer dashboard FE) (MUST INCLUDE Figma)
- **[PQ]** - Ruby on Rails Prequalification and Partner API BE
- **[HOS]** - Homeowner Service (customer dashboard BE)
- **[Marketing]** - Ruby on Rails app for marketing-related config such as Direct Mail
- **[Partner BE]** - Partner portal (aka KBYG) BE
- **[Partner FE]** - Partner portal (aka KBYG) FE
- **[QA]** - Quality Assurance Automation test repo

### Story Point Scale (Kanban)

| Size | Definition | Characteristics | Examples |
|------|-----------|-----------------|----------|
| **1 (Small)** | Fast-flow item | Single, contained change; one component or service; very low risk; minimal testing; should move quickly | Copy or UI tweak; simple bug fix; config or flag update; logging |
| **2 (Medium)** | Normal-flow item | Multiple related changes; some logic or validation; touches more than one layer; light integration testing; well understood, common pattern | Add field with validation; FE + BE change; bug needing some investigation |
| **3 (Large – Max)** | Upper limit for flow | Multiple steps or components; edge cases or error handling; cross-service integration; moderate risk; still expected to flow | New endpoint + UI wiring; non-trivial refactor; feature with multiple acceptance criteria |

### Kanban Hard Rules

| Rule | Description |
|------|-------------|
| **Max size** | Any work larger than 3 must be broken down |
| **Epics** | Epics are never sized |
| **No subtasks** | Use stories only, never subtasks |
| **Unknowns** | If scope is unclear, split or spike first |
| **Flow focus** | Size for throughput and cycle time, not commitment |

### When to Break a Ticket Down

| Signal | Action |
|--------|--------|
| Likely to exceed WIP limits | Split before pulling |
| Multiple handoffs | Split by responsibility |
| Ticket sits idle | Break into smaller flow units |
| Waiting on dependency | Separate dependency from delivery |
| Many acceptance criteria | Split by outcome |

**Example - Epic → Story Breakdown:**
- **Epic**: Voice Prequal
  - Stories: Voice input UI (2); Transcription integration (3); Error handling (2); Analytics & logging (1)

### Ready-to-Pull Checklist (Kanban)

Before pulling a ticket into In Progress, ensure:
- [ ] Acceptance criteria written
- [ ] Dependencies identified or removed
- [ ] Size is 1, 2, or 3
- [ ] Work can move without waiting

### T-Shirt Size (Epic Level)

| Size | Duration | Timeline Guidance |
|------|----------|-------------------|
| **XS** | < 2 weeks | Couple of weeks |
| **S** | 3-4 weeks | About a month |
| **M** | 5-8 weeks | 1-2 months |
| **L** | 9-12 weeks | 1 Quarter |
| **XL** | > 12 weeks | Multiple Quarters |

### Feature Development Lifecycle

1. **Feature Definition**
   - Requirements documented in Jira
   - Acceptance criteria defined
   - Dependencies identified
   - Design/technical specs created

2. **Development**
   - Create feature branch from `main`
   - Follow branch naming: `feature/JIRA-123-short-description`
   - Commit early and often with meaningful messages
   - Keep PRs focused and reviewable

3. **Code Review**
   - All code must be reviewed before merge
   - Minimum 1 approval required
   - Address review comments promptly
   - CI must pass (tests, linting, security scans)

4. **Testing**
   - Unit tests required for new code
   - Integration tests for API changes
   - Manual QA for UI changes
   - Staging environment testing

5. **Deployment**
   - Deploy to staging first
   - Smoke tests in staging
   - Deploy to production
   - Monitor metrics and logs

6. **Post-Deployment**
   - Monitor error rates and performance
   - Verify feature flags if applicable
   - Update documentation
   - Close Jira ticket

### Git Workflow

**Branch Strategy:**
- `main` - Production-ready code
- `staging` - Staging environment (if applicable)
- `feature/*` - Feature branches
- `fix/*` - Bug fix branches
- `hotfix/*` - Production hotfixes

**Commit Message Format:**
```
[JIRA-123] Brief description of change

More detailed explanation if needed.
- Bullet points for multiple changes
- Keep first line under 72 characters
```

**Pull Request Guidelines:**
- Link to Jira ticket in description
- Include testing instructions
- Add screenshots for UI changes
- Tag relevant reviewers
- Keep PRs small and focused (< 500 lines when possible)

---

## Tools & Services

### Core Development Tools

**Jira** (https://pointdf.atlassian.net)
- Issue tracking and project management
- 52 active projects across engineering org
- MCP integration enabled for AI-assisted issue management

**GitHub**
- Source code repository
- Code review via Pull Requests
- CI/CD integration
- [Specify organization name]

**Slack** (assumed)
- Team communication
- Integration with Jira, GitHub, deployment notifications
- [Specify key channels]

### Monitoring & Observability

**Application Monitoring:**
- [New Relic/Datadog/Prometheus - specify]
- APM for performance tracking
- Error tracking and alerting

**Logging:**
- CloudWatch Logs
- [ELK Stack/Splunk - specify if applicable]
- Centralized log aggregation

**Alerting:**
- PagerDuty or similar for on-call
- Slack notifications for deployments and critical alerts

### Third-Party Services

**Financial Services:**
- [Credit bureaus, loan systems - specify]
- [Payment processors - specify]

**Customer Tools:**
- Salesforce (SFO) for CRM
- [Customer support tools - specify]

**Analytics:**
- [Google Analytics, Segment, etc. - specify]
- Data warehouse: [Redshift/Snowflake - specify]

---

## Code Standards & Best Practices

### Ruby on Rails Standards

**Code Style:**
- Follow Ruby Style Guide (RuboCop)
- Use `rubocop` for linting
- 2-space indentation
- Meaningful method and variable names

**Rails Best Practices:**
- Fat models, skinny controllers
- Use service objects for complex business logic
- Background jobs for async operations (Sidekiq)
- Avoid N+1 queries (use `includes`, `joins`)
- RESTful API design

**Security:**
- Always use strong parameters
- Sanitize user input
- Use parameterized queries (avoid SQL injection)
- CSRF protection enabled
- Secure sensitive data (credentials, PII)

### TypeScript/Node.js Standards

**Code Style:**
- Use ESLint and Prettier
- TypeScript strict mode enabled
- Explicit types for function parameters and returns
- Async/await over callbacks

**Node.js Best Practices:**
- Error handling with try/catch for async operations
- Use environment variables for configuration
- Validate input with libraries like Joi or Zod
- Use middleware pattern for Express apps

### React Standards

**Component Structure:**
- Functional components with hooks (avoid class components)
- Prop types or TypeScript interfaces for props
- Keep components small and focused
- Extract custom hooks for reusable logic

**State Management:**
- Local state with `useState` for component-specific state
- [Redux/Context/Zustand - specify] for global state
- Avoid prop drilling

**Performance:**
- Use `React.memo` for expensive components
- Use `useMemo` and `useCallback` appropriately
- Code splitting with lazy loading

### General Best Practices

**Code Quality:**
- Self-documenting code over excessive comments
- DRY principle (Don't Repeat Yourself)
- SOLID principles for OOP
- Functional programming patterns where appropriate

**Security:**
- Never commit secrets or credentials
- Use environment variables for configuration
- Validate and sanitize all user input
- Follow OWASP Top 10 security guidelines
- Regular dependency updates for security patches

**Performance:**
- Optimize database queries
- Cache expensive operations
- Use CDN for static assets
- Minimize API payload sizes

---

## Testing & Quality Assurance

### Testing Strategy

**Unit Tests:**
- Required for all new business logic
- RSpec for Ruby, Jest for JavaScript/TypeScript
- Aim for > 80% code coverage on critical paths
- Test edge cases and error conditions

**Integration Tests:**
- Test API endpoints
- Test service integrations
- Database interactions

**End-to-End Tests:**
- [Cypress/Playwright - specify]
- Critical user flows automated
- Run in CI pipeline

**Manual QA:**
- QA engineer review for major features
- Exploratory testing for complex changes
- Browser compatibility testing

### Test Organization

**Rails Testing:**
```ruby
# spec/models/user_spec.rb
# spec/services/loan_calculator_spec.rb
# spec/controllers/api/v1/loans_controller_spec.rb
```

**JavaScript Testing:**
```javascript
// __tests__/components/LoanForm.test.tsx
// __tests__/utils/calculations.test.ts
```

### Quality Gates

Before merging to main:
- [ ] All tests passing
- [ ] Code coverage maintained or improved
- [ ] Linting passes
- [ ] Security scans pass
- [ ] Code reviewed and approved
- [ ] Manual QA completed (if applicable)

---

## Deployment & Infrastructure

### Deployment Pipeline

**Staging Deployment:**
1. PR merged to main
2. Automatic deployment to staging
3. Smoke tests run automatically
4. QA verification

**Production Deployment:**
1. Manual trigger or automated schedule
2. Deploy during maintenance window (if needed)
3. Blue-green or rolling deployment
4. Health checks and smoke tests
5. Monitor metrics and error rates

### Environment Configuration

**Environments:**
- **Development**: Local developer machines
- **Staging**: Pre-production environment (AWS)
- **Production**: Live production environment (AWS)

**Environment Variables:**
- Managed via [AWS Secrets Manager/Parameter Store - specify]
- Never commit `.env` files
- Use `.env.example` for documentation

### Infrastructure

**Application Servers:**
- [EC2/ECS/EKS - specify configuration]
- Auto-scaling based on load
- Health checks and monitoring

**Database:**
- PostgreSQL RDS
- Automated backups (daily)
- Read replicas for read-heavy operations
- Connection pooling

**Caching:**
- Redis for session management
- [ElastiCache - specify]
- CDN caching for static assets

### Disaster Recovery

- Database backups retained for [X days]
- Point-in-time recovery available
- Regular restore testing
- Documented runbooks for common incidents

---

## Communication & Collaboration

### Daily Workflow

**Daily Standup:**
- Focus: What's blocking flow? What can we complete today?
- Quick updates, not status reports
- Identify blockers immediately

**Asynchronous Communication:**
- Default to async communication (Slack, Jira comments)
- Document decisions in Jira or PRs
- Update ticket status regularly

### Cross-Team Coordination

**Dependencies:**
- Document dependencies in Jira (blocked by/blocks links)
- Communicate early about potential blockers
- Regular sync meetings for complex cross-team work

**Technical Discussions:**
- Use PRs for technical discussions
- Technical design docs for significant changes
- Architecture review for major initiatives

### Documentation

**Code Documentation:**
- README for each major service/repo
- API documentation (OpenAPI/Swagger)
- Complex algorithms and business logic explained in comments

**Process Documentation:**
- Runbooks for common operations
- Onboarding guides
- Architectural decision records (ADRs) for major decisions

---

## Domain Knowledge

### Financial Services Context

**Regulatory Compliance:**
- TILA (Truth in Lending Act)
- RESPA (Real Estate Settlement Procedures Act)
- FCRA (Fair Credit Reporting Act)
- State-specific lending regulations

**Data Security:**
- PII (Personally Identifiable Information) handling
- PCI compliance for payment data
- SOC 2 compliance requirements
- Data encryption at rest and in transit

### Key Business Concepts

**Loan Lifecycle:**
1. **Application**: Customer applies for home equity product
2. **Underwriting**: Risk assessment and decisioning
3. **Closing**: Final approval and fund disbursement
4. **Servicing**: Ongoing account management and payments
5. **Post-Closing**: Document management and compliance

**Risk Assessment:**
- Credit scoring and bureau pulls
- Property valuation
- Income verification
- Debt-to-income ratio calculations

### System Architecture

**Microservices:**
- Core services: [List key services]
- API gateway pattern
- Event-driven architecture for async operations
- Service mesh: [Istio/Linkerd if applicable]

**Data Flow:**
- Customer-facing applications → API Gateway → Backend Services → Database
- Third-party integrations via API adapters
- Event bus for cross-service communication

---

## Quick Reference

### Repository Quick Reference

When creating Jira tickets, **always begin the title** with the appropriate repo tag:

| Tag | Repo | Path | Tech |
|-----|------|------|------|
| **[PQ]** | Prequalification & Partner API | `/prequal` | Rails BE |
| **[CP]** | Customer Portal | `/customer-portal` | React FE |
| **[HOS]** | Homeowner Service | `/homeowner-service` | Rails BE |
| **[Marketing]** | Marketing Config | `/marketing` | Rails BE |
| **[Partner BE]** | Partner Portal Backend | `/partner` | Rails BE |
| **[Partner FE]** | Partner Portal Frontend | `/partner` | React FE |
| **[QA]** | QA Automation | `/qa-automation` | Tests |
| **[Design]** | UI/UX Design Work | N/A | Design |

**Examples:**
- `[PQ] Add new partner API endpoint`
- `[CP] Fix login form validation`
- `[Design] Create dashboard wireframes`

### Common Commands

**Rails:**
```bash
# Start Rails server
rails server

# Run migrations
rails db:migrate

# Run tests
bundle exec rspec

# Console
rails console
```

**Node.js:**
```bash
# Install dependencies
npm install

# Start dev server
npm run dev

# Run tests
npm test

# Build for production
npm run build
```

**Git:**
```bash
# Create feature branch
git checkout -b feature/JIRA-123-description

# Commit with message
git commit -m "[JIRA-123] Description"

# Push and create PR
git push -u origin feature/JIRA-123-description
```

### Key Links

- **Jira**: https://pointdf.atlassian.net
- **GitHub**: [Organization URL]
- **Staging Environment**: [URL]
- **Production Environment**: https://point.com
- **Engineering Docs**: [Confluence or internal docs URL]
- **Monitoring Dashboard**: [New Relic/Datadog URL]

### Documentation Structure

**Main Documentation:**
- `docs/team-engineering-guidelines.md` - This document (comprehensive team guide)
- `docs/kanban-planning.md` - Kanban flow management and planning framework
- `docs/product-features.md` - Product feature catalog and dependencies

**Weekly Planning:**
- `docs/weekly-plans/gro-weekly-plan-template.md` - Reusable template for weekly planning
- `docs/weekly-plans/gro-weekly-plan-YYYY-MM-DD.md` - Weekly work plans by date
  - Date format: YYYY-MM-DD (Monday of the planning week)
  - Example: `gro-weekly-plan-2026-01-27.md`

**Planning Best Practices:**
- Create weekly plan at end of previous week or Monday morning
- Use template as starting point
- Include: Epic focus (60%), bugs (30%), operational health (10%)
- Document individual assignments and capacity analysis
- Review and retrospective at end of week

### Team Members Quick Reference

**Growth Team (GRO):**
- David Conger - Backend (PQ, Marketing, Partner BE, Partner API)
- Robert Cox - Design + Frontend lead (CP, Design) *[also CE]*
- Richard Collins - Full-stack Frontend (Partner FE, CP, HOS)

**Engagement Team (CE):**
- Dylan Oliver - Frontend, team lead
- Robert Cox - Design + Frontend lead (CP, Design) *[also GRO]*
- Tomas Herrera - Full-stack (senior, joined Nov 2025)
- Daniel Cardenas - Full-stack, frontend-heavy (joined Jan 2026)

**Cross-Team Staff Engineer:**
- Pratheesh Harikumar - Staff engineer (both GRO & CE, joined Nov 2025)

### Project Quick Reference

**Primary Teams:**

| Jira Key | Team | Description |
|----------|------|-------------|
| **GRO** | **Growth** | Customer acquisition, conversion optimization, and growth initiatives |
| **CE** | **Engagement** | Customer engagement, user experience, and journey optimization |

**Supporting Domains:**

| Jira Key | Domain | Description |
|----------|--------|-------------|
| SVCG | Servicing | Loan servicing and portfolio management |
| UW2 | Underwriting | Underwriting 2.0 system |
| DEC | Decisioning | Automated decisioning engine |
| AAP | AI Agents | AI-powered automation |
| DEVOPS | DevOps | Infrastructure and CI/CD |
| SEC | Security | Security and compliance |
| POST | Post-Closing | Post-closing operations |
| FIN | Financial Analytics | Risk and financial analytics |

---

## Notes & Maintenance

**Document Updates:**
- Review and update quarterly
- Update when major architecture changes occur
- Update when team structure changes

**Contributing to This Document:**
- Submit PRs for updates
- Discuss major changes in team meetings
- Keep examples current and relevant

**AI Assistant Context:**
- This document is intended to provide context for AI-assisted development
- Reference this document when making architectural decisions
- Use Jira project keys to understand team ownership
- Follow established patterns and conventions

---

**Version:** 1.0
**Last Updated:** 2026-01-23
**Next Review:** 2026-04-23
