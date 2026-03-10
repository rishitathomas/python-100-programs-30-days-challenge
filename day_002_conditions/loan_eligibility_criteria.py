#/* Loan Eligibility Criteria */

age = int(input("Enter the age : "))
salary = float(input("Enter the monthly salary : "))
credit_score = int(input("Enter the credit score : "))


if age < 18:
    print("Sorry, not eligible for loan due to age criteria.")

elif age >= 18 and age <=50:
    if salary <= 2000:
        print("Sorry, loan not approved due to lower salary.")
    elif salary > 2000 and credit_score < 650:
        print("Not approved due to lower credit score.")
    else:
        print("Loan approved.")

elif age > 50 and age <= 70 and salary > 4000 and credit_score > 650:
    print("Eligible after review.")
else:
    print("Sorry, not eligible.")