with open('input.txt', 'r') as f:
    data = f.readlines()

number_sum = 0
for line in data:
    # extract the digits from the line
    digits = [d for d in line if d.isdigit()]
    number = int(digits[0]+digits[-1])
    number_sum += number

print(number_sum)