# install behave
pip install behave

# Test Report
You can generate Allure report for your Behave tests.

# First you need to install Allure Behave formatter:

$ pip install allure-behave

# Then specify the formatter when run your tests:

$ behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features

# This will generate JSON report to %allure_result_folder%. Then, to view HTML report you can use Allure Command line 

$ allure serve %allure_result_folder%
