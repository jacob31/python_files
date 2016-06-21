# file name: download_calc.py 
# by: Ben Silbernagel
# date: 6/7/2016
# class: Intro to Computer Science, by Udacity
# purpose: this is used to calculate download speeds

dictionary = {
    'kb': 2 ** 10 * 1.0,
    'kB': 2 ** 10 * 8 * 1.0,
    'Mb': 2 ** 20 * 1.0,
    'MB': 2 ** 20 * 8 * 1.0,
    'Gb': 2 ** 30 * 1.0,
    'GB': 2 ** 30 * 8 * 1.0,
    'Tb': 2 ** 40 * 1.0,
    'TB': 2 ** 40 * 8 * 1.0}

def convert_seconds(value):
    import math
    min_hr = 60 # converts between minutes and hours
    sec_min = 60 # converts between seconds and minutes

    hours = int(math.floor((value / sec_min) / min_hr))
    minutes = int(math.floor((value - (hours * min_hr * sec_min)) / sec_min))
    seconds = value - (hours * min_hr * sec_min) - (minutes * sec_min)

    # Changes verbage used in return string.
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

def download_time(v1, ty1, v2, ty2):
    scnds = v1 * dictionary[ty1] / (v2 * dictionary[ty2])
    return convert_seconds(scnds)

def test_dt():
    assert download_time(1024,'kB', 1, 'MB') ==  "0 hours, 0 minutes, 1.0 second"
    assert download_time(1024,'kB', 1, 'Mb') ==  "0 hours, 0 minutes, 8.0 seconds"
    assert download_time(13,'GB', 5.6, 'MB') == "0 hours, 39 minutes, 37.1428571429 seconds"
    assert download_time(13,'GB', 5.6, 'Mb') == "5 hours, 16 minutes, 57.1428571429 seconds"
    assert download_time(10,'MB', 2, 'kB') == "1 hour, 25 minutes, 20.0 seconds"
    assert download_time(10,'MB', 2, 'kb') == "11 hours, 22 minutes, 40.0 seconds"
    return "passed tests"

print(test_dt())
