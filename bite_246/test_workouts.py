"""In this Bite you test a function that prints to stdout. Check out pytest's Capturing of the stdout/stderr output how to test this.

You probably want to use the capsys / capfd fixture in your test code and you'll probably find a good use case for @pytest.mark.parametrize here too.

Have fun and keep calm and code in Python!
"""

import pytest

from workouts import print_workout_days

@pytest.mark.parametrize("test_input,expected", [("upper", "Mon, Thu"), ("lower", "Tue, Fri"), 
("cardio", "Wed"), ("ghgf", "No matching workout")])

def test_print_workout_days(capsys, test_input, expected):
    print_workout_days(test_input)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected