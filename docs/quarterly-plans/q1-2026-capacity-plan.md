# Q1 2026 Capacity Planning - Growth & Engagement Teams

**Planning Period:** January 1 - March 31, 2026 (Q1 2026)
**Teams:** Growth (GRO) + Engagement (CE)
**Total Engineering Capacity:** 7 engineers
**Planning Date:** January 24, 2026

---

## 📊 Executive Summary

**Q1 2026 Focus:**
- **Growth Team:** Self-Serve Estimates launch (critical 1/29), HELOC Opt-In optimization, React 19 upgrade prep
- **Engagement Team:** Login SMS completion, HO Dashboard improvements, customer experience optimization
- **Shared Priorities:** Bug debt reduction, operational health improvements, team capacity optimization

**Key Risks:**
- GRO-1211 (Self-Serve Estimates) critical 1/29 deadline - single point of failure (Richard)
- Pratheesh capacity split between GRO and CE - potential bottleneck
- Login SMS scope unclear - may impact CE Q1 deliverables
- React 19 upgrade scope may be larger than anticipated

---

## 🎯 Q1 2026 Strategic Priorities

### Growth Team (GRO) Priorities

**Source:** Product Features data curated from 1H slide engineering deck

**Completed/Near Complete (January):**

1. **Self-Serve Updated Estimates on Dashboard** (XS, P0) **⚠️ CRITICAL**
   - **Timeline:** Jan 29, 2026 (reduced scope) - **CANNOT MISS**
   - **Owner:** Richard Collins
   - **Status:** ✅ Reduced scope to not display multiple offer dropdowns, show exact amount in tasks
   - **Slack:** #proj-self-serve-offer-estimate
   - **Notes:** Jan 15, 2026 scope reduction approved

