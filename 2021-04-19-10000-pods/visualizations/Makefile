plot:
	poetry run python plot.py

# ---

BASE_NAMESPACE?=all-the-pods

HEADER:="timestamp, pending-pods, creating-pods, running-pods"

create-csv:
	echo $(HEADER) > progress.csv

extract-progress:
	@printf `date +'%s', ` >> progress.csv
	@cat pods.txt | grep Pending | wc -l | tr -d '\n'>> progress.csv
	@printf ", " >> progress.csv
	@cat pods.txt | grep ContainerC | wc -l | tr -d '\n'>> progress.csv
	@printf ", " >> progress.csv
	@cat pods.txt | grep Running | wc -l >> progress.csv

echo-progress:
	@tail -1 progress.csv

kubectl-to-file:
	@kubectl get $(RESOURCE) -n $(BASE_NAMESPACE) > $(RESOURCE).txt

track-progress:
	while [[ true ]] ; do \
		$(MAKE) RESOURCE=pods kubectl-to-file ; \
		$(MAKE) extract-progress ; \
		$(MAKE) echo-progress ; \
		sleep 10 ; \
	done