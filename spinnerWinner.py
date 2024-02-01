# <Graysen Schwaller>             <09/28/2023>
# <Assignment #3/ Lab 6>
# <A game in which 2 entities bet points on rolling closer to a randomized number>

# TODO: Student turns in their assignment before the 11:59 p.m. Friday deadline and the file is named spinnerWinner.py
#       (delete this TODO line when completed) (1 pt.) 
#Technically wouldn't I delete this comment after turning it in? so like the final version would never have it deleted?

import random

# NOTE: Your functions should go here!
def printTitleMaterial():
    """ This function prints the 'title material' that prints out when the program starts.
    """
    print("Spinner Winner!")
    print()

    print("By: <Graysen Schwaller>")
    print("[COM S 127 <J>]")
    print()

def initialChoice():
    """ This function allows the player to make various choices when starting the game. This is an 
    example of the 'do-while' pattern.

    :return String: The choice the player has made when starting the program to [p]lay the game, view the
    [i]nstructions, or [q]uit the program..
    """
    choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    while choice != "p" and choice != "i" and choice != "q":
        print("ERROR: Please enter 'p', 'i', or 'q'...")
        choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    return choice

def chooseNumPlayers():
    """ This function allows the player to choose whether they will play against another
    human, or play against the computer.

    :return Integer: The number of players in the game.
    """
    numPlayers = 0
    while(True): 
        numPlayers = input("[1] V.S. AI | [2] LOCAL V.S. ")
        try:
            numPlayers = (int(numPlayers))
        except:
            continue
        if(numPlayers == 1 or numPlayers == 2):
            break
    return numPlayers

def wait():
    """ This function has the computer 'wait' until the [Enter] key is pressed. This allows 
    for better 'readability' in the final output.
    """
    input("Press [Enter] To Continue...")
    print()

def printBanner(spinnerLow, spinnerHigh,numSpinners):
    """ Prints the 'banner' between each round of the game so that the output text does not 
    get too 'messy.'
    """
    print("#######################################################################")
    print()
    print("~~ Starting New Round ~~")
    print()
    print("#######################################################################")
    print()
    print("Spinners can roll {} - {} and there are {} spinners".format(spinnerLow, spinnerHigh, numSpinners))
    print()
    wait()

def printPoints(playerNum, points):
    """ This function prints the number of points a certain player currently has.

    :param Integer playerNum: The player whose points are being displayed.
    :param Integer points: The number of points to be displayed
    """
    print("* Player {0} Has {1} Points!".format(playerNum, points))
    print()

def wagerPointsHuman(playerNum, points):
    """ This function uses the 'do-while' pattern to take in input for the number of points to be wagered. It checks to
    make sure that the player has entered a valid amount of points. Meaning, the player cannot wager more points than
    they have, nor zero points, nor a negative number of points. The function then returns the wager.

    As there could potentially be two human players, this function requires the playerNum to know which player to include
    in any printouts.

    :param Integer playerNum: The player to include in any printouts. Can be 1 or 2.
    :param Integer points: The number of points the specified player currently has.
    :return Integer: The number of points to be wagered.
    """
    wager = 0
    wager = int(input("Wager points for player {} ({} available): ".format(playerNum, points)))
    while(wager == 0 or wager > points):
        print("Please try again, invalid wager (must be more than zero and an available amount of points)")
        wager = int(input("Wager points for player {} ({} available): ".format(playerNum, points)))
    return wager

def wagerPointsAI(playerNum, points):
    """ This function should choose a random number between 1 and the number of points the AI has (inclusive). For example,
    if the computer has 5 points, it can wager either 1, 2, 3, 4, or 5. This function should include a printout similar to 
    what is printed when the human wagers points.

    :param Integer playerNum: The player to include in any printouts. While this will usually be 2, including this value allows 
                              for a future version of the game with 2 computer players.
    :param Integer points: The number of points the specified player currently has.
    :return Integer: The number of points to be wagered.
    """
    wager = 0
    wager = random.randint(1,points)
    print("Wager points for player {} ({} available)[AI]: {}".format(playerNum, points, wager))
    return wager

