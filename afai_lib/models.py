"""
Data models for the Agency First AI (AFAI) framework.
"""
from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class APSInput:
    """
    A structured input for calculating the Agency Preservation Score (APS).

    This class standardizes the core factors of agency while allowing for
    domain-specific extensions.

    Attributes:
        consent (bool): Did the user provide informed, revocable consent?
        reversibility (bool): Can the user easily undo the action?
        transparency (float): How clear and understandable is the AI's reasoning?
                              (A value from 0.0 for opaque to 1.0 for fully transparent).
        custom_factors (Dict[str, Any]): A dictionary for additional domain-specific
                                         factors. Keys are factor names and values
                                         can be bools or floats.
    """
    consent: bool
    reversibility: bool
    transparency: float
    custom_factors: Dict[str, Any] = field(default_factory=dict)
