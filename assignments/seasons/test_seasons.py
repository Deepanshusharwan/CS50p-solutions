import seasons


def test_age_in_words():
    assert seasons.age_in_word(22540860) == "Twenty-two million, five hundred forty thousand, eight hundred sixty minutes"
