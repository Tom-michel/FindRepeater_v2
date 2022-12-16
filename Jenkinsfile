pipeline {
    agent any

    stages {
        
       
        stage('Deploy') {
            steps {
                echo 'Deploying.... prepare docker compose'
                
                    sh "pwd"
                    sh "ls"
                    sh "docker-compose up -d --build"
                    sh "echo Done"
                       
            }
        }
    }
}
