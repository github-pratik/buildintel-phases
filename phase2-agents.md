# IndustrialBriefs — Phase 2: Agent Orchestra & Data Flow
**Memory Context File | Status: 🟢 PHASE 2.1 COMPLETE | Last Updated: 2026-03-08**

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

## 📋 Open Tasks (Phase 2 Original)

- [x] n8n deploy on Railway free tier ✅
- [x] Supabase schema — `published` table created and verified ✅
- [ ] Ghost local install + Admin API key
- [x] First 10 RSS feeds → now 25 verified feeds ✅
- [x] Groq API key in n8n (using Groq LLaMA 3.3 instead of Claude) ✅

---

---

## 🟢 Phase 2.2 — Actual Build State & Execution Plan (2026-03-08)

> This section documents what is **actually deployed**, how agents execute in sequence, and what needs to be built next. Replaces the theoretical Phase 2 plan with ground truth.

---

### 🏗️ What Is Live Right Now

| Agent | n8n Workflow ID | Status | Trigger |
|-------|----------------|--------|---------|
| **WF1 — Scout Agent** | `N2HuAM6ThXrc4aGM` | ✅ Active | Every 6 hours |
| **WF2 — Writer Agent** | `LO93zvn51g2JG2sJ` | ✅ Active | Webhook (called by WF1) |
| **WF3 — Publisher Agent** | TBD | ⏳ Not built | Webhook (called by WF2) |
| **WF4 — Curator Agent** | TBD | ⏳ Not built | Cron daily 5:30am |

**Infrastructure:**
- n8n: `https://n8n-primary-production-e002.up.railway.app` ✅
- Supabase: `https://hcforutxssuhikfzylhe.supabase.co` ✅ (`published` table live)
- Groq LLaMA 3.3 70B: `https://api.groq.com/openai/v1/` ✅
- Ghost CMS: ⏳ Not set up yet
- Beehiiv: ⏳ Not set up yet

---

### 🔄 Full Agent Execution Flow (Current + Planned)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  EVERY 6 HOURS — Automatic trigger
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────┐
│  WF1 — SCOUT AGENT                         [LIVE ✅]   │
│                                                         │
│  Schedule Trigger (every 6h)                            │
│    ↓                                                    │
│  25 RSS Feeds (parallel fetch)                          │
│  ┌──────────────────────────────────────┐               │
│  │ Tier 1: Construction Dive, AEC Mag,  │               │
│  │  MIT Tech Review, VentureBeat AI,    │               │
│  │  AI Business, Smart Cities Dive...   │               │
│  │ Tier 2: ArchDaily, Mfg Dive, Dezeen  │               │
│  │ Tier 3: TechCrunch, Robot Report...  │               │
│  └──────────────────────────────────────┘               │
│    ↓ (all outputs merge into one batch)                 │
│  Filter & Score                                         │
│  - Relevance score 0–20+ per article                    │
│  - Keywords: BIM, AI, contech, modular...               │
│  - Recency bonus: <6h=+4, <24h=+2                      │
│  - Source tier bonus: T1=+3, T2=+1.5, T3=+0.5          │
│  - Threshold ≥ 4 to pass                               │
│  - Output: top 30 articles sorted by score              │
│    ↓                                                    │
│  Supabase Dedup Check                                   │
│  - Batch IN query on `published.source_url`             │
│  - Drops articles already published                     │
│    ↓                                                    │
│  Scrape Full Article (per new article)                  │
│  - HTTP GET article URL                                 │
│  - Extract <article>/<main>/<body>, strip ads/nav       │
│  - Pull og:image + author byline                        │
│  - Up to 4,000 chars of real content                    │
│    ↓                                                    │
│  HTTP POST → /webhook/writer-agent (WF2)                │
│  Payload: { title, link, source, category, score,       │
│             pubDate, snippet, fullContent, image,        │
│             author, scrapedOk }                         │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│  WF2 — WRITER AGENT                        [LIVE ✅]   │
│                                                         │
│  Webhook Trigger: POST /webhook/writer-agent            │
│    ↓                                                    │
│  Parse Article JSON                                     │
│  - Validates required fields: title, link, fullContent  │
│    ↓                                                    │
│  Groq LLaMA 3.3 70B API Call                           │
│  - System: Senior journalist, Semafor format            │
│  - Prompt: title + source + fullContent (4000 chars)    │
│  - Returns JSON: { title, body, summary, tags }         │
│    ↓                                                    │
│  Valid Article? (Filter node)                           │
│  - Checks JSON parsed correctly                         │
│  - Checks body length > 200 chars                       │
│    ↓ [valid]                                            │
│  Save to Supabase (published table)                     │
│  - source_url, title, summary, category, source         │
│    ↓                                                    │
│  Ready for Publisher (NoOp — handoff point to WF3)      │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│  WF3 — PUBLISHER AGENT                  [⏳ TO BUILD]  │
│                                                         │
│  Webhook Trigger: POST /webhook/publisher-agent         │
│    ↓                                                    │
│  Generate Ghost JWT token                               │
│  - Split Admin API key → id + secret                    │
│  - Sign HS256 JWT (5 min expiry, /admin/ audience)      │
│    ↓                                                    │
│  POST to Ghost Admin API                                │
│  - Convert markdown body → HTML (mobiledoc/lexical)     │
│  - Set: title, html, tags, status=published,            │
│         feature_image, custom_excerpt (summary)         │
│    ↓                                                    │
│  Update Supabase published record                       │
│  - Set: ghost_url, ghost_post_id                        │
│    ↓                                                    │
│  Confirm publish → log to pipeline_runs                 │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│  WF4 — CURATOR AGENT (Newsletter)       [⏳ TO BUILD]  │
│                                                         │
│  Cron Trigger: Daily at 5:30am                         │
│    ↓                                                    │
│  Query Supabase: top 5 articles last 24h                │
│  - ORDER BY published_at DESC LIMIT 5                   │
│    ↓                                                    │
│  Has enough articles? (≥3 to send)                      │
│    ↓ [yes]                                              │
│  Format Newsletter digest                               │
│  - Subject: IndustrialBriefs Daily — {date}             │
│  - Body: Top 5 stories with title, summary, link        │
│    ↓                                                    │
│  POST to Beehiiv API                                    │
│  - Create post → auto-send to subscriber list           │
│    ↓                                                    │
│  Log to Supabase pipeline_runs                          │
└─────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  RESULT: Article live on Ghost + subscribers notified
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### 📊 Data Flow Summary

