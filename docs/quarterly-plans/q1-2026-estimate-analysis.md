# Q1 2026 Estimate Analysis

**Analysis Date:** January 28, 2026 (Last refresh: 2:30 PM)
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
| [CE-3865](https://pointdf.atlassian.net/browse/CE-3865) | HO Funding date showing past date | OPEN | High | Robert Cox | 2 | Data sync issue, needs investigation |
| [CE-3923](https://pointdf.atlassian.net/browse/CE-3923) | Docket duplicate logic fails with space/hyphen | OPEN | Medium | Daniel Cardenas | 2 | Logic fix, multiple edge cases |
| [CE-3926](https://pointdf.atlassian.net/browse/CE-3926) | HO Dashboard timeline messaging incorrect | BACKLOG | Medium | Josh Hohman | 1 | Conditional logic fix |

### CE Active Work (In Progress / Open)

| Issue | Title | Status | Assignee | Suggested Size | Rationale |
|-------|-------|--------|----------|----------------|-----------|
| [CE-4021](https://pointdf.atlassian.net/browse/CE-4021) | [CP] Implement throttling | Ready for QA | Robert Cox | 2 | Rate limiting, multiple endpoints |
| [CE-4015](https://pointdf.atlassian.net/browse/CE-4015) | [CP] Remove AuthorizedContacts feature flag | PR | Daniel Cardenas | 1 | Flag cleanup, contained |
| [CE-4017](https://pointdf.atlassian.net/browse/CE-4017) | [CP] Use obscured email from otp response | PR | Robert Cox | 1 | API integration, contained |
| [CE-4032](https://pointdf.atlassian.net/browse/CE-4032) | [CP] Add playwright tests for login v2 | PR | Robert Cox | 2 | Test work, multiple scenarios |
| [CE-4034](https://pointdf.atlassian.net/browse/CE-4034) | [CP] Adjust Post Funding pages based on API Response | Ready for QA | Robert Cox | 1 | FE update, contained |
| [CE-4035](https://pointdf.atlassian.net/browse/CE-4035) | Enum missing error in /dashboard | PR | Pratheesh Harikumar | 1 | Bug fix, contained |
| [CE-4019](https://pointdf.atlassian.net/browse/CE-4019) | Update browser extension for additional fields | RC | Daniel Cardenas | 1 | Extension update, contained |

### CE-3942 - Login Flexibility Epic (31 substories without estimates)

**Active Work:**

| Issue | Title | Status | Assignee | Suggested Size | Rationale |
|-------|-------|--------|----------|----------------|-----------|
| [CE-4016](https://pointdf.atlassian.net/browse/CE-4016) | [CP] Add posthog tracking | IN PROGRESS | Robert Cox | 2 | Analytics integration |
| [CE-4044](https://pointdf.atlassian.net/browse/CE-4044) | [CP] Remove dummy throttling on email magic link | PR | Robert Cox | 1 | FE cleanup, contained |
| [CE-4032](https://pointdf.atlassian.net/browse/CE-4032) | [CP] Add playwright tests for login v2 | PR | Robert Cox | 2 | Test work, multiple scenarios |
| [CE-4017](https://pointdf.atlassian.net/browse/CE-4017) | [CP] Use obscured email from otp response | PR | Robert Cox | 1 | API integration, contained |
| [CE-3964](https://pointdf.atlassian.net/browse/CE-3964) | [TASK] Submit A2P 10DLC registration for SMS | PR | Pratheesh Harikumar | 1 | Admin task, contained |
| [CE-3963](https://pointdf.atlassian.net/browse/CE-3963) | [HOS] Implement SMS Verification Code Generation & Sending | PR | Pratheesh Harikumar | 2 | BE work, SMS integration |
| [CE-3958](https://pointdf.atlassian.net/browse/CE-3958) | [HOS] Implement Session Management for Login by Text | PR | Pratheesh Harikumar | 2 | BE work, session logic |
| [CE-3955](https://pointdf.atlassian.net/browse/CE-3955) | [HOS] Implement throttling on SMS OTP Endpoints | PR | Pratheesh Harikumar | 2 | BE work, rate limiting |
| [CE-3954](https://pointdf.atlassian.net/browse/CE-3954) | [HOS] Implement SMS OTP Validate Endpoint | PR | Pratheesh Harikumar | 2 | BE work, validation logic |
| [CE-3953](https://pointdf.atlassian.net/browse/CE-3953) | [HOS] Implement SMS OTP Request Endpoint | PR | Pratheesh Harikumar | 2 | BE work, OTP generation |
| [CE-4037](https://pointdf.atlassian.net/browse/CE-4037) | [SVC] Enhance search endpoint to search by phone number | Ready for QA | Pratheesh Harikumar | 2 | BE work, search enhancement |
| [CE-4034](https://pointdf.atlassian.net/browse/CE-4034) | [CP] Adjust Post Funding pages based on API Response | Ready for QA | Robert Cox | 1 | FE update, contained |
| [CE-4021](https://pointdf.atlassian.net/browse/CE-4021) | [CP] Implement throttling | Ready for QA | Robert Cox | 2 | Rate limiting, multiple endpoints |
| [CE-3972](https://pointdf.atlassian.net/browse/CE-3972) | [CP] Create post-login experience | Ready for QA | Robert Cox | 2 | FE work, new flow |
| [CE-3968](https://pointdf.atlassian.net/browse/CE-3968) | [CP] Create email sent page | Ready for QA | Robert Cox | 1 | FE work, single page |
| [CE-3961](https://pointdf.atlassian.net/browse/CE-3961) | [CP] Create too many trys ("give us a call") page | Ready for QA | Robert Cox | 1 | FE work, single page |
| [CE-3959](https://pointdf.atlassian.net/browse/CE-3959) | [CP] Create SMS try again page | Ready for QA | Robert Cox | 1 | FE work, single page |
| [CE-3960](https://pointdf.atlassian.net/browse/CE-3960) | [DESIGN] Create post-login experience | RC | Robert Cox | 1 | Design work, contained |

**Done (Still Need Points):**

| Issue | Title | Status | Assignee | Suggested Size | Rationale |
|-------|-------|--------|----------|----------------|-----------|
| [CE-4020](https://pointdf.atlassian.net/browse/CE-4020) | [CP] Implement API's take 2 | DONE | Robert Cox | 2 | API implementation |
| [CE-4003](https://pointdf.atlassian.net/browse/CE-4003) | [CP] Epic ticket for initial commit of login v2 | DONE | Robert Cox | 1 | Initial setup |
| [CE-3988](https://pointdf.atlassian.net/browse/CE-3988) | [CP] Various PDS updates | DONE | Robert Cox | 1 | FE updates |
| [CE-3975](https://pointdf.atlassian.net/browse/CE-3975) | [CP] Create login page v2 feature flag | DONE | Robert Cox | 1 | Feature flag setup |
| [CE-3974](https://pointdf.atlassian.net/browse/CE-3974) | [CP] Create new page template login screens | DONE | Robert Cox | 2 | FE template work |
| [CE-3973](https://pointdf.atlassian.net/browse/CE-3973) | [CP] Wire up API data including throttling to front end | DONE | Orlando De la Pena | 2 | FE/API integration |
| [CE-3971](https://pointdf.atlassian.net/browse/CE-3971) | Add more traceability to the auth flow | DONE | Seva Maltsev | 2 | Logging/observability |
| [CE-3970](https://pointdf.atlassian.net/browse/CE-3970) | [UW] Create Underwrite API Endpoint | DONE | Orlando De la Pena | 2 | BE endpoint |
| [CE-3969](https://pointdf.atlassian.net/browse/CE-3969) | [CP] Create login by email page | DONE | Robert Cox | 1 | FE page |
| [CE-3965](https://pointdf.atlassian.net/browse/CE-3965) | [CP] Create mock responses in CP FE | DONE | Orlando De la Pena | 1 | Test mocks |
| [CE-3957](https://pointdf.atlassian.net/browse/CE-3957) | [CP] Create SMS Verification Code Entry page | DONE | Robert Cox | 1 | FE page |
| [CE-3956](https://pointdf.atlassian.net/browse/CE-3956) | [CP] Create "Log in by text" Entry page | DONE | Robert Cox | 1 | FE page |

---

## Summary by Category

| Category | Active | Done | Total | Suggested Points |
|----------|--------|------|-------|------------------|
| GRO-1211 Substories | 9 | 10 | 19 | ~22 pts |
| GRO-1246 (needs breakdown) | 1 | 0 | 1 | Epic |
| GRO-1189 (React 19) | 2 | 0 | 2 | Spike + Epic |
| CE Bugs | 3 | 0 | 3 | ~5 pts |
| CE-3942 Substories | 18 | 12 | 30 | ~45 pts |
| **Total** | **33** | **22** | **55** | **~72 pts** |

*Note: Excludes "Closed - Won't Do" issues. Done items still need points for historical tracking.*

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

**Substories Missing Estimates (19 total):**

**Active Work:**

| Issue | Title | Status | Assignee | Suggested Size | Rationale |
|-------|-------|--------|----------|----------------|-----------|
| [GRO-1275](https://pointdf.atlassian.net/browse/GRO-1275) | [Release Plan] GRO-1211: Self-Serve Updated Estimates | OPEN | Richard Collins | 1 | Release coordination |
| [GRO-1267](https://pointdf.atlassian.net/browse/GRO-1267) | [CP] Instrument Posthog | OPEN | Richard Collins | 2 | Analytics integration |
| [GRO-1235](https://pointdf.atlassian.net/browse/GRO-1235) | [QA] Add E2E test(s) for automatic offer creation | OPEN | SungMin Hong | 2 | QA automation, multiple flows |
| [GRO-1284](https://pointdf.atlassian.net/browse/GRO-1284) | [CP] Adjust language and progress-bar speed when waiting for new offer | IN PROGRESS | | 1 | FE tweak, contained |
| [GRO-1283](https://pointdf.atlassian.net/browse/GRO-1283) | [CP] Record (in PostHog) time to create a new offer | IN PROGRESS | Richard Collins | 1 | Analytics, contained |
| [GRO-1236](https://pointdf.atlassian.net/browse/GRO-1236) | [CP] Playwright tests for automatic offer creation | IN PROGRESS | Richard Collins | 2 | Test work, multiple scenarios |
| [GRO-1276](https://pointdf.atlassian.net/browse/GRO-1276) | Minor Text issue on Request Complete modal | BACKLOG | Richard Collins | 1 | Copy fix, trivial |
| [GRO-1280](https://pointdf.atlassian.net/browse/GRO-1280) | When accepted, still displays offer as next task | RC | Richard Collins | 1 | Bug fix, contained |
| [GRO-1225](https://pointdf.atlassian.net/browse/GRO-1225) | [HOS] Add details to initial estimate tasks | RC | Richard Collins | 2 | BE change |

**Done (Still Need Points):**

| Issue | Title | Status | Assignee | Suggested Size | Rationale |
|-------|-------|--------|----------|----------------|-----------|
| [GRO-1264](https://pointdf.atlassian.net/browse/GRO-1264) | [CP] Allow requesting a new offer even if current offer at maximum | DONE | Richard Collins | 2 | FE logic |
| [GRO-1253](https://pointdf.atlassian.net/browse/GRO-1253) | [CP] Reuse existing offers when possible | DONE | Richard Collins | 2 | FE optimization |
| [GRO-1234](https://pointdf.atlassian.net/browse/GRO-1234) | [CP] Redirect based on offer details rather than raw URL | DONE | Richard Collins | 2 | FE routing |
| [GRO-1233](https://pointdf.atlassian.net/browse/GRO-1233) | [CP] Create feature flag | DONE | Richard Collins | 1 | Feature flag setup |
| [GRO-1232](https://pointdf.atlassian.net/browse/GRO-1232) | [api-schemas] Add response model for request-new-amount operation | DONE | Christopher Nsimbe | 1 | Schema work |
| [GRO-1229](https://pointdf.atlassian.net/browse/GRO-1229) | [CP] Show waiting modal while new offer is processing | DONE | Richard Collins | 1 | FE modal |
| [GRO-1228](https://pointdf.atlassian.net/browse/GRO-1228) | [CP] Redirect to new offer once request is processed | DONE | Richard Collins | 1 | FE routing |
| [GRO-1227](https://pointdf.atlassian.net/browse/GRO-1227) | [HOS] Sort estimate tasks by descending offer amount | DONE | Richard Collins | 1 | BE sorting |
| [GRO-1213](https://pointdf.atlassian.net/browse/GRO-1213) | [SPIKE] Investigate effort on Backend | DONE | | Spike | Investigation |
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
| Total Stories | 1 |
| Status | Spike only |

**Assessment:** Under-scoped. Capacity plan estimates ~250 hrs FE-heavy. Spike in progress per standards.

**Substories Missing Estimates (2):**

| Issue | Title | Status | Assignee | Suggested Size | Rationale |
|-------|-------|--------|----------|----------------|-----------|
| [GRO-1191](https://pointdf.atlassian.net/browse/GRO-1191) | Investigate LOE | OPEN | | Spike | Investigation spike, no size |
| [GRO-1189](https://pointdf.atlassian.net/browse/GRO-1189) | Upgrade to React 19 | BACKLOG | | Epic | Needs breakdown after spike |

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
| No story points on 55 issues | Can't validate estimates against actuals | Size active (33) + backfill Done (22) |
| GRO-1246 under-scoped | 280 hrs planned but only 1 story exists | Break down before Feb |
| GRO-1189 under-scoped | 250 hrs planned but only spike exists | Complete spike, create stories |
| GRO-1269 not accessible | Can't analyze HELOC Opt-In epic | Verify permissions |

---

## Quick Reference - Points to Add

### GRO Team (GRO-1211 - Active)

| Issue | Points | Assignee |
|-------|--------|----------|
| [GRO-1275](https://pointdf.atlassian.net/browse/GRO-1275) | 1 | Richard Collins |
| [GRO-1267](https://pointdf.atlassian.net/browse/GRO-1267) | 2 | Richard Collins |
| [GRO-1235](https://pointdf.atlassian.net/browse/GRO-1235) | 2 | SungMin Hong |
| [GRO-1284](https://pointdf.atlassian.net/browse/GRO-1284) | 1 | |
| [GRO-1283](https://pointdf.atlassian.net/browse/GRO-1283) | 1 | Richard Collins |
| [GRO-1236](https://pointdf.atlassian.net/browse/GRO-1236) | 2 | Richard Collins |
| [GRO-1276](https://pointdf.atlassian.net/browse/GRO-1276) | 1 | Richard Collins |
| [GRO-1280](https://pointdf.atlassian.net/browse/GRO-1280) | 1 | Richard Collins |
| [GRO-1225](https://pointdf.atlassian.net/browse/GRO-1225) | 2 | Richard Collins |

### GRO Team (GRO-1211 - Done)

| Issue | Points | Assignee |
|-------|--------|----------|
| [GRO-1264](https://pointdf.atlassian.net/browse/GRO-1264) | 2 | Richard Collins |
| [GRO-1253](https://pointdf.atlassian.net/browse/GRO-1253) | 2 | Richard Collins |
| [GRO-1234](https://pointdf.atlassian.net/browse/GRO-1234) | 2 | Richard Collins |
| [GRO-1233](https://pointdf.atlassian.net/browse/GRO-1233) | 1 | Richard Collins |
| [GRO-1232](https://pointdf.atlassian.net/browse/GRO-1232) | 1 | Christopher Nsimbe |
| [GRO-1229](https://pointdf.atlassian.net/browse/GRO-1229) | 1 | Richard Collins |
| [GRO-1228](https://pointdf.atlassian.net/browse/GRO-1228) | 1 | Richard Collins |
| [GRO-1227](https://pointdf.atlassian.net/browse/GRO-1227) | 1 | Richard Collins |
| [GRO-1213](https://pointdf.atlassian.net/browse/GRO-1213) | Spike | |
| [GRO-1212](https://pointdf.atlassian.net/browse/GRO-1212) | Spike | Richard Collins |

### CE Team (Bugs)

| Issue | Points | Assignee |
|-------|--------|----------|
| [CE-3865](https://pointdf.atlassian.net/browse/CE-3865) | 2 | Robert Cox |
| [CE-3923](https://pointdf.atlassian.net/browse/CE-3923) | 2 | Daniel Cardenas |
| [CE-3926](https://pointdf.atlassian.net/browse/CE-3926) | 1 | Josh Hohman |

### CE Team (CE-3942 Login Flexibility - Active)

| Issue | Points | Assignee |
|-------|--------|----------|
| [CE-4016](https://pointdf.atlassian.net/browse/CE-4016) | 2 | Robert Cox |
| [CE-4044](https://pointdf.atlassian.net/browse/CE-4044) | 1 | Robert Cox |
| [CE-4032](https://pointdf.atlassian.net/browse/CE-4032) | 2 | Robert Cox |
| [CE-4017](https://pointdf.atlassian.net/browse/CE-4017) | 1 | Robert Cox |
| [CE-3964](https://pointdf.atlassian.net/browse/CE-3964) | 1 | Pratheesh Harikumar |
| [CE-3963](https://pointdf.atlassian.net/browse/CE-3963) | 2 | Pratheesh Harikumar |
| [CE-3958](https://pointdf.atlassian.net/browse/CE-3958) | 2 | Pratheesh Harikumar |
| [CE-3955](https://pointdf.atlassian.net/browse/CE-3955) | 2 | Pratheesh Harikumar |
| [CE-3954](https://pointdf.atlassian.net/browse/CE-3954) | 2 | Pratheesh Harikumar |
| [CE-3953](https://pointdf.atlassian.net/browse/CE-3953) | 2 | Pratheesh Harikumar |
| [CE-4037](https://pointdf.atlassian.net/browse/CE-4037) | 2 | Pratheesh Harikumar |
| [CE-4034](https://pointdf.atlassian.net/browse/CE-4034) | 1 | Robert Cox |
| [CE-4021](https://pointdf.atlassian.net/browse/CE-4021) | 2 | Robert Cox |
| [CE-3972](https://pointdf.atlassian.net/browse/CE-3972) | 2 | Robert Cox |
| [CE-3968](https://pointdf.atlassian.net/browse/CE-3968) | 1 | Robert Cox |
| [CE-3961](https://pointdf.atlassian.net/browse/CE-3961) | 1 | Robert Cox |
| [CE-3959](https://pointdf.atlassian.net/browse/CE-3959) | 1 | Robert Cox |
| [CE-3960](https://pointdf.atlassian.net/browse/CE-3960) | 1 | Robert Cox |

### CE Team (CE-3942 Login Flexibility - Done)

| Issue | Points | Assignee |
|-------|--------|----------|
| [CE-4020](https://pointdf.atlassian.net/browse/CE-4020) | 2 | Robert Cox |
| [CE-4003](https://pointdf.atlassian.net/browse/CE-4003) | 1 | Robert Cox |
| [CE-3988](https://pointdf.atlassian.net/browse/CE-3988) | 1 | Robert Cox |
| [CE-3975](https://pointdf.atlassian.net/browse/CE-3975) | 1 | Robert Cox |
| [CE-3974](https://pointdf.atlassian.net/browse/CE-3974) | 2 | Robert Cox |
| [CE-3973](https://pointdf.atlassian.net/browse/CE-3973) | 2 | Orlando De la Pena |
| [CE-3971](https://pointdf.atlassian.net/browse/CE-3971) | 2 | Seva Maltsev |
| [CE-3970](https://pointdf.atlassian.net/browse/CE-3970) | 2 | Orlando De la Pena |
| [CE-3969](https://pointdf.atlassian.net/browse/CE-3969) | 1 | Robert Cox |
| [CE-3965](https://pointdf.atlassian.net/browse/CE-3965) | 1 | Orlando De la Pena |
| [CE-3957](https://pointdf.atlassian.net/browse/CE-3957) | 1 | Robert Cox |
| [CE-3956](https://pointdf.atlassian.net/browse/CE-3956) | 1 | Robert Cox |

---

## Next Steps

1. [ ] Add story points to the 55 issues listed above (~72 pts total)
2. [ ] Break down [GRO-1246](https://pointdf.atlassian.net/browse/GRO-1246) into implementation stories
3. [ ] Complete [GRO-1191](https://pointdf.atlassian.net/browse/GRO-1191) spike for React 19 and create stories
4. [x] ~~Assign CE-3923~~ - Assigned to Daniel Cardenas
5. [ ] Verify access to GRO-1269 (HELOC Opt-In)
6. [x] ~~Break down CE-3942 (Login Flexibility) stories~~ - 30 substories identified
7. [ ] Backfill points on Done items for velocity tracking

---

**Document Created:** January 26, 2026
**Next Review:** February 3, 2026 (post 1/29 deadline)
