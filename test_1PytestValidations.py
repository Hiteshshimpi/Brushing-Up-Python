#fixtures --> reusable code
import pytest
#scope = session
#if scope == class then it will be executed once for the entire class similar to module
@pytest.fixture (scope="module") # if scope = function then it will execute for each test , and if module it executes only once for that test file
def rework():
     print("I setup Browser Instance")
     yield
     # Yeild keyword seperates between pre and post condition
     print("I teardown Browser Instance")



def  test_initialCheck(rework):
     print("this is initialCheck")

@pytest.mark.skip
def test_automation1(rework):
     print("this is automation1")

@pytest.mark.smoke
def test_automation2(rework):
     print("this is automation2")