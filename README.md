# QMIX_SMART_for_test
Some unexpected bugs will show up
## Run SMARTS env
```
python main.py --config=qmix --env-config=smarts
```
## Some Bugs
```
[DEBUG 16:15:03] tensorflow Falling back to TensorFlow client; we recommended you install the Cloud TPU client directly with pip install cloud-tpu-client.
2023-04-13 16:15:03.882226: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
[DEBUG 16:15:03] h5py._conv Creating converter from 7 to 5
[DEBUG 16:15:03] h5py._conv Creating converter from 5 to 7
[DEBUG 16:15:03] h5py._conv Creating converter from 7 to 5
[DEBUG 16:15:03] h5py._conv Creating converter from 5 to 7
[DEBUG 16:15:04] trimesh falling back to MD5 hashing: pip install xxhash for 30x faster cache checks
[DEBUG 16:15:04] AgentManager Tearing down AgentManager
[DEBUG 16:15:04] SumoTrafficSimulation Tearing down SUMO traffic sim SumoTrafficSim(
_scenario=None,
_time_resolution=0.1,
_headless=True,
_cumulative_sim_seconds=0,
_non_sumo_vehicle_ids=set(),
_sumo_vehicle_ids=set(),
_is_setup=False,
_last_trigger_time=-1000000,
_num_dynamic_ids_used=0,
_traci_conn=None
)
[DEBUG 16:15:04] SumoTrafficSimulation Nothing to teardown
[DEBUG 16:15:04] SumoTrafficSimulation Setting up SumoTrafficSim SumoTrafficSim(
_scenario=None,
_time_resolution=0.1,
_headless=True,
_cumulative_sim_seconds=0,
_non_sumo_vehicle_ids=set(),
_sumo_vehicle_ids=set(),
_is_setup=False,
_last_trigger_time=-1000000,
_num_dynamic_ids_used=0,
_traci_conn=None
)
[DEBUG 16:15:04] root Starting sumo process:
['/home/xxx/anaconda3/envs/py38_smart/lib/python3.8/site-packages/sumo/bin/sumo', '--remote-port=44365', '--num-clients=1', '--net-file=/home/xxx/smarts/scenarios/sumo/loop/map.net.xml', '--quit-on-end', '--log=/home/xxx/.smarts/_sumo_run_logs/sumo-e98454fe', '--error-log=/home/xxx/.smarts/_sumo_run_logs/sumo-e98454fe', '--no-step-log', '--no-warnings=1', '--seed=1127092023', '--time-to-teleport=-1', '--collision.check-junctions=true', '--collision.action=none', '--lanechange.duration=3.0', '--step-length=0.100000', '--default.action-step-length=0.100000', '--begin=0', '--end=31536000', '--additional-files=/home/xxx/smarts/scenarios/sumo/loop/rerouter.add.xml', '--start', '--route-files=/home/xxx/smarts/scenarios/sumo/loop/build/traffic/basic.rou.xml']
[DEBUG 16:15:05] SumoTrafficSimulation Finished starting sumo process
[DEBUG 16:15:05] VehicleIndex Tearing down vehicle ids: set()
[DEBUG 16:15:05] SumoTrafficSimulation SUMO vehicle car-flow-route-445633931_0_random-445633932_0_max--8872063773308225556---2130553413876864870--endless-2-0.0 entered simulation
[DEBUG 16:15:05] SumoTrafficSimulation SUMO vehicle car-flow-route-445633931_0_random-445633932_0_max--8872063773308225556---5481682861420388098--endless-6-0.0 entered simulation
[DEBUG 16:15:05] SumoTrafficSimulation SUMO vehicle car-flow-route-445633931_1_random-445633932_0_max-2891830898934547453---3925330266029679230--endless-16-0.0 entered simulation
[DEBUG 16:15:05] SumoTrafficSimulation SUMO vehicle car-flow-route-445633931_1_random-445633932_0_max-2891830898934547453---4408281014321500977--endless-22-0.0 entered simulation
[DEBUG 16:15:05] SumoTrafficSimulation SUMO vehicle car-flow-route-445633931_2_random-445633932_0_max-6765479504201222794---2130553413876864870--endless-0-0.0 entered simulation
[DEBUG 16:15:05] SumoTrafficSimulation SUMO vehicle car-flow-route-445633931_2_random-445633932_0_max-6765479504201222794---2130553413876864870--endless-20-0.0 entered simulation
[DEBUG 16:15:05] SumoTrafficSimulation SUMO vehicle car-flow-route-445633932_0_random-445633931_0_max-879489216878698016---2130553413876864870--endless-5-0.0 entered simulation
[DEBUG 16:15:05] SumoTrafficSimulation SUMO vehicle car-flow-route-445633932_0_random-445633931_1_max--5226483183952079403---2130553413876864870--endless-13-0.0 entered simulation
[DEBUG 16:15:05] SumoTrafficSimulation SUMO vehicle car-flow-route-445633932_0_random-445633931_1_max--5226483183952079403--2338792407115996549--endless-23-0.0 entered simulation
[DEBUG 16:15:05] SumoTrafficSimulation SUMO vehicle car-flow-route-445633932_0_random-445633931_2_max-3796886287426974533---3925330266029679230--endless-11-0.0 entered simulation
[DEBUG 16:15:05] SumoTrafficSimulation SUMO vehicle car-flow-route-445633932_0_random-445633931_2_max-3796886287426974533---4408281014321500977--endless-21-0.0 entered simulation
[DEBUG 16:15:05] SumoTrafficSimulation SUMO vehicle car-flow-route-445633932_1_random-445633931_0_max-2182261526775445995---3925330266029679230--endless-9-0.0 entered simulation
[DEBUG 16:15:05] SumoTrafficSimulation SUMO vehicle car-flow-route-445633932_2_random-445633931_0_max--7779908317845345820---3925330266029679230--endless-17-0.0 entered simulation
[DEBUG 16:15:05] VehicleIndex Tearing down vehicle ids: set()
[INFO 16:15:05] Vehicle replacing existing trip_meter_sensor on vehicle Agent_2
[INFO 16:15:05] Vehicle replacing existing driven_path_sensor on vehicle Agent_2
[INFO 16:15:05] Vehicle replacing existing accelerometer_sensor on vehicle Agent_2
[INFO 16:15:05] Vehicle replacing existing lane_position_sensor on vehicle Agent_2
[INFO 16:15:05] Vehicle replacing existing waypoints_sensor on vehicle Agent_2
[INFO 16:15:05] Vehicle replacing existing via_sensor on vehicle Agent_2
[INFO 16:15:05] Vehicle replacing existing trip_meter_sensor on vehicle car-flow-route-445633932_0_random-445633931_0_max-879489216878698016---2130553413876864870--endless-5-0.0
[INFO 16:15:05] Vehicle replacing existing driven_path_sensor on vehicle car-flow-route-445633932_0_random-445633931_0_max-879489216878698016---2130553413876864870--endless-5-0.0
[INFO 16:15:05] Vehicle replacing existing accelerometer_sensor on vehicle car-flow-route-445633932_0_random-445633931_0_max-879489216878698016---2130553413876864870--endless-5-0.0
[INFO 16:15:05] Vehicle replacing existing lane_position_sensor on vehicle car-flow-route-445633932_0_random-445633931_0_max-879489216878698016---2130553413876864870--endless-5-0.0
[INFO 16:15:05] Vehicle replacing existing waypoints_sensor on vehicle car-flow-route-445633932_0_random-445633931_0_max-879489216878698016---2130553413876864870--endless-5-0.0
[INFO 16:15:05] Vehicle replacing existing via_sensor on vehicle car-flow-route-445633932_0_random-445633931_0_max-879489216878698016---2130553413876864870--endless-5-0.0
[DEBUG 16:15:05] VehicleIndex Switching control of Agent_3 to car-flow-route-445633932_0_random-445633931_0_max-879489216878698016---2130553413876864870--endless-5-0.0
[DEBUG 16:15:05] VehicleIndex Tearing down vehicle ids: ['car-flow-route-445633932_0_random-445633931_0_max-879489216878698016---2130553413876864870--endless-5-0.0']
[INFO 16:15:05] Vehicle replacing existing trip_meter_sensor on vehicle car-flow-route-445633932_0_random-445633931_0_max-879489216878698016---2130553413876864870--endless-5-0.0
[INFO 16:15:05] Vehicle replacing existing driven_path_sensor on vehicle car-flow-route-445633932_0_random-445633931_0_max-879489216878698016---2130553413876864870--endless-5-0.0
[INFO 16:15:05] Vehicle replacing existing accelerometer_sensor on vehicle car-flow-route-445633932_0_random-445633931_0_max-879489216878698016---2130553413876864870--endless-5-0.0
[INFO 16:15:05] Vehicle replacing existing lane_position_sensor on vehicle car-flow-route-445633932_0_random-445633931_0_max-879489216878698016---2130553413876864870--endless-5-0.0
[INFO 16:15:05] Vehicle replacing existing waypoints_sensor on vehicle car-flow-route-445633932_0_random-445633931_0_max-879489216878698016---2130553413876864870--endless-5-0.0
[INFO 16:15:05] Vehicle replacing existing via_sensor on vehicle car-flow-route-445633932_0_random-445633931_0_max-879489216878698016---2130553413876864870--endless-5-0.0
[INFO 16:15:05] Vehicle replacing existing trip_meter_sensor on vehicle Agent_1
[INFO 16:15:05] Vehicle replacing existing driven_path_sensor on vehicle Agent_1
[INFO 16:15:05] Vehicle replacing existing accelerometer_sensor on vehicle Agent_1
[INFO 16:15:05] Vehicle replacing existing lane_position_sensor on vehicle Agent_1
[INFO 16:15:05] Vehicle replacing existing waypoints_sensor on vehicle Agent_1
[INFO 16:15:05] Vehicle replacing existing via_sensor on vehicle Agent_1
[DEBUG 16:15:05] root Agent Agent_2 has raised done with Events(collisions=[], off_road=False, off_route=False, on_shoulder=False, wrong_way=False, not_moving=False, reached_goal=False, reached_max_episode_steps=False, agents_alive_done=False)
[DEBUG 16:15:05] root Agent Agent_3 has raised done with Events(collisions=[], off_road=False, off_route=False, on_shoulder=False, wrong_way=False, not_moving=False, reached_goal=False, reached_max_episode_steps=False, agents_alive_done=False)
[DEBUG 16:15:05] root Agent Agent_1 has raised done with Events(collisions=[], off_road=False, off_route=False, on_shoulder=False, wrong_way=False, not_moving=False, reached_goal=False, reached_max_episode_steps=False, agents_alive_done=False)
[DEBUG 16:15:05] VehicleIndex Tearing down vehicle ids: set()
[DEBUG 16:15:05] pymarl Stopping Heartbeat
[ERROR 16:15:05] pymarl Failed after 0:00:02!
Traceback (most recent calls WITHOUT Sacred internals):
File "main.py", line 35, in my_main
run(_run, config, _log)
File "/home/xxx/QMIX_SMART/run.py", line 48, in run
run_sequential(args=args, logger=logger)
File "/home/xxx/QMIX_SMART/run.py", line 82, in run_sequential
env_info = runner.get_env_info()
File "/home/xxx/QMIX_SMART/runners/episode_runner.py", line 37, in get_env_info
return self.env.get_env_info()
File "/home/xxx/QMIX_SMART/envs/multiagentenv.py", line 55, in get_env_info
env_info = {"state_shape": self.get_state_size(),
File "/home/xxx/QMIX_SMART/envs/smarts_env.py", line 161, in get_state_size
return self.get_obs_size() * self.n_agents
File "/home/xxx/QMIX_SMART/envs/smarts_env.py", line 157, in get_obs_size
return len(self.get_obs_agent(0))
File "/home/xxx/QMIX_SMART/envs/smarts_env.py", line 153, in get_obs_agent
return self.get_obs()[agent_id]
File "/home/xxx/QMIX_SMART/envs/smarts_env.py", line 137, in get_obs
print(self.current_observations['Agent_0'])
KeyError: 'Agent_0'
```
