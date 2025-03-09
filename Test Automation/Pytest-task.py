import pytest
from test_exercise import count_vowel_consonant_pairs


# Basic Parameterized Tests
@pytest.mark.parametrize("input_text, expected_output", [
    ("hello", 1),
    ("banana", 3),
    ("AEIOUbc", 5),
    ("", 0),
    ("12345", 0),
    ("PyThOn", 1),
    ("a!e@i#o$u%", 0)
])
def test_count_vowel_consonant_pairs(input_text, expected_output):
    """Test count_vowel_consonant_pairs with various typical input strings."""
    assert count_vowel_consonant_pairs(input_text) == expected_output


# Edge Case Testing
@pytest.fixture
def edge_case_strings():
    """Provide edge case strings for testing, like empty strings or no valid pairs."""
    return [
        ("", 0),
        ("a!e@i#o$u%", 0),
        ("12345", 0),
        ("a", 0),
        ("b", 0),
        ("a1e2i3o4u", 0)
    ]


def test_edge_cases(edge_case_strings):
    """Test count_vowel_consonant_pairs with various edge case strings."""
    for input_text, expected_output in edge_case_strings:
        assert count_vowel_consonant_pairs(input_text) == expected_output


@pytest.fixture
def negative_inputs():
    """Provide invalid inputs to check for proper exception handling."""
    return [
        (None, TypeError),
        (12345, TypeError),
        (["hello"], TypeError),
        ({"text": "hi"}, TypeError)
    ]


def test_negative_inputs(negative_inputs):
    """Test count_vowel_consonant_pairs with invalid inputs, expecting TypeErrors."""
    for input_text, expected_exception in negative_inputs:
        with pytest.raises(expected_exception):
            count_vowel_consonant_pairs(input_text)


def test_large_input():
    """Test count_vowel_consonant_pairs with a large input string of repeated characters."""
    large_text = "a" * 1000 + "b" * 1000
    assert count_vowel_consonant_pairs(large_text) == 1



def test_large_alternating_input():
    """Test count_vowel_consonant_pairs with a large alternating pattern of vowels and consonants."""
    large_text = "ab" * 1000  # Alternating vowels ('a') and consonants ('b'), 1000 pairs
    assert count_vowel_consonant_pairs(large_text) == 1000
