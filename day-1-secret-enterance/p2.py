# d1p2: Secret Entrance
from utils import get_test_data

data = get_test_data("data.txt").split("\n")

max_pos = 100
current_pos = 50
times_rotating_past_zero = 0

for line in data:
    direction = line[0]
    quantity = int(line[1:])

    quantity_full = quantity - quantity % max_pos
    quantity_partial = quantity % max_pos

    prev_pos = current_pos

    if direction == "R":
        current_pos += quantity_partial
    else:
        current_pos -= quantity_partial

    new_pos = current_pos % max_pos

    times_rotating_past_zero += abs(int(quantity_full / max_pos))

    if current_pos != new_pos and prev_pos != 0 or new_pos == 0:
        times_rotating_past_zero += 1

    print(quantity, prev_pos, current_pos, new_pos)

    current_pos = new_pos

print(times_rotating_past_zero)
