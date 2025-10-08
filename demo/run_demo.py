import csv
import logging
import random
from pathlib import Path

# Seed for reproducibility, ensuring every run with this seed is identical.
# This is crucial for auditable and transparent demonstrations.
random.seed(42)

# --- APS Calculation ---
# The Agency Preservation Score (APS) is a placeholder metric to quantify
# how an AI's action impacts human agency. It is a value between 0 and 1.
#
# It is calculated based on three core principles:
# 1. Transparency: Is the AI's reasoning clear? (0-1)
# 2. Consent: Was informed, revocable consent obtained? (0-1)
# 3. Reversibility: Can the action be easily undone? (0-1)
#
# APS = (Transparency + Consent + Reversibility) / 3
def calculate_aps(transparency, consent, reversibility):
    """Calculates the Agency Preservation Score."""
    return (transparency + consent + reversibility) / 3

class AIAgent:
    """A simple AI agent that performs a decision task."""

    def __init__(self, agent_id):
        self.agent_id = agent_id

    def perform_action(self):
        """Simulates the agent performing an action with varying impacts on agency."""
        actions = [
            "Suggest a purchase",
            "Auto-correct a document",
            "Book a non-refundable flight",
        ]
        action = random.choice(actions)

        # These values are placeholders to simulate different scenarios.
        if action == "Suggest a purchase":
            # High agency: transparent suggestion, requires consent, easily ignored.
            transparency = 0.9
            consent = 1.0  # User must approve
            reversibility = 1.0 # User can just not buy it
        elif action == "Auto-correct a document":
            # Medium agency: less transparent, implicit consent, but reversible.
            transparency = 0.5
            consent = 0.5  # Implicit consent by using the feature
            reversibility = 0.8 # Can undo
        else: # "Book a non-refundable flight"
            # Low agency: decision made with low transparency, questionable consent, and is irreversible.
            transparency = 0.2
            consent = 0.1 # Assumed consent from a vague preference
            reversibility = 0.0 # Non-refundable

        aps_score = calculate_aps(transparency, consent, reversibility)

        return {
            "action": action,
            "aps_score": aps_score,
            "reversibility": reversibility > 0.5,
            "consent_involved": consent > 0.5,
        }

def run_simulation(num_agents=3):
    """Runs the full simulation and outputs the results."""
    output_dir = Path("demo/outputs")
    output_dir.mkdir(exist_ok=True)

    log_file = output_dir / "logs.txt"
    csv_file = output_dir / "demo_runs.csv"

    # Setup logging for auditable logs
    logging.basicConfig(filename=log_file, level=logging.INFO, filemode='w',
                        format='%(asctime)s - %(message)s')

    logging.info("Starting AFAI Demo Simulation...")

    agents = [AIAgent(f"Agent-{i+1}") for i in range(num_agents)]
    results = []

    for agent in agents:
        result = agent.perform_action()
        logging.info(f"{agent.agent_id} performed action: '{result['action']}' with APS: {result['aps_score']:.2f}")
        results.append({
            "Agent ID": agent.agent_id,
            "Action": result["action"],
            "APS Score": f"{result['aps_score']:.2f}",
            "Reversibility": result["reversibility"],
            "Consent Involved": result["consent_involved"],
        })

    # Write results to CSV
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["Agent ID", "Action", "APS Score", "Reversibility", "Consent Involved"])
        writer.writeheader()
        writer.writerows(results)

    logging.info(f"Simulation complete. Results saved to {csv_file}")
    print(f"Simulation complete. View outputs in {output_dir.resolve()}")


if __name__ == "__main__":
    run_simulation()