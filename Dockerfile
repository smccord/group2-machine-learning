FROM jupyter/tensorflow-notebook:7a3e968dd212

ADD --chown=100 mlp_MNIST_smp.ipynb /home/jovyan/

