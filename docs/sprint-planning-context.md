# Sprint Planning Context

This document provides a quick reference guide linking engineering organization structure to product features, helping streamline sprint planning and resource allocation.

## Team-to-Feature Mapping

### [Team Name]

**Current Sprint Features:**
- [Feature Name] (FEAT-XXX) - [Status] - [Priority]
- [Feature Name] (FEAT-XXX) - [Status] - [Priority]

**Upcoming Features:**
- [Feature Name] (FEAT-XXX) - [Target Sprint/Date]
- [Feature Name] (FEAT-XXX) - [Target Sprint/Date]

**Team Capacity:**
- Available Engineers: [Number]
- Current Sprint Capacity: [Story Points/Hours]
- Utilization: [Percentage]

**Blockers & Dependencies:**
- [Blocking issue/dependency] - Blocking [Feature] - Resolved by: [Date/Team]
- [Blocking issue/dependency] - Blocking [Feature] - Resolved by: [Date/Team]

---

## Feature Dependency Visualization

### Dependency Chain Example

```
[Upstream Feature A] (Team X)
    ↓
[Feature B] (Team Y) - depends on Feature A
    ↓
[Feature C] (Team Z) - depends on Feature B
```

### Critical Path Features

| Feature | Team | Dependencies | Impact if Delayed |
|---------|------|--------------|-------------------|
| [Feature Name] | [Team] | [List of dependencies] | [Impact description] |
| | | | |

---

## Sprint Planning Checklist

### Pre-Sprint Planning

- [ ] Review current sprint status and carryover items
- [ ] Review product roadmap priorities
- [ ] Check feature dependencies and blockers
- [ ] Verify team capacity and availability
- [ ] Review cross-team dependencies
- [ ] Check for shared resource conflicts
- [ ] Review technical debt and maintenance items

### During Sprint Planning

- [ ] Align features with team capacity
- [ ] Assign features to team members
- [ ] Identify and document dependencies
- [ ] Set up cross-team communication channels
- [ ] Define acceptance criteria for each feature
- [ ] Estimate story points/effort
- [ ] Identify risks and mitigation strategies
- [ ] Plan for code reviews and QA
- [ ] Schedule check-ins and standups

### Post-Sprint Planning

- [ ] Document sprint goals and commitments
- [ ] Share sprint plan with stakeholders
- [ ] Set up tracking and monitoring
- [ ] Schedule dependency check-ins
- [ ] Create communication plan for blockers

---

## Resource Allocation Matrix

| Team | Current Sprint | Next Sprint | Capacity Utilization |
|------|----------------|-------------|----------------------|
| [Team 1] | [Features/Story Points] | [Features/Story Points] | [Percentage] |
| [Team 2] | [Features/Story Points] | [Features/Story Points] | [Percentage] |
| [Team 3] | [Features/Story Points] | [Features/Story Points] | [Percentage] |

---

## Cross-Team Coordination

### Shared Dependencies

| Dependency | Required By | Provided By | Status | Target Date |
|------------|-------------|-------------|--------|-------------|
| [Dependency Name] | [Team/Feature] | [Team] | [Status] | [Date] |
| | | | | |

### Communication Plan

| Teams | Coordination Need | Frequency | Channel |
|-------|-------------------|-----------|---------|
| [Team A] ↔ [Team B] | [Coordination type] | [Daily/Weekly] | [Channel] |
| | | | |

---

## Sprint Metrics & Tracking

### Current Sprint

**Sprint Goal:** [Goal statement]

**Key Metrics:**
- Planned Story Points: [Number]
- Committed Features: [Number]
- Team Velocity: [Story Points]
- Dependency Blockers: [Number]

**Status Dashboard:**
- On Track: [Features]
- At Risk: [Features]
- Blocked: [Features]

### Historical Velocity

| Sprint | Team | Story Points | Features Completed | Notes |
|--------|------|--------------|-------------------|-------|
| [Sprint Name] | [Team] | [Points] | [Count] | [Notes] |
| | | | | |

---

## Quick Reference Links

- [Engineering Organization](./engineering-org.md) - Team structure and members
- [Product Features](./product-features.md) - Feature catalog and details
- [Kanban Planning](./kanban-planning.md) - Kanban flow management (alternative to sprint planning)
- [Sprint Board] - [Link to sprint tracking tool]
- [Product Roadmap] - [Link to roadmap tool]

---

## Notes

- Last updated: [Date]
- Maintained by: [Name/Team]
- Review frequency: [Before each sprint]
- Sprint cadence: [Weekly/Bi-weekly]
