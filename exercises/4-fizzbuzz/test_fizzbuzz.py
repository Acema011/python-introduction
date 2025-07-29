from src import fizzbuzz

def test_1_return_1():
    assert fizzbuzz(1) == "1"

def test_3_return_Fizz():
    assert fizzbuzz(3) == "Fizz"

def test_4_return_4():
    assert fizzbuzz(4) == "4"

def test_5_return_Buzz():
    assert fizzbuzz(5) == "Buzz"

def test_6_return_Fizz():
    assert fizzbuzz(6) == "Fizz"

def test_15_return_FizzBuzz():
    assert fizzbuzz(15) == "FizzBuzz"