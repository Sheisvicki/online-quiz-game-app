# Online Quiz App

#---- The Beginning ----

#-----These are the modules I will be using

import requests
import random
import matplotlib.pyplot as plt

print("Welcome to the Online Ouiz Game!")
player_name = input("What is your name? ")
print(f"Hello {player_name}, Welcome!")

print("Choose Your Category: Movies, Music or General Knowledge") 
category_choice = input("Enter your choice: ").lower()

# Categories
# Using Open Trivia Database API, Looked up the actual Category ID for accuracy.

if category_choice == "movies":
    category_id = 11

elif category_choice == "music":
    category_id = 12

elif category_choice == "general knowledge":
    category_id = 9

else:
    print("Oops! Invalid choice, defaulting to General Knowledge.")
    category_id = 9

# Calling the API. Using Open Trivia Database API. 

def get_questions(category_id):
    url = f"https://opentdb.com/api.php?amount=5&category={category_id}&type=multiple" # Will be using 5 questions for this project
    print(f"Making a request to: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status() # In a case of any errors

        data = response.json()
        return data["results"] 
    except requests.exceptions.RequestException as e:
        print(f"An error occured while fetching questions: {e}")
        return None

# Processinng: Quiz playing part
#-----The Use of functions

while True: # Warped the whole quiz playing part using the "while True" loop so the user/player can play again, instead of the quiz game stoping
    questions = get_questions(category_id)
    score = 0 #The scoring starts at zero 0
    
    for q in questions:
        print(f"\n"+ q["question"]) # This shows the question
        options = q["incorrect_answers"] + [q["correct_answer"]]
        random.shuffle(options)
        
        for i, option in enumerate(options, start=1): # Using emunerate function will make the options and questions look neater and esier to read
            print(f"{i}.{option}")
            
        answer = input("Your answer (1-4): ")
        if options [int(answer)- 1] == q["correct_answer"]:
            print("Yay! That's Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['correct_answer']}")
        
    print(f"\n{player_name}, your Final Score is {score} out of {len(questions)}")

    # I want the program to save scores to a leaderboard

    total = len(questions)
    with open("leaderboard.txt", "a") as file: 
        file.write(f"{player_name} - {score}/{total}\n")
    
    # At the end of the game the leaderboard will show

    print("n\----Leaderboard!----")
    with open("leaderboard.txt", "r") as file:
        print(file.read())
    

    # Inclusion of visualization. Bar Chart: Correct Vs Incorrect
    # The Bar Chart:

    labels = ["Correct", "Incorrect"]
    values = [score, total - score]
    plt.bar(labels, values, color=["green", "red"])
    plt.title(f"{player_name}'s Quiz Results")
    plt.show(block=False) # This shows the chart without stopping the game. Intially the chart was supposed to be the last thing but the player must have an option to continue playing

    input("Press Enter when you are ready to continue...")

    # Asks the player if they would like to play again

    play_again = input("\nDo You Want To Play Again? (yes/no): ").lower()
    
    if play_again != "yes":
        print(f"Thanks for playing {player_name}! Goodbye!")
        break

# ----- The End -----




