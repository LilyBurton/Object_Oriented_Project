As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

"""
Adding a list of experiences into a diary
"""

lib/diary.py

class Diary:
    self.entries = []

    def add(self, entry):
        self.entries.append(entry)
"""
Return a list of past experiences
"""
    def all_experiences(self):
        return self.experiences

"""
Return integer of how many words they can read per minute.
"""
    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("Cannot calculate reading time with wpm 0.")
        experience_words = len(self.experiences.split())
        return experience_words / wpm 

"""
Return string of the chunk based on their wpm and minutes
"""

def reading_chunk(self, wpm, minutes):
        readable_chunks = wpm * minutes
        words = self.experiences.split()
        start_point = self._stop_off_point
        end_point = self._stop_off_point + readable_chunks
        readable_chunk = " ".join(words[start_point:end_point])
        self._stop_off_point += readable_chunks
        return readable_chunk

lib/task_list.py

class TaskList
    self.tasks = []

def add(self, task):
    self.tasks.append(task)

def all(self):
    return self.tasks

def numbers(self)
    return [num for num in self.entries if num.number]
