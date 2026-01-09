# str1="this is string"
# str2='this is string'
# str3=""" this is 
# string
# """

# a="my name\"s is rifat"

# ! concatenation

# a="hello"
# b="world"
# print(len(a))
# print(len(b))


# final_str=a+" "+b
# print(final_str)
# print(len(final_str))


# ! string

# str="hello world"

# print(str[-5:-2])

# str="i am Learning python from college"

# print(str.replace("python","javascript"))

# name=input("enter your fist name:  ")

# print(len(name))


# str=input("enter a string with $ :")
# print(str.count("$"))

# marks=int(input("enter the student marks: "))

# if(marks>=90):
#     grade="A"
# elif(marks>=80 and marks<90):
#     grade="B"
# elif(marks>=70 and marks<80):
#     grade="C"
# elif(marks>60):
#     grade="D"
# else:
#     grade="F"
# print(grade)

# ! nesting

# age=int(input('enter age: '))

# if(age>=18):
#     if(age>=80):
#         print("cannot drive")
#     else:
#         print("can drive")
# else:
#     print("cannot drive")

# num=13
# if(num%2==0):
#     print("even")
# else:
#     print("odd")

a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))

if(a>=b and a>=c):
    print(a,"is biggest")
elif(b>=c):
    print(b ,"is biggest")
else:
    print(c,"is biggest")

