"""
Date: 18/12/21
Name : Callum Gracie
This program estimates an electricity bill
"""
# program instruction
print("Electricity bill estimator")
# gather user inputs
price_per_kWh = int(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
billing_period_length = int(input("Number of days in billing period: "))
# calculate estimated bill
estimated_bill = price_per_kWh * daily_use * billing_period_length / 100
# display bill
print(f"${estimated_bill}")