def generateTargetValue(numSpinners, spinnerLow, spinnerHigh):
    """ This function generates the 'target value' that the players try to match. This number is generated by summing together
    random values between 'spinnerLow' and 'spinnerHigh' (inclusive), produced by a random number of spinners, between 1 and 
    numSpinners (inclusive). For example, if there are 3 spinners, and a spinner can have values between 1 - 3, then the target 
    value would be the summation of 1-3 random values between 1 and 3
    (inclusive).

    :param Integer numSpinners: The number of spinners used in the game.
    :param Integer spinnerLow: The smallest value a spinner can generate.
    :param Integer spinnerHigh: The highest value a spinner can generate.
    :return Integer: The target value generated by summing together 'numSpinners' number of random numbers between 'spinnerLow' and
                     'spinnerHigh' (inclusive).
    """
    target = 0
    spinners = random.randint(1,numSpinners)
    for i in range(spinners):
        target += random.randint(spinnerLow, spinnerHigh)
    return target

def getSpinnerChoiceHuman(playerNum, target, numSpinners, spinnerLow, spinnerHigh):
    """ This function gets the number of spinners that the human wants to spin. It should print out the 'target value' that the player
    is trying to match, as well as the values that a spinner can produce (ex: 1 - 3), and the number of spinners that can be spun. The
    player cannot pick more spinners than are in the game, nor can the pick zero spinners, nor can they pick a negative number of spinners.

    :param Integer playerNum: The player to include in any printouts. Can be 1 or 2.
    :param Integer target: The 'target value' the player is trying to match.
    :param Integer numSpinners: The total number of spinners in the game.
    :param Integer spinnerLow: The smallest value a spinner can generate.
    :param Integer spinnerHigh: The highest value a spinner can generate.
    :return Integer: The number of spinners the player chooses to spin.
    """
    spinnerChoice = 0
    while(spinnerChoice < 1 or spinnerChoice > numSpinners ):
        spinnerChoice = int(input("Number of spinners for player {} to hit the Target Value of {} ({} - {} available) ".format(playerNum, target, 1, numSpinners)))
    return spinnerChoice

def getSpinnerChoiceAI(playerNum, target, numSpinners, spinnerLow, spinnerHigh):
    """ This function gets the number of spinners that the computer wants to spin. This number should be a randomly generated value
    between 1 and numSpinners (inclusive). It should print out text similar to what the 'getSpinnerChoiceHuman()' function produces.

    :param Integer playerNum: The player to include in any printouts. While this will usually be 2, including this value allows 
                              for a future version of the game with 2 computer players.
    :param Integer target: The 'target value' the computer is trying to match. The computer does not take this value into account when
                           choosing the number of spinners - it should be used for printouts, however.
    :param Integer numSpinners: The total number of spinners in the game.
    :param Integer spinnerLow: The smallest value a spinner can generate.
    :param Integer spinnerHigh: The highest value a spinner can generate.
    :return Integer: The number of spinners the computer chooses to spin.
    """
    spinnerChoice = 0
    spinnerChoice = random.randint(1, numSpinners)
    print("Number of spinners for player {} to hit the Target Value of {} ({} - {} available) [AI] {}".format(playerNum, target, 1, numSpinners, spinnerChoice))
    return spinnerChoice

