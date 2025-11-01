"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Sean Telemaque
Date: 10/31/2025

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

def calculate_stats(character_class, level):
    if character_class == "Warrior":
        strength = 15 + (level * 3)
        magic = 3 + (level * 1)
        health = 120 + (level * 10)
    elif character_class == "Mage":
        strength = 5 + (level * 1)
        magic = 18 + (level * 4)
        health = 80 + (level * 8)
    elif character_class == "Rogue":
        strength = 10 + (level * 2)
        magic = 10 + (level * 2)
        health = 70 + (level * 7)
    elif character_class == "Cleric":
        strength = 8 + (level * 2)
        magic = 15 + (level * 3)
        health = 100 + (level * 9)
    else:
        strength, magic, health = 5, 5, 50
    return strength, magic, health


def create_character(name, character_class):
    level = 1
    gold = 100
    strength, magic, health = calculate_stats(character_class, level)
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }
    return character
import os
def save_character(character, filename):
    dir_name = os.path.dirname(filename)
    if dir_name != "" and not os.path.exists(dir_name):
        return False

    file = open(filename, "w")
    file.write("Character Name: " + character["name"] + "\n")
    file.write("Class: " + character["class"] + "\n")
    file.write("Level: " + str(character["level"]) + "\n")
    file.write("Strength: " + str(character["strength"]) + "\n")
    file.write("Magic: " + str(character["magic"]) + "\n")
    file.write("Health: " + str(character["health"]) + "\n")
    file.write("Gold: " + str(character["gold"]) + "\n")
    file.close()
    return True

import os

def load_character(filename):
    if not os.path.exists(filename):
        return None
    character = {}

    # Loop directly over the file; no file variable, no explicit close()
    for line in open(filename, "r"):
        line = line.strip()
        key, value = line.split(": ")
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

    return character

def display_character(character):
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("=======================")


def level_up(character):
    character["level"] += 1
    str_new, mag_new, hp_new = calculate_stats(character["class"], character["level"])
    character["strength"] = str_new
    character["magic"] = mag_new
    character["health"] = hp_new

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
