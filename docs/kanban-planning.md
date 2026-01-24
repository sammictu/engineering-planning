# Kanban Planning

This document provides guidance for kanban-based planning and continuous flow management, linking engineering organization structure to product features through a flow-based approach.

## Kanban Board Structure

### Board Columns

| Column | Description | WIP Limit | Entry Criteria | Exit Criteria |
|--------|-------------|-----------|----------------|---------------|
| Backlog | Prioritized features ready to start | [Limit] | [Criteria] | [Criteria] |
| Ready | Features ready to be pulled | [Limit] | [Criteria] | [Criteria] |
| In Progress | Active development work | [Limit] | [Criteria] | [Criteria] |
| Review | Code review and QA | [Limit] | [Criteria] | [Criteria] |
| Done | Completed and deployed | [Limit] | [Criteria] | [Criteria] |

**WIP Limit Guidelines:**
- Set WIP limits based on team capacity
- Adjust limits based on flow metrics and bottlenecks
- Enforce limits to maintain flow and quality

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

- Last updated: [Date]
- Maintained by: [Name/Team]
- Review frequency: [Weekly]
- Replenishment cadence: [Weekly/Bi-weekly]