```
Internet (25 RSS feeds)
    ↓ every 6h
[Scout] Score + Scrape → top 30 articles
    ↓ new only (Supabase dedup)
[Writer] Groq LLaMA 3.3 → full article JSON
    ↓
[Supabase] published table ← source_url, title, summary, category
    ↓
[Publisher] Ghost CMS ← HTML article, tags, feature image
    ↓
[Curator] Beehiiv ← daily digest of top 5
    ↓
Subscribers 📬
```

---

### 🔧 What To Build Next (Phase 2.2 Tasks)

| Priority | Task | Blocker |
|----------|------|---------|
| 🔴 High | Set up Ghost CMS instance | Need hosting decision (Ghost Pro vs self-hosted) |
| 🔴 High | Get Ghost Admin API key | Needs Ghost instance first |
| 🔴 High | Build WF3 Publisher Agent | Needs Ghost API key |
| 🟡 Medium | Set up Beehiiv account | Free signup |
| 🟡 Medium | Build WF4 Curator Agent | Needs Beehiiv API key |
| 🟡 Medium | Wire WF2 → WF3 handoff | WF2 NoOp node ready as integration point |
| 🟢 Low | Configure `n8n.industrialbriefs.com` DNS | Optional for now |
| 🟢 Low | Add pipeline_runs logging | Monitoring/alerting |

---

### 📐 WF3 Publisher — Ghost API Reference

```javascript
// 1. Generate JWT token (runs inside n8n Code node)
const [id, secret] = GHOST_ADMIN_KEY.split(':');
const header = { alg: 'HS256', typ: 'JWT', kid: id };
const now = Math.floor(Date.now() / 1000);
const payload = { iat: now, exp: now + 300, aud: '/admin/' };
// → base64url(header).base64url(payload).signature

// 2. POST article to Ghost
POST https://{ghost-domain}/ghost/api/admin/posts/
Authorization: Ghost {jwt}
Content-Type: application/json

{
  "posts": [{
    "title": "AI Reshapes Modular Construction Timelines",
    "html": "<p>Full article HTML...</p>",
    "custom_excerpt": "Two sentence summary from Groq",
    "tags": [{"name": "construction"}, {"name": "ai"}],
    "feature_image": "https://og-image-from-scraper",
    "status": "published"
  }]
}
```

### 📐 WF4 Curator — Beehiiv API Reference

```
POST https://api.beehiiv.com/v2/publications/{pub_id}/posts
Authorization: Bearer {BEEHIIV_API_KEY}

{
  "subject": "IndustrialBriefs Daily — March 8, 2026",
  "content": {
    "free": "<h1>Top Stories</h1><p>...</p>"
  },
  "send_at": "immediate",
  "status": "confirmed"
}
```

---

### ⏱️ Performance Targets (Phase 2.2 Goals)

| Metric | Target |
|--------|--------|
| RSS fetch → Writer Agent | < 2 min |
| Writer Agent → Ghost published | < 1 min |
| Articles published per day | 10–20 |
| Newsletter send time | 6:00am daily |
| Human review time | 15 min/day |

---

## ⏭️ Next: Phase 3 — Website Design & UI
## ⏮️ Previous: Phase 1 — Strategy & Master Plan
