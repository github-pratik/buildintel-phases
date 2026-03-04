# BuildIntel — Phase 2: Agent Orchestra & Data Flow
**GPT Memory Context File | Status: 🟠 IN PROGRESS | Last Updated: March 2026**

---

## 🚀 Prototype-First Approach

**Rule:** Build using free tools only. No budget approval needed for the prototype. Prove the pipeline works, then ask the boss for the production budget.

**2-Week Target:** By end of Week 2 we have more than a prototype — Scout pulls real stories, Writer generates real articles, Publisher pushes to Ghost, Curator sends the newsletter. All automated. All free.

**Budget ask:** After the demo, we ask for ~$114/mo to go to full production.

---

## 📅 2-Week Sprint Plan

### Week 1 — Infrastructure

| Day | Task | Done |
|---|---|---|
| Day 1–2 | Deploy n8n (Railway free), Supabase project + 3 tables, Ghost local install. Connect all three. | [ ] |
| Day 3 | Build Scout Agent — fetch 10 RSS feeds → dedupe check → write to Supabase queue | [ ] |
| Day 4 | Build Scorer Agent — Claude Haiku scores ACEM relevance 0–100. ≥60 proceeds | [ ] |
| Day 5 | Build Writer Agent — Claude Haiku/Sonnet rewrites story in Semafor format → draft to Supabase | [ ] |

**Week 1 milestone:** Stories flow from internet → Supabase → AI-written drafts. Pipeline exists.

### Week 2 — Automation

| Day | Task | Done |
|---|---|---|
| Day 6–7 | Hallucination Checker (confidence ≥70 passes) + Publisher (Ghost Admin API → article live) | [ ] |
| Day 8 | SEO Agent (title, meta, slug per article) + Memory Agent (logs every action, crash recovery) | [ ] |
| Day 9 | Connect Beehiiv free + Curator Agent (5:30am cron → newsletter draft → auto send) | [ ] |
| Day 10 | Expand to 30+ RSS sources. Run full pipeline 24hrs. Review output. Fix edge cases. | [ ] |

**Week 2 milestone:** Full pipeline live. Articles publishing autonomously. Newsletter sending. Demo-ready.

---

## 🆓 Free Tools for Prototype

| Tool | Free Tier Used | Notes |
|---|---|---|
| **n8n** | Railway free (500hrs/mo) | Enough for prototype testing |
| **Ghost** | Local install | Same API code works on Ghost Pro when we upgrade |
| **Supabase** | Free tier — 500MB DB | Covers full prototype |
| **Beehiiv** | Free to 2,500 subscribers | Full functionality |
| **RSS + Gov APIs** | 40+ feeds free | Federal Register, EUR-Lex, GDELT, ArXiv |
| **Claude API** | $5 credit (~300 articles) | Only paid item — ask boss for this specifically |

---

## ✅ Decisions Locked in Phase 2

| Decision | Choice | Reason |
|---|---|---|
| Agent builder | **n8n (self-hosted on Railway)** | Unlimited ops, native Claude node, workflows trigger workflows |
| AI brain | **Claude API** | Haiku/Sonnet/Opus tiered by task cost |
| CMS | **Ghost** | Prototype local, upgrade to Ghost Pro after approval |
| vs Make.com | Rejected | ~$300+/mo at our operation volume |
| vs Zapier | Rejected | $400+/mo, no agent-to-agent triggering |
| Vibe coding | **Cursor + Claude Code CLI** | Describe workflows in English → code generated → import to n8n |
| Memory store | **Supabase (PostgreSQL)** | Persistent state, crash recovery, free tier sufficient |

---

## 🏗️ The Agent Hierarchy

### Level 0 — Human (Above All Agents)
- **You (Human Editor)** — Monitors pipeline. 20 min/day. No approval gate — agents publish autonomously.

### Level 1 — Orchestrator
- **🧠 Orchestrator Agent** — Runs every 60 min. Reads system state. Balances topic distribution.

### Semi Level — Safety & Infrastructure (Always Running)
- **⚡ Hallucination Checker** — Confidence score 0–100. Below 70 → back to Writer.
- **📦 Memory Agent** — Writes state to Supabase. Crash recovery. Deduplicates stories.
- **📊 Monitor Agent** — Checks system health every 10 min. Slack alert if any agent fails.

### Level 2 — Department Heads (5 agents)
- 🏗️ Construction Editor · 🏛️ Architecture Editor · ⚙️ Engineering Editor · 🏭 Manufacturing Editor · ⚖️ Policy Editor

### Level 3 — Worker Agents (5 agents)
- 🕷️ Scout · ✍️ Writer (Sonnet) · 🔍 SEO Agent (Haiku) · 📧 Curator · 🚀 Publisher

---

## 🔄 Complete Data Flow

```
WORLD (internet)
  ↓ [every 5 min]
🕷️ SCOUT — fetches 40+ RSS feeds, Gov portals, ArXiv
  ↓
📦 MEMORY CHECK — seen this URL before? skip if yes
  ↓ [new story]
🏗️ DEPT HEAD — scores relevance 0–100
  ↓ [score ≥60]
✍️ WRITER — Claude Sonnet, Semafor format
  ↓
⚡ HALLUCINATION CHECKER — confidence ≥70 passes
  ↓
🔍 SEO AGENT — title, meta, slug, keywords
  ↓ [auto-publish]
🚀 PUBLISHER — Ghost Admin API → article live
  ↓ [5:30am daily]
📧 CURATOR → Beehiiv → 6am newsletter send
```

---

## ⚡ Performance Targets

- Source → Published: **under 4 minutes**
- Daily auto-published articles: **15–25**
- Human editor daily time: **20 minutes**
- Newsletter send time: **6:00am daily**

---

## 💰 Costs — At The End

### Prototype (Now — No Approval Needed)
| Tool | Cost |
|---|---|
| n8n · Ghost (local) · Supabase · Beehiiv · RSS | Free |
| Claude API ($5 credit) | $5 one-off |
| **Prototype Total** | **~$5** |

### Full Production (Ask After Demo)
| Tool | Cost/mo |
|---|---|
| n8n Railway paid | ~$20 |
| Ghost Pro | ~$25 |
| Claude API full volume | ~$40 |
| Crunchbase Basic | ~$29 |
| Supabase + Beehiiv | Free |
| **Production Total** | **~$114/mo** |

**Ask strategy:** $5 now for prototype → demo to boss → ask $114/mo with proof it works.

---

## 📋 Open Tasks

- [ ] n8n deploy on Railway free tier
- [ ] Supabase schema — 3 tables: feeds, queue, published
- [ ] Ghost local install + Admin API key
- [ ] First 10 RSS feeds to connect
- [ ] Claude API key in n8n

---

## ⏭️ Next: Phase 3 — Website Design & UI
## ⏮️ Previous: Phase 1 — Strategy & Master Plan
