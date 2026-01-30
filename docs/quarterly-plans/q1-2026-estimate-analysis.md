# Q1 2026 Estimate Analysis

**Analysis Date:** January 30, 2026 (Last refresh: 9:45 AM)
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

## Jiras Missing Estimates (by Assignee)

### Richard Collins (5 issues)

| Issue | Title | Status | Size |
|-------|-------|--------|------|
| [GRO-1267](https://pointdf.atlassian.net/browse/GRO-1267) | [CP] Instrument Posthog | OPEN | 2 |
| [GRO-1275](https://pointdf.atlassian.net/browse/GRO-1275) | [Release Plan] GRO-1211 | DONE | 1 |
| [GRO-1264](https://pointdf.atlassian.net/browse/GRO-1264) | [CP] Allow requesting new offer at maximum | DONE | 2 |
| [GRO-1253](https://pointdf.atlassian.net/browse/GRO-1253) | [CP] Reuse existing offers when possible | DONE | 2 |
| [GRO-1212](https://pointdf.atlassian.net/browse/GRO-1212) | [SPIKE] Investigate effort on Frontend | DONE | Spike |

### Daniel Cardenas (3 issues)

| Issue | Title | Status | Size |
|-------|-------|--------|------|
| [CE-3923](https://pointdf.atlassian.net/browse/CE-3923) | Docket duplicate logic fails with space/hyphen | PR | 2 |
| [CE-4015](https://pointdf.atlassian.net/browse/CE-4015) | [CP] Remove AuthorizedContacts feature flag | Ready for QA | 1 |
| [CE-4019](https://pointdf.atlassian.net/browse/CE-4019) | Update browser extension for additional fields | RC | 1 |

### Robert Cox (3 issues)

| Issue | Title | Status | Size |
|-------|-------|--------|------|
| [CE-3865](https://pointdf.atlassian.net/browse/CE-3865) | HO Funding date showing past date | OPEN | 2 |
| [CE-4048](https://pointdf.atlassian.net/browse/CE-4048) | [CP] Max tries should have back to login | IN PROGRESS | 1 |
| [CE-4052](https://pointdf.atlassian.net/browse/CE-4052) | Retry throttle should be on /otp response | BACKLOG | 1 |

### Unassigned (3 issues)

| Issue | Title | Status | Size |
|-------|-------|--------|------|
| [GRO-1284](https://pointdf.atlassian.net/browse/GRO-1284) | [CP] Adjust language and progress-bar speed | DONE | 1 |
| [GRO-1246](https://pointdf.atlassian.net/browse/GRO-1246) | Follow Up Work with Self Serve Estimate | BACKLOG | Epic |
| [GRO-1189](https://pointdf.atlassian.net/browse/GRO-1189) | Upgrade to React 19 | IN PROGRESS | Epic |

### Tomas Herrera (1 issue)

| Issue | Title | Status | Size |
|-------|-------|--------|------|
| [GRO-1191](https://pointdf.atlassian.net/browse/GRO-1191) | Investigate LOE (React 19) | IN PROGRESS | Spike |

### SungMin Hong (1 issue)

| Issue | Title | Status | Size |
|-------|-------|--------|------|
| [GRO-1235](https://pointdf.atlassian.net/browse/GRO-1235) | [QA] Add E2E test(s) for automatic offer creation | IN PROGRESS | 2 |

### Pratheesh Harikumar (1 issue)

| Issue | Title | Status | Size |
|-------|-------|--------|------|
| [CE-3964](https://pointdf.atlassian.net/browse/CE-3964) | [TASK] Submit A2P 10DLC registration for SMS | PR | 1 |

### Josh Hohman (1 issue)

| Issue | Title | Status | Size |
|-------|-------|--------|------|
| [CE-3926](https://pointdf.atlassian.net/browse/CE-3926) | HO Dashboard timeline messaging incorrect | BACKLOG | 1 |

---

## Summary by Category

| Category | Missing Estimates | Has Estimates | Suggested Points |
|----------|-------------------|---------------|------------------|
| GRO-1211 Substories | 7 | 13 | ~11 pts |
| GRO-1246 (needs breakdown) | 1 | 0 | Epic |
| GRO-1189 (React 19) | 2 | 0 | Spike + Epic |
| CE Bugs | 2 | 0 | ~3 pts |
| CE-3942 Substories | 6 | 28 | ~6 pts |
| **Total** | **18** | **41** | **~20 pts** |

*Note: Excludes "Closed - Won't Do" issues. Using "Estimate" field (customfield_10026).*

---

## Epic Analysis

### [GRO-1211](https://pointdf.atlassian.net/browse/GRO-1211) - Self-Serve Updated Estimates (T-Shirt: XS)

| Metric | Value |
|--------|-------|
| Total Stories | 22 |
| Completed (DONE/RC) | 13 |
| In Progress | 2 |
| Open/Backlog | 4 |
| Closed - Won't Do | 0 |

**Story Breakdown by Repo:**
- **[CP]** (Customer Portal FE): 11 stories
- **[HOS]** (Homeowner Service BE): 2 stories
- **[UW]** (Underwriting): 2 stories
- **[api-schemas]**: 1 story
- **[QA]**: 2 stories
- **[SPIKE]**: 2 stories

**Assessment:** Well broken down, heavily FE-weighted, scope reduction helped.

**Substories Missing Estimates (7 total):**

**13 substories now have estimates.** Remaining:

**Active Work:**

| Issue | Title | Status | Assignee | Suggested Size | Rationale |
|-------|-------|--------|----------|----------------|-----------|
| [GRO-1235](https://pointdf.atlassian.net/browse/GRO-1235) | [QA] Add E2E test(s) for automatic offer creation | IN PROGRESS | SungMin Hong | 2 | QA automation, multiple flows |
| [GRO-1267](https://pointdf.atlassian.net/browse/GRO-1267) | [CP] Instrument Posthog | OPEN | Richard Collins | 2 | Analytics integration |

**Done (Still Need Points):**

| Issue | Title | Status | Assignee | Suggested Size | Rationale |
|-------|-------|--------|----------|----------------|-----------|
| [GRO-1275](https://pointdf.atlassian.net/browse/GRO-1275) | [Release Plan] GRO-1211: Self-Serve Updated Estimates | DONE | Richard Collins | 1 | Release coordination |
| [GRO-1284](https://pointdf.atlassian.net/browse/GRO-1284) | [CP] Adjust language and progress-bar speed when waiting for new offer | DONE | | 1 | FE tweak, contained |
| [GRO-1264](https://pointdf.atlassian.net/browse/GRO-1264) | [CP] Allow requesting a new offer even if current offer at maximum | DONE | Richard Collins | 2 | FE logic |
| [GRO-1253](https://pointdf.atlassian.net/browse/GRO-1253) | [CP] Reuse existing offers when possible | DONE | Richard Collins | 2 | FE optimization |
| [GRO-1212](https://pointdf.atlassian.net/browse/GRO-1212) | [SPIKE] Investigate effort on Frontend | DONE | Richard Collins | Spike | Investigation |

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

**Substories Missing Estimates (1):**

| Issue | Title | Status | Assignee | Suggested Size | Rationale |
|-------|-------|--------|----------|----------------|-----------|
| [GRO-1246](https://pointdf.atlassian.net/browse/GRO-1246) | Follow Up Work with Self Serve Estimate | BACKLOG | | Epic | Needs breakdown into stories |

### [GRO-1189](https://pointdf.atlassian.net/browse/GRO-1189) - React 19 Upgrade (T-Shirt: S)

| Metric | Value |
|--------|-------|
| Total Stories | 2 |
| Status | Spike in progress |

**Assessment:** Under-scoped. Capacity plan estimates ~250 hrs FE-heavy. Spike now actively being worked.

**Substories Missing Estimates (2):**

| Issue | Title | Status | Assignee | Suggested Size | Rationale |
|-------|-------|--------|----------|----------------|-----------|
| [GRO-1191](https://pointdf.atlassian.net/browse/GRO-1191) | Investigate LOE | IN PROGRESS | Tomas Herrera | Spike | Investigation spike, no size |
| [GRO-1189](https://pointdf.atlassian.net/browse/GRO-1189) | Upgrade to React 19 | IN PROGRESS | | Epic | Needs breakdown after spike |

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
| No story points on 18 issues | Can't validate estimates against actuals | Size active (9) + backfill Done (9) |
| GRO-1246 under-scoped | 280 hrs planned but only 1 story exists | Break down before Feb |
| GRO-1189 under-scoped | 250 hrs planned but only spike exists | Spike in progress (Tomas), create stories after |

---

## Quick Reference - Points to Add

### GRO Team (GRO-1211 - Active)

| Issue | Points | Assignee |
|-------|--------|----------|
| [GRO-1235](https://pointdf.atlassian.net/browse/GRO-1235) | 2 | SungMin Hong |
| [GRO-1267](https://pointdf.atlassian.net/browse/GRO-1267) | 2 | Richard Collins |

### GRO Team (GRO-1211 - Done/Backfill)

| Issue | Points | Assignee |
|-------|--------|----------|
| [GRO-1275](https://pointdf.atlassian.net/browse/GRO-1275) | 1 | Richard Collins |
| [GRO-1284](https://pointdf.atlassian.net/browse/GRO-1284) | 1 | |
| [GRO-1264](https://pointdf.atlassian.net/browse/GRO-1264) | 2 | Richard Collins |
| [GRO-1253](https://pointdf.atlassian.net/browse/GRO-1253) | 2 | Richard Collins |
| [GRO-1212](https://pointdf.atlassian.net/browse/GRO-1212) | Spike | Richard Collins |

### CE Team (Bugs)

| Issue | Points | Assignee |
|-------|--------|----------|
| [CE-3865](https://pointdf.atlassian.net/browse/CE-3865) | 2 | Robert Cox |
| [CE-3923](https://pointdf.atlassian.net/browse/CE-3923) | 2 | Daniel Cardenas |
| [CE-3926](https://pointdf.atlassian.net/browse/CE-3926) | 1 | Josh Hohman |

### CE Team (CE-3942 Login Flexibility)

| Issue | Points | Assignee |
|-------|--------|----------|
| [CE-4048](https://pointdf.atlassian.net/browse/CE-4048) | 1 | Robert Cox |
| [CE-4052](https://pointdf.atlassian.net/browse/CE-4052) | 1 | Robert Cox |
| [CE-4015](https://pointdf.atlassian.net/browse/CE-4015) | 1 | Daniel Cardenas |
| [CE-4019](https://pointdf.atlassian.net/browse/CE-4019) | 1 | Daniel Cardenas |
| [CE-3964](https://pointdf.atlassian.net/browse/CE-3964) | 1 | Pratheesh Harikumar |

*28 other CE-3942 substories now have estimates.*

---

## Next Steps

1. [ ] Add story points to the 18 issues listed above (~20 pts total)
2. [ ] Break down [GRO-1246](https://pointdf.atlassian.net/browse/GRO-1246) into implementation stories
3. [ ] Complete [GRO-1191](https://pointdf.atlassian.net/browse/GRO-1191) spike for React 19 and create stories (Tomas in progress)
4. [x] ~~Assign CE-3923~~ - Assigned to Daniel Cardenas
5. [x] ~~Break down CE-3942 (Login Flexibility) stories~~ - 34 substories identified
6. [x] ~~Add estimates to CE-3942 substories~~ - 29 of 34 now have estimates
7. [ ] Backfill points on Done items for velocity tracking (GRO-1275, GRO-1284, GRO-1264, GRO-1253, GRO-1212)

---

**Document Created:** January 26, 2026
**Last Updated:** January 30, 2026
**Next Review:** February 3, 2026
