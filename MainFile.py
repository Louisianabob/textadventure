gameison = True

#Class to hold the stages
class stage:
     def __init__(self, prompt):
         self.prompt = prompt
         
         self.option1 = ""
         self.option2 = ""
         self.option3 = ""

#Initiate all the stages
gamestart = stage("Welcome to the game! (write the first prompt here for users )\n Option1: go to Paris \n Option2: Guess who dropped their car keys in the Sewers. It was you.  \n Option3: Give up and be at your home. This is MTV and u will be at ur at ur crib \n")
paris = stage("Bonjour, you arrive in Paris. \n You could go somewhere though? \n")
Sewers = stage("Dripping noises and farty smells. You're not in Paris though! You have died of dysentary \n")
Home = stage("You're home because of quarantine \n")
TheSpookyDoor = stage("The Spooky Door opens and accepts you in to the void. You take 5 damge to your life\n")
NavigatingtheVoid = stage("Beyond the door lies the vast absence. Proceed? 1. Yes 2. No\n")
BeyondMatter = stage("The metaphysical plane is a memory which no longer holds concept to you \n")



#Set the stage paths
gamestart.option1 = paris
gamestart.option2 = Sewers
gamestart.option3 = Home

paris.option1 = Sewers
paris.option2 = Home
paris.option3 = TheSpookyDoor

#sewers.option1 = 
#sewers.option2 =
#sewers.option3 =

TheSpookyDoor.option1 = NavigatingtheVoid
#TheSpookyDoor.option2 =
#TheSpookyDoor.option3 =

NavigatingtheVoid.option1 = BeyondMatter

currentstage = gamestart

if currentstage == Sewers:
     gameison = False

def promptresponse():
    global resp
    resp = input(currentstage.prompt)


#loop that runs the game
while gameison == True:
    promptresponse()

    #Allow user to quit
    if resp == "Exit":
        print("Thanks for playing!")
        gameison = False
        
    if resp == "1":
        currentstage = currentstage.option1
    elif resp == "2":
        currentstage = currentstage.option2
    elif resp == "3":
        currentstage = currentstage.option3
    else:
        print("Sorry! Bad input! Type 1 2 or 3! Thanks buddy!")
        


    




