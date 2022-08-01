# Getting Started with Kubernetes

Video: https://www.youtube.com/watch?v=XltFOyGanYE

## Python Application

### Create a virtual environment:
```bash
python3 -m venv ./venv
source ./venv/bin/activate
```

### Install the Dependencies
```bash
pip install -r requirements.txt
```

### Start the App
```bash
uvicorn main:app --reload
```

## Containerize the Application

```bash
docker build -t <IMAGE_TAG> .

docker push -t <IMAGE_TAG>
```

## Deploy to Kubernetess:

```bash
export KUBECONFIG=<PATH_TO_KUBE_CONFIG>

kubectl apply -f .

kubectl get pods 
```

### Validation and Debugging

```bash
kubectl port-forward <POD_NAME> 8080:80

kubectl exec -it <POD_NAME> -- bash
```