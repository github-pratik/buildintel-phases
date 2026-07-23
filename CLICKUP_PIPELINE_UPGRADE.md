# IndustrialBriefs — Pipeline Upgrade
## Phase 2: Trending Intelligence, Long-form Articles & SEO

---

## Overview

The current pipeline fetches news, writes short articles, and publishes them. It works — but it treats every story the same way and produces content that is too short to rank on Google or keep readers on the page long enough to generate ad revenue.

This upgrade makes the pipeline smarter in three ways:

1. **The Scout knows what's trending** — when the same story breaks across 3+ sources, it gets flagged as hot and published immediately instead of waiting in the queue
2. **The Writer produces real journalism** — 1000–1500 word long-form articles with analysis, context, and a strong hook that keeps readers reading
3. **Every article is SEO-ready before it goes live** — a dedicated SEO agent generates the title, meta description, keyword, and URL slug automatically

---

## What We're Building

### 5 changes to the existing pipeline

---

### 1. Scout Agent — Hot Topic Detection
**Priority: Medium | Effort: High**

The Scout currently scores articles individually. After this upgrade it will group articles by topic — if the same story appears across 3 or more sources within 2 hours, it gets flagged as **trending**.

Trending articles skip the 30-minute queue and trigger the Writer immediately.

**Outcome:** Breaking industry news hits the site within minutes, not hours.

---

### 2. Writer Agent — Long-form Journalism
**Priority: High | Effort: Medium**

The current Writer produces ~500 word articles. After this upgrade it will produce **1000–1500 word professional articles** structured for reader retention:

- Strong hook opening (not a summary — a fact that makes you keep reading)
- Expanded What Happened with full specifics
- Deep Why It Matters section with 3–4 paragraphs covering cost, timeline, labour, supply chain impacts
- Industry Context (precedents and comparable events)
- What's Next with concrete upcoming dates
- Bottom Line — one sentence every AECM professional can act on

**Outcome:** Articles worth bookmarking. Readers stay longer → more ad impressions → more revenue.

---

### 3. SEO Agent — New Addition
**Priority: High | Effort: Low**

A lightweight new agent that runs after the Writer and before the Publisher. It reads each article and generates:

- **SEO title** — keyword-rich, under 60 characters (what Google shows in search results)
- **Meta description** — 120–155 characters written to earn a click
- **Focus keyword** — the primary term professionals would search
- **URL slug** — clean, keyword-rich URL

Uses a smaller, cheaper AI model (gpt-4.1-mini). Adds almost nothing to cost.

**Outcome:** Every article is Google-discoverable from day one.

---

### 4. Publisher Agent — SEO-aware Ghost Posts
**Priority: Medium | Effort: Low**

Small update. The Publisher will now:
- Wait for the SEO Agent to finish before publishing
- Pass the SEO title, meta description, and slug directly into Ghost
- Articles publish with proper meta tags — no manual editing needed

**Outcome:** Clean SEO setup on every post automatically.

---

### 5. Curator Agent — Removed
**Priority: Low | Effort: Minimal**

The Beehiiv newsletter agent (WF4) has never worked due to a broken API key. We're deactivating it to keep the pipeline clean. Newsletter can be revisited as a separate project.

---

## Updated Pipeline Flow

```
Every 6 hours:
Scout checks 30 RSS feeds
  ├── Normal story    → queue → Writer picks up within 30 min
  └── Trending story  → queue → Writer triggered immediately

Writer runs (every 30 min + on hot-topic trigger):
  Writes 1000–1500 word article with gpt-4.1
  Saves to database

SEO Agent runs (every 30 min):
  Reads new articles → generates SEO fields with gpt-4.1-mini
  Marks article as SEO-ready

Publisher runs (every 30 min):
  Picks up SEO-ready articles
  Creates scheduled Ghost post (publishes 4h later)
  Notifies via Telegram
```

---

## Tasks

### Database
- [ ] Add `is_trending`, `source_count`, `cluster_id` columns to queue table
- [ ] Add `seo_title`, `meta_description`, `focus_keyword`, `slug`, `seo_ready`, `is_trending` columns to published table
- [ ] Add database indexes for new query patterns

### Scout Agent v4
- [ ] Add topic clustering logic (group articles by keyword overlap)
- [ ] Add trending detection (3+ sources in 2h = trending)
- [ ] Insert trending flag + source count into queue
- [ ] Trigger Writer webhook immediately for trending articles

### Writer Agent v4
- [ ] Update system prompt for long-form format
- [ ] Raise max_tokens from 1200 → 2500
- [ ] Prioritise trending articles in fetch query
- [ ] Pass is_trending field to published table

### SEO Agent v1 (new)
- [ ] Create new n8n workflow
- [ ] Poll published table for seo_ready = false
- [ ] Call gpt-4.1-mini to generate SEO fields
- [ ] Update published table and set seo_ready = true

### Publisher Agent v3
- [ ] Update fetch query to require seo_ready = true
- [ ] Add SEO fields to Ghost post payload (og_title, meta_description, slug)

### Cleanup
- [ ] Deactivate Curator Agent (WF4)
- [ ] Update documentation

---

## Cost

| | Before | After |
|---|---|---|
| Article writing | ~$0.008/article (500 words) | ~$0.022/article (1500 words) |
| SEO generation | — | ~$0.0001/article |
| **Monthly (60 articles/day)** | **~$15/month** | **~$40/month** |

The cost increase is directly tied to 3× longer articles — higher quality content that can earn ad revenue.

---

## Implementation Order

To keep the live pipeline running while we upgrade:

1. Database migration (no downtime)
2. SEO Agent — build new workflow
3. Publisher v3 — add SEO fields
4. Writer v4 — long-form prompt
5. Scout v4 — clustering + trending
6. Deactivate Curator

Each phase can be tested independently before the next one is built.

---

*Technical spec: see `PIPELINE_UPGRADE_PLAN.md` in the repository*
