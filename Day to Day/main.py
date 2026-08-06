import pytest
from Test import hello

def test_default():
   assert hello() == "Hello, World"

def test_argument():
    for name in ["David", "Tony"]:
     assert hello("David") == "Hello, David"
