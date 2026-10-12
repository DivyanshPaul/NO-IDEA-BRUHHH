# Elevator Floor Tracker

# Write a program that simulates the movement of an elevator in a building with 10 floors.

# The elevator initially starts at floor 1.
# Ask the user how many floor requests need to be processed.
# For each request, ask the user to enter the desired floor.
# If the requested floor is outside the range 1–10, display "Invalid floor" and ignore that request.
# If the requested floor is above the elevator's current floor, display "Moving UP".
# If the requested floor is below the current floor, display "Moving DOWN".
# If the elevator is already on the requested floor, display "Already on requested floor".
# After processing a valid request, update the elevator's current floor.
# Keep track of the total number of floors travelled throughout all valid requests.
# At the end, display:
# The elevator's final floor.
# The total number of floors travelled.

current_floor = 1
total_distance = 0

number_of_requests = int(input("Enter number of requests: "))

for i in range(number_of_requests):
    requested_floor = int(input("Enter requested floor: "))

    if requested_floor < 1 or requested_floor > 10:
        print("Invalid floor")
        continue

    if requested_floor > current_floor:
        print("Moving UP")
    elif requested_floor < current_floor:
        print("Moving DOWN")
    else:
        print("Already on requested floor")

    total_distance += abs(requested_floor - current_floor)
    current_floor = requested_floor

print("Final floor:", current_floor)
print("Total floors travelled:", total_distance)