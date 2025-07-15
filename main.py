"""One‑shot adventure orchestration – NO hosted tools passed to model."""

import random
from agents import Runner, set_tracing_disabled
import chainlit as cl
from dotenv import load_dotenv

from model_loader import model
from tools import roll_dice, generate_event
from game_agents.narrator_agent import NarratorAgent
from game_agents.monster_agent import MonsterAgent
from game_agents.item_agent import ItemAgent

load_dotenv()
set_tracing_disabled(True)

# Helper flags
KEYWORDS_COMBAT = [
    "monster", "goblin", "dragon", "orc", "troll", "beast",
    "attack", "fight", "lunge", "strike"
]
VICTORY_WORDS = ["defeated", "slain", "victory", "killed", "falls", "dies"]

def needs_combat(text: str) -> bool:
    t = text.lower()
    return any(k in t for k in KEYWORDS_COMBAT)

def combat_won(text: str) -> bool:
    return any(w in text.lower() for w in VICTORY_WORDS)

@cl.on_chat_start
async def on_start():
    await cl.Message(content="""
👋 **Welcome, adventurer! I am your Game Master** 🎮

🔮 You're entering a fantasy realm full of danger and treasure.
Type an action to begin, e.g.:
• *Enter the forest*
• *Explore the cave*
• *Attack the goblin*

Let the quest begin! 🧙‍♂️
""").send()


@cl.on_message
async def handle_turn(msg: cl.Message):
    user_input = msg.content.strip()

    # 1️⃣ Narration
    narr_out = await Runner.run(NarratorAgent, input=user_input)
    story = narr_out.final_output.strip()

    if len(story.split()) < 5:
        story += " " + generate_event()

    parts = [f"📖 **Story:**\n{story}"]

    # 2️⃣ Optional combat
    if needs_combat(user_input) or needs_combat(story):
        # Simulate dice locally
        dice_roll = roll_dice()
        combat_prompt = f"Player rolled {dice_roll} in combat."
        combat_out = await Runner.run(MonsterAgent, input=combat_prompt)
        combat_text = combat_out.final_output.strip()
        parts.append(f"⚔️ **Combat:**\n{combat_text}")

        # 3️⃣ Loot if victory
        if combat_won(combat_text):
            loot_out = await Runner.run(ItemAgent, input="loot")
            parts.append(f"🎁 **Loot:**\n{loot_out.final_output.strip()}")

    parts.append("🔁 *Your move?* (explore / attack / inventory / flee / etc.)")

    await cl.Message(content="\n\n".join(parts)).send()
