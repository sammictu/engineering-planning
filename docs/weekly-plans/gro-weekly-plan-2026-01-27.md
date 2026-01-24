# Growth Team - Weekly Work Plan

**Week of:** January 27, 2026
**Team:** Growth (GRO)
**Team Size:** 3 engineers (David, Robert, Richard)

---

## 🎯 Weekly Priorities

1. **Primary Epic Focus:** GRO-1211 - Self-Serve Updated Estimates (60% capacity) **⚠️ CRITICAL: Target Release 1/29 - CANNOT MISS**
2. **Critical Bugs:** Customer-facing issues from backlog (30% capacity)
3. **Operational Health:** BugSnag noise cleanup, log sorting (10% capacity)
4. **Prep Work:** Design/planning for GRO-1246 (Follow Up Work with Self Serve Estimate) and GRO-1189 (Upgrade to React 19)

---

## 👤 Individual Assignments

### Richard Collins (Full-stack Frontend)
**Primary Focus:** GRO-1211 (Self-Serve Updated Estimates) + CP/Partner FE work

**Finish (High Priority):**
- Continue existing tickets in flight (6-7 tickets currently active)
- Focus on completing GRO-1211 related work

**New Work (if capacity):**
- GRO-1272: [CP/Partner FE] BugSnag: Audit and categorize top 20 frontend errors (2 hours)
  - Review BugSnag for CP and Partner FE errors
  - Categorize and create action plan

**Operational:**
- BugSnag: Review and categorize frontend errors in CP and Partner FE
- Coordinate with David on cross-stack errors

**Estimated Load:** 6-7 in-flight tickets + 1 operational task

---

### David Conger (Backend)
**Primary Focus:** GRO-1211 backend support + Bug fixes + Operational health

**Finish:**
- Any carryover backend work for GRO-1211

**New Work - Bug Fixes:**
- Review and prioritize critical bugs from backlog
- Focus on PQ, HOS, Marketing, Partner BE issues

**New Work - Epic Support:**
- Backend tasks for GRO-1211 (Self-Serve Updated Estimates)
- Support for GRO-1246 prep work if needed

**Operational:**
- GRO-1272: [BE] BugSnag: Audit and categorize top 20 backend errors (2 hours)
  - Review PQ, HOS, Marketing, Partner BE errors
  - Categorize: Real bugs vs. noise vs. external
- GRO-1274: [BE] Logs: Audit production logs and improve log levels (1-2 hours)
  - Review Rails logs for verbosity
  - Identify missing context in error logs
  - Plan log level improvements

**Estimated Load:** 3-4 bug fixes + 2 operational tasks + epic support

---

### Robert Cox (Design + Frontend)
**Primary Focus:** Design work for GRO-1246 (Follow Up Work with Self Serve Estimate) + Frontend support

**Current:**
- Complete any in-flight design work

**New Work:**
- GRO-1246 (Follow Up Work with Self Serve Estimate): [Design] Design work for upcoming epic
  - Create Figma designs
  - User flow documentation
  - Collaborate with team on requirements

**New Work - Prep:**
- GRO-1189 (Upgrade to React 19): [Design] Initial design exploration if capacity allows

**Code Review Support:**
- Review PRs to unblock pipeline
- Support Richard and David with FE reviews

**Operational:**
- BugSnag: Review design-related errors (CSS, responsive issues) if time allows

**Estimated Load:** 1-2 design tickets + code reviews

---

## 📊 Summary by Focus Area

**Primary Epic (GRO-1211 - Self-Serve Updated Estimates):** 60% of capacity **⚠️ MUST SHIP 1/29**
- Richard: Continuing frontend work (6-7 tickets in flight)
- David: Backend support for Self-Serve Updated Estimates
- **Goal: COMPLETE AND SHIP by 1/29 - CRITICAL DEADLINE**

**Critical Bugs:** 30% of capacity
- David: 3-4 critical customer-facing bugs from backlog
- Focus on PQ, HOS, Partner BE issues
- Prioritize based on customer impact

**Operational Health (NEW - GRO-1271):** 10% of capacity
- **BugSnag Cleanup (GRO-1272, GRO-1273):**
  - David + Richard: Audit top 20 errors (~2 hours each)
  - Categorize: Real bugs vs. noise vs. known issues
  - Create action plan and implement filters
  - Target: 50% reduction in BugSnag noise
- **Log Sorting (GRO-1274):**
  - David: Audit production logs (~1-2 hours)
  - Review log levels and verbosity
  - Plan structured logging improvements

**Prep Work:** 5-10% of capacity
- Robert: Design for GRO-1246 (Follow Up Work with Self Serve Estimate)
- Team: Planning discussions for GRO-1189 (Upgrade to React 19) and GRO-1269 (Increase HELOC Opt-In Rate)

---

## 🎯 Week Goals

**Must Complete:**
- [ ] **⚠️ CRITICAL: Ship GRO-1211 (Self-Serve Updated Estimates) to production by 1/29 - CANNOT MISS**
- [ ] Fix 3-4 critical customer-facing bugs
- [ ] Complete BugSnag error audit (GRO-1272)
- [ ] Complete log audit (GRO-1274)
- [ ] Design work for GRO-1246 (Follow Up Work with Self Serve Estimate) started

