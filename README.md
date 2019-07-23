# group2-machine-learning

# Introduction

## Project phases
- Making the repository and the required materials.
- Build docker containers for the MNIST analyses
- Use workflow tools + cloud/HPC computing to run MNIST analyses
- Repeat steps above for fashion MNIST and humback whale classification if time.

## Instructions

#### Initiate a virtual machine through a cloud server
  1. Log in to [Jetstream](https://use.jetstream-cloud.org/application/dashboard) and click "Start a New Instance."
  2. Select the _Ubuntu 18.04 Devel and Docker_ instance and press launch.
  3. Select an _m1.medium_ instance in instance size, and then click "Launch Instance."
  4. Once the instance is "Active," go into the shell either through the Web Shell or via ssh.
  
### Run the docker image
  - Pull the docker image with the command below. You can use ```sh docker images ``` to check if you successfully pulled the image. 
  ``` docker pull username/machinelearning ```
  
  - Run the image with the command below. 
  ```docker run -it username/machinelearning sh ```
  
  The default is to run a neural net classifier on all of the MNIST, fashion MNIST, and Humpback Whale Tail datasets. If you would like to specify a dataset, you can add it with the ```-e``` tag (see example below). Options are mnist, fashion, whale. 
    ```docker run -e dataset=mnist, -it username/machinelearning sh ```
3. The neural network builder and classifier has launched! When it is finished, you will see an output file with a text and pdf summary of the results. Compare your results to the example output below


## Further exploration

### MNIST classifier with mlp neural network ###
To work with the neural network model, press the button below to launch a jupyter notebook (Note: this notebook runs on Binder servers).
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cyber-carpentry/group2-machine-learning/master)

## Group 2 Useful Links

[HackMD Notes](https://hackmd.io/@stephprince/r1BFBO7MH)

[Planning Notes](https://hackmd.io/8IlRqMagSr-wxBMXtmtgnA?both#Planning)
