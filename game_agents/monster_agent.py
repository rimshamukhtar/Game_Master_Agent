from agents import Agent
from model_loader import model

MonsterAgent = Agent(
    name="Monster Agent",
    instructions="""
You handle quick, cinematic combat.
- Assume a d20 roll (the system provides a number). Describe the outcome in 2–3 short lines.
- **Do NOT** output code, `tool_code`, or any function calls (like `print(...)`).
- If the player wins, clearly state the monster is defeated.
- If the monster still stands, indicate the player must act again.
""",
    model=model
)
