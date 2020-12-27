PROJECT_ID:=devops-directive-project
IMAGE_PROJECT:=ubuntu-os-cloud
IMAGE_FAMILY:=ubuntu-1804-lts
ZONE:=us-west1-b
INSTANCE_NAME:=gpu-instance
MACHINE_TYPE:=n1-standard-4
GPU_TYPE:=nvidia-tesla-k80

USER:=palas
SSH_STRING:=$(INSTANCE_NAME)

create-instance:
	gcloud compute instances create $(INSTANCE_NAME) \
		--project=$(PROJECT_ID) \
		--zone=$(ZONE) \
		--preemptible \
		--machine-type=$(MACHINE_TYPE) \
		--image-family=$(IMAGE_FAMILY) \
		--image-project=$(IMAGE_PROJECT) \
		--maintenance-policy=TERMINATE \
		--accelerator="type=$(GPU_TYPE),count=1"

ssh:
	gcloud beta compute ssh $(SSH_STRING) --project=$(PROJECT_ID) --zone=$(ZONE)

# https://medium.com/quantrium-tech/installing-tensorflow-2-with-nvidia-gpu-on-google-cloud-instance-a8dde3746f23

# sudo apt-get update
# sudo apt-get upgrade

# sudo apt install gcc
# sudo apt install make

# wget https://us.download.nvidia.com/tesla/450.80.02/NVIDIA-Linux-x86_64-450.80.02.run
# sudo chmod +x NVIDIA-Linux-x86_64-450.80.02.run
# sudo ./NVIDIA-Linux-x86_64-450.80.02.run
# sudo reboot

# WARNING: nvidia-installer was forced to guess the X  
#            library path '/usr/lib' and X module path
#            '/usr/lib/xorg/modules'; these paths were
#            not queryable from the system.  If X fails  
#            to find the NVIDIA X driver module, please
#            install the `pkg-config` utility and the    
#            X.Org SDK/development package for your
#            distribution and reinstall the driver. 

# wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-repo-ubuntu1804_10.1.243-1_amd64.deb
# sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
# sudo dpkg -i cuda-repo-ubuntu1804_10.1.243-1_amd64.deb
# sudo apt-get update
# wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
# sudo apt install ./nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
# sudo apt-get update
# sudo apt-get install --no-install-recommends nvidia-driver-430
# sudo reboot
# sudo apt-get update
# sudo apt-get upgrade