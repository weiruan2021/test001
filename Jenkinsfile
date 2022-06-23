pipeline {
  agent {
    label 'macOS12.4'
  }
  stages {
    stage('Build') {
      steps {
        echo 'Building1'
        sh 'ls /usr/local/bin -al'
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
