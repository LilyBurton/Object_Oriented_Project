import math

class Diary:

    def __init__(self):
        self._entries = []

    def add(self, entry):
        self._entries.append(entry)

    def all_experiences(self):
        return self._entries
    
    def count_words(self):
        total = 0
        for word in self._entries:
            total += word.count_words()
        return total
    
    def reading_time(self, wpm):
        word_count = self.count_words()
        return math.ceil(word_count / wpm)
    
    