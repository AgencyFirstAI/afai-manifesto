# How to Contribute to the Agency-First AI Manifesto

First, thank you for considering a contribution. Your involvement is critical to building a framework that genuinely preserves human agency. This document outlines the process and standards for contributing to ensure the project remains transparent, auditable, and resilient.

## Contribution Philosophy

Our contribution process mirrors the principles of AFAI itself:

-   **Transparency:** All significant changes are proposed and discussed publicly.
-   **Optionality:** These are guidelines, not immutable laws. They can be challenged and changed through the governance process.
-   **Reversibility:** A clear Git history and versioning allow us to revert changes that prove to be detrimental.

## Standard Contribution Workflow

For documentation, bug fixes, new adapters, or demo improvements, follow this process:

1.  **Fork the Repository:** Create your own copy of the repository to work on.
2.  **Create a Feature Branch:** Create a new branch with a descriptive name (e.g., `git checkout -b feat/new-decision-support-adapter`).
3.  **Make Your Changes:** Write your code or documentation. Adhere to the standards below.
4.  **Add Tests:** If you add code, you must add tests that validate its functionality.
5.  **Update Documentation:** If your change affects behavior or adds a feature, update the relevant documentation.
6.  **Submit a Pull Request (PR):** Push your branch to your fork and submit a PR to the main repository. The PR description should clearly explain the **why** behind your change.

## Standards and Conventions

-   **Code Style:** We use standard Python style (PEP 8). Code should be clear, well-commented, and readable.
-   **Commit Messages:** Follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification. This helps us automate versioning and makes the project history auditable.
-   **Documentation:** All new modules, classes, and functions must have clear docstrings explaining their purpose, arguments, and return values.

## Proposing Changes to the APS Core

The Agency Preservation Score (APS) is the heart of this framework. Changes to its core factors, calculation logic, or the `APSInput` model are subject to a more rigorous process to ensure stability and prevent capture.

1.  **Create an APS Proposal Issue:** Before writing any code, open an Issue on GitHub with the title `APS Proposal: [Your Change]`. 
2.  **Justify the Change:** The proposal must include:
    -   **The Problem:** What specific deficiency does the current APS model have?
    -   **The Proposed Solution:** A detailed description of the change (e.g., adding a new factor, modifying a calculation).
    -   **Impact Analysis:** How would this change affect existing adapters and scores? Provide simulated before-and-after examples.
    -   **Agency Argument:** A clear argument for why this change results in a more accurate measurement of human agency.
3.  **Public Comment Period:** The proposal must remain open for public comment for at least **14 days**. This allows the community to scrutinize the change and raise concerns.
4.  **Implementation PR:** After the comment period, a PR implementing the change can be submitted. The PR must link to the original proposal issue.
5.  **Maintainer Review:** The PR will be reviewed by the project maintainers to ensure it aligns with the proposal and meets all quality standards.

This process makes changes to the core metric deliberate, transparent, and community-vetted, which is essential for building a trustworthy standard.
