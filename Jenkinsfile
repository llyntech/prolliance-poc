pipeline {
  agent any
  stages {
    stage('Build') {
      environment {
        TESTNFS = '/var/jenkins_home/testnfs'
        WORKSPACE = '/var/jenkins_home/workspace/prolliance-poc_master'
      }
      steps {
        echo 'Build steps are TBD...'
        echo 'Copying test code to test server...'
        sh '''#!/bin/bash

cd $TESTNFS
timestamp=$(date +%Y%m%d%H%M%S)
mkdir $timestamp
cp -r $WORKSPACE/testing/* $timestamp/
export TESTBUILD=$timestamp

'''
      }
    }
    stage('Test') {
      steps {
        echo 'Starting system validation...'
        sh '''#! /bin/bash

ssh llyntech@10.0.0.68 #connect to test server

cd /home/llyntech/testing

cd $TESTBUILD/web_app_test/

pytest --alluredir=./my_allure_results


'''
      }
    }
  }
}