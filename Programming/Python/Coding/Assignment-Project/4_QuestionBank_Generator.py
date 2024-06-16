import random

def create_question(question_number):
    question_text = input(f"Enter the question for Question {question_number}: ")
    choices = []
    for i in range(1, 4): 
        choice = input(f"Enter choice {i} for Question {question_number}: ")
        choices.append(choice)
    correct_answer = input(f"Enter the correct answer (1, 2, or 3) for Question {question_number}: ")

    return {
        "question_text": question_text,
        "choices": choices,
        "correct_answer": correct_answer
    }

def generate_question_bank(num_questions):
    question_bank = []
    for question_number in range(1, num_questions + 1):
        question = create_question(question_number)
        question_bank.append(question)
    return question_bank

def main():
    num_questions = int(input("Enter the number of questions you want to generate: "))
    question_bank = generate_question_bank(num_questions)

    for question_number, question in enumerate(question_bank, start=1):
        print(f"Question {question_number}:")
        print(question["question_text"])
        for i, choice in enumerate(question["choices"], start=1):
            print(f"{i}. {choice}")
        
        user_answer = input("Your answer (1, 2, or 3): ")

        if user_answer == question["correct_answer"]:
            print("Correct!\n")
        else:
            print(f"Wrong. The correct answer is {question['correct_answer']}\n")

if __name__ == "__main__":
    main()
