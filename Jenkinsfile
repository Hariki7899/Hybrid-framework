pipeline {
    agent any

    stages {
        stage('Run Tests') {
            steps {
                bat '''
                    "C:\\Users\\91638\\PycharmProjects\\Hybrid framework\\.venv\\Scripts\\python.exe" -m pytest -v -s ^
    --html=./Reports/report.html ^
    TestCases/ ^
    --browser chrome
                '''
            }
        }

        stage('Analyze Logs') {
            steps {
                bat '''
                    "%WORKSPACE%\\.venv\\Scripts\\python.exe" ^
                    "%WORKSPACE%\\LogSummary\\log_summary.py" ^
                    "%WORKSPACE%\\Logs\\automation.log"
                '''
            }
        }
    }

    post {
        always {
            // Archive both HTML report and log summaries
            archiveArtifacts artifacts: 'Reports/report.html, LogSummary/*.txt'
        }
    }
}