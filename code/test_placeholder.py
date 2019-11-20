import pytest
from placeholder import placeholder


def test_placeholder():
	result = placeholder(2)
	print(result)
	assert (result == 1)

test_placeholder()