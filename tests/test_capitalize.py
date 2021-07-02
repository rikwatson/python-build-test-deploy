# test_capitalize.py

import pytest

import sampleproject.capitalize as capitalize

def test_capital_case():
    assert capitalize.capital_case('semaphore') == 'Semaphore'

def test_capital_case_noop():
    assert capitalize.capital_case('Semaphore') == 'Semaphore'

def test_capital_case_numeric():
    assert capitalize.capital_case('42') == '42'

def test_capital_case_null():
    assert capitalize.capital_case('') == ''

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capitalize.capital_case(9)
