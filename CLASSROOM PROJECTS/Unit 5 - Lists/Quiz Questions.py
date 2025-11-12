my_list = []
my_list.append(20)
my_list.append(30)
my_list.insert(0, 10)
my_list.append(43)
my_list.remove(43)
my_list.pop(1)

print(my_list)

my_list = [3, 6, 9, 12, 15, 18, 21]
print(my_list[2] + my_list[1])
print(my_list[2 + 1])

my_list = [3, 6, 9, 12, 15, 18, 21]
my_list[3] = 24
my_list[6] = 27
my_list[2] = 30
print(my_list)

my_list = []
for x in range(5):
    my_list.append(x + 3)