**Stretch Goals:**
- [ ] Implement BugSnag filters (GRO-1273)
- [ ] Start log improvements from audit findings
- [ ] Begin prep work for GRO-1189 (Upgrade to React 19)

---

## 🔧 Operational Health Tasks (GRO-1271)

### BugSnag Noise Cleanup
**Owner:** Primarily David (backend) + Richard (frontend)
**Time Budget:** 4 hours total (2 hours each)

**This Week:**
1. **Audit Current Errors (GRO-1272)** - 2 hours
   - Review top 20 errors in BugSnag
   - David: Focus on PQ, HOS, Marketing, Partner BE
   - Richard: Focus on CP, Partner FE
   - Categorize: Real bugs | Known issues | Noise | External
   - Document findings in shared doc/spreadsheet

2. **Create Action Plan**
   - Real bugs → Create Jira tickets (priority order)
   - Known issues → Document and silence if non-critical
   - Noise → Plan filters or silence rules
   - External → Update error handling strategy

3. **Implementation (GRO-1273)** - If time allows
   - Configure BugSnag filters for top noise sources
   - Add error boundaries for known patterns
   - Document what's silenced and why

### Log Sorting & Improvement
**Owner:** Primarily David (backend)
**Time Budget:** 1-2 hours

**This Week (GRO-1274):**
1. **Audit Current Logs** - 1-2 hours
   - Review production logs in Rails apps (PQ, HOS, Marketing, Partner BE)
   - Identify overly verbose areas
   - Find missing context in errors (user_id, request_id, etc.)
   - Document findings and recommendations

2. **Plan Improvements**
   - Prioritize which logs to fix first
   - Identify quick wins vs. larger refactors
   - Create follow-up tickets if needed

---

## 🚨 Risk Mitigation

**Risks:**
1. **⚠️ CRITICAL: GRO-1211 (Self-Serve Updated Estimates) MUST ship by 1/29 - CANNOT MISS**
2. Richard has 6-7 tickets in flight - may be at capacity
3. Adding operational work may reduce feature velocity
4. Bug prioritization may change based on customer escalations
5. Design work timing dependent on product requirements clarity

**Mitigation:**
- **GRO-1211 MUST be top priority for entire team - all hands on deck if needed**
- **Daily check-ins on GRO-1211 progress - escalate blockers immediately**
- Richard: Focus on finishing GRO-1211 tickets first, defer operational work if needed
- David: Prioritize GRO-1211 backend support, bugs can be pushed if necessary
- Timebox operational work strictly (4-6 hours total for team) - defer if conflicts with 1/29 deadline
- Robert: Support GRO-1211 with reviews and design clarifications as highest priority
- Daily standups: Check capacity and adjust priorities as needed

---

## 📈 Capacity Analysis

**Growth Team Size:** 3 engineers

**Richard:**
- 6-7 tickets in flight (GRO-1211 - Self-Serve Updated Estimates - **MUST SHIP 1/29**)
- 1 operational task (BugSnag audit - 2 hours) - defer if conflicts with 1/29 deadline
- **Status:** At or near capacity - GRO-1211 is top priority

**David:**
- 3-4 bug fixes (can be deferred if conflicts with GRO-1211)
- GRO-1211 backend support (**MUST SHIP 1/29**)
- 2 operational tasks (BugSnag audit - 2 hours, Log audit - 1-2 hours) - defer if conflicts with 1/29 deadline
- **Status:** Full capacity - GRO-1211 is top priority

**Robert:**
- 1-2 design tickets (GRO-1246 - Follow Up Work with Self Serve Estimate, potentially GRO-1189 - Upgrade to React 19)
- Code review support (prioritize GRO-1211 reviews)
- **Status:** Good capacity, focus on GRO-1211 support and design deliverables

**Total:** ~12-15 work items + operational health tasks

---

## 📝 Notes

**Definitions:**
- **BugSnag Noise:** Errors logged that aren't actionable or are false positives
- **Log Sorting:** Organizing logs by importance and reducing verbosity
- **Operational Health:** Work that improves system observability and reduces on-call burden

**Success Metrics:**
- **⚠️ CRITICAL: GRO-1211 (Self-Serve Updated Estimates) FULLY SHIPPED to production by 1/29**
- Bugs: 3-4 critical bugs resolved
- BugSnag: Top 20 errors categorized, action plan created
- Logs: Audit complete with improvement recommendations
- Design: GRO-1246 (Follow Up Work with Self Serve Estimate) Figma designs in progress

**Key Links:**
- Epic: [GRO-1211 - Self-Serve Updated Estimates](https://pointdf.atlassian.net/browse/GRO-1211)
- Epic: [GRO-1271 - Operational Health](https://pointdf.atlassian.net/browse/GRO-1271)
- Bug Dashboard: https://pointdf.atlassian.net/jira/dashboards/10141?maximized=12474

---

**Plan Created:** January 24, 2026
**Plan Owner:** Wei Huang
**Review Date:** January 31, 2026 (end of week retrospective)
