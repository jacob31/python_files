# file name: list_count.py 
# by: Ben Silbernagel
# date: 6/20/2016
# class: Intro to Computer Science, by Udacity
# purpose: counts the number of lists


# return a true if value is a list.
def is_list(p):
    return isinstance(p, list)

def deep_count_loop(lists):
    count = 0

    for i in lists:
        count += 1
        if is_list(i):
            count = count + deep_count(i)
    return count

def deep_count_recursion(p):
    count = 0

    if is_list(p) == False or p == []:
       return 0
    else:
        count = len(p)
        p = p[-1]
        return count + deep_count(p)

print deep_count([1, 2, 3])
#>>> 3

#The empty list still counts as an element of the outer list
print deep_count([1, [], 3])
#>>> 3

print deep_count([1, 3, 6, 10, 15, 21, [2, []]])
#>>> 9

print deep_count([[[[[[[[1, 2, 3]]]]]]]])
#>>> 10