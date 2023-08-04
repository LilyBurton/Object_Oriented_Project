from lib.diary_entry import DiaryEntry

def test_contrust_entry_to_get_title_and_contents():
    diary_entry = DiaryEntry("Title", "A Contents", "A number")
    assert diary_entry.title == "Title"
    assert diary_entry.content == "A Contents"
    assert diary_entry.number == "A number"

def test_count_words_in_entry():
    diary_entry = DiaryEntry("My Title", "A Contents", "A number")
    assert diary_entry.count_words() == 6

def test_entries_reading_time():
    diary_entry = DiaryEntry("My Title", "A Contents", "A number")
    assert diary_entry.reading_time(2) == 1

def test_reading_chunk():
    diary_entry = DiaryEntry("My Title", "A Contents", "A number")
    assert diary_entry.reading_chunk(2, 1) == "A Contents"

def test_reading_chunk_second_half():
    diary_entry = DiaryEntry("My Title", "A Contents 32", "A number")
    assert diary_entry.reading_chunk(2, 1) == "A Contents"
    assert diary_entry.reading_chunk(2, 1) == "32"


