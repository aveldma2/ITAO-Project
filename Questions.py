class Question:
    def __init__(self, type, numanswers):
        self.type = type
        self.numanswers = numanswers

if input('do you want to enter a new question') == 'Yes':
    question = input('What is your question?')
    questiontype = input('Is this a yes or no question')
    numanswers = int(input('How many answers are there?'))

for i in range(numanswers):
    print('one more answer')
