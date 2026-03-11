#/* Loan Eligibility Checker */

# Loan Eligibility Criteria
#
# Age Range | Salary | Credit Score | Result
# ----------------------------------------------------------
# <18       | Any    | Any          | Not eligible due to age
# 18–50     | ≤2000  | Any          | Loan not approved (low salary)
# 18–50     | >2000  | <650         | Loan not approved (low credit score)
# 18–50     | >2000  | ≥650         | Loan approved
# 51–70     | >4000  | >650         | Eligible after review
# 51–70     | Others | Any          | Not eligible
#-----------------------------------------------------------------------------------------

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