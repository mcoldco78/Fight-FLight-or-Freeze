import random
import time

def displayIntro():
    print("It's 1 am, you're laying in bed drifting off to sleep when you notice your lamp went out")
    time.sleep(5)
    print("You get up to investigate, as you know that light bulb is new")
    time.sleep(5)
    print("You go to the hallway to test out that light, process of elimanation. It does not work..")
    time.sleep(7)
    print("Out of furthered curousity, you go down the hallways to test another room.")
    time.sleep(8)
    print("You make it to the end of the hallway when you realize that the front door at the bottom of the steps is wide open")
    print()

def choosePath():
    path = ""
    while path != "1" and path != "2": # input validation
        path = input("Which path will you choose? (1 or 2): ")

    return path

def checkPath(chosenPath):
    print("Everything is contingent this second")
    time.sleep(2)
    print("One action can change the course of your existence.. dead or alive..")
    time.sleep(2)
    print("You must stick with your action you decided")
    print()
    time.sleep(2)

    correctPath = (1)

    if chosenPath == str(correctPath):
        print("You succusfully ran out the door")
        time.sleep(2)
        print("You are running and make it to the police department down the street")
    else:
        print("You hesitate, you're grabbed by a set of hands coming from the bathroom to your back")
        time.sleep(2)
        print("You fade into the darkness and your fate is left with no question")
        time.sleep(2)
        print("Goodbye")


playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice) 
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")

