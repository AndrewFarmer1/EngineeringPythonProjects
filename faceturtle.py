from turtle import *
import time
direction = None
distance = None
features = ["face","smile","eyes","mouth","reset","hat"]
color = ["black","blue", "orange"]
colorchoice =  None
count = 0 
ite = 0
rt = 0
colorchoice = None
while count < 4:
    if count == 0:
        print "hello this program will draw a face based off of your selections, if you experienced issues type reset in the next box"
        while direction == None:
            direction = raw_input("please type face,smile,eyes,hat, or reset>> ")
            print direction
            if direction in features:
                print "nice selection"
                count += 1 
                print count
                if direction == "reset":
                    for i in range(1):
                        reset(); seth(180)
                        count = 0
                        direction = None
                        time.sleep(2)
                else:
                    continue
            if direction not in features:
                print "something does not seem right"
                direction = None
                count = 0
                continue 
    if count == 1:
        while colorchoice == None:
            colorchoice = raw_input("please select either black, blue, or orange>>")
            if colorchoice in color:
                print colorchoice
                count += 1
                print count
                continue
            if colorchoice not in color:
                colorchoice = None
                continue
    if count == 2:
        if direction == "face":
            if colorchoice == "black":
                ite = 0
                while ite < 1:
                    for i in range(1):
                        pencolor("black")
                        bgcolor("white")
                        pensize(15)
                        for i in range(360):
                            fd(1); left(1)
                        for i in range(1):
                            count += 1 
                            print count
                    ite =+ 1 
            if colorchoice == "blue":
                ite = 0
                while ite < 1:
                    for i in range(1):
                        pencolor("blue")
                        bgcolor("white")
                        pensize(15)
                        for i in range(360):
                            fd(1); left(1)
                        for i in range(1):
                            count += 1 
                            print count
                    ite =+ 1
            if colorchoice == "orange":
                ite = 0
                while ite < 1:
                    for i in range(1):
                        pencolor("orange")
                        bgcolor("white")
                        pensize(15)
                        for i in range(360):
                            fd(1); left(1)
                        for i in range(1):
                            count += 1 
                            print count
                    ite += 1 
        if direction == "smile": 
            if colorchoice == "black":
                ite = 0
                while ite < 1:
                    for i in range(1):    
                        for i in range(1):
                            pencolor("black")
                            pensize(2)
                            bgcolor("white")
                            for i in range(90):
                                pendown()
                                fd(1);left(1)
                                i += 1 
                                if i >= 90:
                                    count =+ 1 
                            for i in range(1):
                                left(90); fd(90)
                                i += 1 
                                if i >= 1:
                                    count += 1
                            for i in range(1):
                                left(90)
                                i += 1 
                                if i >= 1:
                                    count += 1 
                            for i in range(80):
                                fd(1); left(1)
                                i += 1 
                                penup()
                                if i >= 90:
                                    count =+ 1
                    ite += 1
            if colorchoice == "blue":
                ite = 0
                while ite < 1:
                    for i in range(1):    
                        for i in range(1):
                            pensize(2)
                            pencolor("blue")
                            bgcolor("white")
                            for i in range(90):
                                pendown()
                                fd(1);left(1)
                                i += 1 
                                if i >= 90:
                                    count =+ 1 
                            for i in range(1):
                                left(90); fd(90)
                                i += 1 
                                if i >= 1:
                                    count += 1
                            for i in range(1):
                                left(90)
                                i += 1 
                                if i >= 1:
                                    count += 1 
                            for i in range(80):
                                fd(1); left(1)
                                i += 1 
                                penup()
                                if i >= 90:
                                    count =+ 1
                        ite += 1
            if colorchoice == "orange":
                ite = 0
                while ite < 1:
                    for i in range(1):    
                        for i in range(1):
                            pencolor("orange")
                            bgcolor("white")
                            pensize(2)
                            for i in range(90):
                                pendown()
                                fd(1);left(1)
                                i += 1 
                                if i >= 90:
                                    count =+ 1 
                            for i in range(1):
                                left(90); fd(90)
                                i += 1 
                                if i >= 1:
                                    count += 1
                            for i in range(1):
                                left(90)
                                i += 1 
                                if i >= 1:
                                    count += 1 
                            for i in range(80):
                                fd(1); left(1)
                                i += 1
                                penup() 
                                if i >= 90:
                                    count =+ 1
                        ite += 1
        if direction == "eyes": 
            if colorchoice == "black":
                ite = 0
                while ite < 1:
                    for i in range(1):
                        bgcolor("white")
                        pencolor("black")
                        pensize(15)
                        for i in range(1):
                            penup(); goto(40,65);pendown();circle(1); penup(); goto(-40,65); pendown(); circle(1)
                    ite += 1 
                    count += 1 
            if colorchoice == "blue":
                ite = 0
                while ite < 1:
                    for i in range(1):
                        bgcolor("white")
                        pencolor("blue")
                        pensize(15)
                        for i in range(1):
                            penup(); goto(40,65);pendown();circle(1); penup(); goto(-40,65); pendown(); circle(1)
                    ite += 1 
                    count += 1 
            if colorchoice == "orange":
                ite = 0
                while ite < 1:
                    for i in range(1):
                        bgcolor("white")
                        pencolor("orange")
                        pensize(15)
                        for i in range(1):
                            penup(); goto(40,65);pendown();circle(1); penup(); goto(-40,65); pendown(); circle(1)
                    ite += 1 
                    count += 1 
        if direction == "hat":
            if colorchoice == "black":
                ite = 0
                while ite < 1:
                    for i in range(1):
                        pensize(3)
                        bgcolor("white")
                        pencolor("black")
                        rt = 0
                        while rt < 1:
                            for i in range (1):
                                penup();goto(0,100);pendown(); left(0); fd(35); bk(70); goto(20,100); left(90); fd(30); left(90);fd(35); left(90); fd(35)
                            rt += 1 
                    ite += 1
                    count += 1
            if colorchoice == "blue":
                ite = 0
                while ite < 1:
                    for i in range(1):
                        pensize(3)
                        bgcolor("white")
                        pencolor("blue")
                        rt = 0
                        while rt < 1:
                            for i in range (1):
                                penup();goto(0,100);pendown(); left(0); fd(35); bk(70); goto(20,100); left(90); fd(30); left(90);fd(35); left(90); fd(35)
                            rt += 1 
                    ite += 1
                    count += 1
            if colorchoice == "orange":
                ite = 0
                while ite < 1:
                    for i in range(1):
                        pensize(3)
                        bgcolor("white")
                        pencolor("orange")
                        rt = 0
                        while rt < 1:
                            for i in range (1):
                                penup();goto(0,100);pendown(); left(0); fd(35); bk(70); goto(20,100); left(90); fd(30); left(90);fd(35); left(90); fd(35)
                            rt += 1 
                    ite += 1
                    count += 1
    if count == 3:
        for i in range(1):
            penup(); home()
        count += 1 
    if count == 4:
        direction = None
        colorchoice = None
        count = 0
