"""
Test: Text

Version: 1.4.0
Date updated: 20/03/2024 (dd/mm/yyyy)
"""


# Library
###########################################################################
import pytest

from absfuyu.general.data_extension import Text, ListExt


# Test
###########################################################################
# analyze
def test_analyze():
    assert Text("Lmao").analyze() == {'digit': 0, 'uppercase': 1, 'lowercase': 3, 'other': 0}

def test_analyze_2():
    assert Text("Lmao").analyze() != {'digit': 1, 'uppercase': 1, 'lowercase': 3, 'other': 0}

def test_analyze_3():
    assert Text("Lmao$$TEST.").analyze() == {'digit': 0, 'uppercase': 5, 'lowercase': 3, 'other': 3}


# hex
def test_to_hex():
    """raw = True"""
    assert Text("Hello World").to_hex(raw=True) == "48656c6c6f20576f726c64"

def test_to_hex_2():
    """raw = False"""
    assert Text("Hello World").to_hex() == "\\x48\\x65\\x6c\\x6c\\x6f\\x20\\x57\\x6f\\x72\\x6c\\x64"


# pangram
def test_is_pangram():
    assert Text("abcdeFghijklmnopqrstuvwxyz").is_pangram() is True

def test_is_pangram_2():
    assert Text("abcdefghijklmnOpqrstuvwxy").is_pangram() is False

def test_is_pangram_3():
    assert Text("abcdeFghijklmnopqrstuvwxyzsdsd").is_pangram() is True

def test_is_pangram_4():
    assert Text("abcdeFghijklmnopqrs tuvwxyzsdsd").is_pangram() is True


# palindrome
def test_is_palindrome():
    assert Text("madam").is_palindrome() is True

def test_is_palindrome_2():
    assert Text("racecar").is_palindrome() is True


# reverse
def test_reverse():
    assert Text("abc").reverse() == "cba"


# random capslock
def test_random_capslock():
    """0%"""
    test = [Text("random").random_capslock(0) for _ in range(1000)]
    assert len(list(set(test))) == 1
    assert Text("random").random_capslock(0) == "random"

def test_random_capslock_2():
    """100%"""
    test = [Text("random").random_capslock(100) for _ in range(1000)]
    assert len(list(set(test))) == 1
    assert Text("random").random_capslock(100) == "RANDOM"

def test_random_capslock_3():
    """50%"""
    assert Text("random").random_capslock()


# divide
@pytest.fixture
def example_long_text():
    return Text("This is an extremely long text that even surpass my expectation and the rest of this text probably contains some useless stuff")

def test_divide(example_long_text: Text):
    assert example_long_text.divide().__len__() == 3

def test_divide_2(example_long_text: Text):
    assert example_long_text.divide(string_split_size=10).__len__() == 13

def test_divide_with_variable(example_long_text: Text):
    assert example_long_text.divide_with_variable(
        split_size=60,
        custom_var_name="abc"
    ) == [
        "abc1='This is an extremely long text that even surpass my expectat'",
        "abc2='ion and the rest of this text probably contains some useless'",
        "abc3=' stuff'",
        'abc=abc1+abc2+abc3',
        'abc'
    ]

def test_divide_with_variable_2(example_long_text: Text):
    """Check for list len"""
    assert example_long_text.divide_with_variable(
        split_size=60,
        custom_var_name="abc"
    ).__len__() == 5


# reverse capslock
def test_reverse_capslock():
    assert Text("Foo").reverse_capslock() == "fOO"

def test_reverse_capslock_2():
    assert Text("Foo BAr").reverse_capslock() == "fOO baR"


# to list
def test_to_list():
    assert isinstance(Text("test").to_list(), list)

def test_to_listext():
    assert isinstance(Text("test").to_listext(), ListExt)


# count pattern
def test_count_pattern():
    assert Text("Test sentence").count_pattern("ten") == 1

def test_count_pattern_2():
    assert Text("Test sentence").count_pattern("t") == 2

def test_count_pattern_3():
    assert Text("Test sentence").count_pattern("a") == 0

def test_count_pattern_4():
    assert Text("Test sentence").count_pattern("t", ignore_capslock=True) == 3

def test_count_pattern_5():
    try:
        Text("Test").count_pattern("tenss")
    except:
        assert True


# hapax
def test_hapax():
    assert Text("A a. a, b c c= C| d d").hapax() == ['a', 'a.', 'a,', 'b', 'c', 'c=', 'c|']

def test_hapax_2():
    assert Text("A a. a, b c c= C| d d").hapax(strict=True) == ['b']

