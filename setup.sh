#!bin/bash

conda create --name mdp_env 
conda activate mdp_env

conda install pip # also installs latest python

pip install -r requirements.txt