#Lab 2

**1** I have installed python 3.8 using 
pip3 install pipent
pipenv --python 3.8
pipenv shell

**2** Installed requests and ntplib 
**3** Created app.py script 
**4** Installed pytest using pipenv install pytest.
**5** Successfully run unit tests with pytest tests/tests.py. 
**6** Created AmPm() function that returns night or day or throws exception RuntimeError if argument does not contain time string.
**7** Created test_get_time_of_day() unit test for check is function AmPm() works well.
**8** Using > and >> operators stored result of app.py execution to file results.txt command python3 app.py > results.txt. To append result of unit tests execution pytest tests/tests.py >> results.txt.
**9** Created Makefile for the repository. Add rules for set up the environment and install dependencies (make install), run unit tests (make test), run application (make run), and deploy (make deploy).
**10** After running "make" command created a new pipenv environment, installed all project and pushed to the remote.