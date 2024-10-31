# Creator: Mycah Detorres
# Date: October 30, 2024

import random

'''
phraseCards is a dictionary where the keys are the phrases
and the values are a List of possible words to fill in the blank
'''
phraseCards = {
    "Christmas _____": ['tree', 'day', 'present'],
    "computer _____": ['charger', 'engineer', 'screen'],
    "_____ jar": ['mason', 'jam', 'cookie']
}


'''
Class Player
Attributes - name (int), points (int), word (String)
Method set_word() - used when each player chooses their word to fill in the blank of the current phrase card
Method add_points() - used when a player has a unique word from all other players
'''
class Player():
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.word = ""

    def set_word(self, word):
        self.word = word

    def add_points(self):
        self.points = self.points+1


''' 
Function setNumPlayers() asks user for the number of players and 
checks that user input is between 2-8 inclusive
    Input - None
    Output - int numPlayers
'''
def setNumPlayers():

    # Asks user for number of players for the game
    numPlayers = int(input(f"Input number of players (2-8): "))

    # Continuously asks user for number of players if it is not between 2-8 inclusive
    while numPlayers<2 or numPlayers>8:
        numPlayers = int(input(f"Input valid number of players (2-8): "))

    return numPlayers


''' 
Function createPlayers() creates a new instance of all the players
given numPlayers as the 
    Input - int numPlayers
    Output - List[Player()]
'''
def createPlayers(numPlayers):
    myPlayers = []
    for i in range(numPlayers):
        myPlayers.append(Player(i))
    return myPlayers


''' 
Function setNumRounds() asks user for the number of rounds and 
checks that user input is <= total number of phrase cards
    Input - int numPhraseCards
    Output - int rounds (number of rounds for the game)
'''
def setNumRounds(numPhraseCards):

    # Asks user for number of rounds for the game
    rounds = int(input(f"Input number of rounds (1-{numPhraseCards}): "))

    # Continuously asks user for number of rounds if it is not <= to the total number of phrase cards
    while rounds<=0 or rounds>numPhraseCards:
        rounds = int(input(f"Input a valid number of rounds (1-{numPhraseCards}): "))
    
    return rounds


''' 
Function pickCard() chooses a random integer from 0-total number of phrase cards
and returns the phrase at that index in phraseCards
    Input - dict phraseCards (keys: String, values: List[String])
    Output - String of possible new phrase card
'''
def pickCard(phraseCards):
    myNum = random.randint(0, len(phraseCards)-1)
    return list(phraseCards.keys())[myNum]


'''
Function playRound() picks a new phrase card that has not been used yet,
then asks the user to input a word to fill in the blank,
then chooses a random word from the values the phraseCards for the rest of the players,
then checks if any player has a unique word, and adds a point if so
    Input - Player() myPlayers, List myUsedCards, intNumPlayers
    Output - Player() myPlayers, List myUsedCards, intNumPlayers
'''
def playRound(myPlayers, myUsedCards, numPlayers):
    
    # Pick a new phrase card and add it to myUsedCards
    currentPhraseCard = pickCard(phraseCards)
    while currentPhraseCard in myUsedCards:
        currentPhraseCard = pickCard(phraseCards)
    myUsedCards.append(currentPhraseCard)
    print(f"Phrase Card: {currentPhraseCard}")
    
    # Initialize list to keep track of unique words
    wordList = []
    
    # Ask user to fill in blank with their word
    # And then choose words to fill in the blank for rest of players
    for i in range(numPlayers):

        if i == 0:
            # Prompt user to fill in the blank and set as Player0's word
            userWord = input("Fill in the blank: ")
            myPlayers[0].set_word(userWord)

            # Add user's word to wordList, to keep track of unique words
            wordList.append(userWord)
        
        else:
            # Chooses random int between 0 to len of currentPhrase's value array
            myNum = random.randint(0, len(phraseCards[currentPhraseCard])-1)
            
            # Then sets the chosen word to that index's corresponding word
            chosenWord = phraseCards[currentPhraseCard][myNum]
            myPlayers[i].set_word(chosenWord)

            # Add chosen word to wordList, to keep track of unique words
            wordList.append(chosenWord)

    # Print all players answers
    print("-------Reveal all players answers:-------")
    for j in range(numPlayers):
        print(f"Player {myPlayers[j].name+1}: {myPlayers[j].word}")

    # Compare words of all players, and add points to players with a unique word
    for k in range(numPlayers):
        wordList.remove(myPlayers[k].word)
        if myPlayers[k].word not in wordList:
            myPlayers[k].add_points()
        else:
            # Need to add word back into list to account other none unique matching words
            wordList.append(myPlayers[k].word)

    # Print all players updated points
    print("-------Updated Player Points:-------")
    for j in range(numPlayers):
        print(f"Player {myPlayers[j].name+1}: {myPlayers[j].points}")
    
    return myPlayers, myUsedCards, numPlayers



