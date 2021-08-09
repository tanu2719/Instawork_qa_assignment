rem This batch file is used to run framework via command prompt

rem running via Chrome browser needs --browser=Chrome
pytest -v -s E:\Instawork\TestCase\test_flight_booking.py --browser chrome

rem else test case will run via firefox
rem pytest -s -v E:\Instawork\TestCase\test_flight_booking.py 

rem running test cases in parallel
rem pytest -v -s -n=1 E:\Instawork\TestCase\test_flight_booking.py --browser chrome
rem pytest -v -s -n=1 E:\Instawork\TestCase\test_flight_booking.py --browser firefox


