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
          sh 'export PATH=/usr/local/Cellar/maven/3.8.5/bin:$PATH'
          sh 'echo $PATH'
          
        }
        echo 'Building1'
        sh '''
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
