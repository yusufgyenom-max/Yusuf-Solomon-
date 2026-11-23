
def sum_list(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


def average(numbers):
    return sum_list(numbers) / len(numbers)


def median_mode(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    
    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        middle1 = sorted_numbers[n // 2 - 1]
        middle2 = sorted_numbers[n // 2]
        median = (middle1 + middle2) / 2


    frequency = {}

    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    highest_frequency = max(frequency.values())

    modes = [
        number for number, count in frequency.items()
        if count == highest_frequency
    ]

    if highest_frequency == 1:
        mode = "No mode"
    elif len(modes) == 1:
        mode = modes[0]
    else:
        mode = modes

    return median, mode



numbers = []

while True:
    user_input = input("Enter a number (or type 'done' to finish): ")

    if user_input.lower() == "done":
        break

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")



if len(numbers) > 0:
    print("\n--- RESULTS ---")
    print("Numbers:", numbers)
    print("Sum:", sum_list(numbers))
    print("Average:", average(numbers))

    median, mode = median_mode(numbers)

    print("Median:", median)
    print("Mode:", mode)
else:
    print("You did not enter any numbers.")
