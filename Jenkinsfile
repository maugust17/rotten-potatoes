pipeline {
  agent any
  stages {
    stage('Deploy Kubernetes') {
        agent {
            kubernetes {
				yamlFile '/k8s/mongodb/deployment.yaml'
				yamlFile '/k8s/web/deployment.yaml'
            }
        }
    }
  }
}
