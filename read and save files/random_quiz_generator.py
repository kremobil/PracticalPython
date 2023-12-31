import os
import random

capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

folder_name = input("Input the name of the folder you want to store tests in: ")
folder_name = folder_name.replace(" ", "_")

if not os.path.exists(folder_name):
    os.mkdir(folder_name)

for quiz_number in range(35):
    quiz_file = open(f"{folder_name}/capitals quiz{quiz_number + 1}.txt", "w")
    answer_key_file = open(f"{folder_name}/capitals quiz answers{quiz_number + 1}.txt", "w")

    quiz_file.write("name: \n\ndate: \n\n")
    quiz_file.write((" " * 20) + f"USA states capitals quiz {quiz_number + 1}: \n\n")

    states = list(capitals.keys())
    random.shuffle(states)

    for quiestion_number in range(50):
        correct_answer = capitals[states[quiestion_number]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        quiz_file.write(f"\n{quiz_number + 1}. Capital of {states[quiestion_number]} is:\n")
        for i in range(4):
            quiz_file.write(f"\t{'abcd'[i]}) {answer_options[i]}\n")

        answer_key_file.write(f"{quiestion_number + 1}. {'abcd'[answer_options.index(correct_answer)]}\n")
    quiz_file.close()
    answer_key_file.close()

