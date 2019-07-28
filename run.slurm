#!/bin/bash

#SBATCH --job-name=hostname
#SBATCH --partition=cpu
#SBATCH -n 1
#SBATCH --mail-type=end
#SBATCH --mail-user=...
#SBATCH --output=%j.out
#SBATCH --error=%j.err
#SBATCH --time=00:00:10

export alias xml='/usr/bin/xmlstarlet'
