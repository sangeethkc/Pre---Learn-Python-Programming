
# Sum of n digits

list = []
for x in range(5):
  x = int(input("enter a number:"))
  if x > 9:
    list.append(x)
print("sum of remaining numbers: ",sum(list))
