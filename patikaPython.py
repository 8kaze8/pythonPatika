def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item)) 
        else:
            flat_list.append(item)
    return flat_list

input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
print(flatten(input_list))

def reverse_nested(lst):
    lst.reverse()  
    for item in lst:
        if isinstance(item, list):
            reverse_nested(item)  

nested_list = [[1, 2], [3, 4], [5, 6, 7]]
reverse_nested(nested_list)
print(nested_list)