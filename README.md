# Genomic-Sequences
This project, Genomic-Sequences, looks at genomic sequences along with KMERs of different lengths. Identified possible substrings and subsequent substrings while incorporating a large string of genomic sequences. 

One_Specific_Substring.py investigates one substring and where k is specified as an argument, for a single sequence (also specified as an argument), and all unique possible subsequent substrings of each substring. 

All_Possible_Substrings.py looks over the prior function to identify all possible substrings and their subsequent substrings for all sequences read from a file. Said file is denoted as reads.fa with a filepath of ../../shared/439539/reads.fa (note, filepath may need to be altered depending on location of directory). 

Smallest_K_Value.py studies the notion that there is at least one value of k where every substring has only one possible substring that follows it. This function aims to identify the smallest value using the prior functions.

Pytest_code.py is code that aids in the implementation of a test that runs the three prior functions for their functionality. Simply write in the command line "pytest Pytest_code.py" to run. 

All code was ran and tested through the command line of the terminal in an RStudio server. 
