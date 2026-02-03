import pytest

@pytest.mark.smoke
def test_automation3(preSetupWork):
    print("this is automation1")
    assert preSetupWork == 'fail'


#Yeild keyword seperates between pre and post condition