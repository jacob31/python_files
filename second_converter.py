# file name: second_converter.py 
# by: Ben Silbernagel
# date: 6/6/2016
# class: Intro to Computer Science, by Udacity
# purpose: takes aurguement in seconds and returns a string in "hours, minutes, seconds"
# example: convert_seconds(3661) == "1 hour, 1 minute, 1 second"
# def convert_seconds(value):
#     return split_time(sec_split(value))

def convert_seconds(value):
    import math
    # converts from seconds to integer hours
    hours = int(math.floor(value / 3600))

    # converts the remaining seconds to integer minutes
    minutes = int(math.floor((value - (hours * 3600)) / 60))

    # gives the remaining seconds
    seconds = value - (hours * 3600) - (minutes * 60)

    # variables to replace verbage based on time interval
    verb_min = " minutes, "
    verb_hr = " hours, "
    verb_sec = " seconds"

    if minutes == 1:
        verb_min = " minute, "
    if hours == 1:
        verb_hr = " hour, "
    if seconds == 1:
        verb_sec = " second"
    return str(hours) + verb_hr + str(minutes) + verb_min + str(seconds) + verb_sec

def test_convert_seconds():
    test1 = "1 hour, 0 minutes, 0 seconds"
    test2 = "0 hours, 1 minute, 0 seconds"
    test3 = "0 hours, 0 minutes, 1 second"
    test4 = "0 hours, 0 minutes, 0 seconds"
    test5 = "1 hour, 1 minute, 1 second"
    test6 = "2 hours, 2 minutes, 2.2 seconds"
    assert convert_seconds(3600) == test1
    assert convert_seconds(60) == test2
    assert convert_seconds(1) == test3
    assert convert_seconds(0) == test4
    assert convert_seconds(3661) == test5
    assert convert_seconds(7322.2) == test6
    return "tests pass"

print(test_convert_seconds())
print(convert_seconds(3661.2))