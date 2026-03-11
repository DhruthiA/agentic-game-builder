import os
from groq import Groq
from dotenv import load_dotenv

from agent.clarification_agent import ClarificationAgent
from agent.planner_agent import PlannerAgent
from agent.builder_agent import BuilderAgent
from agent.agent_controller import GameAgentController

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

clarifier = ClarificationAgent(client)
planner = PlannerAgent(client)
builder = BuilderAgent(client)

controller = GameAgentController(
    clarifier,
    planner,
    builder
)

idea = input("Enter your game idea:\n")

controller.run(idea)