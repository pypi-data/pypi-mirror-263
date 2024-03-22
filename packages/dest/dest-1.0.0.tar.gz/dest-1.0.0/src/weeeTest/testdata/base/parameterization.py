# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  parameterization.py
@Description    :  
@CreateTime     :  2023/4/25 13:03
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/4/25 13:03
"""
import inspect
from functools import wraps

from parameterized.parameterized import short_repr, to_text, QuietOrderedDict, getargspec, lzip, param

from weeeTest import mark


def default_doc_func(func, num, p):
    if func.__doc__ is None:
        return None

    all_args_with_values = parameterized_argument_value_pairs(func, p)

    # Assumes that the function passed is a bound method.
    descs = ["%s=%s" % (n, short_repr(v)) for n, v in all_args_with_values]

    # The documentation might be a multiline string, so split it
    # and just work with the first string, ignoring the period
    # at the end if there is one.
    first, nl, rest = func.__doc__.lstrip().partition("\n")
    suffix = ""
    if first.endswith("."):
        suffix = "."
        first = first[:-1]
    args = "\n%s [with %s]" % (len(first) and " " or "", ", ".join(descs))
    return "".join(
        to_text(x)
        for x in [first.rstrip(), args, suffix, nl, rest]
    )


def default_name_func(func, num, p):
    base_name = func.__name__
    name_suffix = []
    all_args_with_values = parameterized_argument_value_pairs(func, p)

    if len(all_args_with_values) > 0:
        name_suffix.append(
            "-".join(
                short_repr(v)
                for n, v in all_args_with_values
            )
        )
    value_parts = name_suffix[0].replace("'", "").split("-")  # 去掉单引号并将字符串按 "-" 分割
    joined_str = ["-".join(value_parts)]  # 将分割后的字符串重新拼接
    return f"{base_name}{joined_str}"


def parameterized_argument_value_pairs(func, p):
    argspec = getargspec(func)
    arg_offset = 1 if argspec.args[:1] == ["self"] else 0

    named_args = argspec.args[arg_offset:][-len(p.args):]

    result = lzip(named_args, p.args)
    named_args = argspec.args[len(result) + arg_offset:]
    varargs = p.args[len(result):]

    result.extend([
        (name, p.kwargs.get(name, default))
        for (name, default)
        in zip(named_args, argspec.defaults or [])
    ])

    seen_arg_names = set([n for (n, _) in result])
    keywords = QuietOrderedDict(sorted([
        (name, p.kwargs[name])
        for name in p.kwargs
        if name not in seen_arg_names
    ]))

    if varargs:
        result.append(("*%s" % (argspec.varargs,), tuple(varargs)))

    if keywords:
        result.append(("**%s" % (argspec.keywords,), keywords))

    return result


_test_runner_override = None
_test_runner_guess = False
_test_runners = {"unittest", "unittest2", "nose", "nose2", "pytest"}
_test_runner_aliases = {
    "_pytest": "pytest",
}


class parameterized(object):
    """ Parameterize a test case::

            class TestInt(object):
                @parameterized([
                    ("A", 10),
                    ("F", 15),
                    param("10", 42, base=42)
                ])
                def test_int(self, input, expected, base=16):
                    actual = int(input, base=base)
                    assert_equal(actual, expected)

            @parameterized([
                (2, 3, 5)
                (3, 5, 8),
            ])
            def test_add(a, b, expected):
                assert_equal(a + b, expected)
        """

    @classmethod
    def input_as_callable(cls, input):
        if callable(input):
            return lambda: cls.check_input_values(input())
        input_values = cls.check_input_values(input)
        return lambda: input_values

    @classmethod
    def check_input_values(cls, input_values):
        # Explicitly convery non-list inputs to a list so that:
        # 1. A helpful exception will be raised if they aren't iterable, and
        # 2. Generators are unwrapped exactly once (otherwise `nosetests
        #    --processes=n` has issues; see:
        #    https://github.com/wolever/nose-parameterized/pull/31)
        if not isinstance(input_values, list):
            input_values = list(input_values)
        return [param.from_decorator(p) for p in input_values]

    @classmethod
    def param_as_standalone_func(cls, p, func, name):
        if inspect.iscoroutinefunction(func):
            @wraps(func)
            async def standalone_func(*a, **kw):
                return await func(*(a + p.args), **p.kwargs, **kw)
        else:
            @wraps(func)
            def standalone_func(*a, **kw):
                return func(*(a + p.args), **p.kwargs, **kw)

        standalone_func.__name__ = name

        # place_as is used by py.test to determine what source file should be
        # used for this test.
        standalone_func.place_as = func

        # Remove __wrapped__ because py.test will try to look at __wrapped__
        # to determine which parameters should be used with this test case,
        # and obviously we don't need it to do any parameterization.
        try:
            del standalone_func.__wrapped__
        except AttributeError:
            pass
        return standalone_func

    @classmethod
    def param_as_standalone_func_attrs(cls, p, func, name, attrs):
        if inspect.iscoroutinefunction(func):
            @wraps(func)
            async def standalone_func(*a, **kw):
                return mark.parametrize(attrs, p.args)
                # return await func(*(a + p.args), **p.kwargs, **kw)
        else:
            @wraps(func)
            def standalone_func(*a, **kw):
                return mark.parametrize(attrs, p.args)
                # return func(*(a + p.args), **p.kwargs, **kw)

        standalone_func.__name__ = name

        # place_as is used by py.test to determine what source file should be
        # used for this test.
        standalone_func.place_as = func

        # Remove __wrapped__ because py.test will try to look at __wrapped__
        # to determine which parameters should be used with this test case,
        # and obviously we don't need it to do any parameterization.
        try:
            del standalone_func.__wrapped__
        except AttributeError:
            pass
        return standalone_func
