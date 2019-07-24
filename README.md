# group2-machine-learning

# Introduction

## Project phases
- Making the repository and the required materials.
- Build docker containers for the MNIST analyses
- Use workflow tools + cloud/HPC computing to run MNIST analyses
- Repeat steps above for fashion MNIST and humback whale classification if time.

## Instructions

### Initiate a virtual machine through a cloud server
  1. Log in to [Jetstream](https://use.jetstream-cloud.org/application/dashboard) and click "Start a New Instance."
  2. Select the _Ubuntu 18.04 Devel and Docker_ instance and press launch.
  3. Select an _m1.medium_ instance in instance size, and then click "Launch Instance."
  4. Once the instance is "Active," go into the shell either through the Web Shell or via ssh.
  
### Run the docker image
  1. Pull the docker image with the command below. You can use ``` docker images ``` to check if you successfully pulled the image. 
  
     ``` docker pull sprince399/mlnotebook ```
     
  2. There are two options for running the docker image
  
     **Option 1:** Run the image with the command below if you would like to automatically initiate and run the neural networks. 
  
       ```docker run -e dataset=mnist -it sprince399/mlnotebook sh ```
  
      The default is to run a neural net classifier on MNIST. If you would like to specify a dataset, you can add it with the ```-e``` tag (see example above). Options are mnist, fashion, whale. 
      
      Once you are in the shell, run the commands below:
      ```
      cd cyber-carpentry-group2-machine-learning-*
      python run_main.py dataset --int_param ${dataset}
      ```
      
      Now the neural network builder and classifier has launched! When it is finished, you will see an output file with a text and pdf summary of the results. Compare your results to the example output below
      
     **Option 2:** Run the image with the command below if you would like to explore the neural network models and scripts via jupyter notebooks. You will be given a prompt to access a jupyter notebook.
     
       ```docker run -p 80:8888 sprince399/mlnotebook```
       
       Set the working directory
       ```cd cyber-carpentry-group2-machine-learning-*```
       
        _If you are on your own machine_ go to your browser and type in http://127.0.0.1:80. You will be prompted to enter a token which you can copy from the prompt. 
        
        _If you are on a Jetstream instance_ copy the IP address from the instance. Then in your own browser type in http://JetstreamIPAddress:80. You will be prompted to enter a token which you can copy from the prompt. 
            
       Now you can play around with the neural network models! Select any of the files to explore. 
       
       
## Compare your results to the ones below! 

### MNIST ###
[Model summary](mnist_model_results_summary.txt)

![Model performance](results/mnist_results_summary_plots.pdf)

### fashion MNIST ###
[Model summary](fashion_model_results_summary.txt)

![Model performance](results/fashion_results_summary_plots.pdf)

## Group 2 Useful Links

[HackMD Notes](https://hackmd.io/@stephprince/r1BFBO7MH)

[Planning Notes](https://hackmd.io/8IlRqMagSr-wxBMXtmtgnA?both#Planning)
