pipeline {
  agent any
  stages {
    stage('Deploy App to Kubernetes') {     
      steps {
        sh 'kubectl apply -f k8s/mongodb/deployment.yaml'
      }
    }
  }
}
