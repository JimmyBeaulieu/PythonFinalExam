# Question1) Create a small game using Python (15 points)
#
# This is a simple game. There are 8 locations as shown by blue squares. each location has some exits shown by arrows.
# The player will move from one square to the other one, using the existing exits.
# at each move, the player chooses a direction (North, South, East, West) based on the exists available and proposed by
# the application example: the player is at square 7, then the exits are to the direction West and South.
#  The player starts at square 1.  The exits are in a dictionary, with the keys being the numbers of the
#  locations(squares) and the values being dictionaries holding the exits (as they do at present). There is no end
#  to the game. The player keeps moving around the squares.
#
#  Once that is working, create another dictionary that contains words(directions) that players may use
#  (North, South, West, East). These words will be the keys, and their values will be
#  a single letter that the program can use to determine which way to go.

exits = {
    1: {"N": 5, "E": 3, "S": 4, "W": 2},
    2: {"N": 7},
    3: {"W": 1},
    4: {"N": 1, "E": 6, "W": 8},
    5: {"S": 1, "W": 7},
    6: {"W": 4},
    7: {"E": 5, "S": 2},
    8: {"N": 2, "E": 4}
}

directions = {
    "North": "N",
    "South": "S",
    "West": "W",
    "East": "E",
}

current_location = 1

while True:
    print(f"You are at location {current_location}")
    print("Available exits:", ", ".join(exits[current_location].keys()))

    direction = input("Enter a direction to move (or 'quit' to exit): ")

    if direction == "n" or direction == "north" or direction == "N":
        direction = "North"

    if direction == "e" or direction == "east" or direction == "E":
        direction = "East"

    if direction == "s" or direction == "south" or direction == "S":
        direction = "South"

    if direction == "w" or direction == "west" or direction == "W":
        direction = "West"

    if direction.lower() == "quit":
        break

    if direction in directions:
        direction = directions[direction]

        if direction in exits[current_location]:
            current_location = exits[current_location][direction]
        else:
            print("You can't go that way!")
    else:
        print("Invalid direction!")
