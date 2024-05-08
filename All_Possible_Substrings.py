# Define a function to read sequences from a file
def read_sequences(file_path):
    # Open the file for reading
    with open(file_path, 'r') as file:
        sequences = []  # List to store sequences
        sequence = ''  # Variable to store the current sequence
        # Iterate over each line in the file
        for line in file:
            # Check if the line starts with '>', indicating a sequence header
            if line.startswith('>'): 
                # If there's a sequence already stored, append it to the list and reset the sequence variable
                if sequence:
                    sequences.append(sequence)
                    sequence = ''
            else:
                # Append the sequence data to the current sequence variable, removing leading and trailing whitespace
                sequence += line.strip()
        # If there's a sequence remaining after reading all lines, append it to the list of sequences
        if sequence:
            sequences.append(sequence)
    # Return the list of sequences
    return sequences

# Define a function to identify substrings of a given size (k) in a sequence
def find_substrings(sequence, k):
    substrings = {}  # Dictionary to store substrings and their subsequent sequences
    # Iterate over the sequence to find substrings
    for i in range(len(sequence) - k):
        # Extract substring of size k
        substring = sequence[i:i+k]
        # Extract subsequent substring
        subsequent = sequence[i+1:i+1+k]
        # Check if the length of the subsequent substring is k
        if len(subsequent) == k:
            # If the substring already exists in the dictionary, add the subsequent substring to its set of subsequents
            if substring in substrings:
                substrings[substring].add(subsequent)
            # If the substring is not in the dictionary, initialize a set with the subsequent substring for the current substring
            else:
                substrings[substring] = {subsequent}
    # Return the dictionary containing substrings and their subsequent sequences
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
