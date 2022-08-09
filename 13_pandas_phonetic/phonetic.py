import pandas as pd

path = r"C:\Users\Gumo\Desktop\Git\Class\Udemy\13_pandas\nato_phonetic_alphabet.csv"
df = pd.read_csv(path)

phonetic_dict = dict(zip(df.letter,df.code))

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()