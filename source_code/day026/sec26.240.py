import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_words = {row.letter: row.code for _, row in data.iterrows()}


while True:
    word_entered = input("Enter word: ")

    # User pressing enter exits script
    if not word_entered:
        break

    word_to_nato = [nato_words[letter.upper()] for letter in word_entered]

    print(f"\n{word_to_nato}\n")
