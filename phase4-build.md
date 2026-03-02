# BuildIntel — Phase 4: Build & Deploy
**GPT Memory Context File | Status: 🔘 NOT STARTED | Last Updated: March 2026**

---

## 🎯 What This Phase Is

Phase 4 is the actual construction of BuildIntel — writing code, deploying infrastructure, connecting all services, and going live with the first automated articles publishing to the real website.

---

## 🗓️ Build Sequence (Week by Week)

### Week 1–2: Infrastructure Setup
- [ ] Railway account → deploy n8n instance
- [ ] Supabase project → create Memory Agent schema
- [ ] Vercel account → connect GitHub repo
- [ ] Cloudflare → DNS, CDN setup
- [ ] Sanity.io → create project, define content schema
- [ ] Beehiiv → create account, set up 5 newsletter publications
- [ ] Claude API key → add to n8n Anthropic credential
- [ ] Domain setup → buildintel.com (or chosen domain)

### Week 3–4: Sanity CMS Schema
```typescript
// Core content types to define in Sanity
- Article { title, slug, body, summary, sector, tags, author, publishedAt, sources, confidence, seoTitle, metaDescription }
- Author { name, bio, linkedIn, role }
- Section { name, slug, description, color }
- Tag { name, slug, relatedTags }
- DataPoint { tracker, value, date, source }
```

### Week 5–6: Scout + Memory Agent
- Build Scout Agent workflow in n8n (RSS + API fetching)
- Build Memory Agent with Supabase read/write
- Connect first 10 RSS feeds
- Test deduplication logic
- Verify state persistence on workflow restart

### Week 7–8: Writer + Hallucination Checker
- Build Writer Agent with Claude Sonnet node
- Craft and test rewrite prompt (Semafor format)
- Build Hallucination Checker workflow
- Test confidence scoring against known articles
- Calibrate threshold (70 pass / reject)

### Week 9–10: Department Heads + SEO Agent
- Build 5 Department Head workflows
- Calibrate sector scoring prompts per department
- Build SEO Agent with Claude Haiku
- Test full chain: Scout → Dept Head → Writer → Checker → SEO

### Week 11–12: Human Approval + Publisher
- Set up Slack workspace + approval bot
- Build Slack notification workflow (Approve/Edit/Reject buttons)
- Build Publisher Agent (Sanity write + Beehiiv push + IndexNow ping)
- Test full pipeline end-to-end with real articles
- Verify article appears on site within 60 seconds of approval

### Week 13–14: Next.js Website
- Initialize Next.js 15 project with App Router
- Connect Sanity via GROQ queries
- Build homepage layout (hero, section blocks, trending topics)
- Build article page template with JSON-LD schema
- Set up Meilisearch for site search
- Mobile bottom tab bar implementation
- Deploy to Vercel

### Week 15–16: Newsletter Automation
- Build Curator Agent in n8n
- Connect to Beehiiv API (create draft post endpoint)
- Set up 5:30am cron trigger
- Build Slack approval for newsletter
- Test full newsletter flow: articles → curation → draft → Beehiiv → send

### Week 17–18: Orchestrator + Monitor
- Build Monitor Agent (health checks every 10 min)
- Build Orchestrator (60-min system review)
- Connect Orchestrator to all Dept Head agents
- Add Slack daily summary (9am report)
- Load test full pipeline (stress test 24h run)

### Week 19–20: SEO & Launch Prep
- Submit to Google News Publisher Center
- Submit XML sitemap to Google Search Console
- Set up IndexNow for all published articles
- Write first 20 hand-crafted articles (seed content)
- Publish first 5 SEO pillar pages (Tier 1 keywords)
- Add JSON-LD to all page types
- Create LLMs.txt

### Week 21–24: MCP Server
- Build public REST API (`/api/v1/articles`, `/api/v1/regulations`, etc.)
- Set up Unkey.dev for API key management + rate limiting
- Build MCP server using @anthropic-ai/mcp-sdk
- Set up SSE transport at `mcp.buildintel.com/sse`
- Test with Claude Desktop and ChatGPT custom GPT
- Publish MCP documentation page

### Week 25–28: Community + Monetization
- Set up Beehiiv paid subscription tiers
- Apply to Beehiiv Ad Network (requires 1,000+ active subs)
- Set up direct advertiser contact form + media kit page
- Launch community Slack/Discord
- First monthly virtual roundtable event

---

## 🛠️ Development Tools

| Tool | Purpose |
|---|---|
| **Cursor IDE** | Primary code editor — vibe code in plain English |
| **Claude Code CLI** | Terminal — deployment, debugging, complex logic |
| **GitHub** | Version control for all code |
| **Railway** | n8n hosting + background workers |
| **Vercel** | Next.js deployment |
| **Supabase Studio** | Database management UI |
| **n8n UI** | Workflow monitoring + editing |
| **Sanity Studio** | Content editing UI (editor-facing) |

---

## 📁 Project File Structure

```
buildintel/
├── apps/
│   ├── web/                    ← Next.js website
│   │   ├── app/
│   │   │   ├── page.tsx        ← Homepage
│   │   │   ├── [section]/      ← Section pages
│   │   │   ├── article/[slug]/ ← Article pages
│   │   │   ├── topic/[tag]/    ← Topic cluster pages
│   │   │   ├── data/           ← Data tracker pages
│   │   │   └── api/v1/         ← Public REST API
│   │   ├── components/
│   │   ├── lib/
│   │   └── sanity/             ← Sanity client + queries
│   └── studio/                 ← Sanity Studio
├── agents/                     ← n8n workflow JSON exports
│   ├── scout-agent.json
│   ├── writer-agent.json
│   ├── hallucination-checker.json
│   ├── seo-agent.json
│   ├── curator-agent.json
│   ├── publisher-agent.json
│   ├── memory-agent.json
│   ├── monitor-agent.json
│   └── orchestrator-agent.json
├── docs/                       ← Phase MD memory files
│   ├── phase1-masterplan.md
│   ├── phase2-agents.md
│   ├── phase3-website.md
│   └── phase4-build.md
└── mcp/                        ← MCP server
    └── server.ts
```

---

## 💰 Monthly Cost at Full Operation

| Service | Cost |
|---|---|
| n8n on Railway | $20/mo |
| Claude API (Haiku + Sonnet + Opus) | $40–60/mo |
| Vercel Pro | $20/mo |
| Sanity.io | $0 (free tier) |
| Supabase | $0 (free tier) |
| Beehiiv | $0 → $43/mo at 2,500+ subs |
| Cloudflare | $0 |
| Crunchbase API | $29/mo |
| Domain | $15/yr |
| **Total Phase 1 operating** | **~$109–130/mo** |

---

## 🎯 Launch Success Metrics (Day 90)

- [ ] 500+ newsletter subscribers
- [ ] 1,000+ articles indexed by Google
- [ ] Appearing in Google News carousels
- [ ] 15+ auto-published articles per day
- [ ] First 3 Tier 1 keywords ranking page 1 (EU AI Act construction, OSHA AI, etc.)
- [ ] First advertiser inquiry received
- [ ] MCP server live and tested with Claude Desktop

---

## ⏮️ Previous Phase

**Phase 3 — Website Design & UI**
See: `phase3-website.html` and `phase3-website.md`
