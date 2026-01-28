# Kanban Planning

This document provides guidance for kanban-based planning and continuous flow management, linking engineering organization structure to product features through a flow-based approach.

## Kanban Board Structure

### Board Columns

| Column | Description | WIP Limit | Entry Criteria | Exit Criteria |
|--------|-------------|-----------|----------------|---------------|
| Backlog | Prioritized work awaiting refinement | No limit | Issue created with summary | Acceptance criteria defined, sized (1-3), dependencies identified |
| Ready | Work ready to be pulled | 10 per team | Acceptance criteria written, sized, no blockers | Engineer pulls into In Progress |
| In Progress | Active development work | 2 per engineer | Assigned, branch created, no blockers | Code complete, PR opened |
| PR | Code review | 3 per team | PR opened, CI passing, tests written | Approved by 1+ reviewer, comments addressed |
| Ready for QA | Awaiting QA testing | 5 per team | PR merged to staging, deploy successful | QA sign-off, no critical bugs |
| QA In Progress | Active QA testing | 3 per team | QA assigned, test cases ready | All test cases passed |
| RC | Release candidate | No limit | QA complete, ready for production | Deployed to production |
| Done | Completed and deployed | No limit | In production, smoke tests passed | N/A |

### Entry & Exit Criteria Details

#### Backlog → Ready

**Entry Criteria (to enter Ready):**
- [ ] Summary clearly describes the work
- [ ] Acceptance criteria written and testable
- [ ] Story point estimate assigned (1, 2, or 3)
- [ ] Dependencies identified and resolved (or tracked)
- [ ] Repo tag in title: [CP], [HOS], [PQ], [Design], etc.
- [ ] Figma link included (if [Design] or [CP] with UI changes)
- [ ] No external blockers

**Exit Criteria (to leave Ready):**
- [ ] Engineer available with capacity
- [ ] Engineer pulls work (not pushed)

#### Ready → In Progress

**Entry Criteria (to enter In Progress):**
- [ ] Engineer assigned
- [ ] Feature branch created from main
- [ ] No blockers preventing start

**Exit Criteria (to leave In Progress):**
- [ ] Code implementation complete
- [ ] Unit tests written and passing
- [ ] Self-review completed
- [ ] PR opened with description and Jira link

#### In Progress → PR

**Entry Criteria (to enter PR):**
- [ ] PR opened against main
- [ ] CI pipeline passing (lint, tests, build)
- [ ] PR description includes:
  - Jira ticket link
  - Summary of changes
  - Testing instructions
  - Screenshots (if UI changes)

**Exit Criteria (to leave PR):**
- [ ] At least 1 approval from reviewer
- [ ] All review comments addressed
- [ ] No unresolved conversations
- [ ] CI still passing after changes

#### PR → Ready for QA

**Entry Criteria (to enter Ready for QA):**
- [ ] PR merged to main
- [ ] Successfully deployed to staging
- [ ] No deployment errors

**Exit Criteria (to leave Ready for QA):**
- [ ] QA engineer assigned
- [ ] Test cases documented

#### Ready for QA → QA In Progress

**Entry Criteria (to enter QA In Progress):**
- [ ] QA engineer begins testing
- [ ] Staging environment stable

**Exit Criteria (to leave QA In Progress):**
- [ ] All test cases executed
- [ ] No critical or high bugs remaining
- [ ] QA sign-off obtained

#### QA In Progress → RC

**Entry Criteria (to enter RC):**
- [ ] QA complete with sign-off
- [ ] Analytics sign-off (if feature epic)
- [ ] Ready for production deployment

**Exit Criteria (to leave RC):**
- [ ] Deployed to production
- [ ] Smoke tests passed
- [ ] No rollback needed

#### RC → Done

**Entry Criteria (to enter Done):**
- [ ] In production
- [ ] Smoke tests passed
- [ ] Monitoring shows no issues

**WIP Limit Guidelines:**
- **In Progress:** Max 2 items per engineer to maintain focus
- **PR:** Max 3 per team to prevent review bottleneck
- **Ready for QA:** Max 5 per team to prevent QA bottleneck
- Adjust limits based on flow metrics and observed bottlenecks
- When at limit, focus on completing current work before pulling new

---

## Team-to-Feature Flow Mapping

### [Team Name]

**Current Work in Progress:**
- [Feature Name] (FEAT-XXX) - [Current Column] - [Priority]
- [Feature Name] (FEAT-XXX) - [Current Column] - [Priority]

**Ready to Pull:**
- [Feature Name] (FEAT-XXX) - [Priority] - [Estimated Effort]
- [Feature Name] (FEAT-XXX) - [Priority] - [Estimated Effort]

**Team Capacity:**
- Active Engineers: [Number]
- Current WIP: [Number] / [WIP Limit]
- Available Capacity: [Number]

**Blockers & Dependencies:**
- [Blocking issue/dependency] - Blocking [Feature] - Resolved by: [Date/Team]
- [Blocking issue/dependency] - Blocking [Feature] - Resolved by: [Date/Team]

---

## Continuous Planning Process

### Replenishment Meeting

**Frequency:** [Weekly/Bi-weekly]

**Agenda:**
- [ ] Review completed work since last meeting
- [ ] Review current WIP and identify bottlenecks
- [ ] Review backlog priorities
- [ ] Pull new work based on capacity and priorities
- [ ] Update WIP limits if needed
- [ ] Review and resolve blockers
- [ ] Update flow metrics

### Daily Flow Management

**Daily Standup Focus:**
- What's blocking flow?
- Are we within WIP limits?
- What can we complete today?
- What needs help to move forward?

**Flow Blockers:**
- [Blocker 1] - Affecting [Feature/Team] - Action: [Action item]
- [Blocker 2] - Affecting [Feature/Team] - Action: [Action item]

