count =  0
import random
import time
win = 0 
count = 0
loss = 0 
while count <= 3:
    if count == 0:
        computerchoice = random.randint(0,2)
        if computerchoice == 0:
            computerchoice = "r"
        if computerchoice == 1:
            computerchoice = "p"
        if computerchoice == 2:
            computerchoice = "s"
        print computerchoice
        print "Hello Im Roshi, Lets play some Rock, Paper, Scissors"
        time.sleep(1)
        print "I will let you in on a little secret. I am pretty good at this game"
        time.sleep(1)
        print "Now lets get to the game"
        time.sleep(1)
        choice1 = None
        while choice1 == None:
            choice1 = raw_input("Now select either r for rock, p for paper, or s for scissors>>> ")
            if choice1 in["r","p","s"]:
                print ("Good choice, but do not worry I already made my selection so no cheating for me")
                if computerchoice == "r":
                    print "I picked Rock so "
                    time.sleep(.3)
                    print("...")
                    time.sleep(.3)
                    print("..")
                    time.sleep(.3)
                    print(".")
                    if choice1 == "s":
                        print "You lose"
                        result = "Loss"
                        count = count + 1 
                        loss = loss + 1 
                        time.sleep(1)
                    if choice1 == computerchoice:
                        print "it seems to be a tie then."
                        result = "tie"
                        count = count + 1
                    if choice1 == "p":
                        print "You win"
                        result = "win"
                        count = count + 1
                        win = win + 1 
                        time.sleep(1)
                if computerchoice == "p":
                    print "I picked paper so"
                    time.sleep(.3)
                    print("...")
                    time.sleep(.3)
                    print("..")
                    time.sleep(.3)
                    print(".")
                    if choice1 == "r":
                        print "You lose"
                        result = "Loss"
                        count = count + 1 
                        loss = loss + 1 
                        time.sleep(1)
                    if choice1 == computerchoice:
                        print "it seems to be a tie then."
                        result = "tie"
                    if choice1 == "s": 
                        print "You win"
                        result = "win"
                        win = win + 1
                        count = count + 1 
                        time.sleep(1)
                if computerchoice == "s":
                    print "I picked scissors so "
                    time.sleep(.3)
                    print("...")
                    time.sleep(.3)
                    print("..")
                    time.sleep(.3)
                    print(".")
                    if choice1 == "p":
                        print "You lose"
                        result = "Loss"
                        count = count + 1
                        loss = loss + 1 
                        time.sleep(1)
                    if choice1 == computerchoice:
                        print "it seems to be a tie then."
                        result = "tie"
                        count = count + 1
                    if choice1 == "r":
                        print "You win"
                        result = "win"
                        count = count + 1
                        win = win + 1 
                        time.sleep(1)
            else:
                print "Try again something is not correct"
                choice1 =  None
        if count == 1:
            if result == "Loss":
                print "You'll get me next time"
            if result == "win":
                print "You will not be so lucky this time"
            if choice1 == "r":
                computerchoice = "p"
            if choice1 == "s":
                computerchoice = "r"
            if choice1 == "p":
                computerchoice = "s"
            choice2 = None
            while choice2 == None:
                choice2 = raw_input('Now select your next weapon."r", "p","s">>>' )
                if choice2 in["r","p","s"]:
                    if result == "win":
                        print ("lets see if your luck holds up")
                    if result == "Loss":
                        print ("I wonder if you be able to keep up this losing streak much longer")
                    if computerchoice == "r":
                        print "I picked Rock so "
                        time.sleep(.3)
                        print("...")
                        time.sleep(.3)
                        print("..")
                        time.sleep(.3)
                        print(".")
                        if choice2 == "s":
                            print "You lose"
                            result = "Loss"
                            count = count + 1 
                            loss = loss + 1
                            time.sleep(1)
                        if choice1 == computerchoice:
                            print "it seems to be a tie then."
                            result = "tie"
                            count =  count + 1
                        if choice1 == "p":
                            print "You win"
                            result = "win"
                            count = count + 1 
                            time.sleep(1)
                    if computerchoice == "p":
                        print "I picked paper so"
                        time.sleep(.3)
                        print("...")
                        time.sleep(.3)
                        print("..")
                        time.sleep(.3)
                        print(".")
                        if choice2 == "r":
                            print "You lose"
                            result = "Loss"
                            count = count + 1
                            loss = loss + 1 
                            time.sleep(1)
                        if choice1 == computerchoice:
                            print "it seems to be a tie then."
                            result = "tie"
                            count =  count + 1
                        if choice1 == "s":
                            print "You win"
                            result = "win"
                            count = count + 1 
                            time.sleep(1)
                    if computerchoice == "s":
                        print "I picked scissors so "
                        time.sleep(.3)
                        print("...")
                        time.sleep(.3)
                        print("..")
                        time.sleep(.3)
                        print(".")
                        if choice2 == "p":
                            print "You lose"
                            result = "Loss"
                            count = count + 1
                            loss = loss + 1 
                        if choice1 == computerchoice:
                            print "it seems to be a tie then."
                            result = "tie"
                            count =  count + 1  
                            time.sleep(1)
                        if choice1 == "s":
                            print "You win"
                            result = "win"
                            count = count + 1 
                            time.sleep(1)
                else:
                    choice2 = None
                    print "something does not seem quite right, try again"
        count = count + 1
        if count == 2:
            count = count + 1
        if count == 3:
            count = count + 1
        time.sleep(1)

