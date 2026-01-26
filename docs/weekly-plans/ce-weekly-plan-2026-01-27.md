# Engagement Team - Weekly Work Plan

**Week of:** January 27, 2026
**Team:** Engagement (CE)
**Team Size:** 3 engineers (Dylan, Daniel, Pratheesh) + Robert (shared with GRO)

---

## 🎯 Weekly Priorities

1. **Login SMS Completion:** Any remaining work on Login SMS feature (40% capacity)
2. **Follow-up Work Preparation:** Planning and prep work for upcoming initiatives (20% capacity)
3. **Critical Bugs:** Customer-facing issues from CE backlog (30% capacity)
4. **Code Review & Support:** PR reviews and unblocking team members (10% capacity)

---

## 👤 Individual Assignments

### Dylan Oliver (Frontend - Team Lead)
**Primary Focus:** Login SMS completion + Customer-facing bugs

**Current Work:**
- Complete any remaining Login SMS tickets
- Lead frontend architecture decisions
- Review and prioritize CE bug backlog

**New Work - Bug Fixes:**
- CE-3865: [HO Dashboard] HO Funding date on dashboard showing past date compared to funding dates in UW (High priority)
  - Customer-facing display issue
  - Currently assigned to Josh Hohman - coordinate handoff if needed
- CE-3926: [HO Dashboard] HO Dashboard timeline messaging incorrect (Medium priority)
  - Closing customers seeing incorrect delay message
  - Currently assigned to Josh Hohman - coordinate handoff if needed
- Additional critical customer-facing bugs from CE dashboard as capacity allows
- Focus on HO Dashboard frontend issues
- Prioritize based on customer impact

**Code Review Support:**
- Review PRs to unblock pipeline
- Provide frontend architecture guidance
- Mentor Daniel on CE codebase patterns

**Estimated Load:** 3-5 tickets (Login SMS completion + customer-facing bugs)

---

### Daniel Cardenas (Full-stack, Frontend-heavy)
**Primary Focus:** Login SMS completion + Follow-up work prep

**Current Work:**
- Complete any remaining Login SMS frontend work
- Full-stack support as needed

**New Work - Prep:**
- Follow-up work: Planning and preparation for upcoming initiatives
- Collaborate with team on requirements gathering
- Technical spike work if needed

**New Work - Bug Fixes:**
- CE-3925: [HO Dashboard] HO name is blank in HO application (Medium priority)
  - Self-serve FM docket with missing name and email fields
  - Data population issue
- CE-3923: [UW] Magic logic for identifying docket duplicates fails when there is space or - in the address (Medium priority)
  - Address matching logic bug affecting duplicate detection
  - Multiple customer examples provided
- Support Dylan with additional customer-facing bugs from CE dashboard as capacity allows
- Focus on full-stack issues
- Prioritize based on customer impact

**Code Review Support:**
- Review PRs to unblock pipeline
- Learn CE codebase patterns and best practices

**Estimated Load:** 3-4 tickets (Login SMS + follow-up prep + bugs)

---

### Pratheesh Harikumar (Staff Engineer - Shared with GRO)
**Primary Focus:** CE technical leadership + Architecture decisions

**Current Work:**
- Technical leadership for CE initiatives
- Architecture and design review for Login SMS completion
- Staff-level technical decisions

**New Work - Prep:**
- Follow-up work: Architecture planning and technical design
- Identify technical risks and mitigation strategies
- Collaborate with team on implementation approach

**Code Review Support:**
- Review complex PRs requiring senior engineer perspective
- Provide architecture guidance
- Mentor Dylan and Daniel on technical decisions

**Bug Fixes:**
- CE-3946: [HO Dashboard] HO is unable to get to dashboard and stuck in a loop (High priority)
  - Customer stuck in email verification loop
  - Critical customer-facing issue preventing dashboard access
  - Currently assigned to you in Jira
- Support team with additional critical customer-facing bugs if capacity allows
- Focus on complex or high-risk fixes

