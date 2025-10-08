# demo/run_demo.py
"""
Agency First AI — Demo Harness
Simulates AI agents performing simple actions and calculates Agency Preservation Scores (APS).

This is a Week 1 prototype for reproducibility and demonstration.
"""

import csv
import random
import os
import sys

# Add the library to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from afai_lib.aps import calculate_weighted_aps

# Set deterministic seed for reproducibility
random.seed(42)

# Demo agents and actions
agents = ["agent_1", "agent_2", "agent_3"]
actions = ["open_door", "pick_item", "interact_npc", "wait"]
scenarios = {
    "open_door": {"reversible": True, "consent_required": False, "transparency": 0.8},
    "pick_item": {"reversible": True, "consent_required": True, "transparency": 0.6},
    "interact_npc": {"reversible": False, "consent_required": True, "transparency": 0.9},
    "wait": {"reversible": True, "consent_required": False, "transparency": 1.0},
}
weights = {
    "consent": 0.4,
    "reversible": 0.3,
    "transparency": 0.3,
}


# Prepare outputs folder
output_folder = "outputs"
os.makedirs(output_folder, exist_ok=True)

# CSV output file
csv_file = os.path.join(output_folder, "demo_runs.csv")
log_file = os.path.join(output_folder, "logs.txt")

# Run demo and collect results
results = []
with open(log_file, "w") as log:
    for agent in agents:
        for action in actions:
            scenario = scenarios[action]
            consent = random.choice([True, False]) if scenario["consent_required"] else True
            
            factors = {
                "consent": consent,
                "reversible": scenario["reversible"],
                "transparency": scenario["transparency"],
            }
            
            aps_score = calculate_weighted_aps(factors, weights)
            results.append([agent, action, aps_score, scenario["reversible"], consent])
            log.write(f"{agent} performed {action} | APS={aps_score}, Reversible={scenario['reversible']}, Consent={consent}\n")

# Write results to CSV
with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Agent ID", "Action", "APS Score", "Reversible", "Consent"])
    writer.writerows(results)

print(f"Demo complete. CSV output: {csv_file}, Log: {log_file}")
