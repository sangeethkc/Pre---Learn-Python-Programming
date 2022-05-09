# ● Take 2 integer input from user and print their products(their multiplication) done
# ● IF product is greater than 500 then return their sum - done
# ● If the product is smaller than 500 then return "Hello LNB code is running fine !!"

X = int(input("enter a number:"))
Y = int(input("enter a number:"))
Z = X*Y
print("Product of numbers : ",Z )
print(Z)
if (X*Y) > 500:
    print("sum of numbers : ", X+Y)
else:
    print("Hello LNB code is running fine !!")
