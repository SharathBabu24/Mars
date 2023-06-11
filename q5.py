class RobotWorkspace:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.workspace = [[1] * width for _ in range(height)]  # Initialize workspace with free spaces
        self.robot_position = (0, 0)  # Initial robot position

    def insert_obstacle(self, x, y):
        self.workspace[y][x] = 0

    def move_robot(self, direction):
        x, y = self.robot_position
        if direction == 'up':
            if y > 0 and self.workspace[y - 1][x] != 0:
                self.robot_position = (x, y - 1)
        elif direction == 'down':
            if y < self.height - 1 and self.workspace[y + 1][x] != 0:
                self.robot_position = (x, y + 1)
        elif direction == 'left':
            if x > 0 and self.workspace[y][x - 1] != 0:
                self.robot_position = (x - 1, y)
        elif direction == 'right':
            if x < self.width - 1 and self.workspace[y][x + 1] != 0:
                self.robot_position = (x + 1, y)

    def display_workspace(self):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == self.robot_position:
                    print('R', end=' ')  # Represent robot with 'R'
                elif self.workspace[y][x] == 0:
                    print('0', end=' ')  # Represent obstacle with 'X'
                else:
                    print('1', end=' ')  # Represent free space with '1'
            print()

# Create a workspace of size 5x5
workspace = RobotWorkspace(5, 5)

# Insert obstacles at specific coordinates
workspace.insert_obstacle(2, 1)
workspace.insert_obstacle(3, 2)
workspace.insert_obstacle(1, 3)
workspace.insert_obstacle(4, 4)

# Display the initial workspace
print("Initial Workspace:")
workspace.display_workspace()

# Move the robot and display the updated workspace
workspace.move_robot('right')
workspace.move_robot('down')
workspace.move_robot('right')
print("\nUpdated Workspace:")
workspace.display_workspace()


