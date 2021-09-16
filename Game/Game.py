# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 12:44:27 2021

@author: danie
"""

import random
import os.path

inventory = {}
level = 0
turns = 0
health = 20

def get_wood ():
    global level
    if level == 0:
        print("You pick up some large sticks and small fallen trees.")
        wood = random.randint(2,6)
        print("You make it back to camp with " + str(wood) + " of them.")
    elif level == 1:
        print("You use your makeshift axe to chop down some small trees.")
        wood = random.randint(5, 10)
        print("After choping those up to the size you need, you have " + str(wood) + " small logs.")
    elif level == 2:
        print("With your finely crafted axe, you chop down large trees.")
        wood = random.randint(10,20)
        print("You chop that wood up and end up with " + str(wood) + " pieces of wood.")
    else:
        print("You dont have anything with which to grab or chop wood. Something is wrong.")
        wood = 0
    add_to_inventory("wood" ,wood)

def get_stone ():
    global level
    if level == 0:
        print("You pick up some small stones and large-ish rocks.")
        stone = random.randint(2,6)
        print("You make it back to camp with " + str(stone) + " of them.")
    elif level == 1:
        print("From all your effort picking up logs, you can now pick up some larger rocks.")
        stone = random.randint(5, 10)
        print("You grabbed " + str(stone) + " miniature boulders.")
    elif level == 2:
        print("With your finely crafted axe, you you crack small boulders into pieces to bring back to camp.")
        stone = random.randint(10,20)
        print("You end up with " + str(stone) + " rocks.")
    else:
        print("You dont have anything with which to grab rocks. Something is wrong.")
        stone = 0
    add_to_inventory("stone" ,stone)

def get_fiber():
    print("Around you, you see lots of green vines climbing up trees.")
    fiber = random.randint(1,10)
    print("You twirl the vine until its in it's strongest form and end up with ")
    print(str(fiber) + " plant fibers to use in building items.")
    add_to_inventory("fiber", fiber)

def set_trap():
    if "trap" in inventory:
        print("You set up your trap along an obvious animal trail.")
        meat = random.randint(0,2)
        print("A little bit later you hear it go off and find: ")
        if meat == 0:
            print("Nothing. It must have escaped.")
        elif meat == 1:
            print("A small rabit. You have no choice but to eat it.")
        else:
            print("A small and injured deer. This will feed you for the rest of today.")
        add_to_inventory("meat", meat)
    else:
        print("You need to build a trap to use first.")
        global turns
        turns = turns - 1

def add_to_inventory (item, amount):
    if item in inventory:
        inventory[item] = inventory[item] + amount
    else:
        inventory[item] = amount

def build ():
    print("You look around you at what you have at camp to see what you can do.")
    show_inventory()
    print("You can build the following: ")
    possible_build = can_build()
    user_input = input("Please type one thing you would like to build using what is in the parenthesis by the item.\n")
    build_thing(user_input,possible_build)
    return None
    
def can_build ():
    possible_build = []
    if "wood" in inventory:
        wood_amount = inventory["wood"]
        if wood_amount >= 6:
            print("Campfire (c)")
            possible_build.append("c")
    if "wood" in inventory and "fiber" in inventory:
        wood_amount = inventory["wood"]
        fiber_amount = inventory["fiber"]
        if wood_amount >= 25 and fiber_amount >= 25:
            print("Small Shelter (ss)")
            possible_build.append("ss")
        if wood_amount >= 40 and fiber_amount >= 40:
            print("Large Shelter (ls)")
            possible_build.append("ls")
    if "wood" in inventory and "stone" in inventory and "fiber" in inventory:
        wood_amount = inventory["wood"]
        stone_amount = inventory["stone"]
        fiber_amount = inventory["fiber"]
        if wood_amount >= 6 and stone_amount >= 4 and fiber_amount >= 4:
            print("Small makeshift axe (sa)")
            possible_build.append("sa")
        if wood_amount >= 20 and stone_amount >= 16 and fiber_amount >= 10:
            print("Large strong axe (la)")
            possible_build.append("la")
        if wood_amount >= 5 and stone_amount >= 4 and fiber_amount >= 6:
            print("Trap (t)")
            possible_build.append("t")
    return possible_build
            
def build_thing (user_input, possible_build):
    if user_input == "c" and "c" in possible_build:
        add_to_inventory('campfire', 1)
        inventory["wood"] = inventory["wood"] - 6
    elif user_input == "ss" and "ss" in possible_build:
        add_to_inventory('small_shelter', 1)
        inventory["wood"] = inventory["wood"] - 25
        inventory["fiber"] = inventory["fiber"] - 25
    elif user_input == "ls" and "ls" in possible_build:
        add_to_inventory('large_shelter', 1)
        inventory["wood"] = inventory["wood"] - 40
        inventory["fiber"] = inventory["fiber"] - 40
    elif user_input == "t" and "t" in possible_build:
        add_to_inventory("trap", 1)
        inventory["wood"] = inventory["wood"] - 5
        inventory["stone"] = inventory["stone"] - 4
        inventory["fiber"] = inventory["fiber"] - 6
    elif user_input == "sa" and "sa" in possible_build:
        add_to_inventory('small_axe', 1)
        inventory["wood"] = inventory["wood"] - 6
        inventory["stone"] = inventory["stone"] - 4
        inventory["fiber"] = inventory["fiber"] - 4
        global level
        level = 1
    elif user_input == "la" and "la" in possible_build:
        add_to_inventory('large_axe', 1)
        inventory["wood"] = inventory["wood"] - 20
        inventory["stone"] = inventory["stone"] - 16
        inventory["fiber"] = inventory["fiber"] - 10
        level = 2
    else:
        print("You typed an item you can't build")
        global turns
        turns = turns - 1


def options (user_input):
    if user_input == "get wood" or user_input == "gw":
        return get_wood()
    elif user_input == "build" or user_input == "b":
        return build()
    elif user_input == "get stone" or user_input == "gs":
        return get_stone()
    elif user_input == "get fiber" or user_input == "gf":
        return get_fiber()
    elif user_input == "set trap" or user_input == "st":
        return set_trap()
    elif user_input == "quit" or user_input == "q":
        global turns
        save_game()
        turns = 1000
    elif user_input == "save" or user_input == "s":
        save_game()
        turns = turns - 1
    elif user_input == "remove save" or user_input == "rs":
        remove_save_data()
        turns = turns - 1
    elif user_input == "help" or user_input == "h":
        show_commands()
        turns = turns - 1
    elif user_input == "check stats" or user_input == "cs":
        check_stats()
        turns = turns - 1
    else:
        print("\nYou didn't choose an option. Try again.\n")
        turns = turns - 1
    
    
def show_commands():
    print("Some basic things you can do here are as follows:")
    print("'get wood' (gw), 'get stone' (gs), 'build' (b), 'save' (s), ")
    print("'quit' (q), 'check stats' (cs), 'help' (h), 'get fiber' (gf), ")
    print("'set trap' (st), and 'remove save' (rs).")
    
def check_stats():
    print("You have the following: ")
    show_inventory()
    print("Your level is:", str(level))
    
def show_inventory ():
    for item in inventory:
        if item != None:
            print(str(inventory.get(item)) + " " + item)
        else:
            print("You do not have any items available to use.") 
    return None

def save_game():
    global turns
    global level
    global health
    save_dict = inventory.copy()
    save_dict["turns"] = turns
    save_dict["level"] = level
    save_dict["health"] = health
    #json.dump(save_dict, open(game_save_file, 'wb'))
    import json
    json = json.dumps(save_dict)
    f = open("game_save_file.json","w")
    f.write(json)
    f.close()
    
def load_game():
    global turns
    global level
    global inventory
    global health
    global json
    load_game = {}
    import json
    with open('game_save_file.json') as json_file:
        load_game = json.load(json_file)
    level = load_game["level"]
    del load_game['level']
    turns = load_game["turns"]
    del load_game['turns']
    health = load_game["health"]
    del load_game['health']
    inventory = load_game.copy()
    
def remove_save_data():
    global inventory
    global turns
    global level
    save_dict = {}
    import os
    os.remove("game_save_file.json")
    inventory = save_dict.copy()
    level = 0
    turns = 1
    
def play_unloaded_first_turn ():
    global turns
    global inventory
    turns = turns + 1
    save_game()
    user_input = input("Feel free to pick one to start out your adventure using either the text in apostrophies or the text in parenthesis.\n")
    print(" ")
    options(user_input)
    print("")
    print("You have taken " + str(turns) + " turns.")
    print("")
    print('-'*70)
    turns = turns + 1
    
def play_loaded_first_turn ():
    global turns
    global inventory
    load_game()
    ("Your game has loaded and you may now continue where you left off.")
    user_input = input("What do you want to do to continue your adventure?\n")
    print("")
    options(user_input)
    print("")
    print("You have taken " + str(turns) + " turns.")
    print("")
    print('-'*70)
    turns = turns + 1

def play_next_turn():
    global turns
    global inventory
    user_input = input("Now that you have finished that, what do you want to do next?\n")
    print("")
    options(user_input)
    print("")
    print("You have taken " + str(turns) + " turns.")
    print("")
    print('-'*70)
    turns = turns + 1
    
def check_for_night():
    global turns
    if turns == 10 or turns == 20 or turns == 30 or turns == 40 or turns == 50:
        night_sequence()

def night_sequence():
    print("Night falls upon your camp as you try to gain as much comfort as ")
    print("possible from what you created that day.")
    points = 5
    if "campfire" in inventory:
        print("You are warmed by your camfire as you snuggle into your sleeping bag.")
        points = points - 1
    if "small_shelter" in inventory:
        print("Your small shelter provides you a little break from the wind.")
        points = points - 1
    if "large_shelter" in inventory:
        print("You are completely surrounded by your sturdy shelter and feel no affects of the wind.")
        points = points - 3
    if "meat" in inventory:
        if inventory["meat"] >=2:
            print("You realize you were able to eat enough meals today to have as full of a belly as possible.")
            points = points - 2
    global health
    health = health - points
    print("You realize, humorously, if this were a game you would only have " + str(health) + " health left.")
    
def main():
    global turns
    global level
    print("Welcome to my game!")
    show_commands()
    while turns < 50:
        if turns <=0:
            if os.path.exists('game_save_file.json'):
                check_for_night()
                play_loaded_first_turn()
            else:
                play_unloaded_first_turn()
        else:
            check_for_night()
            play_next_turn()
        
if __name__ == "__main__":
    main()
    
    
    
