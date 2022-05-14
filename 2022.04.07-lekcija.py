"""
#  Иерархия

x=35e3
if x>0:
    print("POSITIVE!")
elif x<0:
    print("NEGATIVE")
elif x==0:
    print(0)
else:
    print("Error!!!")
"""

"""
myStr = int(input("Please,input even number:"))

if myStr%2==0 and myStr>0:
    print(f"{myStr} is EVEN!")
elif myStr<0:
    print("Negative!")
elif myStr==0:
    print("Your number is 0!")
else:
    print("Not EVEN!!!")
"""

# mynum = int(input("Please,input number:"))
# print(mynum>=0 and mynum<=9)

# mynum = int(input("Please,input number:"))
# mynum = 99
# print(not(mynum>=0 or mynum<=9))

"""
mynum = 45
if mynum>0 and (mynum%3==0 or mynum%5==0):
    print("Positive, devisible by 3 and 5!")
else:print("NO!!!!")
"""

####### CYCLES-LOOPS ########

"""myList = ["el1","el2","el3"]
for i in myList:
    print(i)"""

# sum=0
# for i in range(10,5,-2):
#     print(i)

myTxt = ["el1","el2","el3"]
for element in myTxt:
    print(f"Sveiki,{element}!")