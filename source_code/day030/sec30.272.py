import pandas

FILENAME = "nato_phonetic_alphabet.csv"

data = pandas.read_csv(FILENAME)
nato_words = {row.letter: row.code for _, row in data.iterrows()}

while True:
    word_entered = input("Enter word: ")

    # User pressing enter exits script
    if not word_entered:
        break

    try:
        word_to_nato = [nato_words[letter.upper()] for letter in word_entered]

        print(f"\n{word_to_nato}\n")
    
    except KeyError:
        print(f"The word '{word_entered}' includes one or more character's not in the alphabet\n")
