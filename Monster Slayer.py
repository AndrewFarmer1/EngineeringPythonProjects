import random

# TODO : Create lists for the monsters, weapons, and targets.
monster = ["goblin", "ghost", "dragon"]
weapon = ["sword", "bow", "magic"]
target = ["head", "body", "random"]
# TODO : Create a function that gives you the health of a monster. It should take in a monster as a parameter and return the amount of health it starts with.
def health_setter(monster):
    if monster == "goblin":
        monster_health = 10
    elif monster == "ghost":
        monster_health = 15
    elif monster == "dragon":
        monster_health = 20
    return monster_health

# TODO : Create a function that calculates the amount of damage a player will do to a monster. Its parameters should be the monster, the weapon, and the target and it should return the amount of damage the player will do. You may create additional functions to break up the logic if you wish.
def damage_calculator(monster, weapon, target):
    if monster == "goblin" and weapon == "sword" and target == "head":
        damage = 5
    elif monster == "goblin" and weapon == "sword" and target == "body":
        damage = 3
    elif monster == "goblin" and weapon == "sword" and target == "random":
        damage = random.randint (0,5)
    elif monster == "goblin" and weapon == "bow" and target == "head":
        damage = 3
    elif monster == "goblin" and weapon == "bow" and target == "body":
        damage = 5
    elif monster == "goblin" and weapon == "bow" and target == "random":
        damage = random.randint(0,5)
    elif monster == "goblin" and weapon == "magic" and target == "head":
        damage = 1
    elif monster == "goblin" and weapon == "magic" and target == "body":
        damage = 1
    elif monster == "goblin" and weapon == "magic" and target =="random":
        damage = random.randint(0,5)
    elif monster == "ghost" and weapon == "sword" and target == "head":
        damage = 3
    elif monster == "ghost" and weapon == "sword" and target == "body":
        damage = 5
    elif monster == "ghost" and weapon == "sword" and target == "random":
        damage = random.randint(0,5)
    elif monster == "ghost" and weapon == "bow" and target == "head":
        damage = 1
    elif monster == "ghost" and weapon == "bow" and target == "body":
        damage = 1
    elif monster == "ghost" and weapon == "bow" and target == "random":
        damage = random.randint(0,5)
    elif monster == "ghost" and weapon == "magic" and target == "head":
        damage = 5
    elif monster == "ghost" and weapon == "magic" and target == "body":
        damage = 3
    elif monster == "ghost" and weapon =="magic" and target == "random":
        damage = random.randint(0,5)
    elif monster == "dragon" and weapon == "sword" and target == "head":
        damage = 1
    elif monster == "dragon" and weapon == "sword" and target == "body":
        damage = 1
    elif monster == "dragon" and weapon == "sword" and target == "random":
        damage = random.randint(0,5)
    elif monster == "dragon" and weapon == "bow" and target == "head":
        damage = 3
    elif monster == "dragon" and weapon == "bow" and target == "body":
        damage = 5
    elif monter == "dragon" and weapon == "bow" and target == "random":
        damage = random.randint(0,5)
    elif monster == "dragon" and weapon == "magic" and target == "head":
        damage = 5
    elif monster == "dragon" and weapon == "magic" and target == "body":
        damage = 3
    elif monster == "dragon" and weapon == "magic" and target == "random":
        damage = random.randint(0,5)

# TODO : Create a function that calculates the amount of damage a monster will do to the player. It should take in a monster as a parameter and return the amount of health it starts with.
def monster_damage_calculator(monster):
    if monster == "dragon":
        monster_damage = random.randint(0,7)
    elif monster == "ghost":
        monster_damage =random.randint(0,5)
    elif monster == "goblin":
        monster_damage = random.randint(0,3)
def main():
    monster = random.randint(1,3)
    if monster == 1:
        monster = "goblin"
    elif monster == 2:
        monster = "ghost"
    elif monster == 3:
        monster = "dragon"


    return main(monster)
print("A " + str(monster) + " has appeared before you! It looks angry.")
choice = None
while (choice is None):
        if choice != "fight" or "run":
            print ("I didn't understand that...")

    # TODO : Exit the program if the player chose to run away. Otherwise, wish them luck in their fight.
if choice == "run":
    print ("Coward!!!")
    exit()
elif choice == ("fight"):
        print("Best of luck to you adventurer!")
    # TODO : Set the monster's starting health by calling your function
monster_health    =       health_setter(monster)
    # TODO : Set the player's starting health to 10
player_health = 10
    # Turn iterator
while monster_health > 0 and player_health > 0:
    weapon = None
    while (weapon is None):
        raw_input("Will you use sword, bow, or magic>>>")
        if weapon not in weapons:
            print ("I didn't understand that...")
        weapon = None

        # TODO : Randomly pick where the player will attack the monster. Set the result equal to the variable 'target'.
    number = random.randint(1,3)
    if number == 1:
            target = "head"
    elif number == 2:
            target = "body"
    elif number == 3:
            target = "random"  
        # TODO : Set the amount of damage the player will deal to the monster by calling your function
    damage = damage_calculator(monster, weapon, target)
        # TODO : Deal damage to the monster.
    monster_health = monster_health - damage
        # TODO : If the monster is still alive, set the amount of damage the monster will deal to the player by calling your function
    if monster_health > 0:
            damage = monster_damage_calculator(monster)    
        # TODO : Deal damage to the player.
    player_health =  player_health - damage
        # TODO : Inform the player of their health and the monster's health at the end of every turn
print("The monster has " + int(monster_health) + " health.")
print("You have " + int(player_health) + " health." )
    # TODO : Display either a game over or victory message once either the player or the monster has run out of health
if monster_health == 0:
   print("Congratulations")
elif player_health == 0:
    print ("You have died, better luck next time mate. ")
main()