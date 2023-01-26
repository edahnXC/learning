day=int(input("enter the day number: "))   
if day in [1,8,15,22,29]:
   print("it's Sunday")
elif day in [2,9,16,23,30]:
   print("it's Monday")
elif day in [3,10,17,24,31]:
   print("it's Tuesday")
elif day in[4,11,18,25]:
   print("it's Wednesday")
elif day in[5,12,19,26]:
   print("it's Thursday")
elif day in[6,13,20,27]:
   print("it's Friday")
elif day in[7,14,21,28]:
   print("it's Saturday")
else:
   print("day entered is not correct")
      