2. **Partner Info Pass to Voice AI** (XS, P1) - [GRO-1196](https://pointdf.atlassian.net/browse/GRO-1196)
   - **Timeline:** Jan 15, 2026 (completed)
   - **Owner:** David Conger
   - **Status:** ✅ Completed - Need configuration on Feather side

3. **Follow Up Voice AI Work** (XS, P1)
   - **Timeline:** Jan 9, 2026
   - **Owner:** David Conger
   - **Status:** ✅ 2/3 outstanding items completed
   - **Items:** Change Feather outbound PQ call delay to 5 minutes ([GRO-1252](https://pointdf.atlassian.net/browse/GRO-1252)), Editable delays, Expansion to HELOC-ineligible leads

4. **What You Get Calculator** (XS, P1) - [GRO-1180](https://pointdf.atlassian.net/browse/GRO-1180)
   - **Timeline:** Jan 29, 2026
   - **Owner:** Tomas Herrera
   - **Status:** ✅ All in-scope work shipped Jan 26, 2026. One follow-up: [GRO-1279](https://pointdf.atlassian.net/browse/GRO-1279) (handle no debt payoff condition)
   - **Slack:** #proj-estimate-what-you-get

**In Progress/Upcoming (Feb-Mar):**

5. **Persistent Estimate Access on Dashboard** (XS?, P0?)
   - **Timeline:** TBD
   - **Owner:** TBD
   - **Status:** Need input from Josh - follow up meeting (Dec 17, 2025)
   - **Figma:** [Dashboard Pages](https://www.figma.com/design/TgiXhRny7bkGog8tVsFpnr/Pages---Dashboard?node-id=9614-4017&t=c6fhGktYQaviGYmJ-4)

6. **Promo Cap Productization** (TBD, P1)
   - **Timeline:** Mid February
   - **Owner:** Robert Cox
   - **Status:** Will pick up once SMS login is wrapped up (Jan 30, 2026)
   - **Slack:** #proj-promo-cap

7. **HELOC Rejection A/B Test (PQ Test)** (TBD, P1)
   - **Timeline:** TBD
   - **Owner:** TBD
   - **Status:** John Brewer is working on requirements (Dec 19, 2025)

8. **CRO: Continued IEA (Initial Estimate Acceptance) Focused Tests** (TBD, P2)
   - **Timeline:** Ongoing
   - **Owner:** TBD

9. **Single Page Estimates** (TBD, ??)
   - **Timeline:** TBD
   - **Owner:** TBD

10. **CRO: Partner Channel Enhancements** (TBD, P2)
    - **Timeline:** TBD
    - **Owner:** TBD

**Technical Roadmap (P0-P2):**

| Item | Why Important | T-shirt | Priority | Timeline |
|------|---------------|---------|----------|----------|
| **Improve QA Env Testing** | Daily productivity slow down | S | P0 | Feb-Mar 2026 |
| **Upgrade to React 19** | We've done tons of work, push to finish line | S | P0 | March 2026 (may extend to Q2) |
| **Develop Alert Guidelines** | Noise from Bugsnag/stdlog/Cloudwatch/Coralogix making tools not useful | S | P1 | Q1-Q2 2026 |
| **Cleanup Deprecated Feature Flags** | Difficult to search through | S | P2 | Q2 2026 |
| **Convert UI Tests to Playwright/Cosmos** | Reduce test time, improve accuracy | M | P2 | Q2 2026 |

---

### Engagement Team (CE) Priorities

**Source:** Product Features data curated from 1H slide engineering deck

**Completed/Near Complete (January):**

1. **HEI Application Changes** (TBD, P0)
   - **Timeline:** Released Jan 20, 2026
   - **Owner:** Dylan Oliver
   - **QA:** Jonathan Cole
   - **Status:** ✅ All dev work wrapped up on CE Jan 9, small task pending for UW, QA started
   - **Slack:** #application-improvements-q2-2025

**In Progress (January-February):**

2. **Login via SMS** (BE: XS, FE: S, P0) - [PRD](link)
   - **Timeline:** Pending Twilio approval (3-week SLA, submitted week of Jan 18, 2026)
   - **Owner:** Pratheesh Harikumar
   - **QA:** SungMin Hong
   - **Status:** ⚠️ BLOCKED - Awaiting Twilio approval
   - **Slack:** #proj-sms-login
   - **Risk:** External dependency blocking progress

**Upcoming (Feb-Mar):**

3. **Structured Follow-up Support** (??, P1) - [PRD: Structured Follow Ups](link)
   - **Timeline:** Feb-Mar 2026
   - **Owner:** TBD (CE team support for UW dependency)
   - **Status:** Reviewed initial requirements with Glen (Dec 17, 2025)
   - **Slack:** #proj-structured-follow-up
   - **Dependency:** Workflow team (Glen)
   - **Description:** Support for automated follow-up generation from Underwrite, multi-document requests, conditional question flows

4. **Dashboard Status Updates** (??, P1) - **(Mainly AI team?)**
   - **Timeline:** TBD
   - **Owner:** TBD (Joint effort with AI team)
   - **Status:** Need input from Josh - follow up meeting (Dec 17, 2025)
   - **Dependency:** Olivia and Angelique (weekly digest work)
   - **Point of Contact:** Josh Hohman

5. **Persistent Estimate Access on Dashboard** (XS?, P0?)
   - **Timeline:** TBD
   - **Owner:** TBD
   - **Status:** Need input from Josh - follow up meeting (Dec 17, 2025)
   - **Point of Contact:** Josh Hohman
   - **Description:** Ensure homeowners can view accepted estimates on dashboard

6. **>90% Automated Identity Doc Verification + ID Fraud** (P? based on scope)
   - **Timeline:** TBD (Scoping phase)
   - **Owner:** TBD (Cross-functional, CE provides FE support)
   - **Status:** Initial discussion with Glen, need to draw the line on CE team's responsibility (Dec 17, 2025)
   - **Point of Contact:** Glen (Workflow Team)
   - **Description:** Centralized verification service + third-party vendor integration for fraud detection

**Technical Roadmap (P0):**

| Item | Why Important | T-shirt | Priority | Timeline |
|------|---------------|---------|----------|----------|
| **Convert Styled Components to CSS** | Deprecated package, prioritize Customer Portal (PDS) | L | P0 | Q1-Q2 2026 |

**Customer-Facing Bugs (Week of 1/27):**
- CE-3865: HO Funding date on dashboard showing past date (High) - Dylan
- CE-3946: HO unable to get to dashboard, stuck in loop (High) - Pratheesh
- CE-3923: Docket duplicate logic fails with space/hyphen (Medium) - Daniel
- CE-3925: HO name is blank in HO application (Medium) - Daniel
- CE-3926: HO Dashboard timeline messaging incorrect (Medium) - Dylan

---

## 👥 Team Capacity Analysis - Q1 2026

### Q1 Timeline Context
- **Q1 Total:** 13 weeks (January 1 - March 31, 2026)
- **Weeks Elapsed:** ~4 weeks (as of January 27, 2026)
- **Weeks Remaining:** ~9 weeks (February 3 - March 31, 2026)

### Growth Team (GRO)
**Total Q1 Capacity:** 4 engineers × 13 weeks × 40 hours = 2,080 hours
**Remaining Q1 Capacity:** 4 engineers × 9 weeks × 40 hours = 1,440 hours

| Engineer | Role | Q1 Focus Areas | Capacity Notes |
|----------|------|---------------|----------------|
| **Richard Collins** | Full-stack Frontend | GRO-1211 (Jan), GRO-1189 prep (Feb-Mar), Code reviews | At capacity - critical for 1/29 deadline |
| **David Conger** | Backend | Bug fixes, Operational health, Backend support for epics | Full capacity - bug fixes and operational focus |
| **Tomas Herrera** | Full-stack | "What You Get" section, Customer bugs, Epic support | Full capacity - feature work and bugs |
| **Robert Cox** | Design + Frontend | GRO-1269 (Feb), GRO-1246 (Feb-Mar), GRO-1211 support (Jan) | Good capacity - design lead, minimal CE involvement |

**Shared Resources:**
- **Pratheesh Harikumar:** ~40-50% GRO capacity (architecture, code reviews, technical leadership)

**Q1 Capacity Allocation:**
- **Epics:** 60% (GRO-1211, GRO-1269, GRO-1246, GRO-1189)
- **Bugs:** 25% (Customer-facing issues, critical fixes)
- **Operational:** 10% (BugSnag, logs, technical debt)
- **Planning/Reviews:** 5% (Code reviews, planning, retrospectives)

### Growth Team - FE/BE Capacity Breakdown (Remaining Q1)

| Skill | Total Hours/Week | Weeks Remaining | Total Remaining Hours | Committed Hours | Available Hours | Available % |
|-------|------------------|-----------------|----------------------|-----------------|-----------------|-------------|
| **Frontend (FE)** | 94.4 hrs | 9 weeks | 850 hrs | ~510 hrs (60% epics) | **340 hrs** | **40%** |
| **Backend (BE)** | 81.6 hrs | 9 weeks | 734 hrs | ~440 hrs (60% epics) | **294 hrs** | **40%** |
| **Total** | 176 hrs | 9 weeks | 1,584 hrs | ~950 hrs (60% epics) | **634 hrs** | **40%** |

**Engineer Breakdown:**
- **Richard Collins** (Full-stack FE): 32 hrs FE, 8 hrs BE per week → **80% FE, 20% BE**
- **David Conger** (Backend): 0 hrs FE, 40 hrs BE per week → **0% FE, 100% BE**
- **Tomas Herrera** (Full-stack): 20 hrs FE, 20 hrs BE per week → **50% FE, 50% BE**
- **Robert Cox** (Design + FE): 36 hrs FE, 4 hrs BE per week → **90% FE, 10% BE**
- **Pratheesh** (Staff, 40% GRO): 6.4 hrs FE, 9.6 hrs BE per week → **40% FE, 60% BE**

**Committed Capacity (Jan-Mar 2026):**
- GRO-1211 (Self-Serve Estimates): ~160 hrs (completed by 1/29)
- GRO-1269 (HELOC Opt-In): ~320 hrs FE-heavy (Feb)
- GRO-1246 (Follow Up with Self Serve): ~280 hrs FE-heavy (Feb-Mar)
- GRO-1189 (React 19 Upgrade): ~250 hrs FE-heavy (Mar, may extend to Q2)
- Bugs + Operational: ~390 hrs (25% bugs, 10% operational, 5% reviews)

**Key Insights:**
- ⚠️ **FE capacity is tight** - 60% committed to epics, 40% remaining for bugs/operational
- ✅ **BE capacity is good** - David and Tomas provide solid backend support
- 🎯 **340 hrs FE available** for unplanned work, bug fixes, and operational health
- 🎯 **294 hrs BE available** for unplanned work, bug fixes, and operational health

---

### Engagement Team (CE)
**Total Q1 Capacity:** 3 engineers × 13 weeks × 40 hours = 1,560 hours
**Remaining Q1 Capacity:** 3 engineers × 9 weeks × 40 hours = 1,080 hours

| Engineer | Role | Q1 Focus Areas | Capacity Notes |
|----------|------|---------------|----------------|
| **Dylan Oliver** | Frontend, Team Lead | Login SMS (Jan), HO Dashboard (Feb-Mar), Team leadership | Full capacity - team lead responsibilities |
| **Daniel Cardenas** | Full-stack, Frontend-heavy | Login SMS (Jan), Follow-up prep (Feb), Bug fixes | Full capacity - new to team (joined Jan 2026) |
| **Robert Cox** | Design + Frontend | Minimal CE involvement - GRO priorities take precedence | Minimal capacity - focus on GRO |

**Shared Resources:**
- **Pratheesh Harikumar:** ~50-60% CE capacity (architecture, high-priority bugs, technical leadership)
- **Robert Cox:** ~5-10% CE capacity (critical design needs only)

**Q1 Capacity Allocation:**
- **Epics/Features:** 50% (Login SMS, Follow-up work, Dashboard improvements)
- **Bugs:** 35% (Customer-facing issues, HO Dashboard fixes)
- **Planning/Prep:** 10% (Requirements gathering, technical design)
- **Reviews/Support:** 5% (Code reviews, mentorship)

### Engagement Team - FE/BE Capacity Breakdown (Remaining Q1)

| Skill | Total Hours/Week | Weeks Remaining | Total Remaining Hours | Committed Hours | Available Hours | Available % |
|-------|------------------|-----------------|----------------------|-----------------|-----------------|-------------|
| **Frontend (FE)** | 79.4 hrs | 9 weeks | 715 hrs | ~358 hrs (50% epics) | **357 hrs** | **50%** |
| **Backend (BE)** | 26.6 hrs | 9 weeks | 239 hrs | ~120 hrs (50% epics) | **119 hrs** | **50%** |
| **Total** | 106 hrs | 9 weeks | 954 hrs | ~478 hrs (50% epics) | **476 hrs** | **50%** |

**Engineer Breakdown:**
- **Dylan Oliver** (Frontend, Team Lead): 40 hrs FE, 0 hrs BE per week → **100% FE, 0% BE**
- **Daniel Cardenas** (Full-stack, FE-heavy): 28 hrs FE, 12 hrs BE per week → **70% FE, 30% BE**
- **Robert Cox** (Design + FE, 5% CE): 1.8 hrs FE, 0.2 hrs BE per week → **90% FE, 10% BE**
- **Pratheesh** (Staff, 60% CE): 9.6 hrs FE, 14.4 hrs BE per week → **40% FE, 60% BE**

**Committed Capacity (Jan-Mar 2026):**
- Login via SMS: ~200 hrs FE-heavy (Jan, pending Twilio approval)
- Structured Follow-up Support: ~120 hrs FE-heavy (Feb-Mar, PRD in progress)
- HO Dashboard bugs: ~100 hrs FE-heavy (Jan-Feb, 5 customer-facing bugs)
- Dashboard Status Updates: TBD (dependency on AI team)
- Bugs + Operational: ~158 hrs (35% bugs, 10% planning, 5% reviews)

**Key Insights:**
- ⚠️ **BE capacity is constrained** - Only Daniel (12 hrs) and Pratheesh (14.4 hrs) provide BE support
- ✅ **FE capacity is good** - Dylan, Daniel, and Pratheesh provide solid frontend coverage
- 🎯 **357 hrs FE available** for unplanned work, bug fixes, and operational health
- 🎯 **119 hrs BE available** for unplanned work, bug fixes, and operational health
- ⚠️ **Login SMS blocked** - Pending Twilio approval (3-week SLA, submitted week of 1/18)

---

## 📅 Q1 2026 Timeline & Milestones

### January 2026

**Week of 1/6:**
- Planning and priority setting for Q1
- GRO-1211 (Self-Serve Estimates) sprint continues
- Login SMS remaining work audit

**Week of 1/13:**
- GRO-1211 development continues
- Login SMS completion work
- GRO-1269 (HELOC Opt-In) design work begins (Robert)

**Week of 1/20:**
- GRO-1211 final push for 1/29 deadline
- GRO-1275 (Release Plan) sign-offs in progress
- CE bug fixes (5 customer-facing bugs)

**Week of 1/27:** ⚠️ **CRITICAL WEEK**
- **1/29: GRO-1211 MUST SHIP TO PRODUCTION**
- Login SMS completion
- CE Follow-up work requirements gathering

---

### February 2026

**Week of 2/3:**
- GRO-1211 post-launch monitoring and bug fixes
- GRO-1269 (HELOC Opt-In) design finalization
- CE Follow-up work technical design

**Week of 2/10:**
- GRO-1269 (HELOC Opt-In) implementation begins
- GRO-1246 (Follow Up with Self Serve) design work
- CE HO Dashboard improvements

**Week of 2/17:**
- GRO-1269 (HELOC Opt-In) development continues
- GRO-1246 (Follow Up with Self Serve) design finalization
- CE customer experience optimization work

**Week of 2/24:**
- GRO-1269 (HELOC Opt-In) completion and release
- GRO-1246 (Follow Up with Self Serve) implementation begins
- CE dashboard improvements continue

---

### March 2026

**Week of 3/3:**
- GRO-1246 (Follow Up with Self Serve) development continues
- GRO-1189 (React 19 Upgrade) planning and prep work
- CE customer experience optimization

**Week of 3/10:**
- GRO-1246 (Follow Up with Self Serve) completion and release
- GRO-1189 (React 19 Upgrade) technical spike and planning
- CE feature work and bug fixes

**Week of 3/17:**
- GRO-1189 (React 19 Upgrade) begins (if ready)
- Bug debt reduction across both teams
- Q1 retrospective planning

**Week of 3/24:**
- GRO-1189 (React 19 Upgrade) continues (may extend into Q2)
- Bug fixes and operational health
- Q2 planning begins

**Week of 3/31:**
- Q1 completion and retrospective
- Q2 planning finalization
- Team capacity analysis for Q2

---

## 🚨 Q1 Risk Analysis & Mitigation

### Critical Risks

**1. GRO-1211 (Self-Serve Estimates) - 1/29 Deadline** ⚠️
- **Risk Level:** CRITICAL
- **Impact:** Business-critical launch, cannot miss deadline
- **Owner:** Richard Collins (sole engineer)
- **Mitigation:**
  - Daily check-ins on progress
  - Robert available as backup
  - Defer all non-essential work for Richard
  - GRO-1275 release plan sign-offs tracked closely
  - Escalate blockers immediately

**2. Pratheesh Capacity Split (GRO + CE)**
- **Risk Level:** HIGH
- **Impact:** Bottleneck for both teams, architecture decisions delayed
- **Mitigation:**
  - Document capacity split weekly (50-60% CE, 40-50% GRO)
  - Prioritize CE-3946 (customer-blocking bug) in January
  - Daily coordination between GRO and CE leads
  - Consider hiring additional staff engineer in Q2

**3. Login SMS Scope Unknown (CE)**
- **Risk Level:** MEDIUM
- **Impact:** CE Q1 deliverables at risk, follow-up work delayed
- **Mitigation:**
  - Dylan to complete scope audit immediately (1/27)
  - Defer follow-up work if Login SMS scope is large
  - Consider extending timeline into early February if needed

**4. React 19 Upgrade Scope Uncertainty (GRO)**
- **Risk Level:** MEDIUM
- **Impact:** May spill into Q2, delay other GRO initiatives
- **Mitigation:**
  - Complete technical spike and planning in March
  - Break into smaller milestones
  - Consider extending into Q2 if needed
  - Don't commit to hard deadline until scope is clear

**5. Robert Overload (Shared GRO + CE)**
- **Risk Level:** MEDIUM
- **Impact:** Design bottleneck for both teams
- **Mitigation:**
  - Focus Robert on GRO priorities (90-95% capacity)
  - Only involve for critical CE design needs
  - Consider hiring additional designer in Q2

**6. Customer-Facing Bug Volume**
- **Risk Level:** MEDIUM
- **Impact:** Feature work delayed, team morale affected
- **Mitigation:**
  - Maintain 25-35% capacity for bug fixes
  - Prioritize High priority bugs immediately
  - Daily review of bug dashboards
  - Track bug trends and root causes

---

## 📊 Q1 Success Metrics

### Growth Team (GRO)

**Epic Completion:**
- ✅ GRO-1211 (Self-Serve Estimates) shipped to production by 1/29
- ✅ GRO-1269 (HELOC Opt-In) completed by end of February
- ✅ GRO-1246 (Follow Up with Self Serve) completed by mid-March
- 🎯 GRO-1189 (React 19 Upgrade) planning complete, implementation started (may extend to Q2)

**Quality Metrics:**
- ✅ All release plans have mandatory sign-offs (QA, Analytics)
- ✅ BugSnag noise reduced by 50% by end of Q1
- ✅ Production logs improved and structured
- ✅ No critical bugs in production for more than 48 hours

**Team Health:**
- ✅ No engineer over 110% capacity for more than 1 week
- ✅ Richard successfully delivers GRO-1211 without burnout
- ✅ Team velocity maintained or improved throughout Q1

---

### Engagement Team (CE)

**Epic Completion:**
- ✅ Login SMS work completed by end of January
- ✅ 5 customer-facing bugs resolved (CE-3865, CE-3946, CE-3923, CE-3925, CE-3926)
- ✅ Follow-up work requirements gathered and technical design complete
- ✅ HO Dashboard improvements shipped by end of February

**Quality Metrics:**
- ✅ Customer-facing bug count reduced by 40% by end of Q1
- ✅ HO Dashboard customer satisfaction improved
- ✅ No customer-blocking bugs open for more than 24 hours

**Team Health:**
- ✅ Dylan successfully onboards and mentors Daniel
- ✅ Daniel productive on CE codebase by end of Q1
- ✅ Pratheesh capacity balanced between GRO and CE

---

## 🔄 Resource Rebalancing Strategy

### If GRO Falls Behind Schedule:
1. Pull Robert into implementation work (reduce design capacity)
2. Defer GRO-1189 (React 19) to Q2 entirely
3. Pratheesh increases GRO capacity to 60-70%
4. Tomas can shift from "What You Get" to epic support

### If CE Falls Behind Schedule:
1. Defer follow-up work to Q2
2. Focus on Login SMS and High priority bugs only
3. Pratheesh increases CE capacity to 70-80%
4. Robert provides minimal design support if absolutely critical

### If Pratheesh Is Overloaded:
1. CE-3946 and customer-blocking bugs take absolute priority
2. GRO and CE leads can handle non-critical architecture discussions
3. Distribute code reviews to other senior engineers
4. Consider contractor or additional hire in Q2

### If Customer-Facing Bugs Spike:
1. Shift 10% capacity from epics to bugs immediately
2. Daily triage of bug dashboard
3. Identify and fix root causes, not just symptoms
4. Consider dedicated bug rotation for 1-2 weeks

---

## 📈 Capacity Trends & Insights

### January 2026 Capacity Snapshot

**Current State (Week of 1/27):**
- GRO: 60% epic (GRO-1211), 30% bugs, 10% operational
- CE: 40% Login SMS, 30% bugs, 20% follow-up prep, 10% reviews

**Utilization:**
- Richard: 110% (at risk - critical deadline)
- David: 100% (full capacity)
- Tomas: 100% (full capacity)
- Robert: 95% (good capacity, primarily GRO)
- Dylan: 100% (full capacity, team lead)
- Daniel: 90% (learning curve, ramping up)
- Pratheesh: 110% (shared across teams - at risk)

**Red Flags:**
- Richard and Pratheesh over capacity
- Login SMS scope unknown
- 8 customer-facing bugs across teams

---

## 📝 Q1 Planning Recommendations

### For Q2 Planning:

1. **Hire Additional Staff Engineer:**
   - Reduce Pratheesh overload
   - Support both GRO and CE architecture needs
   - Timeline: Start recruiting in February, onboard in Q2

2. **Hire Additional Designer (if budget allows):**
   - Reduce Robert overload across GRO and CE
   - Dedicated design capacity for CE
   - Timeline: Evaluate need by end of Q1

3. **Epic Ownership Model:**
   - Avoid single-engineer ownership for critical deadlines
   - Pair programming on critical epics
   - Knowledge sharing and documentation

4. **Scope Management:**
   - Complete detailed scoping before committing to timelines
   - Use technical spikes for uncertain epics
   - Buffer time for unknowns (add 20-30% to estimates)

5. **Bug Management:**
   - Root cause analysis for recurring bugs
   - Dedicated bug rotation (1 engineer per team per week)
   - Monthly bug debt reduction sprints

6. **Operational Health:**
   - Continue BugSnag and log improvements
   - Invest in monitoring and alerting
   - Automated testing and CI/CD improvements

---

## 🎯 Q1 Key Deliverables Summary

**January:**
- ✅ GRO-1211 (Self-Serve Estimates) shipped to production (1/29)
- ✅ Login SMS work completed
- ✅ 5 CE customer-facing bugs resolved
- ✅ GRO-1269 and GRO-1246 design work in progress

**February:**
- ✅ GRO-1269 (HELOC Opt-In) completed and shipped
- ✅ GRO-1246 (Follow Up with Self Serve) design finalized, implementation started
- ✅ CE HO Dashboard improvements shipped
- ✅ BugSnag noise reduced by 30%

**March:**
- ✅ GRO-1246 (Follow Up with Self Serve) completed and shipped
- ✅ GRO-1189 (React 19 Upgrade) planning complete, implementation started
- ✅ CE customer experience optimization work
- ✅ Q1 retrospective and Q2 planning complete

---

**Plan Created:** January 24, 2026
**Plan Owner:** Wei Huang
**Review Cadence:** Monthly (end of Jan, Feb, Mar)
**Next Review:** January 31, 2026
