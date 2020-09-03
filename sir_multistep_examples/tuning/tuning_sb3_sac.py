
import os
import sys
sys.path.append(os.path.realpath('../..'))

import gym
import sir_multistep_gym
import numpy as np

from stable_baselines3.sac import MlpPolicy
from stable_baselines3 import SAC
from tuning_utils_sb3 import *

def create_env(n_envs=0, eval_env=None):
    env = gym.make("sir-v0", intervention='fc')
    return env

def create_model(*_args, **kwargs):
    """
    Helper to create a model with different hyperparameters
    """
    return SAC(env=create_env(), policy=MlpPolicy, verbose=1, **kwargs)

hyperparam_optimization("sac", create_model, create_env, n_trials=30,
                                             n_timesteps=int(2e5),
                                             n_jobs=1, seed=0, log_interval=int(1e3), 
                                             sampler_method='tpe', pruner_method='median',
                                             verbose=1)
