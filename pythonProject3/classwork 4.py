

#check wheather a number is divisible by  5 & 3



"""
num=int(input("enter a number: "))
if (num%5==0):
    if (num%3==0):
        print("fizzbuzz")
    else:
        print("not divisible")
else :
    print(num)
"""



# divisible by 5 & not by 3
"""
num=int(input("enter a number: "))
if (num%5==0):
    if (num % 3 != 0):
        print("conditions valid")
    else:
        print("conditon doesnt satisy")
else:
    print("condtion does not satisfy")
"""


# divisible 3 and not by 5
"""
num=int(input("enter a number: "))
if (num%3==0):
    if (num % 5 != 0):
        print("conditions valid")
    else:
        print("conditon doesnt satisy")
else:
    print("condtion does not satisfy")
"""

#not divisible by 2 and 3
"""
num=int(input("enter a number: "))
if (num%3!=0):
    if (num % 2 != 0):
        print("conditions valid")
    else:
        print("conditon doesnt satisy")
else:
    print("condtion does not satisfy")
"""


#write a program to find BMI(Body Mass Index)
# BMI= weight in (kg)/ height**2 in (m)
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese
"""
print("BMI:-")
weight=float(input("enter weight: "))
height=float(input("enter height: "))
bmi=weight/(height**2)
if bmi<=18.4:
    print("underweight")
elif (bmi>=18.5) and (bmi<=24.9):
    print("normal")
elif (bmi >= 25) and (bmi <= 39.9):
    print("overweight")
else:
    print("obese")

"""


# A toy vendor supplies three types of toys:
# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.

# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.

# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,

# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.
# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.
# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.


print("""
 1. Battery based
 2. Key based
 3. electrical charging based toys
 """)
choice=int(input("enter choice: "))
amount=int(input("enter order amount: "))
if choice==1:
    if amount>1000:
        discount=(amount/100)*10
        price=amount-discount
        print(price)
    else:
        print(f"amount to be paid: {amount}")
elif choice==2:
        if amount>100:
            discount=(amount/100)*5
            price = amount - discount
            print(price)
        else:
            print(f"amount to be paid: {amount}")
elif choice==3:
        if amount > 500:
            discount = (amount / 100) * 10
            price = amount - discount
            print(price)
        else:
            print(f"amount to be paid: {amount}")
else:
        print("invalid")







