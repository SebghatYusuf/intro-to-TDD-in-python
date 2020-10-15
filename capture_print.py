import unittest

def add_numbers(num1, num2):
    print("Add function started ...")
    result = num1 + num2
    print("Numbers added. Returning result")
    return result


def test_add_numbers(capsys):
    result = add_numbers(2, 3)
    captured = capsys.readouterr()
    assert "Add function started" in captured.out
    assert "Numbers added. Returning result" in captured.out
    # thus far, readouterr() out only has the two print statements from the add_numbers function
    assert result == 5
    print("thank you, next")
    captured = capsys.readouterr()
    # here, readouterr() out doesn't have the two outputs from above
    # it now contains the new value, "thank you, next"
    assert captured.out == "thank you, next\n"