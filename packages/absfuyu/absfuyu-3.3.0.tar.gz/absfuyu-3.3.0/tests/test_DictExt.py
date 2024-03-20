"""
Test: DictExt

Version: 1.3.0
Date updated: 20/03/2024 (dd/mm/yyyy)
"""


# Library
###########################################################################
import pytest

from absfuyu.general.data_extension import DictExt, DictAnalyzeResult


# Test
###########################################################################
@pytest.fixture
def example():
    return DictExt({
        "Line 1": 99,
        "Line 2": 50
    })

@pytest.fixture
def example_2():
    return DictExt({
        "Line 1": 99,
        "Line 2": "test"
    })


# analyze
def test_analyze(example: DictExt):
    # assert example.analyze() == {'max_value': 99, 'min_value': 50, 'max': [('Line 1', 99)], 'min': [('Line 2', 50)]}
    assert example.analyze() == DictAnalyzeResult(99, 50, [('Line 1', 99)], [('Line 2', 50)])

def test_analyze_2(example_2: DictExt):
    """When values are not int or float"""
    try:
        example_2.analyze()
    except:
        assert True


# swap
def test_swap(example: DictExt):
    assert example.swap_items() == {99: 'Line 1', 50: 'Line 2'}


# apply
def test_apply(example: DictExt):
    """Values"""
    assert example.apply(str) == {'Line 1': '99', 'Line 2': '50'}

def test_apply_2():
    """Keys"""
    assert DictExt({1: 1}).apply(str, apply_to_value=False) == {'1': 1}