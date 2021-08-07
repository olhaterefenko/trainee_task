import re
from decimal import Decimal
from pathlib import Path


pattern = '[+-]?[0-9]+\.[0-9]+'
path_to_file = Path("task_1.txt").resolve()
output = open(path_to_file, 'r')
context = output.read()
lines_list = context.split("\n")
sum_of_numbers = 0
for line in lines_list:
    if line.count("#") == 0 and len(line) != 0:
        if re.search(pattern, line):
            try:
                number = Decimal(line)
                sum_of_numbers += number
            except Exception:
                pass
print("sum of numbers is {}".format(sum_of_numbers))
