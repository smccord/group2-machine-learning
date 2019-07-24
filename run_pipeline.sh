#!/bin/sh

cd cyber-carpentry-group2-machine-learning*

python run_main.py my_input_file --int_param $dataset

echo "Running machine learning pipeline for $dataset"
