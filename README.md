# group2-machine-learning

# Introduction

## Project phases
- Making the repository and the required materials.
- Build docker containers for the MNIST analyses
- Use workflow tools + cloud/HPC computing to run MNIST analyses
- Repeat steps above for fashion MNIST and humback whale classification if time.

## Instructions

1. Initiate a virtual machine through a cloud server
  - Log in to [Jetstream](https://use.jetstream-cloud.org/application/dashboard) and click "Start a New Instance."
  - Select the Ubuntu 18.04 Devel and Docker instance and press launch.
  - Select an m1.medium instance in instance size, and then click "Launch Instance."
  - Once the instance is "Active," go into the shell either through the Web Shell or via ssh.
2. Get the docker image from DockerHub
  - Pull the docker image with the command below. You can use ```sh docker images ``` to check if you successfully pulled the image. 
  ``` docker pull username/machinelearning ```
  
  - Run the image with the command below. 
  ```docker run -it username/machinelearning sh ```
  
  The default is to run a neural net classifier on all of the MNIST, fashion MNIST, and Humpback Whale Tail datasets. If you would like to specify a dataset, you can add it with the ```-e``` tag (see example below). Options are mnist, fashion, whale. 
    ```docker run -e dataset=mnist, -it username/machinelearning sh ```
    
3. ...further instructions to follow 


### Launching MNIST classifier with mlp neural network ###

This will launch a jupyter notebook in a docker container running on the BinderHub servers.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cyber-carpentry/group2-machine-learning/master)

## Group 2 Useful Links

[HackMD Notes](https://hackmd.io/@stephprince/r1BFBO7MH)

[Planning Notes](https://hackmd.io/8IlRqMagSr-wxBMXtmtgnA?both#Planning)
