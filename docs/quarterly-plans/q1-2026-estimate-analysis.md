# Q1 2026 Estimate Analysis

**Analysis Date:** January 26, 2026
**Analyst:** Wei Huang
**Source:** Jira data + [Q1 2026 Capacity Plan](./q1-2026-capacity-plan.md)

---

## Overview

This document analyzes story point estimates for active Q1 2026 work across Growth (GRO) and Engagement (CE) teams, identifying gaps and recommending sizing based on [Jira Standards](https://pointdf.atlassian.net/wiki/spaces/engineering/pages/63406251/JIRA+Standard).

---

## Story Point Scale Reference

| Size | Definition | Characteristics |
|------|-----------|-----------------|
| **1 (Small)** | Fast-flow item | Single, contained change; one component; very low risk |
| **2 (Medium)** | Normal-flow item | Multiple related changes; some logic; touches more than one layer |
| **3 (Large – Max)** | Upper limit for flow | Multiple steps/components; edge cases; cross-service integration |

**Rules:** Max size is 3. Epics are never sized. Unknowns require a spike first.

---

## Jiras Missing Story Points

### High Priority (Active Work / Blocking 1/29 Deadline)

| Issue | Title | Status | Assignee | Suggested Size | Rationale |
|-------|-------|--------|----------|----------------|-----------|
| [GRO-1280](https://pointdf.atlassian.net/browse/GRO-1280) | When accepted, still displays offer as next task | OPEN | Richard Collins | 1 | Bug fix, contained to [CP], blocks release |
| [GRO-1236](https://pointdf.atlassian.net/browse/GRO-1236) | [CP] Playwright tests for automatic offer creation | IN PROGRESS | Richard Collins | 2 | Test work, multiple scenarios |
| [GRO-1225](https://pointdf.atlassian.net/browse/GRO-1225) | [HOS] Add details to initial estimate tasks | RC | Richard Collins | 2 | BE change, in release candidate |
| [GRO-1279](https://pointdf.atlassian.net/browse/GRO-1279) | [CP] Section should show when no debt items | IN PROGRESS | Robert Cox | 1 | Edge case fix, contained |

### Medium Priority (Open Work - Q1 Delivery)

| Issue | Title | Status | Assignee | Suggested Size | Rationale |
|-------|-------|--------|----------|----------------|-----------|
| [GRO-1267](https://pointdf.atlassian.net/browse/GRO-1267) | [CP] Instrument Posthog | OPEN | | 2 | Analytics integration, FE work |
| [GRO-1235](https://pointdf.atlassian.net/browse/GRO-1235) | [QA] Add E2E test(s) for automatic offer creation | OPEN | SungMin Hong | 2 | QA automation, multiple flows |
| [GRO-1226](https://pointdf.atlassian.net/browse/GRO-1226) | [UW] Show offer amounts on estimate tasks | OPEN | Christopher Nsimbe | 2 | BE + UW integration |
| [GRO-1282](https://pointdf.atlassian.net/browse/GRO-1282) | Slack msg "HO has requested new offer" still sent | BACKLOG | | 1 | Notification bug, contained |
| [GRO-1276](https://pointdf.atlassian.net/browse/GRO-1276) | Minor Text issue on Request Complete modal | BACKLOG | | 1 | Copy fix, trivial |

### CE Bugs (Week of 1/27 - Per Capacity Plan)

| Issue | Title | Status | Priority | Assignee | Suggested Size | Rationale |
|-------|-------|--------|----------|----------|----------------|-----------|
| [CE-3865](https://pointdf.atlassian.net/browse/CE-3865) | HO Funding date showing past date | OPEN | High | Robert Cox | 2-3 | Data sync issue, needs investigation |
| [CE-3923](https://pointdf.atlassian.net/browse/CE-3923) | Docket duplicate logic fails with space/hyphen | OPEN | Medium | | 2 | Logic fix, multiple edge cases |
| [CE-3925](https://pointdf.atlassian.net/browse/CE-3925) | HO name is blank in HO application | BACKLOG | Medium | | 1 | Data mapping fix, contained |
| [CE-3926](https://pointdf.atlassian.net/browse/CE-3926) | HO Dashboard timeline messaging incorrect | BACKLOG | Medium | Josh Hohman | 1-2 | Conditional logic fix |

---

## Summary by Category

| Category | Issue Count | Total Suggested Points |
|----------|-------------|------------------------|
| GRO-1211 (1/29 deadline) | 4 | ~6 pts |
| GRO-1180 (What You Get) | 1 | ~1 pt |
| GRO Other | 5 | ~8 pts |
| CE Bugs | 4 | ~7 pts |
| **Total** | **14 issues** | **~22 pts** |

---

## Epic Analysis

### [GRO-1211](https://pointdf.atlassian.net/browse/GRO-1211) - Self-Serve Updated Estimates (T-Shirt: XS)

| Metric | Value |
|--------|-------|
| Total Stories | 22 |
| Completed (DONE/RC) | 12 |
| In Progress | 2 |
| Open/Backlog | 5 |
| Closed - Won't Do | 3 |

**Story Breakdown by Repo:**
- **[CP]** (Customer Portal FE): 11 stories
- **[HOS]** (Homeowner Service BE): 2 stories
- **[UW]** (Underwriting): 2 stories
- **[api-schemas]**: 1 story
- **[QA]**: 2 stories
- **[SPIKE]**: 2 stories

**Assessment:** Well broken down, heavily FE-weighted, scope reduction helped.

### [GRO-1180](https://pointdf.atlassian.net/browse/GRO-1180) - What You Get Calculator (T-Shirt: XS)

| Metric | Value |
|--------|-------|
| Total Stories | 5 |
| Completed (DONE) | 4 |
| In Progress | 1 |

**Assessment:** Clean epic, appropriately sized, nearly complete.

### [GRO-1246](https://pointdf.atlassian.net/browse/GRO-1246) - Follow Up with Self Serve (T-Shirt: TBD)

| Metric | Value |
|--------|-------|
| Total Stories | 1 |
| Status | Not started |

**Assessment:** Under-scoped. Capacity plan estimates ~280 hrs FE-heavy. **Needs breakdown before Feb work begins.**

### [GRO-1189](https://pointdf.atlassian.net/browse/GRO-1189) - React 19 Upgrade (T-Shirt: S)

| Metric | Value |
|--------|-------|
| Total Stories | 1 |
| Status | Spike only |

**Assessment:** Under-scoped. Capacity plan estimates ~250 hrs FE-heavy. Spike in progress per standards.

---

## Capacity Plan vs Jira Reality

| Epic | Plan Estimate | Jira Stories | Status |
|------|---------------|--------------|--------|
| [GRO-1211](https://pointdf.atlassian.net/browse/GRO-1211) | ~160 hrs | 22 stories | Aligned |
| [GRO-1180](https://pointdf.atlassian.net/browse/GRO-1180) | Part of plan | 5 stories | Aligned |
| [GRO-1246](https://pointdf.atlassian.net/browse/GRO-1246) | ~280 hrs | 1 story | **Needs breakdown** |
| [GRO-1189](https://pointdf.atlassian.net/browse/GRO-1189) | ~250 hrs | 1 spike | **Needs breakdown** |

---

## Good Practices Observed

1. **Spikes before implementation** - GRO-1211, GRO-1180, GRO-1189 all have spikes
2. **Repo tags in titles** - Consistent use of [CP], [HOS], [UW], etc.
3. **Release plan ticket** - [GRO-1275](https://pointdf.atlassian.net/browse/GRO-1275) exists for GRO-1211
4. **Scope reduction documented** - 3 stories closed as "Won't Do"

---

## Gaps / Risks Identified

| Issue | Impact | Recommendation |
|-------|--------|----------------|
| No story points on active work | Can't validate estimates against actuals | Size the 14 issues listed above |
| GRO-1246 under-scoped | 280 hrs planned but only 1 story exists | Break down before Feb |
| GRO-1189 under-scoped | 250 hrs planned but only spike exists | Complete spike, create stories |
| CE bugs unassigned | 2 of 4 bugs have no owner | Assign per capacity plan |
| GRO-1269 not accessible | Can't analyze HELOC Opt-In epic | Verify permissions |

---

## Quick Reference - Points to Add

| Issue | Points | Assignee |
|-------|--------|----------|
| [GRO-1280](https://pointdf.atlassian.net/browse/GRO-1280) | 1 | Richard Collins |
| [GRO-1236](https://pointdf.atlassian.net/browse/GRO-1236) | 2 | Richard Collins |
| [GRO-1225](https://pointdf.atlassian.net/browse/GRO-1225) | 2 | Richard Collins |
| [GRO-1279](https://pointdf.atlassian.net/browse/GRO-1279) | 1 | Robert Cox |
| [GRO-1267](https://pointdf.atlassian.net/browse/GRO-1267) | 2 | |
| [GRO-1235](https://pointdf.atlassian.net/browse/GRO-1235) | 2 | SungMin Hong |
| [GRO-1226](https://pointdf.atlassian.net/browse/GRO-1226) | 2 | Christopher Nsimbe |
| [GRO-1282](https://pointdf.atlassian.net/browse/GRO-1282) | 1 | |
| [GRO-1276](https://pointdf.atlassian.net/browse/GRO-1276) | 1 | |
| [CE-3865](https://pointdf.atlassian.net/browse/CE-3865) | 2 | Robert Cox |
| [CE-3923](https://pointdf.atlassian.net/browse/CE-3923) | 2 | |
| [CE-3925](https://pointdf.atlassian.net/browse/CE-3925) | 1 | |
| [CE-3926](https://pointdf.atlassian.net/browse/CE-3926) | 1 | Josh Hohman |

---

## Next Steps

1. [ ] Add story points to the 14 issues listed above
2. [ ] Break down [GRO-1246](https://pointdf.atlassian.net/browse/GRO-1246) into implementation stories
3. [ ] Complete [GRO-1191](https://pointdf.atlassian.net/browse/GRO-1191) spike for React 19 and create stories
4. [ ] Assign CE-3923 and CE-3925 per capacity plan
5. [ ] Verify access to GRO-1269 (HELOC Opt-In)

---

**Document Created:** January 26, 2026
**Next Review:** February 3, 2026 (post 1/29 deadline)
