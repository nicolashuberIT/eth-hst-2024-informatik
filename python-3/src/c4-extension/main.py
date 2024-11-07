# %%

# dependencies

import sys
from typing import *

from src.SequenceAnalysis import SequenceAnalysis as sa
from src.Logger import Logger as log

# var

M_AGILIS_SEQ: str    = "TTGTCTTTTAAATAAAGACCTGTATGAATGGCTGAATGAGGATAAACCTGTCTCTTATAACTAATCAGTGAAACTGATCTCCCAGTACAAAAGCTGGAATATACACATAAGACGAGAAGACCCTGTGGAGCTTAAAAC-AAACCACTAAACAA-----GT--ATACCACTACCTTAGTGTAC-GTTTTCAGTTGGGGCGACTTCGGAATAAAATGAAACTTCCGAGCACAGAGGCAC-TTCCTCTAACTAAGGCCAACAAGCCAAAGACCC---ATAAACGACCCGGCC---TTGCCGATCAACGAACCAAGTTACCCCAGGGATAACAGCGCAATCTTCTTCGAGAGCCCTTATCAACAAGAAGGTTTACGACCTCGATGTTGGATCAGGACACCCAAATGGTGCAGCCGCTATTAAAGGTTCGTTTGTTCAACGATT"
M_ATLANTICA_SEQ: str = "TTGTCTTCTAAATAAAGACCAGTATGAACGGCTAAATGAGGACAAACCTGTCTCTTTTAACTAATCAGTGAAACTGATCTCCCAGTACAAAAGCTGGGATACAAACATAAGACGAGAAGACCCCGTGGAGCTTAAAACAAAACCACCAATCCA--C------GCCCTGG-ACCCTGGTGGACTGTTTTGAGTTGGGGCGACTTCGGAATAAAAAGAAACTTCCGAGCACAGAACCAC-AAATTCTAACCAAGGCCAACAAGCCTAAGCATA---TAA-CTGACCCGGCCC--ACGCCGATCAACGAACCAAGTTACCCCGGGGATAACAGCGCTATCTTCTTCAAGAGTCCCTATCAACAAGAAGGTTTACGACCTCGATGTTGGATCAGGACACCCAAATGGTGCAGCCGCTATTAAAGGTTCGTTTGTTCAACGATT"
M_CAPENSIS_SEQ: str  = "TTGTCTTCTAAATAAAGACCTGTATGAACGGCTAAATGAGGATAAACCTGTCTCTTATAACCAACCAGTGAAACTGATCTCCCAGTACAAAAGCTGGAATCAACCCATAAGACGAGAAGACCCTGCGGAGCTTAAAACAAACCACTAATTAATATC-----ATCTT---AACCCTAGTGAAATGTTTTCAGTTGGGGCGACTTCGGAATAAAACACAACTTCCGAGCACAGAACCACT-AATTCTAACCAAGGCCAACAAGCCAAAGTATAA--TA---TGACCCGGCAC--ATGCCGATCAACGAACCAAGTTACCCCAGGGATAACAGCGCTATCCTCTTCAAGAGTCCCTATCAACAAGAGGGTTTACGACCTCGATGTTGGATCAGGACACCCAAATGGTGCAGCCGCTATTAAAGGTTCGTTTGTTCAACGATT"
M_VITTATA_SEQ: str   = "TTGTCTTCTAAATAAAGACCAGTATGAACGGCTAAATGAGGACAAACCTGTCTCTTATAATTAATCAGTGAAACTGATCTCCCAGTACAAAAGCTGGGATATTAACATAAGACGAGAAGACCCCGTGGAGCTTGAAAT-AAACCACTAAACAATAC--GTG----CCACTAGTTTA-TGTACTATTTTCAGTTGGGGCGACTTCGGAACAAAACAAAACTTCCGAGCACAGAACCAC-TTCCTCTAACCAAGGCCAACAAGCCTAAGACTC---ATAAACGACCCGGCCCACTTGCCGATCAACGAACCAAGTTACCCCGGGGATAACAGCGCTATCTTCTTCAAGAGTCCCTATCAACAAGAAGGTTTACGACCTCGATGTTGGATCAGGACACCCAAATGGTGCAGCCGCTATTAAAGGTTCGTTTGTTCAACGATT"

DNA_MAP: dict[str, str] = {
    "Mabuya agilis": M_AGILIS_SEQ,
    "Mabuya atlantica": M_ATLANTICA_SEQ,
    "Mabuya capensis": M_CAPENSIS_SEQ,
    "Mabuya vittata": M_VITTATA_SEQ
}

# istantiate imported classes

Analyzer: sa = sa(DNA_MAP)
Logs: log = log()

# log cartesian product of DNA_MAP keys

print(20 * "-")
print()
print("The following cartesian product of the DNA_MAP keys are be used in the sequential analysis.")
print()
Logs.logCartesianProduct(Analyzer.cartesian_keys)
print()

# nucleotide analysis per dna map element

Analyzer.nucleotideAnalysis()

print(20 * "-")
print()
print("The nucleotide analysis for each individual DNA sequence returns the following results:")
print()

Logs.logNucleotideAnalysis(Analyzer.nucleotide_analysis)

# check DNA sequence lengths

print()
print(20 * "-")
print()
print("The system has performed a length check of all given DNA sequences, which resolved with the following result:")
print()

Analyzer.checkSequenceLength()

print()
Logs.logLengthCheck(Analyzer.sequence_length_check)

if not Analyzer.sequence_length_check:
    print()
    print("Error: Because of the failed sequence length check the program has been stopped.", file=sys.stderr)
    sys.exit(1)

# run DNA sequence comparison

print()
print(20 * "-")
print()
print("The system has performed a DNA sequence comparison for all possible combinations of given DNA sequences, which resolved with the following result:")
print()

Analyzer.compareSequences()
Logs.logSequenceAnalysis(Analyzer.sequence_comparison)

print()
print(20 * "-")
print()
print("The comparison results can be visualised in the following matrix:")
print()
print(Analyzer.generateResultMatrix())

# finish program

print()
print(20 * "-")
print()
print("The program was successfully completed.")
print()
print(20 * "-")
print()

# %%
