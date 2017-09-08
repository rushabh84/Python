# Author: Rushabh Shah
# Original Creation Date: 04/19/17
# Last modification date: 04/21/17
#Description: This program creates objects of class Question which has set of 10 questions, options to that answers and position of the correct answer
             #asks 5 questions to two players and once players give answers to each question asked to them, checks which player guessed more answers correctly and declares him winner


#class Question has attributes like question, four options for that question and the position of the correct question
class Question:
    opt1 = 0
    opt2 = 0
    opt3 = 0
    opt4 = 0
    question = ''
    correct = 0  #this is not the correct answer, but the position of the correct option from the options list passed to the __init__ method
    def __init__(self, question, correct, options):
        self.question = question
        self.opt1 = options[0]
        self.opt2 = options[1]
        self.opt3 = options[2]
        self.opt4 = options[3]
        self.correct = correct

    #this function creates objects of class Question. qp1 is list with 5 questions for player 1, qp2 is for player 2. ap1 is list with answers to 5 questions for player 1 and sp2 is for player 2
    #o1 and o2 are list of options where an element is a list of 4 options
    def set_questionset(qp1, qp2, ap1, ap2, o1, o2):
        per = []  #list that will store objects of class Question
        for i in range(0,len(qp1)):
            per.append(Question(qp1[i], ap1[i],o1[i]))  #append Question object to list 'per'

        for i in range(0,len(qp2)):
            per.append(Question(qp2[i], ap2[i], o2[i]))   #append Question object to list 'per'
        return per

    def get_questionset():
        return self.question
                
            

        

#this function displays the question and its options to player one and player two, takes their input for respective question and evaluates who answered more correctly
def ask_Questions(final):
    print("Player one and two, welcome to the game. It's a round of 5 questions each first, player one goes 1st and then player two. Lets start")
    right1 = 0
    right2 = 0

    for j in range(5):
        print('Player one: your turn: Question ',j+1)
        print(final[j].question)
        print('1.',final[j].opt1,' ','2.',final[j].opt2,' ','3.',final[j].opt3,' ','4.',final[j].opt4)
        while True:  #while loop handles if the player inputs incorrct option which may be just enter, string, and loops unless player gives correct input
            try:
                choice = int(input('What is your choice?'))
                if choice <=4 and choice >=1:  #this condtion checks the int input is not 1,2,3 or 4
                    break
                else:
                    print('Please enter options from 1,2,3,4')
            except ValueError:
                print('Please enter valid choice for this question. Pick options from 1,2,3 or 4')
        if choice == final[j].correct :  #if player answered the correct answer for this question, increase the accumulator variable 'right1' by one.
            right1 += 1

        print('Player two: your turn: Question ',j+1)
        print(final[j+5].question)
        print('1.',final[j+5].opt1,' ','2.',final[j+5].opt2,' ','3.',final[j+5].opt3,' ','4.',final[j+5].opt4)
        while True:  #while loop handles if the player inputs incorrct option which may be just enter, string, and loops unless player gives correct input
            try:
                choice = int(input('What is your choice?'))
                if choice <=4 and choice >=1:  #this condtion checks the int input is not 1,2,3 or 4
                    break
                else:
                    print('Please enter options from 1,2,3,4')
                
            except ValueError:
                print('Please enter valid choice for this question. Pick options from 1,2,3 or 4')
        if choice == final[j+5].correct:  #if player two answered the correct answer for this question, increase the accumulator variable 'right2' by one.
            right2 += 1

    #display points earned by both the players
    print('Points earned by player one are: ',right1)
    print('Points earned by player two are: ',right2)
    #check which player has higher score and declare that player as the winner
    if right1 > right2:
        print('Player one wins')
    elif right2 > right1:
        print('Player two wins')
    else:
        print("It's a draw between person one and person two")
                     

#calls all other functions, and has dictionary for 10 questions, another one with options to those questions and third one with position of correct option    
def main():
    test = {1: 'What is value of 10*2-1?',2:'What is value of 10-10?',3:'What is value of 1*2-1?',4:'What is value of 1000*2/1000?',5:'What is value of 10*2?',6:'What is value of 10*0?',7:'What is value of 10+10+10-1?',8:'What is value of 10*2*2/2?',9:'What is value of 10*10?',10:'What is value of 10-10*2?'}
    options = {1:[19,8,18,20],2:[0,5,1,3],3:[2,1,3,4],4:[1,2,3,5],5:[19,15,20,18],6:[0,1,-1,4],7:[28,27,29,20],8:[12,13,14,20],9:[100,101,90,80],10:[1,0,2,-1]}
    answer = {1:1, 2:1, 3:2, 4:2, 5:3, 6:1, 7:3, 8:4, 9:1, 10:2}  #dictionary that stores the position of correct answer in options dictionary
    
    #below are dummy lists to extract all the questions, options and positon of correct answer and pass it to createObjects method
    quest_list = []
    ans_list = []
    opt_list =[]
    questionsp1 = []
    questionsp2 = []
    answersp1 = []
    answersp2 = []
    opt1 =[]
    opt2 = []

    for key in test:
        quest_list.append(test.get(key))  #gets all the questions from dictionary test in the quest_list
        ans_list.append(answer.get(key))  #gets all the answers from dictionary answer in the ans_list
        opt_list.append(options.get(key))
    #this for loop creates 2 sepearte questions and answers list for player one and player two

    for i in range(5):
        questionsp1.append(quest_list[i])  #list with 5 questions for player 1
        answersp1.append(ans_list[i])  #list with 5 answers for player 1
        opt1.append(opt_list[i])  #list with 5 options list for player 1
        questionsp2.append(quest_list[i+5])
        answersp2.append(ans_list[i+5])
        opt2.append(opt_list[i+5])
    
    allquestions = Question.set_questionset(questionsp1, questionsp2, answersp1, answersp2,opt1, opt2)  #call setter method setquestionset, which returns a list with 10 objects of class Question
    ask_Questions(allquestions)  #Using the list allquestions, ask 5 questions each to player one and player two, and evaluate who answered mored questions correctly
    
#starting point of the program        
main()
   






        
