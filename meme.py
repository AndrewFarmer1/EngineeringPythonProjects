
# This script will keep on opening the cd player
# of a linux pc in every 5 seconds in an infinite loop
import os, time
import time, pygame.cdrom as cdrom

time.sleep(5)

while 1:
    try:
        os.system("eject cdrom")
        time.sleep(5)
    except:
        print("error")


# Using pygame module will make the code universal, i.e. This code will now run on any Operating system



#time.sleep(5)

while 1:
    cdrom.init()
    cd = cdrom.CD(0)
    cd.init()
    cd.eject()
    cd.quit()
    cdrom.quit()
    time.sleep(5)