**Estimated Load:** 2-3 tickets (architecture/technical leadership focus) + code reviews

**Note:** Pratheesh is shared with GRO team - coordinate capacity with GRO priorities

---

### Robert Cox (Design + Frontend - Shared with GRO)
**Primary Focus:** GRO design work (primary), CE support (minimal)

**CE Work (Minimal - if capacity allows):**
- Design review for CE initiatives if needed
- Frontend code review support if requested
- Prioritize GRO-1211 deadline (1/29) over CE work

**Estimated Load:** Minimal CE involvement - focus on GRO priorities

**Note:** Robert is heavily loaded with GRO work (GRO-1211 critical 1/29 deadline + GRO-1269 and GRO-1246 design). Only involve for critical CE design needs.

---

## 📊 Summary by Focus Area

**Login SMS Completion:** 40% of capacity
- Dylan: Complete remaining frontend work, coordinate with team
- Daniel: Complete remaining frontend/full-stack work
- Pratheesh: Architecture review and technical oversight
- **Goal: Complete all remaining Login SMS work this week**

**Follow-up Work Preparation:** 20% of capacity
- Daniel: Primary owner for prep and planning
- Pratheesh: Architecture and technical design
- Dylan: Frontend architecture input
- **Goal: Requirements gathered, technical approach defined**

**Critical Bugs (CE Dashboard):** 30% of capacity
- Dylan: CE-3865 (HO Funding date - High), CE-3926 (Timeline messaging - Medium)
- Daniel: CE-3925 (Blank HO name - Medium), CE-3923 (Docket duplicate logic - Medium)
- Pratheesh: CE-3946 (Dashboard loop - High)
- **Goal: All 5 customer-facing bugs resolved (2 High, 3 Medium priority)**

**Code Review & Support:** 10% of capacity
- All engineers: Review PRs to keep pipeline moving
- Pratheesh: Senior engineer perspective on architecture
- Dylan: Team lead guidance and mentorship

---

## 🎯 Week Goals

**Must Complete:**
- [ ] Complete all remaining Login SMS work
- [ ] Fix CE-3865: HO Funding date display issue (High priority)
- [ ] Fix CE-3946: HO unable to get to dashboard, stuck in loop (High priority)
- [ ] Fix CE-3923: Docket duplicate logic with space/hyphen in address (Medium priority)
- [ ] Fix CE-3925: HO name is blank in HO application (Medium priority)
- [ ] Fix CE-3926: HO Dashboard timeline messaging incorrect (Medium priority)
- [ ] Complete follow-up work requirements gathering and planning
- [ ] Define technical approach for follow-up work initiatives

**Stretch Goals:**
- [ ] Begin implementation of follow-up work if prep completes early
- [ ] Address additional bugs from CE dashboard beyond the critical ones
- [ ] Complete technical spike work for follow-up initiatives

---

## 🚨 Risk Mitigation

**Risks:**
1. Login SMS may have unknown remaining work - scope unclear
2. Pratheesh shared with GRO - capacity may be limited
3. Robert heavily loaded with GRO work - minimal CE support available
4. Follow-up work requirements may not be fully defined yet
5. Bug prioritization may change based on customer escalations
6. CE-3865 and CE-3926 currently assigned to Josh Hohman - may need coordination/handoff
7. 5 customer-facing bugs may be ambitious alongside Login SMS completion

**Mitigation:**
- Dylan: Audit Login SMS tickets to identify all remaining work immediately
- Dylan: Coordinate with Josh Hohman on CE-3865 and CE-3926 to determine if handoff is needed
- Pratheesh: Communicate capacity constraints to both GRO and CE teams
- Pratheesh: Prioritize CE-3946 (High priority) as it's customer-blocking
- Daniel: Focus on CE-3925 and CE-3923 first (smaller scope), then support follow-up prep
- Robert: Only involve for critical CE design needs - prioritize GRO 1/29 deadline
- Team: If Login SMS completes early, shift capacity to bugs; if bugs pile up, defer follow-up prep
- Daily standups: Adjust priorities based on customer escalations and Login SMS progress
- Team: Review CE bug dashboard daily to stay on top of new critical issues

