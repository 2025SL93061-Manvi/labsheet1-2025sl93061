pipeline {
    agent any
 
    stages {
 
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
                echo 'Source code checked out successfully.'
            }
        }
 
        stage('Build') {
            steps {
                echo 'Build stage: Verifying Python environment...'
                sh 'python3 --version'
                sh 'echo "Files in workspace:"'
                sh 'ls -la'
                echo 'Build stage complete.'
            }
        }
 
        stage('Test') {
            steps {
                echo 'Running tests on calculator functions...'
                sh 'python3 test_calculator.py'
            }
        }
 
        stage('Deploy') {
            steps {
                echo 'Deploy stage: Copying calculator.py to local deployment directory...'
                sh '''
                    mkdir -p /tmp/jenkins-deploy
                    cp calculator.py /tmp/jenkins-deploy/calculator.py
                    echo "Deployed files:"
                    ls -la /tmp/jenkins-deploy/
                    echo "Deployment to /tmp/jenkins-deploy successful!"
                '''
            }
        }
 
    }
}
