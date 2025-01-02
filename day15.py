class Box:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def __str__(self) -> str:
        return f"Box in ({self.row},{self.col})"
    def __eq__(self, other) -> bool:
        if isinstance(other, Box):
            return [self.row, self.col] == [other.row, other.col]
        return False
    def move(self, direction):
        if direction == "^" and Box(self.row-1, self.col) not in box_list and Wall(self.row-1, self.col) not in wall_list:
            self.row -= 1
        elif direction == "v" and Box(self.row+1, self.col) not in box_list and Wall(self.row+1, self.col) not in wall_list:
            self.row += 1
        elif direction == "<" and Box(self.row, self.col-1) not in box_list and Wall(self.row, self.col-1) not in wall_list:
            self.col -= 1
        elif direction == ">" and Box(self.row, self.col+1) not in box_list and Wall(self.row, self.col+1) not in wall_list:
            self.col += 1
        return self

class Wall:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def __str__(self) -> str:
        return "#"

wall_list = [ Wall(0,4) ]
box_list = [ Box(3,4), Box(2,4) ]

# TODO: all directions!
def get_boxes_to_move(robot_row, robot_col, closest_wall_row):
    # get_boxes_to_move_list
    boxes_to_move = list()
    for box in box_list:
        for r in range(robot_row, closest_wall_row, -1):
            if box == Box(row=r, col=robot_col):
               # print(box)
                boxes_to_move.append(box)
        #   print(f"mozgatandó boxok: {b}  
    boxes_to_move.sort(key=lambda b: b.row, reverse=False)
    return boxes_to_move

class Robot:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def __str__(self) -> str:
        return f"Robot in ({self.row},{self.col})"
    def can_move(self, direction):
        if direction == "^":
            boxes_to_move = list()
            walls_above_row = [ wall.row for wall in wall_list if wall.col == self.col and wall.row < self.row ]
            if len(walls_above_row) == 0: # no wall at all 
                return True
            closest_wall_row = max(walls_above_row)
            if self.row == closest_wall_row + 1: # next to wall
                return False
            boxes_to_move = get_boxes_to_move(self.row, self.col, closest_wall_row)
            if len(boxes_to_move) == closest_wall_row - self.row:
                return False
            # move boxes before the robot
            for i, bm in enumerate(boxes_to_move):
                 boxes_to_move[i] = bm.move(direction)
               #  print(f"{boxes_to_move[i]} doboz mozgult")
            return True
    def move(self, direction):
        if direction == "^" and self.can_move(direction):
            self.row -= 1
        elif direction == "v" and self.can_move(direction):
            self.row += 1
        elif direction == "<" and self.can_move(direction):
            self.row -= 1
        elif direction == ">" and self.can_move(direction):
            self.row += 1

def read_input(filename):
    robot_map = list()
    with open(filename) as file:
        line = file.readline().strip("\n")
        while line:
            robot_map.append(line)
            line = file.readline().strip("\n")
        commands = file.readline().strip("\n")
    return robot_map, commands

def print_map(robot_map):
    for line in robot_map:
        print(line)

def find_robot_pos(robot_map):
    for row_idx, row in enumerate(robot_map):
        col_idx = str(row).find("@")
        if col_idx != -1:
            return row_idx, col_idx
    return None

def main():
    robot_map, commands = read_input("input/day15-test-input.txt")
    print_map(robot_map)

    row, col = find_robot_pos(robot_map)

    robot = Robot(row, col)
    for command in commands:
        print(robot)
        robot.move(command)
        for box in box_list:
            print(box)

if __name__ == "__main__":
    main()

