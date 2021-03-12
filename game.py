import random
import snake
import ladder
import board
import players
import time

print("\n----------------------------SNAKES AND LADDERS----------------------------")
print("\n Game details are :")

# Object of Snakes
snake1 = snake.Snakes("Snake 1", 90, 60)
snake2 = snake.Snakes("Snake 2", 70, 40)
snake3 = snake.Snakes("Snake 3", 50, 10)
all_snakes = [snake1, snake2, snake3]

time.sleep(0.5)
# Displaying Snake Details
print(f"\nSnake Name :\t{snake1.name} \t{snake2.name} \t{snake1.name}")
print(f"Snake Head :\t{snake1.head} \t\t\t{snake2.head} \t\t\t{snake1.head}")
print(f"Snake Tail :\t{snake1.tail} \t\t\t{snake2.tail} \t\t\t{snake1.tail}")

# Object of Ladders
ladder1 = ladder.Ladders("Ladder 1", 65, 5)
ladder2 = ladder.Ladders("Ladder 2", 75, 25)
ladder3 = ladder.Ladders("Ladder 3", 95, 55)
all_ladders = [ladder1, ladder2, ladder3]

time.sleep(0.5)
# Displaying Ladder Details
print(f"\nLadder Name :\t{ladder1.name} \t{ladder2.name} \t{ladder3.name}")
print(f"Ladder Head :\t{ladder1.head} \t\t\t{ladder2.head} \t\t\t{ladder3.head}")
print(f"Ladder Tail :\t{ladder1.tail} \t\t\t{ladder2.tail} \t\t\t{ladder3.tail}")

# Object of Board
b = board.Board(all_snakes, all_ladders)

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
        print(f"{p.name}'s turn. \nCurrent position : {p.position}")
        input("\nPress 'ENTER' to Roll the Dice \n")

        time.sleep(0.5)
        print(f"\nRolling the dice...\n")
        time.sleep(0.5)
        dice_roll = random.randint(1, 6)
        print(f"Dice rolled is: {dice_roll}")
        new_position = p.position + dice_roll

        # Snake Bite Check.
        for i in all_snakes:
            if i.head == new_position:
                new_position = i.tail
                print(f"Ohh! {p.name}, You got bit by Snake. You moved from {i.head} to {i.tail}")

        # Ladder Jump Check.
        for i in all_ladders:
            if i.tail == new_position:
                new_position = i.head
                print(f"Hurray! {p.name}, You got a ladder jump. You moved from {i.tail} to {i.head}")

        # Check if Player position is in range of Board Size.
        if new_position > b.size:
            print(f"\nOhh! {p.name}, You rolled more. Waste of roll dice. \nNo change in position.\n")
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


# Execute the Algorithm.
play()