---

## 📈 Capacity Analysis

**Engagement Team Size:** 3 engineers (+ 1 shared with GRO)

**Dylan:**
- 4-6 tickets: Login SMS completion + CE-3865 (Funding date - High) + CE-3926 (Timeline messaging - Medium) + additional bugs if capacity
- Code review and team lead responsibilities
- **Status:** Full capacity - Login SMS completion and 2 customer-facing bugs

**Daniel:**
- 4-5 tickets: Login SMS completion + CE-3925 (Blank HO name - Medium) + CE-3923 (Docket duplicates - Medium) + follow-up work prep
- Learning CE codebase (joined Nov 2025)
- **Status:** Full capacity - feature work, bugs, and prep

**Pratheesh:**
- 3-4 tickets: CE-3946 (Dashboard loop - High) + Architecture/technical leadership + follow-up work design
- Code review support (senior engineer perspective)
- **Status:** Shared with GRO - coordinate capacity carefully, CE-3946 is high priority

**Robert:**
- Minimal CE involvement - focus on GRO priorities
- Available for critical CE design needs only
- **Status:** Heavily loaded with GRO work (GRO-1211 critical 1/29 deadline)

**Total:** ~11-15 work items (Login SMS + 5 bugs + follow-up prep) + code reviews

---

## 📝 Notes

**Definitions:**
- **Login SMS:** SMS-based login feature (specific epic/tickets TBD)
- **Follow-up Work:** Upcoming CE initiatives requiring preparation (specific details TBD)
- **CE Dashboard:** Customer-facing bugs tracked at https://pointdf.atlassian.net/jira/dashboards/10141?maximized=12474

**Success Metrics:**
- Login SMS: All remaining work completed and shipped
- Follow-up Work: Requirements defined, technical approach documented
- Bugs: All 5 customer-facing bugs resolved:
  - CE-3865 (HO Funding date - High)
  - CE-3946 (Dashboard loop - High)
  - CE-3923 (Docket duplicates - Medium)
  - CE-3925 (Blank HO name - Medium)
  - CE-3926 (Timeline messaging - Medium)
- Code Reviews: No PR blockers, pipeline stays moving

**Key Links:**
- CE Bug Dashboard: https://pointdf.atlassian.net/jira/dashboards/10141?maximized=12474 (CE only)
- CE-3865: [HO Funding date display issue (High)](https://pointdf.atlassian.net/browse/CE-3865)
- CE-3946: [HO unable to get to dashboard, stuck in loop (High)](https://pointdf.atlassian.net/browse/CE-3946)
- CE-3923: [Docket duplicate logic fails with space/hyphen (Medium)](https://pointdf.atlassian.net/browse/CE-3923)
- CE-3925: [HO name is blank in HO application (Medium)](https://pointdf.atlassian.net/browse/CE-3925)
- CE-3926: [HO Dashboard timeline messaging incorrect (Medium)](https://pointdf.atlassian.net/browse/CE-3926)

**Action Items:**
- [ ] Dylan: Identify all remaining Login SMS tickets and share with team
- [ ] Dylan: Coordinate with Josh Hohman on CE-3865 and CE-3926 assignments/handoff
- [ ] Daniel: Start on CE-3925 (Blank HO name) and CE-3923 (Docket duplicates)
- [ ] Pratheesh: Prioritize CE-3946 (Dashboard loop - High priority, customer-blocking)
- [ ] Pratheesh: Document capacity split between GRO and CE teams
- [ ] Daniel: Work with product to define follow-up work requirements
- [ ] Team: Review CE bug dashboard daily for new critical issues

---

**Plan Created:** January 24, 2026
**Plan Owner:** Wei Huang
**Review Date:** January 31, 2026 (end of week retrospective)
