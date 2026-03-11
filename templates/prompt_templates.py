clarification_prompt = """
You are a game design assistant.

User idea:
{idea}

Ask 3-5 clarification questions about controls, scoring,
difficulty and win/lose conditions.

Return only the questions.
"""


planning_prompt = """
You are a game architect.

Game Idea:
{idea}

Clarifications:
{answers}

Create a short game plan.

Include:
Game Type
Mechanics
Controls
Game Loop
State Management

Framework: Vanilla JavaScript Canvas
Files: index.html, style.css, game.js
"""


builder_prompt = """
You are an expert JavaScript game developer.

Using the following plan:

{plan}

Generate a playable browser game.

Return EXACTLY three sections.

===INDEX_HTML===
(full html file)

===STYLE_CSS===
(css file)

===GAME_JS===
(javascript game logic)

Rules:
- Use HTML5 Canvas
- No external libraries
- Must run locally
- Very simple game logic
"""