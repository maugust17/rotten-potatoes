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
    stage("Deploy"){
    
        echo 'I execute elsewhere'
        sh 'kubectl cluster-info dump'
        sh 'kubectl apply -f ./k8s/mongodb/deployment.yaml'
        sh 'kubectl apply -f ./k8s/web/deployment.yaml'
    }
}
