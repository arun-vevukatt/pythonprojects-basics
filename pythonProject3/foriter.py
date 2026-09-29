# l=[1,2,3,4]
# for i in l:
#     print(i)


#Print sum of numbers in list l=[56,89,34,10]
# l=[56,89,34,10]
# sum=0
# for i in l:
#     sum=sum+i
#     i+=1
# print(sum)




#print each number t=(12,78,34,50)
# t=(12,78,34,50)
# for i in t:
#     print(i)



# for i in range(100,0):
#     print(i)

# s="hello"
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)


#checking palindrome
# s=input("enter a word")
# rev=""
# for i in s:
#     rev=i+rev
# if (s==rev):
#     print("palindrome")
# else:
#     print("not palindrome")


#reverse a number
# n=1034
# s=str(n)
# rev=""
# for i in s:
#     rev=i+rev
# print(rev,end=" ")

#l=[12,34,56,45,89,16,69,33]
#print numbers that contains digit 3 with for loop


#
# for i in l:
#     string = str(i)
#     p=0
#     for k in string:
#         if (k=='3'):
#             p=1
#     if (p == 1):
#         print(i)



#print even values
# for i in l:
#     if(i%2==0):
#         print(i)



# l=[12,4.5,6.8,30,"arun","hello"]
# #print float point values
# for i in l:
#     if type(i)==float:
#         print(i)
#

d={'a':23,'b':25,'c':28,'d':30,'e':22}
#print even numbers

for i in d:
    if (d[i]%2==0):
        print(i, d[i])



colours=['red','green','blue','orange','black']
#starting letter of list

# for i in colours:
#     print(i[0])

#last letter
# for i in colours:
#     print(i[-1],end=", ")

#all colours that contains 'b'
# for i in colours:
#     if ("b" in i):
#         print(i)

#print all 3 digit numbers(100-999)
# for i in range(99,1000):
#     print(i)


#print all numbers divisible by 3 in the range 100-200
# count=0
# for i in range(100,201):
#     if (i%3==0):
#         count+=1
#         print(i)
# print(f"total count: {count}")




#100,200,300,400,500
# for i in range(100,501,100):
#     print(i)


#3,6,9,12,15,18,21
# for i in range(3,22,3):
#     print(i,end=",")