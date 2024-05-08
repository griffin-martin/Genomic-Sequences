import pytest  # Importing the pytest library to run the tests
from One_Specific_Substring import find_substrings  # Importing the find_substrings function from One_Specific_Substring module
from All_Possible_Substrings import read_sequences, find_substrings as find_substrings_this  # Importing read_sequences function and renaming find_substrings function from All_Possible_Substrings module
from Smallest_K_Value import identify_smallest_k_from_fasta  # Importing find_substrings_with_subsequents and find_unique_subsequent_k functions from Smallest_K_Value module

# Test data

def test_find_substrings():
    sequence = 'TCGGTGAGACTCGGTGATACTCGGTGCCACTCGGTGCGACTCGGTGCTACTCGGTGGCACTCGGTGGGACTCGGTGGTACTCGGTGTCACTCGGTGTGACTCGGTGTTACTCGGTTAGACTCGGTTATACTCGGTTCCACTCGGTTCGAC'
    # Test find_substrings for k=2
    actual_result_k2 = find_substrings(sequence, 2)  # Calling find_substrings function with sequence and k=2
    expected_result_k2 = {'CA', 'TG', 'GG', 'CG', 'GC', 'TA', 'TT', 'AC', 'TC', 'CT', 'AT', 'GT', 'AG', 'CC', 'GA'}  # Expected result for k=2
    print("Actual result for k=2:", actual_result_k2)
    print("Expected result for k=2:", expected_result_k2)
    assert actual_result_k2 == expected_result_k2, "Test for k=2 failed"  # Asserting whether actual result matches the expected result for k=2
    
    # Test find_substrings for k=3
    actual_result_k3 = find_substrings(sequence, 3)  # Calling find_substrings function with sequence and k=3
    expected_result_k3 = {'GTC', 'GGC', 'TTA', 'TGA', 'GTA', 'GTT', 'ACT', 'GGT', 'TCC', 'GCG', 'GCT', 'GCC', 'CCA', 'TAT', 'TGT', 'TAC', 'CTC', 'GAC', 'TTC', 'CTA', 'TGC', 'CGA', 'GTG', 'GAG', 'TGG', 'TAG', 'GGA', 'AGA', 'CAC', 'CGG', 'ATA', 'TCG', 'GCA', 'GAT', 'GGG', 'TCA'}  # Expected result for k=3
    print("Actual result for k=3:", actual_result_k3)
    print("Expected result for k=3:", expected_result_k3)
    assert actual_result_k3 == expected_result_k3, "Test for k=3 failed"  # Asserting whether actual result matches the expected result for k=3

def test_read_sequences_and_substrings(tmp_path):
    # Create a temporary fasta file
    d = tmp_path / "sub"  # Creating a subdirectory in the temporary directory
    d.mkdir()  # Creating the subdirectory
    p = d / "test.fasta"  # Defining the path for the temporary fasta file
    p.write_text(">Sequence1\nTCGGTGAGA\n>Sequence2\nCTCGGTGCC")  # Writing test sequences to the temporary fasta file

    # Test read_sequences and find_substrings integration
    sequences = read_sequences(str(p))  # Reading sequences from the temporary fasta file
    assert sequences == ['TCGGTGAGA', 'CTCGGTGCC'], "Read sequences failed"  # Asserting whether sequences are read correctly
    substrings = [find_substrings_this(seq, 2) for seq in sequences]  # Finding substrings for each sequence
    print("Substrings from file:", substrings)  # Printing the substrings obtained from the file
    expected_substrings = [{'TC': {'CG'}, 'CG': {'GG'}, 'GG': {'GT'}, 'GT': {'TG'}, 'TG': {'GA'}, 'GA': {'AG'}, 'AG': {'GA'}}, {'CT': {'TC'}, 'TC': {'CG'}, 'CG': {'GG'}, 'GG': {'GT'}, 'GT': {'TG'}, 'TG': {'GC'}, 'GC': {'CC'}}]  # Expected substrings
    


def test_find_unique_subsequent_k():
    sequence = "../../shared/439539/reads.fa"
    # Test find_unique_subsequent_k
    k = identify_smallest_k_from_fasta(sequence)  # Calling find_unique_subsequent_k function with the sequence
    print("Smallest k for unique subsequent substrings:", k)  # Printing the smallest k for unique subsequent substrings
    assert k == 152, "Test to find unique subsequent k failed"  # Asserting whether the smallest k matches the expected value

# Configure the test to run if the script is executed directly
if __name__ == "__main__":
    pytest.main()  # Running the tests using pytest
