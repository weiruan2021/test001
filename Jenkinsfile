pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building'
         sh 'emulator @sdk_gphone64_x86_64
         sh 'appium &'
        
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
