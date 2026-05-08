# IndustrialBriefs — Phase 4: Production Hardening
**Status: ✅ LIVE | Last Updated: May 2026**

---

## What This Phase Delivered

Phase 4 turned the prototype newsroom into a credentialized, fully automated production pipeline. All six active workflows are live on n8n v2.18.5 (Railway), writing through Supabase, and publishing to Ghost CMS.

---

## Infrastructure

| Service | Details |
|---|---|
| **n8n** | v2.18.5 on Railway (`https://n8n-primary-production-e002.up.railway.app`) |
| **Supabase** | Free tier — core tables + clustering schema |
| **Ghost CMS** | `https://industrial-briefs.ghost.io` |
| **Vercel** | Landing + Phase dashboard (`buildintel-phases.vercel.app`) |

---

## Active Workflows

| ID | Workflow | Version | Schedule | Status |
|---|---|---|---|---|
| `N2HuAM6ThXrc4aGM` | WF1 Scout Agent | v3 | Every 6h | ✅ Active |
| `LO93zvn51g2JG2sJ` | WF2 Writer Agent | v3 (Hybrid) | Every 30m | ✅ Active |
| `6EbAxLnKpc7ZXXC1` | WF3 Publisher Agent | v3 | Every 30m | ✅ Active |
| `PNszQlAAeKVhkE6X` | WF4 Curator Agent | v1 | Manual | ⚠️ Inactive (Beehiiv key) |
| `kGhPKcmF0bk98Awc` | WF5 Clustering Agent | v2 | Every 4h | ✅ Active |
| `fa2Asr28rd2Sm4qS` | WF5.1 Fact Sheet Agent | v1 | Trigger | ✅ Active |
| `l0fJW1JwVzUBMe1Y` | Error Handler | v3 | On error | ✅ Active |

---

## What Was Fixed / Built

### WF1 — Scout Agent v3
- Fetches 26+ active RSS feeds from Supabase `feeds` table (tier-weighted)
- Scores and deduplicates against Supabase `queue` — refuses to enqueue duplicates
- Scrapes full content; logs every run to `pipeline_runs` with granular metrics
- Auto-disables feeds after 5 consecutive failures (`increment_feed_failures` RPC)
- Category balance: min 2 / max 5 per sector, ~15 articles per 6h run (~60/day)
- ENR RSS permanently dead — disabled in feeds

### WF2 — Writer Agent v3.1-Hybrid
- Migrated from Groq (expired key) to OpenAI `gpt-4o` via n8n OpenAI credential
- Writes completed articles to Supabase `published` table (title, content, image_url, tags)
- Exits cleanly with `No pending articles in queue` when Scout queues nothing new
- Queue status lifecycle: `pending → processing → completed/failed`

### WF3 — Publisher Agent v3
- Migrated from hardcoded Ghost JWT (blocked in n8n sandbox) to `Ghost Admin account` n8n credential
- Missing thumbnails trigger OpenAI image generation → Ghost image upload → Supabase patch
- Key facts newline fix: replaced broken `\n` template with `IB_KEY_FACTS:` image-alt carrier (theme-rendered)
- Ghost posts scheduled at next **9:00 AM UTC** (changed from +4h relative delay on 2026-05-06)
- CLAIMING recovery: failed rows auto-released; duplicate slugs reuse existing Ghost posts
- Dedup check prevents re-publishing already-published articles

### WF5 — Clustering Agent v2
- Reads recent `queue` rows, writes to `story_clusters` and `cluster_articles`
- Uses n8n OpenAI credential with `gpt-4o-mini`
- Validated: execution `4870` completed successfully post-deployment

### WF5.1 — Fact Sheet Agent v1
- Builds structured `story_fact_sheets` from clusters using `gpt-4o`
- Does NOT publish to Ghost — intelligence layer only
- Validated: execution `4871` completed successfully

### WF6 — SEO Agent (Deployed, Validating)
- Export: `exports/n8n-workflows/n8n-seo-agent.json`
- Generates `seo_title`, `meta_description`, `focus_keyword`, `slug`, `seo_ready` on `published` rows
- Migration applied: `supabase_migrations/2026-04-10-seo-agent-columns.sql`
- Validation: execution `4911` processed a test row, enforced 153-char meta description
- Publisher gating NOT yet enforced (safe rollout — SEO can't block publication yet)

---

## Supabase Schema (Phase 4 Additions)

```sql
-- published table additions
ALTER TABLE published ADD COLUMN content TEXT;
ALTER TABLE published ADD COLUMN image_url TEXT;
ALTER TABLE published ADD COLUMN tags JSONB;
ALTER TABLE published ADD COLUMN seo_title TEXT;
ALTER TABLE published ADD COLUMN meta_description TEXT;
ALTER TABLE published ADD COLUMN focus_keyword TEXT;
ALTER TABLE published ADD COLUMN slug TEXT;
ALTER TABLE published ADD COLUMN seo_ready BOOLEAN DEFAULT FALSE;

-- Clustering tables
CREATE TABLE story_clusters (...);
CREATE TABLE cluster_articles (...);
CREATE TABLE story_fact_sheets (...);
```

---

## n8n Key Patterns (Hard-Won)

- **No `process.env.*`** — n8n Code nodes block it. Hardcode all keys or use n8n credentials.
- **No `require('crypto')`** — also blocked. Use pure-JS HMAC-SHA256 (as in publisher).
- **No `{{ }}` expressions** in Code nodes. Use hardcoded values or `$getWorkflowStaticData()`.
- **Always init `staticData.metrics`** per node — nodes may run standalone in n8n UI.
- **`webhook/` vs `webhook-test/`** — production uses `/webhook/`; test requires UI "Listen" mode.
- **n8n API**: PUT for workflow updates — only `name/nodes/connections/settings` (no `versionId`/`pinData`). The `active` field is read-only.

---

## Production Metrics (as of May 2026)

| Metric | Value |
|---|---|
| Active n8n workflows | 6 (+ 1 error handler) |
| RSS feeds monitored | 26 active |
| Articles auto-published to Ghost | 150+ |
| Pipeline uptime | 99%+ (Railway) |
| Ghost posts scheduled at | 9:00 AM UTC daily |
| Supabase tables | 8 (queue, published, feeds, pipeline_runs, story_clusters, cluster_articles, story_fact_sheets, draft_articles) |
| n8n version | 2.18.5 (upgraded 2026-05-03) |

---

## Roadmap (Phase 5+)

- **WF7 — Regulatory Intelligence**: Detect Acts, Mandates, Compliance deadlines → plain English AECM impact summaries
- **WF8 — LinkedIn Distribution Agent**: Auto-generate Problem→Impact→Solution posts after each Ghost publish
- **WF4 Fix** — Get correct Beehiiv API key (`bh_*`) to activate Curator Agent for newsletter
- **SEO Gating** — Enable `seo_ready=true` gate on Publisher once WF6 is fully stable
- **MCP Server** — REST `/api/v1/articles`, Unkey.dev rate limiting, SSE transport at `mcp.industrialbriefs.com/sse`
- **WF9 — Monetisation Engine** — Vendor comparison guides, lead-gen CTAs, Ghost paid membership tiers
