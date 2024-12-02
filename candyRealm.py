import random


def shuffle_cards(letters):
    for i in range(5):
        random.shuffle(letters)
    return letters


def display(num_cards, letters):
    players = []

    for i in range(4):
        array = ['     ']
        array += [' '] * ((num_cards * 6) * 2)
        array[1] = i + 1
        players.append(array)

    start_line = []
    cards_line = []
    array1 = [' '] * ((len(letters) * num_cards))
    array2 = [' '] * ((len(letters) * num_cards))
    temp_array = [letter for letter in letters for _ in range(num_cards)]
    for i in range(len(array1)):
        array1[i] = temp_array[i]
        i += 1
        
    for i in range(len(array2)):
        array2[i] = temp_array[i]
        i += 1
        
    array1 = shuffle_cards(array1)
    array2 = shuffle_cards(array2)
    array1.insert(0, 'START')
    array1.append('GOAL!')
    array2.insert(0, 'CARDS')
    start_line.append(array1)
    cards_line.append(array2)
    return players, start_line, cards_line


def setup_game():
    while True:
        try:
            sec_input = int(input('How Many Human Players [1] - [4]?: '))
            if 1 <= sec_input <= 4:
                break
            else:
                print('Invalid input. Enter a number between 1 and 4')
        except ValueError:
            print("Invalid input. Enter a NUMBER between 1 and 4.")
    while True:
        try:
            thrd_input = int(input('How Many Copies Of Each Card [1] - [5]?: '))
            if 1 <= thrd_input <= 5:
                break
            else:
                print('Invalid input. Enter a number between 1 and 5')
        except ValueError:
            print('Invalid input. Enter a NUMBER between 1 and 5')

    letter_list = ['M', 'R', 'B', 'C', 'G', 'Y']
    players_list, start, cards = display(thrd_input, letter_list) 
    return players_list, start, sec_input, cards, sec_input


def check_letter_in_list(list_to_check, item, start_index):
    return item in list_to_check[start_index + 1:]


def check_win(position, win_tile):
    if position < 0 or win_tile <= position:
        return False  
    return position == win_tile - 1


def check_letter_in_list(chk_list, item, start_index):
    try:
        return chk_list.index(item, start_index + 1) 
    except ValueError:
        return None  
    
def player_left(players_list):
    nums_players = [1, 2, 3, 4]
    for player in nums_players:

        if player not in players_list:
            return player  
        
    return None 


def play_game():
    player_display, start, player_num, cards, num_human_Player = setup_game()
    for i in range(len(player_display)):
        print(*player_display[i])

    for i in range(len(start)):
        print(*start[i])

    for i in range(len(cards)):
        print(*cards[i])
    
    nums_list = []
    game_status = True
    while game_status:
        for i in range(len(player_display)):
            if (i + 1) in nums_list:
                continue

            while True:
                curr_player_num = i + 1
                player_type = 'HUMAN' if i < num_human_Player else 'COMPUTER'
                if player_type == 'HUMAN':
                    try:
                        fr_input = str(input(f'Player {i + 1}: Would you like to [d]raw a {cards[0][1]} card, [s]huffle the deck, or [q]uit?: ')).strip().lower()
                        if fr_input in ['d', 's', 'q']:
                            break
                        else:
                            print('Invalid input. Enter [d], [s], or [q]')
                    except ValueError:
                        print('Invalid Input. Enter LETTER [d], [s], or [q]')
                else:
                    choise_list = ['d', 's', 'q']
                    num = random.randint(0, 2)
                    fr_input = choise_list[num]
                    print(f'Player {i + 1} ({player_type}) chose: {fr_input}')
                    break 

            if fr_input == 'q':
                print(f'Goodbye Player {curr_player_num}')
                nums_list.append(curr_player_num)
                player_display[i].pop(player_display[i].index(i + 1))

            elif fr_input == 's':
                print(f'Player {i + 1} ({player_type}) has shuffled the deck')
                word = cards[0].pop(0)
                new_cards = shuffle_cards(cards[0])
                cards[0] = new_cards
                cards[0].insert(0, word)

            elif fr_input == 'd':  
                index = start[0].index(cards[0][1])
                win_index = start[0].index('GOAL!')
                print(f'Player {i + 1} ({player_type}) has drawn: {cards[0][1]}')       
                next_card = check_letter_in_list(start[0], cards[0][1], player_display[i].index(curr_player_num))
                if next_card is None:
                    print(f'Invalid choice Player {i + 1}. The card {cards[0][1]} is not ahead of you.')
                    print('Please [s]huffle the deck or [q]uit on your next turn.')
                    continue  
               
                next_index = start[0].index(cards[0][1], player_display[i].index(curr_player_num) + 1)
                print(f'Player {i + 1} ({player_type}) moves forwards {next_index - player_display[i].index(curr_player_num)} spaces!') 
                player_display[i][player_display[i].index(curr_player_num)], player_display[i][next_index] = player_display[i][next_index], player_display[i][player_display[i].index(curr_player_num)]
                if check_win(player_display[i].index(curr_player_num), win_index):
                    print(f'Player {i + 1} wins!')
                    return  
            
            if len(nums_list) == 3:
                print(f'Player {player_left(nums_list)} is the only one left and wins by default.')
                return

            if len(nums_list) == 4:
                print("All players have quit. Returning to the main menu.\n")
                return  

            input("Press [ENTER] To Continue...\n")
            for display in player_display:
                print(*display)
            for start_row in start:
                print(*start_row)
            for card_row in cards:
                print(*card_row)


def main_menu():
    while True:
        print("---------------------------Welcome to Candy Realm!---------------------------")
        first_input = input('MAIN MENU: [p]lay game, [i]nstructions, or [q]uit?: ').strip().lower()
        if first_input == 'p':
            play_game()  
        elif first_input == 'i':
            print('---------------------------Instructions---------------------------')
            print('Players can choose up to 4 human players')
            print('Players can also choose how many of each card are on the board')
            print('--The game goes as follows--')  
            print('Each player either chooses to draw a card from the deck,')
            print('shuffle the deck, or quit the game.')
            print('The first player to reach the goal wins')
            print('Enjoy!\n' )
        elif first_input == 'q':
            print('Goodbye!')  
            break  
        else:
            print('Invalid input. Enter [p], [i], or [q]')


print('Candy Realm!\n')
print('By: Manasyu Chaudhari')
print('[COM S 1270]\n')


main_menu()
