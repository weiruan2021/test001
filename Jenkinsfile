pipeline {
  agent {
    label 'macOS12.4'
  }
  stages {
    
    stage('Build') {
      steps {
        withEnv(['MY_NAME_IS=Eric']) {
          sh 'echo My Name is $MY_NAME_IS'
        }
        echo 'Building1'
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
