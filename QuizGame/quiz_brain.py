from question_model import question_bank

for question in question_bank:
    print(question.text)
    user_ans = input("Enter is above is 'True' or 'False'.")
    if user_ans == question.answer:
        print("You are correct!")
    else:
        print("Sorry, You are incorrect")

print("Quiz over. Thank you for playing.")


