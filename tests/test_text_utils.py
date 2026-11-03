"""Tests for is_valid_username, count_words, truncate  (function-style tests)."""
import pytest

from qe_utils import count_words, is_valid_username, truncate


# ---- WORKED EXAMPLE (already done for you; read it, then copy the pattern) ----
@pytest.mark.smoke
def test_username_valid_simple_name():
    # Arrange
    name = "qe_trainee"
    # Act
    result = is_valid_username(name)
    # Assert
    assert result is True


# ---- TODO tests: replace each `pytest.fail(...)` line with real test code ----

@pytest.mark.boundary
@pytest.mark.regression
def test_username_too_short_is_rejected():
    # TODO (Task 3): 2 characters must be rejected. Add markers: boundary, regression
    # Arrange
    name = "ab"  # 2 chars, one below the lower limit
    # Act
    result = is_valid_username(name)
    # Assert
    assert result is False


@pytest.mark.boundary
@pytest.mark.regression
def test_username_exactly_3_chars_is_accepted():
    # TODO (Task 3): lower boundary. Markers: boundary, regression
    # Arrange
    name = "abc"  # exactly the lower limit
    # Act
    result = is_valid_username(name)
    # Assert
    assert result is True


@pytest.mark.boundary
@pytest.mark.regression
def test_username_16_chars_is_rejected():
    # TODO (Task 3): upper boundary + 1. Markers: boundary, regression
    # Arrange
    name = "a" * 16  # one above the upper limit of 15
    # Act
    result = is_valid_username(name)
    # Assert
    assert result is False


@pytest.mark.regression
def test_username_starting_with_digit_is_rejected():
    # TODO (Task 3): "1abc" -> False. Marker: regression
    # Arrange
    name = "1abc"
    # Act
    result = is_valid_username(name)
    # Assert
    assert result is False


@pytest.mark.regression
def test_username_with_space_or_symbol_is_rejected():
    # TODO (Task 3): "bad name" and "bad-name" -> False (two asserts are fine). Marker: regression
    # Arrange
    with_space = "bad name"
    with_symbol = "bad-name"
    # Act
    space_result = is_valid_username(with_space)
    symbol_result = is_valid_username(with_symbol)
    # Assert
    assert space_result is False
    assert symbol_result is False


@pytest.mark.regression
def test_username_non_string_raises_type_error():
    # TODO (Task 4): use pytest.raises(TypeError, match=...) with the input 12345
    # Arrange
    not_a_string = 12345
    # Act / Assert
    with pytest.raises(TypeError, match="username must be a string"):
        is_valid_username(not_a_string)


@pytest.mark.smoke
def test_count_words_simple_sentence():
    # TODO (Task 3): "quality is everyone's job" -> 4. Marker: smoke
    # Arrange
    text = "quality is everyone's job"
    # Act
    result = count_words(text)
    # Assert
    assert result == 4


@pytest.mark.boundary
@pytest.mark.regression
def test_count_words_empty_string_is_zero():
    # TODO (Task 3): "" -> 0. Markers: boundary, regression
    # Arrange
    text = ""
    # Act
    result = count_words(text)
    # Assert
    assert result == 0


@pytest.mark.regression
def test_count_words_non_string_raises_type_error():
    # TODO (Task 4): None must raise TypeError
    # Arrange
    not_a_string = None
    # Act / Assert
    with pytest.raises(TypeError, match="text must be a string"):
        count_words(not_a_string)


@pytest.mark.smoke
def test_truncate_short_text_is_unchanged():
    # TODO (Task 3): truncate("hello", 10) == "hello". Marker: smoke
    # Arrange
    text, max_len = "hello", 10
    # Act
    result = truncate(text, max_len)
    # Assert
    assert result == "hello"


@pytest.mark.regression
def test_truncate_long_text_ends_with_ellipsis_and_has_max_len():
    # TODO (Task 3): truncate("abcdefghij", 8) == "abcde..."  (len 8). Marker: regression
    # Arrange
    text, max_len = "abcdefghij", 8
    # Act
    result = truncate(text, max_len)
    # Assert
    assert result == "abcde..."
    assert len(result) == max_len


@pytest.mark.xfail(
    reason="BUG: truncate cuts text whose length equals max_len instead of returning it unchanged",
    strict=True,
)
@pytest.mark.boundary
@pytest.mark.regression
def test_truncate_text_exactly_max_len_is_unchanged():
    # TODO (Task 6): by the docstring, text that fits exactly must NOT be cut.
    # Write the test according to the docstring. It will FAIL - why?
    # Then mark it as a known bug:  @pytest.mark.xfail(reason="...", strict=True)
    # Markers: boundary, regression
    # Arrange
    text, max_len = "hello", 5  # text fits exactly
    # Act
    result = truncate(text, max_len)
    # Assert (per the docstring: text that fits must NOT be cut)
    assert result == "hello"


@pytest.mark.regression
def test_truncate_max_len_below_3_raises_value_error():
    # TODO (Task 4): max_len=2 -> ValueError, check the message with match=
    # Arrange
    text, max_len = "hello", 2
    # Act / Assert
    with pytest.raises(ValueError, match="max_len must be at least 3"):
        truncate(text, max_len)