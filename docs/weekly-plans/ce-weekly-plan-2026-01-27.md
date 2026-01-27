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

### Pratheesh Harikumar (Staff Engineer)
**Primary Focus:** Login SMS implementation (BE + FE) + CE technical leadership

**Current Work:**
- **Login SMS implementation:** Primary owner for backend and frontend work
  - ⚠️ Currently BLOCKED on Twilio approval (3-week SLA, submitted week of Jan 18, 2026)
  - Backend work: XS scope
  - Frontend work: S scope
  - Use blocked time for technical design and preparation
- Technical leadership for CE initiatives
- Staff-level technical decisions

**New Work - Prep:**
- Login SMS: Technical design and architecture while blocked on Twilio
- Follow-up work: Architecture planning and technical design
- Identify technical risks and mitigation strategies
- Collaborate with team on implementation approach

**Code Review Support:**
- Review complex PRs requiring senior engineer perspective
- Provide architecture guidance
- Mentor Dylan and Daniel on technical decisions

**Bug Fixes (if capacity allows):**
- Support team with critical customer-facing bugs if Login SMS preparation is complete
- Focus on complex or high-risk fixes

**Estimated Load:** 2-3 tickets (Login SMS + architecture/technical leadership focus) + code reviews

**Note:** Pratheesh is fully allocated to Engagement team for Q1 2026

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
- Pratheesh: Primary owner - backend and frontend implementation (BLOCKED on Twilio approval)
- Dylan: Frontend support and coordination
- Daniel: Frontend/full-stack support
- **Goal: Complete technical design and preparation while blocked on Twilio; implement immediately when unblocked**

**Follow-up Work Preparation:** 20% of capacity
- Daniel: Primary owner for prep and planning
- Pratheesh: Architecture and technical design
- Dylan: Frontend architecture input
- **Goal: Requirements gathered, technical approach defined**

**Critical Bugs (CE Dashboard):** 30% of capacity
- Dylan: CE-3865 (HO Funding date - High), CE-3926 (Timeline messaging - Medium)
- Daniel: CE-3925 (Blank HO name - Medium), CE-3923 (Docket duplicate logic - Medium)
- **Goal: All 4 customer-facing bugs resolved (1 High, 3 Medium priority)**
- **Note:** CE-3946 (Dashboard loop - High) has been resolved

**Code Review & Support:** 10% of capacity
- All engineers: Review PRs to keep pipeline moving
- Pratheesh: Senior engineer perspective on architecture
- Dylan: Team lead guidance and mentorship

---

## 🎯 Week Goals

**Must Complete:**
- [ ] Complete Login SMS technical design and preparation (while blocked on Twilio)
- [ ] Fix CE-3865: HO Funding date display issue (High priority)
- [ ] Fix CE-3923: Docket duplicate logic with space/hyphen in address (Medium priority)
- [ ] Fix CE-3925: HO name is blank in HO application (Medium priority)
- [ ] Fix CE-3926: HO Dashboard timeline messaging incorrect (Medium priority)
- [ ] Complete follow-up work requirements gathering and planning
- [ ] Define technical approach for follow-up work initiatives

**Completed:**
- [x] ✅ CE-3946: HO unable to get to dashboard, stuck in loop (High priority) - RESOLVED

**Stretch Goals:**
- [ ] Begin implementation of follow-up work if prep completes early
- [ ] Address additional bugs from CE dashboard beyond the critical ones
- [ ] Complete technical spike work for follow-up initiatives

---

## 🚨 Risk Mitigation

**Risks:**
1. ⚠️ **Login SMS BLOCKED on Twilio approval** - Cannot implement until approval received (3-week SLA)
2. Login SMS may have unknown remaining work - scope unclear
3. Robert heavily loaded with GRO work - minimal CE support available
4. Follow-up work requirements may not be fully defined yet
5. Bug prioritization may change based on customer escalations
6. CE-3865 and CE-3926 currently assigned to Josh Hohman - may need coordination/handoff
7. 4 customer-facing bugs may be ambitious alongside Login SMS preparation

