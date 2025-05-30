from utils import filter_even

def test_filter_even():
    assert filter_even([1, 2, 3, 4, 5]) == [2, 4]
    assert filter_even([1, 3, 5]) == []
    assert filter_even([]) == []
