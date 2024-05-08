def read_sequences(file_path):
    with open(file_path, 'r') as file:
        sequences = []
        sequence = ''
        for line in file:
            if line.startswith('>'): 
                if sequence:
                    sequences.append(sequence)
                    sequence = ''
            else:
                sequence += line.strip()
        if sequence:
            sequences.append(sequence)
    return sequences
def find_substrings(sequence, k):
    substrings = {}  # Dictionary to store substrings and their subsequent sequences
    for i in range(len(sequence) - k):
        substring = sequence[i:i+k]  # Extract substring of size k
        subsequent = sequence[i+1:i+1+k]  # Extract subsequent substring
        if len(subsequent) == k:
            if substring in substrings:
                substrings[substring].add(subsequent)
            else:
                substrings[substring] = {subsequent}
    return substrings

# Example file path
file_path = '../../shared/439539/reads.fa'

# Reading sequences from file and processing each sequence
for sequence in read_sequences(file_path):
    # Identify substrings of size 2
    size_2_substrings = find_substrings(sequence, 2)
    print("Substrings of size 2:", size_2_substrings)

    # Specify the value of k (e.g., k = 3)
    k = 3

    # Extend to identify substrings of any size (specified by k)
    size_k_substrings = find_substrings(sequence, k)
    print(f"Substrings of size {k}:", size_k_substrings)
