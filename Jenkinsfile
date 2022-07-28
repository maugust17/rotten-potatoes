pipeline {
  agent {
    kubernetes {
      yaml '''
        spec:
        containers:
        - name: golang
            image: golang:1.16.5
            command:
            - sleep
            args:
            - 99d
        '''
    }
  }
  stages {
    stage('Run maven') {
        agent {
            kubernetes {
                yaml '''
                    spec:
                    containers:
                    - name: maven
                      image: maven:3.8.1-jdk-8
                      command:
                      - sleep
                      args:
                      - 99d
                    '''
            }
        }
      steps {
        sh 'echo Hola Mundo'
      }
    }
  }
}
