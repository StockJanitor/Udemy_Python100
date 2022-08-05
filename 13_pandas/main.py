import pandas as pd

df = pd.read_csv(r"C:\Users\Gumo\Desktop\Git\Class\Udemy\13_pandas\nato_phonetic_alphabet.csv")
print(df)

l1 = dict(zip(df.letter,df.code))
print(l1)
print("skip line here ~~~~~~~~~~~~~~~~~~~~~~~\n\n")

l2 = {row.letter:row.code for (index,row) in df.iterrows()}
print(l2)