pipeline {
  agent {
    label 'macOS'
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
