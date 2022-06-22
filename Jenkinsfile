pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building1'
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
