sequence = 'TCGGTGAGACTCGGTGATACTCGGTGCCACTCGGTGCGACTCGGTGCTACTCGGTGGCACTCGGTGGGACTCGGTGGTACTCGGTGTCACTCGGTGTGACTCGGTGTTACTCGGTTAGACTCGGTTATACTCGGTTCCACTCGGTTCGAC'

# Function to identify all different observed substrings of size k
def find_substrings(sequence, k):
    substrings = set()
    for i in range(len(sequence) - k + 1):
        substrings.add(sequence[i:i+k])
    return substrings

# Identify substrings of size 2
size_2_substrings = find_substrings(sequence, 2)
print("Substrings of size 2:", size_2_substrings)

# Extend to identify substrings of any size
k = 3
size_k_substrings = find_substrings(sequence, k)
print(f"Substrings of size {k}:", size_k_substrings)
