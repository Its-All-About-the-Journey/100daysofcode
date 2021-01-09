from caesarart import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):

    # keep the integrity of the shift amount
    shift = shift % len(alphabet)

    # perform the shift on the readable alphabet
    shifted = alphabet[shift:] + alphabet[:shift]
    
    # set the direction of our encoding/decoding
    if direction == "encode":
        input_family = alphabet
        output_family = shifted
    else:
        input_family = shifted
        output_family = alphabet

    # initalize our results container
    result = ""

    # loop over each letter in the input text
    for letter in text:

        # only perform the transform on letters we are able to
        # and for all others, just keep them the same. e.g., spaces
        if letter in input_family:
            result += output_family[input_family.index(letter)]
        else:
            result += letter
        
    # print our result
    print(result)

def main():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

print(logo)
print()

main()
while input("again? ") == "yes":
    main()
print("bye")