def spinSpinners(playerNum, spinnerChoice, target, spinnerLow, spinnerHigh):
    """ This function can be used for either human or computer players, and it calculates the summed values of the number of
    spinner spins. For example, if the player chooses to spin 3 spinners, and these spinners can have values between 1 and 3,
    the player could spin values of 2, 3, and 1 for a total of 6. This is the value the function would return.

    This function should print out the results of each spin as each spin is spun. The function should then print the sum of 
    all the spins and the target value once all the spins are complete.

    Please note - the winner of the round is *not* calculated here - only the spinner totals.

    :param Integer playerNum: The player to include in any printouts. Can be 1 or 2.
    :param Integer spinnerChoice: The number of spinners the player wishes to spin.
    :param Integer target: Use this value in the printout so the user can compare what they spun compared to the target.
    :param Integer spinnerLow: The smallest value a spinner can generate.
    :param Integer spinnerHigh: The highest value a spinner can generate.
    :return Integer: The sum of all the spinner spins.
    """
    spinVal = 0 # Assign the output of a random number between spinnerLow and spinnerHigh (inclusive) to this variable.
    spinTotal = 0 # Sum the spinVal values together with this variable.
    for i in range(spinnerChoice):
        spinVal = random.randint(spinnerLow, spinnerHigh)
        spinTotal += spinVal
        print("Player {}'s Spinner {} spun a {} for a total of {}/{}".format(playerNum, i+1, spinVal, spinTotal, target))
    print("Player {}'s spin total is {}/{}".format(playerNum, spinTotal,target))
    return spinTotal

def determineWin(player1Spin, player2Spin, target):
    print("player {} got {}/{}, while player {} got {}/{}".format(1,player1Spin,target,2,player2Spin,target))
    player1Diff = abs(target-player1Spin)
    player2Diff = abs(target-player2Spin)
    if(player1Diff < player2Diff):
        print("Player 1 wins this round")
        return 1
    elif(player2Diff < player1Diff):
        print("Player 2 wins this round")
        return 2
    else:
        print("This round was a draw")
        return 0

