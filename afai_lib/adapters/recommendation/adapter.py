"""
Agency-First AI (AFAI) Domain Adapter for Recommendation Systems.

This adapter provides a structured way to calculate the Agency Preservation Score (APS)
for interactions within a recommendation system.
"""

from typing import List, Dict, Any
import sys
import os

# Add the root library to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from afai_lib.models import APSInput
from afai_lib.aps import calculate_weighted_aps, generate_aps_audit_trail

class RecommendationSystemAdapter:
    """
    An adapter to calculate and audit the APS for a recommendation event.

    This class is designed to be integrated into a recommendation system's
    post-processing pipeline. It takes data about the recommendation and
    maps it to agency-preserving factors.
    """

    def __init__(self, weights: Dict[str, float]):
        """
        Initializes the adapter with a specific set of weights for the APS calculation.

        Args:
            weights (Dict[str, float]): A dictionary of weights for the APS factors
                                       (e.g., {"consent": 0.5, "reversibility": 0.3, ...}).
        """
        if not weights:
            raise ValueError("Weights dictionary cannot be empty.")
        self.weights = weights

    def _collect_data(self, recommendation_event: Dict[str, Any]) -> Dict[str, Any]:
        """
        Placeholder method to collect and normalize data from a recommendation event.

        In a real implementation, this method would extract relevant signals from
        the recommender's output, user profile, and UI context.

        Args:
            recommendation_event (Dict[str, Any]): A dictionary containing all data
                related to the recommendation (e.g., items shown, user query,
                UI placement, personalization level).

        Returns:
            Dict[str, Any]: A dictionary of processed and normalized data points.
        """
        print(f"(Placeholder) Collecting data from event: {recommendation_event.get('event_id')}")
        # Example: Normalize personalization from a scale of 1-100 to 0-1
        if 'personalization_score' in recommendation_event:
            recommendation_event['personalization_level'] = recommendation_event['personalization_score'] / 100
        return recommendation_event

    def _map_to_aps_factors(self, processed_data: Dict[str, Any]) -> APSInput:
        """
        Maps the collected data to the standardized APSInput data model.

        This is the core logic of the adapter, translating domain-specific metrics
        into universal agency factors.

        Args:
            processed_data (Dict[str, Any]): The output from the _collect_data method.

        Returns:
            APSInput: A structured APSInput object.
        """
        # --- Default assumptions (to be overridden by event data) ---
        consent = processed_data.get('user_opted_in', False)
        reversibility = processed_data.get('can_ignore_or_hide', True)
        
        # Transparency is a calculated field based on multiple inputs
        explainability_score = processed_data.get('explainability_score', 0.0) # e.g., 0.0 to 1.0
        personalization_level = processed_data.get('personalization_level', 0.0) # e.g., 0.0 to 1.0
        # Transparency is high if explainability is high and personalization is low
        transparency = max(0, min(1, explainability_score - (personalization_level * 0.2)))

        # Custom factors specific to recommendation systems
        custom_factors = {
            "choice_variety": processed_data.get('choice_variety_score', 0.5),
            "serendipity": processed_data.get('serendipity_score', 0.2)
        }

        return APSInput(
            consent=consent,
            reversibility=reversibility,
            transparency=transparency,
            custom_factors=custom_factors
        )

    def _get_explainability_hooks(self, audit_details: Dict[str, Any]) -> List[str]:
        """
        Generates human-readable explanations based on the audit details.

        These hooks can be used to populate a "Why am I seeing this?" UI element.

        Args:
            audit_details (dict): The detailed breakdown from the APS calculation.

        Returns:
            List[str]: A list of strings explaining the score.
        """
        explanations = []
        final_score = audit_details.get('final_score', 0)
        factors = audit_details.get('factors', {})

        if final_score > 0.75:
            explanations.append("This recommendation respects your agency.")
        elif final_score < 0.4:
            explanations.append("This recommendation may be overly intrusive.")

        if not factors.get('consent'):
            explanations.append("It was presented without your explicit prior consent.")
        if factors.get('transparency', 0) < 0.5:
            explanations.append("The reasoning behind it may not be fully clear.")
        
        return explanations

    def score_recommendation_event(self, event: Dict[str, Any], audit: bool = False) -> Dict[str, Any]:
        """
        Scores a single recommendation event and returns a results dictionary.

        This is the main public method of the adapter.

        Args:
            event (Dict[str, Any]): The raw data for the recommendation event.
            audit (bool): If True, a detailed audit trail will be generated and included.

        Returns:
            Dict[str, Any]: A dictionary containing the final APS score, explainability hooks,
                            and an optional audit trail.
        """
        processed_data = self._collect_data(event)
        aps_input = self._map_to_aps_factors(processed_data)
        
        aps_score, audit_details = calculate_weighted_aps(aps_input, self.weights)
        
        results = {
            "event_id": event.get("event_id"),
            "aps_score": aps_score,
            "explainability_hooks": self._get_explainability_hooks(audit_details)
        }

        if audit:
            results['audit_trail'] = generate_aps_audit_trail(
                agent_id=event.get("recommender_id", "unknown_recommender"),
                action=f"recommend_items:{event.get('item_count')}",
                aps_score=aps_score,
                audit_details=audit_details
            )
        
        return results
