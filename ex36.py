from sys import exit

def dining_room():
    print "You need to choose where to sit."
    print "You can sit on the armchair."
    print "You can sit on the chair."
    print "You can sit on the couch."
    print "So where do you choose to sit?"

    next = raw_input("> ")

    if  next == "armchair":
        print "You're facing the deaf. Bye bye!"
    elif "chair" in next:
        print "You appear in the kitchen."
        kitchen()
    elif "couch" in next:
        dead("You are lost and nobody is around you.")
    else:
        dining_room()


def kitchen():
    print "Here you see an apple and a pear. You are taking a bite of?"

    next = raw_input("> ")

    if "apple" in next:
        print "You're in hell now and you see two doors. One on the left and one on the right. Which one would you choose?"
        next = raw_input("> ")
        if next == "left":
            dead("You see devil in front of you who is burning alive people in flames.")
            burnt = False

            while True:
                print "You have 3 choices:"
                print "You help him to burn other inmates."
                print "You begging him to give you a mercy."
                print "You kill yourself so you won't feel the pain later."
                print "So which option do you choose (1st, 2nd, or 3rd)?"
                next = raw_input("> ")

                if next == "1st" and not burnt:
                    print "It's probably the best thing which you could done."
                    # dedame true po apacia, kad sekanti karta nebegaletume sudeginti zmoniu ir WHILE ciklas prasideda is naujo.
                    burnt = True
                elif next == "1st" and burnt:
                    print "Nothing to burn anymore. You appear back in the kitchen."
                    kitchen()
                elif "2nd" in next:
                    dead("Devil cuts your fingers, you're watching he eats it, then pulls out your heart and you die.")
                    kill_program()
                else:
                    dead("You're dead.")
                    kill_program()

        else:
            print "You see gates of paradise. You're rescuied."

    else:
        print "You are going straight to Heaven."


def dead(print_this):
    print print_this, "Oh well."

def kill_program():
    exit(0)  

def bedroom():
    print "You are entering the bedroom. You have two choices - to take a nap on the double sized bed or on the one sized bed. What do you do?"

    next = raw_input("> ")

    if "double" in next:
        dead("You understand that something is in bed with you. An alien! He eats you and you're dead.")
    elif "one sized bed" in next:
        print "You can sleep and one could harm you. After the nap you're free to go out of teh building."
    else:
        print "You're back at the start point."
        start()

def start():
    print "You're enteting the building and you see three doors in front of you."
    print "One door is to the dining room, second door is to the kitchen and the third one is to the bedroom."
    print "You're free to choose one entrance. To which room it will be?"

    next = raw_input("> ")

    if next == "dining room":
        dining_room()
    elif "kitchen" in next:
        kitchen()
    else:
        bedroom()

start()
