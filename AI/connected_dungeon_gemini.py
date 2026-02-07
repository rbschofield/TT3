import random
from typing import Dict, List
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableSequence

import os
os.environ["GOOGLE_API_KEY"] = "(key)"

# ----------------------------
# RANDOM ELEMENT HELPERS
# ----------------------------
def random_room_description():
    shapes = ["square", "rectangular", "circular", "octagonal", "collapsed", "vaulted"]
    size = random.choice(["small (10x10 ft)", "medium (30x30 ft)", "large (50x50 ft)", "huge (100x100 ft)"])
    contents = []
    if random.random() < 0.7:
        contents.append(random.choice([
            "a lurking monster", "a wandering skeleton", "a sleeping troll",
            "a giant spider", "a group of goblins", "a cursed knight"
        ]))
    if random.random() < 0.6:
        contents.append(random.choice([
            "a treasure chest", "a pile of coins", "a glowing crystal",
            "ancient runes carved in the floor", "a magical weapon on a pedestal"
        ]))
    contents_text = " and ".join(contents) if contents else "nothing of note"
    return f"A {size} {random.choice(shapes)} room containing {contents_text}."


def random_hallway_description():
    lengths = ["short (10 ft)", "medium (30 ft)", "long (60 ft)", "very long (100 ft)"]
    features = ["a T-intersection", "a dead end", "a side passage", "a curving corner", "stairs descending into darkness"]
    doors = random.randint(0, 3)
    return f"A {random.choice(lengths)} hallway with {doors} doors and {random.choice(features)}."


# ----------------------------
# DUNGEON STRUCTURE GENERATOR
# ----------------------------
def generate_dungeon_graph(num_rooms: int = 6) -> Dict[str, Dict]:
    """
    Creates a random graph-like dungeon map where rooms are connected by hallways.
    """
    dungeon = {}
    for i in range(1, num_rooms + 1):
        room_id = f"Room-{i}"
        dungeon[room_id] = {
            "description": random_room_description(),
            "connections": []
        }

    # Randomly connect rooms
    room_ids = list(dungeon.keys())
    for i, room_id in enumerate(room_ids):
        possible_targets = [r for r in room_ids if r != room_id]
        num_connections = random.randint(1, min(3, len(possible_targets)))
        dungeon[room_id]["connections"] = random.sample(possible_targets, num_connections)
    return dungeon


# ----------------------------
# LANGCHAIN PIPELINE (RunnableSequence)
# ----------------------------
def build_dungeon_chain():
    prompt = PromptTemplate(
        input_variables=["map_text"],
        template=(
            "You are a fantasy dungeon narrator. Given the following rough dungeon map data:\n\n"
            "{map_text}\n\n"
            "Write a vivid text description for this dungeon as if it were part of a tabletop RPG module. "
            "Describe how the rooms connect, key features, and atmosphere. Limit to 6–10 sentences."
        ),
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.9
    )

    return RunnableSequence(prompt | llm | StrOutputParser())


# ----------------------------
# DUNGEON DESCRIPTION PIPELINE
# ----------------------------
def generate_dungeon_description(num_rooms=6):
    dungeon = generate_dungeon_graph(num_rooms)

    # Create a readable map summary
    map_lines = []
    for room, data in dungeon.items():
        map_lines.append(f"{room}: {data['description']}")
        for conn in data['connections']:
            map_lines.append(f"  connects to {conn} via {random_hallway_description()}")
    map_text = "\n".join(map_lines)

    chain = build_dungeon_chain()
    final_description = chain.invoke({"map_text": map_text})

    return map_text, final_description


# ----------------------------
# MAIN ENTRY POINT
# ----------------------------
if __name__ == "__main__":
    print("🧭 Generating connected dungeon map using Gemini...\n")

    map_text, narrative = generate_dungeon_description(num_rooms=6)

    print("=== 🗺️ RAW DUNGEON MAP STRUCTURE ===")
    print(map_text)
    print("\n=== 📜 NARRATIVE DESCRIPTION ===")
    print(narrative)
