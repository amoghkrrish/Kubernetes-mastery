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
