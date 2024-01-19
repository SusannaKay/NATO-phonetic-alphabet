import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dic = {row.letter:row.code for (index, row) in alphabet.iterrows()}
user_inp = input("Enter a word: ").upper()
list = [nato_dic[letter] for letter in user_inp]


print(list)

