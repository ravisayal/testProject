# test_main.py

from main import print_hi
import builtins
import pytest


def test_print_hi_output(capsys):
    # Call the function
    print_hi("Tester")

    # Capture the output
    captured = capsys.readouterr()

    # Assert that the output is as expected
    assert captured.out.strip() == "Hi, Tester"
