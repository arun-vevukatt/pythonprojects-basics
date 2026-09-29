# lambda function to find cube of a number

# s=lambda n:n**3
# print(s(5))

#sum of two numbes
# a=6
# b=10
# s=lambda a,b:a+b
# print(s(a,b))
###########################################################

#product of three numbers

# s=lambda a,b,c:a*b*c
# print(s(3,4,5))
######################################################################

#length of a string

# s= lambda string:len(string)
# print(s("hello"))
#######################################################################

#square root of a number
# s=lambda root:root**0.5
# print(s(25))

####################################################################

#first letter of a string
# s=lambda first:first[0]
# print(s("hello"))

##################################################################3

#last letter of a string
# s=lambda last:last[-1]
# print(s("hello"))

################################################################

#name value from a dictionary
# d={"name":"arun","salary":4000}
# s=lambda name:d["name"]
# print(s(d))


#salary value from dictionary
# d={"name":"arun","salary":4000}
# s=lambda dict:dict["name"]
# print(s(d))

#add 10 to a number
# n=10
# s=lambda n:n+10
# print(s(10))

##############################################33
##MAP
l=[1,2,3,4,5]
#print(list(map(lambda x:x**2,l)))

#create a new list of cubes
print(list(map(lambda x:x**2,l)))

