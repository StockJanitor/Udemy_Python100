from art import logo
print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


##################################################################################################################################

def caesar(cipher_direction, plain_text,shift_amount):
    
    #initialize end text
    end_text = ""

    # identify direction
    if cipher_direction == 'decode':
        shift_amount *= -1

    #for loop - each letter
    for letter in text:
        if letter not in alphabet:
            end_text += letter
        else:
            # find position
            position = alphabet.index(letter)

            # shift position
            shift_position = position + shift_amount

            # if shift amount pass list index, we get remainder
            if shift_position >25:
                shift_position %= 26

            # append the letter to end_text
            end_text += alphabet[shift_position]

    #print result
    print(f"The {direction}d text is {end_text}.")

again = True
while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction,text,shift)
    go_again = input("Type 'yes' if you want to go again. Otherwise type'no'.\n")
    if go_again !="yes":
        again = False
        print('Goodbye~')