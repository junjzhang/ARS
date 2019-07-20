#This project is to test the perfomance of ARS on breakout-ram-V4

# Augmented Random Search (ARS)

ARS is a random search method for training linear policies for continuous control problems, based on the paper ["Simple random search provides a competitive approach to reinforcement learning."](https://arxiv.org/abs/1803.07055) 

## Prerequisites for running ARS

Our ARS implementation relies on Python 3, OpenAI Gym version 0.9.3, mujoco-py 0.5.7, MuJoCo Pro version 1.31, and the Ray library for parallel computing.  

To install OpenAI Gym and MuJoCo dependencies follow the instructions here:
https://github.com/openai/gym

To install Ray execute:
``` 
pip install ray
```
For more information on Ray see http://ray.readthedocs.io/en/latest/. 

## Running ARS

First start Ray by executing a command of the following form:

```
ray start --head --redis-port=6379 --num-cpus=15
```
This command starts multiple Python processes on one machine for parallel computations with Ray. 
Set "num_cous=X" for parallelizing ARS across X CPUs.
For parallelzing ARS on a cluster follow the instructions here: http://ray.readthedocs.io/en/latest/using-ray-on-a-large-cluster.html.

We recommend using single threaded linear algebra computations by setting: 
```
export MKL_NUM_THREADS=1
```

To train a policy for breakout, execute the following command: 

```
python code/ars.py
```

