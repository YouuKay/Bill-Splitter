# Initialize running total to track accumulated bill amount
running_total = 0

# Get user input for number of people sharing the bill (converted to integer)
num_of_friends = int(input("Enter the number of friends: "))

# Get user input for individual course expenses (converted to float for decimal values)
appetizers = float(input("Enter appetizers cost: "))
main_courses = float(input("Enter main courses cost: "))
desserts = float(input("Enter desserts cost: "))
drinks = float(input("Enter drinks cost: "))

# Get user input for the tip percentage (e.g., enter 25 for a 25% tip)
tip_percentage = float(input("Enter tip percentage (e.g., 25 for 25%): "))

# Calculate the base cost of food and drinks
running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

# Calculate the tip amount based on the user-specified percentage
tip = running_total * (tip_percentage / 100.0)
print('Tip amount:', tip)

# Add the tip to the running total
running_total += tip
print('Total with tip:', running_total)

# Split the total bill evenly among friends
final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)
