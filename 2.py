# 2018-12-06

# problem #2

# have memoization so that instead of time exponential in n we have linear in n

i_to_ith_fibonacci_number = {}

# we are 1-indexed s.t. f_1 == 1 and f_2 == 2
def getFibonacciNumber(i):
  if i == 1:
    return 1
  if i == 2:
    return 2
  else:
    if i in i_to_ith_fibonacci_number:
      return i_to_ith_fibonacci_number[i]
    else:
      result = getFibonacciNumber(i - 2) + getFibonacciNumber(i - 1)
      if i not in i_to_ith_fibonacci_number:
        i_to_ith_fibonacci_number[i] = result
      return result

# target_num_terms = 10
# result = getFibonacciNumber(40)
# print result

candidate_values = []
curr_i = 1
curr_value = None

while True:
  curr_value = getFibonacciNumber(curr_i)
  if curr_value < (4 * 10 ** 6):
    candidate_values.append(curr_value)
  else:
    break
  curr_i += 1

# print candidate_values
even_candidate_values = [x for x in candidate_values if x % 2 == 0]
# print even_candidate_values
result = sum(even_candidate_values)
print result


