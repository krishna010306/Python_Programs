sample_data = [{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, 
               {'VII': 'S005'}, {'V': 'S009'}, {'VIII': 'S007'}]

all_values = [val for dic in sample_data for val in dic.values()]

value_counts = {}
for val in all_values:
    if val in value_counts:
        value_counts[val] += 1
    else:
        value_counts[val] = 1

unique_values = {val for val in value_counts if value_counts[val] == 1}

print("Unique Values:", unique_values)