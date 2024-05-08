# Given sequence
sequence = 'TCGGTGAGACTCGGTGATACTCGGTGCCACTCGGTGCGACTCGGTGCTACTCGGTGGCACTCGGTGGGACTCGGTGGTACTCGGTGTCACTCGGTGTGACTCGGTGTTACTCGGTTAGACTCGGTTATACTCGGTTCCACTCGGTTCGAC'

# Function to identify all different observed substrings of size k
def find_substrings(sequence, k):
    substrings = set()  # Initialize an empty set to store unique substrings
    for i in range(len(sequence) - k + 1):  # Iterate over the sequence to find substrings
        substrings.add(sequence[i:i+k])  # Add the substring of size k to the set
    return substrings  # Return the set of unique substrings

# Identify substrings of size 2
size_2_substrings = find_substrings(sequence, 2) 
print("Substrings of size 2:", size_2_substrings)

# Extend to identify substrings of any size
k = 3  # Specify the size of substrings
size_k_substrings = find_substrings(sequence, k)
print(f"Substrings of size {k}:", size_k_substrings)
