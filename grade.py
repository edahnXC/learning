a=int(input("Enter your marks: "))
if a<=100 and a>=80:
    print("Your grade is 'A+'")
elif a<80 and a>=70:
     print("Your grade is 'A'")
elif a<70 and a>=65:
     print("Your grade is 'B+'")
elif a<65 and a>=60:
     print("Your grade is 'B'")
elif a<60 and a>=55:
     print("Your grade is 'C+'")
elif a<55 and a>=50:
     print("Your grade is 'C'")
elif a<50 and a>=40:
     print("Your grade is 'D'")
elif a<40 and a>=0:
    print("You have failed the exam")
else:
    print('Incorrect Input')