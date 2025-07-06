# import ale_py
# import gymnasium as gym
# # from stable_baselines3 import DQN
#
# # gym.register_envs(ale_py)
# env = gym.make("Pong-v4", render_mode="human")   # PongNoFrameskip-v4, ALE/Breakout-v5, ALE/Pong-v5
#
# # model = DQN("MlpPolicy", env, verbose=1, buffer_size=100000)
# # model.learn(total_timesteps=10000, log_interval=4)
# # model.save("dqn_pong_v4")
# #
# # del model   # remove to demonstrate saving and loading
# # model = DQN.load("dqn_pong_v4")
#
# obs, info = env.reset(seed=42)
# for _ in range(100):
#     # action, _states = model.predict(obs, deterministic=True)
#     action = env.action_space.sample()
#     obs, reward, terminated, truncated, info = env.step(action)
#     if terminated or truncated:
#         obs, info = env.reset()
# env.close()


import gymnasium
import ale_py

gymnasium.register_envs(ale_py)

env = gymnasium.make("ALE/Pong-v5", render_mode="human")
env.reset()
for _ in range(100):
    action = env.action_space.sample()

    obs, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        obs, info = env.reset()

env.close()
