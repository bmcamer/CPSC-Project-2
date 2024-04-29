'''
Name: Brendan Cameron
Date: 4/21/24
Assignment: Project 02
Class: CPSC 1050
Section: 001
GitHub Link: https://github.com/bmcamer/CPSC-Project-2
Description: This code allows a person to play an RPG in the terminal. In this RPG a player 
is inside a locked house and they must complete challenges in order to obtain 3 keys that'll
help them open the locked doors. The 3 challenges that need to be completed include solving a 
word riddle, having a higher dice roll than a CPU, and solving math equations. The player can
find these challenges throughout the house by entering different rooms. If the player does not
complete a challenge, then that room is locked and the player is stuck inside the house forever.
'''
import random
# Importing the WordGame class from office_word_game.py
from office_word_game import WordGame
from basement_dice_roll import DiceGame
from living_room_math_game import MathGame

#Main function
def main():
    #Initial print statements to welcome the player to the game and gives them a brief description of what they need to do
    print("Welcome to Escape House!")
    print("")
    print("In this game you will need to travel throughout the house and complete challenges", end=" ")
    print("in order to collect the 3 keys that are needed to unlock the front door and escape.")
    print("")
    print("If you fail to complete a challenge you will be locked inside the house forever.")
    print("")

    #Asks player if they are ready to begin the game
    print("Are you ready to begin?")
    print("Enter any key to play the game")
    begin_key = input()

    #Initializes an empty inventory that will be filled with they keys that can be used to leave the house
    inventory = []
    #Initializes variables to track when a user has been inside a room
    x = 0
    y = 0
    z = 0

    #List of valid rooms
    valid_rooms = ["office", "living room", "basement"]

    #Print statements let the player know that they are in the house and gives them options for what rooms they can enter
    print("You are now inside the escape house. You can explore the office, living room, and basement in order to find the keys to escape.")
    
    while len(inventory) < 3:
        print("Which room would you like to go to?")
        room_input = input().strip()
        print("")

        #This while loop is run until the player chooses a valid room to enter and explore
        while True:
            if room_input.lower() not in valid_rooms:
                print("Invalid input")
                print("Please select office, living room, or basement")
                room_input = input().strip()
            elif room_input.lower() in valid_rooms:
                break

        #If the player enters the office then our office_word_game file runs 
        if room_input.lower() == "office" and x==0:
            WordGame().main()
            print("")
            inventory.append("key")
            if len(inventory) < 3:
                print("You leave the office and search for the other keys")
            x += 1
        
        #If a player has already been in this room then they must pick a new room
        elif room_input.lower() == "office" and x==1:
            print("You have already been in this room. You need to pick a new room.")

        #If the player enters the living room then our living_room_math_game file runs
        elif room_input.lower() == "living room" and y==0:
            MathGame().main()
            print("")
            inventory.append("key")
            if len(inventory) < 3:
                print("Now search the rest of the house for those keys.")
            y += 1
        
        #If a player has already been in this room then they must pick a new room
        elif room_input.lower() == "living room" and y==1:
            print("You have already been in this room. You need to pick a new room.")

        #If the player enters the basement then our basement_dice_roll file runs
        elif room_input.lower() == "basement" and z==0:
            DiceGame().main()
            print("")
            inventory.append("key")
            if len(inventory) < 3:
                print("Now it is time to get your next key.")
            z += 1

        #If a player has already been in this room then they must pick a new room
        elif room_input.lower() == "basement" and z==1:
            print("You have already been in this room. You need to pick a new room.")  

    #Print statement for once the player obtains all 3 keys and exits the house
    print("You have obtained all 3 keys; you are now free to leave the house.")
    print("You escaped the house, congratulations! You have won!")

#Runs the main line of code    
if __name__ == "__main__":
    main()