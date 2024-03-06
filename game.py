import random


quiz_questions = {
    "What is the capital of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the chemical symbol for water?": "H2O",
    "What is the largest mammal in the world?": "Blue whale",
    "What is the tallest mountain in the world?": "Mount Everest"
}


def display_welcome_message():
    print("Welcome to the Quiz Game!")
    print("You will be asked a series of multiple-choice or fill-in-the-blank questions.")
    print("You will receive feedback on correct/incorrect answers.")
    print("Let's get started!\n")


def present_quiz_questions():
    questions = list(quiz_questions.keys())
    random.shuffle(questions)
    score = 0

    for question in questions:
        print(question)
        user_answer = input("Your answer: ").strip()

        correct_answer = quiz_questions[question]
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect! The correct answer is:", correct_answer)
        
        print()  

    return score


def display_final_results(score, total_questions):
    print("Quiz completed!")
    print("You got {} out of {} questions correct.".format(score, total_questions))
    print("Thanks for playing!")


def main():
    display_welcome_message()

    play_again = "yes"
    while play_again.lower() == "yes":
        score = present_quiz_questions()
        total_questions = len(quiz_questions)
        display_final_results(score, total_questions)
        play_again = input("Do you want to play again? (yes/no): ").strip()

if __name__ == "__main__":
    main()
