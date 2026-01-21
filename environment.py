import random

class GridWorld:
    def __init__(self, size=6):
        self.size = size
        self.reset()

    def reset(self):
        self.agent_pos = [0, 0]

        # Walls (obstacles)
        self.walls = [[2,2], [3,2], [1,4]]

        # Multiple food items
        self.foods = []
        for _ in range(3):
            self.foods.append([
                random.randint(0, self.size-1),
                random.randint(0, self.size-1)
            ])

        self.score = 0
        return self.get_state()

    def get_state(self):
        return (
            self.agent_pos[0],
            self.agent_pos[1],
            tuple(map(tuple, self.foods))
        )

    def step(self, action):
        new_pos = self.agent_pos.copy()

        if action == 0: new_pos[0] -= 1
        if action == 1: new_pos[0] += 1
        if action == 2: new_pos[1] -= 1
        if action == 3: new_pos[1] += 1

        # Boundary + wall check
        if (0 <= new_pos[0] < self.size and
            0 <= new_pos[1] < self.size and
            new_pos not in self.walls):
            self.agent_pos = new_pos

        reward = -1
        done = False

        for food in self.foods:
            if self.agent_pos == food:
                reward = 10
                self.score += 10
                self.foods.remove(food)
                break

        if len(self.foods) == 0:
            done = True

        return self.get_state(), reward, done
