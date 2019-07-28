#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import configparser
import time
import logz
import ray
from ars import *

config = configparser.ConfigParser()
config.read('config.ini')
n_dir=config['agent']['n_directions']
step_size=config['agent']['step_size']
rollout_length=config['agent']['rollout_length']
n_iter=config['agent']['n_iter']
delta_std=config['agent']['delta_std']
start_time = time.time()

local_ip = socket.gethostbyname(socket.gethostname())
    
params = {'env_name': 'Breakout-ram-v0',
        'n_iter': n_iter,
        'n_directions': n_dir,
        'deltas_used': n_dir,
        'step_size': step_size,
        'delta_std': delta_std,
        'n_workers': 16,
        'rollout_length': rollout_length,
        'shift': 0,
        'seed': 237,
        'policy_type': 'linear',
        'dir_path': 'data',
        'filter': 'MeanStdFilter'}

logz.configure_output_dir(params['dir_path'])
ray.init(redis_address= 'localhost:6379')
reward = run_ars(params)
ray.shutdown()

with open('time_elapsed', 'w') as f:
  f.write('%d' % int((time.time() - start_time)/60))