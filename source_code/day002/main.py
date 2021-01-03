#!/usr/bin/env python3
# 100 Days of Code : Day 1 Project
# Band Name Generator
# Adam Pawlowski (@hypermanganate)

print("Welcome ... to the tip calculator!\n")

total_bill = round(float(input("Enter the total amount of the check: ")),2)

number_of_diners = int(input("\nAnd how many are dining today? "))

print("\nNow comes the time to pass judgement.\nSelect a tip percentage, but choose wisely.\nRemember - these are trying times.\n")
print("For example:")
print("     For any reasonable meal with a party of four or more, enter '18' for an 18% gratuity.")
print("     Poor service may warrant something like 12% or 15%, so you would enter '12' or '15'")
print("     Good service maybe has earned 20%, so in that case enter '20'. Is there a limit to your generosity?")
tip_percentage = int(input("\nChoose: "))

total_gratuity = round(tip_percentage * total_bill / 100, 2)
individual_contribution = round(total_gratuity / number_of_diners, 2)

print(f"""\nIt has been decided. Your party will leave a {tip_percentage}% tip, resulting in a ${"{:.2f}".format(total_gratuity)} gratuity.""")
print(f"""Each of the {number_of_diners} members should contribute ${individual_contribution}, or more.""")





