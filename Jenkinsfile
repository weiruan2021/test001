pipeline {
  agent {
    label 'macOS12.4'
  }
  withEnv(['MY_NAME_IS=weiruan']) {
    sh 'echo My Name is $MY_NAME_IS'
  }
  stages {
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
