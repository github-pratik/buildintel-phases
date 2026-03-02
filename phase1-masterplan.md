# BuildIntel — Phase 1: Strategy & Master Plan
**GPT Memory Context File | Last Updated: March 2026**

---

## 🎯 What This Phase Is

Phase 1 is the complete strategic foundation for BuildIntel — an AI-powered news intelligence platform covering Architecture, Construction, Engineering & Manufacturing (ACEM) with an AI-first editorial lens.

This file gives any GPT/AI assistant full context to continue planning, building, or advising on this project.

---

## 📌 Core Concept

**BuildIntel** = The first news publication that covers all four ACEM sectors (Architecture, Construction, Engineering, Manufacturing) under one AI-first editorial lens, with automated content creation, a human editorial gate, and a public MCP server for AI agent integration.

**The gap being filled:** Construction Dive covers construction. ENR covers engineering. AEC Magazine covers architecture. Manufacturing Dive covers manufacturing. Nobody covers all four under one AI-first roof.

---

## 🏢 Target Audience

1. **Industry professionals / engineers** — practical, peer-to-peer, technically literate
2. **Business leaders / investors** — market-informed, data-rich, forward-looking
3. **General public / policymakers** — accessible expertise, why it matters framing

---

## 📰 Editorial Structure

### 5 Primary Sections
- Architecture & Design (generative design, Neural CAD, AI rendering)
- Construction & Building (BIM, robotics, computer vision, safety monitoring)
- Engineering & Simulation (digital twins, AI-powered CAD/CAE, Siemens-NVIDIA)
- Manufacturing & Automation (predictive maintenance, cobots, smart factories)
- Policy & Regulation (EU AI Act, NIST RMF, OSHA gaps, CHIPS Act, state laws)

### 6 Cross-Cutting Beats
- Workforce & Jobs
- Deals & Funding
- Sustainability & ESG
- Safety & Ethics
- Robotics & Autonomy
- Digital Twins

---

## 📊 Market Data (Key Numbers)

- AI-in-construction market: $4.96B (2025) → $14.72B (2030)
- AI in manufacturing: $8.57B → $230.95B by 2034
- Digital twins market: $23.4B → $219.6B by 2033
- Construction tech funding Q2 2025: $3.96B (68% AI/ML)
- EU AI Act high-risk obligations: **August 2, 2026** (major deadline)
- 1,208 AI bills introduced in US states in 2025, 145 enacted

---

## 🔑 10 Competitive Gaps Identified

1. No publication covers all four ACEM sectors under AI
2. No AI-first physical industry publication (like TechCrunch for software)
3. No AI policy + ACEM practice intersection publication
4. No cross-pollination coverage (learnings from one sector applied to another)
5. No independent AI tool assessments for ACEM
6. No full startup/investment landscape tracker
7. No workforce transformation coverage across sectors
8. No sustainability + AI cross-sector publication
9. No international comparative ACEM AI coverage
10. No newsletter-native modern brand for physical-industry AI

---

## 💰 Revenue Streams

1. **Pro API / MCP Access** — $49/mo for companies and AI agents
2. **Native Ad Network** — $40–80 CPM (B2B audience: Autodesk, Siemens, Caterpillar)
3. **Newsletter Monetization** — 5 newsletter products via Beehiiv (0% commission)
4. **Paid Subscriptions** — Premium "Policy Wire" tier
5. **Events** — Annual "AI + Built World" summit
6. **Data Reports** — Quarterly industry data reports

---

## 📧 5 Newsletter Products

1. **The ACEM AI Briefing** (Daily Mon-Fri) — flagship, 5-7 items, Axios format
2. **Deep Build** (Weekly Thursday) — long-form feature + data snapshot
3. **Policy Wire** (Weekly Tuesday) — regulatory developments exclusively
4. **Deal Flow** (Weekly Monday) — investment activity, funding table
5. **Tools & Tech** (Biweekly) — product launches, tool comparisons

---

## 🗺️ URL Architecture

