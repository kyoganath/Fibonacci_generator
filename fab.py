# Defining the Generator function to generate the Fabonacci Sequence
def fibonacci_generator():
    
    # if you Enterd the negative number 
    if n <= 0:
        print("Enter the correct number")
        
    else:
        # intialzing the first two values of the fabonacci series
        a, b = 1, 1 
        
        # It is infinite loop but we will use it to generate the Fibonacci Sequence
        while True:
            
            # Creating the Generator and Yield the current value of a
            yield a 
            
            # updating  the values of the next two numbers in the Sequence 
            a, b = b, a + b


# Creating the instance of the Fabonacci Generator function
value = fibonacci_generator()

# the number which specifies the Fabonacci number we want 
n = int(input("Enter the Number : "))

# Using for loop to get the first n numbers in the Fabonacci Sequence
for i in range(n):
    
    # getting the next number in the Sequence
    result = next(value)

# Printing the  nth Fabonacci number 
print(f"The {n}th Fibonacci number is: {result}")