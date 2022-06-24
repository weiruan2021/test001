pipeline {
  agent {
    label 'macOS12.4'
  }
  stages {
    stage('Build') {
      steps {
        echo 'Building1'
        sh """
          echo $JAVA_HOME
          echo $ANDROID_HOME
          echo $PATH
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
