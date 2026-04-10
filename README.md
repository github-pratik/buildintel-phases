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
| **P2** | AI Agent Architecture | 🟠 In Progress | [phase2-agents.html](https://coral-app-74pa4.ondigitalocean.app/phase2-agents.html) | [phase2-agents.md](https://raw.githubusercontent.com/github-pratik/industrialbriefs/master/phase2-agents.md) |
| **P2.2** | Regulatory Automation | ✅ Done | [phase2.2-regulatory-automation.md](News-plan/phase2.2-regulatory-automation.md) |
| **P5** | Visibility & Monetization | ✅ Done | [phase5-monetization-visibility.md](News-plan/phase5-monetization-visibility.md) |
| **P-ALL** | **CONSOLIDATED ROADMAP** | 🚀 Ready | [ROADMAP-CONSOLIDATED.md](News-plan/ROADMAP-CONSOLIDATED.md) |
| **P-BUILD** | **MASTER BUILD PLAN** | 🛠️ Active | [MASTER_BUILD_PLAN.md](News-plan/MASTER_BUILD_PLAN.md) |
| **P3** | Website Design & UI | ⬜ Planned | [phase3-website.html](https://coral-app-74pa4.ondigitalocean.app/phase3-website.html) | [phase3-website.md](https://raw.githubusercontent.com/github-pratik/industrialbriefs/master/phase3-website.md) |
| **P4** | Build & Execution | ⬜ Planned | [phase4-build.html](https://coral-app-74pa4.ondigitalocean.app/phase4-build.html) | [phase4-build.md](https://raw.githubusercontent.com/github-pratik/industrialbriefs/master/phase4-build.md) |

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

---

## Design System

All pages share a consistent dark glassmorphism design system:

| Token | Value |
|-------|-------|
| Background | `#0d0f14` |
| Orange accent | `#e8863a` |
| Teal accent | `#3ab8a0` |
| Gold accent | `#d4a843` |
| Blue accent | `#5b9bd5` |
| Display font | Cormorant Garamond |
| Mono font | JetBrains Mono |
| Body font | DM Sans |

Pages support **light/dark mode** toggle (persisted in `localStorage`).

---

## Tech

- **Live site:** [DigitalOcean App Platform](https://coral-app-74pa4.ondigitalocean.app/) (`coral-app-74pa4.ondigitalocean.app`)
- **Repos:** [github-pratik/industrialbriefs](https://github.com/github-pratik/industrialbriefs) (primary) · [visioneeritsolutions/industrialbriefs](https://github.com/visioneeritsolutions/industrialbriefs) (company org → DO deploy)
- **Build:** Static HTML — no framework, no build step
- **Fonts:** Google Fonts (Cormorant Garamond, JetBrains Mono, DM Sans)
- **Auto-deploy:** Push to `master` on the App Platform–connected GitHub repo triggers a new DigitalOcean deploy

---

## File Structure

```
industrialbriefs/
├── index.html              # Phase dashboard homepage
├── phase1-masterplan.html  # Phase 1 interactive document
├── phase1-masterplan.md    # Phase 1 AI memory file
├── phase2-agents.html      # Phase 2 interactive document
├── phase2-agents.md        # Phase 2 AI memory file
├── phase3-website.html     # Phase 3 interactive document
├── phase3-website.md       # Phase 3 AI memory file
├── phase4-build.html       # Phase 4 interactive document
├── phase4-build.md         # Phase 4 AI memory file
└── vercel.json             # Optional — if using Vercel alongside DO (clean URLs, no-cache)
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
