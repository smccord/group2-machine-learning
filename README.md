# group2-machine-learning

# Introduction

## Project phases
- Making the repository and the required materials.
- Build docker containers for the MNIST analyses
- Use workflow tools + cloud/HPC computing to run MNIST analyses
- Repeat steps above for fashion MNIST and humback whale classification if time.

## Instructions

### Adding code from other repos to this github repo ###
```sh
git clone repo you want
cd repofolder
git remote add destination https://github.com/cyber-carpentry/group2-machine-learning
git remote rm origin
git pull --allow-unrelated-histories https://github.com/cyber-carpentry/group2-machine-learning
git push -u destination master
```

### Launching MNIST classifier with mlp neural network ###

This will launch a jupyter notebook in a docker container running on the BinderHub servers.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cyber-carpentry/group2-machine-learning/master)

## Group 2 Useful Links

[HackMD Notes](https://hackmd.io/@stephprince/r1BFBO7MH)

[Planning Notes](https://hackmd.io/8IlRqMagSr-wxBMXtmtgnA?both#Planning)
