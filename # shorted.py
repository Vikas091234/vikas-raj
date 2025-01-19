my_dict = {"b": 2, "a": 3, "c": 1}

# Sorting by keys
sorted_by_keys = dict(sorted(my_dict.items()))  # sorts by keys
# Sorting by values
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))  # sorts by values

print("Sorted by keys:", sorted_by_keys)
print("Sorted by values:", sorted_by_values)
