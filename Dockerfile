FROM jupyter/tensorflow-notebook:7a3e968dd212

RUN wget https://github.com/cyber-carpentry/group2-machine-learning/tarball/master -O - \
   | tar -xz -C /home/jovyan/

RUN conda install -c bioconda -c conda-forge snakemake-minimal=5.3.0

