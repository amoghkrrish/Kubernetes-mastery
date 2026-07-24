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

# Kubernetes Day 5 – Persistent Volumes

## What I learned
- Pod storage is temporary; it disappears when the Pod is deleted.
- PersistentVolumes (PV) are storage resources in the cluster.
- PersistentVolumeClaims (PVC) are requests for storage by Pods.
- Binding: PVC binds to a matching PV.
- Using `hostPath` to create a local PV for learning.
- Mounting a PVC into a Pod’s filesystem.
- Data survives Pod deletion because it’s stored on the PV.

## Files
- `pv.yaml` – PersistentVolume (hostPath, 1Gi).
- `pvc.yaml` – PersistentVolumeClaim (1Gi, ReadWriteOnce).
- `pod.yaml` – Pod (busybox) that uses the PVC.

## Commands

### Create PV and PVC
```bash
kubectl apply -f pv.yaml
kubectl apply -f pvc.yaml

# Kubernetes Day 6 – Ingress

## What I learned
- Ingress lets you expose multiple Services through a single IP/port.
- The Ingress Controller (nginx) handles routing based on URL paths.
- Writing Ingress rules with `path` and `pathType`.
- Using `rewrite-target` annotation to strip the path prefix before forwarding.
- Testing Ingress using `kubectl port-forward` and `curl` with a custom `Host` header.

## Files
- `web-app.yaml` – Deployment + Service for the web app.
- `api-app.yaml` – Deployment + Service for the API app.
- `ingress.yaml` – Ingress resource with path rules.

## Commands

### Enable Ingress addon
```bash
minikube addons enable ingress

# Kubernetes Day 7 – Namespaces & Resource Quotas

## What I learned
- Namespaces provide logical isolation inside a cluster.
- How to create a namespace and deploy resources into it.
- Same resource name can exist in different namespaces.
- ResourceQuota limits the total CPU, memory, and object count in a namespace.
- What happens when a Pod tries to exceed the quota (stuck in Pending).

## Files
- `pod-dev.yaml` – Pod in the `dev` namespace.
- `pod-qa.yaml` – Pod in the `qa` namespace.
- `quota-dev.yaml` – ResourceQuota for `dev`.
- `pod-small.yaml` – Pod that respects the quota.
- `pod-huge.yaml` – Pod that violates the quota.

## Commands

### Create namespaces
```bash
kubectl create namespace dev
kubectl create namespace qa
