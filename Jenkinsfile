pipeline {
  agent any
  stages {
    stage('Deploy App to Kubernetes') {     
      steps {
        container('kubectl') {
          withCredentials([file(credentialsId: 'kubernetesLocal', variable: 'KUBECONFIG')]) {
            sh 'kubectl apply -f /k8s/web/deployment.yaml'
          }
        }
      }
    }
  }
}
