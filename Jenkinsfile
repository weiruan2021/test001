pipeline {
  agent {
    label 'macOS12.4'
  }
  stages {
    
    stage('Build') {
      steps {
        withEnv(['JAVA_HOME=/usr/libexec/java_home']) {
          sh 'echo My Name is $JAVA_HOME'
          sh 'echo $PATH'
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
