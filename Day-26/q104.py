def quiz():
    score=0
    print("1.What is the capital of Jharkhand?")
    print("2.What is the capital of India?")
    print("3.where is Taj mahal located?")
    print("4.How many states are there in India?")

    q1answer=str(input("Enter your answer1: "))
    q2answer=str(input("Enter your answer2: "))
    q3answer=str(input("Enter your answer3: "))
    q4answer=str(input("Enter your answer4: "))
    if q1answer.lower()=="ranchi":
        print("your answer1 is correct")
        score+=1
    else:
        print(f"wrong! The correct answer is Ranchi.")
    if q2answer.lower()=="delhi":
        print("your answer2 is correct")
        score+=1
    else:
        print(f"wrong! The correct answer is Delhi.")
    if q3answer.lower()=="agra":
        print("your answer3 is correct")
        score+=1
    else:
        print(f"wrong! The correct answer is Agra.")
    if q4answer.lower()=="28":
        print("your answer4 is correct")
        score+=1
    else:
        print(f"wrong! The correct answer is 28.")

    print(f"Your final score is {score} out of 4")

quiz()