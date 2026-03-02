# BuildIntel — Phase 2: Agent Orchestra & Data Flow
**GPT Memory Context File | Status: 🟠 IN PROGRESS | Last Updated: March 2026**

---

## 🎯 What This Phase Is

Phase 2 designs and documents the complete AI agent hierarchy for BuildIntel's automated newsroom. It covers every agent's role, inputs, outputs, and how they interconnect — built in n8n with Claude API as the intelligence layer.

---

## ✅ Decisions Locked in Phase 2

| Decision | Choice | Reason |
|---|---|---|
| Agent builder | **n8n (self-hosted on Railway)** | Unlimited ops ~$20/mo, native Claude node, workflows trigger workflows, built-in DB |
| AI brain | **Claude API** | Haiku/Sonnet/Opus tiered by task cost. Native Anthropic node in n8n |
| vs Make.com | Rejected | ~$300+/mo at our operation volume (13,000+ ops/day) |
| vs Zapier | Rejected | $400+/mo, no agent-to-agent triggering |
| Vibe coding | **Cursor + Claude Code CLI** | Describe workflows in English → code generated → import to n8n |
| Memory store | **Supabase (PostgreSQL)** | Persistent state across agent crashes, real-time subscriptions |
| Human approval | **Slack buttons** | Approve/Edit/Reject in one click, 20–30 min/day |

---

## 🏗️ The Agent Hierarchy

### Level 0 — Human (Above All Agents)
- **You (Human Editor)** — Final approval gate. Nothing publishes without you. Notified via Slack.

### Level 1 — Orchestrator
- **🧠 Orchestrator Agent** — Runs every 60 min. Reads full system state from Memory Agent. Balances topic distribution across departments. Sends priority instructions to Dept Heads.

### Semi Level — Safety & Infrastructure (Always Running)
- **⚡ Hallucination Checker** — Every draft passes through. Cross-checks claims vs source. Confidence score 0–100. Below 70 → back to Writer.
- **📦 Memory Agent** — Writes state to Supabase after every action. Enables crash recovery. Deduplicates stories.
- **📊 Monitor Agent** — Checks system health every 10 min. Slack alert if any agent fails.

### Level 2 — Department Heads (5 agents)
- 🏗️ Construction Editor
- 🏛️ Architecture Editor
- ⚙️ Engineering Editor
- 🏭 Manufacturing Editor
- ⚖️ Policy Editor

Each: receives raw scored stories → evaluates sector relevance → scores 0–100 → routes to Writer if ≥60

### Level 3 — Worker Agents (5 agents)
- 🕷️ **Scout** — Fetches all sources every 5 min
- ✍️ **Writer** — Rewrites in ACEM voice, Semafor format (Claude Sonnet)
- 🔍 **SEO Agent** — Title, meta, slug, keywords, internal links (Claude Haiku)
- 📧 **Curator** — Builds daily newsletter at 5:30am
- 🚀 **Publisher** — Pushes approved content to Sanity + Beehiiv

---

## 🔄 Complete Data Flow

```
WORLD (internet)
  ↓ [every 5 min]
🕷️ SCOUT — fetches 40+ RSS feeds, APIs, Gov portals, Crunchbase
  ↓
📦 MEMORY CHECK — seen this URL before? skip if yes
  ↓ [new story]
🏗️ DEPT HEAD — scores relevance for sector (0–100)
  ↓ [score ≥60]
✍️ WRITER — Claude Sonnet rewrites completely in ACEM voice
  ↓
⚡ HALLUCINATION CHECKER — cross-checks every claim vs source
  ↓ [confidence ≥70]
🔍 SEO AGENT — Claude Haiku generates title, meta, slug, keywords
  ↓
👤 HUMAN EDITOR — Slack: [APPROVE] [EDIT] [REJECT]
  ↓ [approved]
🚀 PUBLISHER — writes to Sanity → triggers Next.js ISR → pings IndexNow
  ↓ [daily 5:30am]
📧 CURATOR — selects top 5–7 stories → Beehiiv draft → Slack approval → 6am send
```

---

## 📦 Agent Input/Output Specs

### Scout Agent
- **Trigger:** n8n Schedule, every 5 minutes
- **Input:** 40+ RSS feeds, NewsAPI, Federal Register, Crunchbase webhooks, ArXiv
- **Output:** `{url, headline, source, published_at, raw_text, source_category}`
- **Sends to:** Department Head Agents

