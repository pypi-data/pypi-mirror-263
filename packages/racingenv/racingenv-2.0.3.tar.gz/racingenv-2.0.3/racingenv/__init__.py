from gymnasium.envs.registration import register
from collision.collision import CollisionHandler

import os

resource_dir = os.path.dirname(os.path.realpath(__file__)) + '/'

register(
     id="Racing-v2",
     entry_point="racingenv.env:RacingEnv",
     max_episode_steps=7200
)

register(
     id="Racing-features-v2",
     entry_point="racingenv.env:RacingEnv",
     max_episode_steps=7200,
     kwargs={
          "obs_type": "features",
          "action_space": "continuous"
     }
)

register(
     id="Racing-pixels-v2",
     entry_point="racingenv.env:RacingEnv",
     max_episode_steps=7200,
     kwargs={
          "obs_type": "pixels",
          "action_space": "continuous",
          "normalize_images": False
     }
)

register(
     id="Racing-normalized-v2",
     entry_point="racingenv.env:RacingEnv",
     max_episode_steps=7200,
     kwargs={
          "obs_type": "pixels",
          "action_space": "continuous",
          "normalize_images": True
     }
)

register(
     id="Racing-features-discrete-v2",
     entry_point="racingenv.env:RacingEnv",
     max_episode_steps=7200,
     kwargs={
          "obs_type": "features",
          "action_space": "discrete"
     }
)

register(
     id="Racing-pixels-discrete-v2",
     entry_point="racingenv.env:RacingEnv",
     max_episode_steps=7200,
     kwargs={
          "obs_type": "pixels",
          "action_space": "discrete",
          "normalize_images": False
     }
)

register(
     id="Racing-normalized-discrete-v2",
     entry_point="racingenv.env:RacingEnv",
     max_episode_steps=7200,
     kwargs={
          "obs_type": "pixels",
          "action_space": "discrete",
          "normalize_images": True
     }
)
