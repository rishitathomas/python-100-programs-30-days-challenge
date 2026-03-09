#/* Bill Splitter */

bill      = float(input("Enter the bill amount : "))
per       = int(input("Enter the number of people : "))
tip_perc  = int(input("Enter the tip percentage : "))


print("Each person pays around : ", (bill + (bill * tip_perc)/100)/per)