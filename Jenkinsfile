pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building'
        sh "appium"
        
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
