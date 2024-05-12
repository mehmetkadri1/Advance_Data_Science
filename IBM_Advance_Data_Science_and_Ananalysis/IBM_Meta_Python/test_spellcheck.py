''' 
Import statements: 
    1. Import pytest and spellcheck modules
'''
### WRITE IMPORT STATEMENTS HERE
import pytest
import spellcheck
# String variables to be tested
alpha = "Checking the length & structure of the sentence."
beta = "This sentence should fail the test"

# Do not delete this function. You may change the value assigned to input to test different inputs to your test functions.
@pytest.fixture
def input_value():
    input = alpha
    return input

# First test function test_length()
def test_length(input_value):
    """ Tests whether a string has fewer than 10 words and fewer than 50 chars.

    [IMPLEMENT ME]
        1. Use an assert statement to check the given string has fewer than 10 words
        2. Use an assert statement to check the given string has fewer than 50 chars

    Args:
      input_value: a function that returns a string, which can be configured
                   in the input_value() function
    """
    ### WRITE SOLUTION CODE HERE
    string = input_value
    assert len(string.split()) < 10
    assert len(string) < 50
def input_value():
    return "This is a test string with less than 10 words."







# Second test function test_struc()
def test_struc(input_value):
    """ Tests whether a string begins with a capital letter and ends with a period.

    [IMPLEMENT ME]
        1. Use an assert statement to check the given string begins with a capital letter
        2. Use an assert statement to check the given string end with a period ('.')

    Args:
      input_value: a function that returns a string, which can be configured
                   in the input_value() function
    """
    ### WRITE SOLUTION CODE HERE
    
    # Get the string from the input_value function
    string = input_value
    
    # Check if the string begins with a capital letter
    assert string[0].isupper()
    
    # Check if the string ends with a period ('.')
    assert string.endswith('.')

# Example input_value function
    def input_value():
        return "This is a test string with a capital letter and ends with a period."

# Test the function with the example input_value function


def test_string_format():
    def input_value(): return "This is a test string with a capital letter and ends with a period."
    test_struc(input_value)

# Run these tests with `python3 -m pytest test_spellcheck.py`