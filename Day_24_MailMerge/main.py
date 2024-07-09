# # Local File 
# # and 
# # Directors

HOLDER = '[name]'

with open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()
    

with open('./Input/Letters/starting_letter.txt') as letter_file:
    temp = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = temp.replace(HOLDER, stripped_name)
        with open(f'./Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as completed_letter:
            completed_letter.write(new_letter)


