#Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.
fahrenheit = input("What is the temperature in Fahrenheit that you would like converted: ")

#Task 2: Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.
#Use a try block to catch any potential errors during the conversion process. What happens if they type out "thirty" instead of doing 30?
# try: 
#     celsius = ((int(fahrenheit) - 32) * 5/9)
#     print("Temperature in celsius: ", celsius)
# except:
#     print("I need an integer!")
#Task 3: Implement an else block that prints the converted temperature in a user-friendly format. 
# try: 
#     celsius = ((int(fahrenheit) - 32)* 5/9)
# except:
#     print("I need an integer!")
# else:
#     print("Temperature in celsius: ", round(celsius, 3))

#Task 4: Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed
# regardless of whether an exception was caught or not.
try: 
    celsius = ((int(fahrenheit) - 32)* 5/9)
except:
    print("I need an integer!")
else:
    print("Temperature in celsius: ", round(celsius, 3))
finally:
    print("Thank you for using the app!")