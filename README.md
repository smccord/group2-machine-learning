# group2-machine-learning

## Instructions

### Initiate a virtual machine through a cloud server
  1. Log in to [Jetstream](https://use.jetstream-cloud.org/application/dashboard) and click "Start a New Instance."
  2. Select the _Ubuntu 18.04 Devel and Docker_ instance and press launch.
  3. Select an _m1.medium_ instance in instance size, and then click "Launch Instance."
  4. Once the instance is "Active," go into the shell either through the Web Shell or via ssh.
  
Note: All of the commands below can also be launched from the terminal on your local computer if you have Docker installed.

### Create a volume in the virtual machine to store your results ###
  ```
  docker volume create results
  docker volume inspect results
  sudo chown :100 /var/lib/docker/volumes/results/_data
  sudo chmod 775 /var/lib/docker/volumes/results/_data
  sudo chmod g+s /var/lib/docker/volumes/results/_data
  ```
  
### Run the docker image ###
  1. Pull the docker image with the command below. You can use ``` docker images ``` to check if you successfully pulled the image. 
  
     ``` 
     docker pull sprince399/mlnotebook
     ```         
  2. Alternate option: pull from the GitHub page
     ```
     git clone https://github.com/cyber-carpentry/group2-machine-learning/
     cd group2-machine-learning
     docker build -t sprince399/mlnotebook .

 ### Start the neural network classifiers ###    
 
 There are multiple options for using the neural networks. We suggest starting with Option 1 for optimal reproducibility. 
  - [Option 1](README.md#option-1): Run both mnist and fashion mnist datasets in parallel.
  - [Option 2](README.md#option-2): Run mnist or fashion mnist datasets on their own.
  - [Option 3](README.md#option-3): Explore the code via jupyter notebooks.
 
#### **Option 1:** ####
 Run both mnist and fashion mnist datasets in parallel. 
 
 1. Use the command below to find your current directory and make a folder for your results
 
   ``` 
      export RESULTSDIR=$(pwd)/results/
   ```
   
 1. Enter the command below to run the docker image.
 
   ``` 
     ### docker run -v ${RESULTSDIR}:/home/jovyan/results -it sprince399/mlnotebook sh
     docker run --rm --mount source=results,target=/home/jovyan/results -it sprince399/mlnotebook sh
   ```
    
 2. Once you are in the shell, run the command below:
     
     ```
     cd cyber-carpentry-group2-*
     snakemake
     ```
 3. Optional: Delete snakemake results
    ```
    snakemake some_target --delete-all-output
    ```
 4. 
      
   The neural network model and classifier has launched! When they are finished, you will find the files summarizing the output and results of the model in the local path you specified on your computer. Compare your results [here!](README.md#example-results)   
      
#### **Option 2:** ####
Run mnist or fashion mnist datasets on their own.

 1. Enter the command below to run the docker image. Fill in the section ```/local/path/for/results/``` with the location on your instance and/or local computer 
 
   ``` 
     docker run -v /local/path/for/results/:/home/jovyan/results -it sprince399/mlnotebook sh
   ```
    
 2. Once you are in the shell, run the commands below. You can specify the dataset you would like to run by writing ```mnist.txt``` or ```fashion.txt``` as the option for --int_param. 
 
      ```
      cd cyber-carpentry-group2-machine-learning-*
      python run_main.py dataset --int_param mnist.txt
      ```
  The neural network model and classifier has launched! When they are finished, you will find the files summarizing the output and results of the model in the local path you specified on your computer. Compare your results [here!](README.md#example-results)   

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
