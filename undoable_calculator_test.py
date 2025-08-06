from undoable_calculator import UndoableCalculator


def test_addition():
    a = UndoableCalculator(10)
    b = UndoableCalculator(5)
    c = a + b
    assert isinstance(c, UndoableCalculator)
    assert c.value == 15
    assert a.value == 10  # 원본은 변하지 않아야 함
    assert b.value == 5


def test_subtraction():
    a = UndoableCalculator(10)
    b = UndoableCalculator(4)
    c = a - b
    assert c.value == 6


def test_multiplication():
    a = UndoableCalculator(3)
    b = UndoableCalculator(7)
    c = a * b
    assert c.value == 21


def test_division():
    a = UndoableCalculator(20)
    b = UndoableCalculator(4)
    c = a / b
    assert c.value == 5

    try:
        _ = a / UndoableCalculator(0)
        assert False, "ZeroDivisionError expected"
    except ZeroDivisionError:
        pass


def test_undo():
    a = UndoableCalculator(8)
    b = UndoableCalculator(2)
    c = a + b
    c.undo()
    assert c.value == 8  # 원래 a의 값

    # undo 이후 새로운 연산은 undo stack을 덮어씀
    d = c - b
    d.undo()
    assert d.value == 8


def test_hash_and_eq():
    a = UndoableCalculator(3)
    b = UndoableCalculator(3)
    c = UndoableCalculator(5)
    assert a == b
    assert hash(a) == hash(b)
    assert a != c
    assert len(set([a, b, c])) == 2


def test_context_manager():
    a = UndoableCalculator(100)
    with a as timer:
        for _ in range(100000):
            _ = timer + UndoableCalculator(1)
    assert isinstance(timer, UndoableCalculator)


def test_classmethod_expression():
    calc = UndoableCalculator.from_expression("3 + 4 * 2")
    assert isinstance(calc, UndoableCalculator)
    assert calc.value == 11  # if implemented with correct precedence


def run_all_tests():
    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()
    test_undo()
    test_hash_and_eq()
    test_context_manager()
    test_classmethod_expression()
    print("✅ 모든 테스트 통과!")


if __name__ == "__main__":
    run_all_tests()
