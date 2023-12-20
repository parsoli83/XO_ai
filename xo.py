enemy = -1
me = +1
table = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


def wins(table, player):
    
    win_table = [
        [table[0][0], table[0][1], table[0][2]],
        [table[1][0], table[1][1], table[1][2]],
        [table[2][0], table[2][1], table[2][2]],
        [table[0][0], table[1][0], table[2][0]],
        [table[0][1], table[1][1], table[2][1]],
        [table[0][2], table[1][2], table[2][2]],
        [table[0][0], table[1][1], table[2][2]],
        [table[2][0], table[1][1], table[0][2]],
    ]
    if [player, player, player] in win_table:
        return True
    else:
        return False


def game_over(table):
    
    return wins(table, enemy) or wins(table, me)


def available_spots(table):
    
    spots = []

    for x, row in enumerate(table):
        for y, spot in enumerate(row):
            if spot == 0:
                spots.append([x, y])

    return spots


def minimax(table, depth, player):
    
    if player == me:
        best = [-1, -1, -10000]
    else:
        best = [-1, -1, 10000]
    bot_win=wins(table, me)
    enemy_win=wins(table, enemy)
    if depth == 0 :
        if wins(table, me):
            score = +1
        elif wins(table, enemy):
            score = -1
        else:
            score = 0
        return [-1, -1, score]

    for spot in available_spots(table):
        x, y = spot[0], spot[1]
        table[x][y] = player
        score = minimax(table, depth - 1, -player)
        table[x][y] = 0
        score[0], score[1] = x, y

        if player == me:
            if score[2] > best[2]:
                best = score  
        else:
            if score[2] < best[2]:
                best = score  
    return best





def render(table, me_char, enemy_char):
    

    chars = {
        -1: enemy_char,
        +1: me_char,
        0: ' '
    }
    str_line = '.'*15

    print('\n' + str_line)
    for row in table:
        for spot in row:
            symbol = chars[spot]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def ai_turn(me_char, enemy_char):
    
    depth = len(available_spots(table))
    if depth == 0 or game_over(table):
        return

    print(f'me turn [{me_char}]')
    render(table, me_char, enemy_char)

    
    move = minimax(table, depth, me)
    x, y = move[0], move[1]

    if [x, y] in available_spots(table):
        table[x][y] = me


def enemy_turn(me_char, enemy_char):
    
    depth = len(available_spots(table))
    if depth == 0 or game_over(table):
        return

    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    
    print(f'enemy turn [{enemy_char}]')
    render(table, me_char, enemy_char)

    while move < 1 or move > 9:
        try:
            move = int(input('which spot? [1:9]: '))
            coord = moves[move]
            if [coord[0], coord[1]] in available_spots(table):
                table[coord[0]][coord[1]] = enemy
                can_move=True
            else:
                can_move = False
                

            if not can_move:
                print('invalid move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('exit')
            exit()
        except (KeyError, ValueError):
            print('invalid move')


def main():
    
    enemy_char = '' 
    me_char = '' 
    first = ''  

    while enemy_char != 'O' and enemy_char != 'X':
        try:
            print('')
            enemy_char = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    
    if enemy_char == 'X':
        me_char = 'O'
    else:
        me_char = 'X'

    
    while first != 'Y' and first != 'N':
        try:
            first = input('Wanna be first?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    
    while len(available_spots(table)) > 0 and not game_over(table):
        if first == 'N':
            ai_turn(me_char, enemy_char)
            first = ''

        enemy_turn(me_char, enemy_char)
        ai_turn(me_char, enemy_char)

    if wins(table, enemy):
        print(f'enemy turn [{enemy_char}]')
        render(table, me_char, enemy_char)
        print('human won!')
    elif wins(table, me):

        print(f'me turn [{me_char}]')
        render(table, me_char, enemy_char)
        print('AI won!')
    else:
        render(table, me_char, enemy_char)
        print('DRAW!')

    exit()


if __name__ == '__main__':
    main()





































































































