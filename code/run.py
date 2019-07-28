import math
import logz
import ray
import socket
import numpy as np
from ars import *

local_ip = socket.gethostbyname(socket.gethostname())
params = {'env_name': 'Breakout-ram-v4',
        'n_iter': 0,
        'n_directions': 0,
        'deltas_used': 0,
        'step_size': 0,
        'delta_std': 0,
        'n_workers': 16,
        'rollout_length': 0,
        'shift': 0,
        'seed': 237,
        'policy_type': 'linear',
        'dir_path': 'data',
        'filter': 'MeanStdFilter'}
                
logz.configure_output_dir(params['dir_path'])
ray.init(redis_address= 'localhost:6379')

reward_array = np.array([])
best_reward = 0
beast_params = params

for n_iter in range(3):
    for n_directions in range(3):
        for delta in range(10):
            for step_size in range(12):
                for rlength in range(3):
                    print("ITER: "+str(n_iter)+","+str(n_directions)+","+str(delta)+","+str(step_size)+","+str(rlength))
                    params['delta_std'] = 0.04*delta+0.02
                    params['step_size'] = math.pow(2,step_size)*0.0001
                    params['n_directions'] = int(math.pow(2,n_directions)*2)
                    params['rollout_length'] = int(math.pow(2,rlength)*100)
                    params['n_iter'] = int(math.pow(2,n_iter)*25)
                    logz.save_params(params,"ITER: "+str(n_iter)+","+str(n_directions)+","+str(delta)+","+str(step_size)+","+str(rlength))
                    reward = run_ars(params)
                    #record
                    reward_array = np.append(reward_array,reward)
                    logz.save_data(reward,"ITER: "+str(n_iter)+","+str(n_directions)+","+str(delta)+","+str(step_size)+","+str(rlength))
                    #check best
                    if best_reward<reward:
                        best_reward = reward
                        best_params = params
ray.shutdown()
logz.save_best(best_params,best_reward)
logz.data_close()