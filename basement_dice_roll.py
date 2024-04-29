#Imports random so we can get a random dice roll number
import random

class DiceGame:
    #sets the user score and cpu score to 0
    def __init__(self):
        self.user = 0
        self.cpu = 0

    #This function gives back a random number from the dice when it is "rolled"
    def roll_dice(self):
        return random.randint(1, 6)

    #Main function
    def main(self):
        #Print statements to set the scene of the basement and explains what will happen to the user
            print("As you walk down the steps to the basement you see a shadowy figure sitting across a table from you. You are nervouse but decide to take a seat.")
            print('The man says "I have been waiting for you down here; Im sure you are looking for this."')
            print("")
            print("The man holds up a shiny key that you need to escape")
            print("")
            print('The man speaks again "Ill give you this key if you can beat me in a game of luck.", he pulls out two dice, "If you can roll a higher number than me 2 out of 3 times, Ill let you have this key', end=" ")
            print('if you lose to me then you owe me your servitude until you die. Are you in?"')

            #Ask user input if they want to play
            print("")
            print("Input yes or no")

            #checks to see what the user has inputted and makes sure it is valid
            while True:
                yes_no = input().strip()

                #If yes then this print staement is amde and the loop breaks
                if yes_no.lower() == 'yes':
                    print("Perfect, let's begin.")
                    break

                #If no then this print staement is amde and the loop breaks
                elif yes_no.lower() == 'no':
                    print("No isn't an option for you right now.")
                    break

                #If the user inputs an invalid input then they are asked to input their answer again
                else:
                    print("Input yes or no")

            print("")
            print("The man slides you a dice across the table and you both are ready to roll.")
        
            while self.user < 3 and self.cpu < 3:
                #The player inputs anything to roll their dice
                print("Enter any key to roll your dice")
                key = input()

                #Calls our roll function so the user and the man both get a random roll number assigned to them
                user_roll = self.roll_dice()
                cpu_roll = self.roll_dice()

                #This sets a minimum roll of 3 for the user. This gives them a better chance to advance and play the rest of the game
                if user_roll < 3:
                    user_roll = 3

                #These print statements tell the user what themselves and the man has rolled
                print(f"You rolled a {user_roll}.")
                print(f"The man rolled a {cpu_roll}.")

                #If the user_roll is higher than the user gets a point
                if user_roll > cpu_roll:
                    self.user += 1
                    if self.user == 1:
                        print('"Its only one, Im not worried"')
                    else:
                        print('"You got lucky this time. Here is your key"')
                        break
                #If the cpu_roll is higher than the cpu gets a point
                elif cpu_roll > user_roll:
                    self.cpu += 1
                    if self.cpu == 1:
                        print('"Haha, only one more to go!"')
                    else:
                        print('"I win! Looks like the end of the road for you"')
                        print("You have lost the dice roll game and you're now stuck in the escape house forever.")
                        exit(1)

                #If both of the if statements aren't true then it is a tie and the players must roll again
                else:
                    print("A tie!")
                
                print('"Lets roll again"')

            print("The man hands you the much needed key and you hury upstairs and shut the door behind you.")
            
#Runs the main function from our DiceGame class
if __name__ == "__main__":
    game = DiceGame()
    game.main()