### Writer Agent
- **Trigger:** Enriched story ≥60 score from Dept Head
- **Input:** Enriched story + source URL
- **Model:** Claude Sonnet
- **Format:** Semafor — What Happened / Why It Matters / The Numbers / What's Next / Room for Disagreement
- **Output:** `{headline, body, summary, why_it_matters, word_count, sources_cited}`

### Hallucination Checker
- **Input:** Draft article + original source URL
- **Process:** Re-reads source, compares every specific claim (numbers, names, dates, quotes)
- **Scores:** VERIFIED / UNVERIFIED / CONTRADICTED per sentence
- **Routes:** ≥85 → SEO Agent | 70–84 → SEO Agent + flags highlighted | <70 → back to Writer

### Memory Agent
- **Called by:** Every agent, before and after every action
- **Tracks:** Fetched URLs, draft IDs, queue counts, publish status, timestamps, agent health
- **Storage:** Supabase PostgreSQL
- **Critical function:** If agent crashes → restart → reads Memory → resumes exactly where stopped

### Curator Agent
- **Trigger:** 5:30am daily cron
- **Selects:** Top 5–7 stories from last 24h (1 per sector minimum)
- **Writes:** Axios-style 2-line preview per story, 3 subject line A/B options
- **Output:** Complete newsletter pushed to Beehiiv as draft

---

## 💡 Key Technical Specs

### n8n Setup
- Self-hosted on Railway ($20/mo)
- Each agent = one n8n workflow
- Orchestrator = n8n workflow that calls other workflows
- Memory Agent = n8n workflow with Supabase read/write nodes
- Claude connected via Anthropic credential (one API key, all agents)

### Claude Model Usage by Agent
| Agent | Model | Reason |
|---|---|---|
| Scout | None | No AI needed — just fetch |
| Dept Heads | Claude Haiku | Simple scoring, cost-efficient |
| Writer | Claude Sonnet | Quality rewriting essential |
| Hallucination Checker | Claude Sonnet | Accuracy-critical |
| SEO Agent | Claude Haiku | Fast, simple generation |
| Curator | Claude Sonnet | Newsletter quality matters |
| Orchestrator | Claude Opus | Complex reasoning, used sparingly |

### Estimated Monthly Claude API Cost
~$30–60/mo at full pipeline operation (15–25 articles/day)

---

## 🛠️ Build Method

- **Cursor IDE** — vibe code in plain English → generates n8n workflow JSON
- **Claude Code CLI** — terminal-based deployment, debugging, complex logic
- **n8n UI** — visual monitoring, connecting nodes, watching workflows run
- Import workflow JSON into n8n → done (no manual node-by-node building)

---

## 📋 Data Sources (14 Types)

| Source | Type | Cost | Refresh |
|---|---|---|---|
| Industry RSS feeds (40+) | RSS/Atom | Free | 5 min |
| Federal Register API | Gov | Free | Daily |
| Regulations.gov API | Gov | Free | Daily |
| EU EUR-Lex RSS | Gov | Free | Daily |
| GDELT | News API | Free | Real-time |
| ArXiv RSS | Research | Free | Daily |
| Crunchbase Basic | Funding | $29/mo | Webhook |
| Playwright scrapers | Scraping | Free | Hourly |
| X (Twitter) API | Social | $100/mo | Real-time |
| Semantic Scholar | Research | Free | Daily |
| Listen Notes + AssemblyAI | Podcast | ~$50/mo | New episodes |
| NewsAPI.org | News | $449/mo | Real-time |

**Recommended Phase 2 sources (skip expensive ones initially):**
RSS + GDELT + Gov APIs + Crunchbase + Playwright = full coverage at ~$29/mo data cost

---

## ⚡ Performance Targets

- Source → Published: **under 4 minutes**
- Daily auto-published articles: **15–25**
- Human editor daily time: **20–30 minutes**
- Newsletter send time: **6:00am daily**
- Agent health check interval: **every 10 minutes**

---

## 📋 Key Decisions Still Open

- [ ] Slack workspace setup for human approval notifications
- [ ] Supabase schema design for Memory Agent state tables
- [ ] n8n Railway deployment configuration
- [ ] First 10 RSS feeds to connect (start small, expand)
- [ ] Claude API key and credential setup in n8n

---

## ⏭️ Next Phase

**Phase 3 — Website Design & UI**
The actual BuildIntel website: glassmorphism aesthetic, Apple-level polish, GovExec-inspired editorial layout, hot keyword highlighting, mobile-first bottom tab bar, ad placement zones, MCP connection panel.

See: `phase3-website.html` and `phase3-website.md`

## ⏮️ Previous Phase

**Phase 1 — Strategy & Master Plan**
See: `phase1-masterplan.html` and `phase1-masterplan.md`
