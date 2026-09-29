# # given a list
# l=[1,2,3,4,5,5,5,6,7]
# # create a new dictionary where keys are numbers and values are count of each number
# new={}
# for i in l:
#     new[i]=l.count(i)
# print(new)

###########################################################################################################
#
# l=[34,12,56,89,90,11]
#find the second largest element
# l.sort()
# second_largest=len(l)-2
# print(l[second_largest])

#find the smallest element
# l.sort()
# print(l[0])
# s=min(l)
# print(s)



#find the second smallest element
# l.sort()
# print(l[1])


########################################################################3

# l=[
#     ["arun",23,40000],
#     ['amal',24,50000],
#     ['anu',27,30000]]
#
# #create anew list of salary ,
# # find the max salary
# #create anew list and find min age
#
# salary=[]
# age=[]
# for i in l:
#     salary.append(i[2])
#     age.append(i[1])
# print("salary: ",salary)
#
# print("max salary: ",max(salary))
# print("min age: ",min(age))


######################################################################################

#1.Given a list l=[1,1,1,2,3,3,4,5] remove duplicates from list
# l=[1,1,1,2,3,3,4,5]
# s=set(l)
# print(s)

# 2.Given a list
# l=[1,1,1,2,3,3,4,5]
# #remove duplicates without set()
# new=[]
# for i in l:
#     if i not in new:
#         new.append(i)
# print(new)

#3.Given two lists

# l1=[23,45,78,90,12,74]
# l2=[45,89,23,56,34]
# s=set(l1)
# b=set(l2)
# #print common elelments
#
# intersection=s.intersection(b)
# print(list(intersection))

#define a function that takes a list of numbers  as argumnents and print the count of even numbers,odd numbers and
# numbers whose value greater than 50
# l=[23,56,12,78,98,89,31,67]
#
# def func(l):
#     count=0
#     count_odd=0
#     count_value=0
#     for i in l:
#         if i%2==0:
#             count+=1
#         else:
#             count_odd+=1
#     # for i in l:
#         if i>50:
#             count_value+=1
#     print("even count: ",count)
#     print("odd count: ",count_odd)
#     print("greater than 50: ",count_value)
#     return
# func(l)

#define a function that takes a list of words as argumnert and returns a new list of lengths
# l=["red","green","orange","yellow","blue"]
#
# def func(l):
#
#     new=[]
#     for i in l:
#         # length=len(i)
#         new.append(len(i))
#     return new
# print(func(l))



# define a function that takes a number as argumnent and return its square
# n=int(input("enter number: "))
# def square(n):
#     # print("square is : ",n*n)
#     return n*n
# print(square(n))



############################################3
# lambda function to find cube of a number

s=lambda n:n**3
print(s(5))















