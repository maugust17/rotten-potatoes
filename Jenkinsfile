node {
    checkout scm

    docker.withRegistry('https://registry.hub.docker.com/', 'credentials-id') {

        def customImage = docker.build("allwenn/rotten-potatoes:${env.BUILD_ID}","./src")

        /* Push the container to the custom Registry */
        customImage.push()
        customImage.push("latest")
    }
}
