# add 1 to all numbers in a list
def add_one(lst):
    ### solution:start
    return [i + 1 for i in lst]
    ### solution:end

# sum all numbers in a list
def get_sum(lst):
    ### solution:start
    return sum(lst)
    ### solution:end


# return last item in a list
def get_last(lst):
    ### solution:start
    return lst[-1]
    ### solution:end


# return True if all items are truthy
def all_truthy(lst):
    ### solution:start
    return all(lst)
    ### solution:end



# reverse a list
def reverse_list(lst):
    ### solution:start
    return lst[::-1]
    ### solution:end


# return the biggest number in a list
def biggest_number(lst):
    ### solution:start
    return max(lst)
    ### solution:end


# insert an item to index 0
def insert_at_zero(lst, item):
    ### solution:start
    lst.insert(0, item)
    return lst
    ### solution:end

