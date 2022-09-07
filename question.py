# TODO: 1. Write a python script to print MySirG N times on the screen
n = int(input('Enter the value of n:'))
while n:
  print('MySirG')
  n=n-1

# TODO: Write a python script to print first N natural numbers.
n = int(input('Enter the value of n:'))
i=1
while i<=n:
  print(i)
  i=i+1
print()

# TODO: 3. Write a python script to print first N natural numbers in reverse order
i=1
n = int(input('Enter the number:'))
while n>=1:
  print(n)
  n=n-1

# TODO: Write a python script to print first N odd natural numbers
i=1
n = int(input('Enter the value of n:'))
while i<=n*2:
  # if (i % 2 !=0):
  print(i)
  i=i+2
print()

# TODO:5. Write a python script to print first N odd natural numbers in reverse order
i=1
n = int(input('Enter the value of n:'))
while i<=n*2:
  if (i % 2 !=0):
    print(20-i)
  i=i+1
print()

i=1
n = int(input('Enter the number:'))
while i>=n*2:
  print(n-i)
  i=i+2
print()
# TODO: 6. Write a python script to print first N even natural numbers
i=1
n = int(input('Enter the value of n:'))
while i<=n:
    print(2*i)
    i=i+1
print()

# TODO: 7. Write a python script to print first N even natural numbers in reverse order
i=1
n = int(input('Enter the value of n:'))
while i<=n:
    print(22-(2*i))
    i=i+1
print()

# TODO:8. Write a python script to print squares of first N natural numbers
i=1
n = int(input('Enter the value of n:'))
while i<=n:
    print(i**2)
    i=i+1
print()

# TODO:9. Write a python script to print cubes of first N natural numbers
i=1
n = int(input('Enter the value of n:'))
while i<=n:
    print(i**3)
    i=i+1
print()

# TODO: 10. Write a python script to print first 10 multiples of N
i=1
n = int(input('Enter the number:'))
while i<=n:
  print(i*10)
  i=i+1
print()