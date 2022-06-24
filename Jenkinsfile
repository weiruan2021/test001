pipeline {
  agent {
    label 'macOS12.4'
  }
  stages {
    withEnv(['MY_NAME_IS=Eric']) {
      sh 'echo My Name is $MY_NAME_IS'
    }
    stage('Build') {
      steps {
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
