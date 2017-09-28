import random
from time import sleep

# TODO : Create lists for the monsters, weapons, and targets.
monster = ["goblin", "ghost", "dragon"]
weapon = ["sword", "bow", "magic"]
target = ["head", "body", "random"]
choice = ["fight", "run"]
# TODO : Create a function that gives you the health of a monster. It should take in a monster as a parameter and return the amount of health it starts with.
def health_setter(monster):
    monster_health = 0
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
    elif monster == "dragon" and weapon == "bow" and target == "random":
        damage = random.randint(0,5)
    elif monster == "dragon" and weapon == "magic" and target == "head":
        damage = 5
    elif monster == "dragon" and weapon == "magic" and target == "body":
        damage = 3
    elif monster == "dragon" and weapon == "magic" and target == "random":
        damage = random.randint(0,5)
    return damage
# TODO : Create a function that calculates the amount of damage a monster will do to the player. It should take in a monster as a parameter and return the amount of health it starts with.
def monster_damage_calculator(monster):
    if monster == "dragon":
        monster_damage = random.randint(0,7)
    elif monster == "ghost":
        monster_damage =random.randint(0,5)
    elif monster == "goblin":
        monster_damage = random.randint(0,3)
    return monster_damage
def main(monster, weapon, target, choice):
    monster = random.randint(1,3)
    if monster == 1:
        monster = "goblin"
    elif monster == 2:
        monster = "ghost"
    elif monster == 3:
        monster = "dragon"
    print("A " + str(monster) + " has appeared before you! It looks angry.")
    sleep(1)
    global Choice
    choice = None
    while (choice is None):
        choice = raw_input("Would you like to fight or run>>>? ")
        if choice not in ["fight","run"]:
            print ("I didn't understand that...")
        if choice not in ["fight", "run"]:
           choice = None

    # TODO : Exit the program if the player chose to run away. Otherwise, wish them luck in their fight.
    if choice == "run":
        print("Coward!!!")
        exit()
    elif choice == ("fight"):
        print("Best of luck to you adventurer!")
        sleep(2)
    
    # TODO : Set the monster's starting health by calling your function
    monster_health    =   health_setter(monster)
    # TODO : Set the player's starting health to 10
    player_health = 10
    print("You have " + str(player_health) + " health and the monster has " + str(monster_health) + " health.")
    sleep(1)
    while monster_health > 0 and player_health > 0:
        weapon = None
        while (weapon is None):
            weapon = raw_input("Will you use sword, bow, or magic?>>>")
            if weapon not in ["sword", "bow", "magic"]:
                print ("I didn't understand that...")
            if weapon not in ["sword", "bow", "magic"]:
                weapon = None
            if weapon == "sword":
                print("You chose the sword a mighty fine weapon for a coward")
            if weapon == "bow":
                print("An archer, I see falling foes down from afar.")
            if weapon == "magic":
                print("Oh boy I love card tricks. Are you like David Blaine or Chris angle???")
    
        number = random.randint(1,3)
        if number == 1:
            target = "head"
        elif number == 2:
            target = "body"
        elif number == 3:
            target = "random"
        if number == number:
            print("You did %d damage, do not give up!!!") % number
            sleep(1)
        # TODO : Randomly pick where the player will attack the monster. Set the result equal to the variable 'target'.
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
        print ("The monster did %d damage to you, Ouch!!!") % damage
        sleep(2)
        if monster_health >= 0:
            print("The monster has %d health.") % monster_health
            sleep(1)
        if player_health >= 0:
            print("You have %d health.") % player_health
            sleep(1)
    # TODO : Display either a game over or victory message once either the player or the monster has run out of health
        if monster_health <= 0:
            print("Congratulations you have successfully murdered an innocent %s in cold blood. I hope you are happy with yourself") % monster
        elif player_health <= 0:
            print ("You have died, better luck next time mate. You got rekted by a %s man. ") %monster
        
main(monster, weapon, target, choice)