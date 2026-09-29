# l=[1,2,3,4]
# # new=[i**2 for i in l]
# # print(new)
# ##########################################
# new=[5 for i in l]
# print(new)
############################################

#given a list
l=[23,46,55,11,78,90,24]
#
# new=[i for i in l if i%2==0]
# print(new)

#greater than 50
# new=[i for i in l if i>50]
# print(new)


#firsst letter
# colours=['red','green','blue','orange']
# new=[i[0] for i in colours]
# print(new)

#length of letter
# colours=['red','green','blue','orange']
# new=[len(i) for i in colours]
# print(new)


#last character
# colours=['red','green','blue','orange']
# new=[i[-1] for i in colours]
# print(new)

#reverse
# colours=['red','green','blue','orange']
# new=[i[::-1] for i in colours]
# print(new)

# l=[23,78,12,56]
# new=[i+10 for i in l]
# print(new)


##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
#
# # # create a new list of emails
# new={i['email'] for i in l}
# print(new)


################
# d={'arun':25,'amal':34,'akhil':26,'anu':21}
# # # create a list of names
# new={i for i in d.keys()}
# print(new)

###############################
# #Given a list
l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']
# #create a list of string values
# new=[i for i in l if type(i)==str]
# print(new)

# #create a list of floats
# new=[i for i in l if type(i)==float]
# print(new)

#print positive numbers
# new=[i for i in l if (type(i)==int or type(i)==float) and i>0]  ( could also use type(i)!=str)
# print(new)

#####################

# fruits = ['apple', 'orange', 'pineapple', 'avocado', 'grapes']
# create a new list with elements whose length is greater than 6
# new=[i for i in fruits if len(i)>6]
# print(new)

###################

#create a new list with elements whose value is divisible by 3 in range(1,101)
# new=[i for i in range(1,101) if i%3==0]
# print(new)

###################################
#s="python coding  is easy and fun"
# # # create a new list with only vowels
# new=[i for i in s if i in 'aeiou']
# print(new)
################333333333
# for word in s.split():
#     new=[i for i in word if i in 'aeiou']
#     print(f"{word}: {new}")

##################

#set comprehension
# s="python coding  is easy and fun"
# # # # create a new set with only vowels
# new={i for i in s if i in 'aeiou'}
# print(new)
##############################################################


#dictionary comprehension
# l=[1,2,3,4]
# #create a new dictionary where keys are numbers and values the squares of each number
# new={i:i**2 for i in l }
# print(new)



# #create a new dictionary where keys are index and values are numbers itself
# l=[10,20,30,40]
# new={i:l[i] for i in range(0,len(l))}
# print(new)


###########################################3

# s="python coding is easy and fun"
# # create a new dictionary where keys are words and values are length of each if word.
#
# new={i:len(i) for i in s.split()}
# print(new)

##############################################################


















