alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(plain_text=text,shift_amount=shift):
    if direction == 'encode':
        new_text = ""
        for i in text:
            
            # position of letter
            position = alphabet.index(i)
            
            # new position of letter
            shift_position = position + shift

            if shift_position <= 25:
                # new letter from shifted position
                new_i = alphabet[shift_position]

                # append new text
                new_text += new_i
            else:
                # remainder of 26
                remainder = shift_position % 26

                # new letter from shifted position
                new_i = new_i = alphabet[remainder]
                
                # append new text
                new_text += new_i
        # print output
        print(f"The encoded text is {new_text}.")
    elif direction == "decode":
        
    
    
    
    
    
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt()