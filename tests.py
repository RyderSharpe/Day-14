import random
from game_data import data

def select_individual():
    """Randomly select an individual from the dataset."""
    return random.choice(data)

def compare_followers(individual1, individual2):
    """Compare the number of followers between two individuals."""
    return individual1['follower_count'] > individual2['follower_count']

def main():
    score = 0
    current_individual = select_individual()  # Start with a randomly selected individual
    while True:
        new_individual = select_individual()  # Select a new individual for comparison
        print(f"Who has more followers? {current_individual['name']} or {new_individual['name']}?")
        user_guess = input("Enter '1' or '2': ")

        if (user_guess == '1' and compare_followers(current_individual, new_individual)) or \
           (user_guess == '2' and compare_followers(new_individual, current_individual)):
            print("Correct!")
            score += 1
            current_individual = new_individual  # Move to the new individual for the next comparison
        else:
            print("Wrong! Game Over.")
            break

    print(f"Your final score is {score}.")

if __name__ == "__main__":
    main()


