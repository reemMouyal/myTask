Task:
Create Kubernetes cluster Using AKS-Engine(on Azure Cloud provider). Please don't use AKS managed service.
Setup K8s cluster with the latest stable version, with RBAC enabled.
The Cluster should have 2 services deployed – Service A and Service B:
Service A is a WebServer that exposes the following:
Current value of Bitcoin in dollar (updated every 10 seconds).
Average value over the last 10 minutes.
Service B is a REST API service, which expose a single controller that responses 200 status code.
Cluster should have nginx Ingress controller deployed, and corresponding ingress rules for Service A and Service B.
