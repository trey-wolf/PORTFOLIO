# For a linear search we simply want to loop through every element in the list
# 1. Create a variable called `index` that starts at 0
# 2a. Create a for loop that iterates through our list `l`
# 2b. Name the variable for the for loop `item`
# 3a. In the for loop create an if statement that checks if `item` is equal to `value`
# 3b. If that is True return the variable `index`
# 3c. If not, increase `index` by 1
# 4. After the loop return the value -1
#    We do this in case `value` is not in the list at all
# Parameters: Value -> The element you are looking for
#             l -----> The name of an unsorted list
def linear_search(value, l):
    index = 0
    for item in l:
        if item == value:
            return index
        else:
            index += 1
    return -1

# TEST CASES FOR LINEAR SEARCH
print(linear_search(4, [1,2,3,4]))
print(linear_search(13, [5, 18, 13, 16, 12, 100]))
print(linear_search(0, [5, 18, 13, 16, 12, 100]))
# For a binary search we are going to want to follow a 7-step process
# 1. Sort the list `l`
# 2. Create two variables called `low` and `high`
#    `low` will start off at 0 (the first index in the list)
#    `high` will start off at length of our now sorted list `l` minus 1 (the last index in the list)
# 3. We are going to have a while loop that will continue to loop as long as `low` <= `high`
# 4a. As we loop, we want to calculate the middle index between `high` and `low`, we will store this in a variable, `mid`
# 4b. We can do this by simply taking the average between `high` and `low` (convert to an integer)
# 5. Check to see if the element at index `mid` is less than, greater than, or equal to `value` using an if statement
# 6a. if the element at index `mid` (aka: l[mid]) is less than `value` we want to update `low` to be `mid + 1`
# 6b. if the element at index `mid` (aka: l[mid]) is greater than `value` we want to update `high` to be `mid - 1`
# 6c. otherwise, we have found the value! Therefore, return `mid`
# 7. Lastly, after the while loop, if we did not find the value and the loop finishes, we return -1
#    This represents the case where we did not find the index of `value`

# Parameters: Value -> The thing you are looking for
#             l -----> The name of an unsorted list
def binary_search(value, l):
    l.sort()
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] < value:
            low = mid + 1
        elif l[mid] > value:
            high = mid - 1
        else:
            return mid
    return -1



# TEST CASES FOR BINARY SEARCH
print(binary_search(4, [1,2,3,4]))
print(binary_search(13, [5, 18, 13, 16, 12, 100]))
print(binary_search(0, [5, 18, 13, 16, 12, 100]))

by_three = [3, 6, 9, 12, 15, 18]
by_two   = [2, 4, 6, 8, 10, 12]
count = 0

for x in range(6):
    if by_three[x] in by_two:
        count += 1
print(count)

scores = [45, 90, 81, 77, 12]
scores[3] = 40
scores[0] = 51
print(scores)

nums = [4, 5, 6, 8, 9, 5, 6, 2]
print(nums[5 - 2])
print(nums[5] - nums[2])