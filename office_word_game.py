#Imports random so that each time the user plays they will get a new word to guess
import random

#This function prints out underscores for the amount of letters in the word in order to make it easier for players
def blank_word(word):
    blank_word = ''
    for char in word:
        if char == ' ':
            blank_word += ' '
        else:
            blank_word += '_'
    print(blank_word)

class WordGame:
    def __init__(self):
        # Dictionary of words and their riddle description
        self.word_description = {
            "newspaper": "What is black and white; and red all over?",
            "incorrectly": "Which word in the dictionary is spelled incorrectly?",
            "book": "What has many words but never speaks?",
            "stars": "They come at night without being called and are lost in the day without being stolen. What are they?",
            "lightning": "I touch the earth and I touch the sky, but if I touch you, you'll likely die. What am I?",
            "candle": "I'm tall when I'm young, and I'm short when I'm old. What am I?",
            "sponge": "What is full of holes but still holds water?"
        }
        #List of words to choose from
        self.words = list(self.word_description.keys())

    #This function selects a random word from our list of words
    def get_word(self):
        self.current_word = random.choice(self.words)
        return self.current_word

    #This function gets the riddle description of the word from the dictionary of wrods and descriptions
    def get_description(self):
        return self.word_description[self.current_word]   

    #Main function
    def main(self):
        #Prints office statement and asks the player if they want to interact with the safe
        print("You have entered the office and there is an electronic safe on the table.")
        print("You approach the safe and see that there is a message.")
        print("")
        print('It says "Hello, if you want to get the key from inside of this safe you must solve a riddle. You will have 3 chances to solve it. If you cant solve it then this safe will lock forever."')
        print("Let's play")

        #call the function from the class in order to start the game
        game = WordGame()
        word = game.get_word()
        description = game.get_description()

        #Display the description of the word
        print(f"Description: {description}")

        #Give the user 3 attempts to guess the word
        attempts = 3
        while attempts > 0:
            #prints the underscores for each leter in the word
            blank_word(word)
            #Asks the player to guess the word
            print("Guess the word: ")
            guess = input().lower()

            #If the player guesses the word correctly they unlock the safe and get a key
            if guess == word:
                print("Congratulations! You guessed the word correctly.")
                print("Here is your key for successfully completing the challenge.")
                return
            #If they play incorrectly guesses the word they lose an attempt and get to guess again
            else:
                attempts -= 1
                print(f"Incorrect guess. Attempts left: {attempts}")

        #if the player doesn't guess the word in 3 attempts, the safe locks, the player is stuck in the house and the game is over
        print(f"Sorry, you failed to guess the word. The word was: {word}")
        print("This safe is now locked and you are stuck in the escape house forever.")
        exit(1)

    #Runs main function
    if __name__ == "__main__":
        game = WordGame()
        game.main()