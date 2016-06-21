# file name: execution_time.py 
# by: Ben Silbernagel
# date: 6/9/2016
# class: Intro to Computer Science, by Udacity
# purpose: calculates how long it takes to run some code.

def execution_time (code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time