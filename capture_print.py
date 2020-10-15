import unittest

def add_numbers(num1, num2):
    print("Add function started ...")
    result = num1 + num2
    print("Numbers added. returning result ...")
    return result


def test_add_numbers():
    assert add_numbers(2,3) == 5

