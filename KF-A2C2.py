#import gymnasium as gym
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3 import A2C, PPO
import os

#num_cpu = 512

models_dir = "./models/KF/A2C2"
logdir = "./logs/KF"

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(logdir):
    os.makedirs(logdir)

env = env = make_atari_env("KungFuMasterNoFrameskip-v4", seed=42)
env.reset()

model = A2C("CnnPolicy", env, verbose=1, tensorboard_log = logdir)


#save the model after every 100k step
time_steps = 100000
for i in range(1, 30):
    model.learn(total_timesteps=time_steps, reset_num_timesteps = False, tb_log_name="A2C2")
    if (i % 5 == 0) or (i == 1) or (i==2):  # every 50k save
        model.save(f"{models_dir}/{time_steps*i}")


# episodes = 10
# for ep in range(episodes):
#     state = env.reset()
#     done = False
#     while not done:
#         env.render()
#         action, _ = model.predict(state)
#         state, reward, done, _, _ = env.step(action)


env.close()