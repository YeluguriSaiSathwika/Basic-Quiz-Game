def display_question(question_data, question_number):
    """Displays a question and its multiple-choice options."""
    print(f"\nQuestion {question_number + 1}:\n\n{question_data['question']}")
    print()
    for option in question_data['options']:
        print(option)

def get_user_input():
    """Gets and validates user input."""
    user_answer = input("Your answer (A, B, C, or D): ").upper()
    while user_answer not in ['A', 'B', 'C', 'D']:
        print("Invalid input. Please enter A, B, C, or D.")
        user_answer = input("Your answer (A, B, C, or D): ").upper()
    return user_answer

def provide_feedback(user_answer, correct_answer):
    """Provides feedback to the user on their answer."""
    if user_answer == correct_answer:
        print()
        print("Correct!")
        return True
    else:
        print()
        print(f"Incorrect. The correct answer was {correct_answer}.")
        return False

"""Main function to run the quiz game."""
questions = [
    {
        "question": "Which of the following is used to define a block of code in Python?",
        "options": ["A. Curly braces {}", "B. Parentheses ()", "C. Indentation", "D. Semicolons ;"],
        "answer": "C"
    },
    {
        "question": "What is the purpose of the `self` keyword in Python classes?",
        "options": ["A. To indicate a private variable", "B. To refer to the class itself", "C. To refer to the instance of the class", "D. To refer to a global variable"],
        "answer": "C"
    },
    {
        "question": "What is the time complexity of accessing an element in a dictionary in Python?",
        "options": ["A. O(1)", "B. O(log n)", "C. O(n)", "D. O(n log n)"],
        "answer": "A"
    },
    {
        "question": "Which method is used to remove and return an element from a set in Python?",
        "options": ["A. remove()", "B. discard()", "C. pop()", "D. delete()"],
        "answer": "C"
    },
    {
        "question": "What will be the output of the following code snippet?\n\nmy_list = [1, 2, 3, 4]\nprint(my_list[1:3])",
        "options": ["A. [1, 2]", "B. [2, 3]", "C. [3, 4]", "D. [2, 3, 4]"],
        "answer": "B"
    },
    {
        "question": "Which of the following is not a valid data type in Python?",
        "options": ["A. list", "B. tuple", "C. map", "D. dict"],
        "answer": "C"
    },
    {
        "question": "How do you create a dictionary in Python?",
        "options": ["A. d = {}", "B. d = []", "C. d = ()", "D. d = set()"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A. def", "B. func", "C. function", "D. create"],
        "answer": "A"
    },
    {
        "question": "What is the output of the following code: `print(2 ** 3)`?",
        "options": ["A. 5", "B. 6", "C. 8", "D. 9"],
        "answer": "C"
    },
    {
        "question": "Which of the following data types is immutable in Python?",
        "options": ["A. list", "B. dict", "C. set", "D. tuple"],
        "answer": "D"
    },
    {
        "question": "What does the `len()` function do in Python?",
        "options": ["A. Returns the length of an object", "B. Converts a value to an integer", "C. Calculates the sum of a list", "D. Reverses a string"],
        "answer": "A"
    },
    {
        "question": "Which method is used to add an element to the end of a list in Python?",
        "options": ["A. add()", "B. append()", "C. insert()", "D. extend()"],
        "answer": "B"
    },
    {
        "question": "Which of the following is a Python tuple?",
        "options": ["A. [1, 2, 3]", "B. {1, 2, 3}", "C. (1, 2, 3)", "D. <1, 2, 3>"],
        "answer": "C"
    },
    {
        "question": "What is the result of `3 + 2 * 2` in Python?",
        "options": ["A. 7", "B. 10", "C. 8", "D. 11"],
        "answer": "A"
    },
    {
        "question": "Which of the following functions can be used to find the largest number in a list?",
        "options": ["A. max()", "B. min()", "C. largest()", "D. big()"],
        "answer": "A"
    }
]

score = 0
total_questions = len(questions)

for i, question in enumerate(questions):
    display_question(question, i)
    user_answer = get_user_input()
    if provide_feedback(user_answer, question['answer']):
        score += 1
    print()
    
percentage_score = (score / total_questions) * 100
print(f"\nYour final score is {score}/{total_questions}.")
print(f"Your total percentage is {percentage_score:.2f}%.")

