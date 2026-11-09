from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius
print("Temperature converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter a conversion (1 or 2):")

if choice == "1":
    temp = float(input('Enter a temperature in Celsius: '))
    result = celsius_to_fahrenheit(temp)
    print("Temperature in Fahrenheit: ", result)
elif choice == "2":
    temp = float(input("Enter temperature in Fahrenheit: "))
    result = fahrenheit_to_celsius(temp)
    print("Temperature in Celsius: ",result)
else:
    print("Invalid choice.")