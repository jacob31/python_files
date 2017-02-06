import itertools

''' 
    Input / Checks:
    get's input and cleans input for functions 
'''
input_data = str(input('> '))

input_check = int(input_data[-1])
input_id = input_data[0:-1]

id_list = list(input_id)

# input reversed for gen_num function
def rev_list(id_list):
    answer = ""
    for c in reversed(id_list):
            answer = answer + c
    return answer

# takes every other digit and multiplies it by 2 and then rejoins 

def gen_list(i_list):
    o_list = []
    # seperates numbers in the list for math manipulation.
    # every other number from the right gets doubled 
    for idx, val in enumerate(i_list):
        if idx % 2 == 0:
            o_list.append(str(int(val) * 2))
        else:
            o_list.append(val)
    
    return list(filter(None.__ne__, o_list))

# puts the list back into a single string of numbers
def join_list(i_list):
    return ''.join(i_list)

# takes each individual number and adds the all together
def sum_list(ilist):
    o_int = 0

    for item in ilist:
        o_int = o_int + int(item)
    
    return o_int


id_sum = sum_list(join_list(gen_list(rev_list(id_list))))

check = lambda total, check: "Valid id" if (10 - (total % 10)) == check else "*** Invalid id ***"

print(check(id_sum, input_check))