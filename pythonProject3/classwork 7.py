# Q.Write Python Programs Using map(), filter(), or reduce()
# 1.Capitalize all names in a list
# names = ['alin', 'arun', 'anu']
# #map()
# print(list(map(lambda x:x.capitalize(),names)))
import functools


##############################################################################


# # 2.Append "@gmail.com" to a list of usernames
# users = ['user1', 'user2']
# print(list(map(lambda x:x+"@gmail.com",users)))
#
# ############################################################################


#
# # 3.Filter out all empty strings from a list
# words = ['hello', ' ', 'world', ' ', 'python']
#
# print(list(filter(lambda x:x!=" ",words)))

#############################################################################

# 4.Filter names that start with the letter 'A'
# names = ['Anu', 'Neenu', 'Arun', 'Ravi']
# print(list(filter(lambda x:x[0]=="A",names)))

#########################################################################

# 5.Concatenate all strings in a list
    # words = ['Python', 'is', 'fun']
# import functools
# print(functools.reduce(lambda a,b:a+" "+b ,words))
##########################################################################

# 6.Multiply all numbers in a list
# nums = [2, 3, 4]
# import functools
# print(functools.reduce(lambda a,b:a*b,nums,1))
###########################################################################

# 7.Extract First Character of Each Word
# words = ["apple", "banana", "cherry"]
#
# print(list(map(lambda x:x[0],words)))

###########################################################################

# 8.Add 10 to Each Number
# nums = [5, 10, 15]
# print(list(map(lambda x:x+10,nums)))

############################################################################

# 9.Given a list
# l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
#     # #Sum of positive even numbers
# import functools
# #
# # print(functools.reduce(lambda a,b:a+b if b>0 and b%2==0 else a,l,0))
#
# #sum of positive odd numbers
# print(functools.reduce(lambda a,b:a+b if(b>0) and (b%2!=0) else a,l,0))
# # print(functools.reduce(lambda a,b:a+b if(b>0) and (b%2!= 0) else a,l,0))
#
# # #Sum of Negative  odd numbers
# print(functools.reduce(lambda a,b:a+b if b<0 and b%2!=0 else a,l,0))
#
# # #Sum of Negatve Even numbers
# print(functools.reduce(lambda a,b:a+b if b<0 and b%2!=0 else a,l,0))
#
# # #Count of Positive numbers
# print(functools.reduce(lambda a,b:a+1 if b>0 else  a,l,0))
# # #Count of negative numbers
# print(functools.reduce(lambda a,b:a+1 if b<0 else  a,l,0))



# 10.Given a list nums = ["1", "2", "3", "4"]
# Convert all Strings to Integers [1,2,3,4]


# 11.
p= [{'name':'laptop','price':50000},
    {'name':'phone','price':20000},
    {'name':'watch','price':3000},
    {'name':'Tablet','price':25000}]

#print list of product names in Uppercase
print(list(map(lambda a:a['name'].capitalize(),p)))
print(list(map(lambda a:a['name'].upper(),p)))


#print products with price greater than 10000
print(list(filter(lambda a:a['price']>10000,p)))


#Find the total price of all product
print(functools.reduce(lambda a,b:a+b['price'],p,0))
