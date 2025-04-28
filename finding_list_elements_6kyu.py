"""
Write a function that takes an array of numbers (integers for the tests) and a target number. 
It should find two different items in the array that, when added together, 
give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: 
(index1, index2).

"""

def two_sum(numbers, target):
    for i, v1 in enumerate(numbers):
        for j, v2 in enumerate(numbers):
            if v1+v2 == target and i != j:
                return (i, j)

if __name__ == '__main__':

    print(two_sum([1 ,2, 3], 4))