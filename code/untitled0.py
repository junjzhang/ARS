#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 20:16:28 2019

@author: bz
"""
import gym
import numpy as np
env = gym.make('Breakout-ram-v0')
observation = env.reset()
for ii in range 1000