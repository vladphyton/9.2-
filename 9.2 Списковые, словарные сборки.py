



first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
first_result = [len(i) for i in first_strings if len(i) >= 5]
print(first_result)

second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
second_result = [(x, y) for x in first_strings for y in second_strings]
print(second_result)

comb = first_strings + second_strings
third_result = {x : len(x) for x in comb }
print(third_result)