def main():

    numPhraseCards = len(phraseCards)

    # Prompts user to start new game
    print("----------------------------------------------------------------------------------------------------")
    print("---------------------------------------Fill In the Blank Game---------------------------------------")
    print("Directions: Given a phrase, fill in the blank, but try to use a unique word from all other players!")
    user_input = input("Start new game (y/n): ")

    while user_input.lower() == 'y' or user_input.lower() == 'yes':

        # Sets the number of players for the game
        numPlayers = setNumPlayers()

        # Initializes all the players
        myPlayers = createPlayers(numPlayers)

        # Sets the number of rounds for game
        numRounds = setNumRounds(numPhraseCards)

        # Initialize list for Used phrase cards
        myUsedCards = []

        # Loop to play all rounds
        for i in range(numRounds):
            print()
            print(f"---------------------Round {i+1}---------------------")
            myPlayers, myUsedCards, numPlayers = playRound(myPlayers, myUsedCards, numPlayers)

        # Find winner / winners if there is a tie
        myMax = 0
        winner = []
        for j in range(numPlayers):
            if myPlayers[j].points > myMax:
                myMax = myPlayers[j].points
                winner = []
                winner.append(myPlayers[j])
            elif myPlayers[j].points == myMax:
                winner.append(myPlayers[j])
        if myMax == 0:
            print("-------No Winner!-------")
        else:
            if len(winner) == 1:  
                print("-------Winner is:-------")
                print(f"Player {winner[0].name+1}")
            else:
                print("-------Winners are:-------")
                for k in winner:
                    print(f"Player {k.name+1}")


        # Prompts user to start new game
        print()
        print("----------------------------------------------------------------------------------------------------")
        print("---------------------------------------Fill In the Blank Game---------------------------------------")
        print("Directions: Given a phrase, fill in the blank, but try to use a unique word from all other players!")
        user_input = input("Start new game (y/n): ")

        # Resets an empty list of players for the new game
        if user_input.lower() == 'y' or user_input.lower() == 'yes':
            myPlayers = []

    

if __name__ == '__main__':
    main()




#### Brainstorming: #####
# Start or quit
# Enter number of players
# Create that number of players
# Enter number of rounds (make sure # rounds <= total number of phrase cards)
# Pick a phrase card
    # When a card is picked, it can no longer be picked for that game
    # Asks user to fill in the blank for the phrase (capitalization doesn't matter)
    # For all other players, uses a hash function to choose a word from a bank for their filled in phrase
# Compare 'blank' words
    # if word is unique, point given to that player
# After all rounds, shows winner or tie winners

# class player
# player number, points, 

#### Improvements: #####
# New game rules
    # At least 4 players
    # Need to match with just 1 person - get 3 points
    # If match with 2 people - get 1 point
    # If 0 matches, then 0 points
# Chatgpt to come up with words to fill in the blank so that it changes
# Use chatgpt to come up woth more phrase cards