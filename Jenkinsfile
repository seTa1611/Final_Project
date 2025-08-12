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
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
          sh 'docker push asafm1611/fastapi-todo:$BUILD_NUMBER'
          sh 'docker push asafm1611/fastapi-todo:latest'
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