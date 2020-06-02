import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'one'
    elif answerNumber == 2:
        return 'two'
    elif answerNumber == 3:
        return 'three'
    elif answerNumber == 4:
        return 'four'
    elif answerNumber == 5:
        return 'five'

r = random.randint(1,5)
string = getAnswer(r)
print(string)
        
