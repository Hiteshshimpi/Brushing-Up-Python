import pytest

#execute only once per session for all the files
@pytest.fixture(scope="session")

def preSetupWork():
    print("this is preSetup")
    return 'fail'