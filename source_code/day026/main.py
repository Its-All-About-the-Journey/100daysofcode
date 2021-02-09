import pandas

# Create a dictionary from CSV
data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for index, row in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
word = list(input("Enter a word: "))
phonetic = [nato_dict[letter.upper()] for letter in word]
print(phonetic)
