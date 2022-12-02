# use a for loop to capitalize the first letter in a list of strings
def capitalize_first_letter(lst):
    ### solution:start
    return [i.capitalize() for i in lst]
    ### solution:end


# return sum of 2nd numbers (each number at index 1) in a 2d array
def sum_of_second_numbers(lst):
    ### solution:start
    return sum([i[1] for i in lst])
    ### solution:end


# remove duplicates in a list. preserve order
def remove_duplicates(lst):
    ### solution:start
    deduped = []
    [deduped.append(i) for i in lst if i not in deduped]
    return deduped
    ### solution:end


