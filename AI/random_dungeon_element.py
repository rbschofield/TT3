import random
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnableSequence
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser


# ----------------------------
# RANDOM GENERATION FUNCTIONS
# ----------------------------
def random_hallway_description():
    lengths = ["short (10 ft)", "medium (30 ft)", "long (60 ft)", "very long (100 ft or more)"]
    doors = random.randint(0, 4)
    intersections = random.choice(["dead end", "side passage", "T-intersection", "four-way intersection", "curving corner"])
    return f"A {random.choice(lengths)} hallway with {doors} doors and a {intersections}."


def random_room_description():
    shapes = ["square", "rectangular", "circular", "octagonal", "collapsed", "vaulted"]
    size = random.choice(["small (10x10 ft)", "medium (30x30 ft)", "large (50x50 ft)", "huge (100x100 ft)"])
    contents = []
    if random.random() < 0.7:
        contents.append(random.choice([
            "a lurking monster",
            "a wandering skeleton",
            "a sleeping troll",
            "a giant spider",
            "a group of goblins",
            "a cursed knight"
        ]))
    if random.random() < 0.6:
        contents.append(random.choice([
            "a treasure chest",
            "a pile of coins",
            "a glowing crystal",
            "ancient runes carved in the floor",
            "a magical weapon resting on a pedestal"
        ]))
    contents_text = " and ".join(contents) if contents else "nothing of note"
    return f"A {size} {random.choice(shapes)} room containing {contents_text}."


# ----------------------------
# LANGCHAIN LLM PIPELINE (RunnableSequence)
# ----------------------------
def build_dungeon_chain():
    prompt = PromptTemplate(
        input_variables=["hallway", "room"],
        template=(
            "You are a dungeon architect generating random fantasy dungeon elements.\n\n"
            "Hallway: {hallway}\n"
            "Room: {room}\n\n"
            "Combine them into a short vivid dungeon description (3–5 sentences) for a text adventure."
        ),
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0.9
    )

    # The new RunnableSequence pipeline
    chain = RunnableSequence(
        prompt | llm | StrOutputParser()
    )
    return chain


# ----------------------------
# MAIN FUNCTION
# ----------------------------
def generate_random_dungeon():
    chain = build_dungeon_chain()
    hallway = random_hallway_description()
    room = random_room_description()
    return chain.invoke({"hallway": hallway, "room": room})


# ----------------------------
# RUN
# ----------------------------
if __name__ == "__main__":
    print("🧱 Generating a random dungeon element using Gemini...\n")
    print(generate_random_dungeon())
