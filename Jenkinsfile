node {
    checkout scm

    docker.withRegistry('https://hub.docker.com/', 'credentials-id') {

        def customImage = docker.build("my-image:${env.BUILD_ID}","./src")

        /* Push the container to the custom Registry */
        customImage.push()
    }
}
