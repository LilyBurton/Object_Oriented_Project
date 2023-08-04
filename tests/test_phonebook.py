from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.phone_number_extractor import PhoneNumberExtractor

def test_extract_phone_numbers():
    diary_entry = Diary()
    diary_entry_1 = DiaryEntry("My Title", "A Contents", "07777777777")
    diary_entry_2 = DiaryEntry("My Title 1", "A Contents 2", "07999999999")
    diary_entry.add(diary_entry_1)
    diary_entry.add(diary_entry_2)
    extractor = PhoneNumberExtractor(diary_entry)
    assert extractor.extract() == ["07777777777", "07999999999"]