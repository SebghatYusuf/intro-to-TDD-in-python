import pytest

def setup_stuff():
    return False

def test_stuff(): #this test will be executed
    pass

@pytest.mark.skip(reason = "just testing if skip works")
def test_other_stuff(): #This one will be skipped
    if not setup_stuff():
        pytest.skip("Setup failed")
    else:
        pass

# If you prefer to check that the condition is satisfied 
# before the test starts, then you can use skipif:

@pytest.mark.skipif(not setup_stuff(), reason="Setup failed")
def test_other_stuff():
    pass