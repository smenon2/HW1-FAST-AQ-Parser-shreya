# write tests for transcribes

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the
    transcribe function here.
    """
    ex_seq = 'ACGT'
    test_seq = transcribe(ex_seq)

    assert test_seq == 'UGCA', "Should be"


def test_reverse_transcribe():
    """
    Write your unit test for the
    reverse transcribe function here.
    """
    ex_seq = 'ACGT'
    test_seq = reverse_transcribe(ex_seq)

    assert test_seq == 'ACGU', 'Should be'
