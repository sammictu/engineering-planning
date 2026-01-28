# Q1 2026 Estimate Analysis

**Analysis Date:** January 28, 2026 (Updated)
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
| [GRO-1280](https://pointdf.atlassian.net/browse/GRO-1280) | When accepted, still displays offer as next task | RC | Richard Collins | 1 | Bug fix, contained to [CP], blocks release |
| [GRO-1236](https://pointdf.atlassian.net/browse/GRO-1236) | [CP] Playwright tests for automatic offer creation | IN PROGRESS | Richard Collins | 2 | Test work, multiple scenarios |
| [GRO-1225](https://pointdf.atlassian.net/browse/GRO-1225) | [HOS] Add details to initial estimate tasks | RC | Richard Collins | 2 | BE change, in release candidate |

### Medium Priority (Open Work - Q1 Delivery)

| Issue | Title | Status | Assignee | Suggested Size | Rationale |
|-------|-------|--------|----------|----------------|-----------|
| [GRO-1267](https://pointdf.atlassian.net/browse/GRO-1267) | [CP] Instrument Posthog | OPEN | Richard Collins | 2 | Analytics integration, FE work |
| [GRO-1235](https://pointdf.atlassian.net/browse/GRO-1235) | [QA] Add E2E test(s) for automatic offer creation | OPEN | SungMin Hong | 2 | QA automation, multiple flows |
| [GRO-1276](https://pointdf.atlassian.net/browse/GRO-1276) | Minor Text issue on Request Complete modal | BACKLOG | Richard Collins | 1 | Copy fix, trivial |

### CE Bugs (Week of 1/27 - Per Capacity Plan)

| Issue | Title | Status | Priority | Assignee | Suggested Size | Rationale |
|-------|-------|--------|----------|----------|----------------|-----------|
| [CE-3865](https://pointdf.atlassian.net/browse/CE-3865) | HO Funding date showing past date | OPEN | High | Robert Cox | 2-3 | Data sync issue, needs investigation |
| [CE-3923](https://pointdf.atlassian.net/browse/CE-3923) | Docket duplicate logic fails with space/hyphen | OPEN | Medium | Daniel Cardenas | 2 | Logic fix, multiple edge cases |
| [CE-3925](https://pointdf.atlassian.net/browse/CE-3925) | HO name is blank in HO application | BACKLOG | Medium | | 1 | Data mapping fix, contained |
| [CE-3926](https://pointdf.atlassian.net/browse/CE-3926) | HO Dashboard timeline messaging incorrect | BACKLOG | Medium | Josh Hohman | 1-2 | Conditional logic fix |

### CE Active Work (In Progress / Open)

| Issue | Title | Status | Assignee | Suggested Size | Rationale |
|-------|-------|--------|----------|----------------|-----------|
| [CE-4021](https://pointdf.atlassian.net/browse/CE-4021) | [CP] Implement throttling | Ready for QA | Robert Cox | 2 | Rate limiting, multiple endpoints |
| [CE-4015](https://pointdf.atlassian.net/browse/CE-4015) | [CP] Remove AuthorizedContacts feature flag | PR | Daniel Cardenas | 1 | Flag cleanup, contained |
| [CE-4017](https://pointdf.atlassian.net/browse/CE-4017) | [CP] Use obscured email from otp response | PR | Robert Cox | 1 | API integration, contained |
| [CE-4032](https://pointdf.atlassian.net/browse/CE-4032) | [CP] Add playwright tests for login v2 | IN PROGRESS | Robert Cox | 2 | Test work, multiple scenarios |
| [CE-4034](https://pointdf.atlassian.net/browse/CE-4034) | [CP] Adjust Post Funding pages based on API Response | Ready for QA | Robert Cox | 1 | FE update, contained |
| [CE-4035](https://pointdf.atlassian.net/browse/CE-4035) | Enum missing error in /dashboard | PR | Pratheesh Harikumar | 1 | Bug fix, contained |
| [CE-4019](https://pointdf.atlassian.net/browse/CE-4019) | Update browser extension for additional fields | RC | Daniel Cardenas | 1 | Extension update, contained |

### CE-3942 - Login Flexibility Epic

| Issue | Title | Status | Assignee | Suggested Size | Rationale |
|-------|-------|--------|----------|----------------|-----------|
| [CE-3942](https://pointdf.atlassian.net/browse/CE-3942) | Login flexibility (Epic) | IN PROGRESS | Pratheesh Harikumar | Epic | Login via SMS, alternate auth |

---

## Summary by Category

| Category | Issue Count | Total Suggested Points |
|----------|-------------|------------------------|
| GRO-1211 (1/29 deadline) | 3 | ~5 pts |
| GRO Other | 3 | ~5 pts |
| CE Bugs | 4 | ~7 pts |
| CE Active Work | 7 | ~9 pts |
| CE-3942 (Login Flexibility) | 1 | Epic |
| **Total** | **18 issues** | **~26 pts** |

---

## Epic Analysis

### [GRO-1211](https://pointdf.atlassian.net/browse/GRO-1211) - Self-Serve Updated Estimates (T-Shirt: XS)

| Metric | Value |
|--------|-------|
| Total Stories | 22 |
| Completed (DONE/RC) | 12 |
| In Progress | 2 |
| Open/Backlog | 5 |
| Closed - Won't Do | 0 |

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

### GRO Team

| Issue | Points | Assignee |
|-------|--------|----------|
| [GRO-1280](https://pointdf.atlassian.net/browse/GRO-1280) | 1 | Richard Collins |
| [GRO-1236](https://pointdf.atlassian.net/browse/GRO-1236) | 2 | Richard Collins |
| [GRO-1225](https://pointdf.atlassian.net/browse/GRO-1225) | 2 | Richard Collins |
| [GRO-1267](https://pointdf.atlassian.net/browse/GRO-1267) | 2 | Richard Collins |
| [GRO-1235](https://pointdf.atlassian.net/browse/GRO-1235) | 2 | SungMin Hong |
| [GRO-1276](https://pointdf.atlassian.net/browse/GRO-1276) | 1 | Richard Collins |

### CE Team

| Issue | Points | Assignee |
|-------|--------|----------|
| [CE-3865](https://pointdf.atlassian.net/browse/CE-3865) | 2 | Robert Cox |
| [CE-3923](https://pointdf.atlassian.net/browse/CE-3923) | 2 | Daniel Cardenas |
| [CE-3925](https://pointdf.atlassian.net/browse/CE-3925) | 1 | |
| [CE-3926](https://pointdf.atlassian.net/browse/CE-3926) | 1 | Josh Hohman |
| [CE-4021](https://pointdf.atlassian.net/browse/CE-4021) | 2 | Robert Cox |
| [CE-4015](https://pointdf.atlassian.net/browse/CE-4015) | 1 | Daniel Cardenas |
| [CE-4017](https://pointdf.atlassian.net/browse/CE-4017) | 1 | Robert Cox |
| [CE-4032](https://pointdf.atlassian.net/browse/CE-4032) | 2 | Robert Cox |
| [CE-4034](https://pointdf.atlassian.net/browse/CE-4034) | 1 | Robert Cox |
| [CE-4035](https://pointdf.atlassian.net/browse/CE-4035) | 1 | Pratheesh Harikumar |
| [CE-4019](https://pointdf.atlassian.net/browse/CE-4019) | 1 | Daniel Cardenas |

---

## Next Steps

1. [ ] Add story points to the 17 issues listed above
2. [ ] Break down [GRO-1246](https://pointdf.atlassian.net/browse/GRO-1246) into implementation stories
3. [ ] Complete [GRO-1191](https://pointdf.atlassian.net/browse/GRO-1191) spike for React 19 and create stories
4. [x] ~~Assign CE-3923~~ - Assigned to Daniel Cardenas
5. [ ] Assign CE-3925 per capacity plan
6. [ ] Verify access to GRO-1269 (HELOC Opt-In)
7. [ ] Break down [CE-3942](https://pointdf.atlassian.net/browse/CE-3942) (Login Flexibility) stories

---

**Document Created:** January 26, 2026
**Next Review:** February 3, 2026 (post 1/29 deadline)
