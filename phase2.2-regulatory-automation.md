# IndustrialBriefs — Phase 2.2: Regulatory Automation & Accuracy Strategy
**GPT Memory Context File | Created: April 2026**

---

## 🎯 Objective
Upgrade the newsroom to a fully automated "Regulatory Intelligence Engine" that monitors, analyzes, and publishes high-accuracy reports on industry-specific acts (e.g., EU AI Act, OSHA AI regulations, CHIPS Act) with zero human intervention and 99% accuracy.

---

## 🏗️ The Regulatory Pipeline Architecture

To handle the complexity of legal/regulatory text, we split the pipeline into two tracks:

### Track A: The "Fast-Track" News (Standard)
*   **Trigger**: RSS/News feeds.
*   **Goal**: Speed.
*   **Agent**: Scout -> Writer -> SEO -> Publisher.

### Track B: The "Regulatory Intelligence" Track (Deep)
*   **Trigger**: Government gazettes, official PDF releases, specialized legal RSS.
*   **Goal**: Accuracy & Depth.
*   **Workflow**:
    1.  **Scout Agent**: Detects "High-Impact Regulation" (keyword: "Act", "Regulation", "Mandate", "Compliance").
    2.  **Research Agent (NEW)**: Fetches the FULL text (PDF/Web). Extracts specific impact clauses for AECM sectors.
    3.  **Accuracy Agent (NEW)**: Cross-references the Research Agent's output against the raw source to flag "Hallucinations".
    4.  **Writer Agent**: Synthesizes the findings into the "Policy Wire" Axios-style briefing.
    5.  **SEO & Publisher**: Standard flow.

---

## 🔍 Automated Verification Protocol (Accuracy First)

Since regulatory reporting is high-stakes, we implement an **Automated Fact-Check Loop**:

1.  **The "Adversarial" Check**: Before publishing, a second LLM (e.g., Claude 3.5 Sonnet) is given the raw source and the generated article. It must answer: "Does this article claim anything NOT in the source?"
2.  **The "Confidence Score"**: If the Accuracy Agent returns a score < 0.9, the article is automatically moved to a `human_review` queue in Supabase and a Slack notification is triggered.
3.  **Source Citations**: Every regulatory post MUST include direct links to the specific section/page of the official document.

---

## 🤖 Specialized Agent: The "Regulatory Researcher"

**Model**: GPT-4o (Large context window for long PDFs).

**Task**: 
*   Identify the **AECM sectors** affected (Architecture, Construction, Engineering, Manufacturing).
*   Extract **Deadlines** (e.g., "Effective Date", "Grace Period").
*   Identify **Compliance Requirements** (What do companies actually HAVE to do?).
*   Translate "Legalese" into "Industry Impact" (What does this mean for a project manager on-site?).

---

## 📢 Automated B2B Distribution (LinkedIn)

To drive high-value traffic without manual work:

1.  **LinkedIn Distribution Agent**:
    *   **Input**: Published article content + SEO Focus Keyword.
    *   **Action**: Generates a professional LinkedIn post using the "Problem-Impact-Solution" framework.
    *   **Optimization**: Includes relevant AECM hashtags (#AECM, #ConstructionTech, #AIPolicy).
    *   **Trigger**: Fires immediately after the Ghost post status changes to `published`.

---

## 📅 Roadmap for Phase 2.2

1.  **Week 1**: Deploy the `Accuracy Agent` (The Fact-Checker).
2.  **Week 2**: Integrate `PDF-to-Text` capabilities into the Scout/Research agents.
3.  **Week 3**: Build the `LinkedIn Distribution Agent` in n8n.
4.  **Week 4**: Launch the "Policy Wire" newsletter segment (fully automated).

---

## 📋 New Database Requirements (`regulation_intel` table)

```sql
CREATE TABLE regulation_intel (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    source_id TEXT UNIQUE,
    act_name TEXT,
    impact_level TEXT, -- High, Medium, Low
    sectors_affected TEXT[], -- ['Construction', 'Manufacturing']
    key_deadlines JSONB,
    raw_summary TEXT,
    accuracy_score FLOAT,
    status TEXT DEFAULT 'pending' -- 'verified', 'human_review', 'published'
);
```

---

*IndustrialBriefs — Accuracy is our Authority.*
