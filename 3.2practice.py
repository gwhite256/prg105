# Get the users credit score
credit_score = int(input("What is your credit score? "))

if credit_score >= 720:
    print("You have an excellent Credit Score")
elif credit_score >= 690:
    print("You have a good Credit Score")
elif credit_score >= 630:
    print("You have a fair Credit Score ")
else:
    print("You have a bad Credit Score")
