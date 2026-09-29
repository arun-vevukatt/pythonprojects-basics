#create a new list of square roots
# l=[25,36,81,100]
# print(list(map(lambda x:x**.5,l)))

################################################################

# #create a new list of lengths
# colors=['red','green','blue','yellow','black']
# # print(list(map(lambda n:len(n),colors)))

##################################################################

# #create a new list of first characters
# # print(list(map(lambda n:n[0],colors)))

#####################################################################


# #create a new list of last characters
# print(list(map(lambda n:n[-1],colors)))

########################################################################

# #create a new list of reverse of each elemnt
# print(list(map(lambda n:n[::-1],colors)))

##########################################################################

#Given a
# l=[23,78,12,56]
# #Add 10 to each element in the given sequence
#
# print(list(map(lambda n:n+10,l)))
#
# ##########################################################################
#
# ##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#     {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#     {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
# #
# # # create a new list of emails
#
# print(list(map(lambda dict:dict["email"],l)))



# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x:x%2==0,l)))
#
# l=[23,65,89,12,20,33,85,40]
# #filter elemetns greater than 50
# print(list(filter(lambda x:x>50,l)))
#
# #filter even values greater than 50
# print(list(filter(lambda x:(x<50 and x%2==0),l)))

# fruits=['apple','orange','pinapple','grapes','avacado']
# #filter elements whose length is greater than 5
# print(list(filter(lambda x:len(x)>5,fruits)))



#reduce

#sum of list
# l=[1,2,3,4]
# import functools
# print(functools.reduce(lambda a,b:a+b,l,0))



#Q1.Write Python Programs Using map(), filter(), or reduce()





