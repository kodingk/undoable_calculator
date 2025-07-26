import time

class UndoableCalculator:
    __slots__ = ("_value", "_prev_value", "_start_time")

    def __init__(self, value):
        """
        초기값을 받아 계산기를 생성합니다.
        """
        self._value = value
        self._prev_value = None
        self._start_time = None

    def __add__(self, other):
        """
        덧셈 연산자 오버로딩
        UndoableCalculator끼리만 연산 가능
        """
        pass

    def __sub__(self, other):
        """
        뺄셈 연산자 오버로딩
        """
        pass

    def __mul__(self, other):
        """
        곱셈 연산자 오버로딩
        """
        pass

    def __truediv__(self, other):
        """
        나눗셈 연산자 오버로딩
        0으로 나누는 경우 예외 처리할 것
        """
        pass

    def undo(self):
        """
        직전 연산 이전 상태로 되돌립니다.
        되돌릴 상태가 없으면 아무 동작도 하지 않습니다.
        """
        pass

    def __hash__(self):
        """
        동일한 값의 인스턴스는 같은 해시값을 가지도록 합니다.
        """
        pass

    def __eq__(self, other):
        """
        값이 같으면 같은 객체로 간주합니다.
        """
        pass

    def __enter__(self):
        """
        with 문에 진입할 때 호출됩니다.
        시간 측정을 시작합니다.
        """
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        with 문을 벗어날 때 호출됩니다.
        시간 측정을 종료하고 경과 시간을 출력합니다.
        """
        pass

    @classmethod
    def from_expression(cls, expr):
        """
        선택 과제: 문자열 수식에서 계산기 인스턴스를 생성합니다.
        예: '3 + 4 * 2'
        """
        pass

    @property
    def value(self):
        """
        현재 값을 반환합니다.
        """
        return self._value
