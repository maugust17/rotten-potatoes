pipeline {
  agent any
  stages {
    
    stage('Deploy App to Kubernetes') {     
      steps {
        container('kubectl') {
          withCredentials([file(credentialsId: 'kubernetesLocal', variable: 'KUBECONFIG')]) {
            sh 'sed -i "s/<TAG>/${BUILD_NUMBER}/" /k8s/web/deployment.yaml'
            sh 'kubectl apply -f /k8s/web/deployment.yaml'
          }
        }
      }
    }
   
      steps {
        sh 'echo Hola Mundo'
      }
    }
  }
}
