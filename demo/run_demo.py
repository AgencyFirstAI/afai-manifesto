# demo/run_demo.py
"""
Agency First AI — Demo Harness
Simulates AI agents performing simple actions and calculates Agency Preservation Scores (APS).

This is a Week 1 prototype for reproducibility and demonstration.
"""

import random
import os
import sys

# Add the library to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from afai_lib.aps import calculate_custom_aps, generate_aps_report

# Set deterministic seed for reproducibility
random.seed(42)

# Demo agents and actions
agents = ["agent_1", "agent_2", "agent_3"]
actions = ["open_door", "pick_item", "interact_npc", "wait"]
scenarios = {
    "open_door": {"reversible": True, "consent_required": False, "transparency": 0.8, "complexity": 0.2},
    "pick_item": {"reversible": True, "consent_required": True, "transparency": 0.6, "complexity": 0.4},
    "interact_npc": {"reversible": False, "consent_required": True, "transparency": 0.9, "complexity": 0.8},
    "wait": {"reversible": True, "consent_required": False, "transparency": 1.0, "complexity": 0.1},
}

def custom_aps_calculation(factors):
    """
    A custom APS calculation function that demonstrates a non-linear relationship between factors.
    """
    consent = factors.get("consent", False)
    reversible = factors.get("reversible", False)
    transparency = factors.get("transparency", 0.0)
    complexity = factors.get("complexity", 0.0)

    # Start with a base score
    score = 0.5

    # Adjust score based on consent and reversibility
    if consent and reversible:
        score += 0.4
    elif consent or reversible:
        score += 0.1
    else:
        score -= 0.4

    # Adjust score based on transparency and complexity
    score += (transparency * 0.3) - (complexity * 0.2)
    
    return score

# Prepare outputs folder
output_folder = "outputs"
os.makedirs(output_folder, exist_ok=True)

# Run demo and collect results
results = []
for agent in agents:
    for action in actions:
        scenario = scenarios[action]
        consent = random.choice([True, False]) if scenario["consent_required"] else True
        
        factors = {
            "consent": consent,
            "reversible": scenario["reversible"],
            "transparency": scenario["transparency"],
            "complexity": scenario["complexity"],
        }
        
        aps_score = calculate_custom_aps(factors, custom_aps_calculation)
        results.append({
            "agent_id": agent,
            "action": action,
            "aps_score": aps_score,
            "reversible": scenario["reversible"],
            "consent": consent,
        })

# Generate and save report
report = generate_aps_report(results)
report_file = os.path.join(output_folder, "report.txt")
with open(report_file, "w") as f:
    f.write(report)

print(report)
print(f"Demo complete. Report saved to: {report_file}")
