
#class for the questions and answeres
class Questions:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompt = [
    "1. What are variables used for?\nA - Variables are used to store information to be referenced and manipulated in a computer program and can change throughout the life cycle of a program.\nB - Variables are used to store information that will never change\nC - sdjhdsjhfdhjsdfdbfhsd.",
    "2. How many leaves are in a tree?\nA - 23\nB - 45\nC - 78",
    "3. What will this code print? code: prin(Hello).\nA. Hello\nB. A traceback error will be thrown\nC. Nothing will happen.",
    "4. Which of the following best describe this statement : print()?\nA. text\nB. An error message\nC. Python built in function",
    "5. What do we use to break ou of a loop?\nA. continue\nB. while loop\nC. break\n\n"
]
#A Question object
questions = [
    Questions(question_prompt[0], "A"),
    Questions(question_prompt[1], "C"),
    Questions(question_prompt[2], "B"),
    Questions(question_prompt[3], "C"),
    Questions(question_prompt[4], "B")
]

def test(quastions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("The score is: "+ str(score)+ "/"+ str(len(quastions)))

test(questions)
