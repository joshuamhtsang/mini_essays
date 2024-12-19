import numpy as np

class Maze:
    def __init__(self, x_size, y_size, maze_map, maze_props):

        self.state_values = np.zeros((x_size, y_size))
        print(self.state_values)

        self.maze_map = maze_map
        self.maze_props = maze_props
    

    def actions_and_rewards(self, state, action):
        if state not in self.maze_map:
            return "Invalid state"
        else:
            action_mapping = {
                "up": 0,
                "right": 1,
                "down": 2,
                "left": 3
            }
            return self.maze_map[state][action_mapping[action]]
    
    def dice_roll(self, sides):
        thresholds = []
        interval = 1.0/sides
        for i in range(0, sides+1):
            thresholds.append(interval*(i))
        #print(thresholds)
        rand_num = np.random.random()
        result = 0
        for i in range(0, sides):
            if rand_num > thresholds[i] and rand_num < thresholds[i+1]:
                result = i + 1
        return result

    def random_action(self):
        dice_result = self.dice_roll(4)
        dice_to_action_mapping = {
            1: "up",
            2: "right",
            3: "down",
            4: "left"
        }
        return dice_to_action_mapping[dice_result]

    def next_state(self, current_state, action):
        if action == "up":
            next_state = (current_state[0], current_state[1]+1)
        elif action == "right":
            next_state = (current_state[0]+1, current_state[1])
        elif action == "down":
            next_state = (current_state[0], current_state[1]-1)
        else:
            next_state = (current_state[0]-1, current_state[1])
        return next_state

    def generate_random_path(self):
        gain = 0
        state_history = []
        start_state = self.maze_props["start_state"]

        current_state = start_state
        while current_state != self.maze_props["end_state"]:
            state_history.append(current_state)
            
            action = self.random_action()
            if self.actions_and_rewards(current_state, action) == "Invalid state":
                break
            gain += self.actions_and_rewards(current_state, action)
            next_state = self.next_state(current_state, action)
            current_state = next_state

            if current_state == self.maze_props["end_state"]:
                state_history.append(current_state)
                #print("Found successful path with gain " + str(gain))
                if gain > -50:
                    print("Found good path with gain " + str(gain))
                    print("state_history:", state_history)
                break

            


if __name__ == '__main__':
    
    """
    Reward for actions (up, right, down, left)
    1. Free travel => -1 score
    2. Wall => -100 score
    3. Off map => -1000 score
    """
    maze_map_1 = {
        (0, 0): (-100, -1, -1000, -1000),
        (1, 0): (-1, -100, -1000, -1),
        (2, 0): (-1, -1000, -1000, -100),
        (0, 1): (-1, -1, -100, -1000),
        (1, 1): (-1, -100, -1, -1),
        (2, 1): (-1, -1000, -1, -100),
        (0, 2): (-1000, -100, -1, -1000),
        (1, 2): (-1000, -1, -1, -100),
        (2, 2): (-1000, -1000, -1, -1)
    }
    print(maze_map_1[(1, 2)])

    maze_props_1 = {
        "start_state": (0, 0),
        "end_state": (2, 0)
    }

    maze_1 = Maze(3, 3, maze_map_1, maze_props_1)

    for i in range(0, 100000):
        #print("Random path: ", i)
        maze_1.generate_random_path()
