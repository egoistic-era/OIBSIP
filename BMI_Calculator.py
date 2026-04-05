def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Healthy"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("=== BMI Calculator ===")

    try:
        user_name = input("Enter your name: ")
        weight = float(input("Enter weight (kg): "))
        height = float(input("Enter height (meters): "))

        if weight <= 0 or height <= 0:
            print("Invalid input! Values must be positive.")
            return

        bmi_value = calculate_bmi(weight, height)
        category = get_category(bmi_value)

        print("\n--- Result ---")
        print(f"Name: {user_name}")
        print(f"BMI: {round(bmi_value, 2)}")
        print(f"Category: {category}")

    except ValueError:
        print("Please enter valid numeric values!")

# Run program
main()
