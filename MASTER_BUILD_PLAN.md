# IndustrialBriefs Elite Newsroom: Technical Implementation Roadmap
**V2.0 | Optimized for Autonomous Coding Agents**

---

## 🎯 Strategic Objective
Transition IndustrialBriefs from a commodity RSS rewriter to a **High-Authority Intelligence Engine**.
- **Input**: 30 RSS Feeds (AECM Industry, Supabase `feeds`)
- **Output**: Multi-source synthesized journalism, Regulatory alerts, AI-Native SEO, and B2B Lead-Gen.
- **Architecture**: N-to-1 parallel processing (N sources -> 1 Story Cluster -> 1 Fact Sheet -> 1 Article).

---

## 🚦 Phase Dashboard
| Phase | Title | Logic Engine | Status |
|---|---|---|---|
| **1** | **Clustering Foundation** | Event grouping (N-to-1) | ✅ Deployed (WF5 `kGhPKcmF0bk98Awc`, 2026-04-10) |
| **2** | **Fact Extraction** | Data-dense synthesis | ⬜ Pending |
| **3** | **Regulatory Intelligence** | Legal & Compliance deep-fetch | ⬜ Pending |
| **4** | **Editorial Production** | Semafor-style longform + Fact-Check | ⬜ Pending |
| **6** | **Growth & AI-SEO** | Schema.org + LinkedIn Automation | ⬜ Pending |
| **7** | **Monetization Layer** | B2B Lead-Gen CTAs | ⬜ Pending |

---

## 🛠️ Global Execution Rules (FOR AGENTS)
1. **Zero-Touch Production**: Do NOT modify existing `Scout v3` or `Writer v3` workflows.
2. **REST-Only DB**: Use Supabase REST API via `HTTP Request` nodes. No direct SQL.
3. **Looping Protocol**: When inserting mappings, use n8n `Split In Batches` or `Loop` nodes for stability.
4. **Header Protocol**: Always use `Prefer: return=representation` on POSTs to capture IDs.
5. **Self-Documentation**: Update this file's status after every successful sub-phase deploy.

---

## 📦 Phase 1: Clustering Foundation (WF5)
*Target: Convert fragmented RSS items into "Events".*

### 1.1: Harvesting Engine
- [ ] Query `queue` for articles in last 24h.
- [ ] Deduplicate: Filter IDs already present in `cluster_articles`.
- **API Spec**: `GET /rest/v1/queue?select=id,title,snippet,source&created_at=gt.NOW-24H`

### 1.2: Event Grouping (The Brain)
- [ ] **Prompt**: Group articles ONLY if they share the EXACT news event (e.g. same contract award, same specific law).
- [ ] **Model**: `gpt-4o-mini`
- **Output Schema**: `[{"cluster_title": string, "article_ids": string[]}]`

### 1.3: Relational Persistence
- [ ] Insert `story_clusters` -> Capture `cluster_id`.
- [ ] Insert `cluster_articles` -> Map `cluster_id` to each `article_id`.

---

## 🧠 Phase 2: Fact Density & Intelligence (WF5.1)
*Target: Build a "Fact Sheet" that powers high-quality writing.*

### 2.1: Data Synthesis
- [ ] Fetch full content for all `article_ids` in a cluster.
- [ ] **Extraction**: Pull numbers, dates, budgets, project names, and stakeholders.
- **Output Schema**: Save to `story_fact_sheets`.

### 2.2: Journalistic Tension
- [ ] Identify discrepancies between sources (e.g. Source A says "delayed", Source B says "on track").
- [ ] Flag "Conflict Points" for the editorial stage.

---

## ⚖️ Phase 3: Regulatory Deep-Fetch (WF6)
*Target: High-authority compliance reporting.*

### 3.1: Compliance Trigger
- [ ] Detect "Regulation", "Act", or "Policy" keywords in clusters.
- [ ] Use `web_fetch` to retrieve full legal text from government URLs.

### 3.2: AECM Impact Matrix
- [ ] Generate impact summaries for: Architects, Engineers, Contractors, and Manufacturers.
- [ ] Extract "Key Compliance Deadlines".

---

## ✍️ Phase 4: Elite Editorial & Accuracy (WF2 v4)
*Target: 1,500-word authoritative articles.*

### 4.1: Semafor-Style Writing
- [ ] **Structure**: [The News] -> [The View from Top] -> [On-Site Impact] -> [Bottom Line].
- [ ] **Constraint**: Article must use the `story_fact_sheet` as the primary source.

### 4.2: Adversarial Verification
- [ ] **Agent**: Claude 3.5 Sonnet.
- [ ] **Task**: Compare draft against raw source articles. Flag "Hallucination Risk" if claim is unsupported.

---

## 👁️ Phase 6: Visibility & Machine-Readiness (WF7)
*Target: Be the primary citation for AI Agents.*

### 5.1: AI-SEO (Schema.org)
- [ ] Generate `JSON-LD` for `TechArticle` and `SpecialAnnouncement`.
- [ ] Push schema to Ghost `codeinjection_head`.

### 5.2: B2B Viral Distribution
- [ ] Generate LinkedIn "Problem-Impact-Solution" posts.
- [ ] Post via LinkedIn API immediately after Ghost publication.

---

## 💰 Phase 7: B2B Monetization Engine (WF8)
*Target: Automated Lead-Generation.*

### 6.1: High-Intent Matching
- [ ] Tag clusters with "Product Categories" (e.g. BIM, Safety, Robotics).
- [ ] Match category to "Vendor Leads" in Supabase.

### 6.2: Dynamic CTA Injection
- [ ] Inject "Consult a Vendor" or "Download Comparison Guide" boxes into Ghost posts.
- [ ] Set up tracking for lead attribution.

---

*IndustrialBriefs: Moving AECM News from Noise to Intelligence.*
