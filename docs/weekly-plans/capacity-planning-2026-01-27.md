# Cross-Team Capacity Planning - Week of January 27, 2026

**Planning Period:** January 27 - January 31, 2026
**Teams:** Growth (GRO) + Engagement (CE)
**Total Engineering Capacity:** 7 engineers (4 GRO, 3 CE, 2 shared)

---

## 📊 Team Capacity Overview

### Growth Team (GRO)
**Total Capacity:** 4 engineers (160 hours/week @ 40hr each)

| Engineer | Primary Focus | Workload | Capacity Status |
|----------|--------------|----------|-----------------|
| **Richard Collins** | GRO-1211 (Self-Serve Estimates) - **CRITICAL 1/29** | 6-7 tickets + operational | **⚠️ At capacity** |
| **David Conger** | Bug fixes + Operational health | 3-4 bugs + 2 operational tasks | **Full capacity** |
| **Tomas Herrera** | "What You Get" + Customer bugs | 2-4 tickets | **Full capacity** |
| **Robert Cox** | GRO-1269 (HELOC Opt-In) + GRO-1246 design | 2-3 design tickets + reviews | **Good capacity** |

**Key Deliverable:** GRO-1211 MUST ship by 1/29 (CANNOT MISS)

---

### Engagement Team (CE)
**Total Capacity:** 3 engineers (120 hours/week @ 40hr each)

| Engineer | Primary Focus | Workload | Capacity Status |
|----------|--------------|----------|-----------------|
| **Dylan Oliver** | Login SMS + 2 bugs (CE-3865, CE-3926) | 4-6 tickets | **Full capacity** |
| **Daniel Cardenas** | Login SMS + 2 bugs + follow-up prep | 4-5 tickets | **Full capacity** |
| **Pratheesh Harikumar** | CE-3946 (High) + Architecture + GRO support | 3-4 tickets | **⚠️ Shared with GRO** |

**Key Deliverables:** Login SMS completion + 5 customer-facing bugs

---

## 🔄 Shared Resources Analysis

### Pratheesh Harikumar (Staff Engineer)
**Status:** Shared between GRO and CE

**GRO Commitments:**
- Staff-level technical guidance for GRO initiatives
- Architecture review and mentorship
- Code reviews for complex PRs
- **Time allocation:** ~40-50% (16-20 hours)

**CE Commitments:**
- CE-3946: HO unable to access dashboard (High priority) - **Customer-blocking**
- Architecture planning for follow-up work
- Technical leadership and mentorship
- Code reviews for complex PRs
- **Time allocation:** ~50-60% (20-24 hours)

**Capacity Risk:**
- ⚠️ **High risk**: Pratheesh is critical path for CE-3946 (High priority bug)
- **Mitigation:** CE-3946 takes priority this week due to customer impact
- **Coordination needed:** Daily sync between GRO and CE leads on Pratheesh's priorities

---

### Robert Cox (Design + Frontend)
**Status:** Primary GRO, minimal CE

**GRO Commitments (Primary):**
- GRO-1269: Increase HELOC Opt-In Rate (Design) - **Priority epic**
- GRO-1246: Follow Up Work with Self Serve Estimate (Design)
- Code reviews for GRO-1211 (critical 1/29 deadline)
- **Available for GRO-1211 implementation if Richard needs support**
- **Time allocation:** ~90-95% (36-38 hours)

**CE Commitments (Minimal):**
- Design review for CE initiatives (if critical need arises)
- Frontend code review support (if requested)
- **Time allocation:** ~5-10% (2-4 hours)

**Capacity Risk:**
- ✅ **Low risk**: Robert is heavily loaded with GRO work
- **Mitigation:** Only involve Robert for critical CE design needs
- **Priority:** GRO-1211 (1/29 deadline) takes absolute priority over CE work

---

## 📈 Workload Distribution Analysis

### Total Work Items by Team

