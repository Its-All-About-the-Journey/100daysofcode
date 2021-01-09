alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

def encrypt(plain_text: str, shift: int) -> None:
    ascii_a = ord('a')
    ascii_z = ord('z')

    if shift > (ascii_z - ascii_a + 1):
        print(f'{shift} is bigger than my alphabet')
        return None
    
    result = ''
    for char in plain_text:
        ascii_char_num = ord(char) + shift
        
        # Test boundary, greater than z
        if ascii_char_num > ascii_z :
            result += chr( ascii_a + (ascii_char_num - ascii_z - 1) )
        else:
            result += chr(ascii_char_num)
    
    print(f"Here's the encoded result: {result}")

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

if direction == 'encode':
    encrypt(text, shift)
else:
    print('Selection is currently broken!')