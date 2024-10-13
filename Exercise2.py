class Tuple_creator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
        self.tuple_list = []

    def create_tuples(self):
        for i in range(len(self.list1)):
            self.tuple_list.append((self.list1[i], self.list2[i]))

    def get_tuples(self):
        return self.tuple_list

list1 = [1, 2, 3]
list2 = ["mark", "alice", "john"]

creator = Tuple_creator(list1, list2)
creator.create_tuples()
print(creator.get_tuples())
