# Number Statistics

# The program takes a positive integer and processes every digit to determine:
# - Largest digit
# - Smallest digit
# - Digit sum
# - Number of even digits
# - Number of odd digits

# Number Statistics

# Taking input
number = input("Enter Your Number: ")

# Fix: Taking the first digit as largest and smallest
largestNumber = int(number[0])
smallestNumber = int(number[0])

digitSum = 0
evenDigits = 0
oddDigits = 0

# Fix: Checking all digits
for digit in number:

    # Fix: Converting digit into integer
    num = int(digit)

    # Finding largest digit
    if num > largestNumber:
        largestNumber = num

    # Finding smallest digit
    if num < smallestNumber:
        smallestNumber = num

    # Counting even and odd digits
    if num % 2 == 0:
        evenDigits = evenDigits + 1
    else:
        oddDigits = oddDigits + 1

    # Adding digits
    digitSum = digitSum + num

# Displaying results
print(f"Largest: {largestNumber}")
print(f"Smallest: {smallestNumber}")
print(f"Sum: {digitSum}")
print(f"Even Digits: {evenDigits}")
print(f"Odd Digits: {oddDigits}")