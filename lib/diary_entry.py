class DiaryEntry:
    
    def __init__(self, title, content, number):
        self.title = title
        self.content = content
        self.number = number
        self._stop_off_point = 0

    def count_words(self):
        title_length = len(self.title.split())
        content_length = len(self.content.split())
        number_length = len(self.number.split())
        return title_length + content_length + number_length
    
    def reading_time(self, wpm):
        return len(self.content.split()) / wpm
    
    def reading_chunk(self, wpm, minutes):
        readable_chunks = wpm * minutes
        words = self.content.split()
        start_point = self._stop_off_point
        end_point = self._stop_off_point + readable_chunks
        readable_chunk = " ".join(words[start_point:end_point])
        self._stop_off_point += readable_chunks
        return readable_chunk
    
    

        