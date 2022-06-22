pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building1'
        sh 'emulator @sdk_gphone64_x86_64'
        sh 'cd /usr/local/bin'
        sh 'ls -l'
        echo 'Building2'
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
