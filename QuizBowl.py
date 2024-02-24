# Quiz Bowl Program

# Dictionary of questions and answers
quiz_questions = {
    "1. What is the capital of France?": "Paris",
    "2. What is the largest planet in our solar system?": "Jupiter",
    "3. Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "4. What is the main programming language used for building web pages?": "HTML",
    "5. In which year did the Titanic sink?": "1912"
}

# Function to conduct the quiz
def conduct_quiz(questions):
    score = 0
    for question, answer in questions.items():
        user_answer = input(question + "\nYour Answer: ")
        if user_answer.lower() == answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.\n")
    
    print(f"You scored {score}/{len(questions)} in the quiz.")

# Calling the function to conduct the quiz
conduct_quiz(quiz_questions)