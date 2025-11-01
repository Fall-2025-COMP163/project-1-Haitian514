"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

def create_character(name, character_class):
    level = 1
    strength, magic, health = calculate_stats(character_class, level)

    # Assign starting equipment based on class
    if character_class.lower() == "warrior":
        equipment = ["Wooden Sword", "Marred Shield", "Chainmail Armor"]
    elif character_class.lower() == "mage":
        equipment = ["Wooden Staff", "Apprentice Robe", "Mana Crystal"]
    elif character_class.lower() == "rogue":
        equipment = ["Rusty Dagger", "Cloak", "Lockpick Set"]
    elif character_class.lower() == "cleric":
        equipment = ["Stake", "Holy Tome", "Blessed Robe"]
    else:
        equipment = ["Heavy Stick", "Cloth Tunic"]

    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100,
        "equipment": equipment
    }
    return character

def calculate_stats(character_class, level):
    if character_class.lower() == "warrior":
        strength = 15 + (3 * level)
        magic = 3 + (1 * level)
        health = 120 + (10 * level)
    elif character_class.lower() == "mage":
        strength = 5 + (1 * level)
        magic = 18 + (4 * level)
        health = 90 + (6 * level)
    elif character_class.lower() == "rogue":
        strength = 10 + (2 * level)
        magic = 10 + (2 * level)
        health = 80 + (5 * level)
    elif character_class.lower() == "cleric":
        strength = 8 + (2 * level)
        magic = 14 + (3 * level)
        health = 110 + (8 * level)
    else:
        strength = 8
        magic = 8
        health = 100

    return strength, magic, health

def save_character(character, filename):
    file = open(filename, "w")
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")
    file.write("Equipment: " + ", ".join(character["equipment"]) + "\n")
    file.close()

def load_character(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    # Parse character data
    character = {}
    for line in lines:
        if ":" in line:
            key, value = line.strip().split(": ", 1)
            if key == "Character Name":
                character["name"] = value
            elif key == "Class":
                character["class"] = value
            elif key == "Level":
                character["level"] = int(value)
            elif key == "Strength":
                character["strength"] = int(value)
            elif key == "Magic":
                character["magic"] = int(value)
            elif key == "Health":
                character["health"] = int(value)
            elif key == "Gold":
                character["gold"] = int(value)
            elif key == "Equipment":
                character["equipment"] = value.split(", ")

    return character

def display_character(character):
    print("\n=== CHARACTER SHEET ===")
    print("Name:", character["name"])
    print("Class:", character["class"])
    print("Level:", character["level"])
    print("Strength:", character["strength"])
    print("Magic:", character["magic"])
    print("Health:", character["health"])
    print("Gold:", character["gold"])
    print("Equipment:")
    for item in character["equipment"]:
        print(" -", item)
    print("========================\n")

def level_up(character):
    character["level"] += 1
    new_strength, new_magic, new_health = calculate_stats(character["class"], character["level"])
    character["strength"] = new_strength
    character["magic"] = new_magic
    character["health"] = new_health
    print(character["name"], "has leveled up to Level", character["level"], "!")

if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    char = create_character("Aria", "Mage")
    display_character(char)
    save_character(char, "aria_save.txt")

    print("\nLoading saved character...")
    loaded = load_character("aria_save.txt")
    display_character(loaded)

    print("\nLeveling up...")
    level_up(loaded)
    display_character(loaded)
