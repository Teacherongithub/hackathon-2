<!--
Sync Impact Report
- Version change: 0.0.0 → 1.0.0
- List of modified principles: all principles updated
- Added sections: Deliverables, Standards, Success Criteria, Constraints
- Removed sections: none
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs:
  - TODO(RATIFICATION_DATE): requires user input
-->
# Physical AI & Humanoid Robotics Constitution
<!-- Embodied Intelligence with ROS 2, Isaac Sim, and Vision-Language-Action -->

## Core Principles

### I. Practical First
Every concept has runnable, copy-pasteable code.

### II. Sim-to-Real
All examples work in simulation and have a clear hardware migration path.

### III. Modern Stack Only
The project uses ROS 2 Humble/Iron/Jazzy, Isaac Sim 4.x+, Isaac ROS 2.x, and Nav2.

### IV. VLA-Centric
LLMs are used as the cognitive brain to close the perception-plan-action loop.

### V. Reproducible & Open Source
All examples are reproducible, open-source, with zero broken steps.

## Deliverables
- Docusaurus book on GitHub Pages.
- 4 modules + Capstone exactly matching the quarter outline.
- Embedded code sandboxes, diagrams, videos, and downloadable assets.
- Embedded RAG chatbot using OpenAI Agents/ChatKit, FastAPI, Neon Postgres, and Qdrant Cloud, answering only from book content and user-selected text.

## Standards
- **Code:** rclpy only, URDF/Xacro, Gazebo Harmonic or Isaac Sim.
- **Citations:** APA 7th, with ≥60% from peer-reviewed or official documentation.
- **Readability:** Flesch-Kincaid Grade 11–14.
- **Tutorials:** Every tutorial must include objectives, prerequisites, a full working example, troubleshooting guidance, and a sim-to-real guide.
- **Testing:** Tested on Ubuntu 22.04 + ROS 2 Humble + RTX 30xx/40xx.

## Success Criteria
- 100% Spec-Kit Plus validation.
- A live site with a working chatbot.
- All code runs unmodified on a clean machine.
- The capstone project is reproducible in under 2 hours on a gaming laptop.
- Zero plagiarism.

## Constraints
- 120–180 pages equivalent.
- Only free-tier external services are to be used.
- No paid NVIDIA licenses.

## Governance
This Constitution supersedes all other practices. Amendments require documentation, approval, and a migration plan. All PRs and reviews must verify compliance.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE) | **Last Amended**: 2025-12-10