import pytest
from calc import Logic
from models import CalcQuery


def test_model():
    query = {"left": 1, "right": 1, "sign": "add"}

    out = CalcQuery(**query)
    assert out.left == query["left"]
    assert out.right == query["right"]
    assert out.sign == query["sign"]


def test_add():
    query = {"left": 1, "right": 1, "sign": "add"}
    out = Logic(CalcQuery(**query)).run()
    assert out == 2


def test_sub():
    query = {"left": 1, "right": 1, "sign": "sub"}
    out = Logic(CalcQuery(**query)).run()
    assert out == 0


def test_mul():
    query = {"left": 2, "right": 2, "sign": "mul"}
    out = Logic(CalcQuery(**query)).run()
    assert out == 4


def test_div():
    query = {"left": 6, "right": 2, "sign": "div"}
    out = Logic(CalcQuery(**query)).run()
    assert out == 3


def test_div_zero():
    query = {"left": 6, "right": 0, "sign": "div"}

    out = Logic(CalcQuery(**query)).run()
    assert out == "ZeroDivisionError"
