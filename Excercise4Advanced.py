dictionary = {
    "What is the capital of france: ": "paris",
    "Who is the queen of england: ": "queen",
    "What is the capital of Germany? ": "berlin",
    "What is the capital of Italy?: ":  "rome",
    "What is the capital of Spain?: ": "madrid",
    
}
#I've made a dictionary and a function to loop each variable and ask for the user input,
#Whilst also verifying the answers if its correct or not, the ignoring capitalization by
#making the answer lowercase.
def QuestionAnswer(question,correct_answer):
    answer = input(question)
    answer = answer.lower()
    if answer == correct_answer:
        print("You are correct!")
    else:
        print("You are wrong, Try Again!")

for question,answer in dictionary.items():
    QuestionAnswer(question,answer)



