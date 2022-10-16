# find the max number
def max(x,y):
  if x>=y:
    retrun x
  else:
    retrun y
print(max(8,12))
#######################
# find the fectorial
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(factorial(6))
