class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.num_answers = 1
        print('The question is', question)
        print('The answer is', answer)

    def show_options(self):
        raise 'Question must overwrite answer method'

class MultipleChoice(Question):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.num_answer_options = 4
        print('The question is', question)
        print('The answer is', answer)

    def show_options(self):
        self.answer_options = ['A', 'B', 'C', 'D']

class FreeResponse(Question):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.num_answer_options = 1
        print('The question is', question)
        print('The answer is', answer)

    def show_options(self):
        print('Free Response')

class TrueFalse(Question):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.num_answer_options = 2
        print('The question is', question)
        print('The answer is', answer)

    def show_options(self):
        self.answer_options = ['T', 'F']
