some_list = ["a", "b", "c", "b", "m", "n", "n"]

repeated_values = []

clean_list = []

for value in some_list:
    if value not in clean_list:
        clean_list.append(value)
    else:
        repeated_values.append(value)

print(clean_list)

print(repeated_values)