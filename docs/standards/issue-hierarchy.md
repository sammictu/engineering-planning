# Issue Hierarchy Standard

**Effective Date:** January 28, 2026
**Owner:** Engineering
**Last Updated:** January 28, 2026

---

## Overview

This document defines the standard issue hierarchy for Jira. The goal is to maintain a flat, manageable structure that supports flow-based delivery without unnecessary nesting.

---

## Issue Hierarchy

```
Epic
 └── Story / Bug / Spike
```

**No subtasks.** The lowest level of work is always a Story, Bug, or Spike.

---

## Issue Types

| Type | Purpose | Sizing | Parent |
|------|---------|--------|--------|
| **Epic** | Group of related work toward a business outcome | T-Shirt (XS, S, M, L, XL) | None |
| **Story** | Deliverable unit of work | 1, 2, or 3 points | Epic |
| **Bug** | Defect requiring fix | 1, 2, or 3 points | Epic (optional) |
| **Spike** | Time-boxed investigation | Not sized | Epic |

---

## Rules

### No Subtasks

- Subtasks are **not permitted** in our workflow
- If work feels too large, break it into multiple Stories
- Each Story should be independently deliverable and testable

### Why No Subtasks?

1. **Flow visibility** - Subtasks hide work from board views and metrics
2. **Parallel work** - Stories can be worked independently; subtasks create dependencies
3. **Estimation accuracy** - Sizing at subtask level adds noise without improving predictability
4. **Simplicity** - Fewer issue types means less cognitive overhead

### Story Size Guidelines

| Points | Guideline |
|--------|-----------|
| **1** | Single, contained change; one component; very low risk |
| **2** | Multiple related changes; some logic; touches more than one layer |
| **3** | Multiple steps/components; edge cases; cross-service integration |

If a Story feels larger than 3 points, it should be split into multiple Stories.

### Spikes

- Used for investigation or prototyping when scope is unknown
- Time-boxed (typically 1-2 days)
- Output is knowledge, not code (though POC code may result)
- Not sized with story points
- Should result in sized Stories for implementation

### Bugs

- Sized like Stories (1, 2, or 3 points)
- Can exist under an Epic or standalone
- Follow same flow as Stories through the board

---

## Examples

### Correct Structure

```
Epic: GRO-1211 - Self-Serve Updated Estimates
 ├── Story: [CP] Add estimate input form
 ├── Story: [CP] Display updated estimate confirmation
 ├── Story: [HOS] Calculate new offer based on estimate
 ├── Spike: [SPIKE] Investigate Posthog integration
 └── Bug: Fix estimate validation error
```

### Incorrect Structure (Do Not Use)

```
Epic: GRO-1211 - Self-Serve Updated Estimates
 └── Story: Implement estimate feature
      ├── Subtask: Add input form        ❌
      ├── Subtask: Add confirmation page ❌
      └── Subtask: Add backend logic     ❌
```

---

## Migration

If you encounter existing subtasks:

1. Convert subtasks to Stories under the same Epic
2. Add appropriate repo tag to title: `[CP]`, `[HOS]`, `[UW]`, etc.
3. Size the new Story (1, 2, or 3)
4. Delete the original subtask

---

## Related Documents

- [Jira Standards](https://pointdf.atlassian.net/wiki/spaces/engineering/pages/63406251/JIRA+Standard)
- [Kanban Planning](../kanban-planning.md)
- [Q1 2026 Estimate Analysis](../quarterly-plans/q1-2026-estimate-analysis.md)

---

## Questions?

Contact Engineering Leadership if you have questions about issue structure or need help breaking down work.
