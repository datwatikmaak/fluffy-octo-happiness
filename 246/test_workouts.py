import pytest

from workouts import print_workout_days


@pytest.mark.parametrize('test_input, expected', [
    ('upper', 'Mon, Thu'),
    ('lower', 'Tue, Fri'),
    ('cardio', 'Wed'),
    ('running', 'No matching workout')
])
def test_print_workout_days(capsys, test_input, expected):
    print_workout_days(test_input)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
