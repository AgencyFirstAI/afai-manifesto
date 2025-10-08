# demo/run_demo.py
"""
Agency First AI — Demo Harness
Simulates AI agents performing simple actions and calculates Agency Preservation Scores (APS).

This is a Week 1 prototype for reproducibility and demonstration.
"""

import csv
import random
import os

# Set deterministic seed for reproducibility
random.seed(42)

# Demo agents and actions
agents = ["agent_1", "agent_2", "agent_3"]
actions = ["open_door", "pick_item", "interact_npc", "wait"]

# Prepare outputs folder
output_folder = "outputs"
os.makedirs(output_folder, exist_ok=True)

# CSV output file
csv_file = os.path.join(output_folder, "demo_runs.csv")
log_file = os.path.join(output_folder, "logs.txt")

# APS calculation placeholder function
def calculate_aps(action):
    """
    Placeholder APS calculation:
    - Returns score 0-1 for agency preservation
    - Randomly assign reversibility and consent for demonstration
    """
    aps_score = round(random.uniform(0.5, 1.0), 2)  # high preservation
    reversible = random.choice([True, False])
    consent = random.choice([True, False])
    return aps_score, reversible, consent

# Run demo and collect results
results = []
with open(log_file, "w") as log:
    for agent in agents:
        for action in actions:
            aps_score, reversible, consent = calculate_aps(action)
            results.append([agent, action, aps_score, reversible, consent])
            log.write(f"{agent} performed {action} | APS={aps_score}, Reversible={reversible}, Consent={consent}\n")

# Write results to CSV
with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Agent ID", "Action", "APS Score", "Reversible", "Consent"])
    writer.writerows(results)

print(f"Demo complete. CSV output: {csv_file}, Log: {log_file}")
