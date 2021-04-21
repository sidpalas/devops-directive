PROJECT_ID:=devops-directive-gcs-https
KOPS_FEATURE_FLAGS:=AlphaAllowGCE # to unlock the GCE features
STATE_BUCKET:=gs://sid-kops-cluster-state

CLUSTER_NAME=simple.k8s.local
ZONE:=us-central1-a

create-state-store:
	gsutil mb -p $(PROJECT_ID) $(STATE_BUCKET)

create-cluster:
	KOPS_FEATURE_FLAGS=AlphaAllowGCE \
		kops create cluster $(CLUSTER_NAME) \
		--zones $(ZONE) \
		--state $(STATE_BUCKET)/ \
		--project=$(PROJECT_ID) \
		--node-count 44 \
		--node-size n1-standard-1 \
		--master-size n1-standard-4

update:
	KOPS_FEATURE_FLAGS=AlphaAllowGCE \
		kops update cluster $(CLUSTER_NAME) \
		--state $(STATE_BUCKET)/

apply-update:
	KOPS_FEATURE_FLAGS=AlphaAllowGCE \
		kops update cluster $(CLUSTER_NAME) \
		--state $(STATE_BUCKET)/ \
		--yes

rolling-update:
	KOPS_FEATURE_FLAGS=AlphaAllowGCE \
		kops rolling-update cluster $(CLUSTER_NAME) \
		--state $(STATE_BUCKET)/ \
		--yes


validate-cluster:
	kops validate cluster --wait 10m --state $(STATE_BUCKET)

delete-cluster:
	kops delete cluster $(CLUSTER_NAME) \
		--state $(STATE_BUCKET)/ \
		--yes 

edit-cluster:
	kops edit cluster $(CLUSTER_NAME) \
		--state $(STATE_BUCKET)/

edit-node-instance-template:
	kops edit ig --name=$(CLUSTER_NAME) nodes \
		--state $(STATE_BUCKET)/

edit-master-instance-template:
	kops edit ig --name=$(CLUSTER_NAME) master-us-central1-a \
		--state $(STATE_BUCKET)/

create-kubecfg:
	kops export kubecfg $(CLUSTER_NAME) \
		--state $(STATE_BUCKET)
