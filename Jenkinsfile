pipeline {
  agent {
    label 'macOS'
  }
  stages {
    stage('Build') {
      steps {
        echo 'Building1'
        sh 'cd /usr/local/bin'
        sh 'ls -al'
        sh '/usr/local/bin/appium &'
        
      }
    }

    stage('Test') {
      steps {
        echo 'Testing'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying'
      }
    }

  }
  options {
    skipStagesAfterUnstable()
  }
}
