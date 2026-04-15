# "Variables defined inside a function are local to that function"
#
# "python"
def my_function():
 x = 10 # Local variable
 print(x)

my_function() # Output: 10
print(x) # Error: x is not defined outside the function