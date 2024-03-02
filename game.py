# https://www.higherlowergame.com/

import random
from game_data import data
score = 0 # Initialize score outside the loop
stop = False
while not stop:


    # Randomly select two names
    name1 = random.choice(data)['name']
    name2 = random.choice(data)['name']

    # Find the follower counts of the selected names
    follower_count1 = next(entry['follower_count'] for entry in data if entry['name'] == name1)
    follower_count2 = next(entry['follower_count'] for entry in data if entry['name'] == name2)

    # Who has more followers?
    print(f"Who has more followers?: {name1} or {name2}?\n")

    def answer():
        # Compare the follower counts
        if follower_count1 > follower_count2:
            print(f"Pssst {name1} has more followers than {name2}.\n")
        elif follower_count1 < follower_count2:
            print(f"Pssst {name2} has more followers than {name1}.\n")
        else:
            print(f"Pssst {name1} and {name2} have the same number of followers.\n")
    def compare(user_input, name1, name2):
        global stop
        global score
        if user_input.lower() == name1.lower():
            if follower_count1 > follower_count2:
                print('Correct')
                score += 1
            else:
                print('You lose!')
                stop = True
        elif user_input.lower() == name2.lower():
            if follower_count2 > follower_count1:
                print('Correct!')
                score += 1
            else:
                print('You lose!')
                stop = True
        else:
            print('Invalid input.')

    answer()
    user_input = input('Guess who has more followers: ')
    compare(user_input, name1, name2)
print(f"You have reached the end of the game. Your score is {score}. Thank you for playing!")
