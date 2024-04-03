from data import question_data


class Question:
    def __init__(self, qtext, qans):
        self.text = qtext
        self.answer = qans


question_bank = []
for question in question_data:
    q = question["question"]
    ans = question["correct_answer"]
    new_question = Question(q, ans)
    question_bank.append(new_question)



