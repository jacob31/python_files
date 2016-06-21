# file name: time_at_routers.py
# author: Ben Silbernagel
# created: 4/20/2016
# class: Intro to Computer Science, by Udacity
# purpose: verifies that the sudoku board is good

one_way = 2500.0 # kilometers in one direction
distance = one_way * 2
trace_route = 75 # milliseconds round trip
wire_speed = 200000 # km/s speed of data between routers
conversion_factor = 1000 # 1000 milliseconds in a second

def time_at_routers():
    wire_time = (distance / wire_speed) * conversion_factor
    print wire_time
    total_router_time = trace_route - wire_time
    return total_router_time

print time_at_routers()