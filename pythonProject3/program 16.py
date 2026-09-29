
#factor of a number
# n =int(input("enter number:"))
# for i in range(1,n+1):
#     if(n%i==0):
#         print(i)


# l=[1,2,3,4]

#create a new list with squares of each numbers
# new=[]
# for i in l:
#     new.append(i**2)
# print(new)


#create a dictionary where keys are numbers and values are sqaure of each number
# new



#reverse of a string
# s="hello"
# s[::-1]
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)


#reverse a number
# n=[1,2,3,4,5]
# s=str(n)
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)



#classwork 6
# # # 1.Write a program that prints all numbers between 1 and 100 that are divisible by 3 or 5
# for i in range(1,101):
#     if (i%5==0) or (i%3==0):
#             print(i)


# # 2.Print the cumulative sum of a list.
# # Example: [1, 2, 3, 4] → Output: [1, 3, 6, 10]
#l=[1, 2, 3, 4]
# new=[]
# sum=0
# for i in l:
#     sum+=i
#     new.append(sum)
# print(i)

#even index sum
# sum=0
# for i in range(0,3,2):
#     sum=sum+l[i]
# print(sum)


# # 3.Given two numbers a and b, calculate the sum of all numbers between them (inclusive). Use a for loop.
# # Example: a = 3, b = 7 → Output: 25
# sum=0
# for i in range(3,8):
#     sum+=i
# print(sum)


# print seperatly
# n=1234
# for i in str(n):
#     print(int(i),end=" ,")


# # 5.Given a list, sum the elements until a 0 is encountered (stop at 0).
# l = [4, 9, 1, 0, 6, 7]
# sum = 0
# for i in l:
#     if(i==0):
#         break
#     sum+=i
#
# print(sum)


# 6.Loop from 1 to 1000 and find the first number divisible by both 7 and 11. Use break to stop once found.
# for i in range(1,1001):
#     if(i%7==0) and (i%11==0):
#         print(i)
#         break


# 7.Given a list of strings, print only those with length ≥ 5. Use continue to skip shorter ones.
# l=['arun','anu','akhil','kiran','rahul']
# for i in l:
#     if(len(i)<5):
#         continue
#     print(i)


# 8.From a list of numbers, create a new list containing the squares of each element.
# Input: [1, 2, 3] → Output: [1, 4, 9]
# l=[1,2,3,4]
# new=[]
# for i in l:
#     new.append(i**2)
# print(new)


# 9.Given a string, construct a new string with all vowels removed using a loop.
# Input: "hello world" → Output: "hll wrld"
# vowels='aeiouAEIOU'
# word=input("enter word: ")
# for i in word:
#         if i in vowels:
#                 continue
#         print(i)


# 10.Given a list of numbers, create a new list where each number is doubled, but stop if any doubled number is greater than 50 (use break).
# l=[5,2,8,6,2]
#
# for i in l:
#         double=i*2
#         if(double>50):
#                 break
#
#         print(double)

# 11.From a string containing mixed characters, create a new string containing only digits.
# Input: "abc123x7z" → Output: "1237"
# s=input("enter mixed: ")
# digits="0123456789"
# new=""
# for i in s:
#     if(i in digits):
#         new=new+i
# print(new)

# 12.Given a list of strings, create a new list containing the length of each string.
# Input: ["cat", "banana", ""] → Output: [3, 6, 0]
# l=["cat", "banana"]
# new=[]
# for i in l:
#         new.append(len(i))
# print(new)

# 13.Given a list of words, create a string made of the first letter of each word.
# Input: ["Python", "Is", "Great"] → Output: "PIG"
# l=["Python", "Is", "Great"]
# new=[]
# for i in l:
#         new.append(i[0])
# print(new)


#14.Replace Negative Numbers with 0
# Given a list of integers, create a new list where all negative numbers are replaced with 0.
# # Input: [4, -3, 2, -1] → Output: [4, 0, 2, 0]
# l=[4, -3, 2, -1]
#
# new=[]
# for i in l:
#     if i<0:
#         l[i]=0
# print(l)



# 15 d={101:['Arun',23,'ekm'],
#      102:['Amal',25,'tvm'],
#      103:['Anu',26,'tcr'],
#       104:['Kiran',27,'ekm']}
#
# #print all names of students

# for i in d.values:
#     print(i[0])

d={101:['Arun',23,'ekm'],
     102:['Amal',25,'tvm'],
     103:['Anu',26,'tcr'],
      104:['Kiran',27,'ekm']}
for i in d.values():
        print(i[0])

