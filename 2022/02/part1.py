#!/usr/bin/env python3

def main():
    handle = open("./input.txt")
    data = handle.read()

    rock = 'A'
    paper = 'B'
    scissors = 'C'

    rock_play_points = 1
    paper_play_points = 2
    scissors_play_points = 3

    # decrypt
    data = data.replace('X', 'A')
    data = data.replace('Y', 'B')
    data = data.replace('Z', 'C')

    win_points = 6
    draw_points = 3

    games = data.split('\n')
    games = list(filter(None, games))

    my_points = 0
    for game in games:
        op_play, my_play = game.split(' ')

        # Add win/lose/draw points
        if op_play == my_play:
            my_points += draw_points
        if op_play == rock:
            if my_play == paper:
                my_points += win_points
        elif op_play == paper:
            if my_play == scissors:
                my_points += win_points
        elif op_play == scissors:
            if my_play == rock:
                my_points += win_points

        if my_play == rock:
            my_points += rock_play_points
        elif my_play == paper:
            my_points += paper_play_points
        elif my_play == scissors:
            my_points += scissors_play_points

    print(f'{my_points}')


if __name__ == "__main__":
    main()
