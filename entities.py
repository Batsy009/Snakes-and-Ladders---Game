import snake
import ladder
import time

print("\nGame details are :")

# Object of Snakes
snake1 = snake.Snakes("Snake 1", 93, 60)
snake2 = snake.Snakes("Snake 2", 70, 40)
snake3 = snake.Snakes("Snake 3", 50, 10)
snake4 = snake.Snakes("Snake 4", 30, 5)
all_snakes = [snake1, snake2, snake3, snake4]

time.sleep(0.5)
# Displaying Snake Details
print(f"\nSnake Name :\t{snake1.name} \t{snake2.name} \t{snake3.name} \t{snake4.name}")
print(f"Snake Head :\t{snake1.head} \t\t\t{snake2.head} \t\t\t{snake3.head} \t\t\t{snake4.head}")
print(f"Snake Tail :\t{snake1.tail} \t\t\t{snake2.tail} \t\t\t{snake3.tail} \t\t\t{snake4.tail}")

# Object of Ladders
ladder1 = ladder.Ladders("Ladder 1", 24, 4)
ladder2 = ladder.Ladders("Ladder 2", 48, 12)
ladder3 = ladder.Ladders("Ladder 3", 88, 36)
ladder4 = ladder.Ladders("Ladder 4", 92, 56)
all_ladders = [ladder1, ladder2, ladder3, ladder4]

time.sleep(0.5)
# Displaying Ladder Details
print(f"\nLadder Name :\t{ladder1.name} \t{ladder2.name} \t{ladder3.name} \t{ladder4.name}")
print(f"Ladder Tail :\t{ladder1.tail} \t\t\t{ladder2.tail} \t\t\t{ladder3.tail} \t\t\t{ladder4.tail}")
print(f"Ladder Head :\t{ladder1.head} \t\t\t{ladder2.head} \t\t\t{ladder3.head} \t\t\t{ladder4.head}")
