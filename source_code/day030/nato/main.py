import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

alphabet = "source_code/day026/NATO-alphabet-start/nato_phonetic_alphabet.csv"
nato_dict = pandas.read_csv(alphabet).set_index('letter')['code'].to_dict()

# Official method

#nato_alphabet = pandas.read_csv(alphabet)
#nato_dict = {row.letter:row.code for (index,row) in nato_alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def gen_nato_word():
    word = input("Enter a word: ").upper()
    try:
        nato_word = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Only letters please.")
        gen_nato_word()
    else:
        print(nato_word)

gen_nato_word()