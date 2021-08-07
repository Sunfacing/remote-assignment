"""
Assignment 4: Data Manipulation (Python)
Complete the following functions by Python
1. count: return an object which shows the count of each characters.
2. group_by_key: return an object which shows the summed up value of each keys.

Note:
1. The input format is different for these two functions.
2. In the second function, the input may have same key but different values, the output 
should have each key only once.
"""



def count(input):
    dict = {}
    for ch in input:
        if ch not in dict:
            dict[ch] = 1
        else:
            dict[ch] += 1
    return dict


input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}




def group_by_key(input):
    dict = {}
    for i in range(len(input)):
        key = input[i]['key']
        value = input[i]['value']
        if key not in dict.keys():
            dict[key] = value
        else:
            dict[key] += value
    return dict


input2 = [
 {'key': 'a', 'value': 3},
 {'key': 'b', 'value': 1},
 {'key': 'c', 'value': 2},
 {'key': 'a', 'value': 3},
 {'key': 'c', 'value': 5}
]
print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}
