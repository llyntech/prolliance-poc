pipeline {
  agent any
  stages {
    stage('Build') {
      environment {
        TESTNFS = '/var/jenkins_home/testnfs/'
        WORKSPACE = '/var/jenkins_home/workspace/prolliance-poc_master'
      }
      steps {
        echo 'Copying test code to test server...'
        sh '''#!/bin/bash

cd $TESTNFS

timestamp=$(date +%Y%m%d%H%M%S)

mkdir $timestamp

cp -r $WORKSPACE/testing/* $timestamp/'''
      }
    }
  }
}