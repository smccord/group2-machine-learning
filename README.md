# Machine Learning Reproducible Example (Group 2) 
## Background
Machine learning classifiers, such as those found in tensorflow, are powerful tools for image classification. To test new models or newly parameterized models, the MNIST and MNIST-Fashion datasets are commonly used to to explore concepts in machine learning. The module below works through an example of machine learning in tensorflow using MNIST and MNISTFashion to compare model performance on two different datasets. In the future, additional models or datasets could also be added to this workflow to compare across more research situtations. 

## Instructions

### Initiate a virtual machine through a cloud server
  1. Log in to [Jetstream](https://use.jetstream-cloud.org/application/dashboard) and click "Start a New Instance."
  2. Select the _Ubuntu 18.04 Devel and Docker_ instance and press launch.
  3. Select an _m1.medium_ instance in instance size, and then click "Launch Instance."
  4. Once the instance is "Active," go into the shell either through the Web Shell or via ssh.
  
Note: All of the commands below can also be launched from the terminal on your local computer if you have Docker installed.

### Set up the docker image and volume ###
  
  1. Clone the github repo with the relevant dockerfile.
  
     ```
     git clone https://github.com/cyber-carpentry/group2-machine-learning/
     cd group2-machine-learning
     ```
  
  2. Now you will run a shell script to build your docker image and create a volume to store your results. 
  
    ```
    sh setup_docker.sh
    ```
  
### Start the neural network classifiers ###    
 
 There are multiple options for using the neural networks. We suggest starting with Option 1 for optimal reproducibility. 
  - [Option 1](README.md#option-1): Run both mnist and fashion mnist datasets in parallel.
  - [Option 2](README.md#option-2): Run mnist or fashion mnist datasets on their own.
  - [Option 3](README.md#option-3): Explore the code via jupyter notebooks.
 
#### **Option 1:** ####
 Run both mnist and fashion mnist datasets in parallel. 

  1. Enter the command below to run the docker image.
 
     ``` 
     docker run --rm --mount source=results,target=/home/jovyan/results -it sprince399/mlnotebook sh
     ```
    
  2. Once you are in the shell, run the command below:
     
     ```
     cd cyber-carpentry-group2-*
     snakemake
     ```
     
   The neural network model and classifier has launched!
   
  3. When they are finished, you will find the files summarizing the output and results of the model in the /home/jovyan/results folder. You can also access these files outside of the Jetstream instance by entering the command below.
  
  ```
  sudo cat ${MYVOLDIR}/fileyouwanttolookat
  
  #for example
  sudo cat ${MYVOLDIR}/mnist_model_results_summary.txt
  ```
      
  Compare your results [here!](README.md#example-results)  
  
  4. Optional: To rerun the classifier inside the container, first delete the snakemake results with the command below.
    
     ```
     snakemake some_target --delete-all-output
     ```
  
  
#### **Option 2:** ####
Run mnist or fashion mnist datasets on their own.

 1. Enter the command below to run the docker image. Fill in the section `/local/path/for/results/` with the location on your instance and/or local computer 
 
   ``` 
     docker run --rm --mount source=results,target=/home/jovyan/results -it sprince399/mlnotebook sh
   ```
    
 2. Once you are in the shell, run the commands below. You can specify the dataset you would like to run by writing ```mnist.txt``` or ```fashion.txt``` as the option for --int_param. 
 
      ```
      cd cyber-carpentry-group2-machine-learning-*
      python run_main.py dataset --int_param mnist.txt
      ```
  The neural network model and classifier has launched! When they are finished, you will find the files summarizing the output and results of the model in the volume path that was previously created. To access them enter the command below.
  
  ```
  sudo cat ${MYVOLDIR}/fileyouwanttolookat
  
  #for example
  sudo cat ${MYVOLDIR}/mnist_model_results_summary.txt
  ```
  
  Compare your results [here!](README.md#example-results)   

#### **Option 3:** ####

  1. Enter the command below if you would like to explore the neural network model code via jupyter notebooks. You will be given a prompt to access a jupyter notebook.
     
       ```
       docker run -p 80:8888 sprince399/mlnotebook
       ```
              
  _If you are on your own machine_ 
  Go to your browser and type in http://127.0.0.1:80. You will be prompted to enter a token which you can copy from the prompt. 
        
   _If you are on a Jetstream instance_
   Copy the IP address from the instance. Then in your own browser type in http://JetstreamIPAddress:80. You will be prompted to enter a token which you can copy from the prompt. 
            
 Now you can play around with the neural network models! Select any of the files to explore. 
   
## Example results ##

### MNIST ###
[Model summary](results/mnist_model_results_summary.txt)

[Model performance](results/mnist_results_summary_plots.pdf)

### fashion MNIST ###
[Model summary](results/fashion_model_results_summary.txt)

[Model performance](results/fashion_results_summary_plots.pdf)


## Group 2 Useful Links

[HackMD Notes](https://hackmd.io/@stephprince/r1BFBO7MH)

[Planning Notes](https://hackmd.io/8IlRqMagSr-wxBMXtmtgnA?both#Planning)