```
/architecture/2026/03/article-slug/    ← section articles
/construction/2026/03/article-slug/
/engineering/2026/03/article-slug/
/manufacturing/2026/03/article-slug/
/policy/2026/03/article-slug/
/topic/eu-ai-act-construction/         ← topic cluster pages
/data/ai-adoption-tracker/             ← live data dashboards
/api/v1/articles?sector=construction   ← public REST API
/llms.txt                              ← machine-readable manifest
```

---

## 📈 SEO Strategy (3 Tiers)

### Tier 1 — Zero Competition (Start Day 1)
- "EU AI Act construction compliance" — nearly zero quality competitors
- "OSHA AI regulations manufacturing"
- "AI construction site safety monitoring"
- "Physical AI construction 2026"
- "CHIPS Act construction workers"

### Tier 2 — Pillar Authority (Months 3–9)
- "AI in construction" pillar + 8-10 cluster articles
- "AI in architecture" pillar
- "Digital twins" cross-sector cluster

### Tier 3 — Broad Terms (Months 9–18)
- "AI construction news"
- "Construction technology news"
- "AI manufacturing news"

---

## 🏗️ 4 Data-Driven Features (Differentiators)

1. **AI Adoption Tracker** — quarterly dashboard, adoption rates by company/sector/geography
2. **AI Regulation Map** — interactive global visualization, EU + US + state level
3. **ACEM AI Funding & Deal Tracker** — searchable database, weekly updates
4. **Expert Braintrust Panels** — weekly question to 5-8 curated industry experts

---

## 🖥️ GovExec UI Analysis — What We Copy, What We Fix

### Copy from GovExec
- Editorial hierarchy: large hero → skybox → article grid → rail stories
- Section tag + byline + timestamp system
- Clean navigation structure

### Fix vs GovExec
- Remove auto-rotating carousel (UX dark pattern)
- Fix mobile navigation (bottom tab bar instead of hamburger)
- Add dark mode (GovExec has none)
- Add Command-K search (GovExec has basic search only)
- Fix load speed — target LCP <1.5s vs GovExec ~3.2s
- Add AI-readable data layer (GovExec has zero)
- Add live data dashboards (GovExec dashboards are manually updated)

---

## 🚀 Launch Phases (from Master Plan)

### Phase 1 — Foundation (Weeks 1–4)
Core site live, 5 section pages, 50 hand-written articles, newsletter signup, Google News submission, LLMs.txt

### Phase 2 — Data Pipeline (Weeks 5–8)
RSS/API ingestion, Claude relevance classifier, auto-article generation, editor review dashboard, breaking news banner

### Phase 3 — Growth Layer (Weeks 9–14)
All 5 newsletters live, AI Adoption Tracker, Funding Deal Tracker, 5 pillar SEO pages

### Phase 4 — AI Intelligence (Weeks 15–20)
All 5 AI agents live, public REST API /v1, AI Regulation Map, Podcast launch

### Phase 5 — MCP + Community (Weeks 21–28)
MCP server, WebSocket stream, community Slack, annual summit, Pro API tier

---

## 📋 Key Decisions Made in Phase 1

| Decision | Choice | Reason |
|---|---|---|
| CMS | Sanity.io (headless) | API-first, multi-channel, editor-friendly |
| Newsletter | Beehiiv | Morning Brew DNA, 0% commission, ad network |
| Website framework | Next.js 15 | ISR for fast publishing, SEO-perfect |
| Agent builder | n8n (self-hosted) | Unlimited ops, Claude native, agent hierarchy |
| AI model | Claude API | Lower hallucination, Anthropic node in n8n |
| Memory store | Supabase | Persistent state, crash recovery |
| CDN | Cloudflare | Free, global, fast |
| Hosting | Vercel (frontend) + Railway (workers) | |

---

## ⏭️ Next Phase

**Phase 2 — Agent Orchestra & Data Flow**
Building the complete AI agent hierarchy: 15+ agents in n8n, Claude API connections, Memory Agent with Supabase, Hallucination Checker, full data pipeline from source to published article.

See: `phase2-agents.html` and `phase2-agents.md`
