def ohms_law_calculator():
    # Ask user what they want to calculate
    calc_type = input("Calculate (V)oltage, (I)current, or (R)esistance? ").strip().upper()

    if calc_type == 'V':
        current = float(input("Enter current (I) in amperes: "))
        resistance = float(input("Enter resistance (R) in ohms: "))
        voltage = current * resistance
        print(f"Voltage (V) = {voltage:.2f} volts.")

    elif calc_type == 'I':
        voltage = float(input("Enter voltage (V) in volts: "))
        resistance = float(input("Enter resistance (R) in ohms: "))
        if resistance != 0:
            current = voltage / resistance
            print(f"Current (I) = {current:.2f} amperes.")
        else:
            print("Error: Resistance cannot be zero.")

    elif calc_type == 'R':
        voltage = float(input("Enter voltage (V) in volts: "))
        current = float(input("Enter current (I) in amperes: "))
        if current != 0:
            resistance = voltage / current
            print(f"Resistance (R) = {resistance:.2f} ohms.")
        else:
            print("Error: Current cannot be zero.")

    else:
        print("Invalid input. Please enter 'V', 'I', or 'R'.")


# Run the calculator
ohms_law_calculator()