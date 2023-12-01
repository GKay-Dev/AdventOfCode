# https://adventofcode.com/2023/day/1

import re

# Part 1

def calibration_values_sum(data):
    lines = data.split("\n")
    digits = [re.findall("\d", line) for line in lines]
    return sum([int(d[0]+d[-1]) for d in digits])

with open("input.txt") as f:
    data = f.read().strip()

print("1.", calibration_values_sum(data))

# Part 2

data = (data.replace("one", "on1e").replace("two", "tw2o").replace("three", "th3ree").replace("four", "fo4ur").replace("five", "fi5ve").replace("six", "si6x").replace("seven", "se7ven").replace("eight", "ei8ght").replace("nine", "ni9ne"))

print("2.", calibration_values_sum(data))