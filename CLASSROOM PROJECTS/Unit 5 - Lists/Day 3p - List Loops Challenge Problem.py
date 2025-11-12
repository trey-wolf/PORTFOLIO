# Challenge Problem
# 1. Create lists
#    Create a list of 10 different candies you want from trick-or-treating called, 'candies'
#    Create another empty list called 'candy_count'

# 2. Use a for loop, that will loop the length of your list 'candies'
#    As we are looping generate a random number between 1 and 10 and store it in a variable called 'r'
#    then append this number on to the end of candy_count

# 3. Lists we currently have (There is nothing to do here, just to make the observation)
#    we now have two lists 'candies' and 'candy_count' that are the same size, 10 elements
#    So the first candy in 'candies' is equal to the number of candies you received that was recorded in 'candy_count'
#    :for example:
#    candies = ["Snickers", "Twix", "Sweedish Fish", etc.]
#    candy_count = [8, 4, 10, etc.]

# 4. Calculate the total number of candies you have
#    using a for each loop, loop through all your candy counts and add them together
#    store this sum into a variable called 'candy_sum'

# 5. Print your haul
#    using a for loop, loop through the length of your 'candies' list
#    using an f-string, print out each element of your candies along with the respective candy count
#    Hint: the loop variable represents the current element in the list (typically called i)

# 6. Print your total
#    using a simple f-string print statement, print out the total

# 7. Modify your information
#    if you setup your code well, add 3 more candies to your 'candies' list
#    You don't need to use append here, just go back up to the top of your code and add more candies in the list
#    the program should work the same without having to change any other information

# --- OPTIONAL EXTENSIONS ---
# In the way that this problem is represented, we end up with 3 separate for loops.
# This is wildly inefficient, is there a way to combine all the for loops together as one loop?
# Hint: There is a way, try to do it.

# Refactor your code as a function.
# This function can take in a list as a parameter and simply print out the messages from sections 5 and 6