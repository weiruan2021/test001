pipeline {
  agent {
    label 'macOS12.4'
  }
  stages {
    stage('Build') {
      steps {
        echo 'Building1'
        sh """
          pwd
          hostname
          whereis appium
        """   
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
