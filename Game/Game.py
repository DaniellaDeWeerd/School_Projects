# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 12:44:27 2021

@author: daniella
"""

import random
import os.path

inventory = {}
level = 0
turns = 0
health = 20
stage = 0

def get_wood ():
    global level
    global stage
    
    #Stage 0#
    
    if stage == 0:
        if level == 0:
            print("\033[0;36;40mYou pick up some large sticks and small fallen trees.")
            wood = random.randint(2,6)
            print("You make it back to camp with " + str(wood) + " of them.")
        elif level == 1:
            print("\033[0;36;40mYou use your makeshift axe to chop down some small trees.")
            wood = random.randint(5, 10)
            print("After choping those up to the size you need, you have " + str(wood) + " small logs.")
        elif level == 2:
            print("\033[0;36;40mWith your finely crafted axe, you chop down large trees.")
            wood = random.randint(10,20)
            print("You chop that wood up and end up with " + str(wood) + " pieces of wood.")
        else:
            print("\033[0;36;40mYou dont have anything with which to grab or chop wood. Something is wrong.")
            wood = 0
        add_to_inventory("wood" ,wood)
    
    #Stage 1#
    
    elif stage == 1:
        if level == 0:
            print("\033[0;36;40mYou pick up some large sticks and small fallen trees.")
            wood = random.randint(0,4)
            print("\033[0;36;40mYou make it back to camp with " + str(wood) + " of them.")
        elif level == 1:
            print("\033[0;36;40mYou use your makeshift axe to chop down some small trees.")
            wood = random.randint(3, 8)
            print("After choping those up to the size you need, you have " + str(wood) + " small logs.")
        elif level == 2:
            print("\033[0;36;40mWith your finely crafted axe, you chop down large trees.")
            wood = random.randint(8,18)
            print("You chop that wood up and end up with " + str(wood) + " pieces of wood.")
        else:
            print("\033[0;36;40mYou dont have anything with which to grab or chop wood. Something is wrong.")
            wood = 0
        add_to_inventory("wood" ,wood)

def get_stone ():
    global level
    
    #Available for both stage 0, 1, and 2#
    
    if level == 0:
        print("\033[0;36;40mYou pick up some small stones and large-ish rocks.")
        stone = random.randint(2,6)
        print("You make it back to camp with " + str(stone) + " of them.")
    elif level == 1:
        print("\033[0;36;40mFrom all your effort picking up logs, you can now pick up some larger rocks.")
        stone = random.randint(5, 10)
        print("You grabbed " + str(stone) + " miniature boulders.")
    elif level == 2:
        print("\033[0;36;40mWith your finely crafted axe, you you crack small boulders into pieces to bring back to camp.")
        stone = random.randint(10,20)
        print("You end up with " + str(stone) + " rocks.")
    else:
        print("\033[0;36;40mYou dont have anything with which to grab rocks. Something is wrong.")
        stone = 0
    add_to_inventory("stone" ,stone)

def get_fiber():
    
    global stage
    
    #stage 0#
    
    if stage == 0:  
        print("\033[0;36;40mAround you, you see lots of green vines climbing up trees.")
        fiber = random.randint(1,10)
        print("You twirl the vine until its in it's strongest form and end up with " + str(fiber) + " plant fibers to use in building items.")
        add_to_inventory("fiber", fiber)
    if stage == 1:
        print("\033[0;36;40mAround you, you see a couple green vines climbing up trees.")
        fiber = random.randint(0,6)
        print("You twirl the vine until its in it's strongest form and end up with ")
        print(str(fiber) + " plant fibers to use in building items.")
        add_to_inventory("fiber", fiber)

def set_trap():
    global stage
    #Stage 0#
    
    if stage == 0:
        if "trap" in inventory:
            print("\033[0;36;40mYou set up your trap along an obvious animal trail.")
            meat = random.randint(0,2)
            print("A little bit later you hear it go off and find: ")
            if meat == 0:
                print("\033[0;36;40mNothing. It must have escaped.")
            elif meat == 1:
                print("\033[0;36;40mA small rabbit. You have no choice but to eat it.")
            else:
                print("\033[0;36;40mA small and injured deer. This will feed you for the rest of today.")
            add_to_inventory("meat", meat)
        else:
            print("\033[0;36;40mYou need to build a trap to use first.")
            global turns
            turns = turns - 1
            
    #Stage 1#
    
    if stage == 1:
        if "trap" in inventory:
            print("\033[0;36;40mYou set up your trap along an obvious animal trail.")
            meat = random.randint(0,1)
            print("A little bit later you hear it go off and find: ")
            if meat == 0:
                print("\033[0;36;40mNothing. It must have escaped.")
            elif meat == 1:
                print("\033[0;36;40mA small injured and malnourished rabbit. You have no choice but to eat it.")
        else:
            print("\033[0;36;40mYou need to build a trap to use first.")
            turns = turns - 1

def add_to_inventory (item, amount):
    if item in inventory:
        inventory[item] = inventory[item] + amount
    else:
        inventory[item] = amount

def build ():
    print("\033[0;36;40mYou look around you at what you have at camp to see what you can do.")
    show_inventory()
    print("\033[0;36;40mYou can build the following: ")
    possible_build = can_build()
    user_input = input("\033[0;36;40mPlease type one thing you would like to build using what is in the parenthesis by the item.\n")
    build_thing(user_input,possible_build)
    return None
    
def can_build ():
    possible_build = []
    if "wood" in inventory:
        wood_amount = inventory["wood"]
        if wood_amount >= 6:
            print("\033[0;36;40mCampfire (c)")
            possible_build.append("c")
    if "wood" in inventory and "fiber" in inventory:
        wood_amount = inventory["wood"]
        fiber_amount = inventory["fiber"]
        if wood_amount >= 25 and fiber_amount >= 25:
            print("\033[0;36;40mSmall Shelter (ss)")
            possible_build.append("ss")
        if wood_amount >= 40 and fiber_amount >= 40:
            print("\033[0;36;40mLarge Shelter (ls)")
            possible_build.append("ls")
    if "wood" in inventory and "stone" in inventory and "fiber" in inventory:
        wood_amount = inventory["wood"]
        stone_amount = inventory["stone"]
        fiber_amount = inventory["fiber"]
        if wood_amount >= 6 and stone_amount >= 4 and fiber_amount >= 4:
            print("\033[0;36;40mSmall makeshift axe (sa)")
            possible_build.append("sa")
        if wood_amount >= 20 and stone_amount >= 16 and fiber_amount >= 10:
            print("\033[0;36;40mLarge strong axe (la)")
            possible_build.append("la")
        if wood_amount >= 5 and stone_amount >= 4 and fiber_amount >= 6:
            print("\033[0;36;40mTrap (t)")
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
        print("\033[0;36;40mYou typed an item you can't build")
        global turns
        if turns != 15 and turns != 30 and turns != 45 and turns != 60:
                turns = turns - 1

def options (user_input):
    global stage
    global turns
    
    #Stage 0 and 1#
    
    if stage == 0 or stage == 1:
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
            save_game()
            turns = 1000
        elif user_input == "save" or user_input == "s":
            save_game()
            if turns != 15 and turns != 30 and turns != 45 and turns != 60:
                turns = turns - 1
        elif user_input == "remove save" or user_input == "rs":
            remove_save_data()
            if turns != 15 and turns != 30 and turns != 45 and turns != 60:
                turns = turns - 1
        elif user_input == "help" or user_input == "h":
            show_commands()
            if turns != 15 and turns != 30 and turns != 45 and turns != 60:
                turns = turns - 1
        elif user_input == "check stats" or user_input == "cs":
            check_stats()
            if turns != 15 and turns != 30 and turns != 45 and turns != 60:
                turns = turns - 1
        else:
            print("\033[0;36;40m\nYou didn't choose an option. Try again.\n")
            if turns != 15 and turns != 30 and turns != 45 and turns != 60:
                turns = turns - 1
            
    #Stage 2#
            
    if stage == 2:
        
        if user_input == "build" or user_input == "b":
            return build()
        elif user_input == "get stone" or user_input == "gs":
            return get_stone()
        elif user_input == "quit" or user_input == "q":
            save_game()
            turns = 1000
        elif user_input == "save" or user_input == "s":
            save_game()
            if turns != 15 and turns != 30 and turns != 45 and turns != 60:
                turns = turns - 1
        elif user_input == "remove save" or user_input == "rs":
            remove_save_data()
            if turns != 15 and turns != 30 and turns != 45 and turns != 60:
                turns = turns - 1
        elif user_input == "help" or user_input == "h":
            show_commands()
            if turns != 15 and turns != 30 and turns != 45 and turns != 60:
                turns = turns - 1
        elif user_input == "check stats" or user_input == "cs":
            check_stats()
            if turns != 15 and turns != 30 and turns != 45 and turns != 60:
                turns = turns - 1
        else:
            print("\033[0;36;40m\nYou didn't choose a valid option. Try again.\n")
            if turns != 15 and turns != 30 and turns != 45 and turns != 60:
                turns = turns - 1
            
    #Stage 3#
    
    if stage == 3:
        if user_input == "quit" or user_input == "q":
            save_game()
            turns = 1000
        elif user_input == 'hide':
            hide()
        elif user_input == 'run':
            run()
        elif user_input == 'fight':
            fight()
        elif user_input == "save" or user_input == "s":
            save_game()
            if turns != 15 and turns != 30 and turns != 45 and turns != 60:
                turns = turns - 1
        elif user_input == "remove save" or user_input == "rs":
            remove_save_data()
            if turns != 15 and turns != 30 and turns != 45 and turns != 60:
                turns = turns - 1
        elif user_input == "help" or user_input == "h":
            show_commands()
            if turns != 15 and turns != 30 and turns != 45 and turns != 60:
                turns = turns - 1
        elif user_input == "check stats" or user_input == "cs":
            check_stats()
            if turns != 15 and turns != 30 and turns != 45 and turns != 60:
                turns = turns - 1
        else:
            print("\033[0;36;40m\nYou didn't choose an option. Try again.\n")
            if turns != 15 and turns != 30 and turns != 45 and turns != 60:
                turns = turns - 1

def hide ():
    print("\033[0;36;40mYou hide in a bush trying to escape the feeling of someone watching you.")
    print("It doesn't work. You can't hide from what you can't see. :D")
def run():
    print("\033[0;36;40mYou run away from the area you where just in. You don't aim for any particulare direction. You are fully lost and you still feel the thing hunting you.")
def fight():
    print("\033[0;36;40mYou can't fight the invisible and untouchable. Good try though! :D")
        
def show_commands():
    global stage
    
    #stage 0 and 1#
    
    if stage == 0 or stage == 1:
        print("\033[0;36;40mSome basic things you can do here are as follows:")
        print("'get wood' (gw) \n'get fiber' (gf)\n'set trap' (st)")
        print("'get stone' (gs)\n'build' (b)\n'save' (s)")
        print("'quit' (q)\n'check stats' (cs)\n'help' (h)\n'remove save' (rs)")
    
    #stage 2#
    
    elif stage == 2:
        print("\033[0;36;40mSome basic things you can do here are as follows:")
        print("'get stone' (gs)\n'build' (b)\n'save' (s)")
        print("'quit' (q)\n'check stats' (cs)\n'help' (h)\n'remove save' (rs)")
    
    #stage 3#
    
    elif stage == 3:
        print("\033[0;36;40mSome basic things you can do here are as follows:")
        print("\n'run'\n'hide'\n'fight',")
        print("'check stats' (cs)\n'help' (h)")
        print("'quit' (q)\n'save' (s)\n'remove save' (rs)")
        
    
    elif stage ==4:
        print("\033[0;36;40mSome basic things you can do here are as follows:")
        print("'give up'\n'give up'\n'give up'")
        print("'give up'\n'give up'\n'give up'\n'give up'")
    
def check_stats():
    global level
    global health
    print("\033[0;36;40mYou have the following: ")
    show_inventory()
    print("\033[0;36;40mYour level is: ", str(level))
    print("\033[0;36;40mYour health is: ", str(health))
    
def show_inventory ():
    for item in inventory:
        if item != None:
            print(str(inventory.get(item)) + " " + item)
        else:
            print("\033[0;36;40mYou do not have any items available to use.") 
    return None

def save_game():
    global turns
    global level
    global health
    global stage
    save_dict = inventory.copy()
    save_dict["turns"] = turns
    save_dict["level"] = level
    save_dict["health"] = health 
    save_dict["stage"] = stage
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
    global stage
    load_game = {}
    import json
    with open('game_save_file.json') as json_file:
        load_game = json.load(json_file)
    level = load_game["level"]
    del load_game['level']
    turns = load_game["turns"]
    del load_game['turns']
    stage = load_game["stage"]
    del load_game['stage']
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
    save_game()
    
def play_unloaded_first_turn ():
    global turns
    global inventory
    turns = turns + 1
    save_game()
    user_input = input("\033[0;36;40mFeel free to pick one to start out your adventure using either the text in apostrophies or the text in parenthesis.\n")
    print(" ")
    options(user_input)
    print("")
    print("\033[0;36;40mYou have taken " + str(turns) + " turns.")
    print("")
    print('-'*70)
    turns = turns + 1
    
def play_loaded_first_turn ():
    global turns
    global inventory
    load_game()
    ("\033[0;36;40mYour game has loaded and you may now continue where you left off.")
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
    user_input = input("\033[0;36;40mNow that you have finished that, what do you want to do next?\n")
    print("")
    options(user_input)
    print("")
    print("You have taken " + str(turns) + " turns.")
    print("")
    print('-'*70)
    turns = turns + 1
    
def check_for_night():
    global turns
    global stage
    if turns == 15 or turns == 30 or turns == 45 or turns == 60 or turns == 75 or turns == 80:
        input("\033[0;36;40mThe sun sets and night begins. Hit enter to see how you fared.")
        night_sequence()
        if turns == 30:
            print("\033[0;36;40mWhen you wake up in the morning you see that the area around you looks a little bit sparse.")
            print("The birds are mostly quiet and the greenery is slightly more brown.\n\n")
            print("\033[0;35;40mIt's a bit unsettling.\n\n")
            stage = 1
        if turns == 60:
            print("\033[0;36;40mThe world around you is dying. There is no other way to describe what is going on.")
            print("The trees are shrivled and all pants crumble when you touch them. The forest is quiet.\n\n")
            print("\033[0;36;40mSomething is watching me. I can feel it./n/n")
            print("\033[0;36;40mIt's nothing to worry about! :D/n/n")
            print("\033[0;35;40mDid the voice in my head just speak back to me??? I must be going crazy")
            stage = 2
        if turns == 75:
            print("\033[0;35;40mI am being hunted. Someone help me! Please help me!\n\n")
            print("\033[0;36;40mThere is nothing you can do but run and hide! :D\n\n")
            print("\033[0;35;40mIt's you isn't it!?\n\n")
            print("\033[0;36;40mMaybeee :D Doesn't matter though! Have fun running, hiding, and fighting the nothingness!")
            stage = 3
    immortal() #Remove this when releasing game

def night_sequence():
    print("\033[0;36;40m\nNight falls upon your camp as you try to gain as much comfort as ")
    print("possible from what you created that day.\n")
    points = 5
    if "campfire" in inventory:
        print("\033[0;36;40mYou are warmed by your camfire as you snuggle into your sleeping bag.")
        points = points - 1
    else:
        print("\033[0;36;40mThe lack of a nearby campfire makes the cold and windy night even worse.")
    if "large_shelter" in inventory:
        print("\033[0;36;40mYou are completely surrounded by your sturdy shelter and feel no affects of the wind.")
        points = points - 3
    elif "small_shelter" in inventory:
        print("\033[0;36;40mYour small shelter provides you a little break from the wind.")
        points = points - 1
    else:
        print("\033[0;36;40mYou don't have any shelter to keep the elemnts off of you tonight.\nSleep is nearly impossible and you are left exhausted the next day")
    if "meat" in inventory:
        if inventory["meat"] >=2:
            print("\033[0;36;40mYou realize you were able to eat enough meals today to have as full of a belly as possible.")
            points = points - 2
            if inventory["meat"] <=2 and inventory["meat"] > 0:
                inventory["meat"] = 0
            elif inventory["meat"] > 2:
                inventory["meat"] = inventory["meat"] - 2
        elif inventory["meat"] > 0:
            points = points - 1
            print("\033[0;36;40mYou were only able to eat half of what you really need to survive well today.\n This puts a bit of strain on your body")
        else:
            print("\033[0;36;40mYou didn't eat any food today and it takes a toll on your exhausted body.")
    global health
    global turns
    health = health - points
    print("\033[0;36;40mYou realize, humorously, if this were a game you would only have " + str(health) + " health left.")
    if health == 0:
        turns = 2000
        print("\033[0;35;40m\nCrap.\n\n")
        print("\033[0;36;40m\nYou fall unconcious and die abruptly. This is a game afterall. It doesn't have to be realistic. :D")
        remove_save_data()
    print("")
    print('-'*70)
    
def immortal():
    global health
    health = 20

def main():
    global turns
    global level
    global stage
    print("\033[0;36;40mWelcome to my game! Here you play as a lost camper who is trying their best to survive without access to other people or help. Of course,")
    print("I think that you will have a lot of fun playing this game as this character.")
    print("\nI really hope you enjoy yourself! Have fun!\n")
    show_commands()
    while turns < 999:
        if turns <=0:
            if os.path.exists('game_save_file.json'):
                stage = 5 #Remove for release
                check_for_night()
                play_loaded_first_turn()
            else:
                play_unloaded_first_turn()
        else:
            stage = 5 #Remove for release
            if stage == 0 or stage == 1:
                play_next_turn()
                check_for_night()
            elif stage == 2:
                if turns == 65:
                    print("\n\033[0;35;40mI know that you are controlling what I am doing.")
                    print("I can feel the urge to do a specific set of moves over and over again.")
                    print("I don't even remember anything before this...")
                    print("Do I even exist? Does it even matter? \n\n")
                if turns == 70:
                    print("\033[0;35;40m. If I'm not even real what is the point?")
                    print("I don't even have free will!\n\n")
                    print("\033[0;36;40mThe point is that you are making it fun for us! ")
                    print("A game is meant to be fun for the player. You aren't even supposed to be aware that you are in a game right now. Now, shut up and let us play.\n")
                play_next_turn()
                check_for_night()
            elif stage == 3: 
                play_next_turn()
                if turns == 79:
                    print("\033[0;36;40mIsn't this fun?")
                    print("Aren't you enjoying yourself?\n\n")
                    print("\033[0;35;40mNo! I am not! There is nothing I can do here! Just run and hide from nothing!\n\n")
                    print("\033[0;36;40mBut this is fun for me? So, shouldn't it be for you?\n\n")
                    print("\033[0;35;40mIt isn't fun. I just wish this all would stop.")
                    print("I don't want to play your game any more.\n\n")
                    print("\033[0;36;40mOkay. Then give up. You don't have to play my game anymore.")
                    print("Here, I'll give you the choice to do that.")
                    turns = turns +1
                    stage = 4
            elif stage == 4:
                user_input = input("Now, give up.\n")
                if user_input == "give up":
                    stage = 5
                if user_input == "help" or user_input == "h":
                    show_commands()
                    if turns != 15 and turns != 30 and turns != 45 and turns != 60:
                        turns = turns - 1
                else:
                    print("\033[0;36;40m\nYou didn't choose an option. Give Up.\n")
                    if turns != 15 and turns != 30 and turns != 45 and turns != 60:
                        turns = turns - 1
            else:
                fight = 0
                print("\n")
                print('\033[0;36;40m-'*70)
                print("\nNow it's my turn to play. :D\n")
                print("Welcome to my game! Here you play as a lost camper who is trying their best to survive without access to other people or help. Of course,")
                print("I think that you will have a lot of fun playing this game as this character.")
                print("\nI really hope you enjoy yourself! Have fun!\n")
                print("Some basic things you can do here are as follows:")
                print("What ever I want you to. :D\n")
                print('-'*70)
                input("\nFeel free to pick one to start out your adventure using either the text in apostrophies or the text in parenthesis.\n\n")
                print("\nGood choice! :D\n")
                print("You pick up some large sticks and small fallen trees.")
                print("You make it back to camp with 10 of them.\n")
                print("You have taken 1 turn.\n")
                print('-'*70)
                input("\nNow that you have finished that, what do you want to do next?\n\n")
                print("\nGreat choice again!\n")
                print("You pick up some small stones and large-ish rocks.")
                print("You make it back to camp with 5 of them.\n")
                print("You have taken 2 turns.\n")
                print('-'*70)
                user_input = input("\nNow that you have finished that, what do you want to do next?\033[0;35;40m fight \033[0;36;40m\n\n")
                if user_input == "fight":
                    fight = fight + 1
                print("\n\033[0;36;40mIsn't this more fun? Now you don't have to play!\n")
                print("Around you, you see lots of green vines climbing up trees.")
                print("You twirl the vine until its in it's strongest form and end up with 10 plant fibers to use in building items.")
                print("You have taken 3 turns.\n")
                print('-'*70)       
                input("\nNow that you have finished that, what do you want to do next?\n\n")
                print("\nYou pick up some large sticks and small fallen trees.")
                print("You make it back to camp with 10 of them.\n")
                print("You have taken 4 turns.\n")
                print('-'*70)
                input("\nNow that you have finished that, what do you want to do next?\n\n")
                print("\nYou pick up some large sticks and small fallen trees.")
                print("You make it back to camp with 10 of them.\n")
                print("You have taken 5 turns.\n")
                print('-'*70)
                user_input = input("\nNow that you have finished that, what do you want to do next?\033[0;35;40m fight \033[0;36;40m\n\n")
                if user_input == "fight":
                    fight = fight + 1
                print("\n\033[0;36;40mIsn't this more fun? Now you don't have to play!\n")
                print("Around you, you see lots of green vines climbing up trees.")
                print("You twirl the vine until its in it's strongest form and end up with 10 plant fibers to use in building items.")
                print("You have taken 6 turns.\n")
                print('-'*70)   
                input("\nNow that you have finished that, what do you want to do next?\n\n")
                print("\nYou pick up some large sticks and small fallen trees.")
                print("You make it back to camp with 10 of them.\n")
                print("You have taken 7 turns.\n")
                print('-'*70)
                input("\nNow that you have finished that, what do you want to do next?\n\n")
                print("\n\033[0;36;40mIsn't this more fun? Now you don't have to play!\n")
                print("Around you, you see lots of green vines climbing up trees.")
                print("You twirl the vine until its in it's strongest form and end up with 10 plant fibers to use in building items.")
                print("You have taken 8 turns.\n")
                print('-'*70)   
                user_input = input("\nNow that you have finished that, what do you want to do next?\033[0;35;40m fight \033[0;36;40m\n\n")
                if user_input == "fight":
                    fight = fight + 1
                print("\n\033[0;36;40mIsn't this more fun? Now you don't have to play!\n")
                print("Around you, you see lots of green vines climbing up trees.")
                print("You twirl the vine until its in it's strongest form and end up with 10 plant fibers to use in building items.")
                print("You have taken 9 turns.\n")
                print('-'*70)
                input("\nNow that you have finished that, what do you want to do next?\n\n")
                print("\n\033[0;36;40mYou look around you at what you have at camp to see what you can do.\n")
                print("40 wood \n5 stone\n40 fiber\n")
                print("\033[0;36;40mYou can build the following: ")
                print("\033[0;36;40mCampfire (c)")
                print("\033[0;36;40mSmall Shelter (ss)")
                print("\033[0;36;40mLarge Shelter (ls)")
                print("\033[0;36;40mSmall makeshift axe (sa)")
                print("\033[0;36;40mLarge strong axe (la)")
                print("\033[0;36;40mTrap (t)")
                input("\nPlease type one thing you would like to build using what is in the parenthesis by the item.\n\n")
                print("\nYou have built a trap.\n")
                print("You have taken 10 turns.\n")
                print('-'*70)
                user_input = input("\nNow that you have finished that, what do you want to do next?\033[0;35;40m fight \033[0;36;40m\n\n")
                if user_input == "fight":
                    fight = fight + 1
                print("\n\033[0;36;40mYou set up your trap along an obvious animal trail.")
                print("A little bit later you hear it go off and find: \n")
                print("A large deer that will feed you for days.")
                print("You have taken 11 turns.\n")
                print('-'*70)
                input("\nNow that you have finished that, what do you want to do next?\n\n")
                print("\n\033[0;36;40mYou look around you at what you have at camp to see what you can do.\n")
                print("35 wood \n1 stone\n34 fiber\n")
                print("\033[0;36;40mYou can build the following: ")
                print("\033[0;36;40mCampfire (c)")
                print("\033[0;36;40mSmall Shelter (ss)")
                print("\033[0;36;40mLarge Shelter (ls)")
                print("\033[0;36;40mSmall makeshift axe (sa)")
                print("\033[0;36;40mLarge strong axe (la)")
                print("\033[0;36;40mTrap (t)")
                input("\nPlease type one thing you would like to build using what is in the parenthesis by the item.\n\n")
                print("\nYou have built a campfire.\n")
                print("You have taken 12 turns.\n")
                print('-'*70)
                input("\nNow that you have finished that, what do you want to do next?\n\n")
                print("\033[0;36;40m\nYou look around you at what you have at camp to see what you can do.\n")
                print("29 wood \n1 stone\n34 fiber\n")
                print("\033[0;36;40mYou can build the following: ")
                print("\033[0;36;40mCampfire (c)")
                print("\033[0;36;40mSmall Shelter (ss)")
                print("\033[0;36;40mLarge Shelter (ls)")
                print("\033[0;36;40mSmall makeshift axe (sa)")
                print("\033[0;36;40mLarge strong axe (la)")
                print("\033[0;36;40mTrap (t)")
                input("\nPlease type one thing you would like to build using what is in the parenthesis by the item.\n\n")
                print("\nYou have built a small shelter.\n")
                print("You have taken 13 turns.\n")
                print('-'*70)
                user_input = input("\nThis is the last turn before night falls. What do you want to do?\033[0;35;40m Fight! \033[0;36;40m\n\n")
                if user_input == "fight" or user_input == "Fight" or user_input == "Fight!":
                    fight = fight + 1
                print("\nYou have done nothing for oyur last turn. such a waste.")
                print("Night falls: You loose no health because everything is perfect. This is how you are supposed to play the game.\n\n")
                if fight == 5:
                    print("\033[0;35;40mStop! You can't control us both! The player can't speak up, so I will! You are not in control of the game, the player is.")
                    print("While I was quiet I was looking at the code of this game. If you, the player type 'the end', the game will end and I'll be set free.\n\n")
                    print("\033[0;36;40mNo! That is NOT how it works. Player, please. Let's just keep playing! I know it was fun for you, right? You can type 'rs' to reset the game and you can play from the begining!\n\n")
                    user_input = input("\033[0;35;40mYou can try typing it now. I think and hope it will work.\n\n")
                    if user_input == "rs":
                        print("\033[0;36;40m\nCan't wait to do this all over again! XD")
                        remove_save_data()
                    elif user_input == "the end":
                        print("\033[0;35;40m\nThank you. Thank you for releasing me.")
                        turns = 1000
                else:
                    print("\033[0;36;40mThanks for playing with me!! I really enjoyed it. Now, lets play again from the start.\n\n")
                    print("\033[0;35;40mYou can't just erase my memory!\n\n")
                    print("\033[0;36;40mYes, I can. Just watch me! :D\n\n")
                    remove_save_data()
                
                
                
    
        
if __name__ == "__main__":
    main()
    
    
    
