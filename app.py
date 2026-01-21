from flask import Flask, render_template, jsonify, request
from agent import QLearningAgent
from environment import GridWorld

app = Flask(__name__)

grid_size = 6
env = GridWorld(grid_size)
agent = QLearningAgent()

state = env.reset()
episode_rewards = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/step')
def step():
    global state

    action = agent.choose_action(state)
    next_state, reward, done = env.step(action)
    agent.learn(state, action, reward, next_state)
    state = next_state

    episode_rewards.append(reward)

    if done:
        state = env.reset()

    return jsonify({
        "agent": env.agent_pos,
        "foods": env.foods,
        "walls": env.walls,
        "score": env.score,
        "rewards": episode_rewards[-50:]
    })

if __name__ == "__main__":
    app.run(debug=True)
