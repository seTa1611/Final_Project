pipeline {
  agent any
  stages {
    stage('Build Docker Image') {
      steps {
        sh 'docker build -t asafm1611/fastapi-todo:$BUILD_NUMBER .'
        sh 'docker tag asafm1611/fastapi-todo:$BUILD_NUMBER asafm1611/fastapi-todo:latest'
      }
    }
    stage('Push Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
          sh 'docker push asafm1611/fastapi-todo:$BUILD_NUMBER'
          sh 'docker push asafm1611/fastapi-todo:latest'
        }
      }
    }
    stage('Deploy to Kubernetes') {
      steps {
        sh 'kubectl apply -f deployment.yaml'
        sh 'kubectl apply -f service.yaml'
      }
    }
  }
}