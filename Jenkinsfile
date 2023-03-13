pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }
            steps {
                sh 'python3 -m py_compile sources/add2.py sources/calc.py'
                stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --junit-xml test-reports/results.xml sources/test_calc.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Deliver') {
            agent any
//             environment {
//                 VOLUME = '$PWD/sources:/src'
//                 IMAGE = 'cdrx/pyinstaller-linux:python3'
//             }
            steps {
                dir(path: env.BUILD_ID) {
                    unstash(name: 'compiled-results')
                    sh "docker run --rm -v $PWD/sources:/src cdrx/pyinstaller-linux:python3 'pyinstaller -F add2.py'"
                }
            }
            post {
                success {
                    archiveArtifacts "${env.BUILD_ID}/sources/dist/add2"
                    sh "docker run --rm -v $PWD/sources:/src cdrx/pyinstaller-linux:python3 'rm -rf build dist'"
                }
            }
        }

    }
}