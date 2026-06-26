from pricing import apply_discount

def test_ten_percent_off_100_is_90():
    assert apply_discount(100, 10) == 90
