score = int(input("Enter a student's score."))

if score >= 90:
    print("The student's score of " + str(score) +  " is an A")
else:
    if score >= 80:
        print("The student's score of " + str(score) + " is a B")
    else:
        if score >= 70:
            print("The student's score of " + str(score) + " is a C")
        else:
            if score >= 60:
                print("The student's score of " + str(score) + " is a D")
            else: 
                print("The student's score of " + str(score) + " is a F")