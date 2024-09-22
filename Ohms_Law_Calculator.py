def ohms_law_calculator():
    # Ask user what they want to calculate: Voltage, Current, or Resistance
    calc_type = input("Calculate (V)oltage, (I)current, or (R)esistance? ").strip().upper()

    # If user selects 'V' (Voltage)
    if calc_type == 'V':
        # Ask for current in amperes and resistance in ohms
        current = float(input("Enter current (I) in amperes: "))
        resistance = float(input("Enter resistance (R) in ohms: "))
        # Calculate voltage using formula V = I * R
        voltage = current * resistance
        # Print the calculated voltage
        print(f"Voltage (V) = {voltage:.2f} volts.")

    # If user selects 'I' (Current)
    elif calc_type == 'I':
        # Ask for voltage in volts and resistance in ohms
        voltage = float(input("Enter voltage (V) in volts: "))
        resistance = float(input("Enter resistance (R) in ohms: "))
        # Check if resistance is non-zero to avoid division by zero
        if resistance != 0:
            # Calculate current using formula I = V / R
            current = voltage / resistance
            # Print the calculated current
            print(f"Current (I) = {current:.2f} amperes.")
        else:
            # Print error message if resistance is zero
            print("Error: Resistance cannot be zero.")

    # If user selects 'R' (Resistance)
    elif calc_type == 'R':
        # Ask for voltage in volts and current in amperes
        voltage = float(input("Enter voltage (V) in volts: "))
        current = float(input("Enter current (I) in amperes: "))
        # Check if current is non-zero to avoid division by zero
        if current != 0:
            # Calculate resistance using formula R = V / I
            resistance = voltage / current
            print(f"Resistance (R) = {resistance:.2f} ohms.")
        else:
            # Print the calculated resistance
            print("Error: Current cannot be zero.")

    else:
        # Error message if current is zero
        print("Invalid input. Please enter 'V', 'I', or 'R'.")


# Run the calculator
ohms_law_calculator()