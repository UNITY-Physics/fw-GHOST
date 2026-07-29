from utils.parser import make_session_label


class FakeSession:
    def __init__(self, label):
        self.label = label


def test_space_separated_datetime_preserves_time():
    label = make_session_label(FakeSession("2026-07-28 09:09:58"))
    assert label == "20260728090958"


def test_underscore_separated_datetime_preserves_time():
    label = make_session_label(FakeSession("2026-06-24_09_09_58"))
    assert label == "20260624090958"


def test_same_day_different_times_are_distinct():
    label_a = make_session_label(FakeSession("2026-07-28 09:09:58"))
    label_b = make_session_label(FakeSession("2026-07-28 14:30:00"))
    assert label_a != label_b


def test_date_only_label_falls_back_gracefully():
    label = make_session_label(FakeSession("2026-07-28"))
    assert label == "20260728"


def test_output_is_alphanumeric_only():
    label = make_session_label(FakeSession("2026-06-24_09_09_58"))
    assert label.isalnum()
