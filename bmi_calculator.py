def calculate_bmi():
    print("=== BMI Calculator ===")
    
    while True:
        try:
            weight = float(input("Enter your weight (kg): "))
            height = float(input("Enter your height (m): "))
            
            if weight <= 0 or height <= 0:
                print("Error: Weight and height must be positive numbers. Try again.\n")
                continue
            
            break
        except ValueError:
            print("Error: Please enter valid numbers only.\n")
    
    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    print(f"\nYour BMI is: {bmi}")
    print(f"Category: {category}")

calculate_bmi()