---

## Flow Metrics & Tracking

### Current Flow Metrics

**Throughput:**
- Last Week: [Number] features completed
- Last Month: [Number] features completed
- Average: [Number] features/week

**Cycle Time:**
- Average: [Number] days
- Target: [Number] days
- Breakdown by stage:
  - Backlog → Ready: [Number] days
  - Ready → In Progress: [Number] days
  - In Progress → Review: [Number] days
  - Review → Done: [Number] days

**Work in Progress:**
- Current WIP: [Number]
- WIP Limit: [Number]
- Utilization: [Percentage]

**Lead Time:**
- Average: [Number] days (from request to completion)
- Target: [Number] days

### Historical Flow Metrics

| Week/Month | Throughput | Avg Cycle Time | Avg Lead Time | WIP | Notes |
|------------|------------|----------------|---------------|-----|-------|
| [Date] | [Count] | [Days] | [Days] | [Number] | [Notes] |
| | | | | | |

---

## Feature Prioritization

### Prioritization Framework

**Priority Levels:**
- **P0 (Critical):** Must be done immediately, blocking other work
- **P1 (High):** Important for current goals, should be done soon
- **P2 (Medium):** Valuable but not urgent
- **P3 (Low):** Nice to have, can wait

### Backlog Management

**Backlog Structure:**

| Priority | Feature | Owner Team | Estimated Effort | Dependencies | Ready? |
|----------|---------|------------|------------------|--------------|--------|
| P0 | [Feature Name] (FEAT-XXX) | [Team] | [Effort] | [List] | [Yes/No] |
| P1 | [Feature Name] (FEAT-XXX) | [Team] | [Effort] | [List] | [Yes/No] |
| | | | | | |

**Ready Criteria:**
- [ ] Feature requirements are clear
- [ ] Acceptance criteria defined
- [ ] Dependencies identified and resolved
- [ ] Design/specifications complete
- [ ] No blockers

---

## WIP Limit Management

### Team WIP Limits

| Team | Backlog | Ready | In Progress | Review | Total WIP Limit |
|------|---------|-------|-------------|--------|-----------------|
| [Team 1] | [Limit] | [Limit] | [Limit] | [Limit] | [Total] |
| [Team 2] | [Limit] | [Limit] | [Limit] | [Limit] | [Total] |
| [Team 3] | [Limit] | [Limit] | [Limit] | [Limit] | [Total] |

### WIP Limit Adjustments

**When to Increase:**
- Team consistently completing work faster than expected
- No quality issues observed
- Flow is smooth with no bottlenecks

**When to Decrease:**
- Quality issues observed
- Frequent context switching
- Work piling up in certain stages
- Team feeling overwhelmed

---

## Bottleneck Identification & Resolution

### Common Bottlenecks

| Stage | Current WIP | Limit | Status | Action |
|-------|-------------|-------|--------|--------|
| Review | [Number] | [Limit] | [At Limit/Over] | [Action needed] |
| In Progress | [Number] | [Limit] | [At Limit/Over] | [Action needed] |
| | | | | |

### Bottleneck Resolution Strategies

**Review Bottleneck:**
- [ ] Increase review capacity
- [ ] Reduce batch size
- [ ] Improve review process
- [ ] Add more reviewers

**In Progress Bottleneck:**
- [ ] Reduce WIP limit
- [ ] Focus on completing current work
- [ ] Identify blockers and resolve
- [ ] Improve development process

---

## Cross-Team Coordination

### Flow Dependencies

| Feature | Blocking | Blocked By | Status | Target Resolution |
|---------|----------|------------|--------|-------------------|
| [Feature A] | [Feature B] | [Team] | [Status] | [Date] |
| | | | | |

### Shared Resources

| Resource | Used By | Current Utilization | Capacity | Bottleneck? |
|----------|---------|---------------------|----------|-------------|
| [Resource] | [Teams] | [Percentage] | [Capacity] | [Yes/No] |
| | | | | |

---

## Continuous Improvement

### Flow Retrospectives

**Frequency:** [Weekly/Bi-weekly]

**Focus Areas:**
- What's working well?
- Where are the bottlenecks?
- What's blocking flow?
- How can we improve throughput?
- Are WIP limits appropriate?

### Improvement Actions

| Action | Owner | Target Date | Status |
|--------|-------|-------------|--------|
| [Improvement action] | [Name/Team] | [Date] | [Status] |
| | | | |

---

## Planning Checklist

### Weekly Replenishment

- [ ] Review completed work and celebrate wins
- [ ] Analyze flow metrics (throughput, cycle time, lead time)
- [ ] Identify and resolve bottlenecks
- [ ] Review backlog priorities
- [ ] Pull new work based on capacity
- [ ] Update WIP limits if needed
- [ ] Document blockers and dependencies
- [ ] Plan cross-team coordination if needed

### Daily Flow Management

- [ ] Check WIP limits are respected
- [ ] Identify blockers and take action
- [ ] Move work forward through stages
- [ ] Update board status
- [ ] Communicate flow issues

### Monthly Review

- [ ] Review flow metrics trends
- [ ] Assess WIP limit effectiveness
- [ ] Review and update board structure
- [ ] Plan process improvements
- [ ] Review team capacity and allocation

---

## Quick Reference Links

- [Engineering Organization](./engineering-org.md) - Team structure and members
- [Product Features](./product-features.md) - Feature catalog and details
- [Sprint Planning Context](./sprint-planning-context.md) - Sprint-based planning (if using hybrid approach)
- [Kanban Board] - [Link to kanban board tool]

---

## Notes

- Last updated: January 28, 2026
- Maintained by: Wei Huang
- Review frequency: Weekly
- Replenishment cadence: Weekly (Monday)
