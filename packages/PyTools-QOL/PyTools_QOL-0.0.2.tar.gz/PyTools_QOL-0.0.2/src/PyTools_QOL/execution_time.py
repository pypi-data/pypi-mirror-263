import time
from PyTools_QOL import START_TIME


def print_execution_time(start_time=START_TIME) -> None:
    """
    Prints the time it took to run a program after execution.

    Args:
        - start_time (float) : start time of the program (`start_time = time.time()`)

    Returns:
        - None
    """
    assert isinstance(start_time, float)
    exec_time = round(time.time() - start_time)

    ndays, remainder = divmod(exec_time, 86400)
    nhours, remainder = divmod(remainder, 3600)
    nminutes, nseconds = divmod(remainder, 60)

    print("\nProgram executed in", end=" ")

    if ndays:
        day_str = f"{ndays:.0f}"
        if ndays == 1:
            day_str += " day"
        else:
            day_str += " days"
        print(day_str, end=", ")

    if nhours:
        hour_str = f"{nhours:.0f}"
        if nhours == 1:
            hour_str += " hour"
        else:
            hour_str += " hours"
        print(hour_str, end=", ")

    if nminutes:
        minute_str = f"{nminutes:.0f}"
        if nminutes == 1:
            minute_str += " minute"
        else:
            minute_str += " minutes"
        print(minute_str, end=", ")

    second_str = f"{nseconds:.0f}"
    if nseconds == 1:
        second_str += " second"
    else:
        second_str += " seconds"
    print(second_str, end=".\n\n")
