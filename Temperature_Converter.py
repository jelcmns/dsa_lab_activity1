def temperature_converter():
    # Ask for user input
    temperature = float(input("Enter temperature value: "))
    converter_type = input("Convert to (F)ahrenheit or (C)elsius? ").strip().upper()

    if converter_type == 'F':
        converted_temp = (temperature * 9/5) + 32
        print(f"{temperature}°C is {converted_temp:.2f}°F.")
    elif converter_type == 'C':
        converted_temp = (temperature - 32) * 5/9
        print(f"{temperature}°F is {converted_temp:.2f}°C.")
    else:
        print("Invalid conversion type. Please enter 'F' or 'C'.")

# Run the converter
temperature_converter()