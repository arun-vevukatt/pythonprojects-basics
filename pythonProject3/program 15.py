#count those three digit numbers that contains digit 3
# count=0
# i=100
# while(i<=999):
#     s=str(i)
#     if '3' in s:
#         count+=1
#     i+=1
# print(count)

#count of those numbers that are divisible by 7 or 3 in the range(200,300)
# count=0
# i=200
# while(i<=300):
#     if (i%7==0) or (i%3==0):
#         count+=1
#     i+=1
# print(count)

#count odd numbers that are divisible by 5 and 2 in the range(1,100)
# count=0
# i=1
# while(i<=100):
#     if(i%5==0) and (i%2==0):
#         count+=1
#     i+=1
# print(count)

#count all the palindrome numbers in thw range(1,1000)
# count=0
# i=1
# while(i<=1000):
#     s=str(i)
#     e=s[::-1]
#     if (s==e):
#         count+=1
#     i+=1
# print(count)


#count all the divisible numbers divisible by 3 in (1,50)
# count=0
# i=1
# while(i<=50):
#     if(i%3==0):
#         count+=1
#     i+=1
# print(count)


#find the sum of first 5 numbers
# i=0
# sum=0
# while(i<=5):
#     sum=sum+i
#     i+=1
# print(sum,end=",")

#sum of those numbers that are divisible by 3 in the range(1,50)
# i=1
# sum=0
# while(i<=50):
#     if(i%3==0):
#         sum=sum+i
#     i+=1
# print(sum)


#sum of all 3 digit numbers
# i=0
# sum=0
# while(i<=999):
#     sum=sum+i
#     i+=1
# print(sum)

#sum of first 10 even numbers
# i=0
# sum=0
# while(i<=20):
#     if(i%2==0):
#         sum=sum+i
#     i+=1
# print(sum)


#product
#product of series 1,2,3,4,5
# i=1
# product=1
# while(i<=5):
#     product*=i
#     i+=1
# print(product)




#product of first 10 odd numbers
# product=1
# i=1
# while(i<=20):
#     if(i%2!=0):
#         product*=i
#     i+=1
# print(product)



#product of numbers contains digit '3' in the range(1,50)
# i=1
# product=1
# while(i<=50):
#     s=str(i)
#     if '3' in s:
#         product*=i
#     i+=1
# print(product)


#factorial of a number entered by user
# i=1
# product=1
# num=int(input("enter number: "))
# while(i<=num):
#     product*=i
#     i+=1
# print(f"factorial of {num} : {product}")


#multiplication table of number (upto 10)
# i=1
# product=1
# num=int(input("enter a number: "))
# while(i<=10):
#     product=i*num
#     print(f"{num} * {i} = {product}")
#     i+=1



#sum of digits of a number
# s=0
# num=int(input("enter a number: "))
# while(num>0):
#     d=num%10
#     s=s+d
#     num=num//10
# print(s)


#multiplication table of number (upto 10)
i=1
product=1
num=int(input("enter a number: "))
while(i<=10):
    product=i*num
    e=num*(i+10)
    f=num*(i+20)
    print(f"{num} * {i} = {product}","        ",f"{num} *",(10+i),"=",e,"        ",f"{num} *",(20+i),"=",f)
    i+=1



