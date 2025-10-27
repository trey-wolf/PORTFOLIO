name = input("What is your name: ")
greeting = f"Greetings, {name}!\nYour task is to figure out a way to slay the vampire in this mansion, Count Draynor.\nThere are 5 rooms with items that you must find.\nI am told there is a key somewhere in the mansion.\nAlso, remember, vampires hate garlic and must be slayed with a blessed wooden stake.\nI hope you brought those!"
has_key, has_stake, has_garlic, stake_is_blessed = False, False, False, False
location = "Entrance"


print(greeting)

def check_location():
    global location
    return location

def change_location(current_location, new_location):
    global location
    if new_location == "Hallway" and (current_location == "Entrance" or current_location == "Kitchen" or current_location == "Garden"):
        location = "Hallway"
    elif new_location == "Kitchen" and (current_location == "Hallway"):
        location = "Kitchen"
    elif new_location == "Garden" and (current_location == "Hallway" or current_location == "Lair"):
        location = "Garden"
    elif new_location == "Throne Room" and (current_location == "Hallway"):
        location = "Throne Room"
    elif new_location == "Lair" and has_key and current_location == "Garden":
        location = "Lair"
    else:
        print(f"Cannot go to the {new_location} from the {current_location}")
        if new_location == "Lair" and (not has_key):
            print("The Lair is locked, must have a key")
        location = current_location

def pickup_item(item):
    global has_key, has_garlic, has_stake
    if item == "Key" and has_key == False:
        has_key = True
    elif item == "Stake" and has_stake == False:
        has_stake = True
    elif item == "Garlic" and has_garlic == False:
        has_garlic = True
    else:
        print(f"{item} is not something you can pickup")

def describe_location(current_loction, first_time):
    if first_time:
        if current_loction == "Entrance":
            print("You see steps leading to the eerie mansion")
            print("You sense that the is a great evil inside")
            print("If you are brave, there are steps leading to the mansion towards the east")
            print("There is nothing of interest towards the north and south")
            print("If you are scared, head west and leave")
            print("\nWhat direction do you want to go?")
        elif current_loction == "Hallway":
            print("You are greated with a Massive Hallway")
            print("You find ancient gothic architecture all around")
            print("There is a grand staircase towards the east")
            print("There are two unknown doors towards the north and south")
            print("The entrance back to safety is locked, you must continue")
            print("You notice a book shelf and a large table in the room")
            print("\nWhat do you want to do?")
        elif current_loction == " Kitchen":
            print("You walk into a kitchen")
            print("The smell of garlic and herbs fill the air")
            print("The only way back is to the south, back into the hallway")
            print("You notice a cupboard, bookshelf, and a cooking range")
            print("\nWhat do you want to do?")
        elif current_loction == "Throne Room":
            print("After walking up the stairs, you see a large throne room")
            print("The throne is made out of many long poking sticks")
            print("The only way back is to the west, back into the hallway")
            print("You notice that the throne hasnt been used for many years")
            print("You notice a chest to the right of the throne")
            print("\nWhat do you want to do?")
        elif current_loction == "Garden":
            print("You walk outside into a massive overgrown garden")
            print("You immediately notice a large, ornate and shimmering fountain")
            print("There are two ways to go from here\n-To the east is a staircase leading down under the earth\n-Back to the north, is the hallways")
            print("\nWhat do you want to do?")










