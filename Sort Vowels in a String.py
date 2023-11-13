class Solution(object):
    def sortVowels(self, s):
        vowels = "aeiouAEIOU"  # Define the vowels
        vowel_indices = []  # Store the indices of vowels
        vowel_chars = []  # Store the vowel characters

        # Iterate through the string to find vowels and their indices
        for i, char in enumerate(s):
            if char in vowels:
                vowel_indices.append(i)
                vowel_chars.append(char)

        # Sort the vowel characters
        vowel_chars.sort()

        # Replace the vowels in the string with the sorted vowels
        sorted_string = list(s)
        for index, char in zip(vowel_indices, vowel_chars):
            sorted_string[index] = char

        return ''.join(sorted_string)
