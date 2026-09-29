#program to find first 10 numbers using while loop
# i=0
# while(i<10):
#     print(i,end=",")
#     i=i+1


#write a program to print first 10 even numbers
# i=2
# while(i<21):
#     print(i,end=",")
#     i+=2


#print first 10 odd numbers
# i=1
# while(i<21):
#     print(i,end=",")
#     i+=2

#print 1,4,7,10,13,16
# i=1
# while(i<17):
#     print(i,end=", ")
#     i+=3


#print 10,20,30,40,50,60,70,80
# i=10
# while(i<=80):
#     print(i,end=", ")
#     i+=10



#print 3,6,9,12,15,21
# i=3
# while(i<=21):
#     print(i,end=", ")
#     i+=3


#print 5,4,3,2,1
# i=5
# while(i>=1):
#     print(i, end=", ")
#     i-=1

#print 8,6,4,2,0
# i=8
# while(i>=0):
#     print(i,end=",")
#     i-=2


#print 100,101,102....200
# i=100
# while(i<=200):
#     print(i,end=",")
#     i+=1

#print all 4 digit numbers from 1000-9999
# i=1000
# while(i<=9999):
#     print(i,end=",")
#     i+=1


#print those 3 digit numbers divisible by 3
# i=100
# while(i<=999):
#     if(i%3==0):
#         print(i,end=",")
#     i+=1

#print 4 digit numbers where digit 3 is present
# i=1000
# while(i<9999):
#     if "3" in str(i):
#         print(i,end=",")
#     i+=1

#print numbers divisible by 3 and 5  in range (1,100)
# i=1
# while(i<=100):
#     if(i%3==0):
#         if(i%5==0):
#             print(i,end=",")
#     i+=1



#print 1,4,9,16,25.36.49,64,81,100
#not recommended version i did it simply for fun

# s=set()
# i=1
# while(i<=100):
#     a=i**0.5
#     b=round(a)
#     c=b**2
#     s.add(c)
#     i += 1
# d=sorted(s)
# e=list(d)
# f=e[::-1]
# print(d)
# print(f)

#orginal recommended version
i=1
while(i<=10):
    print(i**2,end=",")
    i+=1




