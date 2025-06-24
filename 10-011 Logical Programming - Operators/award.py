# Read the time (in minutes) for each event from the user
swimming_time = float(input("Enter swimming time (minutes): "))
cycling_time = float(input("Enter cycling time (minutes): "))
running_time = float(input("Enter running time (minutes): "))

# Calculate the total time taken for the triathlon
total_time = swimming_time + cycling_time + running_time

# Display the total time taken
print("Total time taken for the triathlon:", total_time, "minutes")

# Determine the award based on the total time taken
if total_time <= 100:
    award = "Provincial Colours"
elif total_time <= 105:
    award = "Provincial Half Colours"
elif total_time <= 110:
    award = "Provincial Scroll"
else:
    award = "No award"

# Display the award
print("Award:", award)
