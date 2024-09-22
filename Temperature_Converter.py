def temperature_converter():
    # Ask for user input
    temperature = float(input("Enter temperature value: "))
    # Ask the user to select conversion type, either Fahrenheit ('F') or Celsius ('C')
    converter_type = input("Convert to (F)ahrenheit or (C)elsius? ").strip().upper()

    # If the user selects 'F', convert Celsius to Fahrenheit
    if converter_type == 'F':
        # Formula for converting Celsius to Fahrenheit
        converted_temp = (temperature * 9/5) + 32
        # Print the converted temperature in Fahrenheit
        print(f"{temperature}°C is {converted_temp:.2f}°F.")
    # If the user selects 'C', convert Fahrenheit to Celsius
    elif converter_type == 'C':
        # Formula for converting Fahrenheit to Celsius
        converted_temp = (temperature - 32) * 5/9
        # Print the converted temperature in Celsius
        print(f"{temperature}°F is {converted_temp:.2f}°C.")
    # If the input is neither 'F' nor 'C', print an error message
    else:
        print("Invalid conversion type. Please enter 'F' or 'C'.")

# Run the converter
temperature_converter()
