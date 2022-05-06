node {
    stage("Build"){
        checkout scm

        docker.withRegistry('https://registry.hub.docker.com/', 'credentials-id') {

            def customImage = docker.build("allwenn/rotten-potatoes:${env.BUILD_ID}","./src")

            /* Push the container to the custom Registry */
            customImage.push()
            customImage.push("latest")
        }
    }
    stage('List pods') {
    withKubeConfig([credentialsId: 'credentials-id-k8s',
                    caCertificate: 'LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUJkekNDQVIyZ0F3SUJBZ0lCQURBS0JnZ3Foa2pPUFFRREFqQWpNU0V3SHdZRFZRUUREQmhyTTNNdGMyVnkKZG1WeUxXTmhRREUyTlRFNE5qWTBNemN3SGhjTk1qSXdOVEEyTVRrME56RTNXaGNOTXpJd05UQXpNVGswTnpFMwpXakFqTVNFd0h3WURWUVFEREJock0zTXRjMlZ5ZG1WeUxXTmhRREUyTlRFNE5qWTBNemN3V1RBVEJnY3Foa2pPClBRSUJCZ2dxaGtqT1BRTUJCd05DQUFUVDBIek5ucEUySTljV2J4T1kxemF0ZEhSMDdlOVZZU1VHdlppd1o0clYKUFBYejFpRjJmTlE2bkVUMHFRTXY4bHIxNDRTT3VvRlNQeHVtbWE5VUVocHpvMEl3UURBT0JnTlZIUThCQWY4RQpCQU1DQXFRd0R3WURWUjBUQVFIL0JBVXdBd0VCL3pBZEJnTlZIUTRFRmdRVU5KV2VUTlgwZXozV0pmSTlTek81CjRRS2QwNlV3Q2dZSUtvWkl6ajBFQXdJRFNBQXdSUUlnYXFPcWRzVjN0U3RNZm5wanR4d0taa0k4QVB4aHQ3aWgKRTNhK2ZQK3RHOFVDSVFDUVNLWmpLc2VaQWUweXIwN1h2MUhrcVo1eGpOSTZWU1M0VHJmM0ZYRHZNdz09Ci0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS0K',
                    serverUrl: 'https://host.docker.internal:1102',
                    contextName: 'k3d-prueba',
                    clusterName: 'k3d-prueba'
                    ]) {
      sh 'kubectl get pods'
    }
  }
    stage("Deploy"){
        
        withKubeConfig([credentialsId: 'credentials-id-k8s', serverUrl: 'https://127.0.0.1:1102']) {
            sh 'kubectl apply -f ./k8s/mongodb/deployment.yaml'
            sh 'kubectl apply -f ./k8s/web/deployment.yaml'
        }
        
    }
}
