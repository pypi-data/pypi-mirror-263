import numpy as np
from polars import Expr, Series
from polars import reduce, max_horizontal, sum_horizontal, min_horizontal, Int64


def abs_(x: Expr) -> Expr:
    if isinstance(x, (Expr, Series)):
        return x.abs()
    else:
        return np.abs(x)


def add(a: Expr, b: Expr, *args, filter_: bool = False) -> Expr:
    """Add all inputs (at least 2 inputs required). If filter = true, filter all input NaN to 0 before adding"""
    _args = [a, b] + list(args)

    if filter_:
        return sum_horizontal(*_args)

    return reduce(function=lambda acc, x: acc + x, exprs=_args)


def arc_cos(x: Expr) -> Expr:
    """If -1 <= x <= 1: arccos(x); else NaN"""
    return x.arccos()


def arc_sin(x: Expr) -> Expr:
    """If -1 <= x <= 1: arcsin(x); else NaN"""
    return x.arcsin()


def arc_tan(x: Expr) -> Expr:
    """This operator does inverse tangent of input. """
    return x.arctan()


def ceiling(x: Expr) -> Expr:
    return x.ceil()


def cos(x: Expr) -> Expr:
    return x.cos()


def cosh(x: Expr) -> Expr:
    return x.cosh()


def densify(x: Expr) -> Expr:
    raise


def divide(x: Expr, y: Expr) -> Expr:
    return x / y


def exp(x: Expr) -> Expr:
    return x.exp()


def expm1(x: Expr) -> Expr:
    """convert log return to simple return
    对数收益率 转 简单收益率"""
    return x.exp() - 1


def floor(x: Expr) -> Expr:
    return x.floor()


def fraction(x: Expr) -> Expr:
    """This operator removes the whole number part and returns the remaining fraction part with sign."""
    # return sign(x) * (abs(x) - floor(abs(x)))
    # return x.sign() * (x.abs() % 1)
    return x % 1


def inverse(x: Expr) -> Expr:
    """1 / x"""
    return 1 / x


def log(x: Expr) -> Expr:
    if isinstance(x, (Expr, Series)):
        return x.log()
    else:
        return np.log(x)


def log10(x: Expr) -> Expr:
    return x.log10()


def log1p(x: Expr) -> Expr:
    """convert simple return to log return
    简单收益率 转 对数收益率"""
    return x.log1p()


def max_(a: Expr, b: Expr, *args) -> Expr:
    """Maximum value of all inputs. At least 2 inputs are required."""
    _args = [a, b] + list(args)
    return max_horizontal(*_args)


def mean(a: Expr, b: Expr, *args) -> Expr:
    _args = [a, b] + list(args)
    return sum_horizontal(*_args) / len(_args)


def min_(a: Expr, b: Expr, *args) -> Expr:
    """Maximum value of all inputs. At least 2 inputs are required."""
    _args = [a, b] + list(args)
    return min_horizontal(*_args)


def mod(x: Expr, y: Expr) -> Expr:
    return x % y


def multiply(a: Expr, b: Expr, *args, filter_: bool = False) -> Expr:
    """Multiply all inputs. At least 2 inputs are required. Filter sets the NaN values to 1"""
    _args = [a, b] + list(args)
    if filter_:
        _args = [_.fill_null(1) for _ in args]

    return reduce(function=lambda acc, x: acc * x, exprs=_args)


def power(x: Expr, y: Expr) -> Expr:
    """x ^ y"""
    return x.pow(y)


def reverse(x: Expr) -> Expr:
    """- x"""
    return -x


def round_(x: Expr, decimals: int = 0) -> Expr:
    """Round input to closest integer."""
    return x.round(decimals)


def round_down(x: Expr, f: int = 1) -> Expr:
    """Round input to greatest multiple of f less than input;"""
    if f == 1:
        return x // 1
    else:
        return x // f * f


def s_log_1p(x: Expr) -> Expr:
    return x.abs().log1p() * x.sign()


def sign(x: Expr) -> Expr:
    if isinstance(x, (Expr, Series)):
        return x.sign()
    else:
        return np.sign(x)


def signed_power(x: Expr, y: Expr) -> Expr:
    """x raised to the power of y such that final result preserves sign of x."""
    if isinstance(y, (int, float)):
        if y == 1:
            return x.abs() * x.sign()
        elif y == 0:
            return x.sign()

    return x.abs().pow(y) * x.sign()


def sin(x: Expr) -> Expr:
    return x.sin()


def sinh(x: Expr) -> Expr:
    return x.sinh()


def sqrt(x: Expr) -> Expr:
    return x.sqrt()


def subtract(a: Expr, b: Expr, *args, filter_: bool = False) -> Expr:
    """x-y. If filter = true, filter all input NaN to 0 before subtracting"""
    _args = [a, b] + list(args)
    if filter_:
        _args = [_.fill_null(0) for _ in _args]

    return reduce(function=lambda acc, x: acc - x, exprs=_args)


def tan(x: Expr) -> Expr:
    return x.tan()


def tanh(x: Expr) -> Expr:
    """Hyperbolic tangent of x"""
    return x.tanh()


def truncate(x: Expr) -> Expr:
    """truncate towards zero
    向零取整"""
    return x.cast(Int64)
