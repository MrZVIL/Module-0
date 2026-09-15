"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


def mul(a: float, b: float) -> float:
    return a * b


def id(a):
    return a


def add(a: float, b: float) -> float:
    return a + b


def neg(a: float) -> float:
    return -a


def lt(first: float, second: float) -> bool:
    return first < second


def eq(first: float, second: float) -> bool:
    return first == second


def max(a: float, b: float) -> float:
    return a if a >= b else b


def is_close(a: float, b: float) -> bool:
    return abs(a - b) < 1e-2


def sigmoid(a: float) -> float:
    return 1.0 / (1.0 + math.exp(-a)) if a >= 0 else math.exp(a) / (1.0 + math.exp(a))


def relu(a: float) -> float:
    return a if a >= 0 else 0.


def log(a: float) -> float:
    return math.log(a)


def exp(a: float) -> float:
    return math.exp(a)


def inv(a: float) -> float:
    return 1.0 / a


def log_back(a: float, d: float) -> float:
    return d / a


def inv_back(a: float, d: float) -> float:
    return -d / (a * a)


def relu_back(a: float, d: float) -> float:
    return d if a > 0 else 0.0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


def map(iter: Iterable, func: Callable):
    for item in iter:
        yield func(item)


def zipWith(iter1: Iterable, iter2: Iterable, func: Callable):
    for item1, item2 in zip(iter1, iter2):
        yield func(item1, item2)


def reduce(iter: Iterable, func: Callable):
    is_first = True
    result = None
    for item in iter:
        if is_first:
            result = item
            is_first = False
        else:
            result = func(result, item)

    return result


def negList(a: list):
    return map(a, neg)


def addLists(a: list, b: list):
    return zipWith(a, b, add)


def sum(a: list):
    res = reduce(a, add)
    return res if res is not None else 0


def prod(a: list):
    res = reduce(a, mul)
    return res if res is not None else 1
