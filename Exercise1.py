class NumberProcessor:
    def __init__(self, numbers):
        self.numbers = numbers
        self.results = []

    def process_numbers(self):
        for x in self.numbers:
            if x % 2 != 0:
                self.results.append(x ** 2)

    def get_results(self):
        return self.results


processor1 = NumberProcessor([2, 4, 3])
processor1.process_numbers()
print(processor1.get_results())

processor2 = NumberProcessor([0, 0, 1, 1])
processor2.process_numbers()
print(processor2.get_results())
