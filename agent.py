import random

class QLearningAgent:
    def __init__(self):
        self.q_table = {}
        self.actions = [0,1,2,3]
        self.lr = 0.1
        self.gamma = 0.9
        self.epsilon = 0.3

    def get_q_values(self, state):
        if state not in self.q_table:
            self.q_table[state] = [0,0,0,0]
        return self.q_table[state]

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        return self.get_q_values(state).index(max(self.get_q_values(state)))

    def learn(self, state, action, reward, next_state):
        q_values = self.get_q_values(state)
        next_q = self.get_q_values(next_state)
        q_values[action] += self.lr*(reward + self.gamma*max(next_q) - q_values[action])
