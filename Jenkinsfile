node {
    
    stage("Build"){
        

        docker.withRegistry('https://registry.hub.docker.com/', 'DockerHub') {

            def customImage = docker.build("devopsteamseducacionit/sitioweb:${env.BUILD_ID}","./src")

            /* Push the container to the custom Registry */
            customImage.push()
            customImage.push("latest")
        }
    }
    stage("Deploy"){
        
        kubernetes {
             
             yamlFile '/k8s/mongodb/deployment.yaml'
             yamlFile '/k8s/web/deployment.yaml'
        }     
    }
}
