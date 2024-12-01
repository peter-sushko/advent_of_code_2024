from aocd import get_data
from aocd import submit

year = 2024
day = 1

data = get_data(year=year, day=day)

pairs = [line.split() for line in data.strip().split("\n")]

left_values = sorted([int(pair[0]) for pair in pairs])
right_values = sorted([int(pair[1]) for pair in pairs])

# For part a:
# answer_a = 0 
# answer_a += sum([abs(left_values[i] - right_values[i]) for i in range(len(left_values))])
# submit(answer_a, part="b", day=day, year=year) # yay this worked!

# For part b:
answer_b = 0 
answer_b += sum([left_values[i] * right_values.count(left_values[i]) for i in range(len(left_values))])

submit(answer_b, part="b", day=day, year=year) # yay this worked!