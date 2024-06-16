data_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

distinct_values = {value for d in data_list for value in d.values()}

print("Unique Values:", distinct_values)