**Growth Team (GRO):**
- Epic work: 6-7 tickets (GRO-1211 - Richard only)
- Feature work: 2-4 tickets (Tomas - "What You Get" section)
- Bug fixes: 3-4 tickets (David - customer-facing bugs)
- Design work: 2-3 tickets (Robert - GRO-1269, GRO-1246)
- Operational: 3 tasks (BugSnag audit, Log audit)
- **Total: ~16-21 work items**

**Engagement Team (CE):**
- Login SMS: Unknown # of tickets (Dylan, Daniel - scope TBD)
- Bug fixes: 5 tickets (CE-3865, CE-3946, CE-3923, CE-3925, CE-3926)
- Follow-up prep: Planning and requirements gathering (Daniel, Pratheesh)
- **Total: ~11-15 work items**

**Combined Total: ~27-36 work items across 7 engineers**

---

## ⚠️ Capacity Risks & Bottlenecks

### Critical Risks

1. **🚨 GRO-1211 (Self-Serve Estimates) - 1/29 Deadline**
   - **Risk Level:** CRITICAL
   - **Owner:** Richard (sole engineer on this epic)
   - **Status:** 6-7 tickets in flight, at capacity
   - **Mitigation:**
     - Robert available as backup if Richard is blocked
     - Daily check-ins on progress
     - Defer Richard's operational work (BugSnag audit) if needed
     - Escalate blockers immediately to team lead

2. **⚠️ Pratheesh Capacity Split (GRO + CE)**
   - **Risk Level:** HIGH
   - **Conflict:** CE-3946 (High priority bug) vs. GRO architecture needs
   - **Mitigation:**
     - CE-3946 takes priority this week (customer-blocking)
     - Communicate capacity daily between GRO and CE leads
     - Document capacity split: ~50-60% CE, ~40-50% GRO
     - Adjust GRO architecture work if CE-3946 takes longer

3. **⚠️ Login SMS Scope Unknown (CE)**
   - **Risk Level:** MEDIUM
   - **Issue:** Unknown number of remaining Login SMS tickets
   - **Mitigation:**
     - Dylan to audit and document all remaining work immediately (Monday)
     - If scope is large, defer follow-up prep work to next week
     - Prioritize bugs over follow-up prep if needed

4. **⚠️ Multiple Customer-Facing Bugs (Both Teams)**
   - **Risk Level:** MEDIUM
   - **Issue:** 8 total customer-facing bugs across both teams (3 GRO, 5 CE)
   - **Mitigation:**
     - Prioritize High priority bugs first: CE-3865, CE-3946
     - David and Daniel focus on Medium priority bugs
     - Daily review of bug dashboard for new escalations

---

## 🎯 Capacity Allocation by Priority

### Critical Work (Must Complete - 70% capacity)

**GRO:**
- GRO-1211 (Self-Serve Estimates) - Richard (60% of GRO capacity)
- Critical bugs: GRO-1129, GRO-1186, GRO-1192 - David, Tomas (20% of GRO capacity)

**CE:**
- Login SMS completion - Dylan, Daniel (40% of CE capacity)
- High priority bugs: CE-3865, CE-3946 - Dylan, Pratheesh (20% of CE capacity)

### Important Work (Should Complete - 20% capacity)

**GRO:**
- "What You Get" section - Tomas
- Design work: GRO-1269, GRO-1246 - Robert

**CE:**
- Medium priority bugs: CE-3923, CE-3925, CE-3926 - Daniel, Dylan
- Follow-up work prep - Daniel, Pratheesh

### Operational/Nice-to-Have (10% capacity)

**GRO:**
- BugSnag audit (GRO-1272) - David, Richard (defer if needed)
- Log audit (GRO-1274) - David

**CE:**
- Code reviews and mentorship
- Additional bugs beyond the 5 identified

---

## 📅 Daily Capacity Checkpoints

