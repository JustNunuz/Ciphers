# Define the list of letters in the English alphabet
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Prompt the user to enter a word
word = input("Enter a word: ")

# Initialize an empty list to hold each character of the word
holder = []

# Loop through each character in the word and add it to the holder list
for char in word:
    holder.append(char)

# Print the length of the chosen word
print("Length of the chosen word is:", len(holder))

# Initialize an empty string to hold the encrypted text
encrypted_text = ""

# Loop through each character in the holder list
for x in range(len(holder)):
    # Loop through each letter in the letters list
    for y in range(len(letters)):
        # If the current character matches the current letter
        if holder[x] == letters[y]:
            # Print the character and its position in the letters list
            print(holder[x], "in position", y)
            # Define the shift value for the Caesar cipher
            shift = 4
            # Calculate the encrypted position of the character
            encrypted_position = (y + shift) % len(letters)
            # Add the encrypted character to the encrypted_text string
            encrypted_text += letters[encrypted_position]
            # Exit the inner loop
            break

# Print the encrypted text
print("Encrypted text:", encrypted_text)
