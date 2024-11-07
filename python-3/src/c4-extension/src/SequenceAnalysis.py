# dependencies

import itertools
import numpy as np
import pandas as pd
from typing import *

# class

class SequenceAnalysis:
    """
    Automates analysis and comparison of a given selection of dna sequences.
    """

    def __init__(self, dna: dict[str, str]) -> None:
        """
        Initialises the SequenceAnalysis class.
        
        Args:
        - dna_map (dict[str, str]): contains data to be analysed

        Returns:
        - None
        """
        self.dna_map: dict[str, str] = dna
        self.dna_keys: List[str] = list(dna.keys())
        self.cartesian_keys: List[Tuple[str, str]] = self.cartesianProduct()

        self.pickers: List[str] = ["A", "T", "G", "C", "-"] # defines the dna sequence elements that are to be analysed
        self.nucleotide_analysis: Dict[str, Dict[str, int]] = {}

        self.sequence_length_check: bool = False # stores the length ckeck and defaults False
        self.sequence_comparison: List[Tuple[str, str], int, int, float] = [] # stores a tuple of key pairs as well as comparisons, similarities and final similarity in this order
        
    def cartesianProduct(self) -> List[Tuple[str, str]]:
        """
        Generates cartesian product for given dictionary keys.
        
        Args:
        - None

        Returns:
        - cartesian_product (List[Tuple[str, str]]) - contains a list of tuples that represent all possible comparisons of the dna sequences
        
        """
        cartesian_product: List[Tuple[str, str]] = list(itertools.product(self.dna_keys, repeat=2))
        return cartesian_product
    
    def nucleotideAnalysis(self) -> Dict[str, Dict[str, int]]:
        """
        Runs nucleotide analysis on each DNA string accessible within this class (dna_map).

        Args:
        - None

        Returns:
        - None
        """

        nucleotide_analysis: Dict[str, Dict[str, int]] = {}

        for key in self.dna_keys:

            counter = 0
            picker_analysis = {}

            for picker in self.pickers:
                sequence = self.dna_map[key]

                for i in range(0, len(sequence)):
                    if sequence[i] == picker:
                        counter += 1

                picker_analysis[picker] = counter

                counter = 0

            picker_analysis['total'] = len(sequence)
            nucleotide_analysis[key] = picker_analysis    
            picker_analysis = {}

            self.nucleotide_analysis = nucleotide_analysis

    def checkSequenceLength(self) -> None:
        """
        Checks if the length of all DNA sequences is the same.

        Args:
        -> None

        Returns:
        -> None
        """
        first_species: str = next(iter(self.nucleotide_analysis))
        first_count: int = self.nucleotide_analysis[first_species]['total']

        for species, nucleotide_counts in self.nucleotide_analysis.items():
            current_count: int = nucleotide_counts['total']
            print(f"--> Checked {species}: {current_count} against {first_species}: {first_count}")  # debug print
            
            if current_count != first_count:
                self.sequence_length_check = False
                return
            
        self.sequence_length_check = True

    def compareSequences(self) -> None:
        """
        Compares given DNA sequences and returns similarity indicators.
        
        Args:
        - None
        
        Returns:
        - None
        """
        counter = 0

        for key_a, key_b in self.cartesian_keys:
            sequence_a = self.dna_map[key_a]
            sequence_b = self.dna_map[key_b]

            comparisons: int = 0
            similarities: int = 0

            for i in range(0, len(sequence_a)):
                if sequence_a[i] != "-" and sequence_b[i] != "-": # checks if either sequence_a or sequence_b contain "-" at given position, if yes skips to next character
                    comparisons += 1

                    if sequence_a[i] == sequence_b[i]: # checks if sequence_a or sequence_b have similar character at given position
                        similarities += 1

            similarity: float = self.calculateSimilarity(comparisons, similarities)
            self.sequence_comparison.append([self.cartesian_keys[counter], comparisons, similarities, similarity])
            counter += 1

    def calculateSimilarity(self, comparisons: int, similarities: int) -> float:
        """
        Calculates the similarity of two given DNA strings.
        
        Args:
        - comparisons (int) - number of comparisons during processing
        - similarities (int) - number of similarities during comparison

        Returns:
        - (float) - similarity in percentage rounded to two decimals
        """
        return round(similarities / comparisons, 2)
    
    def generateResultMatrix(self) -> pd.DataFrame:
        """
        Generates matrix from sequence comparisons to be converted to pd dataframe and printed to console.
        
        Args:
        - None
        
        Returns:
        - None

        REMARK: Implementation assisted by ChatGPT, 20/10/2024
        """
        species_names = sorted(set(pair[0] for pair, _, _, _ in self.sequence_comparison)) # extract the unique species from the data

        n: int = len(species_names)
        similarity_matrix = np.zeros((n, n)) # initialize empty NxN matrix to store similarity percentages
        species_index = {species: idx for idx, species in enumerate(species_names)} # create a mapping from species name to index for the matrix

        for (species_a, species_b), _, _, similarity_percentage in self.sequence_comparison:
            idx_a = species_index[species_a]
            idx_b = species_index[species_b]
            similarity_matrix[idx_a, idx_b] = similarity_percentage

        return pd.DataFrame(similarity_matrix, index=species_names, columns=species_names)
