import random
from game_data import data

score = 0  # Initialize score
current_name = None  # Initialize current_name to start the chain

while True:
    if not current_name:  # If starting a new chain
        name1 = random.choice(data)["name"]
        current_name = name1
    else:
        name1 = current_name  # Use the previous winner as name1

    name2 = random.choice(data)["name"]  # Always select a new name2

    # Find follower counts as before
    follower_count1 = next(entry["follower_count"] for entry in data if entry["name"] == name1)
    follower_count2 = next(entry["follower_count"] for entry in data if entry["name"] == name2)

    def answer():
        # Compare the follower counts
        if follower_count1 > follower_count2:
            print(f"Pssst {name1} has more followers than {name2}.\n")
        elif follower_count1 < follower_count2:
            print(f"Pssst {name2} has more followers than {name1}.\n")
        else:
            print(f"Pssst {name1} and {name2} have the same number of followers.\n")

    print(f"\nWho has more followers?: {name1} or {name2}?\n")
    answer()  # Call the answer() function for debugging

    user_input = input("Guess who has more followers: ")

    if user_input.lower() == name1.lower():
        if follower_count1 > follower_count2:
            print("Correct!")
            score += 1
            current_name = name1  # Keep name1 as the current_name for the next comparison
        else:
            print("You lose!")
            break  # Exit the loop when a wrong guess is made
    elif user_input.lower() == name2.lower():
        if follower_count2 > follower_count1:
            print("Correct!")
            score += 1
            current_name = name2  # Update current_name to name2 for the next comparison
        else:
            print("You lose!")
            break
    else:
        print("Invalid input.")

print(f"You have reached the end of the game. Your score is {score}. Thank you for playing!")

