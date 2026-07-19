pipeline {
    agent any

    stages {

        stage('Checkout Source Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cloudcart:latest app/'
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                cd app
                docker compose down || true
                docker compose up -d
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                sleep 20
                curl -f http://localhost/health
                '''
            }
        }
    }

    post {

        success {
            echo 'CloudCart deployed successfully!'
        }

        failure {
            echo 'Deployment failed!'
        }
    }
}
