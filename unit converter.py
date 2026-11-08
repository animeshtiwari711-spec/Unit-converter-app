def unit_conversion():
    print("Welcome to the unit converter:")
    print("Conversions are as follows:")
    print("1.Length")
    print("2.Weight")
    print("3.Temperature")
    print("4.Exit")

    user_input = int(input("Enter your choice:"))

    if user_input == 1:
        print("Length conversions are as follows:")
        length_input = int(input("Enter 1 for meter to kilometer, 2 for kilometer to meter, 3 for meter to centimeter:"))
        if length_input == 1:
            print("1.Meter to kilometer:")
            meter = float(input("Enter the value in meter:"))
            kilometer = meter/1000
            print("The value in kilometer is:",kilometer)
        elif length_input == 2:
            print("2.Kilometer to meter:")
            kilometer = float(input("Enter the value in kilometer:"))
            meter = kilometer*1000
            print("The value in meter is:",meter)
        elif length_input == 3:
             print("3.Meter to centimeter:")
             meter = float(input("Enter the value in meter:"))
             centimeter = meter*100
             print("The value in centimeter is:",centimeter)
    elif user_input == 2:
        print("Weight conversions are as follows:")
        weight_input = int(input("Enter 1 for kilogram to gram and 2 for gram to kilogram:"))
        if weight_input == 1:
         print("Kilogram to gram:")
         kilogram = float(input("Enter the value in kilogram:"))
         gram = kilogram*1000
         print("The value in gram is:",gram)
        elif weight_input == 2:
         print("Gram to kilogram:")
         gram = float(input("Enter the value in gram:"))
         kilogram = gram/1000
         print("The value in kilogram is:",kilogram)
    elif user_input == 3:
        print("Temperature conversions are as follows:")
        temp_input = int(input("Enter 1 for Celsius to Fahrenheit and 2 for Fahrenheit to Celsius:"))                       
        if temp_input == 1:
          print("Celsius to Fahrenheit:")
          celsius = float(input("Enter the value in celsius:"))
          fahrenheit = (celsius*9/5)+32
          print("The value in fahrenheit is:",fahrenheit)
        elif temp_input == 2:
          print("Fahrenheit to Celsius:")
          fahrenheit = float(input("Enter the value in fahrenheit:"))
          celsius = (fahrenheit-32)*5/9
          print("The value in celsius is:",celsius)
    elif user_input == 4:
        print("Thanks for using the unit converter!")
    else:
        print("Invalid input")

unit_conversion()
