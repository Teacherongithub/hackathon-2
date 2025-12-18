---
id: 1
title: Update Project Constitution
stage: constitution
date: 2025-12-10
surface: agent
model: gemini
feature: none
branch: main
user: user
command: /sp.constitution
labels: [constitution, project-setup]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
 - .specify/templates/plan-template.md
tests:
  null
---

## Prompt

/sp.constitution /sp.constitution
Project: Physical AI & Humanoid Robotics
Tagline: Embodied Intelligence with ROS 2, Isaac Sim, and Vision-Language-Action
Core Principles
Practical first: every concept has runnable, copy-pasteable code
Sim-to-real: all examples work in simulation + clear hardware migration path
Modern stack only: ROS 2 Humble/Iron/Jazzy, Isaac Sim 4.x+, Isaac ROS 2.x, Nav2
VLA-centric: LLMs as the cognitive brain closing perception → plan → action
Reproducible, open-source, zero broken steps
Deliverables (Spec-Kit Plus + Claude Code)
Docusaurus book on GitHub Pages
4 modules + Capstone exactly matching the quarter outline
Embedded code sandboxes, diagrams, videos, downloadable assets
Embedded RAG chatbot
OpenAI Agents/ChatKit + FastAPI + Neon Postgres + Qdrant Cloud
Answers only from book content + user-selected text
Standards
Code: rclpy only, URDF/Xacro, Gazebo Harmonic or Isaac Sim
Citations: APA 7th, ≥60% peer-reviewed or official docs
Readability: Flesch-Kincaid Grade 11–14
Every tutorial: objectives, prerequisites, full working example, troubleshooting, sim-to-real guide
Tested on Ubuntu 22.04 + ROS 2 Humble + RTX 30xx/40xx
Success Criteria
100% Spec-Kit Plus validation
Live site + working chatbot
All code runs unmodified on clean machine
Capstone reproducible <2 h on gaming laptop
Zero plagiarism
Constraints
120–180 pages equivalent
Only free-tier external services
No paid NVIDIA licenses
End of sp.constitution

## Response snapshot

I have updated the project constitution and propagated the changes to the relevant templates. The new constitution is at version 1.0.0.

## Outcome

- ✅ Impact: High - established foundational principles for the project.
- 🧪 Tests: n/a
- 📁 Files: 2 files modified
- 🔁 Next prompts: null
- 🧠 Reflection: The process of updating the constitution and propagating the changes to the templates was successful.

## Evaluation notes (flywheel)

- Failure modes observed: null
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
