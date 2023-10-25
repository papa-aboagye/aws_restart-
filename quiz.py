def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 0  

    for key in questions:
        print("--------------------------")
        print(key)
        for i in options[question_num]:
            print(i)
        guess = input("Enter A, B, or C: ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions[key], guess)  

        question_num += 1  

    display_score(correct_guesses, guesses) 

def check_answer(answer, guess):
    if answer == guess:
        print("Well done!")
        return 1
    else:
        print("WRONG!!!!!!!!!!!")
        return 0

def display_score(correct_guesses, guesses):
    print("---------------")
    print("RESULTS")
    print("---------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions[i], end="")
    print()

def play_again():
    pass


questions = {
    "what is cloud computing?: ": "C",
    "what is the difference between black box testing and white-box testing?: ": "A",
    "what is the primary purpose of a function?: ": "A",
    "what is one way you would troubleshoot a technical problem?: ": "A",
    "which is these is a model of cloud computing?: ": "A",
    "which of these companies use a Saas model of cloud computing?: ": "B",
    "what is a web service?: ": "C",
    "what is the purpose of automatic scaling?: ": "B"
}

options = [["A. cloud computing is refers to the way computers map out cloud formations to predict rainfall", "B. cloud computing is where your data is stored in the sky", "C. cloud computing can be defined as on-demand delivery of compute power, database, storage, applications, and other IT services with a pay-as-you-go pricing."],
           ["A. black box refers to a testing scenario where the internal structure, design, and implementation are unknown to the tester. Whereas white box testing refers to a testing scenario where the internal structure, design, and implementation are known to the tester.", "B. black box refers to a testing scenario where the internal structure, design, and implementation are known to the tester. Whereas white box testing refers to a testing scenario where the internal structure, design, and implementation are unknown to the tester.", "C. Black box testing relies on the system's external behavior, similar to how a user interacts with a program, without considering its internal code. White box testing, on the other hand, looks deep into the code's inner workings, examining data structures, algorithms, and logic."],
           ["A. Reusability", "B. functionality", "scalability"],
           ["A. throw your laptop into the sky and hope the problem is solved by the time it hits the ground", "B. ask stack overflow", "C. quit on the spot"],
           ["A. IaaS", "B. LaaS", "C. QaaS"],
           ["A. salesforce", "B. IBM", "Dropbox"],
           ["A. web service is any piece of software that makes itself available over the internet or on private (internet) networks.", "B. A web service is a protocol for communication between different software applications over the internet, using standardized XML or JSON formats for data exchange.", "C. A web service is a network-based software component that provides a defined set of functionalities and can be invoked and accessed through standard web protocols, typically via HTTP."],
           ["A. it enables resources to scale in and out to match workload demand ", "Is purpose is to automatically store user data in the S3 bucket", "its purpose is to run code"]]

new_game()