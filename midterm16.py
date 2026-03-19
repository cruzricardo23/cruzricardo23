#Ricardo Cruz
#Midterm
#Question 16





x = 0
secret = 8

while x != secret:
    x=float(input("guess a number between 1 and 10"))

    if x < secret:
        print("go higher", x) 

    elif x> secret:
        print("go lower", x)

    else:
        print("8 is correct")


