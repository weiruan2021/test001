pipeline {
  agent {
    label 'macOS12.4'
  }
  environment {
    DISABLE_AUTH = 'true'
  }
  stages {
    
    stage('Build') {
      steps {
        echo 'Building1'
        'appium &'
        '''
          appium &
        '''
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
