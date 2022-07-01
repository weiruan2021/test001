pipeline {
  agent {
    label 'macOS'
  }

  stages {
    
    stage('Build') {
      steps {
        echo 'Building1'
        appium 
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
