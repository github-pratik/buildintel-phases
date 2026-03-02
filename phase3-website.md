# BuildIntel — Phase 3: Website Design & UI
**GPT Memory Context File | Status: 🔵 PLANNED | Last Updated: March 2026**

---

## 🎯 What This Phase Is

Phase 3 designs and builds the actual BuildIntel website — the reader-facing product. This is where all the automated content from Phase 2 appears. The design must balance editorial authority, mobile usability, AI-readability, and ad monetization.

---

## 🎨 Design Vision

**"Apple-level polish meets federal executive authority"**

### Aesthetic Direction
- **Style:** Modern glassmorphism — soft glass effects, blurred backgrounds, subtle transparency, layered depth
- **Feel:** Executive, credible, institutional — visually elevated and future-forward
- **Inspiration:** Apple polish + GovExec editorial authority + Bloomberg data density
- **Motion:** Subtle — depth and entrance animations, not flashy
- **Color:** Neutral dark base + bold accent colors (orange, teal, gold)

### Typography
- **Display/Headlines:** Cormorant Garamond or similar editorial serif — authoritative, credible
- **Body:** DM Sans or Cabinet Grotesk — clean, highly legible
- **Metadata/Code:** JetBrains Mono or Space Mono — technical credibility

### Key Visual Rules
- Eye-catching but not flashy
- Strong headline hierarchy
- Hot keywords highlighted with subtle accent glows
- Generous whitespace for readability
- Glass cards with backdrop blur
- Dark base theme (primary) with light mode option

---

## 📱 Mobile-First Requirements

**Bottom Tab Bar (mobile):**
```
[🏠 Home] [🔍 Search] [📰 Sections] [📧 Newsletter] [🔖 Saved]
```
No hamburger menu. Native app feel. Thumb-friendly touch targets.

**Mobile Article Layout:**
- Full-width article body
- Sticky progress indicator (how far through article)
- Share button via Web Share API
- Related stories after article, not beside it

**Performance Target:** LCP < 1.5 seconds on mobile

---

## 🖥️ Homepage Layout

### Desktop
```
[BREAKING NEWS TICKER — live scrolling]
[PHASE NAV — phase 1 | phase 2 ● | phase 3 | phase 4]
[MAIN NAV — Architecture | Construction | Engineering | Manufacturing | Policy | Data]

[HERO — 3-column grid, largest story left + 2 supporting right]
[TRENDING TOPICS BAR — hot keywords with accent glow]

[SECTION BLOCKS]
  Left column (70%):        Right column (30%):
  Article feed             Newsletter signup
  [Ad Zone A - banner]     Trending topics
  More articles            [Ad Zone B - sidebar]
  Data tracker widget      Deal Flow preview
  [Ad Zone C - inline]     Policy alerts

[FOOTER — links, newsletter, MCP connection panel]
```

### Hot Keyword System
Keywords like "EU AI Act", "Built Robotics", "Digital Twins", "Generative AI" get:
- Subtle orange/teal underline glow on hover
- Auto-linked to topic cluster pages
- Displayed in trending bar when appearing frequently
- Weighted by recency and frequency algorithmically

---

## 📰 Article Page Layout

```
[PHASE NAV]
[MAIN NAV]

[BREADCRUMB: Section → Topic]
[ARTICLE HEADLINE — large editorial serif]
[BYLINE + TIMESTAMP + READ TIME + CONFIDENCE SCORE]

[HERO IMAGE]

[ARTICLE BODY]                    [STICKY SIDEBAR]
  Semafor format:                   Key Facts box
  • What Happened                   Related Articles (3)
  • Why It Matters                  Newsletter signup
  • The Numbers                     [Ad Zone — sidebar]
  • What's Next                     MCP "Use in AI" button
  • Room for Disagreement

[HOT KEYWORDS highlighted inline]

[SOURCES + RELATED ARTICLES]
[COMMENTS / REACTIONS]
[Ad Zone — below article]
```

---

## 💰 Ad Placement Strategy

