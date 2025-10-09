# Integrating APS with a Recommendation System

This guide explains how to use the `RecommendationSystemAdapter` to measure and audit the agency impact of your recommendation engine.

## 1. Why Score Recommendations for Agency?

Recommendation systems can significantly influence user choice. A low-agency recommendation might:
-   Create a filter bubble by never showing diverse content.
-   Pressure a user into a purchase with aggressive personalization.
-   Operate as a "black box" with no explanation.

By scoring recommendations with the Agency Preservation Score (APS), you can identify and mitigate these risks, building user trust and providing more meaningful choices.

## 2. Setup and Initialization

First, define the weights for your recommendation domain. This is a critical step: the weights determine what your system values. For a content discovery platform, you might value `serendipity` highly. For a shopping site, `consent` for personalized ads is key.

```python
from afai_lib.adapters.recommendation.adapter import RecommendationSystemAdapter

# Define weights for your recommendation context
REC_SYS_WEIGHTS = {
    # Core Factors
    "consent": 0.4,
    "reversibility": 0.2,
    "transparency": 0.2,
    
    # Custom Factors for Recommendations
    "choice_variety": 0.1, # Does the recommendation show diverse options?
    "serendipity": 0.1     # Does it include surprising but relevant items?
}

# Initialize the adapter
aps_adapter = RecommendationSystemAdapter(weights=REC_SYS_WEIGHTS)
```

## 3. Integration into Your Pipeline

The adapter is designed to run *after* your recommender has generated a list of items but *before* they are displayed to the user. This allows you to decide whether to show the recommendations, modify them, or attach explainability information.

Here is a simplified example:

```python
# 1. Your system generates recommendations
recommended_items = your_recommender.get_recommendations(user_id="user-123")

# 2. Define the "recommendation event" with all relevant data
# This is the data the adapter will use to calculate the score.
recommendation_event = {
    "event_id": "evt-98765",
    "recommender_id": "rec-engine-v3-music",
    "user_id": "user-123",
    "items": [item.id for item in recommended_items],
    "item_count": len(recommended_items),
    
    # Data that maps to APS factors
    "user_opted_in": True, # Did the user agree to personalized recommendations?
    "can_ignore_or_hide": True, # Can the user dismiss the recommendation carousel?
    "explainability_score": 0.7, # How well can your system explain this choice?
    "personalization_score": 85, # How personalized is this? (0-100)
    "choice_variety_score": 0.6, # A metric of how diverse the items are.
    "serendipity_score": 0.4 # A metric for how novel/surprising the items are.
}

# 3. Score the event
aps_results = aps_adapter.score_recommendation_event(recommendation_event, audit=True)

# 4. Use the results
print(f"APS Score: {aps_results['aps_score']}")

# Use the hooks to explain the recommendation to the user
for hook in aps_results['explainability_hooks']:
    print(f"- {hook}")

# For debugging or logging, print the full audit trail
if 'audit_trail' in aps_results:
    print(aps_results['audit_trail'])
```

## 4. Using the Output

The `score_recommendation_event` method returns a dictionary with three key components:

-   `aps_score` (float): The final score. You can use this to set a threshold. For example, you might choose not to display a recommendation block if its score is below `0.4`.
-   `explainability_hooks` (List[str]): A list of simple, human-readable strings. These are designed to be displayed in a "Why am I seeing this?" tooltip next to the recommendations.
-   `audit_trail` (str, optional): A detailed, multi-line string breaking down the entire calculation. This is invaluable for debugging, logging, and ensuring the system is transparent.

By integrating the adapter, you create a feedback loop that makes the agency impact of your recommendation system visible and actionable.
