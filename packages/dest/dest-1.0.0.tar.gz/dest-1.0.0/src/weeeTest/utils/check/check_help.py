# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  check_log.py
@Description    :  
@CreateTime     :  2023/5/31 10:43
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/5/31 10:43
"""

from weeeTest.utils.check.check_log import log_failure


class Check:
    @staticmethod
    def assert_equal(a, b, msg=""):  # pragma: no cover
        assert a == b, msg

    @staticmethod
    def equal(a, b, msg=""):
        __tracebackhide__ = True
        if a == b:
            return True
        else:
            log_failure(f"check {a} == {b}", msg)
            return False

    @staticmethod
    def not_equal(a, b, msg=""):
        __tracebackhide__ = True
        if a != b:
            return True
        else:
            log_failure(f"check {a} != {b}", msg)
            return False

    @staticmethod
    def is_(a, b, msg=""):
        __tracebackhide__ = True
        if a is b:
            return True
        else:
            log_failure(f"check {a} is {b}", msg)
            return False

    @staticmethod
    def is_not(a, b, msg=""):
        __tracebackhide__ = True
        if a is not b:
            return True
        else:
            log_failure(f"check {a} is not {b}", msg)
            return False

    @staticmethod
    def is_true(x, msg=""):
        __tracebackhide__ = True
        if bool(x):
            return True
        else:
            log_failure(f"check bool({x})", msg)
            return False

    @staticmethod
    def is_false(x, msg=""):
        __tracebackhide__ = True
        if not bool(x):
            return True
        else:
            log_failure(f"check not bool({x})", msg)
            return False

    @staticmethod
    def is_none(x, msg=""):
        __tracebackhide__ = True
        if x is None:
            return True
        else:
            log_failure(f"check {x} is None", msg)
            return False

    @staticmethod
    def is_not_none(x, msg=""):
        __tracebackhide__ = True
        if x is not None:
            return True
        else:
            log_failure(f"check {x} is not None", msg)
            return False

    @staticmethod
    def is_in(a, b, msg=""):
        __tracebackhide__ = True
        if a in b:
            return True
        else:
            log_failure(f"check {a} in {b}", msg)
            return False

    @staticmethod
    def is_not_in(a, b, msg=""):
        __tracebackhide__ = True
        if a not in b:
            return True
        else:
            log_failure(f"check {a} not in {b}", msg)
            return False

    @staticmethod
    def is_instance(a, b, msg=""):
        __tracebackhide__ = True
        if isinstance(a, b):
            return True
        else:
            log_failure(f"check isinstance({a}, {b})", msg)
            return False

    @staticmethod
    def is_not_instance(a, b, msg=""):
        __tracebackhide__ = True
        if not isinstance(a, b):
            return True
        else:
            log_failure(f"check not isinstance({a}, {b})", msg)
            return False

    @staticmethod
    def greater(a, b, msg=""):
        __tracebackhide__ = True
        if a > b:
            return True
        else:
            log_failure(f"check {a} > {b}", msg)
            return False

    @staticmethod
    def greater_equal(a, b, msg=""):
        __tracebackhide__ = True
        if a >= b:
            return True
        else:
            log_failure(f"check {a} >= {b}", msg)
            return False

    @staticmethod
    def less(a, b, msg=""):
        __tracebackhide__ = True
        if a < b:
            return True
        else:
            log_failure(f"check {a} < {b}", msg)
            return False

    @staticmethod
    def less_equal(a, b, msg=""):
        __tracebackhide__ = True
        if a <= b:
            return True
        else:
            log_failure(f"check {a} <= {b}", msg)
            return False

    @staticmethod
    def between(b, a, c, msg="", ge=False, le=False):
        __tracebackhide__ = True
        if ge and le:
            if a <= b <= c:
                return True
            else:
                log_failure(f"check {a} <= {b} <= {c}", msg)
                return False
        elif ge:
            if a <= b < c:
                return True
            else:
                log_failure(f"check {a} <= {b} < {c}", msg)
                return False
        elif le:
            if a < b <= c:
                return True
            else:
                log_failure(f"check {a} < {b} <= {c}", msg)
                return False
        else:
            if a < b < c:
                return True
            else:
                log_failure(f"check {a} < {b} < {c}", msg)
                return False


check = Check()
if __name__ == '__main__':
    check.equal(1, 2, "1不等于2")
    check.equal(1, 3)
    check.equal(1, 1)
