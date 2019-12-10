#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from genericdiff import *

def test_GenericDiff_lt():
    f = GenericDiff(1, 0)
    h = 2
    bool_val = f < h
    assert (bool_val)

def test_GenericDiff_gt():
    f = GenericDiff(1, 3)
    h = 2
    bool_val = f > h
    assert (bool_val)

def test_GenericDiff_eq():
    f = GenericDiff(1, 2)
    h = 2
    bool_val = f == h
    assert (bool_val)

def test_GenericDiff_ne():
    f = GenericDiff(1, 0)
    h = 2
    bool_val = f != h
    assert (bool_val)

def test_GenericDiff_le():
    f = GenericDiff(1, 0)
    h = 2
    bool_val = f <= h
    assert (bool_val)

def test_GenericDiff_ge():
    f = GenericDiff(1, 2)
    h = 2
    bool_val = f >= h
    assert (bool_val)

