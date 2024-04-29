import random

class EquationFinder():
     #Initializes an empty list that we can put our equations in
    def __init__(self):
        self.equations = []

    #This function solves the equations from the list of equation that I created
    def solve_equation(self, equation):
        return eval(equation)

    #This function returns a list of all of the possible functions
    def generate_equations(self):
        return ["(5*5)+17", "8*(6-3)", "(56-33)+11", "92-58", "29+88-15", "(67+14)/9", "51/17", "75/15"]

    #This function shufles all of the equations so everytime you play the RPG you are given new equations
    def shuffle_equations(self, equations):
        random.shuffle(equations)
        return equations

class MathGame(EquationFinder):
    #Main function
    def main(self):
        print("As you enter the living room you see a cage with a key in it. The cage has a lock with 3 rows for numbers.")
        print("Next to the cage is piece of paper with 3 math equations on it. These equations must be the answers to the lock combo.")
        print("If you solve all 3 equations you will be able to get the key.")
        print("")
        print("Let's start.")
        print("")

        #These call our previously defined functions that will generate what equations are used
        self.equations = self.generate_equations()
        self.equations = self.shuffle_equations(self.equations)

        #For the 3 randomly chosen functions the equation will be displayed and the player will have to enter the correct answer
        for equation in self.equations[:3]:
            print(f"Equation: {equation}")
            print("Answer: ")
            user_answer = input()

            #This correct answer is found using our function which solves the equations
            correct_answer = self.solve_equation(equation)

            #This if statement checks to see if the user_input is correct
            if float(user_answer) == correct_answer:
                print("Correct!")
            #If user_input is wrong then an incorrect message is displayed and the lock is locked forever
            else:
                print("Wrong! The correct answer is:", correct_answer)
                print("You busted the lock with your wrong answer and the lock is locked forever. You are now stuck in the house.")
                exit(1)

        #Print statement for completing the level
        print("You have solved all of the equations and have opened the lock and secured the key.")


#Runs main function
if __name__ == "__main__":
    game = MathGame()
    game.main()