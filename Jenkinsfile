pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'python3 --version'
                sh 'python3 -m py_compile src/app.py tests/*.py'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -s tests -v'
            }
        }

        stage('Result') {
            steps {
                echo 'Python application build and tests completed.'
            }
        }
    }

    post {
        success {
            echo 'PIPELINE RESULT: SUCCESS'
        }
        failure {
            echo 'PIPELINE RESULT: FAILURE'
        }
        always {
            echo 'Pipeline execution finished.'
        }
    }
}
