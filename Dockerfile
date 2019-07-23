FROM jupyter/tensorflow-notebook:7a3e968dd212

ADD --chown=100 https://github.com/cyber-carpentry/group2-machine-learning/blob/master/mlp_MNIST_smp.ipynb /home/jovyan/