def main():
    """ This is the main function that executes when the game is started from the terminal. It contains all of the logic/ states
    necessary to play the game.
    """
    # main script running control variable
    running = True
    
    # gameplay variables
    NUM_PLAYERS_POSSIBLE = 2
    SPINNER_LOW = 1 #These are magic numbers, but like pretty obvious as to what they do 
    SPINNER_HIGH = 6
    NUM_SPINNERS = 3
    INITIAL_POINTS = 10
    player1Points = INITIAL_POINTS
    player2Points = INITIAL_POINTS

    # print the title/ author information
    printTitleMaterial()

    # play the game
    while running:
        choice = initialChoice()
        if choice == "p":

            numPlayers = chooseNumPlayers()
            isAI = numPlayers < NUM_PLAYERS_POSSIBLE
            # main game loop
            while True:
                # round setup
                SPINNER_LOW = random.randint(1,6)
                SPINNER_HIGH = random.randint(SPINNER_LOW+1, 12)
                NUM_SPINNERS = random.randint(3,10)
                printBanner(SPINNER_LOW, SPINNER_HIGH, NUM_SPINNERS)

                # NOTE: You can do this any way you like - in fact, you can even discard this file entirely and make your own version!
                #       The comments below provide a general outline of the overall 'algorithm' of the game
                #       Each comment could have multiple lines of code associated with it
                #       Your job is to iteratively build up a game that works - it doesn't really matter how you code it

                # Find a target value.
                target_Val = generateTargetValue(NUM_SPINNERS,SPINNER_LOW,SPINNER_HIGH)
                # Player 1 wager. (Player 1 will always be human.)
                play1Wage = wagerPointsHuman(1,player1Points)
                # Player 2 wager. (Player 2 can be either human or AI - you must account for both.)
                if(isAI):
                    play2Wage = wagerPointsAI(2,player2Points)
                else:
                    play2Wage = wagerPointsHuman(2,player2Points)
                # Player 1 spin - get the total of all the spinners. (Player 1 will always be human.)
                play1SpinChoice = getSpinnerChoiceHuman(1,target_Val, NUM_SPINNERS,SPINNER_LOW,SPINNER_HIGH)
                # Player 2 spin - get the total of all the spinners. (Player 2 can be either human or AI - you must account for both.)
                if(isAI):
                    play2SpinChoice = getSpinnerChoiceAI(2,target_Val, NUM_SPINNERS,SPINNER_LOW,SPINNER_HIGH)
                else:
                    play2SpinChoice = getSpinnerChoiceHuman(2,target_Val, NUM_SPINNERS,SPINNER_LOW,SPINNER_HIGH)
                # Calculate Winner of the round. (If Player1 is closer, Player 1 wins. Else if Player 2 is closer Player 2 wins. If they are equal it is a draw.)
                play1Spun = spinSpinners(1, play1SpinChoice, target_Val, SPINNER_LOW, SPINNER_HIGH)
                wait()
                play2Spun = spinSpinners(2, play2SpinChoice, target_Val, SPINNER_LOW, SPINNER_HIGH)
                wait()
                winner = determineWin(play1Spun, play2Spun, target_Val)
                if(winner == 1):
                    player1Points += play1Wage
                    player2Points -= play2Wage
                elif(winner == 2):
                    player1Points -= play1Wage
                    player2Points += play2Wage
                # Print the points for both players.
                print("Player {} has {} points".format(1, player1Points))
                if(isAI):
                    print("Player {} has {} points [AI]".format(2, player2Points))
                else:
                    print("Player {} has {} points".format(2, player2Points))
                # Check of the game is over - if it is, print a 'game over' message, reset the points to default values, 
                # and break out of the gameplay loop. Otherwise, print that it is the end of the round.
                if(player1Points == 0 or player2Points == 0):
                    if(player1Points == 0):
                        print("Player {} wins!!".format(2))
                    elif(player2Points == 0):
                        print("Player {} wins!!".format(1))
                    else:
                        print("This shouldn't have printed lol")
                    wait()
                    print("#######################################################################")
                    print("GAME OVER")
                    print("#######################################################################")
                    player2Points = INITIAL_POINTS
                    player1Points = INITIAL_POINTS
                    break
                else:
                    print("#######################################################################")
                    print("END OF ROUND")
                    print("#######################################################################")
                    wait()

        elif choice == "i":
            print("\nThe user selects a game between one or two players. A one player game has the user play against the computer. A two player game has two users play against one another.\n\nThe players start the game with a certain number of 'points.'\n\nThe game is divided into 'rounds.'At the start of the 'round,' the computer generates a 'target value.'This is the value that the players try to match.\n\nAt the start of the 'round,' each player 'wagers' a certain number of 'points.'Players cannot 'wager' more 'points' than they have. Nor can they 'wager' zero (0)'points.' Nor can they 'wager' a negative number of 'points.'\n\nThen each player decides how many 'spinners' to spin.Each spin adds its value to a final 'spin value' for the round.Players can not spin more spinners than are available to be spun. Nor can the spinzero (0) spinners. Nor can they spin a negative number of spinners.After each player spins their 'spinners,' their 'spin value' is compared against the 'targetvalue.'\n\nThe player who gets their 'spin value' closest to the 'target value' is the winner of the round.If both players 'spin value' are equally distant from the 'target value' the round is a'draw.'\n\nOnce the winner is decided, 'points' are added and subtracted from each player's score.The winning player gets their wager amount added to their score.The losing player gets their wager amount subtracted from their score.\n\nThe game continues until one player is completely out of 'points.'")
        elif choice == "q":
            theRareOne = "I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU  (This was supposed to be rare, and in my defense, I was bored)"
            exitPhrases = ["Hope you have a nice day!", "Hope you have a mediocre day!", "Hope you have a poor day", "Hope you are doing ok!", "",  "I hope you didn't encounter the really bad exit message!", theRareOne]
            randomExitPhrase = random.choice(exitPhrases)
            if(randomExitPhrase == theRareOne):
                randomExitPhrase = random.choice(exitPhrases)
            print("Goodbye! {}".format(randomExitPhrase))
            running = False
        else:
            print("ERROR: Variable 'choice' should have been 'p', 'i', or 'q', but instead was:", choice)
            quit()

if __name__ == "__main__":
    main()
