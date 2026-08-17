# industrialBriefs — Phase Dashboard

> **Live site:** [coral-app-74pa4.ondigitalocean.app](https://coral-app-74pa4.ondigitalocean.app/)

**Repositories**

- **Phase dashboard (primary GitHub):** [github-pratik/industrialbriefs](https://github.com/github-pratik/industrialbriefs) — same static site as below; develop here, then sync to the company repo for App Platform.
- **DigitalOcean App Platform (deployed from company org):** [visioneeritsolutions/industrialbriefs](https://github.com/visioneeritsolutions/industrialbriefs) — **live URL:** [coral-app-74pa4.ondigitalocean.app](https://coral-app-74pa4.ondigitalocean.app/)

A public documentation hub for the **industrialBriefs** project — an AI-powered automated news intelligence platform for the Architecture, Engineering, Construction, & Manufacturing (AECM) industry.

---

## What Is This?

**industrialBriefs** is a planned automated news media company. This repo contains the **planning and design phases** in two formats for each phase:

- **HTML** — rich interactive documents with diagrams, timelines, and architecture visuals  
- **Markdown** — raw memory files for feeding directly into AI coding tools like Cursor, Claude Code, and Windsurf

---

## Phases

| Phase | Title | Status | HTML | MD |
|-------|-------|--------|------|----|
| **P1** | Strategy & Master Plan | ✅ Done | [phase1-masterplan.html](https://coral-app-74pa4.ondigitalocean.app/phase1-masterplan.html) | [phase1-masterplan.md](https://raw.githubusercontent.com/github-pratik/industrialbriefs/master/phase1-masterplan.md) |
| **P2** | AI Agent Architecture | ✅ Done | [phase2-agents.html](https://coral-app-74pa4.ondigitalocean.app/phase2-agents.html) | [phase2-agents.md](https://raw.githubusercontent.com/github-pratik/industrialbriefs/master/phase2-agents.md) |
| **P2.2** | Regulatory Automation | ✅ Done | — | [phase2.2-regulatory-automation.md](News-plan/phase2.2-regulatory-automation.md) |
| **P3** | Website Design & UI | ✅ Done | [phase3-website.html](https://coral-app-74pa4.ondigitalocean.app/phase3-website.html) | [phase3-website.md](https://raw.githubusercontent.com/github-pratik/industrialbriefs/master/phase3-website.md) |
| **P3.1** | UI Design Showcase | ✅ Done | [phase3.1-ui-showcase.html](https://coral-app-74pa4.ondigitalocean.app/phase3.1-ui-showcase.html) | — |
| **P3.5** | Pipeline Live · 24/7 | ✅ Done | [phase3.5-pipeline.html](https://coral-app-74pa4.ondigitalocean.app/phase3.5-pipeline.html) | — |
| **P4** | Build & Execution Roadmap | ✅ Done | [phase4-build.html](https://coral-app-74pa4.ondigitalocean.app/phase4-build.html) | [phase4-build.md](https://raw.githubusercontent.com/github-pratik/industrialbriefs/master/phase4-build.md) |
| **P5** | Intelligence Upgrade — **the live platform, current milestone** | 🟠 In Progress | [version5-platform.html](https://coral-app-74pa4.ondigitalocean.app/version5-platform.html) | — |
| **P6** | Visibility & Monetization | ✅ Done | — | [phase5-monetization-visibility.md](News-plan/phase5-monetization-visibility.md)¹ |
| **P-ALL** | **CONSOLIDATED ROADMAP** | 🚀 Ready | [ROADMAP-CONSOLIDATED.md](News-plan/ROADMAP-CONSOLIDATED.md) | — |
| **P-BUILD** | **MASTER BUILD PLAN** | 🛠️ Active | [MASTER_BUILD_PLAN.md](News-plan/MASTER_BUILD_PLAN.md) | — |

¹ filename kept as `phase5-monetization-visibility.md` for link stability — it's Phase 6 in the roadmap now that P5 refers to the live Intelligence Upgrade milestone.

---

## What Each Phase Contains

### Phase 1 — Strategy & Master Plan
The complete technical blueprint for the platform:
- Automated data flow pipeline (14 source types → ingestion → enrichment → publishing)
- Full tech stack decisions with rationale (n8n, Sanity, Next.js, Supabase, Beehiiv, Cloudflare)
- GovExec UI audit — 13 identified improvements
- URL structure and schema markup strategy
- SEO playbook and growth strategy
- GPT-readable design and LLMs.txt plan
- MCP (Model Context Protocol) server architecture
- Full build roadmap with weekly milestones

### Phase 2 — AI Agent Architecture
The 15+ agent system design:
- Agent hierarchy: Orchestrator → Department Heads → Worker Agents
- Safety layer: Hallucination Checker, Memory Agent, Monitor Agent
- 5 Department Heads: Construction, Architecture, Engineering, Manufacturing, Policy
- Worker Agents: Scout, Writer, SEO Agent, Curator, Publisher
- Tool relationship diagram (n8n → Claude API → Sanity → Next.js / Beehiiv / MCP API)
- Cost breakdown: ~$109/month total operating cost
- Human approval via Slack — 20–30 min/day editor time

### Phase 3 — Website Design & UI
Reader experience design:
- Design mandate: "Apple-level polish meets federal executive authority"
- Glassmorphism dark UI with editorial serif typography
- Mobile-first system (bottom tab bar, no hamburger)
- 6 premium ad placement zones (B2B CPM $40–80)
- MCP connection panel (ChatGPT, Claude, Perplexity integration)
- Hot keyword highlighting system

### Phase 4 — Build & Execution
Production build sequence:
- 28-week build roadmap from infrastructure to community
- Prerequisites: accounts, tools, and environment setup
- Week-by-week milestones: infra → CMS → agents → website → newsletter → MCP → monetization
- Target metrics: $109/mo ops cost, Day 90 Google News, 500+ subscribers Day 90

### Phase 5 — Intelligence Upgrade (live platform, current milestone)
Where the newsroom and the reader website merged into one running system:
- 15 AI agents (13 live) — Scout, Writer, Publisher, SEO, Clustering, Fact Sheet, Content Intel, Contracts, and more
- 2,900+ articles published autonomously, 99% SEO coverage, 0 errors/24h
- Automated SEO tagging and contract intelligence already in production; trend clustering and long-form journalism are the current build target
- See [version5-platform.html](https://coral-app-74pa4.ondigitalocean.app/version5-platform.html) for the full workflow map and metrics

---

## Design System

The homepage (`index.html`) runs a **retro-technical** design system — a blend of the Phase 1 doc's
neon-on-black palette and the Version 5 platform page's technical/blueprint structure:

| Token | Value |
|-------|-------|
| Background | `#0a0c10` |
| Orange accent (primary/brand) | `#f5792a` |
| Cyan accent | `#00d4ff` |
| Green accent | `#a8ff3e` |
| Yellow accent | `#ffd60a` |
| Purple accent | `#b06eff` |
| Display font | Syne |
| Serif accent font | DM Serif Display (italic) |
| Mono font | JetBrains Mono |

Individual phase documents (`phase1-masterplan.html`, etc.) each carry their own bespoke design system —
see each file's `<style>` block for its specific tokens.

Pages support **light/dark mode** toggle (persisted in `localStorage`). The homepage uses the real
IndustrialBriefs brand logo (`assets/logo/`), theme-swapped between the reverse (dark-mode) and
color (light-mode) variants.

---

## Tech

- **Live site:** [DigitalOcean App Platform](https://coral-app-74pa4.ondigitalocean.app/) (`coral-app-74pa4.ondigitalocean.app`)
- **Repos:** [github-pratik/industrialbriefs](https://github.com/github-pratik/industrialbriefs) (primary) · [visioneeritsolutions/industrialbriefs](https://github.com/visioneeritsolutions/industrialbriefs) (company org → DO deploy)
- **Build:** Static HTML — no framework, no build step
- **Fonts:** Google Fonts (homepage: Syne, DM Serif Display, JetBrains Mono; other pages: Cormorant Garamond, JetBrains Mono, DM Sans)
- **Auto-deploy:** Push to `master` on the App Platform–connected GitHub repo triggers a new DigitalOcean deploy

---

## File Structure

```
industrialbriefs/
├── index.html               # Phase dashboard homepage (retro/technical redesign)
├── assets/logo/              # Real brand logo assets (reverse = dark mode, color = light mode)
├── phase1-masterplan.html   # Phase 1 interactive document
├── phase1-masterplan.md     # Phase 1 AI memory file
├── phase2-agents.html       # Phase 2 interactive document
├── phase2-agents.md         # Phase 2 AI memory file
├── phase2.2-regulatory-automation.md
├── phase3-website.html      # Phase 3 interactive document
├── phase3-website.md        # Phase 3 AI memory file
├── phase3.1-ui-showcase.html
├── phase3.5-pipeline.html
├── phase4-build.html        # Phase 4 interactive document
├── phase4-build.md          # Phase 4 AI memory file
├── phase5-monetization-visibility.md  # Phase 6 content — filename kept for link stability
├── version5-platform.html   # Phase 5 — the live platform (current milestone)
└── vercel.json               # Optional — if using Vercel alongside DO (clean URLs, no-cache)
```

---

## Usage with AI Coding Tools

The MD files are formatted as AI memory files — drop them directly into your AI coding tool as context:

**Cursor / Claude Code / Windsurf:**
```
Read phase1-masterplan.md and use it as the project blueprint.
```

**Raw MD URLs:**
```
https://raw.githubusercontent.com/github-pratik/industrialbriefs/master/phase1-masterplan.md
https://raw.githubusercontent.com/github-pratik/industrialbriefs/master/phase2-agents.md
https://raw.githubusercontent.com/github-pratik/industrialbriefs/master/phase3-website.md
https://raw.githubusercontent.com/github-pratik/industrialbriefs/master/phase4-build.md
```

---

## Deploy On DigitalOcean

The same static phase dashboard can be deployed from the **company** repository on **DigitalOcean App Platform**:

- **GitHub repo:** [visioneeritsolutions/industrialbriefs](https://github.com/visioneeritsolutions/industrialbriefs)
- **Branch:** `master`
- **App spec:** `.do/app.yaml` (at repository root)
- **Deploy mode:** auto-deploy on push

Keep [github-pratik/industrialbriefs](https://github.com/github-pratik/industrialbriefs) aligned with [visioneeritsolutions/industrialbriefs](https://github.com/visioneeritsolutions/industrialbriefs); the company repo is what DigitalOcean builds — public URL: [coral-app-74pa4.ondigitalocean.app](https://coral-app-74pa4.ondigitalocean.app/).

### Recommended setup

1. Add the company remote (once per clone) and sync if the remote already has commits:
   ```bash
   git remote add company https://github.com/visioneeritsolutions/industrialbriefs.git
   git fetch company
   git pull company master --no-rebase   # resolve any conflicts, or merge as needed
   ```
2. Push your branch to `master` on the company remote (use `main:master` if your local default branch is `main`):
   ```bash
   git push company master               # if you are on branch master
   # or
   git push company main:master          # if your local branch is main
   ```
3. In DigitalOcean, go to **Apps** → **Create App** (or open the existing app).
4. Choose **GitHub** as the source and authorize DigitalOcean to access [visioneeritsolutions/industrialbriefs](https://github.com/visioneeritsolutions/industrialbriefs).
5. Select the `master` branch and keep the source directory as `/`.
6. Confirm the app is detected as a **Static Site**.
7. After the first deploy, add your custom domain in the app's **Networking** tab.

### CLI Option

If you use `doctl`, you can create the app from the included spec:

```bash
doctl apps create --spec .do/app.yaml
```

DigitalOcean assigns an `ondigitalocean.app` URL (this project uses [coral-app-74pa4.ondigitalocean.app](https://coral-app-74pa4.ondigitalocean.app/)); you can map a custom domain in **Networking**.

---

*industrialBriefs — Automated News Intelligence for Architecture, Construction, Engineering & Manufacturing*
