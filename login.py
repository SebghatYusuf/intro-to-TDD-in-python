import re
import pytest


def check_email_format(email):
    """check that entered email format is correct."""
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        raise Exception("Invalid email format")
    else:
        return "Email format is OK"


# Using pytest.raises in a with block as a context manager,
#  we can check that an exception is actually raised
#  if an invalid email is given. Running the tests on
#  the code as it is above should fail:
def test_email_exception():
    """test that exception is raised for invalid email"""
    with pytest.raises(Exception):
        assert check_email_format("fine@gmail.com")
