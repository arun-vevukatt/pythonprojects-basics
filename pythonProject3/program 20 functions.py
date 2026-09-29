# def add():
#     n1=int(input("enter a number: "))
#     n2=int(input("enter a number"))
#     sum=n1+n2
#     print("sum: ",sum)
#     return
#
# add()



#################################################################

#define a function to display "hello your name"
# def name():
#     n=input("enter name: ")
#     a="hello "+ n
#     print(a)
#     return
# name()

###############################################################

#define a function to find the count of a specific character in a string
# def length():
#     count=0
#     n=input("enter word: ")
#     a=str(input("letter: "))
#     for i in n:
#         if i in a:
#             print(a)
#             count+=1
#     print(count)
#     return
# length()

#################################################################

# #define a function to find a factorial of a number
# def factorial():
#     num=int(input("enter number: "))
#     fact=1
#     for i in range(1,num+1):
#         fact=i*fact
#     print(fact)
#
#     return
# factorial()

#################################################################


#define a funtion to check wheather a number is armstrong or not


# def armstrong():
#     num=int(input("enter a number: "))
#     b=str(num)
#     sum=0
#     l=len(b)
#     for i in b:
#         a=int(i)**l
#         sum=sum+a
#         if(sum==num):
#             print("armstrong")
#         else:
#             print("not armstrong")
#     return
#
# armstrong()

###################################################################

#define wheather a number is prime or not

# def prime():
#     num=int(input("enter a number: "))
#     for i in range(2,num):
#         if(num%i==0):
#             print("prime")
#         return
# prime()

################################################################3


#define q function to find the factors of a number
# def factors():
#      num=int(input("enter a number: "))
#      for i in range(1,num+1):
#          if(num%i==0):
#              print(i)
#      return
# factors()

###################################################

#sum of two numbers
# def add(n1,n2):
#     sum=n1+n2
#     print("sum: ",sum)
# add(2,2)

####################################################


#define a function that takes 3 arguments and find the simple interest

# def interest():
#     n1=int(input("enter principal amount: "))
#     n2=int(input("enter years: "))
#     n3=float(input("enter rate: "))
#     # simple_interest=(principal_amount*years*rate)/100
#     simple_interest = (n1 * n2* n3) / 100
##     print("interest:",simple_interest)
# interest()
#############################################################

#define a function that takes string and a character as arguments and print the count of the character in the string

# def count():
#     count=0
#     word=input("enter string: ")
#     a=input("character: ")
#     for i in word:
#         if(i==a):
#             count+=1
#     print(count)
# count()

################################################################


#return statments
#
# def add(n1,n2):
#
#     s=n1+n2
#     return s
# n1=int(input("emter a number: "))
# n2=int(input("enter a number: "))
# a=add(n1,n2)
# print("sum: ", a)


################################################################

#define a function that takes 3 numbers and return the product as result call the function and print the result

n1=int(input("enter n1: "))
n2=int(input("enter n2: "))
n3=int(input("enter n3: "))
def product(n1,n2,n3):
    product=n1*n2*n3
    return product
a=product(n1,n2,n3)
print("product: ",a)











