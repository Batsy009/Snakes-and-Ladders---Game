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
def next_turn(p):
    i = all_players.index(p)
    if i == len(all_players) - 1:
        i = -1
    return all_players[i + 1]


def play():
    print("\nLet's Begin the Game...")
    p = all_players[0]

    while True:
        time.sleep(0.5)
        print("-" * 80)
        print(f"It's {p.name}'s turn. \nCurrent position : {p.position}")
        input("\nPress 'ENTER' to Roll the Dice \n")

        time.sleep(0.5)
        print(f"\nRolling the dice...\n")
        time.sleep(0.5)
        dice_roll = random.randint(1, 6)
        print(f"Dice rolled is: {dice_roll}")
        new_position = p.position + dice_roll

        # Snake Bite Check.
        for i in entities.all_snakes:
            if i.head == new_position:
                new_position = i.tail
                print(f"Ohh! {p.name}, You got bit by Snake. You moved from {i.head} to {i.tail}")

        # Ladder Jump Check.
        for i in entities.all_ladders:
            if i.tail == new_position:
                new_position = i.head
                print(f"Hurray! {p.name}, You got a ladder jump. You moved from {i.tail} to {i.head}")

        # Check if Player position is in range of Board Size.
        if new_position > b.size:
            print(f"\nOhh! {p.name}, You rolled more. Waste of turn. \nNo change in position.\n")
            p = next_turn(p=p)
            continue
        print(f"{p.name} moved from {p.position} to {new_position}")
        p.position = new_position
        time.sleep(0.5)

        # Win Condition
        if p.position == b.size:
            print("Hurray!, You Reached 100. ")
            print(f"\n---------WINNER IS {p.name}. CONGRATULATIONS!----------\n")
            time.sleep(1)
            break

        # passing the turn to next player
        p = next_turn(p=p)


# Run here.
play()
