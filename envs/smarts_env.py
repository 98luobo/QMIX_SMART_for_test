import time

import gym
from envs.multiagentenv import MultiAgentEnv
from utils.dict2namedtuple import convert

import os
import sys

from smarts.core.agent_interface import AgentInterface, AgentType

import numpy as np
import gymnasium  # for hiway-v1

from smarts.env.utils.action_conversion import ActionOptions, ActionSpacesFormatter
from smarts.env.utils.observation_conversion import (
    ObservationOptions,
    ObservationSpacesFormatter,
)


def clean_dict_values(d):
    res = []
    for k, v in d.items():
        if isinstance(v, dict):
            res.extend(clean_dict_values(v))
        elif isinstance(v, np.ndarray):
            res.extend(v.flatten().tolist())
        else:
            res.append(float(v))
    return res


class ResetError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"ResetError: {self.message}"


class SMARTSEnv(MultiAgentEnv):
    def __init__(self, **kwargs):
        self.episode_limit = kwargs['episode_limit']
        self.n_agents = kwargs['agent_num']
        self.seed = kwargs['seed']
        self.agent_ids = ["Agent_%i" % i for i in range(self.n_agents)]
        self.n_actions = 4
        self.scenarios = [kwargs['scenarios']]

        self.headless = kwargs['headless']
        self.visdom = kwargs['visdom']
        self.agent_interface = {
            agent_id: AgentInterface.from_type(
                AgentType.Laner,
                max_episode_steps=self.episode_limit
            )
            for agent_id in self.agent_ids

        }

        self.base_env = gymnasium.make(
            "smarts.env:hiway-v1",
            scenarios=self.scenarios,
            agent_interfaces=self.agent_interface,
            headless=self.headless,
            visdom=self.visdom,
            observation_options=ObservationOptions.multi_agent,
            action_options=ActionOptions.multi_agent,
            seed=self.seed
        )

        self.current_observations, info = self.base_env.reset()
        vehicle_ids = self.base_env.agent_ids
        print("vehicle list:", vehicle_ids)
        # sys.exit()
        pass

    def reset(self):
        try:
            self.current_observations, info = self.base_env.reset()
            cur_result = set(self.agent_ids) - set(self.current_observations.keys())
            if cur_result != set():
                raise ResetError("A reset error occurred and the number of agents "
                                 "after the reset is less than the defined agents.")
        except:
            self.base_env.close()
            self.base_env = gymnasium.make(
                "smarts.env:hiway-v1",
                scenarios=self.scenarios,
                agent_interfaces=self.agent_interface,
                headless=self.headless,
                visdom=self.visdom,
                observation_options=ObservationOptions.multi_agent,
                action_options=ActionOptions.multi_agent,
                seed=self.seed,
                fixed_timestep_sec=0.01
            )
            reset_cout = 0
            while reset_cout < 3:
                self.current_observations, info = self.base_env.reset()
                cur_result = set(self.agent_ids) - set(self.current_observations.keys())
                if cur_result == set():
                    break
                reset_cout += 1
            if reset_cout == 3:
                raise ResetError("Tried to reset it 3 times and still had a number problem")
        vehicle_ids = self.base_env.agent_ids
        # print("2.当前智能体ID列表：", vehicle_ids)
        # sys.exit()

        return self.get_obs(), self.get_state()
        pass

    def close(self):
        self.base_env.close()
        pass

    def step(self, actions):
        actions = dict(zip(self.agent_ids, actions.tolist()))
        self.current_observations, rewards, dones, _, _ = self.base_env.step(actions)
        r_n = []
        for agent_id in self.agent_ids:
            r_n.append(rewards.get(agent_id, 0.))
        return sum(r_n), dones['__all__'], {}

        pass

    def get_obs(self):
        obs_n = []
        for agent_id in self.agent_ids:
            if agent_id in self.current_observations.keys():
                ego_state_dict = self.current_observations[agent_id]['ego_vehicle_state']
                ego_state_dict.pop('lane_id', None)
                ego_state_dict.pop('box', None)
                ego_state = clean_dict_values(ego_state_dict)
            else:
                ego_state = np.zeros(29)
            obs_n.append(ego_state)
        return obs_n
        pass

    def get_obs_agent(self, agent_id):
        return self.get_obs()[agent_id]
        pass

    def get_obs_size(self):
        return len(self.get_obs_agent(0))
        pass

    def get_state_size(self):
        return self.get_obs_size() * self.n_agents
        pass

    def get_state(self):
        return np.asarray(self.get_obs()).flatten()
        pass

    def get_avail_actions(self):
        avail_actions = []
        for agent_id in range(self.n_agents):
            avail_agent = self.get_avail_agent_actions(agent_id)
            avail_actions.append(avail_agent)
        return avail_actions
        pass

    def get_avail_agent_actions(self, agent_id):
        return np.ones(self.n_actions)
        pass

    def get_total_actions(self):
        return self.n_actions
        pass

    def get_stats(self):
        return None

    def render(self):
        raise NotImplementedError

    def close(self):
        pass

    def seed(self):
        raise NotImplementedError

    pass
