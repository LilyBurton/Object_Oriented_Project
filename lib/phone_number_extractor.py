import re

class PhoneNumberExtractor:

    def __init__(self, diary):
        self._diary = diary

    def extract(self):
        phone_numbers = []
        for num in self._diary.all_experiences():
            numbers = num.number
            phone_numbers += re.findall(r"0[0-9]{10}", numbers)
        return phone_numbers