### Monday (Jan 27)
- [ ] Dylan: Audit and document all remaining Login SMS tickets
- [ ] Pratheesh: Document capacity split between GRO and CE teams
- [ ] Richard: GRO-1211 progress check - identify any blockers
- [ ] Dylan: Coordinate with Josh Hohman on CE-3865 and CE-3926 handoff

### Tuesday (Jan 28)
- [ ] Richard: GRO-1211 progress check - escalate if behind schedule
- [ ] Pratheesh: CE-3946 progress check
- [ ] Team leads: Review capacity split for Pratheesh based on CE-3946 complexity

### Wednesday (Jan 29) - **GRO-1211 DEADLINE**
- [ ] Richard: GRO-1211 MUST be complete and shipped to production
- [ ] Team: All mandatory sign-offs for GRO-1275 completed (QA, Analytics)
- [ ] CE team: Adjust priorities if Login SMS or bugs are falling behind

### Thursday (Jan 30)
- [ ] Review bug completion status across both teams
- [ ] Dylan: Login SMS completion status check
- [ ] Adjust Friday priorities based on week progress

### Friday (Jan 31)
- [ ] Weekly retrospective: Review completion and learnings
- [ ] Plan next week priorities based on what rolled over
- [ ] Document capacity insights for future planning

---

## 🔄 Resource Rebalancing Options

If capacity constraints arise during the week:

### If GRO-1211 is at risk (Critical):
1. Pull Robert into GRO-1211 implementation (frontend support)
2. Defer all of Richard's operational work (BugSnag audit)
3. David can provide backend support if needed
4. Tomas can help with code reviews to unblock Richard

### If CE is falling behind:
1. Defer follow-up work prep to next week (Daniel)
2. Focus Dylan and Daniel on Login SMS + High priority bugs only
3. Defer Medium priority bugs (CE-3923, CE-3925, CE-3926) if needed
4. Pratheesh can shift more time to CE if GRO architecture can wait

### If Pratheesh is overloaded:
1. CE-3946 (High priority bug) takes absolute priority
2. Dylan or Daniel can take on simpler architecture tasks
3. GRO team can defer non-critical architecture discussions
4. Code reviews can be distributed to other senior engineers

---

## 📊 Success Metrics

**Week Success = All Critical Work Complete:**

**GRO:**
- ✅ GRO-1211 shipped to production by 1/29 (CANNOT MISS)
- ✅ GRO-1275 release plan sign-offs complete (QA, Analytics)
- ✅ Critical bugs resolved: GRO-1129, GRO-1186, GRO-1192

**CE:**
- ✅ Login SMS work completed
- ✅ High priority bugs resolved: CE-3865, CE-3946
- ✅ 3/5 bugs resolved (at minimum)

**Capacity Health:**
- ✅ Pratheesh capacity balanced between GRO and CE
- ✅ No engineer over 110% capacity
- ✅ Robert focused on GRO priorities (minimal CE distraction)

---

## 📝 Capacity Planning Insights

**Strengths:**
- Clear priorities established (GRO-1211 is critical, CE Login SMS + bugs)
- Shared resources (Pratheesh, Robert) have defined boundaries
- Risk mitigation plans in place for capacity conflicts
- Daily checkpoints ensure early detection of capacity issues

**Challenges:**
- Richard is sole engineer on GRO-1211 (critical 1/29 deadline) - single point of failure
- Pratheesh split between two teams - potential bottleneck
- Login SMS scope unknown - could impact CE capacity
- 8 total customer-facing bugs across teams - high volume

**Recommendations for Next Week:**
- Avoid scheduling new critical work during week with hard deadlines
- Consider pairing on critical epics (avoid single-engineer ownership)
- Complete Login SMS scope audit earlier in planning process
- Track actual capacity split for Pratheesh to inform future planning

---

**Plan Created:** January 24, 2026
**Plan Owner:** Wei Huang
**Review Date:** January 31, 2026 (weekly retrospective)
