# DevOps Project — User API

## Overview

This project is a simple **RESTful User API** that allows:
- Adding users
- Modifying user information
- Deleting users

User data (email and password) is stored in a **MariaDB database**.

The project covers the full **DevOps lifecycle**, including:
- Application development
- Infrastructure as Code **(IaC)**
- Docker containerization
- Continuous Integration **(CI)**
- Container orchestration using **Kubernetes**

---

## 1. Work Performed

### Application :
- Development of a **User API** (CRUD operations: create, read, update, delete)
- User data persistence using **MariaDB**
- **Unit and functional tests** to validate differentes cases

### CI/CD :
- **GitHub Actions pipeline**
  - Automated tests to protect the integrity of the `main` branch
  - Pipeline triggered on push and pull requests

### IaC : Vagrant + Ansible

To make the environment reproducible and easy to set up, we implemented an Infrastructure as Code workflow using Vagrant and Ansible. The idea is to automatically create a virtual machine and configure everything required for our FastAPI + MariaDB application without manual installation.

#### Vagrantfile

The `iac/Vagrantfile` is responsible for creating and configuring the development virtual machine. It:

- Creates an Ubuntu 22.04 (ubuntu/jammy64) VM  
- Syncs the project directory into `/vagrant` inside the VM  
- Forwards port 5000 from the VM to the host  
- Automatically runs the Ansible playbook (`iac/provision.yml`) after booting  

This allows the entire environment to be created using a single command.

#### Ansible Provisioning

The `iac/provision.yml` playbook installs and configures everything needed for the application to run:

- Installs Python, pip, virtualenv, and all required system packages  
- Installs MariaDB, enables the service, and creates the application database and user  
- Creates a Python virtual environment inside `/opt/devopsapp` and installs the dependencies from `requirements.txt`  
- Deploys a systemd service (`devopsapp.service`) that starts the FastAPI application automatically  
- Starts the application and performs a health check using Ansible’s `uri` module to ensure the API responds at:  
  `http://127.0.0.1:5000/`

By the time provisioning finishes, the application is fully installed, running, and reachable from the host machine.

---

### How to Run the IaC Setup

**Start the VM:**
```bash
cd iac
vagrant up





### Containerization

- Creation of a **Docker image** for the User API using a Dockerfile
- The image can be used to run the application locally in a consistent environment
- The image is published to **Docker Hub** for easy distribution

### Kubernetes :
- Local cluster setup using Minikube for container orchestration
- Persistent storage with PersistentVolume (PV) and PersistentVolumeClaim (PVC) for MariaDB data persistence
- Deployments for both MariaDB database and FastAPI application using Docker images
- Services configured: ClusterIP for internal database access and NodePort for external API access
- Deployment execution using kubectl apply -f k8s/ with all manifest files in the k8s/ director

---

## 2. Screenshots

Screenshots are available in the `./screenshots` folder.

They include:
- API running and responding to requests
- Docker build and run commands    
- Docker Hub repository
- GitHub Actions CI/CD pipeline
- Kubernetes Deployment & Management

### Flask Application Running Locally
![Flask running locally](./screenshots/flask-running-local.png)

---

### Graphical User Interface – User API
![User API graphical interface](./screenshots/graphical-interface-User-API.png)

---

### Graphical Interface – Create User
![Create user interface](./screenshots/graphical-interface-User-API-CREATE.png)

---

### Graphical Interface – Update User
![Update user interface](./screenshots/graphical-interface-User-API-UPDATE.png)

---

### Docker Hub – Published Image
![Docker Hub image](./screenshots/docker-hub-image.png)

---

### Local MariaDB Container
![Local MariaDB container](./screenshots/screenshots-mariadb-local.png)

---

## Error Handling & Validation

### Invalid password during user creation
![Password validation error](./screenshots/error-pwd-create-user.png)

### Invalid name during user update
![Name validation error](./screenshots/error-name-update-user.png)

### Invalid email during user update
![Email validation error](./screenshots/error-email-update-user.png)

### Flask server error logs
![Flask server logs with error](./screenshots/flask-server-logs-with-error.png)

### GitHub Pull Request – Unmerged Unit Test
![GitHub Pull Request – Unmerged Unit Test](./screenshots/error-github-pull-request-unmerged-unit-test.png)

### GitHub Actions – Failed Merge / Validation
![GitHub Actions merge error](./screenshots/actions-error-merge.png)

---

##  Kubernetes Deployment Verification

### Pod Status
![Kubernetes Pods Status](./screenshots/Pod-Status.png)

---

### Service Configuration  
![Kubernetes Services](./screenshots/Service-Configuration.png)

---

### Application Access URL
![Minikube Access URL](./screenshots/Application-Access-URL.png)

---

### API Response Verification
![API Response Test](./screenshots/API-Response-Verification.png)

---

### Persistent Storage Status
![Persistent Storage](./screenshots/Persistent-Storage-Status.png)

---

##  Deployment Summary
All five verification steps confirm a successful Kubernetes deployment: containers are running, networking is configured, persistent storage is active, and the application is fully accessible.

---

## 3. Useful Commands

Run the application locally (development)
python .\devopsproject\app.py

Build the Docker image
docker build -t devopsapp .

Run the application using Docker
docker run --rm -e DEVOPS_DB_HOST=host.docker.internal -p 5000:5000 devopsapp

Authenticate to Docker Hub
docker login

Tag the Docker image for Docker Hub
docker tag devopsapp hmorais1001/devopsapp:latest

Push the Docker image to Docker Hub
docker push hmorais1001/devopsapp:latest

Basic API testing locally
curl http://localhost:5000/  
curl http://localhost:5000/users

---

### Kubernetes Commands

Start cluster
minikube start

Deploy everything
kubectl apply -f k8s/

Check status
kubectl get all  
kubectl get pods  
kubectl get services

Get access URL
minikube service devops-api --url

Test API
curl http://127.0.0.1:60338/

Check storage
kubectl get pv,pvc

View logs
kubectl logs deployment/devops-api

---

## 4. Links

- GitHub Repository: https://github.com/hugodsti/DevOps-Final-Project-FastAPI
- Docker Hub Image: https://hub.docker.com/r/hmorais1001/devopsapp

## 5. Authors

- **Hugo Morais**
- **Rachid Djamal**
- **Ojong Bessong Nkongho**

---

## 6.

- AI tools (ChatGPT, Gemini) were used to improve the clarity and structure of documentation and to facilitate certain tasks. No application code or infrastructure configuration was fully generated or directly used.

## Bonus

- The application was developed in Python instead of the NodeJS application provided in the labs.
- Additional API features, validation logic, and unit/functional tests were implemented compared to the base example.
