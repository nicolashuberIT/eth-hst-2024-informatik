# dependencies

from typing import *

# class

class Logger:
    """
    Logs the analysis and comparison of a given selection of dna sequences.
    """

    def __init__(self) -> None:
        """
        Intialises the Logger class.
        
        Args:
        - None
        
        Returns:
        - None
        """
        pass

    def logCartesianProduct(self, cartesian: List[Tuple[str, str]]) -> None:
        """
        Logs a cartesian product of given format to console.
        
        Args:
        - cartesian (List[Tuple[str, str]]) - given certesian product to print to console
        
        Returns:
        - None
        """
        for combination in cartesian:
            print(combination)

    def logNucleotideAnalysis(self, analysis: Dict[str, Dict[str, int]]) -> None:
        """
        Logs the result of a nucleotide analysis.
        
        Args:
        - analysis (Dict[str, Dict[str, int]]) - Dictionary containg the results of each individual DNA sequence analysis.
        
        Returns:
        - None
        """
        for species, result in analysis.items():
            print(f"{species}:")
            for nucleotide, count in result.items():
                print(f"--> {nucleotide}: {count}")
        
    def logLengthCheck(self, status: bool) -> None:
        """
        Logs the result of the DNA sequence length checks.
        
        Args:
        - status (bool) - contains True or False depending on the DNA sequence length check
        
        Returns:
        - None
        """
        if status:
            print("All given DNA sequences are of the same length. Check ok.")
        else:
            print("A deviation in the length of the given DNA sequences has been detected. Check not ok.")

    def logSequenceAnalysis(self, comparison_data) -> None:
        """
        Logs the results of the DNA sequence comparisons.
        
        Args:
        - comparison_data () - list of all possible comparisons including results

        Returns:
        - None
        """
        for pair, total_comparisons, similarities, similarity_percentage in comparison_data:
            species_a, species_b = pair
            print(f"Comparison between {species_a} and {species_b}:")
            print(f"--> Total comparisons: {total_comparisons}")
            print(f"--> Similarities: {similarities}")
            print(f"--> Similarity percentage: {similarity_percentage * 100:.2f}%")
            