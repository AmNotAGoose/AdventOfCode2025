# d2p2: Gift Shop
from utils import get_test_data

data = get_test_data("data.txt").split(",")

invalid_ids = set()

for search_range in data:
    start, end = [int(x) for x in search_range.split("-")]

    for cur_id in range(start, end + 1):
        cur_id = str(cur_id)
        cur_id_len = len(cur_id)

        for possible_select_len in range(2, cur_id_len + 1):
            if cur_id_len % possible_select_len != 0:
                continue

            select_len = int(cur_id_len / possible_select_len)

            all_equal = True
            common_segment = cur_id[:select_len]
            prev_index = 0

            for cur_index in range(select_len, cur_id_len + 1, select_len):
                if common_segment != cur_id[prev_index:cur_index]:
                    all_equal = False
                    break
                prev_index = cur_index

            if all_equal:
                invalid_ids.add(int(cur_id))

print(sum(invalid_ids))
