import random
candies = ["skittles", "twix", "circus peanuts", "toothbrush", "apple", "snickers", "hand sanitizer", "orange", "chocolate", "$1 bill"]
candy_count = []

for i in range(len(candies)):
    r = random.randint(1, 10)
    candy_count.append(r)

candy_sum = 0
for i in candy_count:
    candy_sum += i

for i in range(len(candies)):
    print(f"{candies[i]}: {candy_count[i]}")

print(f"Total number of candies: {candy_sum}")

# --- OPTIONAL EXTENSION ---
candy_sum = 0
for i in range(len(candies)):
    r = random.randint(1, 10)
    candy_count.append(r)
    candy_sum += candy_count[i]
    print(f"{candies[i]}: {candy_count[i]}")
print(f"Total number of candies: {candy_sum}")

# --- OPTIONAL EXTENSION ---
def output_halloween_haul(my_candy):
    candy_sum = 0
    for i in range(len(my_candy)):
        r = random.randint(1, 10)
        candy_count.append(r)
        candy_sum += candy_count[i]
        print(f"{my_candy[i]}: {candy_count[i]}")
    print(f"Total number of candies: {candy_sum}")
output_halloween_haul(["skittles", "twix", "circus peanuts", "toothbrush", "apple", "snickers", "hand sanitizer", "orange", "chocolate", "$1 bill"])
output_halloween_haul(["skittles", "twix", "circus peanuts", "toothbrush", "apple", "snickers", "hand sanitizer", "orange", "chocolate", "$1 bill", "Something"])
output_halloween_haul(["skittles", "twix", "circus peanuts", "toothbrush", "apple", "snickers", "hand sanitizer", "orange", "chocolate", "$1 bill", "candy1", "candy2"])



