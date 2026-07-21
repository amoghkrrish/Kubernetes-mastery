# Kubernetes Day 1 – First Pod

## What I learned
- Minikube installation and starting a local cluster.
- Pods are the smallest deployable unit in Kubernetes.
- Writing a Pod manifest (YAML) with `apiVersion`, `kind`, `metadata`, `spec`.
- `kubectl apply -f` to deploy.
- `kubectl get pods`, `describe`, `logs` to inspect.
- Port‑forwarding to access a Pod locally.

## Commands

### Start Minikube
```bash
minikube start --driver=docker

# Kubernetes Day 2 – Deployments

## What I learned
- Deployments manage a set of identical Pods (replicas).
- Writing a Deployment manifest (`kind: Deployment`, `replicas`, `selector`, `template`).
- How to deploy, inspect (`get`, `describe`, `logs`), and scale.
- Rolling updates and rollbacks with zero downtime.
- The relationship: Deployment → ReplicaSet → Pods.

## Commands

### Deploy
```bash
kubectl apply -f deployment.yaml

# Kubernetes Day 3 – Services

## What I learned
- Services give a stable IP/DNS name to a set of Pods selected by labels.
- `ClusterIP` – internal only, reachable from other Pods.
- `NodePort` – exposes a static port on every node, accessible from outside.
- `LoadBalancer` – provisions an external load balancer (simulated with `minikube tunnel`).
- How to test connectivity using `kubectl run --rm -it` and `minikube service`.

## Commands

### Apply the Deployment
```bash
kubectl apply -f deployment.yaml

# Kubernetes Day 4 – ConfigMaps & Secrets

## What I learned
- How to store plain-text configuration in a ConfigMap.
- How to store sensitive data (passwords) in a Secret.
- Injecting ConfigMap and Secret values into Pods as environment variables using `configMapKeyRef` and `secretKeyRef`.
- Updating a ConfigMap and restarting Pods to apply changes.
- Building a Docker image directly into Minikube with `minikube image build`.

## Files
- `app.py` – Flask web app that reads `WELCOME_MESSAGE` and `API_KEY` from env.
- `Dockerfile` – builds the Python image.
- `configmap.yaml` – ConfigMap with `WELCOME_MESSAGE`.
- `deployment.yaml` – Deployment that uses the ConfigMap and Secret.
- `service.yaml` – NodePort service to access the app.

## Commands

### Build image in Minikube
```bash
minikube image build -t my-flask-app:v1 .
