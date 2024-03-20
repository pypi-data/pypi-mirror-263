import time
from PyTools_QOL import print_execution_time


def test_no_start_time_parameter(capfd):

    print_execution_time()
    captured = capfd.readouterr()
    assert "\nProgram executed in 0 seconds.\n\n" == captured.out


def test_zero(capfd):
    start_time = time.time()

    print_execution_time(start_time)
    captured = capfd.readouterr()
    assert "\nProgram executed in 0 seconds.\n\n" == captured.out


def test_seconds(capfd):
    start_time = time.time()

    print_execution_time(start_time - 1)
    captured = capfd.readouterr()
    assert "\nProgram executed in 1 second.\n\n" == captured.out

    print_execution_time(start_time - 5)
    captured = capfd.readouterr()
    assert "\nProgram executed in 5 seconds.\n\n" == captured.out


def test_minutes(capfd):
    start_time = time.time()

    print_execution_time(start_time - 61)
    captured = capfd.readouterr()
    assert "\nProgram executed in 1 minute, 1 second.\n\n" == captured.out

    print_execution_time(start_time - 301)
    captured = capfd.readouterr()
    assert "\nProgram executed in 5 minutes, 1 second.\n\n" == captured.out


def test_hours(capfd):
    start_time = time.time()

    print_execution_time(start_time - 3661)
    captured = capfd.readouterr()
    assert "\nProgram executed in 1 hour, 1 minute, 1 second.\n\n" == captured.out

    print_execution_time(start_time - 18061)
    captured = capfd.readouterr()
    assert "\nProgram executed in 5 hours, 1 minute, 1 second.\n\n" == captured.out


def test_days(capfd):
    start_time = time.time()

    print_execution_time(start_time - 90061)
    captured = capfd.readouterr()
    assert "\nProgram executed in 1 day, 1 hour, 1 minute, 1 second.\n\n" == captured.out

    print_execution_time(start_time - 435661)
    captured = capfd.readouterr()
    assert "\nProgram executed in 5 days, 1 hour, 1 minute, 1 second.\n\n" == captured.out
