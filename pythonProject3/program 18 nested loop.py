# l=[10,20,30]
# for i in l:
#
#     for j in range(1,4):
#         print(i,end=" ")
#     print()



# for i in range(1,4):
#     for j in range(1,4):
#         print(j,end=" ")
#     print()

# l=[['lion','tiger'],['cat','elephant']]
# for i in l:
#     print(i)
#     for j in i:
#         print(j)
#     #print()


# n=['kelly','alan','jenny']
# for i in n:
#     for j in range(2,5):
#         print(i,end=" ")
#     print()


# n=[1,2,3]
# qns=['what','when','why']
# for i in n:
#     print(i)
#     for j in qns: #i.values
#         print(j,end=" ")
#     print()


# d=[
#     {'id':101,'name':'arun','age':25},
#     {'id':102,'name':'amal','age':23},
#     {'id':103,'name':'anu','age':24}
# ]
#
# for i in d:
#    # print(i)
#     for j in i:
#         print(i[j],end=" ")
#     print()


#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
#
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
#


# for i in range(2,9,2):
#     for j in range(2,6):
#         print(i,end=" ")
#     print()

# for i in range(200,9,2):
#     for j in range(2,6):
#         print(i,end=" ")
#     print()

# for i in range(5,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print()


# for i in range(5,0,-1):
#     for j in range(i):
#         print('*',end=" ")
#     print()


# for i in range(1,5):
#     for j in range(1,1+i):
#         if(j%2==1):
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()
#
#


# *
# ***
# *****
# *******

# for i in range(1,8,2):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()


# 1
# 2 3
# 4 5 6
# 7 8 9 10


# k=1
# for i in (range(1,5)):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+1
#     print()


#pyramid
# for i in range(1,6):
#     for j in range(1,2+i):
#         print(" ",end="")
#
#     for k in range(1,i+1):
#             print("*",end=" ")
#     print()





# A
# B C
# D E F
# G H I J
#
# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()



#
# A
# B B
# C C C
# D D D D

# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k), end=" ")
#     k = k + 1
#     print()

# A
# A B
# A B C
# A B C D


# for i in range(1,5):
#     k = ord('A')
#     for j in range(1,i+1):
#         print(chr(k), end=" ")
#         k = k + 1
#     print()


#PRINT ALL EVEN NUMBERS
# l=[23,65,42,80,56,41]
# for i in l:
#     if(i%2!=0):
#         print(i,end=" ")


# for i in l:
#     for j in range(2, i):
#
#         if(i%j==0):
#
#             break
#     else:
#         print(i)
#         print("not prime")


#print all the prime numbers in range(1,100)
# for i in range(2,100):
#     for j in range(2,i):
#         if(i%j==0):
#             break
#     else:
#         print(i)


#print all armstrong numbers in the range(100,1000)

# for i in range(100,1000):
#     sum = 0
#     s=str(i)
#     l = len(s)
#     for j in s:
#         sum=sum+(int(j)**l)
#     if(sum==i):
#         print(i)



