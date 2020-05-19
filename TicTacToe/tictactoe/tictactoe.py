cells = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']
position = [[cells[0], cells[1], cells[2]],
            [cells[3], cells[4], cells[5]],
            [cells[6], cells[7], cells[8]]]


# Create the initial board
def create_board():
    print("-" * 9)
    [print(f'| {" ".join(position[i])} |') for i in range(3)]
    print("-" * 9)


create_board()
num_x = position[0].count('X') + position[1].count('X') + position[2].count('X')
num_o = position[0].count('O') + position[1].count('O') + position[2].count('O')




# Returns True if all the positions are equal to O
def equal_o(location):
    result = all([x == 'O' for x in location])
    return result


# Returns True if all the positions are equal to X
def equal_x(location):
    result = all([x == 'X' for x in location])
    return result


# Find if there is more than one row with 3 X's or O's
def impossible_play(pos_1, pos_2):
    items_x = all([x == 'X' for x in pos_1])
    items_x2 = all([x == 'X' for x in pos_2])
    items_o = all([x == 'O' for x in pos_1])
    items_o2 = all([x == 'O' for x in pos_2])
    if items_x == True and items_o2 == True:
        return True
    elif items_o == True and items_x2 == True:
        return True
    else:
        return False


# Transform the coordinates to the 1-3 format
def transform_coordinate(x, y):
    if x == 1 and y == 1:
        return row_2[0]
    elif x == 1 and y == 2:
        return row_1[0]
    elif x == 1 and y == 3:
        return row_0[0]
    elif x == 2 and y == 1:
        return row_2[1]
    elif x == 2 and y == 2:
        return row_1[1]
    elif x == 2 and y == 3:
        return row_0[1]
    elif x == 3 and y == 1:
        return row_2[2]
    elif x == 3 and y == 2:
        return row_1[2]
    else:
        return row_0[2]


# Update the board with the player input
def update_board(x, y, turn):
    if x == 1 and y == 1:
        position[2][0] = 'X' if turn == 1 else 'O'
    elif x == 1 and y == 2:
        position[1][0] = 'X' if turn == 1 else 'O'
    elif x == 1 and y == 3:
        position[0][0] = 'X' if turn == 1 else 'O'
    elif x == 2 and y == 1:
        position[2][1] = 'X' if turn == 1 else 'O'
    elif x == 2 and y == 2:
        position[1][1] = 'X' if turn == 1 else 'O'
    elif x == 2 and y == 3:
        position[0][1] = 'X' if turn == 1 else 'O'
    elif x == 3 and y == 1:
        position[2][2] = 'X' if turn == 1 else 'O'
    elif x == 3 and y == 2:
        position[1][2] = 'X' if turn == 1 else 'O'
    else:
        position[0][2] = 'X' if turn == 1 else 'O'


# Define when there is a winning configuration
def state_win():
    # Cases for O winning
    if equal_o(row_0) or equal_o(row_1) or equal_o(row_2) or \
            equal_o(column_1) or equal_o(column_2) or equal_o(column_3) \
            or equal_o(diagonal_1) or equal_o(diagonal_2):
        print('O wins')
        return True
        # Cases for X winning
    elif equal_x(row_0) or equal_x(row_1) or equal_x(row_2) or \
            equal_x(column_1) or equal_x(column_2) or equal_x(column_3) \
            or equal_x(diagonal_1) or equal_x(diagonal_2):
        print('X wins')
        return True


# Define when the plays are impossible
def impossible():
    if impossible_play(row_0, row_1) or impossible_play(row_1, row_2) or impossible_play(row_0, row_2) or \
            impossible_play(column_1, column_2) or impossible_play(column_2, column_3) \
            or impossible_play(column_1, column_3):
        return True


turn = 1
while True:
    # Rows
    row_0 = [position[0][0], position[0][1], position[0][2]]
    row_1 = [position[1][0], position[1][1], position[1][2]]
    row_2 = [position[2][0], position[2][1], position[2][2]]
    # Columns
    column_1 = [position[0][0], position[1][0], position[2][0]]
    column_2 = [position[0][1], position[1][1], position[2][1]]
    column_3 = [position[0][2], position[1][2], position[2][2]]
    # Diagonals
    diagonal_1 = [position[0][0], position[1][1], position[2][2]]
    diagonal_2 = [position[2][0], position[2][1], position[0][2]]
    if abs(num_x - num_o) < 2:
        if impossible():
            print('Impossible')
            break
        if state_win():
            break
        elif ' ' not in position[0] and ' ' not in position[1] and ' ' not in position[2]:
            print('Draw')
            break
        elif not state_win():
            if ' ' in position[0] or ' ' in position[1] or ' ' in position[2]:
                try:
                    x, y = input('Enter the coordinates:').split()
                    pos_x = int(x)
                    pos_y = int(y)
                    if 1 <= pos_x <= 3:
                        if 1 <= pos_y <= 3:
                            location = transform_coordinate(pos_x, pos_y)
                            if location == " " and turn == 1:
                                update_board(pos_x, pos_y, turn)
                                print("-" * 9)
                                [print(f'| {" ".join(position[i])} |') for i in range(3)]
                                print("-" * 9)
                                turn = 2
                            elif location == " " and turn == 2:
                                update_board(pos_x, pos_y, turn)
                                print("-" * 9)
                                [print(f'| {" ".join(position[i])} |') for i in range(3)]
                                print("-" * 9)
                                turn = 1
                            else:
                                print("This cell is occupied! Choose another one!")
                        else:
                            print('Coordinates should be from 1 to 3!')
                    else:
                        print('Coordinates should be from 1 to 3!')
                except ValueError:
                    print('You should enter numbers!')

    else:
        print("Impossible")
        break
