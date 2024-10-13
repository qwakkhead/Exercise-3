class VowelConverter:
    def __init__(self, input_string):
        self.input_string = input_string
        self.vowels = "aeiouAEIOU"
        self.result = ""

    def convert_vowels(self):
        self.result = ''.join([char.upper() if char in self.vowels else char for char in self.input_string])

    def get_result(self):
        return self.result


input_string = str(input("Enter what's the word: "))

converter = VowelConverter(input_string)
converter.convert_vowels()
print(converter.get_result())