### Ad Zones (6 positions)
| Zone | Location | Format | Expected CPM |
|---|---|---|---|
| A — Hero Banner | Below breaking ticker | 728×90 leaderboard | $45–70 |
| B — Sidebar Top | Right rail, above fold | 300×250 rectangle | $40–65 |
| C — In-Feed | Between articles 3 and 4 | Native card format | $50–80 |
| D — Article Inline | After 3rd paragraph | In-content 300×250 | $55–85 |
| E — Article End | Below article body | 728×90 leaderboard | $35–55 |
| F — Newsletter | Beehiiv sponsored slot | Email native | $30–50/send |

**Target advertisers:** Autodesk, Siemens, Trimble, Caterpillar, NVIDIA Omniverse, Bentley Systems, Procore, Esri, PTC, Dassault Systèmes

**Why B2B ACEM is premium:** Engineers and construction managers are hard to reach. $40–80 CPM is standard for targeted B2B vertical audiences vs $2–5 for general news.

### Ad Policy
- No auto-play video ads
- No interstitials or popups
- Native/editorial format preferred
- Content loads before ads (defer all ad scripts)

---

## 🔌 MCP Connection Panel

Located in footer and article sidebar. Allows readers to connect BuildIntel as a data source for their AI tools.

### UI Elements
- "Connect to your AI" section with tool logos (ChatGPT, Claude, Perplexity, Custom)
- Copy MCP server URL: `mcp.buildintel.com/sse`
- API key generation for authenticated access
- Rate limit tiers displayed: Free (100 req/day) | Pro ($49/mo, 10k req/day)

### MCP Endpoints Exposed
- `get_latest_news(sector, limit, since)`
- `get_regulation_tracker(jurisdiction, sector)`
- `get_funding_deals(sector, since, min_amount)`
- `search_articles(query, sector, date_range)`
- `subscribe_breaking_news` (WebSocket)

---

## 🤖 GPT/AI Readability Layer

- **Semantic HTML** — proper `<article>`, `<time>`, `<address>` tags
- **JSON-LD NewsArticle schema** on every article page
- **FAQPage schema** on all guide/pillar pages
- **Dataset schema** on all data tracker pages
- **LLMs.txt** at `/llms.txt` — machine manifest for AI crawlers
- **XML Sitemaps** — news sitemap updated every 2 minutes
- **OpenGraph** — auto-generated OG images via Vercel OG

---

## 🛠️ Tech Stack (Frontend)

| Layer | Tool | Reason |
|---|---|---|
| Framework | Next.js 15 (App Router) | ISR, SEO, image optimization |
| Styling | Tailwind CSS + custom CSS | Speed + glassmorphism custom |
| Animations | Framer Motion | Subtle entrance + hover |
| CMS connection | Sanity GROQ queries | Fast, flexible content fetch |
| Search | Meilisearch | Sub-50ms, in-site search |
| Auth (Pro) | Clerk | API key management |
| Analytics | Vercel Analytics + Plausible | Privacy-first |
| Images | Cloudinary or next/image | Auto-optimization |
| OG Images | Vercel OG | Auto-generated per article |
| Hosting | Vercel | ISR, edge network, zero ops |

---

## 📋 Key Pages to Build

1. **Homepage** — hero, sections, data widgets, trending topics
2. **Section landing pages** (5) — Architecture, Construction, Engineering, Manufacturing, Policy
3. **Article page** — full layout with sidebar, schema, MCP button
4. **Topic tag pages** — aggregated articles by topic cluster
5. **Data tracker pages** — AI Adoption Tracker, Funding Tracker, Regulation Map
6. **Newsletter hub** — all 5 newsletter signups
7. **Search results page** — Meilisearch powered
8. **Author profile pages** — E-E-A-T signals for Google
9. **About + Advertise pages** — media kit, ad specs
10. **MCP documentation page** — API reference, connection guide

---

## ⏭️ Next Phase

**Phase 4 — Build & Deploy**
Actual code. n8n workflows. Claude API connections. Sanity schema. Next.js site. Vercel deployment. Full pipeline running.

See: `phase4-build.html` and `phase4-build.md`

## ⏮️ Previous Phase

**Phase 2 — Agent Orchestra & Data Flow**
See: `phase2-agents.html` and `phase2-agents.md`
