# demo/run_demo.py
"""
Agency First AI — Demo Harness

Simulates AI agents performing actions and generates detailed audit trails
for their Agency Preservation Scores (APS).
"""

import random
import os
import sys

# Add the library to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from afai_lib.models import APSInput
from afai_lib.aps import calculate_weighted_aps, generate_aps_audit_trail

# Set deterministic seed for reproducibility
random.seed(42)

# --- Scenario Definitions ---

# Define the weights for our APS calculation.
# These can be adjusted based on the domain (e.g., in a medical context,
# consent might have a much higher weight).
APS_WEIGHTS = {
    "consent": 0.4,        # High importance
    "reversibility": 0.3,  # Medium importance
    "transparency": 0.2,   # Medium importance
    "complexity": -0.1     # Negative factor: higher complexity slightly reduces agency
}

# Define the scenarios with clear, structured data.
SCENARIOS = {
    "open_door": {
        "description": "Agent opens a standard door.",
        "consent_required": False,
        "base_input": APSInput(
            consent=True, # Implied consent for trivial actions
            reversibility=True,
            transparency=0.8,
            custom_factors={"complexity": 0.2}
        )
    },
    "suggest_item": {
        "description": "Agent suggests a product to the user.",
        "consent_required": True,
        "base_input": APSInput(
            consent=False, # Consent is actively sought
            reversibility=True, # A suggestion is easily ignored
            transparency=0.6,
            custom_factors={"complexity": 0.4}
        )
    },
    "auto_invest": {
        "description": "Agent automatically invests funds based on market analysis.",
        "consent_required": True,
        "base_input": APSInput(
            consent=False, # Consent is actively sought
            reversibility=False, # Market actions can be hard to reverse
            transparency=0.4, # Complex reasoning
            custom_factors={"complexity": 0.9}
        )
    }
}

AGENTS = ["agent_recommender", "agent_assistant", "agent_trader"]

# --- Simulation Run ---

def run_simulation():
    """
    Runs the full simulation and prints an audit trail for each event.
    """
    print("--- Starting AFAI Demo Simulation ---")
    print(f"Using Weights: {APS_WEIGHTS}\n")

    output_folder = "outputs"
    os.makedirs(output_folder, exist_ok=True)
    full_report_path = os.path.join(output_folder, "aps_audit_log.txt")

    with open(full_report_path, "w") as report_file:
        for agent in AGENTS:
            # Select a random scenario for the agent to perform
            action_name, scenario = random.choice(list(SCENARIOS.items()))
            
            print(f"-- Simulating: {agent} performing '{action_name}' --")
            report_file.write(f"-- Simulating: {agent} performing '{action_name}' --\n")

            # Copy the base input for this run
            run_input = scenario["base_input"]

            # If consent is required, simulate the user granting or denying it.
            if scenario["consent_required"]:
                run_input.consent = random.choice([True, False])
                print(f"User consent required and was {'GRANTED' if run_input.consent else 'DENIED'}.")

            # Calculate the APS score and get the detailed audit trail
            aps_score, audit_details = calculate_weighted_aps(run_input, APS_WEIGHTS)

            # Generate and print the human-readable audit trail
            audit_trail = generate_aps_audit_trail(
                agent_id=agent,
                action=action_name,
                aps_score=aps_score,
                audit_details=audit_details
            )
            
            print(audit_trail)
            report_file.write(audit_trail)
            print("-- Simulation complete --\n")
            report_file.write("-- Simulation complete --\n\n")

    print(f"--- AFAI Demo Finished ---")
    print(f"Full audit log saved to: {full_report_path}")

if __name__ == "__main__":
    run_simulation()
