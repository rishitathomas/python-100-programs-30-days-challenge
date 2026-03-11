#/* Discount Calculator */

# Discount Rules
# <50 : 0%
# 50-99 : 5%
# 100-199 : 10%
# 200-499 : 15%
# >=500 : 20%
#-----------------------------------------------------------------------------------------


order_value = float(input(" Enter the purchase amount : "))

if order_value <= 50:
    print(f" Order not eligible for discount. Shop for ${50 - order_value} more to be eligible for a 5% discount.")

elif order_value > 50 and order_value <=99:
    print(f"Discount = 5%. Shop for ${100 - order_value} more to be eligible for a 10% discount.")
    print("Amount to pay :", order_value-(order_value * 0.05))

elif order_value > 99 and order_value <=199:
    print(f"Discount = 10%. Shop for ${200 - order_value} more to be eligible for a 15% discount.")
    print("Amount to pay :", order_value-(order_value * 0.1))

elif order_value > 199 and order_value <=499:
    print(f"Discount = 15%. Shop for ${500 - order_value} more to be eligible for a 20% discount.")
    print("Amount to pay :", order_value-(order_value * 0.15))

else:
    print("Discount : 20%")
    print("Amount to pay :", order_value-(order_value * 0.20))



