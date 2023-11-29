from abc import ABC, abstractmethod


class BaseCalculate(ABC):
    @abstractmethod
    def _perform(self):
        ...

    def run(self):
        return self._perform()


class Logic(BaseCalculate):
    def __init__(self, query):
        self.left = query.left
        self.right = query.right
        self.sign = query.sign

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return "ZeroDivisionError"

    def _perform(self):
        out = getattr(self, self.sign, None)
        if out:
            return out(self.left, self.right)
        else:
            raise ValueError("Wrong sign")
