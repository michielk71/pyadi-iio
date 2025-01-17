import sys
from test.globals import *

import iio

import adi
import numpy as np
import pytest


def pytest_configure(config):
    # Add customer marks to ini to remove warnings
    from test import test_map as tm

    test_map = tm.get_test_map()
    vals = []
    for k in test_map:
        vals = vals + test_map[k]
    keys = np.unique(np.array(vals))
    for k in keys:
        config.addinivalue_line("markers", k.replace("-", "_"))


def pytest_collection_modifyitems(items):
    # Map HDL project names to tests as markers
    from test import test_map as tm

    test_map = tm.get_test_map()
    test_map_keys = test_map.keys()

    for item in items:
        if item.originalname:
            for key in test_map_keys:
                if key in item.originalname:
                    for marker in test_map[key]:
                        item.add_marker(marker.replace("-", "_"))
                    break


def pytest_addoption(parser):
    parser.addoption(
        "--username", default="root", help="SSH login username",
    )
    parser.addoption(
        "--password", default="analog", help="SSH login password",
    )


def pytest_generate_tests(metafunc):
    if "username" in metafunc.fixturenames:
        metafunc.parametrize("username", [metafunc.config.getoption("username")])
    if "password" in metafunc.fixturenames:
        metafunc.parametrize("password", [metafunc.config.getoption("password")])


#################################################
def dev_interface(uri, classname, val, attr, tol):
    sdr = eval(classname + "(uri='" + uri + "')")
    # Check hardware
    if not hasattr(sdr, attr):
        raise AttributeError(attr + " not defined in " + classname)

    rval = getattr(sdr, attr)
    is_list = isinstance(rval, list)
    if is_list:
        l = len(rval)
        val = [val] * l

    setattr(sdr, attr, val)
    rval = getattr(sdr, attr)

    if not isinstance(rval, str) and not is_list:
        rval = float(rval)
    del sdr
    if not isinstance(val, str):
        abs_val = np.argmax(abs(np.array(val) - np.array(rval)))
        if abs_val > tol:
            print("Failed to set: " + attr)
            print("Set: " + str(val))
            print("Got: " + str(rval))
        return abs_val
    else:
        return val == str(rval)
