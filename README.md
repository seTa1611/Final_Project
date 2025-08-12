# FastAPI ToDo App (Course Project)

A super simple ToDo API using FastAPI.  
Runs with Docker, deploys to Kubernetes, and has a Jenkins pipeline for CI/CD.

---

## Features

- REST API for ToDos (in memory)
- Dockerized
- K8s manifests included
- Jenkins automation

---

## Quick Start

### 1. Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload