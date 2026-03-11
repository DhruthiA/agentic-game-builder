# Agentic Game Builder AI

## Overview

This project implements an **Agentic AI system** capable of generating a small playable browser game from a natural language description.

The system follows a structured **multi-agent workflow** consisting of three phases:

1. Requirements Clarification
2. Game Planning
3. Game Code Generation

Based on the user's idea, the AI agents collaborate to design and generate a game that runs locally in a web browser.

The generated game consists of three files:

* index.html
* style.css
* game.js

These files run directly in the browser using **HTML5 Canvas and Vanilla JavaScript**.

The entire system is packaged inside a **Docker container**, ensuring the project runs consistently across environments.

---

# Agentic Workflow

The system follows a multi-agent pipeline where each agent has a specific responsibility.

User Idea
↓
Clarification Agent
↓
Planning Agent
↓
Builder Agent
↓
Playable Game Output

---

# Phase 1: Requirements Clarification

The **Clarification Agent** receives the initial game idea from the user.

Since natural language inputs can be ambiguous, the agent asks follow-up questions to clarify details such as:

* Game mechanics
* Player controls
* Scoring rules
* Difficulty level
* Win or lose conditions

Example:

User Input:
Simple Pong Game

Clarification Agent Questions:

* How should the paddles be controlled?
* What colors should the paddles and ball be?
* How should scoring work?
* When should the game end?

This step ensures that the system gathers enough information before implementing the game.

---

# Phase 2: Planning

After receiving clarification answers, the **Planning Agent** creates a structured game design.

The plan includes:

* Game Type
* Game Mechanics
* Player Controls
* Game Loop
* State Management
* Framework choice
* File structure

Example Plan:

Game Type: Pong Game
Controls: W/S keys for Player 1, Arrow Keys for Player 2
Ball Color: Red
Paddle Color: White
Score System: First player to reach 10 points wins
Framework: Vanilla JavaScript Canvas

Files to generate:

index.html
style.css
game.js

This plan acts as the blueprint for code generation.

---

# Phase 3: Execution (Game Generation)

The **Builder Agent** uses the structured plan to generate the actual game.

It produces three files:

index.html
style.css
game.js

The game is rendered using **HTML5 Canvas**, and the JavaScript file implements:

* Game loop
* Ball movement
* Paddle controls
* Collision detection
* Score tracking

After generation, the files are saved to the **output/** directory.

---

# System Architecture

The project uses a **controller-based agent architecture**.

main.py acts as the entry point and initializes the agents.

Architecture:

main.py
↓
GameAgentController
├── ClarificationAgent
├── PlannerAgent
└── BuilderAgent

---

## Component Description

### main.py

Initializes the agents and starts the workflow.

### GameAgentController

Controls the full pipeline:

Idea → Clarify → Plan → Build → Save Output

### ClarificationAgent

Asks follow-up questions about the game idea.

### PlannerAgent

Creates a structured game plan.

### BuilderAgent

Generates the game code files.

---

# Generated Output

After execution, the generated files appear in:

output/

output/
index.html
style.css
game.js

To play the game, open:

output/index.html

in any web browser.

---

# Technologies Used

Python
Groq LLM API
HTML5 Canvas
JavaScript
Docker

---

# Running the Project

## 1 Install Docker

Download Docker from:

https://www.docker.com/

---

## 2 Clone the Repository

git clone <repository-url>
cd agentic-game-builder

---

## 3 Add API Key

Create a .env file in the project root.

Example:

GROQ_API_KEY=api_key_here

---

## 4 Build Docker Image

docker build -t game-agent .

---

## 5 Run the Agent

docker run -it --env-file .env -v ${PWD}/output:/app/output game-agent

---

## 6 Enter Game Idea

Example inputs:

Simple Pong Game
Snake Game
Breakout Game

The agent will:

1. Ask clarification questions
2. Generate a game plan
3. Build the playable game

---

## 7 Run the Game

After generation, open:

output/index.html

in your browser.

---

# Example Game Ideas

Simple Pong Game
Snake Game
Breakout Game
Catch the Falling Ball Game

---

# Tradeoffs

Several design decisions were made to ensure the system runs reliably:

* Vanilla JavaScript was chosen instead of Phaser to avoid dependency issues.
* Games are intentionally simple to ensure they run locally without external assets.
* Output parsing ensures generated code is valid before saving.

---

# Future Improvements

With additional time, the system could be extended by:

* Adding a self-repair agent to automatically fix broken code.
* Supporting Phaser framework for richer games.
* Implementing automated testing of generated games.
* Adding a web UI for interacting with the AI agent.
* Supporting asset generation such as images and sounds.

---

# Demonstration

The demonstration video shows:

1. Building the Docker container
2. Running the AI agent
3. Clarification phase
4. Planning phase
5. Game generation
6. Running the generated game in a browser
