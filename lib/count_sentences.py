class MyString:
    def __init__(self, value: str = ''):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value: str):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            raise ValueError("Value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Replace multiple punctuation with a single one and split the string
        import re
        # This regex finds '.', '!', or '?' and considers them as sentence endings
        sentences = re.split(r'[.!?]+', self.value)
        # Filter out any empty strings from the result
        return len([s for s in sentences if s.strip()])

# Example usage:
my_string = MyString("This is a string! It has three sentences. Right?")
print(my_string.count_sentences())  # Output: 3
