pytest -s -v -m "sanity" --html=./Reports/report.html TestCases/ --browser chrome
REM pytest -s -v -m "sanity" --html=./Reports/report.html TestCases/ --browser firefox
REM pytest -s -v -m "sanity" --html=./Reports/report.html TestCases/ 
REM pytest -s -v -m "sanity or regression" --html=./Reports/report.html TestCases/ --browser chrome
REM pytest -s -v -m "regression" --html=./Reports/report.html TestCases/ --browser chrome
REM pytest -s -v -n=4 -m "sanity" --html=./Reports/report.html TestCases/ --browser chrome
REM pytest -s -v -n=6 -m "sanity or regression" --html=./Reports/report.html TestCases/ --browser chrome