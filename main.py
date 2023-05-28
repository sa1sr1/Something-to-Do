import requests
import json


def activityRequest(suffix: str) -> str:
    try:
        response = requests.get(f"http://www.boredapi.com/api/activity{suffix}")
        js = json.loads(response.text)
        return (f"\nActivity: {js['activity']}")
    except KeyError:
        return "Sorry, no such activity exists, please try again"



def randomActivity():
    print(activityRequest("/")+"\n")


def specificActivity():
    print("\nEnter the type of activity (string, list below), number of participants (an integer),and price (decimal number) seperated by spaces")
    print("Possible types of activities: education, recreational, social, diy, charity, cooking, relaxation, music, busywork")
    print("If you have no preference for a specific attribute, don't enter anything for it\n")
    specificInput = input()
    userInputs = specificInput.split()
    typeActivity, price, numParticipants = None, None, None

    appropriateTypes = ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]

    for input_value in userInputs:
        if input_value in appropriateTypes:
            typeActivity = input_value
        elif "." in input_value:
            price = float(input_value)
        elif input_value.isdigit():
            numParticipants = int(input_value)


    suffix = []
    for assignedInputs in [typeActivity, price, numParticipants]:
        if assignedInputs is not None:
            if type(assignedInputs) == str and assignedInputs in appropriateTypes:
                suffix.append(f"type={assignedInputs}")
            elif type(assignedInputs) == float and 0 < assignedInputs < 1:
                suffix.append(f"price={assignedInputs}")
            elif type(assignedInputs) == int and assignedInputs > 0:
                suffix.append(f"participants={assignedInputs}")
    
    suffix = "&".join(suffix)
    print(activityRequest("?"+suffix)+"\n")

def playAgain() -> bool:
        print("Play again? (yes or no)\n")
        playInput = input()
        try:
            if playInput.lower()[0] == "n":
                print("\nThanks for playing!")
                return False
            return True
        except IndexError:
            print("\nInvalid input, please try again\n")
            return True

def activitySelector():
    play = True
    while play:
        print("______________________________________________________\n")
        print("1. Random Activity")
        print("2. Specify type, number of participants, and cost of activity")
        print("______________________________________________________\n")
        userInput = input()
        try:
            userInput = int(userInput)
            if userInput not in [1,2]:
                print("\nPlease enter a valid input (1 or 2)\n")
                activitySelector()
            if(userInput == 1):
                randomActivity()
            else:
                specificActivity()

        except ValueError:
            print("\nPlease enter an integer\n")
            activitySelector()

        play = playAgain()
    
    

def main():
    print("\nThis command line tool will help you find things to do \n")
    activitySelector()

if __name__ == "__main__":
    main()
