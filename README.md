# online-quiz-game-app
Python project: Interactive quiz game app, with API based questions and score tracking


Final Project: Online Quiz App


Description:

This Python based quiz game allows players to choose between three trivia categories: Movies, Music, and General Knowledge. 
The game fetches questions in real time from the Open Trivia Database API, shuffles the answer options, and tracks the player’s score.
At the end of each round, the results are displayed along with a bar chart comparing correct and incorrect answers, and scores are saved to a leaderboard for reference.



Planning and Detailed Description: Online Quiz App

1. What does your app do?

My app is a Python based Online Quiz Game that lets players choose from three categories: Movies, Music, and General Knowledge. 
The game greets the player, asks for their name, and uses the Open Trivia Database API to fetch multiple-choice questions from the chosen category. 
The player answers the questions, and the app tracks their score and gives feedback after each answer. At the end, the game shows the player’s total score and saves it to a leaderboard.


2. What features will it include?

●	A greeting and name input.
●	Category selection between Movies, Music, and General Knowledge.
●	Live questions fetched from an API instead of hardcoding them.
●	Multiple-choice answers in random order.
●	Score tracking with feedback for correct and incorrect answers.
●	Leaderboard that stores results in a text file.
●	A bar chart using Matplotlib showing correct vs incorrect answers.


3. The concepts I will apply?

●	Variables for storing names, scores, and category IDs.
●	Conditionals (if/elif/else) for choosing quiz categories.
●	Loops (for) for displaying questions and answers.
●	Functions to separate tasks like getting questions from the API.
●	Lists & dictionaries for storing questions, answer options, and correct answers.
●	Modules such as requests for the API, random for shuffling answers, and matplotlib for creating the bar chart.
●	File handling to create and update the leaderboard text file. (Stores results)






Challenges & Concerns

Before starting, I was concerned about how to:

●	Correctly fetching and displaying the API data. (I was concerned about the type of API I will use, I planned on using three categories so I thought I had to use three separate APIs. 
After research, I found that it wouldn't be an issue and I only needed one API).
●	Manage three categories without making the code too complex. 
●	Making sure API questions display cleanly. (The enumerate function helped me out with this)
●	Tracking the scores while giving feedback for each question. 
●	Use lists, dictionaries, loops, and functions effectively without complicating the code.
●	Another challenge was finding a way to loop the game so that when the player is done with one game, they could have the choice to play again and end the game.
●	Finding a way to include the bar chart before the player can choose to continue or end the game. 


This project helped me consolidate everything I learned in the course while also learning how to interact with real-world APIs and a little bit of some advanced applications. 
Overall, this was a fun, challenging and interesting proje
