# Growth Team - Weekly Work Plan Template

**Week of:** [Date]
**Team:** Growth (GRO)
**Team Size:** 3 engineers (David, Robert, Richard)

---

## 🎯 Weekly Priorities

1. **Primary Epic Focus:** [Epic Name and ID]
2. **Critical Bugs:** Customer-facing issues
3. **Operational Health:** BugSnag noise cleanup, log sorting
4. **Prep Work:** Design/planning for upcoming epics

---

## 👤 Individual Assignments

### Richard Collins (Full-stack Frontend)
**Primary Focus:** [CP/Partner FE/HOS work]

**Finish (High Priority):**
- [Ticket ID] [Repo] Description (Status)

**Continue:**
- [Ticket ID] [Repo] Description (In Progress)

**New Work (if capacity):**
- [Ticket ID] [Repo] Description

**Operational:**
- BugSnag: Review and categorize [CP] frontend errors
- Logs: Improve client-side error logging

**Estimated Load:** X tickets

---

### David Conger (Backend)
**Primary Focus:** [PQ/Marketing/Partner BE work]

**Finish:**
- [Ticket ID] [Repo] Description (Status)

**New Work - Bug Fixes:**
- [Ticket ID] [Repo] Description (Priority order)

**New Work - Epic Support:**
- Backend tasks for [Epic Name]

**Operational:**
- BugSnag: Clean up [PQ] backend noise, categorize real errors vs. noise
- Logs: Review and improve Rails logging (reduce verbosity, add structured logging)
- Error handling: Add proper error boundaries for known error patterns

**Estimated Load:** X tickets

---

### Robert Cox (Design + Frontend)
**Primary Focus:** Design work + Frontend support

**Current:**
- [Ticket ID] [Design] Description

**New Work:**
- [Ticket ID] [Design] Description for upcoming epic
- Figma designs required

**Code Review Support:**
- Review PRs to unblock pipeline

**Operational:**
- BugSnag: Review design-related errors (CSS, responsive issues)

**Estimated Load:** X tickets

---

## 📊 Summary by Focus Area

**Primary Epic:** X% of capacity
- [Details]

**Critical Bugs:** X% of capacity
- [Details]

**Operational Health (NEW):** X% of capacity
- **BugSnag Cleanup:**
  - Categorize errors: Real bugs vs. noise
  - Silence known non-critical errors
  - Create tickets for real issues
  - Set up better alerting thresholds
- **Log Sorting:**
  - Review log levels (debug vs info vs error)
  - Add structured logging where missing
  - Remove verbose/unnecessary logs
  - Improve error context in logs

**Prep Work:** X% of capacity
- [Details]

---

## 🎯 Week Goals

**Must Complete:**
- [ ] Ship X tickets to production
- [ ] Fix X critical customer-facing bugs
- [ ] Reduce BugSnag noise by 50%
- [ ] Document log improvement plan

**Stretch Goals:**
- [ ] Complete additional epic work
- [ ] Start next sprint planning
- [ ] Implement log improvements

---

## 🔧 Operational Health Tasks

### BugSnag Noise Cleanup
**Owner:** Primarily David (backend) + Richard (frontend)

**Tasks:**
1. **Audit Current Errors (2 hours)**
   - Review top 20 errors in BugSnag
   - Categorize: Real bugs | Known issues | Noise | External

2. **Create Action Plan**
   - Real bugs → Create Jira tickets
   - Known issues → Document and silence if non-critical
   - Noise → Filter or silence
   - External → Update error handling

3. **Implementation**
   - Add error boundaries for known patterns
   - Update error handling to reduce false positives
   - Configure BugSnag filters

4. **Documentation**
   - Document what's silenced and why
   - Create runbook for error triage

### Log Sorting & Improvement
**Owner:** Primarily David (backend)

**Tasks:**
1. **Audit Current Logs (1-2 hours)**
   - Review production logs for noise
   - Identify overly verbose areas
   - Find missing context in errors

2. **Log Level Review**
   - Downgrade debug logs to appropriate levels
   - Ensure errors have full context
   - Add structured logging (JSON) where missing

3. **Implementation**
   - Update log statements
   - Add contextual information (user_id, request_id, etc.)
   - Remove or reduce verbose logs

4. **Monitoring Setup**
   - Set up better log aggregation queries
   - Create alerts for critical errors only

---

## 🚨 Risk Mitigation

**Risks:**
1. [Risk description]
2. Adding operational work may reduce feature velocity

**Mitigation:**
- [Mitigation strategies]
- Timebox operational work (4-6 hours total)
- Focus on high-impact quick wins

---

## 📈 Capacity Analysis

**Growth Team Size:** 3 engineers
- Richard: X tickets
- David: X tickets + operational work
- Robert: X tickets

**Total: ~X work items + operational health tasks**

---

## 📝 Notes

**Definitions:**
- **BugSnag Noise:** Errors logged that aren't actionable or are false positives
- **Log Sorting:** Organizing logs by importance and reducing verbosity
- **Operational Health:** Work that improves system observability and reduces on-call burden

**Success Metrics:**
- BugSnag error volume reduced by 50%
- Critical errors clearly identified
- Log volume reduced or better organized
- Team spends less time debugging noise

---

**Template Version:** 1.0
**Last Updated:** 2026-01-24
