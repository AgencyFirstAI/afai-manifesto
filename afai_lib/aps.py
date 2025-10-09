"""
Agency First AI (AFAI) - Agency Preservation Score (APS) Library

This module provides the core functionality for calculating and auditing
the Agency Preservation Score (APS).
"""

from dataclasses import asdict
from .models import APSInput

def calculate_weighted_aps(aps_input, weights):
    """
    Calculates a weighted Agency Preservation Score (APS) based on a structured input and corresponding weights.

    Args:
        aps_input (APSInput): A structured data object containing the core and custom factors.
        weights (dict): A dictionary where keys match the factor names in `aps_input`
                        (e.g., 'consent', 'transparency', 'custom_factor_name')
                        and values are the weights (float).

    Returns:
        tuple: A tuple containing the final APS score (float) and a dictionary
               with the detailed breakdown of the calculation for auditing.
    """
    
    all_factors = asdict(aps_input)
    # Separate custom factors for clarity in the audit trail
    custom_factors = all_factors.pop('custom_factors', {})
    all_factors.update(custom_factors)

    weighted_scores = {}
    total_weight = 0

    for factor, value in all_factors.items():
        if factor in weights:
            weight = weights[factor]
            total_weight += abs(weight)
            if isinstance(value, bool):
                # Convert boolean to 1 for True, -1 for False for scoring
                score_value = 1 if value else -1
                weighted_scores[factor] = score_value * weight
            elif isinstance(value, (int, float)):
                # For numeric values (like transparency), scale them from [0, 1] to [-1, 1]
                score_value = 2 * value - 1
                weighted_scores[factor] = score_value * weight

    if total_weight == 0:
        return 0.5, {"error": "No matching weights provided."}

    total_score = sum(weighted_scores.values())
    
    # Normalize the score to be between -1 and 1
    normalized_score = total_score / total_weight

    # Shift the score to be between 0 and 1
    final_score = (normalized_score + 1) / 2

    audit_details = {
        "factors": all_factors,
        "weights": weights,
        "weighted_scores": weighted_scores,
        "total_score": total_score,
        "total_weight": total_weight,
        "normalized_score": normalized_score,
        "final_score": final_score
    }

    return max(0, min(1, round(final_score, 2))), audit_details

def generate_aps_audit_trail(agent_id, action, aps_score, audit_details):
    """
    Generates a detailed, human-readable audit trail for an APS calculation.

    Args:
        agent_id (str): The identifier for the AI agent.
        action (str): A description of the action being evaluated.
        aps_score (float): The final calculated APS score.
        audit_details (dict): The detailed breakdown from the `calculate_weighted_aps` function.

    Returns:
        str: A formatted string containing the detailed APS audit trail.
    """
    report = f"--- AFAI Agency Preservation Score (APS) Audit Trail ---\n\n"
    report += f"Agent ID: {agent_id}\n"
    report += f"Action:   {action}\n"
    report += f"Final APS Score: {aps_score:.2f}\n\n"
    report += "--- Calculation Breakdown ---\n"
    report += "{:<20} {:<10} {:<10} {:<15}\n".format("Factor", "Value", "Weight", "Weighted Score")
    report += "-" * 55 + "\n"

    factors = audit_details.get('factors', {})
    weights = audit_details.get('weights', {})
    weighted_scores = audit_details.get('weighted_scores', {})

    for factor in factors.keys():
        if factor in weights:
            value = factors[factor]
            weight = weights[factor]
            score = weighted_scores.get(factor, 0)
            report += "{:<20} {:<10} {:<10} {:<15.2f}\n".format(
                factor,
                str(value),
                f"{weight:.2f}",
                score
            )

    report += "\n--- Summary ---\n"
    report += f"Total Score:      {audit_details.get('total_score', 0):.2f}\n"
    report += f"Total Weight:     {audit_details.get('total_weight', 0):.2f}\n"
    report += f"Normalized Score: {audit_details.get('normalized_score', 0):.2f} (Total Score / Total Weight)\n"
    report += f"Final Score:      {audit_details.get('final_score', 0):.2f} ((Normalized Score + 1) / 2)\n"
    report += "\n--- End of Audit Trail ---\n"
    return report