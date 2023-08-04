from lib.diary import Diary
from lib.diary_entry import DiaryEntry

def test_diary_adding_entries_to_list():
    diary_entry = Diary()
    diary_entry_1 = DiaryEntry("My Title", "A Contents", "A number")
    diary_entry_2 = DiaryEntry("My Title 1", "My Contents 2", "A number 3")
    diary_entry.add(diary_entry_1)
    diary_entry.add(diary_entry_2)
    assert diary_entry.all_experiences() == [diary_entry_1, diary_entry_2]

def test_count_words_entries():
    diary_entry = Diary()
    diary_entry_1 = DiaryEntry("My Title", "A Contents", "A number")
    diary_entry_2 = DiaryEntry("My Title 1", "My Contents 2", "A number 3")
    diary_entry.add(diary_entry_1)
    diary_entry.add(diary_entry_2)
    assert diary_entry.count_words() == 15

def test_returns_reading_time_from_entries():
    diary_entry = Diary()
    diary_entry_1 = DiaryEntry("My Title", "A Contents", "A number")
    diary_entry_2 = DiaryEntry("My Title 1", "A Contents 2", "A number 3")
    diary_entry.add(diary_entry_1)
    diary_entry.add(diary_entry_2)
    assert diary_entry.reading_time(5) == 3

