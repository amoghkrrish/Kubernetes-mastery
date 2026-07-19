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
