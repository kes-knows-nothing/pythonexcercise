import csv
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


dict_from_csv = pandas.read_csv('nato_phonetic_alphabet.csv')
new_dict = {row.letter: row.code for (index, row) in dict_from_csv.iterrows()}


def code():
    word = input("Enter a word: ").upper()

    try:
        s_code = [new_dict[code] for code in word]

    except KeyError:
        print("Sorry, only letters in the alphabet please")
        code()
    else:
        print(s_code)



code()
