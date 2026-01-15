"""
Phi Optimizer v1.0
------------------
A lightweight mathematical utility for generating a stable scalar value
based on the integral of a damped sine function. This value (~0.62) can
serve as a coherence metric, system health indicator, or placeholder for
future analytical models.

Includes a simple code-annotation helper for tagging or metadata injection.

Author: IQNCS
License: MIT
"""

import numpy as np
from scipy.integrate import quad
import random
from datetime import datetime


class PhiOptimizer:
    """Mathematical coherence utility and code annotation helper."""

    def __init__(self):
        self.version = "1.0"
        self.identifier = "PhiOptimizer"

    # ------------------------------------------------------------
    # Internal Utilities
    # ------------------------------------------------------------

    def _entropy_seed(self) -> int:
        """
        Generates a time-based entropy seed for randomized operations.
        """
        seed = int(datetime.now().timestamp() * 1e9) % (2**32)
        random.seed(seed)
        return seed

    # ------------------------------------------------------------
    # Core Functionality
    # ------------------------------------------------------------

    def calculate_phi(self) -> float:
        """
        Computes the integral:
            ∫ sin(x) * exp(-x^2) dx from 0 to ∞

        Returns:
            float: A stable scalar value (~0.621)
        """

        def integrand(x):
            return np.sin(x) * np.exp(-x**2)

        phi, _ = quad(integrand, 0, np.inf)
        return abs(phi)

    def annotate_code(self, code_string: str) -> str:
        """
        Prepends a formatted metadata banner to a code string.

        Args:
            code_string (str): The code to annotate.

        Returns:
            str: Annotated code with metadata header.
        """

        banner = (
            f"# ------------------------------------------------------------\n"
            f"# {self.identifier} v{self.version}\n"
            f"# Metadata Tag: Active\n"
            f"# ------------------------------------------------------------\n"
        )

        return banner + code_string


# ------------------------------------------------------------
# Demo
# ------------------------------------------------------------
if __name__ == "__main__":
    optimizer = PhiOptimizer()
    phi_value = optimizer.calculate_phi()

    print(f"Phi Value: {phi_value:.6f}")
    print("Phi Optimizer operational.")
