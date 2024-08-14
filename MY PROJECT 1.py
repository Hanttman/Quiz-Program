#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Quiz Program

# Dictionary with questions, options, and answers
quiz_questions = {
    "What is the capital of France?": {
        "A": "Berlin",
        "B": "Paris",
        "C": "London",
        "D": "Rome",
        "answer": "B"
    },
    "What is the largest planet in our solar system?": {
        "A": "Earth",
        "B": "Saturn",
        "C": "Jupiter",
        "D": "Uranus",
        "answer": "C"
    },
    "Who painted the Mona Lisa?": {
        "A": "Leonardo da Vinci",
        "B": "Michelangelo",
        "C": "Raphael",
        "D": "Caravaggio",
        "answer": "A"
    },
    "What is the chemical symbol for gold?": {
        "A": "Ag",
        "B": "Au",
        "C": "Hg",
        "D": "Pb",
        "answer": "B"
    },
    "Which planet is known as the 'Red Planet'?": {
        "A": "Earth",
        "B": "Mars",
        "C": "Jupiter",
        "D": "Saturn",
        "answer": "B"
    },
    "Who wrote the famous novel 'To Kill a Mockingbird'?": {
        "A": "F. Scott Fitzgerald",
        "B": "Harper Lee",
        "C": "Jane Austen",
        "D": "J.K. Rowling",
        "answer": "B"
    },
    "What is the largest living species of lizard?": {
        "A": "Komodo dragon",
        "B": "Saltwater crocodile",
        "C": "Black mamba",
        "D": "African elephant",
        "answer": "A"
    },
    "Which musical instrument is often associated with the country of Scotland?": {
        "A": "Piano",
        "B": "Guitar",
        "C": "Bagpipes",
        "D": "Drums",
        "answer": "C"
    },
    "What is the smallest country in the world, both in terms of population and land area?": {
        "A": "Vatican City",
        "B": "Monaco",
        "C": "Nauru",
        "D": "Tuvalu",
        "answer": "A"
    },
    "Who was the first President of the United States?": {
        "A": "George Washington",
        "B": "Thomas Jefferson",
        "C": "Abraham Lincoln",
        "D": "Franklin D. Roosevelt",
        "answer": "A"
    },
    "What is the deepest part of the ocean?": {
        "A": "Mariana Trench",
        "B": "Grand Canyon",
        "C": "Mount Everest",
        "D": "Great Barrier Reef",
        "answer": "A"
    },
    "Which artist painted the famous painting 'The Starry Night'?": {
        "A": "Leonardo da Vinci",
        "B": "Vincent van Gogh",
        "C": "Pablo Picasso",
        "D": "Claude Monet",
        "answer": "B"
    },
    "What is the largest mammal on Earth?": {
        "A": "Blue whale",
        "B": "Fin whale",
        "C": "Humpback whale",
        "D": "Sperm whale",
        "answer": "A"
    }}


# In[ ]:


# Welcome address
print("Welcome to the Hanttman Quiz Program!")
print("Test your knowledge and have fun!")
print("Please choose your answers from the options provided.")
print("Let's get started!\n")


#Initialize score
score = 0

# Iterate over questions
for question, options in quiz_questions.items():
    print(question)
    for option, value in options.items():
        if option != "answer":
            print(f"{option}: {value}")
    answer = input("Choose your answer (A, B, C, D): ")
    if answer.upper() == options["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Sorry, the correct answer is {options['answer']}")

# Print final score
print(f"\nYour final score is {score} out of {len(quiz_questions)}")

# Add a message based on the score
if score >= len(quiz_questions) * 0.7:
    print("Well done! You're a quiz master!")
elif score >= len(quiz_questions) * 0.4:
    print("Good effort! You're getting there!")
else:
    print("Don't worry, keep practicing and you'll get better!")


# Ask user if they'd like to play again
play_again = input("\nWould you like to play again? (yes/no): ").lower()
if play_again == "yes":
    # Restart the quiz
    score = 0
    for question, options in quiz_questions.items():
        print(question)
        for option, value in options.items():
            if option != "answer":
                print(f"{option}: {value}")
        answer = input("Choose your answer (A, B, C, D): ").upper()
        if answer == options["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is {options['answer']}")
    print(f"\nYour final score is {score} out of {len(quiz_questions)}")
else:
    print("Thanks for playing!")


# In[ ]:






# In[ ]:




