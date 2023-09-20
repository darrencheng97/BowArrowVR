from question import Question # 从question.py 引入 Question Class 而已

test = [
    "1 + 3 = ???\n (a) 2\n (b) 3\n (c) 4\n\n Enter your answer here: ",
    "1 meter equal to how many centimeter (cm)?\n(a) 10\n(b) 100\n(c) 1000\n\n Enter your answer here: ",
    "What is banana colour?\n (a) BLACK\n (b) YELLOW \n (c) WHITE\n\n Enter your answer here: "
]

questions = [
    Question(test[0],"c"),
    Question(test[1],"b"),
    Question(test[2],"b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.description)
        if answer == question.answer:
            score+=1
    
    print("You scored: "+str(score)+", Total Question: "+str(len(questions)))

run_test(questions)