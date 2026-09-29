#define a function that takes string as arguments and return a new dictionary where keys are words and
# values are length of each word
#call the function and print the dictionary

s="python coding is easy and fun"
# def dictionary(s):
#     a=s.split()
#     d={i:len(i) for i in a}
#     return d
# print(dictionary(s))


# def fun(s):
#     new={}
#     for i in s.split():
#         new[i]=len(i)
#     return new
# print(fun(s))


##################################################

#POSITIONAL TYPE ARGUMENTS
# def func(n,a):
#     print("name :",n)
#     print("age: ",a)
#     return
# func("arun",21)

################################################

#KEYWORD ARGUMENTS
# def func(n,a):
#     print("name: ",n)
#     print("age: ", a)
#     return
# func(a=21,n="arun")


###############################################

#DEFAULT ARGUMENTS
# def fun(n,a=23):
#     print("name",n)
#     print("age ",a)
#     return
# fun("arun",34)

##############################################

#VARIABLE LENGTH
# def func(**kwargs):   #prints tuple
#     print(kwargs)
#
# func(a=10,b=20,c=30)


# def func(*args):        #stores as dictionary
#     print(args)
# func(10,20,30)


############################################
#define a function to find the sum od numbers using arbituary positional arguments

# def func(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     return sum
# print(func(10,20,30))

##################################################
import math
num=int(input("enter a number: "))
print(math.factorial(num))