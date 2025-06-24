"""Practical Task 3 model answers"""

# Get the participant's time for each section of the triathlon
swimming = int(input("Swimming time (in minutes): "))
cycling = int(input("Cycling time (in minutes): "))
running = int(input("Running time (in minutes): "))

# Calculate and display the participants total time
total_time = swimming + cycling + running
print(f"Total triathlon time: {total_time} minutes")

# Determine the award the participant will receive based on their total time
if total_time <= 100:
    print("You received Provincial Colours!")
elif total_time >= 101 and total_time <= 105:
    print("You received Provincial Half Colours!")
elif total_time >= 106 and total_time <= 110:
    print("You received Provincial Scroll!")
else:
    print("You did not qualify for an award.")
