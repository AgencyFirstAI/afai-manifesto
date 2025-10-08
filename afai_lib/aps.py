"""
Agency First AI (AFAI) - Agency Preservation Score (APS) Library
"""

def calculate_aps(consent, reversible):
    """
    Calculates the Agency Preservation Score (APS) based on whether consent was given and whether the action is reversible.

    Args:
        consent (bool): Whether the user gave informed consent for the action.
        reversible (bool): Whether the action can be easily undone.

    Returns:
        float: The Agency Preservation Score (APS) between 0.0 and 1.0.
    """
    base_score = 0.5

    # Adjust score based on consent
    if consent:
        base_score += 0.25
    else:
        base_score -= 0.25

    # Adjust score based on reversibility
    if reversible:
        base_score += 0.25
    else:
        base_score -= 0.25

    # Ensure the score is within the 0-1 range
    return max(0, min(1, round(base_score, 2)))

def calculate_weighted_aps(factors, weights):
    """
    Calculates a weighted Agency Preservation Score (APS) based on a dictionary of factors and their corresponding weights.

    Args:
        factors (dict): A dictionary where keys are the names of the factors (e.g., "consent", "reversibility")
                        and values are boolean or float values representing the factor's state.
        weights (dict): A dictionary where keys are the names of the factors and values are the weights (float)
                        to be applied to each factor.

    Returns:
        float: The weighted Agency Preservation Score (APS) between 0.0 and 1.0.
    """
    total_score = 0
    total_weight = 0

    for factor, value in factors.items():
        if factor in weights:
            weight = weights[factor]
            total_weight += abs(weight)
            if isinstance(value, bool):
                total_score += weight if value else -weight
            else:
                total_score += value * weight

    if total_weight == 0:
        return 0.5  # Default score if no weights are provided

    # Normalize the score to be between -1 and 1
    normalized_score = total_score / total_weight

    # Shift the score to be between 0 and 1
    final_score = (normalized_score + 1) / 2

    return max(0, min(1, round(final_score, 2)))

def generate_aps_report(results):
    """
    Generates a text-based report of Agency Preservation Scores (APS).

    Args:
        results (list): A list of dictionaries, where each dictionary contains the following keys:
                        'agent_id', 'action', 'aps_score', 'reversible', 'consent'.

    Returns:
        str: A formatted string containing the APS report.
    """
    report = """--- AFAI Agency Preservation Score (APS) Report ---

"""
    report += "{:<10} {:<15} {:<10} {:<12} {:<10}\n".format("Agent ID", "Action", "APS Score", "Reversible", "Consent")
    report += "-" * 60 + "\n"

    for result in results:
        report += "{:<10} {:<15} {:<10.2f} {:<12} {:<10}\n".format(
            result['agent_id'],
            result['action'],
            result['aps_score'],
            str(result['reversible']),
            str(result['consent'])
        )

    report += "\n--- End of Report ---\n"
    return report

def calculate_custom_aps(factors, calculation_function):
    """
    Calculates the Agency Preservation Score (APS) using a custom, user-defined function.

    Args:
        factors (dict): A dictionary of factors to be used in the calculation.
        calculation_function (function): A function that takes a dictionary of factors as input
                                         and returns the APS score (a float between 0.0 and 1.0).

    Returns:
        float: The Agency Preservation Score (APS) between 0.0 and 1.0.
    """
    aps_score = calculation_function(factors)
    return max(0, min(1, round(aps_score, 2)))