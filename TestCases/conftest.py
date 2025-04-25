from selenium import webdriver
import pytest

@pytest.fixture()                 #### Gives respective browser
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print('***** Launching chrome browser *****')
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print('***** Launching firefox browser *****')
    else:           # Setting edge as default browser if no browser is passed in CLI.
        driver=webdriver.Edge()
        print('***** Launching edge browser *****')
    return driver


def pytest_addoption(parser):   # This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture() # This will return the Browser value to the setup method
def browser(request):
    return request.config.getoption('--browser')


############# pytest HTML Report #####################

# Custom title for the report
def pytest_html_report_title(report):
    report.title = "Automation Test Report - Hybrid Framework"

# Custom environment info in the summary section
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "Project Name: Hybrid Framework",
        "Module Name: Login/Signup",
        "Tester: Hari"
    ])

# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME',None)
    metadata.pop('Plugins',None)




