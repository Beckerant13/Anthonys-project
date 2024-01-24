#game_logics.py

import os 

class player:
    def __init__(self):
        self.name = ''
        self.feeling = ''
        self.job = 'Dealer','Junkie'
        self.hp = 0
        self.dp = 0
        self.status_effects = []
        self.location = 'Allegheny station'
        self.game_over = False
        self.solves = 0
        self.inventory = []
myPlayer = player()

class item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}: {self.description}'


money = item(name='Money', description='Currency used on the streets')
lighter = item(name='Lighter', description='Helps you light things up')
needle = item(name='Needle', description='Used for injecting substances')
spoon = item(name='Spoon', description='A utensil for cooking or preparing substances')
tourniquet = item(name='Tourniquet', description='Used to constrict blood flow')
fentanyl = item(name='Fentanyl', description= 'very strong opiate')



# Display inventory
print("Your inventory:")
for item in myPlayer.inventory:
    print(item)

def move(myAction):
        ask = "Where you trying to go?\n"
        destination = input(ask)
        if destination == 'right' or destination == 'east':
            move_dest = zonemap[myPlayer.location][RIGHT]
            move_player(move_dest)
        elif destination == 'left' or destination == 'west':
            move_dest = zonemap[myPlayer.location][LEFT]
            move_player(move_dest)
        
        else:
            print("Invalid direction command, try using forward, back, left, or right.\n")
            move(myAction)

def move_player(move_dest):
	print("\nYou have moved to the " + move_dest + ".")
	myPlayer.location = move_dest
	print_location()           


def examine():
	if room_solved[myPlayer.location] == False:
		print('\n' + (zonemap[myPlayer.location][INFO]))
		print((zonemap[myPlayer.location][PUZZLE]))
		answer = input("> ")
		checkpuzzle(answer)
	else:
		print("There is nothing new for you to see here.")

def add_to_inventory(item):
    myPlayer.inventory.append(item)
    print(f'Added {item} to your inventory.')

def remove_from_inventory(item):
    if item in myPlayer.inventory:
        myPlayer.inventory.remove(item)
        print(f'Removed {item} from your inventory.')
    else:
        print(f"{item} is not in your inventory.")

def display_inventory():
    if not myPlayer.inventory:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for item in myPlayer.inventory:
            print(f'- {item}')
           
def checkpuzzle(puzzle_answer):
    if myPlayer.location() == 'Allegheny station':
        if puzzle_answer.lower() == zonemap['Allegheny station'][SOLVED]:
            if money in myPlayer.inventory:
                myPlayer.solves = 1  
                myPlayer.inventory.append(money)
            print('You got 20 bucks')
            room_solved[myPlayer.location] = True  # Mark the puzzle as solved
        else:
            print('You need a money to proceed!')
    else:
        print('Incorrect answer. Try again.')
    
    if myPlayer.location == '7/11':
        if puzzle_answer.lower() == zonemap['7/11'][SOLVED]:
            # Check if the player has the required item 'Lighter' and 'Needle'
            if lighter in myPlayer.inventory and needle in myPlayer.inventory:
                myPlayer.solves = 2
                myPlayer.inventory.append(lighter)
                myPlayer.inventory.append(needle)
                print('You got a lighter and a needle')
                room_solved[myPlayer.location] = True  # Mark the puzzle as solved
            else:
                print('You need a lighter and a needle to proceed!')
        else:
            print('Incorrect answer. Try again.')
    
    
    if myPlayer.location == 'Kensington Gold and Silver Exchange':
        if puzzle_answer.lower() == zonemap['7/11'][SOLVED]:
            # Check if the player has the required item 'Lighter' and 'Needle'
            if lighter in myPlayer.inventory and needle in myPlayer.inventory:
                myPlayer.solves = 3
                myPlayer.inventory.append(spoon)
                myPlayer.inventory.append(tourniquet)
                print('You got spoon and a tourniquet')
                room_solved[myPlayer.location] = True  # Mark the puzzle as solved
            else:
                print('You need a spoon and a tourniquet to proceed!')
        else:
            print('Incorrect answer. Try again.')

    if myPlayer.location == 'Cam 3':
        if puzzle_answer.lower() == zonemap['Cam 3'][SOLVED]:
            # Check if the player has the required item 'Lighter' and 'Needle'
            if lighter in myPlayer.inventory and needle in myPlayer.inventory and spoon in myPlayer.inventory and tourniquet in myPlayer.inventory:
                myPlayer.solves = 4
                myPlayer.inventory.append(fentanyl)
                print('You High as fuck')
                room_solved[myPlayer.location] = True  # Mark the puzzle as solved
            else:
                print('You need all the ingredients to proceed!')
        else:
            print('Incorrect answer. Try again.')

    os.system('cls')  # Clear the console for a clean display

    

"""
How this works:

dictionary = {
	keys1: {
		keys2: Value
	}
}
"""

DESCRIPTION = 'description'
INFO = 'info'
PUZZLE = 'puzzle'
SOLVED = False
LEFT = 'left',
RIGHT = 'right',

room_solved = {'Allegheny station': False, '7/11': False, 'Kensington Gold and Silver Exchange': False, 'Cam 3': False,}
zonemap = {
        'Allegheny station': {
            DESCRIPTION: "Allegheny station",
            INFO: 'You get off the subway and you see customers or fellow victims too the FENTANYL TRAIL!',
            PUZZLE: 'You look to your left and you see a wallet on the ground.\n What do you do?',
            SOLVED: 'take money out of wallet',                                                                                   
            LEFT: '',
            RIGHT: '7/11',},
    #STEP ONE GET MONEY FOR DRUGS
    #STEP TWO GET NEEDLE AND LIGHTER
    #STEP THREE GET SPOON
    #STEP FOUR GET tourniquet
    #STEP FIVE GET HIGH :COMPLETE GAME

        '7/11': {
            DESCRIPTION: "7/11",
            INFO: 'You are in a dimmly lit conveniant store with an Indian behind the counter\n'
            'Hello buddy how i help you?',
            PUZZLE: 'You are looking for a lighter and a needle to do some drugs. the slurpy ,machine distracts you',
            SOLVED: 'buy a lighter and a needle',
            LEFT: 'Allegheny station',
            RIGHT: 'Kensington Gold and Silver Exchange',},
        'Kensington Gold and Silver Exchange' : {
            DESCRIPTION: "Kensington Gold and Silver Exchange",
            INFO: 'You arent welcome here but you desperately need a spoon. The man behind the counter looks angry. you see a medical supply case on the wall\n'
            'Man What fuck do you want?',
            PUZZLE: 'examine',
            SOLVED: 'steal spoon and steal the tourniquet from medical supply case',
            LEFT: '7/11',
            RIGHT: 'Cam 3',},
        'Cam 3' : {
            DESCRIPTION: "This is where you will FOREVER lean, you shall never fall",
            INFO: 'place to buy and do fentanyl',
            PUZZLE: 'You must do the steps in the right order or you shall D...I...E...',
            SOLVED: 'spoon, fentanyl, lighter, needle, tourniquet, shoot up',
            LEFT: 'Kensington Gold and Silver Exchange',
            RIGHT: '',},
} 
