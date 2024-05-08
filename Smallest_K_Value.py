from Bio import SeqIO # Install BioPython for further computation functions 

def identify_smallest_k_from_fasta(fasta_file_path):
    # Read sequences from the FASTA file
    with open(fasta_file_path, "r") as fasta_file:
        sequences = fasta_file.readlines()

    # Concatenate all sequences into a single string
    concatenated_sequence = "".join([seq.strip() for seq in sequences if not seq.startswith('>')])

    # Iterate over possible values of k
    for k in range(1, len(concatenated_sequence)):
        unique_substrings = set()
        has_unique_substrings = True

        # Iterate through the concatenated sequence and check substrings of length k
        for i in range(len(concatenated_sequence) - k):
            substring = concatenated_sequence[i:i+k]
            following_substring = concatenated_sequence[i+k:i+2*k]

            # If the following substring is already in the set, it's not unique
            if following_substring in unique_substrings:
                has_unique_substrings = False
                break
            else:
                unique_substrings.add(following_substring)

        # If every substring has a unique following substring, return the smallest k
        if has_unique_substrings:
            return k

    # If no such k is found, return -1 or raise an exception, depending on your preference
    return -1  # Or raise Exception("No such k exists")

# Example usage:
fasta_file_path = "../../shared/439539/reads.fa"
smallest_k = identify_smallest_k_from_fasta(fasta_file_path)
print("Smallest value of k:", smallest_k)
