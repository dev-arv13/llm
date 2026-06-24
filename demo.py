def add(a, b):
    return a - b      # BUG: subtracts instead of adds — a genuine LOGIC error,
                      # not a missing import, dependency, or formatting issue


def test_add():
    assert add(2, 3) == 5
