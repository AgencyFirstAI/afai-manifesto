---
layout: post
title:  "Understanding the Agency Preservation Score (APS)"
date:   2025-10-09 11:00:00 -0500
categories: afai
---

The Agency Preservation Score (APS) is at the heart of the Agency First AI (AFAI) framework. It's a quantifiable metric designed to measure the impact of an AI system on a user's ability to make their own choices. But what exactly is the APS, and how is it calculated?

At its core, the APS is a number between 0.0 and 1.0, where 1.0 represents perfect preservation of agency and 0.0 represents complete erosion of agency. The score is calculated based on a variety of factors, each of which represents a different dimension of agency.

In our initial prototype, we've focused on three key factors:

*   **Consent:** Did the user make an informed and revocable choice to interact with the AI?
*   **Reversibility:** Can the user easily undo the effects of the AI's action?
*   **Transparency:** Is the AI's reasoning clear and understandable to the user?

We believe that these three factors provide a solid foundation for measuring agency. However, we also recognize that they are just the beginning. As we continue to develop the AFAI framework, we plan to incorporate more sophisticated and context-aware variables into the APS calculation.

Our goal is to create a flexible and extensible system that can be adapted to a wide range of AI applications. By providing a standardized way to measure agency, we hope to empower developers to build AI systems that are not only powerful and intelligent, but also respectful of human autonomy.

In our next blog post, we'll take a closer look at the `calculate_weighted_aps` function in our `afai_lib` library and explore how it can be used to create more nuanced and configurable APS calculations.
