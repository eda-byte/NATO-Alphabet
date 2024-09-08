import pandas as pd


#TODO 1. Create a dictionary in this format:
df = pd.read_csv("nato_phonetic_alphabet.csv")
new_dict=dict(df.values)
#print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

nato_dict = dict(zip(df['letter'], df['code']))

#nato_dict_loop={letters: codes for (index, row) in df.iterrows()}
#print(nato_dict)
#
write_name=input("Enter a word:").upper()
#

phonetic_list = [nato_dict[letter]for letter in write_name]

print(phonetic_list)
 #


#new_list=[letter for letter in write_name if dict(df.values)= ]
#print(new_list)
