PLACEHOLDER = "[name]"

with open("/Users/82104/Desktop/Python Workspace/pycharm/day 24/challenge/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("/Users/82104/Desktop/Python Workspace/pycharm/day 24/challenge/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"/Users/82104/Desktop/Python Workspace/pycharm/day 24/challenge/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)



# letter = open(, "r")
#
# b = letter.readlines()
# # print(letter.readlines())
#
# d = b[0]
#
# revised_name = []
#
# for name in a:
#     c = d.replace("[name]", name)
#     revised_name.append(c)
#
# revised_letter = []
#
# for number in range(0, 8):
#     b[0] = revised_name[number]
#     revised_letter.append(b)
#
# print(revised_letter)
#
#
# for namae in revised_letter:
#     with open(f"/Users/82104/Desktop/Python Workspace/pycharm/day 24/challenge/Output/ReadyToSend/{d}.txt", mode="w") as fin:
#         fin.write("New text.")
#
#
#
#
#
#
#
#
#
