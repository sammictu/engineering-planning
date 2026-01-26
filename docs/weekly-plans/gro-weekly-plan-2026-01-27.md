# Growth Team - Weekly Work Plan

**Week of:** January 27, 2026
**Team:** Growth (GRO)
**Team Size:** 4 engineers (David, Robert, Richard, Tomas)

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
**Primary Focus:** Bug fixes + Operational health

**New Work - Bug Fixes:**
- GRO-1129: [PQ] Email lookup is case-sensitive, creating duplicate customers (PR in progress)
- GRO-1186: UTM parameters are not populated correctly (backlog)
- Review and prioritize additional critical bugs from backlog
- Focus on PQ, HOS, Marketing, Partner BE issues
- Prioritize based on customer impact

**New Work - Prep:**
- Support for GRO-1246 prep work if needed

**Operational:**
- GRO-1272: [BE] BugSnag: Audit and categorize top 20 backend errors (2 hours)
  - Review PQ, HOS, Marketing, Partner BE errors
  - Categorize: Real bugs vs. noise vs. external
- GRO-1274: [BE] Logs: Audit production logs and improve log levels (1-2 hours)
  - Review Rails logs for verbosity
  - Identify missing context in error logs
  - Plan log level improvements

**Estimated Load:** 3-4 bug fixes + 2 operational tasks

---

### Robert Cox (Design + Frontend)
**Primary Focus:** Design work for GRO-1269 (Increase HELOC Opt-In Rate) + GRO-1246 (Follow Up Work with Self Serve Estimate) + Frontend support

**Current:**
- Complete any in-flight design work

**New Work:**
- GRO-1269 (Increase HELOC Opt-In Rate): [Design] Design work for growth priority epic
  - Create Figma designs
  - User flow documentation
  - Conversion optimization mockups
  - Collaborate with team on requirements
- GRO-1246 (Follow Up Work with Self Serve Estimate): [Design] Design work for upcoming epic
  - Create Figma designs
  - User flow documentation
  - Collaborate with team on requirements

**New Work - Prep:**
- GRO-1189 (Upgrade to React 19): [Design] Initial design exploration if capacity allows

**Code Review Support:**
- Review PRs to unblock pipeline
- Support Richard and David with FE reviews
- **Available to support GRO-1211 (Self-Serve Updated Estimates) if needed to meet 1/29 deadline**

**Operational:**
- BugSnag: Review design-related errors (CSS, responsive issues) if time allows

**Estimated Load:** 1-2 design tickets + code reviews

---

### Tomas Herrera (Full-stack)
**Primary Focus:** "What You Get" section + Customer-facing bugs

**New Work:**
- Work on "What You Get" section implementation
- Full-stack work (frontend and backend as needed)

**New Work - Bug Fixes:**
- GRO-1192: [CP] "Cash to you" amount only reflects fees, not debt payoff (customer-facing calculation error)
- Additional critical customer-facing bugs from backlog
- Prioritize based on customer impact
- Focus on PQ, HOS, Partner BE/FE issues

**Code Review Support:**
- Review PRs to unblock pipeline
- Provide senior engineer perspective on architecture decisions

**Estimated Load:** 2-4 tickets (What You Get section + customer-facing bugs)

---

## 📊 Summary by Focus Area

**Primary Epic (GRO-1211 - Self-Serve Updated Estimates):** 60% of capacity **⚠️ MUST SHIP 1/29**
- Richard: Continuing frontend work (6-7 tickets in flight) - **ONLY engineer on GRO-1211**
- Robert: Available to support if needed
- **Goal: COMPLETE AND SHIP by 1/29 - CRITICAL DEADLINE**

**Critical Bugs:** 30% of capacity
- David: GRO-1129 (email case-sensitivity), GRO-1186 (UTM parameters), + 1-2 additional bugs
- Tomas: "What You Get" section implementation + GRO-1192 (cash calculation) + 1-2 additional bugs
- Focus on PQ, HOS, CP, Partner BE/FE issues
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
- Robert: Design for GRO-1269 (Increase HELOC Opt-In Rate) - **Priority epic**
- Robert: Design for GRO-1246 (Follow Up Work with Self Serve Estimate)
- Team: Planning discussions for GRO-1189 (Upgrade to React 19)

---

## 🎯 Week Goals

