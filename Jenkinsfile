node {
    checkout scm
    stage("Build"){
        

        docker.withRegistry('https://registry-1.docker.io/v2/', 'DockerHub') {

            def customImage = docker.build("devopsteamseducacionit/sitioweb:${env.BUILD_ID}","./src")

            /* Push the container to the custom Registry */
            customImage.push()
            customImage.push("latest")
        }
    }
    stage("Deploy"){
        sh 'kubectl apply -f k8s/mongodb/deployment.yaml'
        sh 'kubectl apply -f k8s/web/deployment.yaml'     
    }
}
