from functools import partial
from .multiagentenv import MultiAgentEnv
from .smarts_env import SMARTSEnv


def env_fn(env, **kwargs) -> MultiAgentEnv:
    return env(**kwargs)

REGISTRY = {}
REGISTRY["smarts"] = partial(env_fn, env=SMARTSEnv)


