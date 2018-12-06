# 2018-12-06

# problem #1

# max_value = 10
max_value = 1000
candidate_values = range(1, max_value)
next_candidate_values = [x for x in candidate_values if (x % 3 == 0) or (x % 5 == 0)]
result = sum(next_candidate_values)
print result


