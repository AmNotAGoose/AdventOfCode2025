# d2p1: Gift Shop
from utils import get_test_data

data = get_test_data("data.txt").split(",")

invalid_ids = set()

for search_range in data:
    start, end = [int(x) for x in search_range.split("-")]

    for cur_id in range(start, end + 1):
        cur_id = str(cur_id)
        cur_id_len = len(cur_id)

        if cur_id_len % 2 != 0:
            continue

        select_len = int(cur_id_len / 2)

        if cur_id[:select_len] == cur_id[select_len:]:
            print(cur_id)
            invalid_ids.add(int(cur_id))

print(sum(invalid_ids))