**Must Complete:**
- [ ] **⚠️ CRITICAL: Ship GRO-1211 (Self-Serve Updated Estimates) to production by 1/29 - CANNOT MISS**
- [ ] **Complete all mandatory sign-offs for GRO-1275 ([Release Plan] for GRO-1211): QA and Analytics**
- [ ] Fix critical customer-facing bugs: GRO-1129 (email case-sensitivity), GRO-1186 (UTM parameters), GRO-1192 (cash calculation)
- [ ] Complete BugSnag error audit (GRO-1272)
- [ ] Complete log audit (GRO-1274)
- [ ] Design work for GRO-1269 (Increase HELOC Opt-In Rate) started - **Priority epic**
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
- **GRO-1211 MUST be top priority - Richard is sole owner, Robert available as backup**
- **Daily check-ins on GRO-1211 progress - escalate blockers immediately**
- Richard: Focus on finishing GRO-1211 tickets first, defer operational work if needed
- Robert: Available to jump in on GRO-1211 if Richard is blocked or behind schedule
- David: Continue with bugs and operational health, ready to context switch if GRO-1211 needs backend support
- Tomas: Focus on "What You Get" section and bugs, can help with GRO-1211 reviews if needed
- Timebox operational work strictly (4-6 hours total for team) - defer if conflicts with 1/29 deadline
- Daily standups: Check GRO-1211 progress and adjust priorities as needed

---

## 📈 Capacity Analysis

**Growth Team Size:** 4 engineers

**Richard:**
- 6-7 tickets in flight (GRO-1211 - Self-Serve Updated Estimates - **MUST SHIP 1/29**)
- **ONLY engineer working on GRO-1211**
- 1 operational task (BugSnag audit - 2 hours) - defer if conflicts with 1/29 deadline
- **Status:** At or near capacity - GRO-1211 is top priority

**David:**
- 3-4 bug fixes: GRO-1129 (email case-sensitivity), GRO-1186 (UTM parameters), + additional customer-facing issues
- 2 operational tasks (BugSnag audit - 2 hours, Log audit - 1-2 hours)
- **Status:** Full capacity - bug fixes and operational health focus

**Tomas:**
- 2-4 tickets: "What You Get" section + GRO-1192 (cash calculation) + additional customer-facing bugs
- Code review support
- **Status:** Full capacity - feature work and critical bugs

**Robert:**
- 2-3 design tickets (GRO-1269 - Increase HELOC Opt-In Rate [Priority], GRO-1246 - Follow Up Work with Self Serve Estimate)
- Code review support (prioritize GRO-1211 reviews)
- Available to support GRO-1211 if needed for 1/29 deadline
- **Status:** Good capacity, focus on GRO-1269 and GRO-1246 design deliverables and availability for GRO-1211 support

**Total:** ~14-18 work items + operational health tasks

---

## 📝 Notes

**Definitions:**
- **BugSnag Noise:** Errors logged that aren't actionable or are false positives
- **Log Sorting:** Organizing logs by importance and reducing verbosity
- **Operational Health:** Work that improves system observability and reduces on-call burden

**Success Metrics:**
- **⚠️ CRITICAL: GRO-1211 (Self-Serve Updated Estimates) FULLY SHIPPED to production by 1/29**
- **Release Plan (GRO-1275): All mandatory sign-offs completed (QA, Analytics)**
- Bugs: GRO-1129, GRO-1186, GRO-1192 resolved (+ additional critical bugs if identified)
- BugSnag: Top 20 errors categorized, action plan created (GRO-1272)
- Logs: Audit complete with improvement recommendations (GRO-1274)
- Design: GRO-1269 (Increase HELOC Opt-In Rate) Figma designs in progress - **Priority epic**
- Design: GRO-1246 (Follow Up Work with Self Serve Estimate) Figma designs in progress

**Key Links:**
- Epic: [GRO-1211 - Self-Serve Updated Estimates](https://pointdf.atlassian.net/browse/GRO-1211)
- Release Plan: [GRO-1275 - Release Plan for GRO-1211](https://pointdf.atlassian.net/browse/GRO-1275)
- Epic: [GRO-1271 - Operational Health](https://pointdf.atlassian.net/browse/GRO-1271)
- Bug Dashboard: https://pointdf.atlassian.net/jira/dashboards/10141?maximized=12474

---

**Plan Created:** January 24, 2026
**Plan Owner:** Wei Huang
**Review Date:** January 31, 2026 (end of week retrospective)
