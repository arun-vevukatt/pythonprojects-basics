#write a program to check wheather the number is positive or negative
# num=int(input("enter a number: "))
#
# if num%2==0:
#     print(f"{num} is even")            #fstring - formated string , eg : print(f"{n} is even")
# else:
#     print(f"{num} is odd")




#check if two numbers are equal or not
# a=int(input("enter a number: "))
# b=int(input("enter a number: "))
#
# if a==b:
#     print("equal")
# else:
#     print("not equal")




#write a program to check whether two entered words are equal or not
# a=input("enter a word: ")
# b=input("enter a word: ")
# if a==b:
#     print("equal")
# else:
#     print("not equal")



#write a program to find the max of two numbers
# a=int(input("enter a number: "))
# b=int(input("enter a number: "))
#
# if a>b:
#     print(f"{a} is max")
# else:
#     print(f"{b} is max")




#check if entered character is vowel
# a=input("enter a word")
# b="aeiouAEIOU"
# if (a in b):
#     print("vowels found")
# else:
#     print("no vowels")


#check if land in entered country name
# a=input("enter a word")
# c=a.lower()
# b="land"
# if (b in c):
#     print("found")
# else:
#     print("not found")



#check weather entered number is 3 digit
# a=int(input("enter a number"))
# if (a>99) and (a<1000):
#     print("three digit")
# else:
#     print("not three digit")




#check palindrome
# a=(input("enter a word"))
# b=a[::-1]
# if a==b:
#     print("palindrome")
# else:
#     print("not palindrome")




#check wheather given numbers present in list

# l=[3,67,12,90]
# a=int(input("enter number"))
#
# if a in l:
#     print("present")
# else:
#     print("not present")


#write a program if key is present in the dictionary or not
# d={101:'arun',102:'amal',103:'anu'}
# a=int(input("enter key"))
# if a in d.keys():
#     print("key found")
# else :
#     print("key not found")




#write a program to check whether the given program is weak/strong(if less than 8 pass is weak)
# a=str(input("enter pass"))
# if len(a)>8:
#     print("strong")
# else:
#     print("weak")





#greatest of three numbers
a=int(input("enter a number A: "))
b=int(input("enter a number B: "))
c=int(input("enter a number C: "))

if (a> b and a> c):
    print(f"{a} is larger")
elif  (b>c and b>a):
    print(f"{b} is larger")
else:
    print(f"{c} is larger")



