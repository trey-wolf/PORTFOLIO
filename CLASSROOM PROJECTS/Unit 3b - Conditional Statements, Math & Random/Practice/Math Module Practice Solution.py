# --- Challenge Problem: The Tile Project ---
# You are tiling a rectangular room and want to use the largest possible square
# tiles without having to cut any. The side length of the tiles will be the
# greatest common divisor (GCD) of the room's length and width.
#
# 1. Use math.gcd() to find the side length of the largest possible square tile.
#    The room's dimensions are 120 inches by 80 inches.
# 2. Store the result in a variable called 'tile_size'.
# 3. Print the 'tile_size' in a clear, descriptive sentence.
# 4. As an extra step, calculate how many tiles are needed to cover the room.
#    (Hint: Divide the room's total area by the tile's total area.)

import math

room_length = 120
room_width = 80

tile_size = math.gcd(room_length, room_width)
print(f"You need a tile of {tile_size}x{tile_size}")

room_area = room_length * room_width
tile_area = tile_size ** 2 # or math.pow(tile_size, 2)

num_of_tiles = room_area / tile_area

print(f"Number of tiles needed: {num_of_tiles}")

# OPTIONAL EXTENSION: Rewrite your code (refactor) such that a user can decide
# How much the room_length and room_width are before deciding the tiles
room_length = int(input("What is the length of your room"))
room_width = int(input("What is the width of your room"))

tile_size = math.gcd(room_length, room_width)
print(f"You need a tile of {tile_size}x{tile_size}")

room_area = room_length * room_width
tile_area = tile_size ** 2 # or math.pow(tile_size, 2)

num_of_tiles = room_area / tile_area

print(f"Number of tiles needed: {num_of_tiles}")