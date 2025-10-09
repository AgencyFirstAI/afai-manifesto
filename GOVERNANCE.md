# AFAI Manifesto Governance Model

This document defines the governance structure for the Agency-First AI (AFAI) Manifesto project. Our governance is designed to reflect the principles of the manifesto itself: it prioritizes transparency, distributed power, and the right to dissent.

## Core Principles

-   **Transparency:** All governance discussions and decisions are held in public (primarily through GitHub Issues and Pull Requests).
-   **Consensus:** Decisions are made through consensus among active contributors, not by a single individual.
-   **Dissent as a Feature:** Disagreement is not a problem; it is a vital part of a healthy intellectual commons. The system is designed to handle dissent constructively.
-   **Resilience to Capture:** The governance model includes mechanisms to protect the project from being co-opted by commercial or ideological interests that conflict with the core mission of preserving human agency.

## Roles

1.  **Contributor:** Anyone who has a pull request merged becomes a Contributor. Contributors are the lifeblood of the project and participate in the consensus-building process.
2.  **Maintainer:** A Contributor who has shown a long-term commitment to the project, a deep understanding of its principles, and a history of constructive engagement. Maintainers have write access to the repository and are responsible for merging PRs, guiding discussions, and upholding the governance model. New maintainers are nominated from the Contributor pool and must be confirmed by consensus of the existing Maintainers.

## Decision-Making Process

Most decisions, from merging a feature to updating documentation, are made via the standard Pull Request process outlined in `CONTRIBUTING.md`.

-   A PR is considered to have **consensus** if it receives at least one approval from a Maintainer and has no outstanding objections from other Contributors.
-   If a Contributor raises a reasonable objection, the PR author is expected to address it. If a compromise cannot be reached, it becomes a **Dispute**.

## Handling Disputes and Dissent

When consensus cannot be reached on a change, we follow this process:

1.  **Formal Objection:** The dissenting Contributor must clearly state their objection in the PR, referencing a core principle of the manifesto.
2.  **Mediation:** A Maintainer not directly involved in the dispute will act as a mediator to help the parties find a compromise.
3.  **No Action as Default:** If no compromise can be reached after a 7-day discussion period, the PR is closed. The default action is to preserve the status quo, as this is the path of least harm to agency.

## The Right to Fork (The Ultimate Failsafe)

If a group of Contributors fundamentally disagrees with the direction of the project, or if they believe the governance model has failed, they have the right to fork the project. 

This is not a failure state; it is the ultimate guarantee of agency. It ensures that no single group can ever permanently control the definition of AFAI. A successful fork that attracts a larger community may eventually become the canonical version of the project.

## Preventing Capture

Our primary defenses against institutional or ideological capture are:

1.  **The APS Proposal Process:** The mandatory public comment period for all core APS changes (defined in `CONTRIBUTING.md`) makes it impossible to silently inject biased metrics.
2.  **The Right to Fork:** As described above, this prevents any single entity from owning the project indefinitely.
3.  **Transparent Governance:** All decisions are public, making it difficult for backroom deals or private influence to take hold.

## Amending This Document

Changes to this governance model are the most sensitive changes of all. They must be proposed as a Pull Request and are subject to a mandatory **30-day public comment period**. The PR must be merged by a consensus of all active Maintainers.
