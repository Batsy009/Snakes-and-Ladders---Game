import random
import board
import players
import time
import entities

print("\n----------------------------SNAKES AND LADDERS----------------------------")

# Object of Board
b = board.Board(entities.all_snakes, entities.all_ladders)

time.sleep(0.5)
# Object of Players
all_players = []
n = int(input("\nEnter the number of Players : "))
time.sleep(0.5)
for x in range(0, n):
    player = players.Player(input(f"\nEnter player {x + 1}: "))
    all_players.append(player)


# Turn function
def next_turn(pr):
    i = all_players.index(pr)
    if i == len(all_players) - 1:
        i = -1
    return all_players[i + 1]


def dice():
    dice_roll = random.randint(1, 6)
    print(f"Dice rolled is {dice_roll}")
    return dice_roll


def check_snake_bite(new_position, player_name):
    # Snake Bite Check.
    for i in entities.all_snakes:
        if i.head == new_position:
            new_position = i.tail
            print(f"Ohh! {player_name}, You got bit by Snake. You moved from {i.head} to {i.tail}")
            return True, new_position
    return False, new_position


def check_ladder_jump(new_position, player_name):
    # Ladder Jump Check.
    for i in entities.all_ladders:
        if i.tail == new_position:
            new_position = i.head
            print(f"Hurray! {player_name}, You got a ladder jump. You moved from {i.tail} to {i.head}")
            return True, new_position
    return False, new_position


def play(curr_player):
    time.sleep(0.5)
    print("-" * 80)
    print(f"It's {curr_player.name}'s turn. \nCurrent position : {curr_player.position}")
    input("\nPress 'ENTER' to Roll the Dice \n")
    print(f"\nRolling the dice...\n")
    time.sleep(0.5)

    d = dice()
    new_position = curr_player.position + d
    print(f"You moved from {curr_player.position} to {new_position}")
    bite, new_position = check_snake_bite(new_position, curr_player.name)
    jump, new_position = check_ladder_jump(new_position, curr_player.name)

    if new_position <= b.size:
        curr_player.position = new_position
    else:
        print("Oh!! You rolled more. Waste of a turn.")

    return d, bite, jump


def main():
    p = all_players[0]

    while True:
        dice_roll, bite, jump = play(p)
        if p.position == b.size:
            print(f"Congratulations!!. {p} won")
            break

        if dice_roll == 6 and bite is True:
            print("Unlucky. You rolled 6 but got bitten by the snake.")
            p = next_turn(p)

        elif dice_roll != 6:
            p = next_turn(p)
        else:
            print("Hurray. You got bonus move!!")


main()
