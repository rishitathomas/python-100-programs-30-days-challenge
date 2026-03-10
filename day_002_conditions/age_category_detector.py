#/* Age Category Detector */


age = int(input("Enter the age : "))

if age != 0:
    if age >= 1 and age <= 12:
            print("Child")
    elif age >= 13 and age <= 19:
        print("Teenager")
    elif age >= 20 and  age<= 59:
        print("Adult")
    elif age >= 60 :
        print("Elderly")
else:
    print("Infant")

    