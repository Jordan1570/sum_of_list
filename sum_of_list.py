# Find sum of list
# I know there's a sum method lol

def find_sum(list_of_nums):

    # set the value 0 as the intial sum
    sum_of_list = 0
    
    for num in list_of_nums:
        sum_of_list += num

    return sum_of_list

list_sum = find_sum([8, 2, 3, 0, 7])

print(f'The sum of the list is {list_sum}')

