# IndustrialBriefs 2026: Master Development Roadmap (Consolidated)
**GPT Memory Context File | Created: April 2026**

---

## 🎯 The Vision
Transform IndustrialBriefs from a "News Site" into a **"High-Authority Intelligence Utility"** for the AECM (Architecture, Construction, Engineering, Manufacturing) industry. 

The core differentiators are **Accuracy**, **Regulatory Expertise**, and **AI-Ready Infrastructure**.

---

## 🏗️ 1. The Intelligence Pipeline (N-to-1 Architecture)
*   **Agent: WF5 Clustering Agent (FOUNDATION) — deployed**
    *   **n8n workflow ID**: `kGhPKcmF0bk98Awc` (active, **2026-04-10**).
    *   **Focus**: Grouping multiple RSS articles (N) into a single Event (1).
    *   **Action**: Populate `story_clusters` and `cluster_articles`; downstream `story_fact_sheets` and `draft_articles`.
    *   **Value**: Eliminates duplicate news and provides the "Fact Density" needed for long-form reporting.
*   **Target Agent: WF6 Regulatory Analyst (NEW)**
    *   **Focus**: EU AI Act, OSHA, CHIPS Act, NIST.
    *   **Action**: Full-text PDF extraction and "AECM Impact Analysis."
*   **Safety Layer: Adversarial Accuracy Check**
    *   **Action**: A mandatory secondary LLM (Claude 3.5 Sonnet) fact-check before any "Policy Wire" post goes live.
    *   **Human-in-the-Loop**: High-impact news is flagged to a Slack/Telegram "Approve/Reject" dashboard.

---

## 👁️ 2. The Visibility Engine (Cluster-Based SEO)
*   **Target Agent: SEO Agent v2** (future workflow — **not** WF5; WF5 is clustering)
    *   **Focus**: Optimizing the *Cluster* as a Topic Hub.
    *   **Action**: Dual-optimization.
        *   **Human SEO**: Keyword-rich slugs and meta-titles for the *Event*.
        *   **LLM SEO**: JSON-LD Schema (TechArticle/SpecialAnnouncement) + Citation-ready "Key Takeaway" boxes.
*   **AI Access Layer**:
    *   **File**: `/llms.txt` (A direct map for AI crawlers).
    *   **Protocol**: Public MCP Server for Pro users.
*   **Viral Distribution**:
    *   **Agent**: **WF7 LinkedIn Distributor (NEW)**.
    *   **Action**: Automated "Problem-Impact-Solution" posts for every trending *Cluster*.

---

## 💰 3. The Monetization Engine (Cluster-Level Leads)
*   **Target Agent: WF8 Monetization Scout (NEW)**
    *   **Action**: Scan *Clusters* for high-intent keywords (e.g., "Site Safety," "BIM Software").
    *   **Monetization**: Insert automated "Vendor Comparison Guides" or "Consult an Expert" CTAs at the *Story* level.
    *   **Lead Gen**: Capture B2B leads to sell to major AECM vendors (Autodesk, Siemens, Hilti).

---

## 🚀 Combined Execution Sequence

| Phase | Milestone | Priority | Model |
|---|---|---|---|
| **Phase 2.1** | **Parallel Clustering Engine** (WF5 Foundation) | 🚨 High | GPT-4o-mini |
| **Phase 2.2** | **Accuracy & Policy** (WF6 + Fact-Check) | 🚨 High | GPT-4o |
| **Phase 3.0** | **LLM-SEO & Machine Readiness** (JSON-LD + llms.txt) | 🟠 Med | GPT-4o-mini |
| **Phase 4.0** | **Automated B2B Distribution** (LinkedIn Agent) | 🟠 Med | GPT-4o-mini |
| **Phase 6.0** | **Monetization Layer** (Lead Gen + CTAs) | 🟢 Low | GPT-4o-mini |

---

## 📋 Technical Requirements Update (Supabase)

```sql
-- Track regulation impact and accuracy
ALTER TABLE published ADD COLUMN IF NOT EXISTS accuracy_score FLOAT DEFAULT 1.0;
ALTER TABLE published ADD COLUMN IF NOT EXISTS is_regulatory BOOLEAN DEFAULT FALSE;
ALTER TABLE published ADD COLUMN IF NOT EXISTS schema_markup JSONB;

-- Track B2B lead generation status
ALTER TABLE published ADD COLUMN IF NOT EXISTS monetization_cta TEXT;
ALTER TABLE published ADD COLUMN IF NOT EXISTS lead_gen_active BOOLEAN DEFAULT FALSE;
```

---

*IndustrialBriefs — Accuracy. Visibility. Profitability.*
