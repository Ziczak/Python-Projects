import random

options = ['Rock', 'Paper', 'Scissor']
name = input("Enter your name: ")
ComputerScore = 0
PlayerScore = 0
NumberOfRounds = 0
gameOn = True
print(f"Welcome {name.title()}! Let's start the game! ")
while NumberOfRounds < 5:
    ComputerOption = random.choice(options)
    PlayerOption = input("Enter Rock/ Paper/ Scissor: ").title()
    print(f"Computer's option: {ComputerOption}")
    print(f"{name.title()}'s option: {PlayerOption}")
    NumberOfRounds += 1
    if ComputerOption == PlayerOption:
        print('Tie')
    elif (ComputerOption == 'Rock' and PlayerOption == 'Scissor') or (
            ComputerOption == 'Scissor' and PlayerOption == 'Paper') or (
            ComputerOption == 'Paper' and PlayerOption == 'Rock'):
        print("Computer wins")
        ComputerScore += 1
    elif (PlayerOption == 'Rock' and ComputerOption == 'Scissor') or (
            PlayerOption == 'Scissor' and ComputerOption == 'Paper') or (
            PlayerOption == 'Paper' and ComputerOption == 'Rock'):
        print(f"{name.title()} wins")
        PlayerScore += 1
    else:
        print("Choose a valid option to play this game.")
    print("-------------------------")
    print(f"Round No: {NumberOfRounds}")
    print("------ Score Board ------")
    print(f"{name.title()}: {PlayerScore} | Computer: {ComputerScore}")
    print("===============================")
    if NumberOfRounds == 5:
        again = str(input("Do you want to play again? (Type: No/Yes) "))
        if again == "Yes".upper():
            gameOn = True
            ComputerScore = 0
            PlayerScore = 0
            NumberOfRounds = 0
        else:
            if PlayerScore == ComputerScore:
                print("Draw!!")
            elif PlayerScore > ComputerScore:
                print(f"Congrats {name.title()}, you won the game!! You scored {PlayerScore}"
                      f" and the computer scored {ComputerScore}. ")
            else:
                print(f"Oops Computer won the game :( Better luck next time {name.title()}! You scored {PlayerScore}"
                      f" and the computer scored {ComputerScore}. ")

            break
