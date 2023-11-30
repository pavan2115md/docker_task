pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // This step can be used for any pre-build actions if needed
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests if needed
                    sh 'python3 -m unittest test_app.py'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image for the Python script
                    docker.build("my-python-app:${env.ce32d1c45494 }")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the Docker container
                    docker.image("my-python-app:${env.ce32d1c45494 }").run()
                }
            }
        }
    }

    post {
        success {
            // Do something on successful build
            echo 'Build successful!'
        }
        failure {
            // Do something on build failure
            echo 'Build failed!'
        }
    }
}

