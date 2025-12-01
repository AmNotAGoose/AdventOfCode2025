from utils import get_test_data

data = get_test_data("test-data.txt").split("\n")

max_pos = 100
current_pos = 50
times_pointing_to_zero = 0

for line in data:
    direction = line[0]
    quantity = int(line[1:])

    if direction == "R":
        current_pos += quantity
    else:
        current_pos -= quantity

    new_pos = current_pos % max_pos

    if new_pos == 0:
        times_pointing_to_zero += 1

    current_pos = new_pos

print(times_pointing_to_zero)
