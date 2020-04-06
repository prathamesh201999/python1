
a = int(input('Enter the first value'))
b = int(input('Enter the second value'))

try:
    print("Connection open")
    print(a/b)
    k = int(input('Enter the value'))
    print(k)
except ZeroDivisionError as e:
    print("Zero is not a valid input",e)
except ValueError as e:
    print("Give the integer as input",e)
    
finally:
    print("Connection closed")
