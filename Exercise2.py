list1 = [1, 2, 3]
list2 = ["mark", "alice", "john"]
list_of_tuple = []

for i in range(len(list1)):
    list_of_tuple.append((list1[i], list2[i]))

print(list_of_tuple)  
