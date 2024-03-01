import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dic = {row.letter:row.code for (index, row) in alphabet.iterrows()}

while True:
    user_inp = input("Enter a word: ").upper()
    try: 
        list = [nato_dic[letter] for letter in user_inp]

    except KeyError:
        print("sorry, only letters of the alphabet")
    else:
        print(list)
        break
    
    
    



