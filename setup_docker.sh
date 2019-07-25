#get dockerfile from github repo
git clone https://github.com/cyber-carpentry/group2-machine-learning/
cd group2-machine-learning

#build the docker notebook from the dockerfile
docker build -t sprince399/mlnotebook .

#creates the volume
docker volume create results

#gets the directory where the file is stored
export MYVOLDIR=$(docker volume inspect --format '{{ .Mountpoint }}' results)

#set group permissions for read and write access
sudo chown :100 ${MYVOLDIR}
sudo chmod 775 ${MYVOLDIR} 
sudo chmod g+s ${MYVOLDIR}

