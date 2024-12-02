# Manasyu Chaudhari     10-1-2024
#Assignment 3

#Project 'Nim Grab' The goal of the game is to take items from a row of items and to 
# avoid being the player who takes the very last one


print('NIMGRAB!\n')
print('By: Manasyu Chaudhari')
print('[COM S 1270 2]\n')

import random
while True:
    first_input = str(input('Do you want to [p]lay, read the [r]ules, or [q]uit?: '))
    letters =  ['p', 'r', 'q']
    while(first_input not in letters):
        first_input = str(input('Do you want to [p]lay, read the [r]ules, or [q]uit?: '))
    #----------------------------------------------------------------------------------------------------------------------
    if(first_input == 'q'):
        print('Goodbye!')
        break
    #----------------------------------------------------------------------------------------------------------------------
    elif(first_input == 'r'):
        print('Rules of the game: \n')
        print('Players take turns taking only between 1 and 3 sticks')
        print('The game continues until a player takes the last stick')
        print('That player becomes the loser and the game ends')
        print('After the game ends you can choose to:')
        print('Play the game again')
        print('read the rules')
        print('or quit the game \n')
        print('Good Luck!')       
    #----------------------------------------------------------------------------------------------------------------------    
    elif(first_input == 'p'):
        second_input = str(input('Do you want to play against [h]uman or [c]omputer?: '))
        letters2 = ['h', 'c']
        while(second_input not in letters2):                    
            second_input = str(input('Do you want to play against [h]uman or [c]omputer?: '))
        num = random.randint(20,25)
        #----------------------------------------------------------------------------------------------------------------------
        if(second_input == 'c'):
            while(num > 0):
                print(f'Items left: {num}')
                print('|' * num)
                num_input = int(input('How many items do you want to take [1-3]?: '))
                print('\n')
                while( (num_input < 1) or (num_input > 3) or (num_input > num)):
                    print('ERROR: Invalid choice. Please choose again.')
                    num_input = int(input('How many items do you want to take [1-3]?: '))
                    print('\n')
                num -= num_input
                if(num == 0):
                    print('Human took the last item. Computer wins!')
                    break
                num2 = random.randint(1,3)
                if(num <= 3):
                    if(num == 1):
                        num2 = 1
                    else:
                        num2 = num - 1  
                num -= num2
                print(f'Computer takes {num2} items \n')
                if(num == 0):
                    print('Computer took the last item. Human wins!')
                    break
        #----------------------------------------------------------------------------------------------------------------------            
        elif(second_input == 'h'):
            turn = 1  
            while num > 0:
                print(f'Items left: {num}')
                print('|' * num)
                print(f"Player {turn}'s turn:")
                num_input = int(input('How many items do you want to take [1-3]?: '))
                print('\n')
                while((num_input < 1) or (num_input > 3) or (num_input > num)):
                    print('ERROR: Invalid choice. Please choose again.')
                    num_input = int(input('How many items do you want to take [1-3]?: '))
                    print('\n')
                num -= num_input
                if(num == 0):
                    print(f'Player {turn} took the last item. Player {turn} wins!')
                    break
                turn = 1 if(turn == 2) else 2                