import pytest
from GEM import find_substrings
from THIS import read_sequences, find_substrings as find_substrings_this
from FRED import find_substrings_with_subsequents, find_unique_subsequent_k

# Test data
sequence = 'TCGGTGAGACTCGGTGATACTCGGTGCCACTCGGTGCGACTCGGTGCTACTCGGTGGCACTCGGTGGGACTCGGTGGTACTCGGTGTCACTCGGTGTGACTCGGTGTTACTCGGTTAGACTCGGTTATACTCGGTTCCACTCGGTTCGAC'

def test_find_substrings():
    # Test find_substrings for k=2
    actual_result_k2 = find_substrings(sequence, 2)
    expected_result_k2 = {'CA', 'TG', 'GG', 'CG', 'GC', 'TA', 'TT', 'AC', 'TC', 'CT', 'AT', 'GT', 'AG', 'CC', 'GA'}
    print("Actual result for k=2:", actual_result_k2)
    print("Expected result for k=2:", expected_result_k2)
    assert actual_result_k2 == expected_result_k2, "Test for k=2 failed"
    
    # Test find_substrings for k=3
    actual_result_k3 = find_substrings(sequence, 3)
    expected_result_k3 = {'GTC', 'GGC', 'TTA', 'TGA', 'GTA', 'GTT', 'ACT', 'GGT', 'TCC', 'GCG', 'GCT', 'GCC', 'CCA', 'TAT', 'TGT', 'TAC', 'CTC', 'GAC', 'TTC', 'CTA', 'TGC', 'CGA', 'GTG', 'GAG', 'TGG', 'TAG', 'GGA', 'AGA', 'CAC', 'CGG', 'ATA', 'TCG', 'GCA', 'GAT', 'GGG', 'TCA'}
    print("Actual result for k=3:", actual_result_k3)
    print("Expected result for k=3:", expected_result_k3)
    assert actual_result_k3 == expected_result_k3, "Test for k=3 failed"

def test_read_sequences_and_substrings(tmp_path):
    # Create a temporary fasta file
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "test.fasta"
    p.write_text(">Sequence1\nTCGGTGAGA\n>Sequence2\nCTCGGTGCC")

    # Test read_sequences and find_substrings integration
    sequences = read_sequences(str(p))
    assert sequences == ['TCGGTGAGA', 'CTCGGTGCC'], "Read sequences failed"
    substrings = [find_substrings_this(seq, 2) for seq in sequences]
    print("Substrings from file:", substrings)
    expected_substrings = [{'TC': {'CG'}, 'CG': {'GG'}, 'GG': {'GT'}, 'GT': {'TG'}, 'TG': {'GA'}, 'GA': {'AG'}, 'AG': {'GA'}}, {'CT': {'TC'}, 'TC': {'CG'}, 'CG': {'GG'}, 'GG': {'GT'}, 'GT': {'TG'}, 'TG': {'GC'}, 'GC': {'CC'}}]
    


def test_find_unique_subsequent_k():
    # Test find_unique_subsequent_k
    k = find_unique_subsequent_k(sequence)
    print("Smallest k for unique subsequent substrings:", k)
    assert k == 10, "Test to find unique subsequent k failed"

# Configure the test to run if the script is executed directly
if __name__ == "__main__":
    pytest.main()
