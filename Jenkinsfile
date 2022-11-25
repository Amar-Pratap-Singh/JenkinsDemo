pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Amar-Pratap-Singh/JenkinsDemo.git'
            }
        }
        stage('Permissions'){
            steps {
                sh "chmod u+x multiplication.py"
                // sh "chmod u+x testCase1.py testCase2.py testCase3.py testCase4.py testCase5.py"
                sh "chmod u+x testCases.py"
            }
        }
        stage('Build Code') {
            steps {
                sh "./multiplication.py"
            }
        }
        // stage('Test Code') {
        //     steps {
        //         sh "./testCase1.py"
        //         sh "./testCase2.py"
        //         sh "./testCase3.py"
        //         sh "./testCase4.py"
        //         sh "./testCase5.py"
        //     }
        // }
        stage('Test Code'){
            steps{
                sh "./testCases.py"
            }
        }
    } 
}