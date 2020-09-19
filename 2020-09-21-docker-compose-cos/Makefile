PROJECT_ID:=devops-directive-project
REGION:=us-central1
ZONE:=us-central1-a
VM_NAME:=docker-compose
USER:=palas
SSH_STRING:=$(USER)@$(VM_NAME)

HOME_PATH:=/home/$(USER)

create-static-ip:
	gcloud compute \
		addresses create $(VM_NAME) \
		--project=$(PROJECT_ID) \
		--region=$(REGION)

delete-static-ip:
	gcloud compute \
		addresses delete $(VM_NAME) \
		--project=$(PROJECT_ID) \
		--region=$(REGION) \

create-vm:
	gcloud beta compute \
		instances create $(VM_NAME) \
		--project=$(PROJECT_ID) \
		--zone=$(ZONE) \
		--address=$(VM_NAME) \
		--machine-type=e2-medium \
		--subnet=default \
		--network-tier=PREMIUM \
		--metadata=google-logging-enabled=true \
		--maintenance-policy=MIGRATE \
		--service-account=1006868470482-compute@developer.gserviceaccount.com \
		--scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append \
		--tags=http-server \
		--image=cos-stable-81-12871-1196-0 \
		--image-project=cos-cloud \
		--boot-disk-size=10GB \
		--boot-disk-type=pd-standard \
		--boot-disk-device-name=$(VM_NAME)

delete-vm:
	gcloud compute \
		--project=$(PROJECT_ID) \
 		instances delete $(VM_NAME) \
		--zone=$(ZONE) \

#################

ssh:
	gcloud compute ssh $(SSH_STRING) --project=$(PROJECT_ID) --zone=$(ZONE)

define send-ssh-command
gcloud compute ssh $(SSH_STRING) \
		--project=$(PROJECT_ID) \
		--zone=$(ZONE) \
		--command $(1)
endef

CONFIGURE_DOCKER_AUTH:="docker-credential-gcr configure-docker"
configure-gcr:
	$(call send-ssh-command,$(CONFIGURE_DOCKER_AUTH))

REPO:=https://github.com/sidpalas/devops-directive.git
CLONE_REPO:="docker run -i --rm -v $(HOME_PATH):/root -v $(HOME_PATH):/git alpine/git clone $(REPO)"
clone-repo:
	$(call send-ssh-command,$(CLONE_REPO))

define ALIAS_COMMAND
"`cat ./alias.sh`"
endef

alias-docker-compose:
	$(call send-ssh-command,$(ALIAS_COMMAND))
