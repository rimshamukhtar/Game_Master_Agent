# Game Master Agent 🎮

A fantasy text-based adventure game powered by **OpenAI Agent SDK** + **Chainlit**.

Players interact with a Game Master through text to:
- Explore locations
- Engage in combat
- Collect magical items & gold

Agents work behind-the-scenes to orchestrate the gameplay.

---

## 📊 Project Structure

```
Game_Master_Agent/
├── main.py                      # Orchestration logic & Chainlit UI hooks
├── tools.py                     # Dice roll and event generator tools
├── model_loader.py             # Loads the LiteLLM / OpenAI model
└── game_agents/
    ├── narrator_agent.py     # Narrates game events
    ├── monster_agent.py      # Handles combat logic
    └── item_agent.py         # Grants rewards and manages inventory
```

---

## 🧠 Features

### 📖 Narrator Agent
- Responds to player actions with story updates
- Uses `generate_event` tool for fantasy twists

### 🐉 Monster Agent
- Dice-based battle system
- Controls enemies during encounters

### 🏹 Item Agent
- Grants loot & updates inventory
- Adds rewards after victory

### 🎲 Tools
- `roll_dice()`: DnD-style dice roller
- `generate_event()`: Adds random magical/fantasy encounters

---

## ⚖️ Agent Handoff Flow
1. Narrator handles story input
2. If combat needed → handoff to MonsterAgent
3. If player wins → handoff to ItemAgent

---

## 🚀 How to Run

```bash
git clone https://github.com/your-username/Game_Master_Agent.git
cd Game_Master_Agent
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
chainlit run main.py
```

> ⚡ Make sure to add your OpenAI or Gemini API key in `.env`

```env
OPENAI_API_KEY=your_key_here
```

---

## 🎉 Sample Gameplay
```txt
Welcome, adventurer! Type your first action:
> Enter the forest

Story: You step into the forest...
Your move? (explore / attack / flee)

> Attack

Story: You swing your sword at the goblin...
Combat: You rolled a 16. Critical hit!
Loot: 5 gold and a glowing crystal.
```

---

## 🌟 Credits
- Built by [**Rimsha Mukhtar**]
- Agent SDK + Chainlit powered game engine
