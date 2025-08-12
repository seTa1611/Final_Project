pipeline {
  agent any
  stages {
    stage('Clone') {
      steps {
        // Pull the latest code from your GitHub repo
        git 'https://github.com/seTa1611/fastapi-todo.git'
      }
    }
    stage('Build Docker Image') {
      steps {
        // Build the Docker image and tag it (both by build number and 'latest')
        sh 'docker build -t asafm1611/fastapi-todo:$BUILD_NUMBER .'
        sh 'docker tag asafm1611/fastapi-todo:$BUILD_NUMBER asafm1611/fastapi-todo:latest'
      }
    }
    stage('Push Image') {
      steps {
        // Login and push to Docker Hub (needs Jenkins creds set as 'dockerhub-creds')
        pipeline {
  agent any
  stages {
    stage('Clone') {
      steps {
        // Pull the latest code from your GitHub repo
        git 'https://github.com/seTa1611/fastapi-todo.git'
      }
    }
    stage('Build Docker Image') {
      steps {
        // Build the Docker image and tag it (both by build number and 'latest')
        sh 'docker build -t asafm1611/fastapi-todo:$BUILD_NUMBER .'
        sh 'docker tag asafm1611/fastapi-todo:$BUILD_NUMBER asafm1611/fastapi-todo:latest'
      }
    }
    stage('Push Image') {
      steps {
        // Login and push to Docker Hub (needs Jenkins creds set as 'dockerhub-creds')
        withCredentials([usernamePassword(credentialsId: 'github-pat', usernameVariable: 'GIT_USER', passwordVariable: 'GIT_TOKEN')]) {
            git credentialsId: 'github-pat', url: 'https://github.com/seTa1611/fastapi-todo.git'}
        }
      }
    }
    stage('Deploy to Kubernetes') {
      steps {
        // Deploy (or update) on your K8s cluster
        sh 'kubectl apply -f deployment.yaml'
        sh 'kubectl apply -f service.yaml'
      }
    }
  }
}