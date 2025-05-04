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
                    "C:\\Users\\91638\\PycharmProjects\\Hybrid framework\\.venv\\Scripts\\python.exe" ^
                    "C:\\Users\\91638\\PycharmProjects\\Hybrid framework\\LogSummary\\log_summary.py" ^
                    "C:\\Users\\91638\\.jenkins\\workspace\\Hybrid framework Pipeline\\Logs\\automation.log
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