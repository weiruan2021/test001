pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building1'
       
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
