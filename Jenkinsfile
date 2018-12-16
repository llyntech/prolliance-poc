pipeline {
  agent any
  stages {
    stage('Build') {
      environment {
        TESTNFS = '/var/jenkins_home/testnfs/'
      }
      steps {
        echo 'Copying test code to test server...'
        sh '''#! /bin/bash

cd TESTNFS

timestamp=date +%Y%m%d%H%M%S

mkdir $timestamp
'''
      }
    }
  }
}