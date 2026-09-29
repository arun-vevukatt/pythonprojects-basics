#swap

# a=3
# b=5
#
# temp=a
# a=b
# b=temp
#
# print("a=", a)
# print("b=", b)

# a=3
# b=5
# a,b=b,a
# print(a)
# print(b)




def outer():
    y=30
    print("inside",y)

    def inner():
        y=30
        print("inner",y)

    inner()
    print("inside outer functions",y)
outer()