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
        if not isinstance(other, UndoableCalculator):
            raise TypeError("UndoableCalculator끼리만 연산 가능합니다.")

        result = UndoableCalculator(self._value + other._value)
        result._prev_value = self._value
        return result

    def __sub__(self, other):
        """
        뺄셈 연산자 오버로딩
        """
        if not isinstance(other, UndoableCalculator):
            raise TypeError("UndoableCalculator끼리만 연산 가능합니다.")

        result = UndoableCalculator(self._value - other._value)
        result._prev_value = self._value
        return result

    def __mul__(self, other):
        """
        곱셈 연산자 오버로딩
        """
        if not isinstance(other, UndoableCalculator):
            raise TypeError("UndoableCalculator끼리만 연산 가능합니다.")

        result = UndoableCalculator(self._value * other._value)
        result._prev_value = self._value
        return result

    def __truediv__(self, other):
        """
        나눗셈 연산자 오버로딩
        0으로 나누는 경우 예외 처리할 것
        """
        if not isinstance(other, UndoableCalculator):
            raise TypeError("UndoableCalculator끼리만 연산 가능합니다.")

        if other._value == 0:
            raise ZeroDivisionError("0으로 나눌 수 없습니다.")

        result = UndoableCalculator(self._value / other._value)
        result._prev_value = self._value
        return result

    def undo(self):
        """
        직전 연산 이전 상태로 되돌립니다.
        되돌릴 상태가 없으면 아무 동작도 하지 않습니다.
        """
        if self._prev_value is not None:
            self._value = self._prev_value
            self._prev_value = None

    def __hash__(self):
        """
        동일한 값의 인스턴스는 같은 해시값을 가지도록 합니다.
        """
        return hash(self._value)

    def __eq__(self, other):
        """
        값이 같으면 같은 객체로 간주합니다.
        """
        if not isinstance(other, UndoableCalculator):
            return False
        return self._value == other._value

    def __enter__(self):
        """
        with 문에 진입할 때 호출됩니다.
        시간 측정을 시작합니다.
        """
        self._start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        with 문을 벗어날 때 호출됩니다.
        시간 측정을 종료하고 경과 시간을 출력합니다.
        """
        if self._start_time is not None:
            elapsed_time = time.time() - self._start_time
            print(f"실행 시간: {elapsed_time:.6f}초")
            self._start_time = None

    @classmethod
    def from_expression(cls, expr):
        """
        선택 과제: 문자열 수식에서 계산기 인스턴스를 생성합니다.
        예: '3 + 4 * 2'
        """
        # 간단한 수식 파서 구현
        # 공백 제거
        expr = expr.replace(" ", "")

        # 숫자와 연산자를 분리
        tokens = []
        current_number = ""

        for char in expr:
            if char.isdigit() or char == '.':
                current_number += char
            else:
                if current_number:
                    tokens.append(float(current_number))
                    current_number = ""
                tokens.append(char)

        if current_number:
            tokens.append(float(current_number))

        # 곱셈과 나눗셈을 먼저 처리 (연산자 우선순위)
        i = 1
        while i < len(tokens):
            if tokens[i] == '*':
                result = tokens[i-1] * tokens[i+1]
                tokens = tokens[:i-1] + [result] + tokens[i+2:]
            elif tokens[i] == '/':
                if tokens[i+1] == 0:
                    raise ZeroDivisionError("0으로 나눌 수 없습니다.")
                result = tokens[i-1] / tokens[i+1]
                tokens = tokens[:i-1] + [result] + tokens[i+2:]
            else:
                i += 2

        # 덧셈과 뺄셈 처리
        i = 1
        while i < len(tokens):
            if tokens[i] == '+':
                result = tokens[i-1] + tokens[i+1]
                tokens = tokens[:i-1] + [result] + tokens[i+2:]
            elif tokens[i] == '-':
                result = tokens[i-1] - tokens[i+1]
                tokens = tokens[:i-1] + [result] + tokens[i+2:]
            else:
                i += 2

        return cls(tokens[0])

    @property
    def value(self):
        """
        현재 값을 반환합니다.
        """
        return self._value
