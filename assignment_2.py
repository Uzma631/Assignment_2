#1. Write a program which takes 5 inputs from user for different subject’s
#marks, total it and generate mark sheet using grades ?

math=int(input("enter the maths marks"))
eng=int(input("enter the english marks"))
phy=int(input("enter the physics marks"))
chem=int(input("enter the chemistry marks"))
bio=int(input("enter the biology marks"))
sum1=math + eng +phy +chem+bio
print("the total obtained marks are %d \n and grade id %d"%(sum1)


#2. Write a program which take input from user and identify that the given
#number is even or odd?
user_input=int(input("enter the number"))
if (user_input % 2==0):
      print("number is even")
else:
      print("number is odd")


#3. Write a program which print the length of the list?
list=[1,2,3,4,5,6]
n=len(list)
print(n)

#Write a Python program to sum all the numeric items in a list?
length=int(input("length of list"))
list1=[]
for i in range (length):
    num=int(input("enter the list value"))
    list1.append(num)
print(sum(list1))

#Write a Python program to get the largest number from a numeric list.
length=int(input("length of list"))
list1=[]
for i in range (length):
    num=int(input("enter the list value"))
    list1.append(num)
print(max(list1))



#write a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list1=[]
for i in a:
    if i < 5:
        list1.append(i)
print(list1)















