def merge_dicts(dict1, dict2):
    third_dict = {}
    first_dict_keys = set(first_dict.keys())
    second_dict_keys = set(second_dict.keys())
    merged = first_dict_keys.union(second_dict_keys)
    for key in merged:
        third_dict[key] = [first_dict.get(key), second_dict.get(key)]
    return third_dict


first_dict = {'a': 1, 'b': 2, 'c': 3}
second_dict = {'c': 3, 'd': 4, 'e': 5}

print(merge_dicts(first_dict, second_dict))


# for k, v in first_dict.items():
#     third_dict[k] = [v, second_dict.get(k)]
#
# for k, v in second_dict.items():
#     third_dict[k] = [first_dict.get(k), v]