**Mitigation:**
- Pratheesh: Focus on Login SMS technical design and preparation while blocked on Twilio
- Pratheesh: Ready to implement immediately when Twilio approval is received
- Dylan: Audit Login SMS tickets to identify all remaining work immediately
- Dylan: Coordinate with Josh Hohman on CE-3865 and CE-3926 to determine if handoff is needed
- Daniel: Focus on CE-3925 and CE-3923 first (smaller scope), then support follow-up prep
- Robert: Only involve for critical CE design needs - prioritize GRO 1/29 deadline
- Team: Use blocked Twilio time for technical design and prep work
- Daily standups: Adjust priorities based on customer escalations and Twilio approval status
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
- 2-3 tickets: Login SMS implementation (primary owner) + Architecture/technical leadership + follow-up work design
- Code review support (senior engineer perspective)
- **Status:** Fully allocated to Engagement for Q1 2026, Login SMS currently BLOCKED on Twilio approval

**Robert:**
- Minimal CE involvement - focus on GRO priorities
- Available for critical CE design needs only
- **Status:** Heavily loaded with GRO work (GRO-1211 critical 1/29 deadline)

**Total:** ~10-14 work items (Login SMS prep + 4 bugs + follow-up prep) + code reviews
**Note:** CE-3946 resolved, Login SMS blocked on Twilio approval

---

## 📝 Notes

**Definitions:**
- **Login SMS:** SMS-based login feature (specific epic/tickets TBD)
- **Follow-up Work:** Upcoming CE initiatives requiring preparation (specific details TBD)
- **CE Dashboard:** Customer-facing bugs tracked at https://pointdf.atlassian.net/jira/dashboards/10141?maximized=12474

**Success Metrics:**
- Login SMS: Technical design complete, ready to implement when Twilio approved (currently BLOCKED)
- Follow-up Work: Requirements defined, technical approach documented
- Bugs: All 4 remaining customer-facing bugs resolved:
  - CE-3865 (HO Funding date - High)
  - CE-3923 (Docket duplicates - Medium)
  - CE-3925 (Blank HO name - Medium)
  - CE-3926 (Timeline messaging - Medium)
- Code Reviews: No PR blockers, pipeline stays moving

**Completed:**
- ✅ CE-3946 (Dashboard loop - High) - RESOLVED

**Key Links:**
- CE Bug Dashboard: https://pointdf.atlassian.net/jira/dashboards/10141?maximized=12474 (CE only)
- CE-3865: [HO Funding date display issue (High)](https://pointdf.atlassian.net/browse/CE-3865)
- CE-3946: [HO unable to get to dashboard, stuck in loop (High)](https://pointdf.atlassian.net/browse/CE-3946)
- CE-3923: [Docket duplicate logic fails with space/hyphen (Medium)](https://pointdf.atlassian.net/browse/CE-3923)
- CE-3925: [HO name is blank in HO application (Medium)](https://pointdf.atlassian.net/browse/CE-3925)
- CE-3926: [HO Dashboard timeline messaging incorrect (Medium)](https://pointdf.atlassian.net/browse/CE-3926)

**Action Items:**
- [ ] Pratheesh: Complete Login SMS technical design and architecture (while blocked on Twilio)
- [ ] Pratheesh: Monitor Twilio approval status daily, implement immediately when unblocked
- [ ] Dylan: Identify all remaining Login SMS tickets and share with team
- [ ] Dylan: Coordinate with Josh Hohman on CE-3865 and CE-3926 assignments/handoff
- [ ] Daniel: Start on CE-3925 (Blank HO name) and CE-3923 (Docket duplicates)
- [ ] Daniel: Work with product to define follow-up work requirements
- [ ] Team: Review CE bug dashboard daily for new critical issues

---

**Plan Created:** January 24, 2026
**Plan Owner:** Wei Huang
**Review Date:** January 31, 2026 (end of week retrospective)
