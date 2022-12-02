#!/usr/bin/env python3

def main():
    handle = open("./input.txt")
    data = handle.read()

    rock = 'A'
    paper = 'B'
    scissors = 'C'
    
    lose = 'X'
    draw = 'Y'
    win = 'Z'

    rock_play_points = 1
    paper_play_points = 2
    scissors_play_points = 3

    win_points = 6
    draw_points = 3

    games = data.split('\n')
    games = list(filter(None, games))

    my_points = 0
    for game in games:
        op_play, desired_outcome = game.split(' ')

        if op_play == rock:
            if desired_outcome == win:
                my_play = paper
            elif desired_outcome == draw:
                my_play = rock
            elif desired_outcome == lose:
                my_play = scissors
        elif op_play == paper:
            if desired_outcome == win:
                my_play = scissors
            elif desired_outcome == draw:
                my_play = paper
            elif desired_outcome == lose:
                my_play = rock
        elif op_play == scissors:
            if desired_outcome == win:
                my_play = rock
            elif desired_outcome == draw:
                my_play = scissors
            elif desired_outcome == lose:
                my_play = paper

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

        # Points for what I threw
        if my_play == rock:
            my_points += rock_play_points
        elif my_play == paper:
            my_points += paper_play_points
        elif my_play == scissors:
            my_points += scissors_play_points

    print(f'{my_points}')


if __name__ == "__main__":
    main()
