# Adopting Agency-First AI: Practical Pathways

Adopting the Agency-First AI framework doesn't require you to rebuild your systems from scratch. The goal is to make incremental, meaningful improvements that give your users more control and understanding. This guide offers practical starting points for different types of organizations.

## The Core Idea: Start with Measurement

The first step for any organization is to **measure**. You cannot improve what you cannot see. The Agency Preservation Score (APS) is a tool for seeing how your system impacts user agency. Start by measuring, then move on to improving.

---

## Pathway 1: For a Tech Startup

**Goal:** Integrate APS into your product to build user trust and create a better experience.

Let's say you have a mobile app with a recommendation feed.

1.  **Step 1: Define What Agency Means for Your Users.**
    -   Gather your team and ask: What choices do users have? Where do they lack choice? 
    -   For a recommendation feed, you might identify factors like: "Can users hide a recommendation?", "Do we explain why they see an item?", "Can they opt out of personalization?"

2.  **Step 2: Create Your Initial APS Weights.**
    -   Based on your discussion, assign simple weights to these factors. You can use the `afai_lib` to create a weights dictionary. Don't overthink it; a starting guess is fine.
    -   *Example:* `{"consent": 0.5, "reversibility": 0.3, "transparency": 0.2}`

3.  **Step 3: Score One Interaction, Internally.**
    -   Use the `RecommendationSystemAdapter` to score a single recommendation event from your system. Manually create the `recommendation_event` dictionary with data you already have.
    -   Run the `score_recommendation_event` function and look at the audit trail. This is for your team's eyes only. Does the score feel right? Does the audit trail reveal anything surprising?

4.  **Step 4: Build an Internal Dashboard.**
    -   You don't need to show the score to users yet. Log the APS score for every recommendation your system generates. 
    -   Create a simple internal dashboard that tracks the average APS score over time. Your goal is now simple: **make the number go up.** When you launch a new feature, see how it affects the score.

5.  **Step 5: Expose Agency Features to Users.**
    -   Use the `explainability_hooks` from the adapter to add a "Why am I seeing this?" feature. This is a concrete, user-facing improvement that directly improves your APS score.

---

## Pathway 2: For a Public Institution

**Goal:** Audit a third-party AI system (e.g., for loan approvals or resource allocation) to ensure it treats citizens fairly.

1.  **Step 1: Define Your Agency Principles as Policy.**
    -   Your organization likely has policies about fairness, transparency, and due process. Translate these into AFAI terms. 
    -   *Example Policy:* "Citizens must be able to understand the reason for an automated decision" (Transparency), and "There must be a clear process to appeal a decision" (Reversibility).

2.  **Step 2: Demand Data for Auditing.**
    -   As part of your procurement or review process, require the AI vendor to provide the necessary data points to calculate an APS score for each decision.
    -   This includes not just the decision itself, but the data that went into it and the explanations available to the end-user.

3.  **Step 3: Conduct a Retroactive Audit.**
    -   Take a sample of past decisions made by the system. Use an AFAI adapter (or build a simple one) to score each decision.
    -   The audit trail is your primary output. It provides a clear, documented record of how the system treated a citizen in each case.

4.  **Step 4: Set a Minimum APS Threshold.**
    -   Based on your audit, establish a minimum acceptable APS score for this type of automated decision. This score becomes a clear, enforceable requirement in your contracts and service-level agreements (SLAs).
    -   A low score is not necessarily a failure, but it signals that a human review is required.

---

## Pathway 3: For an Open-Source Project

**Goal:** Embed agency-first principles into the design and governance of your project.

1.  **Step 1: Adopt a Governance Model that Distributes Power.**
    -   Your project's governance is a system that impacts the agency of your contributors. Use the AFAI `GOVERNANCE.md` as a template.
    -   Ensure you have clear rules for how decisions are made and how dissent is handled. The "right to fork" is the ultimate guarantee of contributor agency.

2.  **Step 2: Create an "Agency-First" Design Guide.**
    -   Create a document in your repository (e.g., `DESIGN_PRINCIPLES.md`) that outlines how to apply agency principles to your specific domain.
    -   Ask questions like: "Does this feature give the user more control or take it away?", "Is this feature transparent by default?"

3.  **Step 3: Use APS in Pull Request Reviews.**
    -   When a contributor proposes a new feature that impacts the user experience, ask them to include a brief "Agency Impact" section in their PR description.
    -   They don't need to calculate a formal score, but they should explain how their change affects factors like user consent, reversibility, and transparency. This makes agency a conscious part of the development process.
