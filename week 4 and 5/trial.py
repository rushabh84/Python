class Question:
    opt1 = 0
    opt2 = 0
    opt3 = 0
    opt4 = 0
    question = ''
    correct = 0
    def __init__(self, question, correct):
        self.question = question
        self.opt1 = correct
        self.opt2 = correct+2
        self.opt3 =correct-1
        self.opt4 = correct-2
        self.correct = correct
            
            
#this function creates objects of class Question
def createObjects(qp1, qp2, ap1, ap2):
    questionobj =[]
    answerobj = []
    per = []
    for i in range(0,len(qp1)):
        questionobj.append(qp1[i])
        answerobj.append(ap1[1])
        per.append(Question(qp1[i], ap1[i]))

    for i in range(0,len(qp2)):
        questionobj.append(qp2[i])
        answerobj.append(ap2[i])
        per.append(Question(qp2[i], ap2[i]))
    return per      
        


def ask_Questions(final):
    print('Person one please answer the following 5 questions')
    right1 = 0
    right2 = 0
    for j in range(5):
        print(final[j].question)
        print('1.',final[j].opt1,' ','2.',final[j].opt2,' ','3.',final[j].opt3,' ','4.',final[j].opt4)
        choice = int(input('What is your choice?'))
        if choice == final[j].correct :
            right1 += 1
    print('Person one please answer the following 5 questions')
    for j in range(5):
        print(final[j+5].question)
        print('1.',final[j+5].opt1,' ','2.',final[j+5].opt2,' ','3.',final[j+5].opt3,' ','4.',final[j+5].opt4)
        choice = int(input('What is your choice?'))
        if choice == final[j+5].correct:
            right2 += 1
    print('Points earned by player one are: ',right1)
    print('Points earned by player two are: ',right2)
    if right1 > right2:
        print('Person one wins')
    elif right2 > right1:
        print('Person two wins')
    else:
        print("It's a draw between person one and person two")
                     

    
def main():
    test = {1: 'What is value of 10*2-1?',2:'What is value of 10-10?',3:'What is value of 1*2-1?',4:'What is value of 1000*2/1000?',5:'What is value of 10*2?',6:'What is value of 10*0?',7:'What is value of 10+10+10-1?',8:'What is value of 10*2*2/2?',9:'What is value of 10*10?',10:'What is value of 10-10*2?'}
    answer = {1:19, 2:0, 3:1, 4:2, 5:20, 6:0, 7:29, 8:20, 9:100, 10:0}
    i=0
    quest_list = []
    ans_list = []
    questionsp1 = []
    questionsp2 = []
    answersp1 = []
    answersp2 = []
    for key in test:
        quest_list.append(test.get(key))
        ans_list.append(answer.get(key))
    for i in range(5):
        questionsp1.append(quest_list[i])
        answersp1.append(ans_list[i])
        questionsp2.append(quest_list[i+5])
        answersp2.append(ans_list[i+5])
    print(questionsp1)
    print(questionsp2)
    allquestions = createObjects(questionsp1, questionsp2, answersp1, answersp2)
    ask_Questions(allquestions)
    
        
main()
   


