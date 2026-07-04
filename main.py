# Function to calculate performance bonus
def calculate_bonus(base_salary, performance_rating):
    if performance_rating == 5:
        bonus_percentage = 0.20
    elif performance_rating >= 3:
        bonus_percentage = 0.10
    else:
        bonus_percentage = 0.0

    bonus_amount = base_salary * bonus_percentage
    return bonus_amount


# Function to calculate tax
def calculate_tax(gross_salary):
    if gross_salary > 7000:
        tax_percentage = 0.15
    elif 3000 <= gross_salary <= 7000:
        tax_percentage = 0.10
    else:
        tax_percentage = 0.0

    tax_amount = gross_salary * tax_percentage
    return tax_amount


# Main HR Application
def main_hr_app():
    print("=" * 40)
    print(" Corporate Talent & Payroll System ")
    print("=" * 40)

    # User Inputs
    employee_name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    base_salary = float(input("Enter Base Salary (EGP): "))
    performance_rating = int(input("Enter Performance Rating (1-5): "))

    # Input Validation
    if base_salary < 0:
        print("Error: Salary cannot be negative.")
        return

    if performance_rating < 1 or performance_rating > 5:
        print("Error: Performance rating must be between 1 and 5.")
        return

    # Calculations
    bonus = calculate_bonus(base_salary, performance_rating)
    gross_salary = base_salary + bonus
    tax = calculate_tax(gross_salary)
    net_salary = gross_salary - tax

    # Output
    print("\n" + "=" * 40)
    print(f"PAYROLL STATEMENT FOR: {employee_name}")
    print("=" * 40)
    print(f"Department        : {department}")
    print(f"Base Salary       : {base_salary:.2f} EGP")
    print(f"Performance Rating: {performance_rating}")
    print(f"Bonus             : {bonus:.2f} EGP")
    print(f"Gross Salary      : {gross_salary:.2f} EGP")
    print(f"Tax Deduction     : {tax:.2f} EGP")
    print("-" * 40)
    print(f"Net Salary        : {net_salary:.2f} EGP")
    print("=" * 40)


# Run 
main_hr_app()