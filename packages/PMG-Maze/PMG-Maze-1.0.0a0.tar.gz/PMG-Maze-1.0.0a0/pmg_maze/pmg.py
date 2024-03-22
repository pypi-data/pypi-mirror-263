import numpy as np
from PIL import Image
# convert from https://github.com/vladjong/Maze/blob/main/src/model/maze.h
# and modified
# START

#import random
import numpy.random as random

from tqdm import tqdm
class MazeGenerator:
    @staticmethod
    def generate(width, height, debug=False):
        if width < 1 or height < 1:
            return None

        top_limit = 2**32 - 1  # Assuming 32-bit unsigned int for equivalence

        if top_limit // 2 <= width or top_limit // 2 <= height:
            return None

        output_height = height * 2 + 1
        output_width = width * 2 + 1

        maze = []

        if debug: print("Action 1")
        for i in tqdm(range(output_height)):
            row = []
            for j in range(output_width):
                if i % 2 == 1 and j % 2 == 1:
                    row.append(' ')
                elif ((i % 2 == 1 and j % 2 == 0 and j != 0 and j != output_width - 1) or
                      (j % 2 == 1 and i % 2 == 0 and i != 0 and i != output_height - 1)):
                    row.append(' ')
                else:
                    row.append('#')
            maze.append(row)

        row_set = [0] * width
        set_id = 1

        if debug: print("Action 2")
        for i in tqdm(range(height)):
            for j in range(width):
                if row_set[j] == 0:
                    row_set[j] = set_id
                    set_id += 1

            for j in range(width - 1):
                right_wall = random.randint(0, 2)
                if right_wall == 1 or row_set[j] == row_set[j + 1]:
                    maze[i * 2 + 1][j * 2 + 2] = '#'
                else:
                    changing_set = row_set[j + 1]
                    for l in range(width):
                        if row_set[l] == changing_set:
                            row_set[l] = row_set[j]

            for j in range(width):
                bottom_wall = random.randint(0, 2)
                count_current_set = sum(1 for l in range(width) if row_set[j] == row_set[l])
                if bottom_wall == 1 and count_current_set != 1:
                    maze[i * 2 + 2][j * 2 + 1] = '#'

            if i != height - 1:
                for j in range(width):
                    count_hole = sum(1 for l in range(width) if row_set[l] == row_set[j] and maze[i * 2 + 2][l * 2 + 1] == ' ')
                    if count_hole == 0:
                        maze[i * 2 + 2][j * 2 + 1] = ' '

                for j in range(width):
                    if maze[i * 2 + 2][j * 2 + 1] == '#':
                        row_set[j] = 0

        for j in range(width - 1):
            if row_set[j] != row_set[j + 1]:
                maze[output_height - 2][j * 2 + 2] = ' '

        return maze

    @staticmethod
    def print(maze):
        if maze is None:
            return

        for row in maze:
            print(''.join(row))
# END

def maze2pil(maze, debug=False):
    w = len(maze[0])
    h = len(maze)
    img = Image.new("RGB", (w,h), (255,255,255))
    for x, row in enumerate(maze):
        if debug: print("x: ", x, "row: ", row)
        for y,block in enumerate(row):
            if debug: print("y: ", y, "block: ", block)
            if block == '#': img.putpixel((x,y), (0,0,0))
    return img

def maze2x_y(maze, debug=False):
    w = len(maze[0])
    h = len(maze)
    x = []
    y = []
    for xx, row in enumerate(maze):
        if debug: print("x: ", xx, "row: ", row)
        for yy,block in enumerate(row):
            if debug: print("y: ", y, "block: ", block)
            if block == '#':
                x.append(xx)
                y.append(yy)
    return np.array(x), np.array(y)

def maze2matrix(maze, debug=False):
    w = len(maze[0])
    h = len(maze)
    matrix = np.zeros((w, h), dtype=int)
    for xx, row in enumerate(maze):
        if debug: print("x: ", xx, "row: ", row)
        for yy,block in enumerate(row):
            if debug: print("y: ", y, "block: ", block)
            if block == '#':
                matrix[xx][yy] = 1
    return matrix

def generate_maze(*args, **kwargs):
    return MazeGenerator.generate(*args, **kwargs)

def save_maze(maze, filename):
    np.save(filename, np.array(maze))

def load_maze(filename):
    return np.load(filename).tolist()