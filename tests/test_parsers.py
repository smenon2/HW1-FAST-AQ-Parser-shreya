# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pathlib
import pytest

def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    name0 = "seq0"
    name1 = "seq1"
    seq0 = "TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA"
    seq1 = "TCCGCCCGCTGTGCTGACGAGACTAGCAGGGAAATAAATAGAGGGTTTAGTTATACTCAGTAGGCAGTTCGATGGCTTATATCTAACTTCTTATTCCGAT"

    data_dir = pathlib.Path(__file__).resolve().parent.parent / "data"
    fasta_file = data_dir / "test.fa"
    fasta_parser = FastaParser(fasta_file)
    iter_parser = iter(fasta_parser)
    test_seqname0, test_seq0 = next(iter_parser)
    test_seqname1, test_seq1 = next(iter_parser)

    assert name0==test_seqname0 and name1==test_seqname1 and test_seq1==seq1 and test_seq0==seq0, "Should be"


def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    name0='seq0'
    seq0='TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG'
    qual0='*540($=*,=.062565,2>\'487\')!:&&6=,6,*7>:&132&83*8(58&59>\'8!;28<94,0*;*.94**:9+7"94(>7=\'(!5"2/!%"4#32='

    data_dir = pathlib.Path(__file__).resolve().parent.parent / "data"
    fastq_file = data_dir / "test.fq"
    fastq_parser = FastqParser(fastq_file)
    iter_parser = iter(fastq_parser)
    test_name, test_seq, test_qual = next(iter_parser)

    assert name0==test_name and seq0==test_seq and qual0==test_qual, "Should be"


