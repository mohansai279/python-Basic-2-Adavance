import quiz_Database
import quiz_Database

score = 0

def check_answer(user_guess, correct_answer):
    return user_guess == correct_answer

for question_num in range(len(quiz_Database.question_bank)):
    print("********************************")
    print(quiz_Database.question_bank[question_num]["text"])
    for i in quiz_Database.options[question_num]:
        print(i)

    guess = input("Enter your answer (A/B/C/D): ").upper()
    is_correct = check_answer(guess, quiz_Database.question_bank[question_num]["answer"])

    if is_correct:
        print("Correct Answer")
        score += 1
    else:
        print("Incorrect Answer")
        print(f"The correct answer is {quiz_Database.question_bank[question_num]['answer']}")

    print(f"Your current score is {score}/{question_num+1}")

print(f"Your final score is {score}")
print(f"Your score percentage is {(score / len(quiz_Database.question_bank)) * 100:.2f}%")



